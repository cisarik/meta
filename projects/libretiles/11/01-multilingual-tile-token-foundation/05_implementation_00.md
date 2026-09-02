You are a WORKER instance assigned to the persistent AP WORKER role. Execute exactly this bounded task and stop.

```text
Logical whole identity: multilingual-tile-token-foundation
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: MTT-F2b — token-shaped persistence, and two live defects
Phase: Implementation
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Exact baseline: 3fd1a81d79b95a1244db9aa9d4b84ba75a59d6f0
Logical-whole closure: not-closed
```

Reasoning recommendation: **High.** Named risk: this slice rewrites the persistence layer of a shipped, working game and corrects a live rules defect in the starting draw. A representation change that silently loses a tile is not caught by a type checker.

```text
Evidence tier: E2
Evidence tier basis: cross-cutting but fully reversible. The migration runs on EMPTY tables — slice
  F2a already purged them — so there is no data at risk and the schema change is reversible while they
  stay empty. That de-risking is exactly what F2a bought.
Combined implementation envelope: allowed — code, migration, tests, one commit, one non-force push
Activated stricter profile: INFOSEC.md at R1 + R2, inline, non-independent
Independent acceptance: not-required for this slice; the whole receives one fresh independent R4
  application audit after slice F3
Validation ladder: selected. Inspection required; the affected backend suites; new causal regressions
  for both live defects; the full suite because persistence is cross-cutting.
```

## 1. What this slice is, and what it is deliberately NOT

**Is:** the database stores **atomic tokens** instead of joined strings, and two live defects are corrected.

**Is NOT:** any change to what words are legal, to request validation, to the wire format the browser sees, or to the frontend. `_word_passes_dictionary` stays exactly as it is. `serializers.py` stays exactly as it is. The REST and websocket payloads stay **byte-identical** behind a documented temporary adapter.

That last constraint is the point of the slice boundary. If the backend emitted a new shape while the frontend still read the old one, the product would be broken between two commits. The Cooperator opens this application, and a fresh clone that crashes is a first-class defect in his frame. A small named adapter that the next slice deletes is cheaper than a broken window.

## 2. Repository gate

```text
Repository checkout topology: standalone checkout
Working directory: /home/agile/Projects/libretiles
Expected branch: main
Expected HEAD: 3fd1a81d79b95a1244db9aa9d4b84ba75a59d6f0
Expected .ap gitlink and submodule HEAD: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Working-copy topology: canonical-checkout
```

Verify and quote: `git rev-parse HEAD`, `git rev-parse HEAD:.ap`, `git -C .ap rev-parse HEAD`, `git status -sb`, `git ls-remote origin refs/heads/main`, `git status --porcelain=v1`.

Porcelain must be **exactly** the ten untracked Cooperator flag images (`frontend/public/{cs,en,hu,pl,sk}.png` and `{cz,en,hu,pl,sk}.jpeg`) and nothing else. Do not touch them. Anything else: classify with all five AP recovery classes; stop if the primary class is `unexplained-divergence`.

### 2a. Database precondition — the five game tables must be empty when the migration runs

```text
game_chat_message  game_move  game_player_slot  game_session  game_consumed_ws_ticket
```

They were emptied at `3fd1a81`, but **the Cooperator has since played a game** — the Orchestrator measured `game_session 1` and `game_player_slot 2` at the time this prompt was written. That is expected and was invited: he was asked to verify the product still works after the purge.

So count all five yourself, and take **exactly one** of these two branches.

**Branch EMPTY — all five are already 0.** Proceed straight to section 3. Take no checkpoint and run no purge. Record the counts.

**Branch NON-EMPTY — any of the five holds a row.** You are authorized to clear them, in this exact order and with no improvisation:

```text
1  fresh checkpoint, into a NEW directory so the F2a checkpoint is not overwritten:
     mkdir -p /tmp/opencode/mtt-f2b-checkpoint
     sqlite3 /home/agile/Projects/libretiles/backend/db.sqlite3 \
       ".backup '/tmp/opencode/mtt-f2b-checkpoint/db.sqlite3.f2b-checkpoint'"
   ⛔ Not `cp`. Then PROVE it: report byte size and SHA-256; `PRAGMA integrity_check` on the
   checkpoint must be `ok`; and the five counts read FROM the checkpoint must equal the live ones.
   ⛔ Do NOT touch or delete /tmp/opencode/mtt-f2a-checkpoint/ — it belongs to the Cooperator.

2  capture the complete 24-table count map

3  dry run first, and quote its output:
     env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py purge_legacy_game_state --dry-run

4  then the purge, with the flag as a ONE-SHOT environment variable on that command only:
     ALLOW_DESTRUCTIVE_GAME_STATE_RESET=true \
       env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py purge_legacy_game_state
   ⛔ Do NOT write that flag into backend/.env, and do not read that file.

5  capture the 24-table map again and assert: the five are 0, and EVERY other table is identical to
   the before map. Any protected-table change: STOP and report immediately.
```

This is inside the Cooperator's standing authorization — his words, 2026-09-01: `obetovatelne - vsetky rozohrate vymazat predsa, su to len testovacie hry`. The command you are invoking is the one slice F2a committed, tested with nine cases, and proved fail-closed; running it here is also useful second evidence that it works in real use. You are **not** authorized to delete rows by any other means, from any other table, or on any other database.

### 2b. The rest of the gate

Confirm, read-only: `settings.DATABASES["default"]["ENGINE"]` is `django.db.backends.sqlite3` and `["NAME"]` is `/home/agile/Projects/libretiles/backend/db.sqlite3` — print only those two values; `PRAGMA integrity_check` is `ok`; `django_migrations` is 63 and the `game` leaf is `0007_consumedwsticket`; and `ss -tlnp | grep -E ':(3000|8000)'` plus `fuser backend/db.sqlite3` show nothing holding the file.

⛔ **The Cooperator was asked to stop both servers before delivering this prompt.** If either is still up — the Orchestrator saw Django on `127.0.0.1:8000` and `next-server` on `:3000` while writing this — **STOP and report**, naming the PIDs. Kill nothing, ever, and never `pkill` under any pattern: those patterns match his own processes and a previous session survived doing it only by luck.

## 3. Mandatory reading

- `AGENTS.md`; `.ap/AP.md`; `.ap/AP_WORKER.md`; `.ap/PROMPT_CONTRACTS.md`; `.ap/INFOSEC.md` sections 3, 5, 16
- `backend/game/models.py`, `backend/game/services.py`, and `backend/game/admin.py` in full
- `backend/gamecore/board.py`, `backend/gamecore/variant_store.py`, `backend/gamecore/state.py` — slice F1 already put the token primitives there; **use them, do not reinvent them**
- `backend/game/management/commands/purge_legacy_game_state.py` — read it so you understand the guard you are about to mirror
- `backend/tests/test_api.py`, `test_slovak_engine.py`, `test_slovak_full_game.py` — the three suites that set the old field shapes directly

## 4. What slice F1 already gives you

Do not duplicate any of this.

```text
backend/gamecore/board.py       Cell.token, Cell.blank_as, Cell.realized_token — read-only derived
                                properties over the existing letter / is_blank storage fields
backend/gamecore/types.py       TileToken; WordFound.tokens
backend/gamecore/variant_store.py
                                VariantDefinition.alphabet_order, .playable_letters ordered by it,
                                .starting_draw_order_key(token), .slot0_wins_starting_draw(a, b)
backend/gamecore/word_authority.py   exists and is tested, but is NOT wired in this slice
```

⚠️ **`Cell`'s storage fields stay `letter` and `is_blank` in this slice.** Read tokens through the derived properties and write through `letter` / `is_blank` exactly as the engine already does. Inverting that storage is cosmetic, is deferred, and may be dropped entirely later with a recorded decision — say so in your report rather than doing it here.

## 5. The four changes

### 5a. Migration `backend/game/migrations/0008_atomic_token_state_schema.py`

⚠️ The accepted plan called this migration `0009`. It is **`0008`** because the purge became a management command and never took that number. There is no gap.

