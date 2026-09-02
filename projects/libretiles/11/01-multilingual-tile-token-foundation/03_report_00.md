### Report for ORCHESTRATOR_CHAT

Logical whole `multilingual-tile-token-foundation`. Worker session `03`. Worker exchange `01`.

1. **status:** `PASS`  
   Evidence is sufficient to recommend a **separately authorized** F2 implementation slice. This preflight does not authorize that slice, does not create or apply a migration, and does not delete any live rows.

2. **Phase-qualified result: not-applicable**

3. **Repository gate evidence** (working directory `/home/agile/Projects/libretiles`):

```text
git rev-parse HEAD
9f0c5b8141b94785f26f84fd0104131f063c3ed6

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
9f0c5b8141b94785f26f84fd0104131f063c3ed6	refs/heads/main

git status --porcelain=v1
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
```

Porcelain is exactly the ten Cooperator-supplied flag images. No other dirty, staged, or untracked paths. Those files were not touched.

Execution route used from `backend/`: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py …`. `.venv/bin/python` is present (`Python 3.12.12`).

**Threat model (INFOSEC §5, route R1):** assets are the Cooperator’s development SQLite file and the protected account/catalog/JWT/axes rows inside it. Trust boundary is this Worker versus that live file, with all writes confined to `/tmp/opencode/mtt-f2-preflight/`. Actor assumption is local Cooperator-authorized destruction of test games. Relied-on properties: SQLite engine identity, exact `NAME` path, fail-closed flag (not yet present), and an FK set with no unnamed inbound edges. Abuse case: a purge aimed at the wrong engine, path, or table.

4. **The eleven items**

**1. Database identity.** Django-resolved values only:

| key | observed |
|---|---|
| `settings.DATABASES["default"]["ENGINE"]` | `django.db.backends.sqlite3` |
| `settings.DATABASES["default"]["NAME"]` | `/home/agile/Projects/libretiles/backend/db.sqlite3` |

Resolved absolute path: `/home/agile/Projects/libretiles/backend/db.sqlite3`. Byte size: `389120`. mtime: `2026-09-01 14:18:34.571546513 +0200` (`2026-09-01T12:18:34.571547+00:00`). Mode `0644`, owner `agile`. Vendor reported by the live Django connection: `sqlite`. Engine is SQLite, so the stop condition for a non-SQLite engine did not fire.

**2. Complete table inventory with row counts** (live, `SELECT COUNT(*)`, sorted by name). 24 tables. `PRAGMA foreign_keys` = `1`. `PRAGMA busy_timeout` = `5000`.

| table | rows |
|---|---|
| `accounts_user` | 4 |
| `accounts_user_groups` | 0 |
| `accounts_user_user_permissions` | 0 |
| `auth_group` | 0 |
| `auth_group_permissions` | 0 |
| `auth_permission` | 76 |
| `axes_accessattempt` | 0 |
| `axes_accessattemptexpiration` | 0 |
| `axes_accessfailurelog` | 0 |
| `axes_accesslog` | 0 |
| `catalog_ai_model` | 12 |
| `catalog_ai_prompt` | 4 |
| `django_admin_log` | 0 |
| `django_content_type` | 19 |
| `django_migrations` | 63 |
| `django_session` | 0 |
| `game_chat_message` | 2 |
| `game_consumed_ws_ticket` | 1 |
| `game_move` | 42 |
| `game_player_slot` | 58 |
| `game_session` | 29 |
| `sqlite_sequence` | 17 |
| `token_blacklist_blacklistedtoken` | 5 |
| `token_blacklist_outstandingtoken` | 23 |

**3. The five target tables.** All five exist under exactly those names. Counts: `game_chat_message` 2, `game_move` 42, `game_player_slot` 58, `game_session` 29, `game_consumed_ws_ticket` 1. The set is **not empty** (132 rows). F2’s purge is therefore a real deletion, not a documented no-op, and **does** require the opt-in flag.

**4. Protected tables.**

| table | present | rows |
|---|---|---|
| `accounts_user` | yes | 4 |
| `catalog_ai_model` | yes | 12 |
| `catalog_ai_prompt` | yes | 4 |
| `token_blacklist_blacklistedtoken` | yes | 5 |
| `token_blacklist_outstandingtoken` | yes | 23 |
| `billing_credit_balance` | **no** | — |
| `billing_transaction` | **no** | — |
| `axes_accessattempt` | yes | 0 |
| `axes_accessattemptexpiration` | yes | 0 |
| `axes_accessfailurelog` | yes | 0 |
| `axes_accesslog` | yes | 0 |

`billing` is absent from `INSTALLED_APPS`. `backend/billing/migrations/` exists on disk (`0001_initial`, `0002_precise_usd_balances`) but is not in the applied graph. Live `sqlite_master` has no `billing_%` tables. `django_content_type` on the copy has game/catalog/accounts rows and no `billing` rows.

**5. Foreign-key topology.**

SQLite `PRAGMA foreign_key_list` reports every FK as `ON DELETE NO ACTION` / `ON UPDATE NO ACTION`. Django model `on_delete` is the semantic F2 must implement; SQLite will **not** cascade for a raw `DELETE`.

Foreign keys **pointing at** the five (SQLite, exhaustive). No table outside the five appears.

| source table | column | target | SQLite ON DELETE | Django `on_delete` |
|---|---|---|---|---|
| `game_chat_message` | `game_id` | `game_session.id` | NO ACTION | `CASCADE` |
| `game_move` | `game_id` | `game_session.id` | NO ACTION | `CASCADE` |
| `game_move` | `player_slot_id` | `game_player_slot.id` | NO ACTION | `CASCADE` |
| `game_player_slot` | `game_id` | `game_session.id` | NO ACTION | `CASCADE` |

`game_consumed_ws_ticket` has **no** inbound and **no** outbound FKs.

Foreign keys **from** a target **to** a protected table:

| source | column | protected target | Django `on_delete` | null |
|---|---|---|---|---|
| `game_session` | `ai_model_id` | `catalog_ai_model.id` | `SET_NULL` | yes |
| `game_session` | `ai_prompt_id` | `catalog_ai_prompt.id` | `SET_NULL` | yes |
| `game_player_slot` | `user_id` | `accounts_user.id` | `SET_NULL` | yes |
| `game_chat_message` | `user_id` | `accounts_user.id` | `SET_NULL` | yes |

`SET_NULL` fires if the **protected** row is deleted while the game row remains. Deleting the game row removes the FK source and does **not** update or delete the protected row.

`unnamed_tables_with_fk_into_targets`: **empty**. Django reverse relations from non-target installed models into the five: **empty**. Historical `billing_transaction.game` (`SET_NULL` → `game.gamesession`) exists only in the uninstalled `billing` app; those tables are not in this database.

Would any table outside the five lose rows, or violate a constraint, if the five were emptied in the prescribed order? **No**, on this database, with `PRAGMA foreign_keys=1` left on:

- Protected tables are referenced **from** the five, not the other way around.
- `django_admin_log` uses a generic `object_id` (not an FK into the five) and currently has 0 rows.
- `sqlite_sequence` keeps AUTOINCREMENT counters after `DELETE`; its **row count** stays 17. F2 must not `DELETE FROM sqlite_sequence`.

Prescribed order **is provably safe** on this schema:

1. `game_chat_message` (must precede `game_session`; no FK to `game_move` / `game_player_slot`)
2. `game_move` (must precede both `game_player_slot` and `game_session`)
3. `game_player_slot` (must precede `game_session`)
4. `game_session`
5. `game_consumed_ws_ticket` (independent; any position is FK-safe; keep last as authorized)

Redundancy: if F2 uses Django’s collector (`QuerySet.delete()` on historical `GameSession`), steps 1–3 are collector-redundant (`CASCADE`). Step 5 is **not** redundant: tickets are not related to sessions. If F2 uses `schema_editor.execute("DELETE FROM …")`, **none** of 1–4 are redundant, because SQLite `NO ACTION` will reject deleting a parent while children exist. **Do not** `PRAGMA foreign_keys=0`.

No finding of an unnamed inbound FK. The “wrong table” stop condition did not fire.

**6. Migration state.** `showmigrations game`:

```text
game
 [X] 0001_initial
 [X] 0002_multiplayer_chat_and_state
 [X] 0003_gamesession_total_cost_usd
 [X] 0004_gamesession_ai_prompt_alter_move_kind
 [X] 0005_remove_money_state
 [X] 0006_rename_consecutive_scoreless_turns
 [X] 0007_consumedwsticket
