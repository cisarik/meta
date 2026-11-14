# Companion download rows — clickable own media and latest-update order

## Routing and authority

Persistent role identity: WORKER
Logical whole identity: companion-download-notifications
Worker session ordinal: 02
Worker exchange ordinal: 04
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: AMEND-COMPANION-DOWNLOAD-ROWS-01
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — own-media disclosure, an interactive sidebar row, ordering semantics and companion protocol
Recommended context capacity: approximately 250k tokens
Implementation authority: explicit
Exact baseline: 647e6da11416559f1bef52d53e9743acbd2bb688
Changed-path allowlist: exactly these 12 paths and no others: `extension/background/service_worker.js`; `extension/shared/messages.js`; `extension/ui/sidebar.js`; `extension/ui/sidebar.css`; `tests/companion_review_extension.test.js`; `docs/X_COMPANION.md`; `PRODUCT.md`; `SPEC.md`; `SECURITY.md`; `DEVELOPMENT.md`; `docs/adr/0090-companion-download-row-details-and-latest-update-order.md`; `docs/adr/README.md`
Implementation boundaries: clickable own-media download rows, latest-update ordering, the bounded 50/5 read window, and the matching tests and documentation only
Independence required: no

Continuity anchor: correction report `02_report_02.md`, independent acceptance report `03_report_00.md`, and published candidate `647e6da11416559f1bef52d53e9743acbd2bb688`
Authority renewal: prior acceptance authority expired at `03_report_00.md`; the COOPERATOR's rendered acceptance amendments are the current product authority for this correction; this exchange grants complete correction-only authority
Evidence posture: non-independent

This prompt continues the exact implementation session 02 that produced
`02_report_00.md`, `02_report_02.md` and the accepted candidate `647e6da`. If
this is not that session, stop and report BLOCKED. Retained context is
convenience, not authority. Re-gate the repository and environment before
acting. A fresh independent re-acceptance follows this correction.

## Amended Cooperator expectations

The COOPERATOR rendered the published `647e6da` companion and returned PARTIAL
on 2026-11-13. These amendments supersede only the named earlier choices; the
rest of the accepted design remains.

1. **Superseded:** all download rows are inert and do not open Details.
   **Amended:** a download row with an own cataloged media id opens hosted
   Details, including when the save was already read. Rows without a media id
   remain inert.
2. **Superseded:** newest creation first. **Amended:** most recently downloaded
   or updated first, newest to oldest, using the request's last update.

The other confirmed choices remain: a separate Recent downloads block, static
status text without unseen marker/counter/acknowledgement/persistence,
independent Downloads failure hiding with review history and badge retained,
and YouTube rows labelled by video id.

Out of scope and not to be changed by this correction:

- The YouTube acquisition failure with sanitized `INSPECTION_OUTPUT_LIMIT` is a
  separate logical whole.
- The full-page Timeline clipping/emoji spacing and the My contributions
  vertical-text layout are a separate UI/UX whole.
- Nothing in this correction fixes acquisition, the web shell beyond the
  companion side panel, or any backend.

## Required design

### 1. Projection

Extend `DownloadHistoryItem` with exactly two fields while keeping the existing
`source`, `request_id`, `label`, `status`:

```text
media_id: UUID | null        // own cataloged media to open, or null
sort_at_ms: nonnegative safe integer
```

`sort_at_ms` is `updated_at_ms` when it is a valid nonnegative safe integer,
otherwise `created_at_ms` when that is valid, otherwise the row is omitted.
`media_id` is nullable. An invalid non-null media id is normalized to null, not
turned into a foreign or unknown link.

X media id: from `row.assets`, choose the first asset by ascending `ordinal`
whose `state` is `cataloged` and whose `media_id` is a UUID. If no such asset
exists, `media_id` is null. This is the row's representative own media; the
label remains the claim title or `X post <id>`.

YouTube media id: `row.media_id` when it is a UUID, otherwise null. The API
already returns it only for readable completed/completed_private results.

Keep the `downloads: {ok, items}` response shape, the failure shape
`{ok:false, items:[]}`, and the empty shape `{ok:true, items:[]}`. No new
message type, route, mutation, permission or storage key.

### 2. Read window and order

