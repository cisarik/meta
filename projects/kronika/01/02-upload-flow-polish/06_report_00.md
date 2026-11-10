### Report for ORCHESTRATOR_CHAT

Logical whole identity: upload-flow-polish
Worker session ordinal: 06
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: Acceptance
Task identity: KRN-UPLOAD-ACC-06 — full-fresh E2 re-acceptance of the unconditional-start upload correction
status: PASS
Phase-qualified result: acceptance-PASS
Start commit: 076c01658f36f38cb9c8b5a3b4b098d774767616
End commit: 0a96fc18b49191a32e7f482c4e881ad714db094a
Report justification: final-acceptance
Logical-whole closure: not-closed

This session had no prior conversation about this whole. Native Plan mode was off. The audit is read-only. No repository file was edited, and the candidate was not moved.

## Acceptance record

```text
Acceptance candidate: 0a96fc18b49191a32e7f482c4e881ad714db094a
Acceptance owner map: 01_report_00.md (accepted plan); 03_report_00.md (implementation); 04_report_00.md (prior acceptance at 076c016); 05_report_00.md (correction); SPEC.md §18; DEVELOPMENT.md; ADR-0053; ADR-0086; ADR-0088
Acceptance allowlist: exactly the nine changed paths relative to 8646146 in section 2
Acceptance risk claims: unconditional start; removed checkbox and Start control; capability/size/ownership gates; duplicate review and ordinary privacy; replacement lock and handler-level exclusion; full-offset Resume without PATCH; scoped presentation; tests and durable documentation; no API/authorization/payload/schema/protocol change; preserved shell and adjacent cockpits
Acceptance control matrix: 01_report_00.md §3-§8 as amended by 05_correction_00.md; fixed
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

The prior acceptance of `076c016` is historical context only. Every verdict below was re-established from candidate `0a96fc18b49191a32e7f482c4e881ad714db094a` and the commands in this exchange. `02_report_00.md` was not used as an implementation result.

## Gate

```text
HEAD: 0a96fc18b49191a32e7f482c4e881ad714db094a
branch: main
parent: 076c01658f36f38cb9c8b5a3b4b098d774767616
public origin/main: 076c01658f36f38cb9c8b5a3b4b098d774767616
.ap gitlink and submodule HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
worktree before and after the runs: clean
ap doctor: PASS
ap project check --baseline 076c01658f36f38cb9c8b5a3b4b098d774767616: PASS
```

`ap doctor` and `ap project check` printed `WARN sanitized inherited environment classes: GIT_CONFIG_VALUE_0 SSH_AUTH_SOCK PATH GIT_CONFIG_KEY_0 GIT_CONFIG_COUNT` and then PASS. That warning did not fail the gate.

Whole diff `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e..0a96fc18b49191a32e7f482c4e881ad714db094a` is exactly the nine allowlisted paths (739 insertions, 51 deletions) across commits `076c016` and `0a96fc1`. Correction diff `076c016..0a96fc1` is exactly the seven correction paths (74 insertions, 223 deletions). `tests/companion_web_bridge.test.js` and `docs/X_COMPANION.md` have an empty correction diff.

## Matrix

### A Removed controls — PASS

`index.html` upload dialog, from `<dialog id="upload-dialog"` through its footer, contains the file input, progress, close, Pause, Resume, Keep as separate item, Discard duplicate, and Cancel. It contains no checkbox, no `upload-auto-start` markup, no helper sentence, and no `upload-start-button` / `Start upload` control. The header still has `#upload-open-button`. The correction diff deletes only the checkbox block and the Start button from this dialog.

`app.js` no longer contains `uploadAutoStart`, `uploadAutoStartInput`, `syncUploadAutoStartControl`, `uploadStartButton`, the checkbox listener, the Start listener, checkbox disabling, or the unused `startVisible` calculation. `updateUploadActions` no longer references a Start button. `openUploadDialog` returns immediately when `uploadDialogIsOpen()` is true and no longer resets an auto-start flag. The repeated-open test keeps the dialog open and adds no fetch calls while a start is in flight.

Scoped CSS remains:

```text
#upload-dialog[open] { display: flex; flex-direction: column; }
#upload-dialog .upload-file-input:disabled + .upload-file-trigger { cursor: not-allowed; opacity: 0.55; }
```

