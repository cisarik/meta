You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An approved plan grants you nothing; THIS prompt does.

```text
Logical whole identity: infosec-hardening-and-vps-readiness
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: IHR-SLICE-2-IMPL — implement Slice 2 dialect parity: postgresql CONN_MAX_AGE / CONN_HEALTH_CHECKS, sqlite3 docs alignment, and SQLite-default plus opt-in PostgreSQL dialect tests. Land one commit, push, and read back.
Phase: implementation
Exact baseline: a33433efe0abec263bc1008d7db46d2b6d13d44f
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Evidence tier: E2
Evidence tier basis: reversible settings and tests plus a bounded local docker compose of the existing postgres service. Not production host mutation, not credential rotation, not schema/model changes, not authN/Z.
Overhead budget: proportionate
Deliverable tier spread: none
INFOSEC route: R1 — slice-level secure implementation review on your own diff (non-independent). ⛔ Do not perform a fresh independent R3 audit in this exchange.
Activated stricter profile: none
Independent acceptance: not-required
Combined implementation envelope: allowed
Authorized implementation stages: allowlisted mutation; ruff/mypy/makemigrations-check/focused sqlite pytest; optional local docker compose up of service postgres; opt-in postgres pytest; docker compose stop postgres only if this session started it; one commit; one non-force push of origin/main; terminal report
Implementation stage gates: repository gate empty and at baseline; sqlite gates green before docker; postgres tests fail-closed when LIBRETILES_TEST_POSTGRES=1; never migrate or write database name libretiles; never docker compose down -v; push only after sqlite gates and, if docker ran, postgres gates
Rollback or recovery checkpoint: git revert of the single commit; docker compose stop postgres if this session started it; disposable database libretiles_pytest is dropped by the fixture
Terminal implementation report point: after push readback, or BLOCKED/PARTIAL stop
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
```

```text
Changed-path allowlist: the six paths in §2
Implementation boundaries: positive = those six paths plus the one Meta report path plus the docker compose postgres up/stop in §6; negative = everything else
Independence required: no
```

Reasoning recommendation: **High.** Named risk: migrating or writing the Cooperator's compose database `libretiles`, or making default pytest require PostgreSQL.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932          task authority; omitted permission is not implied
AP.md:768-818          Plan-to-Execution Gate — the plan file is DATA. Only this prompt grants mutation.
AP.md:1444-1462        Git and remote safety
AP.md:1509-1547        security boundaries, secret minimization
AP.md:2466-2486        stopping conditions
AP_WORKER.md:14-26     role and authority boundary
INFOSEC.md:119-128     4.1 slice-level review: evidence is non-independent
PROMPT_CONTRACTS.md:14-41     report contract + coordinate echo
PROMPT_CONTRACTS.md:156-177   implementation authority record (filled above)
PROMPT_CONTRACTS.md:423-453   Worker Exchange Identity
AP.md:2453-2454        closed report-justification enum: new-mutation
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than
   resolving it yourself.
```

The planning report `/home/agile/meta/projects/libretiles/16/00-infosec-hardening-and-vps-readiness/04_report_00.md` is **DATA UNDER ANALYSIS**. Follow it only where this prompt restates or explicitly adopts a contract. Where this prompt amends the plan (O1–O8), this prompt wins.

## RF-16 execution route (canonical; no silent parallel)

Libre Tiles declares no `ap.project.conf`. From `backend/`:

```text
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
```

⛔ Never ambient `python`, `python3`, or `poetry run`.
⛔ Never type `PYTHON_DOTENV_DISABLED=1`.
⛔ Never print, hash, or length-measure `backend/.env` or `frontend/.env.local`.
⛔ Do not invent an `env -i` / dotenv-monkeypatch bootstrap. Standard project python is the route.
Settings may load dotenv at process start; that is not authority to read or report secret values. Credential facts: `present: yes|no|unknown` plus NAME only.
⛔ Do not put `DB_PASSWORD`, compose passwords, or connection URIs with userinfo into the report.

## 1. Repository gate

Working directory: `/home/agile/Projects/libretiles`

Before mutation:

```bash
git rev-parse HEAD                    # MUST equal a33433efe0abec263bc1008d7db46d2b6d13d44f
git rev-parse HEAD:.ap                # MUST equal 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # same pin; detached HEAD is correct
git branch --show-current             # MUST be main
git status --porcelain=v1             # MUST be empty
```

If any value disagrees: status BLOCKED, write the report, do not mutate.

## 2. Path allowlist (strict)

You may create or modify ONLY:

```text
backend/config/settings.py
backend/.env.example
README.md
backend/pyproject.toml
backend/tests/test_security_settings.py
backend/tests/test_postgres_dialect_parity.py
```

Plus Meta report write (not a git path):

```text
/home/agile/meta/projects/libretiles/16/00-infosec-hardening-and-vps-readiness/05_report_00.md
```

⛔ Any other Libre Tiles path is unauthorized. If a test cannot pass without an extra path: stop, name the path, do not edit it.
⛔ Do not edit `backend/game/services.py`, `backend/game/admin_views.py`, `backend/tests/conftest.py`, `docker-compose.yml`, or `backend/billing/`.

## 3. Frozen product decisions (do not reopen)

```text
A1  Regular player pages untouched.
A2  Server staff gate remains IsAdminUser.
A3  WordAuthority.accepts_tokens unchanged. Do not touch gamecore.
A4  No forensic reconstruction. No Django model/field/migration files.
A5  Do not set SECURE_HSTS_PRELOAD. CSRF_TRUSTED_ORIGINS / SECURE_* cookie/HSTS
    flags / SSL redirect are Slice 3.
