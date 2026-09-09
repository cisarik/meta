### Report for ORCHESTRATOR_CHAT

Logical whole identity: infosec-hardening-and-vps-readiness
Worker session ordinal: 12, Worker exchange ordinal: 01

## Compact core

```text
status: PASS
Phase-qualified result: not-applicable
  (this is an independent milestone audit; "PASS" records audit completion
  with full evidence and zero acceptance-blocking vulnerabilities — it is NOT
  an implementation verdict and does not certify the tree)
Start commit: 33ffa150fa520118e67a6670422fe7fae1c98741
End commit: 33ffa150fa520118e67a6670422fe7fae1c98741
Changed files and purpose: none — Libre Tiles repository is strictly read-only;
  Meta writes authorized and delivered:
  - /home/agile/meta/projects/libretiles/16/00-infosec-hardening-and-vps-readiness/12_report_00.md
  - /home/agile/meta/projects/libretiles/17/00-public-docs-and-stale-truth/00_handout.md
  - /home/agile/meta/projects/libretiles/17/00-public-docs-and-stale-truth/00_notes.md
Commit/push result: not-applicable
Logical-whole closure: not-closed
Report justification: new-evidence
Authority expiry: this audit grant expires at the report
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
```

---

## Security Audit Report

```text
Security task class: broad milestone application audit (INFOSEC route R4,
  specializations 4.3 broad milestone, 4.4 authN/Z, 4.6 secret-containment &
  output projection, 4.7 manifest search without new dependency install)
Owned/authorized target: local checkout /home/agile/Projects/libretiles and public
  GitHub ref refs/heads/main of cisarik/libretiles (read-only audit grant)
Commit under audit: 33ffa150fa520118e67a6670422fe7fae1c98741
```

### Independence Statement

All evidence below was independently measured in this session directly from the repository tree, the public GitHub ref, and test runs. The whole-16 closure record (`99_closure.md`), Orchestrator notes, planner reports, and slice reports were analyzed as CLAIMS to verify or refute. No implementer or Orchestrator verdict was inherited as proof.

### Repository / Public Gate (Measured)

```text
git rev-parse HEAD                    = 33ffa150fa520118e67a6670422fe7fae1c98741  (MATCH)
git rev-parse HEAD:.ap                = 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656  (MATCH)
git merge-base --is-ancestor a892f74… = true (ancestry confirmed)
git status --porcelain=v1             = empty (clean worktree)
git diff --name-only a892f74…HEAD     = 25 files changed (+4489, -136 across 5 commits)
git ls-remote origin refs/heads/main  = 33ffa150fa520118e67a6670422fe7fae1c98741  (MATCH)
```

The gate passed completely. Local HEAD and public `origin/main` are identical at the named closed whole commit.

### Scope & Selection Rationale

Selected and inspected:
1. Whole-16 lineage `a892f74..33ffa15` (5 commits: `a33433e`, `15793bb`, `7ffe0dc`, `2e034d8`, `33ffa15`).
2. Authentication, session, and privilege enforcement surfaces (`backend/accounts/views.py`, `serializers.py`, `backend/game/admin_views.py`, `simulation_views.py`, `simulations.py`, `replay.py`, `frontend/src/lib/api.ts`, `frontend/src/hooks/useGameStore.ts`, `frontend/src/app/api/admin/simulate/[id]/turn/route.ts`).
3. Database and settings configuration (`backend/config/settings.py`, `backend/.env.example`, `backend/pyproject.toml`).
4. Production deployment templates and scripts (`backend/scripts/nginx/libretiles.conf`, `backend/scripts/systemd/libretiles-*.service`, `backend/scripts/vps_*.sh`, `docs/vps_deployment_guide.md`).
5. Public documentation surfaces (`README.md`, `AGENTS.md`, `docs/architecture.md`, `CONTRIBUTING.md`, `libretiles_PRD.md`).

Exclusions honoured:
- Rendered UI/UX polish and mobile/tablet pinch-zoom (parked per Cooperator intent).
- Live host SSH, UFW mutation, TLS certbot issuance, or live systemd startup (INFOSEC R5 deferred).
- AP submodule upgrade (pinned at `9c5cc44`).
- Commercial integrations (Stripe, LM Studio, Vercel AI Gateway).
- AI provider unfreezing (nine providers frozen pending dedicated whole).
- WordAuthority (`WordAuthority.accepts_tokens` untouched).

