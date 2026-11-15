### Report for ORCHESTRATOR_CHAT

Logical whole identity: companion-download-notifications
Worker session ordinal: 09
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: ACCEPT-COMPANION-DOWNLOAD-NOTIFICATIONS-04
status: PASS
Phase-qualified result: acceptance-PASS
Result artifact or commit: e9943b56b0bb97402fd64ac2143f1cf2fe07401f
Result evidence: local repository gate, whole-diff allowlist, source and documentation inspection, and the selected AP, Python and Node checks below
Start commit: e9943b56b0bb97402fd64ac2143f1cf2fe07401f
End commit: e9943b56b0bb97402fd64ac2143f1cf2fe07401f
Report justification: final-acceptance
Logical-whole closure: not-closed

Acceptance candidate: e9943b56b0bb97402fd64ac2143f1cf2fe07401f
Acceptance owner map: companion-download-notifications-v4 — accepted plan `01_report_00.md`, `SPEC.md`, ADR-0089, ADR-0090, ADR-0091, `docs/X_COMPANION.md`, `PRODUCT.md`, `SECURITY.md`, the four original Cooperator choices, the download-row amendments, the compact companion UI correction and the history compact-five/All expansion
Acceptance allowlist: the 23 declared paths
Acceptance risk claims: R1–R11
Acceptance control matrix: C01–C27
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 3
Automatic corrections used: 0
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates

Independence: this session did not implement `cc8f679`, the identity-login correction `647e6da`, the download-row correction `b543602`, the compact UI correction `35c58b6`, or the history expansion `e9943b5`. Prior reports and notes were read as claims. Evidence is the local repository at the candidate and the checks run in this session.

Repository mutation: none. Host/remote mutation: none. Trace persistence: this report only. Git authority used: read-only. Network: not used. No fetch, stage, commit, push, reset, clean, or test edit. Commit and push result: not authorized.

Requested reasoning recommendation: High. Effective model identity is not independently attested.

## Candidate

Parents match the grant:

- HEAD `e9943b56b0bb97402fd64ac2143f1cf2fe07401f` — `fix: expand companion history downloads behind All`, parent `35c58b6`
- HEAD^ `35c58b693bc885dc115d91df3c6e64680d0c79aa` — compact companion UI
- HEAD^^ `b5436029c66da69c1d14c0f378cbea07bdc74a40` — download-row correction
- HEAD^^^ `647e6da11416559f1bef52d53e9743acbd2bb688` — identity-login correction
- HEAD^^^^ `cc8f67965213ee9b22d113cc200776c42f6503ba` — implementation
- HEAD^^^^^ `e64f2b0f92458fac2590e03672e30da62275b345`

Changed paths, and no others, from `e64f2b0..e9943b5`:

- `DEVELOPMENT.md`
- `PRODUCT.md`
- `SECURITY.md`
- `SPEC.md`
- `docs/X_COMPANION.md`
- `docs/adr/0089-companion-own-download-status-history.md`
- `docs/adr/0090-companion-download-row-details-and-latest-update-order.md`
- `docs/adr/0091-companion-history-compact-five-and-all-expansion.md`
- `docs/adr/README.md`
- `extension/background/service_worker.js`
- `extension/shared/messages.js`
- `extension/ui/sidebar.css`
- `extension/ui/sidebar.html`
- `extension/ui/sidebar.js`
- `src/kronika/adapters/api/web/app.js`
- `src/kronika/adapters/api/web/index.html`
- `src/kronika/adapters/api/web/styles.css`
- `tests/companion_review_extension.test.js`
- `tests/contract/test_local_web_application.py`
- `tests/contract/test_x_request_api.py`
- `tests/contract/test_youtube_request_api.py`
- `tests/kronika_ui.test.js`
- `tests/workspace_media_frontend.test.js`

