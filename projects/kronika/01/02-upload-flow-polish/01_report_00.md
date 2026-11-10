### Report for ORCHESTRATOR_CHAT

Logical whole identity: upload-flow-polish  
Worker session ordinal: 01  
Worker exchange ordinal: 01  
Persistent role identity: WORKER  
Worker session target: fresh-worker-session  
Native planning mode: required  
Worker session profile: Planner  
Phase: Planning  
Task identity: KRN-UPLOAD-PLAN-01 — plan-only — upload-flow polish  
Status: PARTIAL  
Phase-qualified result: planning-PASS  
Start commit: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e  
End commit: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e  
Report justification: new-evidence  
Planning cycle: initial  
Plan disposition: approval-gated  
Implementation in same Worker session: prohibited  
Post-plan implementation session: fresh-worker-session  
Logical-whole closure: not-closed  

# Upload-flow polish — opt-in start in the existing dialog

## 1. Summary and verified baseline

The implementation plan is complete. `PARTIAL` records only the unavailable report-file delivery: active client Plan Mode prohibits writing the report. It does not indicate an incomplete design or implementation authorization.

**Report persistence: client-prohibited; complete exact content returned for authorized persistence**

The intended destination remains `/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/01_report_00.md`. It was absent at initial inspection and final recheck. No file was written; saved-file readback is not claimed.

| Gate | Directly observed result |
|---|---|
| Physical checkout | `/Users/agile/Projects/kronika`; standalone checkout, branch `main` |
| Local HEAD | `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e` |
| Public `main` | Same SHA, verified by `git ls-remote origin refs/heads/main`, including a final readback |
| Worktree | Clean; `.ap` worktree also clean |
| Recorded `.ap` gitlink and submodule HEAD | Both `d7023cf037f6d17885c3ede5c04812c61640da50` |
| `./.ap/ap doctor` | PASS; governing variant `stable` |
| Exact baseline-bound project check | PASS at `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e` |

The project check reported sanitization of inherited environment classes; it passed without environment repair.

The handout’s older baseline, pending predecessor closures and separate History statements are explicitly superseded by the whole’s revalidation notes, closed predecessor records and ADR-0088. No remaining material contradiction was found.

NUC active/web `8646146`, schema `0035`, service active, backup restore-readiness ready and revoked sudo are **carried operational evidence from the supplied notes**. This Planner did not contact the NUC.

No repository, Git, host, browser, extension, provider or private-media mutation occurred. Product test suites were inspected, not executed.

## 2. Re-measured current-state map

### Upload dialog and controller

The dialog is in [index.html](/Users/agile/Projects/kronika/src/kronika/adapters/api/web/index.html:239). Its controller is the upload block in [app.js](/Users/agile/Projects/kronika/src/kronika/adapters/api/web/app.js:2692).

| Surface or state | Current owner and behavior |
|---|---|
| Selection | `#upload-file-input`, `#upload-file-trigger`, `handleUploadFileSelection`; one file. Picker hints GIF, MP4, JPEG and PNG. `setupUploadDropZone` routes the first dropped file through the same change event. |
| Client checks | Server capability discovery and maximum-size check. Picker format filtering is advisory; server validation remains authoritative. |
| Start | `handleStartUpload` synchronously claims an action owner, refreshes capability, creates the session, then calls `runUploadLoop`. |
| Ownership | `generation`, `actionOwner`, `uploadLoopOwner`, `completionOwner` and upload/file context checks fence stale responses and repeated actions. |
| Transfer | `runUploadLoop` refreshes the server-confirmed offset and sends bounded PATCH chunks. The default client chunk ceiling is 1 MiB, also bounded by the server limit. |
| Progress | `renderUploadCockpit` renders the filename, state, confirmed bytes, integer percentage, live status and sanitized failure. |
| Pause/resume | Pause waits for the current request to settle. Resume refreshes server truth before continuing. Reselection currently waits for explicit Resume. |
| Cancel | Reusable confirmation, eligibility recheck and one owned DELETE. Cancellation is offered only for `created`, `receiving` and `received`. |
| Validation | Complete submits received bytes for server validation. Received/validating states poll server truth. |
| Duplicate review | Administrator-only keep/discard controls at `duplicate_pending`; discard requires confirmation. |
| Finalization | `publish_pending` → `published` → `cataloged`; these are distinct stages. Rejected, failed, cancelled and expired states remain distinct failures or terminal outcomes. |
| Recovery | Existing local-storage record contains only upload ID, bounded filename/size/time hints and last state. No bytes or file handles are persisted. |
| Dialog lifecycle | Closing hides the dialog and stops status polling; it does not cancel the upload. Reopening refreshes the same session. `pagehide` retires runtime ownership. |

