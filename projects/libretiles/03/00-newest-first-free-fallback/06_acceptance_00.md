Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator, not the Cooperator, and not an implementer of this candidate.

Logical whole identity: newest-first-free-fallback
Worker session ordinal: 06
Worker exchange ordinal: 01
Implementation authority: none
Native planning mode: not-used
Worker session target: fresh-worker-session
Phase: acceptance
Task identity: independent-acceptance-newest-first-free-fallback-01
Task type: independent-acceptance
Independence required: yes
Material phase gate: yes
Changed material axis: primary-objective
Ordinary-only trigger: no
Routing reopened for: primary-objective
Unchanged axes reopened: none

Continuity anchor: approved Route 2 plan (session 01) implemented across four accepted slices on main: Slice 1 `7e6dcab` (catalog safety, feature flag, sync guards, migration 0009), Slice 2 `f67e700`+`94c1655` (dynamic catalog-validated runtime, shared Play/Judge fallback queue, HTTP budgets, `provider_requests_used`), Slice 3 `a4e8608`+`53e1452`+`a908b0a` (ping-pong overlay, prompt rewrite, reversible hash-gated migration 0010), Slice 4 `e00c922` (docs/env examples/rollout story). Session 03 never filed a terminal report; its candidate was reconciled on direct verification (see 99_orchestrator_reconciliation_00.md).

Acceptance candidate (immutable): `e00c92271e788b78a9460e6daa39d3120b7ca58b` on `main`, already public at `origin/main`. You audit this exact SHA; you do not mutate it.

Exact baseline: e00c92271e788b78a9460e6daa39d3120b7ca58b
Expected branch: main
Repository identity: https://github.com/cisarik/libretiles
Working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Repository gate before work: HEAD equals the candidate SHA; branch main; tracked porcelain empty; ./.ap/ap doctor PASS. If any gate fails, stop and report BLOCKED before any probe.

Independence statement: you are a fresh session that did not materially implement any slice of this candidate. Your evidence is the only independent evidence in this whole.

Audit scope (verify claims against code/tests/docs, then produce your own evidence):
1. **Cap enforcement** — fallback queue caps at three distinct pairs (`frontend/src/lib/ai-fallback.ts`); Play retries share one whole-turn provider-call budget and terminal SSE metadata carries `provider_requests_used` (`frontend/src/lib/ai-move-stream.ts`, `frontend/src/app/api/ai/move/route.ts`); Judge performs at most three sequential attempts with per-attempt timeout 10 s, overall budget 30 s, SDK `maxRetries: 0`, HTTP 503 on exhaustion, and never synthesizes false invalid verdicts (`frontend/src/app/api/ai/judge/route.ts`).
2. **Free-only negative cases** — eligibility normalization rejects paid, malformed, non-text, other-provider, and `openrouter/free` rows; missing/future timestamps rank after dated rows with deterministic ties; NIM tuple untouched by OpenRouter sync and ranked last without a discovery call (`backend/catalog/selection.py`, `backend/catalog/openrouter_sync.py`); frontend fails closed on unknown providers/pairs and repairs stale preferences (`frontend/src/lib/model-catalog.ts`).
3. **Flag semantics and kill switches** — flag off returns exactly the curated bootstrap pairs; flag on yields newest-four-plus-NIM deterministically; neither `seed_models` nor sync may reactivate or deactivate existing Admin-controlled rows; default sync aborts with zero writes on empty or >50% cohort drops, CLI-only `--allow-large-drop` (`backend/catalog/management/commands/seed_models.py`, `backend/catalog/management/commands/sync_openrouter_models.py`, `DYNAMIC_FREE_MODEL_CATALOG_ENABLED` default false in `backend/config/settings.py`).
4. **Migration/rollback behavior** — migration 0009 forward/back preserves killed curated/NIM rows and game FKs; migration 0010 refreshes ONLY SHA-256-hash-matched seeded prompt rows, never Admin-customized rows, reverse restores exactly the updated texts (`backend/catalog/migrations/0009_dynamic_free_catalog.py`, `backend/catalog/migrations/0010_refresh_seeded_prompts.py` and their tests). You may probe forward/back on a disposable local SQLite database.
5. **Collins authority intact** — persisted-move validation still flows through `_word_passes_dictionary()` + Collins 2019 (`backend/game/services.py`); AI overlay candidates may be invalid but never persist without the backend verdict.
6. **Documentation exactness** — spot-check at least five factual doc claims added in `e00c922` (AGENTS.md, README.md, docs/architecture.md, env examples) against source; schedule documented-not-configured; rollback story matches flag reality.
7. **Gate re-run (your own evidence)** — full backend pytest; `ruff check .`; mypy `config game gamecore accounts catalog` compared to recorded baseline 63 errors / 17 files (report exact count; investigate any NEW error); frontend `npx vitest run`, `npm run lint`, `npx tsc --noEmit`, `npm run build`.