`35c58b6..e9943b5` changes exactly these 11 paths: `DEVELOPMENT.md`, `PRODUCT.md`, `SPEC.md`, `docs/X_COMPANION.md`, `docs/adr/0091-companion-history-compact-five-and-all-expansion.md`, `docs/adr/README.md`, `extension/shared/messages.js`, `extension/ui/sidebar.css`, `extension/ui/sidebar.html`, `extension/ui/sidebar.js`, and `tests/companion_review_extension.test.js`.

Purpose: own download status inside the existing companion history sheet, identity-stale discard, clickable own-media rows ordered by latest update, a compact companion-hosted Timeline, Filter, and My contributions layout, and a compact five-download sheet whose All control reveals the retained later downloads and then deduplicated review history.

## Validation

`./.ap/ap project check --root /Users/agile/Projects/kronika --baseline e64f2b0f92458fac2590e03672e30da62275b345` PASS. `./.ap/ap exec --operation runtime-info` at that baseline reported CPython 3.13.14 through `/Users/agile/Projects/kronika/.venv/bin/python`.

Focused Python (`test_x_request_api.py`, `test_youtube_request_api.py`, `test_companion_review_api.py`): 46 passed in 7.07s. Focused Node (`tests/companion_review_extension.test.js`, `tests/x_companion_extension.test.js`): 116 passed, 0 failed. Broader Python: 206 passed in 50.50s. Broader Node: 64 passed, 0 failed. Compact UI Node (`tests/kronika_ui.test.js`, `tests/workspace_media_frontend.test.js`): 44 passed, 0 failed. Affected frontend Node: 287 passed, 0 failed. Served-shell Python (`tests/contract/test_local_web_application.py`): 211 passed in 27.89s. No failure signature. Every command exit was 0.

`git diff --check e64f2b0..e9943b5` exit 0. After the checks, `git status --porcelain=v1 -b` is still `## main...origin/main [ahead 1]` with no other lines. HEAD is unchanged.

Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none

## Control matrix

C01 PASS. `origin` is `https://github.com/cisarik/kronika.git`. Branch `main`. HEAD and all five parents match the declared SHAs. Porcelain is clean and `[ahead 1]`. Local `origin/main` is `35c58b693bc885dc115d91df3c6e64680d0c79aa`, with no fetch, matching the Orchestrator's 2026-11-13 public-main observation. `.ap` HEAD and the gitlink are both `d7023cf037f6d17885c3ede5c04812c61640da50`.

C02 PASS. `git diff --name-only e64f2b0..e9943b5` is exactly the 23 paths above. `git diff --name-only 35c58b6..e9943b5` is exactly the 11 history paths above. `git diff --name-only e64f2b0..e9943b5 -- src` is only the three web-shell assets. No manifest, Alembic, or backend API/schema path is in the diff.

C03 PASS. `git diff e64f2b0..e9943b5 -- extension/manifest.json` is empty. Required `permissions` are exactly `alarms`, `sidePanel`, and `storage`. The file has no `notifications`, no `host_permissions`, and no `externally_connectable`. `optional_permissions` remains the pre-existing `downloads` entry and `optional_host_permissions` remains `https://*.ts.net/*`; neither was added by this range.

C04 PASS. No backend, schema, migration, API route, or `tailscale_ingress.py` path changed. The unchanged policy file has exactly six `companion_mutation=True` routes: `PUT /api/admin/settings/automatic-analysis`, `POST /api/youtube/requests`, `POST /api/companion/review-inbox/{media_id}/opened`, `POST /api/companion/review-inbox/{media_id}/apply`, `POST /api/x/requests`, and `POST /api/x/requests/{claim_id}/retry`. YouTube retry stays unflagged. `TYPES` gained no message. The alarm remains `kronika.review-inbox`. `STORAGE` remains `kronikaOrigin`, and the worker storage keys were not added or renamed. `configurationRevision` is in memory. No download snapshot is written with `chrome.storage.local.set`.

