# Creditless Free Play

## Summary

Remove all application-level money handling: balances, credits, USD amounts, token prices, charges, Stripe references, billing endpoints, monetary UI, admin reporting, and documentation.

Retain:

- The exact five curated `(provider, model_id)` rival pairs.
- OpenRouter/NVIDIA NIM fallback, capped at three sequential attempts.
- Django Admin control of catalog activation and availability.
- Collins 2019 backend validation for every persisted move.
- Judge dispatch through one selected free rival, with no fallback loop.
- Nested provider-error traversal for 401, 429, and 5xx conditions.
- Non-monetary token usage metadata where operationally useful.

Repository gates passed: canonical checkout, clean tracked worktree, `main`, expected HEAD and `.ap` gitlink, and `./.ap/ap doctor` PASS.

## Verified Current Surface

- `billing` owns user balances, transactions, Stripe identifiers, usage-to-price calculations, the charge endpoint, and zero-charge summaries.
- Accounts create and expose balances; game application and state expose `billing`, `last_move_billing`, and `total_cost_usd`.
- Catalog models, serializers, Admin, seeding, and OpenRouter synchronization handle per-game and per-token prices. Selection currently requires explicit parseable zero input/output prices.
- Frontend profile, header, board, history, notifications, store, types, SSE handling, and AI route display or transport credits/USD.
- Product documentation describes credits, USD, pricing, Stripe, spend, and future top-ups.
- `normalizeProviderError` safely traverses nested `lastError`, `cause`, and `errors`, including cycles; this is independent of `credit_balance` and must remain intact.

## Architecture Decision

| Fork | Result | Rollback |
|---|---|---|
| 1 — Dormant schema | Remove product/API/UI money behavior but retain billing tables and catalog price columns. While those columns remain, selection must continue requiring explicit, parseable zero prices; absent or malformed prices are never free. Lower migration risk, but retains sensitive historical records, misleading schema, and future drift risk. | Revert code; tables and data remain. |
| 2 — Drop schema **(recommended)** | Remove runtime billing code and delete balance, transaction, game-cost, and catalog-price storage. Eligibility becomes the positive five-pair allowlist plus active language-model, tools, and provider-availability checks. Missing prices cannot imply free because no pricing fields remain. | Destructive data rollback requires restoring a verified pre-migration database backup and redeploying the preceding release. |

Approval of this plan selects Fork 2. The table/data deletion is intentionally irreversible within Django migrations. Before it may run, capture legacy row counts and a database backup, prove the backup can be restored, and pause writes. Failure of any checkpoint stops the migration.

Historical migration files remain as an inert, uninstalled migration-only tombstone. They are not live product behavior.

## Public Interface Changes

- Remove `credit_balance` and `credit_updated_at` from account/profile responses.
- Remove `/api/billing/charge-ai-turn/`; it must return 404 after rollout.
- Remove `billing`, `last_move_billing`, and `total_cost_usd` from move, game-state, history, and SSE responses.
- Remove `cost_desc`; game history supports the existing non-monetary ordering only.
- Remove catalog `cost_per_game`, `pricing`, and cost-per-million fields.
- Remove frontend `BillingSummary`, credit state/setters, monetary toast fields, and monetary component props.
- Preserve game, fallback, Judge, provider/runtime, and dictionary-validation request shapes otherwise.

## Ordered Implementation Slices

### Slice 1 — `refactor: detach gameplay from billing`

Remove billing behavior from accounts, game APIs, URLs, and Django Admin while retaining the old tables temporarily. Do not alter catalog price fields or `is_explicitly_free` in this slice.

Changed-path allowlist:

- `backend/.env.example`
- `backend/accounts/admin.py`
- `backend/accounts/models.py`
- `backend/accounts/serializers.py`
- `backend/accounts/views.py`
- `backend/billing/admin.py` — delete
- `backend/billing/services.py` — delete
- `backend/billing/urls.py` — delete
- `backend/billing/views.py` — delete
- `backend/config/settings.py`
- `backend/config/urls.py`
- `backend/game/admin.py`
- `backend/game/serializers.py`
- `backend/game/services.py`
- `backend/game/templates/admin/game/dashboard.html`
- `backend/game/views.py`
- `backend/tests/test_api.py`

