# Libre Tiles — Notes for logical whole `infosec-hardening-and-vps-readiness` (Meta 16/00)

Append-only notes ledger for logical whole 16/00.
Maintained by the Agent Orchestrator. Evidence and observation history; not task authority.

---

## §0 Whole 16 Boot and Baseline Record

Whole 16 initialized on 2026-09-08 following the successful closure of `admin-frontend-console` (15/00).
- Baseline commit: `a892f740f194af2492c3865a9a1ea6dcf18ed1a7`
- Pinned AP commit: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- Standing quality gates:
  * Backend: mypy clean (119 source files); ruff clean; makemigrations clean; focused pytest suites clean (< 15s).
  * Frontend: typecheck clean, lint clean, vitest 146 passed tests clean.
- Handout prompt established:
  `/home/agile/meta/projects/libretiles/16/00-infosec-hardening-and-vps-readiness/00_handout.md`
- Core mission:
  1. Comprehensive INFOSEC audit & hardening across newly added admin, simulation, and replay surfaces.
  2. Strict privilege escalation verification, token refresh mutex in `api.ts`, secret minimization, and parameter injection tests.
  3. PostgreSQL production parity, migration verification, and connection pooling.
  4. Production settings & security headers audit (`DEBUG=False`, HSTS, SSL, secure cookies, scoped throttles).
  5. VPS deployment scripts (`vps_deploy.sh`), Nginx reverse proxy template with TLS & websockets, Systemd service units, and comprehensive deployment guide (`docs/vps_deployment_guide.md`).
  6. Next.js standalone build optimization (`output: "standalone"`).
  7. Autonomous Worker Report Archiving (D-17): All workers write terminal reports directly to `meta/`.

---

## §1 Restoration verification — fresh Orchestrator, 2026-09-09

Handout grants no authority. Independent re-measurement of the Handout Integrity Record and of Slice 1 premises.

### 1.1 Repository gate (re-measured)

```text
HEAD            a892f740f194af2492c3865a9a1ea6dcf18ed1a7
origin/main     a892f740f194af2492c3865a9a1ea6dcf18ed1a7   (git ls-remote)
branch          main
porcelain       empty
AP gitlink      9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
.ap HEAD        9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Predecessor     15/00 closed-by-ORCHESTRATOR at the same SHA
                (99_closure.md)
```

### 1.2 Standing gates (re-measured this session)

```text
backend mypy     Success: no issues found in 119 source files
backend ruff     All checks passed
makemigrations    No changes detected
focused pytest    tests/test_admin_{replay,simulation,analytics}_api.py
                  + test_admin_login_brake.py  → 23 passed
                  (combined with makemigrations ~19s; pytest itself not timed alone)
frontend typecheck  clean
frontend lint       clean
vitest 146          NOT re-measured this session (D-13: known-stale-by-design until a later exchange)
```

Applies to: restoration attestation only. Not a claim about later mutated trees.

### 1.3 D-13 handout defects — Slice 1 premises that are already landed

The handout's Slice 1 list treats several items as work to implement. Independent search at the baseline shows they already exist. These are hypotheses the Slice 1 Planner must re-measure, not specifications:

```text
H1  Admin/simulation views already declare
    permission_classes = [IsAuthenticated, IsAdminUser]
    (admin_views.py, simulation_views.py).
H2  401 anonymous / 403 non-staff already asserted in
    test_admin_replay_api.py, test_admin_simulation_api.py,
    test_admin_analytics_api.py.
H3  UserSerializer already lists is_staff in read_only_fields.
    test_user_serializer_exposes_is_staff already PATCHes is_staff=False
    (must not stick) and rejects is_staff=True on register.
    ⚠ Escalation PATCH is_staff=True / is_superuser=True by a non-staff
      user was NOT found as a named test (absence claim; pattern was
      is_superuser and "is_staff": true under backend/tests).
H4  frontend/src/lib/api.ts already has a single-flight refreshPromise.
    No frontend unit test matching refreshPromise / refreshAccessToken
    was found.
H5  simulations.py already compares created_by_id on mutate/lease/stop.
    test_any_staff_can_read_but_only_creator_can_mutate asserts other
    staff GET → 200 and step/stop → 404 (not 403). Product choice, not
    an unimplemented check.
H6  Throttle scopes admin_simulation_create 10/hour and
    admin_simulation_step 120/minute already exist in settings.py and
    are bound on the views. Enforcement tests belong to Slice 3 unless
    the planner finds they are unbound.
H7  Production DEBUG=False default, secret-key strength, secure cookies,
    SSL redirect, HSTS includeSubDomains already exist. OUT OF SLICE 1.
H8  Handout §5.2 says SECURE_HSTS_PRELOAD = True. That CONTRADICTS
    Cooperator decision 5 (PROJECT_CONTEXT.md) and settings.py comment
    that PRELOAD is deliberately unset (accepted residual W021).
    Slice 3 must not silently reverse that decision.
H9  Handout §1 item 5 cites INFOSEC.md "SSRF (4.5)". Pin INFOSEC.md
    has no SSRF heading. 4.5 is File/Upload; 4.4 is authN/Z; 4.6 is AI
    boundary. SSRF work in this product lives in diagnostic_targets.py
    and diagnostic-target-fetch.ts plus diagnostic_ssrf_cases.json.
H10 frontend/next.config.ts has no output: "standalone". That is Slice 5.
H11 NEXT_PUBLIC_ hits in frontend/src are NEXT_PUBLIC_API_URL only
    (api.ts, proxy.ts, one test). Not an API-key leak by that prefix search.
```

