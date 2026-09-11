# Worker Prompt: Fresh Independent Re-Audit of DVP-AUDIT-05-F02 Correction

You are one fresh Worker instance assigned to the persistent WORKER role. You did not implement the candidate or the correction under re-audit, inherit no authority from any prior session, and must establish all evidence independently. This is a complete independent re-audit grant: no correction, no repository mutation.

Logical whole identity: dockerized-vps-deployment
Worker session ordinal: 07
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: Independent Audit
Task identity: DVP-REAUDIT-01
Reasoning recommendation: high, because this re-audit is the independent acceptance boundary for the corrected edge redirect behavior and must confirm that no other accepted control regressed.

Security task class: fresh independent re-audit
Independent of the correction: yes
Correction authority: none
Targets: the DVP-AUDIT-05-F02 correction in `deploy/nginx/entrypoint.sh` (`https://$host` replaced by the literal validated `DOMAIN` in the full-mode port-80 fallback) plus the original risk claim (redirect-target integrity), the preserved bootstrap fail-closed behavior, the 443 canonical-host rejection, and proxy-header overwrite
Verdicts: verified-closed | not accepted, per finding, with evidence
Reporting: security audit report contract

## Delivery

Prompt source: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/07_audit_00.md`
Write the terminal re-audit report atomically to: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/07_report_00.md`

Do not overwrite prior Meta artifacts and do not write anywhere else. After writing the report, return only its exact path and stop.

## Acceptance And Correction Record

