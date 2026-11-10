# Kronika whole 02 — upload-flow-polish

## Opening and Handout Revalidation — 2026-11-10

The COOPERATOR selected `upload-flow-polish` on 2026-11-09 and deferred it until
the preceding UI/UX wholes closed. Whole 01 closed at `e6b26eb`, whole 09 closed
at `65772c6` and whole 10 closed at `8646146` after the Cooperator's final
rendered PASS. The deferral condition is satisfied; this whole opens as a new
logical whole with an independent planning cycle.

```text
Handout revalidation: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/00_handout.md
Received handout status: provisional
Revalidated against: Kronika 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e; AP d7023cf037f6d17885c3ede5c04812c61640da50; NUC active/web 8646146; run map entries 01, 09 and 10 closed; ADR-0088
Usable facts: repository URL and canonical checkout; the Cooperator's selection of upload-flow-polish; the polish objective, likely scope, out-of-scope exclusions and nine planning questions; the manual-delivery, direct-write-report, no-subagent and Meta-Git operating rules; the repository/NUC security boundaries; the upgrade-ledger path; the first Planner coordinates; the whole's Meta directory
Stale facts and corrections: last observed repository HEAD b66ec8f -> 8646146; public main b66ec8f -> 8646146; NUC active/web b66ec8f -> 8646146 with capture 5b86d896b3ea03f89fef2c90f7af2c121d0ef915 and database revision 0035; predecessor whole 01 formal closure pending -> closed at e6b26eb with Cooperator-declared production acceptance; whole 02 deferred until after entry 10 -> entry 10 closed at 8646146; run-map entry 01 active and entry 02 handed-off -> entries 01, 09 and 10 closed and entry 02 active; ADR-0083 separate personal History view -> superseded by ADR-0088 Timeline-as-single-overview, no separate History view; whole 01 preview change as the latest shell context -> whole 10 additionally changed header search, navigation, Timeline filters and chronicle presentation
Not revalidated: none
Handout disposition: adopted-with-corrections
```

The handout remains historical seed evidence; this record is the current
revalidation and does not edit the handout. The Planner must read both and
re-measure the upload flow, companion bridge, shell, tests and documentation
rather than trusting either artifact.

## Stage 1 evidence — 2026-11-10

```text
Repository: https://github.com/cisarik/kronika
Local checkout: /Users/agile/Projects/kronika
HEAD and public main: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
Branch: main; working tree clean
AP pin: d7023cf037f6d17885c3ede5c04812c61640da50 (.ap gitlink, submodule HEAD and governing stable variant)
ap doctor: PASS
ap project check --baseline 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e: PASS
NUC: layout canonical; active/web 8646146; capture 5b86d896b3ea03f89fef2c90f7af2c121d0ef915; service active; database revision 0035; backup restore-readiness ready; sudo timestamp revoked after deployment
Upgrade ledger: docs/AP_UPGRADE_OBSERVATIONS.md valid; one active entry consumer-declared-execution-and-capability-route-binding remains accepted, non-authorizing, retain-active; no ledger mutation
```

The NUC facts were observed through the canonical release helper during the
whole 10 deployment. The sudo timestamp was then revoked with `sudo -K`; a later
deployment needs a fresh Cooperator authorization. No repository, Git, NUC,
browser, provider, secret or host mutation was performed during this
revalidation.

## Current product context the Planner must preserve

- ADR-0088 is current: the Timeline is the single authorized overview; the
  separate History view is removed; question and answer APIs remain; Gallery and
  Details remain separate.
- Whole 10's final shell is at `8646146`: header-slot Timeline/Gallery search,
  Publishing-first Timeline filters, no visible Timeline hero/lede/note,
  request/record routes keep Timeline current, and the chronicle/listbox/glyph
  behavior is accepted.
- ADR-0086 owns the companion `open_upload` message and the hosted upload
  dialog; the extension side panel's upload control posts it only after the
  sidebar handshake.
