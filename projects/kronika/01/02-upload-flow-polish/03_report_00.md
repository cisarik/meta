### Report for ORCHESTRATOR_CHAT

Logical whole identity: upload-flow-polish
Worker session ordinal: 03
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: Implementation
Task identity: KRN-UPLOAD-IMPL-03 — implement the accepted upload-flow polish plan
Status: PASS
Phase-qualified result: implementation-PASS
Start commit: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
End commit: 076c01658f36f38cb9c8b5a3b4b098d774767616
Report justification: new-mutation
Logical-whole closure: not-closed

# Upload-flow polish — implementation

The accepted plan is implemented on `main` as one commit. Parent is `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e`. The commit is `076c01658f36f38cb9c8b5a3b4b098d774767616` with message `feat: add opt-in upload auto-start`. It is not pushed. This result is not acceptance, publication, deployment, or closure.

## Implemented behavior

The upload dialog has one checkbox, “Start automatically after choosing a file,” immediately before the file selector. Helper text says the choice is for the open dialog only and that recovered uploads still need Resume. The choice defaults off, lives outside the resettable upload-session object, and is not written to local storage, session storage, server settings, or the recovery record. It resets only on a closed-to-open transition. A repeated `open_upload` while the dialog is already open neither resets the choice nor creates work. Toggling the checkbox does not start an already selected file.

With the choice on, one permitted picker selection or drop calls the existing start path once. That path claims its action owner before awaiting capability or session creation. It requires current `upload.submit`, configured capability, a positive file size, and the current server size limit. A failed gate creates no session and sends no bytes, and nothing schedules a retry. The POST body remains `display_filename` and `declared_size_bytes`, followed by the existing offset-confirmed PATCH loop and complete request.

File replacement and the checkbox are disabled while preparing, transferring, completing, cancelling, restoring an unresolved session, validating, or awaiting duplicate or finalization outcomes. The selection handler applies the same exclusion, so a synthetic change cannot replace owned state. A blocked drop is consumed with `preventDefault` and does not replace the file or allow navigation. A settled incomplete session can still take a compatible reselected file, and auto-start never resumes it. At a server-confirmed full `receiving` offset, Resume is offered, status is refreshed first, and completion uses the existing complete endpoint with no PATCH. If the refresh still needs bytes and no file is available, the dialog requires reselection.

Administrator duplicate review still shows only keep and discard. Ordinary completion still uses the review wording and does not show duplicate evidence. Transfer percentage follows the server-confirmed offset. Terminal feedback stays in the existing dialog until another permitted selection or closure. Closing does not create or cancel an upload. Reopening refreshes the existing session.

New layout rules are scoped to `#upload-dialog`: vertical flex while open, the existing scrollable body and footer, and wrapping checkbox text. Shared `.upload-dialog` geometry is unchanged.

A failed capability load now keeps the loader’s own message. A disabled capability still says uploads are not configured. A network failure says the capability could not be loaded, rather than being rewritten as not configured.

## Changed paths

```text
DEVELOPMENT.md                               |  25 ++
SPEC.md                                      |  40 ++
docs/X_COMPANION.md                          |  11 +-
src/kronika/adapters/api/web/app.js          | 132 ++++++-
src/kronika/adapters/api/web/index.html      |   5 +
src/kronika/adapters/api/web/styles.css      |  51 +++
tests/companion_web_bridge.test.js           |  39 ++
tests/contract/test_local_web_application.py |  36 ++
tests/upload_cockpit_async_ownership.test.js | 538 ++++++++++++++++++++++++++-
9 files changed, 857 insertions(+), 20 deletions(-)
```

No other repository path changed. `SECURITY.md`, `docs/UX_AUDIT.md`, and the accepted ADR bodies were not edited.

## Documentation

