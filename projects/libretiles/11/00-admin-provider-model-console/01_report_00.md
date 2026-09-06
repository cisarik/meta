---
name: APMC diagnostic console
overview: Read-only AP planning report for an admin-launched, CLI-runnable AI-vs-AI diagnostic console. This session has no implementation authority. The terminal Worker report in chat is the deliverable; an accepted plan grants nothing.
todos:
  - id: slice-1-selfplay
    content: Extract engine self-play core to gamecore (E1, no provider)
    status: pending
  - id: slice-2-metrics-schema
    content: Add v1 report kind + ply metric types without bumping artifact id
    status: pending
  - id: slice-3-position-cli
    content: Position-set generator + catalog CLI scorer (cap 24 live calls)
    status: pending
  - id: slice-4-two-seat-authorship
    content: Diagnostic session, acting-slot, authorship abort (migration)
    status: pending
  - id: slice-5-run-job-admin
    content: DiagnosticRun job + admin launcher for catalog pairs
    status: pending
  - id: slice-6-admin-report-ui
    content: Live run view, finished report, comparison table
    status: pending
  - id: slice-7-ssrf-target
    content: Diagnostic OpenAI-compatible target + SSRF + credential decision
    status: pending
  - id: slice-8-probe-fallback
    content: Ping-pong history + reviewed fallback-order diff
    status: pending
isProject: false
---

# Admin provider-model console — implementation plan (advisory)

This is the AP implementation-planning outcome for `admin-provider-model-console` at baseline `3d7eae96d567a7004a927de45f53e16e2baf108f`. Native planning mode is required; Plan-to-Execution Gate is uncompleted. Implementation needs a later prompt with `Native planning mode: not-used`.

The full decision-complete record is the Worker report beginning `### Report for ORCHESTRATOR_CHAT` (D1–D12). This plan is only the Cursor convenience copy.

## Goal correction

The product goal is to make “will this model beat a human?” measurable before deployment. Three facts change the design:

- Engine-vs-engine full games already exist in tests; LLM-vs-LLM games do not.
- “CLI without the frontend” means no browser, not “no Node”: the one move pipeline is TypeScript in [`frontend/src/app/api/ai/move/route.ts`](frontend/src/app/api/ai/move/route.ts).
- Product-faithful completion rate and final score are engine numbers (rescue always fires). They must never be sold as model strength.

## D1 — Execution route (recommended: L4 hybrid)

Do not reimplement the pipeline in Python (L3). Do not spawn pytest+vitest per ply (current `diagnose_ai_play` topology).

- **Engine tier:** in-process Python in [`backend/gamecore/selfplay.py`](backend/gamecore/selfplay.py) (outside the `game/**` AST pytest guard).
- **Model tier:** one long-lived Node worker per run that imports the existing `POST` handler (same as today’s Vitest worker). Python parent owns the run record, caps, cancellation, and report. Next.js HTTP server is not required. If Next.js is already up, HTTP POST to `/api/ai/move` is an allowed equivalent (L1), not a second pipeline.
- **Auth:** mint a short-lived JWT with `RefreshToken.for_user(diagnostic_owner)` as [`backend/tests/diagnostics/test_turn_probe.py`](backend/tests/diagnostics/test_turn_probe.py) `mint_token` already does. Token stays in the JSON body because that is what the move route reads today.
- **Catalog runs need zero `route.ts` edits.** Admin-typed diagnostic URLs cannot enter `getLanguageRuntime` without a later bounded seam (D8/D12).

## D2 — Metric model (must discriminate at zero authorship)

Do not report final score or completion rate from `assisted` runs as model skill.

Per-ply primitives from persisted `ai_metadata`, SSE `done`, `GET ai-candidates/`, and `_reject_ai_nonscoring` 409 codes. New diagnostic fields (not a seventh `completion_source`): `model_authored`, `first_validate_valid`, `ranked_best_score`, `ranked_search_complete`, `give_up_while_legal`, `executed_runtime_mode`.

Composite **LTAI 0–100** with visible admin-editable weights. When authorship is zero it still moves via tool-valid rate, first-call-valid rate, and give-up-when-legal rate. Move-quality ratio is shown beside it and is `did_not_measure` until enough authored plies exist. Ratio above 1 is allowed (model beat the 750 ms ranked list). Never a function of final score.

New report kind `ai-match` / `model-position` extends [`backend/assets/diagnostics/ai_play_report_v1.schema.json`](backend/assets/diagnostics/ai_play_report_v1.schema.json) by adding an enum value and a `$defs` sample; keep `artifact` at `libretiles.ai-play-diagnostic/v1`. Existing three kinds stay valid because the schema already uses `additionalProperties: true`.

