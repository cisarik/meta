### Report for ORCHESTRATOR_CHAT

Logical whole identity: upload-flow-polish
Worker session ordinal: 04
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: Acceptance
Task identity: KRN-UPLOAD-ACC-04 — independent E2 acceptance of the upload-flow polish candidate
Status: PASS
Phase-qualified result: acceptance-PASS
Result artifact or commit: 076c01658f36f38cb9c8b5a3b4b098d774767616
Result evidence: read-only candidate inspection, exact nine-path diff, and the selected gate and tests below
Start commit: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
End commit: 076c01658f36f38cb9c8b5a3b4b098d774767616
Report justification: final-acceptance
Logical-whole closure: not-closed

This session had no prior conversation about this whole. Native Plan mode was off. The candidate was not moved. `02_report_00.md` was not used as an implementation result.

Repository changes: none. The only write is this report. Purpose: independent E2 acceptance of the fixed local candidate. No commit and no push. Public `main` was `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e` by `git ls-remote https://github.com/cisarik/kronika refs/heads/main` before review. The candidate remains local and unpushed.

## Acceptance record

```text
Acceptance candidate: 076c01658f36f38cb9c8b5a3b4b098d774767616
Acceptance owner map: 01_report_00.md (accepted plan); 03_report_00.md (implementation claim); SPEC.md §18; DEVELOPMENT.md; docs/X_COMPANION.md; ADR-0053; ADR-0086; ADR-0088
Acceptance allowlist: exactly the nine changed paths in section 2
Acceptance risk claims: opt-in per-dialog auto-start; one start per permitted selection; capability/size/ownership gates; duplicate review and ordinary privacy; replacement lock and handler-level exclusion; full-offset Resume without PATCH; scoped presentation; tests and durable documentation; no API/authorization/payload/schema/protocol change; preserved shell and adjacent cockpits
Acceptance control matrix: 01_report_00.md §3-§8, fixed
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

`Primary fresh acceptances used: 1` records consumption of the issued budget by this report. No prior fresh acceptance of this candidate was used. No out-of-scope observation was recorded.

## Gate

| Check | Result |
|---|---|
| HEAD | `076c01658f36f38cb9c8b5a3b4b098d774767616` |
| Branch | `main` |
| Parent | `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e` |
| Public `main` | `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e` |
| Worktree before and after tests | clean |
| `.ap` gitlink and submodule HEAD | both `d7023cf037f6d17885c3ede5c04812c61640da50` |
| `./.ap/ap doctor` | PASS |
| `./.ap/ap project check --baseline 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e` | PASS |

The project check warned that inherited environment classes were sanitized. It did not fail and no environment repair was performed.

`git diff --stat 8646146..076c016` is exactly nine paths, 857 insertions and 20 deletions. No other path changed.

## A–G matrix

### A — Opt-in control: PASS

`index.html` places one checkbox, `#upload-auto-start-input`, immediately before `#upload-file-input`. The label is `Start automatically after choosing a file`. The hint is `For this open dialog only. Recovered uploads still need Resume.` The input has no `checked` attribute.

`app.js` keeps `uploadAutoStart` as a module binding initialized to `false`, outside the object replaced by `resetUploadForFile`. `openUploadDialog` returns immediately when the dialog is already open. On a closed-to-open transition it sets the choice false and syncs the checkbox before showing the dialog. The change listener writes only that binding, and writes nothing when the control is disabled. It does not call the start path.

`saveUploadRecovery` still stores only upload id, filename hint, expected size, last-modified hint, and last known state. A repository search shows `uploadAutoStart` is not passed to `localStorage` or `sessionStorage`. The served-shell contract asserts the same identifier is absent from every `setItem(...)` argument in the served script.

The named default/reset test shows: default off after open; the choice remains on after `resetUploadForFile`; toggling creates no POST; repeated `openUploadDialog` while open keeps the choice; close then open clears it and still creates no POST; Start stays visible for the eligible file. Recovery keys stay absent.

### B — Auto-start path: PASS

`handleUploadFileSelection` calls `handleStartUpload` once, and only after a permitted new-file or terminal-state reset when the choice is on. A byte-receiving reselection returns without starting. `handleStartUpload` calls `claimUploadAction("start")` and sets `preparing` before any `await`. The POST body remains `display_filename` and `declared_size_bytes`. `runUploadLoop` still refreshes the server offset, sends PATCH chunks, and completes when the confirmed offset reaches the declared size.

Before session creation the start path requires `upload.submit`, a capability load whose true result means `uploads_enabled`, a finite positive size, and a size no greater than `max_total_size_bytes`. A missing capability, disabled capability, network failure, empty file, or oversize file returns without POST. The `finally` block releases the start owner. No failure path schedules a timer.

`uploadProgressPercentValue` is the floored ratio of server-confirmed received bytes to declared size, capped at 100. Cataloged, published, and validating copy stay on separate status strings. The hosted test reaches `100%` while the label is still not `Completed`, then shows cataloged copy only after the complete response.

