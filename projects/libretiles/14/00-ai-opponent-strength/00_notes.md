# Libre Tiles — Notes for logical whole `ai-opponent-strength` (Meta 14/00)

Append-only notes ledger for logical whole 14/00.
Maintained by the Agent Orchestrator. Evidence and observation history; not task authority.

---

## §0 Whole 14 Boot and Baseline Record

Whole 14 initialized on 2026-09-07 following the successful closure of `admin-provider-model-console` (11/00).
- Baseline commit: `151e833dd0e78ced075101864cb5f45ee521bebc`
- Pinned AP commit: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- Standing gates:
  * Backend: 92 passed in 10.4s (focused), 1017+ passed in full pytest; ruff clean; mypy clean (99 source files).
  * Frontend: typecheck clean, lint clean, vitest 49 passed.
- Handout prompt refactored and updated:
  `/home/agile/meta/projects/libretiles/14/00-ai-opponent-strength/00_handout.md`
- Core mission:
  1. Elevate AI opponent strength so it decisively beats human players.
  2. Ensure self-play games reliably finish with `BAG_EMPTY_AND_PLAYER_OUT`, completely eliminating dead-rack pass stalls.
  3. Maintain a rock-solid, model-neutral game engine foundation.
  4. Complete the critical readiness gate required prior to VPS deployment.

---

## §1 Stage 1 Baseline Verification (2026-09-07)

- Verified repository state:
  * HEAD: `151e833dd0e78ced075101864cb5f45ee521bebc` == `origin/main`. Working tree clean.
  * Pinned AP submodule commit: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.
- Baseline test execution:
  * `backend/tests/test_strength_benchmark.py` & `backend/tests/test_slovak_full_game.py`:
    - `strength-default` (English ranked vs first-witness, seeds 300, 301 across slots 0 and 1):
      * Seed 300, slot 0: spread +420, `BAG_EMPTY_AND_PLAYER_OUT`, max plies = 35.
      * Seed 300, slot 1: spread +505, `BAG_EMPTY_AND_PLAYER_OUT`, max plies = 35.
      * Seed 301, slot 0: spread +461, `BAG_EMPTY_AND_PLAYER_OUT`, max plies = 35.
      * Seed 301, slot 1: spread +501, `BAG_EMPTY_AND_PLAYER_OUT`, max plies = 35.
      * Total spread = +1887, average spread = +471.75.
    - `slovak-full-game` (Slovak witness-first self-play, seed 0):
      * Terminated at ply 55 with reason `SIX_CONSECUTIVE_ZERO_SCORES` (stall due to dead-rack pass streak).
      * Final scores: P0 = 303, P1 = 243; leftover points: P0 = 5, P1 = 27.
      * Confirms the core diagnosis: Slovak self-play under greedy/first-witness search stalls out on consonant/diacritic clogs rather than reaching `BAG_EMPTY_AND_PLAYER_OUT`.
  * Gates:
    - Backend: mypy clean (99 source files), ruff clean.
    - Frontend: `npm run typecheck` clean, `npm run lint` clean, vitest 37 passed test files (555 passed, 3 skipped).

---

## §3 Slice 1 Acceptance & Readback (2026-09-07)