Fetch the first page with `limit=50` for each available request capability
(`GET /api/x/requests?limit=50`, `GET /api/youtube/requests?limit=50`). Do not
follow cursors. Merge, deduplicate by `(source, request_id)` keeping the first
occurrence, sort by `sort_at_ms` descending, then source ascending and request
ID descending, and retain five rows. The visible block still says **Your latest
five download requests**; the read window is bounded at fifty per source so a
recently completed older request can rise above older creations.

### 3. Sidebar

In `extension/ui/sidebar.js`, `renderDownloadHistory()` must create for each
item an `li` containing:

- a `button` with class `download-history-row download-history-row--action`
  when `item.media_id` is a UUID, with the same three visible spans (source,
  label, status); clicking it calls the existing `openHostedDetails(item.media_id)`
  exactly once. It must not post `REVIEW_INBOX_OPENED`, must not retry, must not
  remove the row, and must remain clickable after the save was read. Give the
  button an accessible name that includes the visible label and an explicit
  open action, while keeping the visible text.
- a `div` with class `download-history-row` when `item.media_id` is null, with
  the same spans and no click, link, button, pointer or mutation.

The row remains within the bounded scrollable sheet. No nested interactive
elements, no `innerHTML`, no `aria-live`, no new animation. Use the existing
theme tokens. Add button reset/focus/hover styling in `sidebar.css` consistent
with the existing dark accent surfaces; non-action rows must not look clickable.
Keep the independent Downloads failure hiding, the review-only badge, the
review row click behavior, single-flight refresh and stale-context handling
unchanged.

### 4. Documentation

- `SPEC.md`: replace the inert-row and creation-order statements. State that a
  download row with an own cataloged media id opens hosted `open_details`, rows
  without a media id are inert, download rows never post opened, the order is
  most recent update first, the read window is the first page at limit 50 and
  retains five, and review pagination remains fail-closed.
- `PRODUCT.md`: state the clickable own-media behavior, the inert no-media rows
  and the latest-update order.
- `docs/X_COMPANION.md`: state the own-media click, the read-row persistence,
  the latest-update order, the 50/5 bounded window and the labels.
- `SECURITY.md`: state that the projection includes an own media id and a sort
  timestamp, no foreign data, and that `open_details` is the existing hosted
  web-bridge message, not a new mutation.
- `DEVELOPMENT.md`: update the acceptance checklist for clickable own-media
  rows, read rows, latest-update order and the bounded window.
- Add `docs/adr/0090-companion-download-row-details-and-latest-update-order.md`
  as an accepted ADR recording the amended decision and superseding only
  ADR-0089's inert-row and creation-order statements. Do not edit the
  ADR-0089 body.
- `docs/adr/README.md`: index ADR-0090 and annotate the ADR-0089 row.
- Do not edit `README.md`, `ROADMAP.md`, `SERVER.md` or `docs/UX_AUDIT.md`.

## Repository and route

Repository identity: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Repository checkout topology: standalone checkout with pinned `.ap` submodule
Expected branch: main
Expected HEAD: 647e6da11416559f1bef52d53e9743acbd2bb688
Expected parent: cc8f67965213ee9b22d113cc200776c42f6503ba
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50 at `/Users/agile/Projects/kronika/.ap`

The Orchestrator observed public `main` equal to `647e6da` after publication;
do not use the network. Verify:

- `git -C /Users/agile/Projects/kronika status --porcelain=v1 -b` is clean and
  reports `## main...origin/main`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD` equals `647e6da`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^` equals `cc8f679`;
- `git -C /Users/agile/Projects/kronika/.ap rev-parse HEAD` equals the
  governing AP pin;
- no untracked files.

If the gate fails, classify with RF-12 and stop.

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
Downloadable prompt filename: 02_correction_03.md
Destination path: /Users/agile/meta/projects/kronika/01/03-companion-download-notifications
Report filename: 02_report_03.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: exactly the 12 allowlisted repository paths
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/03-companion-download-notifications/02_report_03.md

## Authority

Positive authority: read-only inspection of the repository, the accepted plan,
the reports and this prompt at
`/Users/agile/meta/projects/kronika/01/03-companion-download-notifications/02_correction_03.md`;
modify exactly the 12 allowlisted paths; run the selected AP and Node commands
below; check the exact report destination; create exactly one local commit on
`main` on top of `647e6da`; and create/read back `02_report_03.md`.

