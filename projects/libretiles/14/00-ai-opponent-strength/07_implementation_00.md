You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An approved plan grants you nothing; THIS prompt does.

```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 07
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: AIOS-S3-ENDGAME-SOLVER — implement public tile tracking (tile_tracking.py), exact out-play minimax solver (endgame.py), pre-endgame adjustments, pipeline integration, and frontend candidate order preservation, verify benchmark elevation and quality gates, land one commit, push, and read back.
Phase: implementation
Exact baseline: 68afb6df92fccb2996ae83f1a444e4ada7396d10
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Evidence tier: E2
Evidence tier basis: cross-cutting reversible mutation across backend gamecore (tile tracking, endgame minimax solver, move search integration), Django service layer, tests, and frontend SSE candidate order preservation. No external network beyond authorized Git push, no provider spend, no migration, no schema change.
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named risk: In the endgame (`bag == 0`), unseen tiles equal the opponent's rack with 100% certainty. Implementing minimax out-play search with alpha-beta pruning enables the AI to find guaranteed out-play sequences or defensively block the opponent from going out, capturing massive score swings ($2 \times \text{opponent leftover}$). Search bounds (1,250 ms, 10,000 state expansions, 4,096 transposition table entries) must be strictly enforced to avoid timeouts. The frontend merge function in `route.ts` must preserve strategic late-game candidate ordering.

## Execution Rules & Environment Invariants

- ⛔ **RF-16 Mandatory Deviation**: Cursor AppImage intercepts `python*`. Always use `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/` from `backend/`. Never use ambient `python`, `python3`, or `poetry run`.
- ⛔ **Testing Rule**: Never type `PYTHON_DOTENV_DISABLED=1` on shell commands. Use standard `.venv/bin/python`.
- ⛔ **Pytest Warning**: `backend/pyproject.toml` already sets `addopts = "-q"`. Never add a second `-q`.
- ⛔ **Word Authority Invariant**: Formed-word legality is determined solely by `WordAuthority.accepts_tokens`. Never weaken validation. Sections 1–4 of `test_word_authority_parity.py` are the untouchable test oracle.

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
backend/gamecore/game.py                                  Game, PlayerState, GameEndReason, determine_end_reason, apply_final_scoring.
backend/gamecore/move_search.py                           _RankedSearcher, find_ranked_scoring_moves, RankedMoveCandidate, _rank_key.
backend/gamecore/leave_equity.py                          LeaveEquityProfile, leave_equity_cp.
backend/gamecore/selfplay.py                              simulate_engine_game, SelfPlayConfig, POLICY_RANKED_BEST, POLICY_RANKED_WITNESS_SAFE.
backend/gamecore/board.py                                 Board, Cell.
backend/gamecore/legality.py                              evaluate_scoring_move.
backend/game/services.py                                  _check_endgame, _probe_ai_ranked_candidates.
backend/game/position_sets.py                             game_from_snapshot.
frontend/src/app/api/ai/move/route.ts                     mergeCandidateRecommendations (lines 490-520) and prompt assembly.
/home/agile/meta/projects/libretiles/14/00-ai-opponent-strength/06_report_00.md the approved technical plan for Slice 3.
```

