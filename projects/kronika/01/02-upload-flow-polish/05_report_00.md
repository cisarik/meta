### Report for ORCHESTRATOR_CHAT

Logical whole identity: upload-flow-polish
Worker session ordinal: 05
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded UI Polish Worker
Phase: Correction
Task identity: KRN-UPLOAD-CORR-05 — make upload start unconditional and remove the redundant controls
Status: PASS
Phase-qualified result: implementation-PASS
Start commit: 076c01658f36f38cb9c8b5a3b4b098d774767616
End commit: 0a96fc18b49191a32e7f482c4e881ad714db094a
Report justification: new-mutation
Logical-whole closure: not-closed

# Upload-flow polish — unconditional start

The Cooperator rendered deployed `076c016` and passed every upload behavior except the opt-in control. This correction removes that checkbox, its helper text, and the in-dialog Start upload button. One permitted new picker selection or drop now starts exactly one upload. The header Upload control, the companion `open_upload` control, and the dialog close button remain. Explicit Resume remains the only continuation for recovered or paused work. Automatic start does not resume that work.

Parent of the correction commit is `076c01658f36f38cb9c8b5a3b4b098d774767616`. The commit message is `fix: make upload start automatic without controls`. It is not pushed. This result is not acceptance, publication, deployment, or closure.

Native planning mode was off: this session had implementation tools and no Plan-mode write restriction. The report path was absent before the write.

## Behavior

`handleUploadFileSelection` still refuses replacement while unresolved work owns the dialog. When there is no snapshot, or the snapshot is a permitted terminal state, it calls `resetUploadForFile(file)` and then `handleStartUpload()` once. The `uploadAutoStart` branch is gone. `handleStartUpload` still claims its action owner synchronously before awaiting capability discovery or session creation. Capability, configured, positive-size, and size-limit gates are unchanged. A failed gate creates no session, sends no bytes, and schedules no retry; the user retries by choosing another file.

A compatible reselection of a byte-receiving session still stops at explicit Resume. A settled incomplete or recovering session still requires explicit Resume. The POST body, offset-confirmed PATCH loop, complete request, replacement lock, consumed blocked drops, duplicate review, ordinary privacy, pause, resume, cancel, polling, recovery, close, reopen, and terminal-state behavior are unchanged. `uploadDialogIsOpen()` still makes a repeated open or repeated `open_upload` idempotent.

## Removed controls

Removed from `index.html`: the entire `upload-auto-start` block, the checkbox, its label, its helper text, and `<button id="upload-start-button">`. Removed from `app.js`: `uploadAutoStart`, `uploadAutoStartInput`, `syncUploadAutoStartControl`, the closed-to-open checkbox reset, the checkbox change listener, checkbox disabling, `uploadStartButton`, its click listener, and the now-unused `startVisible`, `hasActiveSession`, and `fileWithinLimit` calculations. The unused `Start upload` button-icon entry was removed with the control. Removed from `styles.css`: the `.upload-auto-start*` rules, the checkbox disabled selector, and the narrow-layout checkbox wrap rules. The scoped `#upload-dialog[open]` flex layout, scrollable body, reachable footer, and disabled file-input label styling remain. Shared dialog geometry is unchanged.

## Changed paths

```text
DEVELOPMENT.md                               |   4 +-
SPEC.md                                      |  25 +++---
src/kronika/adapters/api/web/app.js          |  52 +----------
src/kronika/adapters/api/web/index.html      |   6 --
src/kronika/adapters/api/web/styles.css      |  43 +--------
tests/contract/test_local_web_application.py |  38 ++++----
tests/upload_cockpit_async_ownership.test.js | 129 ++++++++-------------------
7 files changed, 74 insertions(+), 223 deletions(-)
```

`tests/companion_web_bridge.test.js` and `docs/X_COMPANION.md` needed no change: neither names the removed choice or the Start control. `SECURITY.md`, `docs/UX_AUDIT.md`, and the accepted ADR bodies were not edited. No other repository path changed.

## Documentation

`SPEC.md` §18 now states that one upload starts automatically after a permitted new selection or drop, that the dialog has no checkbox and no Start control, that a failed gate creates no session and is retried by another selection, and that explicit Resume remains for recovered or paused work. The existing progress, duplicate, privacy, replacement-lock, and companion statements remain. The dialog still must not persist an auto-start choice, and opening an already open dialog must not reset state or create work. `DEVELOPMENT.md` now says selecting or dropping a file starts automatically, no Start control exists, and a failed gate allows another selection. The focused commands and the public-main/NUC prerequisite remain.

