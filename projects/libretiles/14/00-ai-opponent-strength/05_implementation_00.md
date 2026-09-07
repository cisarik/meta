You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An approved plan grants you nothing; THIS prompt does.

```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: AIOS-S2-RACK-EQUITY-REISSUE — implement the pure Python Rack Equity and Leave Valuation engine in backend/gamecore/leave_equity.py and wire it into move_search.py, replacing naive greedy scoring with combined utility ranking (Turn Score + Rack Leave Equity), update test_atomic_tile_tokens.py for declared-vowels leave equity, re-pin affected regression baselines, regenerate the diagnostic position set, verify strength elevation and quality gates, land one commit, push, and read back.
Phase: implementation
Exact baseline: 843251db8da0aee878c3462b14cfe8e73528b399
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Evidence tier: E2
Evidence tier basis: cross-cutting reversible mutation across pure Python gamecore (leave_equity.py, move_search.py), unit tests, position-set diagnostic asset regeneration, and strength benchmark verification. No trust boundary, no network beyond authorized Git push, no provider call, no migration, no schema change.
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Reissued following Worker Session 04's lawful BLOCKED report. `backend/tests/test_atomic_tile_tokens.py` is now on the allowlist, with explicit instructions for `test_declared_vowels_change_leave_quality_slovak_stays_on_default`. Pre-mutation baselines were already captured in Session 04 (cited below).

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1444-1462      Git and remote safety — every write needs the exact authority THIS prompt names
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   role and authority boundary
PROMPT_CONTRACTS.md:14-41   the report contract and the coordinate fields you echo
PROMPT_CONTRACTS.md:423-453 coordinate consistency and Worker Exchange Identity
AP.md:2453-2454      the CLOSED report-justification enum: `new-mutation`.
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it
   yourself.
```

## Mandatory reading

```text
/home/agile/Projects/libretiles/AGENTS.md                 the project brief ("Word validation" and "Making the AI stronger").
backend/gamecore/move_search.py                           _RankedSearcher, _rank_key, RankedMoveCandidate, find_ranked_scoring_moves.
backend/gamecore/selfplay.py                              SelfPlayConfig, simulate_engine_game, POLICY_RANKED_BEST, POLICY_RANKED_WITNESS_SAFE.
backend/tests/test_strength_benchmark.py                  engine benchmark matrix and test_node_bound_strength_regression_tuples.
backend/tests/test_slovak_full_game.py                    full-game termination test (note: uses POLICY_WITNESS).
backend/tests/test_word_authority_parity.py               ⛔ SECTIONS 1-4 ARE TEST ORACLE (DO NOT TOUCH); section 5 is move fixture.
backend/tests/test_move_search.py                         search unit tests.
backend/tests/test_slovak_ranked_search.py                Slovak ranked search tests.
backend/tests/test_atomic_tile_tokens.py                  section 4.9 lines 612-656 (declared vowels leave quality).
/home/agile/meta/projects/libretiles/14/00-ai-opponent-strength/03_report_00.md the approved technical plan for Slice 2.
/home/agile/meta/projects/libretiles/14/00-ai-opponent-strength/04_report_00.md the Session 04 pre-mutation baseline evidence.
```

