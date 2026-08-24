# NVIDIA NIM and Bounded Free-Rival Fallback

## Summary

Add NVIDIA NIM as a second server-side runtime alongside OpenRouter while retaining Django Admin as the catalog authority and charging zero app credits. Seed the exact NIM chat model `nvidia/nemotron-3-super-120b-a12b`; do not use FrameNest’s Omni/VLM model.

The user’s selected rival remains their persistent preference. Fallback models are per-turn runtime attempts only. One AI turn may open at most three sequential `/api/ai/move` SSE streams, under one overall timeout, and stops at the first backend-persisted place, pass, or exchange.

## Verified Current State

- `AIModel` remains fully available through Django Admin, with provider, model ID, tools/pricing metadata, activation, ordering, and OpenRouter-specific sync fields.
- Backend selection currently exposes exactly four curated OpenRouter rows and requires `provider="openrouter"`.
- Settings renders those API rows but describes them as OpenRouter-only.
- `/api/ai/move` and `/api/ai/judge` always instantiate `getOpenRouterModel()`.
- `normalizeRouteError()` inspects only the outer message. AI SDK `RetryError` stores the actionable `429` on `lastError`/`errors`, so the observed OpenRouter failure becomes a generic SSE error.
- The game page understands coded provider errors but performs no automatic fallback.
- All current AI-turn billing paths resolve to zero app credits.

## Interfaces and Architecture

- Define one ordered provider/model registry:

  1. `openrouter` — `google/gemma-4-31b-it:free` (unchanged default)
  2. `nvidia-nim` — `nvidia/nemotron-3-super-120b-a12b`
  3. `openrouter` — `nvidia/nemotron-3-super-120b-a12b:free`
  4. `openrouter` — `z-ai/glm-5.2:free`
  5. `openrouter` — `google/gemma-4-26b-a4b-it:free`

- Catalog eligibility must require the exact curated `(provider, model_id)` pair, `is_active`, `model_type="language"`, a `tools` tag, `cost_per_game=0`, and explicit zero `pricing.input` and `pricing.output`. Missing prices are not treated as zero.
- Retain `openrouter_managed` and `openrouter_available` exclusively as OpenRouter-sync metadata. The NIM seed row sets both false. Do not add a NIM catalog sync or generic discovery mechanism.
- Add only provider-neutral help-text migrations; do not delete, re-key, or replace catalog rows or game foreign keys.
- Add `frontend/src/lib/nvidia-nim.ts` using `@ai-sdk/openai`, `.chat(modelId)`, server-only `NVIDIA_API_KEY`, provider name `nvidia-nim`, and hardcoded base URL `https://integrate.api.nvidia.com/v1`.
- Add a provider registry returning the appropriate `LanguageModel` for an eligible provider/model pair. `/api/ai/judge` uses this dispatch for one model but receives no fallback loop.
- Extend `/api/ai/move` input with optional `runtime_model_id`. Existing `model_id` keeps its meaning as the selected/persisted rival; `runtime_model_id` identifies only the current attempt and defaults to `model_id`.
- Before inference, `/api/ai/move` reads the backend catalog and independently validates the runtime pair. It updates the game’s selected model only when `model_id` differs from the session model; fallback IDs never replace the preference.
- All SSE thinking, error, and done terminals identify `provider_path` and `runtime_model`. A `done` event is legal only after an `ok: true` backend place/pass/exchange response.
- Error normalization traverses bounded, cycle-safe `lastError`, `errors`, and `cause` structures and direct `statusCode` values. Nested 401 maps to `provider_auth_failed`; 429 to `provider_rate_limited`; 402/502/503/504, overload, and known unsupported-tool responses to `provider_unavailable`. Raw provider bodies, headers, and keys never enter SSE errors.

## Ordered Implementation Slices

### Slice 1 — Provider-neutral catalog and zero-credit eligibility

Git subject: `feat: add NVIDIA NIM to the free rival catalog`

Changed-path allowlist:

