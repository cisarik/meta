You are a WORKER instance assigned to the persistent AP WORKER role. Execute exactly this bounded task and stop.

```text
Logical whole identity: multilingual-tile-token-foundation
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: MTT-F2a — the irreversible development game-state purge, alone
Phase: Implementation
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Exact baseline: 9f0c5b8141b94785f26f84fd0104131f063c3ed6
Logical-whole closure: not-closed
```

Reasoning recommendation: **High.** Named risk: this slice performs an **irreversible deletion of database rows**. The governing risk in the accepted plan's register is "destructive migration targets the wrong database or the wrong tables — irrecoverable unrelated data loss". Medium is not sufficient for an E4 operation with a manual recovery path.

```text
Evidence tier: E4
Evidence tier basis: irreversible destruction of durable development data. Recovery is a file-level
  checkpoint, not a transaction rollback.
Combined implementation envelope: PROHIBITED. The stages in section 6 are separated and each has a
  hard gate. A failed gate stops the sequence; you do not continue to the next stage.
Activated stricter profile: INFOSEC.md at R1 + R2, inline and non-independent. The whole receives one
  fresh independent R4 application audit after slice F3; this slice is not it.
Independent acceptance: not-required for this slice, required for the whole after F3
```

## 1. What this slice is, and what it is deliberately NOT

**Is:** one fail-closed setting, one irreversible migration `0008` that empties five named development tables, its documentation in `backend/.env.example`, its tests, and the one-time application of that migration to the Cooperator's development database under a verified checkpoint.

**Is NOT:** any schema change. `GameSession.blanks` stays. `bag_tiles` stays a `TextField`. `board_state` keeps its current shape. No REST change, no websocket change, no frontend change, no `models.py` change, no `services.py` change, no `serializers.py` change. Those are slices F2b and F2c.

The Orchestrator split the accepted plan's single F2 into F2a / F2b / F2c because one allowlist covering a migration, a persistence rewrite, a wire-format change and a frontend rewrite produces a diff nobody can review honestly. You hold **F2a only**.

## 2. Repository, topology, and gate

```text
Repository checkout topology: standalone checkout
Working directory: /home/agile/Projects/libretiles
Repository identity: https://github.com/cisarik/libretiles
Expected branch: main
Expected HEAD: 9f0c5b8141b94785f26f84fd0104131f063c3ed6
Expected .ap gitlink and submodule HEAD: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Working-copy topology: canonical-checkout
Topology rationale: the operation must act on the Cooperator's own development database, which lives
  at backend/db.sqlite3 in this checkout. An isolated worktree would target the wrong file.
```

Verify and quote before anything else:

```text
git rev-parse HEAD                      == 9f0c5b8141b94785f26f84fd0104131f063c3ed6
git rev-parse HEAD:.ap                  == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD               == the same
git status -sb                          == ## main...origin/main
git ls-remote origin refs/heads/main    == 9f0c5b8141b94785f26f84fd0104131f063c3ed6
git status --porcelain=v1
```

Porcelain must report **exactly** these ten untracked files and nothing else:

```text
?? frontend/public/cs.png     ?? frontend/public/cz.jpeg    ?? frontend/public/en.jpeg
?? frontend/public/en.png     ?? frontend/public/hu.jpeg    ?? frontend/public/hu.png
?? frontend/public/pl.jpeg    ?? frontend/public/pl.png     ?? frontend/public/sk.jpeg
?? frontend/public/sk.png
```

Cooperator-supplied flag assets, another logical whole, deliberately uncommitted. Do not touch them. Anything else in porcelain: classify with all five AP recovery classes and stop if the primary class is `unexplained-divergence`.

## 3. Mandatory reading

- `AGENTS.md`; `.ap/AP.md`; `.ap/AP_WORKER.md`; `.ap/PROMPT_CONTRACTS.md`
- `.ap/INFOSEC.md` sections 3, 5, 9, 10, 11, 14, 16
- `backend/game/models.py` in full, and `backend/game/migrations/0007_consumedwsticket.py`
- `backend/game/migrations/0005_remove_money_state.py` — the project's existing irreversible migration; **this is your reference implementation**
- `backend/tests/test_creditless_migration.py` in full, and `backend/tests/_migration_restore.py` — the house harness you must reuse
- `backend/config/settings.py`, in particular `_env_flag` at line 53 and `DYNAMIC_FREE_MODEL_CATALOG_ENABLED` at line 362
- `backend/.env.example` — a committed template, safe to read. ⛔ **Never read `backend/.env`.**