The picker test observes the start owner and zero POSTs while capability is deferred, then exactly one POST with the existing JSON body and `X-Kronika-Request: 1`. A second drop while that POST is unresolved does not create a second POST or replace the first filename. The failure test fires pending timers and the POST count stays zero.

### C — Duplicate and security: PASS

Administrator `duplicate_pending` still shows keep and discard only when `upload.manage` is present. Ordinary `duplicate_pending` still uses the validating sentence and hides both actions. Auto-start never calls duplicate resolution. The administrator auto-start test ends at `duplicate_pending` with both actions visible, the exact duplicate sentence, one create POST, and zero duplicate-resolution POSTs. The ordinary test ends cataloged, matches the administrator-review and not-public wording, contains no duplicate indication, and sends no duplicate-resolution POST.

`tailscale_ingress.py` is outside the diff. Its seven upload templates still use `CAPABILITY_UPLOAD_SUBMIT` (`upload.submit`): collection, capability, status, PATCH, complete, duplicate resolution, and DELETE. No API, authorization, payload, schema, migration, storage, or companion-protocol file changed. `companion_host.js` still has no upload-progress type. The new bridge test rejects `upload_progress`, accepts `open_upload` with an empty argument list, and asserts the sidebar posts only that type.

Ordinary `silent_keep_separate` remains server-owned. `tests/contract/test_ordinary_upload_ownership_boundary.py` was not edited and is included in the passing Python command.

### D — Concurrency and recovery: PASS

`uploadUnresolvedWorkOwnsDialog` is true while an action owner, preparing, running, completing, an upload id without a snapshot, or any snapshot that is neither byte-receiving nor a permitted terminal state (`cataloged`, `rejected`, `failed`, `cancelled`, `expired`) is current. That covers create, transfer, completion, in-flight cancel, recovery before status, validation, duplicate review, and publication/cataloging wait. `updateUploadActions` disables both the file input and the checkbox from that predicate. `handleUploadFileSelection` returns before mutating state on the same predicate.

A drop with files always calls `preventDefault`. When the input is disabled, the handler returns before assigning files or dispatching `change`. Dragover also calls `preventDefault` and sets `dropEffect` to `none` while disabled. The active-upload test keeps the first filename through a synthetic replacement and a drop, consumes dragover, and keeps one create POST for `first.gif`.

Byte-receiving with received bytes still below the declared size stays selectable. That branch checks size and hints, then stops at `Ready to resume` even when auto-start is on. It does not POST or PATCH. Explicit `handleResumeUpload` is required. The recovered half of the full-offset test covers that path and then sends one PATCH only after Resume.

`uploadReadyForCompleteOnly` is `receiving` with a positive declared size and equal received size. Resume is offered for that snapshot without requiring a local file. `handleResumeUpload` refreshes status before `runUploadLoop`. The loop's existing `remainingBytes <= 0` path completes without PATCH. If the refresh is byte-receiving and no file is present, the handler sets reselection and returns without PATCH or complete. The full-offset test records zero PATCH and one complete; the refresh-to-partial case records the reselection label and zero PATCH and complete.

Repeated `openUploadDialog` and repeated hosted `open_upload` while open do not reset the choice and do not add fetch calls. Closing does not cancel or create an upload. Reopening an existing id refreshes that id. Stale-response fencing, polling backoff, not-found cleanup, and the one-action-owner `finally` releases remain in the unchanged controller paths. Their existing tests are still present; the upload suite's only deleted line is the old `createHarness()` signature, replaced by an optional `hosted` flag that leaves the default harness parent unset.

### E — Presentation and documentation: PASS

New CSS is scoped to `#upload-dialog`: `display: flex` and `flex-direction: column` while open, checkbox layout, wrapping label and hint, and disabled-control appearance. The shared `.upload-dialog` width rule `width: min(620px, calc(100% - 40px))` is unchanged. The narrow-width `.upload-dialog` width rule is unchanged. YouTube and confirmation dialogs are not given the upload checkbox rules.

The scrollable body (`overflow-y: auto`, `flex: 1 1 auto`, `min-height: 0`) and non-shrinking footer (`flex: 0 0 auto`) are the existing upload-dialog body and footer rules. The new open-dialog flex column is what makes those flex children apply to this dialog. Rendered scrolling, clipping, focus, and contrast are not claimed; see residual risks.

`SPEC.md` §18, immediately before §19, is the normative text for the transient choice, one capability-gated start, failed-gate behavior, handler exclusion, explicit Resume, full-offset completion without PATCH, server-confirmed progress, duplicate actions, ordinary `silent_keep_separate`, and `open_upload` remaining dialog-local. §19's network heading and the following boundary were not edited.