Coordinate review of this section: re-measured against HEAD a892f74 on 2026-09-09. File:line citations from the predecessor handout were not copied.

### 1.4 Protocol posture for this whole

```text
D-01  every Worker prompt requires Orchestration critique MEASURED/LEAD
D-04  every inventory handed to a Worker is a hypothesis plus the command
D-14  terse Cooperator replies continue the selected scope (Whole 16 /
      Slice 1). They do not select Slice 2–5.
D-17  every Worker, including this Planner, writes
      01_report_00.md (etc.) directly under this directory
D-18  no forensic reconstruction of pre-replay games; 15/00 already purged
AP pin  do not upgrade
```

BRAINSTORMING.md §5 originally excepted the Planner from auto-write. The Cooperator-tagged handout requires every Worker prompt to grant the write. This whole follows the handout.

### 1.5 First exchange

Session 01 / exchange 01 — Slice 1 Planner (`01_planning_00.md`), native Plan mode required. Objective: gap-closing INFOSEC design for admin/simulation/auth surfaces, not a re-implementation of H1–H7.

---

## §2 Slice 1 planning report — claim review (2026-09-09)

Artifact: `01_report_00.md`. Status `PASS`, phase `not-applicable`, baseline unchanged. Planning authority expired.

### 2.1 Protocol notes (not blockers for implementation)

```text
Report language   Slovak. Worker reports are required English. Content is usable;
                  implementation Worker must report in English.
Delivery story    Report claims a Plan-mode write blocker then Cooperator chat
                  acceptance. File now exists on disk; D-17 is satisfied for
                  archival even if the path was late.
```

### 2.2 Orchestrator re-measurement of named defects (independent of the report)

```text
R1  step_playground_simulation does
    _simulation_queryset().select_for_update().get(game__public_id=game_id)
    with no UUID parse and no DoesNotExist → SimulationNotFoundError.
    simulation_views.service_error only maps SimulationNotFoundError /
    SimulationConflictError; other exceptions propagate. CLAIM ACCEPTED.
R2  replay._diagnostic_ply_payload deepcopy(ply.ai_trace) and
    deepcopy(ply.earlier_attempt_failures). CLAIM ACCEPTED as output
    behaviour. Exploitability remains synthetic (planner said so).
R3  api.ts refreshAccessToken on success calls setToken/setRefreshToken
    with no session identity check; on HTTP failure calls clearAuth.
    Logout/account-switch during in-flight refresh can restore or
    overwrite. CLAIM ACCEPTED as code path.
R4  serialize_simulation_state returns config: simulation.config_json
    wholesale. CLAIM ACCEPTED.
R5  admin-simulation-server.ts returns parsed backend JSON object as
    data with no field projection. CLAIM ACCEPTED.
R6  GET-any-staff / mutate-creator-only stays product-choice (A already
    accepted). 404 vs 403 stays.
```

### 2.3 Orchestrator amendments to the frozen plan (issued in 02_implementation_00.md)

```text
O1  Frontend tests are NOT stuffed into turn/route.test.ts. That one-file
    constraint was a planning-prompt defect (D-01). Refresh/session tests
    go in frontend/src/lib/api.test.ts (already imports useGameStore).
    Proxy tests stay in route.test.ts.
O2  Canonical verification is the project RF-16 route
    (env -u APPIMAGE … .venv/bin/python), not the planner's env -i
    dotenv-monkeypatch bootstrap. Never print .env. Never
    PYTHON_DOTENV_DISABLED=1.
O3  Independent R3 audit is a LATER exchange (D-16). This implementation
    is E3 + R1 inline review, non-independent.
O4  Persist version stays 6. authEpoch is not partialized.
```

