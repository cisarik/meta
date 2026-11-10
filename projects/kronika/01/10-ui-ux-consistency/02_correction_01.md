# Authoritative Worker prompt — Kronika whole 10, Worker session 02, exchange 02

Activation: this file is the exact issued Worker prompt for the logical whole
`ui-ux-consistency`. It is stored under the Meta filename mapping
`<worker-session>_<phase>_<meta-exchange-index>.md` as
`02_correction_01.md`. The matching terminal report is `02_report_01.md`.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: ui-ux-consistency
Worker session ordinal: 02
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded UI Polish Worker
Phase: Correction
Task identity: KRN-UX-CORR-02 — header search consistency, Timeline trim and History removal
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — one bounded but broad shell correction across navigation, header search, Timeline presentation, History removal and durable documentation
Recommended context capacity: approximately 250k tokens
Independence required: no
Continuity anchor: terminal implementation-PASS report 02_report_00.md and the current public candidate bbf776c462e1eb5eccb91eb027a85eee9055d2ec
Authority renewal: prior implementation authority expired; this prompt grants a new bounded rendered-acceptance correction
Evidence posture: non-independent correction; a fresh independent E2 re-acceptance follows
```

You are continuing the healthy same Worker session that implemented whole 10 at
`bbf776c462e1eb5eccb91eb027a85eee9055d2ec`. The prior authority expired. This
prompt grants a new, complete, bounded correction. Retained context is
convenience, not authority; re-gate the repository and stop on any conflict.

Before substantive work, confirm that `Native planning mode: not-used` is the
actual client state (native Plan mode OFF). If it is enabled, stop and return
`BLOCKED` naming the contradiction.

## 1. Cooperator's rendered findings

The Cooperator tested the deployed `bbf776c` shell and declared the implemented
grouping/search/filter/listbox/link/glyph changes PASS, then requested three
further consistency changes:

1. **Timeline search belongs in the header toolbar, not the filter row.** It
   currently sits beside Publication/Kind/Status/Visibility and the page
   composition changes when moving between Gallery and Timeline. Put the
   Timeline search in the same header-toolbar position as Gallery search, with
   no layout jump between views.
2. **Remove the Timeline hero/lede/note.** The visible `🕰️ Timeline`, "Everything
   you can access in Kronika — newest first." and "Household sharing does not
   publish to the internet." block is redundant; Gallery has no equivalent.
   Trim it radically and consistently. Keep only a visually hidden heading if
   needed for focus/accessibility.
3. **Remove History entirely.** The Timeline already contains search/research
   history, so the separate History tab and page are redundant. Remove the
   History tab and page; the left browsing group becomes only Timeline and
   Gallery. `#/history` and `#/history/records` must resolve to the Timeline, not
   a dead route. Search/Research/Review actions remain.

This Cooperator decision explicitly supersedes the accepted plan's decision to
preserve personal History as a separate view. It does not remove the question/
answer data model or any API; it removes the separate UI view and updates the
durable truth.

## 2. Exact required behavior

### 2.1 Header search consistency

- Move the Timeline search out of `#kronika-timeline-filters` into the header
  toolbar, in the same slot/position as the Gallery `.header-search` field.
- Both fields share the same visual chrome and occupy the same header slot; only
  the active view's field is visible. Switching Timeline ↔ Gallery must not move
  or resize the search slot or the top-right controls.
- Preserve each view's semantics: Gallery keeps its title/tag suggestions,
  debounce, clear and catalog controller; Timeline keeps explicit submit,
  trim/offset reset, filter preservation, clear, focused-draft protection and
  same-hash reload. Do not share query/tag state or controllers.
- Hide the header search on views that have no search (Search/Research/Review/
  request/record/details); the top-right status controls remain.
- The Timeline filter bar now contains only Publication, Kind, Status and
  Visibility, with Publication first and the existing green-border emphasis;
  Kind/Status/Visibility align with the list columns.
