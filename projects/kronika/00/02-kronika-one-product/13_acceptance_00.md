# Kronika one product — S3 full fresh re-acceptance after the Xvfb lock correction

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 13
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S3-LOCK-REACCEPTANCE
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — full fresh re-audit of the corrected deployment sources after a second host-observed runtime defect; the Cooperator may override.
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
Acceptance candidate: d63d0b725acedf49d1611224c3b5201a90e7ef90
  (tree 95862a1e012256829ada49ed780ad665cd2aea18, branch feat/kronika-one-product,
   parent 94e605c17b881461fad3e22fd8c7fca32cb93976)
Acceptance owner map: the S3 slice paths (20 paths, 82a6a598..c975aba); the first
  correction delta (4 paths, c975aba..94e605c); the second correction delta (3 paths,
  94e605c..candidate: kronika-capture-xvfb.service, docs/UBUNTU_NUC_DEPLOYMENT.md,
  tests/contract/test_kronika_capture_services.py); accepted plan sections 7.2-7.3 and
  the S3 row; reports 04_report_00, 08_report_00, 10_report_00, 10_report_01,
  10_report_02, 10_report_03; the classified host evidence below
Acceptance allowlist: read-only review of the candidate and governing AP; the declared
  focused route; synthetic temporary probe state under one declared temporary root
Acceptance risk claims: the seven fixed claims below
Acceptance control matrix: the fixed positive and negative controls below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 2
Automatic corrections used: 2
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

## Starting state (verified at issuance)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `d63d0b725acedf49d1611224c3b5201a90e7ef90`, parent
  `94e605c17b881461fad3e22fd8c7fca32cb93976`, tree
  `95862a1e012256829ada49ed780ad665cd2aea18`, subject
  `fix(capture): let the unprivileged Xvfb create its display lock`; clean
  index and worktree.
- Local `main` = `origin/main` = public
  `https://github.com/cisarik/framenest.git` `refs/heads/main` =
  `94e605c17b881461fad3e22fd8c7fca32cb93976` (the second correction is not yet
  published).
- Governing AP gitlink and detached `.ap` HEAD:
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- `private/**` is never read. Do not contact the NUC.

### Classified host evidence (not re-observable here)

- `10_report_00.md`: first setup; bridge/runner exit 2 because `--state-dir`
  followed the subcommand; Xvfb exit 1 because it could not create
  `/tmp/.tX99-lock` under `ProtectSystem=strict`; readiness `failed`.
- `10_report_01.md` and commit `94e605c`: argument order corrected; `-nolock`
  chosen because `Xvfb -help` advertises it; host cleaned (units stopped,
  disabled, reset-failed; no processes/listeners).
- `10_report_02.md`: retry; deploy and unit install at `94e605c` succeeded;
  Xvfb logged `Warning: the -nolock option can only be used by root`, ignored
  the option for the unprivileged service user, still needed the lock, exited
  1; readiness `browser_unavailable` (`E_BROWSER_UNAVAILABLE`); bridge and
  runner were left active; no Chromium; no login.
- `10_report_03.md` and candidate `d63d0b7`: `-nolock` removed;
  `ReadWritePaths=/tmp /tmp/.X11-unix /run/kronika-capture`; one documentation
  sentence; the service contract test updated; host cleaned again (units
  inactive/disabled, `NRestarts=0`, no processes/listeners; account, tokens
  and pointers untouched at `94e605c`); route 157 passed.
- The live corrected Xvfb under the unit was never observed.

## Goal

Establish whether the corrected candidate fully satisfies the accepted S3
contract and closes the Xvfb lock defect with the documented fallback, without
weakening any prior S3 guarantee. This is the full fresh correction
re-acceptance for the second host-observed defect. It grants no publication,
deployment or host authority, and cannot observe a live Xvfb (the host retry is
the later check).

## Fixed risk claims

