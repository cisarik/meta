# Newest-first free rival catalog and bounded fallback

Logical whole identity: newest-first-free-fallback  
Worker session ordinal: 01  
Worker exchange ordinal: 01  

Status: PASS  
Phase-qualified result: planning-complete  
Native planning mode: required  
Start commit: `77944d7baf0192ed09b3e6c2876561469d39c101`  
End commit: `77944d7baf0192ed09b3e6c2876561469d39c101`  
Changed files: none  

## Summary and Cooperator decision

Two routes are technically viable:

1. **Curated-only:** retain the five seeded pairs, order eligible members by release metadata, and add shared Play/Judge fallback, UX, and prompt improvements. This is lowest risk but does not satisfy automatic admission of newer models.
2. **Newest cohort — recommended:** expose the four newest verified OpenRouter models plus the separately seeded NVIDIA NIM row, for at most five rivals. Use a backend feature flag to return instantly to curated-only selection.

Recommend Route 2 because it remains bounded by strict eligibility, a fixed cohort size, durable Admin kill switches, runtime catalog revalidation, and a non-destructive rollback. Approval should explicitly select Route 2; otherwise leave the feature flag off and follow Route 1.

## Architecture and interfaces

- Define “newest” as OpenRouter’s `created` timestamp stored in existing `released_at`, descending. Reject implausibly future timestamps; put missing timestamps after dated rows, then use bootstrap `sort_order` and `model_id` as deterministic ties.
- Admit an OpenRouter row only when its native ID ends in `:free`, prompt and completion pricing both parse to zero, tools are advertised, text output is supported, and the row is OpenRouter-managed and currently available. Exclude `openrouter/free` and all paid, malformed, non-text, or other-provider rows.
- Keep four auto-ranked OpenRouter slots. Preserve the exact seeded NIM tuple as the fifth possible row. NIM has no discovery call, is never touched by OpenRouter sync, and ranks last while its `released_at` is unknown.
- Make existing `is_active` the durable Admin kill switch: neither seed nor sync may reactivate or deactivate an existing row. Newly discovered eligible rows start active; unavailable rows retain Admin state but are excluded by availability.
- Add `DYNAMIC_FREE_MODEL_CATALOG_ENABLED`, defaulting false. False returns only bootstrap pairs; true enables the newest-four-plus-NIM policy.
- Change `/api/catalog/models/` to return canonical newest-first order, expose `released_at`, retain money-free fields, and mark only the first row `is_flagship`/recommended.
- A valid explicit preference remains attempt 1; remaining attempts follow untouched catalog order. With no valid preference, catalog row 1 is selected. Play and Judge must call the same queue builder and cap the queue at three distinct pairs.
- Replace the frontend static runtime allowlist with exact backend-catalog validation. OpenRouter accepts only catalog-confirmed `:free` IDs; NIM accepts only its fixed tuple; unknown providers and catalog failures fail closed.
- Keep `/api/ai/move` state-safe: retry only retryable provider failures, only after unchanged-turn reconciliation. Add `provider_requests_used` to terminal SSE metadata and treat `max_steps` as the remaining whole-turn provider-call budget.
- Judge performs up to three sequential attempts using the same queue. Use `maxRetries: 0`, a 10-second timeout per attempt, strict one-result-per-input JSON validation, and HTTP 503 if all attempts fail—never synthesize false “invalid” results from malformed output.
- New users with no server preference receive catalog row 1. Returning valid preferences remain honored; stale preferences are repaired. Remove the hardcoded Zustand default and obsolete `NEXT_PUBLIC_DEFAULT_MODEL` fallback.
- Add structured fallback progress to Zustand. The thinking overlay shows ordered model pills, prior failures, the active attempt, and a purely visual gold/black ping-pong tile. Animation must add no delay, stop with the attempt lifecycle, honor reduced motion, and remain readable without Premium Look.
- Rewrite move prompts around legality-first anchor search, an early validated scoring floor, diverse alternatives only while budget remains, backend validation authority, and no arbitrary candidate-count demand. Rewrite Judge to be Collins-2019-conservative and remove the current natural-usage override.
- Update shipped database prompt presets through a reversible data migration that changes only rows matching known prior-content hashes; preserve Admin-customized prompts. Include the `accounts.User` credit-balance docstring cleanup.

## Ordered implementation slices and allowlists

1. **Catalog safety and reversible selection**
   - Allow: `backend/config/settings.py`, `backend/.env.example`, catalog selection/sync/admin/serializer/view files and templates, both catalog management commands, `backend/catalog/migrations/0009_dynamic_free_catalog.py`, `backend/game/services.py`, `backend/accounts/models.py`, and affected backend tests.
   - Implement strict normalization, deterministic ranking, four-row cap, durable kill-switch behavior, large-drop guard, feature flag, dynamic default, and the compatibility data migration.
   - Default sync must abort without writes when normalized results are empty or fall by more than 50% from the last available cohort. A CLI-only `--allow-large-drop` requires separate operator authority.

2. **Dynamic runtime, shared fallback, and HTTP budgets**
   - Allow: `frontend/src/lib/{free-rivals.ts,model-catalog.ts,ai-runtimes.ts,ai-fallback.ts,ai-move-stream.ts,types.ts}`, home/play/settings pages, both AI routes, game page, store, models proxy, and their existing/new Vitest files.
   - Remove the static frontend ID union, centralize preference resolution, validate exact catalog pairs, and use one shared preference-first/newest-remainder queue.
   - Set AI SDK `maxRetries: 0`. Across normal Play orchestration, total model-step HTTP calls may not exceed the selected 10/20/30/50/80 step budget; fallback attempts share the remainder instead of each receiving a fresh budget.
   - Judge is single-call-in-flight, three calls maximum, and thirty seconds maximum overall.

