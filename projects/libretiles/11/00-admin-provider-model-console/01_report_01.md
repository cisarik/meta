Brána sedí a toto je tá istá relácia. Nižšie je chýbajúci terminálny report — bez zmeny plánu a bez implementácie.

### Report for ORCHESTRATOR_CHAT

Logical whole identity: admin-provider-model-console  
Worker session ordinal: 01, Worker exchange ordinal: 02

Status: PASS  
Phase-qualified result: not-applicable  
Start and end commit: 3d7eae9 → 3d7eae9 (no mutation)  
Changed files and purpose: none — this exchange mutates nothing  
Tests and validation: not-applicable — no candidate was produced  
Commit/push result: not-applicable  
Logical-whole closure: not-closed  
Resolved Execution Issues / Near-Misses: exchange 01 froze a decision-complete client-native planner artifact and omitted the separately required terminal report; cause: CreatePlan was treated as the stop event; resolution: this repair renders the missing report prospectively against the frozen artifact `APMC diagnostic console`; residual risk: none for this rendering — the Plan-to-Execution Gate remains uncompleted and an accepted plan still grants nothing  
Pre-Existing Failure Classification: none

Report justification: new-evidence

Authority expiry: report-rendering-only authority for exchange 02 expires at this terminal report. Frozen-plan content is unchanged. Implementation, mutation, acceptance, publication, and closure remain unauthorized.

Smallest next step: Orchestrator reviews this report against the frozen artifact, then issues a separate implementation prompt (`Native planning mode: not-used`, exact path allowlist, exact baseline) for slice 1 only — extract engine self-play into `backend/gamecore/selfplay.py`.

Visible context pressure: high (two exchanges of a twelve-deliverable plan in one session).

Planning cycle: initial  
Prior planning report: none  
Targeted revision basis: none  
Changed decision boundary: none  
Preserved unaffected decisions: none  
Automatic targeted revisions used: 0

---

## D1 — Execution-route decision for the LLM tier

**Recommendation: L4 hybrid.** Engine tier and model tier use different routes. A single ply is driven by one mechanism; the game loop and job control live in another. L3 is rejected. Per-ply pytest+vitest spawn (today’s `diagnose_ai_play`) is rejected as the whole-game driver.

### L1 — Python POSTs to an already-running Next.js `/api/ai/move`

| Item | Decision |
|---|---|
| Topology | Django parent + already-running Next.js HTTP server. Python `httpx` (already in `backend/pyproject.toml`) POSTs and consumes SSE. The route already commits to Django. |
| Installed/running | Django; Next.js (`npm run dev` or `npm start`). Redis not required (AI-only). |
| Auth | JWT in JSON body (`token`), because that is what `POST` in `frontend/src/app/api/ai/move/route.ts` reads. Mint with `RefreshToken.for_user(diagnostic_owner)` as `mint_token` in `backend/tests/diagnostics/test_turn_probe.py`. |
| SSE / per-ply | Python consumes the SSE stream; per-ply record assembled from `done` frames plus Django `Move.ai_metadata` plus a pre-ply `GET /api/game/{id}/ai-candidates/`. |
| Next.js down | Fail closed: run state `blocked_dependency`, `executed_runtime_mode` records that the model tier did not measure. |
| Admin button | POST creates `DiagnosticRun`; subprocess is the CLI command below. |
| Bare terminal | `manage.py run_diagnostic_match --run-id <uuid>` (parameters from the row, not argv). |
| In-process Django? | Job control yes; the TypeScript pipeline no. |
| H13 | Does not put the six-minute pytest suite on a run. Focused tests only. |

### L2 — Node CLI imports the route module

| Item | Decision |
|---|---|
| Topology | One long-lived Node worker per run imports `POST` from `route.ts` (same as today’s Vitest worker). No Next.js HTTP server. Django still required for state. |
| Installed/running | Django + `node`/`npx` + frontend `node_modules`. |
| Auth | Same JWT-in-body as L1. |
| SSE / per-ply | In-process `NextRequest` → `POST` → `consumeAIStream`. |
| `node` missing / `npx` slow | Fail closed, same `blocked_dependency` / did-not-measure shape. `npx vitest` per ply is the existing cost; L2 must be one worker for the whole run. |
| Admin / CLI | Same as L1: Python parent starts **one** worker, not one per ply. |
| H13 | Same: not the full suite. |

### L3 — Python-native OpenAI-compatible client (second pipeline)

Rejected. A second implementation of forced `validateMove`, fallback queue, repair reserve, and step-budget arithmetic cannot support any claim of the form “this is what players experience.” One drifted clamp, tool-forcing rule, or budget would make the console report a number about a pipeline the product does not run. If L3 were ever forced, every report would have to carry the mandatory label `pipeline: python-reimplementation` and could not set `executed_runtime_mode` to a production-live meaning. Not recommended.

### Fourth route (L4) — recommended

Yes. The prompt’s three routes are not enough.

- **Engine tier (D5):** in-process Python `Game` loop in `backend/gamecore/selfplay.py`. No Node, no provider, no `/api/ai/move`.
- **Model tier:** Python parent owns the run record, caps, cancellation, heartbeat, and report. **One** long-lived Node worker per run imports the existing `POST` (L2-loop). If Next.js is already up, HTTP POST to `/api/ai/move` (L1) is an allowed equivalent, not a second pipeline.
- Catalog-model runs need **zero** edits to `frontend/src/app/api/ai/move/route.ts`.
- Admin-typed diagnostic URLs cannot enter `getLanguageRuntime` without a later bounded seam (D8 / D12). That is not a reason to fork the pipeline in this whole.

