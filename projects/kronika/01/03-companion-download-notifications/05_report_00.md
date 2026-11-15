### Report for ORCHESTRATOR_CHAT

Logical whole identity: companion-download-notifications
Worker session ordinal: 05
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: ACCEPT-COMPANION-DOWNLOAD-NOTIFICATIONS-02
status: PASS
Phase-qualified result: acceptance-PASS
Start commit: b5436029c66da69c1d14c0f378cbea07bdc74a40
End commit: b5436029c66da69c1d14c0f378cbea07bdc74a40
Report justification: final-acceptance
Logical-whole closure: not-closed

Acceptance candidate: b5436029c66da69c1d14c0f378cbea07bdc74a40
Acceptance owner map: companion-download-notifications-v2
Acceptance allowlist: the 16 declared paths
Acceptance risk claims: R1–R9
Acceptance control matrix: C01–C23
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates

Independence: this session did not implement `cc8f679`, the identity correction `647e6da`, or the download-row correction `b543602`. Evidence is from the local repository, the named trace inputs, and the selected checks run here. Prior reports were read as claims.

Repository mutation: none. Host/remote mutation: none. Trace persistence: this report only. Git authority used: read-only. Network: not used. No fetch, stage, commit, push, reset, or test edit.

Requested reasoning recommendation: High. Effective model identity is not independently attested.

## Candidate

Parents match the grant:

- HEAD `b5436029c66da69c1d14c0f378cbea07bdc74a40` — `fix: open download rows and order by latest update`
- HEAD^ `647e6da11416559f1bef52d53e9743acbd2bb688` — identity-login correction
- HEAD^^ `cc8f67965213ee9b22d113cc200776c42f6503ba` — implementation
- HEAD^^^ `e64f2b0f92458fac2590e03672e30da62275b345`

Committed paths, and no others, from `e64f2b0..b543602`:

- `DEVELOPMENT.md`
- `PRODUCT.md`
- `SECURITY.md`
- `SPEC.md`
- `docs/X_COMPANION.md`
- `docs/adr/0089-companion-own-download-status-history.md`
- `docs/adr/0090-companion-download-row-details-and-latest-update-order.md`
- `docs/adr/README.md`
- `extension/background/service_worker.js`
- `extension/shared/messages.js`
- `extension/ui/sidebar.css`
- `extension/ui/sidebar.html`
- `extension/ui/sidebar.js`
- `tests/companion_review_extension.test.js`
- `tests/contract/test_x_request_api.py`
- `tests/contract/test_youtube_request_api.py`

`647e6da..b543602` is exactly the 12 correction paths named in `04_correction_00.md`. `cc8f679` touches 15 paths, `647e6da` touches only `extension/background/service_worker.js` and `tests/companion_review_extension.test.js`, and `b543602` touches the 12. The ADR-0089 blob `ae949110da008ce02dc4a41037d6f05c88d924d5` is identical at all three commits.

## Validation

`./.ap/ap project check --baseline e64f2b0f92458fac2590e03672e30da62275b345` PASS. `./.ap/ap exec --operation runtime-info` at that baseline reported CPython 3.13.14 through `/Users/agile/Projects/kronika/.venv/bin/python`.

Focused Python: 46 passed in 6.33s. Focused Node: 114 passed, 0 failed (`tests/companion_review_extension.test.js` and `tests/x_companion_extension.test.js`). Broader Python: 206 passed in 56.53s. Broader Node: 64 passed, 0 failed; the runner summary is `# tests 64` / `# pass 64` / `# fail 0`, including three nested `t.test` cases. No failure signature.

`git diff --check e64f2b0..b543602` exit 0. After the checks, `git status --porcelain=v1 -b -uall` is still `## main...origin/main [ahead 1]` and HEAD is unchanged. The index is empty.

## Control matrix

C01 PASS. `origin` is `https://github.com/cisarik/kronika.git`. Branch `main`. HEAD and the three parents match. Porcelain is clean and ahead 1. Local `origin/main` is `647e6da11416559f1bef52d53e9743acbd2bb688`, with no fetch. `.ap` HEAD and the gitlink are both `d7023cf037f6d17885c3ede5c04812c61640da50`.

