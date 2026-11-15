### Report for ORCHESTRATOR_CHAT

Logical whole identity: companion-download-notifications
Worker session ordinal: 11
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: ACCEPT-COMPANION-DOWNLOAD-NOTIFICATIONS-05
status: PASS
Phase-qualified result: acceptance-PASS
Result artifact or commit: 2c4f4d89375628df28926060aba305e5d80bacff
Result evidence: local repository gate, whole-diff allowlist, source and documentation inspection, and the selected AP, Python and Node checks below
Start commit: 2c4f4d89375628df28926060aba305e5d80bacff
End commit: 2c4f4d89375628df28926060aba305e5d80bacff
Report justification: final-acceptance
Logical-whole closure: not-closed

Acceptance candidate: 2c4f4d89375628df28926060aba305e5d80bacff
Acceptance owner map: companion-download-notifications-v5 — accepted plan `01_report_00.md`, `SPEC.md`, ADR-0089, ADR-0090, ADR-0091, ADR-0092, `docs/X_COMPANION.md`, `PRODUCT.md`, `SECURITY.md`, the original Cooperator choices, the download-row amendments, the compact companion UI, the compact-five/All expansion and the unread download-row amendment
Acceptance allowlist: the 24 declared paths
Acceptance risk claims: R1–R12
Acceptance control matrix: C01–C27
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 4
Automatic corrections used: 0
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates

Independence: this session did not implement `cc8f679`, the identity-login correction `647e6da`, the download-row correction `b543602`, the compact UI correction `35c58b6`, the compact-five/All expansion `e9943b5`, or the unread/one-All correction `2c4f4d8`. Prior reports and notes were read as claims. Evidence is the local repository at the candidate and the checks run in this session.

Repository mutation: none. Host/remote mutation: none. Trace persistence: this report only. Git authority used: read-only. Network: not used. No fetch, stage, commit, push, reset, clean, or test edit. Commit and push result: not authorized.

Requested reasoning recommendation: High. Effective model identity is not independently attested.

## Candidate

Parents match the grant:

- HEAD `2c4f4d89375628df28926060aba305e5d80bacff` — `fix: mark unread downloads and show one All`, parent `e9943b5`
- HEAD^ `e9943b56b0bb97402fd64ac2143f1cf2fe07401f` — compact five and All expansion
- HEAD^^ `35c58b693bc885dc115d91df3c6e64680d0c79aa` — compact companion UI
- HEAD^^^ `b5436029c66da69c1d14c0f378cbea07bdc74a40` — clickable own-media rows and latest-update order
- HEAD^^^^ `647e6da11416559f1bef52d53e9743acbd2bb688` — identity-login correction
- HEAD^^^^^ `cc8f67965213ee9b22d113cc200776c42f6503ba` — implementation
- HEAD^^^^^^ `e64f2b0f92458fac2590e03672e30da62275b345`

Changed paths, and no others, from `e64f2b0..2c4f4d8`:

- `DEVELOPMENT.md`
- `PRODUCT.md`
- `SECURITY.md`
- `SPEC.md`
- `docs/X_COMPANION.md`
- `docs/adr/0089-companion-own-download-status-history.md`
- `docs/adr/0090-companion-download-row-details-and-latest-update-order.md`
- `docs/adr/0091-companion-history-compact-five-and-all-expansion.md`
- `docs/adr/0092-companion-download-unread-state.md`
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

`e9943b5..2c4f4d8` changes exactly these 9 paths: `DEVELOPMENT.md`, `PRODUCT.md`, `SPEC.md`, `docs/X_COMPANION.md`, `docs/adr/0092-companion-download-unread-state.md`, `docs/adr/README.md`, `extension/ui/sidebar.css`, `extension/ui/sidebar.js`, and `tests/companion_review_extension.test.js`.

Purpose: own download status inside the existing companion history sheet; identity-stale discard including a changed login; clickable own-media rows ordered by latest update; a compact companion-hosted Timeline, Filter, and My contributions layout; five compact downloads and one All that reveals the sixth and later retained downloads plus deduplicated review history; and an unread marker on a matched analyzed download row that posts the existing opened mutation once.

