# Companion-hosted Timeline and My contributions — compact readable layout

## Routing and authority

Persistent role identity: WORKER
Logical whole identity: companion-download-notifications
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: COMPACT-COMPANION-TIMELINE-CONTRIBUTIONS-01
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — companion-hosted responsive layout, filter disclosure, accessibility and test churn
Recommended context capacity: approximately 250k tokens
Implementation authority: explicit
Exact baseline: b5436029c66da69c1d14c0f378cbea07bdc74a40
Changed-path allowlist: exactly these 10 paths and no others: `src/kronika/adapters/api/web/index.html`; `src/kronika/adapters/api/web/app.js`; `src/kronika/adapters/api/web/styles.css`; `tests/kronika_ui.test.js`; `tests/workspace_media_frontend.test.js`; `tests/contract/test_local_web_application.py`; `docs/X_COMPANION.md`; `SPEC.md`; `PRODUCT.md`; `DEVELOPMENT.md`
Implementation boundaries: companion-hosted Timeline text/filters/title layout and My contributions title wrapping, with the matching tests and documentation only
Independence required: no
Evidence posture: non-independent

This is a genuinely fresh correction session. You did not implement the candidate or its earlier corrections. Establish the repository and code evidence independently. The correction is a Cooperator-directed closeout of the same whole, not a new feature objective.

## Why this correction exists

The download block at `b543602` passed its independent acceptance and its rendered click/read/order checks. The COOPERATOR then rendered the companion-hosted shell and returned item 8 FAIL with item 10 explicitly refusing a separate logical whole:

- In the companion-hosted Timeline, the visibility/status emoji stack must go; the status/visibility text must be readable and the title must not be cut off. The panel needs the text, not emoji-only signals.
- The four Timeline filters (Publication, Kind, Status, Visibility) must be hidden behind one **Filter** button in the companion; clicking it expands the complete filtering. The companion should be compact.
- The My contributions page renders the title as one character per line at the companion width; it must use the full row width and wrap normally.
- Fix all of these here. Do not create a separate logical whole.

The COOPERATOR's instruction supersedes the earlier plan's "no web-shell implementation change" exclusion for this bounded companion-rendered UI closeout only. The download block, its privacy, badge, protocol and failure behavior remain unchanged. The YouTube acquisition `INSPECTION_OUTPUT_LIMIT` residual and the full-page layout outside the companion remain separate and are not part of this correction.

## Current truth

Repository: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Expected HEAD: b5436029c66da69c1d14c0f378cbea07bdc74a40
Expected parent: 647e6da11416559f1bef52d53e9743acbd2bb688
Expected grandparent: cc8f67965213ee9b22d113cc200776c42f6503ba
Expected great-grandparent: e64f2b0f92458fac2590e03672e30da62275b345
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50 at `/Users/agile/Projects/kronika/.ap`
Public `main`: `b543602` (Orchestrator observation; no network).
Worktree: clean, local `main` equal to `origin/main`.

The companion-hosted shell is the served web application inside the extension side panel. `app.js` adds the `kronika-companion-hosted` class to the root when hosted. Use that class as the companion trigger; do not change the wide/full-page Timeline or My contributions behavior except where a shared rule is strictly necessary.

Read at least:

- `src/kronika/adapters/api/web/index.html` — Timeline, filters, My contributions.
- `src/kronika/adapters/api/web/app.js` — `kronikaRenderChronicle`, `kronikaChronicleSignal`, `kronikaChronicleLabeled`, `kronikaBindShell`, the companion-hosted class, and the My contributions rendering.
- `src/kronika/adapters/api/web/styles.css` — chronicle grid, narrow rules, filter panel, `admin-media-row`, companion-hosted section.
- `src/kronika/adapters/api/web/companion_host.js` — the hosted protocol/class context.
- `tests/kronika_ui.test.js` — Timeline chronicle/filter tests.
- `tests/workspace_media_frontend.test.js` — My contributions frontend tests.
- `tests/contract/test_local_web_application.py` — served-shell/filter/CSS contract.
- `docs/X_COMPANION.md`, `SPEC.md`, `PRODUCT.md`, `DEVELOPMENT.md`.
- `05_report_00.md` and `00_notes.md` for the rendered-feedback context.

## Required behavior

### 1. Companion Timeline text

In the companion-hosted shell only:

