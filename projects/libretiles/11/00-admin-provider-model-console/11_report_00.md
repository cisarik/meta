### Report for ORCHESTRATOR_CHAT

Logical whole identity: admin-provider-model-console  
Worker session ordinal: 11, Worker exchange ordinal: 01

**Status: PARTIAL.** V-F02/V-F01/V-F03 are verified-closed on a migrated schema. Existing-DB recovery is not a one-command operation: `showmigrations` is quiet, but every `migrate` form raises `InconsistentMigrationHistory` and never applies `accounts.0005`. New finding APMC-S4-IA-F07.

Security task class: fresh independent re-audit, second cycle (INFOSEC 4.11)  
Owned/authorized target: Libre Tiles canonical repository, correction-2 commit `6049f2895321da33c7594aedd922aef63544e18d`  
Commit under audit: `6049f2895321da33c7594aedd922aef63544e18d`  
Scope: correction-2 diff (6 files) + F02 end-to-end + F01/F03 closure persistence + C-regression  
Exclusions: F04 (dispositioned residual; slice-5 obligation stands), F05/F06, INFOSEC 4.6  
Independence: fresh session; no implementation or correction performed.

**Threat model** (session 07 §2, plus measured delta)

Assets: Django session/admin; diagnostic `GameSession` / `DiagnosticRun` rows; service-user JWT; player game-history integrity; formed-word / scoring integrity; provider credentials and quota; catalog `is_active`/`sort_order`.  
Trust boundaries: admin/`created_by` → `create_diagnostic_game`; service JWT → DRF AI endpoints; ordinary player JWT → same endpoints; history serializer → browser; authenticated bearer → account mutation → player participation.  
Attacker-controlled inputs: registration/profile usernames and authenticated game requests.  
Required properties: no adoption of password-enabled claimants; no ordinary player participation by the service bearer; no deletion of password-enabled claimants on reversal; object-level auth stays `slots__user_id`.

Measured delta: `User.is_service_account` is the durable identity-boundary attribute for rename and participation. Username equality remains a second, still-live belt-and-braces predicate. An ordinary bearer cannot set or clear the flag through `UserSerializer` or `RegisterSerializer`. Django Admin `UserAdmin` still exposes `username` and still omits the flag.

**Per-finding verdicts**

| ID | Verdict | Evidence class and pointer |
|---|---|---|
| V-F02 | **verified-closed** (on a migrated schema) | **reproduced-dynamic**, independent probes VF02A–E; `accounts/serializers.py:52-61`, `game/services.py:1082-1102` |
| V-F01 | **verified-closed** | **reproduced-dynamic**, VF01; collision branch still raises before any flag write |
| V-F03 | **verified-closed** (classification-loss residual unchanged) | **reproduced-dynamic**, VF03; **established-static**, reverse body in `game/migrations/0009_diagnostic_session_foundation.py:18-42` is untouched except the new dependency line |
| V-ORD | **not accepted** (item b) | **reproduced-dynamic**, throwaway DB; new finding F07 |
| V-REG | **verified-closed** | C3/C6 dynamic; C8/C10 static — table below |

**V-F02 end-to-end**

| Check | Independent result |
|---|---|
| a. flagged PATCH rename | `400`; username unchanged `libretiles-diagnostic`; flag `True` |
| b. same JWT after refused rename → create → queue | create `400` `ok:false`; queue `400` `ok:false` `waiting is not True`; product delta `0`; vs_human delta `0` |
| c. ordinary rename / create / queue | rename `200` `player1-renamed`; create `201`; queue `200` `ok:true` |
| e. flag flipped `False` → next `ensure` | same pk; flag restored `True` |

**V-F02 (d) guard-bypass hunt**