## 1. Repository Gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 843251db8da0aee878c3462b14cfe8e73528b399
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before you start
```

## 2. Path Allowlist (Strictly Enforced)

You are authorized to modify or create **ONLY** these 15 paths:
1. `backend/gamecore/leave_equity.py` (new)
2. `backend/gamecore/move_search.py`
3. `backend/tests/test_leave_equity.py` (new)
4. `backend/tests/test_move_search.py`
5. `backend/tests/test_strength_benchmark.py`
6. `backend/tests/test_slovak_strength.py` (new)
7. `backend/tests/test_word_authority_parity.py` (⛔ section 5 move fixture pins ONLY; sections 1–4 oracle is forbidden)
8. `backend/tests/test_endgame_policy_matrix.py`
9. `backend/tests/test_api.py`
10. `backend/tests/test_atomic_tile_tokens.py` (section 4.9 declared-vowels test)
11. `backend/assets/diagnostics/position_sets/` (delete old english position set + add regenerated asset)
12. `backend/tests/test_position_sets.py`
13. `backend/tests/test_diagnostic_session.py`
14. `backend/tests/test_diagnostic_runner.py`
15. `backend/tests/test_diagnostic_admin.py`

⛔ Any mutation outside this allowlist is strictly unauthorized.

## 3. Pre-Mutation Baseline Evidence (from Session 04)

You do NOT need to re-run the 446s 100-game acceptance before mutating. Session 04 captured and verified these exact baseline numbers at this exact commit `843251d`:
- English Default 4-game (seeds 300–301): W/D/L 4/0/0, total spread +1887, avg +471.75
- English Node-bound tuples: (300, 0, +420), (300, 1, +505), (301, 0, +461), (301, 1, +501), all `BAG_EMPTY_AND_PLAYER_OUT`
- English 100-game acceptance (seeds 300–349): W/D/L 100/0/0, total +44320, avg +443.20, max_plies 44
- Slovak ranked baseline (seeds 0–4): seed 0: +586:533 (ply 26, OUT), seed 1: +486:480 (ply 25, OUT), seed 2: +466:535 (ply 26, OUT), seed 3: 353:581 (ply 31, SIX_ZERO), seed 4: 547:339 (ply 33, SIX_ZERO).

## 4. Implementation Specifications

### 4.1 Create `backend/gamecore/leave_equity.py`
Pure Python module with NO Django imports.
1. **Integer Centipoints Formulation**: All values in integer centipoints ($1\text{ point} = 100\text{ cp}$).
2. **`LeaveEquityProfile`**: Frozen dataclass containing:
   - `variant_slug: str`
   - `tile_equity_cp: Mapping[str, int]`
   - `vowels: frozenset[str]`
   - `balance_cp: Sequence[Sequence[int]]` (the 7-row table for $n=0..6$)
   - `duplicate_penalties_cp: Mapping[str, int]` (classes: vowel, consonant, S, blank)
   - `synergy_pairs_cp: Mapping[frozenset[str], int]`
3. **`profile_for_variant(variant, tile_points)`**:
   - Resolves variant slug or object via `tiles._resolve_variant`.
   - **Declared Vowels Priority**: If `getattr(variant, "vowels", None)` is provided and not empty, use `frozenset(str(t) for t in variant.vowels)` as the profile's `vowels`.
   - Otherwise, if slug is `"slovak"`:
     * Base tile equity:
       `?`: +2500,
       `A`: +150, `E`: +150, `S`: +150, `T`: +150, `O`: +100, `I`: +100, `N`: +100, `R`: +100,
       `V`: +50, `M`: +50, `D`: +50, `L`: +50, `K`: 0, `P`: 0, `U`: -50,
       `J`: -100, `Á`: -100, `C`: -150, `H`: -150, `Z`: -150, `Í`: -150,
       `B`: -200, `Š`: -200, `Y`: -250, `Č`: -250, `Ž`: -250, `Ý`: -300,
       `Ľ`: -350, `Ť`: -350, `Ú`: -350, `É`: -400, `Ň`: -400, `Ô`: -400,
       `Ď`: -450, `F`: -450, `G`: -450, `Ó`: -550, `Ä`: -600, `Ĺ`: -600, `Ŕ`: -600, `X`: -650.
     * Vowels: `frozenset("AÁÄEÉIÍOÓÔUÚYÝ")`.
     * Synergy pairs: `(O, V)`: +50, `(S, T)`: +50, `(N, I)`: +40, `(E, N)`: +40, `(A, K)`: +40, `(P, R)`: +40.
     * Duplicate penalties: vowel: -75, consonant: -125, blank: -1000.
   - If slug is `"english"`:
     * Base tile equity:
       `?`: +2500, `S`: +800, `E`: +350, `R`: +150, `X`: +150,
       `A`: +100, `H`: +100, `N`: +50, `M`: +50, `C`: 0, `T`: 0,
       `D`: -50, `K`: -50, `L`: -50, `P`: -50, `I`: -100,
       `O`: -150, `G`: -200, `Y`: -200, `J`: -250, `F`: -250,
       `B`: -300, `Z`: -300, `W`: -350, `U`: -450, `V`: -550, `Q`: -700.
     * Vowels: `frozenset("AEIOU")`.
     * Synergy pairs: `(Q, U)`: +600, `(E, R)`: +75, `(?, S)`: +100, `(S, T)`: +50, `(E, S)`: +50, `(I, N)`: +50, `(A, N)`: +40, `(E, D)`: +40.
     * Duplicate penalties: vowel: -75, consonant: -125, S: -300, blank: -1000.
   - Universal Fallback (any other variant without declared vowels):
     * Vowels: NFKD decomposition base letter in `AEIOU`.
     * blank: +2500
     * vowel: $\text{clamp}(200 - 80 \cdot (\text{points} - 1), -400, 200)$
     * consonant: $\text{clamp}(150 - 80 \cdot (\text{points} - 1) + 25 \cdot \min(\text{count} - 1, 5), -700, 300)$
     * Empty synergy map, standard duplicate penalties.
4. **V/C Balance Table `BALANCE_CP`**:
   ```python
   BALANCE_CP = (
       (0,),
       (0, 0),
       (-100, 0, -150),
       (-300, 0, -100, -450),
       (-600, -100, 0, -300, -800),
       (-1000, -300, 0, -150, -700, -1200),
       (-1500, -500, -100, -50, -400, -900, -1800),
   )
   ```
   Each blank in leave halves the balance penalty: `penalty // (2 ** b)`.