## Validation

`./.ap/ap project check --root /Users/agile/Projects/kronika --baseline e64f2b0f92458fac2590e03672e30da62275b345` PASS. `./.ap/ap exec --operation runtime-info` at that baseline reported CPython 3.13.14 through `/Users/agile/Projects/kronika/.venv/bin/python`.

Focused Python (`test_x_request_api.py`, `test_youtube_request_api.py`, `test_companion_review_api.py`): 46 passed in 6.54s. Focused Node (`tests/companion_review_extension.test.js`, `tests/x_companion_extension.test.js`): 118 passed, 0 failed. Broader Python: 206 passed in 48.39s. Broader Node: 64 passed, 0 failed. Compact UI Node (`tests/kronika_ui.test.js`, `tests/workspace_media_frontend.test.js`): 44 passed, 0 failed. Affected frontend Node: 287 passed, 0 failed. Served-shell Python (`tests/contract/test_local_web_application.py`): 211 passed in 29.01s. No failure signature. Every command exit was 0.

`git diff --check e64f2b0..2c4f4d8` exit 0. After the checks, `git status --porcelain=v1 -b` is still `## main...origin/main [ahead 1]` with no other lines. HEAD is unchanged.

Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none

## Control matrix

C01 PASS. `origin` is `https://github.com/cisarik/kronika.git`. Branch `main`. HEAD and all six parents match the declared SHAs. Porcelain is clean and `[ahead 1]`. Local `origin/main` is `e9943b56b0bb97402fd64ac2143f1cf2fe07401f`, with no fetch. That matches the Orchestrator's stated public-main observation of `e9943b5`; this session did not re-contact the network. `.ap` HEAD and the gitlink are both `d7023cf037f6d17885c3ede5c04812c61640da50`.

C02 PASS. `git diff --name-only e64f2b0..2c4f4d8` is exactly the 24 paths above. `git diff --name-only e9943b5..2c4f4d8` is exactly the 9 unread paths above. `git diff --name-only e64f2b0..2c4f4d8 -- src` is only the three web-shell assets. No manifest, Alembic, or backend API/schema path is in the diff.

C03 PASS. `git diff e64f2b0..2c4f4d8 -- extension/manifest.json` is empty. Required `permissions` are exactly `alarms`, `sidePanel`, and `storage`. The file has no `notifications`, no `host_permissions`, and no `externally_connectable`. `optional_permissions` remains the pre-existing `downloads` entry and `optional_host_permissions` remains `https://*.ts.net/*`; neither was added by this range.

C04 PASS. No backend, schema, migration, API route, or `tailscale_ingress.py` path changed. The unchanged policy file has exactly six `companion_mutation=True` routes: `PUT /api/admin/settings/automatic-analysis`, `POST /api/youtube/requests`, `POST /api/companion/review-inbox/{media_id}/opened`, `POST /api/companion/review-inbox/{media_id}/apply`, `POST /api/x/requests`, and `POST /api/x/requests/{claim_id}/retry`. `REVIEW_INBOX_OPENED` remains the existing `"review_inbox_opened"` message and that existing opened route. `TYPES` gained no message. The alarm remains `kronika.review-inbox`. `STORAGE` remains `kronikaOrigin`, and the worker storage reads added in this range use that existing key. `configurationRevision` is in memory. No download snapshot is written with `chrome.storage.local.set`.

C05 PASS. `REVIEW_INBOX` remains `"review_inbox"`. The sidebar still sends that type with payload `{}`. A successful `reviewInbox()` return adds `downloads`. `failedDownloadProjection()` is exactly `{ok:false, items:[]}`. A successful window with no retained rows is `{ok:true, items:[]}`. No second download message type or transport was added.

C06 PASS. `handle()` calls `reviewInbox()` only after `isSidebarReviewSender(sender)`. That check requires `sender.id === chrome.runtime.id`, `sender.url` equal to `ui/sidebar.html`, and `sender.origin` equal to that document's origin. A missing or mismatched sender returns `invalidSenderReviewResult()` and does not call `clearBadgeText()`. The test `spoofed review_inbox senders fetch nothing and keep the badge` passed.