The correction deletes only `.upload-auto-start` rules, including the checkbox half of the disabled-label selector and the narrow-layout auto-start wrap. Shared `.upload-dialog` geometry, including `width: min(620px, calc(100% - 40px));`, is outside both diffs. The served-shell contract asserts that width string and the flex rule, and asserts `.upload-auto-start` is absent.

### B Unconditional start — PASS

`handleUploadFileSelection` calls `resetUploadForFile(file)` and then `handleStartUpload()` when there is no snapshot or the snapshot is terminal (`cataloged`, `rejected`, `failed`, `cancelled`, `expired`). A drop assigns the first file and dispatches `change`, so it uses that same handler. `setupUploadDropZone` is the only drop path.

`handleStartUpload` calls synchronous `claimUploadAction("start", ...)` before `loadUploadCapability` and before `POST /api/uploads`. The picker test observes `actionKind === "start"` and zero create posts while the capability response is still pending, then exactly one post:

```text
{"display_filename":"picked.gif","declared_size_bytes":8}
```

with `Content-Type: application/json` and `X-Kronika-Request: 1`. The drop test observes the same single-post contract for `dropped.gif`. A second drop during that in-flight create leaves the post count at 1 and the file name at `dropped.gif`.

The create body is only `display_filename` and `declared_size_bytes`. `runUploadLoop` still refreshes status, slices from the server offset, and sends `PATCH` with `application/offset+octet-stream` and `Upload-Offset`. `completeUploadIfReady` still `POST`s the existing complete endpoint. `uploadProgressPercentValue` is `floor(received / declared * 100)` capped at 100. The hosted test shows `100%` while the label is not `Completed` and the message is still completing byte reception; `Completed` appears only after the cataloged snapshot.

Nothing in the recovery record stores an auto-start choice. `saveUploadRecovery` writes only `upload_id`, `file_name_hint`, `expected_size_bytes`, `last_modified_hint`, and `last_known_state`. The served script's `setItem` calls contain neither `uploadAutoStart` nor `auto-start`.

Failed gates return before session creation:

- missing `upload.submit`: no capability GET and no POST; message matches "not available";
- `uploads_enabled: false`: no POST; message matches "not configured";
- size `0`: no POST; message matches "non-empty";
- size above `max_total_size_bytes`: no POST; message matches "too large";
- capability request rejection: no POST; message matches "could not be loaded".

Draining active timers after those failures does not add a POST. There is no retry timer on those returns. After `finally` releases the action and clears `preparing`, `uploadUnresolvedWorkOwnsDialog()` is false when no upload id exists, so a later `change` is the retry through the same start path.

### C Duplicate and security — PASS

Administrator `duplicate_pending` after an automatic start shows `Duplicate found`, enables Keep and Discard, and sends zero `duplicate-resolution` posts. Only `handleKeepDuplicate` and `handleDiscardDuplicate` call `submitDuplicateResolution`, with `keep_separate` and `discard`. Automatic start does not call them.

An ordinary identity limited to `gallery.read` and `upload.submit` completes to `cataloged` with the review wording "awaits administrator review" and "not public", with both duplicate buttons hidden and no duplicate-resolution post. `uploadStatusMessage` hides duplicate wording from identities without `upload.manage`.

`silent_keep_separate` remains in unchanged `src/kronika/domain/uploads.py`, the upload schema, ADR-0053, and SECURITY.md. No changed path is an API route, authorization policy, payload schema, migration, storage layout, or companion protocol type. `open_upload` is still the companion type. The bridge test shows a progress-shaped message does not open upload, and an `open_upload` payload is delivered as an empty argument list. The sidebar posts `OPEN_UPLOAD` only.

Header visibility and the start gate both use `upload.submit`. Recovery still uses `kronika.upload.recovery.v1`, with the retired `framenest.upload.recovery.v1` read only through `readMigratedStorageItem`.

### D Concurrency and recovery — PASS

`uploadUnresolvedWorkOwnsDialog` is true while an action owner, preparing, running, or completing flag is set, and for any snapshot that is neither byte-receiving nor terminal. `updateUploadActions` disables `#upload-file-input` in that case. `handleUploadFileSelection` returns before replacement on the same condition. During an in-flight start the test keeps `first.gif`, ignores a second picker file and a third dropped file, and creates one session whose filename is `first.gif`.

A disabled drop still calls `preventDefault` before returning, and dragover calls `preventDefault` for a file drag. The active-start test observes a consumed dragover and an unchanged file. A blocked drop therefore does not navigate or replace state.