- The upload security boundary remains: `upload.submit` for ordinary users,
  `upload.manage` for administrators, quarantine before validation, exact
  duplicate disposition, no publication without the existing approval
  semantics, no public upload service.

## Next step

Prepare the first Planner prompt for Worker session `01`, exchange `01`,
`fresh-worker-session`, `Native planning mode: required`, `Planning cycle:
initial`, `Plan disposition: approval-gated`, implementation prohibited in the
same session and a fresh post-plan implementation session. The prompt is
`01_planning_00.md`; the terminal report is `01_report_00.md`. The Cooperator
delivers it manually.

## Planner report reconciliation — 2026-11-10

`01_report_00.md` is present and was read back in full. The Planner reported
`Status: PARTIAL` solely because the active client Plan Mode prohibited the
report write; the exact report is now persisted at the intended path and read
back, so the persistence limitation is resolved. The plan result is
`planning-PASS`; the design is decision-complete.

The plan recommends:

- one opt-in checkbox, **“Start automatically after choosing a file”**, off by
  default, retained only for one open dialog and reset on dialog reopen; never
  persisted;
- auto-start invokes the existing capability-gated start handler once and
  preserves duplicate review (administrator keep/discard, ordinary silent
  keep-separate), quarantine, validation, publication semantics and the
  existing recovery/cancel/pause/resume model;
- companion progress and terminal results remain inside the existing hosted
  upload dialog; no new message type, panel indicator or protocol change;
- closing two source-observed gaps: selection must not replace an in-flight
  create or unresolved recovery, and a server-confirmed full `receiving` offset
  must offer a reachable Resume that completes without PATCH;
- no API, payload, authorization, schema, migration or companion-protocol
  change;
- nine proposed changed paths: `index.html`, `app.js`, `styles.css`,
  `tests/upload_cockpit_async_ownership.test.js`,
  `tests/companion_web_bridge.test.js`,
  `tests/contract/test_local_web_application.py`, `SPEC.md`, `DEVELOPMENT.md`
  and `docs/X_COMPANION.md`;
- `SPEC.md` §18 as the sole normative owner; `DEVELOPMENT.md` and
  `docs/X_COMPANION.md` updated; `SECURITY.md` unchanged; no new ADR;
  ADR-0086, ADR-0088 and the Gallery/Details freeze preserved;
- no open product decisions; recommended implementation reasoning High, one
  fresh independent E2 acceptance, then publication, routine NUC refresh and
  Cooperator rendered acceptance.

The Orchestrator spot-checked the material claims: the baseline, public `main`
and AP pin are unchanged; all nine proposed paths and all selected Python/Node
test files exist; the upload routes use `upload.submit`; the companion `#frame`
hosts the shell and the sidebar posts `open_upload`; no auto-start markup exists
today. The plan is consistent with current source. No repository, Git, NUC,
browser, provider or host mutation occurred.

Plan status: **reconciled and submitted for Cooperator approval**; not yet
accepted and not yet implementation authority. The two product choices in the
plan — per-dialog default-off auto-start and companion progress inside the
existing dialog — are part of the approval request.

## Plan approval — 2026-11-10

The COOPERATOR approved the reconciled plan as-is and confirmed both product
choices:

1. auto-start is **off by default**, retained only for one open upload dialog
   and reset on dialog reopen; it is not persisted;
2. companion progress and terminal results remain inside the existing hosted
   upload dialog; no persistent panel indicator or new companion message type is
   required.

The plan report `01_report_00.md` is the design of record. The approved scope is
the nine-path UI/test/documentation slice, with no API, payload, authorization,
schema, migration, extension-production or companion-protocol change.

Implementation prompt `02_implementation_00.md` is prepared for a genuinely
fresh Worker session `02`, exchange `01`, `fresh-worker-session`, `Native
planning mode: not-used`, explicit implementation authority, baseline
`8646146`, the exact nine-path allowlist and report `02_report_00.md`. The
Cooperator delivers it manually. Implementation, acceptance, publication,
deployment and rendered acceptance remain pending.

