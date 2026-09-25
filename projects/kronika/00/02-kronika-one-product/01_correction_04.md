# Kronika one product — S2 bounded correction

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 01
Worker exchange ordinal: 05
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-S2-CORRECTION
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: lifecycle accounting across readiness transitions and the exact terminal-failure contract for oversized results, plus one authentication-boundary correction; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Current-session renewal

Continuity anchor: terminal PASS report `01_report_03.md` for task
`KRONIKA-ONE-PRODUCT-S2`, Worker session 01, exchange 04, ending at candidate
`5259b89a9af993e94f00c03e7962681c8ba152a4`.
Findings source: the fresh independent acceptance report `02_report_00.md`
(status PARTIAL; findings S2-ACCEPTANCE-F01, F02, F03).
Authority renewal: all prior authority expired at its terminal report. This
exchange grants complete new bounded correction authority for exactly the three
findings below, on the same candidate line, for this Worker session only.
Reuse rationale: the same healthy session implemented S2 and holds the journal,
job-manager and runner context the corrections touch. The corrector may not
self-certify; a full fresh independent re-acceptance is a later separate
exchange.
Repository and environment re-gating: required before mutation; re-establish
every gate below from current evidence, never from memory.
Retained context: convenience only, never authority. On any conflict between
retained context and current repository evidence, stop and report.
Evidence posture: non-independent.
New terminal report: required (`01_report_04.md`).

## Starting state (verified at issuance)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `5259b89a9af993e94f00c03e7962681c8ba152a4`, parent
  `96ef426f7026c818f5e75733e8f8dfc5ac2321d1`, tree
  `97fac132581632305d4e86fdbdeca11118b83e75`, subject
  `feat(capture): persist submission barriers and browser lifecycle`; clean
  index and worktree.
- Local `main` = `origin/main` =
  `26d28b16c08a5e7e0179a32c16646bfdc1009c81` (unmoved); no remote branch for
  `feat/kronika-one-product`.
- Governing AP gitlink and detached `.ap` HEAD:
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- The acceptance report's reproduction evidence and locations are the finding
  baseline; re-verify each affected location against the current tree before
  editing.

## Implementation authority record

Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Exact baseline: `5259b89a9af993e94f00c03e7962681c8ba152a4`
Changed-path allowlist:

```text
src/kronika_capture/bridge/jobs.py
src/kronika_capture/bridge/journal.py
src/kronika_capture/bridge/server.py
src/kronika_capture/bridge/auth.py
src/kronika_capture/config.py
src/kronika_capture/errors.py
src/kronika_capture/client.py
src/kronika_capture/_assets/extension/src/protocol.js
src/kronika_capture/_assets/extension/src/headless/bridge_client.mjs
src/kronika_capture/_assets/extension/src/headless/job_engine.mjs
src/kronika_capture/_assets/extension/src/headless/runner.mjs
tests/unit/chatgpt_page/**
tests/capture_lifecycle.test.js
tests/chatgpt_page_protocol.test.js
```

Implementation boundaries: exactly the three corrections and the vocabulary
reconciliation below; nothing else.
Independence required: no

## Correction F01 — queued administrator intervention

Confirmed finding: when readiness becomes `needs_admin` (login/consent/
Turnstile/service-limit) while a job is admitted but not yet offered, the
administrator wait is not accounted and the original active deadline expires,
producing early `E_RESPONSE_TIMEOUT` with `admin_wait_s=0` and a released slot.

Required correction:

- Durably account administrator blocking against an admitted, not-yet-offered
  job; retain its active slot and pre-offer phase.
- Exclude cumulative administrator waiting from the active-response deadline
  exactly as for a running paused job, and keep the 1,800-second cumulative
  administrator limit with `E_INTERVENTION_TIMEOUT` expiry that does not
  terminate Chromium.
- An explicit readiness resume must re-run the readiness check before any
  continuation; never send while readiness is blocked.
- Preserve queued recovery/fencing semantics: the job must not be re-offered to
  an invalidated runner/offer identity, and existing confirmed-send protection
  must not weaken.

Required regression tests: readiness loss before offer; waiting beyond the
remaining active deadline; assert the job and slot are retained and the wait is
excluded; explicit resume resumes the same pre-offer phase; exact cumulative
1,800-second expiry ends the job with `E_INTERVENTION_TIMEOUT`; no send occurs
while readiness is blocked.

## Correction F02 — oversized result classification

Confirmed finding: an oversized complete result receives an untyped
`413/E_INTERNAL` rejection; the job stays running and the runner retries the
identical payload. Neither vocabulary contains `E_RESULT_TOO_LARGE`.

Required correction:

- Establish a byte-accurate result limit (accounting for envelope overhead and
  Unicode byte length).
- Persist a small typed `E_RESULT_TOO_LARGE` terminal failure under the job and
  delivery identity when the complete result exceeds the limit; do not truncate
  content while labelling it complete and do not convert a size failure into an
  untyped internal error.
- The runner must classify a permanent size rejection as terminal: no engine
  re-execution and no repeated identical delivery of the rejected payload.