```text
dependencies   game.0007_consumedwsticket
operation 1    THE REFUSAL GUARD, and it runs FIRST, before any schema operation.
               A RunPython that counts the five game-state tables through apps.get_model historical
               models. If ANY is non-empty it raises with a message naming
               `manage.py purge_legacy_game_state`.
               It is a REFUSAL, never a deletion. This migration must not delete one row, ever.
               Its reverse applies the SAME refusal, so reversing after games exist is blocked
               rather than silently corrupting new-shape data.
operation 2    RemoveField GameSession.blanks — blank identity now lives inside each board cell
operation 3    RemoveField GameSession.bag_tiles, then AddField bag_tiles as
               JSONField(default=list). Two operations, not an AlterField: this avoids a
               database-specific text-to-JSON cast.
operation 4    AlterField GameSession.board_state — same JSONField, new default and help text
               describing a 15x15 structured cell grid
reversible     yes, while the five tables stay empty
forbidden      no data deletion, no touch of any table outside game_session's own columns,
               no PRAGMA change, no VACUUM
```

That guard is what replaces the ordering the deleted purge migration would have given by graph position. It is **mandatory** and it needs its own two tests.

### 5b. `backend/game/models.py`

Remove `blanks`. Retype `bag_tiles` to `JSONField(default=list)` with help text naming it an ordered token array. Update `board_state`'s help text and default to describe the structured grid. Update `PlayerSlot.rack`'s help text to say **tokens** rather than letters — it is already a JSON list and needs no type change.

Canonical persisted shapes, and no code path may concatenate tokens and later re-split them:

```text
board_state   15 rows x 15 cells.  Cell = null | {"token": "SZ", "blank_as": null}
                                   a blank playing CS = {"token": "?", "blank_as": "CS"}
bag_tiles     ordered token array, e.g. ["A", "SZ", "?"]
rack          ordered token array (unchanged)
```

### 5c. `backend/game/services.py` — persistence, plus both live defects

```text
_board_from_session   read structured cells into a Board. Set cell.letter to the realized token and
                      cell.is_blank from blank_as. ⛔ No per-code-point indexing of a row string.
_persist_board        write structured cells from a Board, using Cell.token / Cell.blank_as.
                      ⛔ No "".join(row_chars).
_bag_from_session     bag_tiles is already a list; copy it. ⛔ Never list() a string.
_persist_bag          store list(bag.tiles). ⛔ No "".join(bag.tiles).
the blanks store      services.py currently reads or writes session.blanks at seven places
                      (around lines 237, 258, 267, 274, 370, 482, 497). Remove all of them; blank
                      identity is inside the cell. Find them yourself and list them in your report.
```

**`uii-01-F06` — the bag count.** `bag_remaining = len(session.bag_tiles)` at services.py:372 and :558 reports a **string length** as a tile count today. One `SZ` would count as two tiles, `BAG_EMPTY_AND_PLAYER_OUT` reads that count, and the bag could appear to hold 109 tiles for a 100-tile set. Retyping the field to a JSON array makes `len()` correct **by construction** — but you must still prove it with a test that fails before the change.

**`uii-01-F07` — the starting draw, live in production today.** `_perform_starting_draw` at services.py:453-464 decides who opens the board with `slot0_value <= slot1_value` on raw tile strings. `('Á' <= 'Z')` is `False` — code points 193 versus 90 — so all seventeen single-copy Slovak diacritic tiles sort after `Z` and a player drawing `Á` is treated as further from A than one drawing `Z`. In the Slovak alphabet `Á` is second.

Wire F1's pure helper in: `_perform_starting_draw` takes the session's `VariantDefinition` and returns `slot0_first` from `variant.slot0_wins_starting_draw(slot0_tile, slot1_tile)`. Update its caller at services.py:470. Blank stays lowest and equal tokens still resolve to slot 0 — the helper already does both. **This is the correction that closes `uii-01-F07`.**

### 5d. The temporary wire adapter in `_build_state`

`_build_state` at services.py:369-372 currently emits the raw stored values:

```text
"board":         session.board_state        -> 15 joined strings
"blanks":        session.blanks
"bag_remaining": len(session.bag_tiles)
```

The stored shape changes; **the emitted shape must not.** Build both `board` and `blanks` from the structured grid so every existing consumer — REST, the websocket envelope, the frontend, and `test_api.py`'s assertions — sees byte-identical output.

