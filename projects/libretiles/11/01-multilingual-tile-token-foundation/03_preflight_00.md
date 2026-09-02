You are a WORKER instance assigned to the persistent AP WORKER role. Execute exactly this bounded task and stop.

```text
Logical whole identity: multilingual-tile-token-foundation
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Worker-Executed Preflight
Task identity: MTT-F2-PRE — read-only preflight for the irreversible game-state purge
Phase: Preflight
Implementation authority: NONE
Independence required: no
Evidence posture: non-independent
Exact baseline: 9f0c5b8141b94785f26f84fd0104131f063c3ed6
Logical-whole closure: not-closed
```

Reasoning recommendation: **High.** Named risk: the operation this preflight prepares is irreversible destruction of database rows, classified **E4**. The governing risk in the accepted plan's register is "destructive migration targets the wrong database or the wrong tables — irrecoverable unrelated data loss". Your job is to make that boundary exact before anyone writes a migration. You do not perform the deletion and you do not write the migration.

⛔ **This preflight grants NO implementation authority.** A `PASS` here recommends that a separately authorized implementation slice may be issued. It never authorizes it. You will not create, edit, or apply a migration in this exchange.

## 1. Repository, topology, and gate

```text
Repository checkout topology: standalone checkout
Working directory: /home/agile/Projects/libretiles
Repository identity: https://github.com/cisarik/libretiles
Expected branch: main
Expected HEAD: 9f0c5b8141b94785f26f84fd0104131f063c3ed6
Expected .ap gitlink and submodule HEAD: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

Verify and quote, before anything else:

```text
git rev-parse HEAD                      == 9f0c5b8141b94785f26f84fd0104131f063c3ed6
git rev-parse HEAD:.ap                  == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD               == the same
git status -sb                          == ## main...origin/main
git ls-remote origin refs/heads/main    == 9f0c5b8141b94785f26f84fd0104131f063c3ed6
git status --porcelain=v1
```

`git status --porcelain=v1` must report **exactly** these ten untracked files and nothing else:

```text
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

They are Cooperator-supplied flag assets belonging to a different logical whole. Do not touch them. If porcelain shows anything else, classify the difference with all five AP recovery classes and stop if the primary class is `unexplained-divergence`.

The repository must still be at `9f0c5b8` when you finish. This exchange produces **no commit and no push.**

## 2. Mutation domains — read this before you run anything

AP requires these four domains to be distinguished explicitly. For this exchange:

```text
Repository mutation:            PROHIBITED. No file created, edited, renamed, deleted, staged, or committed.
Durable project-state mutation: PROHIBITED. No write to the development database. No migrate, no
                                makemigrations, no DELETE, no UPDATE, no INSERT, no schema change,
                                no VACUUM, no PRAGMA that writes.
External or production mutation: PROHIBITED. No network except the one authorized git ls-remote.
Temporary probe-state mutation:  AUTHORIZED, and only inside this exact directory:
                                    /tmp/opencode/mtt-f2-preflight/
                                You may create it, copy files into it, run SQLite against those
                                copies, and remove it. Nothing outside it may be written.
```

Report the temporary root, its owner, its permission mode, its contents class, the cleanup owner, and the cleanup outcome, per the AP containment ledger contract. Cleanup removes that exact path only — **no wildcards.**

⛔ **Never read or print `backend/.env` or `frontend/.env.local`.** You may print resolved Django settings **only** as named below. If any value you are about to print could be a credential, print its presence as a boolean instead.

## 3. Mandatory reading

- `AGENTS.md` and `.ap/AP.md`, `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md`
- `.ap/INFOSEC.md` sections 3, 5, 9, 10, 11, 16
- `backend/game/models.py` in full
- `backend/game/migrations/` — every file, in order
- `backend/tests/_migration_restore.py` and any two of the seven existing `test_*_migration*.py` test files, to learn the house style for migration tests
- `backend/config/settings.py`, the `DATABASES` block only

## 4. Goal — one coherent outcome

Produce the exact, evidence-backed mutation boundary for slice F2's irreversible purge, so that the F2 implementation grant can be written from measured facts instead of assumptions.

Background you need, already decided and not open for you to re-decide:

- The Cooperator authorized deletion of **development** game state on 2026-09-01, in his own words: `obetovatelne - vsetky rozohrate vymazat predsa, su to len testovacie hry`.
- Authorized tables, in this deletion order: `game_chat_message`, `game_move`, `game_player_slot`, `game_session`, `game_consumed_ws_ticket`.
- **NOT** authorized, ever: `accounts_user` rows, credentials, `password_changed_at`, the JWT blacklist, `catalog_ai_model`, `catalog_ai_prompt`, or any other table.
- **NOT** authorized: `manage.py flush`, a raw `DELETE` without a named historical model, or anything against a database other than his development one.
- F2 will add a fail-closed setting `ALLOW_DESTRUCTIVE_GAME_STATE_RESET`, default `false`.

## 5. The eleven items you must establish

Answer each with exact observed evidence. Where you cannot establish something, say `not established` and name what evidence is missing — do not infer.

