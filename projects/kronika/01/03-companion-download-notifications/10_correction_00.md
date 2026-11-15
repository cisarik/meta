# Companion history — one All and unread download rows

## Routing and authority

Persistent role identity: WORKER
Logical whole identity: companion-download-notifications
Worker session ordinal: 10
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: COMPANION-HISTORY-UNREAD-AND-SINGLE-ALL-01
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — companion history expansion, unread state, existing opened mutation and test churn
Recommended context capacity: approximately 250k tokens
Implementation authority: explicit
Exact baseline: e9943b56b0bb97402fd64ac2143f1cf2fe07401f
Changed-path allowlist: exactly these 9 paths and no others: `extension/ui/sidebar.js`; `extension/ui/sidebar.css`; `tests/companion_review_extension.test.js`; `docs/X_COMPANION.md`; `SPEC.md`; `PRODUCT.md`; `DEVELOPMENT.md`; `docs/adr/0092-companion-download-unread-state.md`; `docs/adr/README.md`
Implementation boundaries: one All when downloads exist, unread marking and the existing opened mutation on matched download rows, with the matching tests and documentation only
Independence required: no
Evidence posture: non-independent

This is a genuinely fresh correction session. You did not implement the candidate or its earlier corrections. Establish the repository and code evidence independently. The correction is a Cooperator-directed closeout of the same whole, not a new feature objective.

## Why this correction exists

The COOPERATOR rendered `e9943b5`. The compact five + All expansion works, but item 1 FAILS for two remaining UI reasons:

- Two All controls appear: the download All and the review All. The first All collapses; the second makes no sense. When downloads exist, there must be exactly one All. It must reveal the later retained downloads and the complete review history, and collapse them again. The review All remains only when no downloads exist.
- A downloaded post that is still unread is not visually marked in the download row. The unread review row is deduplicated away, so the download row must carry the unread marker. Opening that row must use the existing review opened mutation for the matching analyzed unread item so the marker and the review-only badge can clear.

The «Save to Kronika failed» message and the failed X download rows are acquisition outcomes, not history-list defects. Some X saves succeeded and some failed; the history row correctly shows `Download failed`. Do not change the acquisition path. Record the save failure as a separate residual/whole, like the YouTube `INSPECTION_OUTPUT_LIMIT`.

## Current truth

Repository: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Expected HEAD: e9943b56b0bb97402fd64ac2143f1cf2fe07401f
Expected parent: 35c58b693bc885dc115d91df3c6e64680d0c79aa
Expected grandparent: b5436029c66da69c1d14c0f378cbea07bdc74a40
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50 at `/Users/agile/Projects/kronika/.ap`
Public `main`: `e9943b5` (Orchestrator observation; no network).
Worktree: clean, local `main` equal to `origin/main`.

Read at least:

- `extension/ui/sidebar.js` — `presentHistory`, `renderDownloadHistory`, `renderReviewCollections`, `applyHistoryDisclosure`, `setDownloadHistoryExpanded`, `onDownloadAllClick`, `onAllClick`, `onReviewListClick`, `refreshInbox`, `openHostedDetails`, the `REVIEW_INBOX_OPENED` request.
- `extension/ui/sidebar.html` — `#download-history`, `#download-history-all`, `#download-history-expanded`, `#review-history-rest`, review lists/All.
- `extension/ui/sidebar.css` — download row, unread accent/row, All styling.
- `extension/shared/messages.js` — review item sanitization and `unread`/`analysis_run_id`.
- `tests/companion_review_extension.test.js` — compact history, All, dedupe, unread, opened, failure, badge tests.
- `docs/X_COMPANION.md`, `SPEC.md`, `PRODUCT.md`, `DEVELOPMENT.md`, `docs/adr/0090-companion-download-row-details-and-latest-update-order.md`, `docs/adr/0091-companion-history-compact-five-and-all-expansion.md`, `docs/adr/README.md`.
- `09_report_00.md` and `00_notes.md` for the rendered-feedback context.

## Required behavior

### 1. One All when downloads exist