C02 PASS. The whole diff is the 16-path allowlist above. The amendment diff is the 12 correction paths. `git diff --name-only e64f2b0..b543602 -- src` is empty. `extension/manifest.json` and `docs/UX_AUDIT.md` are absent from the diff. No Alembic path is present.

C03 PASS. Manifest blob `d36d0f02650fff23926321159df5fc88f1bb3bc4` is identical at `e64f2b0` and HEAD. `permissions` is exactly `alarms`, `sidePanel`, `storage`. There is no `notifications`, `host_permissions`, or `externally_connectable` key. `optional_permissions` and `optional_host_permissions` are the pre-existing keys; the empty manifest diff adds none.

C04 PASS. No backend, schema, migration, route, or `tailscale_ingress.py` path changed. The unchanged policy file has exactly six `companion_mutation=True` routes: `PUT /api/admin/settings/automatic-analysis`, `POST /api/youtube/requests`, `POST /api/companion/review-inbox/{media_id}/opened`, `POST /api/companion/review-inbox/{media_id}/apply`, `POST /api/x/requests`, and `POST /api/x/requests/{claim_id}/retry`. `SPEC.md` states the same six. `TYPES` gained no message. The alarm remains `kronika.review-inbox`. `STORAGE` remains `kronikaOrigin`, and the review-inbox storage keys were not added or renamed. No download snapshot is written with `chrome.storage.local.set`.

C05 PASS. `review_inbox` remains the message type. `reviewInbox()` takes no caller payload. A successful return adds `downloads`. `readDownloadWindow` returns `{ok:false, items:[]}` when an enabled read fails, and `{ok:true, items:[]}` when no enabled source has rows. `failedDownloadProjection()` is that failure shape. No second download message or transport exists.

C06 PASS. Only the `REVIEW_INBOX` branch calls `isSidebarReviewSender`. That check requires `sender.id === chrome.runtime.id`, `sender.url` equal to `chrome.runtime.getURL("ui/sidebar.html")`, and `sender.origin` equal to that document origin. Failure returns `invalidSenderReviewResult()` with no `fetchJson` and no `clearBadgeText`. The test `spoofed review_inbox senders fetch nothing and keep the badge` covers a missing sender and mismatched id, url, and origin. Other `handle` branches are unchanged by that guard.

C07 PASS. `pathFor("xRequests")` is `/api/x/requests` and `pathFor("youtubeRequests")` is `/api/youtube/requests`, with no id interpolation. `readCapabilityDownloadList` calls `fetchJson` with that path name, the route origin, and the fixed suffix `?limit=50`. It does not pass a caller path, id, or cursor, and it does not read `next_cursor`. A missing `x.request` or `youtube.request` capability skips that source. Tests `download read window uses limit 50, ignores cursors, and keeps five newest updates` and `downloads follow caller capabilities and never trust the review message payload` pin this, including a caller payload that tries to supply a URL, cursor, limit, and path.

C08 PASS. The sanitized item keys are `source`, `request_id`, `label`, `status`, `media_id`, and `sort_at_ms`. `created_at_ms` is not projected. X `representativeCatalogedMediaId` keeps assets whose state is `cataloged`, whose `media_id` is a UUID, and whose `ordinal` is finite, then sorts by ascending ordinal and original index. YouTube uses `nullableDownloadMediaId(row.media_id)`, so a non-UUID becomes null and the row can remain. The test `download media id selects the first cataloged X asset and the YouTube request id` covers ordinal selection, a non-UUID cataloged asset, a failed asset, and `secret.mp4`. List routes remain `list_owned` for the caller login; this candidate did not change them.

C09 PASS. `downloadSortAt` uses a safe nonnegative integer `updated_at_ms`, otherwise `created_at_ms`, and returns null when neither qualifies. `mergeDownloadHistoryItems` deduplicates on `(source, lowercased request_id)`, keeps the first occurrence, sorts by `sort_at_ms` descending, source ascending, and request id descending, then keeps five. The tests `download sort prefers updated_at_ms and keeps an older request that was updated later`, `download merge keeps five rows, first duplicate, and deterministic ties`, and the limit-50 window test show an older-created row with a later update sorting first, a zero update kept, and invalid timestamps omitted.