`diagnose_ai_play` remains prior art for one isolated turn, not the whole-game driver: `turn_count` loops **independent** games via pytest live_server → `npx vitest` per turn.

---

## D2 — Metric model

Product-faithful final score, ply count, and completion rate are **engine** numbers (section 3.1 / H5 rescue). They must never be sold as model strength. `executed_runtime_mode` and a machine-readable `did_not_measure` travel with every aggregate.

### (a) Per-ply primitives

| name | type/unit | source today | RED | ENGINE / MODEL / BOTH |
|---|---|---|---|---|
| `model_authored` | bool | NEW from `completion_source ∈ {provider_candidate, repair_candidate}` on persisted `Move.ai_metadata` (`boundedAiMetadata` in `route.ts`) | false when a legal scoring move existed | MODEL |
| `first_validate_valid` | bool | NEW — first `validateMove` tool result in the turn (SSE `candidate` / overlay). Not in `boundedAiMetadata` today | false | MODEL |
| `valid_candidate_count` | int | `ai_metadata.valid_candidate_count` (already stored) | 0 when playability `found` | MODEL |
| `model_legal_score` | int points | persisted `Move.points` **only if** `model_authored`; else null | null / 0 when authored expected | MODEL |
| `ranked_best_score` | int points | NEW from `GET /ai-candidates/` (`_ranked_candidates_payload` → `candidates[0].score` by max `total_score`) **before** the move commits. Route already fetches this internally (`fetchRankedCandidatesOnce`); observer GET is the zero-`route.ts`-edit path | null if `status=indeterminate` and empty list | ENGINE |
| `ranked_search_complete` | bool | `search.complete` on that payload | false (denominator incomplete) | ENGINE |
| `give_up_while_legal` | bool | NEW from HTTP 409 `code=legal_scoring_move_exists` via `_reject_ai_nonscoring` | true | MODEL |
| `playability_status` | found/none/indeterminate | `get_ai_playability` / existing turn sample | indeterminate when a verdict needs found/none | ENGINE |
| `completion_source` | enum of six | `ai_metadata.completion_source` / SSE `done` | n/a — vocabulary frozen | BOTH |
| `terminal_cause` | string | `ai_metadata.terminal_cause` | `provider_error` / `generic_error_fallback` as model-failure signal, not a score | MODEL |
| `provider_requests_used` | int | `ai_metadata.provider_requests_used` | 0 when live was requested | MODEL |
| `steps_consumed` | int | SSE / tracker snapshot; not all persisted today — NEW diagnostic field if missing | grant exhausted with 0 valid | MODEL |
| `wall_clock_ms` | ms | SSE `elapsed_ms` | above attempt timeout | BOTH |
| `malformed_or_non_tool` | bool | SSE / `terminal_kind` | true | MODEL |
| `fallback_attempt_index` | int 1–3 | SSE attempts / `TurnAttemptRecord` | n/a | MODEL |
| `earlier_attempt_failures` | codes | attempt records | n/a | MODEL |
| `executed_runtime_mode` | fake/live | `derive_executed_runtime_mode` / turn sample | mismatch with requested → sample FAILURE `runtime_mode_not_honored` | BOTH |
| `assist_mode` | assisted/authorship | NEW run parameter, copied onto the ply | n/a | BOTH |
| `score_authority` | engine/model | NEW: `engine` iff completion was rescue/witness/ranked and assist_mode=assisted | must be `engine` whenever final score is shown from assisted | BOTH |

No seventh `completion_source`. Distinctions live in the NEW fields above.

### (b) Per-run aggregates

Each has `did_not_measure` and a floor below which the UI renders **insufficient sample**, not a number.

| aggregate | floor | notes |
|---|---|---|
| tool-valid rate (TV) | 20 plies | `valid_candidate_count > 0` |
| first-call-valid rate (FV) | 20 plies | |
| give-up-when-legal rate (GU) | 20 plies | inverse is the “too many passes” signal |
| authorship rate (AR) | 20 plies | |
| malformed rate (MF) | 20 plies | |
| move-quality ratio (MQR) | 8 **authored** plies | mean `model_legal_score / ranked_best_score`; null plies excluded |
| engine completion / final score | n/a as model skill | assisted runs: labelled `score_authority: engine` or omitted from model table |
| truncated | any cancel/crash | compute from completed plies; MQR still respects its floor |

### (c) Per-model rolling aggregate

Storage: `DiagnosticModelStats` keyed by `(provider, model_id, variant_slug, assist_mode, prompt_id, MOVE_PROMPT_VERSION, pipeline_fingerprint)` where `pipeline_fingerprint` is commit SHA plus a frozen route/prompt-hash. A run folds in only when every key matches and `executed_runtime_mode` was the requested live/fake. A changed prompt, variant, assist_mode, pipeline, or commit **starts a new series**; old series are retained and never mixed.

### Composite: LTAI 0–100

Visible, admin-editable weights (defaults; renormalize on edit): TV 25, FV 15, GU 20 (inverted), MQR 25, AR 10, MF 5 (inverted). Never a function of final score.

- Discriminates at **zero authorship** via TV, FV, GU, MF. MQR is `did_not_measure` until its floor.
- Never a bare number: every component shown beside it.
- Cancel/crash: LTAI from completed plies with `truncated: true`; refuse MQR if authored n is below floor.

### Attack on move-quality ratio (do not adopt as the only index)

