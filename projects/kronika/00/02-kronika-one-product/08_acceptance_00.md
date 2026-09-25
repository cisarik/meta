# Kronika one product — S3 fresh targeted deployment/credential-boundary review

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 08
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S3-ACCEPTANCE
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — fresh independent review of deployment tooling and a systemd-credential boundary that will be installed on a real host; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: yes — required-fresh-independent

## Session and independence declaration

This must be a genuinely fresh session that did not implement S3. Declare your
actual independence posture in the report. The plan, prior reports and the
classified preflight facts are evidence; inherited implementation reasoning is
disqualifying. You do not correct anything; findings are reported, never fixed.

## Acceptance and Correction Record

```text
Acceptance candidate: c975aba14840b97944aecc655907e3abc370341d
  (tree a80ab53cf5ee19ffe0af46de4e015519cd97d941, branch feat/kronika-one-product,
   parent 82a6a59803ed8830c19e51cd8f9bc1665c28a975)
Acceptance owner map: the S3 changed paths (20 paths: five capture unit sources,
  the capture env template, deploy/ubuntu/{framenest-release,framenest_release.py,README.md},
  docs/UBUNTU_NUC_DEPLOYMENT.md, src/kronika_capture/{config,paths,cli}.py,
  src/kronika_capture/bridge/auth.py, four existing test_nuc_* contracts,
  tests/contract/test_kronika_capture_services.py,
  tests/unit/chatgpt_page/test_systemd_credentials.py); the accepted plan
  01_report_00.md sections 7.2-7.3 and the S3 row; the S3 report 04_report_00.md;
  the classified preflight facts below
Acceptance allowlist: read-only review of the candidate and governing AP; the
  declared focused routes; synthetic temporary probe state under one declared root
Acceptance risk claims: the six fixed claims below
Acceptance control matrix: the fixed positive and negative controls below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

## Starting state (verified at issuance)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `c975aba14840b97944aecc655907e3abc370341d`, parent
  `82a6a59803ed8830c19e51cd8f9bc1665c28a975`, tree
  `a80ab53cf5ee19ffe0af46de4e015519cd97d941`; clean index and worktree.
- Local `main` = `origin/main` =
  `26d28b16c08a5e7e0179a32c16646bfdc1009c81` (unmoved); no remote branch for
  `feat/kronika-one-product`.
- Governing AP gitlink and detached `.ap` HEAD:
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- `private/**` is never read. Do not contact the NUC, SSH, or any host; the
  preflight facts below are Cooperator-observed and Orchestrator-classified.

### Classified preflight facts (owner-executed, read-only)

Ubuntu 24.04.4 LTS, x86_64; systemd 255 (255.4-1ubuntu8.17, `LoadCredential`
supported); `framenest` uid 999 present; `kronika-capture` absent (expected);
all capture paths absent (`/var/lib/kronika-capture`, `/run/kronika-capture`,
`/etc/kronika-capture`, credentials dir, `/opt/framenest/capture-current`);
`/tmp/.X11-unix` root:root 1777, no `:99` lock; web release
`/opt/framenest/releases/26d28b16…` active, installed unit carries one existing
credential line from an AI drop-in; `/usr/bin/chromium` resolves to Chrome for
Testing 154.0.8037.57; Xvfb, x11vnc 0.9.16, websockify, `/usr/bin/install`,
xauth 1.1.2, mcookie 2.39.3 and node v22.23.2 present; ports 8765/5900/6080
free; no related processes; unprivileged-userns restriction value `1` with the
existing AppArmor userns profile present; ample disk; sudo released.

## Goal

Independently establish whether the accepted S3 repository slice is safe and
correct to deploy: the capture units, the systemd-credential token boundary,
and the release helper's capture transition. This is the plan's fresh targeted
deployment/credential-boundary review before publication and host setup. It
does not contact the host and grants no deployment authority.

## Fixed risk claims

1. **Unit directives.** No capture unit contains `PartOf=framenest.service`.
   Xvfb and the runner set `Restart=no`; the bridge may restart independently.
   The runner requires Xvfb and does not require the bridge, so a bridge
   restart cannot stop the browser. Xvfb uses `-auth` and `-nolisten tcp`
   (never `-ac`) with a shared Xauthority and `/tmp/.X11-unix`. VNC and noVNC
   are loopback-only, normally not installed, limited to 1800 seconds and have
   no `[Install]`. State directories use 0700; the runner creates profile and
   staging privately. Bridge debugging stays loopback-only.
2. **Credential boundary.** The per-install token is delivered with
   `LoadCredential=token:...` to the bridge and runner; a systemd credential
   wins over the state token; a missing credential falls back to the previous
   behavior; an empty/oversized/non-UTF8 credential does not mint a
   replacement; symlinks are ignored; the token never appears in command
   arguments, logs or frontend configuration; the web account gains no
   profile access; the existing Host/Origin/token semantics and constant-time
   comparison are unchanged; the Chromium executable is explicit with no
   stealth and no sandbox weakening.
3. **Release helper.** The manifest carries capture runtime identity
   (`capture_code_tree`, runtime and unit contract hashes, bridge protocol).
   `activate-capture` and `rollback-capture` verify the exact installed SHA,
   manifest identity and protocol; drain queued capture work; refuse
   offered/running/needs_admin; enforce the 300-second launch brake; switch
   `capture-current` atomically; perform exactly one planned runner restart;
   poll readiness without automatic retry on failure; report both pointer
   SHAs. Web deploy/rollback touch only the web pointer and service; a web
   rollback cannot downgrade or restart capture. A missing capture pointer is
   reported as absent. The `migration-required` continuation is preserved and
   the helper performs no implicit migration or database deletion.
4. **Documentation and tests.** The deployment documentation describes the
   capture units, paths, credential delivery, view procedure and activation
   rules without claiming that capture is deployed; the new contract tests
   cover the directives and behaviors above; no secret, token, hostname or
   private network value appears in any new or changed file.
5. **Capture semantics preserved.** The bounded credential/launcher changes do
   not alter token entropy, wire authentication, protocol version, error
   codes, journal behavior or any S2 lifecycle guarantee.
6. **Preflight consistency.** The classified host facts are consistent with
   the units' and template's assumptions, and no host fact contradicts the
   plan's deployment design. Unverified facts are named, not assumed.

## Fixed control matrix

Positive controls (run independently from the repository root; report the
counts you actually observe):

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline c975aba14840b97944aecc655907e3abc370341d

./.ap/ap exec --root /home/agile/Projects/framenest --baseline c975aba14840b97944aecc655907e3abc370341d --operation test-focus -- tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py tests/contract/test_kronika_capture_services.py tests/unit/chatgpt_page tests/unit/test_import_boundaries.py tests/unit/test_package_import.py tests/unit/test_api_import_boundary.py -q -p no:cacheprovider
```

Negative and adversarial controls (bounded synthetic probes under one declared
temporary root, e.g. `/tmp/kronika-one-product-s3-acceptance`, mode 0700,
cleaned up by you):

- Unit directive matrix: parse every capture unit and confirm each required
  property by inspection and by an independent directive check; attempt to
  find a coupling, restart loop, non-loopback view bind, missing time limit or
  missing credential.
- Credential probes: with the candidate code and synthetic inputs, verify
  credential-wins, missing-credential fallback (including the existing mint
  behavior only where intended), empty/oversized/non-UTF8 credential
  non-minting, symlink refusal, unchanged Host/Origin/token results, and that
  the launcher argv contains the credential directory but never the token
  value. Do not use a real token.
- Helper probes: with a fake runner, exercise `activate-capture` and
  `rollback-capture`: live/paused refusal, queued drain, brake enforcement,
  exactly one restart, no second restart after a failed readiness, protocol
  refusal, atomic pointer switch, dual-pointer preservation, web rollback
  leaving capture untouched, missing-pointer reporting.
- Leak hunt: search the changed paths, the units, the env template, the helper
  and the tests for token/secret material, non-loopback binds, `-ac`,
  `PartOf=framenest.service`, stealth/sandbox weakening and profile-path
  exposure; report any finding.

State the exact observed result for every control. Unverified controls are
reported as unverified, never as PASS.

## Authority and containment

Positive authority: read-only inspection of the candidate and governing
`.ap`; the declared route command; creation, use and cleanup of one declared
temporary probe root under `/tmp` (mode 0700, synthetic data only); and
creation of the terminal report.

Commands: bounded read-only inspection; `rg` with private-value-safe output;
read-only Git queries; the declared `./.ap/ap` route; bounded synthetic probe
scripts and fake-runner/credential probes inside the temporary root; the
native file writer for the report only.

Negative authority: no host, NUC, SSH, gate transport, deployment, service,
account or privilege operation; no real token or credential creation; no
product-code, test, documentation, AP, packaging or configuration edit; no
correction of any finding; no push or publication; no new dependency or
toolchain; no subagent; no Meta commit. Do not read `private/**`.

## Stopping conditions

Stop with `PARTIAL` or `BLOCKED` on: identity or git-state mismatch; a
required route that cannot run; a probe exceeding the authorized effects;
sensitive output; or a required control that cannot be established without a
forbidden mutation. Preserve the first causal failure and report the exact
missing evidence. Missing evidence is never PASS. Do not correct anything.

## Evidence selection and report delivery

Evidence tier: E3
Evidence tier basis: fresh independent review of deployment tooling and a
credential boundary before host installation
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the declared route
Affected tests: the S3 changed and added tests
New causal regression: none — this is review, not implementation
Broad or full suite: not-used
Runtime or testbed: declared route plus synthetic temporary probes; no host
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
Downloadable prompt filename: 08_acceptance_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 08_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

## Completion and report contract

`PASS` means every fixed claim is independently established and no blocking
finding remains. `PARTIAL` means useful evidence exists but a claim remains
unverified. `BLOCKED` means the review cannot proceed safely. Use
`Phase-qualified result: acceptance-PASS` only for a PASS. Logical-whole
closure stays `not-closed`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include: the compact core; the
completed Acceptance and Correction Record; per-claim verdicts; the control
matrix results with your independently observed test counts; adversarial
outcomes; findings if any (with the full finding structure used by the
predecessor acceptance reports); the containment ledger and cleanup outcome;
residual risk and limitations; one smallest next step; `Report justification:
final-acceptance` (or `new-evidence` for PARTIAL); authority expiry; and:

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
