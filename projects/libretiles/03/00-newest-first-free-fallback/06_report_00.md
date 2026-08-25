### Report for ORCHESTRATOR_CHAT

Logical-whole identity: newest-first-free-fallback · Worker session ordinal: 06 · Worker exchange ordinal: 01

**Status:** PASS  
**Phase-qualified result:** acceptance-complete

**Start commit:** `e00c92271e788b78a9460e6daa39d3120b7ca58b`  
**End commit:** `e00c92271e788b78a9460e6daa39d3120b7ca58b`  
(immutable acceptance candidate; local `HEAD` = `origin/main` = candidate SHA; branch `main`; tracked porcelain empty before and after; `.ap` gitlink `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`; `./.ap/ap doctor` PASS)

**Changed files:** none tracked. Disposable probe DB `backend/.acceptance-probe-06.sqlite3` was created, used only for migration forward/back, then deleted (`cleanup_ok`; no leftover `-wal`/`-shm`/`-journal`).

Independence: this session did not implement any slice of the candidate. Evidence below is this session's own reads, pytest/vitest/lint/mypy/build, and the disposable SQLite probe.

**Audit vs claims**

1. **Cap enforcement — observed as claimed.** `MAX_FALLBACK_ATTEMPTS = 3` and `buildFallbackQueue` cap distinct pairs (`frontend/src/lib/ai-fallback.ts`). Play `orchestrateFallbackTurn` shares one whole-turn `maxStepsTotal` / `maxStepsRemaining` budget; game page posts `max_steps` from that remainder. Move route `maxRetries: 0`; terminal SSE includes `provider_requests_used` on done and post-generation error paths (`frontend/src/app/api/ai/move/route.ts`, `ai-move-stream.ts`). Judge: `queue.slice(0, MAX_FALLBACK_ATTEMPTS)`, `ATTEMPT_TIMEOUT_MS = 10_000`, `OVERALL_BUDGET_MS = 30_000`, `maxRetries: 0`, HTTP 503 with no `results` on exhaustion; `parseJudgeResults` returns `null` for malformed output and never synthesizes false invalid verdicts (`frontend/src/app/api/ai/judge/route.ts`).

2. **Free-only negative cases — observed as claimed.** `normalize_openrouter_model` rejects paid, malformed pricing, non-tools, non-text, `openrouter/free`, non-`:free`, slash-less ids, and the NIM chat id (`backend/catalog/openrouter_sync.py`). Future `created` timestamps store as missing; `_newest_first_key` ranks missing/future after dated rows, then bootstrap `sort_order`, then `model_id` (`backend/catalog/selection.py`). Sync skips the NIM id and any existing `nvidia-nim` row; NIM is appended last and has no discovery call. Frontend `isValidRuntimePair` / `playableCatalogPairs` / `revalidateRuntimePair` fail closed on unknown providers, paid shapes, and catalog-unconfirmed pairs; `resolveEligibleModelId` repairs stale ids to a live eligible id then catalog row 1 (`frontend/src/lib/model-catalog.ts`).

3. **Flag and kill switches — observed as claimed.** `DYNAMIC_FREE_MODEL_CATALOG_ENABLED` defaults false via `.lower() in ("true", "1", "yes")` (`backend/config/settings.py:160-162`). Flag off returns `FREE_RIVAL_PAIRS` order; flag on returns four newest eligible OpenRouter rows plus seeded NIM last. `seed_models` sets `is_active=True` only on create and does not write `is_active` on update. Sync creates new rows active and never updates `is_active` on existing rows. Empty cohort always aborts; `new_count * 2 < previous_count` aborts with zero writes unless CLI `--allow-large-drop`; empty still aborts with that flag.

4. **Migrations 0009/0010 — observed as claimed, including disposable SQLite probe (`PROBE_PASS`).** 0009 forward re-enables only non-curated OpenRouter `:free` rows; killed curated and NIM stay inactive; game FKs preserved. Reverse does not revive those kills. 0010 SHA-256-gates forward to `PRIOR_PROMPTS` hashes only; Admin-customized rows untouched; reverse restores exactly the texts forward updated. `migrate catalog 0008 ↔ 0009 ↔ 0010` on the probe DB matched the same invariants. Probe file removed afterward.

5. **Collins authority — observed as claimed.** `_submit_move_locked` (human and AI persist paths) and `validate_move_for_ai` / `validate_words` all call `_word_passes_dictionary()` via `_get_dictionary()` loaded from `PRIMARY_DICTIONARY_PATH` (`collins2019.txt`). Overlay candidates may be `valid: false`; persist goes through Django `ai-move`.