## Implementation delivery mismatch — 2026-11-10

The file `02_report_00.md` is byte-identical to `01_report_00.md` (SHA-256
`42d28851c7236d17bd8a3297dbd04a96dd940190bd44a515f0b167dbf87a9ef3`) and
carries the Planner's session 01 / Planning coordinates, not the implementation
session 02 coordinates. The repository is still at
`8646146b7dfd50a9a99ec94dbd696102cbe5ca4e`; there is no implementation commit,
no worktree change and no new branch. The file is a misdelivered planning copy,
not a terminal implementation report, and is preserved unchanged as delivery
evidence.

The implementation session 02/01 coordinates are consumed. A corrected
implementation prompt `03_implementation_00.md` is prepared for a genuinely
fresh session `03`, exchange `01`, with baseline `8646146`, the same accepted
plan and nine-path allowlist, and report `03_report_00.md`. The prior report path
`02_report_00.md` must not be overwritten. Implementation, acceptance,
publication, deployment and rendered acceptance remain pending.

## Implementation reconciliation — 2026-11-10

`03_report_00.md` is present and was read back in full. It is a terminal
**implementation-PASS** report for local candidate
`076c01658f36f38cb9c8b5a3b4b098d774767616`, parent
`8646146b7dfd50a9a99ec94dbd696102cbe5ca4e`, changing exactly the nine
allowlisted paths (857 insertions, 20 deletions). Public `main` remains
`8646146`; the candidate is local and unpushed; the worktree is clean.

The Orchestrator inspected the diff: the checkbox is placed before the file
selector with the approved label and helper text; the choice is outside the
resettable upload state, resets only on closed-to-open, survives repeated opens
and is not persisted; auto-start invokes the existing start path once and keeps
the existing POST/PATCH/complete payload; capability, configured, positive-size
and size-limit gates fail closed without automatic retry; duplicate review stays
administrator-only keep/discard with ordinary silent keep-separate; replacement
selection is locked during active or unresolved work with handler-level
exclusion and consumed blocked drops; a server-confirmed full `receiving` offset
offers Resume and completes without PATCH; the presentation rules are scoped to
`#upload-dialog`; SPEC §18, DEVELOPMENT and X_COMPANION are updated; SECURITY,
docs/UX_AUDIT.md, the ADRs and extension production sources are untouched. No
API, authorization, payload, schema, migration or companion-protocol change was
introduced.

The Orchestrator independently re-ran the exact selected evidence:
`ap project check --baseline 8646146` PASS, the selected Python suite **277
passed**, and the selected Node suite **285 passed**. The implementation
report's counts match. `git diff --check` is clean and the worktree is clean.

Implementation reconciliation disposition: **accepted for fresh E2
acceptance**, not final acceptance. Prompt `04_acceptance_00.md` is prepared for
fresh Worker session `04`, exchange `01`, profile Fresh Independent Audit,
against fixed candidate `076c016`, with the nine-path allowlist, the A-H matrix
and the exact selected tests. Report destination `04_report_00.md`; the
Cooperator delivers it manually. No repository, Git, NUC, browser, provider or
host mutation was performed by this reconciliation.

## Acceptance reconciliation — 2026-11-10

`04_report_00.md` is present and was read back in full. It is a terminal
**acceptance-PASS** report for candidate
`076c01658f36f38cb9c8b5a3b4b098d774767616`, start
`8646146b7dfd50a9a99ec94dbd696102cbe5ca4e`, with all A-G claims PASS. The
auditor independently re-ran the exact selected gate and tests: **277** selected
Python tests and **285** selected Node tests passed; the worktree remained
clean, HEAD stayed at the candidate, and the diff was exactly the nine
allowlisted paths (857 insertions, 20 deletions). No API, authorization,
payload, schema, migration, extension-production or companion-protocol change
was found. Rendered geometry, native picker, Brave iframe/modal, scrolling,
clipping, focus, contrast, upload timing and assistive-technology output remain
the Cooperator's rendered acceptance.