`SPEC.md` §18 now owns the transient auto-start lifecycle, explicit recovery and Resume, and truthful progress. §19’s companion origin and handshake boundary is unchanged. `DEVELOPMENT.md` has the focused commands, the synthetic-fixture checklist, and the public-main/NUC rendered-acceptance prerequisite. `docs/X_COMPANION.md` states that 📤 posts `open_upload` and that progress and results stay in the hosted dialog, with a link to SPEC §18.

## Gate and tests

Observed before editing: HEAD `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e`, branch `main`, clean worktree, recorded `.ap` gitlink and submodule HEAD both `d7023cf037f6d17885c3ede5c04812c61640da50`.

```text
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
```

Both PASS. The project check sanitized inherited environment classes and did not require environment repair.

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e --operation test-focus -- tests/contract/test_local_web_application.py tests/contract/test_upload_api.py tests/contract/test_ordinary_upload_ownership_boundary.py tests/contract/test_upload_session_architecture.py tests/contract/test_atomic_upload_publication_contract.py tests/integration/test_local_web_upload_cockpit.py tests/integration/test_atomic_upload_publication.py -q -p no:cacheprovider
```

277 passed, 0 failed, 60.02s.

```text
node --test tests/upload_cockpit_async_ownership.test.js tests/companion_web_bridge.test.js tests/x_companion_extension.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js tests/kronika_ui.test.js tests/gallery_search_tag_filters.test.js tests/automatic_analysis_lifecycle.test.js tests/cover_frontend.test.js
```

285 passed, 0 failed.

`git diff --check` and `git diff --cached --check` were clean. Final `git status --short` is empty.

New or extended test identities:

- “Auto-start defaults off, survives file reset, and resets only on dialog reopen.”
- “Opted-in picker and drop selection start one upload with the existing payload.”
- “Auto-start fails closed for capability, empty-file and size failures without delayed retry.”
- “Active or recovering uploads reject replacement selection and repeated open requests.”
- “Auto-start preserves administrator duplicate review and ordinary duplicate privacy.”
- “Full-offset Resume completes without PATCH, while recovered byte transfer still requires explicit Resume.”
- “Hosted open_upload opens the same dialog without starting a transfer and renders its progress and result.”
- `open_upload carries no progress and a progress type does not open upload`
- `test_upload_dialog_auto_start_is_opt_in_and_scoped`

The hosted test loads `companion_host.js` into the upload harness and dispatches `open_upload` through that host. Existing upload, companion, shell, and acquisition assertions were not weakened. Evidence-only Python files were not edited.

## Deviation and residual risk

No allowlist or authority deviation. Rendered geometry, native picker behavior, real Brave iframe and modal behavior, scrolling, clipping, focus, contrast, and actual upload timing were not exercised. Node and contract tests do not prove them.

A lost create response can still leave an unused server session until its existing expiry. This client guarantees one active transfer in its own runtime, not exactly-once creation across an unknown response or another tab.

## Resolved Execution Issues / Near-Misses

The first JavaScript run failed for three local causes, all fixed before the commit. Repeated `const` declarations in `vm.runInContext` collided on the shared context, so the new harness snippets run inside functions. The full-offset test queued one status refresh while Resume refreshes again inside the transfer loop, so the test now queues both. A failed capability load was then overwritten with the not-configured sentence; the start path now keeps the loader’s message. The corrected JavaScript run and the Python run both passed.

## Pre-Existing Failure Classification

None. The selected Python and JavaScript commands passed after the corrections above. No evidence-only test failed, and no non-allowlisted test was edited.

## Smallest next step

One fresh independent E2 acceptance of `076c01658f36f38cb9c8b5a3b4b098d774767616`, focused on auto-start ownership, duplicate privacy, the unchanged upload interface, and adjacent shell behavior. Publication, NUC refresh, and Cooperator rendered acceptance remain separate grants.

Implementation authority expires with this report. No push, acceptance, publication, deployment, or closure authority remains.

Orchestration critique:
MEASURED: none
LEAD: none
