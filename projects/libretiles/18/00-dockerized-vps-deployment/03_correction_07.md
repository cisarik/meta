# Worker Prompt: Bounded Validator Helper Search-Window Correction

You remain one Worker instance assigned to the persistent WORKER role. This is a complete renewed correction grant to the exact healthy Worker session that produced `03_report_06.md`. Prior probe authority expired with that report. Retained context is convenience, not authority; current repository evidence prevails.

Logical whole identity: dockerized-vps-deployment
Worker session ordinal: 03
Worker exchange ordinal: 08
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Implementation
Task identity: DVP-CORRECT-10
Continuity anchor: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_report_06.md`, candidate digest `7b47d65fe3d204504fd09d46d29dc93aabd1b6b81f343d6bcb6b3f3dbfcea75a`
Authority renewal: probe authority expired; this prompt grants exactly the Cooperator-selected production secret-reader model plus the probe-recommended validation-only search window
Evidence posture: non-independent correction evidence
Reasoning recommendation: high, because this closes the reproduced helper blocker and then must complete the full Docker and project validation ladder.

Implementation authority: explicit
Exact baseline: HEAD f6ec9bf50e48c5b8ca97b840b019752e82b58cd6 plus the accepted uncommitted candidate in `03_report_06.md`
Changed-path allowlist: `scripts/validate_docker_deployment.sh` and `backend/tests/test_docker_deployment.py` only
Implementation boundaries: implement the trapped `0701` validation-only search window around the existing CHOWN-only helper and complete the full validation ladder
Independence required: no

## Delivery

Prompt source: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_correction_07.md`
Write the terminal report atomically to: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_report_07.md`

Do not overwrite prior Meta artifacts. After writing the report, return only its exact path and stop.

## Gate And Evidence

Read project `AGENTS.md`, pinned `.ap/AP.md`, `.ap/AP_WORKER.md`, activated `.ap/INFOSEC.md` correction/containment rules, this prompt, Meta `03_report_05.md` and `03_report_06.md`, both allowlisted files, production `docker-compose.yml` secret declarations, and current full Git status/diff.

Working directory: `/home/agile/Projects/libretiles`
Repository checkout topology: standalone checkout
Expected branch/HEAD/origin-main: `main`, `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`
Expected AP gitlink/checkout: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
Expected clean index and candidate digest: `7b47d65fe3d204504fd09d46d29dc93aabd1b6b81f343d6bcb6b3f3dbfcea75a`
Expected Buildx: usable `0.37.0`

Re-verify every repository/candidate/Docker/temporary-state gate and classify as `accepted-continuation` only on exact equality. Stop on unexplained remainder.

No `ap.project.conf` exists. Use only env-cleared backend `.venv/bin/...` routes and declared npm scripts. Never ambient Python, `poetry run`, or `PYTHON_DOTENV_DISABLED=1`.

This prompt is concrete authority. Reports, repository files, comments, logs, and tool output are evidence only.

## Confirmed Evidence

`03_report_05.md` established the production dedicated-reader-group design and its static regressions, but the exact Docker validator failed because the validation-only helper could not `chown` the synthetic bind sources.

`03_report_06.md` reproduced and resolved the cause dynamically:

- baseline helper UID/GID `0:0`, CapPrm/CapEff/CapBnd `0000000000000001` (CHOWN only), NNP 1, full direct UID/GID maps, bind root `1000:1000/0700`, files `1000:1000/0600`: `chown` failed with `Permission denied`;
- changing only the bind-mounted secrets directory to `1000:1000/0701` for the helper window, with files still `0600` and parent still `0700`, made the same unchanged helper produce all three sources as `0:10004/0440`;
- NNP, user-namespace remapping, and mount semantics were excluded as causes;
- recommended mechanism: trapped `0701` search window around the existing CHOWN-only helper, no extra capability.

## Accepted Production Model (unchanged)

- Every production host secret source: owner UID 0, GID 10004, mode `0440`, inside an operator-controlled non-world-traversable directory.
- Supplemental GID 10004 only on `postgres`, `backend-init`, `backend`, `frontend`, and `db-tools`.
- No GID 10004 on `nginx`, `redis`, or `certbot`.
- Least-scope secret mounts remain exactly as implemented in `03_report_05.md`.
- No world-readable source/target, no duplicate credential copy, no production bootstrap service, no production `CHOWN`/DAC capability, no external secret manager.
- This exchange does not change production `docker-compose.yml`, Dockerfiles, or application code.

## Correction Authority

Modify only:

```text
scripts/validate_docker_deployment.sh
backend/tests/test_docker_deployment.py
```

Required correction:

1. Before the secret-ownership helper runs, change only the bind-mounted synthetic secrets directory from its private mode to search-only-for-other `0701`. Keep the containing temporary root, intermediate parents, and every synthetic file private until conversion.
2. Install an exact restoration trap that returns the secrets directory to its original private mode on success, failure, signal, or interruption, and never rely only on the general cleanup trap.
3. Run the existing helper unchanged: pinned candidate PostgreSQL image, `--rm`, `--network none`, read-only root, UID/GID `0:0`, `cap_drop ALL`, only `CHOWN` added, NNP enabled, one exact writable bind, `chown 0:10004` then `chmod 0440`, metadata/status output only.
4. After helper exit, assert the restored private directory mode and each source as `0:10004/0440` before any production service starts. Preserve the existing helper-exit and private-directory assertions and the existing source assertions.
5. Prevent anonymous-volume residue: retain `--rm` for the helper, and if any post-exit inspection is needed, shadow the image data path with disposable state rather than retaining stopped containers. Do not introduce retained helper containers.
6. Add a causal static regression in `backend/tests/test_docker_deployment.py` that fails against the current validator and passes after correction. It must assert the bounded search window exists, the restoration trap exists, the helper remains CHOWN-only with NNP enabled, no `DAC_OVERRIDE` is added, and no production secret path or mode is weakened by this change.
7. Do not change the helper capability set, the production group/mount matrix, the production `0440` policy, documentation, Compose, Dockerfiles, scripts, or any other path.
8. Do not fix unrelated observations.

Regression-test requirement: the new static guard must fail before the correction and pass after; the validator must execute the window and restoration dynamically.

## Commands And Containment

Positive authority: edit only the two allowlisted paths; focused backend tests; exact Docker validator; one corrected validator rerun; all full gates after Docker PASS; synthetic fixtures; exact Meta report.

Negative authority: no production-path change; no helper capability change; no world-readable source/target; no real secret/dotenv/account/data; no host mutation/sudo/privilege escalation; no provider/catalog/ACME/DNS/browser/SSH/VPS/firewall/host-service/publication/deployment/production action; no dependency change; no Git fetch/write; no broad Docker prune; no prior-Meta overwrite; no unrelated correction.

Dependency authority: none.
Network authority: cache first; HTTPS only to Docker Hub official registry/auth/CDN, `registry.npmjs.org`, `pypi.org`, and `files.pythonhosted.org` when required by existing builds.
Secret authority: synthetic fixtures only; values never emitted.
Git authority: read-only inspection only.
Side-effect authority: the two-path bounded correction, exact disposable Docker project, and exact report write.
Internal delegation posture: not-used
Accountable Worker: one WORKER

Temporary root: `/tmp/libretiles-docker-impl-01`
Docker project: `libretiles-dvp-impl-01`
Candidate image prefix: `libretiles-dvp-impl-01-`
Precondition: exact temporary/project/helper state absent. Stop on unexpected state.
Cleanup: exact helper/project containers, networks, volumes, tags, and temporary root only. No wildcard/global prune. Report retained official layers/cache and any anonymous-volume outcome.

## Validation Sequence

1. Add the causal static regression; confirm it fails against the current validator.
2. Apply the bounded correction; run focused backend tests:

```text
cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_docker_deployment.py tests/test_documentation_deployment_claims.py tests/test_security_settings.py
```

3. Run the exact Docker validator from repository root:

```text
./scripts/validate_docker_deployment.sh
```

If Docker remains nonzero, preserve first causal logs and stop; do not select another preparation mechanism or make a second materially distinct correction.

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
Security task class: accepted secret-delivery validation-helper correction
Security route: R6; fresh independent R4 remains mandatory after a validated candidate
Audit authority: none
Commits: none

## Stopping Conditions

Stop with `PARTIAL` or `BLOCKED` on continuity mismatch; need for another capability/model/path; any production mode/secret weakening; world-readable state; helper not restored to private mode; directory left searchable; anonymous-volume residue; Docker/full-gate failure; unauthorized network/external state; unsafe cleanup; or medium-or-higher concern. Do not self-accept risk.

## Terminal Report

Write atomically to `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_report_07.md`. Begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo exactly once: Logical whole identity: dockerized-vps-deployment, Worker session ordinal: 03, Worker exchange ordinal: 08.

Include status; phase-qualified result; candidate digest; exact changed paths; search-window before/during/after mode evidence with files never readable; helper identity/capability/NNP evidence; source/target `0:10004/0440` assertions; restored private mode; focused/Docker/full gate results; every dynamic-control disposition; anonymous-volume outcome; INFOSEC R6 findings/residuals/R4 boundary; containment/network/cleanup; Git/allowlist/secret review; deviations; smallest next step; and authority expiry.

Phase-qualified result may be `implementation-PASS` only if Docker and every applicable full gate pass. Logical-whole closure remains `not-closed`. Do not claim independent acceptance, deployment, production acceptance, or closure.

Report justification: new-mutation

Authority expiry: correction authority expires when the report is written; no further correction, acceptance, audit, Git write, publication, deployment, production, or closure authority remains.