Polling uses a 1,200 ms interval with transient-error backoff capped at 10,000 ms. Publication-pending polling stops after 25 attempts; `published` continues polling until cataloging.

Two source-observed gaps matter to this change:

- Selection currently can invalidate an in-flight create action or pending recovery because its initial branch treats an absent snapshot as a fresh selection. Auto-start therefore needs both control disabling and handler-level exclusion.
- Resume visibility requires bytes still missing, although the resume controller contains a complete-only path for `receiving` at the full offset. That path needs a reachable control and regression coverage.

The second point is a measured predicate mismatch, not a claimed baseline test failure.

### Duplicate review, API and persistence

The security owner remains ADR-0053, with administrator disposition inherited from ADR-0041.

- All seven upload routes use `upload.submit` in `tailscale_ingress.py`.
- Session access additionally requires the verified owner or administrator `upload.manage` override; foreign ordinary callers receive sanitized `404 UPLOAD_SESSION_NOT_FOUND`.
- Creation stamps ownership and chooses the persisted duplicate mode. The client does not choose it.
- Proven administrator creation uses `explicit`. A qualifying server-derived size/SHA-256 match enters `duplicate_pending`; keep sends `{"resolution":"keep_separate"}`, discard sends `{"resolution":"discard"}`.
- Ordinary creation uses `silent_keep_separate`. Validation atomically records a separate copy and advances to `publish_pending`, without exposing duplicate-pending state or matching evidence.
- Explicit resolution of a privacy-safe session fails without revealing the match.
- Storage publication, cataloging and household content publication remain separate. Ordinary completion still states that the submission awaits administrator review and is not public.

Relevant implementation owners are `upload_api.py`, `upload_transport.py` and `upload_session_repository.py`. **None requires modification.**

### Companion and predecessor interaction

The companion’s `#frame` already hosts the complete Kronika shell. Its 📤 control posts `open_upload`; the upload progress and terminal result are rendered inside that same iframe.

The existing guards are:

- Canonical protocol `kronika.companion.web.v1`.
- Host accepts messages only while framed, from its parent window and the pinned extension origin.
- Sidebar sends `open_upload` only after its handshake and with a valid stored Kronika origin.
- Application callback opens the dialog only when the upload control is visible; that visibility follows `upload.submit`.
- Upload HTTP mutations originate from the hosted web shell and retain their existing web-origin and mutation-header checks.

There is no upload-progress message or separate extension upload controller. Neither is needed for the chosen behavior.

Whole 01 added preview/list ownership and pagehide retirement, then corrected ordinary visibility changes so they do not retire previews. Whole 10 changed shared shell navigation, header searches, filters, listboxes, glyphs and test harnesses. Their upload API, companion host and sidebar sources were unchanged in the inspected predecessor diffs.

The implementation must retain ADR-0088’s Timeline-only overview, header search behavior, request/record current marking and the Gallery/Details freeze.

## 3. Recommended behavior and event flow

Two product choices were explicitly confirmed by the Cooperator during this exchange:

1. Auto-start is **off by default**, retained only during one opening of the dialog, and reset when the dialog is reopened.
2. Companion progress and results remain **inside the existing upload dialog**. No persistent panel indicator is required.

### Auto-start choice

Add one checkbox immediately before the file selector:

**“Start automatically after choosing a file”**

Helper text: **“For this open dialog only. Recovered uploads still need Resume.”**