⛔ **The adapter MUST RAISE on a token longer than one code point.** It cannot represent one, and a silent truncation would be exactly the class of corruption this whole era exists to remove. Raise with a message naming the next slice as the removal point. Not reachable today — only English and Slovak variants exist and both are single-code-point — and the raise is what guarantees it can never be reached silently.

Mark the adapter in the source as temporary, with the exact removal condition: it is deleted when the wire format moves to `state_schema_version` 4.

### 5e. `backend/game/admin.py` — required, not optional

`backend/game/admin.py:112` lists `"blanks"` in `GameSession`'s `readonly_fields`. Removing the model field without removing that entry makes Django's admin system check fail, so **`manage.py check` would go red**. Remove exactly that one entry. `backend/tests/test_admin.py` does not reference these fields.

## 6. Positive authority — the exact changed-path allowlist

```text
backend/game/migrations/0008_atomic_token_state_schema.py   NEW FILE
backend/game/models.py
backend/game/services.py
backend/game/admin.py                           <- the single "blanks" entry only
backend/tests/test_atomic_token_persistence.py  NEW FILE
backend/tests/test_api.py
backend/tests/test_slovak_engine.py
backend/tests/test_slovak_full_game.py
```

The last three test files set the **old** field shapes directly — `board_state=["." * 15] * 15`, `bag_tiles=""`, `bag_tiles="ABCDE"` — and must be updated to the new shapes. `test_api.py` has nineteen such references. Update them mechanically and **disclose every changed expected value** per section 8.

Eight paths. A ninth means **stop and report**.

## 7. Negative authority

```text
NO change to word legality. _word_passes_dictionary stays exactly as it is, and
   evaluate_scoring_move keeps being called with is_word rather than authority. That is the NEXT slice.
NO change to backend/game/serializers.py. The one-code-point placement filter stays. It is what stops
   a multi-token placement from arriving before the wire format can carry it, and that ordering is
   deliberate.
NO change to backend/gamecore/. Slice F1 finished it.
NO change to the emitted REST or websocket payload shape. No state_schema_version field yet.
NO change anywhere under frontend/, including the ten untracked images.
NO change to backend/game/consumers.py, views.py, diagnostics.py, or routing.py.
NO change to backend/accounts/, backend/catalog/, backend/billing/, backend/config/.
NO new variant manifest. Czech, Polish and Hungarian are blocked on Cooperator-supplied dictionaries.
   Multi-token coverage in this slice is SYNTHETIC test fixtures only.
NO deletion of any database row, by any route. No purge command invocation. No flush.
NO makemigrations — hand-write the migration. NO migrate of any app other than game to 0008.
NO write to backend/.env, and no read of it.
NO staging of backend/db.sqlite3 or any *.sqlite3 file.
NO killing, restarting, or signalling any process. No pkill, ever.
NO dependency, lockfile, runtime, or toolchain change. NO documentation change.
NO network except the authorized git ls-remote and one git push.
```

Four standing Cooperator locks, none of which this slice touches: the nine AI providers are frozen; MOVE CORE hash `c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60` and version `pfr-s2-core-1` are pinned; `DEFAULT_MAX_ELAPSED_MS = 2000` and `DEFAULT_RANKED_MAX_ELAPSED_MS = 750` are fixed; exactly six `completion_source` values.

⛔ **The formed-word invariant is untouched by this slice and must stay untouched.** A move is illegal only when a **complete** formed word has physical length two and is outside the variant two-tile lexicon — never because a longer word *contains* a two-letter string. `OSAMENIU` is legal despite containing `AM`. If any line you write implies `"am" not in word`, you have failed.

## 8. Required new regression tests

In `backend/tests/test_atomic_token_persistence.py`. Every one needs a **pre-fix / post-fix** entry with the exact pre-fix failure output.

