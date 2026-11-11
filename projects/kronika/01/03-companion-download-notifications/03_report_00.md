### Report for ORCHESTRATOR_CHAT

Logical whole identity: companion-download-notifications
Worker session ordinal: 03
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: ACCEPT-COMPANION-DOWNLOAD-NOTIFICATIONS-01
status: PASS
Phase-qualified result: acceptance-PASS
Start commit: 647e6da11416559f1bef52d53e9743acbd2bb688
End commit: 647e6da11416559f1bef52d53e9743acbd2bb688
Candidate: 647e6da11416559f1bef52d53e9743acbd2bb688
Parent: cc8f67965213ee9b22d113cc200776c42f6503ba
Grandparent: e64f2b0f92458fac2590e03672e30da62275b345
Report justification: final-acceptance
Logical-whole closure: not-closed

Acceptance candidate: 647e6da11416559f1bef52d53e9743acbd2bb688
Acceptance owner map: companion-download-notifications-v1
Acceptance allowlist: the 15 paths named in the grant
Acceptance risk claims: R1–R8, independently rechecked below
Acceptance control matrix: C01–C22
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates

Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/03-companion-download-notifications/03_report_00.md
Git result: read-only. No fetch, stage, commit, push, reset, clean, or checkout.
Changed files: none. The repository worktree stayed at the candidate. This report is the only granted write, and it is outside the repository.

The candidate is two local commits on `main`: `cc8f67965213ee9b22d113cc200776c42f6503ba` (`Surface own download status in companion history`) and `647e6da11416559f1bef52d53e9743acbd2bb688` (`fix: bind download history to the identity context`). Their combined purpose is a read-only Recent downloads block inside the existing companion history sheet, plus the identity-login stale-context correction. This phase result does not publish, deploy, or close the whole.

## Independence

This session did not implement `cc8f679` and did not author the correction `647e6da`. Prior plan and implementation reports were read as claims. The matrix below is from the local objects, the candidate tree, and the granted commands. Network, browser, NUC, provider, and secret paths were not used.

## Validation

Governing AP pin `d7023cf037f6d17885c3ede5c04812c61640da50` matches the `.ap` gitlink and `.ap` HEAD.

`./.ap/ap project check --baseline e64f2b0f92458fac2590e03672e30da62275b345` returned `ap project check --baseline: PASS` for project `cisarik/kronika`, contract schema 1, CPython 3.13.

`./.ap/ap exec --baseline e64f2b0f92458fac2590e03672e30da62275b345 --operation runtime-info` returned `/Users/agile/Projects/kronika/.venv/bin/python`, `3.13.14`, and `/Users/agile/Projects/kronika/src/kronika/__init__.py`.

Focused Python: 46 passed in 10.56s, exit 0. Files: `tests/contract/test_x_request_api.py`, `tests/contract/test_youtube_request_api.py`, `tests/contract/test_companion_review_api.py`.

Focused Node: tests 110, pass 110, fail 0, exit 0. Files: `tests/companion_review_extension.test.js`, `tests/x_companion_extension.test.js`.

Broader Python: 206 passed in 54.51s, exit 0. The seven files named in the grant.

Broader Node: tests 64, pass 64, fail 0, exit 0. TAP plan `1..61` plus three nested subtests (`web_ready`, `host_ack`, `attach_request`) accounts for the summary total of 64. Files: `tests/companion_web_bridge.test.js`, `tests/companion_settings_automatic_analysis.test.js`, `tests/youtube_request_cockpit.test.js`, `tests/youtube_acquisition_cockpit.test.js`, `tests/x_acquisition_cockpit.test.js`.

`git diff --check e64f2b0..647e6da` exit 0. After these commands, `git status --porcelain=v1 -uall -b` was `## main...origin/main [ahead 2]` with no other lines. `git diff --cached --name-only` was empty.

## Control matrix