- Django Admin `UserAdmin` still includes inherited `username` and does **not** include `is_service_account`. An ORM/admin username assignment left the flag `True`; the same JWT then got create/queue `400`. The flagged principal cannot participate after an operator rename.
- `PATCH /api/auth/me/` with `{"is_service_account": false}` returned `200` and did not expose or clear the flag (field is not serialized).
- Case-variant registration `Libretiles-Diagnostic` returned `201`, flag `False`; that user renamed to a fresh name (`200`) and created a product game (`201`). That user is **not** a service identity. Boundary: the flag marks **the managed account**. Other users are ordinary by design. Case variants are not the F02 principal.
- The F02 property “service bearers cannot participate as ordinary players” is now enforced by `is_service_account` on the user id the JWT maps to. An attacker cannot set that attribute through the product API (registration create path has no `validate_username`; `UserSerializer` fields omit the flag; `create_user` defaults `False`).
- Belt-and-braces username branch is **still reachable**, not dead: an unflagged occupant of `DIAGNOSTIC_SERVICE_USERNAME` still got create `400`. The two predicates will diverge after an admin/ORM rename that frees the reserved name: the original principal stays blocked by the flag; whoever currently holds the reserved username is blocked by string equality (and `ensure` still fail-closes on a usable-password occupant).

**V-F01** — usable-password claimant: `ensure` raised (message contains `usable password`); password check intact; `is_service_account` remained `False`; claimant row untouched. The new flag write is after the collision `raise` and did not adopt or flag the claimant.

**V-F03** — reverse kept the claimant (password intact), deleted the unusable managed account. `is_password_usable(managed.password)` agrees with `has_usable_password()`. Reverse docstring still documents classification-loss residual. Dependency-line-only change to `0009` did not alter reverse behaviour.

**V-ORD**

| Path | Result |
|---|---|
| a. fresh DB from zero | **verified-closed**. Throwaway HEAD tree: `Applying accounts.0005_service_account_flag... OK` then `Applying game.0009_diagnostic_session_foundation... OK`. Graph index `29 < 30`. Seeded account `is_service_account=True`, unusable password. Import path confirmed as the temp tree. |
| b. existing DB with `0009` already applied | **not accepted**. Shape reproduced: migrate through `f6c9db9` (no `0005`), overlay HEAD `0005` + `0009` dependency. `showmigrations` quiet, rc `0`, `[ ] 0005` / `[X] 0009`. Then `migrate`, `migrate accounts 0005`, and `migrate --plan` all rc `1` with `InconsistentMigrationHistory: Migration game.0009_diagnostic_session_foundation is applied before its dependency accounts.0005_service_account_flag on database 'default'.` Zero schema writes. Column absent. `User` ORM raises `OperationalError: no such column: accounts_user.is_service_account`. |
| c. `0009` RunPython on fresh DB | **verified-closed**. Fresh path completed; helper set the flag; no `AttributeError`. |

The correction report’s operator story (`showmigrations` quiet **and** one normal `migrate` resolves it) is false for item b. `showmigrations` does not call `check_consistent_history`; `migrate` always does, before applying anything (`django/core/management/commands/migrate.py:117`, Django 5.2.17).

**V-REG**

| Claim | Verdict | Evidence |
|---|---|---|
| C3 object-level 404s both directions | verified-closed | player JWT on diagnostic `404`; service JWT on unowned product `404` |
| C6 abort zero-Move | verified-closed | move delta `0`; `game_end_reason` empty; status `abandoned`; AST of `abort_diagnostic_run` calls neither `_submit_pass_locked` / `_submit_exchange_locked` nor `_reject_ai_nonscoring` |
| C8 four invariant files | verified-closed | `git diff --stat f6c9db9..6049f28` is exactly 6 files. Blob SHAs identical for `backend/gamecore/legality.py`, `word_authority.py`, `move_search.py`. `_reject_ai_nonscoring` function body SHA-256 identical (`6848980bf8339f7eb3bb2127dfa3f2666bd403ba9b50f3e0d7462778044dec12`). `services.py` changed only the guard/`ensure` hunks. |
| C10 no new secret materialization | verified-closed | `parameters_json` block byte-identical (`variant_slug`, `seed`, `seat0_model_id`, `seat1_model_id`, `prompt_id`, `assist_mode`). Correction diff has no token/key/credential writes. |
| Serializer create path | verified-closed | `RegisterSerializer` has no `validate_username`; register `201`; new user flag `False`; ordinary PATCH username still `200` |

