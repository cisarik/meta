# Slice 3: Pre-Endgame Tracking and Exact Endgame Search

```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 06, Worker exchange ordinal: 01

Status: PARTIAL — technical design complete; unconditional exactness and universal out-play guarantees are not supportable.
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: not-applicable
Logical-whole closure: not-closed
Changed files and purpose: none — this exchange mutates nothing
Commit/push result: not-applicable
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
Evidence tier: E0
Evidence posture: non-independent

Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

Start and end commit: `68afb6df92fccb2996ae83f1a444e4ada7396d10`. Branch: `main`. Working tree clean. The `.ap` checkout matches gitlink `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.

Validation performed: repository inspection and two in-memory baseline self-play probes using existing code. No files written, dependencies installed, secret files read, network requests made, or providers called. Full test suites were not run.

Context pressure: moderate; sufficient context remained for the complete design.

## Summary

Add public-information tile tracking, deterministic pre-endgame adjustments, and bounded minimax search that certifies exact results only when its proof is complete. Preserve existing legality, final scoring, and pass/exchange authority.

Two limits must remain explicit:

- Top-K pruning or an unfinished search cannot establish global optimality.
- Legal deadlocks exist, and maximizing spread can favor a deadlock over an available out-play. Therefore, `BAG_EMPTY_AND_PLAYER_OUT` cannot be guaranteed universally.

Treat 100% out-play completion as a fixed benchmark acceptance gate. An unsuccessful run fails that gate; do not change rules, exclude failed seeds, or relabel terminal reasons to satisfy it.

### D1 — Unseen Tile Tracking and State Modeling

Create `backend/gamecore/tile_tracking.py` with a pure context builder.

Calculate:

```text
unseen = Counter(variant.distribution)
unseen.subtract(each occupied Cell.token)
unseen.subtract(my_rack)
```

Use physical tokens throughout. An assigned blank removes `"?"`, not its `blank_as` assignment. A multigraph tile removes one token. Validate canonical tokens against the resolved variant.

The builder receives the board, acting rack, variant, bag count, player count, opponent rack size, scoreless-turn count, and opponent action rules. It returns an immutable `LateGameContext` or an unavailable result with a bounded reason.

`LateGameContext` contains:

- `bag_remaining`
- Canonically ordered unseen token counts
- `opponent_rack_size`
- `consecutive_scoreless_turns`
- Opponent action rules: AI scoring-only policy or human policy

Board and acting rack remain the existing move-search arguments.

Eligibility and validation:

- Activate only for two players and `0 <= bag_remaining <= 7`.
- Require valid rack sizes, nonnegative inventory counts, and `sum(unseen) == bag_remaining + opponent_rack_size`.
- Preserve negative counts during subtraction so overdraws cannot disappear through `Counter` arithmetic.
- Reject malformed occupied cells, unknown tokens, invalid counts, and inconsistent inventory.
- With an empty bag, expand the unseen multiset into the exact opponent rack.
- With a nonempty bag, retain the combined pool; never assign particular tiles to the opponent or inspect bag order.

Unavailable tracking disables strategic analysis and preserves ordinary ranked search. It never establishes “no legal move.”

Django supplies opponent rack **size**, not its contents. Self-play uses the same builder without passing `game.bag.tiles` or the opponent’s rack contents. Tests may compare the deduction against those private values.

### D2 — Exact Endgame Out-Play Solver

Create `backend/gamecore/endgame.py`. Implement iterative-deepening minimax with alpha-beta pruning and a per-search transposition table.

**Move generation**

Extract a private placement-enumeration seam from `_RankedSearcher`. Preserve the existing first-witness search behavior.

The solver needs every legal action potentially relevant to optimality. Public `top_k` limits the returned recommendations, not the solver’s legal action set. Existing utility, immediate outs, and the previous principal variation determine traversal order. Discarding lower-ranked moves makes the result bounded, never exact.

Every placement passes through `evaluate_scoring_move` and the same `WordAuthority`, variant, and blank alphabet used by live validation.

Model the existing action rules:

- AI nodes contain positive-scoring placements; passing becomes available only after exhaustive absence of such placements.
- Human opponent nodes also allow voluntary passes and legal zero-score placements. The evaluator’s `non_scoring` result retains legality evidence; accept that specific result only for simulated human actions.
- No exchanges occur with an empty bag.
- Actual zero-score placement transitions reset the scoreless counter, matching current engine/service behavior.

**State and transitions**

Search state comprises board cells, premium-consumption state, both physical racks, side to move, scoreless counter, and action rules. Evaluate spread changes relative to the root; current accumulated spread is an additive constant.

Use a private board copy, then reversible make/unmake operations. Restore `token`, `blank_as`, and `premium_used` in `finally` blocks. Consume physical rack tiles with the existing rack helper. Do not instantiate an empty `TileBag`: its constructor repopulates an empty list.

Use `determine_end_reason` and `apply_final_scoring` as the terminal authorities. Search must not introduce another scoring implementation.

**Values**

From the root player’s perspective:

| Outcome | Additional spread |
|---|---:|
| Immediate out | `my_score + 2 × opponent_leftover` |
| Opponent goes out after my first move | `my_score − opponent_score − 2 × my_remaining_points` |
| My second move goes out | `my_score_1 − opponent_score + my_score_2 + 2 × opponent_remaining_points` |
| Deadlock | Accumulated placement spread `+ opponent_leftover − my_leftover` |

Thus, scoring 15 and going out against 20 leftover points contributes **55 spread points**. Do not add a separate “own leftover saved” bonus to this formula.

Search depths `1, 3, 5, …` cover the requested move–reply–out sequence at depth three. At an unresolved horizon, use accumulated placement spread plus `opponent_leftover − my_leftover` as an explicitly heuristic evaluation.

Maximize spread first. Resolve equal evaluated values by immediate rack-out, tiles consumed, then canonical placement key. Do not sacrifice proven spread merely to produce a preferred terminal reason.

**Exactness and out-play certificates**

Return separate strategy metadata:

- `exact`: root optimality and terminal value established.
- `bounded`: useful legal recommendation, unfinished strategic proof.
- `unavailable`: invalid context or no usable strategic analysis.

Keep this separate from placement-search `found|none|indeterminate` and root enumeration completeness.

For the selected move, expose an internal `out_in_two` certificate: `proven|refuted|unknown`. “Proven” requires an immediate out or exhaustive coverage of every legal opponent reply, with a legal root-player out available afterward. A principal variation alone is insufficient. A capped reply search yields `unknown`.

**Deadlocks**

Preserve six consecutive scoreless turns and their existing leftover deductions. Two exhaustive forced passes on an unchanged board may be collapsed internally to the equivalent six-pass terminal value. Do not manufacture a persisted `NO_MOVES_AVAILABLE` ending; live services currently pass `no_moves_available=False`.

### D3 — Pre-Endgame Strategic Adjustment

For `1 <= bag_remaining <= 7`, retain heuristic status. A nearly empty bag does not make draws known: with one tile in the bag and seven on the opponent’s rack, eight unseen physical tiles can still be possible draws.

Implement deterministic arithmetic without sampled hidden racks or provider calls.

For each placement define:

- `L`: retained rack before refill
- `d = min(bag_remaining, 7 − len(L))`
- `b_after = bag_remaining − d`
- `N`: unseen pool size
- `F`: face-point sum
- `E`: existing leave equity for `L`

Use the following initial calibration:

1. **Transition burden.** Blend existing equity toward expected leftover burden:

   ```text
   T = −100 × (F(L) + d × F(unseen) / N)
   transition_equity = (b_after × E + (7 − b_after) × T) / 7
   ```

2. **Unrepairable imbalance.** Under an explicitly heuristic uniform unseen-pool assumption:

   ```text
   P(no helpful draw) = C(N − helpful_count, d) / C(N, d)
   ```

   Helpful tiles are vowels plus blanks for a consonant-heavy leave, and consonants plus blanks for a vowel-heavy leave. Penalize each excess tile beyond a one-tile imbalance by 200 cp times the corresponding probability; cap the combined penalty at 1,200 cp. Each retained blank halves it.

