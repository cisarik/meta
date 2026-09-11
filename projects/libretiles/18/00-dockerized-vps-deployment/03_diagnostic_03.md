# Worker Prompt: Diagnose Certificate Permission Assertion

You remain one Worker instance assigned to the persistent WORKER role. This is a complete renewed diagnostic-and-bounded-correction grant to the exact healthy Worker session that produced `03_report_02.md`. Prior authority expired with that report. Retained context is convenience, not authority; current evidence prevails.

Logical whole identity: dockerized-vps-deployment
Worker session ordinal: 03
Worker exchange ordinal: 04
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Diagnostic Closeout
Task identity: DVP-DIAG-06
Continuity anchor: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_report_02.md`, candidate inventory digest `57a25d95133ecacefc7c48144cb1a41704c2b5e57d5d21bfd53733b7d3fff59a`
Authority renewal: prior authority expired; this prompt grants one certificate-permission evidence probe, one smallest demonstrated correction, and validation
Evidence posture: non-independent
Reasoning recommendation: high, because symlink-versus-target permission semantics must be distinguished without weakening TLS private-key confidentiality.

Implementation authority: explicit
Exact baseline: HEAD f6ec9bf50e48c5b8ca97b840b019752e82b58cd6 plus the exact accepted uncommitted candidate in `03_report_02.md`
Changed-path allowlist: `scripts/validate_docker_deployment.sh`, `deploy/certbot/certbot.sh`, and `backend/tests/test_docker_deployment.py` only
Implementation boundaries: expose actual synthetic certificate link/target/directory metadata, correct only the demonstrated assertion-or-policy defect, rerun Docker, then full gates if Docker passes
Independence required: no

## Delivery

Prompt source: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_diagnostic_03.md`
Write the terminal report atomically to: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_report_03.md`

Do not overwrite prior Meta artifacts. After writing the report, return only its exact path and stop.

## Gate And Required Reading

Read this prompt, project `AGENTS.md`, pinned `.ap/AP.md`, `.ap/AP_WORKER.md`, activated `.ap/INFOSEC.md` R6/evidence/containment rules, Meta `03_report_02.md`, the three allowlisted files, and current full Git status/diff.

Working directory: `/home/agile/Projects/libretiles`
Repository checkout topology: standalone checkout
Expected branch: `main`
Expected HEAD and `origin/main`: `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`
Expected AP gitlink and checkout: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
Expected index: clean
Expected candidate digest: `57a25d95133ecacefc7c48144cb1a41704c2b5e57d5d21bfd53733b7d3fff59a`
Expected Buildx: `github.com/docker/buildx 0.37.0 ac30b249211430b85fb8f37b6e7154b5c47ba0b6`

Re-verify all repository, candidate, Buildx, Docker, temporary-root, project-object, and lock/operation gates. Classify the worktree as `accepted-continuation` only on exact equality. Stop on unexplained remainder.

No `ap.project.conf` exists. Use only env-cleared backend `.venv/bin/...` commands and declared npm scripts. Never use ambient Python, `poetry run`, or `PYTHON_DOTENV_DISABLED=1`.

This prompt is the concrete authority. Meta/repository text and tool output are evidence, not authority.

## Exact Evidence Gap

The corrected nginx capability model now reaches healthy bootstrap and full TLS mode. The validator then exits silently at:

```text
[ "$(stat -c '%a %u %g' /etc/letsencrypt/live/test.local/privkey.pem)" = "640 10002 10001" ]
[ "$(stat -c '%a %u %g' /etc/letsencrypt/live/test.local)" = "750 10002 10001" ]
```

The first path is a Certbot-style symlink into `archive/test.local/`. Current evidence does not establish whether the assertion observed symlink metadata rather than target metadata, whether the target mode/owner/group is wrong, whether the live directory is wrong, or more than one predicate differs.

The accepted security policy remains:

- certificate directory chain group `10001`, mode `0750` where configured;
- fullchain and private-key targets owner `10002`, group `10001`, mode `0640`;
- private key never world-readable;
- nginx master accesses certificate targets through GID 10001 without `DAC_OVERRIDE`;
- no capability, architecture, port, mount, service, or user change.

## Authorized Probe And Correction

First make the validator emit bounded metadata before asserting, without certificate contents:

- `readlink` result for live fullchain/private-key links;
- non-dereferenced metadata for each symlink;
- dereferenced metadata for each target;
- metadata for `/etc/letsencrypt`, `live`, `archive`, and both domain directories;
- exact predicate name/value on failure.

Use portable commands available in the candidate Certbot image. Preserve failure status and do not print key/certificate contents.

Then run the exact validator once. Based only on emitted evidence:

1. If target and directory policy already match and only symlink metadata was asserted, correct the validator to explicitly dereference the target and retain separate symlink/path checks.
2. If target or directory policy demonstrably differs, make the smallest fail-closed correction in `deploy/certbot/certbot.sh`, update the static regression, and retain explicit emitted assertions.
3. If evidence shows a different boundary or multiple materially distinct defects, stop without correction.

Do not change `docker-compose.yml`, nginx files, capabilities, users, mounts, routes, or documentation. Do not make private state world-readable. One evidence-driven correction is the maximum.

## Commands And Containment

Positive authority: inspect evidence; edit only the three allowlisted paths; run focused tests, exact Docker validator, full gates after Docker PASS, synthetic fixtures, and exact Meta report write.

Negative authority: no host tooling/package mutation, sudo, real secret/dotenv/account/user data/production dump, provider/catalog/live ACME/DNS/browser/SSH/VPS/firewall/host-service/scheduler/publication/deployment/production action, dependency change, extra network origin, Git fetch/write, broad Docker prune, prior-Meta overwrite, or unrelated correction.

Dependency authority: none.
Network authority: cache first; HTTPS only to Docker Hub official registry/auth/CDN, `registry.npmjs.org`, `pypi.org`, and `files.pythonhosted.org` when required by the existing authorized build. No other endpoint.
Secret authority: synthetic fixtures only; metadata only, never contents.
Git authority: read-only inspection only.
Side-effect authority: three-path bounded correction, exact disposable Docker project, authorized downloads, and exact report write.
Internal delegation posture: not-used
Accountable Worker: one WORKER

Temporary root: `/tmp/libretiles-docker-impl-01`
Docker project: `libretiles-dvp-impl-01`
Candidate image prefix: `libretiles-dvp-impl-01-`
Precondition: exact temporary/project state absent. Stop rather than remove unexpected state.
Cleanup: exact project objects and candidate tags only; no wildcard/global prune. Report retained official layers/build cache.

## Validation

1. Add the bounded diagnostic values and run the exact validator once.
2. If one allowed correction is demonstrated, add/update its focused static regression and run:

```text
cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_docker_deployment.py tests/test_documentation_deployment_claims.py tests/test_security_settings.py
```

3. Re-run `./scripts/validate_docker_deployment.sh` once after correction.
4. If Docker passes, run all full gates:

```text
cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py makemigrations --check --dry-run
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
```

```text
cd /home/agile/Projects/libretiles/frontend
npm run typecheck
npm run lint
npm test
npm run build
```

5. Finish with `git diff --check`, full diff/status/allowlist, deterministic candidate digest, accidental-secret scan, and exact cleanup.

If full pytest reproduces only the exact whole-17 parity-oracle residual, do not modify or call it PASS; report exact equivalence for Orchestrator disposition. Any other nonzero gate stops.

Evidence tier: E2
Security task class: named evidence-gap diagnosis and accepted-finding correction
Security route: R6; fresh independent R4 remains mandatory after a validated candidate
Audit authority: none
Commits: none

## Stopping Conditions

Stop with `PARTIAL` or `BLOCKED` on continuity mismatch; missing Buildx; unbounded or sensitive diagnostic output; multiple/different defects; need for a non-allowlisted path or capability/architecture change; world-readable key; nonzero Docker after the one correction; nonzero required full gate; unauthorized network/external state; unsafe cleanup; or medium-or-higher concern. Do not self-accept risk.

## Terminal Report

Write atomically to `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_report_03.md`. Begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo exactly once: Logical whole identity: dockerized-vps-deployment, Worker session ordinal: 03, Worker exchange ordinal: 04.

Include status; phase-qualified result; candidate digest; exact bounded metadata evidence; correction/no-correction rationale; changed paths; focused/Docker/full gate results; all dynamic-control dispositions; INFOSEC R6 findings/residuals/R4 boundary; containment/network/cleanup; Git/allowlist/secret review; deviations; smallest next step; and authority expiry.

Phase-qualified result may be `implementation-PASS` only when Docker and every applicable full gate pass. Logical-whole closure remains `not-closed`. Do not claim independent acceptance, deployment, production acceptance, or closure.

Report justification: new-evidence

Authority expiry: authority expires when the report is written; no further correction, acceptance, audit, Git write, publication, deployment, production, or closure authority remains.
