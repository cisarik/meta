# Kronika one product — S3 C3 full fresh independent acceptance

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 22
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S3-C3-REACCEPTANCE
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — full fresh independent acceptance of a capture runner temporary-storage correction that changes runtime behavior; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: yes — required-fresh-independent

## Session and independence declaration

This must be a genuinely fresh session that did not implement or correct the
C3 change or any earlier S3 candidate. Declare your actual independence
posture. Prior plans, reports and classified host evidence are evidence;
inherited implementation or correction reasoning is disqualifying. You do not
correct anything; findings are reported, never fixed. Do not contact the NUC.
Do not ask for or receive prompts in another session.

## Acceptance and Correction Record

```text
Acceptance candidate: fd277a9a64a6965df76127dbec5b1735d2fb3cdd
  (tree 3b9014956a3bc738a209af51034fcac58ef5c498, branch feat/kronika-one-product,
   parent e408bb5503f359ec24542304ac1a621c6b9e4ffb)
Acceptance owner map: the C3 delta (3 paths, e408bb5..candidate); accepted plan
  15_report_00.md §3 C3; 19_report_00.md branch B and decision table; the
  prerequisite probe 20_report_00.md; implementation report 21_report_00.md; the
  classified instrumented-launch evidence in 00_notes.md
Acceptance allowlist: read-only review of the candidate and governing AP; the
  declared focused route; one declared temporary probe root under /tmp
Acceptance risk claims: the six fixed claims below
Acceptance control matrix: the fixed positive and negative controls below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

## Starting state (verified at issuance, 2026-09-25)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `fd277a9a64a6965df76127dbec5b1735d2fb3cdd`, parent
  `e408bb5503f359ec24542304ac1a621c6b9e4ffb`, tree
  `3b9014956a3bc738a209af51034fcac58ef5c498`, subject
  `fix(capture): point the capture runner temporary directory at its runtime dir`;
  clean index and worktree; the baseline-to-HEAD diff is exactly the three
  allowlisted paths.
- Local `main` = `origin/main` = public
  `https://github.com/cisarik/framenest.git` `refs/heads/main` =
  `e408bb5503f359ec24542304ac1a621c6b9e4ffb` (the correction is not yet
  published).
- Governing AP gitlink and detached `.ap` HEAD:
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- `private/**` is never read. Do not contact the NUC, SSH, the gate or any
  host. Never read the token, the browser profile or the installed
  `/etc/kronika-capture/capture.env`.

### Established evidence (input)

Chromium's Linux process singleton creates its socket directory with
`ScopedTempDir::CreateUniqueTempDir()` in the temporary directory (`$TMPDIR`,
else `/tmp`); the runner runs with `ProtectSystem=strict` and a writable-path
allowlist that excludes general `/tmp`, so the instrumented launch failed with
`process_singleton_posix.cc:1043 Failed to create socket directory.` and exit
21, and the P1 probe independently showed `/tmp` mkdir `EROFS`. The accepted
C3 correction points `TMPDIR` at the already-writable runtime directory.

## Fixed claims

1. **Exact and contained unit change.** The runner unit adds exactly
   `Environment=TMPDIR=/run/kronika-capture/tmp` and extends `ExecStartPre` to
   create `/run/kronika-capture/tmp` at mode 0700 together with the profile
   and staging paths. `User`, `Group`, `WorkingDirectory`, the other
   `Environment=` lines, `EnvironmentFile`, `ExecStart` (with `--state-dir`
   before the subcommand), `Restart=no`, `LoadCredential`, `StateDirectory`,
   `StateDirectoryMode`, `UMask`, `NoNewPrivileges=true`,
   `ProtectSystem=strict`, `ProtectHome=read-only`, `ReadWritePaths`, the
   `Protect*`/`Restrict*`/`Lock*` and capability directives, `[Unit]` and
   `[Install]` are unchanged. No general `/tmp` writable path and no
   `PrivateTmp` were added.
2. **Causal regression.** The new contract test asserts the exact new lines,
   the unchanged `ReadWritePaths`, the absence of `PrivateTmp=true` from the
   runner and Xvfb units, the preserved `ProtectSystem=strict` and
   `NoNewPrivileges=true`, and that `kronika-capture.env.example` does not
   assign `TMPDIR`; existing assertions are preserved. The baseline unit text
   read read-only (`git show e408bb5:deploy/systemd/kronika-capture-runner.service`)
   lacks the asserted lines, so the regression is causal.
3. **Documentation.** `docs/UBUNTU_NUC_DEPLOYMENT.md` records the correction
   and keeps the Xvfb `/tmp` write distinct from the runner; no existing
   security or operational guarantee is weakened or contradicted.
4. **Containment.** The baseline-to-candidate diff is exactly the three
   allowlisted paths; no capture Python or JavaScript asset, protocol, HTTP
   endpoint, CLI command, journal schema, other unit, `framenest.service`,
   AP file, managed block, upgrade ledger, `poetry.lock`, `pyproject.toml` or
   `AGENTS.md` change; nothing was pushed.
