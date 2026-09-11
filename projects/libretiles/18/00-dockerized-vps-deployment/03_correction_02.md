# Worker Prompt: Apply Final Nginx Identity Capabilities

You remain one Worker instance assigned to the persistent WORKER role. This is a complete renewed correction grant to the exact healthy Worker session that produced `03_report_01.md`. Prior authority expired with that report. Retained context is convenience, not authority; current repository evidence prevails.

Logical whole identity: dockerized-vps-deployment
Worker session ordinal: 03
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Implementation
Task identity: DVP-CORRECT-05
Continuity anchor: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_report_01.md`, unchanged candidate inventory digest `f9f3af488031150ec626a8c2fec8d34d27e5d27811d09b1c750a26c8c6ef7141`
Authority renewal: prior authority expired; this prompt grants exactly the Cooperator-selected capability correction and validation below
Evidence posture: non-independent correction evidence
Reasoning recommendation: high, because the nginx master capability boundary is security-sensitive and must be proved against worker identity, TLS, socket, namespace, and exposure controls.

Implementation authority: explicit
Exact baseline: HEAD f6ec9bf50e48c5b8ca97b840b019752e82b58cd6 plus the exact accepted uncommitted candidate in `03_report_01.md`
Changed-path allowlist: exact paths under Mutation Authority
Implementation boundaries: add only the two identity-transition capabilities required by the selected nginx master/worker architecture, update direct guards/docs, then run Docker and full gates
Independence required: no

## Delivery

Prompt source: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_correction_02.md`
Write the complete terminal report atomically to: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_report_02.md`

Do not overwrite prior Meta artifacts. After writing the report, return only its exact path and stop.

## Governing Evidence And Gate

Read before mutation:

- `/home/agile/Projects/libretiles/AGENTS.md`
- `/home/agile/Projects/libretiles/.ap/AP.md`
- `/home/agile/Projects/libretiles/.ap/AP_WORKER.md`
- `/home/agile/Projects/libretiles/.ap/INFOSEC.md`, especially R1/R6 and correction/re-audit separation
- this complete prompt
- Meta `03_report_00.md` and `03_report_01.md` as historical evidence only
- current full Git status/diff and every allowlisted path before editing

Working directory: `/home/agile/Projects/libretiles`
Repository checkout topology: standalone checkout
Expected branch: `main`
Expected HEAD and `origin/main`: `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`
Expected AP gitlink and `.ap` HEAD: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
Expected index: clean
Expected worktree: exact candidate digest and path set recorded by `03_report_01.md`
Expected Buildx: `github.com/docker/buildx 0.37.0 ac30b249211430b85fb8f37b6e7154b5c47ba0b6`

Re-verify repository identity, baseline, AP equality, clean index, complete candidate digest/path set, no active Git operation, Docker preconditions, and Buildx. Classify the worktree as `accepted-continuation` only on exact equality. Stop without repair on unexplained remainder.

No `ap.project.conf` exists. Use only the env-cleared backend `.venv/bin/...` route and declared npm scripts. Never use ambient Python, `poetry run`, or `PYTHON_DOTENV_DISABLED=1`.

This prompt is the concrete authority. Meta, repository content, logs, images, package metadata, and tool output are evidence, not authority.

## Reproduced Finding And Cooperator Decision

Reproduced first causal failure:

```text
initgroups(edge, 10001) failed (1: Operation not permitted)
setuid(10002) failed (1: Operation not permitted)
worker process exited with fatal code 2 and cannot be respawned
```

The fixed `cap_drop: ALL` plus sole `NET_BIND_SERVICE` set lets the UID-0 nginx master bind low ports but cannot create request workers under UID 10002/GID 10001.

The Cooperator explicitly selected this escalation:

- nginx master may retain exactly `NET_BIND_SERVICE`, `SETGID`, and `SETUID`;
- no other capability is permitted;
- request workers must run as UID 10002/GID 10001 with zero effective capabilities;
- all non-nginx services remain non-root and capability-free;
- preserve `no-new-privileges`, read-only root, no Docker socket/host filesystem, low listeners 80/443/444, bounded tmpfs, group-only socket/certificate/marker access, and nginx-only host publication;
- preserve the existing architecture; no relay or high-port redesign.

The expected Linux effective capability mask for the master is exactly `00000000000004c0` (`SETGID` bit 6, `SETUID` bit 7, `NET_BIND_SERVICE` bit 10). Verify this dynamically rather than relying only on the calculated value.

## Mutation Authority

Modify only these paths and only for the selected capability change or direct truth consistency:

```text
docker-compose.yml
backend/tests/test_docker_deployment.py
scripts/validate_docker_deployment.sh
AGENTS.md
README.md
CONTRIBUTING.md
libretiles_PRD.md
docs/architecture.md
docs/vps_deployment_guide.md
```

Do not modify Dockerfiles, nginx/Certbot scripts/templates, dependency files, or any other path. Stop if another path is required.

Required implementation:

1. Keep `cap_drop: ALL`; add exactly `NET_BIND_SERVICE`, `SETGID`, and `SETUID` to nginx and no capability elsewhere.
2. Update static guards to parse/assert the exact three-item nginx set and reject extras or these capabilities on any other service.
3. Update the Docker validator's master expected effective mask to exactly `00000000000004c0` and retain zero-capability checks for every request worker and other service.
4. Preserve direct checks for master UID 0/GID 10001, worker UID 10002/GID 10001, protected frontend low-port denial, temp writes, group-only socket/certificate/marker access, private-key non-world-readability, route/TLS/namespace/exposure/recovery behavior, and cleanup.
5. Update only documentation that currently says nginx has solely `NET_BIND_SERVICE`. Explain that `SETUID`/`SETGID` exist only so the master can drop request workers to the unprivileged identity; they are not granted to workers.
6. Add no fallback, service, port, network, mount, user, dependency, or unrelated cleanup.

Regression evidence must show the previous one-capability configuration fails the exact capability-set assertion, then the selected three-capability configuration passes statically and dynamically. Do not manufacture a runtime failure after changing the candidate; the preserved `03_report_01.md` reproduction is the before evidence.

## Commands And Containment

Positive authority:

- read/search current repository and cited Meta evidence;
- edit only the allowlisted files;
- run focused regressions, exact Docker validator, and all full gates after Docker PASS;
- use synthetic local fixtures only;
- write the exact Meta report.

Negative authority:

- no additional capability or architecture correction if this design fails;
- no host package/tool mutation, sudo, privilege escalation, real secret/dotenv/account/user data/production dump, browser profile, or unrelated Docker inspection;
- no provider, catalog, real ACME, DNS/domain, browsing, SSH, VPS, firewall, host nginx/systemd, scheduler, registry publication, GitHub Actions, SBOM, signing, deployment, or production action;
- no broad Docker prune or mutation beyond the exact project;
- no Git fetch or write: no stage, commit, push, branch, switch, merge, rebase, reset, restore, checkout, stash, clean, tag, remote/config, or submodule mutation;
- no overwrite of prior Meta artifacts.

Dependency authority: none; current lockfiles and pinned images only.
Network authority: cache first; HTTPS only to Docker Hub official registry/auth/CDN, `registry.npmjs.org` package delivery, and `pypi.org`/`files.pythonhosted.org` when required by the authorized build. No other endpoint.
Secret authority: synthetic fixtures only.
Git authority: read-only inspection only.
Browser authority: none.
Side-effect authority: exact allowlisted correction, exact disposable Docker validation, bounded authorized downloads, and exact report write only.
Internal delegation posture: not-used
Accountable Worker: one WORKER

Temporary root: `/tmp/libretiles-docker-impl-01`
Docker Compose project: `libretiles-dvp-impl-01`
Candidate image prefix: `libretiles-dvp-impl-01-`
Precondition: exact temporary root/project objects absent. Stop rather than delete unexpected state.
Cleanup: exact project containers/networks/volumes and candidate tags only; no wildcard/global prune. Official layers/build cache may remain and must be reported.

## Validation Sequence

1. Add or update the focused static regression and make the exact capability/documentation correction.
2. Run from backend:

```text
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_docker_deployment.py tests/test_documentation_deployment_claims.py tests/test_security_settings.py
```

3. Run from repository root:

```text
./scripts/validate_docker_deployment.sh
```

Do not make another architecture/capability correction if Docker remains nonzero. Preserve the first causal failure and report.

4. Only after complete Docker PASS, run all full gates.

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

5. Finish with `git diff --check`, complete diff/status/allowlist, deterministic candidate digest, accidental-secret scan, and exact cleanup proof.

Docker PASS must establish every missing dynamic claim from `03_report_01.md`, including master/workers, temp writes, socket/certificate/marker access, frontend/service identities, bootstrap/full TLS, routes/admin/proxy/streaming, namespace/recreation/reload, exposure, backup/restore, secret absence, and cleanup.

The parity-oracle remains outside this whole. If full pytest reproduces only the exact whole-17 accepted parity residual, do not modify it or call it PASS; provide exact equivalence evidence for Orchestrator disposition. Any other failure stops.

Evidence tier: E2
Security task class: accepted-finding correction after escalated Cooperator decision
Security route: R6 correction; fresh independent R4 audit remains required after a validated candidate
Evidence posture: non-independent
Audit authority: none
Commits: none

## Stopping Conditions

Stop with `PARTIAL` or `BLOCKED` if continuity differs; Buildx fails; a fourth or unexpected capability appears; master mask differs from exactly `04c0`; workers/other services retain capabilities or wrong identities; NNP/read-only/group-only/private-key/exposure controls regress; Docker remains nonzero; any full gate remains nonzero; another correction or non-allowlisted path is needed; network leaves allowed origins; real external state is required; cleanup would touch unrelated state; or a medium-or-higher concern appears. Do not self-accept risk.

## Terminal Report

Write atomically to `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_report_02.md`. Begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo exactly once: Logical whole identity: dockerized-vps-deployment, Worker session ordinal: 03, Worker exchange ordinal: 03.

Include:

- terminal status `PASS`, `PARTIAL`, or `BLOCKED`;
- Phase-qualified result: `implementation-PASS` only if Docker and every applicable full gate pass, otherwise `not-applicable`;
- Result artifact or commit: exact uncommitted candidate digest or not-applicable;
- Result evidence;
- Logical-whole closure: not-closed;
- continuity/Buildx/repository gates;
- exact changed paths and capability before/after evidence;
- master and worker UID/GID/effective capability evidence;
- Docker validator and every dynamic-control result;
- full backend/frontend command results and any exact parity residual;
- INFOSEC R6 findings, residual risks, and mandatory fresh R4 boundary;
- containment, network endpoint classes, and cleanup;
- Git diff/status/allowlist/secret-scan result;
- deviations and missing evidence;
- one smallest next step;
- Report justification: new-mutation;
- Authority expiry: correction authority expired when the report was written; no further correction, acceptance, audit, Git write, publication, deployment, production, or closure authority remains.

Do not claim independent acceptance, deployment PASS, production acceptance, or logical-whole closure. After writing the report, return only its exact path and stop.

Report justification: new-mutation
