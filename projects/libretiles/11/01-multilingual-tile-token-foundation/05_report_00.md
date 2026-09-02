### Report for ORCHESTRATOR_CHAT

Logical whole `multilingual-tile-token-foundation`. Worker session `05`. Worker exchange `01`.

1. **status:** `PASS`

2. **Phase-qualified result: implementation-PASS**

Evidence is **non-independent**. This report is not logical-whole closure and not independent acceptance. Independent acceptance is not required for this slice; the whole receives one fresh independent R4 application audit after slice F3.

3. **Start and end commit**

```text
start: 3fd1a81d79b95a1244db9aa9d4b84ba75a59d6f0
end:   8c00a331560f16b7d27eae04dc789a5124dd4497
```

4. **Section 2 gate evidence** (working directory `/home/agile/Projects/libretiles`)

```text
git rev-parse HEAD
3fd1a81d79b95a1244db9aa9d4b84ba75a59d6f0

git rev-parse HEAD:.ap
9c5cc44f8b6c92dd56ad2427d13223d7d59c5656

git -C .ap rev-parse HEAD
9c5cc44f8b6c92dd56ad2427d13223d7d59c5656

git status -sb
## main...origin/main
?? frontend/public/cs.png
?? frontend/public/cz.jpeg
?? frontend/public/en.jpeg
?? frontend/public/en.png
?? frontend/public/hu.jpeg
?? frontend/public/hu.png
?? frontend/public/pl.jpeg
?? frontend/public/pl.png
?? frontend/public/sk.jpeg
?? frontend/public/sk.png

git ls-remote origin refs/heads/main
3fd1a81d79b95a1244db9aa9d4b84ba75a59d6f0	refs/heads/main
```