The auditor marked `Primary fresh acceptances used: 1`, recording consumption of
the issued budget by this report. No correction is required.

Acceptance disposition: **accepted**. The candidate is ready for publication,
NUC deployment and the Cooperator's rendered upload-flow acceptance.

## Publication — 2026-11-10

Publication PASS. The accepted candidate was pushed normally:
`8646146..076c016` on `main`, no force. Direct `git ls-remote` readback
returned `076c01658f36f38cb9c8b5a3b4b098d774767616`; local HEAD and
`origin/main` match; the worktree is clean.

NUC deployment is pending a fresh Cooperator sudo authorization. The canonical
`sudo -n true` probe still requires a password, so the NUC remains at
`8646146b7dfd50a9a99ec94dbd696102cbe5ca4e`. Once the Cooperator refreshes the
timestamp outside the Worker, the deployment can proceed through the canonical
helper and the rendered upload-flow acceptance follows.

## Deployment — 2026-11-10

The Cooperator refreshed the sudo timestamp and the canonical helper completed
the routine deployment at
`076c01658f36f38cb9c8b5a3b4b098d774767616` with exit 0. Post-deploy `status`
reports `layout: canonical`, `active_release` and `web_release`
`076c01658f36f38cb9c8b5a3b4b098d774767616`, `capture_release`
`5b86d896b3ea03f89fef2c90f7af2c121d0ef915`, `service_active: active`,
`database_revision: 0035` and `backup_restore_readiness: ready`. Bounded
read-only checks confirmed the deployed shell contains the auto-start checkbox
and controller bindings; the deployed `SPEC.md` and docs are from the same
release. Terminal `sudo -K` was run; a following `sudo -n true` requires a
password.

The Cooperator's rendered upload-flow acceptance remains the only pending
closure input. It covers the opt-in control, auto-start, progress/terminal
state, replacement lock, duplicate review/privacy, pause/resume/cancel, reopen,
companion `open_upload`, narrow layout and adjacent views.

## Rendered finding and correction — 2026-11-10

The Cooperator rendered the deployed `076c016` upload flow and declared the
behavior **PASS** except for the opt-in control. His product decision:

- the **“Start automatically after choosing a file” checkbox is unnecessary and
  bad UX**;
- auto-start is the **default and only** behavior: one upload starts
  automatically after a permitted file selection or drop;
- the in-dialog **“Start upload” button is unnecessary** and is removed;
- the header/companion Upload controls remain as the way to open the dialog;
- explicit Resume remains for recovered or paused uploads; auto-start never
  resumes that work.

This supersedes the opt-in/default-off and manual-Start parts of the accepted
plan `01_report_00.md` and the implementation report `03_report_00.md`. The
rest of the accepted upload behavior — capability and size gates, duplicate
review and ordinary privacy, replacement locks, full-offset Resume, progress,
companion `open_upload`, scoped presentation and no API/authorization/schema/
protocol change — remains in force.

Bounded correction prompt `05_correction_00.md` is prepared for a genuinely
fresh Worker session `05`, exchange `01`, baseline `076c016`, with the same
nine-path allowlist and report `05_report_00.md`. A fresh E2 re-acceptance,
publication, NUC refresh and rendered re-test follow. The published and deployed
`076c016` remains the functional baseline, not the final release.

## Correction reconciliation — 2026-11-10

`05_report_00.md` is present and was read back in full. It is a terminal
**implementation-PASS** report for local candidate
`0a96fc18b49191a32e7f482c4e881ad714db094a`, parent
`076c01658f36f38cb9c8b5a3b4b098d774767616`, changing seven allowlisted paths
(74 insertions, 223 deletions). Public `main` remains `076c016`; the candidate is
local and unpushed; the worktree is clean.

