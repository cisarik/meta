You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An approved plan grants you nothing; THIS prompt does.

```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 09
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: AIOS-S4-BOARD-DEFENSE — implement board control and defensive opportunity cost in gamecore/board_defense.py, wire into move_search.py, services.py, and frontend move route, adding dynamic score-differential posture and fast premium-exposure penalties, verify victory margin expansion and quality gates, land one commit, push, and read back.
Phase: implementation
Exact baseline: 6e20a4f5e901ebbcd4354e77a3e103ff2bcdfa8b
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Evidence tier: E2
Evidence tier basis: cross-cutting reversible mutation across backend gamecore (board defense, move search integration), Django services, selfplay, tests, and frontend SSE candidate order preservation. No external network beyond authorized Git push, no provider spend, no migration, no schema change.
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named risk: In Scrabble, pure greedy scoring or score + leave evaluation alone has a severe blind spot: opening unblocked premium squares (TW/TL) for the opponent's counter-strike. Board control penalizes reckless exposure of premium cells while adapting strategic posture based on score differential (lockdown when ahead by $\ge +30$, aggressive opening when trailing by $\le -30$). Evaluation must remain $O(1)$ fast per candidate to stay strictly within the 750 ms live search budget.

## Execution Rules & Environment Invariants

- ⛔ **RF-16 Mandatory Deviation**: Cursor AppImage intercepts `python*`. Always use `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/` from `backend/`. Never use ambient `python`, `python3`, or `poetry run`.
- ⛔ **Testing Rule**: Never type `PYTHON_DOTENV_DISABLED=1` on shell commands. Use standard `.venv/bin/python`.
- ⛔ **Pytest Warning**: `backend/pyproject.toml` already sets `addopts = "-q"`. Never add a second `-q`.
- ⛔ **Word Authority Invariant**: Formed-word legality is determined solely by `WordAuthority.accepts_tokens`. Never loosen validation. Sections 1–4 of `test_word_authority_parity.py` are the untouchable test oracle.
- ⛔ **Position Sets**: In `backend/game/position_sets.py`, keep `board_defense_enabled=False` during position set generation/remount to preserve the committed diagnostic asset and historical digests.

## Cooperator Standing Decision Record

The Cooperator has made an explicit standing decision: real provider API calls (including NVIDIA NIM) are authorized as needed for development until quota limits are hit ("volat real API kym nenarazime na limit"). While Slice 4 is algorithmic gamecore work and does not require provider calls, this decision enables provider-driven validation runs if relevant.

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
backend/gamecore/board.py                                 Board, Cell.
backend/gamecore/leave_equity.py                          LeaveEquityProfile, leave_equity_cp.
backend/gamecore/tile_tracking.py                         LateGameContext.
backend/gamecore/selfplay.py                              simulate_engine_game, SelfPlayConfig, POLICY_RANKED_BEST, POLICY_RANKED_WITNESS_SAFE.
backend/game/services.py                                  _probe_ai_ranked_candidates, submit_move.
backend/game/position_sets.py                             game_from_snapshot, _selfplay_config, _ranked_on_game.
frontend/src/app/api/ai/move/route.ts                     mergeCandidateRecommendations (lines 450-460, 490-520).
/home/agile/meta/projects/libretiles/14/00-ai-opponent-strength/08_report_00.md the approved technical plan for Slice 4.
```

