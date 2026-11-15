# Companion history — compact five downloads, one All, no duplicate review rows

## Routing and authority

Persistent role identity: WORKER
Logical whole identity: companion-download-notifications
Worker session ordinal: 08
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: EXPAND-COMPANION-HISTORY-DOWNLOADS-01
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — companion history composition, deduplication, expansion state and test churn
Recommended context capacity: approximately 250k tokens
Implementation authority: explicit
Exact baseline: 35c58b693bc885dc115d91df3c6e64680d0c79aa
Changed-path allowlist: exactly these 11 paths and no others: `extension/ui/sidebar.js`; `extension/ui/sidebar.html`; `extension/ui/sidebar.css`; `extension/shared/messages.js`; `tests/companion_review_extension.test.js`; `docs/X_COMPANION.md`; `SPEC.md`; `PRODUCT.md`; `DEVELOPMENT.md`; `docs/adr/0091-companion-history-compact-five-and-all-expansion.md`; `docs/adr/README.md`
Implementation boundaries: companion history compact-five/All composition, download expansion, review-row deduplication and the matching tests and documentation only
Independence required: no
Evidence posture: non-independent

This is a genuinely fresh correction session. You did not implement the candidate or its earlier corrections. Establish the repository and code evidence independently. The correction is a Cooperator-directed closeout of the same whole, not a new feature objective.

## Why this correction exists

The COOPERATOR rendered `35c58b6`. Items 1–3, 5–8 passed; item 4 is PARTIAL and item 9 is PARTIAL because of the companion history list:

- The compact sheet shows the five Recent downloads and then the review-history compact rows. One review row duplicates the latest download title (the unread «The rebellion starts from within»), and another duplicates «Before she left…».
- The COOPERATOR wants one **All** control immediately after the five downloads, not the inline review rows. After All, the sixth download must appear; the last retained download must be visible, not truncated at five.
- There must be no duplication between downloads and review history. The latest download stays at the top; the review history remains accessible behind the All, but must not duplicate a download media/title and must not precede the All in the compact view.

The compact companion UI (Timeline text, Filter disclosure, My contributions) passed. The YouTube acquisition `INSPECTION_OUTPUT_LIMIT` remains a separate logical whole. The full-page narrow My contributions LEAD remains outside the companion.

## Current truth

Repository: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Expected HEAD: 35c58b693bc885dc115d91df3c6e64680d0c79aa
Expected parent: b5436029c66da69c1d14c0f378cbea07bdc74a40
Expected grandparent: 647e6da11416559f1bef52d53e9743acbd2bb688
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50 at `/Users/agile/Projects/kronika/.ap`
Public `main`: `35c58b6` (Orchestrator observation; no network).
Worktree: clean, local `main` equal to `origin/main`.

Read at least:

- `extension/ui/sidebar.html` — `#review-history`, `#download-history`, the review lists and All control.
- `extension/ui/sidebar.js` — `renderDownloadHistory`, `renderReviewCollections`, `presentHistory`, `applyInboxResult`, `historyUserExpanded`, the review All and click handling.
- `extension/ui/sidebar.css` — download rows, review compact/expanded lists, All styling.
- `extension/shared/messages.js` — `DOWNLOAD_HISTORY`, `mergeDownloadHistoryItems`, `sanitizeDownloadProjection`.
- `extension/background/service_worker.js` — `readDownloadWindow` and `reviewInbox` (read-only reference; do not change it).
- `tests/companion_review_extension.test.js` — download block, review history, click, failure and badge tests.
- `docs/X_COMPANION.md`, `SPEC.md`, `PRODUCT.md`, `DEVELOPMENT.md`, `docs/adr/0090-companion-download-row-details-and-latest-update-order.md`, `docs/adr/README.md`.
- `07_report_00.md` and `00_notes.md` for the rendered-feedback context.

## Required behavior

### 1. Retain the expanded download window

The download projection must no longer be truncated to five rows. Keep the compact/retained distinction in `DOWNLOAD_HISTORY`: a compact limit of five and a retained/read window of fifty. `mergeDownloadHistoryItems` returns up to the retained limit, with the current deduplication and `sort_at_ms` order. The response `downloads.items` may therefore carry more than five rows.

