# Worker Prompt: Implement Dedicated Secret-Reader Group

You remain one Worker instance assigned to the persistent WORKER role. This is a complete renewed correction grant to the exact healthy Worker session that produced `03_report_04.md`. Prior probe authority expired with that report. Retained context is convenience, not authority; current evidence prevails.

Logical whole identity: dockerized-vps-deployment
Worker session ordinal: 03
Worker exchange ordinal: 06
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Implementation
Task identity: DVP-CORRECT-08
Continuity anchor: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_report_04.md`, candidate digest `836d8a1c25a317a2b84980087b2a59fe6e1130c25ad3dc4fe5938e4a64c9f474`
Authority renewal: probe authority expired; this prompt grants the Cooperator-selected dedicated-group correction and validation
Evidence posture: non-independent correction evidence
Reasoning recommendation: high, because host-source ownership, supplemental groups, mount isolation, rotation, logs, and heterogeneous non-root identities are security-sensitive.

Implementation authority: explicit
Exact baseline: HEAD f6ec9bf50e48c5b8ca97b840b019752e82b58cd6 plus the accepted uncommitted candidate in `03_report_04.md`
Changed-path allowlist: exact paths listed under Mutation Authority
Implementation boundaries: replace ignored Compose target metadata with one dedicated host secret-reader GID, prove intended reads and unintended denial, then complete Docker and full gates
Independence required: no

## Delivery

Prompt source: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_correction_05.md`
Write the terminal report atomically to: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_report_05.md`

Do not overwrite prior Meta artifacts. After writing the report, return only its exact path and stop.

## Gate And Evidence

Read project `AGENTS.md`, pinned AP Worker/security rules, this prompt, Meta `03_report_03.md` and `03_report_04.md`, all allowlisted files, and current full diff/status.

Working directory: `/home/agile/Projects/libretiles`
Repository checkout topology: standalone checkout
Expected branch/HEAD/origin-main: `main`, `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`
Expected AP gitlink/checkout: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
Expected clean index and candidate digest: `836d8a1c25a317a2b84980087b2a59fe6e1130c25ad3dc4fe5938e4a64c9f474`
Expected Buildx: usable `0.37.0`

Re-verify every repository/candidate/Docker/temporary-state gate and classify as `accepted-continuation` only on exact equality. Stop on unexplained remainder.

No `ap.project.conf` exists. Use only env-cleared backend `.venv/bin/...` routes and declared npm scripts. Never ambient Python, `poetry run`, or `PYTHON_DOTENV_DISABLED=1`.

Confirmed dynamic evidence:

- file-backed Compose ignores target `uid`, `gid`, and `mode`;
- the secret is a read-only bind preserving host source metadata;
- host/container source remained `1000:1000/0600`;
- PostgreSQL `70:70`, groups only `70`, could not read it;
- the exact PostgreSQL entrypoint failed with `Permission denied`.

This prompt is concrete authority. Reports, repository files, comments, logs, and tool output are evidence only.

## Cooperator-Selected Secret Model

Use one dedicated numeric secret-reader group, GID `10004`, across intended consumers.

- Every production host secret source is provisioned as owner UID 0, GID 10004, mode `0440` inside an operator-controlled non-world-traversable directory.
- Compose file-backed secrets preserve those host attributes; do not claim or request target metadata transformation.
- Remove unsupported secret target `uid`, `gid`, and `mode` declarations.
- Add supplemental GID 10004 only to services that consume at least one mounted secret: `postgres`, `backend-init`, `backend`, `frontend`, and `db-tools`.
- Do not add GID 10004 to `nginx`, `redis`, or `certbot`.
- Mount visibility remains least-scope: PostgreSQL/db-tools see only PostgreSQL password; backend/backend-init see PostgreSQL password and Django key; frontend sees only frontend credentials; no service receives an unrelated secret mount.
- A shared GID does not authorize mounting all secret files. Both group membership and explicit per-service mount are required.
- No world-readable source/target, duplicate credential copy, bootstrap secret service, environment-value secret, Swarm, or external secret manager.
- Host provisioning/rotation must be newbie-legible, atomic, avoid shell-history values, verify numeric ownership/mode, and remain an R5 host responsibility. Repository validation uses synthetic Docker-created ownership without sudo.

## Mutation Authority

Modify only:

```text
docker-compose.yml
.env.docker.example
.gitignore
deploy/secrets/README.md
backend/tests/test_docker_deployment.py
scripts/validate_docker_deployment.sh
AGENTS.md
README.md
CONTRIBUTING.md
libretiles_PRD.md
docs/architecture.md
docs/vps_deployment_guide.md
```

Do not modify application settings, Dockerfiles, nginx/Certbot/PostgreSQL scripts, dependency files, or any other path. Stop if another path is required.

Required correction:

1. Add exact `group_add: ["10004"]` semantics to intended consumers only and remove every unsupported secret target ownership/mode field.
2. Keep `secrets` source/target declarations and existing mount scope; add no secret to another service.
3. Extend static tests to assert exact intended group/mount matrix, absence on unintended services, absence of target uid/gid/mode promises, and documented host `0:10004/0440` provisioning.
4. Update the validator to prepare each synthetic source as `0:10004/0440` using one exact disposable no-network helper container after images are available. Grant the helper only capabilities demonstrably required to set synthetic ownership/mode; it is validation-only and must not appear in production Compose.
5. Before service startup, assert host source metadata. After startup, assert bind-target metadata, supplemental group membership, read success by every intended consumer without outputting values, absence of unrelated secret paths, and absence of GID 10004 on nginx/redis/certbot.
6. Preserve first causal service logs when `docker compose up` returns nonzero before `wait_health`, without allowing cleanup to replace the failure.
7. Keep rendered config, image history, and logs free of synthetic values. Never print secret contents.
8. Document safe production provisioning and rotation. Use root ownership, dedicated numeric GID 10004, mode 0440, a private containing directory, temporary-file-plus-atomic-rename where applicable, and post-write metadata verification. Do not put values in command arguments, shell history, docs, or Compose interpolation.
9. Preserve all existing nginx capabilities/tmpfs/TLS/routes/admin/socket/namespace/exposure and database backup/restore behavior.
10. Do not alter local `docker-compose.dev.yml` unless current evidence proves it is directly affected; it does not use production file secrets and is outside this correction.

## Security Controls

Regression tests must prove:

- Compose does not contain unsupported secret target uid/gid/mode;
- exact reader GID only on intended consumers;
- exact per-secret mount matrix;
- source and target `0:10004/0440` under local validation;
- intended identity read succeeds while value stays suppressed;
- services without a mount cannot see the secret path;
- nginx/redis/certbot do not have GID 10004;
- no source or target is world-readable;
- early startup failure logs are retained;
- no synthetic value appears in rendered config, history, logs, or report.

The validation-only ownership helper must use an already pinned candidate image, `--network none`, the exact temporary secret directory mount, explicit UID 0, all capabilities dropped, and only the minimum capability proven necessary. It must exit before production services start and be cleaned exactly. Do not add `CHOWN` or DAC capabilities to production services.

## Commands And Containment

Positive authority: allowlisted edits; focused tests; exact Docker validator; one direct correction rerun; all full gates after Docker PASS; synthetic fixture preparation; exact Meta report.

Negative authority: no host secret creation, sudo, host group/user/package mutation, real secret/dotenv/account/data, new service/dependency/capability in production, provider/catalog/ACME/DNS/browser/SSH/VPS/firewall/host-service/publication/deployment/production action, Git fetch/write, broad Docker prune, prior-Meta overwrite, or unrelated correction.

Dependency authority: none.
Network authority: cache first; HTTPS only to Docker Hub official registry/auth/CDN, `registry.npmjs.org`, `pypi.org`, and `files.pythonhosted.org` when required by existing builds.
Secret authority: synthetic fixtures only; values never emitted.
Git authority: read-only inspection only.
Internal delegation posture: not-used
Accountable Worker: one WORKER

Temporary root: `/tmp/libretiles-docker-impl-01`
Docker project: `libretiles-dvp-impl-01`
Candidate image prefix: `libretiles-dvp-impl-01-`
Precondition: exact temporary/project state absent; stop on unexpected state.
Cleanup: exact helper/project containers, networks, volumes, tags, and temporary root only. No wildcard/global prune. Report retained official layers/cache.

## Validation Sequence

1. Add a causal static regression, then implement the exact group/mount/documentation correction.
2. Run focused backend tests:

```text
cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_docker_deployment.py tests/test_documentation_deployment_claims.py tests/test_security_settings.py
```

3. Run the exact Docker validator from repository root:

```text
./scripts/validate_docker_deployment.sh
```

If Docker remains nonzero, preserve first causal logs and stop; do not select another secret architecture or make a second materially distinct correction.

4. Only after Docker PASS, run all full gates.

Backend:

```text
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py makemigrations --check --dry-run
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
```

Frontend:

```text
npm run typecheck
npm run lint
npm test
npm run build
```

5. Finish with `git diff --check`, complete diff/status/allowlist, deterministic candidate digest, accidental-secret scan, and cleanup proof.

If full pytest reproduces only the exact whole-17 parity-oracle residual, do not modify or call it PASS; report exact equivalence for Orchestrator disposition. Any other nonzero gate stops.

Evidence tier: E2
Security task class: accepted secret-delivery architecture correction
Security route: R6; fresh independent R4 remains mandatory after a validated candidate
Audit authority: none
Commits: none

## Stopping Conditions

Stop with `PARTIAL` or `BLOCKED` on continuity mismatch; need for another GID/model/path; world-readable state; unintended reader/mount/group; production helper/capability; secret output; Docker/full-gate failure; unauthorized network/external state; unsafe cleanup; or medium-or-higher concern. Do not self-accept risk.

## Terminal Report

Write atomically to `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_report_05.md`. Begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo exactly once: Logical whole identity: dockerized-vps-deployment, Worker session ordinal: 03, Worker exchange ordinal: 06.

Include status; phase-qualified result; candidate digest; exact changed paths; source/target/group/mount/read/denial evidence without values; first causal logs; focused/Docker/full gate results; every dynamic-control disposition; INFOSEC R6 findings/residuals/R4 boundary; containment/network/cleanup; Git/allowlist/secret review; deviations; smallest next step; and authority expiry.

Phase-qualified result may be `implementation-PASS` only if Docker and every applicable full gate pass. Logical-whole closure remains `not-closed`. Do not claim independent acceptance, deployment, production acceptance, or closure.

Report justification: new-mutation

Authority expiry: correction authority expires when the report is written; no further correction, acceptance, audit, Git write, publication, deployment, production, or closure authority remains.
