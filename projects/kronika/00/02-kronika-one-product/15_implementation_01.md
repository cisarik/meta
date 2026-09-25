# Kronika one product — S3 startup diagnostics and fresh-identity activation

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 15
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S3-DIAGNOSTICS-CORRECTION
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: bounded safe startup diagnostics on the real browser path and a freshness fix in the deployment readiness gate, both binding runtime behavior; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Current-session renewal

Continuity anchor: terminal PASS planning report `15_report_00.md` for task
`KRONIKA-ONE-PRODUCT-S3-RECOVERY-PLAN`, Worker session 15, exchange 01.
Authority renewal: that planning authority expired at its terminal report.
This exchange grants complete new bounded implementation authority for C1 and
C2 only, in this session. The plan remains the ground; C3 is conditional and
not implemented here. Re-gate the repository before mutation; retained context
is convenience only. Evidence posture: non-independent. New terminal report:
required (`15_report_01.md`).

## Accepted plan (do not reopen)

The Cooperator accepted the recovery plan: the missing Chromium has no uniquely
established cause yet; the zero-job journal state clears through the designed
browser + explicit-null-job-resume path (no journal reset); and activation must
require a fresh runner/browser identity before accepting readiness. Implement
C1 and C2 together now. C3 (runner `TMPDIR`) is applied only if the bounded
host diagnostic later establishes temporary-file failure.

Cooperator binding directive: Workers never run `sudo -v` or `sudo -K`; the
Cooperator releases the timestamp manually. This exchange is repository-only
anyway.

## Starting state (verified at issuance)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `d63d0b725acedf49d1611224c3b5201a90e7ef90`, tree
  `95862a1e012256829ada49ed780ad665cd2aea18`; clean index and worktree; local
  `main` = `origin/main` = public `refs/heads/main` = that commit; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- `private/**` is never read. No host, NUC, SSH, gate, browser or credential
  contact.

## C1 — preserve safe startup diagnostics

Files: `src/kronika_capture/_assets/extension/src/headless/driver.mjs`,
`src/kronika_capture/_assets/extension/src/headless/runner.mjs`,
`tests/capture_lifecycle.test.js`, `docs/UBUNTU_NUC_DEPLOYMENT.md`.

Required behavior:

- Preserve the public error code `E_BROWSER_UNAVAILABLE`.
- Attach internal, allowlisted diagnostic fields for the failed stage:
  executable preflight, profile-directory preflight, launch lock, brake
  metadata, spawn, endpoint discovery, CDP connection, page opening,
  navigation.
- Distinguish an occupied launch lock, an unexpired interval and unverifiable
  timestamp metadata.
- Preserve a bounded spawn errno, numeric child exit code, allowlisted signal,
  endpoint-seen flag and endpoint-budget-exhausted flag.
- Within the existing bounded stderr processing, recognize fixed
  classifications for sandbox/namespace refusal, X display/authentication
  failure, read-only temporary storage and profile-in-use refusal. Emit only
  the classification and discard the input text. Unknown messages remain
  `unclassified`; never infer a cause from an unrelated warning.
- Log one sanitized startup outcome from the runner. Never interpolate raw
  exceptions, stderr, URLs, argv, environment values, profile paths, DOM or
  credentials.
- Preserve the first startup failure if shutdown also fails; report cleanup
  failure separately.
- Preserve exactly one startup attempt, existing cleanup, the launch brake,
  the lock lifecycle and the unavailable service loop.

Required causal tests:

- Each launch stage produces the expected safe classification.
- A startup failure emits one record and makes one start attempt across
  multiple job-loop iterations.
- Synthetic secret markers in stderr, exception messages and paths never reach
  logs.
- Oversized/split stderr remains bounded; non-loopback endpoints remain
  rejected.
- Confirmed termination releases the lock; unconfirmed termination retains it.
- Diagnostics do not change spawn arguments, submission behavior or retry
  counts.

## C2 — require fresh readiness after activation

Files: `deploy/ubuntu/framenest_release.py`,
`tests/contract/test_kronika_capture_services.py`,
`docs/UBUNTU_NUC_DEPLOYMENT.md`.

Established defect: `cmd_remote_capture_readiness_gate()` accepts
`service_state == ready` plus an active unit without requiring a fresh runner
or browser-session identity, so a restart can pass on the previous persisted
`ready`; the current deadline is 30 seconds.

Required behavior:

1. After the work and brake checks, snapshot the journal's previous runner and
   browser-session identities using only service metadata.
2. Switch the pointer and restart the runner exactly once.
3. Treat readiness belonging to the previous identity as `starting`,
   including stale terminal readiness.
4. Accept `ready` only after both valid runner and browser-session identities
   have changed and the runner unit is active.
5. A failed unit is immediately terminal. A fresh runner's `needs_admin` or
   `browser_unavailable` readiness remains terminal.