3. **Premium exposure.** Calculate the largest unused premium multiplier available on an empty anchor before and after placement. Penalize newly increased exposure to unseen tiles worth at least eight points. Weight each tile by its probability of appearing in an opponent rack of the known size; use the largest weighted risk and cap it at 1,500 cp.

Final utility is immediate score in centipoints plus transition equity minus the two penalties. Use rational/integer arithmetic and floor once per component for deterministic results.

This supplies vowel-scarcity awareness, tile shedding, and conservative premium denial. It does not certify that an opponent holds a particular consonant or cannot go out.

Keep existing `leave_equity_cp` behavior unchanged. Add a separate pre-endgame valuation helper; freeze its initial constants in tests. Any later calibration requires the fixed benchmark comparison.

### D4 — Search Budget and Complexity

**Measured baseline**

Both probes used seed `0`, ranked-best self-play, and a 20,000-node bound:

| Variant | Plies | Ending | Final scores |
|---|---:|---|---|
| English | 22 | `BAG_EMPTY_AND_PLAYER_OUT` | 497–340 |
| Slovak | 26 | `BAG_EMPTY_AND_PLAYER_OUT` | 502–452 |

Re-enumeration of their four empty-bag roots found **60, 111, 417, and 657** legal placements: mean 311.25. Enumeration took **30–577 ms**. This small sample is feasibility evidence, not a population average.

Worst-case search remains exponential, approximately `O(B^D)` before pruning. Even an eight-move beam has 512 depth-three paths and does not establish exactness.

**Chosen bounds**

- Preserve the current 750 ms midgame default.
- Give eligible live late-game quality searches a **1,250 ms total budget**, reserving 50 ms for finishing.
- Retain a total 500,000 work-unit ceiling; charge both generator expansion and minimax expansion.
- Limit minimax state expansions to 10,000.
- Limit retained placement records across active search frames to 25,000.
- Limit the per-search transposition table to 4,096 entries.
- Root enumeration receives at most 60% of the time/work budget; remaining resources fund deeper analysis.
- All child searches share the same counters and absolute deadline. They never receive renewed budgets.

Check the deadline before expansions, certification, and bulk result processing. Return the last completed iteration or the certified root fallback. An incomplete iteration must not selectively promote partially evaluated candidates.

Explicit caller budgets remain authoritative. Node-bound tests may retain their existing very large elapsed limit to remove machine timing from tuple evidence.

Use a conservative depth ceiling of `6 × (total remaining rack tiles + 1)`, at most 90 for two seven-tile racks. Placements consume tiles; pass streaks terminate, so this bounds the finite game tree without assuming three plies suffice.

Transposition keys include board tokens and blank assignments, premium state, rack multisets, side, scoreless counter, and action rules. Entries retain depth and exact/lower/upper-bound classification. A truncated result is never cached as an exact value.

These bounds ensure finite work and bounded retained structures. Cooperative Python deadlines cannot guarantee a strict wall-clock maximum under arbitrary scheduling or cold initialization. Measure latency separately; do not describe `<1500 ms` as a hard real-time guarantee.

### D5 — Pipeline Integration

**Move search**

Add optional `late_game_context` and bounded strategy metadata to `find_ranked_scoring_moves`. Calls without context preserve current behavior.

Append defaulted fields to result dataclasses so existing positional constructions remain valid. Preserve:

- Actual placement score in `total_score`
- Existing leave equity in `leave_equity_cp`
- Existing legality status
- `complete` as root placement-enumeration completeness

Keep strategic value, strategy mode, completed depth, and proof status separate. Include all strategic work in reported total search cost.

**Self-play and position sets**

Build context immediately before each ranked decision. Ranked-best and ranked-witness-safe select the strategy’s first candidate. During eligible late-game turns, ranked-rack-aware must also honor that recommendation rather than overriding it with its rare-tile bonus.

Add `SelfPlayConfig.late_game_enabled=True`; use `False` for retained Slice 2 controls. Witness-first remains unchanged. Carry optional strategy diagnostics in trace decisions.