- Keep the choice outside the resettable upload-session state. Selecting another file after a terminal result preserves the choice until the dialog closes.
- Reset it only on a genuine closed-to-open transition. Repeated `open_upload` messages while the dialog is already open must neither reset the choice nor create work.
- Toggling the checkbox alone never starts an already selected file.
- Do not persist the choice in local storage, session storage, server settings or the recovery record.
- Preserve manual Start whenever an eligible selected file has not started.

### Ordered event flow

1. **Open:** show the existing dialog, reset auto-start to off, discover capability and restore or refresh the existing session.
2. **Select or drop:** accept one new file only when no unresolved session or action owns the dialog.
3. **Auto-start off:** show Ready and wait for Start.
4. **Auto-start on:** invoke the existing start handler once for that selection. Claim ownership synchronously before awaiting capability or session creation.
5. **Pre-create checks:** require current `upload.submit`, configured capability, a positive file size and compliance with the current server size limit. Failure creates no session and sends no bytes.
6. **Transfer:** retain the existing POST payload, offset-confirmed PATCH loop and complete request.
7. **Validation:** show confirmed transfer progress independently of server validation. A displayed 100% means bytes transferred, not publication or successful completion.
8. **Administrator duplicate:** stop at the existing review with exactly the two existing duplicate actions. Auto-start never chooses a disposition.
9. **Ordinary duplicate:** follow the existing privacy-safe server outcome with no duplicate indication.
10. **Finalization:** retain publication-pending, published and cataloged feedback, including ordinary review wording. Keep the terminal result visible until another permitted selection or dialog closure.

### Concurrency, recovery and failures

- Disable file replacement and the checkbox while preparing, transferring, completing, cancelling, restoring an unresolved session, validating or awaiting duplicate/finalization outcomes.
- Apply the same exclusion in selection handlers so synthetic events cannot bypass disabled controls. Consume blocked file drops without replacing state or allowing navigation.
- Allow compatible reselection for a settled incomplete session, but always require explicit Resume. Auto-start never resumes recovered or paused work.
- At a server-confirmed full `receiving` offset, offer Resume to finish through the existing complete endpoint. Refresh status first; send no PATCH when all bytes are present. If refreshed truth requires bytes and no file is available, require reselection.
- Preserve cancellation and duplicate-discard confirmations, stale-response fencing and one action owner.
- Capability failure, network failure or rejected creation never triggers an automatic retry. Manual Start or Resume remains the retry route where applicable.
- After uncertain completion or duplicate resolution, refresh server truth before presenting the next permitted action.
- Preserve transient polling backoff, generic not-found recovery cleanup and unknown-state fail-closed behavior.
- Closing and reopening never creates a new upload. Closing retains the existing transfer behavior; reopening refreshes the existing session and resumes eligible status polling.
- Preserve the existing recovery-key format, legacy-key fallback and cleanup policy. This whole does not add durable upload history or guarantee transfer survival after the browser or side panel is destroyed.

A lost create response can leave an unused server session until its existing expiry. Without an API idempotency change, this UI can guarantee one active transfer in its own runtime, not exactly-once session creation across an unknown response or independent tabs. Do not retry creation automatically or claim cross-tab coordination.

### Presentation

Retain the existing row, progress bar, status and action labels. Keep error and progress information in the existing live-status surface.

Scope new layout rules to `#upload-dialog`: use a vertical flex layout while open, retain a scrollable body and reachable footer, and let the checkbox text wrap at narrow widths. Do not alter shared `.upload-dialog` geometry for YouTube, X or confirmation dialogs.

No API, payload, capability, schema, storage or companion protocol change is needed.

## 4. Scope and exact proposed changed-path allowlist

This is a proposal for the later grant, not mutation authority.

| Group | Exact paths |
|---|---|
| Upload UI | `src/kronika/adapters/api/web/index.html` |
| Upload UI | `src/kronika/adapters/api/web/app.js` |
| Upload UI | `src/kronika/adapters/api/web/styles.css` |
| Behavioral tests | `tests/upload_cockpit_async_ownership.test.js` |
| Companion guard tests | `tests/companion_web_bridge.test.js` |
| Served-shell contracts | `tests/contract/test_local_web_application.py` |
| Normative behavior | `SPEC.md` |
| Development validation guide | `DEVELOPMENT.md` |
| Companion usage guide | `docs/X_COMPANION.md` |