### 2. Compact sheet: five downloads and one All

When downloads exist and the history sheet is opened:

- Show the five latest download rows in `#download-history-list`.
- Show one visible **All** control immediately after those five rows.
- Do not show the review-history compact rows or the review All before that All in the compact state.
- Hide the download expanded list and the review compact/expanded lists until All is activated.
- The latest download remains first; the five compact rows keep the current click/read/inert behavior and the review-only badge remains unchanged.

When All is activated:

- Expand the remaining download rows, so the sixth and later retained downloads are visible; the last retained row must be present, not truncated at five.
- Then show the review history in its existing compact/All/expanded behavior, deduplicated against downloads.
- Activating All again collapses the remaining downloads and the review history back to the compact five-download view.
- The All control is a real `type="button"` with `aria-controls`, `aria-expanded` kept in sync, accessible name **All** and keyboard operation.
- The title-bar history toggle still opens/closes the whole sheet. The download All state starts collapsed on each panel load and is not persisted.
- If no downloads exist, the review history keeps its current compact/All behavior (no empty download All).
- If downloads exist but no review rows exist, All expands the remaining downloads only.

### 3. No duplicate review rows

Filter the review history against the downloads by media id:

- If a review item’s `media_id` matches any download item’s `media_id`, omit the review item from both the compact and expanded review lists.
- The download row is the primary representation; do not render the same media/title twice.
- Review rows with distinct media remain in the review history behind All.
- The toolbar badge and server `unopened_count` remain truthful; do not change the badge math or add a second counter.
- A download row without a media id is inert and does not cause a review row to be dropped unless the media ids match.

The existing download click/read behavior, review row hosted Details, opened mutation, review All behavior, failure isolation, single-flight refresh and stale-context handling remain unchanged.

### 4. Tests and documentation

Update `tests/companion_review_extension.test.js` to prove:

- The response may carry more than five downloads; the compact list shows five and the sixth appears after All.
- The compact state shows exactly one All after the five downloads and no review rows before it.
- The expanded state shows the remaining downloads, including the last retained row, and then the deduplicated review history.
- A review row whose media id is in the downloads is absent; a review row with a distinct media id remains.
- The download All toggles `aria-expanded` and the expanded lists; the title-bar toggle still works; no new request or query change is caused by All.
- Download-only, review-only, empty, failed, unread and read cases still behave; the badge remains review-only.
- The existing click/inert/read, failure, single-flight and stale-context tests still pass.

Update:

- `docs/X_COMPANION.md` — compact five downloads, one All, expanded sixth/later downloads, deduplicated review history and badge.
- `SPEC.md` — replace the at-most-five/single-window wording with the compact-five + retained-window + All-expansion behavior; state no duplicate review row for a download media; keep the review-only badge and failure rules.
- `PRODUCT.md` — record the compact five + All + deduplicated review behavior.
- `DEVELOPMENT.md` — add the rendered acceptance checks for the sixth download, last download, one All, no duplicate review row and review history behind All.
- Add `docs/adr/0091-companion-history-compact-five-and-all-expansion.md` as an accepted ADR that supplements ADR-0090 and supersedes only its at-most-five/single-window presentation statements. Do not edit the ADR-0090 body.
- `docs/adr/README.md` — index ADR-0091 and annotate the ADR-0090 row.
- Do not edit `README.md`, `ROADMAP.md`, `SERVER.md`, `docs/UX_AUDIT.md`, or the ADR-0090 body. No backend, API, schema, manifest, permission, mutation or message-type change.

## Repository and route

Verify before acting:

- `git -C /Users/agile/Projects/kronika status --porcelain=v1 -b` is clean and reports `## main...origin/main`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD` equals `35c58b6`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^` equals `b543602`;
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
Downloadable prompt filename: 08_correction_00.md
Destination path: /Users/agile/meta/projects/kronika/01/03-companion-download-notifications
Report filename: 08_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: only the 11 allowlisted repository paths (the actual changed subset)
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/03-companion-download-notifications/08_report_00.md