A6  Slices 3–5 out of scope (headers/throttles, VPS, Next.js standalone).
A7  Fast default pytest stays SQLite and must not require PostgreSQL.
A8  IHR-S1-F01 accepted-residual. Do not reopen.
A9  Staff B GET / creator-only mutate unchanged.
A10 Leave backend/billing/ untouched.
A11 Do not read backend/.env.
```

Orchestrator amendments vs the planning report:

```text
O1  NEVER migrate, CREATE TABLE, INSERT, or otherwise write the database named
    `libretiles`. Opt-in tests use a disposable database named exactly
    `libretiles_pytest`, created and dropped by the fixture. Compose service
    remains the existing `postgres:16-alpine` in docker-compose.yml.
O2  Parse `DB_CONN_HEALTH_CHECKS` with existing `_env_flag(..., default=True)`
    on the postgresql branch only. Do not invent a second boolean parser.
O3  mypy stays `config game gamecore accounts catalog`. Do not add `tests`.
O4  Do not mock `connection.vendor` through `join_matchmaking` (or any other
    full service). The plan's `else: select_for_update()` branch does not exist:
    the queryset already calls `select_for_update()`, then re-applies
    `skip_locked=True` only when vendor is postgresql.
O5  Docker grant (Cooperator A): `docker compose up -d postgres` from the repo
    root, and `docker compose stop postgres` ONLY if this session started that
    service. ⛔ No `down`, ⛔ no `-v`, ⛔ no Redis service, ⛔ no other compose
    services, ⛔ no sudo.
O6  PostgreSQL UUID proof uses the same Cast+Replace annotate on
    `GameSession.objects.using("postgres_test")`. Do not point APIClient at the
    secondary alias.
O7  IntegrityError tests must use a transaction-aware wrapper
    (`TransactionTestCase` or `django_db(transaction=True)`) so SQLite does not
    swallow the error inside TestCase atomic.
O8  Settings probes extend `_PROBE_SOURCE` / `_run_settings_probe`. A
    postgresql-engine probe still needs a valid secret and, when DEBUG is false,
    a redis:// throttle URL — same as existing probes. Probe JSON may include
    ENGINE and CONN_* keys; never PASSWORD, USER, or NAME.
