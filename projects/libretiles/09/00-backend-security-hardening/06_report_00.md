Implementácia single-use je hotová a v izolácii prechádza; plný pytest padá, lebo dva existujúce migračné testy vracajú `game` na `0006` a tým zmažú `0007`. To je mimo allowlistu — commit/push nespúšťam a eskalujem.

### Report for ORCHESTRATOR_CHAT

Logical whole identity: backend-security-hardening  
Worker session ordinal: 06  
Worker exchange ordinal: 01

**Status:** BLOCKED  
**Phase-qualified result:** Implementation BLOCKED (non-independent). The replay correction is present in the working tree and passes in isolation; the standing full-suite gate is red for a reason outside the path allowlist. This Worker does not certify the correction and did not commit or push.  
**Escalation disposition: NEEDS_ORCHESTRATOR_DECISION**

**Start commit:** `04fe823ac2eea6c8398dd9f00830d30d71568e97`  
**End commit:** unchanged (`04fe823ac2eea6c8398dd9f00830d30d71568e97`); no corrective commit

### Changed paths (uncommitted; allowlist only)

| Path | Purpose |
|---|---|
| `backend/game/models.py` | `ConsumedWsTicket`: SHA-256 hex unique `ticket_hash`, `expires_at`, `consumed_at`; never stores the ticket string |
| `backend/game/migrations/0007_consumedwsticket.py` | One auto-named migration creating `game_consumed_ws_ticket` |
| `backend/game/services.py` | Runtime TTL, per-issue nonce, DB consume via unique insert, bounded cleanup |
| `backend/config/settings.py` | `GAME_WS_TICKET_MAX_AGE_SECONDS` default `"60"` → `"10"` |
| `backend/tests/test_ws_ticket_single_use.py` | New regression file (tests 1–11) |

```text
git diff --stat (tracked):
 backend/config/settings.py |  2 +-
 backend/game/models.py     | 18 ++++++++++++++++
 backend/game/services.py   | 54 ++++++++++++++++++++++++++++++++++++++++------
 3 files changed, 67 insertions(+), 7 deletions(-)

git diff --name-only (tracked vs HEAD):
backend/config/settings.py
backend/game/models.py
backend/game/services.py

git status --porcelain=v1:
 M backend/config/settings.py
 M backend/game/models.py
 M backend/game/services.py
?? backend/game/migrations/0007_consumedwsticket.py
?? backend/tests/test_ws_ticket_single_use.py
```

`frontend/**` and `backend/game/consumers.py` are untouched. `backend/db.sqlite3` is gitignored (`gitignore:24:*.sqlite3`) and is not in porcelain.

### Repository and pre-push gate evidence

At start and still now:

```text
git rev-parse HEAD                      04fe823ac2eea6c8398dd9f00830d30d71568e97
git rev-parse HEAD:.ap                  9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD               9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git status -sb                          ## main...origin/main
git ls-remote origin refs/heads/main    04fe823ac2eea6c8398dd9f00830d30d71568e97
```

Start porcelain was empty. Current porcelain is the uncommitted correction candidate. Pre-push gate was **not** exercised: no commit, no push.

### Capability handshake

- Requested reasoning: High (prompt). Observed: this session’s model is Cursor Grok 4.6; reasoning depth is inferred, not independently attested.
- Declared route `poetry run ...` is unusable (Cursor AppImage intercepts `python*` via inherited `APPIMAGE`/`PYTHONHOME`).
- Authorized bounded deviation used from `backend/`: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` and `.venv/bin/ruff`. Ambient `python`/`python3`/`poetry run` were not used as a parallel route.

### Tests 1–11 before/after (isolated file; never printed a ticket)

Pre-fix command: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_ws_ticket_single_use.py -v --tb=line`  
Pre-fix summary: `3 failed, 8 passed in 2.13s`