- **Ratio > 1:** the model beat the 750 ms ranked list. Allowed. Means the production cap left points on the table. Do not clip to 1. Show `ranked_search_complete`.
- **`indeterminate` + empty list:** no denominator → `did_not_measure`.
- **`indeterminate` + some candidates:** noisy denominator; comparable across models **only on the same position set**, not across diverging full games.
- **`leave_value` / `rack_out`:** `_ranked_candidates_payload` omits both; product `_rank_key` is not `max(total_score)`. MQR denominator is **max `total_score`** (points left on the table). Leave-adjusted gap is later, not this whole.
- **Cost:** 0 extra provider calls. Observer `GET ai-candidates/` is one extra ranked search per ply at `DEFAULT_RANKED_MAX_ELAPSED_MS = 750`. 24-position set ≈ 18 s extra engine time.

### Schema

Keep `artifact` const `libretiles.ai-play-diagnostic/v1`. Add enum values `ai-match` and `model-position` to `report_kind`; add `$defs` sample types; `samples.items.oneOf` gains those refs. Root already has `additionalProperties: true`. Existing `engine` / `turn` / `policy-comparison` reports still validate. Tests that freeze the enum list (`test_endgame_policy_matrix.py` asserts membership, does not freeze exclusivity of three) must be extended. **No v2.**

---

## D3 — `assist_mode`

| mode | behaviour | what the numbers mean |
|---|---|---|
| `assisted` | Full product pipeline; engine rescue on | Player experience. Completion, ply count, final score are **engine**. Machine-readable `score_authority: engine`. |
| `authorship` | Commit only a backend-valid **model** placement (`provider_candidate` or `repair_candidate`) | On failure: **abort the diagnostic run** with `diagnostic_end_reason=model_authorship_failure`. This is **not** a `GameEndReason`. |

Rejected failure actions: forced pass, forced exchange, or any path around `_reject_ai_nonscoring`. Those would weaken the backend. Attributed rescue-and-continue was considered and rejected for authorship mode because it would recreate 3.1 invisibility for stall/pass rates.

Invariants untouched (call sites):

- `_reject_ai_nonscoring` still gates `_submit_pass_locked` and `_submit_exchange_locked` when `player_slot.is_ai`.
- `evaluate_scoring_move` remains the only certifier inside `_submit_move_locked`.
- `WordAuthority.accepts_tokens` remains the only formed-word authority.
- `move_search.py` defaults (`DEFAULT_MAX_ELAPSED_MS = 2000`, `DEFAULT_RANKED_MAX_ELAPSED_MS = 750`) are never assigned; diagnostic bounds are kwargs.

**Third mode (prompt A/B):** not a third `assist_mode`. Shape the runner now with nullable `PlayerSlot.ai_model` and `PlayerSlot.ai_prompt`. Cost today: two nullable FKs + `get_ai_context` reading the **acting** slot. Prompt **content** stays out of this whole.

---

## D4 — Position-set vs full games

They are **two instruments**. The Cooperator asked for one console; the console exposes both.

| Question | Instrument |
|---|---|
| How strong is this model? | **Position set** — N byte-stable snapshots from a seeded engine-vs-engine game (`gamecore.selfplay`). Same board/rack/bag/to-move for every model. |
| Does the game play through to the end? | **Full game** — `assisted` measures the engine; `authorship` measures stalls/passes via abort, not via a fake pass. |

**Generation / storage:** seeded `simulate_engine_game`; snapshot at fixed plies; store as versioned JSON under `backend/assets/diagnostics/` (same family as `ai_play_scenarios_v1.json`); SHA-256 of the file is the set identity. Comparable across commits only when the digest matches.

**N = 24** (8 opening / 8 mid / 8 late from 3 seeds). Matches D2 floors for TV/FV/GU; MQR still needs authored hits.

**Provider cost per model:** `selected-only` queue, cap **24** calls. Reason: one call per position, enough for TV CI, inside one admin sitting. Fallback (`catalog-fallback`) is out of the default position-set budget.

Position set is **stronger** for strength comparison (identical inputs). Full game is **stronger** for “plays through” and for interaction effects the snapshot cannot see. Full games diverge after the first differing move and are not the same measurement twice.

---

## D5 — Promote the self-play core

**Module:** `backend/gamecore/selfplay.py` — **outside** the AST guard.

Guard quote (`backend/tests/test_game_app_has_no_dev_imports.py`):

- Forbidden first dotted segments: `pytest`, `pytest_django`, `_pytest`, `ruff`, `mypy`.
- Path scope: `backend/game/**` only (`_GAME_ROOT = .../game`). `gamecore`, `catalog`, `accounts`, `config` are not scoped.

**Public API (specification):**

```text
SelfPlayInvariantError
SelfPlayConfig(variant_slug, seed, policy_id, max_plies, witness_max_elapsed_ms, ranked_max_elapsed_ms, ranked_max_nodes, ...)
simulate_engine_game(config: SelfPlayConfig) -> PolicyComparisonSample
```

Reporting types `PolicyComparisonSample` / `PolicySearchCost` stay in `backend/game/diagnostics.py` (already importable production code). The **ply loop and selectors** move.

| symbol | current home | dest |
|---|---|---|
| `_simulate` | `test_endgame_policy_matrix.py` | `simulate_engine_game` |
| `_choose` / `_select_rack_aware` | same | `gamecore/selfplay.py` |
| `_tile_counter` / `_fingerprint` | duplicated in matrix, `test_slovak_full_game.py`, `test_full_game_simulation.py`, `test_strength_benchmark.py` | shared helpers in `selfplay.py` |
| `pytest.fail(...)` | matrix loop | `raise SelfPlayInvariantError`; diagnostics map to report verdict `fail`, not a test abort inside production |

