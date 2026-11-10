# Authoritative Worker prompt — Kronika whole 01, Worker session 02, exchange 03

Activation: this file is the exact issued Worker prompt for the logical whole
`timeline-and-history-media-thumbnails`. It is stored under the Meta filename
mapping `<worker-session>_<phase>_<meta-exchange-index>.md` as
`02_correction_02.md`. The matching terminal report is `02_report_02.md`.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: timeline-and-history-media-thumbnails
Worker session ordinal: 02
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded UI Polish Worker
Phase: Correction
Task identity: KRN-THT-UI-02 — History Questions-only Timeline-style list
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — one UI correction across the History surface, its markup, styles and Node contract
Recommended context capacity: approximately 250k tokens
Independence required: no
Continuity anchor: terminal correction report 02_report_01.md and the current public candidate 65772c6028c07edcab47b6928dbb31e30876c70a
Authority renewal: prior whole-01 authority expired; this prompt grants a new bounded UI polish correction
Evidence posture: non-independent correction; the Orchestrator verifies the diff and the Cooperator renders the result
```

You are continuing the healthy same Worker session that produced whole 01's
thumbnail implementation and its earlier correction. The prior authority
expired. This prompt grants a new, complete, bounded UI polish correction.
Retained context is convenience, not authority; re-gate the repository and stop
on any conflict with current evidence.

Before substantive work, confirm that `Native planning mode: not-used` is the
actual client state (native Plan mode OFF). If it is enabled, stop and return
`BLOCKED` naming the contradiction.

## 1. Cooperator's rendered finding

The Cooperator tested the deployed History view at `65772c6`. The **Questions**
and **Records** tabs show effectively the same personal items; the split is
duplicate and confusing. The current History cards are also visually
inconsistent with the new eye-candy Timeline chronicle list.

The Cooperator's exact direction:

- keep **only Questions**; remove the duplicate Records tab and its separate
  history view;
- present History as the **same compact table/list visual language as the new
  Timeline** — rows, header, separators, emoji status/visibility, subtle green
  hover/focus, generous question-text space;
- do not show a visible Added/created date in History rows; the question text
  is the priority;
- keep it user-friendly, consistent and attractive;
- do not reopen the Timeline design, Gallery/Details freeze, API, authorization
  or stored data.

## 2. Exact required behavior

### 2.1 Questions only

- Remove the History Questions/Records tab pair and the `#/history/records`
  view from the UI. The History page has one personal-question list.
- `#/history/records` must redirect to `#/history` (or otherwise resolve to the
  Questions view) instead of rendering a second list. Do not leave a dead link
  or an empty duplicate tab.
- The list uses the existing personal question/answer data already returned by
  the History request endpoint. Do not call the personal-record list for this
  view and do not add a new API.
- Keep the page heading and a short lede that describes personal questions,
  answers and saved records. Remove the now-redundant tab controls.

### 2.2 Timeline-style list

Use the current Timeline chronicle visual language, adapted for questions:

- a compact semantic ordered list with one row per question;
- a desktop header and per-field labels; header `aria-hidden` as in Timeline;
- question text is the primary flexible column, allowed to use the available
  width and up to two lines;
- fields: Question/Item, Kind (Search or Research), Status, Visibility or
  publication state; no media-preview column and no Added/created date;
- compact emoji/glyph status and visibility, with accessible text preserved via
  `visually-hidden`/`aria-label`/`title`; reuse the Timeline glyph vocabulary
  where it fits;
- a quick, subtle green hover/focus treatment consistent with Timeline, with
  `prefers-reduced-motion` respected and no layout shift;
- at 720 px and below, one row per question, question text gets the flexible
  space, and the compact fields wrap beneath it without horizontal page
  scrolling; 44 px interactive targets;
- links remain: saved record → existing record route; unfinished request →
  existing request route; no inline playback, approval, download or provider
  controls.

### 2.3 Preserve

- personal ownership and privacy: only the caller's questions and saved records;
- current request lifecycle states, labels, links, route state and focus;
- Timeline, Gallery, Details, previews and the closed whole 09 behavior;
- no API, repository, authorization, payload or schema change;
- no new dependency, font, image, network request or external asset.

## 3. Allowlist and negative scope

Change only these paths, and only where needed:

```text
src/kronika/adapters/api/web/app.js
src/kronika/adapters/api/web/index.html
src/kronika/adapters/api/web/styles.css
tests/kronika_ui.test.js
tests/contract/test_local_web_application.py   (only if it pins the changed History markup)
SPEC.md                                        (only if its normative History text names the removed Records tab or card layout)
```

Negative allowlist: no API, repository, domain, audience, authorization, route
inventory, schema, migration, public composition, preview route, Timeline,
Gallery/Details, ADR, `SERVER.md`, `AGENTS.md`, access inventory, extension,
deploy, host or other documentation path. No new file. If a required change
falls outside the allowlist, stop and report.