C01 PASS. Local `origin` is `https://github.com/cisarik/kronika.git`. `status --porcelain=v1 -b` is `## main...origin/main [ahead 2]` and clean. `HEAD` is `647e6da11416559f1bef52d53e9743acbd2bb688`, `HEAD^` is `cc8f67965213ee9b22d113cc200776c42f6503ba`, `HEAD^^` is `e64f2b0f92458fac2590e03672e30da62275b345`. The stored `origin/main` ref is that grandparent. No fetch was run; the public-main observation is the local remote-tracking ref, which matches the declared value. `.ap` HEAD and the gitlink are both `d7023cf037f6d17885c3ede5c04812c61640da50`.

C02 PASS. `git diff --name-only e64f2b0..647e6da` is exactly the 15 allowlist paths, 1625 insertions and 59 deletions. `git diff --name-only cc8f679..647e6da` is exactly `extension/background/service_worker.js` and `tests/companion_review_extension.test.js` (9 and 32 lines). `git diff --name-only e64f2b0..647e6da -- src` is empty. `extension/manifest.json` has an empty diff.

C03 PASS. `extension/manifest.json` is outside the diff. `permissions` is exactly `["alarms", "sidePanel", "storage"]`. The file has no `notifications`, no `host_permissions`, and no `externally_connectable`. Pre-existing `optional_permissions: ["downloads"]` and `optional_host_permissions: ["https://*.ts.net/*"]` are unchanged, so no new optional permission was added. The manifest test at `tests/companion_review_extension.test.js` asserts the same required-permission and absence checks.

C04 PASS. No path under `src`, Alembic, or an API module is in the diff. `companion_mutation=True` remains on exactly six policies in `src/kronika/adapters/api/tailscale_ingress.py`: `PUT /api/admin/settings/automatic-analysis`, `POST /api/youtube/requests`, `POST /api/companion/review-inbox/{media_id}/opened`, `POST /api/companion/review-inbox/{media_id}/apply`, `POST /api/x/requests`, and `POST /api/x/requests/{claim_id}/retry`. The messages diff adds no `TYPES` member, no `STORAGE` key, and no alarm name. The only alarm remains `kronika.review-inbox`. The persisted origin key remains `kronikaOrigin`.

C05 PASS. `TYPES.REVIEW_INBOX` remains `"review_inbox"`. `reviewInbox()` returns `downloads` on the same response. `readDownloadWindow()` returns `{ok:true, items}` after a successful read, including a successful empty merge. `failedDownloadProjection()` is exactly `{ok:false, items:[]}`. No second message type or transport was added. Tests `history shows own terminal X and YouTube request states`, `downloads follow caller capabilities`, and `one failed download source` pin the three shapes.

C06 PASS. `handle()` passes `sender` and, only for `REVIEW_INBOX`, returns `invalidSenderReviewResult()` unless `isSidebarReviewSender()` matches `sender.id`, `sender.url`, and `sender.origin` to `ui/sidebar.html`. That result sets `error: "invalid_sender"`, empty items, and a failed download projection, and it does not call `clearBadgeText()` or `fetch`. The other `handle()` arms are unchanged. Test `spoofed review_inbox senders fetch nothing and keep the badge` covers a missing sender and mismatched id, url, and origin, and leaves badge text `"4"` with no new fetch.

C07 PASS. `readCapabilityDownloadList()` calls `fetchJson` with fixed names `xRequests` and `youtubeRequests`. `pathFor()` returns `/api/x/requests` and `/api/youtube/requests` with no caller id. The suffix is `?limit=5` from `DOWNLOAD_HISTORY.limit`. No `next_cursor` is read or followed. Absent `xRequest` or `youtubeRequest` skips that call. A caller payload url, cursor, limit, or path is ignored. YouTube-only identities still fail the pre-existing history route (`workflowRead`, then `x.request`) before any download read; the accepted plan keeps that eligibility, and the capability test pins it.