**Tests:** matrix / Slovak / English / strength **keep their assertions** (conservation, allowed `GameEndReason`, two-letter policy via `classify_complete_formed_words` over **token sequences**). They import the new module. That does not weaken the assertions if the tests still prove properties of `simulate_engine_game` rather than only that a helper exists.

**Search kwargs (fork 9):** never assign module defaults. Witness path: `max_elapsed_ms=10_000` (today `WITNESS_MAX_ELAPSED_MS`). Ranked path: `max_elapsed_ms=750`, `max_nodes=DEFAULT_RANKED_MAX_NODES` passed explicitly.

**`Game` imports (exchange 01):** production `game/services.py` imports `PlayerState`, `apply_final_scoring`, `determine_end_reason` — **not** `Game`. `Game` is tests + the new module.

Do not copy `test_turn_probe.apply_scenario` (legacy string `board_state` + instance attr `blanks`). Snapshots must write structured `{token, blank_as}` cells.

---

## D6 — Two AI seats

**New surface:** `create_diagnostic_game(...)` in `game/services.py`. No new `game_mode` value.

- Keep `game_mode="vs_ai"` so `_load_vs_ai_session` / `/ai-context/` / `/ai-candidates/` / `/ai-move/` keep working without `route.ts` edits.
- Discriminator: `GameSession.is_diagnostic = True` (migration).
- `_load_session_for_user` still filters `slots__user_id`.
- Acting slot: **server-derived** `session.current_turn_slot`; require that slot `is_ai=True`. Replace “first `is_ai=True`” in `submit_*_for_ai`, `get_ai_context`, `get_ai_playability`, `get_ai_candidates`. Compatible with one-AI product games (AI is slot 1 when it is the AI’s turn).
- Seat models/prompts: nullable `PlayerSlot.ai_model`, `PlayerSlot.ai_prompt`; context reads the acting slot, then session FK. Does not touch the locked route; the Node worker passes the acting seat’s `runtime_model_id` in the JSON body (already supported).

**Not reachable by ordinary players:**

| surface | control |
|---|---|
| DB | `is_diagnostic=True` |
| `/api/game/history/` | `list_games_for_user` adds `.filter(is_diagnostic=False)` |
| Admin | list filter + badge; not hidden from staff |
| Ownership | dedicated service user, unusable password, owns slot 0 (`is_ai=True`); slot 1 `is_ai=True`, `user=None`. Never the Cooperator’s player account |

---

## D7 — Bounded background job (no Redis, no scheduler)

**Model `DiagnosticRun`:** `id` (UUID), `status` (`queued` / `running` / `completed` / `failed` / `cancelled` / `abandoned` / `blocked_dependency` — last five terminal), `assist_mode`, `instrument` (`position-set` / `full-game`), `variant_slug`, `seat0_model_id`, `seat1_model_id`, `prompt` FKs, `position_set_digest`, `max_plies`, `max_provider_requests`, `max_wall_clock_s`, `heartbeat_at`, `pid`, `diagnostic_end_reason`, `executed_runtime_mode`, `score_authority`, `report_path`, `log_path`, `created_by` (admin user), timestamps, parameters JSON (range-checked copy of the form).

**Parameter defaults / hard max (exchange 01):**

| param | default | hard max |
|---|---|---|
| plies (full-game) | 40 | 200 (`TURN_COUNT_MAX` family) |
| positions | 24 | 24 in v1 |
| provider requests | 24 position-set / 80 full-game | 80 |
| wall clock | 30 min | 60 min |
| timeout_seconds per ply | 120 | 600 |
| max_steps per ply | 50 | 100 |
| queue_mode | `selected-only` | `catalog-fallback` only if explicitly set |

Ceiling behaviour: stop, persist completed plies, `truncated: true`, terminal status `failed` or `completed` with reason `cap_plies` / `cap_provider_requests` / `cap_wall_clock`.

**One run in flight:** partial unique constraint on a singleton in-flight row (status `queued` or `running`), plus `select_for_update` on launch. **Not cache.** Holds when `CACHES` is LocMemCache. LocMem is per-process; a cache lock would not hold locally (3.3).

**Launch contract:** `manage.py run_diagnostic_match --run-id <uuid>` and **nothing else**. Every parameter is read from the validated row. ⛔ Never `call_command` with admin strings (same discipline as `catalog.admin.sync_models_view`, which forwards no CLI flags — `test_admin.py` asserts `activate_new` / `allow_large_drop` stay out of kwargs).

**Cancel:** admin POST sets `status=cancelled`; runner reads the row each ply (and Node worker polls a cancel file/row); leaves `truncated` report.

**Crash recovery:** no scheduler. Admin GET and CLI `status` mark `running` with stale `heartbeat_at` as `abandoned`. Heartbeat every ply.

**Progress:** poll ~2 s; one PK read of `DiagnosticRun` plus latest `DiagnosticPly` rows. Readable log: bounded JSONL file **and** `DiagnosticPly` table. Table is metric truth; file is the transcript. Precedent: `write_report_atomically`. Cap file size.

**Provider accounting:** purpose per call (`ply` / `probe`); one call in flight unless a later prompt authorizes concurrency; terminal classification before the next call; numerical cap **24** (position-set) or **80** (full-game) with reason “admin sitting + D2 floors, not an unbounded eval.”