C07 PASS. Download reads call `pathFor("xRequests")` and `pathFor("youtubeRequests")`, which return the fixed `/api/x/requests` and `/api/youtube/requests` templates, joined to the route origin. The suffix is `?limit=` plus `DOWNLOAD_HISTORY.readLimit` (50). `readCapabilityDownloadList` does not pass a caller path, id, or cursor. `readDownloadWindow` performs one call per present capability and does not follow a cursor. A missing `x.request` or `youtube.request` capability skips that source. The test `download read window uses limit 50, ignores cursors, and keeps the retained rows` passed.

C08 PASS. The sanitized item keys are exactly `source`, `request_id`, `label`, `status`, `media_id`, and `sort_at_ms`. `created_at_ms` is not a projection field. `representativeCatalogedMediaId` keeps cataloged assets with UUID media ids and finite ordinals, sorts by ordinal then index, and takes the first. `nullableDownloadMediaId` returns a UUID or null, so an invalid non-null media id becomes null. YouTube uses that helper on the request media id. The test `download media id selects the first cataloged X asset and the YouTube request id` passed.

C09 PASS. `downloadSortAt` uses a nonnegative safe-integer `updated_at_ms`, otherwise a valid `created_at_ms`, and the X and YouTube item builders omit the row when that value is null. `mergeDownloadHistoryItems` deduplicates on `(source, lowercased request_id)`, sorts by `sort_at_ms` descending, source ascending, and request id descending, then returns `slice(0, DOWNLOAD_HISTORY.readLimit)`. The tests `download merge keeps the retained window, first duplicate, and deterministic ties` and `download sort prefers updated_at_ms and keeps an older request that was updated later` passed.

C10 PASS. X maps `submitted`, `queued`, `extracting`, `acquiring`, `handing_off`, `completed`, `completed_partial`, `duplicate_resolved`, `failed`, and `catalog_removed`, matching `XAcquisitionState`. YouTube maps `queued`, `processing`, `downloading`, `completed`, `completed_private`, `failed`, and `unavailable`, matching the requester phases. An unmapped or malformed row returns null. Status comes only from those maps. A cataloged media id, analysis flag, or publication field does not change the status. The test `download rows map every accepted state and reject unknown or unsafe fields` passed.

C11 PASS. An own UUID media id renders a `button` with class `download-history-row download-history-row--action`, type `button`, the three spans for source, label, and status, and an accessible open action. Its click calls `openHostedDetails`, which posts one `open_details` message with that media id. The handler does not retry or remove the row, and the button remains after a read refresh. A null media id renders a non-focusable `div.download-history-row` with no click listener. The test `own-media download rows open hosted details per click and stay clickable after a read save` passed. Unread rows add the marker spans covered by C15; a matched read row in `matched unread download row posts opened once and clears the marker` has exactly the action class and the open-details label, and stays present.

C12 PASS. `DOWNLOAD_HISTORY.limit` is 5. `presentHistory` renders the first five downloads in `#download-history-list` and the remainder in `#download-history-expanded`. While downloads exist, `#download-history-all` is the only visible All: `#review-history-all` is hidden and its `aria-expanded` is forced false. Expanding reveals the later retained downloads, including the sixth and the last retained row, and both review lists. Collapsing returns to the five-download sheet. There is no second All control. `onHistoryToggle` still opens and closes `#review-history`, and closing clears the download expansion. The tests `compact history shows five downloads, one All, then deduplicated review rows`, `one download All reveals later downloads and the complete review history`, and `download All toggles retained rows without a new inbox request` passed.

C13 PASS. With no downloads, `#download-history` and the download All stay hidden, `downloadHistoryExpanded` is cleared, and the review compact list plus `#review-history-all` keep the existing five-then-All behavior. With downloads and no review rows, the download All expands only the later download list. The same compact-history and one-All tests cover those states.