A recovering `receiving` session rejects replacement selection: zero create posts and zero PATCH, and the upload id stays `UPLOAD_A`. After a compatible reselection the label is `Ready to resume`, with zero PATCH and zero create, until explicit `handleResumeUpload`. That resume then sends one PATCH. Automatic start is not on the byte-receiving branch.

Full-offset `receiving` (`received === declared`) offers an enabled Resume. Resume refreshes status first. Because `uploadIsByteReceiving` requires `received < declared`, `runUploadLoop` calls `completeUploadIfReady` and does not PATCH. The test observes zero PATCH and one complete post, then snapshot state `received` and `100%`. When the refreshed snapshot still needs bytes and `uploadState.file` is null, Resume sets reselection and sends neither PATCH nor complete.

One action owner, stale-response fencing, bounded poll backoff, and not-found cleanup remain covered by the unchanged tests that passed in this run, including synchronous start/resume fencing, one completion owner, bounded poll retry, and poll 404 clearing stale recovery without a cancel. `closeUploadDialog` stops eligible polling and closes; it does not create or cancel. `openUploadDialog` refreshes an existing id or restores recovery and does not POST. `pagehide` still calls `cleanupUploadRuntime`, which invalidates ownership and saves recovery. The correction touches `openUploadDialog` only by deleting the auto-start reset.

### E Presentation and documentation — PASS

Both CSS diffs are confined to `#upload-dialog` rules. Shared `.upload-dialog` width, max-height, padding, overflow, header, body, and footer rules are unchanged. SPEC.md §18 now states that one permitted selection or drop starts one upload, that the dialog must not offer an auto-start checkbox or a Start control, that the header Upload control and companion `open_upload` open the dialog, that the client claims the start synchronously before capability or session creation, that a failed gate creates no session, sends no bytes, and schedules no retry, and that another selection is the retry. The same section keeps explicit Resume, full-offset complete without another PATCH, reselection when refreshed truth needs bytes, truthful progress, explicit administrator keep/discard, and `silent_keep_separate`. DEVELOPMENT.md points at SPEC §18, carries the focused Python and Node commands, the synthetic-fixture checklist for unconditional start, and the public-main/NUC prerequisite for rendered acceptance. `docs/X_COMPANION.md` still says Upload posts `open_upload` only after the sidebar handshake and that progress and terminal results stay in the hosted dialog. SECURITY.md, `docs/UX_AUDIT.md`, and accepted ADR bodies are outside the diff. No new ADR was added. SPEC §18 is the normative owner of the corrected behavior.

### F Tests and preserved behavior — PASS

The cockpit tests cover the removed controls, one picker start, one drop start, synchronous ownership before create, the existing create payload, capability/configured/empty/oversize/offline fail-closed behavior with no delayed POST, replacement exclusion, consumed dragover, idempotent reopen, administrator duplicate review without an automatic disposition, ordinary cataloged wording without duplicate evidence, full-offset Resume without PATCH, recovered reselection that waits for explicit Resume, and hosted `open_upload` that does not start a transfer and keeps progress in the dialog. Removed assertions are the opt-in checkbox, default-off, and manual-Start expectations superseded by the rendered finding. Existing fencing, duplicate, recovery-key, pause/resume, polling, and shell assertions remain, and this run did not fail them.

The served-shell contract still requires `upload.submit` visibility, the recovery-key pair, server-offset PATCH framing, pause/resume/reselection wording, and truthful publish/catalog labels. `tests/companion_web_bridge.test.js` still requires pinned-origin `open_upload` and rejects a progress type. Extension production sources are not in the diff. The selected Node command also ran the X companion, YouTube cockpit, X cockpit, shell UI, gallery search/tag, automatic-analysis, and cover frontend tests. All passed.

### G Validation and allowlist — PASS

Commands and counts are in the next section. Whole paths: 9. Correction paths: 7. Companion and `X_COMPANION.md` correction diff: empty. Evidence-only Python files named in the grant are absent from the diff. `git diff --check` is clean. `git status --short` is empty after the runs. HEAD is still `0a96fc18b49191a32e7f482c4e881ad714db094a`. No full Python suite was run. No browser or rendered-geometry result is claimed.

## Tests and validation