5. **`leave_equity_cp(leave: Mapping[str, int], *, profile: LeaveEquityProfile, bag_count: int, tile_points: Mapping[str, int]) -> int`**:
   - If `bag_count == 0`: return $-100 \cdot \sum_{t} \text{tile\_points}[t] \cdot \text{count}$.
   - Else: sum base equities, balance penalty, duplicate penalties, synergy bonuses. Clamp total to $[-3000, 6000]$.

### 4.2 Create `backend/tests/test_leave_equity.py`
Unit test suite verifying profile resolution (en, sk, fallback, declared vowels), blank retention equity (+2500) vs 1-point face score, Q-with-U vs Q-without-U synergy, balance curve extremes, duplicate escalation, endgame mode switch when `bag_count == 0`, determinism, and clamping bounds.

### 4.3 Update `backend/gamecore/move_search.py`
1. `RankedMoveCandidate`:
   - Rename field `leave_value: int` to `leave_equity_cp: int`.
2. `_rank_key`:
   ```python
   @staticmethod
   def _rank_key(candidate: RankedMoveCandidate) -> tuple[object, ...]:
       return (
           -(candidate.total_score * 100 + candidate.leave_equity_cp),
           -(1 if candidate.rack_out else 0),
           -candidate.tiles_used,
           candidate.canonical_key,
       )
   ```
3. `_RankedSearcher`:
   - Initialize `self.profile = profile_for_variant(variant, tile_points)`.
   - Add `self._leave_cache: dict[tuple[tuple[str, int], ...], int] = {}`.
   - Replace `_leave_components` with `_calculate_leave_equity(placed)` that constructs the remaining multiset, checks/updates `self._leave_cache`, and calls `leave_equity_cp`.
   - Delete `_leave_components` and `_vowel_set`.
4. Ensure `find_ranked_scoring_moves` signature remains completely backward compatible.

### 4.4 Update `backend/tests/test_atomic_tile_tokens.py`
In section 4.9 (`test_declared_vowels_change_leave_quality_slovak_stays_on_default`):
Update the test to verify that declared vowels affect leave equity through `_calculate_leave_equity` (or `searcher.profile.vowels`):
```python
    def _leave_equity(variant: object) -> int:
        searcher = _RankedSearcher(
            board=Board(get_premiums_path()),
            rack=["Á", "B"],
            authority=WordAuthority.from_words(("ÁB", "BÁ")),
            bag_count=10,
            top_k=1,
            max_nodes=1,
            max_elapsed_ms=10,
            max_unique_placements=1,
            tile_points={"Á": 4, "B": 4},
            blank_letters=("Á", "B"),
            variant=variant,
        )
        return searcher._calculate_leave_equity([])

    default_equity = _leave_equity(slovak)
    declared_equity = _leave_equity(declared)
    assert default_equity != declared_equity
```
And verify that in `declared`, `searcher.profile.vowels` contains `Á`.

### 4.5 Update Other Construction Sites and Existing Tests
1. `backend/tests/test_move_search.py`:
   - Update tests asserting on `RankedMoveCandidate.leave_value` to `leave_equity_cp`.
   - Update `test_ranked_search_is_deterministic_and_immediate_score_dominates` and `test_ranked_midgame_prefers_stronger_collins_move` to assert utility-based ordering and re-measure deterministic top.
2. `backend/tests/test_word_authority_parity.py`:
   - **DO NOT TOUCH sections 1–4 (the oracle)!**
   - In section 5 (`test_ranked_search_matches_the_pinned_baseline`), update `leave_equity_cp` pin to the newly measured value.