### Threat Model

- **Assets**: Staff JWT sessions; simulation turn leases; dual-player rack states & move replays; provider credential names/values; regular player private racks; production environment files; reverse proxy routing boundaries; public documentation integrity.
- **Trust Boundaries**:
  1. Browser → Next.js turn route → Django admin/simulation API.
  2. Public 443 → Loopback `127.0.0.1:8001` (Next-to-Django callback) & `127.0.0.1:8443` (Django admin TLS).
  3. Staff A vs. Staff B vs. Ordinary Player.
  4. Client store (`useGameStore`) vs. Server JWT session authority.
  5. Repository Git templates vs. Live host deployment.
  6. Executable repository truth vs. Public documentation.
- **Attacker-Controlled Inputs**: Authorization headers; PATCH/register request payloads; simulation game IDs; simulation action/turn request JSON; Host and X-Forwarded headers; operator environment variables; public documentation followed by developers or LLMs.
- **Security Properties Verified**: Server-side staff authorization (`IsAdminUser`); creator-only simulation mutation; fail-closed 404s on invalid/absent IDs; in-flight token refresh cannot restore logged-out sessions or overwrite accounts; strict output projection (no secret/path leakage); CSRF trusted origins derived fail-closed from CORS; proxy SSL indication default disabled; loopback-enforced service binds; Next/Django route separation in nginx.

---

### RC1–RC12 Adjudication Table