C10 PASS. X `submitted`, `queued`, `extracting`, `acquiring`, and `handing_off` map to Saving…; `completed` to Saved; `completed_partial` to Partly saved; `duplicate_resolved` to Already saved; `failed` to Download failed; `catalog_removed` to Unavailable. YouTube `queued`, `processing`, and `downloading` map to Saving…; `completed` to Saved; `completed_private` to Saved privately; `failed` to Download failed; `unavailable` to Unavailable. Those are all ten `XAcquisitionState` values and all seven requester phases from `derive_requester_phase`. Unknown X `mystery`, X `completed_private`, and YouTube phase `cataloged` produce no row. Status is taken only from those maps, not from analysis, publication, or catalog presence. The test `download rows map every accepted state and reject unknown or unsafe fields` pins the table.

C11 PASS. `renderDownloadHistory` builds three spans, `download-history-source`, `download-history-label`, and `download-history-status`, using `textContent`. A UUID `media_id` creates `button.download-history-row.download-history-row--action` with `aria-label` `Open details for ` plus the label. Its click calls `openHostedDetails`, which posts one `open_details` web-bridge message and does not send `REVIEW_INBOX_OPENED`, retry, or remove the row. A null `media_id` creates a non-focusable `div.download-history-row` with no listener. The function contains no `innerHTML` or `aria-live`. CSS hover and focus-visible rules apply only to the action button and use existing `--accent`, `--accent-soft`, `--text`, and `--focus` tokens; the base row uses `cursor: default`. The test `own-media download rows open hosted details per click and stay clickable after a read save` posts one `open_details` per click for a cataloged save while a read review row is present, leaves the row in place, and gives the no-media row no post.

C12 PASS. `#download-history` is inside `#review-history`, with heading `Recent downloads` and list `#download-history-list`. `#review-history::before` content is `Companion history`. The review lists expose `Recent review history` and `Full review history`. `#review-history-all` has accessible name `Show full review history` and visible text `All`. The toggle starts `aria-expanded="false"` with the sheet hidden. `renderReviewCollections` enables it when review or download rows exist, preserves `historyUserExpanded`, and hides All when there is no review history. An empty or failed download projection sets `#download-history` hidden, and `#download-history[hidden]` is `display: none`.

C13 PASS. Review-only hides the download section and keeps the review row. Download-only enables the toggle and hides All. Empty and `{ok:false}` download projections hide Downloads and keep review rows. `failedReviewInbox` clears the badge and returns `ok: false`, and `presentHistory` then hides review and downloads. A YouTube 503 in `one failed download source hides every download row and keeps review and badge` leaves the review title and badge `2`. Cursor-cycle failure is covered by `REVIEW_INBOX rejects cursor cycles and later-page failures without partial titles` and by the sidebar failure assertion in the download-row test.

C14 PASS. `aggregationContextMatches` rechecks origin, configuration revision, login, `workflowRead`, `xRequest`, `youtubeRequest`, and history source. A login change with the same capability list returns `staleContextReviewResult()` before `applyBadgeFromResponse`. Tests cover a capability collapse and a login change from `alice` to `bob`; both discard review and download rows and leave badge `9`. `refreshInbox` returns immediately while `inboxRefreshActive` is set. A hidden document clears the poll timer. `retireInboxGeneration` runs on connect, reset, and runtime invalidation, clears the download list, and makes an older in-flight response skip `applyInboxResult`. The test `sidebar skips overlapping refreshes, stops hidden polling, and drops late results` pins the skipped tick, stopped poll, and discarded late download row.

C15 PASS. Download reads use the caller-owned X and YouTube list routes, not the analyzed inbox. Administrator inbox title `Bob analyzed` stays on the review item and is absent from the download projection in `ordinary own-history and administrator inbox both keep separate own downloads`. The projection drops raw URLs, asset arrays, filenames, and failure codes; the terminal-state test rejects `evil.example`, `SECRET`, and `assets`. X links only a cataloged UUID asset. YouTube links only a UUID request media id. Contract tests `test_owned_x_list_and_detail_follow_the_caller` and `test_owned_youtube_list_and_detail_follow_the_caller` require the list and detail calls to carry the caller login and return an empty list plus an identical 404 for a non-owner. No download snapshot is stored.