- Received `02_report_00.md` from Worker Session 02 (`AIOS-S1-PROMPT-SPECS`).
- Mutation & Verification:
  * Commit: `843251db8da0aee878c3462b14cfe8e73528b399`
  * Pre-push check passed against `151e833dd0e78ced075101864cb5f45ee521bebc`.
  * Post-push readback confirmed: `origin/main == HEAD == 843251db8da0aee878c3462b14cfe8e73528b399`.
  * Files modified:
    - `frontend/src/lib/prompts.ts`: Added native MovePromptSpec and JudgePromptSpec for all 10 un-spec'd variants, prototype-safe `Map`-backed dispatch for `movePromptSpecFromContext` and `judgePromptSpecFromBody` resolving `lexicon_id` first, then `variant`, with fallback to English. Unchanged template keeps `CORE_SHA256` (`c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`) byte-identical.
    - `frontend/src/lib/prompts.test.ts`: Added 54 new assertions covering all 12 move cores, all 12 judge cores, and dispatch lookups/fallbacks. All 99 tests pass.
    - `frontend/src/app/api/ai/move/route.ts`: Fixed hardcoded English string in `validateMove` description.
  * Quality gates:
    - Frontend: `prompts.test.ts` (99 passed), `move/route.test.ts` + `judge/route.test.ts` (83 passed), `ai-turn-simulation.test.ts` (5 passed), `typecheck` clean, `lint` clean.
    - Backend: `mypy` clean (99 source files), `ruff` clean, `pytest tests/test_strength_benchmark.py tests/test_slovak_full_game.py` (9 passed, 2 skipped in 43.95s).
- **Slice 1 (Variant-Aware Prompt Specs & Defect H1 Fix) is ACCEPTED.**

---

## §4 Session 03 Evaluation & Plan Acceptance (2026-09-07)

- Received `03_report_00.md` from Worker Session 03 (`AIOS-SLICE-2-PLAN`).
- Findings & Evaluation:
  * Formulated utility function: $\text{Utility}(m) = 100 \cdot \text{total\_score}(m) + \text{leave\_equity\_cp}(L(m))$.
  * Integer centipoints (fixed-point ×100, no floats, byte-for-byte deterministic). Clamped to $[-3000, +6000]$.
  * Endgame mode ($bag\_count == 0$): $E_{\text{endgame}}(L) = -100 \cdot \sum \text{face\_points}(t)$ to minimize leftover penalties.
  * Curated base tile equity tables for English and Slovak, plus fallback derived profile for all other 10 variants.
  * Vowel-consonant balance table `BALANCE_CP[n][v]` based on non-blank leave size (0-6) and vowel count. Blanks act as wildcards halving penalties.
  * Duplicate tile penalties and synergy pair bonuses (e.g. English Q+U, Slovak O+V, S+T, N+I, etc.).
  * Architectural clean-up: New module `backend/gamecore/leave_equity.py`. In `move_search.py`, `leave_value` renamed to `leave_equity_cp: int`. Old `_leave_components` and defective `_vowel_set` deleted. Per-searcher memo cache `_leave_cache` added.
  * Crucial discovery: `test_slovak_full_game.py` uses `POLICY_WITNESS` (first witness), not ranked search; thus, a dedicated `backend/tests/test_slovak_strength.py` will be created to measure Slovak ranked strength and clog elimination.
  * Blast radius identified: `backend/assets/diagnostics/position_sets/english-f5ae61b4.json` records ranked traces and must be regenerated via `manage.py generate_position_set --variant-slug english`, updating the 4 test files that pin its digest.
- Plan accepted in full. Evidence tier: E2 (cross-cutting reversible).
- Implementation grant will target Worker Session 04 in a fresh Worker session (`Native planning mode: not-used`).

---

## §5 Session 04 BLOCKED Evaluation & Prompt Reissue Resolution (2026-09-07)

- Received `04_report_00.md` with status `BLOCKED` (`implementation-BLOCKED`).
- Blocker analysis:
  * Worker stopped lawfully prior to any mutation upon discovering that deleting `_RankedSearcher._leave_components` from `backend/gamecore/move_search.py` would cause an `AttributeError` in `backend/tests/test_atomic_tile_tokens.py` (line 647: `test_declared_vowels_change_leave_quality_slovak_stays_on_default`), which was not included in the path allowlist.
  * Zero mutation occurred. Repository remains clean at `843251db8da0aee878c3462b14cfe8e73528b399`. Pre-mutation baselines were successfully captured.