- On narrow screens the search remains in the header toolbar (or its responsive
  header row) consistently for both views; no horizontal page overflow.

### 2.2 Timeline trim

- Remove the visible Timeline hero, lede and note block.
- Keep a visually hidden `h1`/heading (`#kronika-timeline-heading`, tabindex
  `-1`) if route focus/accessibility needs it; do not show a visible hero.
- The Timeline content starts with the header search and filter toolbar, then
  the status/list/pager. Preserve focus, labels, list behavior and the existing
  visual language.

### 2.3 Remove History

- Remove the History nav anchor from `.kronika-nav__browse`; the browsing group
  is Timeline and Gallery only. Search/Research/Review actions remain.
- Remove the `#kronika-history` section, its heading/status/header/list/pager/
  retry markup, CSS, JS loading/render/route state and tests. Remove dead
  `historyMode`, `questions`/`records` list state only where no other caller
  uses it; do not remove the question/answer API or data model.
- `#/history` and `#/history/records` must resolve to the Timeline route (hash
  replaced with `#/timeline` or equivalent) instead of a missing view. Update
  every `#/history` link (for example the question view's "Past answers") to the
  Timeline or remove it.
- The Timeline's complete chronicle remains the place where saved and unfinished
  search/research items appear. Do not add a new History view or second list.

### 2.4 Durable documentation and decision

The separate History view is a product/architecture decision, not only CSS.
Update the current owners that name it:

- create the next free ADR (expected `0088`) recording that the separate History
  view is removed, Timeline is the single authorized overview, Search/Research
  remain actions, personal question/answer data and APIs remain, Gallery remains
  separate, and the removed-view parts of ADR-0083/ADR-0087 are superseded;
- update `docs/adr/README.md` with the new ADR;
- update `AGENTS.md`, `PRODUCT.md`, `SPEC.md`, `SECURITY.md`, `SERVER.md`,
  `ROADMAP.md`, `README.md`, `GALLERY.md` and `DEVELOPMENT.md` only where they
  currently state or imply the removed separate History view; preserve privacy,
  authorization, API, provider and Gallery/Details claims;
- do not edit accepted ADR-0082 through ADR-0087 bodies;
- do not create a second semantic owner.

## 3. Allowlist and negative scope

Change only these paths, and only where needed:

```text
src/kronika/adapters/api/web/index.html
src/kronika/adapters/api/web/app.js
src/kronika/adapters/api/web/styles.css
tests/kronika_ui.test.js
tests/gallery_search_tag_filters.test.js
tests/contract/test_local_web_application.py
AGENTS.md
README.md
PRODUCT.md
SPEC.md
SECURITY.md
SERVER.md
ROADMAP.md
GALLERY.md
DEVELOPMENT.md
docs/adr/0088-timeline-as-single-overview.md   (new; use the next free number if 0088 is unavailable)
docs/adr/README.md
```

If a listed document does not need a change, leave it unchanged. Negative
allowlist: no API, repository, domain, application service, persistence,
authorization/capability/route-policy, schema, migration, public composition,
preview route, Gallery/Details renderer, provider, capture, companion,
dependency, asset, font, network, deployment or host change. No other path. No
new file except the ADR. If a required change falls outside the allowlist, stop
and report.

## 4. Baseline, allowlist and gate

```text
Repository: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Expected branch: main
Baseline commit under test: bbf776c462e1eb5eccb91eb027a85eee9055d2ec
Parent of the correction commit: bbf776c462e1eb5eccb91eb027a85eee9055d2ec
Public main: bbf776c462e1eb5eccb91eb027a85eee9055d2ec
Containing-repository .ap gitlink: d7023cf037f6d17885c3ede5c04812c61640da50
Submodule HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
```

Verify before editing:

```text
git rev-parse HEAD
git status --short
git log --oneline -2
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline bbf776c462e1eb5eccb91eb027a85eee9055d2ec
```

Stop if the worktree is not clean or HEAD is not `bbf776c`.

## 5. Tests and validation

Run from `/Users/agile/Projects/kronika`:

```text
# [MacBook / fish]
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline bbf776c462e1eb5eccb91eb027a85eee9055d2ec
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline bbf776c462e1eb5eccb91eb027a85eee9055d2ec --operation test-focus -- tests/contract/test_local_web_application.py -q -p no:cacheprovider
node --test tests/kronika_ui.test.js tests/gallery_search_tag_filters.test.js tests/gallery_filter_controls.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js
git diff --check
git status --short
#------------------------------------------------------
```

Update/add causal tests for:

- one browse group with Timeline and Gallery only; no History anchor/section;
- header search slot consistent between Timeline and Gallery, with each view's
  semantics preserved and the other field hidden;
- Timeline filter bar without search, Publication first and aligned fields;
- no visible Timeline hero/lede/note; hidden heading/focus preserved;
- `#/history` and `#/history/records` fold to Timeline; no stale history links;
- no `/api/research-requests` History-list fetch from the removed view; Timeline
  still shows saved/unfinished search/research items;
- ADR/docs current, no API/authorization/payload/schema change;
- existing preview, listbox, underline, glyph, Gallery/Details and retry tests
  remain green.

Do not run the full Python suite. Classify pre-existing failures with evidence;
do not repair unrelated behavior. Rendered 320/390 px and subjective acceptance
remain the Cooperator's after a later deployment.

## 6. Authority

```text
Positive authority: edit exactly the allowlisted paths; read-only inspection of
  the repository, the accepted plan, implementation/acceptance reports, current
  shell source and this whole's Meta notes; run the exact gate and tests above;
  stage exactly the changed allowlisted paths and create exactly one normal
  corrective local commit on main; exact direct-write of the terminal report
  below if it is absent, followed by a complete readback.

Negative authority: any other file edit, creation, deletion or rename; any API,
  repository, domain, application, persistence, audience, route-inventory,
  schema, migration, public-composition, preview-route, Gallery/Details,
  provider, capture, companion, dependency, asset, font, network, deployment or
  host change; any accepted ADR body edit; any Git push, fetch, pull, merge,
  rebase, reset, restore, clean, stash, checkout, switch, branch, tag, remote,
  config write or amend; any NUC, SSH, sudo, deploy, browser, provider, secret
  or private-media access; any acceptance, publication, deployment or closure
  claim.

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
git commit -m "fix: finish Timeline and header consistency"
git show --stat --oneline HEAD
```

Do not push. Report the commit SHA and its parent.

Write the terminal report to:

```text
/Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/02_report_01.md
```

The report starts exactly with `### Report for ORCHESTRATOR_CHAT`, echoes the
coordinates and role fields, and contains:

```text
status: PASS
Phase-qualified result: implementation-PASS
Start commit: bbf776c462e1eb5eccb91eb027a85eee9055d2ec
End commit: <correction commit SHA>
Report justification: new-mutation
Logical-whole closure: not-closed
```

Include the three Cooperator findings, the exact shell/search/Timeline/History
changes, the new ADR and doc updates, the changed paths and diff stat, gate and
test commands with actual counts, new/updated test identities, any deviation or
residual risk, `Resolved Execution Issues / Near-Misses`, `Pre-Existing Failure
Classification`, one smallest next step, and the orchestration critique. Do not
claim acceptance, publication, deployment or closure.

## 8. Delivery and trace

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/
Trace project key: kronika
Trace logical-whole projection identity: 10-ui-ux-consistency
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_correction_01.md
Destination path: /Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/
Report filename: 02_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: exactly the changed allowlisted paths
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/02_report_01.md
```

If the report path exists, including an empty file, stop `BLOCKED` without
overwriting it.

## Visible delivery capsule

```text
🟡 Ready for delivery
Recipient: Bounded UI Polish Worker · current-worker-session · manual
Recommendation: High · approximately 250k tokens
Client: Native Plan Mode OFF
Prompt: /Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/02_correction_01.md
Report: /Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/02_report_01.md
Archival: wait-for-report
```
