# Kronika one product — S3 NUC capture foundation (repository grant)

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S3-REPO
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: deployment tooling and a systemd-credential boundary that must stay loopback-only and must never couple capture to the web service's restart; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Session declaration

This must be a genuinely fresh session that did not implement or correct S2.
Declare your actual session and independence posture in the report. Read the
accepted plan and prior reports as evidence, not authority. This grant is
repository-only: no host, NUC, SSH, browser, login or provider execution.

## Starting state (verified at issuance)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `82a6a59803ed8830c19e51cd8f9bc1665c28a975`, parent
  `5259b89a9af993e94f00c03e7962681c8ba152a4`, tree
  `190338dde238c414cf4e80999b29b18797d4f72d`, subject
  `fix(capture): correct queued waits and oversized result delivery`; clean
  index and worktree.
- Local `main` = `origin/main` =
  `26d28b16c08a5e7e0179a32c16646bfdc1009c81` (unmoved); no remote branch for
  `feat/kronika-one-product`.
- Governing AP gitlink and detached `.ap` HEAD:
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- The release engine is `deploy/ubuntu/framenest_release.py` (standard library
  only) behind `deploy/ubuntu/framenest-release`; current subcommands are
  `status`, `check`, `deploy`, `rollback` plus hidden `_remote` operations.
  Existing NUC contract tests live under `tests/contract/test_nuc_*.py`.
- Capture token today comes from `<state-dir>/token`; the CLI already accepts
  an explicit `--state-dir`.
- `private/**` contains key material and is never read.

## Implementation authority record

Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: `82a6a59803ed8830c19e51cd8f9bc1665c28a975`
Changed-path allowlist:

```text
deploy/ubuntu/framenest-release
deploy/ubuntu/framenest_release.py
deploy/ubuntu/README.md
deploy/systemd/kronika-capture.env.example            (new)
deploy/systemd/kronika-capture-xvfb.service           (new)
deploy/systemd/kronika-capture-bridge.service         (new)
deploy/systemd/kronika-capture-runner.service         (new)
deploy/systemd/kronika-capture-vnc.service            (new)
deploy/systemd/kronika-capture-view.service           (new)
docs/UBUNTU_NUC_DEPLOYMENT.md
tests/contract/test_nuc_release_source_contract.py
tests/contract/test_nuc_release_docs.py
tests/contract/test_nuc_release_remote_contract.py
tests/contract/test_nuc_operator_runbook.py
tests/contract/test_kronika_capture_services.py       (new)
src/kronika_capture/config.py
src/kronika_capture/paths.py
src/kronika_capture/bridge/auth.py
src/kronika_capture/cli.py
tests/unit/chatgpt_page/**
```

The four `src/kronika_capture/*.py` paths are allowed only for the bounded
credential/launcher integration described below; no other capture behavior may
change.
Implementation boundaries: the positive and negative authority below.
Independence required: no

## Goal

Make the accepted capture runtime installable and supervizable separately from
the web service using the existing release infrastructure: source systemd units
and a non-secret environment template for the persistent browser, bridge,
runner and on-demand operator view; an explicit configured Chromium executable;
systemd-credential token delivery; and an extension of the existing release
helper that carries capture-runtime identity and an explicit capture activation
operation. Repository sources only; no host contact.

## Governing decisions (accepted plan; do not reopen)

Paths and ownership (from plan section 7.2):

```text
Account:                 kronika-capture
Private state:           /var/lib/kronika-capture
Profile:                 /var/lib/kronika-capture/profile
Journal:                 /var/lib/kronika-capture/capture-journal.sqlite3
Staging:                 /var/lib/kronika-capture/staging
Runtime directory:       /run/kronika-capture
Nonsecret configuration: /etc/kronika-capture/capture.env
Capture release pointer: /opt/framenest/capture-current
Existing web pointer:    /opt/framenest/current
```

Unit and credential rules (from plan section 7.2):

- Source units: `kronika-capture-xvfb.service`,
  `kronika-capture-bridge.service`, `kronika-capture-runner.service`,
  `kronika-capture-vnc.service`, `kronika-capture-view.service`.