| # | Test | Pre-fix | Isolated post-fix |
|---|---|---|---|
| 1 | fresh ticket verifies once | PASSED | PASSED |
| 2 | same ticket string twice fails | FAILED (`assert False is True`) — demonstrated finding | PASSED |
| 3 | ticket for game A rejected for game B | PASSED | PASSED |
| 4 | non-participant rejected | PASSED | PASSED |
| 5 | expired ticket rejected (time patched, no sleep) | PASSED | PASSED |
| 6 | two different tickets, same user+game, each once | PASSED | PASSED |
| 7 | HTTP ticket → connect → disconnect → new HTTP ticket → connect | PASSED | PASSED |
| 8 | consumed row does not contain raw ticket | FAILED (`ConsumedWsTicket` absent) | PASSED |
| 9 | cleanup removes expired, keeps unexpired | FAILED (`ConsumedWsTicket` absent) | PASSED |
| 10 | `GameWSTicketView` 200 participant / 404 outsider | PASSED | PASSED |
| 11 | full websocket connect with fresh ticket | PASSED | PASSED |

Isolated post-fix with existing WS tests: `tests/test_ws_ticket_single_use.py tests/test_multiplayer_ws.py` → `14 passed`.

### Applied migration and makemigrations check

- `manage.py migrate` applied **`game.0007_consumedwsticket`** to the existing development database (`Applying game.0007_consumedwsticket... OK`). The table was not dropped or rebuilt.
- `manage.py makemigrations --check --dry-run` → `No changes detected`

Development DB still has `0007` applied. If this working tree is discarded, unapply with `migrate game 0006` **before** deleting the migration file.

### TTL

Default **10 seconds**, still overridable via `GAME_WS_TICKET_MAX_AGE_SECONDS`. The client fetches the ticket over HTTP and opens the WebSocket in the same turn (`getWSTicket` then `new WebSocket(...)` on waiting and game pages). Ten seconds covers slow devices and scheduling delay; sixty seconds was a wide replay window for a value that is used immediately. `expires_in` in the HTTP body follows the live setting. `.env.example` and README still document `60` (not in allowlist).

Services now read the setting at call time (no import-time freeze) so the configured value is actually used.

### Single-use mechanism (not per-process)

1. `verify_ws_ticket` still: `signing.loads` with salt + `max_age`, payload `game_id` must match, then `_load_session_for_user` membership re-check.
2. Only after those checks: SHA-256 (UTF-8) of the **ticket string** is inserted into `game_consumed_ws_ticket.ticket_hash` (`unique=True`). The raw ticket is never stored.
3. `IntegrityError` on that unique constraint is treated as replay → `GameNotFoundError` (consumer still closes 4403). Insert runs inside `transaction.atomic()` so PostgreSQL integrity failures do not poison an outer transaction.
4. This is a **database unique constraint**, visible to every worker sharing the DB. It does not use Django’s cache (currently LocMemCache / per-process).

Each `build_ws_ticket` also signs a `nonce` (`uuid.uuid4().hex`). Django `TimestampSigner` is deterministic within the same integer second for the same payload; without a nonce, two fetches in one second would be the same string and single-use would look like “one connection per game forever.” That is why tests 6 and 7 exist. Binding fields remain `game_id` and `user_id`; nonce is not an authorization input.

### Cleanup

`cleanup_consumed_ws_tickets(limit=100)` deletes rows with `expires_at < now`, capped at 100 IDs per call. `expires_at` is `timezone.now() + TTL` at consume time, so a hash outlives remaining signature validity. Called from **both** `build_ws_ticket` and `verify_ws_ticket`. The function is safe to call from a later management command. No scheduled job, no Redis.

### Bindings unchanged

Ticket-to-user, ticket-to-game, and the `_load_session_for_user` membership re-check are unchanged and still run **before** consume. Tests 3, 4, and 10 lock that.

### Residual of audit-01-F09

**Query-string transport REMAINS.** `consumers.py` `connect()` is unchanged. Browsers cannot set headers on the WebSocket handshake; moving the ticket out of the query string is the tracked residual part of audit-01-F09 and needs a later slice with frontend + handshake authority. This Worker did not change `frontend/**`.

### Standing gates

```text
mypy config game gamecore accounts catalog
Success: no issues found in 79 source files

ruff check .
All checks passed!

manage.py makemigrations --check --dry-run
No changes detected

pytest (full suite, verbatim summary):
4 failed, 294 passed, 4 skipped in 138.37s (0:02:18)
```

Start-commit baseline was `287 passed, 4 skipped`. Isolated new tests add 11. Full-suite failures (all `no such table: game_consumed_ws_ticket`):

