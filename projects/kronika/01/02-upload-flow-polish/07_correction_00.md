# Authoritative Worker prompt — Kronika whole 02, Worker session 07, exchange 01

Activation: this file is the exact issued Worker prompt for the Cooperator's
bounded post-acceptance cover UX correction in logical whole
`upload-flow-polish`. It is stored under the Meta filename mapping
`<worker-session>_<phase>_<meta-exchange-index>.md` as `07_correction_00.md`.
The matching terminal report is `07_report_00.md`.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: upload-flow-polish (post-acceptance UX correction)
Worker session ordinal: 07
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded UI Polish Worker
Phase: Correction
Task identity: KRN-COVER-CORR-01 — move Choose cover, add a brain icon and auto-preview the selected frame
Delivery route: manual Cooperator delivery
Reasoning recommendation: Medium — bounded UI/test correction with asynchronous preview, nested dialogs and a real-browser evidence fixture
Recommended context capacity: approximately 200k tokens
Independence required: no
Continuity anchor: rendered upload-flow PASS at 0a96fc18b49191a32e7f482c4e881ad714db094a and the Cooperator's 2026-11-10 cover UX finding
Authority renewal: prior acceptance and correction authority expired; this prompt grants a new bounded correction
Evidence posture: non-independent correction; Orchestrator verification and Cooperator rendered acceptance follow
```

You are a genuinely fresh Worker for this bounded correction. The upload-flow
whole is already accepted and deployed at `0a96fc1`; do not re-open it. The
Cooperator directed this cover UX correction explicitly and said it does not
need a new planning whole. The design below is complete; do not re-plan it.

Read for context, not as proof:

```text
/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/00_notes.md
/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/01_report_00.md
/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/06_report_00.md
```

Before substantive work, confirm that `Native planning mode: not-used` is the
actual client state (native Plan mode OFF). If it is enabled, stop and return
`BLOCKED` naming the contradiction.

## 1. Cooperator finding and exact design

The media-details window currently shows **Choose cover**; the Edit window has
**Analyze by AI** but no cover action. The Choose cover dialog has a
**Preview frame** button that the Cooperator rejects. The requested design:

1. Remove **Choose cover** from the media-details footer. The Details footer
   keeps only Edit.
2. Add **Choose cover** to the Edit metadata dialog footer, immediately after
   **Analyze by AI** and before **Cancel**. It opens the existing cover dialog
   for the item currently open in the metadata workspace.
3. Use a **brain** emoji for **Analyze by AI** instead of the current
   invisible sparkle. The existing button text and accessible name remain
   exactly “Analyze by AI”.
4. Style **Choose cover** like **Analyze by AI** but with a slightly grey, not
   pure-white, surface. Keep the existing 🖼️ leading icon, dark text, readable
   focus and disabled states.
5. In the cover dialog, remove the **Preview frame** button. Keep the timeline
   slider, `−250 ms` and `+250 ms` steps, the readout and the preview region.
6. When the cover dialog opens, automatically load and show the **first frame**
   at timestamp 0 after the timeline/source metadata resolves. Do this for
   video, animated-image and still-image items.
7. While the user drags the slider, update the readout only. When the slider is
   **released** (`change`), automatically request the selected frame preview.
   The `±250 ms` step buttons also request the preview after updating the time.
8. Keep the existing preview abort/token fencing, loading/error status,
   “not saved until Set as cover” wording, explicit **Set as cover** and
   replace-confirmation behavior. A preview never becomes the accepted cover.
9. No API, payload, authorization, schema, migration, storage or cover-accept
   semantics change. This is presentation and client interaction only.

## 2. Exact implementation

### 2.1 HTML

- In `src/kronika/adapters/api/web/index.html`, remove the whole
  `#media-details-choose-cover` button from the media-details footer.
- Add to the metadata footer, immediately after `#metadata-ai-analyze-button`
  and before `#metadata-discard-button`:

```html
<button id="metadata-choose-cover" class="metadata-choose-cover-button" type="button" hidden>Choose cover</button>
```

- Remove `<button id="cover-preview-button" ...>Preview frame</button>` from the
  cover timeline actions. Keep `#cover-step-back` and `#cover-step-forward`,
  the range input, readout, preview container/status and Set/Cancel controls.

### 2.2 JavaScript

- Replace the `detailsChooseCoverButton` binding with a
  `metadataChooseCoverButton` binding for `#metadata-choose-cover`; update the
  capability visibility in `applyIdentityCapabilities` to that button.
- Move the click handler: when the metadata button is clicked, call
  `openCoverDialog(metadataWorkspace.openItem, metadataChooseCoverButton)` if
  the workspace has an item. Remove the old details-button handler.
