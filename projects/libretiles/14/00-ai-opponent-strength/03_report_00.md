### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: ai-opponent-strength
Worker session ordinal: 03, Worker exchange ordinal: 01
```

```text
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: not-applicable
Logical-whole closure: not-closed
Changed files and purpose: none — this exchange mutates nothing
Commit/push result: not-applicable
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
```

```text
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

Status: PASS (read-only planning). Repository gate verified: HEAD is exactly `843251db8da0aee878c3462b14cfe8e73528b399`, porcelain clean, AP pin `9c5cc44f` unchanged. All ten mandatory-reading files read at this baseline; every claim below is grounded in them.

---

## D1: Theoretical Model & Mathematical Formulation of Rack Equity

**Formulation.** For each certified candidate move \(m\) with leave \(L(m)\) (the multiset of rack tiles not placed):

\[\text{Utility}(m) = 100 \cdot \text{total\_score}(m) + E(L(m))\]

where \(E\) is Leave Equity in **integer centipoints** (fixed-point ×100; no floats anywhere, preserving byte-for-byte determinism of the ranked search). Since the pre-move rack is constant across all candidates of one turn, maximizing `score + E(leave)` is mathematically identical to maximizing `score + ΔRackEquity`; the absolute form is chosen because it needs no valuation of the full pre-move rack.

**Mid-game equity decomposition** (all terms centipoints, all integer):

\[E(L) = \sum_{t \in L} \text{tile\_equity}(t) \;+\; \text{balance}(v, n, b) \;+\; \text{duplicates}(L) \;+\; \text{synergy}(L)\]

with \(v\) = vowel count in \(L\) excluding blanks, \(n\) = non-blank size of \(L\), \(b\) = blank count. The total is clamped to \([-3000, +6000]\) as a safety envelope so no leave term can ever dominate a legitimate scoring difference of more than 60 points.

**Endgame condition (`bag_count == 0`).** Balance, duplicates, and synergy are meaningless without redraws. When the bag is empty:

\[E_{\text{endgame}}(L) = -100 \cdot \sum_{t \in L} \text{face\_points}(t)\]