Porcelain was exactly the ten untracked Cooperator flag images. They were not touched. `.venv/bin/python` present (`Python 3.12.12`). Route: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python …`.

**G0.2** — only these two values from `settings.DATABASES["default"]`:

```text
django.db.backends.sqlite3
/home/agile/Projects/libretiles/backend/db.sqlite3
```

**G0.5** — `PRAGMA integrity_check` == `ok`. `django_migrations` 63. Game leaf `0007_consumedwsticket`.

**G0.6** — `ss -tlnp | grep -E ':(3000|8000)'` → no listeners. `fuser` on the absolute db path → empty. Nothing killed.

**Branch taken: NON-EMPTY.** Five counts before purge:

```text
game_chat_message          0
game_move                  0
game_player_slot           2
game_session               1
game_consumed_ws_ticket    0
```

Fresh checkpoint (did not touch `/tmp/opencode/mtt-f2a-checkpoint/`):

```text
path              /tmp/opencode/mtt-f2b-checkpoint/db.sqlite3.f2b-checkpoint
byte size         389120
SHA-256           3e9438ac04c71fac934dc142b3a1cc40683ef0d6dfe5a52cec7cc4eec18c70a4
integrity_check   ok
five counts       chat 0, move 0, slot 2, session 1, ticket 0  (equal to live)
created by        /usr/bin/sqlite3 .backup  (not cp)
```

`--dry-run` output, quoted:

```text
INFO game purge_legacy_game_state pre-purge counts: {'game_chat_message': 0, 'game_move': 0, 'game_player_slot': 2, 'game_session': 1, 'game_consumed_ws_ticket': 0}
INFO game purge_legacy_game_state dry-run; no rows deleted
pre-purge counts: {'game_chat_message': 0, 'game_move': 0, 'game_player_slot': 2, 'game_session': 1, 'game_consumed_ws_ticket': 0}
dry-run: would delete rows from game_chat_message, game_move, game_player_slot, game_session, game_consumed_ws_ticket in order ChatMessage, Move, PlayerSlot, GameSession, ConsumedWsTicket; no rows deleted.
```

Live purge (one-shot `ALLOW_DESTRUCTIVE_GAME_STATE_RESET=true` on that command only; `.env` not read or written):

```text
deleted 0 rows from ChatMessage
deleted 0 rows from Move
deleted 2 rows from PlayerSlot
deleted 1 rows from GameSession
deleted 0 rows from ConsumedWsTicket
post-purge counts: {'game_chat_message': 0, 'game_move': 0, 'game_player_slot': 0, 'game_session': 0, 'game_consumed_ws_ticket': 0}
```

Five counts after purge: all 0. Every protected table identical to the before map. F2a checkpoint SHA-256 unchanged (`af196f178cf1e711401c3d9912deb7896200c3a65365d8bc14b1718e06039931`).

5. **Changed paths**

| path | action | purpose |
|---|---|---|
| `backend/game/migrations/0008_atomic_token_state_schema.py` | NEW | refusal guard (forward first + reverse first via a trailing RunPython), RemoveField `blanks`, RemoveField+AddField `bag_tiles` as JSON, AlterField `board_state` |
| `backend/game/models.py` | keep | drop `blanks`; `bag_tiles` JSON token array; structured `board_state` default; rack help text |
| `backend/game/services.py` | keep | structured persist/load; bag list copy; starting-draw via F1 helper; temporary one-code-point wire adapter |
| `backend/game/admin.py` | keep | remove the single `"blanks"` `readonly_fields` entry |
| `backend/tests/test_atomic_token_persistence.py` | NEW | P1–P9 |
| `backend/tests/test_api.py` | keep | old field-shape fixtures → structured cells / token lists |
| `backend/tests/test_slovak_engine.py` | keep | NFC board-from-session fixture → one structured cell |
| `backend/tests/test_slovak_full_game.py` | keep | empty board/bag fixtures → structured / `[]` |
| `backend/tests/test_scoreless_turns_migration.py` | keep | **ninth path (deviation):** delete leftover `game_session` before `restore_apps_to_leaf("game")` so 0008's refusal does not trap the 0005↔0006 rename test |

`session.blanks` sites removed from `services.py` (line numbers at baseline `3fd1a81`):

```text
237  for pos in session.blanks or []
258  blanks: list[...] = []  (local builder)
267  blanks.append({"row": r, "col": c})
274  session.blanks = blanks
370  "blanks": session.blanks
482  session.blanks = []
497  "blanks" in update_fields
```

Two additional writes of `blanks=[]` at create/join (baseline 1023 and 1347) were also removed; they would have been `TypeError` after the field deletion.

6. **24-table map around the live `migrate game 0008`**

django_migrations **63 → 64**. New row: `game|0008_atomic_token_state_schema`. Five game-state tables stayed 0. Every other table identical. `blanks` column absent from `game_session` after migrate.

| table | before | after |
|---|---:|---:|
| `accounts_user` | 4 | 4 |
| `accounts_user_groups` | 0 | 0 |
| `accounts_user_user_permissions` | 0 | 0 |
| `auth_group` | 0 | 0 |
| `auth_group_permissions` | 0 | 0 |
| `auth_permission` | 76 | 76 |
| `axes_accessattempt` | 0 | 0 |
| `axes_accessattemptexpiration` | 0 | 0 |
| `axes_accessfailurelog` | 0 | 0 |
| `axes_accesslog` | 0 | 0 |
| `catalog_ai_model` | 12 | 12 |
| `catalog_ai_prompt` | 4 | 4 |
| `django_admin_log` | 0 | 0 |
| `django_content_type` | 19 | 19 |
| `django_migrations` | 63 | 64 |
| `django_session` | 0 | 0 |
| `game_chat_message` | 0 | 0 |
| `game_consumed_ws_ticket` | 0 | 0 |
| `game_move` | 0 | 0 |
| `game_player_slot` | 0 | 0 |
| `game_session` | 0 | 0 |
| `sqlite_sequence` | 17 | 17 |
| `token_blacklist_blacklistedtoken` | 5 | 5 |
| `token_blacklist_outstandingtoken` | 24 | 24 |

`showmigrations game` before: 0008 unchecked. After: 0008 `[X]`.

7. **Eight gates**

Before live migrate (implementation candidate):

| gate | result |
|---|---|
| mypy `config game gamecore accounts catalog` | `Success: no issues found in 83 source files` (baseline 82; +1 is `game/migrations/0008_atomic_token_state_schema.py`) |
| ruff | `All checks passed!` |
| `manage.py check` | `System check identified no issues (0 silenced).` |
| pytest | first full run `3 failed, 367 passed, 4 skipped` (scoreless restore + two WS IntegrityError cascades); after the ninth-path finally: `370 passed, 4 skipped in 196.89s (0:03:16)` |
| `npm run typecheck` | exit 0 (`tsc --noEmit --incremental false`) |
| `npx vitest run` | `Tests  342 passed \| 3 skipped (345)` / `Test Files  26 passed \| 1 skipped (27)` |
| `npm run lint` | exit 0 |
| `npm run build` | exit 0 after `ss -tlnp \| grep :3000` showed no listener |

The code type-checks (mypy 83 files; frontend `tsc --noEmit --incremental false` exit 0). The build passed. Those are separate claims.

After live migrate:

```text
manage.py check: System check identified no issues (0 silenced).
pytest: 370 passed, 4 skipped in 197.60s (0:03:17)
```

Accounting: baseline 361 passed + 9 new P-cases = 370.

8. **Pre-fix / post-fix for P1–P9**

| case | pre-fix | post-fix |
|---|---|---|
| P1 | applying the schema rewrite with a `GameSession` row present would drop/retype columns under live rows | `RuntimeError` names `manage.py purge_legacy_game_state`; the row still exists |
| P2 | reverse after games exist would recast JSON tokens into joined strings | empty tables apply 0008 and reverse to 0007; `blanks` gone forward, restored on reverse |
| P3 | `"".join(["SZ","A"])` → `"SZA"`; `list("SZA")` → `["S","Z","A"]` | one cell `{"token":"SZ","blank_as":None}` and bag `["SZ","A"]` after reload |
| P4 | blank identity lived in a sidecar coordinate list; joined-string board could not store `blank_as="CS"` | round-trip `{"token":"?","blank_as":"CS"}`; `is_blank` true; `base_points==1` (blank contributes 0) |
| P5 | `len("SZA")==3` (`bag_remaining` counted code points). Captured: `F06 len('SZA'): 3 (expect 2 tiles)` | `bag_tiles=["SZ","A"]` → `bag_remaining==2` |
| P6 | `_perform_starting_draw` used `slot0_value <= slot1_value`. Captured: `('Á' <= 'Z') is False`; draw `slot0_first: False` for Á vs Z | Slovak Á beats Z; blank lowest; English A-before-Z unchanged; equal tokens → slot 0 |
| P7 | `_build_state` emitted raw `session.board_state` / `session.blanks` | 15 strings of 15 chars; `blanks == [{"row":7,"col":7}]` for a center blank |
| P8 | joined persist truncated or split `SZ` | `ValueError` with `_WIRE_ADAPTER_REMOVAL` naming `state_schema_version 4` |
| P9 | n/a (rack was already a JSON list) | `["A","A","?","B"]` round-trips through `_build_state["my_rack"]` |

9. **Every changed expected value in the three existing suites**

All classified **shape**. No behaviour assertion was retargeted.

**`test_api.py`**

| location | pre | post | class |
|---|---|---|---|
| scoring fixture `board` | 15 joined `"."` strings, T spliced into row 7 | `[[None]*15]`, cell `[7][8]={"token":"T","blank_as":None}` | shape |
| scoring fixture `bag_tiles` | `""` | `[]` | shape |
| AI-pass fixture `bag_tiles` | `"ABCDE"` | `["A","B","C","D","E"]` | shape |
| `_ai_turn_game` param | `bag_tiles: str \| None` | `list[str] \| None` | shape |
| `_ai_turn_game` board type | `list[str] \| None` | `list[Any] \| None` | shape |
| playability `bag_tiles="ABCDEF"` | string of 6 chars | `["A","B","C","D","E","F"]` | shape |
| three `bag_tiles="ABCDE"` callers | string of 5 chars | five-token lists | shape |
| live-incident board | joined row with `S` at index 7 | cell `[7][7]={"token":"S","blank_as":None}` | shape |

Assertion values (`BAG_EMPTY_AND_PLAYER_OUT`, scores 7 / −3, `"bag_tiles" not in serialized`, 409 codes) are unchanged.

**`test_slovak_engine.py`**

| location | pre | post | class |
|---|---|---|---|
| `test_board_from_session_nfc_keeps_fifteen_cells` | NFD `Š` concatenated into a 15-char row string plus `blanks=[]` | one structured cell `{"token": <NFD Š>, "blank_as": None}` | shape |

Expected values still: cell (0,0) is NFC `Š`; cell (0,1) empty.

**`test_slovak_full_game.py`**

| location | pre | post | class |
|---|---|---|---|
| endgame fixture `board_state` | `["." * 15] * 15` | `[[None] * 15 for _ in range(15)]` | shape |
| endgame fixture `bag_tiles` | `""` | `[]` | shape |

Leftover-point assertions unchanged.

10. **Unchanged surfaces (explicit)**

- `_word_passes_dictionary` is byte-identical.
- `backend/game/serializers.py` is unchanged (`git diff` empty).
- `backend/gamecore/` is unchanged.
- Emitted REST/websocket shape: `board` is still 15 joined strings, `blanks` is still a coordinate list, no `state_schema_version`. The adapter is what keeps that byte-identical for English and Slovak.
- Frontend tree unchanged (vitest still 342; ten flag images still untracked).

11. **Temporary wire adapter**

Source: `backend/game/services.py` `_legacy_wire_board_and_blanks` (lines 321–364), called from `_build_state` (line 442).

Removal condition, recorded in the docstring and the raise message: **deleted when the wire format moves to `state_schema_version` 4.**

12. **Cell storage inversion**

`Cell`'s storage fields remain `letter` and `is_blank`. Tokens are read through the F1 derived properties and written back through those storage fields. Inverting storage onto `token` / `blank_as` is deferred and may be dropped later with a recorded decision.

13. **INFOSEC R1 + R2 (non-independent)**

Threat model:

- Assets: persisted game state, bag occupancy, starting-draw fairness, legacy wire envelope.
- Trust boundaries: Django ORM / SQLite; REST and websocket emission of `_build_state`.
- Actor: local authenticated player / operator. Migration 0008 is operator-facing and deletes no rows.
- Properties: no silent token split; empty bag stays empty; adapter fails closed on multi-code-point tokens; schema change refuses if any of the five tables is non-empty, including on reverse.
- Abuse cases: apply 0008 with live games (refused); reverse 0008 with new-shape games (trailing RunPython refuses first); truncate `SZ` on the wire (raises).

Inline review of this diff found no candidate above `low`. No authN/Z, secret, or cryptographic touch. Residual: `tests/diagnostics/test_turn_probe.py` still assigns a string grid and a non-field `session.blanks`; empty-board fixtures still pass because skipped string rows look empty. Not modified (outside allowlist). Recorded, not fixed.

14. **Deviations, risks, missing evidence**

- **Ninth path:** `backend/tests/test_scoreless_turns_migration.py`. The 0008 refusal made `restore_apps_to_leaf("game")` fail on that test's leftover `GameSession`, then left the test DB at 0007 (`blanks` NOT NULL) so two websocket tests raised `IntegrityError`. One correction: delete the leftover row in `finally`, same pattern as P1. Pytest then 370. Staged and committed because the selected validation ladder is the full suite; leaving it out would publish a red suite. Disclose vs section 6's eight-path list.
- Trailing `RunPython(refuse, refuse)` in 0008 is extra to the four named operations. Without it, Django reverse order would undo schema *before* refusing. Needed for the stated reverse invariant.
- `_bag_from_session` must not pass `tiles=[]` into `TileBag`: that constructor treats an empty list as “fill from the distribution”. Empty persisted bags take the old create-and-draw-all path. See near-miss below.
- P1/P2 pre-fix failure output is reconstructed from the unguarded behaviour, not from a recorded pytest run against an unguarded 0008 (the guard shipped in the first candidate). P5/P6 pre-fix output is reproduced-dynamic against `3fd1a81` services.
- Did not independently re-verify websocket byte identity with a live client; adapter tests plus unchanged `test_api.py` assertions are the evidence.

15. **Resolved Execution Issues / Near-Misses**

- `TileBag(tiles=[])` silently refills a 100-tile bag. First scoring-endgame test then failed (`game_end_reason == ''` instead of `BAG_EMPTY_AND_PLAYER_OUT`) because the empty JSON bag was read back as a full bag. Fixed in `_bag_from_session` before the full suite. This is exactly the class of persistence bug the slice exists to catch.
- First full pytest: scoreless restore refused, then WS inserts hit leftover `blanks` NOT NULL. Classified as harness contamination from the new guard, not as a product regression. One correction on the ninth path.
- `addopts = "-q"`: no second `-q`. Summaries quoted verbatim.

16. **Pre-Existing Failure Classification**

None that blocked the slice. Latent, outside allowlist, tests still green: `backend/tests/diagnostics/test_turn_probe.py` `apply_scenario` writes joined-string `board_state` and sets `session.blanks` as a non-field attribute. Empty-board named fixtures remain equivalent under the new reader. Seeded-board diagnostic fixtures would load as empty. Recorded, not fixed.

17. **Commit and push**

```text
git add <nine explicit paths>
git commit  8c00a331560f16b7d27eae04dc789a5124dd4497
            feat(game): store atomic tokens and fix the bag count and starting draw