| Claim | Verdict | Evidence Class | Pointer & Evidence |
| :--- | :--- | :--- | :--- |
| **RC1** Unauth→401, non-staff→403 on admin games list, replay, analytics, simulation create/state/step/action/stop | **holds** | `reproduced-dynamic` + `established-static` | `test_admin_routes_reject_invalid_access_token`, `test_admin_routes_reject_expired_access_token`, `test_simulation_remaining_endpoints_require_staff` passed; `simulation_views.py:24`, `admin_views.py:26`, `analytics_views.py:12` enforce `[IsAuthenticated, IsAdminUser]`. |
| **RC2** Non-staff cannot set `is_staff` / `is_superuser` / `is_service_account` / `groups` / `user_permissions` via PATCH me or register | **holds** | `reproduced-dynamic` + `established-static` | `test_nonstaff_patch_cannot_change_privileged_fields`, `test_patch_ignores_privilege_fields_while_updating_email`, `test_register_ignores_unexposed_user_fields` passed; `UserSerializer.Meta.read_only_fields` includes `is_staff`; `RegisterSerializer.Meta.fields` limited to username/email/password. |
| **RC3** Staff B GET Staff A simulation is 200; mutate is 404 (not 403); leases absent from GET | **holds** | `reproduced-dynamic` + `established-static` | `test_staff_cannot_use_another_creators_lease`, `test_simulation_state_never_exposes_lease_material` passed; `get_playground_simulation` queries without creator filter; `step_playground_simulation`, `_locked_lease`, `stop_playground_simulation` filter by `created_by_id=user_id`, raising `SimulationNotFoundError` (404) on mismatch. |
| **RC4** IHR-S1-F01 remains: simulation pass write path unsanitized, reads sanitized, staff-creator-only | **holds** | `established-static` | `SimulationActionSerializer.validate` (`simulation_serializers.py:107-131`) routes `place` through `ApplyAIMoveSerializer` and `exchange` through `ExchangeSerializer`, but `pass` accepts raw `ai_metadata`; `services._submit_pass_locked` persists it; read paths in `simulations.py:174` and `replay.py:183` sanitize via `sanitize_ai_metadata`. |
| **RC5** Fast default pytest still SQLite; postgresql `CONN_MAX_AGE` default 600 & `CONN_HEALTH_CHECKS` only on postgresql; opt-in `LIBRETILES_TEST_POSTGRES` uses `libretiles_pytest` | **holds** | `reproduced-dynamic` + `established-static` | `test_postgres_dialect_parity.py` ran default: 4 passed, 6 skipped in 0.05s; settings probes passed; `settings.py:228-253` configures connection persistence only in `if _DB_ENGINE == "postgresql":`; `_POSTGRES_TEST_DB_NAME = "libretiles_pytest"`. |
| **RC6** `CSRF_TRUSTED_ORIGINS` derived from CORS (optional override), fail-closed parse; `DJANGO_SECURE_PROXY_SSL_HEADER` default false; `SECURE_HSTS_PRELOAD` unset; `security.W021` still asserted | **holds** | `reproduced-dynamic` + `established-static` | `test_security_settings.py` probes passed; `_csrf_trusted_origins` (`settings.py:120-157`) validates scheme, rejects wildcards/paths/userinfo/queries/fragments; `SECURE_PROXY_SSL_HEADER` defaults to None (`settings.py:330-334`); `test_production_like_hsts_closes_w005_and_keeps_w021_accepted` asserts `security.W021` presence. |
| **RC7** Nginx templates do NOT send all `/api/` or `/admin/` to Daphne; Next owns `/api/ai/*`, `/api/models`, `/api/prompts`, `/api/admin/simulate/<id>/turn`, and `/admin`; contrib admin unpublished on 443; proto overwritten to https on 443 and loopback 8001; `BACKEND_URL` is `http://127.0.0.1:8001` | **holds** | `reproduced-dynamic` + `established-static` | `test_vps_templates.py` passed (12 tests in 0.11s); `libretiles.conf` routes `/api/ai/`, models, prompts, simulation turn regex, and `/admin` to `127.0.0.1:3000`; Daphne on `127.0.0.1:8000`; private admin on `127.0.0.1:8443`; loopback callback on `127.0.0.1:8001` with Host `YOUR_DOMAIN` and proto `https`; `docs/vps_deployment_guide.md:40` documents `BACKEND_URL=http://127.0.0.1:8001`. |
| **RC8** Frontend systemd launches standalone `server.js` with `/usr/bin/env HOSTNAME=127.0.0.1 PORT=3000` after EnvironmentFile; no 0.0.0.0; deploy copies `public/.` & `.next/static/.`; no dotenv copied into standalone | **holds** | `reproduced-dynamic` + `established-static` | `test_systemd_units_are_non_root_and_loopback_only`, `test_frontend_systemd_launch_prefix_replaces_environment_file_bind`, `test_deploy_script_copies_public_and_static_into_standalone` passed; `libretiles-frontend.service` uses `/usr/bin/env` prefix; `vps_deploy.sh:182-189` copies `public/.` and `.next/static/.` via `run_in_dir` without copying `.env*`. |
| **RC9** `WordAuthority.accepts_tokens` untouched by whole 16; regular player gameplay pages not redesigned; Zustand persist version remains 6 | **holds** | `established-static` | `git log a892f74..HEAD -- backend/gamecore/` is empty; `frontend/src/app/game`, `/play`, `/settings` untouched; `frontend/src/hooks/useGameStore.ts:328` specifies `version: 6`. |
| **RC10** Public docs vs tree: `AGENTS.md` claiming Vercel frontend hosting; `README.md` throttle prose saying `DEBUG=true`; `README.md` teaching `runserver 0.0.0.0:8000`; architecture.md Production vs Vercel AI SDK library distinction | **holds** | `established-static` | Confirmed all 4 claims: `AGENTS.md:187` says "Frontend: Vercel"; `README.md:111` says "local DEBUG=true boot"; `README.md:77,203` and `AGENTS.md:32` teach `0.0.0.0:8000`; `docs/architecture.md:33,40,309` distinguishes self-hosted VPS from Vercel AI SDK library name. |
| **RC11** `backend/billing/migrations/` leftover exists and is not in `INSTALLED_APPS` (A4) | **holds** | `established-static` | `backend/billing/migrations/` holds `0001_initial.py` and `0002_precise_usd_balances.py`; `settings.py:164-183` `INSTALLED_APPS` does not contain `billing`. |
| **RC12** No `credential_env_name` / `api_key` / filesystem-path fragrance in admin/replay/simulation JSON at HEAD | **holds** | `reproduced-dynamic` + `established-static` | `test_replay_projects_diagnostic_trace`, `test_replay_bounds_failure_codes`, `test_admin_list_and_analytics_exclude_internal_payloads`, `test_simulation_config_output_is_projected` passed; Next turn route 5xx tests confirm fixed public error detail. |

---

### P1–P5 Process Claims Evaluation