- Orchestrator Resolution:
  1. Add `backend/tests/test_atomic_tile_tokens.py` to the path allowlist.
  2. In `backend/gamecore/leave_equity.py`, ensure `profile_for_variant(variant, tile_points)` explicitly respects `getattr(variant, "vowels", None)` when present on the variant object.
  3. Update `test_declared_vowels_change_leave_quality_slovak_stays_on_default` in `backend/tests/test_atomic_tile_tokens.py` to test the new leave equity mechanism (`searcher._calculate_leave_equity([])` or `leave_equity_cp`), proving that declared variant vowels are respected and alter leave equity compared to variants without declared vowels.
  4. Issue reissued implementation prompt `05_implementation_00.md` for Worker Session 05.

---

## §6 Slice 2 Acceptance & Readback (2026-09-07)

- Received `05_report_00.md` from Worker Session 05 (`AIOS-S2-RACK-EQUITY-REISSUE`).
- Mutation & Verification:
  * Commit: `68afb6df92fccb2996ae83f1a444e4ada7396d10`
  * Pre-push check passed against `843251db8da0aee878c3462b14cfe8e73528b399`.
  * Post-push readback confirmed: `origin/main == HEAD == 68afb6df92fccb2996ae83f1a444e4ada7396d10`.
  * 16 files modified (+3374 / -2796 lines).
  * Major Deliverables Landed:
    - `backend/gamecore/leave_equity.py`: Pure-Python integer-centipoint Rack Equity & Leave Valuation engine.
    - `backend/gamecore/move_search.py`: Utility-based ranking (`total_score * 100 + leave_equity_cp`), `leave_value` renamed to `leave_equity_cp`, per-searcher profile resolution, memo cache.
    - `backend/game/position_sets.py`: Cooperator-authorized fix preventing `TileBag.__post_init__` from refilling an explicitly empty snapshot bag.
    - Regenerated diagnostic position set `english-aaac5c27.json` and updated 4 test files pinning its digest.
    - New tests: `test_leave_equity.py` (12 tests) and `test_slovak_strength.py`.
  * Empirical Performance Improvements (Proven):
    - English 100-game acceptance: Total spread increased by **+3,075 points** (from +44,320 to **+47,395**, average spread **+473.95**, 100/0/0 W/D/L).
    - English default 4-game: Average spread increased from +471.75 to **+479.00**.
    - Slovak full ranked self-play (node-bound 20k, seeds 0–4):
      * Pre-change: 3/5 finished with `BAG_EMPTY_AND_PLAYER_OUT` (seeds 3 and 4 stalled on `SIX_CONSECUTIVE_ZERO_SCORES` with 6 and 7 passes).
      * Post-change: **5/5 (100%)** finished with `BAG_EMPTY_AND_PLAYER_OUT` with zero pass stalls!
      * Seed 3: went from SIX_ZERO (353:581, 6 passes) to **OUT (504:493, 0 passes)**.
      * Seed 4: went from SIX_ZERO (547:339, 7 passes) to **OUT (552:363, 0 passes)**.
    - Slovak ranked vs witness: 4/0/0 with spreads +503, +329, +526, +346.
  * Quality gates:
    - Backend: `mypy` clean (100 source files), `ruff` clean, `pytest` clean across all suites including parity oracle.
    - Frontend: `typecheck` clean, `lint` clean, `prompts.test.ts` (99 passed).
- Cooperator Decision Recorded:
  * Cooperator explicitly authorized real provider API calls (including NVIDIA NIM) as needed for development until quota limits are hit.
- **Slice 2 (Rack Equity & Leave Valuation in Move Search) is ACCEPTED.**

---

## §7 Session 06 Evaluation & Plan Acceptance (2026-09-07)