## 1. Repository Gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 68afb6df92fccb2996ae83f1a444e4ada7396d10
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before you start
```

## 2. Path Allowlist (Strictly Enforced)

You are authorized to modify or create **ONLY** these 19 paths:
1. `backend/gamecore/tile_tracking.py` (new)
2. `backend/gamecore/endgame.py` (new)
3. `backend/gamecore/leave_equity.py`
4. `backend/gamecore/move_search.py`
5. `backend/gamecore/selfplay.py`
6. `backend/game/services.py`
7. `backend/game/position_sets.py`
8. `backend/tests/test_tile_tracking.py` (new)
9. `backend/tests/test_endgame.py` (new)
10. `backend/tests/test_pre_endgame.py` (new)
11. `backend/tests/test_endgame_services.py` (new)
12. `backend/tests/test_endgame_benchmark.py` (new)
13. `backend/tests/test_move_search.py`
14. `backend/tests/test_strength_benchmark.py`
15. `backend/tests/test_slovak_strength.py`
16. `backend/tests/test_endgame_policy_matrix.py`
17. `backend/tests/test_position_sets.py`
18. `frontend/src/app/api/ai/move/route.ts`
19. `frontend/src/app/api/ai/move/route.test.ts`

⛔ Any mutation outside this allowlist is strictly unauthorized.

## 3. Implementation Specifications

Follow the approved technical plan in `06_report_00.md`:

### 3.1 Public Tile Tracking (`backend/gamecore/tile_tracking.py`)
1. Implement pure-Python context builder with zero private information leakage:
   ```python
   unseen = Counter(variant.distribution)
   # subtract all board tokens
   for row in board.cells:
       for cell in row:
           if cell.token is not None:
               unseen[cell.token] -= 1
   # subtract acting player's rack
   for token in acting_rack:
       unseen[token] -= 1
   ```
2. Data class `LateGameContext`:
   - `bag_remaining: int`
   - `unseen_tiles: Counter[str]` (canonically sorted items)
   - `opponent_rack_size: int`
   - `consecutive_scoreless_turns: int`
   - `opponent_action_rules: str` ("ai_scoring" | "human_open")
3. Verification and bounds:
   - Active only when 2 players and $0 \le \text{bag\_remaining} \le 7$.
   - Validates non-negative counts and $\sum \text{unseen} == \text{bag\_remaining} + \text{opponent\_rack\_size}$.
   - If `bag_remaining == 0`, expands unseen into exact opponent rack.
   - If invalid or unavailable, returns `None`, gracefully falling back to standard midgame search.

### 3.2 Pre-Endgame Heuristics (`backend/gamecore/leave_equity.py`)
When $1 \le \text{bag\_remaining} \le 7$:
- Implement `pre_endgame_equity_cp(leave, *, unseen_tiles, bag_remaining, opponent_rack_size, profile, tile_points)`:
  1. Transition burden: blend current leave equity toward expected leftover burden based on unseen tiles:
     $T = -100 \times \left(F(L) + d \times \frac{F(\text{unseen})}{N}\right)$
     $\text{transition\_equity} = \frac{b_{\text{after}} \times E + (7 - b_{\text{after}}) \times T}{7}$
  2. Unrepairable imbalance penalty: if unseen pool has severe vowel/consonant scarcity.
  3. Premium exposure penalty: penalize opening access to unused triple/double word scores when unseen pool contains high-value tiles ($F \ge 8$).
  4. Clamp and combine using deterministic integer arithmetic.

### 3.3 Exact Endgame Minimax Solver (`backend/gamecore/endgame.py`)
When `bag_remaining == 0`:
1. **Search Architecture**:
   - Iterative deepening minimax with alpha-beta pruning.
   - Search depths 1, 3, 5... (covering my move $\to$ opponent reply $\to$ my out-play).
   - Transposition table (capped at 4,096 entries) keyed by (board state, racks, side, scoreless turns).
   - Bounded execution: total budget 1,250 ms, minimax state expansions $\le 10,000$, retained placements $\le 25,000$.
2. **Terminal Spread Valuation**:
   - Immediate out: $\text{my\_score} + 2 \times \text{opponent\_leftover}$
   - Opponent goes out after my move: $\text{my\_score} - \text{opponent\_score} - 2 \times \text{my\_leftover}$
   - 2-ply out: $\text{my\_score\_1} - \text{opponent\_score} + \text{my\_score\_2} + 2 \times \text{opponent\_remaining\_points}$
   - Deadlock / 6 scoreless turns: accumulated score $+ \text{opponent\_leftover} - \text{my\_leftover}$
3. **Placements Generation**:
   - Uses `_RankedSearcher` enumeration seam and re-certifies each move via `evaluate_scoring_move`.
   - AI opponent nodes allow positive scoring placements, and pass only when no legal move exists.
   - Human opponent nodes also allow voluntary passes and zero-score legal placements.
4. **Metadata & Certificates**:
   - `EndgameSearchResult`: `candidates`, `status`, `strategy_mode` ("exact" | "bounded" | "unavailable"), `completed_depth`, `out_in_two` ("proven" | "refuted" | "unknown").

### 3.4 Move Search & Self-Play Integration
1. In `backend/gamecore/move_search.py`:
   - Add optional parameter `late_game_context: LateGameContext | None = None` to `find_ranked_scoring_moves`.
   - When `late_game_context` is present and eligible, invoke `endgame.solve_endgame` (for bag==0) or pre-endgame equity adjustment.
   - Attach strategy metadata to `RankedSearchResult`.
2. In `backend/gamecore/selfplay.py`:
   - Add `late_game_enabled: bool = True` to `SelfPlayConfig`.
   - In `_choose`, construct `LateGameContext` for eligible turns ($0 \le \text{bag} \le 7$).
3. In `backend/game/services.py`:
   - In `_probe_ai_ranked_candidates`, build `LateGameContext` and pass to `find_ranked_scoring_moves`.
   - When strategic endgame search succeeds, mark candidates with strategy metadata (`strategy_mode: "exact" | "bounded"`).
4. In `backend/game/position_sets.py`:
   - Pass `late_game_context` consistently during position reconstruction.

### 3.5 Frontend SSE Candidate Order Preservation
In `frontend/src/app/api/ai/move/route.ts`:
- In `mergeCandidateRecommendations` (around line 494):
  Check if backend response carries `strategy_mode` ("exact" or "bounded") or late-game marker.
  If present, **preserve the backend candidate order** (do not re-sort by raw immediate score!).
  Place backend strategic candidates first, followed by deduplicated provider candidates.
- Add focused tests in `frontend/src/app/api/ai/move/route.test.ts`.

### 3.6 Test Suites and Benchmarks
1. `backend/tests/test_tile_tracking.py`:
   - Test inventory subtraction across English, Slovak, and variants.
   - Test assigned blanks, multigraphs, bag counts 0, 1, 7, 8.
   - Test error handling for malformed boards, negative residuals, and wrong player counts.
2. `backend/tests/test_endgame.py`:
   - Test immediate out-play (+55 swing case).
   - Test 2-ply out-play setup (lower immediate score setting up guaranteed out).
   - Test defensive blocking against opponent's out-play threat.
   - Test transposition table, node caps, and time deadline cutoff.
3. `backend/tests/test_pre_endgame.py`:
   - Test transition burden and vowel scarcity penalties when $1 \le \text{bag} \le 7$.
4. `backend/tests/test_endgame_services.py`:
   - Test Django service integration: `_probe_ai_ranked_candidates` builds context and returns strategy marker.
5. `backend/tests/test_endgame_benchmark.py`:
   - Paired A/B benchmark (with vs without late_game_enabled) on English (seeds 300-349) and Slovak (seeds 0-49).
   - Verify `BAG_EMPTY_AND_PLAYER_OUT` completion and spread expansion.
6. Verify and maintain green status on existing regression suites:
   `test_move_search.py`, `test_strength_benchmark.py`, `test_slovak_strength.py`, `test_endgame_policy_matrix.py`, `test_position_sets.py`.

## 4. Verification Procedures

Execute and ensure clean exit (0) on:

From `backend/`:
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_tile_tracking.py tests/test_endgame.py tests/test_pre_endgame.py tests/test_endgame_services.py tests/test_move_search.py tests/test_leave_equity.py tests/test_strength_benchmark.py tests/test_slovak_strength.py tests/test_endgame_policy_matrix.py tests/test_position_sets.py tests/test_api.py tests/test_word_authority_parity.py
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
```