```

Every on-disk migration of every **installed** app is applied (`unapplied_migrations: []`, `applied_missing_from_disk: []`, `django_migrations` row count 63 matches the `[X]` list). Current `game` leaf is exactly `game.0007_consumedwsticket`. `0008` and `0009` do not exist on disk. No installed app has more than one leaf. `token_blacklist` has the upstream skipped `0009` (leaf `0013_alter_blacklistedtoken_options_and_more`); that is existing SimpleJWT history, not a branch. Disk-only `billing` migrations are not in the loader because the app is not installed.

**7. Fields `0009` will change** (current `0007` shape in `backend/game/models.py`). None of these four fields are `null=True` or `blank=True`.

```26:33:backend/game/models.py
    board_state = models.JSONField(
        default=list,
        help_text="15x15 grid as list of 15 strings",
    )
    blanks = models.JSONField(default=list, help_text="List of {row, col} for blank tiles")
    premium_used = models.JSONField(default=list, help_text="List of {row, col} for used premiums")
    bag_tiles = models.TextField(default="", help_text="Remaining tiles in order")
```

```82:82:backend/game/models.py
    rack = models.JSONField(default=list, help_text="Current rack letters as list of strings")
```

Starting shape for later `0009`: `GameSession.board_state` JSON, non-null, `default=list`; `GameSession.blanks` JSON, non-null, `default=list` (to be removed); `GameSession.bag_tiles` `TextField`, non-null, `default=""` (to be retyped); `PlayerSlot.rack` JSON, non-null, `default=list`.

**8. Setting does not exist yet.** Repository search for `ALLOW_DESTRUCTIVE_GAME_STATE_RESET`: **no matches**. `backend/.env.example` does **not** contain that name. `backend/.env` was not read. Presence in a live env file: **not established** (and not authorized to establish by reading `.env`).

**9. Live processes.** `ss -tlnp | grep -E ':(3000|8000)'`:

```text
LISTEN 0      50                       127.0.0.1:8000       0.0.0.0:*    users:(("python",pid=211102,fd=11))
```

No listener on `:3000`. PID `211102`: user `agile`, started `2026-09-01 20:24:24 +0200`, cwd `/home/agile/Projects/libretiles/backend`, command `/home/agile/Projects/libretiles/backend/.venv/bin/python manage.py runserver 127.0.0.1:8000`. One thread `211103`. `fuser` shows this PID holds `db.sqlite3` open. Nothing was killed.

**F2’s migration requires the Cooperator to stop that Django process first.** Reason: the live file is open; `migrate` needs an exclusive writer; a concurrent request can insert game rows during or after the purge; SQLite can raise `database is locked`. This PID is point-in-time; F2 must re-check `ss`/`fuser`, not assume `211102`.

**10. Backup and restore rehearsal.** Live (read-only): `PRAGMA journal_mode` = `delete`; `PRAGMA integrity_check` = `ok`. Sidecars `db.sqlite3-wal` and `db.sqlite3-shm` **absent**. Filesystem holding the DB: `/dev/nvme0n1p2` on `/`, `201751524` 1K-blocks free (~193 GiB), DB 389120 bytes.

Copies were taken only under `/tmp/opencode/mtt-f2-preflight/`:

- plain `shutil.copy2` of the single file: 389120 bytes, `integrity_check=ok`, all 24 table counts identical to live, five target counts identical.
- `sqlite3.Connection.backup` via `file:…?mode=ro`: same size, same `ok`, same counts.
- restore rehearsal: backup API from that copy onto a third temp file; `integrity_check=ok`; five target counts and protected counts matched.

Because `journal_mode` is `delete` and no sidecars exist, a **plain copy of the single file is sufficient in the observed mode**. `-wal`/`-shm` copy is not required **in this mode**. F2 should still use the backup API (a process currently has the file open; `delete` mode can change).

Exact checkpoint command F2 should use (after writers are stopped, or at least with no in-flight write):

```text
sqlite3 /home/agile/Projects/libretiles/backend/db.sqlite3 ".backup '/ABS/CHECKPOINT/db.sqlite3.f2-checkpoint'"
```

Equivalent authorized Python (same `.venv` deviation):

```text
env -u APPIMAGE -u ARGV0 -u APPDIR /home/agile/Projects/libretiles/backend/.venv/bin/python -c "import sqlite3; s=sqlite3.connect('file:/home/agile/Projects/libretiles/backend/db.sqlite3?mode=ro', uri=True); d=sqlite3.connect('/ABS/CHECKPOINT/db.sqlite3.f2-checkpoint'); s.backup(d); d.close(); s.close()"
```

Exact restore (Django must already be stopped; replace the live file, do not write into an open DB):

```text
cp /ABS/CHECKPOINT/db.sqlite3.f2-checkpoint /home/agile/Projects/libretiles/backend/db.sqlite3
```

or:

```text
sqlite3 /ABS/CHECKPOINT/db.sqlite3.f2-checkpoint ".backup '/home/agile/Projects/libretiles/backend/db.sqlite3'"
```

Do not `VACUUM` the live database. Do not restore while PID-holding the file is still running.

**11. Migration test house style.** Seven files: `test_creditless_migration.py`, `test_scoreless_turns_migration.py`, `test_playable_seeded_prompts_migration.py`, `test_refresh_seeded_prompts_migration.py`, `test_dynamic_free_catalog_migration.py`, `test_openrouter_catalog_migration.py`, `test_multi_provider_catalog_migration.py`.

Pattern:

- Schema / graph moves: `TransactionTestCase` + `MigrationExecutor(connection).migrate(migrate_from|migrate_to)` and historical models via `executor.loader.project_state(...).apps.get_model(...)` (`test_scoreless_turns_migration.py`).
- Destructive / irreversible data steps: `TransactionTestCase` + `call_command("migrate", app, target, verbosity=0)` or direct `importlib.import_module` of the migration’s `RunPython` callables; assert unrelated rows survive (`test_creditless_migration.py` is the closest cousin to a purge).
- Seeded-prompt / catalog data steps: often `TestCase` calling the migration function in-process, then a `TransactionTestCase` reverse that uses `call_command("migrate", …)` and `restore_apps_to_leaf`.
- `backend/tests/_migration_restore.py`: teardown only. `restore_apps_to_leaf(*app_labels)` calls `call_command("migrate", app_label, verbosity=0)` so tests never pin a hardcoded leaf in `finally`.
- Assertions: `assert` on columns/tables/counts/preserved FKs (`session.ai_model_id`, `User.objects.filter(pk=…).exists()`); irreversible money cleanup expects `CommandError` or `IrreversibleError`.
- F2 tests must use this harness, not a new one: `TransactionTestCase`, historical models, `restore_apps_to_leaf("game")` (and catalog/accounts if touched), explicit before/after counts for the five targets **and** the protected tables, a fail-closed case when the flag is false, and a no-op case on already-empty targets.

5. **Exact proposed mutation boundary for F2**

- **Database:** only `ENGINE=django.db.backends.sqlite3` with resolved `NAME` equal to `/home/agile/Projects/libretiles/backend/db.sqlite3`. Any other engine or path: refuse.
- **Flag:** add `ALLOW_DESTRUCTIVE_GAME_STATE_RESET`, default `false`, fail-closed. On this database the five tables are non-empty, so forward purge **must not run** unless the flag is true in the process that runs `migrate`. If all five counts are 0, the data step is a documented no-op and must not require the flag. Document the name in `backend/.env.example` only; do not require a Worker to read `.env`.
- **Authorized deletes, this order, named historical models only:** `game_chat_message` → `game_move` → `game_player_slot` → `game_session` → `game_consumed_ws_ticket`. No `flush`. No raw `DELETE` that does not go through a named historical model. No `PRAGMA foreign_keys=0`. No `VACUUM`.
- **Assert before:** the 24-table inventory matches the names above; billing tables absent; no inbound FK to the five from outside the five; captured counts for every non-target table; checkpoint exists and `integrity_check=ok`.
- **Assert after:** five targets at 0; every other table’s row count identical to the before snapshot, including `accounts_user=4`, `catalog_ai_model=12`, `catalog_ai_prompt=4`, both SimpleJWT tables, all four `axes_*` tables, `django_migrations=63`, `django_content_type=19`, `auth_permission=76`, `sqlite_sequence=17`. Optionally assert `sqlite_sequence.seq` values unchanged.
- **Must not change:** `accounts_user` rows (including `password_changed_at`), credentials, JWT blacklist, `catalog_ai_model`, `catalog_ai_prompt`, axes, sessions, admin log, content types, migration records, billing (must remain absent).
- **Apply-time gate:** Cooperator stops any process holding the SQLite file; Worker does not kill.
- **Numbering:** next unused `game` name is `0008_*`. Plan’s field rewrite remains a later `0009` on the current 0007 shape. F2 is the purge only.

6. **Recommendation.** F2 implementation **should proceed only under a new grant**. First-stage gate of that grant, before any file under `backend/game/migrations/` is created: (a) Cooperator-stopped Django / no `fuser` on `db.sqlite3`; (b) checkpoint via `.backup` as above; (c) tests written first in the existing harness proving fail-closed default, ordered purge, and unchanged protected counts; (d) identity assertions on `ENGINE`/`NAME`/absent billing/empty unnamed inbound FK set. This preflight is not that grant.

7. **Risks not already named in the accepted plan**

- SQLite stores these FKs as `ON DELETE NO ACTION` while Django models declare `CASCADE`/`SET_NULL`. A parent `DELETE` without prior child deletes fails (or, if someone turns FK checks off, is unconstrained). Implementation must keep FK checks on and either follow the SQL order or use the ORM collector.
- `game_consumed_ws_ticket` is disconnected; collector-delete of `GameSession` will not remove tickets.
- Live `runserver` holds the DB open (`pid 211102` at inspection time). Apply-while-running is a lock and concurrent-insert hazard.
- If `billing_transaction` were ever recreated with its historical `SET_NULL` to `game_session`, session deletes could update unauthorized rows. F2 must **refuse** if any `billing_%` table exists.
- `journal_mode` is `delete`, not WAL. WAL sidecar procedure would be the wrong checkpoint recipe on this file today; still prefer `.backup`.
- `sqlite_sequence` counters survive `DELETE`. Tests that expect reset PKs starting at 1 will be wrong unless they assert non-reset.

8. **INFOSEC containment ledger**

| field | value |
|---|---|
| temporary root | `/tmp/opencode/mtt-f2-preflight/` |
| owner | `agile:agile` (uid 1000, gid 1000) |
| permission mode | `0700` |
| contents class | temporary SQLite copies, a read-only inspection script, and JSON evidence; no secrets; no live-DB writes |
| cleanup owner | this Worker |
| cleanup outcome | exact path removed with `rm -rf /tmp/opencode/mtt-f2-preflight` (no glob). After cleanup the path is absent. `/tmp/opencode/` itself was left untouched. |

9. **Limitations / not established**

- Whether `ALLOW_DESTRUCTIVE_GAME_STATE_RESET` is already set in unread `backend/.env`: not established.
- Whether PID `211102` will still exist at F2 apply time: not established; re-check then.
- Test suite was not run (out of grant). Standing gate numbers from `9f0c5b8` were not re-measured; nothing observed contradicted them.
- `billing` disk migrations were not applied (forbidden). Their live absence is established; their future accidental presence is a refuse condition, not a current row-loss finding.
- Usernames, emails, password hashes, JWT strings, and ticket hashes were not read or printed.

10. **Resolved Execution Issues / Near-Misses:** initial `ls` of `backend/db.sqlite3` from cwd already `backend/` missed the file; recovered with the absolute path. Django shell printed `19 objects imported automatically`. Neither wrote the repository or the live DB.

11. **Pre-Existing Failure Classification: none**

12. **End-state confirmation.** HEAD is still `9f0c5b8141b94785f26f84fd0104131f063c3ed6`. Porcelain is still exactly the ten flag images. No commit, no push, no staged path. Live DB mtime and size after inspection and cleanup are unchanged (`2026-09-01 14:18:34.571546513 +0200`, `389120` bytes). No `migrate`, no `makemigrations`, no `DELETE`/`UPDATE`/`INSERT`/`VACUUM` on the live file.

13. **Smallest next step.** Orchestrator issues a **separate** F2 implementation grant whose first stage is the apply-time gate in section 6 (stop Django, `.backup` checkpoint, fail-closed tests, then `0008` purge only).

14. **Report justification: new-evidence**

15. **Logical-whole closure: not-closed**

16. **Authority expiry.** Worker-exchange `03`/`01` authority ends at this terminal report. This preflight does not authorize creating, editing, or applying a migration, and it emits no logical-whole closure signal.