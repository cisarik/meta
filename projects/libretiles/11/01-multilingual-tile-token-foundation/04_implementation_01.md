You are the SAME WORKER instance that returned the `PARTIAL` / `NEEDS_ORCHESTRATOR_DECISION` report for MTT-F2a. Your prior authority expired at that terminal report. This prompt grants complete new bounded authority.

```text
Logical whole identity: multilingual-tile-token-foundation
Worker session ordinal: 04
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: MTT-F2a-CORR — the purge becomes a management command, not a migration
Phase: Implementation
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Exact baseline: 9f0c5b8141b94785f26f84fd0104131f063c3ed6
Continuity anchor: your terminal PARTIAL report for MTT-F2a, Worker session 04 exchange 01, whose
  uncommitted four-path candidate is still in the working tree
Authority renewal: prior authority expired at that report; this exchange grants a new bounded task
Logical-whole closure: not-closed
```

Reasoning recommendation: **High.** Named risk unchanged: this slice still performs an irreversible deletion of development database rows. The mechanism changes; the consequence does not.

Retained context is convenience, not authority. Re-gate the repository and the database yourself. If anything you retained conflicts with what you now measure, **stop and report** rather than trusting memory.

## 1. Your report was correct, and your recommendation was incomplete

You stopped at exactly the right place. You did not apply, did not checkpoint, did not commit, did not touch a fifth path, and did not make `0008` reversible to force a green gate. The Orchestrator verified all of that independently: `HEAD` is still `9f0c5b8`, `django_migrations` is still 63, the five target tables still hold 132 rows, the live SQLite mtime is unchanged, and no checkpoint directory exists.

Your diagnosis of the G1 failure was also right, and the Orchestrator reproduced it:

```text
tests/test_scoreless_turns_migration.py:14  executor.migrate([("game","0005_remove_money_state")])
  -> IrreversibleError: Legacy game-state purge cannot be reversed.
     raised from game/migrations/0008_purge_legacy_game_state.py:33
```

**But your recommended option A would have failed at the next gate, and the Orchestrator measured that too.** Fake-unapplying `0008` before the backward walk fixes line 14. Line 34 then re-applies `0008` **forward** through `restore_apps_to_leaf("game")` while the row created at line 17 still exists, and your fail-closed guard fires:

```text
PROBE rows before teardown: 1
PROBE teardown re-apply: RAISED RuntimeError: Refusing to purge non-empty game state because
  ALLOW_DESTRUCTIVE_GAME_STATE_RESET is false.
```

That probe was a throwaway test file, run against the test database, and removed immediately; the tree is clean.

So a data-destroying, fail-closed, irreversible migration is hostile to Django's own test harness in **two independent directions** — backward because it is irreversible, and forward because its guard raises on re-apply. That is not a test defect to be patched. It is the mechanism being wrong.

## 2. ORCHESTRATOR DECISION: the purge becomes a management command

This **deviates from accepted planning decision 2 and from section 7 of the `11/01` handout**, both of which named a migration `0008_purge_legacy_game_state`. The deviation is deliberate, is the Orchestrator's to make because it is mechanism rather than product, and is recorded in `DEFECT_LEDGER.md` with the two measured hazards above as its evidence.

What the Cooperator authorized is unchanged: delete the development game state in those five tables, fail-closed, never any other table. Only *how* changes.

```text
BEFORE   migration game.0008 deletes rows during `manage.py migrate`
AFTER    manage.py purge_legacy_game_state deletes rows when an operator runs it,
         and F2b's schema migration REFUSES to run while legacy rows remain
```

Six reasons, in descending weight:

1. **`manage.py migrate` must never be a destructive command.** Under the migration design, a production deployment that happened to carry `ALLOW_DESTRUCTIVE_GAME_STATE_RESET=true` in its environment — a plausible copy-paste — would silently delete every production game during a routine `migrate`. The plan states in terms that production deletion is not authorized and would need separate authority, a verified backup, and a maintenance window. A command makes that accident impossible; a migration invites it.
2. **Onboarding stays intact.** `README.md` documents `manage.py migrate` as the first command a fresh clone runs. `acc-01-D06` was precisely "a fresh clone cannot boot, and the documented onboarding path is broken". A migration that aborts whenever game rows exist re-breaks that path for anyone with data.
3. **Both measured hazards disappear**, rather than being patched. No irreversible node enters the graph, so `test_scoreless_turns_migration.py` needs no change and no fifth allowlist path. No forward guard sits inside a migration, so the teardown re-apply hazard is gone for every current and future test.
4. **A third hazard is made moot.** `test_creditless_migration.py::test_cleanup_migrations_are_irreversible` asserts that migrating `game` back to `0004` raises. With an irreversible `0008` in the graph it would raise at `0008` and never reach `0005`, so the test would keep passing while no longer proving what it was written to prove. The Orchestrator did not measure this, because the chosen mechanism removes the possibility; it is named so the reasoning is legible.
5. **E4 wants stage separation.** Hiding an irreversible deletion inside `migrate` is the opposite of it. An explicit operator-invoked command is the separation.
6. **It is directly testable** with `call_command`, with no migration-graph gymnastics.