**Redis promise:** intact. Job uses DB + subprocess + files. `realtime.py` already swallows missing Redis. `CHANNEL_LAYERS` stays unused by this console. AI-only local boot still does not require Redis.

---

## D8 — Admin-registerable diagnostic target (minimal, diagnostic-only)

Not the full Provider entity. Not catalog de-hardcoding. Diagnostic-only-by-default so a typed URL cannot serve a player until a later whole’s promotion gate.

**Fields:** `name`, `base_url`, `model_id`, `credential_env_name`, `is_active`, `last_probe_at` (history is a child table, not a last-result field). No price, USD, balance, or spend column (`test_api.py` forbids `Edit balances`, `AI spend`, `charged credits`, `USD`).

**Save-time validation:** https only; host parse; reject userinfo; SSRF checks (D9). Runtime: Next.js diagnostic worker receives target id, Django returns non-secret fields + env **name**; Node reads `process.env[name]`.

**Promotion seam (later whole):** `promoted_catalog_id` nullable FK. Player path stays `get_selectable_models` + `isValidRuntimePair`. Nothing in this whole writes `is_active` on `AIModel` from a diagnostic target.

**Credential story — Cooperator decides (cost first):**

| option | cost | benefit |
|---|---|---|
| **A — env-var NAME only** (recommended) | New provider needs env file + Next.js restart (closest to the SSH workflow he does not want) | No secret in DB; no encryption; admin history cannot leak a value; existing `heldCredentialValues()` redaction keeps working |
| B — encrypted value in DB | Key-management, rotation, and a new redaction story (`CREDENTIAL_ENV_NAMES` would not see the value) | No restart to try a key |
| C — hybrid | Adds a second trust boundary (DB ciphertext **and** env) | Name required always; optional ciphertext later |

Process holding the secret: **Next.js** (A) vs Next.js+Django (B/C). Display: `credential present: yes/no/unknown` by **name**, never the value. Absent: fail closed, no provider call.

IBM watsonx is a separate transport (`ibm-watsonx.ts`); a typed OpenAI-compatible URL cannot represent it. Out of this diagnostic-target v1.

---

## D9 — INFOSEC threat model and controls

**Primary route: R3** (AI and provider-boundary audit).  
**Trigger row:** “AI or provider boundary, tool invocation, egress, untrusted-content ingestion.” Novel admin URL / SSRF is an escalation **within** R3 (fresh independent audit on D8 slices), not a default R4 full-application audit.

### Threat-Model Fields

Assets: provider credentials and quota; Django session/admin (highest-value target once this console exists); JWT of the diagnostic service user; catalog `sort_order` / `is_active` (player opponent selection); diagnostic reports and readable logs (model-produced text); formed-word / scoring integrity; availability of the Django process.

Trust boundaries: admin browser → Django admin (session + CSRF + axes); Django → subprocess runner; runner → Node worker → provider HTTPS; Node worker → Django JWT API; admin-typed `base_url` → arbitrary network (SSRF); model output → admin HTML; Next.js CSP (`proxy.ts`) **does not** reach Django admin.

Attacker-controlled inputs: admin form fields (`base_url`, `model_id`, run parameters); model-produced analysis and move text; provider error bodies; diagnostic JSONL.

Security properties: staff+model permission on spend/launch; CSRF on every state-changing POST; no GET spend; no `call_command` with admin strings; SSRF controls at save **and** request time; redaction by value for held env credentials; autoescape / text nodes; backend remains sole formed-word authority; Redis not required for AI-only boot.

Abuse cases: SSRF to cloud metadata via admin URL; stolen staff session launches unbounded provider spend; XSS in admin via model output (`|safe`); last usable catalog row deactivated via “fallback-order” POST; diagnostic games leak into `/api/game/history/`; cache-only lock bypassed in LocMem dev; L3-style second pipeline silently mis-measures.

### Controls (candidate findings where weak today)

1. **SSRF:** https-only; reject private, loopback, link-local, multicast, metadata ranges; DNS resolve and re-validate the **address**; no redirect into a private range; connect/read timeouts; bounded response. Checks at **Django save and Next.js request**. Admin-only is not a mitigation. Host allowlist vs free-form: D12.
2. **Production egress insertion point:** `createTrackedProviderFetch` in `frontend/src/lib/openai-compatible.ts` (today it labels via `inferProviderFromInput` and still `fetch`es; `"unknown"` is not a block). `installFetchGuard` is test-harness only.
3. **New HTTP surfaces:** admin POST + `admin_view` + extra `has_change_permission` + CSRF; throttle: new scope strings, do not rename existing (`auth_*`, `ai_context`). Failure bodies: no provider error strings, no credential-adjacent text. ⛔ Do not copy `parseBackendJson` (ignores HTTP status). Follow `api-auth.ts`: branch on `res.status` **before** body parse. Quote: “Branch on HTTP status before reading the body. A 401/429 JSON payload that happens to look like a user profile must not count as authenticated.”
4. **`admin_view` (MEASURED, Django 5.2 `AdminSite`):** `has_permission` is `request.user.is_active and request.user.is_staff` only; then `never_cache` and `csrf_protect`. **Not** model-level `change` permission. Custom launch/cancel views must also call `has_change_permission`.
5. **Audit log:** Django `LogEntry` plus a `DiagnosticAudit` row (who registered/changed a target, activated, started, cancelled) with timestamps and redacted parameters. Retention: same as admin log unless Cooperator sets otherwise — if not set in exchange 01: default keep with `LogEntry`.
6. **Redaction:** reuse `redacted_copy` / `SECRET_KEY_FRAGMENTS` on reports; `provider-logging.ts` longest-first by held env values; `provider_transport` already drops the raw message. A credential **not** in `CREDENTIAL_ENV_NAMES` is only heuristically redacted — option A keeps names on that list; B breaks it (D12).
7. **Resource abuse:** D7 caps; one in-flight run; ordinary non-staff: default DRF `IsAuthenticated` still cannot see diagnostic sessions they do not own, and they do not own the service user. Staff is the spend principal.
8. **Prompt injection / XSS:** Django templates autoescape; **no** `|safe`, `mark_safe`, or inline script for model text. Render as text nodes. `dangerouslySetInnerHTML` is absent under `frontend/src` (exchange 01 grep).
9. **Analyst LLM:** advisory only; never overrides a number or Django. Page is complete without it. On failure: hide prose, keep numbers. Default **off** in v1 (structured analysis from aggregates). If enabled later: same spend auth as D7.