1. **Unit directives (corrected units).** No capture unit contains `PartOf=`,
   `BindsTo=`, `ConsistsOf=` or `PropagatesStopTo=`. Xvfb and runner
   `Restart=no`; bridge `Restart=on-failure`; runner `Requires=` only
   `kronika-capture-xvfb.service`. Xvfb keeps `-nolisten tcp` and `-auth`,
   contains neither `-nolock` nor `-ac`, and has
   `ReadWritePaths=/tmp /tmp/.X11-unix /run/kronika-capture` with
   `ProtectSystem=strict`; Xvfb and runner do not set `PrivateTmp`. VNC/noVNC
   remain loopback-only, 1800-second limited, without `[Install]`. Modes stay
   0700; `UMask=0077`; credential loading unchanged. Bridge and runner
   `ExecStart` place `--state-dir` before the subcommand and parse with the
   candidate CLI parser.
2. **F-HOST-01 remains closed.** The corrected bridge and runner command lines
   still parse; the old order still fails; the regression test still proves both
   directions.
3. **F-HOST-02 closure via the fallback.** Xvfb no longer depends on
   `-nolock`; its lock path under `/tmp` is writable while the rest of the
   filesystem stays read-only; the broadening is limited to `/tmp` beyond the
   previous list; no `PrivateTmp` is introduced; `-auth` still enforces access
   control and `-ac` remains absent.
4. **Credential boundary (unchanged files).** Credential-wins,
   missing-credential fallback, empty/oversized/non-UTF8 non-minting, symlink
   refusal, unchanged Host/Origin/token and constant-time comparison, no token
   in argv/logs/frontend, explicit Chromium path, no sandbox weakening.
5. **Release helper (unchanged logic).** Manifest capture identity reflects
   the corrected unit contract; `activate-capture`/`rollback-capture` keep
   verify/drain/refuse/brake/atomic-switch/one-restart/no-retry/dual-pointer
   behavior; web deploy/rollback touch only the web pointer and service;
   `migration-required` preserved.
6. **Correction containment and regressions.** The second correction delta is
   exactly the three allowed paths; no capture source, helper, packaging,
   credential or AP file changed; every existing directive assertion and the
   declared route pass; the updated lock assertion and the CLI-parse
   regression are causal; the documentation sentence is accurate.
7. **Evidence consistency.** The classified host evidence is consistent with
   the corrected unit; both observed failures are explained and closed at the
   source level; the remaining unknown (a live corrected Xvfb) is named.

## Fixed control matrix

Positive controls (run independently from the repository root; report observed
counts):

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline d63d0b725acedf49d1611224c3b5201a90e7ef90

./.ap/ap exec --root /home/agile/Projects/framenest --baseline d63d0b725acedf49d1611224c3b5201a90e7ef90 --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py tests/unit/chatgpt_page tests/unit/test_import_boundaries.py tests/unit/test_package_import.py tests/unit/test_api_import_boundary.py -q -p no:cacheprovider
```

Negative and adversarial controls (bounded synthetic probes under one declared
temporary root, e.g. `/tmp/kronika-one-product-s3-lock-reacceptance`, mode
0700, cleaned up by you):

- Unit directive matrix for all five units on the corrected text.
- Xvfb strategy checks: no `-nolock`, no `-ac`, `-auth` present, exact
  `ReadWritePaths`, no `PrivateTmp`; reconstruct the parent unit text and
  confirm the updated assertion fails on it (causal).
- CLI-parse matrix: every `ExecStart` invoking `kronika-capture` parses; the
  old option order fails.
- Credential probes (synthetic) and helper fake-runner probes as in the prior
  re-acceptance, including the corrected unit-contract hash.
- Leak hunt across the S3 slice and both correction deltas.

State every observed result; unverified controls are reported as unverified,
never as PASS.

## Authority and containment

Positive authority: read-only inspection of the candidate and governing `.ap`;
the declared route; creation, use and cleanup of one declared temporary probe
root under `/tmp` (mode 0700, synthetic data only); and the terminal report
write.

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
after a second host-observed runtime defect
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the declared route
Affected tests: the S3 and both correction tests
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
Downloadable prompt filename: 13_acceptance_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 13_report_00.md
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
completed Acceptance and Correction Record; per-claim verdicts; the Xvfb lock
strategy closure; the control matrix with observed counts; adversarial
outcomes; findings if any (full finding structure); containment and cleanup;
residual risk and limitations; one smallest next step (publication of the
second correction, then the host retry); `Report justification:
final-acceptance`; authority expiry; and:

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