5. **Preserved boundaries.** The loopback/token/Host-Origin boundary, the
   credential boundary, the single-browser lifecycle, the durable-submission
   and no-automatic-resend semantics, and the journal recovery contract are
   untouched by the diff.
6. **Evidence honesty and residual risk.** Synthetic tests do not establish
   host Chromium startup; the host proof remains the later separately
   authorized corrected start. The installed `/etc/kronika-capture/capture.env`
   was not read; because `EnvironmentFile=` is processed after
   `Environment=`, an installed `TMPDIR` assignment would override the unit
   value, so that read-only deployment-time check remains open and must be
   reported, not assumed.

## Fixed control matrix

Positive controls (run independently from the repository root; report observed
counts and exit codes):

```text
git rev-parse HEAD 'HEAD^{tree}' 'HEAD^'
git diff --name-status e408bb5503f359ec24542304ac1a621c6b9e4ffb HEAD
git show e408bb5503f359ec24542304ac1a621c6b9e4ffb:deploy/systemd/kronika-capture-runner.service

./.ap/ap project check --root /home/agile/Projects/framenest --baseline e408bb5503f359ec24542304ac1a621c6b9e4ffb

./.ap/ap exec --root /home/agile/Projects/framenest --baseline e408bb5503f359ec24542304ac1a621c6b9e4ffb --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py -q -p no:cacheprovider

node --test tests/capture_lifecycle.test.js
```

Negative and adversarial controls (bounded synthetic work under one declared
temporary root, e.g. `/tmp/kronika-one-product-s3-c3-reacceptance`, mode 0700,
synthetic data only, cleaned up by you):

- Review the full three-path diff for unintended changes (leak hunt): confirm
  no `--no-sandbox`, no stealth, no argument-order, no writable-path, no
  `PrivateTmp`, no account/credential and no Xvfb/bridge/view/vnc directive
  change.
- Demonstrate the regression's causality by applying the test's asserted exact
  strings to the baseline unit text read via `git show`; the assertions must
  be absent there and present on the candidate.
- Confirm the runner's `ReadWritePaths` path list contains no bare `/tmp`
  element, and that the new `ExecStartPre` uses mode 0700.
- Confirm the documentation change does not claim that synthetic tests prove
  host startup and does not authorize general `/tmp` access.
- Confirm the commit contains only the three allowlisted paths and no Meta
  artifact.

State every observed result; unverified controls are reported as unverified,
never as PASS.

## Authority and containment

Positive authority: read-only inspection of the candidate and governing
`.ap`; the declared route; creation, use and cleanup of one declared
temporary probe root under `/tmp` (mode 0700, synthetic data only); and the
terminal report write at the exact destination when absent.

Negative authority: no host, NUC, SSH, gate transport, deployment, service or
privilege operation; no `sudo -v` or `sudo -K`; no product, test,
documentation, AP, packaging or configuration edit; no correction; no push or
publication; no new dependency; no subagent; no Meta commit. Do not read
`private/**`, the token, the browser profile or the installed capture
environment file.

## Stopping conditions

Stop with `PARTIAL` or `BLOCKED` on: identity or git-state mismatch; a route
that cannot run; a probe exceeding the authorized effects; sensitive output;
or a required control that cannot be established without a forbidden
mutation. Preserve the first causal failure; missing evidence is never PASS.

## Evidence selection and report delivery

Evidence tier: E3
Evidence tier basis: runtime-behavior change in a capture service unit with
host consequences; full fresh independent acceptance required
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the declared route
Affected tests: the C3 delta and the preserved capture contracts
New causal regression: none — this is acceptance of the implemented regression
Broad or full suite: not-used
Runtime or testbed: declared route; no host
Independent acceptance: required-separate-fresh-worker (this exchange)

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
Downloadable prompt filename: 22_acceptance_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 22_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

## Completion and report contract

`PASS` means every fixed claim is independently established and no blocking
finding remains. Use `Phase-qualified result: acceptance-PASS` only for a PASS.
Logical-whole closure stays `not-closed`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include: the compact core; the
completed Acceptance and Correction Record; per-claim verdicts; the control
matrix with observed counts and exit codes; adversarial outcomes; findings if
any (full finding structure); containment and cleanup; residual risk and
limitations (including the installed `capture.env` TMPDIR question); one
smallest next step (publication of the accepted candidate, then deployment,
unit reinstall and the single corrected bootstrap start);
`Report justification: final-acceptance`; authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

Direct communication with the Cooperator (the short completion notice) is in
Slovak, masculine address for him. This prompt and the formal report are in
English. Do not use subagents. Do not commit Meta artifacts. Finalize the
report, save it at the exact destination only if absent, read it back in full,
verify its first line/coordinates/content/path, then send the short separate
completion notice with status, exact path and SHA-256. Terminal report or
cancellation expires this authority.
