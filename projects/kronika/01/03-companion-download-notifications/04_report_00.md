### Report for ORCHESTRATOR_CHAT

Logical whole identity: companion-download-notifications
Worker session ordinal: 04
Worker exchange ordinal: 01

## Status

Status: implementation-PASS
Phase-qualified result: implementation-PASS
Logical-whole closure: not-closed
Report justification: new-mutation

Start commit: 647e6da11416559f1bef52d53e9743acbd2bb688
End commit: b5436029c66da69c1d14c0f378cbea07bdc74a40
Parent: 647e6da11416559f1bef52d53e9743acbd2bb688
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50

Fresh correction session. The worktree gate was clean `## main...origin/main` at `647e6da11416559f1bef52d53e9743acbd2bb688`, parent `cc8f67965213ee9b22d113cc200776c42f6503ba`, origin `https://github.com/cisarik/kronika.git`, and `.ap` HEAD matched the recorded gitlink `d7023cf037f6d17885c3ede5c04812c61640da50`. No publication, deployment, acceptance, or closure is claimed.

## Amended expectations

A download row with an own cataloged media id opens hosted Details through the existing `open_details` web-bridge message, including after that save was already read. The click posts that message once, does not post `review_inbox_opened`, does not retry, and does not remove the row. A row without a media id stays inert.

Order is the request's latest update, newest to oldest. `sort_at_ms` prefers a valid nonnegative `updated_at_ms` and otherwise uses a valid `created_at_ms`. A row with neither is omitted. Each available request capability is read once at `limit=50`, cursors are not followed, and five rows are retained. The visible block still says "Your latest five download requests".

X media id is the first asset in ascending ordinal whose state is `cataloged` and whose media id is a UUID. YouTube media id is the request media id when it is a UUID. An invalid non-null media id becomes null. Labels, static status text, separate Recent downloads block, independent download-failure hiding, and the review-only badge stay as previously accepted.

## Change

`DownloadHistoryItem` now keeps `source`, `request_id`, `label`, and `status`, and carries `media_id` plus `sort_at_ms` instead of `created_at_ms`. `DOWNLOAD_HISTORY.limit` remains 5. `DOWNLOAD_HISTORY.readLimit` is 50 and is the only query limit used by `readCapabilityDownloadList()`. Merge still deduplicates by source and request id, keeping the first occurrence, then sorts by `sort_at_ms` descending, source ascending, and request id descending.

`renderDownloadHistory()` puts a `button.download-history-row.download-history-row--action` inside the `li` when `media_id` is a UUID. Its visible text remains the source, label, and status spans. Its accessible name is `Open details for <label>`. The click calls `openHostedDetails(mediaId)` only. A null media id renders a non-focusable `div.download-history-row` with the same spans and no listener. Button reset, hover, and focus use the existing dark accent tokens. Non-action rows keep the default cursor.

No message type, route, manifest, permission, schema, storage key, alarm, or backend change. ADR-0089's body is unchanged. ADR-0090 records the amendment and supersedes only the inert-row and creation-order statements. SPEC, PRODUCT, X companion, SECURITY, DEVELOPMENT, and the ADR index match that decision.

## Tests

New:

- `download media id selects the first cataloged X asset and the YouTube request id`
- `download sort prefers updated_at_ms and keeps an older request that was updated later`
- `download read window uses limit 50, ignores cursors, and keeps five newest updates`
- `own-media download rows open hosted details per click and stay clickable after a read save`

Updated:

- own terminal history expects `limit=50`, projects the YouTube media id, and leaves a non-cataloged X asset id out of the projection
- accepted-state mapping expects `media_id` and `sort_at_ms`
- capability routing expects `limit=50` and still refuses caller cursors
- media-less sidebar rows stay a `div`; `renderDownloadHistory` calls `openHostedDetails` and does not contain `open_details`, `REVIEW_INBOX_OPENED`, `innerHTML`, or `aria-live`

The click test renders an already-read review item beside an own-media download row, posts exactly one `open_details` per click with that media id, leaves the row in place, posts no `review_inbox_opened`, and shows that the media-less row cannot post `open_details`.

Existing privacy, failure isolation, review-only badge, single-flight refresh, and stale-context tests passed in the same file.

## Validation

`git diff --check` was clean. Staged `git diff --cached --name-only` and committed `git show --name-only` are exactly these 12 paths:

- `DEVELOPMENT.md`
- `PRODUCT.md`
- `SECURITY.md`
- `SPEC.md`
- `docs/X_COMPANION.md`
- `docs/adr/0090-companion-download-row-details-and-latest-update-order.md`
- `docs/adr/README.md`
- `extension/background/service_worker.js`
- `extension/shared/messages.js`
- `extension/ui/sidebar.css`
- `extension/ui/sidebar.js`
- `tests/companion_review_extension.test.js`

Worktree after commit: `## main...origin/main [ahead 1]`, clean. Not pushed.

```text
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 647e6da11416559f1bef52d53e9743acbd2bb688
```

PASS.

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 647e6da11416559f1bef52d53e9743acbd2bb688 --operation runtime-info
```

PASS. CPython 3.13.14 through `/Users/agile/Projects/kronika/.venv/bin/python`.

```text
node --test tests/companion_review_extension.test.js tests/x_companion_extension.test.js
```

114 passed. That is 58 companion-review tests, including the four new download-row tests, and 56 X companion tests.

```text
node --test tests/companion_web_bridge.test.js tests/companion_settings_automatic_analysis.test.js tests/youtube_request_cockpit.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js
```

64 passed.

## Orchestration critique

MEASURED: none
LEAD: none

## Proposed next step

A fresh independent full re-acceptance of `b5436029c66da69c1d14c0f378cbea07bdc74a40`. This report does not grant it.