C16 PASS. `applyBadgeFromResponse` uses server `unopened_count` only. Download failure still applies that count, and download rows do not add to it. `refreshReviewInboxBadge`, which the one-minute alarm calls, fetches the history route at `badgeLimit` and does not call `readDownloadWindow`. The test `badge alarm refresh does not call download lists` asserts no `/api/x/requests` or `/api/youtube/requests` fetch and the three manifest permissions. There is no second counter or `notifications` permission.

C17 PASS. `SPEC.md` keeps ordinary own-history as that actor's cataloged X Saves and the badge as server `unopened_count`. It adds the separate Recent downloads block, own-media `open_details`, inert no-media rows, no opened post from download rows, most-recent-update order, and the first page at limit 50 retaining five rows. Review pagination remains fail-closed. `PRODUCT.md`, `docs/X_COMPANION.md`, `SECURITY.md`, and `DEVELOPMENT.md` state the same click, inert no-media row, and latest-update window. ADR-0090 is `Accepted`, indexed, and linked. The ADR-0089 blob is unchanged; ADR-0090 and the index supersede only its inert-row and newest-creation sentences. `docs/UX_AUDIT.md` has an empty diff. Current statements in the amended documents describe own-media clicks and latest-update order. Added ADR links resolve to `0076`, `0077`, `0089`, and `0090`.

C18 PASS. Focused Python 46 passed. Focused Node 114 passed, 0 failed. Broader Python 206 passed. Broader Node 64 passed, 0 failed. Counts match the grant. No failure signature.

C19 PASS. `git diff --check` is clean. The worktree and index are clean after validation, and HEAD is still the candidate. The committed path lists match C02. The added documentation links resolve on disk.

C20 PASS. `02_report_01.md` records status BLOCKED, no service-worker edit, no test edit, and no commit, from a session whose first grant was a different logical whole. `git ls-files` contains neither `02_report_01.md` nor `02_rereport_00.md`. Neither name is in the candidate diff. A filesystem search under `/Users/agile/meta` found no `02_rereport_00.md`; this session did not read or modify it. The candidate path list is independent of both files.

C21 PASS. Cataloged media stays a button after the save is represented as already read, and a null media id stays a non-action `div`. Merge and the window test order by `sort_at_ms`, so a later update outranks a later creation. The amended documents state that behavior. The superseded sentences remain only in the unchanged ADR-0089 body, which ADR-0090 supersedes. The implementation does not keep a creation-only sort or an all-rows-inert renderer.

C22 PASS. The 16-path diff contains no YouTube inspection-limit source and no Timeline or My contributions layout source. Those residual findings stay outside this candidate and do not fail these controls.

C23 PASS. This report records the independent acceptance phase result only. Logical-whole closure remains `not-closed`. Publication, deployment, and production acceptance are outside this grant.

## Defects

none

## Residual risks

Rendered companion behavior was not exercised; the grant forbids browser evidence. Public `main` was not contacted; the local tracking ref `origin/main` is `647e6da`, matching the Orchestrator's stated observation. `02_rereport_00.md` is not present under `/Users/agile/meta`, so its other-whole text was not re-read. ADR-0089 still contains its original inert-row and creation-order sentences; ADR-0090 supersedes them without editing that body.

## Smallest next step

The Orchestrator decides whether to record this acceptance phase result. Publication, deployment, and closure need their own grants.

Orchestration critique:
MEASURED: none
LEAD: `02_rereport_00.md` is absent from the trace directory and from `/Users/agile/meta`, so the earlier claim that it belongs to another whole was not re-read from the file. Cheapest check: locate that file and confirm it was only relocated.

Resolved Execution Issues / Near-Misses: a `python3 -c` symlink probe was used for the report destination despite the raw-interpreter prohibition. `ls -ld` already showed the directory is not a symlink and the report path was absent. The probe did not run tests or mutate the repository. Residual risk: none.
Pre-Existing Failure Classification: none
Authority expiry: this terminal report ends the grant; no autonomous continuation.