i.e. pure leftover-burden minimization, aligned with `apply_final_scoring` semantics (leftover face points are subtracted at game end; the out-player additionally gains the opponent's leftover). `rack_out` **keeps its existing position as a discrete tie-break key immediately after utility** (today it sits after score): a rack-out candidate has an empty leave, so \(E = 0\), and it already dominates any equal-scoring non-out candidate whose leave burden is negative; the explicit flag then breaks exact utility ties toward going out. Exact out-play sequencing and the +opponent-leftover bonus are deliberately **not** modeled here — that is Slice 3 (endgame solver) per the handout slice sequence, and modeling half of it now would create a moving target for Slice 3's baseline.

**Pre-endgame (`1 ≤ bag_count ≤ 6`).** Standard equity applies unchanged. Unseen-tile tracking is Slice 3 scope.

## D2: Base Tile Equity & Letter Valuation Tables

All values are **calibration data constants, not architecture** — initial values follow published Quackle/Maven leave-value methodology adapted to Collins 2019 and the SSS tile set, and D7's A/B benchmark is the acceptance authority. Units: centipoints.

**English** (`english.json`: 100 tiles, points verified against the manifest):

```text
?  +2500      S  +800       E  +350       R  +150       X  +150
A  +100       H  +100       N  +50        M  +50        C  0    T  0
D  -50        K  -50        L  -50        P  -50        I  -100
O  -150       G  -200       Y  -200       J  -250       F  -250
B  -300       Z  -300       W  -350       U  -450       V  -550       Q  -700
```

Rationale anchors: blank ≈ +25 pts of future scoring equity (the prompt's stated 25–30 range, low end chosen because the engine has no bingo-directed search yet); S ≈ +8 (hook monopoly); Q ≈ −7 (dead weight without U); U ≈ −4.5; V/W worst 4-point consonants (no two-letter words with V in Collins). X is kept mildly **positive** (+150) despite the prompt grouping it with clunky tiles: Collins gives it AX/EX/OX/XI/XU hooks, and the "stranded without vowels" hazard is carried by the D3 balance term, not the base value. Vowel set: `A E I O U`.

**Slovak** (`slovak.json`: 100 tiles, 42 tile types, 17 single-copy diacritics, verified):

```text
?  +2500
A  +150   E  +150   S  +150   T  +150   O  +100   I  +100   N  +100   R  +100
V  +50    M  +50    D  +50    L  +50    K  0      P  0      U  -50
J  -100   Á  -100   C  -150   H  -150   Z  -150   Í  -150
B  -200   Š  -200   Y  -250   Č  -250   Ž  -250   Ý  -300
Ľ  -350   Ť  -350   Ú  -350   É  -400   Ň  -400   Ô  -400
Ď  -450   F  -450   G  -450   Ó  -550   Ä  -600   Ĺ  -600   Ŕ  -600   X  -650
```

Rationale: the nine 1-point letters (A O E I N R S T V) are the lexicon's workhorses; Á stays only mildly negative (common vowel, 4-point endgame burden); the single-copy 8–10-point diacritics (Ď F G Ň Ô Ä Ĺ Ó Ŕ X) are the consonant-clog culprits named in the problem statement and receive strong negative retention values, which makes the search *prefer spending them* whenever a near-equal-scoring placement exists. Vowel set for D3: `A Á Ä E É I Í O Ó Ô U Ú Y Ý` (Slovak Y/Ý are vowels; syllabic Ĺ/Ŕ stay consonants).

**Universal variant fallback** (the other 10 variants), derived per tile from the manifest at profile build time:

```text
blank:                 +2500
vowel (see below):     clamp(200 − 80·(points−1), −400, +200)
consonant:             clamp(150 − 80·(points−1) + 25·min(count−1, 5), −700, +300)
```

Vowel classification for fallback variants: NFKD-decompose the token, strip combining marks, vowel iff the base letter is in `AEIOU` — this reproduces today's `AEIOU` default exactly for unaccented tiles while correctly classifying Č-like consonants and Á-like vowels in cs/pl/de/pt/is/it/nl/da/sv/af. Fallback profiles get **no synergy pairs** and class-based duplicate penalties only. Sanity anchors: a 1-point, count-4 consonant (S-like) → +225; a 10-point singleton → −570.

## D3: Vowel-Consonant Balance Function

Penalty table `BALANCE_CP[n][v]` (n = non-blank leave size 0–6; v = vowels; a move places ≥1 tile from a ≤7 rack, so n ≤ 6 always):

```text
n=0:  [0]
n=1:  [0, 0]
n=2:  [-100,    0, -150]
n=3:  [-300,    0, -100, -450]
n=4:  [-600, -100,    0, -300,  -800]
n=5:  [-1000, -300,   0, -150,  -700, -1200]
n=6:  [-1500, -500, -100,  -50,  -400,  -900, -1800]
```

Design properties: optimum sits at ~40–50 % vowels (2V/2C for n=4, 2V/3C for n=5, 3V/3C for n=6, exactly the prompt's healthy ratios); all-consonant and all-vowel leaves are penalized 6–18 points, the prompt's "disastrous" −20 to −30 band scaled down ~35 % because the base tile values already carry part of that signal (e.g. an all-diacritic Slovak leave is already deeply negative before the balance term). Asymmetry: surplus consonants are punished slightly harder than surplus vowels at small n and the reverse at n=6, matching observed clog direction (consonant strand) vs. vowel dump.

**Blanks are wildcards**: excluded from both v and n, and each blank halves the balance penalty — `penalty // (2 ** b)` (integer floor division, deterministic). When `bag_count == 0` the whole D3 term is bypassed (D1 endgame mode).

## D4: Duplicate Tile Penalties & Synergy Pair Bonuses

**Duplicates.** For each tile with multiplicity \(k \ge 2\) in the leave: `dup_cp(class) · (k−1) + dup_cp(class) · max(k−2, 0)` (third and later copies count double). Class values: vowel −75, consonant −125, `S` −300 (a second S is worth far less than the first, English profile), blank −1000 (second blank retained nets +1500, still positive but strongly diminished). So `EE` costs −75, `UUU` costs −225, `LLL` −375 — matching the prompt's examples directionally.

**Synergy.** Curated unordered-pair bonuses, each applied `min(count_a, count_b)` times, total synergy clamped to \([−800, +800]\):

- English: `(Q,U) +600` (the dominant case: a Q with U in hand is playable, Q alone is dead — this effectively converts the −700 Q to −100 when U is kept), `(E,R) +75`, `(?,S) +100`, `(S,T) +50`, `(E,S) +50`, `(I,N) +50`, `(A,N) +40`, `(E,D) +40`.
- Slovak: `(O,V) +50`, `(S,T) +50`, `(N,I) +40`, `(E,N) +40`, `(A,K) +40`, `(P,R) +40` (frequent SK stems; no CH pair — CH is an alphabet letter, **not a tile**, per `playable_letters`).
- Fallback profiles: empty synergy set.

**Blank synergy** is already carried by the blank's +2500 base value plus the balance-halving rule; no separate blank-pair table is needed (keeping blank+high-value-consonant would otherwise double-count).

## D5: Integration with Move Search Architecture

**New module `backend/gamecore/leave_equity.py`** (pure Python, no Django imports):
- `LeaveEquityProfile` (frozen dataclass): `tile_equity_cp: Mapping[str,int]`, `vowels: frozenset[str]`, `balance_cp` table, duplicate class values, `synergy_cp: Mapping[frozenset[str],int]`.
- `profile_for_variant(variant, tile_points) -> LeaveEquityProfile`: resolves `str | VariantDefinition | None` through the existing `tiles._resolve_variant`; curated `english`/`slovak` profiles selected by slug; every other slug gets the derived fallback built from the manifest's `distribution`/`tile_points`. Build cost is O(42) — done once per searcher, no global cache needed.
- `leave_equity_cp(leave: Mapping[str,int], *, profile, bag_count) -> int`: the D1 evaluator, endgame branch included.

**`backend/gamecore/move_search.py` changes:**
- `RankedMoveCandidate.leave_value: int` → **`leave_equity_cp: int`** (signed, higher-is-better). A rename, not an addition: the semantic inversion (penalty→equity) must not survive under the old name, and the rename forces every construction site through review. Recommended over `float` (nondeterministic ordering risk) and over a parallel new field (dead weight).
- `_leave_components` and `_vowel_set` are **deleted** (they become dead code; `_vowel_set` is today defective anyway — see Orchestration critique). The remaining-rack Counter loop from `_leave_components` moves into a new `_leave_equity(placed)` which computes the leave, forms `key = tuple(sorted(leave.items()))`, and consults a per-searcher memo dict `self._leave_cache: dict[tuple, int]` (leaves repeat massively across placements; hit rate is high).
- `_rank_key` becomes:

```python
(-(candidate.total_score * 100 + candidate.leave_equity_cp),
 -(1 if candidate.rack_out else 0),
 -candidate.tiles_used,
 candidate.canonical_key)
```

`canonical_key` stays the final key: full determinism is preserved.
- **`top_k` pruning**: mechanism unchanged (insert, sort by `_rank_key`, pop beyond `top_k`); only the order changes. Because the trim now uses utility, the retained set under `MAX_RANKED_TOP_K` caps can differ from today — that is the feature, not a side effect.
- **Traversal untouched**: `_extend`, `_cross_ok`, `has_prefix` pruning, `_touch` node accounting, `seen`/`max_unique_placements`, and status/complete semantics do not consult ranking. Therefore `nodes`, `unique_placements`, `status`, `complete` are bit-identical for every input — the parity pins `nodes == 2408` / `unique_placements == 350` survive without edit.
- **Performance**: equity is computed only per *certified* candidate (post-`evaluate_scoring_move`, ≤ `max_unique_placements` = 25 000 worst case, typically hundreds), each O(rack) table lookups plus memo hits. No per-node cost, so `max_nodes`/`max_elapsed_ms` behavior is unchanged; no pre-filtering needed.
- `find_ranked_scoring_moves` signature is **unchanged** — `variant` and `tile_points` parameters already carry everything the profile needs; `bag_count` already exists for the endgame branch. Callers (`selfplay._ranked_search`, `services._probe_ai_ranked_candidates`, `position_sets._ranked_on_game`, `diagnostics`) need zero call-site changes.
- `selfplay.py` needs **no code change**: `POLICY_RANKED_BEST`/`POLICY_RANKED_WITNESS_SAFE` take `candidates[0]` and become leave-aware automatically; `_select_rack_aware` still compiles (reads `total_score`, `canonical_key`). `services.get_ai_candidates` payload shape is unchanged (exposes `score`/`tiles_used` only), so the frontend `backend_ranked_candidate` rescue path inherits the stronger ordering with zero frontend edits.

## D6: Impact Analysis on Self-Play & Existing Tests

- **`test_word_authority_parity.py`** — the frozen oracle (sections 1–4, digest-pinned `_word_passes_dictionary` copy) is **untouched**: Slice 2 changes no word verdict. Section 5's `test_ranked_search_matches_the_pinned_baseline` is a separate move-fixture pin, *not* the oracle: `nodes==2408`, `unique_placements==350`, status/complete survive unchanged (D5); `top.leave_value == 200` (verified: leave E+R, point_burden 2 → 200 under the old formula) is re-pinned as the measured `leave_equity_cp` of the new top candidate. SQUIZ 66 leaving E+R has near-maximal leave (+350+150+75 synergy, balance 0), so it very likely remains top; the pin is re-measured, never guessed.
- **`test_move_search.py`** — `test_ranked_search_is_deterministic_and_immediate_score_dominates` pins exactly the greedy semantics Slice 2 replaces (`candidates` strictly score-descending): rewritten to assert determinism plus **utility**-descending order and a re-measured deterministic top. `test_ranked_midgame_prefers_stronger_collins_move` (`candidates[0].total_score == 38 > witness`): re-derived — the new invariant is that some candidate's raw score still exceeds the witness score and `candidates[0]` maximizes utility; the exact top pin is re-measured.
- **`test_strength_benchmark.py`** — `test_ranked_strategy_beats_first_witness_on_default_balanced_seeds` (all four spreads > 0, seeds 300/301): the witness opponent is untouched by this slice, so this stays the honest A/B axis; expected to hold or improve, must be re-run, and a flipped seed is a **stop-and-investigate finding, not a re-pin** (handout lesson 6). `test_node_bound_strength_regression_tuples` — its own docstring frames the tuples `(300,0,420,…)/(300,1,505,…)/(301,0,461,…)/(301,1,501,…)` as "new candidate baselines", i.e. re-pinnable: re-pin with measured post-change tuples; current average spread ≈ +472 is the reference the new tuples should not fall below in aggregate.
- **`test_slovak_full_game.py`** — **unaffected**: measured fact, its `_simulate` runs `policy_id=POLICY_WITNESS`, which never touches ranked search, so the node-bound tuple `(55, "SIX_CONSECUTIVE_ZERO_SCORES", (303, 243))` and all conservation/leftover regressions stay byte-identical. Consequence: proving Slovak clog elimination requires **new** ranked-policy Slovak coverage (D7/D8), not edits here.
- **`test_slovak_ranked_search.py`** — assertions are order-insensitive (`status=="found"`, top score > 0, OU/AM crosses absent from *all* candidates): expected green without edit.
- **`test_endgame_policy_matrix.py` and `test_api.py`** — construct `RankedMoveCandidate(..., leave_value=…)` directly; mechanical field rename only. The `test_api` payload assertions are unaffected (leave never crossed the API).
- **Committed position-set asset** — the largest hidden blast radius: `backend/assets/diagnostics/position_sets/english-f5ae61b4.json` records `ranked_best_score` engine baselines from ranked-policy traces (seeds 300/301/302, 24 positions), and generation enforces `_assert_mount_equivalence` (top candidate's score/placements/words must equal the recorded decision). New ranking changes the traces → the asset must be **regenerated** via `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py generate_position_set --variant-slug english` (defaults `--seeds 300,301,302 --total 24` match the committed config), the old file deleted, and the new `set_digest` (also the filename suffix) updated in **four** pinned constants: `test_position_sets.py`, `test_diagnostic_session.py`, `test_diagnostic_runner.py`, `test_diagnostic_admin.py`.
- **`game/position_sets.py`, `game/diagnostics.py`** — no code change: both re-certify whatever top candidate emerges. Any additional pinned-fixture failure surfaced by the full suite (e.g. in `test_ai_play_engine_diagnostic.py`) is enumerated and classified at implementation time, never silently re-pinned.
- **Frontend** — zero changes; `ai-turn-simulation.test.ts` runs against injected fixtures, not the Python engine.

## D7: Empirical Measurement Strategy

All commands from `backend/`, RF-16 form (`env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/…`). The A/B design exploits that `find_legal_scoring_move` (the witness opponent) is untouched: pre-change vs post-change ranked-vs-witness results on identical seeds isolate exactly the ranking change.

1. **Baseline capture (pre-mutation, same Worker session, read-only):**
   - `…/pytest tests/test_strength_benchmark.py -s` → record the four default spreads and node-bound tuples.
   - `LIBRETILES_RUN_STRENGTH_ACCEPTANCE=1 …/pytest tests/test_strength_benchmark.py -s -k one_hundred` → 100-game W/D/L, total and average spread (seeds 300–349, both slots).
   - Slovak ranked baseline (no test exists yet): a read-only `.venv/bin/python` snippet driving the existing `simulate_engine_game` with `POLICY_RANKED_WITNESS_SAFE`, `variant_slug="slovak"`, seeds 0–9, recording `end_reason`, `final_scores`, `exchanges`, `passes`, `stranded_total`, `rare_unplayed` per seed. No repository mutation.
2. **Post-change measurement:** identical commands plus the new Slovak ranked strength test (node-bound pin + opt-in seed matrix printing the `end_reason` distribution).
3. **Metrics:** average spread and W/D/L vs witness (English 100-game matrix); `GameEndReason` distribution, passes/exchanges, `stranded_total`, `rare_unplayed` (Slovak ranked matrix); average placement score per ply.
4. **Acceptance thresholds:** 100-game acceptance still passes (`total_spread > 0`, `wins > losses`) with average spread ≥ baseline; Slovak ranked `BAG_EMPTY_AND_PLAYER_OUT` share strictly greater than the captured ranked baseline on the same seeds (100 % is the Whole-14 target but is owed by Slice 3's endgame solver, not this slice alone); zero `SelfPlayInvariantError` anywhere.
5. **Negative results are results:** if measured spread drops, the Worker reports the regression with both tables instead of forcing green pins.

## D8: Slice 2 Implementation Plan

Ordered steps for one implementation Worker (fresh session, `Native planning mode: not-used`):

1. Capture D7 baselines (read-only).
2. Add `backend/gamecore/leave_equity.py` (D2–D4 profiles, D1 evaluator, fallback derivation).
3. Add `backend/tests/test_leave_equity.py`: profile resolution (curated en/sk, derived e.g. czech), blank-retention beats +1-point blank dump, Q-without-U vs Q-with-U ordering, balance extremes, duplicate escalation, endgame mode switch, int-ness/determinism/clamps.
4. Wire `move_search.py`: field rename `leave_value` → `leave_equity_cp`, new `_rank_key`, profile + memo, delete `_leave_components`/`_vowel_set`.
5. Update construction sites and pins: `test_move_search.py` (two tests rewritten per D6), `test_word_authority_parity.py` (**section-5 move pins only — the oracle sections are forbidden**), `test_endgame_policy_matrix.py`, `test_api.py`.
6. Re-pin `test_strength_benchmark.py` node-bound tuples from measurement; add Slovak ranked strength coverage as new `backend/tests/test_slovak_strength.py` (keeps the witness harness file untouched).
7. Regenerate the English position set; swap the asset; update the four digest constants.
8. Gates: `ruff check .`, `mypy config game gamecore accounts catalog`, full `pytest`, plus both opt-in matrices (`LIBRETILES_RUN_STRENGTH_ACCEPTANCE=1`, `LIBRETILES_RUN_SLOVAK_FULL_GAME=1`). No frontend gates required (zero frontend paths touched).
9. One commit, explicit paths, pre-push readback per the handout Git pattern.

**Path allowlist for the implementation grant:**

```text
backend/gamecore/leave_equity.py                                  (new)
backend/gamecore/move_search.py
backend/tests/test_leave_equity.py                                (new)
backend/tests/test_move_search.py
backend/tests/test_strength_benchmark.py
backend/tests/test_slovak_strength.py                             (new)
backend/tests/test_word_authority_parity.py                       (⛔ section-5 move pins only)
backend/tests/test_endgame_policy_matrix.py                       (constructor field only)
backend/tests/test_api.py                                         (constructor field only)
backend/assets/diagnostics/position_sets/                         (delete old + add regenerated asset)
backend/tests/test_position_sets.py                               (digest constant)
backend/tests/test_diagnostic_session.py                          (digest/path constant)
backend/tests/test_diagnostic_runner.py                           (digest constant)
backend/tests/test_diagnostic_admin.py                            (digest constant)
```

**Proposed Evidence Tier: E2 (cross-cutting reversible)** — a user-visible behavioral change to AI move selection crossing gamecore, the test suite, and a committed diagnostic asset, with moderate calibration uncertainty; evidence = full backend suite plus both opt-in strength matrices plus the D7 pre/post tables; reversible single non-force commit. E1 is insufficient (not localized; behavior pins move across five test files and one asset); E3 triggers (security boundary, migration, production mutation) are absent.

---

```text
Orchestration critique:
  MEASURED — the prompt's D6 framing implies test_slovak_full_game.py exercises ranked search; measured,
    its _simulate runs POLICY_WITNESS, so leave equity cannot move any pin there and cannot by itself
    convert seed 0's SIX_CONSECUTIVE_ZERO_SCORES. New ranked-policy Slovak coverage is required to
    measure the clog claim (planned in D7/D8).
  MEASURED — the current vowel/consonant imbalance term is defective for every non-English variant:
    selfplay and services pass variant as a slug STRING, so _vowel_set(getattr(str,"vowels")) always
    falls back to AEIOU, and no shipped manifest declares "vowels" — Slovak Á/É/Í/Ó/Ô/Ú/Ý/Ä/Y are
    counted as consonants today. Slice 2 supersedes the term, so no separate fix is needed, but any
    plan revision that keeps _leave_components must treat this as a live defect.
  LEAD — the committed position-set asset digest is pinned in four test files; any future slice that
    changes ranked ordering (Slice 3, Slice 4) pays the same regeneration cost. A single shared digest
    constant would reduce that recurring surface.
Enumeration widened: backend/assets/diagnostics/position_sets/english-f5ae61b4.json plus the four
  digest-pinning test files (test_position_sets.py, test_diagnostic_session.py, test_diagnostic_runner.py,
  test_diagnostic_admin.py) — a mutation surface implied by no prompt deliverable but forced by
  _assert_mount_equivalence over recorded ranked baselines.
```

Report justification: `new-evidence`

Authority expiry: this Worker exchange's authority ends with the submission of this report; no implementation, mutation, or follow-on authority survives it, and no acceptance of this plan grants any.

One smallest next step: ORCHESTRATOR reviews this design, decides the X-valuation and threshold calibration points flagged in D2/D7 if he disagrees, and issues the Slice 2 implementation prompt (fresh Worker session, `Native planning mode: not-used`, proposed tier E2, path allowlist per D8).

Context pressure: comfortable — well under half of the window consumed, no truncation pressure.