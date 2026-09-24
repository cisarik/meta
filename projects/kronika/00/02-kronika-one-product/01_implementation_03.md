# Kronika one product — S2 durable submission and persistent browser

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 01
Worker exchange ordinal: 04
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S2
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: the submission barrier and crash recovery cross process, journal and browser boundaries, where a wrong path can double-send a prompt or acknowledge unpersisted work; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Current-session renewal

Continuity anchor: terminal PASS report `01_report_02.md` for task
`KRONIKA-ONE-PRODUCT-S1`, Worker session 01, exchange 03, ending at accepted
relocation commit `96ef426f7026c818f5e75733e8f8dfc5ac2321d1`.
Authority renewal: that exchange's authority expired at its terminal report.
This exchange grants complete new bounded implementation authority for S2 only.
Reuse rationale: the same healthy session holds the plan and the relocated
kernel; retained understanding of the bridge, job manager and runner reduces
error for the lifecycle work that builds directly on them. No independence is
required for implementation; the required independent review is a separate
fresh exchange.
Repository and environment re-gating: required before mutation; re-establish
every gate below from current evidence, never from memory.
Retained context: convenience only, never authority. On any conflict between
retained context and current repository evidence, stop and report.
Evidence posture: non-independent.
New terminal report: required (`01_report_03.md`).

## Starting state (verified at issuance)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `96ef426f7026c818f5e75733e8f8dfc5ac2321d1`, parent
  `93e7742d56d46d4725d4561bd8751b15e55e5eb5`, tree
  `570e99abb77b062b7a3ac3c6f7f9f0be5d74dda3`, subject
  `feat(capture): relocate kernel into kronika_capture`; clean index and
  worktree. Local `main` = `origin/main` =
  `26d28b16c08a5e7e0179a32c16646bfdc1009c81` (unmoved).
- Governing AP gitlink and detached `.ap` HEAD:
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- The capture kernel lives only under `src/kronika_capture/**` (32 files);
  `vendor/` holds no tracked file; both entry points resolve to
  `kronika_capture.cli:main`.
- Current capture jobs are principally in memory; terminal persistence does not
  provide crash-safe submission idempotency; runner bridge failures can exit
  through browser shutdown; the submission path contains a possible
  second-click retry. These are the behaviors this slice corrects.
- Bridge defaults: `127.0.0.1:8765`; CLI has `ask`, `bridge run`,
  `bridge status`, `login`.

## Implementation authority record

Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Exact baseline: `96ef426f7026c818f5e75733e8f8dfc5ac2321d1`
Changed-path allowlist:

```text
src/kronika_capture/bridge/jobs.py
src/kronika_capture/bridge/server.py
src/kronika_capture/bridge/store.py
src/kronika_capture/bridge/journal.py            (new)
src/kronika_capture/config.py
src/kronika_capture/errors.py
src/kronika_capture/client.py
src/kronika_capture/cli.py
src/kronika_capture/_assets/extension/src/protocol.js
src/kronika_capture/_assets/extension/src/engine/interventions.js
src/kronika_capture/_assets/extension/src/headless/bridge_client.mjs
src/kronika_capture/_assets/extension/src/headless/driver.mjs
src/kronika_capture/_assets/extension/src/headless/job_engine.mjs
src/kronika_capture/_assets/extension/src/headless/runner.mjs
tests/unit/chatgpt_page/**                       (existing tests updated; new journal/readiness/admin tests)
tests/capture_lifecycle.test.js                  (new)
tests/chatgpt_page_protocol.test.js
tests/contract/test_chatgpt_page_packaging.py
```

Implementation boundaries: the positive and negative authority below.
Independence required: no

## Goal

Make capture submission durable and the browser persistent: one Chromium
instance survives ordinary jobs and bridge outages; an uncertain send can
never repeat; an administrator intervention pauses and safely resumes work.
Repository code and fake-driver tests only. No host, browser, login or provider
execution.