## 4. Cooperator authorization, and its exact limits

Cooperator decision, 2026-09-01, in his own words: `obetovatelne - vsetky rozohrate vymazat predsa, su to len testovacie hry`.

```text
AUTHORIZED      deleting development game state through these five tables, in this order:
                game_chat_message, game_move, game_player_slot, game_session, game_consumed_ws_ticket
NOT AUTHORIZED  accounts_user rows, credentials, password_changed_at, the JWT blacklist tables,
                catalog_ai_model, catalog_ai_prompt, axes tables, sessions, admin log, content types,
                migration records, or ANY other table
NOT AUTHORIZED  manage.py flush; a raw DELETE that does not go through a named historical model;
                any database other than the development SQLite file named in section 5
```

⛔ **Never ask the Cooperator to perform a destructive action.** He authorized the migration's behaviour; you execute it under the explicit flag. Do not ask him to run a `DELETE`, drop a database, or reset anything by hand. Asking him to stop a dev server is fine and has already been done — see the stage 0 gate.

## 5. Measured facts from the F2a preflight — verify, do not trust

Worker session 03 established these at `9f0c5b8`, and the Orchestrator independently re-measured all eighteen row counts, the FK topology, and the PRAGMA values. **Re-verify every one before you mutate anything**; if any differs, that is a finding and you stop.

```text
database        ENGINE django.db.backends.sqlite3
                NAME   /home/agile/Projects/libretiles/backend/db.sqlite3
                size 389120 B, journal_mode delete, no -wal / -shm sidecars, integrity_check ok
tables          24 total
five targets    game_chat_message 2   game_move 42   game_player_slot 58
                game_session 29       game_consumed_ws_ticket 1        total 132  (NOT empty)
protected       accounts_user 4   catalog_ai_model 12   catalog_ai_prompt 4
                token_blacklist_outstandingtoken 23   token_blacklist_blacklistedtoken 5
                axes_accessattempt 0   axes_accesslog 0   axes_accessfailurelog 0
                axes_accessattemptexpiration 0
                django_migrations 63   django_content_type 19   auth_permission 76
                sqlite_sequence 17     django_session 0   django_admin_log 0
                accounts_user_groups 0   accounts_user_user_permissions 0
                auth_group 0   auth_group_permissions 0
billing_%       ABSENT. The app is not in INSTALLED_APPS; its disk migrations were never applied.
inbound FKs     exactly 4 edges into the five, ALL from inside the five. From outside: ZERO.
outbound FKs    game_session.ai_model_id -> catalog_ai_model,  .ai_prompt_id -> catalog_ai_prompt,
                game_player_slot.user_id -> accounts_user,  game_chat_message.user_id -> accounts_user
                Django on_delete is SET_NULL on all four. Deleting a GAME row never touches the
                protected row; SET_NULL only fires in the other direction.
game leaf       0007_consumedwsticket.  0008 and 0009 do not exist.
setting         ALLOW_DESTRUCTIVE_GAME_STATE_RESET appears NOWHERE in the repository yet.
```

### Six preflight findings that constrain your implementation

```text
1  SQLite stores every one of these FKs as ON DELETE NO ACTION while the Django models declare
   CASCADE / SET_NULL. A raw parent DELETE therefore FAILS while children exist.
   CONSEQUENCE, mandatory: delete through named historical models with ORM querysets. No raw SQL
   DELETE. ⛔ Never touch `PRAGMA foreign_keys`, in either direction.
2  game_consumed_ws_ticket has no FK in either direction. A collector delete of GameSession will NOT
   remove tickets. Step 5 is independent and mandatory, not redundant.
3  A process may hold db.sqlite3 open. See the stage 0 gate. Never assume a PID; re-check.
4  journal_mode is `delete`, not WAL, so no sidecar copy is needed today — but the checkpoint must use
   the SQLite `.backup` API rather than a plain file copy, because the mode can change and a process
   may hold the file.
5  sqlite_sequence AUTOINCREMENT counters survive DELETE and its own row count stays 17. Do NOT
   DELETE FROM sqlite_sequence, and no test may expect primary keys to restart at 1.
6  If any billing_% table exists, REFUSE and stop: historical billing_transaction declared SET_NULL
   to game_session, which would mean a session delete updating unauthorized rows.
```