## D3 — assist_mode

- `assisted` — product-faithful; engine rescue on; machine-readable `score_authority: engine`.
- `authorship` — commit only a backend-valid model placement; on failure **abort the diagnostic run** with `diagnostic_end_reason=model_authorship_failure` (not a `GameEndReason`). Do not force pass/exchange around `_reject_ai_nonscoring`.
- Prompt A/B: two nullable FKs on `PlayerSlot` (`ai_model`, `ai_prompt`). Cheap now; prompt content stays out of this whole.

## D4 — Two instruments

- **Position set** answers “how strong is this model” (byte-stable snapshots from seeded engine self-play). Default 24 positions, `selected-only` queue, cap 24 provider calls per model.
- **Full games** answer “does the game play through” — engine question in `assisted`, stall/pass question only in `authorship`.

The Cooperator asked for one console; the console must expose both instruments, not one number.

## D5–D7 — Core, two seats, job

- Extract `_simulate` / selectors / conservation helpers from [`backend/tests/test_endgame_policy_matrix.py`](backend/tests/test_endgame_policy_matrix.py) into `gamecore`. Tests keep assertions; `pytest.fail` becomes `SelfPlayInvariantError`. Search bounds passed as kwargs only (`max_elapsed_ms=10000` witness, `750` ranked). Production defaults unchanged.
- Two AI seats: `GameSession.is_diagnostic=True` (keep `game_mode=vs_ai` so `/ai-context/` still works). Acting slot = `current_turn_slot` if `is_ai`. History: `list_games_for_user` excludes `is_diagnostic`. Service user with unusable password owns slot 0.
- Run job: `DiagnosticRun` row is the lock (partial unique on in-flight status — holds under LocMemCache). Subprocess argv is only `manage.py run_diagnostic_match --run-id <uuid>`. No Redis, no Celery. Heartbeat per ply; stale `running` → `abandoned` on admin GET / CLI status. Readable JSONL file plus `DiagnosticPly` rows. Poll ~2 s, one cheap PK lookup.

## D8–D9 — Diagnostic target and INFOSEC

Diagnostic-only OpenAI-compatible target first (not player catalog). Credential default recommendation is env-var **name** reference (option A); options B/C are Cooperator-costed. SSRF: Django save-time plus Next.js request-time (DNS re-resolve, no private ranges, https-only, timeouts). `admin_view` checks **staff only** (`is_active and is_staff`), not model perms — extra `has_change_permission` required. CSP from Next [`frontend/src/proxy.ts`](frontend/src/proxy.ts) does **not** reach Django admin. Primary INFOSEC route: **R3** (AI/provider-boundary audit).

Do not copy [`parseBackendJson`](frontend/src/app/api/ai/move/route.ts) (ignores HTTP status). New spend surfaces follow [`frontend/src/lib/api-auth.ts`](frontend/src/lib/api-auth.ts): branch on `res.status` before body parse.

## D10 — Admin surface

Hang launcher off `AIModelAdmin` (object tool, like OpenRouter sync). Live run + report off `GameSessionAdmin` dashboard pattern. Ping→pong **reuses** [`frontend/src/lib/provider-capability.ts`](frontend/src/lib/provider-capability.ts) (tool-calling probe, not ICMP). Auto-refresh via `Refresh:` header or tiny static JS; no `|safe`, no `mark_safe`. Fallback-order change is a reviewed POST diff of `sort_order`; refuse last-usable deactivation.

## D11 — Slice order (runner before provider registry)

The Orchestrator sequence is right: measure today’s catalog before any admin URL. Predecessor “provider model first” is wrong because `getLanguageRuntime` already plays catalog pairs, and a typed URL cannot enter the pipeline without the D8 seam plus SSRF.

1. Extract selfplay core (E1)
2. Schema + metric types (E1)
3. Position-set generator + CLI scorer on catalog (E2; live cap 24)
4. Diagnostic session + acting-slot + authorship abort (E2/E3 migration)
5. Bounded run job + admin launcher for catalog pairs (E3)
6. Live view + reports (E2)
7. Diagnostic target + SSRF + credential decision (E3; E4 if secrets-in-DB)
8. Probe history + fallback-order proposal (E2)

## Explicitly later / Cooperator-owned

Prompt content, H10 English CORE on non-Slovak variants, full Provider entity, player-path promotion, deployment/nginx/axes-behind-nginx, Stripe/LM Studio/Vercel AI Gateway.

Do not implement in this session.
