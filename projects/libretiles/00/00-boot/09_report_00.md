### Report for ORCHESTRATOR_CHAT

Logical whole identity: free-openrouter-rival  
Worker session ordinal: 09  
Worker exchange ordinal: 01

- status: **PARTIAL**
- phase-qualified result: **acceptance-complete**
- start commit: `3aee63240da29f6dcf5e3bdd6b5ab9dbacec1761`
- end commit: `3aee63240da29f6dcf5e3bdd6b5ab9dbacec1761` (equal to start; no mutation)
- changed files: none tracked (`git status --porcelain` empty before and after; lockfiles unchanged)

Capability handshake (abbreviated; capability does not grant authority):
- Plan Mode: **off** (Native planning mode `not-used`; no mode switch)
- Python: CPython **3.12.12** via `backend/.venv/bin/python` with `env -u APPIMAGE -u ARGV0 -u APPDIR`
- Poetry: **2.3.2**
- Node: **v26.4.0** / npm **12.0.1**
- Git: read-only
- `OPENROUTER_API_KEY` values: **not probed**. Cooperator stated a real key exists in `frontend/.env.local`; Next.js build only reported `Environments: .env.local`. No secret printed.

Tests and validation:

| Gate | Result |
|---|---|
| Repository gate | **PASS** — HEAD `3aee632…`, branch `main`, tracked porcelain empty, `HEAD:.ap` = `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |
| `./.ap/ap doctor` (before) | **PASS**; governing variant **stable** |
| `makemigrations --check --dry-run` | **No changes detected** |
| `ruff check .` | **All checks passed** |
| mypy `config game gamecore accounts catalog billing` | **70 errors in 21 files** — classified **Pre-Existing** (same count/class as Slice 5). `catalog/openrouter_sync.py` and `catalog/selection.py` have **zero** mypy errors. `billing/services.py` / `game/services.py` hits are unused-ignore / no-untyped-def / arg-type on pre-existing patterns, not new OpenRouter typing defects. |
| Focused pytest | **70 passed**, 0 failed, 12.46s |
| Full pytest | **73 passed**, 0 failed, 13.79s (includes websocket; Redis was not started; InMemoryChannelLayer as documented) |
| `npm ci` | exit 0 (381 packages; install-scripts blocked for `sharp@0.34.5` and `unrs-resolver@1.11.1` — same class as Slice 3; lint/tsc/build still passed) |
| `npm run lint` | **PASS** |
| `npx tsc --noEmit` | **PASS** |
| `npm run build` | **PASS** (Next.js 16.2.0 webpack; 10/10 pages) |
| `./.ap/ap doctor` (after) | **PASS**; tracked tree still clean |

Named-test confirmation (exist + passed; class names are singular `CatalogAPITest` / `GameAPITest`):

| Test | Evidence |
|---|---|
| `test_list_models_returns_shortlist_in_free_rival_order_with_zero_costs` | IDs equal `FREE_RIVAL_IDS`; all costs `0.00`; one flagship |
| `test_list_models_excludes_paid_malformed_non_tool_lm_novita_xai_openai_and_inactive_extra_free` | passed |
| `test_ineligible_ids_are_rejected_for_preference_create_and_switch` | PATCH `/api/auth/me/`, POST create, in-game switch all **400** for openai / malformed / old-free / lmstudio / novita / x-ai / inactive extra free |
| `test_create_game_rejects_dynamic_lmstudio_model_id` | HTTP 400; no AIModel row created |
| `test_can_switch_game_ai_model_to_dynamic_lmstudio_model` | HTTP **400**; does not enable LM |
| `test_apply_ai_move_returns_billing` | `charge_source == "free_rival"`, `charged_credits == "0.000000"`, balance unchanged at `10.000000` |
| `test_charge_ai_turn_endpoint_deducts_credits` | `free_rival` / `0.000000`; `Transaction` count unchanged |
| `test_seed_models_is_idempotent_and_has_no_reset_flag` | double seed; leftover row survives; `--reset` absent |
| `test_data_step_keeps_legacy_rows_and_makes_them_ineligible` | row IDs preserved; non-shortlist deactivated/ineligible |
| `test_dictionary_validation.py` | 6 tests passed |

Inspection:
- Commit range `origin/main` (`805bc4c…`) → HEAD, **6 commits, not pushed**: `b8f763e` AP pin → `bef5ef4` OpenRouter runtime → `d9be596` catalog/billing → `b79a3e1` settings UX → `2cc4474` leftover LM/providers → `3aee632` bootstrap docs.
- Catalog migration `0006`: two `RenameField` (`gateway_*` → `openrouter_*`) + non-deleting `RunPython(deactivate_non_shortlist, noop_reverse)`. Reverse is a documented **no-op**. Developer sqlite was **not** reversed.
- Negative live-path search (exclude migrations `0001`–`0005`, `package-lock.json`, reject-LM assertions): **no** remaining runtime import of `ai-gateway`, `lm-studio`, `local-ai`, `/api/ai/local/status`, `AI_GATEWAY_API_KEY`, or `OPENAI_API_KEY`. Frontend uses `createOpenAI` from `@ai-sdk/openai` only as an OpenRouter-compatible adapter with `process.env.OPENROUTER_API_KEY` and hardcoded `https://openrouter.ai/api/v1`. Remaining `lmstudio` / `your-vercel-ai-gateway-api-key` strings are reject-assertions and placeholder matchers in `scripts/start-frontend.sh` / `scripts/libretiles.sh`.
- Seed idempotence covered by pytest; developer `db.sqlite3` was not mutated for a second live seed.