## Gate and tests

Observed before editing: HEAD `076c01658f36f38cb9c8b5a3b4b098d774767616`, branch `main`, clean worktree, recorded `.ap` gitlink and submodule HEAD both `d7023cf037f6d17885c3ede5c04812c61640da50`. The same gates were run again after the edit and before the commit.

```text
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 076c01658f36f38cb9c8b5a3b4b098d774767616
```

Both PASS. The project check sanitized inherited environment classes and did not require environment repair.

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 076c01658f36f38cb9c8b5a3b4b098d774767616 --operation test-focus -- tests/contract/test_local_web_application.py tests/contract/test_upload_api.py tests/contract/test_ordinary_upload_ownership_boundary.py tests/contract/test_upload_session_architecture.py tests/contract/test_atomic_upload_publication_contract.py tests/integration/test_local_web_upload_cockpit.py tests/integration/test_atomic_upload_publication.py -q -p no:cacheprovider
```

277 passed, 0 failed, 68.64s.

```text
node --test tests/upload_cockpit_async_ownership.test.js tests/companion_web_bridge.test.js tests/x_companion_extension.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js tests/kronika_ui.test.js tests/gallery_search_tag_filters.test.js tests/automatic_analysis_lifecycle.test.js tests/cover_frontend.test.js
```

285 passed, 0 failed.

`git diff --check` and `git diff --cached --check` were clean. Final `git status --short` is empty.

Updated test identities:

- “The upload dialog renders no auto-start choice and no Start control.”
- “A permitted picker or drop selection starts one upload with the existing payload.”
- “Selection fails closed for capability, empty-file and size failures without delayed retry.”
- “Active or recovering uploads reject replacement selection and repeated open requests.”
- “Automatic start preserves administrator duplicate review and ordinary duplicate privacy.”
- “Full-offset Resume completes without PATCH, while recovered byte transfer still requires explicit Resume.”
- “Hosted open_upload opens the same dialog without starting a transfer and renders its progress and result.”
- `test_upload_dialog_has_no_auto_start_choice_or_start_control`

The lifecycle action matrix no longer expects a Start action for a selected file. The served-shell cockpit contract no longer requires the Start button. Existing ownership, stale-response, polling, duplicate-copy, cancellation, recovery, and privacy assertions remain, except assertions that named the removed controls. `open_upload carries no progress and a progress type does not open upload` was left unchanged. Evidence-only and non-allowlisted tests were not edited.

## Correction record

```text
Acceptance candidate: 076c01658f36f38cb9c8b5a3b4b098d774767616
Acceptance owner map: prior E2 matrix in 04_report_00.md; this correction supersedes only the opt-in and manual-Start claims
Acceptance allowlist: index.html, app.js, styles.css, tests/upload_cockpit_async_ownership.test.js, tests/companion_web_bridge.test.js, tests/contract/test_local_web_application.py, SPEC.md, DEVELOPMENT.md, docs/X_COMPANION.md
Acceptance risk claims: unconditional start, removed controls, preserved gates, replacement lock, duplicate privacy, explicit Resume, companion open_upload
Acceptance control matrix: not re-executed by this corrector
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: none
```

`full-fresh` is required because the correction changes runtime behavior. This Worker does not accept its own correction.

## Deviation and residual risk

No allowlist or authority deviation. `docs/X_COMPANION.md` and `tests/companion_web_bridge.test.js` were inspected and left unchanged.

Rendered geometry, native picker behavior, real Brave iframe and modal behavior, scrolling, clipping, focus, contrast, upload timing, and assistive-technology output were not exercised. Node and contract tests do not prove them.

A lost create response can still leave an unused server session until its existing expiry. This client guarantees one active transfer in its own runtime, not exactly-once creation across an unknown response or another tab.

## Resolved Execution Issues / Near-Misses

none

## Pre-Existing Failure Classification

none

## Smallest next step

One fresh independent E2 re-acceptance of `0a96fc18b49191a32e7f482c4e881ad714db094a`, focused on unconditional start, the removed controls, duplicate privacy, explicit Resume, and the unchanged upload interface. Publication, NUC refresh, and Cooperator rendered re-acceptance remain separate grants.

Correction authority expires with this report. No push, acceptance, publication, deployment, or closure authority remains.

Orchestration critique:
MEASURED: none
LEAD: none
Authority expiry: this terminal report ends the grant; no autonomous continuation.