## Governing decisions (binding; from the accepted plan, do not reopen)

These are the accepted plan's section 4.1–4.6 contracts for this slice. The
full text is in `01_report_00.md`; where this grant summarizes, the plan
governs.

### State machines

```text
Service:
  starting -> ready
  ready -> needs_admin | browser_unavailable
  needs_admin -> explicit resume -> readiness check -> ready
  browser_unavailable -> authorized manual recovery -> readiness check

Job:
  queued -> offered -> running -> done | failed | cancelled
                       +-> needs_admin -> safe continuation
                                        or failed/cancelled
```

A paused job retains the only active slot. Persist the job phase, runner
instance, offer identity, submission state and intervention timing.

### Submission barrier

```text
not_started
send_intent_persisted
send_confirmed
```

Before any send action, the runner must receive acknowledgement that send
intent was durably recorded. If that write fails, it must not click Send.
Remove the existing second-click retry. A missing acknowledgement after a click
is not evidence that nothing was sent.

Safe continuation rules:

- Before send, resume only when the same job/page phase is known and readiness
  passes.
- After confirmed send, continue observing the same identified response where
  that association remains provable.
- Never submit again to recover an uncertain response.
- Lost association, uncertain click or ambiguous crash recovery ends with
  `E_AMBIGUOUS_SEND`.
- Repeated result delivery may be retried with the same job/result identity;
  browser execution may not.

A bridge restart reconciles its journal before accepting work. Uncertain
in-flight jobs become typed failures. A durably queued job that was never
offered may remain queued. Old offers cannot execute after their runner/offer
identity is invalidated. Cancellation and timeout never trigger resubmission.
If stopping the current page activity cannot be confirmed, service readiness
remains blocked even after the job becomes terminal.

### Readiness and administrator intervention

Readiness examines bounded structural evidence on the runner-owned page:
browser/CDP connection and owned target exist; allowed page origin is correct;
composer and required mode controls are available; no login, consent, Turnstile
or service-limit state blocks work; no previous generation remains ambiguously
active. Do not inspect model/reasoning controls, unrelated tabs, history or
profile contents.

`needs_admin` records a typed reason, job ID, phase and elapsed wait.
Administrator status exposes operational metadata only; another owner's prompt,
answer, title and source URL remain private. An explicit resume invokes
readiness again; it is not a blind state reset. The cumulative administrator
wait per job is limited to 1,800 seconds and excluded from active-response
timeout accounting. Expiry produces `E_INTERVENTION_TIMEOUT`, ends the job and
cleans its attachment; it does not terminate Chromium.

### Process lifecycle

- Ordinary jobs reuse the same browser process and owned page context.
- Bridge transport failure causes capped reconnection backoff while Chromium
  remains alive; a bridge restart must not shut the browser down.
- A browser crash blocks service readiness. No automatic browser restart.
- Keep the runner service out of web-service restart dependencies.
- Enforce at least 300 seconds between browser starts using persisted launch
  metadata outside the profile and an exclusive launch lock. A backward clock
  or unverifiable last-start state must not bypass the brake.
- A problematic profile is not replaced automatically.
- Replace the `DevToolsActivePort` profile read with bounded in-memory parsing
  of Chromium's emitted DevTools endpoint. Discard unrelated browser stderr; do
  not log it. This removes application reads from profile contents.
- Use an explicitly configured, preflight-verified Chromium executable. Do not
  enable stealth or weaken its sandbox.

### Bridge endpoints and wire contract (this slice's subset)

Preserve existing compatible job fields and response names.

| Endpoint | Contract |
|---|---|
| `POST /v1/jobs` | Existing JSON fields plus required `request_id`; existing successful HTTP 200 response extended with status and request identity. |
| `GET /v1/jobs/{job_id}` | Status, timestamps, intervention metadata and terminal result. |
| `POST /v1/jobs/{job_id}/cancel` | Idempotent cancellation request; repeated terminal cancellation does not change the result. |
| `GET /v1/status` | Authenticated service readiness, supported capabilities, opaque browser-session identity, adapter identity and active-job metadata. |
| `POST /v1/resume` | Authenticated explicit resume with expected job/intervention identity; readiness check required. |
| Existing runner endpoints | Extend `/v1/hello`, `/v1/next`, job events and result submission; retain one manager. |