- Xvfb and runner have no automatic restart loop.
- The bridge may restart independently; the runner reconnects.
- No `PartOf=framenest.service` coupling for capture.
- Runner and Xvfb share the required display socket and a restricted
  Xauthority; avoid incompatible private `/tmp` namespaces. Do not use
  unauthenticated `-ac`.
- Browser debugging remains loopback-only.
- VNC/noVNC are normally stopped, loopback-only and time-limited to at most
  30 minutes.
- Default view ports are 5900 and 6080; a preflight collision stops setup
  rather than silently selecting a public or random listener.
- The Cooperator opens the view through an SSH tunnel; agents never view
  authentication screens or enter credentials.
- The per-install bridge token is created by the authorized setup mechanism and
  delivered to the web, bridge and runner using systemd credentials. Never
  place the token in frontend configuration, command-line arguments or logs,
  and never grant the web account access to the browser profile through a
  shared state-reading group.
- Use an explicitly configured, preflight-verified Chromium executable; no
  stealth and no sandbox weakening.
- Only non-secret configuration belongs in `/etc/kronika-capture/capture.env`.

Release-helper rules (from plan section 7.3):

- Keep `deploy/ubuntu/framenest-release` the sole entry point and preserve its
  pinned deployment tooling.
- Extend release manifests with capture-runtime identity derived from the
  packaged capture code/assets, the relevant installed runtime dependencies,
  and the capture unit/runtime configuration contracts.
- Normal web deploy/rollback changes only the web pointer and service.
- Add an explicit capture activation option to the same helper. It must:
  (1) verify the exact accepted release and a compatible bridge protocol;
  (2) drain active capture work and refuse a live or paused job;
  (3) enforce the restart brake;
  (4) switch `capture-current` and perform one planned runner/browser restart;
  (5) verify readiness without automatically retrying a failed browser launch.
- Retain any release referenced by either active pointer; report both SHAs.
- A web rollback must not downgrade or restart capture. Capture rollback is a
  separate deliberate transition subject to the same brake.
- Preserve the existing `migration-required` continuation; the helper must not
  perform implicit schema migrations or database deletion.

## Required outputs

1. The five capture unit sources and the non-secret
   `deploy/systemd/kronika-capture.env.example` template, consistent with the
   existing `deploy/systemd/` conventions, with the restart, loopback,
   credential, display and view-time rules above.
2. The bounded capture credential/launcher integration: the bridge and runner
   can obtain the token from the systemd credentials directory when systemd
   provides it, falling back to the existing behavior otherwise. Keep token
   entropy, constant-time comparison, Host/Origin checks, protocol, lifecycle
   and error semantics unchanged. If the systemd credential mechanism cannot be
   integrated with a smaller change, stop and report.
3. The release-helper extension: capture-runtime identity in the release
   manifest, the explicit capture activation operation with the five steps
   above, dual-pointer retention/reporting, and the web/capture separation.
   Standard library only; no new dependency.
4. Updated deployment documentation: `docs/UBUNTU_NUC_DEPLOYMENT.md` and
   `deploy/ubuntu/README.md` describing the capture units, paths, credential
   delivery, view procedure and the capture activation/rollback rules, without
   claiming that capture is already deployed.
5. Tests: update the four existing `tests/contract/test_nuc_*.py` contracts for
   the extension and add `tests/contract/test_kronika_capture_services.py`
   covering at least: unit sources parse and contain the required directives
   (no `PartOf=framenest.service`, no auto-restart for Xvfb/runner, loopback
   ports, credential loading, 30-minute view limit); the env template contains
   no secret and matches the documented paths; the helper's capture activation
   refuses live/paused work, enforces the brake, switches `capture-current`,
   performs exactly one planned restart, verifies readiness without automatic
   retry, and reports both pointers' SHAs; web rollback leaves capture
   untouched; the credential integration tests under
   `tests/unit/chatgpt_page/**`.

## Positive authority