#### P1: Proportion of Independent R3 vs E2/R1 Acceptance
- **Claim**: Independent R3 occurred only on Slice 1. Slices 2–5 were accepted on E2/R1 (with isolated static tests in Slices 4–5). Is that proportionate or an audit hole?
- **Verdict**: **Proportionate to landed attack surface; NOT an audit hole.**
- **Rationale**: Slice 1 modified actual authentication and session handling code (`api.ts` refresh mutex, `authEpoch` session invalidation, simulation UUID parsing, and payload projections). Per INFOSEC 4.4, that required a fresh independent audit (R3), which was executed in session 03. Slices 2, 3, 4, and 5 modified database settings, production security headers, operational deployment templates, and Next.js standalone build configuration. None of Slices 2–5 introduced new authentication backends, password validators, token generation, or model schema changes. Accepting Slices 2–5 on E2/R1 with isolated static tests was proportionate.

#### P2: Opening Handout §5.3 vs Product and Documentation Truth
- **Claim**: The opening `00_handout.md` §5.3 said proxy `/api/` and `/admin/` to :8000. Did later work correct the PRODUCT, or only the templates, while AGENTS.md/README still lie?
- **Verdict**: **Templates and architecture.md were corrected; README and AGENTS.md were left lagging.**
- **Evidence**:
  - `00_handout.md` §5.3 stated: `Proxy pass /api/ and /admin/ to port 8000. Proxy pass all other frontend routes to port 3000.`
  - In Slice 4, `backend/scripts/nginx/libretiles.conf` corrected this: Next.js explicitly owns `/api/ai/*`, `/api/models`, `/api/prompts`, `/api/admin/simulate/<id>/turn`, and `/admin`. Only Django-owned API routes (`/api/auth/`, `/api/catalog/`, `/api/game/`, `/api/admin/` non-turn) and `/ws/` route to port 8000.
  - `docs/architecture.md` was updated in Slices 4 and 5 to reflect standalone VPS hosting.
  - However, `AGENTS.md:187` still states `- Frontend: Vercel (env from frontend/.env.local.example).`, `backend/config/settings.py:295` still comments `# CORS — allow Vercel frontend`, and `README.md:77,203` still teaches binding `0.0.0.0:8000`. The product and templates are correct; developer documentation still carries stale claims.

#### P3: Slice Overclaiming Analysis
- **Claim**: Name any slice that overclaimed relative to its diff.
- **Verdict**: **Confirmed bounded overclaim in Slice 5.**
- **Analysis**:
  - Slice 5 commit `33ffa15` is titled `feat(frontend): run production Next as a standalone server`. In reality, `npm run build` was strictly forbidden in tests to prevent generating untracked `.next/` artifacts. The tests verified only the configuration and templates (`next.config.ts`, `libretiles-frontend.service`, `vps_deploy.sh` text, and Bash syntax). The actual `.next/standalone` bundle was never built or executed during the slice. The closure record honestly noted this as an operational residual ("Standalone tree exists only after operator `npm run build` on a VPS").
  - Slices 1–4 accurately reported their diffs and passed tests without overclaiming capability.

#### P4: Prompt Defects & Worker Waste Analysis
- **Claim**: Name any prompt defect that caused Worker waste.
- **Classification**: **Process residuals (no product defects introduced).**
- **Findings**:
  1. *Plan-Mode Meta Report Write Blocker*: Sessions 08 (Slice 4 planner) and 10 (Slice 5 planner) terminated with `status: PARTIAL` because developer-level native Plan Mode prohibited writing reports to `/home/agile/meta/`. The Cooperator had to intervene to archive the report.
  2. *Slice 5 Heredoc Typo*: `11_implementation_00.md` included a heredoc formatting join that produced `EnvironmentFileoverrides` (missing space) in commit `33ffa15`'s message body.
  3. *Slice 5 Ruff Subcommand Typo*: The implementation prompt had a typo in the ruff invocation (`.venv/bin/ruff cheame ...`). The worker corrected it to `ruff check`.
  4. *Slice 1 Signature Mismatch*: Prompt §4.5 gave an unworkable one-parameter signature for `applyRefreshedAuth`. The worker adopted the planner's coherent two-parameter signature.