**New finding record**

Finding ID: APMC-S4-IA-F07  
Title: Editing already-applied `game/0009` dependency strands existing databases  
Status: confirmed  
Severity: high  
Confidence: high  
Evidence class: reproduced-dynamic  
Affected commit: `6049f2895321da33c7594aedd922aef63544e18d`  
Affected component and exact location: `backend/game/migrations/0009_diagnostic_session_foundation.py:48` (`("accounts", "0005_service_account_flag")` added to an already-applied migration); Django 5.2.17 `migrate.handle` → `check_consistent_history`  
Security property: the F02 flag must be deployable onto existing `0009` databases by one normal `migrate` without data-rescue  
Asset at risk: operator migrate/run loop; entire `User` ORM; product create/queue once HEAD is checked out  
Trust boundary: developer/operator schema application  
Attacker-controlled input or local actor: local-actor `manage.py migrate` after pulling `6049f28` onto a DB that already recorded `game.0009` (the Cooperator’s documented shape)  
Reachability: default post-pull migrate; reproduced on a throwaway SQLite copy of that history  
Preconditions: `game.0009` in `django_migrations`; `accounts.0005` not applied; disk `0009` now depends on `0005`  
Required privileges: local  
Observed or potential impact: every `migrate` form aborts; `0005` never applies; `accounts_user.is_service_account` is absent; any `User` queryset raises `OperationalError`. Belt-and-braces username equality is unreachable because the SELECT lists the missing column. This is not a one-command recovery.  
C/I/A effect: demonstrated availability loss of migrate and of the running app against existing `0009` DBs. No confidentiality compromise. The F02 authz closure cannot be installed on those DBs until a multi-step rescue.  
CWE mapping: none assigned  
ASVS mapping: none assigned  
Source-standard references: Django 5.2.17 (Django Software Foundation, shipped), `django.db.migrations.exceptions.InconsistentMigrationHistory` / `MigrationLoader.check_consistent_history`; retrieval 2026-09-06 from the installed venv  
Dynamic reproduction evidence: temp tree archived at `f6c9db9`, migrated through `0009`, HEAD files overlaid; `showmigrations` rc 0; `migrate` / `migrate accounts 0005` / `migrate --plan` rc 1 with the quoted exception; ORM `OperationalError` on `is_service_account`  
Static evidence: `0009` dependency line; Django `migrate.py:117` runs the history check before any plan  
Synthetic containment: `/tmp/apmc-s4-reaudit2` (declared before use; removed after evidence capture)  
False-positive analysis: `showmigrations` quiet is not recovery. Restricting the command to `accounts 0005` still hits the global check. A fresh empty DB is a different path (V-ORD-a) and does not rescue the Cooperator’s existing DB.  
Exploitability conclusion: demonstrated (availability / deployability), not an unauthenticated remote exploit  
Smallest safe correction direction: stop depending an already-applied `game/0009` on a new `accounts` migration; keep `0005` as an accounts-only AddField that existing DBs can apply, and put any fresh-DB ordering / re-flag `ensure` on a **new** unapplied `game` migration. Do not invent a data-rescue in this audit.  
Regression-test requirement: throwaway DB with `0009` applied and `0005` absent in history must reach a consistent schema by one normal `migrate`, then the seeded row must be flagged (or flagged on next `ensure` without breaking other User queries)  
Residual risk: even a successful later AddField defaults existing rows to `False`; the managed row needs an `ensure`/data step so the flag is actually `True` on pre-seeded accounts  
Acceptance-blocking decision: blocking; the operator story required by this re-audit is false, and pulling the F02 fix breaks existing `0009` databases  
Redaction requirements: never publish real bearers, signing keys, or credential-file contents

**Tests and validation — gate summaries, verbatim**