Controls that need a Cooperator decision: credential A/B/C; host allowlist vs free-form URL; whether a bounded `route.ts` diagnostic-runtime branch is allowed for D8.

---

## D10 — Admin console surface

| page | hangs off | extends / block | POST-only? | shows |
|---|---|---|---|---|
| Launcher | `AIModelAdmin` | `admin/catalog/aimodel/change_list.html` `object-tools-items` (same pattern as Sync OpenRouter) | POST start | variant (`list_variant_summaries()`, do not hardcode), two catalog seats, assist_mode, instrument, caps |
| Live run | `GameSessionAdmin` custom url (dashboard pattern: `get_urls` + `admin_view`) | `admin/base_site.html` | GET poll; POST cancel | readable ply log, heartbeat, caps remaining |
| Finished report | same | same | GET | LTAI + components, `did_not_measure`, `executed_runtime_mode`, `score_authority` |
| Cross-model table | `AIModelAdmin` | changelist extra | GET | rolling stats; insufficient sample, not a fake 0 |
| Health/latency history | child of diagnostic target **or** catalog row | GET | history table, not last-result |
| Ping→pong | POST next to launcher | POST | `probeProviderCapability` result |

**Platform:** Django admin can do forms, tables, and `Refresh:` without JS. Auto-refresh: HTTP `Refresh: 2` on the live view (cost: D7 poll). Tiny static JS only if progressive enhancement is wanted; CSP from `frontend/src/proxy.ts` **does not apply** to Django admin (Next matcher only). Django emits `X-Frame-Options` / nosniff / HSTS-when-not-DEBUG, not a CSP. Still no `|safe`.

**Ping→pong:** reuse `frontend/src/lib/provider-capability.ts` (`probeProviderCapability`) — capability probe (answers, text, **tool calling**, latency), not ICMP. Smallest honest tool probe: existing validate → pong → `finishMove` state machine (`provider-capability.test.ts`). Cost: cap **1** live call per POST, cached in history; throttle a new admin scope. Flaky endpoint: history shows mix of pass/fail, not a single green.

**Fallback-order:** console **proposes** a `sort_order` diff from rolling health. Write is a reviewed POST, not one click from a GET. Refuse if the result would leave zero selectable tools-tagged active models or deactivate the last usable row.

---

## D11 — Slice sequence

Orchestrator sequence stands: **runner on today’s catalog before any provider URL.** Predecessor “provider data model first” is wrong: `getLanguageRuntime` already plays catalog pairs; a typed URL cannot enter without the D8 seam and SSRF.

If a slice’s deliverable-tier spread is two or more, it is already split below.

### Slice 1 — selfplay extract  
Objective: importable engine self-play in `gamecore`.  
Allowlist: `backend/gamecore/selfplay.py` (new), `backend/tests/test_endgame_policy_matrix.py`, `test_slovak_full_game.py`, `test_full_game_simulation.py`, `test_strength_benchmark.py`, `test_game_app_has_no_dev_imports.py` (must stay green). Negative: no `frontend/**`, no `game/models.py`.  
Tier: **E1** — bounded reversible, strong tests.  
Gates that can move: focused pytest on those tests; ruff/mypy on `gamecore`. Full 6-minute pytest not required; do not skip documented mypy scope if `gamecore` is in it (it is).  
Fail-before: `from gamecore.selfplay import simulate_engine_game` does not exist.  
Negative PASS: extract abandoned because a test would only re-export the helper and lose an assertion — say so.  
Provider: none. Independent acceptance: no. Spread: none.

### Slice 2 — schema + metric types  
Objective: v1 `report_kind` + ply fields without bumping artifact id.  
Allowlist: `backend/assets/diagnostics/ai_play_report_v1.schema.json`, `backend/game/diagnostics.py`, `backend/tests/test_ai_play_engine_diagnostic.py`, `test_ai_play_turn_diagnostic.py`, policy-comparison schema assertions.  
Tier: **E1**.  
Gates: focused pytest on diagnostic tests.  
Fail-before: enum rejects `model-position` / `ai-match`.  
Provider: none. Spread: none.

### Slice 3 — position-set + catalog CLI  
Objective: generate 24-position set; score one catalog pair from CLI without admin URL.  
Allowlist: `backend/assets/diagnostics/` (position-set JSON), `backend/game/management/commands/` (new command), `gamecore/selfplay.py`, focused tests. Negative: no `route.ts`, no diagnostic target model.  
Tier: **E2** — cross-cutting CLI + assets.  
Live cap: **24** provider calls, reason D4; default path is fake/`selected-only` with 0 live. Independent acceptance: no unless live is used (then R3 provider-boundary on that exchange).  
Fail-before: no command emits `did_not_measure` / LTAI components.  
Spread: none (live optional second exchange).

