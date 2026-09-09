### Report for ORCHESTRATOR_CHAT

Logical whole identity: infosec-hardening-and-vps-readiness
Worker session ordinal: 04, Worker exchange ordinal: 01

```text
status: PASS
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: not-applicable
Logical-whole closure: not-closed
Changed files and purpose: none — this exchange mutates no Libre Tiles file; meta report write is the authorized side effect
Commit/push result: not-applicable
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
```

```text
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

---

## D1 — Migration and App Inventory (Landed vs Missing)

The database schema and migration inventory was evaluated against `INSTALLED_APPS` in `backend/config/settings.py`, the filesystem under `backend/*/migrations/`, and test suites.

| Artifact / Range | Evidence | Status | Notes |
|---|---|---|---|
| `accounts` migrations (`0001`–`0005`) | `backend/accounts/migrations/*.py` | `landed-tested` (SQLite) / `landed-untested` (Postgres) | 5 migrations (`0001_initial` through `0005_service_account_flag`). Fully applied and exercised on SQLite. Never tested on PostgreSQL in automated test runs. |
| `catalog` migrations (`0001`–`0014`) | `backend/catalog/migrations/*.py` | `landed-tested` (SQLite) / `landed-untested` (Postgres) | 14 migrations (`0001_initial` through `0014_strategic_seeded_prompts`). Includes data migrations for seeded prompts, catalog selection, and money removal. Fully exercised on SQLite; untested on PostgreSQL. |
| `game` migrations (`0001`–`0014`) | `backend/game/migrations/*.py` | `landed-tested` (SQLite) / `landed-untested` (Postgres) | 14 migrations (`0001_initial` through `0014_playground_simulation`). Contains table reorganizations, partial unique constraints, and diagnostic target models. Tested on SQLite; untested on PostgreSQL. |
| `billing` migrations (`0001`–`0002`) | `backend/billing/migrations/0001_initial.py`, `0002_precise_usd_balances.py` | `orphan` | `billing` is NOT in `INSTALLED_APPS`. Models, views, and services were deleted in 15/00 (`game.0005_remove_money_state`). The directory contains only `__init__.py` and the two obsolete migration files. |
| Built-in / Third-party migrations (`admin`, `auth`, `contenttypes`, `sessions`, `token_blacklist`, `axes`) | `INSTALLED_APPS` | `landed-tested` (SQLite) / `landed-untested` (Postgres) | Standard upstream migrations; apply without issue on SQLite. |
| SQLite-only SQL operations | `backend/*/migrations/*.py` | `landed-tested` (None found) | A codebase-wide regex search for `RunSQL`, `PRAGMA`, and `sqlite_sequence` in migrations returned zero matches. `game.0005_remove_money_state` executes `DROP TABLE IF EXISTS ...`, which is standard SQL supported by both engines. |
| `manage.py migrate` on PostgreSQL | `backend/tests/` | `landed-untested` | Zero automated tests currently run `manage.py migrate` against PostgreSQL. All existing migration tests (`test_creditless_migration.py`, `test_openrouter_catalog_migration.py`, `test_diagnostic_session.py`, etc.) execute against SQLite. |

---

## D2 — UUID / JSON Dialect Surfaces

### 1. Live `Cast` and `Replace` Query Paths
Codebase-wide search confirmed exactly one live `Cast` / `Replace` query path in the application:
- **Location:** `backend/game/admin_views.py:101-106` in `AdminGameListView`:
  ```python
  compact = search.replace("-", "")
  if re.fullmatch(r"[0-9a-fA-F]+", compact):
      queryset = queryset.annotate(
          public_id_text=Replace(
              Cast("public_id", output_field=CharField()), Value("-"), Value("")
          )
      )
      predicate |= Q(public_id_text__istartswith=compact)
  ```
- **Dialect Analysis:**
  - `GameSession.public_id` is a `models.UUIDField(default=uuid.uuid4, unique=True)`.
  - **SQLite:** `UUIDField` is stored as `char(32)` hex (no hyphens). `Cast("public_id", output_field=CharField())` returns the 32 hex characters. `Replace(..., Value("-"), Value(""))` is a harmless no-op, preserving the 32 hex characters.
  - **PostgreSQL:** `UUIDField` is stored as native `uuid`. `Cast("public_id", output_field=CharField())` casts `uuid` to text, yielding 36 characters with hyphens (`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`). `Replace(..., Value("-"), Value(""))` strips the hyphens, yielding the exact 32 hex characters.
  - In both engines, `public_id_text` evaluates to the 32 hex characters without hyphens, matching `compact = search.replace("-", "")`.
- **Existing Coverage & Gap:**
  - `test_admin_replay_api.py:94-97` tests searching with a 10-character hex prefix (`str(first.public_id).replace("-", "")[:10]`), but does not test searching with a hyphenated string (e.g. `str(first.public_id)[:14]`).
  - Test needed: verify prefix search succeeds with both compact hex and hyphenated search inputs on both SQLite and PostgreSQL.

### 2. JSONField and Handout §5.1 Claims
- **Falsification:** Handout §5.1 claimed `KeyTextTransform` was used in `backend/game/analytics_expressions.py`.
- **Finding:** Completely falsified.
  - `backend/game/analytics_expressions.py` contains only 20 lines with 3 numeric helper functions: `nonnegative_number`, `average`, `rounded`.
  - A full codebase search for `KeyTextTransform` returned zero matches.
  - `backend/game/analytics.py` queries `PlaygroundSimulation` and `Move` records using `.values("game_id", "config_json")` and `.values("player_slot_id", "ai_metadata")`, then extracts values using standard Python dictionary `.get()` lookups. No ORM JSON path expressions or database-level JSON transforms are used in queries.
  - The only JSONField ORM filter in the repository is `Move.objects.exclude(ai_metadata__isnull=True)` in `backend/game/admin.py:221`.
- **Dialect Parity for JSONField:**
  - On SQLite: stored as `text` with a `CHECK ((JSON_VALID("column") OR "column" IS NULL))` constraint.
  - On PostgreSQL: stored as native `jsonb`.
  - Test needed: round-trip serialization and deserialization of nested objects (strings with Unicode, integers, floats, booleans, lists, dicts, nulls) on `PlaygroundSimulation.config_json` on both SQLite and PostgreSQL to ensure no lossy conversion occurs.

---

## D3 — Connection Persistence (PostgreSQL Engine Only)

### 1. Settings Design
In `backend/config/settings.py`, inside the `if _DB_ENGINE == "postgresql":` branch:
- Add `CONN_MAX_AGE`: integer representing maximum connection lifetime in seconds. Default to `600` (10 minutes), overridable via environment variable `DB_CONN_MAX_AGE`.
- Add `CONN_HEALTH_CHECKS`: boolean determining whether Django tests connection liveness before reusing an existing connection. Default to `True`, overridable via environment variable `DB_CONN_HEALTH_CHECKS`.
- Update `DATABASES` type annotation on line 180 from `dict[str, dict[str, str | Path]]` to `dict[str, dict[str, Any]]` (or `dict[str, dict[str, str | Path | int | bool]]`) so `mypy` strict type checking succeeds.

```python
if _DB_ENGINE == "postgresql":
    _conn_max_age_raw = os.getenv("DB_CONN_MAX_AGE", "600")
    try:
        _conn_max_age = int(_conn_max_age_raw)
    except ValueError:
        raise ImproperlyConfigured(f"DB_CONN_MAX_AGE must be an integer, got {_conn_max_age_raw!r}")
    _conn_health_checks = os.getenv("DB_CONN_HEALTH_CHECKS", "true").lower() in ("true", "1", "yes")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME", "libretiles"),
            "USER": os.getenv("DB_USER", "libretiles"),
            "PASSWORD": os.getenv("DB_PASSWORD", "libretiles"),
            "HOST": os.getenv("DB_HOST", "localhost"),
            "PORT": os.getenv("DB_PORT", "5432"),
            "CONN_MAX_AGE": _conn_max_age,
            "CONN_HEALTH_CHECKS": _conn_health_checks,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
```

### 2. SQLite Exemption
The SQLite branch explicitly retains Django defaults (`CONN_MAX_AGE=0`, no `CONN_HEALTH_CHECKS`).
- **Concrete Defect on SQLite:** SQLite is a single-file, process/thread-isolated embedded database. Enabling persistent connections across HTTP requests causes file locking contention (`sqlite3.OperationalError: database is locked`) during concurrent ASGI / Channels requests and concurrent test worker executions.

### 3. Documentation Alignment
- `backend/.env.example`: Add commented documentation:
  ```bash
  # DB_CONN_MAX_AGE='600'
  # DB_CONN_HEALTH_CHECKS='true'
  ```
- `README.md`: Line 108 table currently states:
  `| DB_ENGINE | sqlite | sqlite or postgresql |`
  This is a `stale-docs` mismatch: `settings.py` line 179 defaults to `"sqlite3"`, and `.env.example` line 37 specifies `DB_ENGINE='sqlite3'`.
  README.md line 108 must be corrected to:
  `| DB_ENGINE | sqlite3 | sqlite3 or postgresql |`

### 4. Settings Subprocess Probes
Extend `backend/tests/test_security_settings.py` (reusing the isolated subprocess probe pattern without modifying `.env`):
- Probe with synthetic `DB_ENGINE="postgresql"`: asserts `CONN_MAX_AGE == 600` and `CONN_HEALTH_CHECKS is True`.
- Probe with default / `DB_ENGINE="sqlite3"`: asserts `CONN_MAX_AGE` is not present (or 0) and `CONN_HEALTH_CHECKS` is not present (or False).
- Probe with malformed `DB_CONN_MAX_AGE="not-an-int"`: asserts `ImproperlyConfigured` is raised fail-closed.

---

## D4 — Other Dialect-Sensitive ORM

### 1. Partial Unique Constraints
1. **`unique_unfinished_playground_simulation`** (`game/models.py:113-117`):
   ```python
   UniqueConstraint(
       fields=["created_by"],
       condition=Q(ended_at__isnull=True),
       name="unique_unfinished_playground_simulation",
   )
   ```
   - **Engine behavior:** SQLite (3.8.0+) and PostgreSQL both support partial indexes: `CREATE UNIQUE INDEX "unique_unfinished_playground_simulation" ON "game_playground_simulation" ("created_by_id") WHERE "ended_at" IS NULL`.
   - **Current coverage:** Untested. No test verifies that attempting to create a second simulation with `ended_at=None` for the same user raises `IntegrityError`.
2. **`unique_inflight_diagnostic_run`** (`game/models.py:455-459`):
   ```python
   UniqueConstraint(
       Value(1),
       condition=Q(status__in=["queued", "running"]),
       name="unique_inflight_diagnostic_run",
   )
   ```
   - **Engine behavior:** PostgreSQL and SQLite both support expressions in partial indexes (`ON ... ((1)) WHERE status IN (...)`).
3. **`unique_diagnostic_ply_index`** (`game/models.py:526`): Standard composite unique constraint on `(run_id, ply_index)`. Supported uniformly.

### 2. `select_for_update(skip_locked=True)`
- **Location:** `backend/game/services.py:2015-2018`:
  ```python
  if connection.vendor == "postgresql":
      waiting_queryset = waiting_queryset.select_for_update(skip_locked=True)
  else:
      waiting_queryset = waiting_queryset.select_for_update()
  ```
- **Analysis:**
  - SQLite does not support `SKIP LOCKED` or row-level locking. Calling `select_for_update(skip_locked=True)` on SQLite raises `django.db.NotSupportedError`.
  - PostgreSQL natively supports `SELECT ... FOR UPDATE SKIP LOCKED` for concurrent worker queue claims.
  - The codebase already correctly gates `skip_locked=True` behind `connection.vendor == "postgresql"`.
  - **Constraints:**
    - ⛔ Do NOT change skip_locked semantics on PostgreSQL.
    - ⛔ Do NOT enable skip_locked on SQLite.
  - Unit test: verify branch dispatch on SQLite (mock/patch vendor to `"postgresql"` and `"sqlite"` to confirm proper parameter passing).
  - Postgres opt-in test: execute an actual transaction with `select_for_update(skip_locked=True)` on live PostgreSQL 16 to confirm query execution and lock release.

---

## D5 — How Postgres Verification Runs Without Poisoning Default Pytest

### 1. Constraints and Core Design
- **Fast Default Pytest (A7):** Default `pytest` must remain on SQLite, take <30s, and NEVER fail or skip because PostgreSQL is absent or stopped.
- **Opt-in Gate:** Controlled via environment variable `LIBRETILES_TEST_POSTGRES=1`.
- **Pytest Marker:** Register `postgres` in `backend/pyproject.toml` under `[tool.pytest.ini_options].markers`:
  ```toml
  markers = [
      "internet: tests requiring live API calls",
      "slow: deterministic extended acceptance tests",
      "postgres: tests requiring a running PostgreSQL database",
  ]
  ```

### 2. Skip vs. Fail-Closed Contract
- **When `LIBRETILES_TEST_POSTGRES` is UNSET or `"0"`:**
  Any test marked `@pytest.mark.postgres` is SKIPPED with message:
  `"PostgreSQL opt-in tests disabled. Set LIBRETILES_TEST_POSTGRES=1 to enable."`
  Default `pytest` passes cleanly on SQLite.
- **When `LIBRETILES_TEST_POSTGRES=1` IS SET:**
  The test harness connects to PostgreSQL using connection settings (`DB_HOST` default `localhost`, `DB_PORT` default `5432`, `DB_NAME` default `libretiles`, `DB_USER` default `libretiles`, `DB_PASSWORD` default `libretiles`, matching `docker-compose.yml` and `.env.example`).
  If the connection cannot be established or the host/port is unreachable:
  The test **FAILS-CLOSED** (`pytest.fail(f"PostgreSQL connection failed despite LIBRETILES_TEST_POSTGRES=1: {exc}")`). It must never silently skip when explicitly requested.

### 3. Execution Strategy: Dynamic Connection Alias
To allow Postgres verification without having to switch the entire test suite backend (which would slow down all 900+ tests and require rebuilding SQLite-specific test fixtures), the Postgres test harness configures a secondary database alias `postgres_test` in `django.db.connections.databases`:
1. Dynamically registers `postgres_test` with PostgreSQL engine, connection parameters, `CONN_MAX_AGE=600`, and `CONN_HEALTH_CHECKS=True`.
2. Calls `call_command("migrate", database="postgres_test", verbosity=0)`:
   - Migrates all apps (`accounts`, `catalog`, `game`, `auth`, `admin`, `contenttypes`, `sessions`, `token_blacklist`, `axes`) from 0 to head.
   - Proves migration capability on PostgreSQL 16.
3. Performs targeted dialect parity operations against `postgres_test`:
   - UUID search with hyphens and compact hex.
   - JSONField round-trip.
   - Partial unique constraint enforcement.
   - `select_for_update(skip_locked=True)` query.
   - Connection health probe verification.
4. Cleans up test records created in `postgres_test`.

### 4. Docker Authority Boundary
- **Planning Session:** ZERO Docker authority. No container was started, stopped, or inspected.
- **Implementation Session (Session 05):** Flagged as **Cooperator-owned**:
  - The Cooperator decides whether Session 05 is granted host authority to execute `docker compose up -d postgres` (and `docker compose stop postgres` upon completion).
  - If granted: Session 05 starts the container, executes `LIBRETILES_TEST_POSTGRES=1 pytest -m postgres`, verifies PASS, and stops the container.
  - If not granted: Session 05 verifies all SQLite tests and settings probes pass, leaving the opt-in Postgres command for Cooperator execution.

---

## D6 — Test Matrix

All new dialect parity tests will be consolidated in a single backend test module: `backend/tests/test_postgres_dialect_parity.py`, supplemented by isolated settings probe tests in `backend/tests/test_security_settings.py`.

| Test Name | File | Backend / Mode | Assertion / Coverage |
|---|---|---|---|
| `test_settings_probe_postgresql_persistence_keys` | `test_security_settings.py` | Subprocess probe (`DB_ENGINE=postgresql`) | Asserts `CONN_MAX_AGE == 600` and `CONN_HEALTH_CHECKS is True` in isolated settings load. |
| `test_settings_probe_sqlite_omits_persistence_keys` | `test_security_settings.py` | Subprocess probe (`DB_ENGINE=sqlite3` / unset) | Asserts `CONN_MAX_AGE` is 0 or absent, and `CONN_HEALTH_CHECKS` is False or absent on SQLite. |
| `test_settings_probe_invalid_conn_max_age_fails` | `test_security_settings.py` | Subprocess probe (`DB_CONN_MAX_AGE=invalid`) | Asserts `ImproperlyConfigured` is raised fail-closed on invalid integer string. |
| `test_uuid_search_compact_and_hyphenated_sqlite` | `test_postgres_dialect_parity.py` | SQLite default | Creates `GameSession`. Queries `AdminGameListView` search with compact hex (32-char prefix) and hyphenated UUID prefix (e.g. 14 chars with hyphens). Asserts both return the session. |
| `test_jsonfield_complex_structure_roundtrip_sqlite` | `test_postgres_dialect_parity.py` | SQLite default | Creates `PlaygroundSimulation` with nested dict, list of ints/floats/bools, Slovak unicode tokens (`"Á"`, `"Č"`, `"Ť"`), and nulls in `config_json`. Re-reads from DB; asserts deep equality. |
| `test_unique_unfinished_playground_simulation_sqlite` | `test_postgres_dialect_parity.py` | SQLite default | Creates first unfinished simulation (`ended_at=None`) for User A -> succeeds. Second unfinished for User A -> raises `IntegrityError`. Unfinished for User B -> succeeds. Sets `ended_at` on User A's first simulation -> creating new unfinished for User A succeeds. |
| `test_select_for_update_vendor_branch_sqlite` | `test_postgres_dialect_parity.py` | SQLite default | Asserts that `services.join_matchmaking` calls `select_for_update()` without `skip_locked` when `connection.vendor == "sqlite"`, and passes `skip_locked=True` when vendor is `"postgresql"`. |
| `test_postgres_migrate_zero_to_head` | `test_postgres_dialect_parity.py` | Postgres opt-in (`@pytest.mark.postgres`) | Calls `call_command("migrate", database="postgres_test")`. Asserts all migrations across all installed apps apply without error. |
| `test_postgres_uuid_search_compact_and_hyphenated` | `test_postgres_dialect_parity.py` | Postgres opt-in (`@pytest.mark.postgres`) | Creates `GameSession` in PostgreSQL. Executes `Cast` + `Replace` hyphen-stripping query with both compact hex and hyphenated search strings. Asserts match on native `uuid` column. |
| `test_postgres_jsonfield_roundtrip_jsonb` | `test_postgres_dialect_parity.py` | Postgres opt-in (`@pytest.mark.postgres`) | Saves complex nested JSON in `PlaygroundSimulation.config_json` in PostgreSQL. Re-fetches; asserts full equality under PostgreSQL native `jsonb`. |
| `test_postgres_unique_unfinished_playground_simulation` | `test_postgres_dialect_parity.py` | Postgres opt-in (`@pytest.mark.postgres`) | Verifies that PostgreSQL enforces the partial unique index on `game_playground_simulation` (`IntegrityError` on second unfinished; allowed when ended). |
| `test_postgres_select_for_update_skip_locked` | `test_postgres_dialect_parity.py` | Postgres opt-in (`@pytest.mark.postgres`) | Executes an atomic block on PostgreSQL invoking `select_for_update(skip_locked=True)`. Asserts query succeeds and lock releases cleanly. |
| `test_postgres_connection_health_probe` | `test_postgres_dialect_parity.py` | Postgres opt-in (`@pytest.mark.postgres`) | Verifies `connection.is_usable()` returns `True` and connection persists across transactions on PostgreSQL with `CONN_HEALTH_CHECKS=True`. |

---

## D7 — Path Allowlist and Verification Commands

### 1. Path Allowlist (for later Implementation Session)
- `backend/config/settings.py` (Add `CONN_MAX_AGE`, `CONN_HEALTH_CHECKS` to PostgreSQL `DATABASES` branch; update `DATABASES` type annotation).
- `backend/.env.example` (Document `DB_CONN_MAX_AGE` and `DB_CONN_HEALTH_CHECKS`).
- `README.md` (Update line 108 table to default `sqlite3`).
- `backend/pyproject.toml` (Register `postgres` marker in `[tool.pytest.ini_options].markers`).
- `backend/tests/test_security_settings.py` (Add isolated subprocess settings probes for database connection parameters).
- `backend/tests/test_postgres_dialect_parity.py` (New single test module containing SQLite default parity tests and opt-in PostgreSQL tests).

⛔ Explicitly Prohibited:
- No changes to `backend/billing/` (orphaned files left untouched).
- No changes to VPS scripts (`scripts/vps/*` is Slice 4).
- No production security header changes (`SECURE_*`, `CSRF_*` is Slice 3).
- No changes to frontend files.
- No changes to `docker-compose.yml`.

### 2. Verification Commands
From `backend/`:

1. **Static Analysis & Fast SQLite Suite (Default, <30s):**
   ```bash
   env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
   env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog tests
   env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_security_settings.py tests/test_postgres_dialect_parity.py
   ```

2. **Full Fast Pytest Gate (Fast SQLite, <30s):**
   ```bash
   env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest -m "not internet and not slow"
   ```

3. **Opt-in PostgreSQL Verification (Requires running Postgres):**
   ```bash
   LIBRETILES_TEST_POSTGRES=1 env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_postgres_dialect_parity.py -m postgres -v
   ```

---

## D8 — Implementation Grant Sketch

### 1. Ordered Implementation Steps
1. **Settings Update:** In `backend/config/settings.py`, configure `CONN_MAX_AGE` (default `600`) and `CONN_HEALTH_CHECKS` (default `True`) in the `postgresql` branch. Update `DATABASES` typing.
2. **Docs & Env Sync:** Add `DB_CONN_MAX_AGE` and `DB_CONN_HEALTH_CHECKS` to `backend/.env.example`. Correct `DB_ENGINE` default in `README.md` line 108 table to `sqlite3`.
3. **Marker Registration:** Add `postgres` marker definition to `backend/pyproject.toml`.
4. **Settings Probes:** Add subprocess probe tests to `backend/tests/test_security_settings.py` verifying PostgreSQL and SQLite connection configurations in isolation.
5. **Parity Test Module:** Implement `backend/tests/test_postgres_dialect_parity.py` containing:
   - SQLite parity tests (UUID search with/without hyphens, JSONField roundtrip, partial unique constraint, skip_locked vendor branch).
   - PostgreSQL opt-in tests guarded by `LIBRETILES_TEST_POSTGRES=1` and marked `@pytest.mark.postgres`.
6. **SQLite Gate Verification:** Run `ruff`, `mypy`, and default `pytest`. Ensure 100% pass under 30s.
7. **PostgreSQL Verification (Subject to Cooperator Docker Grant):** Start `postgres:16-alpine` via `docker compose up -d postgres`, execute opt-in Postgres tests, verify migrate-to-head and dialect parity, and tear down container.

### 2. Risk and Evidence Classification
- **Proposed Evidence Tier:** E2 (Reversible settings changes + comprehensive automated unit and integration tests).
- **INFOSEC Risk Routing:** R1 (Internal database dialect configuration and connection hardening; no authZ changes, no secret handling, no external network exposure).
- **Cooperator-Owned Decisions:**
  1. **Docker Execution Grant:** Whether implementation Worker (Session 05) is authorized to run `docker compose up -d postgres` and `docker compose stop postgres` on the host to verify PostgreSQL 16 live.
  2. **Leftover Billing Files:** Whether to retain `backend/billing/migrations/` as documented orphan artifacts or delete them in a subsequent housekeeping cut (Decision A10 currently designates deletion as Cooperator-owned; plan retains them untouched).
- **Deferred Items:**
  - **Slice 3:** Production security headers (`SECURE_HSTS_SECONDS`, `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`, `CSRF_TRUSTED_ORIGINS`, `SECURE_PROXY_SSL_HEADER`) and DRF throttle configurations.
  - **Slice 4:** VPS systemd service definitions, Caddy reverse-proxy configuration, deploy scripts.
  - **Slice 5:** Next.js standalone containerization.
- **Residual Risks:**
  - Docker daemon availability on the development host during Session 05. (Mitigated: fail-closed opt-in gate ensures default SQLite development is never impaired).

---

## Analytical Fields

### Orchestration Critique
- **MEASURED:**
  1. The prompt hypothesis H3 correctly suspected that handout §5.1 was stale regarding `analytics_expressions.py` and `KeyTextTransform`. Measurement verified 0 occurrences of `KeyTextTransform` in the repository and confirmed `analytics.py` relies strictly on in-memory Python dictionary access.
  2. The prompt hypothesis H6 correctly anticipated that `services.py:2015-2018` already branches on `connection.vendor == "postgresql"` for `select_for_update(skip_locked=True)`.
  3. The prompt hypothesis H10 correctly identified the documentation discrepancy where `README.md` line 108 claimed `DB_ENGINE` defaults to `sqlite`, while `settings.py` line 179 and `.env.example` line 37 use `sqlite3`.
- **LEAD:**
  1. Handout §5.1's assertion that complex database-level JSON expressions existed in analytics had the potential to derail planning into inventing nonexistent ORM transforms; ground-truth inspection prevented this distraction.
  2. The prompt noted `pytest` markers currently lack a `postgres` marker. Registering this marker in `pyproject.toml` prevents `PytestUnknownMarkWarning` and ensures clean filtering.

### Enumeration Widened
1. **Inspected all `UniqueConstraint` declarations:** Found `unique_inflight_diagnostic_run` on `Value(1)` in `game/models.py:455-459` and `unique_diagnostic_ply_index` in `game/models.py:526` in addition to `unique_unfinished_playground_simulation`. Both SQLite and PostgreSQL generate valid partial/unique indexes for these models.
2. **Examined installed `psycopg` environment:** Confirmed that `psycopg 3.3.3` with binary extras is already installed and fully importable in `backend/.venv`, ensuring `django.db.backends.postgresql` is ready for immediate live execution without package additions.
3. **Verified table dropping in `game.0005`:** Inspected `game/migrations/0005_remove_money_state.py` line 28 to confirm that `schema_editor.execute("DROP TABLE IF EXISTS ...")` uses SQL syntax that is valid in both SQLite and PostgreSQL.

---

Report justification: new-evidence

This concludes the Implementation-Planning exchange for Slice 2 (IHR-SLICE-2-PLAN). Planning authority expires at this report.

Smallest next step: Orchestrator presents the Cooperator decision on Docker execution authority for Session 05 and issues the Implementation prompt.

Context pressure: nominal (~25k tokens used, well within window limits).