## 6. The five separated stages, each with a hard gate

E4 prohibits a combined envelope. Execute these in order. **A failed gate stops the sequence — you do not proceed, you do not improvise, you report.**

### Stage 0 — gates, before any mutation whatsoever

```text
G0.1  the repository gate of section 2, quoted
G0.2  settings.DATABASES["default"]["ENGINE"] == "django.db.backends.sqlite3"
      and ["NAME"] == "/home/agile/Projects/libretiles/backend/db.sqlite3"
      Print ONLY those two values from that dict. Nothing else.
G0.3  no billing_% table exists in that database
G0.4  a fresh whole-database sweep of PRAGMA foreign_key_list over every table finds ZERO inbound
      foreign keys into the five target tables from any table outside the five
G0.5  PRAGMA integrity_check == ok
G0.6  NO process holds the database open. Run `ss -tlnp | grep -E ':(3000|8000)'` and
      `fuser backend/db.sqlite3` (or `lsof` if fuser is unavailable). Both must show nothing
      holding the file.
      ⛔ If something does hold it, STOP and report. Do NOT kill it. Never use pkill or any broad
      pattern kill — the Cooperator's own servers run on those ports.
G0.7  the eighteen row counts of section 5 still match
```

Any G0 failure: stop, report `BLOCKED`, mutate nothing.

### Stage 1 — write code and tests, apply NOTHING

Create, in this stage only:

**1a. The setting.** In `backend/config/settings.py`, add `ALLOW_DESTRUCTIVE_GAME_STATE_RESET` using the existing `_env_flag` helper at line 53, `default=False`. Follow the house style of `DYNAMIC_FREE_MODEL_CATALOG_ENABLED`. Write a comment that records: what `false` means, what `true` means, that it exists for a one-time development purge, that it is fail-closed, and that a pre-existing `.env` overrides code defaults and is read once at process start.

**1b. `backend/.env.example`.** Document the variable with the same exact spelling and a default of `'false'`, in the style of the surrounding entries. This is a committed template; it is safe to edit.

**1c. `backend/game/migrations/0008_purge_legacy_game_state.py`.**

```text
dependencies      game.0007_consumedwsticket
operation         migrations.RunPython(forward, reverse)
reverse           MUST raise django.db.migrations.exceptions.IrreversibleError
flag read         INSIDE the forward callable via django.conf.settings, NEVER at module import time,
                  so override_settings works in tests
no-op path        count all five tables FIRST. If all five are already empty, return without
                  requiring the flag, and log that it was a no-op.
fail-closed path  if ANY row exists and the flag is false, raise before deleting anything. The
                  message names the flag and the five tables. No partial deletion is possible.
delete path       with the flag true, delete through apps.get_model historical models, using ORM
                  querysets, in exactly this order:
                    1 game.ChatMessage        (game_chat_message)
                    2 game.Move               (game_move)
                    3 game.PlayerSlot         (game_player_slot)
                    4 game.GameSession        (game_session)
                    5 game.ConsumedWsTicket   (game_consumed_ws_ticket)
                  Resolve the exact historical model names from backend/game/models.py yourself.
assertions        record pre and post counts for all five; assert all five are 0 afterwards; raise if
                  not. Emit the counts through the migration's stdout or a logger so the apply-time
                  output is evidence.
forbidden inside  no flush, no raw SQL DELETE, no PRAGMA change, no VACUUM, no touch of any table
                  outside the five, no schema change, no field alteration
```

⚠️ **Orchestrator decision you must follow and not "improve":** the migration asserts only that the **five** are empty. It does **not** assert protected-table counts, because reaching `token_blacklist` and `axes` historical models would add third-party migration-state dependencies to a `game` migration for no safety gain. Protection is proven twice elsewhere instead: in your tests, and in the stage 3 live before/after evidence. Record this in your report.

