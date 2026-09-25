# Kronika one product — S3 full fresh re-acceptance after the host correction

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 11
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S3-REACCEPTANCE
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — full fresh re-audit of the corrected deployment sources after real host execution produced two runtime defects; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: yes — required-fresh-independent

## Session and independence declaration

This must be a genuinely fresh session that did not implement or correct S3.
Declare your actual independence posture. Prior plans, reports and the
classified host evidence are evidence; inherited implementation or correction
reasoning is disqualifying. You do not correct anything; findings are
reported, never fixed. Do not contact the NUC.

## Acceptance and Correction Record

```text
Acceptance candidate: 94e605c17b881461fad3e22fd8c7fca32cb93976
  (tree 4667f47c24e84d80574beb66b71aca533393d994, branch feat/kronika-one-product,
   parent c975aba14840b97944aecc655907e3abc370341d)
Acceptance owner map: the S3 slice paths (20 paths, 26d28b16..c975aba) plus the
  correction delta (4 paths, c975aba..candidate: bridge, runner and xvfb units and
  tests/contract/test_kronika_capture_services.py); accepted plan 01_report_00.md
  sections 7.2-7.3 and the S3 row; S3 report 04_report_00.md; S3 acceptance
  08_report_00.md; host setup report 10_report_00.md; correction report 10_report_01.md;
  the classified host evidence quoted below
Acceptance allowlist: read-only review of the candidate and governing AP; the declared
  focused route; synthetic temporary probe state under one declared temporary root
Acceptance risk claims: the seven fixed claims below
Acceptance control matrix: the fixed positive and negative controls below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

## Starting state (verified at issuance)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `94e605c17b881461fad3e22fd8c7fca32cb93976`, parent
  `c975aba14840b97944aecc655907e3abc370341d`, tree
  `4667f47c24e84d80574beb66b71aca533393d994`, subject
  `fix(capture): accept the capture CLI state directory and skip the Xvfb lock`;
  clean index and worktree.
- Local `main` = `origin/main` = public
  `https://github.com/cisarik/framenest.git` `refs/heads/main` =
  `c975aba14840b97944aecc655907e3abc370341d` (the correction is not yet
  published).
- Governing AP gitlink and detached `.ap` HEAD:
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- `private/**` is never read. Do not contact the NUC, SSH, the worker gate or
  any host.

### Classified host evidence (not re-observable in this exchange)

Host setup from `10_report_00.md`: account `kronika-capture` (uid 996), capture
directories, one token value as 0600 root credential plus matching 0600
capture-owned state token, release `c975aba` deployed, five units installed,
xvfb/bridge/runner enabled, `activate-capture` exit 16 with
`readiness=failed`. Two confirmed defects: **F-HOST-01** — bridge and runner
`ExecStart` placed `--state-dir` after the subcommand and both exited 2 with
`unrecognized arguments`; **F-HOST-02** — Xvfb could not create
`/tmp/.X99-lock` under `ProtectSystem=strict` with only `/tmp/.X11-unix`
writable and exited 1.

Correction from `10_report_01.md`: the three units stopped, disabled and
reset-failed (no chrome/Xvfb processes, no listeners on 8765/5900/6080);
`/usr/bin/Xvfb -help` shows `-nolock` ("disable the locking mechanism");
corrected unit lines use `kronika-capture --state-dir /var/lib/kronika-capture
bridge run --port 8765`, `kronika-capture --state-dir /var/lib/kronika-capture
runner run --profile /var/lib/kronika-capture/profile --port 8765 --headed`,
and `/usr/bin/Xvfb :99 -screen 0 1280x800x24 -nolisten tcp -nolock -auth
/run/kronika-capture/Xauthority`; a CLI-parse regression was added; the route
ran 157 passed; account, token and release pointers were retained.

## Goal

Establish whether the corrected candidate fully satisfies the accepted S3
contract and closes both host-observed defects without weakening any prior S3
guarantee. This is the one full fresh correction re-acceptance of S3. It is not
a new slice, grants no publication or deployment authority, and cannot observe
a live corrected Xvfb (the host retry is the later check).

## Fixed risk claims

1. **Unit directives (re-verified on the corrected units).** No capture unit
   contains `PartOf=`, `BindsTo=`, `ConsistsOf=` or `PropagatesStopTo=`.
   Xvfb and runner `Restart=no`; bridge `Restart=on-failure`. Runner
   `Requires=` only `kronika-capture-xvfb.service`. Xvfb keeps `-nolisten tcp`,
   `-auth` and does not use `-ac`; the corrected command adds `-nolock`.
   VNC/noVNC stay loopback-only, 1800-second limited, without `[Install]`.
   State/runtime modes stay 0700; `UMask=0077`; credential loading unchanged.
   Bridge and runner `ExecStart` place `--state-dir` before the subcommand and
   their full argument lists parse with the candidate CLI parser; no other
   capture unit contains an invalid CLI invocation.