C14 PASS. `reviewItemsOmittingDownloadMedia` drops a review item whose media id matches any download media id, case-insensitively, from the items passed to both review lists. A distinct review media id remains. A null download media id is not added to the covered set. In `matched unread download row posts opened once and clears the marker`, `Fresh save` and `Read save` are absent from the compact review list, `Distinct review` remains, and `Pending review` remains in the expanded list.

C15 PASS. `unreadRunByMediaId` matches only an analyzed unread review item with a UUID `analysis_run_id`. That download row gets `download-history-row--unread`, the accent rule in `sidebar.css`, a visible dot, and the text `Unread` in both `aria-label` and a clipped span. The click posts one `open_details` and one existing `REVIEW_INBOX_OPENED` for that analysis run, then refreshes. A second click before refresh does not post a second opened. After the refreshed unopened-false state, the marker is gone and a further click posts no opened. The row remains. A read match posts `open_details` and no opened. The inert null-media row is a `div` and posts neither. The test `matched unread download row posts opened once and clears the marker` passed.

C16 PASS. Review-only, download-only, empty, failed, and mixed states are covered by `presentHistory` and the compact-history test. A failed download projection hides `#download-history` while the review items still render, and `reviewInbox()` still applies the badge from `unopened_count`. `failedReviewInbox` clears the badge and returns `ok: false`, so `presentHistory` hides the whole history sheet. The test `one failed download source hides every download row and keeps review and badge` passed, as did `REVIEW_INBOX rejects cursor cycles and later-page failures without partial titles`.

C17 PASS. `aggregationContextMatches` re-reads origin, configuration revision, login, the three history capabilities, and history source. A login change with identical capabilities returns `staleContextReviewResult()` before the badge update, so the previous badge text stays. The test `changed identity login discards the in-flight history result without clearing the badge` passed, as did the capability-change twin. `refreshInbox` returns while `inboxRefreshActive` is true, and a changed `inboxGeneration` discards the late result. A hidden document stops the poll in both the interval callback and `visibilitychange`. `connect`, `reset`, and runtime invalidation call `retireInboxGeneration()`, which clears both download lists, hides the section, and sets the download All `aria-expanded` to false. The test `sidebar skips overlapping refreshes, stops hidden polling, and drops late results` passed.

C18 PASS. Download reads use `GET /api/x/requests` and `GET /api/youtube/requests` for the signed-in requester. Administrator review items stay on the review-inbox history source and are not copied into the download projection. The projection keeps source, request id, bounded label, status, own media id, and sort timestamp. The sidebar renders source, label, and status text, plus the unread marker when C15 matches. It does not render a raw URL, asset array, media filename, provider payload, or failure detail. The only linked media is the row's own cataloged UUID. No download snapshot is stored. The test `ordinary own-history and administrator inbox both keep separate own downloads` passed, and `download rows map every accepted state and reject unknown or unsafe fields` rejects unsafe fields.

C19 PASS. `applyBadgeFromResponse` uses `unopenedCountFromBody`. Download outcomes are not added to that count. The alarm listener calls only `refreshReviewInboxBadge()`, which fetches the review source at `badgeLimit` and does not call `readDownloadWindow`. The manifest has no `notifications` permission and no second counter. The existing opened mutation may clear the marker and the review badge after a matched download-row click, which C15 pins. The test `badge alarm refresh does not call download lists` passed.

C20 PASS. `SPEC.md`, `docs/X_COMPANION.md`, and `DEVELOPMENT.md` state compact five, retained fifty, one All, the sixth and last retained rows, deduplicated review, the unread marker and existing opened behavior, own-media click, inert no-media rows, latest-update order, and the review-only badge. `PRODUCT.md` states the same behavior, using "later retained downloads" for the window that the other three bound at fifty. `SECURITY.md` states the own-list read, the sanitized projection, the omitted invalid media id, sidebar-only `review_inbox`, existing `open_details`, and that no download snapshot or new mutation is added. It does not restate the compact-five or unread presentation, and it does not contradict them. ADR-0092 status is `Accepted`, and `docs/adr/README.md` indexes it as supplementing ADR-0091. `git log` shows ADR-0090 only in `b543602` and ADR-0091 only in `e9943b5`, so neither body is in the unread commit.

