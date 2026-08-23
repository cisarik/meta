### Report for ORCHESTRATOR_CHAT
Logical whole identity: free-openrouter-rival
Worker session ordinal: 01
Worker exchange ordinal: 01
- status: PASS
- phase-qualified result: planning-complete
- start commit: 805bc4c350629508d6800ed7d975eae3c8cf88ae
- end commit: 805bc4c350629508d6800ed7d975eae3c8cf88ae
- changed files: none
- tests and validation: inspection only; tests, builds, migrations, and application processes were not run
- commit and push result: not authorized
- repository evidence: clean main; local and public main equal the baseline; .ap and .gitmodules absent; AP sibling and public AP main equal 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Capability handshake:
Capability	Requested	Observed
Product/client and model	Codex Worker; GPT-5 family	Codex workspace observed; exact deployed model not observably exposed
Reasoning and context	High reasoning	Effective setting and numerical context telemetry unknown; qualitative pressure manageable
Native planning / permission	Plan Mode required	Plan Mode directly observed; unrestricted technical filesystem permission did not expand read-only authority
Filesystem	Repository inspection; no writes	Source readable; technical write capability unused
Network	One public OpenRouter GET and optional Git remote reads	Both succeeded
Source inspection/editing	Inspection required; editing prohibited	Inspection succeeded; no editing attempted
Tests	Not run in this exchange	Shell capability exists; test execution withheld by authority
Commit/push	Read-only Git	Git reads succeeded; commit and push not authorized or probed
Browser/provider inference	Browser none; one catalog GET only	No browser, authenticated request, secret access, or model inference call


Capability does not grant authority.
Provider accounting:
- Provider call authority: authorized for one unauthenticated GET to https://openrouter.ai/api/v1/models
- Numerical call cap: 1 because rate-limit
- Unlimited call authority: no
- Concurrency: single-call-in-flight
- Terminal outcome before next call: required
- Task scope: current free/tool-capable model-catalog evidence
- Bounded time window: one completed request on 2026-08-23
- Subject identity: public OpenRouter model catalog
- Evidence source: successful HTTP response filtered locally with jq
- Evidence freshness: current for this planning exchange
- Reconciliation status: fully-reconciled
- Actual external provider invocations: 1, total
- Retry attempts: 0, subset of invocations
- Defect-driven duplicates: 0, subset of invocations
- Retry/duplicate overlap: 0
- Terminal outcomes: completed=1 failed=0 refused=0 cancelled=0, one-to-one with invocations
- In-flight invocations: 0
- Unresolved invocations: 0
- UI submissions, durable rows, analysis rows, security events, and canonical saves: not applicable; this was a read-only planning request
- Count divergence: none
- Accounting authority effect: none
Deviations: none.
Missing evidence: no live model/tool-call behavior, browser happy path, installed-environment validation, database contents, or deployment evidence was authorized. OpenRouter advertising tools does not prove reliable validateMove invocation.
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
Risks and missing evidence: free-model tool reliability, actual local dependency health, existing database value distribution, browser behavior, and live OpenRouter rate/auth behavior remain unverified.
Smallest next step for the Orchestrator: accept this plan and issue the fresh AP-pin implementation grant to Worker session 02, exchange 01.
Report justification: new-evidence
Planning authority expires when this terminal report is submitted.
Logical-whole closure: not-closed

# OpenRouter-Only Free Rival Implementation Plan

## Summary and verified current state

The implementation will remain sequential and non-deployable until all slices pass integrated validation.

Verified repository findings:

- `frontend/src/lib/ai-gateway.ts` currently routes among Vercel AI Gateway, direct OpenAI, and LM Studio, with `openai/gpt-5.4` as its default.
- The AI move route contains Gateway-to-OpenAI fallback, LM Studio load/unload and compact-prompt paths, local opening fallback words, and a user-credit gate. The game page independently repeats the empty-credit gate and sends LM Studio settings.
- The judge route uses the same multi-provider helper.
- Django currently stores `gateway_managed`, `gateway_available`, provider, type, tags, pricing, quality tier, and legacy per-game cost. Its sync source is Vercel AI Gateway.
- Selection ranks up to 20 models by descending token cost, pins GPT-5.4, and specially admits arbitrary `lmstudio/*` IDs.
- Seeding creates paid OpenAI/Anthropic/Google entries and two LM Studio entries.
- Settings is a 1,445-line provider-aware table with LM Studio discovery/runtime controls, provider icons for LM Studio/OpenAI/Google/Anthropic/OpenRouter/Novita/xAI, price and quality presentation, and an unfinished top-up surface.
- `@ai-sdk/google` is installed but unused. No direct Anthropic SDK is installed.
- OpenRouter is not a runtime provider today; its live frontend presence is only a provider icon. Novita and xAI are dead icon surfaces. Historical migration `0001_initial.py` also contains provider choices and must remain untouched.
- Billing already yields zero when both token pricing and legacy cost are zero, but frontend credit checks prevent every non-LM cloud model from playing at a zero balance.
- Model defaults are duplicated across backend selection, frontend provider code, the move route, Zustand, environment examples, and documentation.
- Existing tests encode the Gateway, paid-model, pinned-GPT, and dynamic-LM behavior and therefore require causal replacement.
- AP is not yet integrated.

## Target architecture and interfaces

### Runtime and SDK choice

- Keep `ai@6` and `@ai-sdk/openai@3.x`.
- Use `createOpenAI({ baseURL: "https://openrouter.ai/api/v1", apiKey: process.env.OPENROUTER_API_KEY, name: "openrouter" })`, with `.chat(modelId)`.
- This retains the already-compatible AI SDK v6 tool-calling path, adds no provider package, and avoids an AI SDK v7 migration.
- `@ai-sdk/openai` becomes only an OpenAI-compatible protocol adapter; direct OpenAI requests and `OPENAI_API_KEY` disappear.
- `@ai-sdk/gateway` may remain transitively in `package-lock.json` through `ai@6`; there must be no direct import, configuration, or Vercel Gateway runtime use.
- Hardcode OpenRouter’s API base URL. The only AI credential is the server-only `OPENROUTER_API_KEY`.
- Use OpenRouter-native IDs unchanged, such as `google/gemma-4-31b-it:free`. Never add an extra `openrouter/` prefix.

### Recommended free rival list

The 2026-08-23 public catalog returned 422 models, of which 19 had zero prompt/completion price and advertised `tools`. The application will apply the stricter requirements of an explicit `:free` ID, explicit zero input/output pricing, advertised tools, text output, and membership in this ordered shortlist:

1. `google/gemma-4-31b-it:free` — recommended default; the catalog advertises native function calling, a 262,144-token context, and a 32,768-token completion ceiling.
2. `nvidia/nemotron-3-super-120b-a12b:free` — larger agentic alternate with tools and 262,144-token context.
3. `z-ai/glm-5.2:free` — reasoning/agent-workflow alternate with tools and 256,000-token context.
4. `google/gemma-4-26b-a4b-it:free` — lighter Gemma fallback with the same advertised context and tool support.

The recommendation is new planning advice, not an already accepted Cooperator decision. `openrouter/free` is excluded because its random routing weakens reproducibility and model auditability. Zero-priced IDs without an explicit `:free` suffix are also excluded.

If the recommended default is no longer eligible when implementation starts, promote the first still-eligible alternate in the order above and update every default consistently. Stop if fewer than two listed rivals remain eligible.

### Catalog and selection

- Rename internal fields to `openrouter_managed` and `openrouter_available`; do not edit historical migrations.
- Store `provider="openrouter"` for newly synced rows. The model author remains visible in the native ID.
- Normalize OpenRouter `pricing.prompt` and `pricing.completion` into the existing internal `input` and `output` keys; retain cache price keys where supplied.
- Store `supported_parameters` in the existing `tags` JSON, and treat only `tools` as tool capability.
- Sync only explicit free, zero-priced, text-output, tool-capable records. Do not create or refresh paid rows in this cut.
- Newly discovered eligible models outside the four-ID shortlist remain inactive. The public selection predicate requires shortlist membership, active state, availability, explicit free pricing, and tools.
- Preserve existing paid and non-OpenRouter rows for historical foreign keys, but make them selection-ineligible. Do not delete them.
- Replace `PINNED_MODEL_ID` with `DEFAULT_FREE_MODEL_ID`. Public ordering is the curated order, not price.
- `GET /api/catalog/models/` keeps its response shape for compatibility, but returns at most the four eligible rivals. Pricing and `cost_per_game` are zero; `is_flagship` identifies the recommended default.
- Replace `sync_gateway_models` with `sync_openrouter_models`. Remove `--activate-new`; code owns shortlist activation.