### Slice 4 — diagnostic session + acting slot + authorship abort  
Objective: two AI seats, `is_diagnostic`, acting slot = `current_turn_slot`, authorship abort.  
Allowlist: `backend/game/models.py`, new migration (`game` 0009), `backend/game/services.py`, `backend/game/views.py` (history filter only), tests. Negative: no `route.ts`.  
Tier: **E3** — durable migration + privilege-adjacent session visibility.  
Gates: focused pytest including history-exclusion and “first is_ai” replacement. Independent acceptance: **yes**, INFOSEC authN/Z + “ordinary user cannot list diagnostic games.”  
Fail-before: `list_games_for_user` returns a diagnostic session; `submit_move_for_ai` always slot 0 when both seats are AI.  
Spread: none (migration and service are one coherent outcome).

### Slice 5 — DiagnosticRun job + admin launcher for **catalog** pairs  
Objective: one in-flight DB-locked run, argv = run id only, admin POST launch.  
Allowlist: new `DiagnosticRun`/`DiagnosticPly` models+migration, `manage.py run_diagnostic_match`, `catalog/admin.py` or `game/admin.py` launcher, templates, tests. Negative: no diagnostic `base_url` field.  
Tier: **E3** — long-running process + provider spend (even on catalog).  
Independent acceptance: yes (R3). Live cap: inherit run caps (24/80).  
Fail-before: two overlapping `running` rows can exist; GET link starts a run.  
Spread: none.

### Slice 6 — live view + finished report + comparison table  
Objective: readable ply log and LTAI components in admin.  
Allowlist: admin templates/views/static under `backend/game/templates/admin/` and `backend/catalog/templates/admin/`. Negative: no `|safe`.  
Tier: **E2**. Independent acceptance: Cooperator rendered look (not Worker browser MCP).  
Fail-before: assisted final score shown as model skill; missing `did_not_measure`.  
Spread: none.

### Slice 7 — diagnostic target + SSRF + credential decision  
Objective: diagnostic-only OpenAI-compatible target with SSRF at save and request time.  
Allowlist: new model, admin, `openai-compatible.ts` seam export, **possibly** a bounded `getLanguageRuntime` / worker branch — **not** a pipeline fork. Negative: no player-catalog promotion write.  
Tier: **E3** (E4 if Cooperator chooses credential-in-DB). Independent acceptance: **mandatory** fresh audit (INFOSEC 4.6).  
Provider cap: 1 probe call per accepted POST.  
Fail-before: loopback/metadata URL saved or fetched; secret rendered in admin.  
Spread: if credential-in-DB is chosen, split key-management to its own E4 exchange.

### Slice 8 — probe history + fallback-order diff  
Objective: persist capability-probe history; reviewed `sort_order` POST that cannot zero the catalog.  
Allowlist: `frontend/src/lib/provider-capability.ts` (call, don’t redesign), admin POST, `AIModel.sort_order` write path, tests.  
Tier: **E2**. Independent acceptance: R2 on the diff is enough unless it can deactivate the last row without the refuse-test (then E3).  
Fail-before: GET reorders models; last usable row can be deactivated.  
Live cap: 1 per probe POST.  
Spread: none.

---

## D12 — What this plan cannot decide

### (a) Cooperator decisions (cost before benefit)

1. **Credential storage** — A env-name (cost: restart; benefit: no secret in DB; **recommended**); B encrypted DB (cost: KMS/rotation/redaction rewrite); C hybrid (cost: two boundaries). Exchange 01 did not choose; recommendation A stands.
2. **Host allowlist vs free-form URL** — Allowlist-only (cost: cannot type an arbitrary trial host the same day; benefit: SSRF surface collapses); free-form + SSRF (cost: must get DNS-rebinding right; benefit: matches “type a URL”); allowlist with an explicit add-host POST (cost: one extra review step). **Recommended:** free-form https + SSRF **and** a default allowlist of shipped origins, with an add-host POST. Not chosen for him.
3. **Bounded `route.ts` / `getLanguageRuntime` diagnostic branch for D8** — Edit (cost: touches locked fork 2; benefit: typed URL works); no edit (cost: D8 targets cannot use the one pipeline; benefit: catalog runner ships first). Exchange 01: catalog path needs zero edits; D8 later. Not chosen.
4. **Analyst LLM on/off** — Off (cost: no prose “analysis”; benefit: numbers cannot be overridden; **recommended v1**); on as advisory (cost: extra spend + injection surface).
5. **Authorship failure = abort** was decided in exchange 01 as the design; **attributed rescue** remains a costed alternative if he rejects abort (cost: stall rate becomes invisible again; benefit: full games always finish).

### (b) Measurements needed and not taken in exchange 01

- Live authorship rate on current catalog at `3d7eae9` (prompt cites ~zero; this Worker did not repeat live provider calls — network forbidden).
- Whether `test_slovak_unicode_witness_round_trips` still passes given `apply_scenario`’s string board (LEAD only; full pytest not re-run).
- Installed Django admin CSP: none found in `settings.py`; not a live header capture.
- Credential files: `present: unknown` by design (not read).

### (c) Section-3 assumptions not verified, or verified disagreeing