Update position-set reconstruction search to pass the same context as the generating self-play search. Otherwise `_assert_mount_equivalence` would compare different policies.

**Django**

Build context within `_probe_ai_ranked_candidates`, using the session variant and active slot’s board/rack state. Supply the fixed late-game budget only when tracking is valid.

Extend `ai-candidates.search` only for active strategic analysis with a strategy marker and bounded proof metadata. Do not serialize unseen counts, inferred racks, bag contents, or principal variations containing opponent tiles. Leave `ai_context` unchanged.

Submission continues to revalidate submitted placements and apply existing final scoring under the current transaction. No search result authorizes a pass or exchange.

**Required SSE integration**

The current merge function (`frontend/src/app/api/ai/move/route.ts:494`) sorts recommendations by immediate score. That would undo this feature.

For responses carrying the recognized late-game strategy marker, preserve backend recommendation order and place those choices before provider-only candidates. Continue canonical deduplication and submission validation. Responses without the marker retain the existing merge behavior.

Apply this through the shared choice path used by normal completion, timeout, no-progress, and rescue handling. No new provider calls, prompt changes, or completion-source values are needed.

The frontend route and its focused tests are therefore required additions to the implementation allowlist for live-play parity.

### D6 — Tests and Benchmark Impact

**Correctness tests**

- Inventory subtraction: all twelve distributions, duplicates, assigned blanks, multigraphs, Unicode, bag counts 0/1/7/8, wrong player counts, negative residuals, and count mismatches.
- Exact values: immediate +55 example, maximum opponent scoring out, lower-scoring first move enabling a superior two-turn out, defensive blocking, and losing positions.
- A best move outside the ordinary top eight.
- Human voluntary pass and zero-score placement versus AI action restrictions.
- Forced passes, six-scoreless termination, one side immobile, both sides immobile, and terminal-state precedence.
- Board/rack/premium restoration on success, cap, and exception.
- Shared node/time limits, fake-clock termination, memory limits, deterministic rack-order independence, and transposition key separation.
- Exhaustive tiny-position comparison against a test-only brute-force reference that independently enumerates placements and uses existing legality/final-scoring authorities.
- Unknown search results never authorizing a nonscoring action.

**Existing matrices**

- Preserve the four existing English node-bound tuples under `late_game_enabled=False`: spreads **583, 419, 282, 515**, all player-out.
- Add enabled counterparts for seeds 300/301 in both strategy seats; retain four production-budget games.
- Extend the existing English 100-game acceptance run for seeds 300–349 and both seats.
- Extend Slovak ranked checks for seeds 0/1 and both seats, plus its ranked self-play case.
- Preserve `test_slovak_full_game.py` as a witness control. Its pinned seed-0 result is 55 plies, six scoreless turns, scores 303–243.
- Preserve witness rows in the policy matrix. Apply the 100% target to the declared strategy-enabled cohort, not unchanged witness controls.

Keep legacy checks allowing legitimate deadlocks. Add separate explicit player-out assertions for the strength acceptance cohort.

**Position sets and diagnostics**

The committed 24-position English asset has bag counts **13–86**. It supplies no coverage for this feature.

Add dedicated late-game fixtures under tests, including conservation-valid snapshots and mount-equivalence checks. Do not regenerate the committed asset or change its schema.

Existing engine probes use `bag_count=100`; they remain midgame regression coverage. Diagnostic runners continue reporting actual move scores; those scores are not proxies for endgame spread.

**Live integration**

Test that a lower immediate-score backend recommendation survives SSE merging against higher-scoring backend and provider alternatives. Cover incomplete analysis, missing strategy markers, rejected/stale placements, and existing completion paths. Verify API privacy and unchanged participant/active-turn checks.

### D7 — Empirical Measurement Strategy

Run paired enabled/disabled comparisons on identical seeds, seats, dictionaries, and explicit budgets.

Use these fixed cohorts:

- English: seeds 300–349, both strategy seats, against witness-first.
- Slovak: seeds 0–49, both strategy seats, against witness-first.
- Ranked self-play: both variants, seeds 0–3.
- Tiny exact-solver fixtures: compare every completed result with the reference oracle.

Report:

- Wins/draws/losses, total and average spread, and paired spread change
- Counts of every terminal reason, including failures and incomplete games
- Player-out rate, bag count at termination, stranded tiles, passes, and plies
- Empty-bag and pre-endgame decision counts
- Exact/bounded/unavailable rates and completed depth
- Generator work, tree nodes, cap reasons, cache hits, and latency distribution

Acceptance requires:

1. Correctness, conservation, and authority tests pass.
2. Enabled strength cohorts reach 100% player-out; controls remain visible separately.
3. Existing strength requirements hold and aggregate paired spread does not decline for either language.
4. No strategic-cap result becomes a false no-move decision.
5. Warm late-game searches meet the stated latency target on recorded hardware; report cold timing separately.
6. Midgame choices remain identical in deterministic comparisons; measure performance against the unchanged path.

Record source revision and node-bound tuples after implementation. Do not preinvent new expected scores. If a gate fails, report the position and failure; do not weaken the cohort or substitute terminal labels.

### D8 — Ordered Implementation Slice and Grant

Overall proposed tier: **E2**, because the change crosses engine search, self-play, service responses, and live selection. No migration, credential handling, production operation, or new external trust boundary is required.

| Step | Work | Evidence |
|---|---|---|
| 1 | Tracking, context validation, pre-endgame arithmetic | Focused positive/negative tests; E1 component |
| 2 | Shared enumeration, bounded minimax, proof metadata | Reference-oracle, terminal, restoration, and budget tests; E2 |
| 3 | Self-play, position-set, Django, and SSE integration | State/authority/privacy and selection parity tests; E2 |
| 4 | Fixed benchmark comparisons and regression pins | Complete matrix accounting, latency evidence, and rollback review; E2 |

**Exact proposed path allowlist**

```text
backend/gamecore/tile_tracking.py
backend/gamecore/endgame.py
backend/gamecore/leave_equity.py
backend/gamecore/move_search.py
backend/gamecore/selfplay.py
backend/game/services.py
backend/game/position_sets.py
backend/tests/test_tile_tracking.py
backend/tests/test_endgame.py
backend/tests/test_pre_endgame.py
backend/tests/test_endgame_services.py
backend/tests/test_endgame_benchmark.py
backend/tests/test_move_search.py
backend/tests/test_strength_benchmark.py
backend/tests/test_slovak_strength.py
backend/tests/test_endgame_policy_matrix.py
backend/tests/test_position_sets.py
frontend/src/app/api/ai/move/route.ts
frontend/src/app/api/ai/move/route.test.ts
```

Leave game rules, scoring authorities, dictionaries, manifests, migrations, `.ap`, environment files, and the frozen word-authority parity oracle unchanged.

**Orchestration critique**

- **MEASURED:** Baseline and AP pin match; the tree is clean. Two existing games reproduced their pinned ranked-best outcomes. Empty-bag root branching is already substantial.
- **MEASURED:** SSE currently reorders backend choices by raw score. The committed position asset never reaches the requested phase. Existing witness controls deliberately include six-scoreless endings.
- **LEAD:** Unconditional exactness, strict latency, universal player-out completion, and unrestricted spread maximization cannot all be promised. This plan preserves truthful bounded results and makes 100% a measured acceptance gate.
- **LEAD:** A backend-only implementation grant cannot deliver live selection parity; it must include the two listed frontend paths.

Enumeration widened: SSE final-choice merging and position-set reconstruction were inspected because they affect delivery. Live providers, production behavior, full benchmark matrices, and broader security surfaces were not exercised.

Report justification: new-evidence

Authority expiry: this terminal report ends Worker session 06, exchange 01 planning authority; it grants no implementation authority.

Smallest next step: ORCHESTRATOR reviews the stated guarantee limits and issues one fresh E2 implementation grant with the complete allowlist and `Native planning mode: not-used`.