```text
P1  migration guard refuses: with one GameSession row present, applying 0008 raises and names
    `manage.py purge_legacy_game_state`. Nothing is deleted — assert the row still exists.
P2  migration guard passes cleanly on empty tables, and 0008 reverses cleanly while empty.
    Use the house harness: TransactionTestCase, MigrationExecutor or call_command, and
    restore_apps_to_leaf("game") in a finally. backend/tests/_migration_restore.py is the helper.
P3  a full round trip through the database preserving a multi-code-point token: place a synthetic
    two-code-point tile, persist, reload, and assert it is ONE cell and ONE bag entry. No S+Z split
    anywhere. Use a synthetic variant; do not add a manifest.
P4  a blank realized as a multi-code-point token round-trips as {"token": "?", "blank_as": "CS"},
    keeps its physical blank identity, and still scores zero.
P5  uii-01-F06: bag_remaining counts TILES, not code points. With a bag holding one two-code-point
    token plus one single token, bag_remaining is 2. Must fail before the change.
P6  uii-01-F07: in Slovak, a player drawing `Á` beats a player drawing `Z` in the starting draw.
    Must fail before the change. Also assert blank-lowest, English ordering unchanged, and that two
    equal tokens give slot 0 the tie.
P7  the adapter is lossless for English and Slovak: build a session with a realistic board including
    a blank, and assert the emitted `board` is 15 strings of 15 characters and `blanks` is the exact
    coordinate list the old shape produced.
P8  the adapter RAISES on a multi-code-point token rather than truncating.
P9  the rack survives as an ordered token array including a duplicate and a blank.
```

## 9. Validation — the eight standing gates

Baseline at `3fd1a81`, Orchestrator-measured. Match or exceed every one:

```text
mypy               Success: no issues found in 82 source files
ruff               All checks passed!
manage.py check    System check identified no issues (0 silenced).   <- 5e is why this can go red
pytest             361 passed, 4 skipped in 196.18s
npm run typecheck  exit 0
npx vitest run     342 passed | 3 skipped   (26 files passed | 1 skipped)
npm run lint       exit 0
npm run build      exit 0
```

Execution route — mandatory bounded deviation under RF-16:

```text
Declared route that could not be used:  poetry run <tool>, as documented in AGENTS.md "Code quality"
Exact alternate path, from backend/:    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python …
Rationale:  the Cursor AppImage environment intercepts python* through inherited APPIMAGE / ARGV0 /
            APPDIR / PYTHONHOME
Evidence class: reproduced-dynamic, established repeatedly in this project
Bounded authority: this task only; never a second standing canonical route
Stopping condition: if .venv/bin/python is absent or the deviation fails, STOP. Do not use ambient
            python, python3, or poetry run, and do not repair the environment.
```

Four traps that have each cost a real session here:

1. `backend/pyproject.toml` sets `addopts = "-q"`. A second `-q` **silently suppresses the pytest summary line.** Run plain `-m pytest` and quote the summary verbatim.
2. Running mypy on a **narrowed** path set once hid 62 real errors behind a reported 12 for six consecutive sessions. Use the full documented scope.
3. `npm run build` and `npm run dev` share `frontend/.next`. Run `ss -tlnp | grep :3000` first; **if a listener exists, stop and report — do not build and do not kill it.** Never `pkill -f next-server`; that pattern matches the Cooperator's own server.
4. `npm run build` can report success while type errors exist because `tsconfig.json` sets `incremental: true`. State **"the build passed"** and **"the code type-checks"** as two separate claims.

The frontend gates must run even though you change no frontend file: they prove you changed none, and an unchanged vitest count of 342 is that proof.

### Disclose every changed expected value

You are updating three existing suites. For **every** expected value you change, report the pre value, the post value, the causal reason, and whether it is a **shape** update (expected, the field type changed) or a **behaviour** change (a finding that needs explaining). ⛔ Never edit an expected value without that disclosure — silently updating one is how a real regression gets buried, and this project has a recorded history of exactly that.

If any existing test fails for a reason you cannot classify, **stop and report** rather than adjusting it.

## 10. Git authority and sequence

```text
Authorized: git status, diff, log, show, rev-parse, ls-remote, add <explicit paths>, commit,
            one git push origin main
Forbidden:  git add -A, git add ., force push, amend, rebase, reset, revert, clean, stash, branch,
            tag, checkout of another ref, any remote or config modification
```