## Authority

Positive authority: read-only inspection of the repository, the accepted plan and reports, and this prompt at `/Users/agile/meta/projects/kronika/01/03-companion-download-notifications/08_correction_00.md`; modify exactly the 11 allowlisted paths; run the selected AP and Node checks below; check the exact report destination; create exactly one local commit on `main` on top of `35c58b6`; and create/read back `08_report_00.md`.

Commands: `./.ap/ap project check`, `./.ap/ap exec` with the exact baseline and declared operations, `node --test` with the selected suites, read-only Git inspection, exact-path `git add`, one local `git commit`, and the native file writer for the exact report path. Do not invoke raw `.venv/bin/python`, `python`, `python3` or `poetry run`.

Git authority: one local commit on `main` on top of `35c58b6`, subject `fix: expand companion history downloads behind All`. Stage only the changed subset of the 11 allowlisted paths; never `git add .` or `git add -A`. No fetch, push, force, amend, reset, clean, stash, checkout, switch, tag or remote change.

Network authority: none. Secret authority: none. Do not read `private/`, `.venv`, credentials, browser profiles, cookies or unrelated paths.

Negative authority: any change outside the 11 allowlisted paths; any web-shell, extension manifest, permission, route, schema, migration, acquisition or download-projection privacy change; any push, publication, deployment, full suite, browser run, NUC access, provider call or secret access; any edit to the plan, reports, notes, handout, `02_rereport_00.md` or the run map; any acceptance or closure claim.

## Validation

Run the focused Node selection first:

```text
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 35c58b693bc885dc115d91df3c6e64680d0c79aa
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 35c58b693bc885dc115d91df3c6e64680d0c79aa --operation runtime-info
node --test tests/companion_review_extension.test.js tests/x_companion_extension.test.js
```

Then the adjacent companion selection:

```text
node --test tests/companion_web_bridge.test.js tests/companion_settings_automatic_analysis.test.js tests/youtube_request_cockpit.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js
```

Run `git diff --check`, `git status --porcelain=v1`, inspect the exact diff and verify the committed path list is the exact changed subset of the 11-path allowlist, with no path outside it. Python tests are not required for this extension-side correction; the project check and runtime-info are the AP envelope evidence. Do not run a full suite, browser evidence, real acquisition, provider calls or NUC commands.

## Report contract

Write the terminal report to `08_report_00.md`. Begin it exactly with:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three exchange coordinates exactly once (`08`/`01`). Include the item 4/9 amendment, the exact change, the new and updated tests, the test commands and counts, the new commit SHA and parent, the staged and committed path lists, and Orchestration critique with MEASURED and LEAD findings or none. Use `Phase-qualified result: implementation-PASS` only if the correction and all selected checks pass; otherwise `PARTIAL` or `BLOCKED` with exact evidence. Use `Logical-whole closure: not-closed` and `Report justification: new-mutation`.

Direct-write the report, read it all back, verify content, path and SHA-256, and only then send a short separate completion notice. If the report path already exists, including an empty file, stop and report the collision. If the client blocks the exact write, return the complete report and state `File delivery: pending client restriction`.

Do not claim acceptance, publication, deployment or closure. A fresh independent full re-acceptance follows.

## Stopping conditions

Stop and report the exact blocker if:

- the repository identity, branch, baseline, parent, worktree or `.ap` gate fails;
- a required change falls outside the 11-path allowlist;
- a selected test fails for a reason outside this correction;
- the compact/All/dedup behavior cannot be achieved without changing the review-only badge, privacy or query semantics;
- a durable contract change or new ADR beyond ADR-0091 appears necessary;
- the report path already exists or its parent/symlink resolution is unsafe;
- the client cannot write the report or run a required command;
- secrets, private data, browser state or another ungranted effect would be touched.

After a prerequisite stop, only report preparation and necessary cleanup inside this grant may finish. Preserve the first causal failure.

## Authority expiry

This grant expires at the terminal correction report, cancellation or supersession. Retained context, a green test run, the local commit or a later conversation is not acceptance or closure authority.