- H13 pytest **813 passed, 4 skipped** — not re-run here; Orchestrator-stated, treated as given.
- Prompt claimed `test_full_game_simulation.py` has a local `_is_word` — **MEASURED false** (uses `WordAuthority`).
- `apply_scenario` / `session.blanks` — **LEAD** that the closest LLM-turn instrument writes a legacy board; not proven red in this session.
- Cloudflare `baseURL` interpolates `CLOUDFLARE_ACCOUNT_ID` (env), not an admin runtime URL — verified as not a free-form production base URL.

### (d) Different logical whole

Prompt content / SEARCH_PROFILE; H10 English CORE on Czech/Polish/eight-newest; full Provider entity and catalog de-hardcoding; player-path promotion beyond the seam; deployment, nginx, host hardening, axes-behind-nginx; Stripe / LM Studio / Vercel AI Gateway; seventh `completion_source`; changing `MAX_FALLBACK_ATTEMPTS` or `move_search.py` defaults.

---

## Orchestration critique

**MEASURED**

- Exchange 01 produced a frozen planner artifact and no `### Report for ORCHESTRATOR_CHAT`; that is why exchange 02 exists (`AP.md` 467–478).
- Git gate at exchange 02: `HEAD` `3d7eae96d567a7004a927de45f53e16e2baf108f`, porcelain empty, `## main...origin/main`.
- `AdminSite.admin_view` checks staff only (`is_active and is_staff`), plus `csrf_protect` / `never_cache` (Django 5.2 `sites.py`).
- `inferProviderFromInput` returns `"unknown"` and `createTrackedProviderFetch` still fetches; production egress allowlist absent. `installFetchGuard` is test-only (`SHIPPED_PROVIDER_ORIGINS` is two hosts).
- `MovePromptLexiconId` is `"collins2019" | "slovak"`; non-Slovak variants get the English CORE (H10 recorded, not fixed).
- `list_variant_summaries()` is a module-level function with per-variant `readiness`.
- Judge route has no production frontend caller (tests only); it authenticates via `api-auth.ts` **before** `req.json()`. Move route authenticates only by using `token` against Django and `parseBackendJson` ignores HTTP status.
- Next `proxy.ts` CSP does not wrap Django admin.
- `test_game_app_has_no_dev_imports.py` scopes `game/**` only; forbidden set is `pytest`, `pytest_django`, `_pytest`, `ruff`, `mypy`.
- `Game` is not imported by production `game/services.py`.
- No Celery/RQ/Huey/dramatiq/APScheduler in `backend/pyproject.toml`.
- `provider-capability.ts` already implements the tool-calling ping→pong the prompt treated as greenfield.
- `test_full_game_simulation.py` has no local `_is_word`.
- Catalog `AIModelListView` / `AIPromptListView` are `AllowAny`; `VariantListView` has no explicit class and inherits DRF `IsAuthenticated`.
- `_ranked_candidates_payload` omits `leave_value` and `rack_out`.
- `runDiagnosticTurn` hardcodes `aiSlot: 1` and drives one turn.
- Money-string assertion lives in `backend/tests/test_api.py`.

**LEAD**

- `test_turn_probe.apply_scenario` writes a string grid and `session.blanks = []` (not a model field) and may ignore occupied fixtures under structured `board_state` — do not copy it.
- A cheaper answer to “how strong is this model” than D1–D4’s full console is slice 3 alone (24-position CLI on catalog). The console is still what he asked to **operate**; the cheaper instrument is the first slices, not a different whole.
- Prompt self-contradiction resolved toward section 2’s goal: “no `route.ts` edits” holds for the catalog runner; D8 may later need a bounded seam — named in D12 rather than forked as L3.
- “CLI without loading the frontend” was interpreted as no browser / no rendered Next page, not “no Node,” because L3 would falsify the measuring instrument.
- Completion-rate-as-model-skill is the wrong question under `assisted` (3.1); D3/D4 are the right questions.

The whole **is** shaped as a measuring instrument for a question he has (“which model should players face / which fallback to try”), provided it does not report engine scores as model skill. Deliverable D2 would be the wrong question if it used final score; the frozen plan does not.

---

## Enumeration widened

- `frontend/src/lib/provider-capability.ts` + unit test + `npm run probe:provider` / `PROVIDER_PROBE_LIVE=1` live file — prior art for ping→pong.
- `CREDENTIAL_ENV_NAMES` in `provider-logging.ts` (nine providers + IBM fields); a diagnostic env name not on that list is weakly redacted.
- Four `createOpenAI` call sites, all compile-time or env-derived bases (`openrouter.ts`, `nvidia-nim.ts`, `openai-compatible.ts`, `ibm-watsonx.ts`).
- Cloudflare base URL includes `CLOUDFLARE_ACCOUNT_ID` (env), still not admin-supplied.
- Public `AllowAny` catalog list vs authenticated variant list.
- `observe_source_revision` already `subprocess`es `git rev-parse` inside `game/diagnostics.py` (AST-legal; pytest is not).
- `cleanup_consumed_ws_tickets` is the project’s background-work precedent (bounded row cleanup, no scheduler).
- Operations dashboard GET at `game_gamesession_dashboard` is read-only (token totals — not USD).
- `GameSession` `MODE_CHOICES` are only `vs_ai` / `vs_human`; discriminator chosen is `is_diagnostic`, not a third mode.
- `FREE_RIVAL_PAIRS` vs `DIRECT_FREE_RIVALS` both exist in `catalog/selection.py`; selectable order is direct then bootstrap/dynamic.
- Next.js 16 agent guide lives in `frontend/AGENTS.md`; no Next behaviour was asserted from memory that required `node_modules/next/dist/docs/`.

---

This report’s authority is expired. An accepted planner artifact still grants no implementation.