`POST /v1/attachments` belongs to S5 and is not implemented now; `files`
remains a list of server attachment IDs (empty in this slice's contexts).
Modes are `null` for ordinary ask; `web_search`/`deep_research` completion
belongs to S4 — this slice must not fake them. Preserve timeout bounds: default
600 seconds, maximum 3,600 seconds; administrator waiting has its separate
limit. The runner-only offer may resolve attachment IDs to validated
server-owned paths; public job/status responses never return staging paths.

### Idempotency and journal

- Use a server-generated application UUID as `request_id`; the CLI also
  generates an ID for its request.
- Canonicalize defaults and immutable request content. Preserve prompt
  whitespace. Compare attachment content by its recorded digest and size.
- Identical request/content returns the original job, including after
  completion or while service readiness is blocked.
- Different content under the same ID returns `E_IDEMPOTENCY_CONFLICT`.
- Resolve known retries before applying busy, readiness or capacity checks.
- Persist admission before acknowledging it.
- Keep active jobs and retain terminal jobs/results for 24 hours after
  termination. Maximum retained job count is 256. Do not evict unexpired
  entries to admit another job.
- Journal failure blocks admission/submission; do not swallow persistence
  errors.
- Bound operational events; do not store unbounded DOM snapshots or progress
  text.
- The journal is transient capture coordination state, not another family
  library.

The durable journal is standard-library SQLite behind the existing
`JobManager` (`bridge/journal.py`); no new dependency.

### Errors and authentication

Use the existing error envelope with fixed, safe messages. Add the typed codes
this slice's paths produce, at least: `E_BROWSER_UNAVAILABLE`, `E_NEEDS_ADMIN`,
`E_BUSY`, `E_SERVICE_LIMIT`, `E_RESPONSE_TIMEOUT`, `E_INTERVENTION_TIMEOUT`,
`E_CANCELLED`, `E_IDEMPOTENCY_CONFLICT`, `E_AMBIGUOUS_SEND`,
`E_JOURNAL_UNAVAILABLE`. Do not add attachment, mode-specific or result-size
errors before their slices; retain the codes that already exist.

Use HTTP 400 for malformed input, 409 for busy/conflict, 429 for
capacity/service limits and 503 for unavailable service. Terminal job failures
remain available through successful status reads. Bind only `127.0.0.1`,
default port 8765. Keep exact Host validation, absent-or-exact approved
loopback Origin, constant-time token comparison and no wildcard CORS. The
existing unauthenticated health endpoint may expose only liveness/protocol
identity; readiness remains authenticated. The token never reaches a frontend
client, report or log.

## Out of scope (do not implement)

- S4 Search/Research modes, export and markdown/sanitize modules.
- S5 attachment upload/staging and `/v1/attachments`.
- S6 records/ownership/privacy, migrations, API/UI, application capture client.
- Any host, NUC, deployment, systemd, database, browser, login or provider
  execution.
- Any dependency, lockfile, project identity or version change; any
  `src/framenest/**` change; any documentation change; any AP change.

## Positive authority

Edit exactly the allowlisted paths; stage exactly those paths; create one
commit on `feat/kronika-one-product`. Run the declared route checks below.

Commands (binding route):

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 96ef426f7026c818f5e75733e8f8dfc5ac2321d1

./.ap/ap exec --root /home/agile/Projects/framenest --baseline 96ef426f7026c818f5e75733e8f8dfc5ac2321d1 --operation test-focus -- tests/unit/chatgpt_page tests/contract/test_chatgpt_page_packaging.py tests/contract/test_chatgpt_page_js_syntax.py tests/unit/test_import_boundaries.py tests/unit/test_package_import.py tests/unit/test_api_import_boundary.py -q -p no:cacheprovider

node --test tests/capture_lifecycle.test.js tests/chatgpt_page_protocol.test.js
```

The packaging test's internal `poetry build` is part of the existing test. No
ambient Python, `poetry run` or substitute route. No browser, login, provider
or host execution; fake drivers only.

## Negative authority

- No push, publication, remote change, force, amend, rebase, reset, clean,
  stash, `git add -A`, `git add .`, `--no-verify`, `--no-gpg-sign` or config
  write. Do not read `private/**`. No subagents.
- No attachment upload, mode restoration, records work, UI, migrations, host
  work or deployment.
- No stealth, sandbox weakening, model/reasoning inspection, cookie/profile
  reading, or credential access.
- Do not weaken existing token, Host/Origin, CORS, loopback or render-key
  invariants.
- If a required change falls outside the allowlist, stop and report.

## Validation

1. `./.ap/ap project check` passes before mutation and after the commit against
   the exact baseline.
2. The focused Python route and the two Node suites pass; the updated packaging
   test still verifies the wheel inventory (now including `bridge/journal.py`)
   while provenance continues to cover exactly the 32 upstream-relocated files.
3. New fake-driver lifecycle tests prove: one browser launch across multiple
   jobs; bridge-outage reconnection without browser restart or shutdown; browser
   crash blocks readiness with no automatic restart; pause/resume around
   `needs_admin` with the readiness check; timer separation (admin wait excluded
   from active-response timeout); no automatic resend on any uncertain path;
   journal recovery makes uncertain in-flight jobs typed failures; idempotent
   replay returns the original job; `E_IDEMPOTENCY_CONFLICT` on changed content;
   24 h/256 retention bounds; admission-before-acknowledgement; restart brake
   of at least 300 seconds including a backward-clock case.
4. Failure injection covers admission, offer, send intent, click, result and
   journal recovery boundaries.
5. `git diff --name-status <baseline>..HEAD` equals the allowlist; worktree
   clean after the commit; one commit above the baseline; branch, HEAD, parent
   and tree read back.
6. AP pin, managed block, `.gitmodules`, `ap.project.conf`, upgrade ledger,
   `poetry.lock` and `src/framenest/**` unchanged; `main`/`origin/main` still at
   `26d28b16`.
7. No path can re-click Send, restart Chromium on bridge loss, or acknowledge
   unpersisted work.

Evidence before S3: a fresh independent targeted lifecycle/provider/
authentication review report proving single launch, reconnect, pause/resume,
timer separation and no automatic resend. That review is a separate fresh
exchange and is not performed by this Worker.

## Stopping conditions

Stop and report on: baseline, cleanliness, AP-pin or managed-block mismatch; an
unexpected pre-existing change; a needed change outside the allowlist; a
focused check that fails and cannot be corrected inside the allowlist; a
required dependency, host, browser or provider operation; an unresolved
instruction conflict; or any path that cannot be made safe within the allowlist.
Preserve the first causal failure; do not improvise a workaround and never
commit a state that can double-send or acknowledge unpersisted work.

## Completion and report contract

`PASS` means the S2 lifecycle, journal, idempotency, readiness/admin and
endpoint work is complete within the allowlist, all validation above passed,
and one commit exists on `feat/kronika-one-product`. Use `PARTIAL` or `BLOCKED`
honestly otherwise. No push occurred. This report is implementation evidence
only; it is not independent acceptance and does not authorize S3.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core: status;
`Phase-qualified result: implementation-PASS` (or `not-applicable` on failure);
start and end commit; changed files and purpose; validation results including
the failure-injection matrix; commit result with `no push`; deviations/risks/
missing evidence; one smallest next step; `Report justification: new-mutation`;
authority expiry; and:

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
Downloadable prompt filename: 01_implementation_03.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 01_report_03.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