```text
Acceptance candidate: corrected uncommitted candidate inventory digest c2d08f489e2bc038899d7633651b856e593d880d8c067cae0a67c019a97437a9 at HEAD f6ec9bf50e48c5b8ca97b840b019752e82b58cd6
Acceptance owner map: deploy/nginx/entrypoint.sh (redirect target); scripts/validate_docker_deployment.sh (dynamic redirect proof); backend/tests/test_docker_deployment.py (causal static guard); all other 42 candidate paths unchanged from digest d554d11be386bdc73f94d2ea6eaa6f396f1a6f35441a477c3a4ce55625ff0900
Acceptance allowlist: the exact 45-path candidate inventory
Acceptance risk claims: port-80 full-mode redirect resolves to the literal validated DOMAIN and never reflects the request Host; bootstrap remains 503 fail-closed; 443 rejects non-canonical hosts with 444; proxy-header overwrite is unchanged; DOMAIN cannot inject sed replacement metacharacters; the corrected digest differs from the previously accepted digest only in the three allowlisted paths
Acceptance control matrix: independent static inspection of the three corrected paths; independent delta reconstruction to the previously accepted digest; one exact Docker validator run; independent port-80 Host probes in full and bootstrap modes; independent 443 rejection and forged-header probes; focused backend suite; full backend and frontend gates
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

## Mandatory Reading

- `/home/agile/Projects/libretiles/AGENTS.md`
- `/home/agile/Projects/libretiles/.ap/AP.md`
- `/home/agile/Projects/libretiles/.ap/AP_WORKER.md`
- `/home/agile/Projects/libretiles/.ap/INFOSEC.md` (sections 4.11, 5–17)
- `/home/agile/Projects/libretiles/.ap/PROMPT_CONTRACTS.md` (Fresh Independent Re-Audit Prompt Contract, Security Finding Record, Containment Ledger, Security Audit Report)
- this complete prompt
- Meta reports as claims to verify, never as trusted conclusions: `05_report_00.md`, `06_report_00.md`
- the three corrected paths and the relevant unchanged edge paths: `deploy/nginx/nginx.conf.template`, `docker-compose.yml`
- current full Git status and diff

## Repository And Continuity Gate

Working directory: `/home/agile/Projects/libretiles`
Repository checkout topology: standalone checkout
Expected branch/HEAD/origin-main: `main`, `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`
Expected AP gitlink and checkout: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
Expected clean index
Expected candidate inventory digest: `c2d08f489e2bc038899d7633651b856e593d880d8c067cae0a67c019a97437a9`, recomputed with the ordered NUL-delimited `git status --porcelain=v1 --untracked-files=all` record plus present-content SHA-256 or `DELETED` marker method
Expected Buildx: `github.com/docker/buildx 0.37.0 ac30b249211430b85fb8f37b6e7154b5c47ba0b6`

Verify root, Git directory, remote, branch, baseline, AP equality, clean index, complete 45-path set, digest, active Git operations/locks, Docker/Buildx, and the absence of the exact temporary root and project objects. Stop on mismatch; a digest mismatch is a stopping condition, not a finding to route around.

No `ap.project.conf` exists. Use only the env-cleared backend `.venv/bin/...` route and declared npm scripts. Never ambient Python, `poetry run`, or `PYTHON_DOTENV_DISABLED=1`.

## Re-Audit Requirements

1. Independently verify the three-path delta claim: inspect the exact diff of `deploy/nginx/entrypoint.sh`, `scripts/validate_docker_deployment.sh`, and `backend/tests/test_docker_deployment.py`; then, in a temporary staging area outside the canonical repository, reverse only those three corrections and recompute the candidate inventory digest. The reconstruction must equal `d554d11be386bdc73f94d2ea6eaa6f396f1a6f35441a477c3a4ce55625ff0900`; report the exact result. If it does not match, stop with `BLOCKED` and report the first divergent path.
2. Inspect the corrected entrypoint render logic directly. Verify with the exact sed expressions that full mode renders `return 301 https://<literal DOMAIN>$request_uri;`, that `$request_uri` remains an nginx variable, that no `https://$host` fallback remains anywhere, and that bootstrap still renders `return 503;`.
3. Verify injection safety independently: confirm the `DOMAIN` validation character class rejects every sed replacement metacharacter and that no new substitution layer exists.
4. Run the exact Docker validator once under the exact disposable containment and capture its full output. Independently inspect the new validator assertions for tautology or self-reference.
5. Run independent port-80 Host probes in full mode with at least `Host: test.local` and a hostile non-canonical `Host`; confirm both return `301` with `Location` beginning `https://test.local/` and never the hostile host. Confirm bootstrap mode still returns `503` for an application request. Confirm 443 rejects a non-canonical host. Confirm forged forwarding headers do not change origin behavior.
6. Run the focused backend suite `tests/test_docker_deployment.py tests/test_documentation_deployment_claims.py tests/test_security_settings.py`, the backend full gates (`mypy`, `ruff`, `makemigrations --check`, `pytest`), and the frontend gates (`typecheck`, `lint`, `test`, `build`). The whole-17 parity-oracle residual and the two declared pre-existing frontend test reds remain baseline residuals: restate them, do not modify or re-label them.
7. Return per-finding verdicts. For DVP-AUDIT-05-F02 the verdict is `verified-closed` only if the corrected behavior is directly reproduced and injection-safe; otherwise `not accepted` with the disproving evidence. State the residual-risk summary for the Orchestrator.
8. Do not correct anything and do not modify the candidate. Any further change requires a separate Orchestrator grant and another fresh re-audit.

## Threat Model

- Assets: user trust in the operator redirect, edge fail-closed availability, canonical-host integrity, proxy trust, and the accepted candidate's other controls.
- Trust boundaries: internet to nginx port 80/443; nginx to the shared frontend namespace; nginx to Django over the Unix socket; operator DOMAIN value into the rendered configuration.
- Attacker-controlled inputs or local actor: the `Host` header and forwarding headers on plaintext HTTP; a hostile hosted domain name; a malformed operator domain would be an operator error, not attacker input.
- Security properties relied on: literal-domain redirect target, bootstrap fail-closed, 443 canonical-host rejection, strict proxy-header overwrite, and no sed/configuration injection from the validated domain.
- Abuse cases: host-reflection redirection, fallback regex mis-substitution leaving `$host`, domain injection into the rendered directive, loss of bootstrap `503`, or regression of the 443 rejection or proxy overwrite.

## Containment