#### P5: Closure Residuals Table Audit (`99_closure.md` §4)
- **Claim**: Walk the closure residuals table against the tree; mark any row stale, overstated, or missing.
- **Audit Outcome**:
  - Rows 1–12 of `99_closure.md` §4 are accurate and confirmed by source inspection.
  - **MISSING RESIDUAL**: `README.md` (lines 77, 203) and `AGENTS.md` (line 32) explicitly teach `runserver 0.0.0.0:8000`. The closure table noted `README DEBUG=true` (row 8) and `AGENTS.md Vercel` (row 7), but omitted the `0.0.0.0` network-exposure bind instruction.
  - **MISSING RESIDUAL**: `backend/config/settings.py:295` comment `# CORS — allow Vercel frontend` was omitted from the residuals table.

---

### Security Findings Record

```text
Finding ID: IHR-P16-F01
Status: open, accepted-residual
Severity: low
Confidence: high (code fact)
Evidence class: established-static
Category: output/storage hygiene (INFOSEC 4.6 adjacent)
Location: backend/game/simulation_serializers.py:107-131 (SimulationActionSerializer.validate)
Description: Simulation action operation "pass" accepts ai_metadata as a raw DictField without
  validating through a serializer, whereas "place" uses ApplyAIMoveSerializer and "exchange" uses
  ExchangeSerializer. Move.ai_metadata persists this raw payload for pass.
Reachability: Authenticated staff creator with a valid turn lease on their own simulation only.
Impact: Bounded to staff simulation instances. All read paths project through sanitize_ai_metadata.
  No cross-principal leak established.
Acceptance-blocking: non-blocking.
```

```text
Finding ID: IHR-P16-F02
Status: open
Severity: low (security-adjacent documentation defect)
Confidence: high
Evidence class: established-static
Category: network exposure & documentation truth
Location: README.md:77, 203; AGENTS.md:32; CONTRIBUTING.md:45; scripts/start-backend.sh:33
Description: Public developer documentation and helper scripts explicitly instruct operators and
  developers to launch Django with `runserver 0.0.0.0:8000`.
Reachability: Public documentation read by human developers, interviewers, and automated LLM agents.
Impact: Binding to 0.0.0.0 exposes the unauthenticated development HTTP server across all network
  interfaces (including untrusted local networks and public interfaces if run on a cloud VPS).
Remediation: Update documentation and scripts to teach loopback binding `127.0.0.1:8000` for development.
Acceptance-blocking: non-blocking.
```

```text
Finding ID: IHR-P16-F03
Status: open
Severity: info (documentation contradiction)
Confidence: high
Evidence class: established-static
Category: architectural integrity & deployment truth
Location: AGENTS.md:187; backend/config/settings.py:295; libretiles_PRD.md:25, 174
Description: AGENTS.md states "- Frontend: Vercel (env from frontend/.env.local.example)", settings.py
  states "# CORS — allow Vercel frontend", and libretiles_PRD.md states frontend deployed on Vercel.
  This directly contradicts Whole 16's standalone VPS architecture (systemd + loopback standalone Next.js).
Impact: Public readers, interviewers, and automated coding agents receive contradictory deployment
  instructions.
Remediation: Update AGENTS.md, settings comments, and PRD to reflect the self-hosted standalone VPS architecture.
Acceptance-blocking: non-blocking.
```

```text
Finding ID: IHR-P16-F04
Status: open, accepted-residual
Severity: low (database migration hygiene)
Confidence: high
Evidence class: established-static
Category: database migration compatibility
Location: backend/game/migrations/0008_atomic_token_state_schema.py:19-24
Description: The pre-migration check `refuse_if_game_state_present` checks `model.objects.count()` on
  the default database connection rather than using `schema_editor.connection.alias`.
Impact: Running `manage.py migrate --database=<other>` fails if the default database contains legacy records,
  even if the target database is empty.
Acceptance-blocking: non-blocking.
```

```text
Finding ID: IHR-P16-F05
Status: open, accepted-residual
Severity: info (repository hygiene)
Confidence: high
Evidence class: established-static
Category: dead code / orphaned schema
Location: backend/billing/migrations/0001_initial.py, 0002_precise_usd_balances.py
Description: `backend/billing/` contains legacy migration files from the removed billing app, but
  `billing` is absent from `INSTALLED_APPS`.
Impact: Orphaned files confuse static analysis and migration introspection.
Acceptance-blocking: non-blocking.
```

```text
Finding ID: RFP-01 (Rejected False Positive)
Status: rejected-false-positive
Severity: none
Category: authorization boundary
Location: frontend/src/app/api/admin/simulate/[id]/turn/route.ts
Description: Suspected that Next.js simulation turn route bypassed server-side staff checks by calling
  internal AI functions directly.
Audit Result: Disproved dynamically and statically. Missing Authorization returns 401; non-staff token
  returns 403; no provider or AI move execution occurs without Django-level staff verification.
```