**1d. `backend/tests/test_atomic_token_purge_migration.py`.** Reuse the house harness — `TransactionTestCase`, `importlib.import_module("game.migrations.0008_purge_legacy_game_state")`, direct invocation of the `RunPython` callables with `apps` and `schema_editor`, `call_command("migrate", ...)` for graph moves, and `restore_apps_to_leaf("game")` in a `finally`. `backend/tests/test_creditless_migration.py` lines 104-234 is the pattern; follow it rather than inventing a harness.

Required cases, each with a **pre-fix / post-fix** note:

```text
T1  flag false + non-empty tables  -> raises before deletion; all five counts UNCHANGED
T2  flag true + non-empty tables   -> all five become 0
T3  all five already empty + flag false -> no-op, no exception, nothing raised
T4  reverse raises IrreversibleError (assertRaises((CommandError, IrreversibleError)), matching the
    existing test_cleanup_migrations_are_irreversible shape)
T5  protected rows survive a flag-true purge: create a User, an AIModel, an AIPrompt, an
    OutstandingToken (or the closest available blacklist row), and an axes AccessAttempt if
    constructible; run the purge; assert every one still exists with an unchanged count
T6  deletion order safety: with FK enforcement in whatever state the Django connection uses, a
    populated session with chat, moves and slots purges without an integrity error
T7  a ConsumedWsTicket unrelated to any session is still deleted — this is preflight finding 2 and
    proves step 5 is not redundant
T8  sqlite_sequence: after the purge, assert primary keys do NOT restart at 1 for a newly created
    GameSession. This locks preflight finding 5 so a future reader does not "fix" it.
```

Then run the **eight standing gates**. Baseline at `9f0c5b8`, Orchestrator-measured — match or exceed:

```text
mypy               Success: no issues found in 81 source files
ruff               All checks passed!
manage.py check    System check identified no issues (0 silenced).
pytest             352 passed, 4 skipped in 195.32s
npm run typecheck  exit 0
npx vitest run     342 passed | 3 skipped   (26 files passed | 1 skipped)
npm run lint       exit 0
npm run build      exit 0
```

Traps: `backend/pyproject.toml` sets `addopts = "-q"` — a second `-q` **silently suppresses the pytest summary line**, so run plain `-m pytest` and quote the summary verbatim. Run mypy on the full documented scope, never narrowed. Before `npm run build`, run `ss -tlnp | grep :3000`; if a listener exists, **stop and report — do not build and do not kill it.** `npm run build` can pass while type errors exist because `incremental: true`, so state "the build passed" and "the code type-checks" as two separate claims.

**Gate G1: every one of the eight is green and every T-case passes. Nothing has been applied to the live database yet.** If G1 fails, stop and report — do not proceed to stage 2.

### Stage 2 — the checkpoint

```bash
mkdir -p /tmp/opencode/mtt-f2a-checkpoint
sqlite3 /home/agile/Projects/libretiles/backend/db.sqlite3 \
  ".backup '/tmp/opencode/mtt-f2a-checkpoint/db.sqlite3.f2a-checkpoint'"
```

If `sqlite3` is unavailable on PATH, use the authorized Python equivalent through the `.venv` deviation and the SQLite `backup` API. **Do not use a plain `cp` of the live file as the checkpoint** — preflight finding 4.

Then prove the checkpoint is usable, not merely present:

```text
G2.1  the checkpoint file exists and its byte size is reported
G2.2  PRAGMA integrity_check on the CHECKPOINT == ok
G2.3  the five target counts read FROM THE CHECKPOINT equal the live counts (2, 42, 58, 29, 1)
G2.4  the full 24-table count map read from the checkpoint is captured and reported
G2.5  the SHA-256 of the checkpoint file is reported
```

**Gate G2: all five hold.** If any fails, stop and report — the live database has still not been modified.

⛔ Do not `VACUUM`. Do not restore anything in this slice. Do not delete the checkpoint — see the containment ledger in section 9.

### Stage 3 — apply the purge to the development database

Capture the complete 24-table count map **immediately before**:

```bash
ALLOW_DESTRUCTIVE_GAME_STATE_RESET=true \
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py migrate game 0008
```

The flag is a **one-shot environment variable on this one command**. ⛔ Do **not** write it into `backend/.env`; do not read that file at all. Migrate **only** the `game` app to **only** target `0008`.

Capture the complete 24-table count map immediately after.