C21 PASS. Companion rules hide `.kronika-chronicle__glyph`, show `.kronika-chronicle__reading`, and keep Kind, Status, and Visibility labels readable. Rows are built with `kronikaChronicleLabeled` for Kind and `kronikaChronicleSignal` for Status and Visibility. Companion title rules set wrapping and `line-clamp: none`. The wide title rule remains `-webkit-line-clamp: 2` and the wide chronicle header remains. The Filter button is one `type="button"` for `#kronika-timeline-filters`. The form starts with `is-collapsed` and `aria-expanded="false"`. Its click only toggles `is-collapsed` and `aria-expanded`. The four menus are publication, kind, status, and visibility. The only collapsed-hide rule is under `.kronika-companion-hosted`. The wide page hides the button with `.kronika-chronicle-filter-toggle { display: none }` and does not hide the filters. The test `companion Timeline text and Filter disclosure stay off the wide page` passed.

C22 PASS. Companion My contributions sets `.workspace-media-browser .admin-media-row` to `minmax(0, 1fr)` and the title and metadata to block layout, full width, `overflow-wrap: break-word`, `word-break: normal`, and `white-space: normal`. The wide `.workspace-media-browser .admin-media-row` grid stays four columns. The test `companion My contributions title fills the row and the wide grid stays` passed. The styles diff adds companion-hosted rules and does not replace that wide grid.

C23 PASS. Wide Timeline glyphs, the two-line title clamp, the visible filters, and the multi-column contributions grid remain outside `.kronika-companion-hosted`. The full-page narrow My contributions LEAD is outside this companion boundary and is recorded under residual risks. It did not fail a selected check.

C24 PASS. Actual counts match the declared evidence: focused Python 46, focused Node 118, broader Python 206, broader Node 64, compact UI Node 44, affected frontend Node 287, served-shell Python 211. All failed counts are 0.

C25 PASS. `git diff --check e64f2b0..2c4f4d8` is clean. The worktree after validation is clean and still ahead 1. The committed path lists match C02. Relative links in the changed Markdown files resolve to existing files.

C26 PASS. `08_report_00.md` is the trace report for `e9943b5`. Its saved text includes the complete correction report and a trailing note that an empty destination already existed and states `File delivery: collision`. `02_report_01.md` records status BLOCKED, no service-worker edit, and no repository change. Neither file is in the candidate diff. `git ls-files` finds no `02_rereport_00.md` in the repository, and the trace directory listing has `02_report_00.md`, `02_report_01.md`, and `02_report_02.md` with no `02_rereport_00.md`.

C27 PASS. The residual YouTube acquisition `INSPECTION_OUTPUT_LIMIT`, the X acquisition failures and «Save to Kronika failed» outcome, and the full-page narrow My contributions LEAD are outside the allowlist and did not fail a selected check. This report records the independent acceptance phase result only. It does not claim publication, deployment, production acceptance, or closure. The Orchestrator owns the accept decision.

## Deviations, risks, and residuals

Defects: none.

Residual risks, outside this acceptance:

- YouTube acquisition `INSPECTION_OUTPUT_LIMIT` and the X acquisition failure outcome, including «Save to Kronika failed», remain outside this companion candidate. The selected YouTube and X lifecycle tests passed.
- The full-page narrow My contributions layout remains an out-of-scope LEAD. Companion-hosted rows use their own single-column rule.
- Rendered companion behavior was not exercised. This grant forbids browser evidence. Public `main` was not contacted; the local tracking ref matches the stated observation. Local `main` is one commit ahead of `origin/main`.

Orchestration critique:
MEASURED: none
LEAD: none

Proposed next step: the Orchestrator decides whether to accept this phase result. Publication of `2c4f4d89375628df28926060aba305e5d80bacff` and the Cooperator's rendered pass remain separate later decisions.

Authority expiry: this acceptance grant expires with this terminal report. A green test run and this phase result are not publication, deployment, production acceptance, or closure authority.