**Nine paths; no new files.**

The implementation excludes backend, route policy, persistence, migrations, dependencies, extension production sources, manifest permissions, acquisition pipelines, providers, capture, public composition, deployment helpers and `.ap`.

It also excludes batching, a queue, background-transfer infrastructure, cross-tab coordination, new notifications, a second upload manager, Gallery/Details redesign, localization, broad accessibility work and `app.js` modularization.

## 5. Test strategy and acceptance matrix

**No product test execution is claimed by this Planner.** The following is the selected future validation.

### Existing pins and required updates

| Test owner | What it pins; planned treatment |
|---|---|
| `upload_cockpit_async_ownership.test.js` | Exact lifecycle action sets, duplicate copy/actions, confirmations, request ownership, polling, recovery, explicit Resume and ordinary privacy. Extend the harness and scenarios; preserve stale-response and explicit-recovery assertions. |
| `test_local_web_application.py` | Exact picker markup, supported-format copy, live status, button markup, danger CSS, capability discovery, offsets, recovery keys and truthful lifecycle copy. Add checkbox/scoped-layout contracts without weakening existing assertions. |
| `companion_web_bridge.test.js` | Canonical protocol, pinned origin, parent source, upload opener and handshake checks. Extend OPEN_UPLOAD negative coverage; keep the protocol unchanged. |
| `x_companion_extension.test.js` | Sidebar iframe, Upload title-bar control and Settings/Disconnect arrangement. Run unchanged. |
| `youtube_acquisition_cockpit.test.js`, `x_acquisition_cockpit.test.js` | Adjacent cockpits sharing dialog/confirmation styling and controller context. Run unchanged. |
| `kronika_ui.test.js`, `gallery_search_tag_filters.test.js` | Accepted shell, Timeline, navigation, previews and header-search behavior. Run unchanged. |
| `automatic_analysis_lifecycle.test.js`, `cover_frontend.test.js` | Cataloged-upload AI wording and adjacent modal/markup hooks. Run unchanged. |

The present explicit-Resume recovery assertion must continue passing even with auto-start selected. Existing stale-create tests that deliberately replace state remain valid; add real-event tests proving that ordinary user selection cannot perform that replacement while creation is owned.

Add named causal tests in the existing upload suite:

- **“Auto-start defaults off, survives file reset, and resets only on dialog reopen.”**
- **“Opted-in picker and drop selection start one upload with the existing payload.”**
- **“Auto-start fails closed for capability, empty-file and size failures without delayed retry.”**
- **“Active or recovering uploads reject replacement selection and repeated open requests.”**
- **“Auto-start preserves administrator duplicate review and ordinary duplicate privacy.”**
- **“Full-offset Resume completes without PATCH, while recovered byte transfer still requires explicit Resume.”**
- **“Hosted open_upload opens the same dialog without starting a transfer and renders its progress and result.”**

Use deferred responses to exercise capability, creation, PATCH, completion and cancellation races. Extend the upload harness with the actual companion host registration for the hosted behavior test; do not claim a callback-only mock proves application wiring.

### Exact future commands

Re-run the declared doctor and baseline gate. Python uses only this envelope:

`./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e --operation test-focus -- tests/contract/test_local_web_application.py tests/contract/test_upload_api.py tests/contract/test_ordinary_upload_ownership_boundary.py tests/contract/test_upload_session_architecture.py tests/contract/test_atomic_upload_publication_contract.py tests/integration/test_local_web_upload_cockpit.py tests/integration/test_atomic_upload_publication.py -q -p no:cacheprovider`

JavaScript:

`node --test tests/upload_cockpit_async_ownership.test.js tests/companion_web_bridge.test.js tests/x_companion_extension.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js tests/kronika_ui.test.js tests/gallery_search_tag_filters.test.js tests/automatic_analysis_lifecycle.test.js tests/cover_frontend.test.js`

The complete local-web contract file is selected because the shared monolithic shell/controller and CSS can affect unrelated served-shell assumptions. A full repository suite is not required.

Other discovered upload tests own domain transitions, transport rollback/locking, validation coordinators, filesystem quarantine/publication, persistence and migrations. Their production owners are unchanged; no new backend tests or migration tests are needed for this UI-only slice.