3. `backend/tests/test_endgame_policy_matrix.py` & `backend/tests/test_api.py`:
   - Update `leave_value=` keyword arguments to `leave_equity_cp=`.
4. `backend/tests/test_strength_benchmark.py`:
   - Re-pin `test_node_bound_strength_regression_tuples` with measured tuples under new ranking.
   - Verify `test_ranked_strategy_beats_first_witness_on_default_balanced_seeds` passes with spread > 0.
5. Create `backend/tests/test_slovak_strength.py`:
   - Test Slovak ranked strategy vs witness on balanced seeds.
   - Test full Slovak ranked self-play game verifying tile conservation and proper termination.

### 4.6 Regenerate Position Set Asset
1. Run:
   ```bash
   env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py generate_position_set --variant-slug english
   ```
2. Locate the new position set JSON under `backend/assets/diagnostics/position_sets/` (e.g. `english-<new_digest>.json`).
3. Delete the obsolete `backend/assets/diagnostics/position_sets/english-f5ae61b4.json`.
4. Update the pinned digest constant in the four test files:
   - `backend/tests/test_position_sets.py`
   - `backend/tests/test_diagnostic_session.py`
   - `backend/tests/test_diagnostic_runner.py`
   - `backend/tests/test_diagnostic_admin.py`

## 5. Verification Procedures

Execute and ensure clean exit (0) on:

From `backend/`:
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_leave_equity.py tests/test_move_search.py tests/test_strength_benchmark.py tests/test_slovak_strength.py tests/test_word_authority_parity.py tests/test_position_sets.py tests/test_atomic_tile_tokens.py
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
LIBRETILES_RUN_STRENGTH_ACCEPTANCE=1 env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_strength_benchmark.py -s -k one_hundred
```

From `frontend/`:
```bash
npm run typecheck
npx vitest run src/lib/prompts.test.ts
```

## 6. Git Commit and Push Sequence

Stage ONLY the allowlisted files by explicit paths:
```bash
git add backend/gamecore/leave_equity.py \
        backend/gamecore/move_search.py \
        backend/tests/test_leave_equity.py \
        backend/tests/test_move_search.py \
        backend/tests/test_strength_benchmark.py \
        backend/tests/test_slovak_strength.py \
        backend/tests/test_word_authority_parity.py \
        backend/tests/test_endgame_policy_matrix.py \
        backend/tests/test_api.py \
        backend/tests/test_atomic_tile_tokens.py \
        backend/assets/diagnostics/position_sets/ \
        backend/tests/test_position_sets.py \
        backend/tests/test_diagnostic_session.py \
        backend/tests/test_diagnostic_runner.py \
        backend/tests/test_diagnostic_admin.py

git diff --staged --stat
```

Commit message:
```bash
git commit -m "feat(gamecore): implement rack equity and leave valuation in move search"
```

Pre-push verification:
```bash
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "843251db8da0aee878c3462b14cfe8e73528b399"
git push origin main
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "$(git rev-parse HEAD)"
```

## 7. Stopping Conditions

Stop and report immediately if:
- Repository gate fails before start or working tree is dirty.
- Baseline 100-game strength acceptance drops below baseline spread (negative result).
- Any test in `test_word_authority_parity.py` sections 1–4 fails (verdict parity compromised).
- Pre-push verification reveals remote diverged from `843251db8da0aee878c3462b14cfe8e73528b399`.

## 8. Report Contract

Begin **exactly** with:
```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinate fields unchanged:
```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 05, Worker exchange ordinal: 01
```

Then provide the standard 11-item compact core:
- Status: `PASS | PARTIAL | BLOCKED`
- Phase-qualified result: `implementation-PASS`
- Start commit: `843251db8da0aee878c3462b14cfe8e73528b399`
- End commit: `<exact SHA>`
- Changed files and purpose (explicit paths)
- Pre- and post-change empirical benchmark comparison table (100-game spread, W/D/L, Slovak ranked metrics)
- Gate summaries (mypy, ruff, full pytest, vitest)
- Commit and push result (SHA and readback check)
- Deviations, risks, or missing evidence: none | <details>
- One smallest next step
- Report justification: `new-mutation`
- Explicit authority-expiry statement

Plus the two analytical fields:
```text
Orchestration critique: none | <findings> (labelled MEASURED and LEAD)
Enumeration widened: none | <surfaces not reached>
```