Tests:

- Registration and profile responses have no balance fields and create no new balance row.
- Billing endpoint returns 404.
- AI place, pass, and exchange succeed without charge calls or billing metadata.
- Game state/history contain no cost or billing response fields; `cost_desc` is rejected.
- Admin has no balance, spend, charge, or USD controls.
- Run focused API tests, then Ruff, MyPy, full pytest, and `makemigrations --check`.

Stop if any gameplay path still imports billing, the existing explicit-free predicate changes, or removing billing affects Collins validation.

### Slice 2 — `refactor: remove money from the game client`

Remove all monetary state, rendering, SSE handling, and charge requests. Preserve profile/password functionality and ordinary move notifications.

Changed-path allowlist:

- `frontend/src/app/api/ai/move/route.ts`
- `frontend/src/app/api/ai/move/route.test.ts` — new
- `frontend/src/app/api/ai/judge/route.test.ts` — new
- `frontend/src/app/game/[id]/page.tsx`
- `frontend/src/app/globals.css`
- `frontend/src/app/page.tsx`
- `frontend/src/app/settings/page.tsx`
- `frontend/src/components/board/Board.tsx`
- `frontend/src/components/game/GameHistoryPanel.tsx`
- `frontend/src/components/game/ProfileModal.tsx`
- `frontend/src/components/game/ScorePanel.tsx`
- `frontend/src/hooks/useGameStore.ts`
- `frontend/src/lib/ai-move-stream.test.ts`
- `frontend/src/lib/ai-move-stream.ts`
- `frontend/src/lib/api.ts`
- `frontend/src/lib/premiumSurface.ts`
- `frontend/src/lib/types.ts`

Tests:

- AI place/pass/exchange streams never call the removed billing endpoint and emit no billing fields.
- Game, profile, board, and history render without balance, spend, cost, or USD text.
- Mocked Judge resolves one curated rival and invokes one runtime dispatch with no fallback.
- Existing fallback tests still prove at most three sequential attempts, provider diversity, and turn reconciliation.
- Existing runtime tests still prove nested 401/429/503 classification, cycle handling, and redaction.
- Run `npm test`, `npm run lint`, and `npm run build`.

`ai-runtimes.ts` and `ai-fallback.ts` are outside the allowlist. Stop if the slice appears to require changing their behavior or making a live provider request.

### Slice 3 — `refactor: drop dormant money schema`

Atomically remove price-dependent eligibility and its fields, the billing model, and game-cost storage.

Final selection predicate:

1. Exact `(provider, model_id)` membership in `FREE_RIVAL_PAIRS`.
2. `is_active=True`.
3. `model_type="language"`.
4. `tools` capability.
5. OpenRouter rows require `openrouter_available=True`; the NVIDIA NIM row does not.
6. No price-based inference or fallback.

OpenRouter synchronization continues accepting only eligible `:free`, text-output, tools-capable records and protecting the NIM row, but it no longer parses or persists price data. Only the exact curated pairs can become gameplay-selectable.

Changed-path allowlist:

- `backend/billing/models.py` — delete
- `backend/catalog/admin.py`
- `backend/catalog/management/commands/seed_models.py`
- `backend/catalog/migrations/0008_remove_aimodel_money_fields.py` — new
- `backend/catalog/models.py`
- `backend/catalog/openrouter_sync.py`
- `backend/catalog/selection.py`
- `backend/catalog/serializers.py`
- `backend/catalog/views.py`
- `backend/config/settings.py`
- `backend/game/migrations/0005_remove_money_state.py` — new
- `backend/game/models.py`
- `backend/pyproject.toml`
- `backend/tests/test_api.py`
- `backend/tests/test_creditless_migration.py` — new
- `backend/tests/test_openrouter_catalog_migration.py`

Migration behavior:

- Remove `cost_per_game`, `pricing`, and `total_cost_usd`.
- Remove top-level `billing` keys from existing `Move.ai_metadata` while preserving unrelated AI metadata.
- Delete stale billing permissions and content types.
- Drop `billing_transaction` before `billing_credit_balance`, using backend-compatible guarded SQL.
- Remove `billing` from installed apps and packaging.
- Leave only `backend/billing/__init__.py` and historical migration files as inert migration history.
- Mark the cleanup migration irreversible.