C08 PASS. `mergeDownloadHistoryItems()` drops rows that fail `sanitizeDownloadHistoryItem()`, dedupes on `source + request_id.toLowerCase()` keeping the first, sorts by `created_at_ms` descending, source ascending, request id descending, and slices to five. X labels use the canonicalized claim title or `X post <id>` from `acceptXPostId()`. YouTube labels use `YouTube video <videoId>` from `acceptYouTubeVideoUrl()` and do not fetch media detail. `canonicalizeCompanionAliasTitle()` bounds the label to 240 code points. Test `download merge keeps five rows, first duplicate, and deterministic ties` pins the order `First sight`, `Newer id`, `Older X`, then the YouTube row, and keeps the first duplicate status `failed`.

C09 PASS. X `submitted`, `queued`, `extracting`, `acquiring`, and `handing_off` map to `saving` / `Saving…`. X and YouTube `completed` map to `saved` / `Saved`. YouTube `completed_private` maps to `saved_private` / `Saved privately`. X `completed_partial` maps to `partial` / `Partly saved`. X `duplicate_resolved` maps to `already_saved` / `Already saved`. Terminal `failed` maps to `failed` / `Download failed`. X `catalog_removed` and YouTube `unavailable` map to `unavailable` / `Unavailable`. Unknown or malformed rows return null, including X `completed_private`, YouTube `cataloged`, a non-YouTube URL, and an unsafe timestamp. Analysis and publication fields are not status inputs. Test `download rows map every accepted state and reject unknown or unsafe fields` exercises the table.

C10 PASS. `extension/ui/sidebar.html` places `#download-history` inside `#review-history`, with heading `Recent downloads` and inert `#download-history-list`. Download rows are `li` plus three `span` nodes. No download click listener exists; click listeners stay on the review lists, All, toggle, and chrome controls. `#review-history::before` content is `Companion history`. Review list labels are `Recent review history` and `Full review history`. The All control's accessible name is `Show full review history` and its visible text is `All`. Test `title-bar merged history has the accepted DOM, ARIA, and status contract` matches these strings, and `sidebar download rows are inert` rejects `BUTTON` and `A` in the download list and rejects `open_details`, `innerHTML`, and a button or link in that HTML slice.

C11 PASS. The toggle starts `disabled` with `aria-expanded="false"`, and `#review-history` starts `hidden`. `historyUserExpanded` starts false. `renderReviewCollections()` enables the toggle when review rows or download rows exist, reopens only that remembered choice, and sets All `hidden` when there is no review history. Empty or failed downloads set `#download-history` hidden; CSS `#download-history[hidden]` is `display: none`, and an empty download list is `display: none`. Test `history stays closed by default and only the toggle changes it across refreshes` keeps the sheet closed, then open across a second render. Download-only presentation hides All.

C12 PASS. Review-only hides the download section and keeps the review row. Download-only enables the toggle, hides All, and renders status text. A missing or `{ok:false}` download projection hides the block and keeps the review row. `{ok:false}` for the review result clears both lists and disables the toggle. A YouTube 503 makes `downloads` exactly `{ok:false, items:[]}` while the review item `Bob analyzed`, `unopened_count` 2, and badge `"2"` remain. Review cursor and later-page failures still go through `failedReviewInbox()`, which calls `clearBadgeText()` and returns no items. Mixed coexistence is the same `presentHistory()` path: the administrator and ordinary worker tests keep review titles and own download labels in one successful response, and the two render arms do not clear each other.

C13 PASS. `aggregationContextMatches()` re-reads origin and `configurationRevision`, re-fetches identity, and returns false on login mismatch, capability mismatch, or history-source mismatch. `configureOrigin()` and `resetState()` increment `configurationRevision`. A mismatch returns `staleContextReviewResult()` before `applyBadgeFromResponse()`, with `stale: true`, `ok: false`, empty review items, and a failed download projection. `presentHistory()` hides both collections when `stale` is true. The capability-change test and the login-change test are separate. The login test changes `alice` to `bob` with the same capability array and asserts `stale`, `ok: false`, empty review items, empty download items, and badge text left at `"9"`.