Extended benchmark acceptance:
```bash
LIBRETILES_RUN_STRENGTH_ACCEPTANCE=1 env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_strength_benchmark.py -s -k one_hundred
LIBRETILES_RUN_ENDGAME_ACCEPTANCE=1 env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_endgame_benchmark.py -s
```

From `frontend/`:
```bash
npm run typecheck
npm run lint
npx vitest run src/app/api/ai/move/route.test.ts src/lib/prompts.test.ts
```

## 5. Git Commit and Push Sequence

Stage ONLY the allowlisted files by explicit paths:
```bash
git add backend/gamecore/tile_tracking.py \
        backend/gamecore/endgame.py \
        backend/gamecore/leave_equity.py \
        backend/gamecore/move_search.py \
        backend/gamecore/selfplay.py \
        backend/game/services.py \
        backend/game/position_sets.py \
        backend/tests/test_tile_tracking.py \
        backend/tests/test_endgame.py \
        backend/tests/test_pre_endgame.py \
        backend/tests/test_endgame_services.py \
        backend/tests/test_endgame_benchmark.py \
        backend/tests/test_move_search.py \
        backend/tests/test_strength_benchmark.py \
        backend/tests/test_slovak_strength.py \
        backend/tests/test_endgame_policy_matrix.py \
        backend/tests/test_position_sets.py \
        frontend/src/app/api/ai/move/route.ts \
        frontend/src/app/api/ai/move/route.test.ts

git diff --staged --stat
```

Commit message:
```bash
git commit -m "feat(gamecore): implement pre-endgame tracking and exact endgame minimax solver"
```

Pre-push verification:
```bash
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "68afb6df92fccb2996ae83f1a444e4ada7396d10"
git push origin main
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "$(git rev-parse HEAD)"
```

## 6. Stopping Conditions

Stop and report immediately if:
- Repository gate fails before start or working tree is dirty.
- Solver causes unbounded latency (> 2500 ms) or memory exhaustion.
- Any test in `test_word_authority_parity.py` sections 1–4 fails (parity oracle compromised).
- Pre-push verification reveals remote diverged from `68afb6df92fccb2996ae83f1a444e4ada7396d10`.

## 7. Report Contract

Begin **exactly** with:
```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinate fields unchanged:
```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 07, Worker exchange ordinal: 01
```

Then provide the standard 11-item compact core:
- Status: `PASS | PARTIAL | BLOCKED`
- Phase-qualified result: `implementation-PASS`
- Start commit: `68afb6df92fccb2996ae83f1a444e4ada7396d10`
- End commit: `<exact SHA>`
- Changed files and purpose (explicit paths)
- Endgame benchmark comparison table (spread changes, out-play frequencies, latency metrics)
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