No Cooperator product decision is open. `Pokracuj` continues Slice 1 → implementation grant.

---

## §3 Slice 1 implementation claim review — `02_report_00.md` (2026-09-09)

Worker: session 02 / exchange 01. Claim: `implementation-PASS` at `a33433efe0abec263bc1008d7db46d2b6d13d44f`.

### 3.1 Independent re-measurement

```text
HEAD            a33433efe0abec263bc1008d7db46d2b6d13d44f
origin/main     a33433efe0abec263bc1008d7db46d2b6d13d44f
parent          a892f740f194af2492c3865a9a1ea6dcf18ed1a7
porcelain       empty
AP pin          9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
diff paths      exactly the nine allowlisted files (+2363 −129)
pytest focused  129 passed, ~50s (over 30s guideline; Worker classified
                pre-existing 39s on the six older modules — not re-timed
                in isolation this pass, but the combined set is green)
vitest          3 files, 46 passed
```

Code contracts present at HEAD: `_parse_simulation_id`, step/stop/lease `DoesNotExist` → 404 with creator filter on mutate, `_project_simulation_config`, `_project_ai_trace` / `_project_earlier_attempt_failures`, `authEpoch` + `applyRefreshedAuth` (persist version still 6), `projectedSimulationError`, turn route uses `bearerTokenFromAuthorizationHeader`.

Deviation `applyRefreshedAuth` two-parameter form: accepted. Prompt §4.5 type was incoherent; plan D5 was coherent. Worker followed D5.

Worker `Orchestration critique: none` is thin — the signature mismatch belonged there as MEASURED. Not a product defect.

Worker next-step that bundles R3 with "advance to Slice 2" is rejected (D-14 / D-16). Slice 2 is not selected.

### 3.2 Ladder position

```text
Implementation mutation   landed, public, non-independent evidence
Final Slice 1 acceptance  NOT done — E3 requires fresh independent R3
Slice 2                   not selected
```

Next exchange: session 03 / exchange 01, Fresh Independent Audit, `03_audit_00.md`.

---

## §4 Independent R3 audit — `03_report_00.md` (2026-09-09)

Worker: session 03 / exchange 01. Claim: audit-task PASS, not-applicable phase result, zero blocking findings, HEAD unchanged.

Gate (Worker-measured; Orchestrator confirmed HEAD/origin/pin still `a33433e` / `9c5cc44` / porcelain empty at review time): accepted as consistent with §3.1.

RC1–RC10: Worker verdict `holds` with named tests. Orchestrator does not re-run the suite this pass (already green in §3.1). Treats RC table as independent evidence.

### 4.1 Finding IHR-S1-F01 — Orchestrator re-measurement

CONFIRMED established-static:

- `SimulationActionSerializer.validate` routes `place` through `ApplyAIMoveSerializer` (sanitizes) and `exchange` through `ExchangeSerializer` (sanitizes).
- `pass` is allowed to carry `ai_metadata` but is not passed through `AIPassSerializer` (the human AI-pass sanitizer in `game/serializers.py`).
- `_submit_pass_locked` stores `_stored_ai_metadata(...)` as given.
- Read paths still call `sanitize_ai_metadata` (`_move_payload`, replay).

Severity low, staff-creator-only write, no cross-principal leak established. Auditor recommended residual acceptance OR a one-serializer correction + re-audit.

### 4.2 What this audit does not select

Slice 2 is named in the Worker's next-step. D-14: that does not select Slice 2. F01 disposition is the open Cooperator/Orchestrator residual decision.

---

## §5 Slice 1 acceptance — Cooperator chose A (2026-09-09)

Cooperator reply `A` to the costed F01 choice. That selects residual acceptance of IHR-S1-F01. It does not select Slice 2.

```text
Residual-risk decision
  Finding ID: IHR-S1-F01
  Decision: accepted-residual
  Severity: low
  Approver: Cooperator (explicit A)
  Regression test: not-applicable — no correction in this whole yet
  Rationale: staff-creator write into own simulation only; all in-scope
    read paths already sanitize; no cross-principal leak established;
    correction-plus-re-audit cost is two Worker sessions for hygiene
    parity, not a blocking hole.
  Recorded in: this notes section
```

Slice 1 (`INFOSEC Audit & Hardening across Admin & Simulation Surfaces`) is **accepted** at commit `a33433efe0abec263bc1008d7db46d2b6d13d44f` with that residual.

```text
Logical-whole closure: not-closed
Required preceding Slice 1 results: satisfied (implementation + independent R3)
Cooperator-owned F01 decision: satisfied (A)
Active mutation: none
Slice 2: not selected — Selection Echo pending
```

