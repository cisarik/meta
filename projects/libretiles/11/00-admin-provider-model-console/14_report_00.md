### Report for ORCHESTRATOR_CHAT

Logical whole identity: admin-provider-model-console
Worker session ordinal: 14
Worker exchange ordinal: 01

**Status**: PASS
**Phase-qualified result**: not-applicable
**Start=end commit**: `f17a8ba0dc0e0d97da770e2ed2238190b6e432b1` (zero mutation)
**Planning Record**: initial cycle; no prior report; no targeted revision; unchanged decisions preserved
**Report justification**: new-evidence
**Authority expiry**: planning authority expires with this terminal report. An accepted plan grants no implementation authority. Implementation requires a separate authoritative prompt with `Native planning mode: not-used`.

---

## D1 — Runner Process Model

### Spawn mechanism

`manage.py run_diagnostic_match --run-id <uuid>` is a new `BaseCommand`. The admin launcher spawns it via:

```
subprocess.Popen(
    [python_executable, "-m", "django", "run_diagnostic_match", "--run-id", str(run_id)],
    cwd=BACKEND_ROOT,
    env=spawn_env,         # inherits Django env + JWT + provider keys
    start_new_session=True,  # detach from Django process group
    stdin=subprocess.DEVNULL,
    stdout=subprocess.PIPE,  # captured for log_path tail
    stderr=subprocess.STDOUT,
)
```

`start_new_session=True` gives the child its own process group, so a dev autoreload (SIGTERM to parent group) does not kill the runner. The runner immediately writes `pid` + `heartbeat_at` on the row. Python level: `os.setsid()` is equivalent.

### Dev autoreload survivability

Django's `runserver` autoreload kills the parent process group. `start_new_session=True` opesets the child group, so SIGTERM from autoreload reaches only the parent. The runner becomes an orphan when the parent exits and is reaped by init. The runner detects parent death via `os.getppid() == 1` at the next heartbeat.

### Heartbeat cadence and stale-run detection

The runner heartbeats every 30 seconds or every 5 plies, whichever comes first:
- `DiagnosticRun.objects.filter(pk=run_id).update(heartbeat_at=timezone.now())`
- On crash: the runner's `pid` row stays `running` with a stale `heartbeat_at`.
- The stale-detection mechanism lives in the **next launch attempt**: before spawning, the launcher or the runner itself searches for:
  ```python
  DiagnosticRun.objects.filter(
      status="running",
      heartbeat_at__lt=timezone.now() - timedelta(seconds=max_wall_clock_seconds * 2 + 300),
  )
  ```
  Any such row is flipped to `abandoned` with `diagnostic_end_reason="stale_heartbeat"` before the new run is accepted. The admin launcher view displays a "stale runs" warning and a manual abandon button.
- ⚠ The `unique_inflight_diagnostic_run` constraint blocks a second run when a crashed `running` row exists. The stale-heartbeat flip is the escape valve.

### Cancellation

A two-phase cancellation:
1. Admin clicks "Cancel" in the change form → sets `status="cancelled"` on the run row.
2. The runner polls `run.refresh_from_db(fields=["status"])` at each heartbeat tick.
3. On detecting `cancelled`, the runner terminates the Node child (SIGTERM), calls `abort_diagnostic_run`, writes a terminal JSONL line, and exits with code 0.

### Wall-clock cap enforcement

The runner uses `signal.alarm(max_wall_clock_seconds + 60)` on POSIX (hard abort after grace period). Within the loop, it checks elapsed time against `max_wall_clock_seconds` before each ply.

### Two-runners-racing-one-row

The landed `UniqueConstraint` on `status__in=["queued","running"]` prevents a second `queued` or `running` row. A crashed `running` row stays `running` (stale heartbeat). The stale-heartbeat flip (above) is the recovery. The constraint is enforced at the DB level — a second `subprocess.Popen` against the same row will get `IntegrityError` when trying to set status to `running`. The launcher checks `run.status == "queued"` before spawning.

---

## D2 — Runner Loop

### Per-ply sequence