### Containment Ledger with Cleanup Outcome

- Repository mutations: ZERO. `git status --porcelain=v1` verified empty before and after all actions.
- Network requests: Limited strictly to `git ls-remote origin refs/heads/main` (verified SHA equality). No external HTTP, no package downloads, no provider API calls, no SSH.
- Protected files: `backend/.env` and `frontend/.env.local` were NOT read, printed, hashed, or length-measured.
- Test execution: Ran only authorized existing pytest/vitest suites using synthetic in-memory fixtures.
- Cleanup: Temporary test output buffers deleted. Meta report and handout/notes written atomically via `.tmp` rename.

### Limitations

1. No live VPS was provisioned or connected via SSH. INFOSEC R5 live host acceptance remains deferred until a real host is provided.
2. Next.js standalone runtime was verified via configuration, systemd unit, and deploy script static analysis; `npm run build` was not executed in this test environment.
3. PostgreSQL tests ran in SQLite mode by default; opt-in PostgreSQL verification requires a running docker container (which was not running and not started).

### Residual-Risk Summary

All 12 Risk Claims hold. Zero acceptance-blocking vulnerabilities exist. The codebase is secure, staff-gated, fail-closed, and architecturally sound for standalone VPS operation. The primary open residuals are documentation-truth and network-exposure instructions (`runserver 0.0.0.0:8000` and stale Vercel claims) which mislead developers and LLM agents.

---

## Product-Horizon Annex

### Ranked Candidate Logical Wholes

#### 1. `public-docs-and-stale-truth` (⭐ SELECTED FOR META 17)
- **One-sentence objective**: Eliminate network-exposure instructions (`0.0.0.0:8000`), remove stale Vercel claims, streamline `README.md` for interviewer clarity, and freeze documentation truth with static tests.
- **Why now**: Highest leverage for interview presentation and open-source readers. A technical reviewer or LLM following `README.md` or `AGENTS.md` is currently instructed to expose Django on `0.0.0.0:8000` and deploy on Vercel, contradicting Whole 16's VPS standalone achievements.
- **Why not now**: None. Scope is strictly bounded to documentation files and static tests; zero application code mutation.
- **First slice sketch**: Replace all `0.0.0.0:8000` binds with `127.0.0.1:8000`; eliminate Vercel hosting claims in `AGENTS.md` and `settings.py`; fix `DEBUG=true` throttle prose; create `backend/tests/test_documentation_deployment_claims.py`.
- **Out of scope**: UI changes, mobile pinch-zoom, provider unfreezing, live host deployment.

#### 2. `codebase-hygiene-and-residual-reconciliation`
- **One-sentence objective**: Close carried code residuals: route simulation pass `ai_metadata` through a serializer sanitizer, fix `game.0008` migration alias binding, and purge orphaned `billing` migration files.
- **Why now**: Cleans lingering technical debt and removes schema confusion.
- **Why not now**: Lower impact on external readers and interviewers than documentation clarity.
- **First slice sketch**: Update `SimulationActionSerializer` to validate pass metadata; add regression test.
- **Out of scope**: New features, UI, documentation rewrite.

#### 3. `github-actions-ci-and-sbom`
- **One-sentence objective**: Establish an automated GitHub Actions CI pipeline running ruff, mypy, pytest, vitest, and typecheck, plus automated dependency SBOM generation.
- **Why now**: Demonstrates professional enterprise DevOps maturity in interviews.
- **Why not now**: Requires external GitHub Actions workflow setup; better sequenced after documentation truth.
- **First slice sketch**: Create `.github/workflows/ci.yml` running fast backend/frontend quality gates on push.
- **Out of scope**: Live deployment automation, CD pipelines.

#### 4. `dependency-currency-and-lockfile-hygiene`
- **One-sentence objective**: Audit and update Python (Django 5.2.x, psycopg 3.x) and Node (Next 16.3.x, React 19) dependencies, resolving Vite/Vitest deprecation warnings.
- **Why now**: Prevents software rot and resolves deprecation warnings observed during vitest runs.
- **Why not now**: Moderate risk of upstream breaking changes; requires comprehensive regression testing across all 12 game variants.
- **First slice sketch**: Audit npm and poetry dependencies; update minor patch versions and fix Vitest CJS config warning.
- **Out of scope**: Major framework migrations.