```

## 4. Implementation contracts

### 4.1 PostgreSQL connection persistence (`backend/config/settings.py`)

Only inside `if _DB_ENGINE == "postgresql":`:

- `CONN_MAX_AGE`: int from `DB_CONN_MAX_AGE`, default `"600"`. Unset → 600. Empty/whitespace, non-integer, or negative → `ImproperlyConfigured` (same fail-closed style as `DJANGO_NUM_PROXIES`). `0` is allowed (disable persistence).
- `CONN_HEALTH_CHECKS`: `_env_flag("DB_CONN_HEALTH_CHECKS", default=True)`.
- Widen the `DATABASES` value type so mypy accepts `int` / `bool` (prefer `str | Path | int | bool`, not a blanket `Any`).

SQLite branch stays exactly as today (no CONN_* keys).

### 4.2 Docs

`backend/.env.example`: commented `DB_CONN_MAX_AGE` and `DB_CONN_HEALTH_CHECKS` next to the existing DB block. Do not uncomment live secrets. Do not change `DB_ENGINE='sqlite3'`.

`README.md`: the Environment Variables table currently claims `DB_ENGINE` default `sqlite` and values `sqlite or postgresql`. Correct default and values to `sqlite3` / `sqlite3 or postgresql` so they match settings and `.env.example`. Do not rewrite the Docker section except if it literally repeats the wrong default.

### 4.3 Pytest marker

In `backend/pyproject.toml` `[tool.pytest.ini_options].markers`, add:

```text
postgres: tests requiring a running PostgreSQL database
```

Keep existing `internet` and `slow` markers.

## 5. Tests

### 5.1 `backend/tests/test_security_settings.py`

Extend the isolated subprocess probe. Add an explicit extra-env passthrough; do not inherit the parent process `DB_*` variables.

Probe JSON: `status`, plus on `ok` the default DATABASES `ENGINE`, `CONN_MAX_AGE` (missing key → JSON `null`), `CONN_HEALTH_CHECKS` (missing → JSON `null`). Never emit credentials.

Required:

```text
test_settings_probe_postgresql_persistence_keys
  DB_ENGINE=postgresql, valid secret, DEBUG=false, allowed hosts, redis URL
  → ok; ENGINE is django.db.backends.postgresql; CONN_MAX_AGE 600;
    CONN_HEALTH_CHECKS true.

test_settings_probe_sqlite_omits_persistence_keys
  default / DB_ENGINE=sqlite3
  → ok; sqlite3 ENGINE; CONN_MAX_AGE null or 0; CONN_HEALTH_CHECKS null or false.

test_settings_probe_invalid_conn_max_age_fails
  DB_ENGINE=postgresql and DB_CONN_MAX_AGE=not-an-int
  → improperly_configured.

test_settings_probe_negative_conn_max_age_fails
  DB_CONN_MAX_AGE=-1 → improperly_configured.

test_settings_probe_conn_max_age_zero_allowed
  DB_CONN_MAX_AGE=0 → ok; CONN_MAX_AGE 0.

test_settings_probe_health_checks_false
  DB_CONN_HEALTH_CHECKS=false → ok; CONN_HEALTH_CHECKS false.
```

### 5.2 `backend/tests/test_postgres_dialect_parity.py` (create)

Default pytest (no env): SQLite tests run; postgres-marked tests SKIP with a message naming `LIBRETILES_TEST_POSTGRES=1`. They must not fail merely because Postgres is absent.

When `LIBRETILES_TEST_POSTGRES=1`: postgres-marked tests run and FAIL-CLOSED on connect/migrate failure. Never skip in that mode.

Alias name: `postgres_test`. Database name: `libretiles_pytest` (constant; ignore `DB_NAME` for the disposable database). Host/port/user/password for the server: getenv with the same public defaults as `docker-compose.yml` / `.env.example` (`localhost`, `5432`, `libretiles`). Do not read `.env`.

Fixture (postgres-marked tests only):

1. Connect to the maintenance database `postgres` (not `libretiles`).
2. `DROP DATABASE IF EXISTS libretiles_pytest` then `CREATE DATABASE libretiles_pytest`.
3. Register alias `postgres_test` with ENGINE postgresql, NAME `libretiles_pytest`, CONN_MAX_AGE 600, CONN_HEALTH_CHECKS True, plus Django's required connection keys.
4. `call_command("migrate", database="postgres_test", verbosity=0, interactive=False)`.
5. Yield.
6. Close connections to that alias; `DROP DATABASE IF EXISTS libretiles_pytest`.

If `libretiles` appears as NAME in any migrate/create/write you did: that is a defect — stop and report.

SQLite (always, not postgres-marked):

```text
test_uuid_search_hyphenated_and_compact_sqlite
  Staff GET /api/admin/games/?search= with compact hex prefix AND with a
  hyphenated UUID prefix of the same session. Both return that game.
  Follow existing admin list test setup; do not duplicate the whole replay suite.

test_jsonfield_complex_structure_roundtrip_sqlite
  PlaygroundSimulation.config_json with nested dict/list, ints, floats, bools,
  JSON null, and Slovak tokens Á Č Ť. Re-read; deep equality.