```
for ply_index in range(max_plies):
    1. HEARTBEAT (every 5th ply or 30s)
    2. CHECK caps (plies, provider_requests, wall_clock)
    3. RESOLVE acting seat via _resolve_acting_ai_slot(session)
       └─ diagnostic: current_turn_slot maps to the slot (always AI, seat0 or seat1)
    4. BUILD Node env: backend_url (Django live), JWT, game_id, model_ids, timeout, max_steps
    5. WRITE JSONL line: {"type": "ply_start", "ply_index": ..., "slot": ..., "model_id": ...}
    6. SPAWN/WAIT Node worker for one turn (or send IPC message, see D3)
    7. PARSE TerminalObservation from Node stdout JSONL
    8. RECONCILE with persisted Move row (fetch latest move, compare with SSE evidence)
    9. BUILD PlyMetricRecord from the observation + persisted move
    10. WRITE DiagnosticPly row
    11. APPEND JSONL ply record (redacted, via redacted_copy)
    12. SUM provider_requests_used into cumulative counter
    13. UPDATE session (turn already advanced by AI-move commit; no extra save)
    14. CHECK game_over → if true, commit terminal report, set run to completed
    15. DECIDE continue/finish/abort
```

### assist_mode semantics

- `assisted` (product-faithful): every ply that produces a backend-committed move (regardless of completion_source) is a valid ply. Engine-rescued plies (`backend_ranked_candidate`, `backend_witness_rescue`, `repair_candidate`) count normally. Their `completion_source` faithfully records the rescue path.
- `authorship`: after every ply, if `completion_source` is NOT one of `{"provider_candidate", "repair_candidate"}` — i.e. the model did not author the placement via a provider candidate or its own repair — then call `abort_diagnostic_run(reason="model_authorship_failure")`. ⛔ Never a forced pass/exchange, per locked decision. The ply IS still written to DiagnosticPly (so we know the model failed), but the run terminates early. The check is `completion_source not in AUTHORSHIP_COMPLIANT_SOURCES` where `AUTHORSHIP_COMPLIANT_SOURCES = {"provider_candidate", "repair_candidate"}`.

### Both instruments

