### Report for ORCHESTRATOR_CHAT

Logical whole identity: ai-opponent-strength
Worker session ordinal: 12, Worker exchange ordinal: 01
Visible context pressure: negligible (< 5% of 1M window utilized).

- Status: PASS
- Phase-qualified result: not-applicable
- Start commit: `128116210a2a9e9394b0e57d3ef037acdd940ccf`
- End commit: `128116210a2a9e9394b0e57d3ef037acdd940ccf`
- Changed files and purpose: none — this exchange mutates nothing
- Commit/push result: not-applicable
- Resolved Execution Issues / Near-Misses: none
- Pre-Existing Failure Classification: none

---

### D1: Code Hygiene, Architectural Layering, and "Spaghetti" Analysis

- **Layering Integrity**: `backend/gamecore/` remains strictly pure Python with zero imports from Django or `backend/game/` (proven via `python -c "import gamecore.leave_equity, gamecore.tile_tracking, gamecore.endgame, gamecore.board_defense, gamecore.move_search"` without Django initialization). The only Django reference in all of `gamecore/` is the pre-existing fallback in `assets.py` for optional `settings.ASSETS_DIR` path resolution.
- **Modularity & Separation of Concerns**: The four new modules each address an isolated domain:
  1. `leave_equity.py`: Pure rack-leave evaluation in integer centipoints. Computes base tile equity, V/C balance penalty matrices, duplicate penalties, and synergy bonuses without touching board state.
  2. `tile_tracking.py`: Deduces unseen tile pools solely from public state (variant distribution, board occupants, acting rack, opponent rack size). Never accesses private opponent rack contents or bag tile ordering.
  3. `endgame.py`: Bounded iterative-deepening minimax solver with alpha-beta pruning and transposition caching (4,096 entries) operating on private cloned boards.
  4. `board_defense.py`: Evaluates opponent premium exposure risk, lane closure, and opening bonuses using 225-bit integer bitboards and access channels without recursive move generation.
- **Data Integrity & Determinism**: All heuristics, leave valuations, minimax scores, and board defense penalties are expressed in integer centipoints (`CENTIPOINTS_PER_POINT = 100`). No floating-point arithmetic is used in candidate scoring or ranking. Candidate sorting in `_RankedSearcher._rank_key` provides 100% deterministic, byte-identical ordering:
  ```python
  (-candidate.evaluation_cp, -(1 if candidate.rack_out else 0), -candidate.tiles_used, candidate.canonical_key)
  ```
- **Dead Code and Drift**: Verified clean. Deprecated helpers (`_leave_components`, `_vowel_set`, `leave_value`) were purged in Slice 2. No orphaned functions or dead code remnants exist across the touched modules.

---

### D2: Game Invariants and Formed-Word Legality

- **The ONE Formed-Word Authority**: `WordAuthority.accepts_tokens` remains the sole certifier of formed-word legality. In `move_search.py`, candidate generation filters prefix validity via `authority.accepts_tokens(prefix)` and scores via `evaluate_scoring_move(..., authority=self.authority)`. The endgame solver (`endgame.py`) generates moves exclusively through `enumerate_certified_moves`, which re-certifies each candidate. The board defense evaluator (`board_defense.py`) performs zero word validation and merely adjusts utility on moves already certified by `evaluate_scoring_move`.
- **Parity Oracle**: Sections 1–4 of `backend/tests/test_word_authority_parity.py` remain untouched and green (`50 passed in 117.61s`). Parity with the frozen pre-collapse baseline oracle across English and Slovak tile sets is fully preserved.
- **Variant Invariants**: SSS 100 Slovak tiles, 12 variant definitions, multigraph token boundaries (`SZ`, `CS`, `CH`, `DZ`, `DŽ`), and blank zero-point scoring assignments remain strictly invariant and green (`test_atomic_tile_tokens.py` 24 passed in 5.99s, `test_multigraph_end_to_end.py` 9 passed in 2.06s, and variant suites 208 passed in 39.05s).

---

### D3: Engine / CPU Standalone Playability Analysis