- An authenticated status read must return the durable typed terminal failure
  with HTTP 200.
- Repeating delivery of the stored typed failure envelope may be retried with
  the same job/result identity; browser execution may not.

Required regression tests: serialize an oversized complete result through the
runner and the real loopback bridge; assert one engine execution, bounded
delivery attempts, a durable `E_RESULT_TOO_LARGE` terminal failure readable
through authenticated status, and no successful re-execution.

## Correction F03 — present empty Origin

Confirmed finding: `src/kronika_capture/bridge/auth.py` treats a present empty
`Origin` header as absent; the accepted contract is absent-or-exact approved
loopback Origin.

Required correction: reject a present empty `Origin`; accept only an absent
header or the exact approved loopback origin. Keep token enforcement, exact
Host validation, constant-time comparison and no wildcard CORS unchanged.

Required regression tests: distinguish absent, present-empty, exact, literal
`null` and foreign Origin; prove token enforcement still rejects unauthenticated
requests; prove no tested response carries a wildcard CORS header.

## Vocabulary reconciliation (binding scope decision)

- Add `E_RESULT_TOO_LARGE` now, in `errors.py` and `protocol.js`, used by F02.
- `E_ATTACHMENT_INVALID` is explicitly deferred to slice S5 (attachment upload),
  where its runtime path is implemented.
- `E_RESULT_EXPIRED` is explicitly deferred to the later application-recovery
  integration (S7), where the retention horizon is consumed.
- Do not add those two codes now. Record this reconciliation in the report so
  the re-acceptance can scope claim 7 accordingly.

## Positive authority

Edit exactly the allowlisted paths; stage exactly those paths; create one
commit on `feat/kronika-one-product`. Run the declared route checks below.

Commands (binding route):

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 5259b89a9af993e94f00c03e7962681c8ba152a4

./.ap/ap exec --root /home/agile/Projects/framenest --baseline 5259b89a9af993e94f00c03e7962681c8ba152a4 --operation test-focus -- tests/unit/chatgpt_page tests/contract/test_chatgpt_page_packaging.py tests/contract/test_chatgpt_page_js_syntax.py tests/unit/test_import_boundaries.py tests/unit/test_package_import.py tests/unit/test_api_import_boundary.py -q -p no:cacheprovider

node --test tests/capture_lifecycle.test.js tests/chatgpt_page_protocol.test.js
```

The packaging test's internal `poetry build` is part of the existing test. No
ambient Python, `poetry run` or substitute route. No browser, login, provider
or host execution; fake drivers only.

## Negative authority

- No change outside the three corrections and the vocabulary reconciliation: no
  new features, no S3+ work, no attachment/mode/records/UI/host work.
- No weakening of any S2 guarantee: single-use durable send intent, no second
  click, recovery fencing, journal retention, privacy of operational metadata.
- No dependency, lockfile, project identity, version, documentation, AP,
  ledger or protected-path change.
- No push, force, amend, rebase, reset, clean, stash, `git add -A`,
  `--no-verify` or config write. Do not read `private/**`. No subagents.
- Do not self-certify acceptance; the re-acceptance is a separate fresh
  exchange.
- If a required change falls outside the allowlist, stop and report.

## Validation

1. `./.ap/ap project check` passes before mutation and after the commit against
   the exact baseline.
2. The full declared focused route and both Node suites pass after the fix.
3. Each finding has a new regression test proving the corrected behavior and
   the negative cases above.
4. No existing S2 regression weakens: the S2 failure-injection matrix still
   passes (admission, offer, send intent, click, confirmation, result,
   recovery, retention, launch brake, privacy).
5. `git diff --name-status <baseline>..HEAD` equals the allowlist; worktree
   clean after the commit; one commit above the baseline; branch, HEAD, parent
   and tree read back.
6. AP pin, managed block, `.gitmodules`, `ap.project.conf`, upgrade ledger,
   `poetry.lock`, `pyproject.toml`, `src/framenest/**` and all documentation
   unchanged; `main`/`origin/main` still at `26d28b16`.
7. The correction introduces no path that can click twice, acknowledge
   unpersisted work, or bypass token/Host/Origin checks.

## Stopping conditions

Stop and report on: baseline, cleanliness, AP-pin or managed-block mismatch; a
finding that cannot be corrected inside the allowlist; a focused check that
fails and cannot be corrected inside the allowlist; any conflict between the
finding evidence and current repository truth; a needed dependency, host or
browser operation; or any instruction conflict. Preserve the first causal
failure; do not improvise.

## Completion and report contract

`PASS` means all three corrections and the vocabulary reconciliation are
complete within the allowlist, every regression test above passes, one commit
exists on `feat/kronika-one-product`, and no S2 guarantee weakened. Use
`PARTIAL` or `BLOCKED` honestly otherwise. No push occurred.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; per-finding
correction evidence (exact location, change, regression test, observed result);
the vocabulary reconciliation record; the full route results; changed files;
commit result with `no push`; deviations/risks/missing evidence; one smallest
next step; `Report justification: new-mutation`; authority expiry; and:

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
Downloadable prompt filename: 01_correction_04.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 01_report_04.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