3. **Fallback presentation and prompts**
   - Allow: `frontend/src/components/game/AIThinkingOverlay.tsx`, `frontend/src/app/game/[id]/page.tsx`, `frontend/src/hooks/useGameStore.ts`, `frontend/src/lib/{premiumSurface.ts,prompts.ts,types.ts}`, `backend/catalog/migrations/0010_refresh_seeded_prompts.py`, and prompt/fallback tests.
   - Add structured attempt progress and the non-blocking ping-pong presentation.
   - Migrate unmodified seeded prompts only; never overwrite an Admin-edited row and never edit historical migration files.

4. **Operations, documentation, and rollout**
   - Allow: `AGENTS.md`, `README.md`, `CONTRIBUTING.md`, `libretiles_PRD.md`, `docs/architecture.md`, `frontend/README.md`, and environment examples.
   - Define the production schedule as `libretiles-openrouter-catalog-refresh`, daily at `03:17 UTC`, invoking `python manage.py sync_openrouter_models` under a non-overlapping platform lock.
   - One scheduled run performs one unauthenticated OpenRouter catalog GET, with a 20-second timeout, no retries, no per-model probes, and no NIM request.
   - Deploy backend initially with the dynamic flag false, deploy the dynamic-capable frontend, run migration/sync evidence, then enable the flag. Configure the scheduler only under separate production authority.

All slices are sequential. Exclude package/lock changes, provider base URLs, secrets, `.env` contents, gamecore/dictionaries, paid models, Stripe, Slovak support, FrameNest code, live keyed-provider probes, deployment, commit, and push unless separately authorized.

## Tests and acceptance

- Backend tests cover free/pricing/tool/text rejection, future/null/tied release dates, top-four ranking, NIM isolation, persistent Admin disables across seed/sync, next-row fill after a kill, missing-row availability, large-drop rollback, one catalog GET, newest default selection, stale preference rejection, serializer order, and money-field absence.
- Migration tests cover re-enabling previously code-disabled non-curated candidates without re-enabling killed curated/NIM rows, preserving game foreign keys, reversible prompt updates, and preserving customized prompts.
- Frontend tests cover dynamic pair validation, paid/unknown rejection, identical Play/Judge queue order, selected-first behavior, three-attempt cap, shared provider-call budget, zero SDK retries, deadline/reconciliation stops, Judge malformed-output fallback, exhausted 503, and fail-closed catalog loss.
- Prompt tests assert strict JSON, backend legality authority, Collins-only Judge policy, budget-aware search, and absence of sponsor/USD language in live presets.
- Run focused tests, full backend pytest, Ruff, frontend Vitest, lint, `tsc --noEmit`, and production build. Run mypy and require no new errors relative to the already recorded 64-error baseline.
- No live OpenRouter/NIM generation or live 429→NIM acceptance is part of implementation validation.
- A fresh independent acceptance Worker reviews the immutable candidate, cap enforcement, free-only negative cases, migration/rollback behavior, and exact documentation.
- Cooperator-rendered acceptance checks newest-first cards, new-account default, preference retention, model-switch animation, reduced-motion behavior, exhaustion messaging, and instant removal after an Admin kill switch.
- Production acceptance separately verifies the named schedule, non-overlap, one-request accounting, last-known-good preservation on failure, and successful flag-off rollback.

## Rollback and stop rules

- Immediate product rollback: set `DYNAMIC_FREE_MODEL_CATALOG_ENABLED=false` and restart Django. Dynamic rows remain stored but become unselectable; stale frontend preferences repair to a bootstrap row.
- Operational rollback: pause the named schedule and deactivate a problematic row in Admin. No catalog row is deleted.
- Roll backend selection to curated-only before rolling back the dynamic-capable frontend.
- Stop Route 2 and retain Route 1 if OpenRouter’s catalog cannot provide trustworthy free pricing, tools, text-output, or release metadata.
- Stop without another Play attempt when turn reconciliation fails, the turn changes, time is below 15 seconds, provider-call usage is missing, or the shared budget is exhausted.
- Stop Judge after three attempts or thirty seconds; return an explicit service failure.
- Stop rollout if the frontend capable of dynamic IDs is not deployed before the feature flag is enabled.

Validation performed for this plan: exact repository, branch, baseline, clean tracked state, AP gitlink, and `ap doctor` PASS; mandatory protocol and task files inspected. No tests or provider calls were run because this planning authority permitted read-only inspection only.

Commit: not performed.  
Push: not performed.  
Deviations: none.  
Residual risks: catalog metadata cannot prove real model quality/tool reliability; runtime fallback and Admin kill switches contain that risk. Production scheduling remains separately authorized operational work.

Smallest next step: Orchestrator presents Route 1 versus recommended Route 2 to Michal for approval, then issues Slice 1 to a fresh Worker.

Report justification: new-evidence  
Authority expiry: this planning authority expires with this terminal report; implementation, mutation, provider calls, commit, push, deployment, acceptance, and closure remain unauthorized.  
Logical-whole closure: not-closed  

Resolved Execution Issues / Near-Misses: none  
Pre-Existing Failure Classification: none