The Orchestrator inspected the diff: the checkbox, helper text, `uploadAutoStart`
state, checkbox listener and reset, the Start upload button, its binding and
listener, the unused start-visibility calculations and the checkbox-specific
CSS are removed. A permitted new selection or drop now calls
`resetUploadForFile(file)` and then `handleStartUpload()` unconditionally;
recovered or paused work still requires explicit Resume. Capability, size,
duplicate, privacy, replacement-lock, polling, recovery and companion
`open_upload` behavior are unchanged. The scoped `#upload-dialog[open]` flex
layout remains; shared dialog geometry is untouched. `SPEC.md` §18 and
`DEVELOPMENT.md` describe the unconditional behavior; `X_COMPANION.md` and the
companion bridge test needed no change. No API, authorization, payload, schema,
migration, extension-production or companion-protocol change was introduced.

The Orchestrator independently re-ran the exact selected evidence:
`ap project check --baseline 076c016` PASS, the selected Python suite **277
passed**, and the selected Node suite **285 passed**. The correction report's
counts match. `git diff --check` is clean and the worktree is clean.

Correction disposition: **accepted for full-fresh E2 re-acceptance**, not final
acceptance. Prompt `06_acceptance_00.md` is prepared for fresh Worker session
`06`, exchange `01`, profile Fresh Independent Audit, against fixed candidate
`0a96fc1`, with the nine-path whole allowlist, the seven-path correction, the
A-G matrix and the exact selected tests. Report destination `06_report_00.md`;
the Cooperator delivers it manually.

## Re-acceptance reconciliation — 2026-11-10

`06_report_00.md` is present and was read back in full. It is a terminal
**acceptance-PASS** report for candidate
`0a96fc18b49191a32e7f482c4e881ad714db094a`, start
`076c01658f36f38cb9c8b5a3b4b098d774767616`, with all A-G claims PASS. The
auditor independently re-ran the exact selected gate and tests: **277** selected
Python tests and **285** selected Node tests passed; the worktree remained
clean, HEAD stayed at the candidate, the whole diff was exactly the nine paths
(739 insertions, 51 deletions) and the correction diff exactly seven paths (74
insertions, 223 deletions). No API, authorization, payload, schema, migration,
extension-production or companion-protocol change was found. Rendered geometry,
native picker, Brave iframe/modal, scrolling, clipping, focus, contrast, upload
timing and assistive-technology output remain the Cooperator's rendered
re-acceptance.

The auditor marked `Primary fresh acceptances used: 1`, recording consumption of
the re-acceptance budget by this report. No correction is required.

Re-acceptance disposition: **accepted**. The candidate is ready for publication,
NUC deployment and the Cooperator's rendered re-acceptance of unconditional
start without a checkbox or Start control.

## Publication and deployment status — 2026-11-10

Publication PASS. The accepted candidate was pushed normally:
`076c016..0a96fc1` on `main`, no force. Direct `git ls-remote` readback
returned `0a96fc18b49191a32e7f482c4e881ad714db094a`; local HEAD and
`origin/main` match; the worktree is clean.

NUC deployment is blocked by reachability, not by authorization. The canonical
worker gate probe reports the SSH agent ready, but two bounded connections to
`framenest-nuc.tail247768.ts.net:22` timed out (`Operation timed out`, exit 255)
before any sudo probe. The NUC is therefore still expected to be at
`076c01658f36f38cb9c8b5a3b4b098d774767616`, the last successful release. No
deployment, status check or rendered acceptance can proceed until the host and
Tailscale path are reachable again. The next step is for the Cooperator to
restore NUC reachability; deployment and rendered re-acceptance follow.

## Deployment — 2026-11-10