- Received `06_report_00.md` from Worker Session 06 (`AIOS-SLICE-3-PLAN`).
- Findings & Evaluation:
  * Theoretical and architectural design for Pre-Endgame Tracking (`backend/gamecore/tile_tracking.py`) and Exact Endgame Minimax Solver (`backend/gamecore/endgame.py`).
  * Terminal swing valuation modeled rigorously: immediate out = $\text{my\_score} + 2 \times \text{opponent\_leftover}$; 2-ply out and deadlock terminal spread accurately account for `apply_final_scoring` transfers.
  * Discovered critical live defect: in `frontend/src/app/api/ai/move/route.ts:494`, the SSE move route re-sorted backend candidate recommendations by immediate raw score, which would undo strategic endgame choices. Added route and its test to allowlist to respect the late-game strategy marker.
  * Search bounding: 1,250 ms budget, 10,000 minimax state expansions, 25,000 placements cap, 4,096 transposition table entries.
  * Realistic protocol-grounded acceptance: recognizes that rare legal deadlocks exist in Scrabble; maintains 100% `BAG_EMPTY_AND_PLAYER_OUT` as our empirical acceptance target on benchmark seeds without faking legality.
  * Execution command discipline: reinforced RF-16 requirement: always use `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/` from `backend/`; never `PYTHON_DOTENV_DISABLED=1` and never `poetry run`.
  * Plan accepted in full. Evidence tier: E2 (cross-cutting reversible).
  * Implementation grant will target Worker Session 07 in a fresh Worker session (`Native planning mode: not-used`).

---

## §8 Slice 3 Acceptance & Readback (2026-09-08)

- Received `07_report_00.md` from Worker Session 07 (`AIOS-S3-ENDGAME-SOLVER`).
- Mutation & Verification:
  * Commit: `6e20a4f5e901ebbcd4354e77a3e103ff2bcdfa8b`
  * Pre-push check passed against `68afb6df92fccb2996ae83f1a444e4ada7396d10`.
  * Post-push readback confirmed: `origin/main == HEAD == 6e20a4f5e901ebbcd4354e77a3e103ff2bcdfa8b`.
  * 19 files modified/created across backend gamecore, Django services, tests, and frontend SSE move route.
  * Major Deliverables Landed:
    - `backend/gamecore/tile_tracking.py`: Pure-Python public unseen-pool builder (`LateGameContext`) calculating unseen tiles without private information leakage, expanding into exact opponent rack when `bag == 0`.
    - `backend/gamecore/endgame.py`: Iterative-deepening minimax solver with alpha-beta pruning and 4,096-entry transposition table, modeling terminal swings ($2 \times \text{opponent leftover}$). Bounded to 1,250 ms live budget and 10,000 state expansions.
    - `backend/gamecore/leave_equity.py`: `pre_endgame_equity_cp` with transition burden and premium-exposure penalty.
    - `frontend/src/app/api/ai/move/route.ts`: Preserves backend recommendation order when `strategy_mode` is present, preventing raw-score sorting from overriding multi-turn endgame out-play sequences.
    - New test suites: `test_tile_tracking.py`, `test_endgame.py`, `test_pre_endgame.py`, `test_endgame_services.py`, `test_endgame_benchmark.py`.
  * Empirical Performance Improvements (Proven):
    - Paired A/B benchmark (100 seeds: 50 English + 50 Slovak):
      * English 50: ranked-out increased from 49 to **50/50 (100% out-play completion)**.
      * Slovak 50: spread increased by **+210 points**; ranked-out increased from 34 to **38/50**, bag-empty from 39 to 41/50.
      * Slovak seed 1 converted from `SIX_CONSECUTIVE_ZERO_SCORES` to `BAG_EMPTY_AND_PLAYER_OUT` with +38 spread expansion.
      * Combined 100 seeds: Total spread increased (+4 net), ranked-out increased from 83 to **88/100**, bag-empty from 88 to **91/100**.
  * Quality gates:
    - Backend: `mypy` clean (102 source files), `ruff` clean, `pytest` clean across all 1109 tests.
    - Frontend: `typecheck` clean, `lint` clean, `vitest` (167 passed).
- **Slice 3 (Pre-Endgame Tile Tracking & Exact Endgame Minimax Solver) is ACCEPTED.**

---