Pre-declared residuals — do NOT rediscover as findings (verify they remain as stated, nothing more): mypy baseline noise (django-stubs/channels typing); `selection.py` comment referencing deleted `free-rivals.ts` (parked ledger candidate for a future one-line correction); DB prompt presets duplicate prompts.ts strings by design (snapshot semantics); host schedule intentionally unconfigured (separate production authority); flag intentionally default false until rollout.

Exact boundaries:
Positive: read anything in the repository and meta archive; run the permitted commands below; create/destroy ONLY a disposable local SQLite database inside backend/ for migration probes (gitignored); ordinary test/lint/build invocations.
Negative: ZERO repository file edits; no commits, no push, no force ops; no code fixes (findings are reported, never repaired); no live OpenRouter/NVIDIA HTTP of any kind including unauthenticated catalog GETs; no dev/prod servers started beyond what pytest needs; no Redis; never read or print frontend/.env.local or backend/.env; no deployment; do not close any logical whole — closure belongs to the Orchestrator after Cooperator decisions; browser use NOT authorized (Cooperator-rendered UI checks are a separate human activity).

Environment facts (mandatory):
- Wrap every Poetry/Python invocation as: env -u APPIMAGE -u ARGV0 -u APPDIR ... using backend/.venv CPython 3.12.
- Backend: cd backend && env -u APPIMAGE -u APPDIR -u ARGV0 poetry run pytest [args] / ruff check . / mypy config game gamecore accounts catalog.
- Frontend: npx vitest run, npm run lint, npx tsc --noEmit, npm run build (from frontend/).
- Redis not required; Channels connection-refused noise expected.

Commands allowed: git status/log/show/diff/rev-parse/ls-remote, ./.ap/ap doctor, poetry run pytest/ruff/mypy (wrapped), npx vitest run, npm run lint, npm run build, npx tsc --noEmit, python manage.py migrate against disposable SQLite. Forbidden: everything else that mutates the repository or contacts external services.

Validation ladder: broad-or-full suites ARE required here because this is the independent acceptance gate for an E2 cross-layer whole; run each once, diagnose failures narrowly, never rerun an unchanged failing broad gate without a named hypothesis.

Stopping conditions: repository gate failure; any need to mutate tracked state; pressure to fix findings yourself; temptation to call live providers; second acceptance cycle (you produce ONE terminal report); any secret exposure.

Communication routing:
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Required report header: ### Report for ORCHESTRATOR_CHAT

Terminal report contract: status PASS | PARTIAL | BLOCKED; phase-qualified result (acceptance-complete | acceptance-partial | acceptance-blocked); start=end commit (the candidate); changed files: none tracked (report disposable-DB usage); gate re-run table with exact counts (pytest, ruff, mypy vs baseline, vitest, lint, tsc, build); numbered findings list — each finding states file/line claim vs observed truth and whether it blocks PASS; confirmation each pre-declared residual remains as declared; deviations; risks; missing evidence; smallest next step (expected: Orchestrator routes at most one smallest coherent correction per concrete finding, or proceeds to Cooperator-rendered UI checks and closure evaluation); exactly one report justification; authority expiry; Logical-whole closure: not-closed.

Do not repair. Do not close wholes A/B/C/D. Do not push.
