### Report for ORCHESTRATOR_CHAT

Logical whole identity: admin-provider-model-console  
Worker session ordinal: 04, Worker exchange ordinal: 03

**Status:** PASS  
**Phase-qualified result:** implementation-PASS  
**Start commit:** `3faa3f83ed8358d833c55f34dfb0b4f25451370d`  
**End commit:** `c9396f417baf5b44e60469432be871671d030a37`

**Changed files**
- `backend/game/position_sets.py` — complete-state capture, `game_from_snapshot`, generation-time mount-equivalence (F9).
- `backend/tests/test_position_sets.py` — F4 cell key `premium_used`; F8 extra complete-state keys; F9 JSON-roundtrip mount; digest re-pin.
- `backend/assets/diagnostics/position_sets/` — `english-8d40f3bc.json` replaced by `english-f4d334c8.json`. Command file / `gamecore` untouched.

**State-surface enumeration** (measured from `Game`, `PlayerState`, `Cell`, `TileBag`)

| Field | Before | If missing | Now |
|---|---|---|---|
| `Cell.token` / `blank_as` | captured | tile identity / blanks wrong | captured |
| `Cell.premium_used` | **miss** | consumed premiums re-awarded; MQR denominator corrupt | captured |
| `Cell.premium` | omitted | layout, not progress | **omitted** — reload `Board(premiums_path)`; not game-progress |
| `Cell.letter` / `is_blank` / derived | omitted | derived from token+blank_as | omitted (derived) |
| acting `rack` / `opponent_rack` | captured | cannot mount seats | captured |
| `PlayerState.score` | **miss** | final reported scores wrong | `seat_scores` |
| `PlayerState.pass_streak` | **miss** | seat pass state lost on continue | `seat_pass_streaks` |
| `PlayerState.name` | **miss** | leftover/score keys drift | `seat_names` |
| `Game.current_index` | captured | wrong seat to move | `to_move_seat_index` |
| `Game.consecutive_scoreless_turns` | **miss** | six-zero endgame fires late/early | captured |
| `Game.ended` / `end_reason` | **miss** | terminal vs live mount confused | captured |
| `Game.leftover_points` / `winner_name` | **miss** | post-terminal scores/winner lost | captured |
| `Game._no_moves_available` | **miss** | `NO_MOVES_AVAILABLE` end reason wrong | `no_moves_available` |
| `TileBag.tiles` / count | captured | bag identity wrong | captured |
| `TileBag._rng` | **miss** | next exchange shuffle diverges | `bag_rng_state` (lossless `getstate`) |
| `TileBag.variant*` | omitted | reconstructed from `variant_slug` | omitted (slug is enough) |
| `TileBag.seed` attr | snapshot `seed` | RNG restored via `setstate`; reconstructed `.seed` is `None` | play seed stays on snapshot |

**F9** — at capture, every ply snapshot is mounted via `game_from_snapshot` (pure gamecore, no DB). One node-bound `find_ranked_scoring_moves` on the mounted game is compared to the original trace decision: `status`, `complete`, `nodes`, score, placements, words. `elapsed_ms` is observational and not compared. Mismatch aborts generation. Tests re-check after JSON round-trip. Result: PASS on all candidate plies of seeds 300–302 and on the 3-position envelope.

Gate summaries (verbatim):
- mypy: `Success: no issues found in 88 source files`
- ruff: `All checks passed!`
- pytest: `843 passed, 4 skipped in 515.82s (0:08:35)`

Baseline at `3faa3f8`: 88 files, `842 passed, 4 skipped`. One test added (F9); no removals, no new skips. Python via `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python`.

NEW `set_digest`: `f4d334c82d50c5ba05deeebe96a4bb8038c3ee14290e87e0d194d57ae33e7b48`

**Commit and push**  
Subject: `feat(game) complete-state position snapshots with mount-equivalence`  
Pre-push `git ls-remote origin refs/heads/main`: `3faa3f83ed8358d833c55f34dfb0b4f25451370d`  
Push: non-force fast-forward `3faa3f8..c9396f4`  
Readback: local `c9396f417baf5b44e60469432be871671d030a37` = remote `c9396f417baf5b44e60469432be871671d030a37`  
Porcelain empty; `## main...origin/main`

**Deviations / risks / missing evidence**  
`Cell.premium` is intentionally not in the JSON (layout asset). Fixture `generator_source_revision` is parent `3faa3f8`. Reconstructed `TileBag.seed` is `None`; RNG and play seed are still complete.

**Smallest next step**  
Orchestrator acceptance of slice 3; then slice 4 persisted diagnostic session that mounts `english-f4d334c8.json`.

**Report justification:** new-mutation

**Authority expiry:** This Worker’s authority ended at this report. Slice 3 is closed pending Orchestrator acceptance. No slice 4, no Meta archive.

Resolved Execution Issues / Near-Misses: none — F9 node counts matched on the first capture pass; no comparison was weakened.

Pre-Existing Failure Classification: none

Orchestration critique:  
MEASURED — mount still binds to shipped `premiums.json` for `Cell.premium` tags. A layout change would alter scores of an old fixture without changing that fixture’s `set_digest`.  
LEAD — that is the same class of coupling as the lexicon file; storing per-cell premium tags would make the snapshot layout-independent at the cost of duplicating the board asset. Not a play-state gap.

Enumeration widened: snapshot field set only (not `report_kind`). New keys: `premium_used`, `seat_names`, `seat_scores`, `seat_pass_streaks`, `bag_rng_state`, `consecutive_scoreless_turns`, `ended`, `end_reason`, `leftover_points`, `winner_name`, `no_moves_available`.

Context pressure: moderate — Game/Cell/TileBag surfaces plus F9 comparison were in view; enough headroom to keep RNG lossless and skip wall-clock.