C05 PASS. `REVIEW_INBOX` remains `"review_inbox"`. The sidebar still sends that type with payload `{}`. A successful `reviewInbox()` return adds `downloads`. `failedDownloadProjection()` is exactly `{ok:false, items:[]}`. A successful window with no retained rows is `{ok:true, items:[]}`. No second download message type or transport was added.

C06 PASS. `handle()` calls `reviewInbox()` only after `isSidebarReviewSender(sender)`. That check requires `sender.id === chrome.runtime.id`, `sender.url` equal to `ui/sidebar.html`, and `sender.origin` equal to that document's origin. A missing or mismatched sender returns `invalidSenderReviewResult()` and does not call `clearBadgeText()`. The test `spoofed review_inbox senders fetch nothing and keep the badge` pins that path.

C07 PASS. Download reads call `pathFor("xRequests")` and `pathFor("youtubeRequests")`, which return the fixed `/api/x/requests` and `/api/youtube/requests` templates, joined to the configured origin. The suffix is `?limit=` plus `DOWNLOAD_HISTORY.readLimit` (50). `readCapabilityDownloadList` does not pass a caller path, id, or cursor. `readDownloadWindow` performs one call per present capability and returns before any cursor follow. A missing `x.request` or `youtube.request` capability skips that source. The test `download read window uses limit 50, ignores cursors, and keeps the retained rows` keeps six rows, one call per source, and `readLimit` 50.

C08 PASS. The sanitized item keys are exactly `source`, `request_id`, `label`, `status`, `media_id`, and `sort_at_ms`. `created_at_ms` is not a projection field. `representativeCatalogedMediaId` keeps cataloged assets with UUID media ids and ascending finite ordinals, then takes the first. `nullableDownloadMediaId` returns a UUID or null, so an invalid non-null media id becomes null. The test `download media id selects the first cataloged X asset and the YouTube request id` pins the selection.

C09 PASS. `downloadSortAt` uses a nonnegative safe-integer `updated_at_ms`, otherwise a valid `created_at_ms`, and the X and YouTube item builders omit the row when that value is null. `mergeDownloadHistoryItems` deduplicates on `(source, lowercased request_id)`, sorts by `sort_at_ms` descending, source ascending, and request id descending, then returns `slice(0, DOWNLOAD_HISTORY.readLimit)`. The limit-50 test retains six rows with `Window 0` first because its `updated_at_ms` is 90. `download merge keeps the retained window, first duplicate, and deterministic ties` and `download sort prefers updated_at_ms and keeps an older request that was updated later` pin the same rules.

C10 PASS. X maps `submitted`, `queued`, `extracting`, `acquiring`, `handing_off`, `completed`, `completed_partial`, `duplicate_resolved`, `failed`, and `catalog_removed`, matching the acquisition state check. YouTube maps `queued`, `processing`, `downloading`, `completed`, `completed_private`, `failed`, and `unavailable`, matching the requester phases. An unmapped or malformed row returns null. Status comes only from those maps. A cataloged media id does not change the status. The test `download rows map every accepted state and reject unknown or unsafe fields` passed.

C11 PASS. An own UUID media id renders `button.download-history-row.download-history-row--action` with type `button`, three spans, and `aria-label` `Open details for <label>`. Its click calls `openHostedDetails`, which posts one `open_details` web-bridge message with that media id. The handler does not send `REVIEW_INBOX_OPENED`, retry, or remove the row. A null media id renders a `div.download-history-row` with no button, link, click listener, or tabindex. The test `own-media download rows open hosted details per click and stay clickable after a read save` posts `open_details` twice for the action row, posts nothing for the inert row, and leaves both rows in place.

C12 PASS. `sidebar.html` has `#download-history` inside `#review-history`, heading `Recent downloads`, compact `#download-history-list`, and `#download-history-all`. `#review-history-rest` contains the compact review list, `#review-history-all`, and the expanded review list. `#review-history::before` is `Companion history`. Review labels remain `Recent review history` and `Full review history`. The title-bar toggle still opens and closes `#review-history`. `#download-history[hidden]` and `.download-history-list:empty` are `display: none`.