In response to the Cooperator's question (*"Dokazal by Libre Tiles hrat proti userovi aj bez API volani? ... v Settings mat moznost nastavit hru proti CPU"*):

1. **Standalone CPU Capability**: The enhanced engine in `backend/gamecore/` is fully capable of playing as a standalone, zero-API "CPU opponent". It requires zero LLM API calls, zero network round-trips, and zero external credentials.
2. **Operational Policy**: `POLICY_RANKED_WITNESS_SAFE` (defined in `backend/gamecore/selfplay.py:311–321`) provides the ideal production CPU engine policy:
   - Evaluates moves via `find_ranked_scoring_moves` using the unified utility function:
     $$\text{Utility}(m) = 100 \cdot \text{total\_score}(m) + \text{leave\_equity\_cp}(m) - \text{defense\_penalty\_cp}(m)$$
   - Automatically activates the minimax solver (`solve_endgame`) when the bag is empty, and pre-endgame valuation (`pre_endgame_equity_cp`) when bag remaining is 1–7.
   - Falls back to `POLICY_WITNESS` (`find_legal_scoring_move`) only if ranked search returns no moves, guaranteeing that legal moves are never missed before authorizing a pass or exchange.
3. **Exact Technical Seam**:
   - **Frontend / Next.js Seam (Recommended)**: In Settings / Model Selector, expose a "Local Engine (CPU)" option (`modelId: "engine/cpu"`). When `selectedModelId === "engine/cpu"`, `/api/ai/move` bypasses LLM streaming, calls `GET /api/game/{id}/ai-candidates/`, takes `candidates[0]`, and immediately returns an SSE terminal with `completion_source: "backend_ranked_candidate"` and submits the move to Django. Turn execution takes ~15–50 ms.
   - **Backend Seam**: In Django `PlayerSlot`, a seat with `is_ai=True, ai_model=None` (or `ai_model="engine"`) can be advanced by calling `_probe_ai_ranked_candidates()` and `submit_move()` directly in Django services.
4. **Current Engine Strength**:
   - English 100-game acceptance against first-witness baseline: **+47,395 aggregate spread (+473.95 points/game)**, **100% win rate (100/0/0)**, and **100% `BAG_EMPTY_AND_PLAYER_OUT` completion**.
   - Paired board-defense benchmark: reduces opponent points per turn from 37.15 to 35.57.
   - Slovak self-play: completely eliminates the consonant/diacritic clog stall, converting former `SIX_CONSECUTIVE_ZERO_SCORES` deadlocks into 100% `BAG_EMPTY_AND_PLAYER_OUT` finishes.

---

### D4: LLM Integration, Prompt Engineering, and Anchor Quality

- **Structured Anchors Evaluation**: `frontend/src/lib/prompts.ts` replaces flat coordinate pairs with rich hook context in `anchorsFromCells`:
  - Adjacent runs with exact indices and letter sequences (e.g., `E:(7,8..10)=[R|A|T|E]`).
  - Open orthogonal spans (e.g., `ACROSS W3/E5; DOWN N2/S4`).
  - Cross-check context indicating perpendicular word boundaries (`cross=free` or `cross=[S|_|ED]`).
  - Reachable high-value premiums within physical 7-tile rack capacity (`reaches TW at (0,7)`).
  - Deterministic prioritization: anchors reaching TW/TL/DW premiums rank first, followed by largest open spans.
- **Coordinate Mapping Guidance**: `buildMoveUserPrompt` explicitly defines placement mechanics under `COORDINATE MAPPING & RULES`:
  - ACROSS increments col; DOWN increments row.
  - REUSE EXISTING TILES: strictly instructs the model to omit tiles already on board from the placements array, eliminating the primary cause of model-generated placement rejections.
- **System Prompt Preservation**: `CORE_SHA256` (`c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`) remains byte-identical. Historical user prompt compatibility is frozen and verified via `prompts.baseline.fixture.ts`.
- **Strategic Presets**: Migration `0014_strategic_seeded_prompts.py` hash-gates updates to the four seed rows (`Initial`, `Fast Search`, `Short Hooks`, `Grandmaster`), providing tailored chain-of-thought strategic guidance while preserving custom admin edits.