- Keep the existing download All control after the five compact downloads.
- When downloads exist, hide the review All entirely. The download All must:
  - expand the later retained download rows, including the sixth and last retained row;
  - expand the complete review history (the compact and expanded review lists) behind it;
  - collapse both back to the five-download sheet on the second activation.
- When no downloads exist, the review compact/All/expanded behavior remains exactly as now; no empty download All is shown.
- The download All remains a `type="button"` with `aria-controls`, `aria-expanded` in sync, accessible name All, keyboard operation, starts collapsed and is not persisted.
- The title-bar toggle still opens/closes the sheet. The review history must not show a second All when downloads exist.
- The review All remains in the DOM for the no-downloads case; hide it with the existing disclosure logic when downloads exist.

### 2. Unread download row

- When a download row’s `media_id` matches an analyzed review item with `unread: true`, visually mark that download row as unread. Use the existing unread dot/accent language where practical; add an accessible unread indication (for example an `aria-label` or visually hidden text containing “Unread”) so the state is not color-only.
- The review row remains deduplicated from both review lists; the download row is the primary representation.
- Clicking a download row with an own media id still opens hosted Details through the existing `open_details` message.
- If the matching review item is analyzed, unread, has an `analysis_run_id`, and the row has a media id, the same click must also post the existing `REVIEW_INBOX_OPENED` request with that analysis run, exactly once, then refresh the inbox so the unread marker and the server badge can clear. This is the existing mutation the review row would have used; do not add a new route, message or counter.
- If there is no matching analyzed unread item, the click posts only `open_details` as before. A null-media or pending row remains inert and cannot mark anything opened.
- The row stays clickable after read; the unread marker disappears after the opened refresh. The review-only badge remains truthful; no new badge math.

### 3. Tests and documentation

Update `tests/companion_review_extension.test.js` to prove:

- With downloads, exactly one All is visible and the review All is hidden; expanding shows the sixth/last retained downloads and the complete review history; collapsing returns to five; no second All.
- A download row matching an analyzed unread review item has the unread marker/accessible text; clicking it posts one `open_details` and one `REVIEW_INBOX_OPENED` with the matching analysis run, then refreshes; the row remains; the marker clears after the refreshed unread state.
- A download row without a matching analyzed unread item posts no `REVIEW_INBOX_OPENED`; a distinct review row stays deduplicated/visible as appropriate; pending/null-media rows remain inert.
- No-downloads review All behavior remains.
- Existing click/inert/read, dedupe, failure, badge, single-flight and stale-context tests still pass.

Update:

- `docs/X_COMPANION.md` — one All when downloads exist, complete review history behind it, unread marker and opened behavior on matched download rows, no second All, review-only badge, acquisition residuals.
- `SPEC.md` — state the one-All rule, complete review history behind it, unread marker and the existing opened mutation on a matched analyzed unread download row, no new mutation, review-only badge, no-downloads review All.
- `PRODUCT.md` — record the one All, unread download marker and opened behavior.
- `DEVELOPMENT.md` — add rendered acceptance checks for one All, sixth/last download, complete review history, unread marker, opened clear and no second All.
- Add `docs/adr/0092-companion-download-unread-state.md` as an accepted ADR that supplements ADR-0091 and supersedes only its review-All presentation when downloads exist and the no-opened statement for a matched analyzed unread download row. Do not edit the ADR-0090 or ADR-0091 bodies.
- `docs/adr/README.md` — index ADR-0092 and annotate the ADR-0091 row.
- Do not edit `README.md`, `ROADMAP.md`, `SERVER.md`, `docs/UX_AUDIT.md`, or the ADR-0090/0091 bodies. No backend, API, schema, manifest, permission, mutation or message-type change.

## Repository and route

Verify before acting:

- `git -C /Users/agile/Projects/kronika status --porcelain=v1 -b` is clean and reports `## main...origin/main`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD` equals `e9943b5`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^` equals `35c58b6`;
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
Downloadable prompt filename: 10_correction_00.md
Destination path: /Users/agile/meta/projects/kronika/01/03-companion-download-notifications
Report filename: 10_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: only the 9 allowlisted repository paths (the actual changed subset)
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/03-companion-download-notifications/10_report_00.md

## Authority