### Acceptance matrix

| Claim | Automated evidence | Cooperator rendered check |
|---|---|---|
| Default/manual flow | Checkbox lifecycle; no POST on selection when off | Choose file, inspect Ready, then Start |
| Opted-in start | One POST and one loop for picker/drop; unchanged payload | Enable choice and select/drop a file |
| Validation gates | Empty/oversize/capability failures; server API contracts | Clear failure presentation; no false success |
| Concurrency | Deferred creation, replacement, repeated activation and recovery tests | Picker/control locking remains understandable |
| Pause/resume | Server-offset refresh and full-offset completion tests | Pause settles; Resume works without restarting |
| Cancel | Existing confirmation and stale-PATCH tests | Dismiss preserves upload; confirm cancels once |
| Duplicate behavior | Administrator explicit review; ordinary indistinguishability | Administrator keep/discard and ordinary non-disclosure |
| Final result | Distinct validation/publication/cataloging states | 100% is not mistaken for completion; review wording remains clear |
| Companion | Actual host/app wiring plus origin/source/protocol negatives | 📤 opens the same usable dialog in Brave |
| Shell preservation | Existing shell/search/cockpit suites | Header, Timeline, Gallery and Details remain accepted |

Rendered review should cover desktop, approximately 390–400 px and a short-height panel, including a long synthetic filename, both duplicate actions and the footer.

Node and contract tests do **not** prove native picker behavior, real Brave iframe/modal rendering, scrolling, clipping, focus behavior, contrast or actual upload timing. Those claims remain with the Cooperator after deployment. Use `PASS`, `FAIL` or `NOT TESTED` per row; do not infer untested rendered claims.

## 6. Documentation and ADR plan

- **`SPEC.md` §18** is the sole normative owner of the new auto-start lifecycle, transient choice, explicit recovery/resume and truthful progress semantics. Retain §19’s existing companion boundary.
- **`DEVELOPMENT.md`** supplies the focused commands, synthetic-fixture checklist and public-main/NUC acceptance prerequisite, linking to SPEC for behavior.
- **`docs/X_COMPANION.md`** explains that 📤 opens the hosted dialog and that progress/results stay there, linking to SPEC.
- **`SECURITY.md` remains unchanged:** its upload boundary is preserved.
- **`docs/UX_AUDIT.md` remains frozen historical evidence.** Its old recommendation is not a second live behavior owner.
- **No new ADR is needed.** This is bounded interaction behavior within ADR-0053 and ADR-0086; ADR-0088 remains intact.

Do not update unrelated stale historical prose or reopen predecessor wholes.

## 7. Security and authorization assessment

**No boundary widens.**

- Auto-start is a local user opt-in that invokes the same capability-gated handler and same endpoints.
- Ownership, duplicate mode, checksums, validation and disposition remain server-owned.
- No duplicate decision is made before transfer or automatically for an explicit administrator session.
- Ordinary users receive neither matching evidence nor duplicate controls.
- Quarantine precedes validation. Clients gain no placement, publication or source-media write authority.
- Cataloging does not authorize household or internet publication.
- Existing administrator AI behavior is unchanged; ordinary uploads do not gain automatic-analysis authority.
- No file bytes, filenames, recovery data or progress payloads are added to companion messages.
- Pinned origin, parent source, canonical protocol, sidebar handshake and shell capability visibility remain intact.
- Upload routes do not become extension-origin `companion_mutation` routes; permissions and CORS stay unchanged.

Tests use synthetic identities, temporary catalogs and harmless fixture bytes. Later rendered upload checks require bounded fixture authority and a provider-free configuration. If existing automatic analysis could cause a live call, that precondition must be resolved through a separate grant before administrator upload testing.

## 8. Risks, rollback and deployment

### Risks and rollback

- **Async ownership:** auto-start exposes selection/create races more readily. Synchronous ownership and event-level negative tests are mandatory.
- **Test harness limits:** VM tests need faithful checkbox, disabled-input and host-callback behavior; they cannot establish rendered geometry.
- **Shared CSS:** scope changes to `#upload-dialog` and run adjacent cockpit tests.
- **Companion protocol:** no new protocol risk is introduced; test the existing opener without expanding it.
- **Recovery limits:** preserve the existing published-state recovery cleanup. Do not promise durable terminal history after reload.