- `backend/catalog/models.py`
- `backend/catalog/selection.py`
- `backend/catalog/openrouter_sync.py`
- `backend/catalog/management/commands/seed_models.py`
- `backend/catalog/migrations/0007_provider_neutral_model_help.py`
- `backend/accounts/models.py`
- `backend/accounts/migrations/0003_provider_neutral_ai_model_help.py`
- `backend/billing/services.py`
- `backend/tests/test_api.py`
- `backend/tests/test_openrouter_catalog_migration.py`

Implement the five-entry pair registry, strict free predicate, NIM seed row, provider-neutral model/preference help text, and pair-aware zero-credit classification. Preserve paid and legacy Admin rows as dormant data. Confirm OpenRouter sync cannot update or disable the NIM row.

Validation:

- Migration checks and forward/reverse help-text migration tests.
- Catalog ordering/provider tests and negative tests for wrong provider, inactive, non-language, missing/nonzero pricing, and missing tools.
- Seed idempotency, NIM game/preference selection, OpenRouter-sync isolation, and zero-balance/zero-transaction billing tests.
- `ruff`, `mypy`, targeted pytest, then full backend pytest.

Stop if a migration would delete/re-key existing models, alter game foreign keys, activate paid rows, or make OpenRouter sync own NIM rows.

### Slice 2 — NIM runtime and correct provider failures

Git subject: `feat: add the NVIDIA NIM AI runtime`

Changed-path allowlist:

- `frontend/package.json`
- `frontend/package-lock.json`
- `frontend/src/lib/openrouter.ts`
- `frontend/src/lib/nvidia-nim.ts`
- `frontend/src/lib/ai-runtimes.ts`
- `frontend/src/lib/ai-runtimes.test.ts`
- `frontend/src/lib/free-rivals.ts`
- `frontend/src/app/api/ai/move/route.ts`
- `frontend/src/app/api/ai/judge/route.ts`
- `frontend/.env.local.example`

Add Vitest as a test-only dependency. Implement runtime dispatch, catalog revalidation, `runtime_model_id`, sanitized provider metadata, legal-terminal checks, and nested RetryError classification. Keep AI SDK v6 and `.chat()`; add no provider SDK and no configurable base URL.

Validation:

- Unit tests for both runtime mappings, missing-key sanitization, wrong provider/model rejection, nested/direct 401/429/503 cases, unknown errors, and no secret/raw-body disclosure.
- Mocked route tests proving failed pass/exchange responses never emit `done`.
- `npm run test`, `npm run lint`, and `npm run build`.

Stop if the exact NIM model cannot compile through the existing Chat Completions tool interface, requires a Responses/VLM adapter, or would expose `NVIDIA_API_KEY`.

### Slice 3 — One-turn, three-model fallback

Git subject: `feat: retry AI turns across free rivals`

Changed-path allowlist:

- `frontend/src/lib/ai-fallback.ts`
- `frontend/src/lib/ai-fallback.test.ts`
- `frontend/src/lib/ai-move-stream.ts`
- `frontend/src/lib/ai-move-stream.test.ts`
- `frontend/src/app/game/[id]/page.tsx`
- `frontend/src/app/settings/page.tsx`
- `frontend/src/app/play/page.tsx`

Extract the SSE consumer into a terminal-result API. At AI-turn start, fetch the selectable catalog and build a maximum-three queue:

1. selected eligible model;
2. first eligible model from a provider not yet tried;
3. another previously unseen provider if available, otherwise the next catalog model.

Use one overall `aiTimeout` deadline. Pass the remaining whole-turn seconds to each stream and do not begin another attempt with less than the route’s 15-second minimum. `aiMaxSteps` remains per attempt; existing bounded AI SDK internal retries remain unchanged.

Retry only after a coded provider error. Before every retry, fetch current Django game state and require the same game, unchanged `move_count`, active status, AI still owning the turn, and no game-over flag. If state changed or cannot be reconciled, stop without another provider call. Any successful `done` for place/pass/exchange, including pass after timeout or no candidate, ends the sequence. Generic/backend/authentication-token failures do not trigger provider fallback.

