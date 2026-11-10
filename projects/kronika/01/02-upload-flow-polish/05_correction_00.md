# Authoritative Worker prompt — Kronika whole 02, Worker session 05, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`upload-flow-polish`. It is stored under the Meta filename mapping
`<worker-session>_<phase>_<meta-exchange-index>.md` as `05_correction_00.md`.
The matching terminal report is `05_report_00.md`.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: upload-flow-polish
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded UI Polish Worker
Phase: Correction
Task identity: KRN-UPLOAD-CORR-05 — make upload start unconditional and remove the redundant controls
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — the change touches the asynchronous upload start path, replacement locks, recovery and the tested dialog contract
Recommended context capacity: approximately 250k tokens
Independence required: no
Continuity anchor: accepted plan 01_report_00.md and implementation report 03_report_00.md at baseline 076c01658f36f38cb9c8b5a3b4b098d774767616
Authority renewal: prior implementation authority expired; this prompt grants a new bounded correction
Evidence posture: non-independent correction; a fresh independent E2 re-acceptance follows
```

You are continuing the accepted upload-flow polish from a genuinely fresh
session. The plan and implementation are accepted except for the Cooperator's
rendered UX finding below. Read the accepted plan and implementation report in
full before editing:

```text
/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/01_report_00.md
/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/03_report_00.md
```

The plan is the design of record except where this prompt explicitly supersedes
it. If the plan, report and this prompt conflict, stop and report the
contradiction rather than improvising.

Before substantive work, confirm that `Native planning mode: not-used` is the
actual client state (native Plan mode OFF). If it is enabled, stop and return
`BLOCKED` naming the contradiction.

## 1. Cooperator finding and decision

The Cooperator rendered the deployed `076c016` upload flow. All behavior passed
except the opt-in control. His decision:

- the **“Start automatically after choosing a file” checkbox is unnecessary and
  bad UX**; remove it and its helper text;
- auto-start is the **default and only** behavior: one upload starts
  automatically after a permitted picker selection or drop;
- the in-dialog **“Start upload” button is unnecessary**; remove it;
- the header and companion Upload controls remain as the way to open the dialog;
- explicit Resume remains for recovered or paused uploads; automatic start never
  resumes that work.

This supersedes the opt-in/default-off and manual-Start parts of the accepted
plan and the `03_report_00.md` implementation. All other accepted upload
behavior remains: capability and size gates, duplicate review and ordinary
privacy, replacement locks, full-offset Resume, progress/terminal truthfulness,
companion `open_upload`, scoped presentation and no API, authorization, schema
or companion-protocol change.

## 2. Exact required change

### 2.1 Remove the redundant controls

- In `src/kronika/adapters/api/web/index.html`, remove the entire
  `upload-auto-start` block, the checkbox, its label and its helper text.
- Remove the in-dialog `<button id="upload-start-button" ...>Start upload</button>`.
- Keep the header Upload menu item, the companion `open_upload` control and the
  dialog's close button.
- In `src/kronika/adapters/api/web/app.js`, remove:
  - the `uploadAutoStart` module binding and every reference;
  - the `uploadAutoStartInput` element binding;
  - `syncUploadAutoStartControl`;
  - the checkbox reset in `openUploadDialog`;
  - the checkbox change listener;
  - checkbox disabling and focus-list references;
  - `uploadStartButton` binding, click listener, `startVisible`,
    `hasActiveSession` and `fileWithinLimit` if they become unused.
- Keep the `uploadDialogIsOpen()` guard so repeated `open_upload` or repeated
  open calls remain idempotent.
- In `src/kronika/adapters/api/web/styles.css`, remove the
  `.upload-auto-start*` rules and the checkbox-specific disabled selector. Keep
  the scoped `#upload-dialog[open]` flex layout, the scrollable body and the
  reachable footer if they remain useful and do not alter shared dialog
  geometry. Keep the disabled file-input label styling.

### 2.2 Start on every permitted selection

- In `handleUploadFileSelection`, when there is no snapshot or the snapshot is a
  permitted terminal state, call `resetUploadForFile(file)` and then
  **unconditionally** invoke `handleStartUpload()` once.
- Remove the `if (uploadAutoStart)` branch.
- Preserve the byte-receiving reselection branch: a compatible reselected file
  still stops at explicit Resume and must not start a second upload.
- Preserve the settled incomplete/session branch and its explicit Resume
  requirement; automatic start does not resume recovered or paused work.
- Keep the existing synchronous action-owner claim before awaiting capability
  or session creation.
- Keep the capability, configured, positive-size and size-limit gates. A failed
  gate creates no session, sends no bytes and schedules no retry. Because there
  is no Start button, the user retries by choosing another file.
- Keep the existing POST body, offset-confirmed PATCH loop and complete request.
- Keep the replacement lock, handler-level selection exclusion, consumed blocked
  drops, duplicate review, ordinary privacy, pause/resume/cancel, polling,
  recovery, close/reopen and terminal-state behavior unchanged.