- Remove `coverPreviewButton` binding, listener, disabled/enabled updates and
  any dead start/visibility branches tied to it.
- In `loadCoverTimeline`, after `showCoverContent()` and the context check,
  call `void requestCoverPreview()` for every media kind, not only images.
- Keep `handleCoverRangeInput` for the `input` event (readout and replace
  confirmation only). Add a `change` listener that requests the preview after
  the slider is released.
- In `stepCoverTimestamp`, update the timestamp/readout, hide replace
  confirmation, then request the preview.
- Keep the preview request's abort controller, preview token, source-version
  check and `Set as cover` enablement. Remove only the preview-button
  enable/disable.
- In `KRONIKA_BUTTON_ICONS`, change `"Analyze by AI": "✨"` to
  `"Analyze by AI": "🧠"` and remove the now-unused `"Preview frame": "👁️"`
  entry. Keep `"Choose cover": "🖼️"`.

### 2.3 CSS

- Remove the unused `.cover-button--primary` rule if no other control uses it.
- Add a `.metadata-dialog__footer .metadata-choose-cover-button` style based on
  the Analyze-by-AI treatment: inline-flex, centered, same gap/padding/focus
  shape, dark text on a slightly grey background (for example `#c9d1c9` with a
  lighter grey hover such as `#d7ded7`), grey-green border and a clear disabled
  state. It must not be pure white and must remain readable.
- Update the public-audience selector from
  `#media-details-choose-cover` to `#metadata-choose-cover` if that selector is
  retained. Shared metadata-details and cover-dialog geometry stays unchanged.

## 3. Exact changed-path allowlist

Change only these six paths:

```text
src/kronika/adapters/api/web/index.html
src/kronika/adapters/api/web/app.js
src/kronika/adapters/api/web/styles.css
tests/cover_frontend.test.js
tests/browser_cover_evidence.test.js
tests/contract/test_local_web_application.py
```

No new files. If a listed file needs no change, leave it unchanged. Negative
allowlist: every other repository path, especially API, domain, application,
persistence, authorization, schema, migration, provider, capture, companion,
extension-production, dependency, asset, deployment or host files; `.ap/**`;
the AP gitlink; `AGENTS.md`; `ap.project.conf`; `SECURITY.md`;
`docs/UX_AUDIT.md`; `SPEC.md`; accepted ADR bodies; and all Meta files except
the report. `SPEC.md` and `docs/UX_AUDIT.md` remain unchanged: this correction
does not change cover acceptance, authorization or durable cover semantics.

## 4. Tests

Update the existing tests without weakening them:

- `tests/cover_frontend.test.js`:
  - replace `media-details-choose-cover` with `metadata-choose-cover` in the
    markup ID list;
  - remove `cover-preview-button` from the present-ID list and assert it is
    absent;
  - assert the details footer no longer contains the cover button and the
    metadata footer places the cover button after Analyze by AI and before
    Cancel;
  - assert the brain icon mapping and the absence of the Preview-frame icon
    entry;
  - add source assertions for automatic preview: the open path requests a
    preview, the range `change` listener requests one, and the step helper
    requests one.
- `tests/contract/test_local_web_application.py`: add or update one focused
  contract test for the moved button, footer order, removed preview button,
  grey `.metadata-choose-cover-button` style, `🧠` icon mapping and no
  `coverPreviewButton`/details-cover remnants. Keep all existing metadata and
  cover assertions intact.
- `tests/browser_cover_evidence.test.js`: update the two cover-authoring flows
  to open **Edit** and then click `#metadata-choose-cover` instead of the
  removed details button; remove the `#cover-preview-button` click and wait for
  the automatic first-frame preview; close the metadata dialog after cover
  success before opening the next details flow. Keep the browser test gated by
  `KRONIKA_RUN_BROWSER_EVIDENCE=1`; a skipped run is acceptable and must be
  reported honestly.

Run from `/Users/agile/Projects/kronika`:

```text
# [MacBook / fish]
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 0a96fc18b49191a32e7f482c4e881ad714db094a
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 0a96fc18b49191a32e7f482c4e881ad714db094a --operation test-focus -- tests/contract/test_local_web_application.py tests/contract/test_cover_api.py -q -p no:cacheprovider
node --test tests/cover_frontend.test.js tests/catalog_card_ai_quick_action.test.js tests/kronika_ui.test.js tests/browser_cover_evidence.test.js
git diff --check
git status --short
#------------------------------------------------------
```

The browser evidence test may skip without `KRONIKA_RUN_BROWSER_EVIDENCE=1`.
If Chrome/ffmpeg and the gated environment are available, run it; otherwise
report `skipped` and do not claim rendered evidence. The Cooperator's rendered
cover check remains the final UI evidence.

