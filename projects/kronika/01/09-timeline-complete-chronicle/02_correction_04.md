# Authoritative Worker prompt — Kronika whole 09, Worker session 02, exchange 05

Activation: this file is the exact issued Worker prompt for the logical whole
`timeline-complete-chronicle`. It is stored under the Meta filename mapping
`<worker-session>_<phase>_<meta-exchange-index>.md` as
`02_correction_04.md`. The matching terminal report is `02_report_04.md`.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: timeline-complete-chronicle
Worker session ordinal: 02
Worker exchange ordinal: 05
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded UI Polish Worker
Phase: Correction
Task identity: KRN-TCC-UI-04 — Timeline eye-candy polish: custom filter dropdowns, remove Added, emoji status/visibility, subtle hover motion
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — visual and interaction design across the main page, with accessibility and test-pin risk
Recommended context capacity: approximately 250k tokens
Independence required: no
Continuity anchor: terminal documentation correction report 02_report_03.md and public candidate commit 5be63b13b45a051ab76ad3c444ad769b11ff89cc
Authority renewal: prior implementation/correction authority expired; this prompt grants a new bounded UI polish correction
Evidence posture: non-independent correction; the Cooperator's rendered acceptance and a fresh independent re-acceptance follow
```

You are continuing the healthy same Worker session that produced the current
public candidate `5be63b13b45a051ab76ad3c444ad769b11ff89cc`. The prior authority
expired. This prompt grants a new, complete, bounded UI polish correction.
Retained context is convenience, not authority; re-gate the repository and stop
on any conflict with current evidence.

Before substantive work, confirm that `Native planning mode: not-used` is the
actual client state (native Plan mode OFF). If it is enabled, stop and return
`BLOCKED` naming the contradiction.

## 1. Cooperator's rendered findings

The Cooperator tested the deployed `5be63b1` Timeline and rejected the current
visual result as not user-friendly enough. The exact findings:

1. **The filter dropdowns look default and ugly.** The Kind, Status, Visibility
   and Publication controls are native `<select>` elements. The project already
   has custom Matrix-style menu/dropdown language in the shell (header menus,
   metadata suggestion list, tag suggestions). Reuse that language for the
   Timeline filters; if a suitable component does not exist, build one with the
   same visual and interaction quality. Do not add a dependency.
2. **The visible "Added" date is unwanted.** Rows show
   `Added 2026-11-08T19:31:12.823Z`. Remove the visible Added column, header cell
   and date from the Timeline. Keep the data for ordering; the UI must not show
   it. Give the freed horizontal space to the title.
3. **Status and visibility take too much text.** `Analysed` and
   `Private · Unpublished` should become compact emoji/icon indicators, with the
   accessible text preserved. Use emoji/icon vocabulary already present in the
   shell where it fits; if none fits, choose a small consistent set.
4. **The header is cramped.** The desktop header currently reads `PreviewItem`
   with no breathing room. Fix the header grid and column spacing so each label
   is clearly separated: Preview, Item, Kind, Status, Visibility (no Added).
5. **The page needs eye candy.** The Cooperator wants a genuinely user-friendly,
   attractive web app. Improve spacing, typography, filter-bar affordances, row
   separators, hover/focus states and dropdown styling within the existing dark
   green design. Add a quick, unobtrusive green hover/focus animation on rows —
   subtle, transparent/soft, not distracting, no layout shift, not a looping
   animation. The Worker may be creative inside the existing design language.
6. **Preserve behavior and privacy.** This is presentation and interaction
   polish. Do not change the API, authorization, visibility predicates, payload
   keys, route inventory, ordering, counts, pagination, preview behavior,
   Gallery/Details freeze, or the accepted ADR-0087 model.

## 2. Exact required behavior

### 2.1 Custom filter dropdowns

Replace the Timeline filter native selects with custom, accessible dropdowns for
Kind, Status, Visibility and Publication. Reuse the existing shell menu/dropdown
visual language and design tokens where suitable; if the existing components are
not reusable as selects, build a small Timeline-local custom dropdown without a
new dependency.

Required accessibility and interaction:

- a labelled trigger with `aria-haspopup="listbox"`/`listbox` or an equivalent
  correct pattern, `aria-expanded`, and a visible selected label/icon;
- keyboard open, arrow navigation, Enter/Space select, Escape close, outside
  click close, focus return to the trigger;
- visible focus, 44 px targets, no ARIA grid or custom arrow-key navigation
  beyond the dropdown itself;
- the selected value updates the existing route state and resets offset to zero;
- Search and Clear controls keep their existing behavior and layout;
- no native select popup remains visible.

### 2.2 Remove Added

Remove the Added header cell and the date from every Timeline row. Keep the
desktop grid aligned to Preview, Item, Kind, Status, Visibility. At 720 px and
below, the title gets the remaining width and the compact fields wrap under it
without a date row. Do not remove `created_at_ms` from the API or ordering code.

### 2.3 Emoji status and visibility

Use compact emoji/glyph indicators for status and visibility/publication. The
accessible name must remain explicit through `visually-hidden` text or
`aria-label`; do not use color or emoji alone. Cover the existing statuses
(unanalysed, in progress, analysed/complete, failed, cancelled) and the existing
visibility/publication states (private, household, unpublished, approved,
withdrawn, legacy publication) with a consistent small icon set. Use the
existing emoji vocabulary where it fits; the Worker may choose a coherent set
if none exists. Keep the glyphs small and legible on the dark background.

### 2.4 Hover/focus animation

Add a quick, subtle green hover/focus treatment on Timeline rows: for example a
soft green left accent, translucent background/glow or a small opacity/translate
transition. Keep it under roughly 200 ms, non-looping, transparent/soft, without
layout shift, and honor `prefers-reduced-motion`. Do not reuse Gallery card
hover transforms or large cover imagery.

### 2.5 General polish

Improve the filter bar, row spacing, typography, separators, selected/hover/focus
states and empty/loading/error presentation within the existing palette. The
Timeline must remain a compact list, not a Gallery grid. Do not add external
fonts, images, network requests or dependencies.

## 3. Allowlist and negative scope

Change only these paths, and only where needed:

```text
src/kronika/adapters/api/web/app.js
src/kronika/adapters/api/web/index.html
src/kronika/adapters/api/web/styles.css
tests/kronika_ui.test.js
tests/contract/test_local_web_application.py   (only if it pins the changed markup)
SPEC.md                                        (only if its normative Timeline UI text names Added or the text status presentation)
```

Negative allowlist: no API, repository, domain, audience, authorization, route,
schema, migration, public-composition, preview-route, Gallery/Details, ADR,
`SERVER.md`, `AGENTS.md`, `docs/KRONIKA_ACCESS_INVENTORY.md`, extension, deploy,
host or other documentation path. No new file. If a required change falls
outside the allowlist, stop and report.

## 4. Baseline and gate

```text
Repository: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Expected branch: main
Baseline commit under test: 5be63b13b45a051ab76ad3c444ad769b11ff89cc
Parent of the correction commit: 5be63b13b45a051ab76ad3c444ad769b11ff89cc
Public main: 5be63b13b45a051ab76ad3c444ad769b11ff89cc
Containing-repository .ap gitlink: d7023cf037f6d17885c3ede5c04812c61640da50
Submodule HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
```

Verify before editing:

```text
git rev-parse HEAD
git status --short
git log --oneline -2
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 5be63b13b45a051ab76ad3c444ad769b11ff89cc
```

Stop if the worktree is not clean or HEAD is not `5be63b1`.

## 5. Tests and validation

Run from `/Users/agile/Projects/kronika`:

```text
# [MacBook / fish]
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 5be63b13b45a051ab76ad3c444ad769b11ff89cc
node --test tests/kronika_ui.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 5be63b13b45a051ab76ad3c444ad769b11ff89cc --operation test-focus -- tests/contract/test_local_web_application.py -k 'kronika_shell or details or persistent_preview or initial_card or available_cards or gallery' -q -p no:cacheprovider
git diff --check
git status --short
#------------------------------------------------------
```

Add or update causal Node tests for:

- custom dropdown open/select/close, keyboard path, selected value and focus;
- no visible Added header/date and the title receives the space;
- emoji status/visibility with accessible text;
- header alignment and narrow layout rules;
- subtle hover animation and `prefers-reduced-motion`;
- preserved filter route state, Reset offset, preview, Retry, identity and
  pagination behavior.

Do not run the full Python suite. Do not weaken unrelated tests. Rendered
320/390 px and subjective eye-candy acceptance remain the Cooperator's after a
later deployment.

## 6. Authority

```text
Positive authority: edit exactly the allowlisted UI paths; read-only inspection
  of the repository, the accepted plan, ADR-0087, the reports, the current shell,
  existing menu/dropdown and emoji patterns, and this whole's Meta notes; run
  the exact gate and tests above; stage exactly the changed allowlisted paths and
  create exactly one normal UI polish local commit on main; exact direct-write
  of the terminal report below if it is absent, followed by a complete readback.