Rollback is a bounded UI/docs revert under a later Git grant, followed by normal validation and publication. Operational rollback uses the canonical helper to the previously recorded complete release under explicit authority. It does not delete uploaded objects, restore the database or undo user actions.

### Exact future release and rendered-acceptance sequence

This sequence is a plan, not current operational authority.

1. A fresh Implementation Worker receives a complete grant, re-gates the baseline, implements the nine-path slice, runs the selected checks and returns the candidate.
2. Perform one fresh independent E2 acceptance against the fixed candidate, focusing on auto-start ownership, duplicate privacy, unchanged interfaces and adjacent shell behavior.
3. Under explicit publication authority, publish the accepted candidate normally to `main`; verify its exact 40-hex SHA **T** by direct public-ref readback.
4. Obtain a bounded NUC release grant naming **T**. Recheck capability through `scripts/operator/network/kronika_nuc_worker_gate.fish --probe`. The Cooperator establishes fresh sudo outside the Worker using `sudo -v`, then `sudo -n true`; the Worker never handles a password.
5. Use the canonical release helper and existing transport configuration: `deploy/ubuntu/kronika-release status`, then `deploy/ubuntu/kronika-release check --release T`. Record the previous release and require healthy service, ready backup evidence and the expected schema.
6. Only under explicit deployment authority, run `deploy/ubuntu/kronika-release deploy --release T --yes`. A successful check supplies no deployment authority.
7. This slice expects schema `0035`. Stop on `migration-required` or any other unexpected result; any required schema continuation belongs to the documented runbook under separately sufficient authority.
8. Run canonical `status` again. Require active/web **T**, service active, database revision `0035`, backup restore-readiness ready and unchanged capture release. Use release provenance markers, not `.git` inside deployed trees.
9. Release remote sudo with `sudo -K` through the supported gate at terminal handling, including failure handling when reachable. Report an unavailable release check honestly.
10. Reload the served shell/reopen the companion panel so it loads **T**, then ask the Cooperator to execute the rendered matrix. No extension reinstall, key rotation or source-media access is required.

Routine deployment retains the exact Poetry 2.4.1 and CPython 3.13.14 tooling paths from the runbook. No `uv`, bootstrap, package-manager or host-configuration work is part of this whole.

## 9. Open Cooperator decisions and chosen defaults

**No product decisions remain open.**

Confirmed choices are per-dialog, default-off auto-start and progress/results inside the existing companion-hosted dialog.

The complete plan and nine-path allowlist remain approval-gated. Implementation, publication, deployment and rendered acceptance remain separate results requiring their respective authority.

## 10. Smallest next step and closeout

The smallest next step is authorized persistence of this exact report at the absent destination, followed by complete readback. The Orchestrator can then reconcile and accept or reject the plan and issue one complete fresh Implementation Worker grant with `Native planning mode: not-used`.

Recommended implementation reasoning: **High**, specifically for asynchronous upload ownership and recovery. Recommended acceptance route: one separate fresh independent E2 acceptance, then publication, routine NUC refresh and Cooperator rendered acceptance.

### Resolved Execution Issues / Near-Misses

Two exploratory path guesses did not match the repository layout; file discovery identified the actual sidebar and ingress-policy owners. Broad reads also exceeded output limits; bounded follow-up reads established the material source facts. No failed repository gate, environment repair or mutation resulted.

### Pre-Existing Failure Classification

None. Product tests were not run, and no pre-existing test failure is asserted. The full-offset Resume issue is a source-observed control gap assigned prospective regression coverage.

Planning authority expires with submission of this terminal report. No implementation, acceptance, publication, deployment or closure authority remains.

Orchestration critique:  
MEASURED: The P4 route is necessary in this client: the report destination is absent, but active Plan Mode prohibits its write. Effect: complete planning content exists while file delivery remains unverified. Smallest correction: an authorized persister stores this exact report and reads it back without reopening planning.  
LEAD: none