- Hide the status and visibility glyph emojis. Do not replace them with another emoji.
- Show readable text for Kind, Status and Visibility. The status/visibility captions must be visible text, not only a tooltip or visually hidden text. Include the labels (`Kind`, `Status`, `Visibility`) so the meaning is clear.
- Do not clip the title. Remove the two-line clamp in the companion-hosted card so the full title wraps; allow the card to grow. The text must not be cut horizontally or vertically.
- Keep the card compact: a wrapped text metadata area is acceptable; no giant empty columns and no emoji-only rows.
- The wide/full-page Timeline keeps its existing table/glyph behavior.

The existing `kronikaChronicleSignal` builds a glyph plus a visually hidden caption. Extend or replace it so the companion-hosted rendering can show a label and value as text. The kind label already has the `kronika-chronicle__label` pattern; reuse that pattern for status and visibility where practical. The existing accessible name/title must remain truthful.

### 2. Companion Filter disclosure

- Add one **Filter** button in the Timeline section before `#kronika-timeline-filters`.
- It is visible in the companion-hosted shell. At wide/full-page sizes it is hidden and the filters remain visible as today.
- In the companion, the four filters are collapsed by default. Clicking Filter expands the complete `#kronika-timeline-filters` form; clicking again collapses it.
- The button is a real `type="button"` control with `aria-controls="kronika-timeline-filters"`, `aria-expanded` kept in sync, an accessible name `Filter`, and keyboard operation.
- The filter form, its four menus, their labels, values, listboxes, keyboard behavior and query behavior remain unchanged. Do not add a second filter system or change filtering semantics.
- Use an explicit class such as `is-collapsed` on the form for the collapsed state; the wide/full page must ignore it and keep the form visible.
- The compact panel should look deliberate: a compact Filter button and the expanded filters beneath it, using existing theme tokens.

### 3. Companion My contributions

In the companion-hosted shell only:

- The My contributions row must use the available width. The title must wrap at words and normal spaces, never one character per line.
- The title control must fill the row width (for example `display: block; width: 100%` in the companion-hosted narrow rule) while remaining a valid button/link and keeping its accessible name.
- The thumbnail, metadata, badges and actions remain readable in the single-column companion row. Do not hide required information.
- The wide/full-page My contributions layout remains unchanged.

### 4. Tests and documentation

Update or add tests that prove:

- The Filter button exists, has the right `aria-controls`/initial `aria-expanded`, is visible only under the companion-hosted rule, and toggles the form's collapsed class/`aria-expanded` without changing filter query behavior.
- The companion-hosted Timeline hides the status/visibility glyphs, shows the status/visibility text labels/values, and removes the title clamp; the wide page retains the existing glyph/table behavior.
- The companion-hosted My contributions title uses full-width normal wrapping; the wide page remains unchanged.
- Existing Timeline filter, chronicle, navigation, search and My contributions tests are updated only where the intentional markup/CSS change requires it; no unrelated behavior regresses.

Update:

- `docs/X_COMPANION.md` — companion-hosted Timeline text, no status/visibility emoji, Filter disclosure, full title wrapping and My contributions readable title.
- `SPEC.md` — add the normative companion-hosted Timeline/My contributions compact behavior at the existing Timeline/companion owner; keep the wide-page behavior and ADR-0088 Timeline model intact.
- `PRODUCT.md` — record the user-visible compact companion behavior.
- `DEVELOPMENT.md` — add the rendered acceptance checks for the compact companion Timeline, Filter disclosure and My contributions.
- Do not edit `README.md`, `ROADMAP.md`, `SERVER.md`, `docs/UX_AUDIT.md`, or any ADR body. No new ADR is expected; if you believe a durable contract change is required, stop and report.

## Repository and route

Verify before acting:

- `git -C /Users/agile/Projects/kronika status --porcelain=v1 -b` is clean and reports `## main...origin/main`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD` equals `b543602`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^` equals `647e6da`;
- `git -C /Users/agile/Projects/kronika/.ap rev-parse HEAD` equals the governing AP pin;
- no untracked files.

If the gate fails, classify with RF-12 and stop. Do not fetch, repair, reset, clean, checkout or stash.

## Trace and delivery

External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/01/03-companion-download-notifications
Trace project key: kronika
Trace logical-whole projection identity: companion-download-notifications
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 06_correction_00.md
Destination path: /Users/agile/meta/projects/kronika/01/03-companion-download-notifications
Report filename: 06_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: only the 10 allowlisted repository paths (the actual changed subset)
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/03-companion-download-notifications/06_report_00.md

