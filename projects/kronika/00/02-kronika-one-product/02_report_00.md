### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 02
Worker exchange ordinal: 01

Persistent role identity: WORKER
Task identity: KRONIKA-ONE-PRODUCT-S2-ACCEPTANCE
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Audit
Native planning mode: not-used
Phase: acceptance
Status: PARTIAL
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Report justification: new-evidence
Evidence tier: E3
Delivery route: manual Cooperator delivery

The frozen candidate is not accepted. The independent prescribed runs passed (62 Python tests and 28 Node tests), and the durable send barrier, recovery fencing, browser retention, launch brake, packaging and normal authenticated wire controls have supporting evidence. Additional synthetic probes reproduced two lifecycle/contract defects: administrator waiting before an offer consumes the active deadline, and an oversized result receives an untyped rejection which the runner repeatedly retries. A third, low-severity inherited contract discrepancy accepts a present empty Origin header. None of these probes demonstrated a second Send click or a token bypass. No candidate correction was made.

#### Compact core and independence

- Actual independence posture: fresh conversation with the manually delivered acceptance prompt; no earlier S2 implementation turns or implementation reasoning were inherited in the visible session. I did not implement or materially participate in the candidate. The accepted plan and implementation report were read as evidence, not as authority or conclusions. This declaration is based on this session's actual available history; no unavailable cross-session telemetry is claimed.
- Start commit = end commit: `5259b89a9af993e94f00c03e7962681c8ba152a4`.
- Tree: `97fac132581632305d4e86fdbdeca11118b83e75`; parent: `96ef426f7026c818f5e75733e8f8dfc5ac2321d1`.
- Repository: `/home/agile/Projects/framenest`; branch: `feat/kronika-one-product`; clean index and worktree at initial and final checks.
- Local `main` and `origin/main`: `26d28b16c08a5e7e0179a32c16646bfdc1009c81`, unchanged. No local remote-tracking ref for the candidate branch. These are local Git observations; no remote contact or current public-ref verification occurred.
- AP gitlink and submodule HEAD: `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`, unchanged and clean.
- Original Kronika checkout: `/home/agile/Tools/cli_chatgpt`, clean at `66c40d43c577276b0ad304a494fbbb1ffb6fc933` before and after review.
- Changed project files: none. The only durable external output is this report. Temporary synthetic probe scripts/state were removed.
- Commit/push/publication: not authorized and not performed. No Meta artifacts were committed.
- Validation: the three prescribed positive controls, targeted static inspection, six additional Python observational probes and one bounded Node probe script. Passing observational probes mean their stated observations were reproduced; they do not turn the observed defects into acceptance PASS.
- Smallest next step: the Orchestrator should issue one bounded correction grant addressing F01 and F02, and explicitly reconcile F03 and the full error-vocabulary requirement, followed by fresh acceptance of the changed lifecycle/wire boundaries. Do not grant S3 on this report as acceptance evidence.

#### Acceptance and Correction Record

```text
Acceptance candidate: 5259b89a9af993e94f00c03e7962681c8ba152a4
Acceptance tree: 97fac132581632305d4e86fdbdeca11118b83e75
Acceptance owner map: the exact 20 S2 changed paths listed below; accepted plan 01_report_00.md sections 4.1-4.3, 4.5-4.6 and S2 subset of 4.4; S2 terminal report 01_report_03.md
Acceptance allowlist: read-only candidate/governing AP inspection; declared focused routes; synthetic probes under /tmp/kronika-one-product-s2-acceptance; this terminal report
Acceptance risk claims: the eight fixed claims in the issued prompt, unchanged
Acceptance control matrix: the fixed positive and negative controls in the issued prompt, with observed results below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
Result artifact or commit: this report against the frozen acceptance candidate
Result evidence: independent prescribed tests, static inspection, contained synthetic reproductions
```

The exact changed-path inventory is 20 paths (17 modified, three added):

