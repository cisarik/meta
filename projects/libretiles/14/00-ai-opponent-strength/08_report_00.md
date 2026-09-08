# Slice 4: Board Control and Defensive Opportunity Cost

```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 08
Worker exchange ordinal: 01

Status: PASS — bounded implementation planning complete; advisory
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: not-applicable
Logical-whole closure: not-closed
Start and end commit: 6e20a4f5e901ebbcd4354e77a3e103ff2bcdfa8b
Changed files and purpose: none — this exchange mutates nothing
Commit/push result: not-applicable
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
```

Validation: required checkout and baseline verified; working tree clean before and after inspection. AP checkout matches its recorded gitlink, `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`. Repository inspection and six pure-engine timing probes on Python 3.12.12 completed. No test suite, network request, provider call, secret-file read, or mutation occurred.

```text
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

Context pressure: moderate; sufficient context retained to complete this report.

## D1 — Evaluation model

Add a pure `board_defense.py` module. Its output estimates **incremental opponent premium opportunity**, expressed in integer centipoints. It does not calculate an exact expected reply score: that would require an opponent-rack distribution and substantially more search.

For midgame candidates only, use:

\[
U(m)=100\,score(m)+leave(m)-D(m)
\]

\[
D(m)=clamp\left(
\left\lfloor wR/100\right\rfloor
-\left\lfloor gG/100\right\rfloor
-\left\lfloor cC/100\right\rfloor
-\left\lfloor tV/100\right\rfloor,
-800,\;3000
\right)
\]

The terms are:

| Term | Definition |
|---|---|
| `R` | Newly exposed premium risk, capped at 2,400 cp |
| `G` | Premium opportunity denied, capped at 400 cp before posture weighting |
| `C` | Reduction in total empty anchors, capped at 200 cp before posture weighting |
| `V` | New high-variance opportunities, capped at 400 cp |
| `w,g,c,t` | Integer posture percentages from D3 |

A negative defense penalty is a positional bonus. Final positional influence is bounded between an 8-point bonus and a 30-point penalty.

For each unused premium, calculate exposure before and after the candidate using D2. Let the two largest positive exposure changes be `p1,p2`, and the two largest magnitudes of negative changes be `n1,n2`; missing values are zero.

```text
R = min(2400, p1 + p2 // 2 + 200 * min(2, newly_opened_lanes))
G = min(400, (n1 + n2 // 2) // 4)
C = min(200, 50 * max(0, anchors_before - anchors_after))
V = min(400,
        100 * min(2, newly_exposed_TW_or_TL_count)
        + 200 * min(1, newly_opened_lanes))
```

Using the strongest two premium changes discounts competing opportunities: the opponent has one next move. Denial receives less weight because consuming a premium already contributes to immediate score.

An illustrative neutral comparison, with equal leave equity:

- Safe 12-point move: `1200 cp`.
- 22-point move opening a maximum-strength vowel/TW opportunity: `2200 − 1500 = 700 cp`.

The safe move wins. Conversely, a small distant exposure cannot erase a substantial scoring gain. With equal leave, a scoring advantage greater than 38 points exceeds the entire possible difference in defense adjustments.

These are fixed initial calibration values, subject to the acceptance measurements in D7. Improvement is not established by this planning exchange.

## D2 — Fast premium and anchor detection

**Representation and preprocessing**

Use flattened cell IDs, `15 * row + column`, and Python integer bitboards. Construct:

- Occupancy and three support-class masks.
- Empty-anchor mask: orthogonal neighbours of occupancy, excluding occupancy.
- Actual unused TW/DW/TL cells from `Board.cells`; an occupied or `premium_used` cell has zero exposure.
- Short access segments and inverse dependency tables.
- Baseline exposure per premium and baseline active lanes.

Read premium types from the supplied board. Do not assume the standard layout or reload its JSON during candidate evaluation. DL remains valued through scoring; Slice 4 assigns it no separate defensive weight.

The shipped layout has **8 TW, 17 DW, and 12 TL cells**.

**Support classes**

Use `LeaveEquityProfile.vowels`, preserving the existing English, Slovak, and derived variant treatment.

Once per search, compute each playable token’s two-tile hook degree: the number of distinct partner tokens accepted in either order by `WordAuthority.accepts_tokens`.

Assign support percentages:

| Support token | Percentage |
|---|---:|
| Vowel | 150 |
| Consonant with fewer than four legal partner tokens | 50 |
| Other consonant | 100 |

An anchor touching multiple occupied cells takes the highest support percentage. This makes exposed vowels more costly and derives low-synergy consonants from the actual authority instead of universally hardcoding English `C` and `V`.

These percentages remain heuristic. A low hook degree does not certify that a longer reply is impossible.

Assigned blanks use their realized token for support classification. Their physical identity and zero face score remain unchanged. Multigraph tokens are never split into characters.

**Premium exposure**

Base weights:

```text
TW = 1000 cp
DW =  500 cp
TL =  600 cp
```

For each premium `p`, precompute 13 access channels: the premium itself, plus anchor positions one, two, or three cells away along each orthogonal ray.

A channel contributes only when:

1. Its anchor is empty and adjacent to an occupied cell.
2. Every cell from that anchor through the premium is empty.
3. The premium is unused.

Distance percentages are `100, 60, 35, 20` for distances `0,1,2,3`.

```text
channel_risk =
    premium_weight * distance_percentage * support_percentage // 10000

premium_exposure = maximum channel_risk, or zero
```

This covers a premium that becomes an anchor, an adjacent anchor that reaches a premium, and short scoring lanes. Occupied corridor cells invalidate that channel. Recompute the maximum across alternate channels before crediting a blocked opportunity.

“Access” means geometrically available under this bounded heuristic. It does not certify a complete opponent word, cross-word legality, or rack availability. Longer approaches beyond three cells are deliberately outside this estimator.

**Parallel lanes**

Precompute premium endpoint pairs that:

- Share a row or column.
- Are at most six cells apart.
- Are both TW/DW/TL cells.

A lane is active when both endpoints have positive exposure, the inclusive segment is empty, and at least one cell in that segment is an anchor. Its length is therefore at most seven physical placements. Count only inactive-to-active transitions for `newly_opened_lanes`.

This captures parallel openings beside the candidate as well as other newly reachable premium corridors. It does not claim that a dictionary-valid seven-tile reply exists.

**Incremental evaluation**

For a certified candidate:

1. Build its placement mask and support-class additions in `O(k)`.
2. Derive after-move occupancy, support, and anchor masks with integer operations.
3. Union affected premium and lane IDs through precomputed inverse dependencies.
4. Recompute only those features against the virtual overlay.
5. Calculate D1’s signed penalty.

A premium dependency includes its access segments and neighbours of their anchor cells. A lane dependency includes its segment, anchor neighbours, and both endpoint-premium dependencies. This catches consumption, obstruction, support changes, and alternate access.

No board copy, make/unmake operation, or secondary move enumeration occurs per candidate.

## D3 — Score-differential posture

Use the **current pre-move** score difference:

```text
score_differential = acting_score - opponent_score
```

Do not add the candidate’s score when choosing posture.

| Score differential | Risk `w` | Denial `g` | Closure `c` | Opening `t` |
|---|---:|---:|---:|---:|
| ≤ −60 | 40 | 50 | 0 | 100 |
| −59 through −30 | 65 | 75 | 0 | 50 |
| −29 through +29 | 100 | 100 | 0 | 0 |
| +30 through +59 | 150 | 150 | 100 | 0 |
| ≥ +60 | 200 | 200 | 200 | 0 |

Consequences:

- Leading players penalize exposure more strongly and receive additional value for denial and net anchor reduction.
- Trailing players retain a positive risk cost while receiving a bounded opening bonus.
- Neutral players balance scoring, leave, and exposure without an opening or cluster bonus.

Activate this module only when the **pre-move bag count exceeds seven**. Preserve the existing pre-endgame and empty-bag paths, including fallback behavior when late-game context is unavailable.

“Lockdown” changes placement ranking. It introduces no deliberate pass, exchange, clock manipulation, or new game-ending rule.

## D4 — Complexity and latency

The current ranked search allows 500,000 nodes, 25,000 unique certified placements, and 750 ms. The placement limit is a ceiling, not a promise to evaluate 25,000 placements within 750 ms.

Measured warm-dictionary baseline on three committed English midgame positions:

| Position | Certified placements | Nodes | Elapsed across two runs |
|---|---:|---:|---:|
| 1 | 236 | 3,971 | 149–173 ms |
| 2 | 701 | 5,724 | 338–356 ms |
| 3 | 288 | 3,341 | 157–157 ms |

All six searches completed. These measurements establish a local reference, not a latency guarantee or evidence about the proposed implementation.

Implementation bounds:

- Preprocessing: `O(board cells + alphabet² + premium/lane geometry)`.
- Candidate evaluation: `O(k + 13 × affected premiums + affected lanes)`.
- Memory is bounded by board geometry and the current search; no candidate-board cache or unbounded cross-request cache.
- Start accounting before defense initialization. Initialization belongs to the existing search budget.
- With defense active, reserve `min(10, max_elapsed_ms // 10)` milliseconds for finishing. Preserve caller node and placement limits.
- Check the deadline before initialization, after initialization, and between candidate evaluations. An interrupted traversal retains the existing `found`/`indeterminate` contract.

Add an exact ranking optimization after certification and leave calculation: when top-k is full, skip defense evaluation if `score * 100 + leave + 800` is **strictly below** the worst retained utility. Still count that placement as seen. Equality requires evaluation to preserve tie-breaking.

Performance acceptance:

- On fixed-node, matched candidate workloads, warm median total-time overhead must be at most 10%.
- Under the production deadline, median evaluated-node throughput must remain at least 90% of defense-off throughput on cap-reaching positions.
- Measure total latency, initialization cost, candidate count, and cap frequency separately.
- Include a 25,000-evaluation stress measurement without asserting that a complete 25,000-candidate search fits the live deadline.
- Require the measured midgame corpus to remain below 750 ms on the reference runner. Report scheduler overruns explicitly; Python deadline checks are cooperative.

## D5 — Pipeline and interfaces

**Gamecore**

Append keyword parameters to `find_ranked_scoring_moves`:

```python
score_differential: int = 0
board_defense_enabled: bool = False
```

The disabled default preserves existing callers. The live service explicitly enables defense.

Append `defense_penalty_cp: int = 0` to `RankedMoveCandidate`, preserving existing positional construction. Add an `evaluation_cp` property containing D1's unified utility while keeping `leave_equity_cp`'s pre-endgame meaning intact.

`_RankedSearcher` constructs one defense context for enabled midgame searches and evaluates candidates only after `evaluate_scoring_move` succeeds. `_rank_key` uses `evaluation_cp`, followed by the existing rack-out, tiles-used, and canonical-placement tie-breaks.

Add `"board_control"` to `StrategyMode`. Emit it when the enabled midgame evaluator ran, even if all available premiums produce zero adjustment. Its `out_in_two` remains `None` and `completed_depth` remains zero.

Do not change first-witness search, `LateGameContext`, `solve_endgame`, or exhaustive endgame enumeration.

**Self-play**

Append:

```python
board_defense_enabled: bool = False
player_board_defense_enabled: tuple[bool, bool] | None = None
```

A per-seat tuple overrides the global value. `_ranked_search` passes the acting seat’s setting and current score difference; use zero for the existing one-player synthetic fixture.

Both `POLICY_RANKED_BEST` and `POLICY_RANKED_WITNESS_SAFE` consume the resulting ordering. The existing rack-aware policy already respects non-null strategy modes. Witness behavior stays unchanged.

Append the selected candidate’s `defense_penalty_cp`, defaulting to zero, to `_Decision` for trace analysis.

**Django**

In `_probe_ai_ranked_candidates`:

- Derive the difference from `PlayerSlot.score` and the other session seat’s score.
- Use zero if exactly one opponent cannot be identified.
- Pass `board_defense_enabled=True`.
- Do not read opponent rack contents or accept client-provided score/posture settings.

The existing candidate payload automatically carries the new strategy marker. Candidate `score` remains the actual immediate score; equity fields remain internal.

`submit_move_for_ai` and `_submit_move_locked` retain legality and scoring authority. A strategic penalty never rejects an otherwise legal submission.

**Required frontend integration**

The move route currently preserves backend order only for three late-game markers (`frontend/src/app/api/ai/move/route.ts:455`). Unmarked midgame candidates are re-sorted by raw score, which would discard this feature.

Add `"board_control"` to that existing recognized set. Reuse the established strategic merge behavior: backend candidates first in backend order, then deduplicated provider candidates. Preserve commit-time backend revalidation and fallback when a candidate cannot be committed.

This also means provider candidates without comparable positional evaluation follow backend candidates, even when their immediate score is higher. That limitation must be visible in acceptance evidence.

**SEARCH_PROFILE**

Presets do not configure these coefficients in Slice 4. They remain advisory model instructions. Do not parse prompt names or text into backend strategy settings. Grandmaster and Fast Search receive the same board-defense policy.

## D6 — Benchmark and position-set compatibility

- Preserve the English legacy node-bound tuples exactly: spreads `583, 419, 282, 515` for the existing seed/seat ordering.
- Keep existing English default four-game and opt-in 100-game legacy assertions. Explicitly disable defense in their legacy configuration.
- Add defense-enabled four-game smoke coverage on English seeds `300,301`, with both strategy seats.
- Preserve Slovak legacy and late-game coverage. Add enabled runs on seeds `0,1`, with both seats, plus defense-enabled ranked self-play.
- Enabled smoke games must terminate, conserve tiles, preserve formed-word authority, and produce positive aggregate spread with more wins than losses against first-witness.
- Keep existing late-game benchmark inputs defense-disabled when they serve as Slice 3 regression evidence.

**No committed position-set regeneration is required.**

Explicitly disable defense in both `position_sets._selfplay_config` and `_ranked_on_game`. Preserve the existing asset, schema, digest, and mount-equivalence expectations.

A default differential of zero is insufficient: neutral defense still changes ranking. New defense tests should reuse static boards while passing `−60`, `0`, and `+60`; they must not overwrite historical engine baselines.

## D7 — Empirical acceptance strategy

Use identical search limits, dictionaries, seeds, starting-seat rules, and late-game settings across arms. Set `late_game_enabled=True` in both arms to isolate the addition beyond Slice 3.

**Paired acceptance cohorts**

- English: seeds `300..349`, each strategy seat — 100 games per arm.
- Slovak: seeds `0..9`, each strategy seat — 20 games per arm.
- Control: strategy seat uses ranked-without-defense.
- Treatment: strategy seat uses ranked-with-defense.
- Opponent: ranked-without-defense in both arms.
- Use `POLICY_RANKED_WITNESS_SAFE` for terminal safety in both seats.
- Use 20,000 ranked nodes and the existing large deterministic elapsed allowance. Measure production-cap performance separately.

A shared seed couples the initial setup; changed moves can change later draw allocation. Do not describe subsequent racks as identical.

Report per variant:

1. W/D/L and win rate, counting a draw as half a win.
2. Mean final spread and paired treatment-minus-control spread.
3. Opponent points per turn: placement points divided by all opponent turns, including zero-score passes/exchanges.
4. Opponent immediate-reply score following defense-active midgame decisions, separated by leading, neutral, and trailing posture.
5. Own points per turn, passes, exchanges, game length, end reasons, and stranded tiles.
6. Search time, nodes, candidate counts, and cap frequency.
7. Frequency of selected moves with nonzero defense adjustment.

Exclude final rack adjustments from turn-score statistics; include them in final spread.

For uncertainty reporting, use 10,000 paired bootstrap resamples grouped by seed, keeping both seats together, with `random.Random(4004)`. Report 95% intervals without claiming broad strength improvement when intervals include zero.

Predeclare acceptance:

- All legality, conservation, terminal, compatibility, and performance checks pass.
- Each variant has positive paired mean spread improvement.
- Treatment win rate is at least control win rate.
- Aggregate opponent points per turn do not increase.
- The leading-posture reply cohort is nonempty and its mean reply score decreases.

Failure is a reported acceptance finding. Do not repin historical results, silently weaken thresholds, or repeatedly retune against the acceptance seeds.

## D8 — Ordered implementation grant proposal

1. **Implement and test the pure evaluator.** Add masks, channel/lane dependencies, fixed coefficients, signed adjustment, and posture boundaries.
2. **Integrate ranked search and self-play.** Add defaulted interfaces, utility ranking, bounded pruning, strategy metadata, and per-seat comparison controls.
3. **Integrate live consumption.** Pass server-derived scores, recognize the frontend marker, and freeze historical position-set behavior explicitly.
4. **Validate behavior and strength.** Run focused regressions, required offline gates, performance comparisons, and opt-in acceptance cohorts. Submit measured results against the exact candidate.

Proposed exact mutation allowlist:

```text
backend/gamecore/board_defense.py                         NEW
backend/gamecore/move_search.py
backend/gamecore/selfplay.py
backend/game/services.py
backend/game/position_sets.py

backend/tests/test_board_defense.py                      NEW
backend/tests/test_board_defense_services.py             NEW
backend/tests/test_board_defense_benchmark.py            NEW
backend/tests/test_move_search.py
backend/tests/test_strength_benchmark.py
backend/tests/test_slovak_strength.py
backend/tests/test_position_sets.py

frontend/src/app/api/ai/move/route.ts
frontend/src/app/api/ai/move/route.test.ts
```

No asset regeneration, migration, dependency change, preset modification, or protocol edit is proposed.

**Evidence tier:** E2 for implementation: reversible behavior changes across ranking, service output, and live candidate selection, with empirical strength uncertainty. This planning exchange remains E0. Fresh acceptance is recommended for the ranking-consumption and benchmark claims if uncertainty remains.

**Orchestration critique:**

- **MEASURED — static inspection:** backend-only work would lose its strategic ordering in the frontend raw-score merge; two frontend paths are necessary.
- **MEASURED — static inspection:** neutral score context does not preserve historical position sets; explicit disabling does.
- **MEASURED — execution:** three baseline positions completed below 357 ms on Python 3.12.12. No proposed-defense timing or strength result exists.
- **LEAD:** local exposure is a reply-risk surrogate. Conservative play may lower opponent scoring without improving final spread; both must be measured.
- **LEAD:** prioritizing backend strategy over unvalued provider candidates can overlook a stronger provider move. Extending positional valuation to provider candidates is outside this bounded slice.

**Enumeration widened:** frontend strategic merge and route tests; position-set generation/replay; test environment configuration. No broader UI, provider-runtime, catalog, or production audit.

Report justification: new-evidence

Authority expires with this terminal planning report; this Worker has no implementation or mutation authority.

Smallest next step: ORCHESTRATOR reviews this advisory design and issues a complete fresh-worker implementation grant with `Native planning mode: not-used`, the exact baseline, and the proposed allowlist.