Push: **not performed** (`main` remains **ahead 6** of `origin/main`).

Deviations, risks, missing evidence:
1. **Root `.env.example` residual (named):** still says frontend env is “AI Gateway, API URL”. Pointer comment only; off this allowlist; not a live-key recipe.
2. **mypy pre-existing residual (named):** 70/21, same class as Slice 5. Not used as a this-whole product fail.
3. Websocket tests **passed** (3 extra in the full suite). Redis-absent skip classification **does not apply**.
4. Named test names are **not stale**.
5. No live OpenRouter inference, no browser, no secrets read. Credential-bounded happy-path (register → Settings → one AI turn) remains a **separate grant**.
6. **Cooperator request outside this envelope (not executed):** order free rivals newest→oldest on the assumption that newer models are stronger. Current shortlist order (frontend + backend + frozen `0006`) is `google/gemma-4-31b-it:free` (default), `nvidia/nemotron-3-super-120b-a12b:free`, `z-ai/glm-5.2:free`, `google/gemma-4-26b-a4b-it:free`. Reorder would be a tracked product change and was **not authorized**. Cooperator also stated a real `OPENROUTER_API_KEY` is present locally; that is capability context, not this-session authority to call the provider.

One smallest next step: **do not close the logical whole**. Return these findings to the Orchestrator. Optional later grants (separate, not implied): (a) credential-bounded happy-path with explicit OpenRouter/browser authority; (b) if Michal still wants it, a bounded reorder of `FREE_RIVAL_IDS` newest→oldest with matching seed/migration/test updates.

Report justification: **new-evidence**  
Authority-expiry statement: this acceptance authority expires when this terminal report is submitted. A UI approval or retained plan grants no extra authority.  
Logical-whole closure: **not-closed**

Resolved Execution Issues / Near-Misses:
- Cursor AppImage `APPIMAGE`/`ARGV0`/`APPDIR` still intercept `python*`; all Poetry/pytest/mypy used `env -u APPIMAGE -u ARGV0 -u APPDIR`.
- First named-test re-run used plural class names (`CatalogAPITests`); corrected to `CatalogAPITest` / `GameAPITest`. Product gates were already green from the 70/73 suite.

Pre-Existing Failure Classification:
- **mypy strict-mode noise:** 70 errors in 21 files (unused `type: ignore`, missing generics, untyped Channels). Same count and class as Slice 5. Not a this-whole product defect.
- **Root `.env.example` Gateway pointer:** residual docs drift named in the prompt; not edited.