Costs, stated plainly rather than minimised: the purge is no longer recorded as a `django_migrations` row, so its evidence lives in the command's logged pre/post counts, your report, and the ledger. And ordering now depends on F2b's guard instead of graph position, which is why that guard is a mandatory F2b obligation below.

## 3. Repository and database gate — re-verify, do not trust retained context

```text
git rev-parse HEAD                      == 9f0c5b8141b94785f26f84fd0104131f063c3ed6
git rev-parse HEAD:.ap                  == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD               == the same
git status -sb                          == ## main...origin/main
git ls-remote origin refs/heads/main    == 9f0c5b8141b94785f26f84fd0104131f063c3ed6
```

`git status --porcelain=v1` must show **exactly** your four candidate paths plus the ten flag images:

```text
 M backend/.env.example
 M backend/config/settings.py
?? backend/game/migrations/0008_purge_legacy_game_state.py
?? backend/tests/test_atomic_token_purge_migration.py
?? frontend/public/{cs,en,hu,pl,sk}.png  and  {cz,en,hu,pl,sk}.jpeg
```

Anything else: classify with all five AP recovery classes and stop if the primary class is `unexplained-divergence`.

Then re-run the **stage 0 gates G0.2 through G0.7 from your previous prompt, unchanged**. The Orchestrator re-measured them minutes ago and they still hold:

```text
ENGINE django.db.backends.sqlite3    NAME /home/agile/Projects/libretiles/backend/db.sqlite3
five targets   chat 2  move 42  slot 58  session 29  ticket 1   = 132, NOT empty
django_migrations 63,  game leaf 0007_consumedwsticket,  no 0008 row
accounts_user 4   catalog_ai_model 12   catalog_ai_prompt 4
billing_%  ABSENT        inbound FKs into the five from outside the five: ZERO
integrity_check ok       journal_mode delete, no -wal / -shm sidecars
```

G0.6 stands unchanged and is a hard gate: `ss -tlnp | grep -E ':(3000|8000)'` and `fuser backend/db.sqlite3` must both show nothing holding the file. ⛔ **Kill nothing. Never `pkill`, under any pattern.**

## 4. What to do, exactly

### 4a. Delete the migration

```text
rm backend/game/migrations/0008_purge_legacy_game_state.py
```

It was never applied — `django_migrations` has no `0008` row and the live leaf is `0007`. Deleting an unapplied, uncommitted, never-pushed migration file is not a history rewrite. Confirm in your report that no `0008` row exists before and after.

**The number `0008` is now free, and F2b's schema migration will take it.** The accepted plan called that migration `0009`; it becomes `0008_atomic_token_state_schema`. Say so in your report so nobody later hunts for a missing `0008`.

### 4b. Keep the setting and the template entry as they are

`backend/config/settings.py` and `backend/.env.example` from your candidate stay. Re-read your own comment and adjust only what is now factually wrong: it must describe a **command** gate rather than a migration gate, and it must still record that `false` is fail-closed, that `true` permits a one-time development purge, and that a pre-existing `.env` overrides code defaults and is read once at process start.

### 4c. Create `backend/game/management/commands/purge_legacy_game_state.py`

