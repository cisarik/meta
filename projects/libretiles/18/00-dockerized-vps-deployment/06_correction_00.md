# Worker Prompt: Correct Canonical Port-80 Redirect Target

You are one fresh Worker instance assigned to the persistent WORKER role. This is a complete fresh-session correction grant for the accepted audit finding DVP-AUDIT-05-F02 in logical whole `dockerized-vps-deployment`. You inherit no authority or trusted private context from prior sessions; their reports are evidence only. Re-establish all repository and environment facts independently before mutation.

Logical whole identity: dockerized-vps-deployment
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Implementation
Task identity: DVP-CORRECT-13
Reasoning recommendation: high, because the correction touches the edge redirect/security behavior and must preserve bootstrap fail-closed behavior, canonical-host rejection, proxy-header overwrite, and the full deployment validator.

Implementation authority: explicit
Exact baseline: HEAD f6ec9bf50e48c5b8ca97b840b019752e82b58cd6 plus the accepted uncommitted candidate recorded by Meta `05_report_00.md`, inventory digest `d554d11be386bdc73f94d2ea6eaa6f396f1a6f35441a477c3a4ce55625ff0900`
Changed-path allowlist: `deploy/nginx/entrypoint.sh`, `scripts/validate_docker_deployment.sh`, `backend/tests/test_docker_deployment.py`
Implementation boundaries: fix only the non-canonical port-80 full-mode redirect target, add its causal regression, then complete the Docker validator and all project gates
Independence required: no

## Delivery

Prompt source: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/06_correction_00.md`
Write the terminal report atomically to: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/06_report_00.md`

Do not overwrite prior Meta artifacts. After writing the report, return only its exact path and stop.

## Mandatory Reading

- `/home/agile/Projects/libretiles/AGENTS.md`
- `/home/agile/Projects/libretiles/.ap/AP.md`
- `/home/agile/Projects/libretiles/.ap/AP_WORKER.md`
- `/home/agile/Projects/libretiles/.ap/INFOSEC.md` (correction/re-audit separation, residual-risk rules)
- this complete prompt
- Meta reports as historical evidence only: `04_report_00.md`, `05_report_00.md`
- the three allowlisted files before editing
- current full Git status and diff

## Repository And Continuity Gate

Working directory: `/home/agile/Projects/libretiles`
Repository checkout topology: standalone checkout
Expected branch/HEAD/origin-main: `main`, `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`
Expected AP gitlink and checkout: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
Expected clean index
Expected candidate inventory digest: `d554d11be386bdc73f94d2ea6eaa6f396f1a6f35441a477c3a4ce55625ff0900` under the established ordered NUL-delimited porcelain-record plus present-content-hash/deleted-marker method
Expected Buildx: `github.com/docker/buildx 0.37.0 ac30b249211430b85fb8f37b6e7154b5c47ba0b6`

Re-verify root, Git directory, remote, branch, baseline, AP equality, clean index, complete 45-path candidate set, digest, active Git operations/locks, Docker/Buildx, and absence of the exact temporary root and Docker project objects. Classify as `accepted-continuation` only on exact equality. Stop on unexplained remainder.

No `ap.project.conf` exists. Use only the env-cleared backend `.venv/bin/...` route and declared npm scripts. Never ambient Python, `poetry run`, or `PYTHON_DOTENV_DISABLED=1`.

## Accepted Finding

Finding ID: DVP-AUDIT-05-F02
Title: Full-mode HTTP redirect reflects the request Host value
Severity: info
Status: open, non-blocking
Evidence: in full TLS mode, the port-80 fallback renders `return 301 https://$host$request_uri;`, so `Host: evil.local` receives `Location: https://evil.local/some/path`. The 443 server already rejects non-canonical hosts with `444`, and bootstrap mode returns `503`; no browser-redirection exploit was established.
Required correction direction: the full-mode port-80 redirect target must use the literal validated `DOMAIN` value, not the request `$host`.

## Correction Authority

Modify only:

```text
deploy/nginx/entrypoint.sh
scripts/validate_docker_deployment.sh
backend/tests/test_docker_deployment.py
```

Required correction:

1. In `deploy/nginx/entrypoint.sh`, change only the full-mode `__HTTP_FALLBACK__` substitution so the rendered directive is `return 301 https://<validated DOMAIN>$request_uri;` with the operator `DOMAIN` value embedded literally and `$request_uri` preserved as an nginx variable.
2. Do not rely on a second sed pass over a substitution result: sed applies `-e` expressions sequentially per line, so a domain placeholder introduced by the fallback replacement would not be re-expanded. Embed the shell `${DOMAIN}` value directly in the fallback replacement with correct quoting so `$request_uri` survives to the rendered configuration.
3. Preserve exactly: bootstrap mode `503` fail-closed behavior; `server_name __DOMAIN__`; the 443 `if ($host != __DOMAIN__) return 444;` rejection; all proxy header overwrite behavior; TLS modes; the reload watcher; the domain validation that rejects `example.invalid`, wildcards, and illegal characters.
4. Verify that a validated `DOMAIN` cannot inject sed replacement metacharacters (`&`, `\`, delimiter) into the rendered configuration; the existing `validate_domain()` character set plus `sed` replacement semantics must be sufficient, and the correction must not add a new injection path.
5. Add a causal static regression in `backend/tests/test_docker_deployment.py` that fails against the current `$host` fallback and passes after: assert the full-mode fallback renders the literal domain, that no `https://$host` fallback remains, and that bootstrap `503` and the 443 host rejection are preserved.
6. Extend `scripts/validate_docker_deployment.sh` to assert dynamically, in full mode, that a port-80 request with a non-canonical `Host` returns `301` with a `Location` beginning `https://test.local/` (the exact configured domain), never the attacker Host; keep the existing bootstrap and route assertions.
7. Do not change any other file, template, Compose definition, capability, secret, port, or documentation claim.

Regression-test requirement: the new guard must fail before the fix and pass after; the exact Docker validator must prove both canonical and non-canonical port-80 full-mode redirect targets.

## Commands And Containment

Positive authority: edit only the three allowlisted paths; focused backend tests; exact Docker validator; one corrected rerun; all full gates after Docker PASS; synthetic fixtures; exact Meta report.

Negative authority: no other path; no dependency/lockfile change; no capability/privilege/service/network/port change; no real secret/dotenv/account/data; no host mutation/sudo; no provider/catalog/ACME/DNS/browser/SSH/VPS/firewall/host-service/publication/deployment/production action; no Git fetch/write; no broad Docker prune; no prior-Meta overwrite; no unrelated correction.

Dependency authority: none.
Network authority: cache first; HTTPS only to Docker Hub official registry/auth/CDN, `registry.npmjs.org`, `pypi.org`, and `files.pythonhosted.org` when required by existing builds.
Secret authority: synthetic fixtures only; values never emitted.
Git authority: read-only inspection only.
Side-effect authority: the three-path bounded correction, exact disposable Docker project, and exact report write.
Internal delegation posture: not-used
Accountable Worker: one WORKER

Temporary root: `/tmp/libretiles-docker-impl-01`
Docker project: `libretiles-dvp-impl-01`
Candidate image prefix: `libretiles-dvp-impl-01-`
Precondition: exact temporary/project state absent. Stop on unexpected state.
Cleanup: exact helper/project containers, networks, volumes, tags, and temporary root only. No wildcard/global prune. Report retained official layers/cache.

## Validation Sequence

1. Add the causal static regression; confirm it fails against the current fallback.
2. Apply the correction; run from `/home/agile/Projects/libretiles/backend`:

```text
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_docker_deployment.py tests/test_documentation_deployment_claims.py tests/test_security_settings.py
```

3. Run the exact Docker validator from the repository root:

```text
./scripts/validate_docker_deployment.sh
```

If Docker remains nonzero, preserve first causal logs and stop; do not make a second materially distinct correction.

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

The whole-17 parity-oracle backend residual and the two declared pre-existing frontend test reds remain baseline residuals: do not modify them, do not re-label them PASS, and report their exact equivalence as before. Any other nonzero gate stops.

5. Finish with `git diff --check`, complete diff/status/allowlist, deterministic candidate digest, accidental-secret scan, and exact Docker cleanup proof.

Post-acceptance boundary: this correction changes runtime edge behavior, so a fresh independent re-audit is mandatory before publication or closure. Do not commit, push, or claim acceptance.

Evidence tier: E2
Security task class: post-acceptance correction of an info finding
Security route: R6 bounded correction; fresh independent re-audit required after the corrected candidate
Audit authority: none
Commits: none

## Stopping Conditions

Stop with `PARTIAL` or `BLOCKED` on continuity mismatch; any non-allowlisted change; domain-injection risk into the rendered configuration; loss of bootstrap fail-closed, canonical-host rejection, or proxy-header behavior; Docker/full-gate failure; unauthorized network/external state; unsafe cleanup; or a medium-or-higher concern. Do not self-accept risk.

## Terminal Report

Write atomically to `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/06_report_00.md`. Begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo exactly once: Logical whole identity: dockerized-vps-deployment, Worker session ordinal: 06, Worker exchange ordinal: 01.

Include status; phase-qualified result; candidate digest; exact changed paths; rendered before/after fallback evidence; preserved bootstrap/host-rejection/proxy behavior; focused/Docker/full gate results; every dynamic-control disposition including the new canonical redirect assertion; INFOSEC R6 findings, residual risks, and the mandatory fresh re-audit boundary; containment/network/cleanup; Git/allowlist/secret review; deviations; smallest next step; and authority expiry.

Phase-qualified result may be `implementation-PASS` only if Docker and every applicable full gate pass. Logical-whole closure remains `not-closed`. Do not claim acceptance, publication, deployment, production acceptance, or closure.

Report justification: new-mutation

Authority expiry: correction authority expires when the report is written; no further correction, acceptance, audit, Git write, publication, deployment, production, or closure authority remains.
