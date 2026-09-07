You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An accepted plan grants you nothing; THIS prompt does.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 15
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: APMC-S5-RUNNER — the diagnostic runner: `manage.py run_diagnostic_match --run-id`, DiagnosticPly persistence (migration 0011), the plain-Node model-tier worker importing the existing move-route POST handler, the runner's access-only JWT mint (the owed F04 disposition), and the Django-admin launcher with cancel. FAKE MODE ONLY. Provider calls: ZERO.
Phase: implementation
Implementation authority: explicit
Exact baseline: f17a8ba0dc0e0d97da770e2ed2238190b6e432b1
Changed-path allowlist: exactly the paths in section 4
Implementation boundaries: positive and negative authority in sections 3-5
Independence required: no
Evidence posture: non-independent
Evidence tier: E3
Evidence tier basis: credential-adjacent surface (minted service JWT), a long-lived privileged subprocess an admin can start, and a durable migration. Combined implementation envelope allowed under E3 with gates; final acceptance is a separate fresh audit (slice 5-IA).
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named risks: (1) the minted JWT is a real credential — one echo into argv, a log, a report, a DiagnosticPly row, `parameters_json`, or an IPC JSON line is a finding, not a style issue; (2) the runner is a detached long-lived process — a wrong lifecycle leaves orphaned Node children or a permanently-blocked in-flight constraint; (3) the Node worker inherits an env you construct — a blanket `os.environ` copy leaks Django secrets into a JavaScript process.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1444-1462      Git and remote safety — every write needs the exact authority THIS prompt names
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   role and authority boundary
PROMPT_CONTRACTS.md:14-41   the report contract and the coordinate fields you echo back unchanged
AP.md:2452-2454      the CLOSED report-justification enum. Read it; do not recall it.
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it
   yourself. That sentence is what makes a reading shortcut fail closed.
```

## Mandatory reading — by symbol; re-measure every symbol before you use it

```text
/home/agile/Projects/libretiles/AGENTS.md            project brief; "Word validation" binds
/home/agile/Projects/libretiles/frontend/AGENTS.md   Next.js 16 — verify any Next behaviour in
                                                     frontend/node_modules/next/dist/docs/, never from memory
backend/game/models.py            GameSession.is_diagnostic, bag_rng_state, DiagnosticRun
                                  (partial unique unique_inflight_diagnostic_run).
                                  ⛔ DiagnosticRun is FROZEN — no field change. DiagnosticPly is NEW.
backend/game/services.py          _resolve_acting_ai_slot · ensure_diagnostic_service_user ·
                                  create_diagnostic_game · apply_position_snapshot ·
                                  abort_diagnostic_run · list_games_for_user
                                  ⛔ create_diagnostic_game signature is FROZEN (already audited).
                                  ⛔ abort_diagnostic_run always sets status="failed" — do not
                                  change that. Cancel must NOT call it.
backend/game/diagnostics.py       PlyMetricRecord (the 21-field vocabulary; None = not measured) ·
                                  SECRET_KEY_FRAGMENTS · redacted_copy · write_report_atomically ·
                                  ply_metric_to_dict · build_ai_match_report · LIVE_SENTINEL
                                  ("LIBRETILES_AI_PLAY_LIVE") · CREDENTIAL_FORWARD_NAMES
                                  ⛔ This file is byte-frozen — import it.
backend/game/position_sets.py     default_position_set_dir · game_from_snapshot
                                  ⛔ byte-frozen — import only.
backend/game/admin.py             GameSessionAdmin only today — no DiagnosticRunAdmin yet.
                                  Dashboard cards already exclude is_diagnostic.
backend/catalog/admin.py          get_urls + admin_site.admin_view — the custom-view house
                                  pattern; the sync view passes NO user argument to call_command
backend/tests/diagnostics/test_turn_probe.py   mint_token uses RefreshToken.for_user — ⛔ do NOT
                                  copy that (it persists OutstandingToken). Your mint is AccessToken.