```text
gate            settings.ALLOW_DESTRUCTIVE_GAME_STATE_RESET, read at handle() time, never at import
--dry-run       report the pre counts and the intended action, delete NOTHING, exit 0
no-op path      count all five FIRST. If all five are already empty, report the no-op and exit 0
                WITHOUT requiring the flag.
fail-closed     if any row exists and the flag is false, raise CommandError naming the flag and the
                five tables, before deleting anything. No partial deletion is reachable.
delete path     with the flag true, delete via the real models in exactly this order:
                  1 ChatMessage      game_chat_message
                  2 Move             game_move
                  3 PlayerSlot       game_player_slot
                  4 GameSession      game_session
                  5 ConsumedWsTicket game_consumed_ws_ticket
                Use ORM querysets. ⛔ No raw SQL DELETE — SQLite stores these FKs as ON DELETE
                NO ACTION while the models declare CASCADE, so a raw parent delete fails while
                children exist. ⛔ Never touch PRAGMA foreign_keys, in either direction.
transaction     wrap the deletion in transaction.atomic() so a failure mid-sequence rolls back
assertions      print and log pre counts, per-model deleted counts, and post counts. Raise if any of
                the five is non-zero afterwards.
forbidden       no flush, no schema change, no VACUUM, no touch of any table outside the five,
                no DELETE FROM sqlite_sequence
```

Since this is a command rather than a migration you use the **real** models from `game.models`, not `apps.get_model` historical models. That is simpler and correct here.

Note preflight finding 2, which still applies: `ConsumedWsTicket` has no foreign key in either direction, so a cascade from `GameSession` will **not** remove tickets. Step 5 is independent and mandatory.

### 4d. Retarget the tests

Rename `backend/tests/test_atomic_token_purge_migration.py` to `backend/tests/test_purge_legacy_game_state.py` and retarget your eight cases at the command. Most of them survive almost unchanged.

```text
T1  flag false + non-empty  -> CommandError; all five counts UNCHANGED
T2  flag true + non-empty   -> all five become 0
T3  all five already empty + flag false -> no-op, no exception
T4  REPLACES the old irreversibility case: --dry-run with flag TRUE and non-empty tables deletes
    NOTHING and reports the counts. This is the new "you cannot destroy by accident" property.
T5  protected rows survive a flag-true purge: User, AIModel, AIPrompt, an OutstandingToken, and an
    axes AccessAttempt if constructible — counts and primary keys all unchanged
T6  deletion order safety: a populated session with chat, moves and slots purges with no IntegrityError
T7  a ConsumedWsTicket unrelated to any session is still deleted (preflight finding 2)
T8  sqlite_sequence: after the purge a newly created GameSession primary key does NOT restart at 1
    (preflight finding 5)
T9  NEW: the command is idempotent — running it twice in a row leaves the second run a clean no-op
```

Use `django.core.management.call_command` and `override_settings`. You no longer need `MigrationExecutor`, `restore_apps_to_leaf`, or any migration-graph handling in this file — which is the point.

Give every case a **pre-fix / post-fix** note with the exact pre-fix behaviour.

## 5. Positive authority — the exact changed-path allowlist

```text
backend/config/settings.py                                     keep, comment corrected
backend/.env.example                                           keep
backend/game/management/commands/purge_legacy_game_state.py    NEW FILE
backend/tests/test_purge_legacy_game_state.py                  NEW FILE
backend/game/migrations/0008_purge_legacy_game_state.py        DELETE (uncommitted, never applied)
backend/tests/test_atomic_token_purge_migration.py             DELETE (uncommitted; superseded)
```

`backend/game/management/commands/` already exists and already holds `diagnose_ai_engine.py`, `diagnose_ai_play.py`, and an `__init__.py`, so no package scaffolding is needed. Follow the house style of `backend/catalog/management/commands/seed_models.py`.

Nothing else. A seventh path means **stop and report**.

⛔ `backend/tests/test_scoreless_turns_migration.py` is **NOT** in the allowlist and must not be touched. Under this mechanism it needs no change, and that is one of the reasons the mechanism changed. If it still fails, that is a finding and you stop.

## 6. Negative authority

```text
NO migration created, edited, or deleted other than the uncommitted 0008 named in 4a.
NO makemigrations, ever. NO migrate of any app. The live database schema does not change in F2a.
NO change to backend/game/models.py, services.py, serializers.py, views.py, consumers.py,
   diagnostics.py, or anything under backend/gamecore/.
NO change anywhere under frontend/, including the ten untracked images.
NO change to backend/accounts/, backend/catalog/, backend/billing/, backend/config/ beyond the flag.
NO change to test_scoreless_turns_migration.py or test_creditless_migration.py.
NO manage.py flush, no raw SQL DELETE, no PRAGMA change, no VACUUM, no schema change.
NO write to backend/.env, and no read of it. .env.example only.
NO staging of backend/db.sqlite3 or any *.sqlite3 file.
NO killing, restarting, or signalling any process. No pkill, ever.
NO dependency, lockfile, runtime, or toolchain change.
NO documentation change: not README.md, not AGENTS.md.
NO network except the authorized git ls-remote and one git push.
NO writes outside the repository allowlist except /tmp/opencode/mtt-f2a-checkpoint/.
```