```text
Success: no issues found in 90 source files
All checks passed!
872 passed, 4 skipped in 540.79s (0:09:00)
```

Documented mypy command, never narrowed. Plain `-m pytest`, no second `-q`. No `npm run build`. Independent probes (in-memory test DB, synthetic JWTs never printed): VF02A–E, VF01, VF03, C3, C6, register create-path — all passed after a harness assertion-order fix on VF03 (product behaviour was already keep-claimant / delete-managed on the first run’s prints).

**Containment ledger**

Declared root: `/tmp/apmc-s4-reaudit2` (mode `0755`, owner this audit). Contents class: git archives of `f6c9db9` and `6049f28`, throwaway SQLite files, independent pytest file, migrate logs. No repo writes. Cleanup: `rm -rf /tmp/apmc-s4-reaudit2` → `CLEANUP_OK`. Filesystem permission mode of nested trees: default umask. Process-local pytest DBs: transaction rollback/process exit. Network: none. Credential files: `backend/.env` present: yes; `frontend/.env.local` present: yes — not read, not printed. Synthetic `DJANGO_SECRET_KEY` used only in the throwaway trees.

**Limitations**

SQLite / in-process HTTP only; production PostgreSQL collation and the Cooperator’s live `db.sqlite3` were not opened. No live provider spend. Admin rename was exercised via ORM `user.save()` plus `UserAdmin.get_fieldsets`, not a full Admin POST of every contrib field. F04/F05/F06 not reopened.

**Residual-risk summary (for slice-4 acceptance)**

On any database that has already applied `game.0009`, the F02 flag mechanism is not installable by `migrate`, and checking out `6049f28` makes `User` queries fail until a multi-step rescue. That is worse, for the operator, than the JWT-rename bypass it fixed. On a migrated schema the flag **does** close the demonstrated P09 chain, F01/F03 did not regress, and the product API cannot assign the flag. Belt-and-braces username equality is a second semantics (namespace lock), not a second setter for the managed principal. Slice-4 acceptance is the ORCHESTRATOR’s decision on this evidence.

**Compact closeout**

- Phase-qualified result: `not-applicable`
- Start/end commit: both `6049f2895321da33c7594aedd922aef63544e18d`
- Changed files: none
- Commit/push result: not-applicable
- Deviations, risks, missing evidence: F07 as above; repository gate matched (HEAD, AP pin `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`, porcelain empty at start and end)
- Smallest next step: ORCHESTRATOR issues a bounded correction that can apply `is_service_account` on already-`0009` databases without editing the applied `0009` dependency line (new unapplied `game` migration if fresh-DB ordering still needs a graph edge)
- Report justification: `new-material-risk`
- Authority expiry: this Worker’s task authority expires upon this report. Slice-4 acceptance remains the ORCHESTRATOR’s decision. No closure signal.

Resolved Execution Issues / Near-Misses: independent VF03 first assertion ran after a username-delete that removed the claimant row the probe itself had just preserved; prints already showed keep/delete. Harness assertion moved; re-run passed. Cursor AppImage env required `env -u APPIMAGE -u ARGV0 -u APPDIR` for `.venv/bin/python`.

Pre-Existing Failure Classification: none for gates. New F07 is introduced by correction-2’s dependency edit, not a pre-existing test failure.

Orchestration critique: **MEASURED:** the flag is a sound identity boundary for the managed principal on a migrated schema; the username OR-branch is a second, still-live semantics (namespace lock) that will diverge after an admin rename and must not be treated as the same predicate. The session-10 grant treated `showmigrations` quiet as existing-DB success; Django’s history check makes `migrate` refuse, so the Cooperator’s actual recovery is not one command and the running app is broken until rescued. **LEAD:** do not add dependencies onto already-applied migrations; put the fresh-DB ordering edge on a new unapplied `game` revision.

Enumeration widened: Admin fieldsets (flag omitted, username present); `PATCH` extra-field ignore for the flag; case-variant ordinary participation; username-branch occupant with flag `False`; User ORM `OperationalError` on the stranded DB (not only `migrate`).