- `tests/test_multiplayer_ws.py::test_waiting_player_receives_match_found_event`
- `tests/test_multiplayer_ws.py::test_chat_and_game_state_events_are_user_specific`
- `tests/test_ws_ticket_single_use.py::test_reconnect_fetches_new_http_ticket_and_connects_again`
- `tests/test_ws_ticket_single_use.py::test_websocket_connect_succeeds_end_to_end_with_fresh_ticket`

`test_invalid_ticket_is_rejected` still passes because `consumers.py` swallows any `Exception` as close 4403.

Reproduction: those four tests pass when run alone with the new migration applied; they fail if run **after** either:

- `tests/test_creditless_migration.py` `FreshCreditlessSchemaTests.test_cleanup_migrations_are_irreversible` `finally`: `call_command("migrate", "game", "0006_rename_consecutive_scoreless_turns", ...)`
- `tests/test_scoreless_turns_migration.py` `finally`: `executor.migrate(self.migrate_to)` where `migrate_to` is game `0006`

Both restore **game HEAD to 0006**, which **unapplies `0007`** and drops `game_consumed_ws_ticket`. That was correct when 0006 was HEAD. It is not correct once this slice’s required migration exists. Updating those restore targets (to `0007_consumedwsticket` or unbounded `migrate game` / leaf nodes) is the smallest honest suite fix. Those two test files are **outside the allowlist**. This Worker did not edit them, did not weaken them, and did not paper over the missing table in `services.py` (that would silently disable single-use after those tests).

### Authorized Git result

Not performed. Standing pytest is not green. Public readback: origin `main` remains `04fe823ac2eea6c8398dd9f00830d30d71568e97`.

### Deviations, risks, missing evidence

- Full-suite pytest red for the HEAD-pin reason above. Commit/push stopped.
- Working tree is dirty with the allowlisted candidate. A later `fresh-worker-session` repository gate will fail until this is committed, restored, or explicitly continued as `current-worker-session`.
- Human-vs-human multiplayer was **not** exercised manually in a browser. Tests 6, 7, and 11 are synthetic harness coverage only.
- No live provider call. `LIBRETILES_AI_PLAY_LIVE` unset. No `.env` / `.env.local` read. No ticket/token/secret printed.
- Query-string ticket remains capturable within the TTL; residual of audit-01-F09.
- This correction is non-independent. Fresh independent re-audit (INFOSEC.md 4.11, P-10) is still mandatory after a green commit; this Worker must not perform it.

### Out-of-scope observations (not findings)

- `backend/.env.example` and README still show `GAME_WS_TICKET_MAX_AGE_SECONDS` default `60`.
- `test_creditless_migration.py` catalog restore is pinned to `0012_multi_provider_free_rivals`; not touched.
- audit-01-F13, orch-01-F20, orch-01-F18, throttles, and cache backend were not touched.

### Smallest next step

Orchestrator expands the allowlist by **two restore-to-current-HEAD lines** (not new product behavior):

1. `backend/tests/test_creditless_migration.py` — `finally` migrate `game` to current HEAD (`0007_consumedwsticket` or `migrate game` with no target), not `0006`.
2. `backend/tests/test_scoreless_turns_migration.py` — `finally` migrate to current leaf / full game HEAD, not `0006`.

Then a **current-worker-session** (or a fresh Worker on this dirty tree with explicit dirty-tree authority) re-runs the standing pytest gate, makes the one authorized commit, pushes, and the Orchestrator routes the mandatory fresh independent re-audit. Do not route S6 (CSP / security headers) until this slice is committed and re-audited.

**Report justification:** new-evidence  
**Logical-whole closure:** not-closed  
**Authority expiry:** this exchange’s authority expires with this terminal report. Retained context is not a renewal.

**Resolved Execution Issues / Near-Misses:** AppImage `python*` intercept classified; used the prompt’s bounded `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/...` route. Full-suite `no such table` classified as existing tests pinning game HEAD to `0006`, not as a defect in the unique-constraint mechanism; did not catch `OperationalError` to fake green. Residual risk: dirty tree + `0007` applied on the development DB until the expanded-allowlist follow-up or an authorized unapply.

**Pre-Existing Failure Classification:** `tests/test_creditless_migration.py` and `tests/test_scoreless_turns_migration.py` restore `game` to `0006` as if it were HEAD. That was valid at the start commit (0006 was HEAD). It becomes a suite-schema hazard for any later `game` migration. Not a product bug; not independent evidence against single-use. Exposed by the authorized `0007` migration.