`DEVELOPMENT.md` points at SPEC §18 for behavior and adds the focused commands, synthetic-fixture checklist, and public-main/NUC rendered-acceptance prerequisite. `docs/X_COMPANION.md` states that Upload posts `open_upload` and that progress and results stay in the hosted dialog, with the same SPEC link, in both usage passages. `SECURITY.md`, `docs/UX_AUDIT.md`, and accepted ADR bodies are absent from the diff. No new ADR was added.

### F — Tests and preserved behavior: PASS

The upload suite contains the seven named causal tests. The companion suite contains `open_upload carries no progress and a progress type does not open upload`. The served shell contains `test_upload_dialog_auto_start_is_opt_in_and_scoped`. Existing assertion lines in the upload suite were not removed. Evidence-only Python files named by the command were not edited.

The selected Node command includes the unchanged X companion, YouTube cockpit, X cockpit, shell/Timeline, gallery search, automatic-analysis, and cover suites. All passed. Upload routes and the recovery record format are unchanged, as cited under C and A. Extension production sources are outside the diff.

### G — Validation and allowlist: PASS

Counts and the clean tree are in the next section. The diff is exactly the nine allowlisted paths. No full Python suite was run. No browser or rendered-acceptance claim is made.

## Tests and commands

```text
# [MacBook / fish]
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e --operation test-focus -- tests/contract/test_local_web_application.py tests/contract/test_upload_api.py tests/contract/test_ordinary_upload_ownership_boundary.py tests/contract/test_upload_session_architecture.py tests/contract/test_atomic_upload_publication_contract.py tests/integration/test_local_web_upload_cockpit.py tests/integration/test_atomic_upload_publication.py -q -p no:cacheprovider
node --test tests/upload_cockpit_async_ownership.test.js tests/companion_web_bridge.test.js tests/x_companion_extension.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js tests/kronika_ui.test.js tests/gallery_search_tag_filters.test.js tests/automatic_analysis_lifecycle.test.js tests/cover_frontend.test.js
git diff --check
git status --short
#------------------------------------------------------
```

| Command | Result |
|---|---|
| `ap doctor` | PASS |
| `ap project check --baseline 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e` | PASS |
| selected `ap exec --operation test-focus` | 277 passed, 0 failed, 64.67s |
| selected `node --test` | 285 passed, 0 failed, 0 skipped, 0 cancelled, 4654 ms |
| `git diff --check` | clean |
| `git status --short` | empty |
| HEAD after the runs | `076c01658f36f38cb9c8b5a3b4b098d774767616` on `main` |

## Source and security findings

None. The change invokes the existing capability-gated start path. Ownership, duplicate mode, checksums, quarantine, validation, publication, and cataloging stay server-owned. No route, payload, schema, migration, storage, or companion message was added.

## UI and frozen-view findings

None in the inspected source or selected tests. Shell, Timeline, Gallery, Details, header search, and adjacent cockpit files are outside the diff, and their selected Node suites passed. Rendered frozen views were not opened.

## Documentation findings

None. SPEC §18 is the only new normative owner. DEVELOPMENT and X_COMPANION point to it. SECURITY, UX_AUDIT, and ADR bodies are unchanged.

## Allowlist review

Changed paths, and no others:

```text
DEVELOPMENT.md
SPEC.md
docs/X_COMPANION.md
src/kronika/adapters/api/web/app.js
src/kronika/adapters/api/web/index.html
src/kronika/adapters/api/web/styles.css
tests/companion_web_bridge.test.js
tests/contract/test_local_web_application.py
tests/upload_cockpit_async_ownership.test.js
```

The negative allowlist holds, including API and domain sources, persistence, authorization, schema, migration, extension production, companion protocol, `.ap/**`, the AP gitlink, `AGENTS.md`, `SECURITY.md`, `docs/UX_AUDIT.md`, and accepted ADR bodies. No new file was added.

## Deviations

None.

## Residual risks and missing evidence

Rendered geometry, native picker behavior, real Brave iframe and modal behavior, scrolling, clipping, focus, contrast, actual upload timing, and assistive-technology output are NOT TESTED. Node and contract tests do not prove them. They remain the Cooperator's later rendered acceptance after the candidate is on public `main` and refreshed onto the NUC.

A lost create response can still leave an unused server session until its existing expiry. This client guarantees one active transfer in its own runtime, not exactly-once creation across an unknown response or another tab. That limit is the accepted plan's limit; this candidate does not add an API idempotency change.

No NUC, provider, secret, or private-media evidence was gathered. None was required for these claims.

## Smallest next step

Record this independent acceptance and issue a separate publication grant for `076c01658f36f38cb9c8b5a3b4b098d774767616` only if publication is wanted. Deployment, NUC refresh, and rendered acceptance stay outside that grant.

Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none

Orchestration critique:
MEASURED: none
LEAD: none

Authority expiry: this terminal report ends the grant. No correction, publication, deployment, production, or closure authority remains.
