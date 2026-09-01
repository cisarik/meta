### Report for ORCHESTRATOR_CHAT

Logical whole identity: parameterized-cli-ai-play
Worker session ordinal: 05
Worker exchange ordinal: 01

Status: **PASS**
Phase-qualified result: **implementation-PASS**; **publication-PASS** (public `origin/main` readback equals local HEAD)

Start commit: `93d665d2c25f0923fdbcdedb0df98e460175f641`
End commit: `01a1c9229fe3b9385136828384406adf03b5cb96`

Changed files (allowlist only):
- `backend/tests/test_endgame_policy_matrix.py` — harness-only three-policy matrix, invariants, default + opt-in wide run
- `backend/game/diagnostics.py` — additive `policy-comparison` report helpers; no Slice E/T behavior change; no dev-group import
- `backend/assets/diagnostics/ai_play_report_v1.schema.json` — add `policy-comparison` report kind and sample def

Zero `backend/gamecore/**` edits. Zero production search-cap, scoring, services, SSE, or prompt change.

Implementation Authority Record (echoed):
- Implementation authority: explicit
- Independence required: no
- Material phase gate: no
- Changed material axis: none
- Ordinary-only trigger: no
- Routing reopened for: none
- Unchanged axes reopened: none

Capability handshake:

| Capability | Requested | Directly observed |
|---|---|---|
| Native planning mode | not-used | absent |
| Exact model | none named | unknown-not-observably-exposed |
| Reasoning | Medium recommended | unknown-not-observably-exposed |
| Filesystem / tests / one commit / one push | required | exercised |
| Browser / provider / credentials | no authority | not used or probed |

Policy definitions and constants (harness-only; stated before any result):

Shared interface: choose a scoring placement or return `none`. Exchange and pass are identical for A/B/C and match product rules: `none` and bag ≥ 7 → exchange whole rack; `none` and bag < 7 → pass; `indeterminate` fails the test.

- **A `witness-first`**: `find_legal_scoring_move` with explicit `max_nodes=DEFAULT_MAX_NODES`, `max_elapsed_ms=10000` (same bound as the existing Slovak full-game harness). Play the first legal scoring witness.
- **B `ranked-best`**: `find_ranked_scoring_moves` with explicit production kwargs `top_k=DEFAULT_RANKED_TOP_K` (8), `max_nodes=DEFAULT_RANKED_MAX_NODES` (500000), `max_elapsed_ms=DEFAULT_RANKED_MAX_ELAPSED_MS` (750). Play `candidates[0]` (highest raw score, product tiebreak).
- **C `ranked-rack-aware`**: same ranked call and same candidate list as B. Let `S*` be max `total_score`. Eligible candidates satisfy `S* - total_score <= SCORE_LOSS_THRESHOLD`. Maximize `total_score + RARE_BONUS * rare_consumed`, then rare count, then raw score, then `canonical_key`. `rare_consumed` counts physical tiles whose `placement.letter` is in the 17 single-copy Slovak diacritics; blanks never count. If the rare set is empty (English), C is identical to B.

Constants: `RARE_BONUS = 5`, `SCORE_LOSS_THRESHOLD = 8`. No tuning loop. Opt-in env: `LIBRETILES_RUN_ENDGAME_MATRIX=1`.

Rare set (Slovak distribution ∩ diacritic ∧ count==1): `Á Ä É Í Ó Ô Ú Ý Č Ď Ĺ Ľ Ň Ŕ Š Ť Ž` (17). English rare set is empty. No `isascii` predicate in new code; two-letter policy is complete-formed-word membership via `_word_passes_dictionary`.

Orchestrator baseline: **reproduced**.
- Slovak A, seed 0: `SIX_CONSECUTIVE_ZERO_SCORES`, **55 plies** (exact).
- Slovak A, seeds 1–3: `{SIX_CONSECUTIVE_ZERO_SCORES: 3}` (exact). Zero `BAG_EMPTY_AND_PLAYER_OUT` under A.
- Precision vs Orchestrator prose: seed 0 A ended with **bag=0**, racks 3+5 (stranded 8), rare_unplayed **3/17**, passes=7, exchanges=0. The bag was already empty; tiles were stranded on racks, not in the bag.
- English 100-game witness mix `{BAG_EMPTY_AND_PLAYER_OUT: 15, SIX_CONSECUTIVE_ZERO_SCORES: 85}` was not re-run here (existing slow harness). This slice’s English A seeds 0–3 were all `SIX_CONSECUTIVE_ZERO_SCORES`, consistent with that majority.

Default run: seeds `(0,)`, both variants, all three policies = **6 games**, wall **24.615s** (repeat 24.845s). File run including the extra uncached determinism pair: **35.6s**. Under the ~2 minute budget.

Opt-in wide: seeds `(1, 2, 3)`, both variants, all three policies = **18 games**, wall **73.640s**. Combined `LIBRETILES_RUN_ENDGAME_MATRIX=1` command: **109.1s**, 8 passed.

FULL metric table (default seed 0):