6. **Documentation exactness — five-plus spot-checks held.**
   - Flag identifier and default false: `settings.py` ↔ `backend/.env.example` ↔ AGENTS.md / README / architecture.
   - Sync: one GET `https://openrouter.ai/api/v1/models`, `timeout: float = 20.0`, no retry loop, no NIM URL (`openrouter_sync.py:53-59`).
   - Judge budgets 10 s / 30 s / `maxRetries: 0` / HTTP 503: `judge/route.ts` matches AGENTS.md and architecture.
   - Hardcoded bases: `OPENROUTER_BASE_URL` and `NVIDIA_NIM_BASE_URL` match README / frontend README / architecture; no base-URL env vars in examples.
   - `NEXT_PUBLIC_DEFAULT_MODEL` absent from `.env.example`, `backend/.env.example`, and `frontend/.env.local.example`.
   - Schedule `libretiles-openrouter-catalog-refresh` / 03:17 UTC is documentation-only: zero `.timer` / `.service` / cron / workflow hits in the repository.
   - Rollback copy (flag false + Django restart → bootstrap selection; stored dynamic rows unselectable; stale prefs repair to a bootstrap row) matches `_bootstrap_selectable` + `resolveEligibleModelId`.
   - Five bootstrap IDs in AGENTS.md / architecture match `FREE_RIVAL_PAIRS`.

7. **Gate re-run (this session; each suite once; CPython 3.12.12 via `backend/.venv`, wrapped `env -u APPIMAGE -u APPDIR -u ARGV0`)**

| Gate | Result |
|---|---|
| `poetry run pytest` | **109 passed** (100% of 109 collected) |
| `poetry run ruff check .` | All checks passed |
| `poetry run mypy config game gamecore accounts catalog` | **63 errors in 17 files** (66 source files checked) — equals recorded baseline; **0 new errors**. `selection.py`, `openrouter_sync.py`, `0009_dynamic_free_catalog.py`, and `0010_refresh_seeded_prompts.py` are not in the error set. Remaining noise is django-stubs / channels `import-untyped` / untyped admin and serializer generics. |
| `npx vitest run` | **10 files / 107 tests passed** |
| `npm run lint` (eslint) | exit 0 |
| `npx tsc --noEmit` | exit 0 |
| `npm run build` | compiled successfully (Next.js 16.2.0) |

**Findings:** none.

**Pre-declared residuals — remain as stated, nothing more**
- mypy baseline 63/17 django-stubs and channels typing noise: still present, unchanged count.
- `backend/catalog/selection.py:10` still comments `frontend/src/lib/free-rivals.ts`; that file does not exist.
- DB prompt presets still duplicate `frontend/src/lib/prompts.ts` by snapshot design (`0010` `NEW_PROMPTS` vs live `MOVE_SYSTEM_PROMPT`).
- Host schedule intentionally unconfigured (docs only; no install artifacts).
- Flag intentionally default false until rollout.

**Deviations:** none from the acceptance grant. First disposable-probe script had a Worker-side `SyntaxError` (`pk` keyword repeated) and exited before `migrate`; rerun with a corrected script produced `PROBE_PASS`. Not a product defect.

**Risks:** none beyond the pre-declared residuals. Flag-off and unconfigured schedule are intentional.

**Missing evidence:** Cooperator-rendered UI checks (newest-first cards, new-account default, preference retention, ping-pong / reduced-motion, exhaustion messaging, Admin kill). Browser use was not authorized.

**Authorized Git / side effects:** none. No commits, no push, no live OpenRouter/NVIDIA HTTP, no `.env` / `.env.local` opened or printed, no servers started beyond pytest, no Redis.

Resolved Execution Issues / Near-Misses: probe script syntax error before any DB write; corrected and rerun once; disposable path never left behind. Residual risk: none.  
Pre-Existing Failure Classification: none

**Smallest next step:** Orchestrator proceeds to Cooperator-rendered UI checks and closure evaluation. No correction slice is indicated.

Report justification: new-evidence  
Authority expiry: this authority expires with this terminal report; mutation, push, deployment, and logical-whole closure remain unauthorized.  
Logical-whole closure: not-closed

---
*Orchestrator reconciliation addendum (2026-08-25 ~19:10): independently confirmed candidate immutability after acceptance — HEAD = `origin/main` = `e00c92271e788b78a9460e6daa39d3120b7ca58b`, porcelain empty, no leftover probe artifacts. Acceptance PASS accepted; zero findings; unknown-unknown budget consumed 1 of 1 primary fresh acceptances, 0 corrections. Remaining before ORCHESTRATOR closure of whole D: Cooperator-rendered UI checks + residual-risk disposition (see handout §5 and closure evaluation).* 