Recommendation adopted as the plan default: do not newly sync paid OpenRouter models. Existing paid rows remain dormant for historical compatibility.

### Billing and API behavior

- Remove both frontend empty-credit gates and the `insufficient_user_credit` error path.
- Exact curated free model IDs always charge zero, create no `Transaction`, and do not change `CreditBalance` or `GameSession.total_cost_usd`, even when token usage is present.
- Keep billing models, historical paid rows, profile/header balance readouts, and the billing endpoint dormant for compatibility. Stripe and paid-model enablement remain separate work.
- Remove the Settings balance/top-up panel because it is misleading in a free-only rival picker; do not implement checkout.
- `/api/ai/move` stops accepting or emitting LM Studio runtime fields. `provider_path` is always `openrouter`; Gateway-fallback metadata disappears.
- Replace provider errors with `provider_auth_failed`, `provider_rate_limited`, and `provider_unavailable`. Messages direct users to another free rival or a later retry, never to app-credit top-up.
- Keep backend move validation and final re-validation unchanged.

### Settings and client-state migration

- Replace the collapsible provider/price table with an always-visible responsive list or card grid of the short catalog response.
- Each entry shows name, description, context, a Free badge, and selected state. No provider icon map, quality tier, token-price bar, LM Studio status, context controls, or reload controls.
- Keep thinking time, search steps, board theme, shine, and premium-look settings unchanged.
- Version the Zustand persisted store. Remove LM Studio keys and remap any model outside the four-ID list to the recommended default.
- On login, Settings load, and Play entry, reconcile stored/account preference against the returned catalog. Select the first eligible rival and PATCH the stale non-empty `preferred_ai_model_id`.
- Preserve all old `AIModel` rows, so finished and abandoned `GameSession.ai_model` foreign keys remain valid. An active legacy AI game is switched through the existing model PATCH before its next AI turn.
- Blank preferences remain “no explicit choice” until normal reconciliation.

## Ordered implementation slices

### 1. Minimum AP integration

- Changed-path allowlist: `.gitmodules`, `.ap` gitlink, `AGENTS.md`.
- Positive authority: start from the exact clean baseline; run `git submodule add https://github.com/cisarik/ap.git .ap`, `./.ap/ap init`, and `./.ap/ap doctor`; review `.gitmodules`, the gitlink, and the managed `AGENTS.md` block.
- Negative authority: no FrameNest NUC, worker-execution contract, `ap.project.conf`, upgrade ledger, copied universal AP files, or edits inside `.ap`.
- Git write: yes—stage exactly the three integration paths and create one reviewable commit, recommended subject `docs: adopt analytic programming`; no push without separate authority.
- Validation: `./.ap/ap doctor`, `git diff -- .gitmodules AGENTS.md`, `git diff --submodule`, `git diff --check`, final clean status.
- Evidence tier: E1.
- Suggested Worker target: fresh worker; next implementation session, exchange 01.
- Stop condition: baseline/cleanliness/identity failure, AP sibling mismatch, unexpected generated files, or doctor failure.

### 2. Local development bootstrap preflight

