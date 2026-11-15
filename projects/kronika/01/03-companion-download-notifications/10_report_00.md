### Report for ORCHESTRATOR_CHAT

Logical whole identity: companion-download-notifications
Worker session ordinal: 10
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: COMPANION-HISTORY-UNREAD-AND-SINGLE-ALL-01
status: PASS
Phase-qualified result: implementation-PASS
Start commit: e9943b56b0bb97402fd64ac2143f1cf2fe07401f
End commit: 2c4f4d89375628df28926060aba305e5d80bacff
Report justification: new-mutation
Logical-whole closure: not-closed

Independence required: no
Evidence posture: non-independent
Repository mutation: one local commit on `main`. Host/remote mutation: none. Network: not used. No fetch, push, reset, or deployment.
Requested reasoning recommendation: High. Effective model identity is not independently attested.

## Item 1 amendment

Rendered `e9943b5` kept two All controls when downloads exist, and a downloaded post that is still unread lost its marker because the matching review row is deduplicated. This correction makes the download All the only All when downloads exist, and puts the unread marker and the existing opened mutation on the matching download row.

«Save to Kronika failed» is the existing X-save outcome name in `reduceXSaveOutcome` when the save result is not ok. The history row already shows `Download failed`. That pair is an acquisition residual, recorded in `docs/X_COMPANION.md`, and the acquisition path was not changed.

## Change

When downloads exist, `#download-history-all` stays the only visible All. Activating it reveals later retained downloads, including the sixth and last retained row, and the complete review history (compact and expanded review lists). Activating it again returns to the five-download sheet. The review All stays in the DOM and stays hidden. With no downloads, the review All behaves as before.

A download row whose media id matches an analyzed review item with `unopened: true` and an `analysis_run_id` gets the unread dot and accent plus accessible text `Unread`. The same click posts one `open_details` and one existing `REVIEW_INBOX_OPENED` for that run, then refreshes. The row remains and the marker clears when the refreshed item is no longer unread. A download without that match posts no opened request. A null-media row stays inert. The review-only badge math is unchanged. ADR-0092 supplements ADR-0091 and supersedes only its review-All presentation when downloads exist and the no-opened statement for a matched analyzed unread download row. The ADR-0090 and ADR-0091 bodies were not edited.

## Tests

New:

- `one download All reveals later downloads and the complete review history`
- `matched unread download row posts opened once and clears the marker`

Updated:

- compact history now expects the review All to stay hidden while downloads are expanded
- the download All shell toggle expects no second All

Commands and counts:

- `./.ap/ap project check --root /Users/agile/Projects/kronika --baseline e9943b56b0bb97402fd64ac2143f1cf2fe07401f` PASS. It also printed `WARN sanitized inherited environment classes` and then `ap project check --baseline: PASS`.
- `./.ap/ap exec --root /Users/agile/Projects/kronika --baseline e9943b56b0bb97402fd64ac2143f1cf2fe07401f --operation runtime-info` PASS. CPython 3.13.14 at `/Users/agile/Projects/kronika/.venv/bin/python`.
- `node --test tests/companion_review_extension.test.js tests/x_companion_extension.test.js`: 118 passed, 0 failed.
- `node --test tests/companion_web_bridge.test.js tests/companion_settings_automatic_analysis.test.js tests/youtube_request_cockpit.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js`: 64 passed, 0 failed.
- `git diff --check` produced no findings.

## Commit

Parent: `e9943b56b0bb97402fd64ac2143f1cf2fe07401f`
Commit: `2c4f4d89375628df28926060aba305e5d80bacff`
Subject: `fix: mark unread downloads and show one All`

Staged paths and committed paths are the same nine allowlisted paths:

- `DEVELOPMENT.md`
- `PRODUCT.md`
- `SPEC.md`
- `docs/X_COMPANION.md`
- `docs/adr/0092-companion-download-unread-state.md`
- `docs/adr/README.md`
- `extension/ui/sidebar.css`
- `extension/ui/sidebar.js`
- `tests/companion_review_extension.test.js`

The index is clean after the commit. `main` is ahead of `origin/main` by 1. No push.

## Orchestration critique

MEASURED: none
LEAD: «Save to Kronika failed» is the existing X-save outcome name; the particular rendered failure cause was not isolated beyond that reducer. Cheapest check: a separate acquisition whole, not this history sheet.

Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
Authority expiry: this terminal report ends the grant; no autonomous continuation.