```text
src/kronika_capture/bridge/jobs.py
src/kronika_capture/bridge/server.py
src/kronika_capture/bridge/store.py
src/kronika_capture/bridge/journal.py
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
tests/capture_lifecycle.test.js
tests/chatgpt_page_protocol.test.js
tests/contract/test_chatgpt_page_packaging.py
tests/unit/chatgpt_page/test_bridge_security.py
tests/unit/chatgpt_page/test_job_limits.py
tests/unit/chatgpt_page/test_capture_journal.py
```

#### Scope and threat model

Security task class: fresh independent targeted lifecycle/provider/authentication acceptance, bounded to the issued claims; no broad product audit or correction authority.

Assets: single submission identity, retained job/results, active slot and readiness, local journal integrity, operational metadata privacy, browser availability and opaque profile ownership.

Trust boundaries: authenticated loopback client to bridge; bridge transaction to protocol acknowledgement; runner/offer/epoch to journal; acknowledged send intent to the owned page click; response association to terminal delivery; browser stderr to loopback CDP endpoint discovery.

Attacker-controlled inputs/local actors: synthetic unauthenticated loopback callers, synthetic authenticated request/event/result envelopes, changed request content, lost acknowledgements, persistence failure, fake browser/clock/readiness and stale lock state. A valid bridge token is trusted local authority, not a separate per-user authorization system in S2.

Security properties: no automatic resend, durable admission, fencing, bounded state, separate administrator timing, exact wire authentication, metadata minimization and no application profile-content access. Abuse/failure cases were selected only from the fixed matrix and observed related branches.

External standards: none cited; no web, provider, host, browser, SSH or external-service execution. No real credential/token/profile/private material was inspected. All HTTP credentials in added probes were explicitly synthetic constants. Governing AP Worker spine/report/stop provisions and the project execution contract were read; no new authority was inferred from the plan or prior report.

#### Per-claim verdicts

| Fixed claim | Verdict | Exact evidence and limits |
| --- | --- | --- |
| 1. Browser lifecycle | PASS within authorized fake-driver/static scope | `runner.mjs:293-379` starts once, opens one owned page, retains it through bridge failures, and caps retries at 30,000 ms. Existing tests independently reproduced two jobs/one start/one open, repeated outages, crash and startup failure without restart. `driver.mjs:250-315,883-988` plus added probes refused 299,999 ms, backward/nonfinite time, invalid/missing state and stale locks; exactly 300,000 ms succeeded. Unconfirmed termination retained lock/process. No actual Chromium was started; host service restart topology is later work. |
| 2. No automatic resend | PASS for reachable S2 capture execution | `jobs.py:389-459`, `job_engine.mjs:1502-1546`, and `runner.mjs:212-290` enforce durable single-use intent and one send attempt. Independently executed candidate tests cover admission/offer/intent/confirmation/result/recovery uncertainty. Added real `_submit` probes observed zero clicks when intent was refused, one click on click/confirmation uncertainty, and rejection of a second invocation in every case. No second click or replay of browser execution was observed. See complete click inventory below. |
| 3. Journal durability/idempotency | PASS within synthetic storage scope | `journal.py:15-96` uses SQLite FULL synchronization and a writer transaction from recovery load through epoch commit; `jobs.py:118-199,296-343,467-563` publishes committed copies, resolves known requests before readiness/capacity, fences recovery and retains terminals. Existing failure-injection tests passed at four write/ack boundaries and all recovery phases. Additional SQLite writer contention produced `database is locked`; old manager writes failed with `E_JOURNAL_UNAVAILABLE`. Existing 256-entry/24-hour/backward-clock test independently passed with no unexpired eviction. No real power-loss test was authorized. |
| 4. Readiness/administration | FAIL: F01 | Structural readiness, explicit recheck, running-job slot retention, cumulative waiting and 1,800-second expiry are supported by existing tests and inspection. However, readiness loss while a job is still queued never starts administrator accounting; the original active deadline expires and releases its slot. Synthetic reproduction below disproves the unqualified timing claim. |
| 5. Authenticated wire | PARTIAL: F03 | Loopback bind, constant-time token comparison, all tested content/readiness authentication, foreign Host/Origin rejection, exact-Origin echo, no wildcard CORS, health minimization and metadata privacy passed. `auth.py:96` also treats a present empty Origin as absent; a real loopback probe returned authenticated HTTP 200 for it. Thus the literal absent-or-exact requirement is not fully satisfied. No token bypass was demonstrated. |
| 6. No profile/credential access | PASS within inspection/fake-driver scope | No `DevToolsActivePort` reference remains under the capture package. File-read inventory shows launch metadata outside the canonical profile, packaged assets and capture-owned configuration/token files; no browser-profile content or cookie/credential/storage APIs were found in the active capture path. `driver.mjs:296-315,883-925` consumes bounded stderr only in memory; extra probes checked exact 65,536-byte cap, long-line discard and loopback/port rejection. Launch flags reject stealth and contain no sandbox weakening. Existing operator-login field forwarding remains its separately defined exception; no real login action was executed. |
| 7. Typed failures | FAIL: F02 and vocabulary gap | Core S2 codes and 400/409/429/503 mapping are established by focused tests; cancelled terminal failure remained readable with HTTP 200 in an added probe. Oversized result delivery instead receives 413/E_INTERNAL and remains nonterminal; runner retries the rejected payload. Both Python and JS error vocabularies lack `E_RESULT_TOO_LARGE`, `E_ATTACHMENT_INVALID`, `E_RESULT_EXPIRED` from plan 4.6. Future attachment/application behavior was not exercised or silently required here, but the prompt's full vocabulary claim cannot be marked PASS. |
| 8. Packaging/protected paths | PASS | Independent wheel test passed: exact source bytes for 33 capture files, both entry points loading the same callable from the extracted wheel, assets resolving without importing `framenest`. Independent tracked inventory: 15 Python modules + 18 assets. Provenance test covers exactly 32 relocated files plus only the new journal outside that set. Exact parent/candidate diff contains only the 20 paths above. All named protected paths, documentation and AP pin are unchanged. `git diff --check` passed; repository-root `dist/` absent. |