## Authority

Positive authority: read-only inspection of the repository, the accepted plan and reports, and this prompt at `/Users/agile/meta/projects/kronika/01/03-companion-download-notifications/06_correction_00.md`; modify exactly the 10 allowlisted paths; run the selected AP, Python and Node checks below; check the exact report destination; create exactly one local commit on `main` on top of `b543602`; and create/read back `06_report_00.md`.

Commands: `./.ap/ap project check`, `./.ap/ap exec` with the exact baseline and declared operations, `node --test` with the selected suites, read-only Git inspection, exact-path `git add`, one local `git commit`, and the native file writer for the exact report path. Do not invoke raw `.venv/bin/python`, `python`, `python3` or `poetry run`.

Git authority: one local commit on `main` on top of `b543602`, subject `fix: compact the companion timeline and contributions layout`. Stage exactly the 10 allowlisted paths; never `git add .` or `git add -A`. No fetch, push, force, amend, reset, clean, stash, checkout, switch, tag or remote change.

Network authority: none. Secret authority: none. Do not read `private/`, `.venv`, credentials, browser profiles, cookies or unrelated paths.

Negative authority: any change outside the 10 allowlisted paths; any extension, manifest, permission, route, schema, migration, acquisition or download-block change; any full-page desktop redesign; any push, publication, deployment, full suite, browser run, NUC access, provider call or secret access; any edit to the plan, reports, notes, handout, `02_rereport_00.md` or the run map; any acceptance or closure claim.

## Validation

Run the focused checks first:

```text
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline b5436029c66da69c1d14c0f378cbea07bdc74a40
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline b5436029c66da69c1d14c0f378cbea07bdc74a40 --operation runtime-info
node --test tests/kronika_ui.test.js tests/workspace_media_frontend.test.js
```

Then the affected frontend selection from `DEVELOPMENT.md`:

```text
node --test tests/upload_cockpit_async_ownership.test.js tests/companion_web_bridge.test.js tests/x_companion_extension.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js tests/kronika_ui.test.js tests/gallery_search_tag_filters.test.js tests/automatic_analysis_lifecycle.test.js tests/cover_frontend.test.js
```

Run the focused Python contract check for the served shell:

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline b5436029c66da69c1d14c0f378cbea07bdc74a40 --operation test-focus -- tests/contract/test_local_web_application.py -q -p no:cacheprovider
```

Run `git diff --check`, `git status --porcelain=v1`, inspect the exact diff and verify the committed path list is the exact changed subset of the 10-path allowlist, with no path outside it. Do not run a full suite, browser evidence, real acquisition, provider calls or NUC commands.

## Report contract

Write the terminal report to `06_report_00.md`. Begin it exactly with:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three exchange coordinates exactly once (`06`/`01`). Include the Cooperator's item 8/10 amendment, the exact change, the new and updated tests, the test commands and counts, the new commit SHA and parent, the staged and committed path lists, and Orchestration critique with MEASURED and LEAD findings or none. Use `Phase-qualified result: implementation-PASS` only if the correction and all selected checks pass; otherwise `PARTIAL` or `BLOCKED` with exact evidence. Use `Logical-whole closure: not-closed` and `Report justification: new-mutation`.

Direct-write the report, read it all back, verify content, path and SHA-256, and only then send a short separate completion notice. If the report path already exists, including an empty file, stop and report the collision. If the client blocks the exact write, return the complete report and state `File delivery: pending client restriction`.

Do not claim acceptance, publication, deployment or closure. A fresh independent full re-acceptance follows.

## Stopping conditions

Stop and report the exact blocker if:

- the repository identity, branch, baseline, parent, worktree or `.ap` gate fails;
- a required change falls outside the 10-path allowlist;
- a selected test fails for a reason outside this correction;
- the compact behavior cannot be achieved without changing the wide/full-page layout or the filter query semantics;
- a durable contract change or new ADR appears necessary;
- the report path already exists or its parent/symlink resolution is unsafe;
- the client cannot write the report or run a required command;
- secrets, private data, browser state or another ungranted effect would be touched.

After a prerequisite stop, only report preparation and necessary cleanup inside this grant may finish. Preserve the first causal failure.

## Authority expiry

This grant expires at the terminal correction report, cancellation or supersession. Retained context, a green test run, the local commit or a later conversation is not acceptance or closure authority.
