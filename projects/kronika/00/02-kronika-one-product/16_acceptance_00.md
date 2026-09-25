# Kronika one product — S3 diagnostics/activation full fresh re-acceptance

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 16
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S3-DIAGNOSTICS-REACCEPTANCE
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — full fresh re-audit of the corrected capture diagnostics and activation readiness after the Planner-established defects; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: yes — required-fresh-independent

## Session and independence declaration

This must be a genuinely fresh session that did not implement or correct S3.
Declare your actual independence posture. Prior plans, reports and the
classified host evidence are evidence; inherited implementation or correction
reasoning is disqualifying. You do not correct anything; findings are
reported, never fixed. Do not contact the NUC. Do not ask for or receive
prompts in another session.

## Acceptance and Correction Record

```text
Acceptance candidate: e408bb5503f359ec24542304ac1a621c6b9e4ffb
  (tree dadc01726a354c319374832bfd385be0bdffb516, branch feat/kronika-one-product,
   parent d63d0b725acedf49d1611224c3b5201a90e7ef90)
Acceptance owner map: the S3 slice paths (20 paths, 82a6a598..c975aba); correction
  deltas at c975aba..94e605c (4 paths) and 94e605c..d63d0b7 (3 paths); the accepted
  recovery plan 15_report_00.md; the C1+C2 implementation delta (7 paths,
  d63d0b7..candidate); implementation report 15_report_01.md; the classified host
  evidence in the plan
Acceptance allowlist: read-only review of the candidate and governing AP; the declared
  focused route; synthetic temporary probe state under one declared temporary root
Acceptance risk claims: the six fixed claims below
Acceptance control matrix: the fixed positive and negative controls below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 3
Automatic corrections used: 3
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

## Starting state (verified at issuance)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `e408bb5503f359ec24542304ac1a621c6b9e4ffb`, parent
  `d63d0b725acedf49d1611224c3b5201a90e7ef90`, tree
  `dadc01726a354c319374832bfd385be0bdffb516`, subject
  `fix(capture): diagnose startup and require fresh activation readiness`; clean
  index and worktree.
- Local `main` = `origin/main` = public
  `https://github.com/cisarik/framenest.git` `refs/heads/main` =
  `d63d0b725acedf49d1611224c3b5201a90e7ef90` (the correction is not yet
  published).
- Governing AP gitlink and detached `.ap` HEAD:
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- `private/**` is never read. Do not contact the NUC, SSH, the gate or any
  host.

### Accepted recovery plan (input)

`15_report_00.md` established: the missing Chromium has no uniquely
established cause because the runner hid the startup exception; the zero-job
`needs_admin` state clears through the designed browser + explicit null-job
resume + fresh readiness acknowledgement (no journal reset); and activation
could accept a previous persisted `ready` without a fresh identity. C3
(runner `TMPDIR`) is conditional on the bounded host diagnostic and is not
part of this candidate.

## Fixed claims

1. **C1 closure — bounded safe startup diagnostics.** The driver exposes only
   the allowlisted diagnostic projection; it distinguishes occupied lock,
   unexpired interval and unverifiable brake metadata; spawn errno and signal
   are fixed enums or `OTHER`, exit code an integer 0–255 or null; endpoint
   flags and cleanup status are booleans; fixed stderr classifications are
   `sandbox_namespace`, `display_authentication`,
   `temporary_storage_read_only`, `profile_in_use`, `unclassified`, with the
   input discarded; no raw exception, stderr, URL, argv, environment value,
   profile path, DOM or credential enters the record. Exactly one
   `capture_startup` record is emitted for one start attempt across repeated
   unavailable-loop iterations; cleanup records are separate and never replace
   the first failure; the spawn argv, stderr bounds (65,536 bytes / 4,096-char
   lines), endpoint host rejection, launch brake and lock lifecycle are
   preserved (confirmed termination releases the lock; unconfirmed termination
   retains it).
2. **C2 closure — fresh-identity activation readiness.** The helper snapshots
   only journal service metadata, and refuses an unverifiable snapshot before
   the pointer switch; old `ready` and old terminal readiness are treated as
   `starting`; `ready` is accepted only after both valid runner and
   browser-session identities have changed and the runner unit is active; a
   failed unit is immediately terminal; a fresh runner's `needs_admin` or
   `browser_unavailable` remains terminal exit 16; no fresh identity times out
   at the 180-second deadline with exit 17; exactly one pointer switch and one
   runner restart occur; failure retains and reports the new pointer; the
   connection fence and journal schema are unchanged.
