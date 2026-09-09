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