C13 PASS. `presentHistory` renders `slice(0, DOWNLOAD_HISTORY.limit)` in the compact list and the remainder in `#download-history-expanded`. With downloads present, `#download-history-all` is a `type="button"` control, accessible name `All`, `aria-controls="download-history-expanded review-history-rest"`, and initial `aria-expanded="false"`. `downloadHistoryExpanded` starts false and is not written to storage. Before All, `#review-history-rest` and the review All stay hidden. The test `compact history shows five downloads, one All, then deduplicated review rows` shows five compact rows, one All, and a hidden review rest.

C14 PASS. `onDownloadAllClick` only calls `setDownloadHistoryExpanded`. Expanding reveals the retained rows after five, including the sixth and the last retained row in the seven-row fixture, then shows `#review-history-rest`. Activating again collapses to the five-download sheet. The test `download All toggles retained rows without a new inbox request` passed. `onHistoryToggle` still opens and closes the sheet and reapplies disclosure. All does not change the timeline filter or query.

C15 PASS. `reviewItemsOmittingDownloadMedia` drops a review item whose media id matches any download media id, case-insensitively, before both compact and expanded review lists are rendered. A distinct review media id remains and is behind All while downloads exist. A null download media id is not added to the covered set, so it does not drop a review row. The compact-history test omits `Duplicate review` from both review lists and keeps `Distinct review`.

C16 PASS. No downloads hides `#download-history` and the download All, and leaves review compact/All behavior. Downloads without review rows keep the download All and, once expanded, show only the later download rows. Download failure uses the failed projection, hides the Downloads block, and still renders the review list. Empty history disables the title-bar toggle. The same compact-history test covers download-only, review-only, empty, and `{ok:false}` states.

C17 PASS. `readDownloadWindow` returns the failed projection for the whole Downloads block when either enabled source fails, while `reviewInbox()` still returns the review items and applies the badge from `unopened_count`. `failedReviewInbox` clears the badge on review-list, pagination, or cursor failure and hides history through `presentHistory`. The badge and the one-minute `kronika.review-inbox` alarm remain review-only. The manifest has no `notifications` permission and no second counter. The test `one failed download source hides every download row and keeps review and badge` pins the YouTube 503 case. `badge alarm refresh does not call download lists` passed.

C18 PASS. `aggregationContextMatches` re-reads origin, configuration revision, login, the three history capabilities, and history source. A login change with identical capabilities returns `staleContextReviewResult()` and does not clear the badge. The test `changed identity login discards the in-flight history result without clearing the badge` pins that case. `refreshInbox` returns while `inboxRefreshActive` is true, and a changed `inboxGeneration` discards the late result. Hidden visibility stops the poll. `connect`, `reset`, and runtime invalidation call `retireInboxGeneration()`, which clears both download lists, hides the section, and sets download All `aria-expanded` to false. The test `sidebar skips overlapping refreshes, stops hidden polling, and drops late results` passed.

C19 PASS. List routes call `list_owned` with the signed-in requester. Administrator review items stay on the review list. The projection drops raw URL, asset arrays, filenames, provider payloads, and failure details; the sidebar renders source, label, and status text. The only linked media is the row's own cataloged UUID. `ordinary own-history and administrator inbox both keep separate own downloads` asserts the foreign analyzed title is absent from the download projection. No download storage key was added.

C20 PASS. `SPEC.md`, `PRODUCT.md`, `docs/X_COMPANION.md`, and `DEVELOPMENT.md` state the compact five, one All, later retained downloads including the sixth and last, deduplicated review rows, own-media click, inert no-media rows, latest-update order, the first page at limit 50 retaining fifty, and the review-only badge. `SECURITY.md` states the own-list read, the sanitized projection, the omitted invalid media id, sidebar-only `review_inbox`, and that no download snapshot or new mutation is added; it does not contradict the All presentation. ADR-0091 is `Accepted` and indexed. `docs/adr/README.md` records that ADR-0091 supersedes only ADR-0090's at-most-five and single-window presentation. `git diff 35c58b6..e9943b5 -- docs/adr/0090-companion-download-row-details-and-latest-update-order.md` is empty, so the ADR-0090 body is unchanged.