---

### D5: Test Suite Hygiene & Runtime Performance

- **Heavy vs Fast Tests**:
  - Pure unit and service integration tests are fast (< 15 seconds):
    `test_strategic_seeded_prompts_migration.py`, `test_tile_tracking.py`, `test_endgame.py`, `test_leave_equity.py`, `test_board_defense.py` pass 63 tests in **4.17s**.
    `test_board_defense_services.py` and `test_endgame_services.py` pass 8 tests in **12.95s**.
    Frontend `prompts.test.ts` and `atomic-tiles.test.ts` pass 117 tests in **290ms**.
  - **Hygiene Issue Identified**: Benchmark suites (`test_board_defense_benchmark.py`, `test_endgame_benchmark.py`, `test_strength_benchmark.py`, `test_slovak_strength.py`) contain un-skipped "default smoke" tests that simulate multi-ply 20,000-node games. This causes a bare `pytest` run to take over 10 minutes.
  - When acceptance env vars (`LIBRETILES_RUN_BOARD_DEFENSE_ACCEPTANCE=1` or `LIBRETILES_RUN_STRENGTH_ACCEPTANCE=1`) are enabled, the runner executes 100 to 240 full games, taking **1 to 4 hours**. These must remain strictly opt-in.
- **Search Latency & Safety Caps**:
  - Midgame search is bounded by `DEFAULT_RANKED_MAX_ELAPSED_MS = 750` and `DEFAULT_RANKED_MAX_NODES = 20_000`.
  - Endgame solver is bounded by `ENDGAME_MAX_ELAPSED_MS = 1250`, `ENDGAME_MAX_EXPANSIONS = 10_000`, and `ENDGAME_TT_MAX_ENTRIES = 4_096`.
  - Live probe in `services.py` enforces these budgets; exceeding a deadline degrades gracefully to partial candidates or `bounded`/`indeterminate` without hanging.

---

### D6: Findings, Technical Debt, and Recommendations

- **Critical / Blocker**:
  - None (0). All functional, game-theoretic, and safety invariants are intact.
- **Medium / Material**:
  - **M1: Default Benchmark Game Simulation in Pytest**:
    - *Finding*: Default tests in `test_board_defense_benchmark.py` (`test_default_paired_benchmark_terminates_and_engages_board_control`), `test_endgame_benchmark.py`, and `test_slovak_strength.py` execute full 20,000-node simulated games by default, causing standard `pytest` runs to take 10+ minutes.
    - *Recommendation*: Mark all full-game simulation tests with `@pytest.mark.slow` or gate them behind `LIBRETILES_RUN_BENCHMARKS=1`, allowing standard development `pytest` to finish in under 30 seconds.
  - **M2: Residual Slice 4 Slovak Acceptance Evidence**:
    - *Finding*: In Slice 4, the 100-game English paired board-defense acceptance finished (+494 spread, 100/100 outs), but Slovak seeds 3–9 were not run to full matrix completion.
    - *Recommendation*: Schedule a standalone background verification run for the remaining Slovak seeds when host resources allow.
- **Minor / Clean-up**:
  - **m1: Anchor Count in `anchorsFromCells`**:
    - *Finding*: `anchorsFromCells` formats all anchor candidates without a cardinality cap (`candidates.map(...).join("\n")`). On dense midgame boards, this can emit 30–50 lines of anchors (~1,000 tokens).
    - *Recommendation*: Cap at top 15–20 anchors (`.slice(0, 20)`) to conserve LLM attention and context window budget.
  - **m2: Vitest Native Config Warning**:
    - *Finding*: Vitest emits `ESM syntax in a file loaded as CommonJS (vitest.config.ts)`.
    - *Recommendation*: Set `VITE_CONFIG_NATIVE_IGNORE_WARNING=true` in `vitest.config.ts` or rename to `vitest.config.mts`.