backend/tests/test_game_app_has_no_dev_imports.py   AST guard: no pytest/pytest_django/ruff/mypy
                                  import under backend/game/**
backend/tests/test_diagnostic_session.py   create_diagnostic_game / abort / in-flight house tests
frontend/src/lib/ai-play-diagnostic.ts   runDiagnosticTurn · serializeTerminalObservation ·
                                  TerminalObservation · FakeScript · QueueMode ·
                                  ⭐ aiSlot hardcoded 1 — the one existing-line product change
frontend/src/lib/ai-play-diagnostic.test.ts   focused vitest house style
frontend/src/lib/ai-play-diagnostic.worker.test.ts   in-process route drive (BACKEND_URL before
                                  dynamic import, mocks @/lib/ai-runtimes)
backend/game/management/commands/diagnose_ai_play.py   docstring: must not import pytest into
                                  game/**. Study the isolation, do not import the harness.
backend/game/migrations/0010_diagnostic_service_account.py   latest game migration; 0011 depends
                                  on it. ⛔ Do not edit 0009 or 0010.
backend/pyproject.toml            ⚠ addopts = "-q": never pass a second -q
```

Enumeration status: hypothesis. Line numbers drift; re-measure before editing.
Your report carries `Enumeration widened:`.

## 1. Repository gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be f17a8ba0dc0e0d97da770e2ed2238190b6e432b1
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before start and before commit
```

If `main` has advanced past `f17a8ba`: re-gate against the THEN-HEAD, state the new baseline in your
report, and continue — your allowlist and claims do not change. Any other divergence: classify with
the five canonical recovery classes and stop on `unexplained-divergence`.

## 2. THE GOAL — one paragraph

Slice 4 landed the persisted diagnostic session (two AI seats, server-derived acting slot, abort
path, reserved service account). This slice makes it RUN in fake mode: an admin launches a
DiagnosticRun from Django admin; a detached `manage.py run_diagnostic_match --run-id <uuid>`
process drives plies through ONE long-lived plain-Node worker that imports the existing
`/api/ai/move` POST handler; each ply is persisted as DiagnosticPly; cancel, caps, heartbeat, and
an access-only service JWT all work; provider calls stay ZERO. Live NIM (K1) is a later exchange.

## 3. The design contract — accepted plan, with Orchestrator corrections baked in

The planning report is advisory and typo-ridden. Copy field names from SOURCE, not from that
report. The corrections below are binding and override the plan.

### 3.1 Command and process (D1, corrected)

```text
Command:  manage.py run_diagnostic_match --run-id <uuid>
          ⛔ the ONLY CLI argument. No --token, no --worker, no --base-url, no user strings.
Spawn:    admin launcher uses subprocess.Popen(
            [sys.executable, str(backend / "manage.py"), "run_diagnostic_match",
             "--run-id", str(run.id)],
            cwd=backend,
            start_new_session=True,
            stdin=subprocess.DEVNULL,
          )
          ⛔ NOT `python -m django run_diagnostic_match` (that is not a management-command entry).
          Python-child env: copy os.environ THEN unset APPIMAGE, ARGV0, APPDIR. No JWT in this env.
          The child mints the JWT itself after start.
Lifecycle:
  · select_for_update the row; require status=="queued"; set running + pid + heartbeat_at
  · heartbeat every 30s or every 5 plies, whichever comes first
  · wall-clock: check elapsed vs max_wall_clock_seconds before each ply; POSIX signal.alarm
    with a +60s grace is allowed
  · on Node death mid-ply: log it, inspect whether a Move was committed, write DiagnosticPly
    from persisted state and/or observation (None where not measured), spawn a FRESH Node
    worker for the next ply
Stale escape from unique_inflight_diagnostic_run:
  Before creating/spawning, flip status="running" (and queued-with-stale-heartbeat if you
  prove that case) rows whose heartbeat_at is older than max(300, 2 * max_wall_clock_seconds)
  seconds to status="abandoned", diagnostic_end_reason="stale_heartbeat".
  A second in-flight create is a FORM MESSAGE, never HTTP 500, never an uncaught IntegrityError
  at the admin view.
Cancel (CORRECTED — the plan called abort_diagnostic_run here; that is wrong):
  Admin sets status="cancelled" via a dedicated helper (see 3.6).
  Runner polls status at heartbeat / ply boundary, SIGTERM the Node child, writes the log,
  exits 0. ⛔ Do NOT call abort_diagnostic_run on cancel (it always sets failed).
Authorship failure: abort_diagnostic_run(reason="model_authorship_failure") — that path stays.
Caps hit: status="completed", diagnostic_end_reason="truncated", score_authority="".
Natural finish: status="completed", diagnostic_end_reason naming the game-over / set-exhausted
  case you choose; quote it in the report.
```

### 3.2 Runner loop (D2, corrected)

```text
Per ply:
  1. heartbeat / cancel / cap / wall-clock checks
  2. acting = _resolve_acting_ai_slot(session); None → fail closed
  3. send ONE JSONL command to the long-lived Node worker (no token field — see 3.3)
  4. parse one JSONL observation (length-capped; json.loads in try/except)
  5. reconcile with the latest persisted Move on the session (if any)
  6. build PlyMetricRecord; persist DiagnosticPly; append redacted JSONL
  7. add provider_requests_used (0 in fake generic_unchanged) into the run cumulative
  8. assisted: continue on any backend-committed move; record completion_source faithfully
  9. authorship: if completion_source not in {provider_candidate, repair_candidate},
     WRITE the ply first, THEN abort_diagnostic_run(reason="model_authorship_failure")
 10. game_over (full-game) or positions exhausted (position-set) → complete

Instruments:
  full-game: create_diagnostic_game session, drive until game_over or cap.
  position-set: ONE DiagnosticRun, ONE session remounted per position via
    apply_position_snapshot. Load the committed asset from
    default_position_set_dir() by matching position_set_digest (64-hex).
    ⛔ Do not generate new assets. ⛔ Do not edit position_sets.py.

⭐ SSE DOES NOT CARRY first_validate_valid, earlier_attempt_failures, or steps_consumed.
   TerminalObservation (ai-play-diagnostic.ts) carries: completion_source, probe_status,
   repair_attempted, terminal_cause, provider_requests_used / turn_provider_requests_used,
   valid_candidate_count (via serialize path), action, score, attempts[], queue.
   Derive what you can from TerminalObservation + persisted Move + loop state.
   What you cannot observe, store as None (did_not_measure). ⛔ Do not invent booleans.
```

### 3.3 Node worker (D3, corrected) — K2 machinery, in-repo

```text
New files (preferred location — keep them OUT of the Next app graph):
  frontend/scripts/diagnostic-resolve-hooks.mjs
  frontend/scripts/diagnostic-worker.mjs

Runtime (already proven; re-prove by construction):
  1. Node native TypeScript type stripping — no tsx, no esbuild, no bundle, no extra flag
  2. module.registerHooks() resolve hook:
       @/  →  frontend/src/
       retry .ts .tsx .js /index.ts
       (".js" is required for next/server)
  3. cwd = frontend/ so node_modules resolve
  ⛔ If import fails because of non-erasable syntax (enum/namespace), STOP and report.
     Do NOT silently add --experimental-transform-types.
  ⛔ Do NOT add "type": "module" to frontend/package.json.

Worker process: ONE long-lived Node per run. stdin/stdout JSONL. Dies on stdin EOF.
IPC command (Python → Node) — NO token, NO secret:
  { "cmd": "run_turn", "seq": <int>,
    "game_id": "...", "provider": "...", "model_id": "...",
    "timeout_seconds": <int>, "max_steps": <int>,
    "script": "generic_unchanged" | "noop_rescue" | ...,
    "queue_mode": "selected-only" | "catalog-fallback",
    "ai_slot": 0 | 1 }
IPC result (Node → Python):
  { "seq": <int>, "status": "done", "observation": { TerminalObservation fields } }
  { "seq": <int>, "status": "error", "message": "<redactable>" }
Shutdown: { "cmd": "shutdown" } then wait for exit.

JWT: Node reads process.env.LIBRETILES_AI_PLAY_JWT and passes it as runDiagnosticTurn's
     `token`. ⛔ Never log it. ⛔ Never put it on argv. ⛔ Never put it in an IPC field
     (stdin JSONL can be dumped).
BACKEND_URL: process.env.BACKEND_URL (same name the vitest worker already uses).

Node env is a WHITELIST, never os.environ.copy(). Allowed names (add only if a test
proves the worker cannot start without them):
  PATH, HOME, LANG, LC_ALL, TZ, NODE_PATH (only if required — prefer omitting),
  BACKEND_URL, LIBRETILES_AI_PLAY_JWT, LIBRETILES_AI_PLAY_SCRIPT (optional; IPC script
  wins when both exist)
Forbidden in Node env (fail the test if present):
  APPIMAGE, ARGV0, APPDIR, DJANGO_SECRET_KEY, DATABASE_URL, SECRET_KEY,
  NVIDIA_API_KEY, OPENROUTER_API_KEY, every name in CREDENTIAL_FORWARD_NAMES,
  LIBRETILES_AI_PLAY_LIVE (must be ABSENT — fake mode)

aiSlot: add `aiSlot?: number` to runDiagnosticTurn opts; default 1 so the product path
        stays slot 1. Diagnostic commands pass session.current_turn_slot.
        ⛔ Do not change any non-diagnostic caller to a wrong seat.

L4 is REQUIRED. L1 (HTTP to a running Next.js) is an allowed equivalent in the locked
decision but is OUT OF THIS SLICE. If the Node worker cannot import POST, STOP and
report — do not silently fall back to HTTP.
```

### 3.4 DiagnosticPly + migration 0011 (D4, corrected)

```text
NEW backend/game/migrations/0011_<descriptive>.py
  depends on ("game", "0010_diagnostic_service_account")
  reversible CreateModel only — no data migration, no RunPython
  ⛔ do not edit 0009 or 0010
  ⛔ do not add fields to DiagnosticRun

DiagnosticPly MUST persist a PlyMetricRecord. Source of truth for field names:
  backend/game/diagnostics.py PlyMetricRecord + ply_metric_to_dict.
  Do not copy the planning report's truncated/typo column list.

Lawful shapes (pick one; say which):
  A. JSONField `metrics` = redacted_copy(ply_metric_to_dict(record)) PLUS relational
     columns: run FK, ply_index, position_index (nullable). UniqueConstraint(run, ply_index).
  B. Columns matching every PlyMetricRecord field (nullable where the dataclass is
     Optional) PLUS run FK, ply_index, position_index.

SECRET_KEY_FRAGMENTS = authorization, token, secret, password, api_key, apikey,
  bearer, cookie, prompt, raw_body, env.
  ⛔ No DiagnosticPly *column name* may contain any of those substrings.
     `token` is the dangerous one — do not name anything *token*.
  JSON payloads go through redacted_copy before save.

created_at auto_now_add is fine. related_name="plies".
```

### 3.5 JWT mint — owed F04 disposition (D5, corrected)

```text
from rest_framework_simplejwt.tokens import AccessToken
token = AccessToken.for_user(service_user)
token.set_exp(lifetime=timedelta(seconds=min(max_wall_clock_seconds + 600, 6 * 3600)))
jwt = str(token)

AccessToken does NOT inherit BlacklistMixin. AccessToken.for_user does NOT write
OutstandingToken. RefreshToken.for_user DOES (token_blacklist is in INSTALLED_APPS).
⛔ Never mint RefreshToken in this slice.
⛔ Do not change SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"] (stays 2h); override is per-token.

Echo rules — each has a test:
  never argv · never logs · never report artifact · never DiagnosticPly ·
  never parameters_json · never IPC JSON · never SSE
  Logs may say token_present: yes. Tests grep for the minted string and fail on a hit.
  OutstandingToken.objects.count() is unchanged across mint.
Never return the JWT from a service helper to the admin view.
```

### 3.6 Admin launcher (D6, corrected)

```text
DiagnosticRunAdmin on DiagnosticRun, get_urls + admin_site.admin_view, PLUS an explicit
has_change_permission(request) guard (slice-4 residual). Staff-only.
created_by = request.user (staff).

Launcher POST:
  typed fields: instrument, assist_mode, seat0_model_id, seat1_model_id, prompt_id,
  variant_slug, seed, max_plies, max_provider_requests, max_wall_clock_seconds,
  position_set_digest (required iff instrument=position-set).
  ⛔ NO base_url field (slice 7).
  ⛔ NO call_command. ⛔ NO user string on any argv besides the UUID you created.
  Flow: stale-heartbeat flip → in-flight form error OR
        create_diagnostic_game(...) → configure_diagnostic_run(...) → Popen.
  Store django_origin (from the request, e.g. request.build_absolute_uri("/").rstrip("/"))
  inside parameters_json so the runner can set BACKEND_URL. That is NOT a provider base_url.

Caps the launcher must write (create_diagnostic_game currently leaves them at 0):
  max_plies default 60, admin max 200
  max_provider_requests default 200, admin max 1000   (R4)
  max_wall_clock_seconds default 3600, admin max 21600
  parameters_json includes subcaps_provisional: true
  executed_runtime_mode = "fake" on the run row for this slice
  Refuse to spawn if any cap is still 0.

Cancel control: POST action → cancel_diagnostic_run (new helper):
  status="cancelled", diagnostic_end_reason="cancelled", ended_at=now,
  session.status="abandoned", session.game_end_reason="".
  ⛔ Does not set failed. ⛔ Does not create Move rows.

Changelist: heartbeat age, in-flight badge. Keep diagnostic sessions visible to staff
(filter, not invisibility) — GameSessionAdmin already has is_diagnostic.

This slice's launched runs are FAKE: script generic_unchanged, queue_mode selected-only,
LIVE_SENTINEL unset, no provider keys in Node env. The form may still collect model ids
(they are real catalog ids stored on the run for later live work).
```

### 3.7 Caps, fake mode, K1, INFOSEC (D7–D9, corrected)

```text
Ply ceiling and provider-request ceiling are INDEPENDENT. Hitting either:
  diagnostic_end_reason="truncated"; metrics below sample stay None.
K1 (8–12 live NIM calls) is NOT this slice. Do not freeze instrument subcaps.
This slice: executed_runtime_mode="fake". If LIVE_SENTINEL is set in the runner
process, refuse to start (fail closed) — live is a later grant.
INFOSEC: JWT mint is R3 / section 4.4 (owed at slice 5-IA, not you).
Provider-boundary 4.6 is deferred until a live call exists. You do not certify either.
Threat-model constraints you implement: whitelist Node env, token-no-echo, no
call_command with user args, JSONL length cap, reports under backend/var/ (gitignore).
```

### 3.8 Helpers in services.py

Add only what the command and admin need. Suggested:

```text
configure_diagnostic_run(run, *, instrument, position_set_digest, max_plies,
                         max_provider_requests, max_wall_clock_seconds,
                         extra_parameters) -> DiagnosticRun
  range-check caps; merge extra_parameters into parameters_json (must not contain
  JWT or any SECRET_KEY_FRAGMENTS key)

cancel_diagnostic_run(*, run_id) -> dict   # see 3.6; never returns a JWT

mint_diagnostic_access_token(service_user, *, lifetime) -> str
  ⛔ called ONLY from the management command, never from admin.py
```

create_diagnostic_game stays signature-frozen (always instrument="full-game", caps 0).
The launcher/helper updates the row after create. Prefer this over changing the audited
function.

## 4. Path allowlist and negative authority

```text
Positive authority (exact paths; stage by explicit path, never git add -A):
  backend/game/models.py                                          DiagnosticPly only
  backend/game/migrations/0011_<descriptive>.py                   NEW
  backend/game/services.py                                        helpers in §3.8; no abort semantics change
  backend/game/admin.py                                           DiagnosticRunAdmin + launcher/cancel
  backend/game/management/commands/run_diagnostic_match.py        NEW
  backend/game/templates/admin/game/diagnosticrun/                NEW templates
  backend/tests/test_diagnostic_runner.py                         NEW
  backend/tests/fixtures/diagnostic_stub_worker.mjs               NEW (Python-loop tests)
  frontend/src/lib/ai-play-diagnostic.ts                          aiSlot parameterization
  frontend/src/lib/ai-play-diagnostic.test.ts                     focused aiSlot + no-echo tests
  frontend/scripts/diagnostic-resolve-hooks.mjs                   NEW
  frontend/scripts/diagnostic-worker.mjs                          NEW
  .gitignore                                                      ONLY to ignore backend/var/

Negative authority (⛔ forbidden):
  backend/gamecore/**                     byte-frozen
  backend/game/diagnostics.py             byte-frozen (import only)
  backend/game/position_sets.py           byte-frozen (import only)
  backend/game/migrations/0009_*          byte-frozen
  backend/game/migrations/0010_*          byte-frozen
  backend/accounts/**                     import User via settings.AUTH_USER_MODEL
  backend/catalog/**, backend/config/**   ⛔ no SIMPLE_JWT change, no new setting required
  backend/assets/**                       do not generate/edit position-set assets
  frontend/package.json                   ⛔ no "type": "module"
  frontend/src/app/api/ai/move/route.ts   ⛔ no edit
  ⛔ No Redis, no Celery, no live NIM, no provider call, no K1, no L1 HTTP driver
  ⛔ No git add -A, no force, no amend, no rebase, no new branch, no tag
  ⛔ Never read or print backend/.env / frontend/.env.local
```

Commands and the RF-16 bounded deviation: all Python through
`env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from `backend/` — the declared `poetry run`
route is unusable in this Worker boundary (the Cursor AppImage intercepts `python*` via inherited
`APPIMAGE`/`PYTHONHOME`); rationale, evidence class, bounded authority, and stopping condition as
previously stated. ⛔ Never ambient `python`, `python3`, or `poetry run`.

## 5. Fail-before table — capture BEFORE you edit, verbatim

| ID | Pre-fix claim (must fail on current HEAD) |
|---|---|
| F01 | No DiagnosticPly model/table; a runner ply cannot persist |
| F02 | No cancel path: DiagnosticRunAdmin / cancelled-from-running does not exist |
| F03 | Caps default 0 on DiagnosticRun; no truncated end-reason from a runner |
| F04 | No runner mint; after the slice: minted JWT string absent from argv, logs, report, DiagnosticPly, parameters_json, and IPC fixtures; OutstandingToken count unchanged |
| F05 | LIVE_SENTINEL set → runner must refuse (command does not exist pre-fix) |
| F06 | authorship + completion_source outside {provider_candidate, repair_candidate} → abort_diagnostic_run (failed, model_authorship_failure) AND the ply row still exists |
| F07 | in-flight second launch is a form message, not 500 |
| F08 | AST guard still holds: game/** does not import pytest |
| F09 | Node worker env whitelist: no DJANGO_SECRET_KEY, no NVIDIA_API_KEY, no OPENROUTER_API_KEY |
| F10 | runDiagnosticTurn accepts aiSlot; omitting it keeps product behaviour at slot 1 |

Python-loop tests MUST use the stub worker (backend/tests/fixtures/diagnostic_stub_worker.mjs) so
pytest does not import Next.js. Additionally run the committed real worker once under plain `node`
with script generic_unchanged and a closed/unused BACKEND_URL to prove the K2 import path is
in-repo (zero provider env). Quote that invocation's exit code and a redacted one-line result.

## 6. Validation — standing backend set PLUS focused frontend (you mutate frontend)

From `backend/`:

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py migrate
```

Documented mypy scope, never narrowed. Plain `-m pytest`, never a second `-q`; quote all summaries
VERBATIM. Also quote the 0011 migrate line.

From `frontend/` (required because ai-play-diagnostic.ts changes):

```bash
npm run typecheck
npm run lint
npx vitest run src/lib/ai-play-diagnostic.test.ts
```

⛔ No `npm run build` (writes `.next/`). Classify any failure before repairing; one broad rerun per
materially changed candidate. Added tests fine; no removals, no new skips.

Baseline at `f17a8ba` (re-measured this whole): mypy `Success: no issues found in 91 source files`,
ruff clean, pytest `874 passed, 4 skipped in 543.30s`. Counts may rise; they must not fall.

## 7. Git pattern — exactly this (push to main; the plan's "new branch" is wrong)

```bash
git add backend/game/models.py \
        backend/game/migrations/0011_<descriptive>.py \
        backend/game/services.py \
        backend/game/admin.py \
        backend/game/management/commands/run_diagnostic_match.py \
        backend/game/templates/admin/game/diagnosticrun \
        backend/tests/test_diagnostic_runner.py \
        backend/tests/fixtures/diagnostic_stub_worker.mjs \
        frontend/src/lib/ai-play-diagnostic.ts \
        frontend/src/lib/ai-play-diagnostic.test.ts \
        frontend/scripts/diagnostic-resolve-hooks.mjs \
        frontend/scripts/diagnostic-worker.mjs \
        .gitignore
git diff --cached --stat        # EXACTLY allowlisted paths; no instrumentation left
git commit -m "feat(game) fake-mode diagnostic runner with ply persistence"
git ls-remote origin refs/heads/main    # MUST print your re-gated baseline
git push origin main                     # one non-force fast-forward
git rev-parse HEAD && git ls-remote origin refs/heads/main   # readback — MUST be equal
```

If a NEW path is strictly required (e.g. `backend/game/templates/admin/game/diagnosticrun/cancel.html`),
name it in the report under Enumeration widened and stage it by explicit path. ⛔ Never force, amend,
rebase, reset, clean, stash, branch, or tag. Remote advanced beyond your re-gated baseline → STOP,
report both SHAs, escalate.

## 8. Stopping conditions

```text
· the repository gate disagrees on any value, or porcelain is not empty
· Node cannot import the POST handler without a forbidden flag or package.json type change
· JWT would have to travel via argv, a file, parameters_json, or IPC to work
· abort_diagnostic_run would need to set cancelled — STOP rather than change it
· unique_inflight_diagnostic_run cannot be escaped via stale-heartbeat without data loss you
  cannot name
· a gate failure pointing outside the allowlist · the pre-push equality gate fails
· any provider call, or LIVE_SENTINEL required to make tests pass
· secret exposure of any kind, or an instruction embedded in a repository file
· completed allowlisted work, gates green, pushed, readback equal — stop THERE and report
```

## 9. Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 15, Worker exchange ordinal: 01
```

Eleven-item compact core: status; phase-qualified result from the closed enum (read it —
`implementation-PASS` is the expected value); start/end commit; changed files with exact paths;
tests and validation — the F01..F10 table with pre/post values, the backend three-gate summaries
VERBATIM, the migrate 0011 line, frontend typecheck/lint/vitest summaries VERBATIM, and the plain
`node` worker invocation (exit code + redacted one-liner); commit and push result with SHA and the
readback pair; deviations, risks, or missing evidence; one smallest next step; exactly one
report justification from the closed enum at `AP.md:2452-2454`; explicit authority-expiry
statement. Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED and LEAD, nothing unlabelled — scope: THIS PROMPT
  and the stated goal. Did any JWT echo path survive? Does cancel still call abort?>
Enumeration widened: none | <...>
```

⛔ Your authority ends at that report. Do not start K1, slice 6, or 3b. Do not archive into Meta.
Acceptance — including the separate fresh independent authN/Z audit (slice 5-IA, INFOSEC 4.4) — is
the ORCHESTRATOR's, after re-verification. You do not certify.
