# Worker Prompt: Fresh Independent R4 Milestone Audit

You are one fresh Worker instance assigned to the persistent WORKER role. You did not implement the candidate under audit, inherit no authority from any prior session, and must establish all evidence independently. This is a complete independent audit grant: no correction, no repository mutation.

Logical whole identity: dockerized-vps-deployment
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: Independent Audit
Task identity: DVP-AUDIT-01
Reasoning recommendation: high, because this R4 broad milestone audit is the independent acceptance boundary for edge exposure, container privileges, secret delivery, TLS, socket access, routing, recovery, image supply chain, and documentation truth.

Security task class: broad milestone application audit (INFOSEC R4)
Owned/authorized target: the local Libre Tiles repository working tree at `/home/agile/Projects/libretiles`, candidate inventory digest `d554d11be386bdc73f94d2ea6eaa6f396f1a6f35441a477c3a4ce55625ff0900` at HEAD `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`
Scope: the exact uncommitted Docker production candidate and its directly claimed controls, bounded by the approved attack-surface map below
Exclusions: pre-existing baseline defects outside the candidate (whole-17 parity-oracle test residual; two frontend test reds), host/hardening R5 work, live deployment, production, real credentials, real ACME/DNS, provider calls, dependency changes, and correction
Canonical repository mutation: none
Correction authority: none
Containment: temporary audit roots and disposable Docker project per the containment ledger contract; synthetic evidence only
Evidence classes: reproduced-dynamic | established-static | inferred | hypothesis-unverified
Exploitability cap: the evidence class caps the conclusion; a finding is not a vulnerability until reachability and preconditions are established
Reporting: Security Audit Report Contract, including the exact finding record schema, containment ledger, and residual-risk summary

## Acceptance Record