### 2.3 Tests

Update the existing tests rather than weakening them:

- `tests/upload_cockpit_async_ownership.test.js`:
  - remove the checkbox/Start-control harness helpers and assertions;
  - replace or rewrite the old opt-in/default-off tests;
  - keep the seven causal behaviors as tests for unconditional start:
    - **“A permitted picker or drop selection starts one upload with the
      existing payload.”**
    - **“The upload dialog renders no auto-start choice and no Start control.”**
    - **“Selection fails closed for capability, empty-file and size failures
      without delayed retry.”**
    - **“Active or recovering uploads reject replacement selection and repeated
      open requests.”**
    - **“Automatic start preserves administrator duplicate review and ordinary
      duplicate privacy.”**
    - **“Full-offset Resume completes without PATCH, while recovered byte
      transfer still requires explicit Resume.”**
    - **“Hosted open_upload opens the same dialog without starting a transfer
      and renders its progress and result.”**
  - preserve every existing assertion for ownership, stale responses, polling,
    duplicate copy, cancellation, recovery and privacy except those that
    necessarily reference the removed controls.
- `tests/contract/test_local_web_application.py`:
  - remove the old opt-in checkbox assertions and the Start-button assertion;
  - replace `test_upload_dialog_auto_start_is_opt_in_and_scoped` with a test
    that asserts the dialog has **no** `upload-auto-start-input`, **no**
    `upload-start-button`, no checkbox/helper copy and no `uploadAutoStart`
    binding, while retaining the scoped `#upload-dialog[open]` layout and the
    existing file/progress/duplicate/cancel markup;
  - assert the choice is not persisted and no storage write mentions it.
- `tests/companion_web_bridge.test.js`: keep the existing `open_upload` and
  no-progress assertions; update only if a removed control is referenced.
- Do not edit `tests/x_companion_extension.test.js`,
  `tests/youtube_acquisition_cockpit.test.js`,
  `tests/x_acquisition_cockpit.test.js`, `tests/kronika_ui.test.js`,
  `tests/gallery_search_tag_filters.test.js`,
  `tests/automatic_analysis_lifecycle.test.js` or
  `tests/cover_frontend.test.js`; run them unchanged. If one fails because of
  this change, stop and report the exact failure.

### 2.4 Documentation

- `SPEC.md` §18: replace the opt-in/transient-choice and manual-Start wording
  with the unconditional behavior: one upload starts automatically after a
  permitted new selection or drop; no checkbox and no Start control; failed
  gates create no session and allow another selection; explicit Resume remains
  for recovered/paused work; all existing progress, duplicate, privacy,
  replacement-lock and companion statements remain.
- `DEVELOPMENT.md`: update the synthetic-fixture checklist so it says selecting
  or dropping a file starts automatically, no Start control exists, and a
  failed gate allows another selection. Keep the focused commands and
  public-main/NUC prerequisite.
- `docs/X_COMPANION.md`: update only if it names the removed choice or Start
  control; otherwise leave it unchanged.
- `SECURITY.md`, `docs/UX_AUDIT.md` and accepted ADR bodies remain unchanged.
  No new ADR is needed.

## 3. Exact changed-path allowlist

Change only these paths, and only where this correction requires it:

```text
src/kronika/adapters/api/web/index.html
src/kronika/adapters/api/web/app.js
src/kronika/adapters/api/web/styles.css
tests/upload_cockpit_async_ownership.test.js
tests/companion_web_bridge.test.js
tests/contract/test_local_web_application.py
SPEC.md
DEVELOPMENT.md
docs/X_COMPANION.md
```

If a listed file needs no change, leave it unchanged. No new files. Negative
allowlist: every other repository path, especially any API, domain, application
service, persistence, authorization/capability/route-policy, schema, migration,
public-composition, provider, capture, extension-production,
companion-protocol, dependency, asset, deployment or host file; `.ap/**`; the
AP gitlink; `AGENTS.md`; `ap.project.conf`; `SECURITY.md`; `docs/UX_AUDIT.md`;
accepted ADR bodies; and all Meta files except the terminal report. If a
required change falls outside this allowlist, stop and report.

## 4. Baseline and gate

```text
Repository: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Expected branch: main
Baseline commit under test: 076c01658f36f38cb9c8b5a3b4b098d774767616
Parent of the correction commit: 076c01658f36f38cb9c8b5a3b4b098d774767616
Public main: 076c01658f36f38cb9c8b5a3b4b098d774767616
Containing-repository .ap gitlink: d7023cf037f6d17885c3ede5c04812c61640da50
Submodule HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
```

Verify before editing:

```text
git rev-parse HEAD
git status --short
git log --oneline -3
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 076c01658f36f38cb9c8b5a3b4b098d774767616
```

Stop if the worktree is not clean or HEAD is not `076c016`.