C21 PASS. Companion rules hide `.kronika-chronicle__glyph`, show `.kronika-chronicle__reading`, and make Kind, Status, and Visibility labels readable. Companion title rules set wrapping and `-webkit-line-clamp: none`. The wide title rule remains `-webkit-line-clamp: 2` and the wide header grid remains. The Filter button is a `type="button"` for `#kronika-timeline-filters`, starts collapsed, and its click only toggles `is-collapsed` and `aria-expanded`. The only collapsed-hide rule is under `.kronika-companion-hosted`. The wide page hides the button with `.kronika-chronicle-filter-toggle { display: none }` and keeps the four filters visible. The test `companion Timeline text and Filter disclosure stay off the wide page` toggles the button without changing the hash or issuing another timeline request.

C22 PASS. Companion My contributions sets the row to `minmax(0, 1fr)` and the title and metadata to block layout, full width, `overflow-wrap: break-word`, `word-break: normal`, and `white-space: normal`. The wide `.workspace-media-browser .admin-media-row` grid stays four columns. The test `companion My contributions title fills the row and the wide grid stays` pins both rules. The styles diff adds companion rules and does not delete the wide grid.

C23 PASS. Wide Timeline glyphs, the two-line title clamp, the visible filters, and the multi-column contributions grid remain outside `.kronika-companion-hosted`. The full-page narrow My contributions LEAD is outside this companion boundary and is recorded under residual risks.

C24 PASS. Actual counts match the declared evidence: focused Python 46, focused Node 116, broader Python 206, broader Node 64, compact UI Node 44, affected frontend Node 287, served-shell Python 211. All failed counts are 0.

C25 PASS. `git diff --check e64f2b0..e9943b5` is clean. The worktree after validation is clean and still ahead 1. The committed path lists match C02. Relative links in the nine changed Markdown files resolve.

C26 PASS. `08_report_00.md` is the history correction report for `e9943b5`. Its saved text records that the destination already existed empty, was not overwritten by that session, and states `File delivery: collision`; the complete report content is present now. `02_report_01.md` records status BLOCKED and no repository change. Neither that report nor a `02_rereport_00.md` is in the candidate diff. No `02_rereport_00.md` is in the trace directory.

C27 PASS. `INSPECTION_OUTPUT_LIMIT` remains in `src/kronika/infrastructure/youtube/downloader.py`, which is outside the allowlist. The full-page narrow My contributions LEAD is outside the companion-hosted rules. Neither failed a selected check. This report records the independent acceptance phase result only. It does not claim publication, deployment, production acceptance, or closure. The Orchestrator owns the accept decision.

## Deviations, risks, and residuals

Defects: none.

Residual risks, outside this acceptance:

- YouTube acquisition `INSPECTION_OUTPUT_LIMIT` remains in the downloader and was not part of this candidate. The selected YouTube lifecycle tests passed.
- The full-page narrow My contributions layout remains an out-of-scope LEAD. Companion-hosted rows use their own single-column rule.
- Rendered companion behavior was not exercised. This grant forbids browser evidence. Public `main` was not contacted; the local tracking ref matches the stated observation.

Orchestration critique:
MEASURED: none
LEAD: none

Proposed next step: the Orchestrator decides whether to accept this phase result and, separately, whether to publish `e9943b56b0bb97402fd64ac2143f1cf2fe07401f` for the Cooperator's rendered pass.

Authority expiry: this acceptance grant expires with this terminal report. A green test run and this phase result are not publication, deployment, production acceptance, or closure authority.