---

## §6 Slice 2 selected — Cooperator `ano` (2026-09-09)

Cooperator reply `ano` to the Selection Echo for Slice 2. That continues the named slice; it does not select Slices 3–5 and does not reopen IHR-S1-F01.

```text
Selected slice: 2
Name: Database Dialect Parity & PostgreSQL Verification
Planner session: 04 / exchange 01
Exact baseline: a33433efe0abec263bc1008d7db46d2b6d13d44f
Native planning mode: required
Active mutation: none until a later implementation grant
```

Orchestrator reconnaissance at that SHA (hypothesis for the planner, D-13 — not spec):

- `DATABASES` has no `CONN_MAX_AGE` / `CONN_HEALTH_CHECKS`.
- `analytics_expressions.py` is number helpers only; no `KeyTextTransform`.
- `admin_views.py` does `Cast("public_id", CharField())` + hyphen `Replace` for hex search.
- Handout migration list omits leftover `billing/migrations/` (0001, 0002). `billing` is not in `INSTALLED_APPS`.
- No `*postgres*` test module. `skip_locked=True` is already vendor-gated in `services.py`.
- Repo-root `docker-compose.yml` already has `postgres:16-alpine`.
- README documents `DB_ENGINE` default as `sqlite`; `backend/.env.example` and settings default are `sqlite3`.

---

## §7 Slice 2 planner review — session 04 `04_report_00.md` (2026-09-09)

Planner status PASS, English, D-17 disk write. Planning authority expired. Plan is advisory.

Verified against tree at `a33433e` (claims, not copy-through):

| Claim | Verdict |
|---|---|
| No `KeyTextTransform` anywhere | holds |
| `analytics_expressions.py` is three numeric helpers | holds |
| UUID search is one Cast+Replace in `admin_views.py`; existing test is compact hex only | holds (`test_admin_replay_api.py`) |
| `CONN_MAX_AGE` / `CONN_HEALTH_CHECKS` absent | holds |
| README `sqlite` vs settings/`sqlite3` | holds |
| `billing` leftover, not in `INSTALLED_APPS` | holds (only `0001`/`0002`; no `__init__.py` on disk — planner overstated that file) |
| `unique_unfinished_playground_simulation` untested by IntegrityError | holds |
| `skip_locked` vendor-gated | holds in spirit; plan invented an `else: select_for_update()` branch. Actual code already calls `select_for_update()` then re-applies with `skip_locked=True` only when vendor is postgresql. |
| Fast default pytest must stay SQLite | accepted (A7) |
| E2 / R1 for implementation | accepted |
| Handout §5.1 stale | accepted |

Orchestrator constraints for the later implementation prompt (not a targeted planner revision):

1. Never `migrate` or write the compose database named `libretiles`. Dedicated disposable name `libretiles_pytest` (create/drop around the opt-in fixture). Cooperator local data stays untouched.
2. Reuse `_env_flag` for `DB_CONN_HEALTH_CHECKS`. Do not invent a second boolean parser.
3. Settings probes extend `_PROBE_SOURCE` / `_run_settings_probe`. A `DB_ENGINE=postgresql` probe must still satisfy existing fail-closed settings (secret, and Redis URL when DEBUG is false). No `PYTHON_DOTENV_DISABLED=1`.
4. `mypy` stays `config game gamecore accounts catalog` (AGENTS.md). Do not add `tests`.
5. Do not mock `connection.vendor` through the whole `join_matchmaking` path. Vendor-branch assertion must stay narrow.
6. `backend/billing/` stays untouched (A10). Billing deletion remains Cooperator-owned and is not this slice.

Open Cooperator decision (one): Docker grant for session 05 — `docker compose up -d postgres` / `docker compose stop postgres` only. No `down -v`. No Redis container required for this slice.

---

## §8 Slice 2 docker grant — Cooperator chose A (2026-09-09)

```text
Docker grant: yes
Allowed: docker compose up -d postgres (repo root); docker compose stop postgres
  only if session 05 started the service
Forbidden: down, -v, Redis service, sudo, migrate/write database name libretiles
Disposable test database: libretiles_pytest
Implementation session: 05 / exchange 01
Native planning mode: not-used
```

---

## §9 Slice 2 implementation review — session 05 `05_report_00.md` (2026-09-09)

Worker status PASS, `implementation-PASS`, English. Commit `15793bb08f132a1e86e20708d7fa88ae9156df6d` on `origin/main` (fast-forward from `a33433e`). Porcelain empty. Diff is exactly the six allowlisted paths.