Four standing Cooperator locks, none of which this slice touches: the nine AI providers are frozen; MOVE CORE hash `c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60` and version `pfr-s2-core-1` are pinned; `DEFAULT_MAX_ELAPSED_MS = 2000` and `DEFAULT_RANKED_MAX_ELAPSED_MS = 750` are fixed; exactly six `completion_source` values.

## 7. The five separated stages

```text
Evidence tier: E4
Combined implementation envelope: PROHIBITED. A failed gate stops the sequence.
Activated stricter profile: INFOSEC.md at R1 + R2, inline, non-independent
```

**Stage 0** — the gate of section 3. Any failure: stop, `BLOCKED`, mutate nothing.

**Stage 1** — write everything in section 4, apply nothing. Then the eight standing gates. Baseline at `9f0c5b8`, Orchestrator-measured:

```text
mypy               Success: no issues found in 81 source files    <- back to 81; no migration module
ruff               All checks passed!
manage.py check    System check identified no issues (0 silenced).
pytest             352 passed, 4 skipped   PLUS your nine new cases, and
                   tests/test_scoreless_turns_migration.py MUST be green again
npm run typecheck  exit 0
npx vitest run     342 passed | 3 skipped   (26 files passed | 1 skipped)
npm run lint       exit 0
npm run build      exit 0
```

Traps: `addopts = "-q"` is already set, so a second `-q` **silently suppresses the pytest summary** — run plain `-m pytest` and quote the summary verbatim. mypy on the full documented scope, never narrowed. Before `npm run build` run `ss -tlnp | grep :3000`; a listener means stop and report, never kill. State "the build passed" and "the code type-checks" as two separate claims.

**Gate G1: all eight green, all nine cases pass, and `test_scoreless_turns_migration.py` is green.** If G1 fails, stop and report — do not enter stage 2.

**Stage 2** — the checkpoint, unchanged from your previous prompt:

```bash
mkdir -p /tmp/opencode/mtt-f2a-checkpoint
sqlite3 /home/agile/Projects/libretiles/backend/db.sqlite3 \
  ".backup '/tmp/opencode/mtt-f2a-checkpoint/db.sqlite3.f2a-checkpoint'"
```

`sqlite3` is present at `/usr/bin/sqlite3`. ⛔ Do **not** use a plain `cp` as the checkpoint. Then prove it: report the byte size and SHA-256; `PRAGMA integrity_check` on the checkpoint must be `ok`; the five counts read **from the checkpoint** must equal the live ones; capture the full 24-table map from the checkpoint. **Gate G2: all of that holds.**

**Stage 3** — run the purge on the development database. Capture the complete 24-table count map immediately before, then:

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py purge_legacy_game_state --dry-run
ALLOW_DESTRUCTIVE_GAME_STATE_RESET=true \
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py purge_legacy_game_state
```

Run `--dry-run` first, without the flag, and quote its output — it is free evidence that the gate reports correctly before anything is destroyed. The flag is a **one-shot environment variable on the second command only**. ⛔ Do not write it into `backend/.env`.

Capture the complete 24-table map immediately after.

```text
G3.1  the five target tables are all 0
G3.2  EVERY other table's count is identical to the before map — accounts_user 4,
      catalog_ai_model 12, catalog_ai_prompt 4, token_blacklist 23 and 5, all four axes_* 0,
      django_content_type 19, auth_permission 76, sqlite_sequence 17, django_session 0,
      django_admin_log 0, and the rest
G3.3  django_migrations is STILL 63 and the game leaf is STILL 0007_consumedwsticket.
      This is now a positive assertion: the purge is not a migration and must leave the graph alone.
G3.4  PRAGMA integrity_check on the live database == ok
G3.5  billing_% still absent
```

**Gate G3: all five hold.** Any failure: stop immediately, report the exact divergence and the checkpoint path, do not attempt a restore, do not commit. A restore is a Cooperator-visible decision the Orchestrator will route.

**Stage 4** — re-run `manage.py check` and the full `pytest`. Tests use their own database, so the counts must be unchanged from stage 1. **Gate G4: both clean.**

**Stage 5** — commit and push.

```text
stage by EXPLICIT PATH only, including the two deletions
re-run git status --porcelain=v1 and confirm the ten flag images are still untracked and unstaged
review the complete staged diff
commit subject: feat(game): add a fail-closed command to purge legacy development game state
pre-push gate: git ls-remote origin refs/heads/main MUST still equal
               9f0c5b8141b94785f26f84fd0104131f063c3ed6 — if it advanced, STOP and report
