# Authoritative Worker prompt — Kronika whole 02, Worker session 02, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`upload-flow-polish`. It is stored under the Meta filename mapping
`<worker-session>_<phase>_<meta-exchange-index>.md` as `02_implementation_00.md`.
The matching terminal report is `02_report_00.md`.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: upload-flow-polish
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: Implementation
Task identity: KRN-UPLOAD-IMPL-02 — implement the accepted upload-flow polish plan
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — asynchronous upload ownership, recovery and duplicate privacy are easy to regress
Recommended context capacity: approximately 300k tokens
Implementation authority: explicit
Exact baseline: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
Changed-path allowlist: exactly the nine repository paths in section 2
Implementation boundaries: the positive and negative authority in section 6
Independence required: no
Continuity anchor: accepted plan report 01_report_00.md
```

You are a genuinely fresh Implementation Worker. The plan is accepted; do not
re-plan it. Read the accepted plan report in full before editing:

```text
/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/01_report_00.md
```

That report is the design of record. This prompt supplies the implementation
authority, the exact allowlist, the baseline and the completion contract. If the
plan and this prompt conflict, stop and report the contradiction rather than
improvising.

Before substantive work, confirm that `Native planning mode: not-used` is the
actual client state (native Plan mode OFF). If the client has native Plan mode
enabled, do not start; return `BLOCKED` naming the contradiction.

## 1. Goal

Implement the approved upload-flow polish exactly as planned:

- an opt-in, per-dialog **“Start automatically after choosing a file”** control,
  off by default, reset on dialog reopen and never persisted;
- automatic start invokes the existing capability-gated start path once for a
  new selection or drop, preserving duplicate review, quarantine, validation,
  publication and recovery semantics;
- progress and terminal results stay in the existing hosted upload dialog; no
  new companion message type or persistent panel indicator;
- the two source-observed ownership/resume gaps are fixed:
  - selection cannot replace an in-flight create, active transfer or unresolved
    recovery;
  - a server-confirmed full `receiving` offset offers a reachable Resume that
    completes through the existing endpoint without PATCH;
- the accepted plan's test, documentation and presentation requirements are
  implemented without weakening any existing assertion.

No API, payload, capability, authorization, schema, migration, storage or
companion-protocol change is permitted.

## 2. Exact changed-path allowlist

Change exactly these nine paths, and no others:

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

No new files. Negative allowlist: every other repository path, especially any
API, domain, application service, persistence, authorization/capability/
route-policy, schema, migration, public-composition, provider, capture,
extension-production, companion-protocol, dependency, asset, deployment or
host file; `.ap/**`; the AP gitlink; `AGENTS.md`; `ap.project.conf`;
`SECURITY.md`; `docs/UX_AUDIT.md`; accepted ADR bodies; and all Meta files except
the terminal report. If a required change falls outside the nine paths, stop and
report `BLOCKED`; do not widen the slice.

The selected Python command also runs `test_upload_api.py`,
`test_ordinary_upload_ownership_boundary.py`,
`test_upload_session_architecture.py`,
`test_atomic_upload_publication_contract.py`,
`test_local_web_upload_cockpit.py` and
`test_atomic_upload_publication.py`. Those files are evidence-only and are not
in the edit allowlist. If one fails because of the change, stop and report the
exact failure; do not edit it or weaken it.

## 3. Required behavior

Implement the accepted plan's §3, §5, §6 and §7. The following is the binding
summary; the plan remains the design of record.

### 3.1 Opt-in control

- Add one checkbox immediately before the file selector in `#upload-dialog`.
- Label: **“Start automatically after choosing a file”**.
- Helper text: **“For this open dialog only. Recovered uploads still need
  Resume.”**
- Default **off**; the choice lives outside the resettable upload-session state.
- Reset only on a genuine closed-to-open transition. Repeated `open_upload`
  messages while the dialog is already open must neither reset the choice nor
  create work.
- Toggling the checkbox alone never starts an already selected file.
- Do not persist the choice in local storage, session storage, server settings
  or the recovery record.
- Preserve manual Start whenever an eligible selected file has not started.

### 3.2 Auto-start flow

- Accept one new file only when no unresolved session or action owns the dialog.
- With auto-start off: show Ready and wait for Start.
- With auto-start on: invoke the existing start handler once for that selection.
  Claim ownership synchronously before awaiting capability or session creation.
- Pre-create gates: current `upload.submit`, configured capability, positive
  file size and the current server size limit. Failure creates no session and
  sends no bytes; do not schedule an automatic retry.
- Retain the existing POST payload, offset-confirmed PATCH loop and complete
  request.
- Show confirmed transfer progress independently of server validation. A
  displayed 100% means bytes transferred, not publication or completion.
- Administrator duplicate review remains exactly the existing keep/discard
  actions; auto-start never chooses a disposition.
- Ordinary duplicate handling remains the existing privacy-safe
  `silent_keep_separate` outcome with no duplicate indication or matching
  evidence.
- Retain publication-pending, published and cataloged feedback, including
  ordinary review wording. Keep the terminal result visible until another
  permitted selection or dialog closure.

### 3.3 Concurrency, recovery and failures

- Disable file replacement and the checkbox while preparing, transferring,
  completing, cancelling, restoring an unresolved session, validating or
  awaiting duplicate/finalization outcomes.
- Apply the same exclusion in selection handlers so synthetic events cannot
  bypass disabled controls. Consume blocked file drops without replacing state
  or allowing navigation.
- Allow compatible reselection for a settled incomplete session, but always
  require explicit Resume. Auto-start never resumes recovered or paused work.
- At a server-confirmed full `receiving` offset, offer Resume to finish through
  the existing complete endpoint. Refresh status first; send no PATCH when all
  bytes are present. If refreshed truth requires bytes and no file is
  available, require reselection.
- Preserve cancellation and duplicate-discard confirmations, stale-response
  fencing and one action owner.
- Capability failure, network failure or rejected creation never triggers an
  automatic retry. Manual Start or Resume remains the retry route where
  applicable.
- After uncertain completion or duplicate resolution, refresh server truth
  before presenting the next permitted action.
- Preserve transient polling backoff, generic not-found recovery cleanup and
  unknown-state fail-closed behavior.
- Closing and reopening never creates a new upload. Closing retains the existing
  transfer behavior; reopening refreshes the existing session and resumes
  eligible status polling.
- Preserve the existing recovery-key format, legacy-key fallback and cleanup
  policy. Do not add durable upload history or claim cross-tab coordination.
- Do not retry creation automatically and do not claim exactly-once session
  creation across an unknown response or independent tabs.

### 3.4 Presentation

- Retain the existing row, progress bar, status and action labels. Keep error
  and progress information in the existing live-status surface.
- Scope new layout rules to `#upload-dialog`: vertical flex while open, a
  scrollable body, a reachable footer and wrapping checkbox text at narrow
  widths.
- Do not alter shared `.upload-dialog` geometry for YouTube, X or confirmation
  dialogs.

### 3.5 Tests

Extend the upload harness and scenarios in
`tests/upload_cockpit_async_ownership.test.js` with named causal tests covering:

- **“Auto-start defaults off, survives file reset, and resets only on dialog
  reopen.”**
- **“Opted-in picker and drop selection start one upload with the existing
  payload.”**
- **“Auto-start fails closed for capability, empty-file and size failures
  without delayed retry.”**
- **“Active or recovering uploads reject replacement selection and repeated
  open requests.”**
- **“Auto-start preserves administrator duplicate review and ordinary duplicate
  privacy.”**
- **“Full-offset Resume completes without PATCH, while recovered byte transfer
  still requires explicit Resume.”**
- **“Hosted open_upload opens the same dialog without starting a transfer and
  renders its progress and result.”**

Use deferred responses to exercise capability, creation, PATCH, completion and
cancellation races. Extend the upload harness with the actual companion host
registration for the hosted behavior test; do not claim a callback-only mock
proves application wiring.

Extend `tests/companion_web_bridge.test.js` for the existing `open_upload`
negative coverage; do not change the protocol. Extend
`tests/contract/test_local_web_application.py` for the checkbox, scoped layout
and truthful copy without weakening existing assertions.

### 3.6 Documentation

- `SPEC.md` §18 is the sole normative owner: add the bounded auto-start
  lifecycle, the transient per-dialog choice, explicit recovery/resume and
  truthful progress semantics. Retain §19's companion boundary.
- `DEVELOPMENT.md`: focused commands, synthetic-fixture checklist and the
  public-main/NUC rendered-acceptance prerequisite, linking to SPEC for
  behavior.
- `docs/X_COMPANION.md`: explain that 📤 opens the hosted dialog and that
  progress/results stay there, linking to SPEC.
- `SECURITY.md` remains unchanged; its upload boundary is preserved.
- `docs/UX_AUDIT.md` remains frozen historical evidence.
- No new ADR is needed. ADR-0053, ADR-0086 and ADR-0088 remain intact.

## 4. Baseline and gate

```text
Repository: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Expected branch: main
Baseline commit under test: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
Parent of the implementation commit: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
Public main: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
Containing-repository .ap gitlink: d7023cf037f6d17885c3ede5c04812c61640da50
Submodule HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
```

Verify before editing:

```text
git rev-parse HEAD
git status --short
git log --oneline -3
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
```

Stop if the worktree is not clean or HEAD is not `8646146`.

## 5. Tests and completion

Run from `/Users/agile/Projects/kronika`:

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

Do not run the full Python suite. Report actual counts. A failure stops the
affected work and is reported with exact evidence; do not repair unrelated
behavior or edit a non-allowlisted test.

Rendered geometry, real Brave iframe/modal behavior, native picker behavior,
scrolling, clipping, focus, contrast and actual upload timing remain the
Cooperator's later rendered acceptance. Do not claim them from Node or contract
tests.

## 6. Authority

```text
Positive authority: edit exactly the nine allowlisted paths; read-only
  inspection of the repository, the accepted plan, the whole notes and the
  current upload/companion sources and tests; run the exact gate and selected
  tests above; stage exactly the changed allowlisted paths and create exactly
  one normal implementation commit on main; exact direct-write of the terminal
  report below if it is absent, followed by a complete readback.

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

Git authority: read-only inspection plus exactly one normal implementation
  commit on main of the changed allowlisted paths; no push and no amend.
Network authority: none.
Secret authority: none.
```

## 7. Commit and report

After the selected tests pass and `git diff --check` is clean, stage exactly the
changed allowlisted paths and create one implementation commit:

```text
git add -- <the changed allowlisted paths>
git diff --cached --check
git commit -m "feat: add opt-in upload auto-start"
git show --stat --oneline HEAD
git status --short
```

Do not push. Report the commit SHA and its parent.

Write the terminal report to:

```text
/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/02_report_00.md
```

The report starts exactly with `### Report for ORCHESTRATOR_CHAT`, echoes the
coordinates and role fields, and contains:

```text
Status: PASS
Phase-qualified result: implementation-PASS
Start commit: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
End commit: <implementation commit SHA>
Report justification: new-mutation
Logical-whole closure: not-closed
```

Include the implemented behavior, exact changed paths and diff stat, gate and
test commands with actual counts, new/updated test identities, documentation
updates, any deviation or residual risk, `Resolved Execution Issues /
Near-Misses`, `Pre-Existing Failure Classification`, one smallest next step, and
the orchestration critique. Do not claim acceptance, publication, deployment or
closure.

## 8. Mandatory reading

- The accepted plan `01_report_00.md` in full, especially §2, §3, §4, §5, §6,
  §7 and §8.
- The whole's `00_notes.md` and `00_handout.md` for context; the handout is
  historical seed evidence, not authority.
- `.ap/AP.md` at the pinned commit: §2 Roles; §3 Instances, Sessions, and Worker
  Session Profiles; §5 Task Authority; §6 Adaptive Orchestration Lifecycle;
  §7 Orchestrator Responsibilities; §12 Validation and Public Verification;
  §13 Artifact Lifecycle; §15 Fresh-Slice Implementation and Diagnostic
  Closeout; §17 Compact Communication; §19 Anti-Patterns (skim); and the Finite
  Convergence Contract.
- `.ap/AP_WORKER.md` in full.
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header; Common Worker Task Fields;
  Repository Checkout Topology; Worker Session Target; Cooperator Delivery and
  Trace Destination; Mutation Axes; Validation Ladder; Pre-Existing Failure
  Classification.
- `AGENTS.md`, `SPEC.md`, `SECURITY.md`, `DEVELOPMENT.md`,
  `docs/X_COMPANION.md`, `docs/UX_AUDIT.md`, ADR-0053, ADR-0086 and ADR-0088.
- The exact upload, companion and test sources named in the plan.

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
Downloadable prompt filename: 02_implementation_00.md
Destination path: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/
Report filename: 02_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: exactly the nine allowlisted paths
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/02_report_00.md
```

If the report path exists, including an empty file, stop `BLOCKED` without
overwriting it. The verified parent directory exists.

## Visible delivery capsule

```text
🟡 Ready for delivery
Recipient: Fresh Implementation Worker · fresh-worker-session · manual
Recommendation: High · approximately 300k tokens
Client: Native Plan Mode OFF
Prompt: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/02_implementation_00.md
Report: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/02_report_00.md
Archival: wait-for-report
```