| variant | policy | plies | end_reason | bag | racks | stranded | rare_unplayed | exch | pass | placement | final |
|---|---|---|---|---|---|---|---|---|---|---|---|
| slovak | witness-first | 55 | SIX_CONSECUTIVE_ZERO_SCORES | 0 | 3+5 | 8 | 3/17 | 0 | 7 | 308/270 | 303/243 |
| slovak | ranked-best | 29 | BAG_EMPTY_AND_PLAYER_OUT | 0 | 0+1 | 1 | 0/17 | 0 | 0 | 520/558 | 521/557 |
| slovak | ranked-rack-aware | 26 | BAG_EMPTY_AND_PLAYER_OUT | 0 | 1+0 | 1 | 0/17 | 0 | 0 | 469/445 | 468/446 |
| english | witness-first | 69 | SIX_CONSECUTIVE_ZERO_SCORES | 0 | 1+5 | 6 | 0/0 | 0 | 7 | 376/174 | 375/138 |
| english | ranked-best | 22 | BAG_EMPTY_AND_PLAYER_OUT | 0 | 1+0 | 1 | 0/0 | 0 | 0 | 512/417 | 511/418 |
| english | ranked-rack-aware | 22 | BAG_EMPTY_AND_PLAYER_OUT | 0 | 1+0 | 1 | 0/0 | 0 | 0 | 512/417 | 511/418 |

Wide aggregate (seeds 1–3):

| variant | policy | end_reasons | plies min/med/max | stranded min/med/max | rare_unplayed min/med/max | pass min/med/max |
|---|---|---|---|---|---|---|
| slovak | witness-first | SIX: 3 | 61/63/72 | 5/6/6 | 3/5/6 of 17 | 6/7/8 |
| slovak | ranked-best | BAG: 3 | 25/26/26 | 1/2/2 | 0/1/2 of 17 | 0/0/0 |
| slovak | ranked-rack-aware | BAG: 2, SIX: 1 | 23/25/35 | 2/3/4 | 0/2/2 of 17 | 0/0/6 |
| english | witness-first | SIX: 3 | 70/70/74 | 4/5/6 | 0/0/0 | 6/6/6 |
| english | ranked-best | BAG: 3 | 19/21/25 | 1/3/5 | 0/0/0 | 0/0/0 |
| english | ranked-rack-aware | BAG: 3 | 19/21/25 | 1/3/5 | 0/0/0 | 0/0/0 |

Search cost is observational only. Seed-0 A ~282 nodes / 3.5 ms per decision; Slovak B ~4921 nodes / 140 ms; English B ~15k nodes / 353 ms. No `indeterminate`.

Invariants: every game terminated with an allowed end reason; tile conservation held; two-letter policy held (complete-word membership, no substring, no `isascii`); English C === English B on every measured seed (control that C does not inject a variant-biased predicate).

Interpretation (evidence, not a product decision):
- The lever that **does** move Slovak endgame occupancy is **A → B**: first-witness vs product-like highest-score. On seeds 0–3, A is 4/4 `SIX_CONSECUTIVE_ZERO_SCORES` with 3–6 rares unplayed; B is 4/4 `BAG_EMPTY_AND_PLAYER_OUT` with 0–2 rares unplayed and no passes.
- The lever that **does not** help, and on seed 3 **hurts**, is **C**: reranking the same top-8 list with a rare-tile bonus. Seed 3 C fell back to `SIX_CONSECUTIVE_ZERO_SCORES` (35 plies, 2 rares unplayed, 6 passes) while B went out. A negative result for C is a PASS. C must not be promoted.
- English control shows the same A-vs-B end_reason split and identical B/C traces, so the Slovak A-vs-B gap is not a harness ASCII bias.

Validation:
- `pytest tests/test_endgame_policy_matrix.py -q -s`: 7 passed, 1 skipped, default matrix 24.6s
- `LIBRETILES_RUN_ENDGAME_MATRIX=1 … -m "slow or not slow"`: 8 passed, wide 73.6s
- Stay-green list: passed, 3 expected skips
- ruff: clean on `game/diagnostics.py` and `tests/test_endgame_policy_matrix.py`
- mypy (required command): **Found 12 errors in 6 files (checked 18 source files)**; **zero in touched files**

Commit subject: `test(engine): measure Slovak endgame policy matrix`
Commit SHA: `01a1c9229fe3b9385136828384406adf03b5cb96`
Pre-push gate: `git ls-remote origin refs/heads/main` = `93d665d2c25f0923fdbcdedb0df98e460175f641`
Push result: fast-forward `93d665d..01a1c92  main -> main` (non-force)
Public readback SHA: `01a1c9229fe3b9385136828384406adf03b5cb96` (local HEAD = `origin/main` = `ls-remote`)
Final `git status --porcelain`: empty
Temp cleanup: pytest `tmp_path` report file only; no leftover mktemp; cleanup OK

Deviations, risks, missing evidence:
- No fourth partial-rack exchange policy.
- English 100-seed witness mix not re-measured in this slice.
- C only reranks B’s top-8; a rare dump that is not in that list cannot be chosen. That is part of why C did not help.
- Sample is 4 Slovak seeds. Direction is consistent; it is not a 100-game claim.

One smallest next step: do **not** issue a production heuristic slice for C. If a later slice acts on this evidence, measure shipping **ranked-best** (already the product English quality path) on the Slovak AI path, on a larger seed matrix, still without a rack-bonus.

Report justification: new-evidence
Logical-whole closure: not-closed
Authority expiry: this exchange’s authority expires with this terminal report.

Resolved Execution Issues / Near-Misses: ranked 750 ms cap could have returned `indeterminate` on Slovak; it did not. C’s seed-3 regression was reported, not tuned away.

Pre-Existing Failure Classification: parked mypy debt is unchanged — 12 errors in 6 files (`config/settings.py`, `game/models.py`, `game/realtime.py`, `gamecore/scoring.py`, `gamecore/game.py`, `game/services.py`). None introduced by this slice; `game/diagnostics.py` is clean.