one non-force git push origin main
public readback: git ls-remote origin refs/heads/main compared with git rev-parse HEAD, both quoted
```

⛔ `backend/db.sqlite3` is untracked and must never be staged. Confirm explicitly.

## 8. Containment ledger

```text
temporary root    /tmp/opencode/mtt-f2a-checkpoint/
owner             you
mode              report the observed mode
contents class    one SQLite checkpoint of the development database, containing development game state
                  and account rows. NOT public-safe: do not print its contents, do not copy it
                  elsewhere, do not attach it to the report. Path, size and SHA-256 are metadata and
                  are required.
cleanup owner     the COOPERATOR, after the Orchestrator accepts this slice
cleanup outcome   retain-with-reason — it is the only recovery path for an irreversible operation.
                  ⛔ Do NOT delete it yourself.
```

## 9. Stopping conditions

Stop, preserve state, and report on: any gate G0–G4 failing; porcelain showing anything unexpected; a non-SQLite engine or a different `NAME`; any `billing_%` table; an inbound FK into the five from outside the five; any protected count changing; a checkpoint that cannot be proven usable; needing a seventh path; `test_scoreless_turns_migration.py` still failing; a process holding the database at stage 0; a listener on port 3000 at build time; the pre-push gate not matching; the `.venv` route unavailable; a pre-existing defect outside the allowlist — **record it, do not fix it**.

If the same failing gate survives one correction attempt with an unchanged hypothesis and candidate, report `PARTIAL` or `BLOCKED` with exactly `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`. This is already the second exchange on this slice; a third equivalent cycle is prohibited without new material evidence.

## 10. Report contract

Begin **exactly** `### Report for ORCHESTRATOR_CHAT`. Echo the coordinates once: logical whole `multilingual-tile-token-foundation`, Worker session `04`, Worker exchange `02`.

Then: status; `Phase-qualified result`; start and end commit; the stage 0 gate evidence quoted; every changed path including both deletions; **the complete 24-table before/after count map side by side, with each row marked target-emptied or protected-unchanged** — this is the central evidence of the slice; the `--dry-run` output quoted; positive confirmation that `django_migrations` stayed 63 and the game leaf stayed `0007`; the eight gates for stage 1 and the stage 4 re-run, with pytest and vitest summaries verbatim and the two build claims stated separately; explicit confirmation that `test_scoreless_turns_migration.py` is green and untouched; the pre-fix / post-fix table for T1–T9; the checkpoint path, size, SHA-256, `integrity_check` and five counts; the containment ledger with `retain-with-reason`; confirmation that `db.sqlite3` was never staged and no `.env` was read or written; the F2b and F2c obligations below; deviations, risks and missing evidence honestly; `Resolved Execution Issues / Near-Misses`; `Pre-Existing Failure Classification`; commit and push with the public readback; one smallest next step; `Report justification: new-mutation`; `Logical-whole closure: not-closed`; and an explicit authority-expiry statement.

Hand these forward, and add the two new ones:

```text
- F2b MUST add the ordering guard: migration 0008_atomic_token_state_schema refuses to run while any
  of the five game-state tables is non-empty, with an error naming
  `manage.py purge_legacy_game_state`. This guard is what replaces the graph-position ordering the
  deleted migration would have given. It must be a refusal, never a deletion, and it needs its own
  test proving both the refusal and the clean pass on empty tables.
- F2b's schema migration is numbered 0008, not 0009.
- delete _word_passes_dictionary and re-point evaluate_scoring_move at WordAuthority
- invert the Cell storage and remove the F1 derived properties
- wire slot0_wins_starting_draw into _perform_starting_draw
- correct uii-01-F06
- then REST/websocket v4 and the frontend in F2c
```

⛔ Do not emit any logical-whole closure signal. Your evidence is **non-independent** — say so.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 04_implementation_01.md
Destination path: /home/agile/meta/projects/libretiles/11/01-multilingual-tile-token-foundation/
Archival: wait-for-report
```

You do not archive this pair. The Cooperator does, after your report exists.

Your authority expires at your terminal report.