```text
G3.1  the five target tables are all 0
G3.2  EVERY other table's row count is byte-identical to the before map — accounts_user 4,
      catalog_ai_model 12, catalog_ai_prompt 4, token_blacklist_outstandingtoken 23,
      ...blacklistedtoken 5, all four axes_* 0, django_content_type 19, auth_permission 76,
      sqlite_sequence 17, django_session 0, django_admin_log 0, and the rest
G3.3  django_migrations has exactly one new row, for game.0008_purge_legacy_game_state
      (63 -> 64)
G3.4  PRAGMA integrity_check on the live database == ok
G3.5  showmigrations game reports 0008 applied and it is the leaf
G3.6  billing_% is still absent
```

**Gate G3: all six hold.** If any fails, stop immediately and report with the exact divergence and the checkpoint path — do not attempt a restore, do not commit, do not push. A restore is a Cooperator-visible decision and the Orchestrator will route it.

### Stage 4 — re-validate after the live mutation

Re-run from `backend/`: `manage.py check` and the full `pytest`. Tests use their own test database, so they must still report `352 passed, 4 skipped` plus your new T-cases. Also confirm the application still boots by running `manage.py check` — do **not** start a server.

**Gate G4: `manage.py check` clean and pytest at or above baseline plus the new cases.**

### Stage 5 — commit and push

```text
stage by EXPLICIT PATH only; every path must appear in section 7
then re-run git status --porcelain=v1 and confirm the ten flag images are still untracked and unstaged
review the complete staged diff before committing
commit subject: feat(game): purge legacy development game state behind a fail-closed flag
pre-push gate: git ls-remote origin refs/heads/main MUST still equal
               9f0c5b8141b94785f26f84fd0104131f063c3ed6
               If it has advanced, another actor is active — STOP, push nothing, report.
one non-force git push origin main
public readback: git ls-remote origin refs/heads/main compared with git rev-parse HEAD; quote both
```

⛔ `backend/db.sqlite3` is **not** tracked and must never be staged. Confirm that explicitly.

## 7. Positive authority — the exact changed-path allowlist

```text
backend/config/settings.py                                  the one new flag and its comment
backend/.env.example                                        document the flag
backend/game/migrations/0008_purge_legacy_game_state.py      NEW FILE
backend/tests/test_atomic_token_purge_migration.py           NEW FILE
```

Four paths. Nothing else. If the work appears to require a fifth path, **stop and report** — that is a scope finding, not a judgement call.

## 8. Negative authority — prohibited without exception

```text
NO change to backend/game/models.py. GameSession.blanks stays; bag_tiles stays TextField;
   board_state keeps its shape. That is migration 0009 in slice F2b.
NO migration 0009. NO makemigrations, ever. You hand-write 0008 only.
NO change to backend/game/services.py, serializers.py, views.py, consumers.py, diagnostics.py.
NO change anywhere under frontend/. Not one file, including the ten untracked images.
NO change to backend/gamecore/. Slice F1 finished it.
NO change to backend/accounts/, backend/catalog/, backend/billing/.
NO migrate of any app other than game, and no target other than 0008.
NO manage.py flush, no raw SQL DELETE, no PRAGMA change, no VACUUM, no schema change.
NO write to backend/.env, and no read of it either. .env.example only.
NO staging of backend/db.sqlite3 or any *.sqlite3 file.
NO killing, restarting, or signalling any process. No pkill, ever, under any pattern.
NO dependency, lockfile, runtime, or toolchain change. No pip, poetry add, or npm install.
NO documentation change: not README.md, not AGENTS.md.
NO network except the authorized git ls-remote and one git push.
NO writes outside the repository allowlist except /tmp/opencode/mtt-f2a-checkpoint/.
```

Four standing Cooperator locks, none of which this slice touches — keep it that way: the nine AI providers are frozen; the MOVE CORE hash `c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60` and version `pfr-s2-core-1` are pinned; `DEFAULT_MAX_ELAPSED_MS = 2000` and `DEFAULT_RANKED_MAX_ELAPSED_MS = 750` are fixed; there are exactly six `completion_source` values.

## 9. Execution route, and the containment ledger