3. **Zero-job recovery regression.** A persisted `browser_unavailable` service
   state with zero jobs reconstructs as `needs_admin`/`E_AMBIGUOUS_SEND`;
   wrong intervention and job identities are rejected; a ready browser alone
   or an incorrect resume acknowledgement leaves the pause; an explicit
   null-job resume plus the matching fresh readiness acknowledgement clears it
   with zero jobs; no journal reset, SQL surgery or state recreation.
4. **Preserved S3/S2 guarantees.** The five capture units, the credential
   boundary (`paths.py`, `bridge/auth.py`, `cli.py` token handling), the
   capture kernel semantics, the work/brake gates, manifest/runtime identity,
   capture rollback and web/capture separation are unchanged from the accepted
   `d63d0b7` sources except where C2 deliberately changes the readiness gate.
5. **Containment.** The implementation delta is exactly the seven allowed
   paths; no protocol version, HTTP endpoint, CLI command or journal schema
   change; `src/framenest/**`, AP files, managed block, upgrade ledger,
   `poetry.lock`, `pyproject.toml`, `AGENTS.md` and the accepted units are
   unchanged; documentation reflects the corrected behavior.
6. **Evidence consistency.** No claim that synthetic tests establish Chromium
   startup or a unique host cause; C3 is not implemented and remains
   conditional; the parent-causality claims are supported by the reviewed diff
   (no observed parent red-run is required).

## Fixed control matrix

Positive controls (run independently from the repository root; report observed
counts):

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline e408bb5503f359ec24542304ac1a621c6b9e4ffb

./.ap/ap exec --root /home/agile/Projects/framenest --baseline e408bb5503f359ec24542304ac1a621c6b9e4ffb --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py tests/unit/chatgpt_page -q -p no:cacheprovider

node --test tests/capture_lifecycle.test.js
```

Negative and adversarial controls (bounded synthetic probes under one declared
temporary root, e.g. `/tmp/kronika-one-product-s3-diag-reacceptance`, mode
0700, cleaned up by you):

- Reproduce the diagnostic classifications with synthetic inputs, including
  secret markers that must not reach logs, split/oversized stderr, exact byte
  exhaustion and rejected endpoint hosts.
- Reproduce the C2 stale-readiness matrix against the generated gate with a
  synthetic journal and stubbed `systemctl`: old `ready`, old
  `browser_unavailable`, partially changed identities, absent/invalid
  identities, fresh ready, fresh blocked, failed unit, and the 180-second
  deadline; assert one switch and one restart.
- Reconstruct the parent behaviors in the temporary root where practical to
  demonstrate the causal delta (no host execution).
- Verify the zero-job recovery regression and the preserved kernel/credential
  boundaries.
- Leak hunt across the seven-path delta and the S3 slice.

State every observed result; unverified controls are reported as unverified,
never as PASS.

## Authority and containment

Positive authority: read-only inspection of the candidate and governing `.ap`;
the declared route; creation, use and cleanup of one declared temporary probe
root under `/tmp` (mode 0700, synthetic data only); and the terminal report
write.

Negative authority: no host, NUC, SSH, gate transport, deployment, service or
privilege operation; no `sudo -v` or `sudo -K`; no real token or credential
creation; no product, test, documentation, AP, packaging or configuration
edit; no correction; no push or publication; no new dependency; no subagent;
no Meta commit. Do not read `private/**`.

## Stopping conditions

Stop with `PARTIAL` or `BLOCKED` on: identity or git-state mismatch; a route
that cannot run; a probe exceeding the authorized effects; sensitive output; or
a required control that cannot be established without a forbidden mutation.
Preserve the first causal failure; missing evidence is never PASS.

## Evidence selection and report delivery

Evidence tier: E3
Evidence tier basis: full fresh re-acceptance of corrected capture diagnostics
and activation readiness after real host and planner evidence
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the declared route
Affected tests: the S3 slice and all correction deltas
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
Downloadable prompt filename: 16_acceptance_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 16_report_00.md
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
completed Acceptance and Correction Record; per-claim verdicts with explicit
C1 and C2 closure; the control matrix with observed counts; adversarial
outcomes; findings if any (full finding structure); containment and cleanup;
residual risk and limitations; one smallest next step (publication of the
corrected commit, then the single bounded host diagnostic); `Report
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