Positive authority: read-only inspection of the repository, the accepted plan and reports, and this prompt at `/Users/agile/meta/projects/kronika/01/03-companion-download-notifications/10_correction_00.md`; modify exactly the 9 allowlisted paths; run the selected AP and Node checks below; check the exact report destination; create exactly one local commit on `main` on top of `e9943b5`; and create/read back `10_report_00.md`.

Commands: `./.ap/ap project check`, `./.ap/ap exec` with the exact baseline and declared operations, `node --test` with the selected suites, read-only Git inspection, exact-path `git add`, one local `git commit`, and the native file writer for the exact report path. Do not invoke raw `.venv/bin/python`, `python`, `python3` or `poetry run`.

Git authority: one local commit on `main` on top of `e9943b5`, subject `fix: mark unread downloads and show one All`. Stage only the changed subset of the 9 allowlisted paths; never `git add .` or `git add -A`. No fetch, push, force, amend, reset, clean, stash, checkout, switch, tag or remote change.

Network authority: none. Secret authority: none. Do not read `private/`, `.venv`, credentials, browser profiles, cookies or unrelated paths.

Negative authority: any change outside the 9 allowlisted paths; any acquisition, web-shell, manifest, permission, route, schema, migration or download-projection field change; any push, publication, deployment, full suite, browser run, NUC access, provider call or secret access; any edit to the plan, reports, notes, handout, `02_rereport_00.md` or the run map; any acceptance or closure claim.

## Validation

Run the focused Node selection first:

```text
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline e9943b56b0bb97402fd64ac2143f1cf2fe07401f
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline e9943b56b0bb97402fd64ac2143f1cf2fe07401f --operation runtime-info
node --test tests/companion_review_extension.test.js tests/x_companion_extension.test.js
```

Then the adjacent companion selection:

```text
node --test tests/companion_web_bridge.test.js tests/companion_settings_automatic_analysis.test.js tests/youtube_request_cockpit.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js
```

Run `git diff --check`, `git status --porcelain=v1`, inspect the exact diff and verify the committed path list is the exact changed subset of the 9-path allowlist, with no path outside it. Python tests are not required for this extension-side correction; the project check and runtime-info are the AP envelope evidence. Do not run a full suite, browser evidence, real acquisition, provider calls or NUC commands.

The correction must add or update tests that prove the one-All/unread/opened behavior. If the «Save to Kronika failed» has a UI cause rather than an acquisition cause, report it with exact evidence; do not change acquisition code.

## Report contract

Write the terminal report to `10_report_00.md`. Begin it exactly with:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three exchange coordinates exactly once (`10`/`01`). Include the item 1 amendment, the exact change, the new and updated tests, the test commands and counts, the new commit SHA and parent, the staged and committed path lists, and Orchestration critique with MEASURED and LEAD findings or none. Use `Phase-qualified result: implementation-PASS` only if the correction and all selected checks pass; otherwise `PARTIAL` or `BLOCKED` with exact evidence. Use `Logical-whole closure: not-closed` and `Report justification: new-mutation`.

Direct-write the report, read it all back, verify content, path and SHA-256, and only then send a short separate completion notice. If the report path already exists, including an empty file, stop and report the collision. If the client blocks the exact write, return the complete report and state `File delivery: pending client restriction`.

Do not claim acceptance, publication, deployment or closure. A fresh independent full re-acceptance follows.

## Stopping conditions

Stop and report the exact blocker if:

- the repository identity, branch, baseline, parent, worktree or `.ap` gate fails;
- a required change falls outside the 9-path allowlist;
- a selected test fails for a reason outside this correction;
- the one-All/unread/opened behavior cannot be achieved without changing the review-only badge, privacy, acquisition or query semantics;
- a durable contract change or new ADR beyond ADR-0092 appears necessary;
- the report path already exists or its parent/symlink resolution is unsafe;
- the client cannot write the report or run a required command;
- secrets, private data, browser state or another ungranted effect would be touched.

After a prerequisite stop, only report preparation and necessary cleanup inside this grant may finish. Preserve the first causal failure.

## Authority expiry

This grant expires at the terminal correction report, cancellation or supersession. Retained context, a green test run, the local commit or a later conversation is not acceptance or closure authority.