## 1. Repository Gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 6e20a4f5e901ebbcd4354e77a3e103ff2bcdfa8b
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before you start
```

## 2. Path Allowlist (Strictly Enforced)

You are authorized to modify or create **ONLY** these 14 paths:
1. `backend/gamecore/board_defense.py` (new)
2. `backend/gamecore/move_search.py`
3. `backend/gamecore/selfplay.py`
4. `backend/game/services.py`
5. `backend/game/position_sets.py`
6. `backend/tests/test_board_defense.py` (new)
7. `backend/tests/test_board_defense_services.py` (new)
8. `backend/tests/test_board_defense_benchmark.py` (new)
9. `backend/tests/test_move_search.py`
10. `backend/tests/test_strength_benchmark.py`
11. `backend/tests/test_slovak_strength.py`
12. `backend/tests/test_position_sets.py`
13. `frontend/src/app/api/ai/move/route.ts`
14. `frontend/src/app/api/ai/move/route.test.ts`

⛔ Any mutation outside this allowlist is strictly unauthorized.

## 3. Implementation Specifications

Follow the approved technical design from `08_report_00.md`:

### 3.1 Create `backend/gamecore/board_defense.py`
Pure-Python module with NO Django imports.
1. **Evaluation Model**:
   Active only when `bag_remaining > 7`.
   $$\text{Utility} = 100 \cdot \text{total\_score} + \text{leave\_equity\_cp} - D(m)$$
   $$D(m) = \text{clamp}\left(\lfloor wR/100 \rfloor - \lfloor gG/100 \rfloor - \lfloor cC/100 \rfloor - \lfloor tV/100 \rfloor, -800, 3000\right)$$
   Where:
   - $R$: Newly exposed premium risk (capped at 2400 cp), based on top two positive exposure changes $p_1 + p_2 // 2 + 200 \times \min(2, \text{new\_lanes})$.
   - $G$: Premium opportunity denied / consumed (capped at 400 cp), $(n_1 + n_2 // 2) // 4$.
   - $C$: Anchor reduction / board closure (capped at 200 cp), $50 \times \max(0, \text{anchors\_before} - \text{anchors\_after})$.
   - $V$: High-variance opportunities opened (capped at 400 cp), $100 \times \min(2, \text{new\_TW\_or\_TL}) + 200 \times \min(1, \text{new\_lanes})$.
2. **Support Classes**:
   - Vowel: 150% support.
   - Low-hook consonant (<4 legal two-tile partner tokens via `WordAuthority.accepts_tokens`): 50% support.
   - Standard consonant: 100% support.
   - Anchor touching multiple cells uses highest support percentage.
3. **Premium Channel Geometry**:
   - Base weights: TW = 1000 cp, DW = 500 cp, TL = 600 cp.
   - Channels up to 3 cells away along orthogonal rays with distance attenuation: 100%, 60%, 35%, 20%.
4. **Score-Differential Posture**:
   Derived from pre-move $\Delta\text{Score} = \text{acting\_score} - \text{opponent\_score}$:
   - $\le -60$: $w=40, g=50, c=0, t=100$ (comeback opening)
   - $-59 \dots -30$: $w=65, g=75, c=0, t=50$
   - $-29 \dots +29$: $w=100, g=100, c=0, t=0$ (neutral)
   - $+30 \dots +59$: $w=150, g=150, c=100, t=0$ (leading defense)
   - $\ge +60$: $w=200, g=200, c=200, t=0$ (lockdown)
5. **Fast Incremental Evaluation**:
   Uses integer bitmasks over 225 cells ($15 \times \text{row} + \text{col}$), inverse dependency sets, and avoids full board copies.

### 3.2 Update `backend/gamecore/move_search.py`
1. Parameter additions to `find_ranked_scoring_moves`:
   `score_differential: int = 0`, `board_defense_enabled: bool = False`.
2. `RankedMoveCandidate`:
   - Append `defense_penalty_cp: int = 0`.
   - Add property `evaluation_cp: int`:
     Returns `self.total_score * 100 + self.leave_equity_cp - self.defense_penalty_cp`.
3. `_RankedSearcher`:
   - If `board_defense_enabled` and `bag_count > 7`, construct `BoardDefenseEvaluator(self.board, score_differential, authority, variant)`.
   - In `_try_complete`: after certifying move and calculating `leave_equity_cp`:
     * Pruning check: If top-k candidates are full and $100 \cdot \text{score} + \text{leave\_equity\_cp} + 800 < \text{worst utility}$, skip defense evaluation.
     * Else, compute `defense_penalty_cp`.
   - `_rank_key`:
     Order by:
     `(-(candidate.evaluation_cp), -(1 if candidate.rack_out else 0), -candidate.tiles_used, candidate.canonical_key)`
4. `StrategyMode`:
   Add `"board_control"`. Emit when `board_defense_enabled` ran in midgame.

### 3.3 Update `backend/gamecore/selfplay.py`
1. Add `board_defense_enabled: bool = False` and `player_board_defense_enabled: tuple[bool, bool] | None = None` to `SelfPlayConfig`.
2. In `_ranked_search`, pass acting seat's defense setting and current `acting_score - opponent_score`.
3. `POLICY_RANKED_BEST` and `POLICY_RANKED_WITNESS_SAFE` consume the resulting candidates in order.
4. Record `defense_penalty_cp` in trace decision.

### 3.4 Update `backend/game/services.py` & `backend/game/position_sets.py`
1. In `_probe_ai_ranked_candidates`:
   - Calculate `score_differential = active_slot.score - opponent_slot.score` (0 if no opponent).
   - Pass `board_defense_enabled=True` and `score_differential`.
   - Candidate payload carries strategy marker.
2. In `backend/game/position_sets.py`:
   - Explicitly pass `board_defense_enabled=False` in `_selfplay_config` and `_ranked_on_game` so committed position set `english-aaac5c27.json` and its tests remain untouched.

### 3.5 Update Frontend SSE Route (`frontend/src/app/api/ai/move/route.ts`)
1. In `mergeCandidateRecommendations`:
   Add `"board_control"` to the recognized strategy markers (alongside `"exact"`, `"bounded"`, `"pre_endgame"`).
   When present, **preserve backend recommendation order**! Backend strategic candidates come first, followed by deduplicated provider candidates.
2. In `frontend/src/app/api/ai/move/route.test.ts`:
   Add test verifying that `"board_control"` strategy marker preserves backend candidate order.

### 3.6 Create and Update Test Suites
1. `backend/tests/test_board_defense.py` (new):
   - Direct TW/TL exposure penalty vs safe placement.
   - Vowel vs consonant anchor support differences.
   - Denial bonus for consuming/blocking premium cells.
   - Posture shifts ($\le -60, -30, 0, +30, \ge +60$).
   - Pruning and determinism tests.
2. `backend/tests/test_board_defense_services.py` (new):
   - Test Django service layer derives correct differential and attaches `"board_control"`.
3. `backend/tests/test_board_defense_benchmark.py` (new):
   - Paired A/B benchmark (defense ON vs OFF) on English (seeds 300–349) and Slovak (seeds 0–9).
   - Gate with `LIBRETILES_RUN_BOARD_DEFENSE_ACCEPTANCE=1`.
   - Measure spread difference, opponent points per turn, and leading-posture reply suppression.
4. Ensure existing regression tests stay green:
   `test_move_search.py`, `test_strength_benchmark.py`, `test_slovak_strength.py`, `test_position_sets.py`.

## 4. Verification Procedures

Execute and ensure clean exit (0) on:

From `backend/`:
```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_board_defense.py tests/test_board_defense_services.py tests/test_move_search.py tests/test_position_sets.py tests/test_endgame_services.py tests/test_pre_endgame.py
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
LIBRETILES_RUN_BOARD_DEFENSE_ACCEPTANCE=1 env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_board_defense_benchmark.py -s
LIBRETILES_RUN_STRENGTH_ACCEPTANCE=1 env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_strength_benchmark.py -s -k one_hundred
```

From `frontend/`:
```bash
npm run typecheck
npm run lint
npx vitest run src/app/api/ai/move/route.test.ts src/lib/ai-turn-simulation.test.ts
```

## 5. Git Commit and Push Sequence

Stage ONLY the allowlisted files by explicit paths:
```bash
git add backend/gamecore/board_defense.py \
        backend/gamecore/move_search.py \
        backend/gamecore/selfplay.py \
        backend/game/services.py \
        backend/game/position_sets.py \
        backend/tests/test_board_defense.py \
        backend/tests/test_board_defense_services.py \
        backend/tests/test_board_defense_benchmark.py \
        backend/tests/test_move_search.py \
        backend/tests/test_strength_benchmark.py \
        backend/tests/test_slovak_strength.py \
        backend/tests/test_position_sets.py \
        frontend/src/app/api/ai/move/route.ts \
        frontend/src/app/api/ai/move/route.test.ts