## 5. Tests and validation

Run from `/Users/agile/Projects/kronika`:

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

Do not run the full Python suite. Report actual counts. A test failure stops the
affected review and is reported with exact evidence; do not edit a
non-allowlisted test.

Rendered geometry, native picker behavior, real Brave iframe/modal behavior,
scrolling, clipping, focus, contrast, upload timing and assistive-technology
output remain the Cooperator's later rendered acceptance.

## 6. Authority

```text
Positive authority: edit exactly the nine allowlisted paths; read-only
  inspection of the repository, the accepted plan, the implementation report,
  the whole notes and the current upload/companion sources and tests; run the
  exact gate and selected tests above; stage exactly the changed allowlisted
  paths and create exactly one normal corrective commit on main; exact
  direct-write of the terminal report below if it is absent, followed by a
  complete readback.

Negative authority: any other file edit, creation, deletion, rename or chmod;
  any API, repository, domain, application, persistence, authorization,
  capability, route-inventory, schema, migration, public-composition, provider,
  capture, extension-production, companion-protocol, dependency, asset,
  deployment or host change; any edit to SECURITY.md, docs/UX_AUDIT.md, an
  accepted ADR body or AGENTS.md; any Git push, fetch, pull, merge, rebase,
  reset, restore, clean, stash, checkout, switch, branch, tag, remote, config
  write or amend; any NUC, SSH, sudo, deploy, browser, provider, secret or
  private-media access; any acceptance, publication, deployment or closure
  claim; any Meta write except the exact report.

Git authority: read-only inspection plus exactly one normal corrective commit
  on main of the changed allowlisted paths; no push and no amend.
Network authority: none.
Secret authority: none.
```

## 7. Commit and report

After the selected tests pass and `git diff --check` is clean, stage exactly the
changed allowlisted paths and create one corrective commit:

```text
git add -- <the changed allowlisted paths>
git diff --cached --check
git commit -m "fix: make upload start automatic without controls"
git show --stat --oneline HEAD
git status --short
```

Do not push. Report the commit SHA and its parent.

Write the terminal report to:

```text
/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/05_report_00.md
```

The report starts exactly with `### Report for ORCHESTRATOR_CHAT`, echoes the
coordinates and role fields, and contains:

```text
Status: PASS
Phase-qualified result: implementation-PASS
Start commit: 076c01658f36f38cb9c8b5a3b4b098d774767616
End commit: <correction commit SHA>
Report justification: new-mutation
Logical-whole closure: not-closed
```

Include the Cooperator finding, the removed controls, the unconditional start
behavior, exact changed paths and diff stat, gate and test commands with actual
counts, new/updated test identities, documentation updates, any deviation or
residual risk, `Resolved Execution Issues / Near-Misses`, `Pre-Existing Failure
Classification`, one smallest next step, and the orchestration critique. Do not
claim acceptance, publication, deployment or closure.

## 8. Mandatory reading

- The accepted plan `01_report_00.md` and implementation report `03_report_00.md`
  in full, understanding that this prompt supersedes the opt-in/default-off and
  manual-Start parts.
- The whole's `00_notes.md` and the `076c016` rendered finding.
- `.ap/AP.md` at the pinned commit: §2 Roles; §3 Instances, Sessions, and Worker
  Session Profiles; §5 Task Authority; §6 Adaptive Orchestration Lifecycle;
  §7 Orchestrator Responsibilities; §12 Validation and Public Verification;
  §13 Artifact Lifecycle; §15 Fresh-Slice Implementation and Diagnostic
  Closeout; §17 Compact Communication; §19 Anti-Patterns (skim); and the Finite
  Convergence Contract.
- `.ap/AP_WORKER.md` in full and `.ap/PROMPT_CONTRACTS.md` Worker Report Header,
  Correction Record, Common Worker Task Fields, Mutation Axes, Validation Ladder
  and Pre-Existing Failure Classification.
- `AGENTS.md`, `SPEC.md` §18-§19, `SECURITY.md`, `DEVELOPMENT.md`,
  `docs/X_COMPANION.md`, ADR-0053, ADR-0086 and ADR-0088.
- The current upload dialog/controller, upload test suite, companion bridge test
  and served-shell contract.

## 9. Delivery and trace

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/
Trace project key: kronika
Trace logical-whole projection identity: 02-upload-flow-polish
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 05_correction_00.md
Destination path: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/
Report filename: 05_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: exactly the changed allowlisted paths
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/05_report_00.md
```

If the report path exists, including an empty file, stop `BLOCKED` without
overwriting it. The verified parent directory exists.

## Visible delivery capsule

```text
🟡 Ready for delivery
Recipient: Bounded UI Polish Worker · fresh-worker-session · manual
Recommendation: High · approximately 250k tokens
Client: Native Plan Mode OFF
Prompt: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/05_correction_00.md
Report: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/05_report_00.md
Archival: wait-for-report
```