```text
# [MacBook / fish]
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 076c01658f36f38cb9c8b5a3b4b098d774767616
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 076c01658f36f38cb9c8b5a3b4b098d774767616 --operation test-focus -- tests/contract/test_local_web_application.py tests/contract/test_upload_api.py tests/contract/test_ordinary_upload_ownership_boundary.py tests/contract/test_upload_session_architecture.py tests/contract/test_atomic_upload_publication_contract.py tests/integration/test_local_web_upload_cockpit.py tests/integration/test_atomic_upload_publication.py -q -p no:cacheprovider
node --test tests/upload_cockpit_async_ownership.test.js tests/companion_web_bridge.test.js tests/x_companion_extension.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js tests/kronika_ui.test.js tests/gallery_search_tag_filters.test.js tests/automatic_analysis_lifecycle.test.js tests/cover_frontend.test.js
git diff --check
git status --short
#------------------------------------------------------
```

```text
ap doctor: PASS
ap project check --baseline 076c01658f36f38cb9c8b5a3b4b098d774767616: PASS
Python test-focus: 277 passed, 62.50s, exit 0
Node --test: tests 285, pass 285, fail 0, cancelled 0, skipped 0, todo 0, exit 0
git diff --check: clean
git status --short: empty
```

Python evidence used only `./.ap/ap exec --operation test-focus`. JavaScript evidence used `node --test`.

## Source and security findings

none

## UI and frozen-view findings

none in source or the selected tests. Rendered geometry, the native picker, Brave iframe/modal behavior, scrolling, clipping, focus, contrast, upload timing, and assistive-technology output were not exercised. Adjacent shell, Timeline, Gallery, Details, and acquisition coverage is the selected Node and served-shell contract set above, which passed. No frozen Gallery or Details visual claim is made.

## Documentation findings

none. SPEC.md §18 and DEVELOPMENT.md match the unconditional candidate. `docs/X_COMPANION.md` remains consistent with `open_upload` and was not changed by `076c016..0a96fc1`.

## Allowlist review

```text
8646146..0a96fc1 (9):
  DEVELOPMENT.md
  SPEC.md
  docs/X_COMPANION.md
  src/kronika/adapters/api/web/app.js
  src/kronika/adapters/api/web/index.html
  src/kronika/adapters/api/web/styles.css
  tests/companion_web_bridge.test.js
  tests/contract/test_local_web_application.py
  tests/upload_cockpit_async_ownership.test.js

076c016..0a96fc1 (7):
  DEVELOPMENT.md
  SPEC.md
  src/kronika/adapters/api/web/app.js
  src/kronika/adapters/api/web/index.html
  src/kronika/adapters/api/web/styles.css
  tests/contract/test_local_web_application.py
  tests/upload_cockpit_async_ownership.test.js
```

No other repository path changed. No new files. `.ap/**`, the AP gitlink, `AGENTS.md`, `ap.project.conf`, `SECURITY.md`, `docs/UX_AUDIT.md`, and accepted ADR bodies are unchanged. The evidence-only upload tests named in the grant are unchanged.

## Deviations and near-misses

none

## Residual risks and missing evidence

Rendered Cooperator acceptance is still required after this candidate is on public `main` and refreshed onto the NUC. This audit does not establish native picker behavior, real drop navigation, scrolling, clipping, focus, contrast, timing, or assistive-technology output.

Unverified possibility, not a source failure: after a failed gate the file input keeps its value and there is no Start control. A later different selection starts again. Whether a native picker emits `change` for the same file was not tested.

Public `main` is still `076c01658f36f38cb9c8b5a3b4b098d774767616`. The candidate is local and unpushed. No publication, deployment, or closure is claimed.

## Smallest next step

Orchestrator decides publication of `0a96fc18b49191a32e7f482c4e881ad714db094a` and the subsequent NUC refresh so the Cooperator can render the unconditional upload flow.

Changed files: none in the Kronika repository. This report is the only write, at `/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/06_report_00.md`.
Git result: read-only inspection only. No add, commit, push, fetch, or other Git write.
Out-of-scope observations: ledger-candidates, unchanged by this audit.

Orchestration critique:
MEASURED: none
LEAD: a failed gate leaves the file input value in place and removes Start, so a native same-file reselection may not emit change; cheapest useful check is the Cooperator's rendered retry after a capability or size failure, once this candidate is on the NUC.

Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
Authority expiry: this terminal acceptance report ends the grant. No correction, publication, deployment, production, or closure authority remains.