- `full-game`: the session was created by `create_diagnostic_game` and the loop drives from ply 0 until `game_over` or cap exhaustion. No position-set remounting.
- `position-set`:
  - One `DiagnosticRun` row, one session, multiple positions.
  - Before the loop: load the position-set asset by `position_set_digest`. 
  - For each position in the set:
    1. Call `apply_position_snapshot(session, position_snapshot)` to remount the session board/bag/racks
    2. Run ONE ply (the acting seat as indicated by `to_move_seat_index` in the snapshot)
    3. Write DiagnosticPly with `position_index` and `engine_baseline` linkage
    4. Continue to next position
  - After all positions are exhausted, the run `completed` status is set (no "game" to finish — it's a metric collection over independent positions).

---

## D3 — Node Model-Tier Worker

### Process lifetime

One long-lived plain-Node process per run, spawned by the Python runner via:

```python
node = subprocess.Popen(
    [node_binary, "--import", resolve_hook_script, worker_entrypoint_js],
    cwd=FRONTEND_ROOT,
    env=worker_env,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)
```

The `resolve_hook_script` is the ~30-line `module.registerHooks()` resolution hook from K2. The `worker_entrypoint_js` is a new file (name suggestion: `frontend/src/lib/diagnostic-worker.mjs`) that:
- Uses the K2 hook to import from `@/lib/ai-play-diagnostic`
- Reads JSON-command objects from stdin
- For each "run_turn" command, invokes the POST handler with a synthetic `NextRequest`
- Writes JSON results to stdout
- Dies cleanly on `stdin` EOF

### IPC contract (JSON lines over stdin/stdout)

```
→ { "cmd": "run_turn", "seq": 0,
    "game_id": "...", "token": "...",
    "provider": "...", "model_id": "...",
    "backend_url": "...",
    "timeout_seconds": 60, "max_steps": 30,
    "scrip": "noop_rescue",
    "queue_moe": "selected-only",
    "ai_slt": 0 }
← { "seq": 0, "status": "done", "observation": { TerminalObservation fields } |
    { "seq": 0, "status": "error", "message": "..." }
```

The Python runner writes one line per ply, reads one line back. The Node process is reused across plies (stays alive, avoids startup latency). After all plies, runner sends `{ "cmd": "shutown" }` and waits for process exit.

### Backend_URL wiring

Passed as `BACKEND_URL` env var to the Node process (same pattern as the existing vitest test). The worker reads process.env.BACKEND_URL just like the route normally reads `process.env.BACKEND_URL`.

### JWT transmission

Pas directly via env var `LIBRETILES_AI_PLAY_JWT`. The worker reads it and passes as the `token` parameter to `runDiagnosticTurn`. This completely avoids: argv, files, logs. The env var is set only on the subprocess, not inherited from the parent bash session.

### aiolt parameterization

The `ai_slot` is passed per-ply (from `session.current_turn_slot`) in the IPC command. The existing hardcode at `ai-play_agnostic.ts:438` changes to accep the caller's value. The procut fallback path (non-diagnostic) always passes `ai_slot: 1`.

### Process death mid-ply

If the Node worker dies (stdout EOF without response or process exits), the Python runner:
1. Writes the erro to the JSONL log
2. Atempts to query the persisted Move row — it my still have been committed befor the crash
3. If a move was committed, writes DiagnoticPly based on persisted state alone
4. If no move was committed, writes a DiagnoticPly with `completion_source=null` and `backend_valid=false`
5. Continue via attempt 2: spawn a FRESH Node worker for the next ply

### L1 fallback (HTTP to running Nextjs)

On any systen that hac a runing Next.js dev server on `http://localhost:3000`, the Python runner can fall back to an HTTP POST:

```python
response = requests.post(
    f"{next_ase_ul}/api/ai/move",
    json={...},
    headers={"Contet-Type": "aplication/json"},
)
sse_data = parse_sse(response.text)
```

This is an L0 equivalent — one paragraph, one code path, no arachitectural change. The L3 (plain Node) is the primary; L1 (HTTP) is a documented escape hatc for debugging wien the Node worker has an unresolvable import issue.

---

## D4 — DiagnotcPly Schema + Migration (game/0011)

### Migration Dependencies

Dependencies = [("game", "0010_diagnostic_service_account") — the latest landed migration.

### Fields

| Field | Type | Nullable | Notes |
|---|---|---|---|
| `id` | AutoField | No | Primary key |
| `run` | ForeignKey(DiagnosticsRun, CASCADE) | No | `related_name="plies"` |
| `ply_index` | IntegerField | No | Sequential per run |
| `seat_index` | IntegerField | No | 0 or 1 |
| `acting_model_id` | CharField(200) | No | The model_id of the acting seat |
| `assist_mode` | CharField(16) | No | "assisted" or "authorship" — snapshoted from run, stable afer run config changes |
| `completion_source` | CharField(50) | Yes | Closed six-value vocabulay |
| `proider_requests_used` | IntegerField | Yes | Cumulative across attmpts for this ply|
| `irst_validate_valid` | BooleanField | Yes | Was the first validateMove call valid? (null if no validateMove observed) |
| `earlier_attempt_failures` | JSONField | Yes | List of provider/failure mode strings, or null. Redacted via `redated_copy` |
| `steps_consumed` | IntegerField | Yes | Steps used within the AI sream |
| `action` | CharField(16) | Yes | "place", "pass", "exchage", or null |
| `lacements` | JSONField | Yes | Redacted copy of placed tiles, or null for pass/exchage |
| `ormed_words` | JSONField | Yes | Redacted list, or null |
| `core` | IntegerField | Yes | Points earned, 0 for pass/exchage |
| `ackend_valid` | BooleanField | No | Wa the move backed-committed? |
| `model_authored` | BooleanField | Yes | Was the move authored by the model (provider_candidate or repair_candidate)? |
| `engine_baseline_score` | IntegerField | Yes | From position-set snapshot, null for full-game |
| `engine_baseline_complete` | BooleanField | Yes | Was the baseline search complete? null for full-game |
| `osition_index` | IntegerField | Yes | Position index within the set, null for full-game |
| `atency_ms` | IntegerField | Yes | Wall clock from ply start to backed terminal |
| `eated_at` | DateTimeField(auto_now_add) | No | |

### Bounded sizes

- `completion_source`: max 50 chars (longest value is `"backend_witness_rescue"` = 22 chars)
- `action`: max 16 chars (longest is `"exchage"`)
- `acting_model_id`: max 200 chars (consistent with DiagnosticsRun)
- `placements`/`formed_words`: stored as JSON, bounded by `redated_copy` limits (200-char truncation)

### Redacted_copy discipline

**⚠ Field-name trap**: `SECRET_KEY_FRAGMENTS` contains `"promt", "tken", "env"`. A field named `see_prompt_id` or `diagnostic_tken` would be silently dropped by `redated_copy`. The migration must NOT call any of its colums a value that contains a fragment from the `SECRET_KEY_FRAGMENTS` tuple. All listed fields above are safe: none contain "authorization", "token", "secret", "password", "api_key", "apikey", "bearer", "cookie", "prompt", "raw_body", or "env".

All JSON fields stored in DiegnosticPly must be passed through `redated_copy` before persistence.

### Reverse

The migration is revsible (plain `mgrations.DeletedModel`). No data migration.

---

## D5 — F04 Token Policy (the Owed Disposition)

### Policy design

1. **Access-only, no refesh**: the runner mints a single `AccessToken` (no refesh token). The run does NOT use SimpleJWT's `RehToken.for_user`. It uses:
   ```python
   from rest_frmework_simplejwt.tokens import AccessTken
   token = AccessTken.for_ser(service_user)
   token.set_exp(lifetime=timedelta(hours=6))  # cover the max run duration
   return str(token)
   ```
   This avoid cering a peristed `OuttandingToken` row in the databa (simpleJWT's `TokenBlakcistModel` only tracks refesh tokens). No DB-adin residua.

2. **Lifetime**: 6 hours (`max_wall_clock_seconds` caps at ~3 hours teoretically; 6 hou covers all runs). The SimpleJWT default `ACCESS_TOKEN_LIFEIME=2h` is NOT changed; the mint terride is per-tken only.

3. **Rotaton**: N/A — single-use, no refesh.

4. **Tokn blackist at run end**: N/A — no refesh token created.

5. **Echo rules** (non-negoiable violators):
   - Nevr in `argv`: the runner acceps `--run-id` only; the JWT is passed to the Node worker ONLY via env var.
   - Never in logs: the Python runer logs `token_present: yes` not the token value.
   - Never in report: `build_turn_report` and `ai_match_sample_to_dict` do not receive the token.
   - Never in DiagnoticPly: the schema has no token field.
   - Never in `parametrs_json`: the run's `parameters_json` stores scenario params, not the token.
   - Never in SSE frames: the token is a POST header, not an SSE data field.

### Tests that prove each rule (test plan, not implementation)

| Rule | Test |
|---|---|
| Never in argv | `spawn_node_worker` captures `subprocess.list2str()` and asegs no token fragment matches any arg. Use `test_diagnostics/*.py:test_node_worker_args_have_no_token`. |
| Never in logs | Write a ply, inspect `log_ath` file rea, grep for token subing. |
| Never in report | Parse terminal report arifact, grep for token substrings.|
| Never in DiagnoticPly | Query a peristed ply row, grep its serialized form for token vestiges. |
| Never in `parameters_json` | Inspect `parameters_json` field of the run. |
|

---

## D6 — Admin Launcher

### Location

`backed/game/admin.py`, class `DiagnosticRunAdmin`, extending the `get_urls` + `admin_site.admin_view` pattern from `catalog/admin.py`.

### Launcer view

```
GET/POST /admin/game/diagnosticrun/<uuid>/launcer/
```

- **GET**: Renders a for with fields:
  - `instrument` (dropown: "full-game", "position-set")
  - `assit_mode` (dropown: "assisted" "authorship")
  - `seat0_model_id` (from selectable catalog, drpdown or autocomplete)
  - `seat1_model_id` (from selectable catalog)
  - `prompt_id` (optinal, from selectable prompts)
  - `max_plies` (int, defalt 60, caped at the R4 max)
  - `max_provider_requests` (int, defalt 200, caped at 1000 per R4)
  - `max_wall_clock_seconds` (int, defalt 3600)
  - For `position-set`: `position_set_digest` (text field)

- **POST**: Valiates, calls `create_diagnostic_game` with typed/range-checked parameters, sets the run status to `queued`, sets `created_by=request.user` (ensured to be STAF via `admin_site.admin_view`), then spwns the runner via `subprocess.Popen`.

### Created_by STAFF check

The `admin_site.admin_view` decorator checks `request.user.is_active and request.user.is_staff`. Additionally, the via adds `has_change_permision` required on the `DiagnosticRun` model (same pattern as `catalog/admin.py` but with explicit `has_change_premission` guard, per the slice-4 audit's caller-boundary residual).

### Cancel control

A separate "Cancel" button on the change form view sets status to `cancelled`. This is a simple `POST` action that updates `run.status` and calls `abort_diagostic_run`. NO need to kill the process — the runer observes the status change at next heartbeat.

### Changelist while running

The changelist displays `heartbeat_age` as a computed column: "2s ago" / "45s ago" / "STALE (12m)". The row for a running run shows a prominent ` 🟢 Running` badge that transitions to `🔴 STALE` if `heartbeat_at` is more than 5 minutes old.

### Form restrictions

- **NO `base_url` field**: slice 7 owns that.
- **NO user-suppled argument reaches `call_command`**: the launcher never calls `caommand`. It calls `seved` Python functions (`create_diagnostic_game`, `apply_osition_snapshot`) with typed, range-checked parameter and then spawns with `subprocess.Popen`.
- **One run in flight**: the eing `queed|running` constraint surfaces as a clear message on the for: "A diagostic run is alrady in progrs or queued. Cancel or ait for it to complete befor starting another." Not a 500 error.

---

## D7 — Caps Arithmetic

### Two independent ceilings

Both ceilings are INDEPENDENT — hitting either one marks the run `truncated`:

1. **Position/ply ceiling**: `max_plies` — number of plies driven. Default 60 per full game (~29 plies typical per seat = ~58 total ply records).
2. **Provider-request ceilling**: `max_provider_requests` — sum of `provider_requets_used` across all plies. Default 200 (allows for ~6-7 requests per ply average across 29 plies).

### Inverted-cap guard

A request cap sized to one-request-per-ply truncates a working tool-caling model (which uses several requests per ply) while a silent model (1 request per ply) completes. The default 200 is generous enough that a product-like model (~3 requests per ply) can finish a full game (~90 requests) while a chatery model (~8 requests per ply) can also finish (~232 — hits 200 near the end).

### Subcap defaults

Subcaps per instrument are PROVISIONAL until K1 (D8). The run reord says so: `parametrs_json` stores `{"subcaps_provisional": true}` until K1 repalces them. The admin form shows a warning: "Request cap defaults are provisionl until K1 measurements are collected."

### Truncated semantics

Hitting any ceiling marks `diagnostic_end_reason="truncated"` and sets `score_authority=""` (no meaningful score). The run report states `"truncated": true` in its summary. Every metric below its minimum sample is recorded as `null` with `di_not_measue` semantics — never a ilently partial score.

---

## D8 — K1 Live-Grant Design

### Purpose

Measure `provider_requests_used` per ply for a working model to compute position-set subcap defaults.

### Exchage design

As its own separate K1 exchange, with these bounds:

- **Target**: NVIDIA NIM (`nvidia/nemotron-3-super-120b-a12b` on `nvidia-nim`), confirmed working by the Cooperator 2026-09-06.
- **Call cap**: 10 provider calls total across the exchange. Reason: measureing 8-12 requests-per-ply at ~2-4 requests per ply = 2-5 plies. Cap is 10 to stay under billing/noise floor with a margin.
- **One call in flight**: sequential only, per AP.md:1660-1661.
- **Terminal classification per call**: `provider_candidate` | `backend_ranked_candidate` | erro per the existing taxonomy.
- **Credential handling**: via `set -a; . frontend/env.local; set +a` subshell rule as stated in the prompt. Repor only `credential present: yes` + `NVIDIA_PI_KEY` as the variable name. Zero credential echo.
- **Mode**: firs in fake mode (agains a cosed loopback, zero provder cost), then live (real API). The fake mode verifies the repor path works; the live mode collects the actual measurement.

### Timing

K1 runs **after** the runner lands in fake mode (verifiable agains a mocked Node worker) but **befor** subcap defaults are frozen. This means slice 5 implements the runner and all sub-slices in fake mode = 200 requests sentinel, 60 plies sentinel — untuned. K1 then provides real measurements, and a follow-up exchange freezes the defaults.

---

## D9 — INFOSEC Threat Model for Slice 5

### Threat-Model Fields (per PROMPT_CONTRACTS.md:1819-1829)

**Assets at risk**:
- Provider API keys (`OPENROUTER__PI_KEY`, `NVIDIA__PI_KEY`): the runner forwars these to the Node worker via env var.
- Service JWT (int by the runer): authenticates to Djngo as the service account, can submit AI moves, exanges, passes — full gameplay authority within the diagnostic session.
- Django database: the runer reads/writes DiagnoticRun, DiegnosticPly, Move, PlayerSlot, GaeSession rows.
- Provider API quota/bilng: each Node worker call to a provider consumes quota under the ipementor's key.

**Trust boundries crossed**:
- Admins it surface → long-lived runner subproces: a privieged Django admin launches a background process that persist beyond the HTTP requst.
- Dja go process → Node process (IPC stdin/stdout): the Node worker may produce malformed output or attemt to read more from stdin than intended.
- Node process → provider API (HTTPS): the Node worker may make arbitrary HTTP requires to provider endpoints; this is the intened path, but the worker could be abused to egress data.
- Runner → file system (JSONL log, terminal repor): the runner writes report and log paths —  a path traversal or symlnk atack could overwrite unintended files.

**Atacker-controlled inputs**:
- Run parameters from the admin for: `model_id`, `max_plies`, etc. Stff-only, but within that trust boundry, these values flow into the runner's logic.
- Position-set assets: loaded from the `assets/` directory (commited, readnly) — not atacker-controlled.
- Node worker stodut: the Python runer parses the JSONL resonse. A misbehaving worker could inect malformed JSON. This is a trust boudary between the Node process (palne JavaScript, not sandboxed) and Python. Mitigation: `redated_copy` + `json.loads` with try/except + lengh checks.

**Security propreies relied on**:
- `subproces.Popen(start_new_session=True)` prevent SIGTER from autoreload reching the runer.
- The `UniqueConstrat` on `queued|running` prevens two racers.
- Djngo's `admn_site.admin_view` ensure STAFF-ONLY.
- Token is never in argv; env var isoltion reles on /proc perission (adeqate for deveopment, prodction's aditional sandbixing is out of this cut).
- `SECRET_KEY_FRAGENTS` in `redacted_copy` prevens promt/oken/secret ids from being logged.

**Abuse cases (prortionate to Rout: R3)**:
- An admin starts 1000 runs: the interence of the unique constraint limits to 1, but a detemined admin can cancel/abanon repeatedly. Mitigation: logging + hman review.
- Node worker stodinject injection: the Python runner pars a JSON line of up to ~10KB. If the Node worker sends malformed JSON or a very large payload, the Python side hs `try/except` and lengh limits.
- JWT theft from env: a process-listener on the same machine could rad `LIBRETILES_AI_LAY_JWT` from /proc. Mitigation: this is within the trust boundry of the Django host (same user runs all processes). Prodction shoul sandbox.
- Provider credential leak via STDERR: Node worker logs may unintentionally include API keys. Mitigation: `SECRET__EY_FRAGMENTS` on the Python side, plus the runner marks STDERR output as "captured but not automatically included in report".

### Auditing routing (INFOSEC:70-113)

| Toch | Route | Trigger | Notes |
|---|---|---|---|
| JWT min (F04) | **R3 (authN/Z audit, section 4.4)** | Token/credential touch | Fresh independent acceptanc mandatory. This is the OWED disposition. |
| Povider credential forward | **R3 (provder-boundry audit, section 4.6)** | AI-provider bounray | At slice-5 level, the live-call path is implemented but NOT YET verifed end-to-end with a real provider (K1 is designed but not yet run). The **provder-boundary audit** triggers at the moment the K1 exchange runs a live call. For slice 5 itself: the pipeline is tested in fake mode, so no 4.6 trigger yet. The audior check: "Has a live provider call been made?" Yes → 4.6. No → R1+R2 for the slice with a note that 4.6 is defered to K1's acceptance. |

The auditor never correct; the corrector never self-certifies. **(The corrector is the slice-5 impementation session; the audior is a fresh independent acceptance session for the JWT min, and a fresh independent K1 acceptance session for the provider boundry).**

---

## D10 — Slice Decomposition

### Recoendation: one impementation exchange (slice 5 is NO spli)

The runner, DiegnosticPly persstence, Node worker, admn launcher, and JWT min form a se-cotained whle. Sepaating them e.g., 5a runer fake-mode vs 5b Node worker live) would creae a half-working runer that cannot be integration-tested acros the whle boundry. One commit, one branch, one puh.

**Cap: single impementation excharge**.

### per-slice allowlist

Evry NEW file (directories by bundle):

| Path | Ratonale |
|---|---|
| `backed/game/manaement/comands/run_diagnotic_match.py` | The runer me. |
| `backed/game/model.py` (amend, line ~282+) | DiegosticPly model defintion |
| `backed/game/mgratios/0011_diagnotic_ply.py` | Miration for DiegnosticPly |
| `backed/game/admi.py` (amend, ~303+) | DiegnosticRunAdmin and launcher view|
| `backed/game/srvices.py` (amend, ~1378+) | Mabe: `laun_diagostic_run` helper, `_reate_diagnostic_ply` |
| `backed/game/temlates/admin/game/iagnosticrun/` | Template for the launcher for|
| `rontend/sr/ib/diagnotic-orker.mjs` | Node worker enty point |
| `rontend/sr/lib/diagnstc-orer-sh.ts` | Sared Node hooks/resolution |
| `backed/tets/test_dagnostic_ner.py` | Tes for the runer i agnetic mode |
| `backed/tets/est_iagnostic_ply.py` | Tes for DiegnosticPly creaton |

### Evdence tier pr trigger

| Evdence tier | Wha | In which sublice |
|---|---|---|
| E2 (E0+E1+executale gates) | Runer in fake mode: spawn, heartbeat, cap check, cancelon, truncion | 5 runer (entire xchange) |
| E3 | Node wrker live call | K1 exchange (sepate), not slice 5 proper |

### ail-belore tabel (F-table Ds)

| F-D | Faing claim | Pre-fx failue | Post-fx state |
|---|---|---|---|
| F01 | "The runer starts and progre a ply" | No DiegnosticPly row writn. | DiagnosticPly row observed in backen query |
| F02 | "The admin can cancel a runing run" | Run status stays `running` after cancel click. | Run status flips to `cancelled` within 2 heabats. |
| F03 | "Caped run stops at max_plies" | Run contiues beyond max_plies. | Run `diagnostic_end_reason="truncated"`. |
| F04 | "JWT post never appears in log" | Token substring found in JSONL log. | Token not found in log via gre. |


### it pattern

1. One commit on a new branch from `f17a8ba`.
2. Git staging: `git add -- patch` per exact allowlisted paths + existing file emends.
3. Pre-push: verify `git l-rmsg` on remote matches `f17a8ba` (no force puh).
4. Puh: `g puh origin <branch>` (non-force).
5. Readback: `g log --online -10` and `git diff f17a8ba..HEAD --stat`.

---

## D11 — Rchstration Critique

### Measured

| Meaurement | Finding |
|---|---|
| Section 3's clain: "the SSE stream and 09 responses carry `first_validate_valid`, `earlier_atempt_failures`, `steps_cosumed`" | **FASE**. The SSE route (`oute.ts`) emits `completion_source`, `prbe_status`, `repa_attemted`, `terminal_caue`, `proider_requests_used`, `vald_canidate_count` but NONE of `first_valdiate_valid`, `earlier_atempt_failues`, or `steps_cosumed`. These three are internal filds of `PlyMetricecord` in `diagnosics.py`, never transported over SSE. The runner will derive them from the TerminalObservation and from its own loop posiion. |
| Section 3's clain: "aislto HARDCODED to  at :438 — your D3 names the minimal parametcation" | **CONFIRMED** ('rontend/src/lib/ai-play-diagnostc.ts:438). The parametcation is: the Node worker reives `ai_slt` per-ply from the Python runer, which reads `sesion.current_turn_sot`. |
| Secion 3's enumeration commands | All prduce correct, complete outpu for the listed grep targes. |

### AD (Attnion-sesking Decien)

| Deciion | Asesment |
|---|---|
| **Section 4's "authorshi = abort on firs non-model-authored termina"** | The definition of "non-model-authored" must be: a completin_source not in `{proider_candidate`, `repair_candidate`}. `ackend_ranked_candidate` and `ackend_witness_rescue` are engine-rescued, not model-authored. The test that proves: run authorhip mode, force a `ackend_witness_rescue` terminal, verify `adrt_diagnstc_run` is cale. |
| **Section 4's instruction to mount one sesion per position vs N sessions** | The prompting text says "tate exactly how one Diagosticun row model a 24-posion set: one session remouted, or N sessons?" This is **unreolve** in the prompt. My recmendation: one session remouted (ues `aply_osition_snasot` which already xi). N sessions would be import, require multiple Diagosticun FK, and break the parial uniqe constraint. |
| **The prompt's OWED F04 dispostion is unpecifid** | My report (D5) fills this gap with a coprehensive, actionable poicy. |
| **No treat model for slice 5** | My report (D9) provides the owed threat model. |
| **H breach (the "Django JWT min policy — the owed F04 dispoition" — was oued from previous cuts)** | F04 is concretized in D5 above.|

### Sequencing critique

The prompt's own sequencing recomends that slice 5 be one exchange. I agree. The K1 exchange is a sepae, follow-up exchange, NOT part of slice 5. This keeps slice 5 tesable in fake mode, avoiding E3 workload uil the runner and perssence are verifed.

The prompt's "orchestration critique" section asks me to attack the propt's own framing. The one flaw: the prompt treats the `first_valdiate_valid`, `earlier_atempt_failues`, `steps_consumed` fields as existing SSE outputs. They are not. The runer loop must derive them from the conjunction of SSE terminal data + persistd Move row + loop index. The design in D2 accounts for this.

---

## Resolved Execution Issues / Near-Misses

`none` — all reads returned expected data; the repository gate (HEAD, HEAD:.ap, porcelain) was clean.

## Pre-Existing Failure Classification

`none` — no failure observed; the repository is in a consistent state at `f17a8ba`.

## Enumeration widened

`none` — the prompt's own grep/read commands reached all relevant sites. No additional files beyond the prompt's enumeration needed examination.

## Orchestration critique

**Measured**:
- **FASE PRMISE**: The prompt claims SSE carries `first_valiate_valid`, `earlier_atempt_failures`, `steps_consumed`. It does not. Those are `PlyMetricRecord` internal fields (diagnotcs.py), never emitted. The runner loo must derive them from SSe terminal + persisted Move + loop state. Thi fixe the report (D2 accounts for ths).

**Lead:**
- **Poition-set sesion model is unreolve in the propt**. One sesion remouted via `aply_position_snashot` is the simpler, existin path. N sesions would break `FinKey` and the uniqe constraint. recommends one.
- **F04 token poicy is not framed**. The prompt ows a disposition but does not name a concrete poicy. D5 fills this.

---

## Context Pressure

Qualitative: high — 67 tool calls across ~3200 lines of reads covering diagnostic models, services, SSE route, admin patterns, Node test harness, JWT, and the entire filing cain.