1. after the gates are green, apply the migration to the development database:
   `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py migrate game 0008`
   Capture `showmigrations game` before and after, and confirm `django_migrations` moves 63 → 64 with exactly one new row. The five tables must still be empty and every protected table unchanged — report the 24-table map before and after.
2. re-run `manage.py check` and the full `pytest` after the live migration;
3. stage by **explicit path only**; every path must appear in section 6;
4. re-check porcelain and confirm the ten flag images are still untracked and unstaged; confirm no `*.sqlite3` is staged;
5. review the complete staged diff;
6. commit: `feat(game): store atomic tokens and fix the bag count and starting draw`;
7. pre-push gate: `git ls-remote origin refs/heads/main` **must still equal** `3fd1a81d79b95a1244db9aa9d4b84ba75a59d6f0`. If it advanced, **stop, push nothing, report**;
8. one non-force `git push origin main`;
9. public readback: `ls-remote` compared with `git rev-parse HEAD`, both quoted.

## 11. Stopping conditions

Stop, preserve state, and report: any repository or database gate fails; a protected table's count changes during the branch-NON-EMPTY purge; the fresh checkpoint cannot be proven usable; either of the Cooperator's servers still holds the database or port 3000; porcelain shows anything beyond the ten flag images; the work needs a ninth path; a lock would be touched; an existing test fails for a reason you cannot classify; `manage.py check` goes red and 5e does not explain it; port 3000 has a listener at build time; the pre-push gate does not match; the `.venv` route is unavailable; you find a pre-existing defect outside the allowlist — **record it, do not fix it**. If the same failing gate survives one correction attempt with an unchanged hypothesis and candidate, report `PARTIAL` or `BLOCKED` with exactly `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`.

## 12. Report contract

Begin **exactly** `### Report for ORCHESTRATOR_CHAT`. Echo the coordinates once: logical whole `multilingual-tile-token-foundation`, Worker session `05`, Worker exchange `01`.

Then: status; `Phase-qualified result`; start and end commit; the section 2 gate evidence quoted, including which branch you took, the five counts before and after, and — if branch NON-EMPTY — the fresh checkpoint path, size, SHA-256 and `integrity_check`, plus the `--dry-run` output verbatim; every changed path with its purpose, and the exact `session.blanks` sites you removed with line numbers; the 24-table before/after map around the live migration, with `django_migrations` 63 → 64 and the new row named; the eight gates before and after the live migration, pytest and vitest summaries verbatim, the two build claims separate; the pre-fix / post-fix table for P1 through P9; **every changed expected value in the three existing suites, classified shape versus behaviour**; explicit confirmation that `_word_passes_dictionary`, `serializers.py`, `gamecore/`, the emitted wire shape, and the frontend are all unchanged; the adapter's exact source location and its removal condition; a statement that the `Cell` storage inversion is deferred and may be dropped; deviations, risks and missing evidence honestly; `Resolved Execution Issues / Near-Misses`; `Pre-Existing Failure Classification`; commit and push with the public readback; one smallest next step; `Report justification: new-mutation`; `Logical-whole closure: not-closed`; an explicit authority-expiry statement.

Hand these forward:

```text
- F2c: emit state_schema_version 4 with BoardCell[][], DELETE the temporary adapter, and update the
  frontend in the same slice — types, store persist v4, board / tile / blank picker / draw rendering
- F2c or later: re-point evaluate_scoring_move at WordAuthority and DELETE _word_passes_dictionary.
  Two authority paths must not become permanent.
- F2c: relax the serializers.py one-code-point placement filter, together with the wire format
- F3: build_ai_state_dict is still lossy for multi-code-point cells; the AI boundary is F3's
- optional, may be dropped with a recorded decision: invert Cell storage onto token / blank_as and
  remove the F1 derived properties
```

⛔ Do not emit any logical-whole closure signal. Your evidence is **non-independent** — say so.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 05_implementation_00.md
Destination path: /home/agile/meta/projects/libretiles/11/01-multilingual-tile-token-foundation/
Archival: wait-for-report
```

You do not archive this pair. The Cooperator does, after your report exists.

Your authority expires at your terminal report.