Temporary root: an audit-owned root under the permitted client write area, mode `0700`, synthetic fixtures only; the declared name is `libretiles-reaudit-07-01`, and if the client policy denies that exact path, record the deviation and use the permitted equivalent under `/tmp/opencode/`
Docker Compose project: `libretiles-reaudit-07-01`
Audit image tag prefix: `libretiles-reaudit-07-01-`
The exact validator uses its own hardcoded project/root identities; do not modify the script to change them, and verify its internal temporary root and project are clean afterward
Cleanup owner: this re-audit session before the terminal report
Cleanup: exact audit/validator containers, networks, volumes, tags, and temporary roots only; no wildcard or global prune; report retained official layers/cache; never touch unrelated pre-existing Docker objects (`libretiles-postgres-1`, `libretiles-redis-1`, `libretiles_pgdata`, `libretiles_default`)
Evidence handling: synthetic values only; report metadata, statuses, and header values; never secret or private-key contents

Positive authority: read-only repository/Git/Docker inspection; one exact validator run; bounded independent probes and synthetic fixtures; temporary reconstruction outside the repository; full project gates; exact report write.

Negative authority: no repository or Meta mutation other than the exact report; no correction; no real secret/dotenv/account/user data; no host mutation, sudo, package install, or privilege escalation; no provider/catalog/real ACME/DNS/browser/SSH/VPS/firewall/host-service/publication/deployment/production action; no dependency or lockfile change; no Git fetch/write; no broad Docker prune; no unrelated Docker object inspection or removal.

Dependency authority: none.
Network authority: cache first; HTTPS read/download only to Docker Hub official registry/auth/CDN, `registry.npmjs.org`, `pypi.org`, and `files.pythonhosted.org` when an existing build cannot proceed from cache. No other endpoint.
Secret authority: synthetic fixtures only; values never emitted.
Git authority: read-only inspection only.
Browser authority: none.
Internal delegation posture: not-used
Accountable Worker: one WORKER

Evidence tier: E2 corrected candidate with required fresh independent re-acceptance; R5 host hardening remains deferred and out of scope.

## Stopping Conditions

Stop and report `PARTIAL` or `BLOCKED` if the repository/candidate/digest gate fails; the delta reconstruction diverges; the corrected behavior cannot be reproduced; a probe needs real secrets, host state, privilege escalation, or an unauthorized endpoint; a probe would mutate the repository or unrelated Docker state; the validator cannot run under the exact containment; cleanup would touch unrelated state; or a new medium-or-higher finding appears. Report the exact blocker, preserved evidence, and smallest safe next step. Do not correct or reinterpret evidence.

## Terminal Report

Write atomically to `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/07_report_00.md`. Begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo exactly once: Logical whole identity: dockerized-vps-deployment, Worker session ordinal: 07, Worker exchange ordinal: 01.

Include:

- terminal status `PASS`, `PARTIAL`, or `BLOCKED`;
- Phase-qualified result: `acceptance-PASS` only if the corrected candidate passes the re-audit control matrix with no acceptance-blocking finding; otherwise `not-applicable`;
- Result artifact or commit: exact audited digest `c2d08f48...`, or not-applicable;
- Result evidence;
- Logical-whole closure: not-closed;
- verified repository/candidate/digest gate and the exact three-path delta reconstruction result;
- per-finding verdict for DVP-AUDIT-05-F02 (`verified-closed` or `not accepted` with evidence);
- independent rendered-fallback, port-80 Host, bootstrap, 443 rejection, and proxy-overwrite evidence;
- independent validator assessment, including tautology inspection and the new redirect assertions;
- project-gate results with baseline residuals restated, not re-labelled;
- containment ledger with cleanup outcomes;
- limitations and unverifiable items;
- residual-risk summary;
- out-of-scope observations as ledger candidates;
- one smallest next step (publication decision remains ORCHESTRATOR/COOPERATOR-owned);
- Report justification: new-evidence;
- Authority expiry: re-audit authority expires when the report is written; no correction, Git write, publication, deployment, production, or closure authority remains.

The re-auditor must not modify the candidate, must not self-certify a correction, and must not claim deployment PASS, production acceptance, or logical-whole closure.

Report justification: new-evidence