## 5. Baseline and gate

```text
Repository: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Expected branch: main
Baseline commit under test: 0a96fc18b49191a32e7f482c4e881ad714db094a
Parent of the correction commit: 0a96fc18b49191a32e7f482c4e881ad714db094a
Public main: 0a96fc18b49191a32e7f482c4e881ad714db094a
Containing-repository .ap gitlink: d7023cf037f6d17885c3ede5c04812c61640da50
Submodule HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
```

Verify before editing:

```text
git rev-parse HEAD
git status --short
git log --oneline -3
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 0a96fc18b49191a32e7f482c4e881ad714db094a
```

Stop if the worktree is not clean or HEAD is not `0a96fc1`.

## 6. Authority

```text
Positive authority: edit exactly the six allowlisted paths; read-only
  inspection of the repository, the whole notes, the accepted plan, the
  implementation/acceptance reports and the cover/upload sources and tests; run
  the exact gate and selected tests above; stage exactly the changed
  allowlisted paths and create exactly one normal corrective commit on main;
  exact direct-write of the terminal report below if it is absent, followed by
  a complete readback.

Negative authority: any other file edit, creation, deletion, rename or chmod;
  any API, repository, domain, application, persistence, authorization,
  capability, route-inventory, schema, migration, public-composition, provider,
  capture, extension-production, companion-protocol, dependency, asset,
  deployment or host change; any edit to SPEC.md, SECURITY.md,
  docs/UX_AUDIT.md, an accepted ADR body or AGENTS.md; any Git push, fetch,
  pull, merge, rebase, reset, restore, clean, stash, checkout, switch, branch,
  tag, remote, config write or amend; any NUC, SSH, sudo, deploy, browser,
  provider, secret or private-media access outside the optional gated local
  browser evidence test; any acceptance, publication, deployment or closure
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
git commit -m "fix: move cover selection and auto-preview the frame"
git show --stat --oneline HEAD
git status --short
```

Do not push. Report the commit SHA and its parent.

Write the terminal report to:

```text
/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/07_report_00.md
```

The report starts exactly with `### Report for ORCHESTRATOR_CHAT`, echoes the
coordinates and role fields, and contains:

```text
Status: PASS
Phase-qualified result: implementation-PASS
Start commit: 0a96fc18b49191a32e7f482c4e881ad714db094a
End commit: <correction commit SHA>
Report justification: new-mutation
Logical-whole closure: not-closed
```

Include the Cooperator finding, the exact moved controls and icon/style
changes, the automatic preview wiring, exact changed paths and diff stat, gate
and test commands with actual counts, browser-test skip/run status, any
deviation or residual risk, `Resolved Execution Issues / Near-Misses`,
`Pre-existing Failure Classification`, one smallest next step, and the
orchestration critique. Do not claim acceptance, publication, deployment or
closure.

## 8. Mandatory reading

- The whole's `00_notes.md`, `01_report_00.md` and `06_report_00.md`.
- `.ap/AP.md` at the pinned commit: §2 Roles; §3 Instances, Sessions, and Worker
  Session Profiles; §5 Task Authority; §6 Adaptive Orchestration Lifecycle;
  §7 Orchestrator Responsibilities; §12 Validation and Public Verification;
  §13 Artifact Lifecycle; §15 Fresh-Slice Implementation and Diagnostic
  Closeout; §17 Compact Communication; §19 Anti-Patterns (skim); and the Finite
  Convergence Contract.
- `.ap/AP_WORKER.md` in full and `.ap/PROMPT_CONTRACTS.md` Worker Report Header,
  Correction Record, Common Worker Task Fields, Mutation Axes, Validation Ladder
  and Pre-Existing Failure Classification.
- `SPEC.md` §13 cover requirements (read-only), `SECURITY.md` cover boundary,
  `docs/UX_AUDIT.md` (historical), ADR-0050, ADR-0053 and ADR-0088.
- The current media-details, metadata-dialog and cover-dialog markup,
  controller, CSS, `tests/cover_frontend.test.js`,
  `tests/browser_cover_evidence.test.js` and the relevant metadata contract
  tests.

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
Downloadable prompt filename: 07_correction_00.md
Destination path: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/
Report filename: 07_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: exactly the changed allowlisted paths
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/07_report_00.md
```

If the report path exists, including an empty file, stop `BLOCKED` without
overwriting it. The verified parent directory exists.

## Visible delivery capsule

```text
🟡 Ready for delivery
Recipient: Bounded UI Polish Worker · fresh-worker-session · manual
Recommendation: Medium · approximately 200k tokens
Client: Native Plan Mode OFF
Prompt: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/07_correction_00.md
Report: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/07_report_00.md
Archival: wait-for-report
```