Commands: `./.ap/ap project check`, `./.ap/ap exec` with the exact baseline and
declared operations, `node --test` with the selected suites, read-only Git
inspection, exact-path `git add`, one local `git commit`, and the native file
writer for the exact report path. Do not invoke raw `.venv/bin/python`,
`python`, `python3` or `poetry run`.

Git authority: one local commit on `main` on top of `647e6da`, subject
`fix: open download rows and order by latest update`. Stage exactly the 12
allowlisted paths; never `git add .` or `git add -A`. No fetch, push, force,
amend, reset, clean, stash, checkout, switch, tag or remote change.

Network authority: none. Secret authority: none. Do not read `private/`,
`.venv`, credentials, browser profiles, cookies or unrelated paths.

Negative authority: any change outside the 12 allowlisted paths; any backend,
schema, migration, manifest, permission, route, mutation, alarm, message type
or persisted storage key change; any acquisition or web-shell change; any
push, publication, deployment, full suite, browser run, NUC access, provider
call or secret access; any edit to the plan, reports, notes, handout,
`02_rereport_00.md` or the run map; any acceptance or closure claim.

## Validation

Run the focused Node selection first:

```text
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 647e6da11416559f1bef52d53e9743acbd2bb688
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 647e6da11416559f1bef52d53e9743acbd2bb688 --operation runtime-info
node --test tests/companion_review_extension.test.js tests/x_companion_extension.test.js
```

Then the adjacent companion selection:

```text
node --test tests/companion_web_bridge.test.js tests/companion_settings_automatic_analysis.test.js tests/youtube_request_cockpit.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js
```

Run `git diff --check`, `git status --porcelain=v1`, inspect the exact diff and
verify the committed path list is exactly the 12 allowlisted paths. Python
tests are not required for this JS/docs correction; the project check and
runtime-info are the AP envelope evidence. Do not run a full suite, browser
evidence, real acquisition, provider calls or NUC commands.

The correction must add or update tests that prove:

- a row with an own media id renders an action control and posts exactly one
  `open_details` with that media id, with no `REVIEW_INBOX_OPENED` and no row
  removal, including after a read/opened state;
- a row without a media id is inert and cannot post `open_details`;
- X selects the first cataloged asset by ordinal and YouTube uses the request
  media id;
- `sort_at_ms` prefers a valid `updated_at_ms`, falls back to `created_at_ms`,
  and orders an older-created/newer-updated row above an older-created row;
- the read window uses `limit=50`, does not follow cursors, and retains five;
- the existing privacy, failure isolation, badge, single-flight and
  stale-context tests still pass.

## Report contract

Write the terminal report to `02_report_03.md`. Begin it exactly with:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three exchange coordinates exactly once (`02`/`04`). Include the
amended expectations, the exact change, the new and updated tests, the test
commands and counts, the new commit SHA and parent, the staged and committed
path lists, and Orchestration critique with MEASURED and LEAD findings or none.
Use `Phase-qualified result: implementation-PASS` only if the correction and all
selected checks pass; otherwise `PARTIAL` or `BLOCKED` with exact evidence. Use
`Logical-whole closure: not-closed` and `Report justification: new-mutation`.

Direct-write the report, read it all back, verify content, path and SHA-256, and
only then send a short separate completion notice. If the report path already
exists, including an empty file, stop and report the collision. If the client
blocks the exact write, return the complete report and state
`File delivery: pending client restriction`.

Do not claim acceptance, publication, deployment or closure. A fresh
independent full re-acceptance follows.

## Stopping conditions

Stop and report the exact blocker if:

- this is not the exact implementation session 02 or its continuity anchor does
  not match;
- HEAD is not `647e6da`, the parent is not `cc8f679`, or the worktree is not
  clean;
- a required change falls outside the 12-path allowlist;
- a selected test fails for a reason outside this correction;
- the own-media id cannot be selected deterministically from the existing
  response without a backend change;
- the report path already exists or its parent/symlink resolution is unsafe;
- the client cannot write the report or run a required command;
- secrets, private data, browser state or another ungranted effect would be
  touched.

After a prerequisite stop, only report preparation and necessary cleanup inside
this grant may finish. Preserve the first causal failure.

## Authority expiry

This grant expires at the terminal correction report, cancellation or
supersession. Retained context, a green test run, the local commit or a later
conversation is not acceptance or closure authority.