pre-push ls-remote origin refs/heads/main
            3fd1a81d79b95a1244db9aa9d4b84ba75a59d6f0
git push origin main
            3fd1a81..8c00a33  main -> main
public readback
            ls-remote  8c00a331560f16b7d27eae04dc789a5124dd4497
            rev-parse  8c00a331560f16b7d27eae04dc789a5124dd4497
```

Ten flag images remain untracked and unstaged. No `*.sqlite3` staged. Non-force push.

18. **Smallest next step**

F2c: emit `state_schema_version` 4 with `BoardCell[][]`, DELETE `_legacy_wire_board_and_blanks`, and update the frontend in the same slice (types, store persist v4, board / tile / blank picker / draw rendering). Also relax the `serializers.py` one-code-point placement filter together with that wire format.

Hand forward:

```text
- F2c: emit state_schema_version 4 with BoardCell[][], DELETE the temporary adapter, and update the
  frontend in the same slice — types, store persist v4, board / tile / blank picker / draw rendering
- F2c or later: re-point evaluate_scoring_move at WordAuthority and DELETE _word_passes_dictionary.
  Two authority paths must not become permanent.
- F2c: relax the serializers.py one-code-point placement filter, together with the wire format
- F3: build_ai_state_dict is still lossy for multi-code-point cells; the AI boundary is F3's
- optional, may be dropped with a recorded decision: invert Cell storage onto token / blank_as and
  remove the F1 derived properties
- later: retarget tests/diagnostics/test_turn_probe.py apply_scenario onto structured cells
```

`Report justification: new-mutation`

`Logical-whole closure: not-closed`

This Worker's authority expired at this terminal report. A follow-up in the same conversation needs a new complete prompt targeting `current-worker-session`.