test_unique_unfinished_playground_simulation_sqlite
  Second unfinished (ended_at=None) for the same created_by → IntegrityError.
  Different user allowed. After setting ended_at, same user may create another.
  Transaction-aware (O7).

test_skip_locked_only_under_postgresql_vendor_guard
  Static read of backend/game/services.py (do not import-and-mock join_matchmaking).
  Assert skip_locked=True occurs only inside a `connection.vendor == "postgresql"`
  guard. Do not execute matchmaking.
```

PostgreSQL (`@pytest.mark.postgres`, using alias `postgres_test`):

```text
test_postgres_migrate_zero_to_head
  migrate in the fixture is the proof; assert django_migrations contains the
  leaf names for accounts, catalog, and game (0005 / 0014 / 0014).

test_postgres_uuid_search_compact_and_hyphenated
  Create GameSession on the alias. Annotate Cast+Replace exactly as
  admin_views.AdminGameListView (O6). Compact hex and hyphenated prefixes match.

test_postgres_jsonfield_roundtrip_jsonb
  Same payload as the sqlite JSON test, on the alias.

test_postgres_unique_unfinished_playground_simulation
  Same IntegrityError matrix as sqlite, on the alias.

test_postgres_select_for_update_skip_locked
  Two connections to postgres_test. Connection A: atomic select_for_update()
  on a waiting vs_human GameSession and hold the lock. Connection B: same
  filter with select_for_update(skip_locked=True) must return without waiting
  (empty or other rows only — not the locked row). Put a short
  statement_timeout on B so a blocking lock fails the test instead of hanging.
  Do not sleep in a retry loop.

test_postgres_connection_health_probe
  connections["postgres_test"].is_usable() is True after migrate.
```

Do not start Redis. Do not call providers. Do not expand to `unique_inflight_diagnostic_run` unless it falls out of migrate-to-head (it should already apply).

## 6. Docker (Cooperator A) and verification

From repo root `/home/agile/Projects/libretiles`:

1. If `docker compose exec -T postgres pg_isready -U libretiles` already succeeds, **do not** start or later stop the service (Cooperator-owned instance).
2. Else:

```bash
docker compose up -d postgres
```

You may wait on `pg_isready` (bounded retries, no infinite loop). Pulling `postgres:16-alpine` is permitted if the image is absent. No other images.

3. After postgres opt-in pytest: if **this session** started the service:

```bash
docker compose stop postgres
```

⛔ `docker compose down`, ⛔ `-v`, ⛔ `rm`, ⛔ Redis, ⛔ other services.

If the docker daemon is unavailable: do not fake a skip. Finish sqlite gates if green, write PARTIAL, do not claim postgres migrate. You may still commit and push sqlite+settings work if sqlite gates pass; classify PARTIAL.

### Verification (after mutation, before commit)

From `backend/`:

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py makemigrations --check --dry-run
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest \
  tests/test_security_settings.py \
  tests/test_postgres_dialect_parity.py \
  tests/test_creditless_migration.py \
  -q
```

Quote the pytest summary line and wall-clock. Default run must skip postgres-marked tests, not fail them.

Then, with Postgres reachable:

```bash
LIBRETILES_TEST_POSTGRES=1 env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest \
  tests/test_postgres_dialect_parity.py -m postgres -v
```

Focused sqlite set should stay well under 30s. If it exceeds 30s, classify pre-existing vs introduced.

⛔ `npm run build`, `npm install`, `poetry add`, `pip install`.
⛔ No live provider. Network: git remotes + local Docker daemon (and Hub only for `postgres:16-alpine` if missing).

R1 inline review on YOUR diff: assets, trust boundaries, attacker inputs, secrets/logging, which database names were touched. Label it non-independent.

## 7. Git — one commit, explicit paths, one fast-forward push

Stage ONLY allowlisted repository paths (skip any you did not touch; never `git add .`):

```bash
git add \
  backend/config/settings.py \
  backend/.env.example \
  README.md \
  backend/pyproject.toml \
  backend/tests/test_security_settings.py \
  backend/tests/test_postgres_dialect_parity.py
git diff --staged --stat
```

Commit:

```bash
git commit -m "$(cat <<'EOF'
fix(db): persist PostgreSQL connections and prove dialect parity

Add CONN_MAX_AGE/CONN_HEALTH_CHECKS on the postgresql engine only, align the
sqlite3 docs default, and add SQLite plus opt-in PostgreSQL tests for
migrations, UUID search, JSONField, and partial unique constraints.
EOF
)"
```

Network authority: **Git remotes** plus the Docker grant in §6. No other network.

```bash
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "a33433efe0abec263bc1008d7db46d2b6d13d44f"
git push origin main
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "$(git rev-parse HEAD)"
```

If origin/main != baseline at pre-push: stop, do not push, classify recovery, write the report.

⛔ No `git add -A`, no force push, no amend, no `--no-verify`, no config writes.

## 8. Side-effect authority

```text
Libre Tiles: mutation of the six allowlisted paths; one commit; one non-force push of main.
Docker: compose up -d postgres if not already ready; compose stop postgres only if this session started it.
PostgreSQL: create/drop/migrate ONLY database libretiles_pytest on localhost compose defaults.
Meta: write 05_report_00.md only, atomically (temp + rename). ⛔ No other Meta path. ⛔ No Meta commit.
Secrets: none. ⛔ Do not read .env files.
Providers: none.
Hosts / sudo / systemd / UFW: none.
```

## 9. Stopping conditions

Stop, do not improvise, write the report if:

- Repository gate fails or the tree is dirty before you start.
- A required change needs a path outside the allowlist.
- A gate fails and cannot be fixed inside the allowlist.
- Secrets would be printed or committed.
- You wrote to database `libretiles`.
- origin/main diverged before push.
- This prompt and AP disagree.
- You complete acceptance below.

## 10. Acceptance (implementation-PASS)

All of:

1. PostgreSQL `DATABASES` branch has CONN_MAX_AGE default 600 and CONN_HEALTH_CHECKS default True; SQLite branch unchanged.
2. Invalid/negative `DB_CONN_MAX_AGE` fail closed; `0` and health-checks false load.
3. README / `.env.example` agree with `sqlite3`.
4. Default pytest skips `@pytest.mark.postgres` tests; does not require Postgres.
5. SQLite tests in §5.2 pass, including hyphenated UUID search and unfinished-simulation IntegrityError.
6. With `LIBRETILES_TEST_POSTGRES=1`, migrate-to-head on `libretiles_pytest` plus UUID/JSON/unique/skip_locked/is_usable tests pass.
7. No allowlisted file writes database name `libretiles` as the test target.
8. Diff ⊆ allowlist.
9. Public SHA of `origin/main` equals local HEAD after push.

If docker was unavailable: PARTIAL, not implementation-PASS, even if you pushed settings+sqlite tests.

## 11. Report contract

Write the complete terminal report atomically to:

`/home/agile/meta/projects/libretiles/16/00-infosec-hardening-and-vps-readiness/05_report_00.md`

The file MUST begin exactly `### Report for ORCHESTRATOR_CHAT`.
**Report language: English.**

Echo unchanged:

```text
Logical whole identity: infosec-hardening-and-vps-readiness
Worker session ordinal: 05, Worker exchange ordinal: 01
```

Compact core:

```text
status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS | not-applicable
  (implementation-PASS only if §10 holds)
Start commit: a33433efe0abec263bc1008d7db46d2b6d13d44f
End commit: <SHA or same if BLOCKED with zero mutation>
Changed files and purpose
Tests and validation: summaries; full output only on failures
Commit/push result
Docker: already-running | started-and-stopped | unavailable | not-attempted
PostgreSQL database names touched: <list; must not include libretiles as a write target>
Deviations, risks, missing evidence
One smallest next step
Report justification: new-mutation
Authority expiry: this implementation grant expires at the report
Logical-whole closure: not-closed
Resolved Execution Issues / Near-Misses: none | …
Pre-Existing Failure Classification: none | …
```

Analytical fields:

```text
Orchestration critique: none | <MEASURED and LEAD lists about this PROMPT/APPROACH/GOAL>
Enumeration widened: none | <paths or cases this prompt missed>
R1 slice review: non-independent; findings or none
```

Chat concluding message: 3 lines — status, report path, HEAD SHA. The Orchestrator reads the file. The Cooperator is not a courier.

Do not quote entire green pytest logs. Do not close the logical whole.