- Changed-path allowlist: no tracked files. Reversible local state only under `backend/.venv/`, `backend/.env`, `backend/db.sqlite3`, `frontend/node_modules/`, `frontend/.env.local`, `frontend/.next/`, and project cache directories.
- Positive authority: initialize the submodule, create the Python 3.12 environment, install locked Poetry/npm dependencies, copy example env files only when absent, migrate SQLite, seed models, and establish baseline test/build results.
- Commands for the future Worker: `git submodule update --init --recursive`; `./.ap/ap doctor`; backend venv plus `poetry install`; `manage.py migrate`; `manage.py seed_models`; focused pytest; frontend `npm ci`, lint, and build.
- Negative authority: do not overwrite existing env files, print env contents, acquire provider keys, call an AI provider, start persistent app processes, alter lockfiles, or repair unrelated failures.
- Git write: no.
- Validation: package manifests and locks remain unchanged; record exact runtime versions and focused baseline failures.
- Evidence tier: E1.
- Suggested Worker target: current worker after a complete renewed grant from Slice 1.
- Stop condition: missing supported runtime/toolchain, unexpected lockfile change, unexplained test failure, or secret requirement.

### 3. OpenRouter-only runtime

- Changed-path allowlist:
  - `frontend/src/lib/openrouter.ts` (new)
  - `frontend/src/lib/free-rivals.ts` (new)
  - `frontend/src/app/api/ai/move/route.ts`
  - `frontend/src/app/api/ai/judge/route.ts`
  - `frontend/src/app/game/[id]/page.tsx`
- Positive authority: introduce one OpenRouter client, native-ID validation, one default/list definition, remove Gateway/direct-OpenAI/LM runtime branches, remove credit blocking, simplify provider metadata, and update provider error handling.
- Negative authority: no live inference, secret access, prompt-strength work, SDK v7 upgrade, new provider dependency, backend catalog changes, browser work, or deployment.
- Git write: yes—one local commit limited to the allowlist; no push.
- Validation: frontend lint, TypeScript/build, and static inspection that all AI generation uses the OpenRouter client.
- Evidence tier: E2.
- Suggested Worker target: fresh worker because the runtime/provider boundary changes materially.
- Stop condition: tool calling cannot compile on AI SDK v6, a v7 bump appears necessary, OpenRouter-native IDs require rewriting, or validation would need a secret/live call.

### 4. Free catalog, migration, selection, and zero billing

- Changed-path allowlist:
  - `backend/catalog/models.py`
  - `backend/catalog/selection.py`
  - `backend/catalog/openrouter_sync.py` (new)
  - `backend/catalog/gateway_sync.py` (delete)
  - `backend/catalog/admin.py`
  - `backend/catalog/serializers.py`
  - `backend/catalog/management/commands/seed_models.py`
  - `backend/catalog/management/commands/sync_openrouter_models.py` (new)
  - `backend/catalog/management/commands/sync_gateway_models.py` (delete)
  - `backend/catalog/templates/admin/catalog/aimodel/change_list.html`
  - `backend/catalog/templates/admin/catalog/aimodel/sync_models.html`
  - `backend/catalog/migrations/0006_openrouter_catalog.py` (new)
  - `backend/accounts/models.py`
  - `backend/accounts/migrations/0002_openrouter_preference_help.py` (new)
  - `backend/game/services.py`
  - `backend/billing/services.py`
  - `backend/tests/test_api.py`
  - `backend/tests/test_openrouter_catalog_migration.py` (new)
- Positive authority:
  - Rename Gateway fields/help text without editing migration history.
  - Make seed idempotently create/update only the four curated zero-cost rows and remove the destructive `--reset` option.
  - Normalize and sync only explicit free/tool/text OpenRouter records.
  - Deactivate missing managed records and prevent every paid, non-tool, non-shortlisted, unavailable, LM, or other-provider ID from selection.
  - Remove dynamic LM model creation from game services.
  - Add the explicit free-model billing guard.
  - Reset new OpenRouter availability/management flags for legacy rows while retaining rows and foreign keys.
- Negative authority: no row deletion, no paid activation, no provider key, no authenticated call, no production migration, no game-rule/prompt/multiplayer changes, and no edits to migrations `0001`–`0005`.
- Git write: yes—one local migration/catalog commit; no push.
- Validation: migration state check, focused catalog/game/billing tests, migration regression, ruff, mypy, and mocked sync-command tests.
- Evidence tier: E2.
- Suggested Worker target: fresh worker because this is a database and backend-policy boundary.
- Stop condition: source metadata lacks explicit zero/tool evidence, fewer than two shortlisted models remain eligible, migration would require deleting referenced rows, or paid/LM IDs remain API-selectable.