The Cooperator restored NUC reachability and refreshed the sudo timestamp. The
canonical helper completed the routine deployment at
`0a96fc18b49191a32e7f482c4e881ad714db094a` with exit 0. Post-deploy `status`
reports `layout: canonical`, `active_release` and `web_release`
`0a96fc18b49191a32e7f482c4e881ad714db094a`, `capture_release`
`5b86d896b3ea03f89fef2c90f7af2c121d0ef915`, `service_active: active`,
`database_revision: 0035` and `backup_restore_readiness: ready`. Bounded
read-only checks of the deployed shell report zero `upload-auto-start-input`,
zero `upload-start-button`, zero `uploadAutoStart` and the expected
`uploadDialogIsOpen` guard; the checkbox and Start control are gone from the
release.

Terminal `sudo -K` was run; a following `sudo -n true` requires a password. The
Cooperator's rendered re-acceptance of unconditional start remains the only
pending closure input. It covers the removed controls, picker/drop auto-start,
progress/terminal state, replacement lock, duplicate review/privacy,
pause/resume/cancel, reopen, explicit recovered Resume, companion `open_upload`,
narrow layout and adjacent views.

## Rendered PASS and post-acceptance cover UX correction — 2026-11-10

The Cooperator rendered the deployed `0a96fc1` upload flow and declared it
**PASS**: the checkbox and Start control are gone, picker and drop start
automatically, progress/terminal state, replacement lock, duplicate behavior,
pause/resume/cancel, reopen, companion `open_upload` and the narrow layout are
accepted. Whole 02's upload-flow result is production-accepted at `0a96fc1`.

During the same rendered session he found a separate cover-authoring UX issue.
He explicitly directed a bounded correction, not a new planning whole:

- the media-details window must not show **Choose cover**; move it to the Edit
  window next to **Analyze by AI**;
- the **Analyze by AI** icon is invisible; use a **brain** emoji;
- **Choose cover** uses the Analyze-by-AI treatment but with a slightly grey,
  not pure-white, surface;
- in the Choose cover dialog, remove the **Preview frame** button; show the
  first frame when the dialog opens and load the selected frame automatically
  after the slider is released (and after the ±250 ms steps);
- keep explicit **Set as cover**, the accepted-cover semantics, the timeline
  readout and the existing API/authorization boundary unchanged.

This is a Cooperator-directed post-acceptance scope extension, not a second
semantic owner and not a new logical whole. Bounded prompt `07_correction_00.md`
is prepared for fresh Worker session `07`, exchange `01`, baseline `0a96fc1`,
with the six-path UI/test allowlist and report `07_report_00.md`. Orchestrator
verification plus the Cooperator's rendered cover check follow; the whole stays
active until that PASS.

## Cover correction reconciliation — 2026-11-10

`07_report_00.md` is present and was read back in full. It is a terminal
**implementation-PASS** report for local candidate
`e64f2b0f92458fac2590e03672e30da62275b345`, parent
`0a96fc18b49191a32e7f482c4e881ad714db094a`, changing exactly the six
allowlisted paths (205 insertions, 48 deletions). Public `main` remains
`0a96fc1`; the candidate is local and unpushed; the worktree is clean.

The Orchestrator inspected the diff: the details footer keeps only Edit; the
metadata footer has `#metadata-choose-cover` after Analyze by AI and before
Cancel; the handler opens the cover dialog from `metadataWorkspace.openItem`;
the Analyze icon is 🧠; Choose cover is grey (`#c9d1c9`, hover `#d7ded7`) with
readable focus; the Preview-frame button, its listener and the primary cover
CSS are gone; the cover timeline now requests the first frame on open and the
selected frame on slider release and on the ±250 ms steps; preview tokens,
abort handling, unsaved-until-Set-as-cover wording and explicit Set as cover
remain. No API, authorization, payload, schema, migration, storage or
cover-accept semantics changed.

The Orchestrator independently re-ran the exact selected evidence:
`ap project check --baseline 0a96fc1` PASS, the selected Python suite **222
passed**, and the selected Node suite **75 passed with 1 skipped** (the gated
real-browser evidence test). `git diff --check` is clean and the worktree is
clean.