#### 5. `multilingual-catalog-review-and-quality`
- **One-sentence objective**: Perform second-opinion human and expert linguistic review of the 8 machine-authored interface catalogs (German, Portuguese, Icelandic, Italian, Dutch, Danish, Swedish, Afrikaans).
- **Why now**: Enhances international user experience and closes the AGENTS.md "not done yet" item.
- **Why not now**: Requires extensive translation review; purely non-technical copy refinement.
- **First slice sketch**: Review and refine German and Italian message catalogs; add exact-text regression assertions.
- **Out of scope**: Backend game engine, lexicons.

#### 6. `session-storage-and-csp-hardening`
- **One-sentence objective**: Migrate client JWT storage from `localStorage` to HttpOnly secure cookies and eliminate `'unsafe-inline'` from style CSP.
- **Why now**: Closes the theoretical XSS-to-token-theft residual.
- **Why not now**: High complexity; requires rewriting frontend auth state hydration across SSR and client components.
- **First slice sketch**: Design cookie-based refresh token transport on auth endpoints.
- **Out of scope**: Game logic, UI changes.

#### 7. `nine-provider-unfreeze-and-catalog-decoupling`
- **One-sentence objective**: Unfreeze the nine hardcoded AI providers, establishing dynamic provider discovery, runtime registry abstraction, and quota tracking.
- **Why now**: Enables dynamic multi-provider expansion beyond hardcoded constants.
- **Why not now**: Explicitly FROZEN by Cooperator decision (2026-08-31) pending dedicated whole; no incident-class defect requires emergency unfreezing.
- **First slice sketch**: Design decoupled provider interface and configuration schema.
- **Out of scope**: Changing engine scoring authority.

### Explicitly Excluded & Rejected Candidate Wholes

- **`C-ui` (UI/UX polish, responsive mobile/tablet pinch-zoom)**: EXPLICITLY PARKED by Cooperator direction. Must not be selected until he explicitly activates it.
- **`C-vpslive` (Named VPS live installation and INFOSEC R5 host gate)**: Requires real host credentials, IP, and SSH access which have not been granted.

---

### Handout & Notes Deliverables

- Handout path: `/home/agile/meta/projects/libretiles/17/00-public-docs-and-stale-truth/00_handout.md`
- Notes path: `/home/agile/meta/projects/libretiles/17/00-public-docs-and-stale-truth/00_notes.md`
- Handout Integrity Record (D-13): Fully completed in `00_handout.md` section 0 with honest coordinate review against baseline `33ffa150fa520118e67a6670422fe7fae1c98741`.

---

## Analytical Fields

### Orchestration Critique

- **MEASURED**:
  1. The audit prompt's decomposition into RC1–RC12 and P1–P5 mapped cleanly onto the landed 5-commit surface, allowing comprehensive verification without un-gated benchmark runs.
  2. The prompt's strict enforcement of read-only repository boundaries prevented accidental mutations.
  3. The prompt correctly anticipated the documentation discrepancies between `architecture.md` (updated in whole 16) and `AGENTS.md` / `README.md` (which lagged).
- **LEAD**:
  1. The prompt should explicitly require checking `CONTRIBUTING.md`, `scripts/start-backend.sh`, and `scripts/libretiles.sh` when auditing `0.0.0.0` exposure, as these scripts also repeat the bind command.
  2. Future milestone audit prompts should specify an exact format for the Handout Integrity Record to ensure zero ambiguity in successor orchestration.

### Enumeration Widened

1. `CONTRIBUTING.md:45` and `scripts/start-backend.sh:33` were identified as additional sites teaching `runserver 0.0.0.0:8000`.
2. `libretiles_PRD.md:25, 174` and `backend/config/settings.py:295` were identified as additional sites claiming Vercel deployment.
3. `package.json` scripts and Vitest configuration warnings were measured during test execution.

### Internal Delegation Used
`no` (All measurements and analyses conducted directly by this accountable Worker instance).

---

## One Smallest Next Step

Cooperator pastes the handout `/home/agile/meta/projects/libretiles/17/00-public-docs-and-stale-truth/00_handout.md` into a **FRESH Agent Orchestrator session**.