## 4. Baseline and gate

```text
Repository: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Expected branch: main
Baseline commit under test: 65772c6028c07edcab47b6928dbb31e30876c70a
Parent of the correction commit: 65772c6028c07edcab47b6928dbb31e30876c70a
Public main: 65772c6028c07edcab47b6928dbb31e30876c70a
Containing-repository .ap gitlink: d7023cf037f6d17885c3ede5c04812c61640da50
Submodule HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
```

Verify before editing:

```text
git rev-parse HEAD
git status --short
git log --oneline -2
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 65772c6028c07edcab47b6928dbb31e30876c70a
```

Stop if the worktree is not clean or HEAD is not `65772c6`.

## 5. Tests and validation

Run from `/Users/agile/Projects/kronika`:

```text
# [MacBook / fish]
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 65772c6028c07edcab47b6928dbb31e30876c70a
node --test tests/kronika_ui.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 65772c6028c07edcab47b6928dbb31e30876c70a --operation test-focus -- tests/contract/test_local_web_application.py -k 'kronika_shell or details or persistent_preview or initial_card or available_cards or gallery' -q -p no:cacheprovider
git diff --check
git status --short
#------------------------------------------------------
```

Add or update causal Node tests for:

- History has only the Questions view; `#/history/records` resolves to it;
- question rows use the compact chronicle list, header and per-field labels;
- no duplicate/my-records fetch from History;
- question text gets the flexible column and no Added date is rendered;
- emoji status/visibility with accessible text;
- hover/focus and reduced-motion rules;
- saved and unfinished links, identity, route state and focus remain.

Do not run the full Python suite. Do not weaken unrelated tests. Rendered
acceptance remains the Cooperator's after a later deployment.

## 6. Authority

```text
Positive authority: edit exactly the allowlisted UI paths; read-only inspection
  of the repository, the current Timeline/History shell, the reports and this
  whole's Meta notes; run the exact gate and tests above; stage exactly the
  changed allowlisted paths and create exactly one normal History UI correction
  commit on main; exact direct-write of the terminal report below if it is
  absent, followed by a complete readback.

Negative authority: any other file edit, creation, deletion or rename; any API,
  repository, domain, audience, route-inventory, schema, migration, public
  composition, preview route, Timeline, Gallery/Details, ADR, documentation
  outside the conditional SPEC edit, dependency, asset, font, network or host
  change; any Git push, fetch, pull, merge, rebase, reset, restore, clean,
  stash, checkout, switch, branch, tag, remote, config write or amend; any NUC,
  SSH, sudo, deploy, browser, provider, secret or private-media access; any
  acceptance, publication, deployment or closure claim.

Git authority: read-only inspection plus exactly one normal History UI
  correction commit on main of the changed allowlisted paths; no push and no
  amend.
Network authority: none.
Secret authority: none.
```

## 7. Commit and report

After the selected tests pass and `git diff --check` is clean, stage exactly the
changed allowlisted paths and create one commit:

```text
git add -- <the changed allowlisted paths>
git diff --cached --check
git commit -m "fix: make History a Questions-only chronicle list"
git show --stat --oneline HEAD
```

Do not push. Report the commit SHA and its parent.

Write the terminal report to:

```text
/Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/02_report_02.md
```

The report starts exactly with `### Report for ORCHESTRATOR_CHAT`, echoes the
coordinates and role fields, and contains:

```text
status: PASS
Phase-qualified result: implementation-PASS
Start commit: 65772c6028c07edcab47b6928dbb31e30876c70a
End commit: <History UI correction SHA>
Report justification: new-mutation
Logical-whole closure: not-closed
```

Include the Cooperator's finding, the exact design changes, the removed
Records view and redirect, the Questions-only list and its fields, the glyph and
accessibility mapping, the hover/motion behavior, the changed paths and diff
stat, gate and test commands with actual counts, new/updated test identities,
any deviation or residual risk, `Resolved Execution Issues / Near-Misses`,
`Pre-Existing Failure Classification`, one smallest next step, and the
orchestration critique. Do not claim acceptance, publication, deployment or
closure.

## 8. Delivery and trace

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/
Trace project key: kronika
Trace logical-whole projection identity: 01-timeline-and-history-media-thumbnails
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_correction_02.md
Destination path: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/
Report filename: 02_report_02.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: exactly the changed UI allowlisted paths
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/02_report_02.md
```

If the report path exists, including an empty file, stop `BLOCKED` without
overwriting it.

## Visible delivery capsule

```text
🟡 Ready for delivery
Recipient: Bounded UI Polish Worker · current-worker-session · manual
Recommendation: High · approximately 250k tokens
Client: Native Plan Mode OFF
Prompt: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/02_correction_02.md
Report: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/02_report_02.md
Archival: wait-for-report
```