Correction disposition: **accepted for Cooperator rendered verification**. This
is a presentation-only correction with no security-boundary or evidence-
authority change, so the low-risk continuous-closure route applies; no separate
E2 audit is required. Publication, NUC refresh and the Cooperator's rendered
cover check follow. The whole remains active until that PASS.

## Cover publication — 2026-11-10

Publication PASS. The accepted cover correction was pushed normally:
`0a96fc1..e64f2b0` on `main`, no force. Direct `git ls-remote` readback
returned `e64f2b0f92458fac2590e03672e30da62275b345`; local HEAD and
`origin/main` match; the worktree is clean.

NUC deployment is pending a fresh Cooperator sudo authorization. The canonical
`sudo -n true` probe requires a password, so the NUC remains at
`0a96fc18b49191a32e7f482c4e881ad714db094a`. Once the timestamp is refreshed
outside the Worker, the canonical helper deployment and the Cooperator's
rendered cover check follow.

## Cover deployment — 2026-11-10

The Cooperator refreshed the sudo timestamp and the canonical helper completed
the routine deployment at
`e64f2b0f92458fac2590e03672e30da62275b345` with exit 0. Post-deploy `status`
reports `layout: canonical`, `active_release` and `web_release`
`e64f2b0f92458fac2590e03672e30da62275b345`, `capture_release`
`5b86d896b3ea03f89fef2c90f7af2c121d0ef915`, `service_active: active`,
`database_revision: 0035` and `backup_restore_readiness: ready`. Bounded
read-only checks of the deployed shell report one `metadata-choose-cover`, zero
`media-details-choose-cover`, zero `cover-preview-button` and six
`metadataChooseCoverButton` bindings.

Terminal `sudo -K` was run; a following `sudo -n true` requires a password. The
Cooperator's rendered cover check remains the final closure input.

## Rendered cover PASS and closure — 2026-11-10

The COOPERATOR rendered the deployed `e64f2b0` cover flow and declared **PASS**:
Choose cover is in the Edit footer and absent from Details; the Analyze by AI
button shows a visible brain icon; Choose cover uses the slightly grey
Analyze-style treatment; the Preview frame button is gone; the first frame
appears on open; the slider release and `±250 ms` steps load the selected frame;
Set as cover and replace confirmation work; the Gallery cover updates and the
narrow layout is usable. Combined with the upload-flow PASS at `0a96fc1`, the
whole's rendered acceptance is satisfied.

```text
Phase-qualified result: production-acceptance-PASS (Cooperator-declared)
Result artifact or commit: e64f2b0f92458fac2590e03672e30da62275b345
Result evidence: Cooperator rendered PASS for the upload flow at 0a96fc1 and
  the cover UX at e64f2b0; E2 acceptance-PASS at 0a96fc1; cover correction
  implementation-PASS and Orchestrator verification at e64f2b0;
  publication-PASS and NUC deployment-PASS at e64f2b0 with active/web e64f2b0,
  service active, database revision 0035 and backup restore-readiness ready
Required preceding results: satisfied
Cooperator-owned decisions: satisfied — upload-flow and cover rendered
  acceptance; the cover correction was directed as a bounded post-acceptance
  scope extension, not a new logical whole, so no separate E2 audit was required
Residual-risk disposition: satisfied — the gated real-browser evidence test was
  skipped, but the Cooperator's rendered cover PASS covers the changed UI; no
  medium or higher residual
Upgrade-ledger reconciliation: complete — entry
  consumer-declared-execution-and-capability-route-binding remains accepted,
  non-authorizing, retain-active; no ledger mutation
Active mutation: none
Closure actor: ORCHESTRATOR
Logical-whole closure: closed-by-ORCHESTRATOR
```

These notes are frozen at closure. The run map remains open for the Cooperator's
later selection among the provisional entries; the deferred AP Playwright MCP
whole remains a separate record.
