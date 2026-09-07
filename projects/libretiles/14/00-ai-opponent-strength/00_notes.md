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

## §2 Session 01 Evaluation & Plan Acceptance (2026-09-07)

- Received `01_report_00.md` from Worker Session 01 (`AIOS-SLICE-1-PLAN`).
- Findings & Evaluation:
  * Full 12-variant inventory (D1) verified against `backend/assets/variants/*.json` and `backend/assets/dicts/`.
  * All 10 new native MovePromptSpec exemplars (D2) and shed tiles (D3) verified: words exist in target lexicons, scores match `premiums.json` DW center opening and unattached-first/pivot pattern.
  * JudgePromptSpec (D4) eliminates false Collins claims for all 10 non-English variants.
  * Dispatch architecture (D5) uses prototype-safe `ReadonlyMap` resolving `lexicon_id` first, then `variant`, with fallback to `englishMoveSpec`.
  * `CORE_SHA256` (`c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`) remains unchanged and pinned because `moveSystemPromptFor` template and `englishMoveSpec` are byte-identical.
  * Discovered adjacent defect: `frontend/src/app/api/ai/move/route.ts:1401-1406` had hardcoded "plausible English candidates" in `validateMove` tool description. Included in Slice 1 fix.
  * Plan accepted in full. Evidence tier: E1.
  * Implementation grant will target Worker Session 02 in a fresh Worker session (`Native planning mode: not-used`).