Orchestrator re-ran default focused pytest: 43 passed, 6 skipped (postgres-marked). Did not re-run live Postgres.

Verified vs tree:

| Contract | Verdict |
|---|---|
| postgresql `CONN_MAX_AGE` default 600, fail-closed on non-int/negative; `0` allowed | holds |
| `CONN_HEALTH_CHECKS` via `_env_flag(..., default=True)` | holds |
| SQLite `DATABASES` has no CONN_* keys | holds |
| README / `.env.example` `sqlite3` | holds |
| Disposable DB constant `libretiles_pytest`; `DB_NAME` ignored | holds |
| Maintenance connect is `postgres`, not `libretiles` | holds |
| Probe JSON omits NAME/USER/PASSWORD; extra_env passthrough | holds |
| skip_locked static guard; live skip_locked via two connections | holds (raw SQL SKIP LOCKED + statement_timeout negative control) |
| Module-scoped create/migrate/drop instead of per-test | accepted bounded adaptation (Django 5.2 alias validation) |
| Docker started-and-stopped; no `down -v` | accepted as reported |

Pre-existing (not Slice 2, not Slice 3): `game.0008_atomic_token_state_schema.refuse_if_game_state_present` counts on the default alias (`model.objects.count()`), not `schema_editor.connection.alias`. Latent trap for `migrate --database=<other>`. Recorded residual; do not mix into headers/throttles.

```text
Slice 2: accepted
End commit: 15793bb08f132a1e86e20708d7fa88ae9156df6d
Independent R3: not-required (E2 / R1; no authN/Z)
IHR-S2-R01: 0008 default-alias guard — residual, out of this slice
Logical-whole closure: not-closed
Slice 3: not selected — Selection Echo pending
```

---

## §10 Slice 3 selected — Cooperator `ano` (2026-09-09)

Cooperator confirmed Selection Echo for Slice 3 and that the Orchestrator does **not** dispatch the Worker. Delivery is copy-paste of `06_planning_00.md` into a fresh session with native Plan mode ON. Report returns as `06_report_00.md`.

```text
Selected slice: 3
Name: Production Settings & Security Headers Hardening
Planner session: 06 / exchange 01
Exact baseline: 15793bb08f132a1e86e20708d7fa88ae9156df6d
Native planning mode: required
Dispatch: Cooperator-manual (Orchestrator does not start the Worker)
Active mutation: none until a later implementation grant
```

Orchestrator reconnaissance (hypothesis for the planner, D-13):

- HTTPS flags (Secure cookies, SSL redirect, HSTS seconds + includeSubDomains, NOSNIFF, XFO) already landed and probed; PRELOAD deliberately unset (W021 asserted).
- `CSRF_TRUSTED_ORIGINS` and `SECURE_PROXY_SSL_HEADER` absent from the tree.
- Simulation create/step/action have throttle scopes; state GET and stop POST do not; admin list/replay/analytics have none.
- `admin_simulation_*` rates exist; no 429 test found for them.
- Handout §5.2 `SECURE_HSTS_PRELOAD = True` is stale (A5).

---

## §11 Slice 3 planner review — session 06 `06_report_00.md` (2026-09-09)

Planner status PASS, English, D-17 disk write. Planning authority expired. Plan is advisory. Cooperator-owned decisions: none.

Verified against tree at `15793bb`:

| Claim | Verdict |
|---|---|
| HTTPS cookies / SSL redirect / HSTS seconds+includeSubDomains / NOSNIFF / XFO landed-tested | holds |
| HSTS preload accepted-residual; W021 asserted | holds |
| `CSRF_TRUSTED_ORIGINS` and `SECURE_PROXY_SSL_HEADER` absent | holds |
| create/step/action scoped; state/stop/admin GET unbound | holds |
| No `admin_simulation` 429 tests today | holds |
| `SimpleRateThrottle.THROTTLE_RATES` is class-body from `api_settings` | holds (`throttling.py`) |
| Env-gated proxy header (default off) | accepted (spoofing on unproxied process) |
| Unbound GET/stop/admin as product-choice | accepted |
| E2 / R1 (R2-shaped origin parse, no independent R3) | accepted |

Orchestrator amendments for session 07 (not a targeted planner revision): O1 reject userinfo/query/fragment; O2 must patch THROTTLE_RATES; O3 no view-file edits; O4 3-request staff 429s; O5 exemption is `throttle_scope is None`, not a flood.

```text
Slice 3 plan: accepted with O1–O8
Implementation session: 07 / exchange 01
Native planning mode: not-used
Dispatch: Cooperator-manual
```