C14 PASS. `refreshInbox()` returns immediately while `inboxRefreshActive` is true and discards a response whose captured generation differs. A hidden document makes the poll callback return, and `visibilitychange` calls `stopInboxPoll()`. `connect()`, `reset()`, and the runtime-stale handler call `retireInboxGeneration()`, which clears the download list and hides `#download-history`. Test `sidebar skips overlapping refreshes, stops hidden polling, and drops late results` keeps the in-flight count at 1, clears the interval when hidden, and leaves both lists empty after a late successful payload following Disconnect.

C15 PASS. Download rows are built only from `list_owned` responses on `GET /api/x/requests` and `GET /api/youtube/requests`, keyed by the caller login. Administrator review titles stay on `items` and are absent from `downloads`. The sanitized item keys are `source`, `request_id`, `label`, `status`, and `created_at_ms`. The projection test rejects `evil.example`, `SECRET`, `assets`, and the media id. No download snapshot is written to storage. `test_owned_x_list_and_detail_follow_the_caller` and `test_owned_youtube_list_and_detail_follow_the_caller` pass for two ordinary logins and an administrator, with list calls bound to that login and no login-key field in the list body.

C16 PASS. `applyBadgeFromResponse()` uses `unopenedCountFromBody()` only. Download failure does not change that count. `refreshReviewInboxBadge()` fetches the history route with `badgeLimit` and does not call `readDownloadWindow()`. The alarm listener ignores every name other than `kronika.review-inbox` and calls only that badge refresh. Test `badge alarm refresh does not call download lists` finds no `/api/x/requests` or `/api/youtube/requests` fetch and asserts the three manifest permissions. There is no second counter and no `notifications` permission.

C17 PASS. The correction diff adds `identityLoginFromBody()`, stores `login` on the route, and compares it inside `aggregationContextMatches()` before the capability comparison. The new test is `changed identity login discards the in-flight history result without clearing the badge`. The older capability-change test remains a separate test and still expects `stale`, empty collections, and an unchanged badge.

C18 PASS. `SPEC.md` keeps X-only own-history and a badge taken only from `unopened_count`, adds the bounded Recent downloads block and its failure isolation, narrows `open_details` to review rows, and states that complete review pagination stays fail-closed. `PRODUCT.md`, `docs/X_COMPANION.md`, `SECURITY.md`, and `DEVELOPMENT.md` describe the same block, inert rows, own-request reads, and review-only badge. ADR-0089 is `Accepted`, indexed in `docs/adr/README.md`, and the ADR-0076 index row records supplementation. ADR-0076's body is not in the diff. `docs/UX_AUDIT.md` is not in the diff. None of the seven changed documents still says every history row opens Details.

C19 PASS. Counts match the grant: focused Python 46, focused Node 110, broader Python 206, broader Node 64. All four commands exited 0. No failure signature.

C20 PASS. `git diff --check` is clean. The worktree and index are clean after validation. Both commit path lists match C02. Relative Markdown links in the seven changed documents resolve on disk.

C21 PASS. `02_report_01.md` records status BLOCKED, no service-worker edit, no test edit, and no commit, in a session whose first grant was a different logical whole. `02_rereport_00.md` is a `bookradar-persistence-and-history-slice` trace report. `git ls-files` in this repository contains neither file. This session only read them.

C22 PASS. This report records `acceptance-PASS` as the phase result only. It does not claim publication, deployment, production acceptance, or logical-whole closure. Closure remains `not-closed`.

## Defects and residual risks

Defects: none.

Residual risks: rendered companion behavior and the NUC were outside this grant, so they remain for a later Cooperator pass after publication and routine refresh. Local `main` is two commits ahead of the stored `origin/main`; that is unpublished state, not a defect in the candidate. A YouTube-only identity still has no history route, which the accepted plan retains.

## Orchestration critique

MEASURED: none
LEAD: none

Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none

Smallest next step: the Orchestrator records this acceptance decision. Publication, deployment, and closure need their own grants.

Authority expiry: this terminal report ends the grant; no autonomous continuation.