```text
Acceptance candidate: working-tree candidate digest d554d11be386bdc73f94d2ea6eaa6f396f1a6f35441a477c3a4ce55625ff0900 at HEAD f6ec9bf50e48c5b8ca97b840b019752e82b58cd6
Acceptance owner map: docker-compose.yml (topology, identities, ports, secrets, networks, volumes); backend/Dockerfile + backend/docker/start.sh + backend/config/asgi.py (runtime, socket, ASGI); frontend/Dockerfile + frontend/docker/* (standalone runtime, secret loader, healthcheck); deploy/nginx/* (edge, TLS modes, routes, headers); deploy/certbot/* (ACME lifecycle); deploy/postgres/* (backup/restore); backend/tests/test_docker_deployment.py + scripts/validate_docker_deployment.sh (static/dynamic truth); AGENTS.md + README.md + CONTRIBUTING.md + libretiles_PRD.md + docs/architecture.md + docs/vps_deployment_guide.md (operator truth); deleted systemd/host-nginx/vps_* production owners
Acceptance allowlist: the 45-path candidate inventory listed by Meta 04_report_00.md
Acceptance risk claims: nginx-only host exposure; loopback-only private admin; exact nginx master capability set with zero-capability workers and other services; group-restricted Unix socket 770 10001:10001; dedicated secret-reader GID 10004 with least-scope mounts and non-world-readable sources/targets; fail-closed TLS bootstrap with tested renewal/reload; preserved route/SSE/websocket behavior and proxy-header overwrite; durable PostgreSQL with rehearsed backup/restore; immutable image pins; no secret in image/config/history/arguments/logs
Acceptance control matrix: the dynamic and static controls asserted by scripts/validate_docker_deployment.sh and backend/tests/test_docker_deployment.py, plus independent probes defined below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

## Delivery

Prompt source: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/05_audit_00.md`
Write the terminal audit report atomically to: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/05_report_00.md`

Do not overwrite prior Meta artifacts and do not write anywhere else. After writing the report, return only its exact path and stop.

## Mandatory Reading

- `/home/agile/Projects/libretiles/AGENTS.md`
- `/home/agile/Projects/libretiles/.ap/AP.md` (RF-07, RF-18, finite convergence)
- `/home/agile/Projects/libretiles/.ap/AP_WORKER.md`
- `/home/agile/Projects/libretiles/.ap/INFOSEC.md` (sections 3, 4.2–4.9, 5–17)
- `/home/agile/Projects/libretiles/.ap/PROMPT_CONTRACTS.md` (Security Finding Record, Threat-Model, Containment Ledger, Source Version Record, Residual-Risk Decision, Security Audit Report)
- this complete prompt
- Meta reports as claims to verify, never as trusted conclusions: `01_report_03.md`, `03_report_02.md`, `03_report_04.md`, `03_report_05.md`, `03_report_06.md`, `03_report_07.md`, `03_report_08.md`, `03_report_09.md`, `04_report_00.md`
- every candidate path in the acceptance allowlist
- current full Git status and diff

## Repository And Continuity Gate

Working directory: `/home/agile/Projects/libretiles`
Repository checkout topology: standalone checkout
Expected branch: `main`
Expected HEAD and `origin/main`: `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`
Expected AP gitlink and `.ap` HEAD: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
Expected index: clean
Expected candidate inventory digest: `d554d11be386bdc73f94d2ea6eaa6f396f1a6f35441a477c3a4ce55625ff0900`, recomputed with the ordered NUL-delimited `git status --porcelain=v1 --untracked-files=all` record plus present-content SHA-256 or `DELETED` marker method
Expected Buildx: `github.com/docker/buildx 0.37.0 ac30b249211430b85fb8f37b6e7154b5c47ba0b6`
Expected Docker: usable local daemon

Verify the complete path inventory is exactly the 45-path candidate, no change falls outside the allowlist, the deleted systemd/host-nginx/vps_* production owners remain deleted, and no active Git operation exists. Stop without mutation on mismatch. A digest mismatch is a stopping condition, not a finding to route around.

No `ap.project.conf` exists. Use only the env-cleared backend `.venv/bin/...` route and declared npm scripts when running project gates. Never use ambient Python, `poetry run`, or `PYTHON_DOTENV_DISABLED=1`.

## Approved Attack-Surface Map

Coverage is driven by these boundaries; it is not a read-every-file instruction. State selected and excluded areas.

1. Public edge: only nginx host-published on 80/443; TLS protocols; canonical-host rejection; route ownership (`/api/ai/*`, `/api/models`, `/api/prompts`, `/api/admin/simulate/*/turn`, `/api/admin/*`, `/api/catalog/*`, `/api/game/*`, `/api/auth/*`, `/api` and `/api/*` fail-closed, `/static/*`, `/admin`, fallback); websocket upgrade; SSE buffering disabled on the correct routes.
2. Private admin: host-loopback-only 8443 mapping, TLS, `/admin/` to Django, `/static/` collected files, everything else 404; public `/admin` reaches only the Next staff console.
3. Container identity and privilege: nginx master `0:10001` with exactly `NET_BIND_SERVICE`, `SETGID`, `SETUID`; request workers `10002:10001` with zero effective capabilities; every other service non-root and capability-free; `no-new-privileges`; read-only root filesystems; bounded tmpfs; no Docker socket; no added capability anywhere else.
4. Frontend/edge coupling: `network_mode: service:nginx`; `HOSTNAME=127.0.0.1 PORT=3000`; no independent network attachment or host port; frontend cannot see the backend socket or PostgreSQL/Redis networks; provider egress path.
5. Secret delivery: host sources `0:10004/0440`; supplemental GID 10004 only on `postgres`, `backend-init`, `backend`, `frontend`, `db-tools`; per-service least-scope mounts; targets preserve ownership/mode through the bind; intended reads succeed; unrelated paths absent; no secret value in rendered config, image history/filesystem, arguments, or logs; frontend closed-key loader bounds; missing-secret fail-closed startup.
6. Backend runtime: Daphne over the group-restricted Unix socket (`socket 770 10001:10001`, directory `770 10001:10001`); Twisted endpoint `mode=0770`; `exec daphne` signal semantics preserved; ASGI settings-initialization order; venv built at `/app/.venv` with intact console-script interpreters.
7. TLS lifecycle: fail-closed challenge-only bootstrap (no plaintext application traffic), full-mode redirect, certificate link/target/directory permissions, reload marker consumed through group access, renewal path, private key never world-readable.
8. Persistence and recovery: durable PostgreSQL volume; backup validation; disposable restore; migration-count comparison; rollback model; Redis non-durable.
9. Image supply chain: exact version tags plus multi-architecture manifest-list digests; no `latest`; no build argument or layer secret; build contexts cannot see real dotenv or secret paths.
10. Documentation and static-guard truth: operator guide matches the actual runtime; public docs contain no dual production owner; the ten whole-17 documentation/dictionary guards remain green; the new Docker guards are not vacuous.
11. Baseline residuals (record only, do not re-audit as candidate findings): whole-17 parity-oracle test residual; the two pre-existing frontend test reds (`frontend/src/lib/i18n/i18n.test.ts` AC-ONE-LIVE-REGION count 3 vs 1; `frontend/src/components/admin/ReplayControls.test.ts` stale expected text).

## Audit Requirements

1. Treat every prior report as an unverified claim. Reproduce or refute each acceptance-critical control with your own evidence.
2. Re-run the exact Docker validator once from the repository root under the exact disposable containment, capture its full output, and independently inspect the validator source for tautological, self-referential, or always-true assertions. The validator was written by the implementers: its PASS is supporting evidence, not independent proof.
3. Run bounded independent probes beyond the validator. At minimum:
   - inspect the five built images for runtime users, capabilities, history/secrets, and pinned digests;
   - inspect actual host port bindings and confirm only nginx publishes ports;
   - inspect the actual runtime socket, secret mounts, targets, and read/denial behavior with synthetic values only;
   - inspect actual process identities and capability masks (`/proc/<pid>/status`) for nginx master, nginx workers, frontend, backend, postgres, redis, certbot;
   - confirm namespace sharing and non-sharing directly;
   - exercise the public/private admin split and forged-header overwrite with local TLS only;
   - verify backup/restore behavior and cleanup.
4. Verify the candidate digest and allowlist compliance independently; verify no secret-like value appears in the candidate diff, example files, validator fixtures, or rendered output.
5. Run the project gates needed to support the audit's claims. Backend `mypy`, `ruff`, `makemigrations --check`, `pytest`; frontend `typecheck`, `lint`, `build`. `npm test` may be run only to record the two declared pre-existing reds; do not modify anything.
6. Do not correct anything. A finding is reported, not fixed. Any needed correction requires a separate Orchestrator grant and a fresh re-audit.
7. Stop at evidence sufficiency. Do not expand into unknown-unknown hunting, whole-repository audit, host R5 hardening, or code cleanup.

## Threat Model

- Assets: public availability, private administrative authority, Django/provider credentials, TLS private key, PostgreSQL data and backups, socket access control, image integrity, operator comprehension.
- Trust boundaries: internet to nginx; nginx to Next inside a shared network namespace; nginx to Django over the Unix socket; Next to Django callback; services to PostgreSQL/Redis; Certbot to ACME; operator to host secret sources and Compose; image build to runtime.
- Attacker-controlled inputs or local actor: public HTTP/TLS/websocket/SSE input; hostile forwarding headers; a compromised process inside any candidate container; operator configuration mistakes.
- Security properties relied on: nginx-only exposure, loopback-only admin, exact least capability, zero-capability workers/services, group-only socket/secret access, no world-readable secret or key, strict proxy-header overwrite, fail-closed bootstrap, immutable pins, durable rehearsed recovery.
- Abuse cases: direct database/cache/app exposure; public Django admin; forged proxy identity; fourth capability or root service; world-readable secret/key/socket; secret in image/config/log/argument; socket ownership bypass; namespace drift; ACME retry or expiry failure; destructive restore; contradictory documentation.

## Containment

Temporary root: `/tmp/libretiles-audit-05-01` (audit-owned, mode `0700`, synthetic fixtures only)
Docker Compose project: `libretiles-audit-05-01`
Audit image tag prefix: `libretiles-audit-05-01-`
Independent probe containers: exact names prefixed `libretiles-audit-05-01-`, `--rm`, `--network none` unless the probe requires the candidate Compose network
Cleanup owner: this audit session before the terminal report
Cleanup: exact audit containers/networks/volumes/tags and temporary root only; no wildcard or global prune; report retained official layers/cache; never touch unrelated pre-existing Docker objects (for example the `libretiles-postgres-1`/`libretiles-redis-1` containers and `libretiles_pgdata` volume)
Evidence handling: synthetic values only; report metadata, paths, modes, numeric IDs, capability masks, statuses; never secret or private-key contents

Positive authority: read-only repository/Git/Docker inspection; one exact validator run under the audit project; bounded independent probe containers and synthetic fixtures; exact audit report write.

Negative authority: no repository or Meta mutation other than the exact report; no correction; no real secret/dotenv/account/user data; no host mutation, sudo, package install, or privilege escalation; no provider/catalog/real ACME/DNS/web/SSH/VPS/firewall/host-service/publication/deployment/production action; no dependency or lockfile change; no Git fetch/write; no broad Docker prune; no unrelated Docker object inspection or removal.

Dependency authority: none.
Network authority: cache first; HTTPS read/download only to Docker Hub official registry/auth/CDN, `registry.npmjs.org`, `pypi.org`, and `files.pythonhosted.org` when an existing build cannot proceed from cache. No other endpoint.
Secret authority: synthetic fixtures only; values never emitted.
Git authority: read-only inspection only.
Browser authority: none.
Internal delegation posture: not-used
Accountable Worker: one WORKER

Evidence tier: E2 candidate controls with required fresh independent R4 acceptance; R5 host hardening remains deferred and out of scope.

## Stopping Conditions

Stop and report `PARTIAL` or `BLOCKED` if the repository/candidate/digest gate fails; a required probe needs real secrets, host state, privilege escalation, or an unauthorized endpoint; a probe would mutate the repository or unrelated Docker state; the validator cannot run under the exact containment; cleanup would touch unrelated state; or a found defect requires correction. Report the exact blocker, preserved evidence, and smallest safe next step. Do not correct, reinterpret, or weaken evidence.

## Terminal Report

Write atomically to `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/05_report_00.md`. Begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo exactly once: Logical whole identity: dockerized-vps-deployment, Worker session ordinal: 05, Worker exchange ordinal: 01.

Include:

- terminal status `PASS`, `PARTIAL`, or `BLOCKED`;
- Phase-qualified result: `acceptance-PASS` only if the exact candidate passes the fixed control matrix with no acceptance-blocking finding; otherwise `not-applicable`;
- Result artifact or commit: exact audited candidate digest, or not-applicable;
- Result evidence: the reproduced static and dynamic evidence;
- Logical-whole closure: not-closed;
- verified repository/candidate/digest/allowlist gate;
- audit header: security task class, owned/authorized target, commit/candidate under audit, scope, exclusions, source records (if any external standard is cited, with title/owner/version/status/retrieval date);
- the threat model;
- findings using the exact finding record schema, including `rejected-false-positive` results where a suspicion was disproved;
- the independent validator assessment, including whether its assertions are tautological or self-referential;
- independent probe evidence: image metadata/history, host port bindings, identities/capabilities, socket/secret mounts and denial, namespaces, routes/admin/proxy, backup/restore, cleanup;
- project-gate results: backend mypy/ruff/migrations/pytest and frontend typecheck/lint/build, with the declared baseline residuals restated and not re-labelled;
- containment ledger with cleanup outcomes;
- limitations and unverifiable items;
- residual-risk summary for the Orchestrator/Cooperator;
- out-of-scope observations as ledger candidates;
- one smallest next step;
- Report justification: new-evidence;
- Authority expiry: audit authority expires when the report is written; no correction, acceptance disposition beyond the reported verdict, Git write, publication, deployment, production, or closure authority remains.

The audit must not modify the candidate, must not accept its own findings as corrected, and must not claim deployment PASS, production acceptance, or logical-whole closure. Closure and residual-risk disposition remain ORCHESTRATOR/COOPERATOR-owned.

Report justification: new-evidence