#### Positive controls: independently observed

Run from `/home/agile/Projects/framenest`:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 5259b89a9af993e94f00c03e7962681c8ba152a4

./.ap/ap exec --root /home/agile/Projects/framenest --baseline 5259b89a9af993e94f00c03e7962681c8ba152a4 --operation test-focus -- tests/unit/chatgpt_page tests/contract/test_chatgpt_page_packaging.py tests/contract/test_chatgpt_page_js_syntax.py tests/unit/test_import_boundaries.py tests/unit/test_package_import.py tests/unit/test_api_import_boundary.py -q -p no:cacheprovider

node --test tests/capture_lifecycle.test.js tests/chatgpt_page_protocol.test.js
```

| Control | Observed result |
| --- | --- |
| AP project check | Exit 0, PASS; exact baseline contract/project identity, sanitized-v1 and CPython 3.13 verified. |
| Focused Python route | Exit 0; `62 passed in 4.22s`. The internal authorized wheel build and JS syntax/protocol subprocess checks passed. |
| Node route | Exit 0; 28 tests, 28 passes, zero failures/cancellations/skips/todos; reported duration 392.610028 ms. |

The AP warning reported inherited environment variable classes sanitized by the canonical route. It was not an execution failure. No ambient Python invocation, environment repair, dependency installation or broader suite was used.

#### Negative/adversarial control matrix

| Boundary/control | Observed result |
| --- | --- |
| Unauthenticated content/readiness | Added actual HTTP probes returned 401 for GET status/job/next and POST jobs/hello/resume/job events/result/cancel. Wrong synthetic token also returned 401. |
| Host/Origin/CORS | Foreign Host, foreign Origin and literal `null` Origin returned 403. Exact loopback Origin was echoed; no tested response had `Access-Control-Allow-Origin: *`. Empty Origin exception is F03. Static comparator is `hmac.compare_digest`; non-loopback bind rejection passed the existing test. |
| Health | Unauthenticated 200 with exactly `ok`, `api`, `api_version`; no readiness/content. |
| Wrong render/route | `/s/synthetic/r/1` without authentication returned 404; authenticated unknown route returned 404; retained unavailable file route returned 501. Existing removed ingest/author/capture-auth/mode tests passed. These S2 removed render routes do not serve local result pages. |
| Admission before acknowledgement | Existing SQLite second-reader test passed before `create_job` returned. Added HTTP admission returned 200 only with a matching committed row. Injected commit failure returned 503/E_JOURNAL_UNAVAILABLE and added no job. |
| Admission lost acknowledgement | Existing parameterized commit-then-fail probe independently passed: recovery returned original queued request identity, without reexecution. |
| Offer before/after commit failure | Existing precommit failure acknowledged no offer and changed no published memory; lost acknowledgement recovered to E_AMBIGUOUS_SEND. Node offer-accept failure executed no engine. |
| Intent before/after commit failure | Existing precommit/lost-ack/recovery cases passed. Additional real submit probe refused intent with zero clicks; its second invocation returned E_AMBIGUOUS_SEND, still zero clicks. Duplicate intent and post-cancel intent were rejected in existing manager tests. |
| Click uncertainty | Existing and added CDP-click-exception probes counted exactly one attempt and E_AMBIGUOUS_SEND; repeated submit invocation did not click again. |
| Confirmation uncertainty | Existing missing-response and lost-confirmation-ack tests passed with one click and E_AMBIGUOUS_SEND. Added confirmation-ack failure reproduced the same one-click result. |
| Successful submission repeated locally | Added `_submit` success produced one click; invoking it again returned E_AMBIGUOUS_SEND and retained one click. |
| Result transaction/replay | Existing before-commit and commit/lost-ack cases passed; committed result survived recovery. Added HTTP result replay returned 200 twice under one identity. Changed-result replay conflict passed the existing test. |
| Result transport retry | Existing probe executed once and sent three identical deliveries. Added permanent-413 probe also executed once but retried the same oversized success payload three times at 250/500/1,000 ms; it was then explicitly aborted to bound the probe. F02. |
| Recovery/fencing | Existing offered/accepted/intent/confirmed recovery cases all produced ambiguity and invalidated old runner/manager writes. Added direct writer contention confirmed recovery locking, retained request identity and old-manager rejection. Corrupt/unavailable journal and recovery-commit failure tests passed without replacement. |
| Idempotency/conflict | Canonical-default replay and whitespace-sensitive conflict passed existing tests; added HTTP identical request returned original job, changed content returned 409/E_IDEMPOTENCY_CONFLICT, another active request returned 409. Blocked-service/full-journal replay priority passed existing tests. |
| Retention | Independently executed 256-terminal test refused item 257 with 429/E_SERVICE_LIMIT, returned known replay at capacity, retained all on backward time and at 86,399 seconds, then pruned at 86,400 seconds. No early eviction observed. |
| Running administrator pause/resume | Existing pre-send and confirmed-response tests passed: explicit identity and fresh readiness required, slot retained, deadline extended only by wait, association loss failed ambiguous, cumulative 100+1,700 seconds expired once with E_INTERVENTION_TIMEOUT. Fake driver was not stopped at admin expiry. |
| Queued administrator pause | Added t=0/2/10 clock probe returned E_RESPONSE_TIMEOUT with admin_wait_s=0 and zero active jobs after readiness became needs_admin. F01. |
| Cancellation/timeout | Existing cancellation/timeout tests retained terminal results and blocked readiness when stopping was unconfirmed. Added authenticated read returned cancelled failure via HTTP 200. No cancellation/timeout path observed reexecuting submission. |
| Privacy/events | Existing 80-event probe retained 64 events and discarded arbitrary DOM text. Added status/events/log marker checks found no synthetic prompt, answer or source marker in operational metadata; prompt/answer were available only on intended content surfaces. Static status/event construction admits bounded operational fields. No staging exists in S2. |
| Browser reuse/outage/crash | Existing fake driver observed one start and one page for two jobs, capped bridge backoff, zero outage shutdown, and no crash/startup auto-relaunch. Explicit final shutdown is separate. |
| Launch brake | Existing malformed/missing metadata controls passed. Added probes rejected 299,999 ms, backward time, NaN, Infinity and a precreated stale lock despite a much later time; lock remained. Exactly 300,000 ms was allowed. |
| CDP stderr/readiness | Existing structural challenge/login/consent/limit/origin/generation/CDP-loss controls passed. Additional parser probes exhausted exactly 65,536 bytes, discarded a 4,097-character line, parsed a subsequent valid line within budget, and rejected foreign host/localhost/port 65,536. No real stderr/profile/browser accessed. |
| Oversized result wire | Added actual HTTP probe supplied an over-limit Content-Length, received 413/E_INTERNAL before body acceptance, and read manager state still running/result=null. F02. |
| Specified code inventory | Direct Python and JS checks found the same three missing codes named in claim 7. No claim was made that later attachment/result-expiry integration exists. |

All required control categories received evidence. The failed properties above are reproduced failures, not unverified controls relabelled PASS. Live Chromium/provider, actual power loss and deployment behavior remain unverified by design and outside this grant.

#### Click-path inventory and evidence interpretation

- Python capture code performs no page clicks. It issues offers/events/results and launches only the explicitly selected operator login command when that command is invoked; the audit did not invoke it.
- Supported capture execution: `JobEngine.run -> _submit -> _clickRect -> ChromiumDriver.clickXY`. One Send call site exists at `job_engine.mjs:1525`, following the acknowledged durable intent. The other reachable `_clickRect` call at line 880 is the bounded Stop control in cleanup, not a retry of Send. Newline composition uses `Input.insertText` rather than Enter key dispatch.
- Driver mouse dispatch sends move/press/release with clickCount 1. It has no retry loop around the click. Navigation retries are page navigation and occur before the submission path.
- Retained `engine/dom_engine.js:392` has a DOM `ready.click()` and line 593 clicks New Chat. It is a packaged legacy asset, but the supported S2 headless runner neither imports nor injects it; the bridge only accepts the headless executor, and there is no shipped extension manifest/wiring in the 33-file capture inventory. Its unjournaled legacy submit function is not evidence that the active runner bypasses the barrier. Future activation of that asset would require separate lifecycle review; record this as a ledger candidate, not a discovered supported second-send path.
- Operator login `clickTarget`, viewport actions and login-app controls are a separate explicitly operated wizard, not an automatic capture/retry route. No real credential interaction occurred.

#### Findings

Finding ID: S2-ACCEPTANCE-F01
Title: Queued administrator intervention consumes the active response deadline
Status: confirmed
Severity: medium
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 5259b89a9af993e94f00c03e7962681c8ba152a4
Affected component and exact location: `src/kronika_capture/bridge/jobs.py:242-257` (service-only readiness update), `:418-447` (administrator timing only after running), `:547-558` (queued active deadline).
Security property: administrator waiting must retain the active job and be excluded from active-response time, with its own 1,800-second cap.
Asset at risk: admitted job availability and correct terminal/intervention state.
Trust boundary: runner readiness report to durable job/watchdog accounting.
Attacker-controlled input or local actor: no adversary required; synthetic valid runner reports login intervention after admission but before offer.
Reachability: ordinary `create_job -> hello(needs_admin) -> watchdog`; the existing test explicitly supports queued resume, but only tests immediate resumption.
Preconditions: admitted queued job, readiness changes before offer, operator takes longer than the remaining active deadline.
Required privileges: local authenticated runner; ordinary timing can trigger the condition.
Observed or potential impact: the job fails early with E_RESPONSE_TIMEOUT, admin_wait_s stays zero, and its active slot is released. The later administrator cannot safely continue that request as a paused queued job.
C/I/A effect: availability and lifecycle-state integrity; no confidentiality loss or repeat send demonstrated.
CWE mapping: none.
ASVS mapping: none.
Source-standard references: none; accepted plan 4.1-4.2 and fixed claim 4 are the requirement.
Dynamic reproduction evidence: synthetic clock t=0, ready manager, job timeout_s=10; at t=2 same runner/browser hello reports needs_admin/E_LOGIN_REQUIRED; at t=10 watchdog. Observed service needs_admin, job failed/E_RESPONSE_TIMEOUT, admin_wait_s=0, jobs.active=0. Added `test_queued_admin_wait_observation` passed those observation assertions through the declared AP route.
Static evidence: `hello` commits only service state for this branch; `watchdog` exempts only jobs whose status equals needs_admin from active timeout.
Synthetic containment: the declared 0700 root, subdirectory queued-admin, synthetic journal/clock only; removed.
False-positive analysis: no offer or send occurred, and the test extended connection freshness to avoid confusing a heartbeat disconnect with administrator timing. Running-job pause tests passing do not cover this queued state. A deliberate exclusion of queued intervention from the contract would require explicit contract reconciliation, not an auditor assumption.
Exploitability conclusion: not applicable; demonstrated ordinary lifecycle defect.
Smallest safe correction direction: durably account for administrator blocking of an admitted queued job, retain its slot, and preserve its pre-offer phase across explicit readiness resume with cumulative administrator timing.
Regression-test requirement: readiness loss before offer; wait beyond the remaining active deadline; assert retained job/slot and excluded wait, then test explicit resume and the exact cumulative 1,800-second expiry.
Residual risk: correction must preserve queued recovery and offer fencing and avoid granting a send while readiness is blocked.
Acceptance-blocking decision: blocking for fixed claim 4.
Redaction requirements: synthetic state only; no profile, credential, prompt/answer or local secret values in evidence.

Finding ID: S2-ACCEPTANCE-F02
Title: Oversized results are not terminally classified and permanent rejection is retried
Status: confirmed
Severity: medium
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 5259b89a9af993e94f00c03e7962681c8ba152a4
Affected component and exact location: `src/kronika_capture/bridge/server.py:288-290`; `src/kronika_capture/_assets/extension/src/headless/runner.mjs:271-290`; `src/kronika_capture/errors.py:10-44`; corresponding `protocol.js` ERROR_CODES.
Security property: an unacceptably large complete result must end in a readable typed failure; result-delivery retry must not treat permanent size rejection as recoverable transport loss.
Asset at risk: durable terminal result, accurate job status and runner availability.
Trust boundary: captured result serialization to bounded authenticated bridge admission and durable completion.
Attacker-controlled input or local actor: oversized synthetic answer/result; no malicious actor or live provider needed.
Reachability: a completed ask can yield a result whose serialized bytes exceed BODY_MAX_BYTES (2,097,152). The active runner sends the full payload without a typed size fallback.
Preconditions: otherwise accepted/confirmed job and a result larger than the wire body cap.
Required privileges: authenticated runner to reproduce the wire request; normal capture may produce the oversized answer.
Observed or potential impact: bridge returns 413/E_INTERNAL without recording a terminal failure. The runner retries the identical oversized done payload. The job remains running until some independent lifecycle event intervenes; E_RESULT_TOO_LARGE is never produced. No browser reexecution occurred.
C/I/A effect: result/lifecycle integrity and availability; no credential or content disclosure demonstrated.
CWE mapping: none.
ASVS mapping: none.
Source-standard references: none; accepted plan 4.4/4.6 and fixed claim 7 are the requirement.
Dynamic reproduction evidence: a real contained loopback request with a truthful over-limit Content-Length was rejected before its body with 413/E_INTERNAL; manager read remained running/result=null. Separately, the real executeOffer retry loop with an Engine returning 2,097,153 synthetic answer characters and a client raising that exact HTTP error executed once and delivered the same result identity three times, sleeping 250/500/1,000 ms. A probe abort bounded further retries. This proves the two boundaries separately; no live end-to-end provider execution is claimed.
Static evidence: the runner retries every result-delivery error except 404/409, after clearing its heartbeat; the server's early body rejection is E_INTERNAL and never reaches resolve. Neither error vocabulary contains E_RESULT_TOO_LARGE. Both also lack E_ATTACHMENT_INVALID and E_RESULT_EXPIRED specified in plan 4.6; later attachment/application behavior remains outside the runtime probe scope.
Synthetic containment: declared 0700 root, oversized-result journal and in-memory generated text/fake client; all removed or process-local and released.
False-positive analysis: HTTP 413 is correctly a size rejection, but its existence is not the promised typed terminal job failure. Static code confirms the result serialization has no earlier byte-limit conversion. Only three retries were executed; an indefinite retry conclusion follows from the loop under sustained 413, rather than an unbounded experiment. Provider likelihood is unmeasured and does not remove the reachable wire contract defect.
Exploitability conclusion: not applicable; demonstrated result-delivery/lifecycle defect, not a demonstrated attack.
Smallest safe correction direction: establish a byte-accurate result limit and persist a small E_RESULT_TOO_LARGE terminal envelope under the job/delivery identity; classify permanent delivery rejection without rerunning capture. Reconcile the missing declared vocabulary explicitly, preserving later-slice scope.
Regression-test requirement: serialize an oversized complete result through runner and real loopback bridge; assert one engine execution, bounded delivery, a durable typed terminal failure and authenticated HTTP 200 status read, including retry/recovery of that failure envelope.
Residual risk: envelope overhead and Unicode bytes matter; a correction must not truncate content while labelling it complete or weaken the durable result/offer identity.
Acceptance-blocking decision: blocking for fixed claim 7.
Redaction requirements: generate bounded synthetic text; never include captured real answer or credential data.

Finding ID: S2-ACCEPTANCE-F03
Title: Present empty Origin is accepted as absent
Status: confirmed
Severity: low
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 5259b89a9af993e94f00c03e7962681c8ba152a4
Affected component and exact location: `src/kronika_capture/bridge/auth.py:95-100`, reached through `server.py` authentication.
Security property: literal absent-or-exact approved loopback Origin validation.
Asset at risk: consistency of the declared request-origin boundary.
Trust boundary: HTTP Origin header to loopback API authorization checks.
Attacker-controlled input or local actor: a loopback HTTP caller can supply an empty Origin header.
Reachability: GET /v1/status with `Origin:` present but empty.
Preconditions: correct loopback Host; a valid token is still needed for content/readiness.
Required privileges: local caller with synthetic valid bridge token for the accepted status read.
Observed or potential impact: authenticated status returns HTTP 200 for an Origin value that is neither absent nor the exact approved origin. Without a token, the same request returns 401. No token bypass, cross-origin browser exploit or content disclosure is demonstrated.
C/I/A effect: no direct compromise demonstrated; strict contract discrepancy only.
CWE mapping: none.
ASVS mapping: none.
Source-standard references: none; fixed claim 5 and plan 4.6.
Dynamic reproduction evidence: actual contained loopback HTTP status requests with empty Origin returned [401 without token, 200 with synthetic valid token]. Foreign and literal null origins returned 403 in the main probe.
Static evidence: the condition is `origin is not None and origin != ""`; empty values skip comparison. Parent and candidate auth.py share blob `da73b391e341bb21903eab4bad0d374e13464013`.
Synthetic containment: declared 0700 root, empty-origin synthetic bridge; shut down and removed.
False-positive analysis: treating empty Origin as absent may be an intended compatibility policy, and token enforcement remains intact. However, that exception is not in the fixed absent-or-exact claim. It is inherited, not newly introduced by S2. Do not describe it as an exploitable CORS bypass.
Exploitability conclusion: not demonstrated.
Smallest safe correction direction: the Orchestrator must either explicitly reconcile the contract exception or authorize rejecting present empty Origin. The auth.py correction path lies outside the S2 changed-path list and requires an explicit new allowlist if chosen.
Regression-test requirement: distinguish absent, empty, exact, null and foreign Origin while retaining token enforcement and no wildcard CORS.
Residual risk: accepting this exception must be explicit; no broader CORS assurance follows from these synthetic cases.
Acceptance-blocking decision: prevents an unqualified PASS of fixed claim 5; low-severity contract issue, not a demonstrated security compromise.
Redaction requirements: synthetic token only; no authorization value persisted in the report.

#### Containment, provenance and cleanup

```text
Temporary root: /tmp/kronika-one-product-s2-acceptance
Owner: assigned acceptance WORKER
Mode: 0700, verified before removal
Contents class: synthetic probe scripts, disposable SQLite journals, metadata/log fixtures, launch-lock fixtures and pytest temporary directories only
Network targets: only probe-owned 127.0.0.1 listeners on ephemeral ports
Cleanup owner: assigned acceptance WORKER
Cleanup outcome: removed; exact path absence verified
```

Every added HTTP server was shut down, closed and its thread joined; opened journals/readers were closed. The Node result probe was bounded by explicit abort after three delivery failures. No browser child process was spawned. Cleanup verified ownership, directory mode, no symlink and exact realpath, then removed only the declared root without wildcard cleanup. The prescribed repository suites ran unchanged with their existing internal fixture mechanisms; their declared execution route was not replaced by a new harness/toolchain.

Transient probe source hashes before removal:

```text
test_acceptance.py  04da7c9873f1abc0f4d9903c073f591b67d91ecfcff5ea52e39921bc9711dec0
acceptance.mjs      fbd9e1673e58833b1637ff84100337e6fb8b6c92d4dd1d8105d31b76630deff6
```

Additional probe invocations used the same baseline-bound `test-focus` operation and existing pytest installation, selecting `/tmp/kronika-one-product-s2-acceptance/test_acceptance.py`, then only the newly added oversize and empty-Origin functions. Options were `-q -s -p no:cacheprovider --basetemp` with exact subdirectories of the declared root. Observed results: 4 passed in 0.07s, 1 passed in 0.07s, 1 passed in 0.06s. `node /tmp/kronika-one-product-s2-acceptance/acceptance.mjs` exited 0 and emitted the bounded observations recorded above. These files were probes, not committed regressions or candidate corrections.

Report destination: `/home/agile/meta/projects/kronika/00/02-kronika-one-product/02_report_00.md`. The parent realpath matched the authorized destination and the report was absent before creation. Trace remains private historical evidence only, with archival/publication owned by the Cooperator. No acceptance or next-phase authority is granted by persisting it.

#### Residual risk, limitations and critique

F01 and F02 remain uncorrected. F03 remains an explicit inherited exact-contract exception, not an accepted residual risk. No Worker residual-risk acceptance is granted. Missing attachment/result-expiry error names require explicit scope reconciliation; their future integrations were not audited. The inactive DOM submit asset is a ledger candidate for any future activation, not authority to change packaging or reopen S1.

All runtime evidence is synthetic. No real Chromium, login, page DOM, provider answer, host service, NUC, deployment, full suite, sdist or current public branch state was tested. The tests therefore establish code and contained lifecycle behavior, not current provider compatibility or production readiness. No external source claims were used.

Orchestration critique:
MEASURED: The full claim-7 vocabulary includes E_ATTACHMENT_INVALID and E_RESULT_EXPIRED, absent from both current protocol lists, while corresponding runtime integrations belong to later slices; effect: the full vocabulary assertion cannot pass by relying only on S2's existing tests; smallest correction: explicitly bind each required code to S2 or a named deferred slice without weakening E_RESULT_TOO_LARGE handling for existing ask results.
LEAD: none

Resolved Execution Issues / Near-Misses: An initial combined governance read exceeded output limits; the governing FrameNest AP Worker spine, report/stop anchors and relevant contracts were then read in bounded sections before substantive execution. No secret output, gate bypass, code correction, environment repair, subagent or parallel workstream occurred. All prescribed gates ran through the declared routes.

Pre-existing Failure Classification: No prescribed suite failed. The generic 413/E_INTERNAL body rejection and missing error names are statically present in parent 96ef426f7026c818f5e75733e8f8dfc5ac2321d1; F03's authentication implementation is byte-identical in parent and candidate. No parent runtime was executed, so no dynamic pre-existing-test-failure exemption is claimed. The new queued-intervention and durable-delivery contracts are evaluated against the candidate regardless of inherited mechanisms.

Authority expiry: this terminal acceptance report expires the complete current Worker grant, including unused probe/report authority. No autonomous correction, further audit, S3 work, Meta commit, publication or deployment follows. Logical-whole closure remains not-closed.