6. Use a bounded 180-second capture readiness deadline, accommodating the
   existing 90-second connection fence and reconnect backoff.
7. On timeout or failure, retain the new pointer and report failure without
   another restart.

Do not change the bridge's connection fence and do not reset the journal.

Required causal tests:

- Old `ready` survives a restart: activation must not return success.
- Old `browser_unavailable` survives a restart: it must not cause premature
  terminal failure before the new identity arrives.
- Fresh identity plus `ready`: success after exactly one restart.
- Fresh identity plus blocked readiness: exit 16, no retry.
- No fresh identity: exit 17 at the deadline, no retry.
- A failed unit remains immediately terminal.
- Existing work refusal, brake refusal, manifest validation and web/capture
  separation still pass.

## Recovery regression (plan §4)

Add the zero-job restart/resume causal scenario to
`tests/unit/chatgpt_page/test_capture_journal.py`: start with zero jobs and a
persisted `browser_unavailable` service state; reconstruct the manager and
observe `needs_admin`/`E_AMBIGUOUS_SEND`; reject wrong intervention and job
identities; clear only after an explicit null-job resume plus matching fresh
readiness acknowledgement. No journal reset, SQL surgery or state-directory
recreation.

## Implementation authority record

Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Exact baseline: `d63d0b725acedf49d1611224c3b5201a90e7ef90`
Changed-path allowlist:

```text
src/kronika_capture/_assets/extension/src/headless/driver.mjs
src/kronika_capture/_assets/extension/src/headless/runner.mjs
deploy/ubuntu/framenest_release.py
tests/capture_lifecycle.test.js
tests/contract/test_kronika_capture_services.py
tests/unit/chatgpt_page/test_capture_journal.py
docs/UBUNTU_NUC_DEPLOYMENT.md
```

Implementation boundaries: C1, C2 and the recovery regression only; nothing
else. No new protocol version, HTTP endpoint, CLI command or journal schema.
Independence required: no

## Positive authority

Edit exactly the allowlisted paths; stage exactly those paths; create one
commit on `feat/kronika-one-product`. Run the declared route below.

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline d63d0b725acedf49d1611224c3b5201a90e7ef90

./.ap/ap exec --root /home/agile/Projects/framenest --baseline d63d0b725acedf49d1611224c3b5201a90e7ef90 --operation test-focus -- tests/contract/test_kronika_capture_services.py tests/contract/test_nuc_release_source_contract.py tests/contract/test_nuc_release_docs.py tests/contract/test_nuc_release_remote_contract.py tests/contract/test_nuc_operator_runbook.py tests/unit/chatgpt_page -q -p no:cacheprovider

node --test tests/capture_lifecycle.test.js
```

No ambient Python, `poetry run` or substitute route. No host command.

## Negative authority

- No host, NUC, SSH, gate, service, account, privilege, browser or credential
  action; no `sudo -v` or `sudo -K`.
- No C3/TMPDIR change now; no other unit, helper, capture source, packaging, AP
  or documentation change.
- No push or publication (separate grant follows); no Meta commit; no
  subagents; no `private/**`.
- Do not change submission semantics, retry counts, spawn arguments, the
  connection fence, token/credential handling or the journal schema.

## Validation

1. The declared route passes; report the observed counts.
2. Every C1 stage classification and C2 freshness case has a causal test that
   fails on the parent behavior where practical and passes on the candidate.
3. The zero-job recovery regression passes and proves the designed clear path.
4. Leak controls prove no synthetic secret reaches a log; bounded stderr
   limits and endpoint rejection are preserved.
5. `git diff --name-status <baseline>..HEAD` equals the allowlist; clean
   worktree; one commit above the baseline; branch, HEAD, parent and tree read
   back.
6. AP pin, managed block, `.gitmodules`, `ap.project.conf`, upgrade ledger,
   `poetry.lock`, `pyproject.toml`, `src/framenest/**`, `AGENTS.md` and the
   accepted units unchanged; local and public `main` still at the baseline.
7. No host claim: synthetic tests do not establish Chromium startup.

## Stopping conditions

Stop and report on: baseline, cleanliness, AP-pin or managed-block mismatch; a
needed change outside the allowlist; a route failure that cannot be corrected
inside the allowlist; a design conflict with the accepted plan; or any
instruction conflict. Preserve the first causal failure; do not improvise.

## Completion and report contract

`PASS` means C1, C2 and the recovery regression are complete within the
allowlist, all validation passed and one commit exists. `PARTIAL`/`BLOCKED`
otherwise. No push. Full-fresh acceptance, publication, then the single
bounded host diagnostic follow as separate grants.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; per-item
correction evidence with exact locations and observed test results; the route
counts; changed files; commit result with `no push`; deviations/risks/missing
evidence; one smallest next step (full-fresh acceptance); `Report
justification: new-mutation`; authority expiry; and:

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
report or cancellation expires this authority.

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
Downloadable prompt filename: 15_implementation_01.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 15_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