Tests and gates:

- Exercise upgrade-style cleanup against representative legacy rows and fresh-database migration on SQLite.
- Rehearse the migration on a restored PostgreSQL snapshot before production.
- Assert the legacy tables and columns are absent, metadata is scrubbed, unrelated data survives, and no stale billing content types/permissions remain.
- Assert malformed or absent catalog metadata cannot admit non-curated rows.
- Run `makemigrations --check`, focused migration/catalog tests, Ruff, MyPy without `billing`, and full pytest.

Stop before migration if the snapshot cannot be restored, legacy counts are not recorded, the database backend differs from those rehearsed, or unrelated tables/data would be affected.

### Slice 4 — `docs: declare free-only creditless play`

Update product, contributor, architecture, and roadmap documentation to describe a free-only application with no balances, pricing, Stripe, top-ups, or billing roadmap.

Changed-path allowlist:

- `AGENTS.md`
- `CONTRIBUTING.md`
- `README.md`
- `docs/architecture.md`
- `libretiles_PRD.md`

Document that provider quotas or trial terms are external and may change; they are not Libre Tiles credits or charges. Preserve the five-rival, Admin, fallback, Judge, and Collins descriptions.

Stop if documentation proposes Stripe, paid catalog tiers, or changes provider/dictionary scope.

## Rollout and Independent Acceptance

Deploy the final frontend before the backend migration; it tolerates extra legacy response fields while ceasing charge requests. Then pause backend writes, record counts, take and restore-test the backup, deploy the backend, apply migrations, and complete local smoke checks before reopening writes.

A fresh independent Worker must perform acceptance against the fixed candidate commit:

- Search live product code, configuration, and documentation for credits, balances, USD, charges, token-price fields, `cost_per_game`, `total_cost_usd`, `/api/billing`, Stripe, top-up, cost, and spend surfaces.
- Exclude `.ap`, dictionaries, tests, and migration history from the zero-live-surface assertion. Inspect migrations separately.
- Classify natural game phrases such as “balanced leave” and “spend blank” as non-monetary.
- Explicitly allow provider-error phrases such as “payment required” or “insufficient funds” only inside `normalizeProviderError` and its tests.
- Introspect SQLite and restored PostgreSQL schemas for removed tables/columns and stale metadata/content types.
- Verify profile, catalog, game-state, history, SSE, and removed-endpoint contracts.
- Verify all five curated pairs and only eligible active rows are selectable; confirm NIM deactivation remains its kill switch.
- Run backend gameplay tests proving persisted moves still use Collins 2019.
- Run mocked Judge and fallback tests with no network, credentials, or provider HTTP.
- Run full backend and frontend quality commands.

## Assumptions, Risks, and Non-Goals

- Existing billing records are intentionally discarded only after Michal approves Fork 2 and the backup gate passes.
- Removing response fields and the billing endpoint is an accepted coordinated API break.
- Token counts may remain as non-monetary diagnostics; token prices and charge calculations may not.
- Provider free-tier availability remains external operational risk. Catalog activation and fallback handle availability; the application will not add monetary accounting.
- The largest risks are destructive migration rollback, frontend/backend deployment skew, and accidentally weakening eligibility or nested provider-error classification. The slice gates address each.

Non-goals: Stripe design, top-ups, paid catalog tiers, LM Studio, AI SDK upgrades, live provider calls, live 429→NIM testing, Slovak dictionary work, unbeatable-AI research, FrameNest copying, deployment/push during planning, or closing `nim-fallback-free-rivals`.

Report justification: new-evidence  
Authority expiry: planning authority expires with this terminal report; no implementation authority was granted.  
Logical-whole closure: not-closed  
Smallest next step: Orchestrator presents the plan to Michal for approval, then issues Slice 1 to a fresh Worker with Native planning mode: not-used.  
Near-Misses: Broad searches also matched dictionary words, game-strategy language, and required provider-error classifications; these are classified explicitly rather than removed blindly. Removing SSE balance handling must not be used as a reason to simplify nested error traversal.  
Pre-Existing Failure Classification: none observed. Product tests were prohibited in this planning session; the repository gate and AP doctor passed.