git diff --staged --stat
```

Commit message:
```bash
git commit -m "feat(gamecore): implement board control and defensive opportunity cost"
```

Pre-push verification:
```bash
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "6e20a4f5e901ebbcd4354e77a3e103ff2bcdfa8b"
git push origin main
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "$(git rev-parse HEAD)"
```

## 6. Stopping Conditions

Stop and report immediately if:
- Repository gate fails before start or working tree is dirty.
- Board defense evaluation introduces latency exceeding 750 ms midgame ceiling.
- Any test in `test_word_authority_parity.py` sections 1–4 fails (parity oracle compromised).
- Pre-push verification reveals remote diverged from `6e20a4f5e901ebbcd4354e77a3e103ff2bcdfa8b`.

## 7. Report Contract

Begin **exactly** with:
```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinate fields unchanged:
```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 09, Worker exchange ordinal: 01
```

Then provide the standard 11-item compact core:
- Status: `PASS | PARTIAL | BLOCKED`
- Phase-qualified result: `implementation-PASS`
- Start commit: `6e20a4f5e901ebbcd4354e77a3e103ff2bcdfa8b`
- End commit: `<exact SHA>`
- Changed files and purpose (explicit paths)
- Board defense benchmark comparison table (spread changes, opponent reply score suppression)
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