Negative authority: any other file edit, creation, deletion or rename; any API,
  repository, domain, audience, route, schema, migration, public-composition,
  preview-route, Gallery/Details, ADR, documentation outside the conditional
  SPEC edit, dependency, asset, font, network or host change; any Git push,
  fetch, pull, merge, rebase, reset, restore, clean, stash, checkout, switch,
  branch, tag, remote, config write or amend; any NUC, SSH, sudo, deploy,
  browser, provider, secret or private-media access; any acceptance, publication,
  deployment or closure claim.

Git authority: read-only inspection plus exactly one normal UI polish commit on
  main of the changed allowlisted paths; no push and no amend.
Network authority: none.
Secret authority: none.
```

## 7. Commit and report

After the selected tests pass and `git diff --check` is clean, stage exactly the
changed allowlisted paths and create one commit:

```text
git add -- <the changed allowlisted paths>
git diff --cached --check
git commit -m "feat: polish the Timeline chronicle presentation"
git show --stat --oneline HEAD
```

Do not push. Report the commit SHA and its parent.

Write the terminal report to:

```text
/Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_report_04.md
```

The report starts exactly with `### Report for ORCHESTRATOR_CHAT`, echoes the
coordinates and role fields, and contains:

```text
status: PASS
Phase-qualified result: implementation-PASS
Start commit: 5be63b13b45a051ab76ad3c444ad769b11ff89cc
End commit: <UI polish commit SHA>
Report justification: new-mutation
Logical-whole closure: not-closed
```

Include the Cooperator's findings, the exact design changes, the custom dropdown
behavior and accessibility, the removed Added field, the emoji/accessibility
mapping, the hover/motion behavior, the changed paths and diff stat, the gate
and test commands with actual counts, new/updated test identities, any deviation
or residual risk, `Resolved Execution Issues / Near-Misses`, `Pre-Existing
Failure Classification`, one smallest next step, and the orchestration critique.
Do not claim acceptance, publication, deployment or closure.

## 8. Delivery and trace

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/
Trace project key: kronika
Trace logical-whole projection identity: 09-timeline-complete-chronicle
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_correction_04.md
Destination path: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/
Report filename: 02_report_04.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: exactly the changed UI allowlisted paths
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_report_04.md
```

If the report path exists, including an empty file, stop `BLOCKED` without
overwriting it.

## Visible delivery capsule

```text
🟡 Ready for delivery
Recipient: Bounded UI Polish Worker · current-worker-session · manual
Recommendation: High · approximately 250k tokens
Client: Native Plan Mode OFF
Prompt: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_correction_04.md
Report: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_report_04.md
Archival: wait-for-report
```