Keep the selected preference unchanged. Show attempt/provider progress during fallback; show the blocker modal only after the queue, deadline, or catalog eligibility is exhausted. If the browser catalog request fails, permit only the selected model attempt and no speculative static fallback.

Validation:

- Queue ordering, provider diversity, de-duplication, cap-three, empty/single-provider catalogs, and inactive-row exclusion.
- SSE tests proving `done` wins, coded errors remain distinguishable, malformed events do not create terminals, and a lost connection after `done` cannot retry.
- State-reconciliation tests proving a changed move count, changed turn, or game-over state prevents a second stream.
- Missing NIM key, nested OpenRouter 429, all-providers-unavailable, catalog failure, deadline exhaustion, and successful second-model scenarios with mocked provider/backend boundaries.
- `npm run test`, `npm run lint`, and `npm run build`.

Stop if the implementation cannot prove that no action persisted before retrying; introduce no retry until that invariant is testable.

### Slice 4 — Configuration, operations, and durable documentation

Git subject: `chore: document provider-diverse free rivals`

Changed-path allowlist:

- `scripts/libretiles.sh`
- `scripts/start-frontend.sh`
- `scripts/start-backend.sh`
- `backend/.env.example`
- `AGENTS.md`
- `README.md`
- `CONTRIBUTING.md`
- `libretiles_PRD.md`
- `docs/architecture.md`

Document both server-only keys, the hardcoded provider bases, five seeded cards, Admin kill switch, zero app credits, bounded fallback, and the distinction between app credits and changeable external NIM trial/quota terms. Startup scripts warn that AI is unavailable only when neither provider credential is usable; never print credential values.

Validation:

- `bash -n` on modified scripts.
- Search for stale “four OpenRouter rivals,” “OpenRouter only,” and “only AI credential” claims.
- Final backend and frontend quality gates and clean diff/status review.

Stop if documentation suggests permanent free/unlimited NIM service, client-visible keys, Stripe completion, or automatic NIM catalog discovery.

## Acceptance, Rollback, and Risks

A separately authorized live acceptance should seed the catalog, verify five Settings cards and provider badges, play one direct NIM tool-calling turn, then exercise an OpenRouter-429-to-NIM fallback from one Play action. Evidence must show at most three model streams, exactly one persisted legal AI action, Collins 2019 backend validation, unchanged app balance/transactions, and no second game. Provider keys and raw provider responses must remain undisclosed.

Rollback order:

1. Immediately deactivate the NIM row in Django Admin to remove it from Settings and fallback queues.
2. Remove the server’s `NVIDIA_API_KEY` if credential revocation is required.
3. Revert Slices 3, 2, then 1. Help-text migrations are reversible; existing NIM rows become hidden under the old OpenRouter-only predicate and need not be destructively deleted.

Material risks:

- NIM trial quota or terms can change and may also return 429; Admin deactivation is the operational kill switch.
- Publicly advertised tool calling does not prove reliable `validateMove` execution; live acceptance remains required.
- AI SDK retries within each stream can multiply actual provider requests even though model streams are capped at three.
- A lost SSE terminal can otherwise duplicate a turn; mandatory Django-state reconciliation is the shipping gate.
- `NVIDIA_API_KEY` leakage is prevented through server-only naming, sanitized errors, no logging, and no `NEXT_PUBLIC_` exposure.

## Assumptions and Non-goals

- The NVIDIA public model-card evidence is sufficient for planning; permanent free availability is not assumed.
- The default rival remains OpenRouter Gemma. Fallback does not rewrite the game or account preference.
- Collins 2019 English remains authoritative.
- No Stripe, paid catalog tier, app-credit charging, Slovak/multilingual dictionary, prompt/search-strength research, LM Studio, Vercel AI Gateway, FrameNest adapter copy, NIM model discovery, circuit breaker, deployment, push, or second-game fallback is included.