**1. Database identity.** Print **only** `settings.DATABASES["default"]["ENGINE"]` and `["NAME"]`. Nothing else from that dict. Then report the resolved absolute path of the SQLite file, its byte size, and its mtime.

⛔ **If `ENGINE` is not `django.db.backends.sqlite3`, STOP immediately and report `BLOCKED`.** A non-SQLite engine means this is not the expected development database and the destructive boundary is not the one the Cooperator authorized.

**2. Complete table inventory with row counts.** Every table in that database, with its row count. Not only the interesting ones — the complete list is what lets F2 assert "the protected tables are unchanged". Present it as a table sorted by name.

**3. The five target tables.** Confirm each of `game_chat_message`, `game_move`, `game_player_slot`, `game_session`, `game_consumed_ws_ticket` exists with exactly that name, and give its row count. State whether the set is currently empty, because an empty database makes F2's migration a documented no-op that does not require the opt-in flag.

**4. The protected tables.** Confirm existence and row counts for at least `accounts_user`, `catalog_ai_model`, `catalog_ai_prompt`, and the SimpleJWT blacklist tables. Report whether `billing_credit_balance` and `billing_transaction` exist in the database — `backend/billing/` has migrations on disk but the app is absent from `INSTALLED_APPS`, so their presence or absence is itself a fact F2 needs. Also report the `django-axes` tables and their counts.

**5. Foreign-key topology, in both directions.** This is the item that protects against the governing risk, so be exhaustive rather than brief:

- every foreign key **pointing at** any of the five target tables, with its source table, column, and `on_delete` behaviour;
- every foreign key **from** a target table **to** a protected table (`GameSession.ai_model` and `ai_prompt` are two of these — confirm and report their `on_delete`);
- whether **any table outside the five** would lose rows, or violate a constraint, if the five were emptied in the prescribed order.

Then state explicitly whether the prescribed deletion order is provably safe, and whether any of the five steps is redundant because Django's collector already cascades. If you find a table with an FK into the five that the authorized list does not name, that is a **finding** and it changes the boundary — report it prominently.

**6. Migration state.** Output of `showmigrations` for the `game` app and a statement of whether every migration in every app is applied. Confirm the current `game` leaf is `0007_consumedwsticket` and that `0008` and `0009` do not exist. Report whether any app has an unapplied migration or more than one leaf.

**7. The fields `0009` will change.** From `backend/game/models.py`, quote with line numbers the current definitions of `GameSession.board_state`, `GameSession.blanks`, `GameSession.bag_tiles`, and `PlayerSlot.rack`, including nullability, defaults, and help text. `0009` removes `blanks` and retypes `bag_tiles`; F2 needs the exact starting shape.

**8. The setting does not exist yet.** Confirm by search that `ALLOW_DESTRUCTIVE_GAME_STATE_RESET` appears nowhere in the repository. Confirm whether `backend/.env.example` documents it — read `.env.example`, which is a committed template and is safe. **Do not read `backend/.env`.** Report only whether the variable name is present in the example template.

**9. Live processes holding the database.** Run `ss -tlnp | grep -E ':(3000|8000)'` and report every listener with its PID and command. ⛔ **Kill nothing. Never use a broad pattern kill such as `pkill -f`** — the Cooperator's own development server runs on these ports and a previous session survived doing that only by luck. Then state plainly whether F2's migration requires his Django server to be stopped first, and why.

**10. Backup and restore rehearsal.** Establish that the checkpoint F2 will rely on actually works:

- report `PRAGMA journal_mode` and `PRAGMA integrity_check` on the live database (both are read-only);
- report available free space on the filesystem holding it;
- **copy** the database file into `/tmp/opencode/mtt-f2-preflight/`, then prove the copy is usable: open the copy, run `PRAGMA integrity_check`, and read the same five row counts from it, and show that they match the live ones;
- if `journal_mode` is `wal`, say explicitly whether a plain file copy is sufficient or whether the `-wal` and `-shm` sidecars must be copied too, and demonstrate whichever you conclude;
- state the **exact** command F2 should use to take its checkpoint, and the exact command to restore from it.

The live database is read-only to you throughout. The rehearsal happens on the copy.

**11. Migration test house style.** From the seven existing `test_*_migration*.py` test files, report the pattern this project uses to test a migration: how the test harness applies and reverses migrations, what `backend/tests/_migration_restore.py` is for, and what the house assertion style looks like. F2's migration tests must match it rather than invent a new harness.

## 6. Execution route — mandatory bounded deviation under RF-16

```text
Declared route that could not be used:  poetry run <tool>, as documented in AGENTS.md "Code quality"
Exact alternate path, from backend/:    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python …
Rationale:                              the Cursor AppImage environment intercepts python* through
                                        inherited APPIMAGE / ARGV0 / APPDIR / PYTHONHOME
Evidence class:                         reproduced-dynamic, established repeatedly in this project
Bounded authority:                      this task only; never a second standing canonical route
Stopping condition:                     if .venv/bin/python is absent or the deviation fails, STOP and
                                        report. Do not use ambient python, python3, or poetry run, and
                                        do not repair the environment.
```