## §9 Session 08 Evaluation & Plan Acceptance (2026-09-08)

- Received `08_report_00.md` from Worker Session 08 (`AIOS-SLICE-4-PLAN`).
- Findings & Evaluation:
  * Unified midgame board defense formula:
    $\text{Utility}(m) = 100 \cdot \text{total\_score}(m) + \text{leave\_equity\_cp}(m) - D(m)$,
    with $D(m) \in [-800, 3000]\text{ cp}$ (from $+8$ points denial/closure bonus to $-30$ points catastrophic premium exposure penalty).
  * Fast anchor-based detection using flattened bitboards and access channels without recursive move generation.
  * Score-differential posture: $\le -60$ (trailing comeback opening bonus), $-59\dots -30$, $-29\dots +29$ (neutral), $+30\dots +59$, and $\ge +60$ (lockdown with closure and denial bonuses).
  * Pruning optimization: if $100 \cdot \text{score} + \text{leave} + 800 < \text{worst top\_k utility}$, skip defense evaluation.
  * StrategyMode: adds `"board_control"`, recognized by frontend SSE route to preserve backend strategic order.
  * Preserves historical position sets: explicitly sets `board_defense_enabled=False` during position set generation/replay, avoiding any asset regeneration.
  * Path allowlist: 14 files (12 backend, 2 frontend).
  * Plan accepted in full. Evidence tier: E2 (cross-cutting reversible).
  * Implementation grant will target Worker Session 09 in a fresh Worker session (`Native planning mode: not-used`).

---

## §10 Session 09 Implementation Evaluation (2026-09-08)

- Received `09_report_00.md` from Worker Session 09 (`AIOS-S4-BOARD-DEFENSE`). Status: `PARTIAL` / `implementation-PARTIAL`.
- Direct Orchestrator readback (not Worker claim):
  * `HEAD == origin/main == f6b6fff42736c5124b508fde319f8bf5ae96cfc3`
  * Message: `feat(gamecore): implement board control and defensive opportunity cost`
  * Working tree clean. AP pin unchanged: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.
- Implementation landed (14 allowlisted files, +1511 / −21):
  * `backend/gamecore/board_defense.py` — integer-centipoint midgame defense, bag > 7 only.
  * Ranked search ranks by `evaluation_cp`; emits `strategy_mode: "board_control"`.
  * Live probe enables defense with server-derived score differential.
  * SSE route recognizes `"board_control"` and preserves backend order.
  * Position sets remain frozen via explicit `board_defense_enabled=False`.
- Default E2 gates (Worker-observed, not re-run at this evaluation):
  * mypy 103 files clean; ruff clean.
  * Full pytest: 1128 passed, 6 skipped.
  * Frontend: typecheck clean, lint clean, vitest 74 passed (move route + turn simulation).
- Compatibility deviation (lawful, allowlist-preserving):
  * `board_control` is a **top-level** payload marker only; `search` keeps the five-key midgame shape so unlisted `test_api.py` stays green. Frontend reads top-level `strategy_mode`.
- Opt-in D7: **not pytest-complete**.
  * English 100 (seeds 300–349, both seats): paired spread **+494** (mean **+4.94**), WR 0.500=0.500, opponent PPT 37.15 → 35.57, 100/100 `BAG_EMPTY_AND_PLAYER_OUT`.
  * Slovak: 6/20 pairs only (seeds 0–2); partial mean +47.83. Seeds 3–9 missing.
  * `LIBRETILES_RUN_STRENGTH_ACCEPTANCE` 100-game (legacy, defense off) **never started**.
- **Slice 4 implementation is ACCEPTED as landed product.** Residual measurement (Slovak D7 remainder + 100-game strength command) is **not** a revert trigger. Coefficients were not retuned.
- Whole `ai-opponent-strength` remains **not-closed**. Next logical slice is not selected until the Cooperator picks the residual-measurement vs proceed-to-next-slice decision.

---