```text
Declared route that could not be used:  poetry run <tool>, as documented in AGENTS.md "Code quality"
Exact alternate path, from backend/:    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python …
Rationale:                              the Cursor AppImage environment intercepts python* through
                                        inherited APPIMAGE / ARGV0 / APPDIR / PYTHONHOME
Evidence class:                         reproduced-dynamic, established repeatedly in this project
Bounded authority:                      this task only; never a second standing canonical route
Stopping condition:                     if .venv/bin/python is absent or the deviation fails, STOP.
                                        Do not use ambient python, python3, or poetry run, and do not
                                        repair the environment.
```

Never present ambient `python`, `python3`, or `poetry run` as an equivalent alternative.

Containment ledger, required in the report per INFOSEC 10:

```text
temporary root    /tmp/opencode/mtt-f2a-checkpoint/
owner             you
mode              report the observed mode
contents class    one SQLite checkpoint of the development database. It contains development game
                  state and account rows. It is NOT public-safe: do not print its contents, do not
                  copy it anywhere else, do not attach it to the report.
cleanup owner     the COOPERATOR, after the Orchestrator accepts this slice
cleanup outcome   retain-with-reason: it is the only recovery path for an irreversible operation.
                  ⛔ Do NOT delete it yourself.
```

Report the checkpoint's absolute path, byte size, and SHA-256 — those are metadata, not contents.

## 10. Stopping conditions

Stop, preserve state, mutate nothing further, and report:

- any G0 through G4 gate fails;
- porcelain shows anything beyond the ten flag images;
- the database `ENGINE` is not SQLite or `NAME` is not the exact path in section 5;
- any `billing_%` table exists;
- a foreign key into the five exists from outside the five;
- any protected table's count changes;
- the checkpoint cannot be proven usable;
- the work would require a fifth path, a schema change, or `makemigrations`;
- a process holds the database open at stage 0;
- port 3000 has a listener at build time;
- the pre-push `ls-remote` gate does not equal the baseline;
- the `.venv` route is unavailable;
- you find a pre-existing defect outside the allowlist — **record it, do not fix it**;
- the same failing gate survives one correction attempt with an unchanged hypothesis and candidate; then report `PARTIAL` or `BLOCKED` with exactly `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`.

## 11. Report contract

Begin **exactly**:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once, unchanged: logical whole `multilingual-tile-token-foundation`, Worker session `04`, Worker exchange `01`.

Then:

1. status `PASS` / `PARTIAL` / `BLOCKED`;
2. `Phase-qualified result: implementation-PASS` or `not-applicable`;
3. start and end commit;
4. the stage 0 gate evidence, all seven items, quoted;
5. every changed path with its purpose;
6. **the complete 24-table before and after count map, side by side**, with a column marking each row as target-emptied or protected-unchanged. This is the central evidence of the slice.
7. `django_migrations` 63 → 64 and the new row's identity;
8. the eight gate results, with the pytest and vitest summary lines quoted verbatim, and "the build passed" stated separately from "the code type-checks" — for stage 1 **and** the stage 4 re-run;
9. the pre-fix / post-fix table for T1 through T8;
10. the checkpoint: absolute path, byte size, SHA-256, `integrity_check`, and the five counts read from it;
11. the containment ledger of section 9, with `retain-with-reason`;
12. confirmation that `backend/db.sqlite3` was never staged and that no `.env` file was read or written;
13. the F2b and F2c obligations you are handing forward, unchanged from the F1 report: delete `_word_passes_dictionary` and re-point `evaluate_scoring_move` at `WordAuthority`; invert the `Cell` storage and remove the F1 derived properties; wire `slot0_wins_starting_draw` into `_perform_starting_draw`; correct `uii-01-F06`; migration `0009`; then REST/websocket v4 and the frontend in F2c;
14. deviations, risks, and missing evidence, honestly, including anything you could not verify;
15. `Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>`;
16. `Pre-Existing Failure Classification: none | <the complete contract record>`;
17. commit and push result with the public readback;
18. one smallest next step;
19. `Report justification: new-mutation`;
20. `Logical-whole closure: not-closed`;
21. an explicit authority-expiry statement.

⛔ Do **not** emit any logical-whole closure signal. Your evidence is **non-independent** — say so.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 04_implementation_00.md
Destination path: /home/agile/meta/projects/libretiles/11/01-multilingual-tile-token-foundation/
Archival: wait-for-report
```

You do not archive this pair. The Cooperator does, after your report exists.

Your authority expires at your terminal report.