### 5. Simplified free-rival Settings UX

- Changed-path allowlist:
  - `frontend/src/app/settings/page.tsx`
  - `frontend/src/app/page.tsx`
  - `frontend/src/app/play/page.tsx`
- Positive authority: render the short free-only card/list picker, remove provider/price/quality/local-runtime/top-up surfaces, preserve unrelated visual settings, and reconcile stale local/account choices against the catalog.
- Negative authority: no redesign of game chrome, profile billing, prompts, multiplayer, board behavior, Stripe, provider runtime, or catalog schema.
- Git write: yes—one local UI commit; no push.
- Validation: frontend lint/build; empty, loading, selected, stale-preference, and four-model states inspected statically.
- Evidence tier: E2.
- Suggested Worker target: fresh UI-focused worker after the accepted runtime/catalog commits.
- Stop condition: the UI can expose an ID absent from the backend response, account reconciliation would silently select paid/non-tool entries, or unrelated settings regress.

### 6. Delete LM Studio and other-provider leftovers

- Changed-path allowlist:
  - `frontend/src/lib/ai-gateway.ts` (delete)
  - `frontend/src/lib/local-ai.ts` (delete)
  - `frontend/src/lib/lm-studio.ts` (delete)
  - `frontend/src/app/api/ai/local/status/route.ts` (delete)
  - `frontend/src/lib/prompts.ts`
  - `frontend/src/hooks/useGameStore.ts`
  - `frontend/package.json`
  - `frontend/package-lock.json`
- Positive authority: remove local-only prompt helpers, persisted LM settings, stale provider files/routes, and the unused direct `@ai-sdk/google` dependency; add the Zustand versioned migration.
- Negative authority: retain `@ai-sdk/openai` as the OpenRouter compatibility client; do not remove AI SDK’s transitive Gateway package, add `@openrouter/ai-sdk-provider`, bump AI SDK, or introduce a new Local mode.
- Git write: yes—one local subtractive cleanup commit; no push.
- Validation: `npm ci`, lint/build, dependency-tree inspection, and live-source search proving no LM Studio imports/routes or direct Google/Anthropic SDK dependency.
- Evidence tier: E2.
- Suggested Worker target: current worker from Slice 5 under renewed authority.
- Stop condition: any remaining in-scope import depends on deleted modules, lockfile changes exceed dependency removal, or cleanup would require unrelated refactoring.

### 7. Environment, bootstrap scripts, and documentation

- Changed-path allowlist:
  - `AGENTS.md`
  - `README.md`
  - `CONTRIBUTING.md`
  - `docs/architecture.md`
  - `libretiles_PRD.md`
  - `frontend/README.md`
  - `frontend/.env.local.example`
  - `backend/.env.example`
  - `backend/pyproject.toml`
  - `scripts/start-frontend.sh`
  - `scripts/start-backend.sh`
  - `scripts/libretiles.sh`
- Positive authority:
  - Document `OPENROUTER_API_KEY`, native IDs, the default/alternates, `sync_openrouter_models`, free-zero billing, and AI-only local boot without Redis.
  - Make startup scripts seed the offline shortlist and warn when the OpenRouter key must be supplied.
  - Keep sync optional during boot so an unavailable public catalog does not block local startup.
  - Update only provider/settings/testing claims in the stale PRD.
- Negative authority: preserve the AP-managed block, never include a real key, do not add deployment/publication/Stripe/NUC instructions, and do not rewrite unrelated product history.
- Git write: yes—one local docs/bootstrap commit; no push.
- Validation: `bash -n` on touched scripts, link/path inspection, `git diff --check`, and provider-term search outside immutable migrations and lockfile transitive metadata.
- Evidence tier: E1.
- Suggested Worker target: current integration worker under renewed authority.
- Stop condition: documentation would require a real secret, a startup change overwrites user env files, or scope expands into deployment/billing/public launch.

### 8. Integrated validation and fresh acceptance