## §11 Session 10 Evaluation & Scope Guard for Slice 5 (2026-09-08)

- Received `10_report_00.md` from Worker Session 10 (`AIOS-SLICE-5-PLAN`).
- Scope Analysis & Orchestrator Decision:
  * The Worker proposed an unauthorized scope expansion: rewriting the Zustand store from v6 to v7, removing user-facing settings (`aiTimeout`, `aiMaxSteps`), altering `AIThinkingOverlay`, and modifying 34+ frontend and documentation files.
  * Per AP Core Mandates and protocol rules, the Orchestrator strictly **rejects** this frontend store/UI deletion. The user settings, thinking-time UI, and store schemas remain intact and supported.
  * The implementation scope for Slice 5 is strictly bounded to the core objective:
    1. `frontend/src/lib/prompts.ts`: Implement structured candidate anchors with rich hook context (adjacent letters/runs, directions, open spans, reachable premiums) in `buildMoveUserPrompt` to eliminate 2D spatial coordinate hallucination. Add coordinate guidance to `validateMove` description. Keep `CORE_SHA256` pinned and unchanged.
    2. `backend/catalog/migrations/0014_strategic_seeded_prompts.py`: Hash-gated refresh of the 4 seeded `SEARCH_PROFILE` presets (`Initial`, `Fast Search`, `Short Hooks`, `Grandmaster`) adding CoT guidance for anchor selection, leave preservation, and score-differential posture.
    3. Live Verification: Run live NVIDIA NIM AI turns via `manage.py diagnose_ai_play` under the Cooperator's standing API authorization to observe non-zero `provider_candidate` authoring.
  * Path allowlist strictly bounded to ~8 files (prompts, migration, tests, diagnostic harness).
  * Implementation grant will target Worker Session 11 in a fresh Worker session (`Native planning mode: not-used`).

---

## §12 Slice 5 Acceptance & Readback (2026-09-08)

- Received `11_report_00.md` from Worker Session 11 (`AIOS-S5-ANCHORS-AND-STRATEGY`).
- Mutation & Verification:
  * Commit: `128116210a2a9e9394b0e57d3ef037acdd940ccf`
  * Pre-push check passed against `f6b6fff42736c5124b508fde319f8bf5ae96cfc3`.
  * Post-push readback confirmed: `origin/main == HEAD == 128116210a2a9e9394b0e57d3ef037acdd940ccf`.
  * 9 files modified/created across frontend prompts/tests and backend catalog migrations/tests.
  * Major Deliverables Landed:
    - `frontend/src/lib/prompts.ts`: Implemented rich structured candidate anchors in `anchorsFromCells` (adjacent runs, open spans, perpendicular cross-check indicators, reachable TW/TL/DW premiums) and explicit coordinate mapping guidance (`COORDINATE MAPPING & RULES`) in `buildMoveUserPrompt`.
    - `frontend/src/lib/prompts.baseline.fixture.ts`: Test-only frozen copy of baseline `buildMoveUserPrompt` from `f6b6fff` preserving historical `BASELINE_USER_PROMPT_SHA256` oracle.
    - System prompt core digest `CORE_SHA256` (`c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`) verified byte-identical.
    - `backend/catalog/migrations/0014_strategic_seeded_prompts.py`: Hash-gated reversible migration updating Initial, Fast Search, Short Hooks, and Grandmaster `SEARCH_PROFILE` presets.
    - Live NIM verification executed: `manage.py diagnose_ai_play` ran live against `nvidia/nemotron-3-super-120b-a12b`, scoring 84 points on ply ("BACKARE") under single-call-in-flight concurrency.
  * Quality gates:
    - Frontend: `typecheck` clean, `lint` clean, `vitest` (117/117 passed).
    - Backend: `mypy` clean (104 files), `ruff` clean, `pytest` on migrations and diagnostics clean (29/29 passed in 7.51s).
- **Slice 5 (Structured Candidate Anchors & LLM Strategic Direction) is ACCEPTED.**