Edit exactly the allowlisted paths; stage exactly those paths; create one
commit on `feat/kronika-one-product`. Run the declared route checks below.

Commands (binding route):

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 82a6a59803ed8830c19e51cd8f9bc1665c28a975

./.ap/ap exec --root /home/agile/Projects/framenest --baseline 82a6a59803ed8830c19e51cd8f9bc1665c28a975 --operation test-focus -- tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py tests/contract/test_kronika_capture_services.py tests/unit/chatgpt_page tests/unit/test_import_boundaries.py tests/unit/test_package_import.py tests/unit/test_api_import_boundary.py -q -p no:cacheprovider
```

No ambient Python, `poetry run` or substitute route. No `node --test` suite is
affected in this slice unless a changed capture path requires it; if it does,
run only the directly affected existing Node suite and say why.

## Negative authority

- No host, NUC, SSH, deployment, service, account, filesystem or privilege
  operation. Do not connect to the NUC.
- No browser, login, provider or credential use; no real token creation; the
  credential integration is source-level only and must be covered by synthetic
  tests.
- No S4–S10 work: no Search/Research restoration, no attachment upload, no
  records/migrations/API/UI, no application capture client, no public
  renaming.
- No change to the S2 lifecycle/wire semantics, error codes, protocol version,
  token entropy, Host/Origin checks or journal behavior.
- No dependency, lockfile, project identity, version, AGENTS.md, README.md,
  SERVER.md, ADR or managed-block change.
- No push, force, amend, rebase, reset, clean, stash, `git add -A`,
  `--no-verify` or config write. Do not read `private/**`. No subagents.
- Do not claim that capture is deployed or that host preflight passed.
- If a required change falls outside the allowlist, stop and report.

## Validation

1. `./.ap/ap project check` passes before mutation and after the commit against
   the exact baseline.
2. The declared focused route passes; report the observed counts.
3. New capture-service contract tests prove the unit directives, env template,
   helper capture-activation behavior and web/capture separation.
4. Credential integration tests prove systemd-credential sourcing when present,
   existing fallback otherwise, and unchanged authentication semantics.
5. `git diff --name-status <baseline>..HEAD` equals the allowlist; worktree
   clean after the commit; one commit above the baseline; branch, HEAD, parent
   and tree read back.
6. AP pin, managed block, `.gitmodules`, `ap.project.conf`, upgrade ledger,
   `poetry.lock`, `pyproject.toml`, `src/framenest/**` and `AGENTS.md`
   unchanged; `main`/`origin/main` still at `26d28b16`.
7. No secret, token, hostname or private network value appears in any new or
   changed source file, template, test or documentation.

## Stopping conditions

Stop and report on: baseline, cleanliness, AP-pin or managed-block mismatch; an
unexpected pre-existing change; a needed change outside the allowlist; a route
that fails and cannot be corrected inside the allowlist; a needed host,
dependency or credential operation; any conflict between the plan and current
repository truth; or any instruction conflict. Preserve the first causal
failure; do not improvise a host action.

## Completion and report contract

`PASS` means the repository sources, helper extension, documentation and tests
above are complete within the allowlist, all validation passed, and one commit
exists on `feat/kronika-one-product`. Use `PARTIAL` or `BLOCKED` honestly
otherwise. No push occurred. No deployment or host claim is made; the separate
read-only NUC preflight and bounded host setup/deployment grant follow.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the unit and
helper design decisions with their exact locations; the credential-integration
choice and its test evidence; validation results; changed files; commit result
with `no push`; deviations/risks/missing evidence; one smallest next step;
`Report justification: new-mutation`; authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

Direct communication with the Cooperator (the short completion notice) is in
Slovak, masculine address for him. This prompt and the formal report are in
English. Do not use subagents. Do not commit Meta artifacts.

Finalize the report, save it at the exact destination, read it back in full,
and verify its first line, coordinates, content and path before the short
separate completion notice with status, exact report path and SHA-256. Terminal
report, cancellation or supersession expires this authority. Do not continue
autonomously after the report.

## Trace and delivery record

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 04_implementation_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 04_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