2. **F-HOST-01 closure.** The exact corrected bridge and runner command lines
   parse with `kronika_capture.cli.build_parser()`, and the previous order
   (option after the subcommand) fails; the added regression test proves both
   directions.
3. **F-HOST-02 closure.** The Xvfb lock strategy is `-nolock`, consistent with
   the classified `-help` evidence; `ReadWritePaths` remains
   `/tmp/.X11-unix /run/kronika-capture` (no broader `/tmp` grant); Xvfb and
   runner still do not set `PrivateTmp`. No lock file is required for the
   single-instance unit.
4. **Credential boundary (unchanged files).** Credential-wins,
   missing-credential fallback, empty/oversized/non-UTF8 non-minting, symlink
   refusal, unchanged Host/Origin/token and constant-time comparison, no token
   in argv/logs/frontend, explicit Chromium path, no sandbox weakening.
5. **Release helper (unchanged logic).** Manifest capture identity now reflects
   the corrected unit contract; `activate-capture`/`rollback-capture` keep
   verify/drain/refuse/brake/atomic-switch/one-restart/no-retry/dual-pointer
   behavior; web deploy/rollback still touch only the web pointer and service;
   `migration-required` preserved; no implicit migration or deletion.
6. **Correction containment and regressions.** The correction delta is exactly
   the four allowed paths; no capture source, helper, packaging, credential,
   AP or documentation file changed; every existing directive assertion and
   the declared route still pass; the new regression is causal; no secret or
   private value appears.
7. **Evidence consistency.** The classified host evidence is consistent with
   the corrected units; the two observed failures are explained and closed;
   the remaining unknown (a live corrected Xvfb under the unit) is named, not
   assumed.

## Fixed control matrix

Positive controls (run independently from the repository root; report observed
counts):

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 94e605c17b881461fad3e22fd8c7fca32cb93976

./.ap/ap exec --root /home/agile/Projects/framenest --baseline 94e605c17b881461fad3e22fd8c7fca32cb93976 --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py tests/unit/chatgpt_page tests/unit/test_import_boundaries.py tests/unit/test_package_import.py tests/unit/test_api_import_boundary.py -q -p no:cacheprovider
```

Negative and adversarial controls (bounded synthetic probes under one declared
temporary root, e.g. `/tmp/kronika-one-product-s3-reacceptance`, mode 0700,
cleaned up by you):

- Unit directive matrix for all five units on the corrected text.
- CLI-parse matrix: for every `ExecStart` that invokes `kronika-capture`,
  parse the arguments with the candidate parser; reconstruct the old
  option-after-subcommand order in the temporary root and confirm the
  regression test fails on it (causal evidence).
- Credential probes: the same synthetic matrix as the S3 acceptance
  (credential-wins, fallback, empty/oversized/non-UTF8, symlink, unchanged
  auth results, launcher argv without the token).
- Helper probes: fake-runner `activate-capture`/`rollback-capture` behaviors
  and the manifest identity reflecting the corrected unit contract.
- Leak hunt across the correction delta and the S3 slice.

State every observed result; unverified controls are reported as unverified,
never as PASS.

## Authority and containment

Positive authority: read-only inspection of the candidate and governing
`.ap`; the declared route; creation, use and cleanup of one declared temporary
probe root under `/tmp` (mode 0700, synthetic data only); and the terminal
report write.

Negative authority: no host, NUC, SSH, gate transport, deployment, service or
privilege operation; no real token or credential creation; no product, test,
documentation, AP, packaging or configuration edit; no correction; no push or
publication; no new dependency; no subagent; no Meta commit. Do not read
`private/**`.

## Stopping conditions

Stop with `PARTIAL` or `BLOCKED` on: identity or git-state mismatch; a route
that cannot run; a probe exceeding the authorized effects; sensitive output; or
a required control that cannot be established without a forbidden mutation.
Preserve the first causal failure; missing evidence is never PASS.

## Evidence selection and report delivery

Evidence tier: E3
Evidence tier basis: full fresh re-acceptance of corrected deployment sources
after real host defects
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the declared route
Affected tests: the S3 and correction tests
New causal regression: none — this is re-acceptance
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
Downloadable prompt filename: 11_acceptance_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 11_report_00.md
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
completed Acceptance and Correction Record; per-claim verdicts; explicit
F-HOST-01 and F-HOST-02 closure verdicts; the control matrix with observed
counts; adversarial outcomes; findings if any (full finding structure);
containment and cleanup; residual risk and limitations; one smallest next step
(publication of the corrected commit, then the host retry); `Report
justification: final-acceptance`; authority expiry; and:

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