For database inspection, prefer the Django ORM through the project's own settings resolution — a read-only script executed with `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py shell < your_script` or the equivalent — so that you measure the database Django actually targets rather than a path you guessed. You may additionally use the `sqlite3` module against the **copy** in the temporary root.

Never present ambient `python`, `python3`, or `poetry run` as an equivalent alternative.

## 7. Negative authority

```text
NO migration created, edited, or applied. No manage.py migrate. No manage.py makemigrations.
NO manage.py flush, no DELETE, no UPDATE, no INSERT, no schema change, no VACUUM, no write PRAGMA.
NO repository file written, edited, renamed, deleted, or staged. No commit. No push.
NO write to the live development database, by any route.
NO reading or printing of backend/.env or frontend/.env.local. .env.example is fine.
NO killing, restarting, or signalling any process. No pkill, ever.
NO dependency, lockfile, or toolchain change. No pip, no poetry add, no npm install.
NO change to the ten untracked flag images.
NO network access except the one authorized git ls-remote.
NO writes anywhere outside /tmp/opencode/mtt-f2-preflight/.
```

The four standing Cooperator locks are untouched by a read-only preflight and must stay that way: the nine AI providers are frozen; the MOVE CORE hash `c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60` and version `pfr-s2-core-1` are pinned; `DEFAULT_MAX_ELAPSED_MS = 2000` and `DEFAULT_RANKED_MAX_ELAPSED_MS = 750` are fixed; there are exactly six `completion_source` values.

## 8. Validation

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none — running the suite is NOT part of this preflight
Affected tests: none
New causal regression: none
Broad or full suite: not-used
Runtime or testbed: the authorized temporary probe root only
Independent acceptance: not-required
Evidence tier: E1 for this exchange — read-only inspection plus bounded temporary probe state
Evidence tier basis: it prepares an E4 operation but performs none of it; every effect is confined to
  a temporary directory and is fully reversible by removing that directory
Activated stricter profile: INFOSEC.md at R1, with the containment ledger of section 10 required
Combined implementation envelope: prohibited
Terminal implementation report point: not-applicable — this exchange produces a preflight report
```

You do not need to run the eight standing gates. The tree is unchanged, so they are still the values the Orchestrator measured at `9f0c5b8`: mypy 81 files, ruff clean, `manage.py check` clean, pytest `352 passed, 4 skipped`, typecheck exit 0, vitest `342 passed | 3 skipped`, lint exit 0, build exit 0. If you happen to observe something that contradicts any of those, report it as a finding.

## 9. Stopping conditions

Stop, preserve evidence, and report:

- any repository or baseline gate fails, or porcelain shows anything beyond the ten flag images;
- `settings.DATABASES["default"]["ENGINE"]` is not SQLite;
- a table with a foreign key into the five target tables exists that the authorized list does not name;
- any protected table would lose rows under the prescribed deletion order;
- the backup rehearsal cannot demonstrate a usable restore;
- `PRAGMA integrity_check` on the live database is not `ok`;
- establishing an item would require a write, a kill, a credential read, or a path outside the temporary root;
- the `.venv` execution route is unavailable.

## 10. Report contract

Begin the report **exactly**:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once, unchanged: logical whole `multilingual-tile-token-foundation`, Worker session `03`, Worker exchange `01`.

Then:

1. status: `PASS`, `PARTIAL`, or `BLOCKED`, using the preflight meanings — `PASS` when the evidence is sufficient to recommend a separately authorized F2 implementation slice, `PARTIAL` when a material prerequisite, risk, or recovery detail is unresolved, `BLOCKED` when implementation must not be authorized;
2. `Phase-qualified result: not-applicable` — a preflight is not one of the five PASS results;
3. the repository gate evidence, quoted;
4. the eleven items of section 5, each with exact observed evidence;
5. **the exact proposed mutation boundary for F2**: the precise table list, the deletion order, the flag semantics, what must be asserted before and after, and what must provably not change;
6. **your explicit recommendation on whether F2 implementation should proceed**, and if so what its first stage gate must be;
7. every risk you found that the accepted plan does not already name;
8. the INFOSEC containment ledger: temporary root, owner, mode, contents class, cleanup owner, cleanup outcome;
9. limitations and anything `not established`, honestly;
10. `Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>`;
11. `Pre-Existing Failure Classification: none | <the complete contract record>`;
12. confirmation that the repository is still at `9f0c5b8141b94785f26f84fd0104131f063c3ed6`, that porcelain is unchanged, that no commit or push occurred, and that the live database was not written;
13. one smallest next step;
14. `Report justification: new-evidence`;
15. `Logical-whole closure: not-closed`;
16. an explicit authority-expiry statement.

⛔ You must **not** emit any logical-whole closure signal, and you must not describe this preflight as authorizing the migration.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 03_preflight_00.md
Destination path: /home/agile/meta/projects/libretiles/11/01-multilingual-tile-token-foundation/
Archival: wait-for-report
```

You do not archive this pair. The Cooperator does, after your report exists.

Your authority expires at your terminal report.