- Changed-path allowlist: none; read-only inspection and generated caches/test databases only.
- Positive authority:
  - Run `./.ap/ap doctor`.
  - Backend: `makemigrations --check --dry-run`, ruff, project-scoped mypy, focused catalog/API/migration/dictionary tests, then the full pytest suite once.
  - Frontend: `npm ci`, lint, `tsc --noEmit`, and production build.
  - Inspect final diff, commit ordering, migration reversibility, seed idempotence, and negative provider searches.
- Negative authority: no correction, live OpenRouter inference, browser account access, secrets, deployment, push, or publication. A finding requires a separately authorized bounded correction.
- Git write: no.
- Validation acceptance:
  - API returns only the ordered free/tool shortlist.
  - Paid, malformed, non-tool, LM, Novita, xAI, direct-provider, and unavailable IDs are rejected for profile update, game creation, and in-game switching.
  - Free usage at a zero app balance charges exactly zero and creates no billing transaction.
  - Legacy model rows and completed-game foreign keys survive migration.
  - Existing `backend/tests/test_api.py` and `backend/tests/test_dictionary_validation.py` remain passing.
  - No frontend test framework is added; lint/build are the automated frontend gates.
- Evidence tier: E2.
- Suggested Worker target: fresh worker for independent acceptance of the integrated candidate.
- Stop condition: any selected model is not explicitly free/tool-capable, a broad gate fails, migration loses history, or required evidence would need an unauthorized provider/browser call.

## Acceptance, rollback, risks, and assumptions

Later browser/provider acceptance, under a separate credential- and call-bounded grant, is one happy path only: register, open Settings, select a free rival, create an AI game, and complete one AI turn. The backend must remain the final move validator. This plan does not execute that flow.

Rollback:

- Do not deploy intermediate commits.
- Before any production migration, take a database checkpoint under a separate deployment preflight.
- Source rollback is commit-by-commit in reverse order.
- Schema rollback returns the renamed catalog fields to their prior names; old model rows were never deleted.
- Exact rollback after users resume games or preferences are lazily reconciled uses the database checkpoint, because those normal application writes can change selected model IDs.
- Local development databases may instead be recreated from migrations and seeds.
- AP removal, if the whole is abandoned, is a separate explicit revert of the AP integration commit.

Key risks and controls:

- Tool advertisement may not equal reliable function calling: retain backend validation, deterministic alternates, and explicit live acceptance.
- Free catalog churn or pricing change: require `:free`, explicit zero pricing, tools, shortlist membership, and availability on every sync.
- Rate limits and free-capacity exhaustion: structured retry/switch messaging; never charge app credits.
- Secret leakage: empty/example-only `OPENROUTER_API_KEY`; server-side access only; never print env files.
- Accidental paid exposure: paid records are not newly synced and cannot pass the selection predicate even if manually marked active.
- Legacy data: preserve model rows/FKs; migrate choices lazily and use a database checkpoint for exact operational rollback.
- Transitive package naming: `@ai-sdk/gateway` in the lockfile is acceptable only as an unused `ai@6` transitive dependency.
- Scope creep: stop on requests for stronger AI research, public launch, Stripe, multiplayer changes, Local mode, AP extras, or deployment.

Explicit non-goals:

- Unbeatable-opponent research, prompt search, candidate generation, or model-quality campaign.
- Public publication, deployment, or play by strangers.
- Stripe, top-up completion, paid rivals, or general billing redesign.
- Multiplayer behavior changes.
- Reintroducing LM Studio or another Local mode.
- AI SDK v7 migration.
- FrameNest NUC, worker-execution envelope, `ap.project.conf`, upgrade ledger, or other AP extras.
- Browser/live-provider execution in this planning exchange.

Assumptions/defaults:

- The dated OpenRouter catalog evidence is planning evidence, not guaranteed future availability.
- The recommended four-model order and no-paid-sync policy are adopted unless the Orchestrator explicitly rejects them.
- Existing public catalog response fields remain compatible even though Settings stops displaying price and quality.
- Historical migrations and Git history retain old provider text; current runtime/source/docs are the cleanup boundary.
- Implementation, commits, pushes, provider calls, acceptance, publication, deployment, and closure each require their own later authority.
