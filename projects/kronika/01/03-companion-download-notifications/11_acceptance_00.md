# Companion downloads, compact UI and unread history — fresh independent re-acceptance

## Routing and authority

Persistent role identity: WORKER
Logical whole identity: companion-download-notifications
Worker session ordinal: 11
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: ACCEPT-COMPANION-DOWNLOAD-NOTIFICATIONS-05
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — own-media privacy, companion protocol, unread/opened behavior and the amended history boundary
Recommended context capacity: approximately 250k tokens
Independence required: yes
Acceptance candidate: 2c4f4d89375628df28926060aba305e5d80bacff
Acceptance owner map: companion-download-notifications-v5 — accepted plan `01_report_00.md`, `SPEC.md`, ADR-0089, ADR-0090, ADR-0091, ADR-0092, `docs/X_COMPANION.md`, `PRODUCT.md`, `SECURITY.md`, the original Cooperator choices, the download-row amendments, the compact companion UI, the compact-five/All expansion and the unread download-row amendment
Acceptance allowlist: exactly these 24 whole-diff paths and no others: `DEVELOPMENT.md`; `PRODUCT.md`; `SECURITY.md`; `SPEC.md`; `docs/X_COMPANION.md`; `docs/adr/0089-companion-own-download-status-history.md`; `docs/adr/0090-companion-download-row-details-and-latest-update-order.md`; `docs/adr/0091-companion-history-compact-five-and-all-expansion.md`; `docs/adr/0092-companion-download-unread-state.md`; `docs/adr/README.md`; `extension/background/service_worker.js`; `extension/shared/messages.js`; `extension/ui/sidebar.css`; `extension/ui/sidebar.html`; `extension/ui/sidebar.js`; `src/kronika/adapters/api/web/app.js`; `src/kronika/adapters/api/web/index.html`; `src/kronika/adapters/api/web/styles.css`; `tests/companion_review_extension.test.js`; `tests/contract/test_local_web_application.py`; `tests/contract/test_x_request_api.py`; `tests/contract/test_youtube_request_api.py`; `tests/kronika_ui.test.js`; `tests/workspace_media_frontend.test.js`
Acceptance risk claims: R1 own-download privacy and no foreign data; R2 review-only badge and no second counter; R3 no new backend, route, schema, permission, message type, alarm, storage key or mutation; R4 download-read failure isolation, polling and stale-context behavior; R5 companion test pins and manifest permissions; R6 documentation truth and the confirmed/amended choices; R7 identity-login correction C1; R8 clickable own-media rows and latest-update order; R9 compact companion-hosted Timeline/Filter/My contributions; R10 compact five + one All + retained sixth/later downloads + deduplicated review history; R11 unread marker and existing opened mutation on matched download rows; R12 no acceptance, publication or closure claim
Acceptance control matrix: C01–C27 below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 4
Automatic corrections used: 0
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates

This is a genuinely fresh independent acceptance session. You did not implement the candidate or any correction. Do not rely on any implementation session's retained context or on this Orchestrator's conclusions. Verify the candidate, the reports, the repository and the test evidence independently. Do not fix any finding; report it. A correction requires a new Orchestrator grant.

## Candidate and accepted inputs

Candidate `2c4f4d89375628df28926060aba305e5d80bacff` contains:

- `cc8f67965213ee9b22d113cc200776c42f6503ba` — implementation, parent `e64f2b0`;
- `647e6da11416559f1bef52d53e9743acbd2bb688` — identity-login correction, parent `cc8f679`;
- `b5436029c66da69c1d14c0f378cbea07bdc74a40` — clickable own-media rows and latest-update correction, parent `647e6da`;
- `35c58b693bc885dc115d91df3c6e64680d0c79aa` — compact companion UI correction, parent `b543602`;
- `e9943b56b0bb97402fd64ac2143f1cf2fe07401f` — compact five + All expansion, parent `35c58b6`;
- `2c4f4d89375628df28926060aba305e5d80bacff` — unread download rows and one All, parent `e9943b5`.

Read and reconcile these accepted inputs as claims, not proof:

- `01_report_00.md` — the decision-complete plan.
- `02_report_00.md` — implementation report at `cc8f679`.
- `02_report_01.md` — blocked correction delivery; no repository change.
- `02_report_02.md` — identity-login correction at `647e6da`.
- `03_report_00.md` — independent acceptance of `647e6da` (superseded for the amended boundary).
- `04_report_00.md` — download-row correction at `b543602`.
- `05_report_00.md` — independent re-acceptance of `b543602`.
- `06_report_00.md` — compact companion UI correction at `35c58b6`.
- `07_report_00.md` — independent re-acceptance of `35c58b6`.
- `08_report_00.md` — compact five/All expansion at `e9943b5`.
- `09_report_00.md` — independent re-acceptance of `e9943b5`.
- `10_report_00.md` — unread/one-All correction at `2c4f4d8`.
- `00_notes.md` — Orchestrator reconciliation, including the rendered amendments and residuals.
- `00_handout.md` — the frozen provisional seed.

The COOPERATOR confirmed the original four choices and every subsequent amendment. The active behavior is:

1. A separate Recent downloads block in the companion history sheet; static status rows; only the requester's own data; no second badge/counter.
2. A download row with an own cataloged media id opens hosted Details, stays clickable after read, and rows without a media id stay inert.
3. Download rows are ordered by the latest request update; each source is read at `limit=50` and up to fifty rows are retained.
4. The compact sheet shows five downloads and one All. All reveals the sixth/last retained downloads and the complete review history. The review All stays hidden while downloads exist; with no downloads it behaves as before.
5. A review row whose media id matches a download row is omitted from both review lists. A download row matching an analyzed unread review item shows an unread dot/accent and accessible “Unread”; clicking it opens Details and posts the existing `REVIEW_INBOX_OPENED` once for that analysis run, then refreshes, clearing the marker and badge.
6. Companion-hosted Timeline: no status/visibility glyphs, readable Kind/Status/Visibility text, unclamped titles, one Filter button for the four filters. Companion My contributions: full-width wrapping title. The wide page keeps its glyph table, visible filters and multi-column grid.

The residual YouTube acquisition `INSPECTION_OUTPUT_LIMIT`, the X acquisition failures/«Save to Kronika failed» outcome, and the full-page narrow My contributions LEAD are outside this companion acceptance and must not fail it. The Cooperator's rendered acceptance will decide any later follow-up.

## Repository and route

Repository identity: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Repository checkout topology: standalone checkout with pinned `.ap` submodule
Expected branch: main
Expected HEAD: 2c4f4d89375628df28926060aba305e5d80bacff
Expected parent: e9943b56b0bb97402fd64ac2143f1cf2fe07401f
Expected grandparent: 35c58b693bc885dc115d91df3c6e64680d0c79aa
Expected great-grandparent: b5436029c66da69c1d14c0f378cbea07bdc74a40
Expected fourth: 647e6da11416559f1bef52d53e9743acbd2bb688
Expected fifth: cc8f67965213ee9b22d113cc200776c42f6503ba
Expected sixth: e64f2b0f92458fac2590e03672e30da62275b345
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50 at `/Users/agile/Projects/kronika/.ap`

The Orchestrator observed public `main` equal to `e9943b5` on 2026-11-14; do not use the network. Verify the local repository gate:

- `git -C /Users/agile/Projects/kronika status --porcelain=v1 -b` is clean and reports `## main...origin/main [ahead 1]`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD` equals the candidate;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^` equals `e9943b5`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^^` equals `35c58b6`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^^^` equals `b543602`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^^^^` equals `647e6da`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^^^^^` equals `cc8f679`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^^^^^^` equals `e64f2b0`;
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
Downloadable prompt filename: 11_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/01/03-companion-download-notifications
Report filename: 11_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/03-companion-download-notifications/11_report_00.md

## Authority

Positive authority: read-only inspection of the repository, the named trace inputs, the accepted plan and the current candidate; run the selected AP, Python and Node checks; read-only Git inspection; create the complete terminal report at the exact trace path and read it back. No repository write, test modification, correction, stage, commit or push is granted.

Commands: `./.ap/ap project check`, `./.ap/ap exec` with the exact baseline and declared operations, `node --test` with the selected suites, `rg`, and read-only Git object/status/diff/log commands. Do not invoke raw `.venv/bin/python`, `python`, `python3` or `poetry run`.

Git authority: read-only. No fetch, stage, commit, push, force, amend, reset, clean, stash, checkout, switch or tag.

Network authority: none. Secret authority: none. Do not read `private/`, `.venv`, credentials, browser profiles, cookies or unrelated paths.

Negative authority: any repository or test modification; any correction; any new provider, browser, NUC, deployment or publication action; any edit to the plan, reports, notes, handout or run map; any acceptance, publication, deployment or closure claim beyond this report's phase result.

## Acceptance control matrix

Report every row with `PASS`, `FAIL`, `NOT TESTED` or `BLOCKED`, exact evidence, and no correction. A FAIL is a finding, not permission to fix.

| ID | Claim and required evidence |
|---|---|
| C01 | Repository identity, branch, candidate HEAD, all six parents, clean worktree, `.ap` gitlink/HEAD and public-main observation match the declared values. |
| C02 | The whole diff `e64f2b0..2c4f4d8` is exactly the 24-path allowlist. The unread commit `e9943b5..2c4f4d8` is exactly its 9 allowed paths. No manifest, Alembic or backend API/schema change; the only `src` paths are the three web-shell assets. |
| C03 | `extension/manifest.json` is unchanged; permissions are exactly `alarms`, `sidePanel`, `storage`; no `notifications`, `host_permissions`, `externally_connectable` or new optional permission. |
| C04 | No backend, schema, migration, API route, `tailscale_ingress.py` policy, `companion_mutation` route, alarm, message type or persisted storage key changed. Exactly six `companion_mutation` routes remain; `REVIEW_INBOX_OPENED` is the existing route. |
| C05 | `review_inbox` keeps its message type and request shape. A successful response adds `downloads: {ok, items}`; download failure is exactly `{ok:false, items:[]}`; successful empty is `{ok:true, items:[]}`. No second message type or transport. |
| C06 | `review_inbox` is restricted to the extension's own sidebar sender; missing/mismatched sender makes no network call and does not clear the badge. |
| C07 | X/YouTube download reads use the fixed `pathFor()` templates and configured origin, with `limit=50`, one first page per available capability, no caller-controlled URL/path/ID/cursor, no cursor following. Capability absence skips that source. |
| C08 | The projection adds exactly an own `media_id` (UUID/null) and `sort_at_ms`, replacing `created_at_ms`; X selects the first cataloged asset by ordinal with a UUID; YouTube uses the request media id when UUID; invalid non-null becomes null. |
| C09 | `sort_at_ms` prefers a valid `updated_at_ms`, falls back to `created_at_ms`, omits when neither is valid; merge deduplicates by `(source, request_id)`, sorts by `sort_at_ms` descending, source ascending, request ID descending, and returns up to fifty. |
| C10 | State mapping covers all X active/terminal states and all YouTube requester phases; unknown/malformed rows produce no row; analysis/publication/catalog presence never create a completion claim. |
| C11 | A download row with an own media id is a button with three spans and an accessible open action; clicking posts one `open_details`, no retry/removal, and remains clickable after read. A null-media row is a non-focusable inert `div`. |
| C12 | The compact sheet shows five downloads and one All; the review All is hidden while downloads exist; expanding reveals the sixth/last retained downloads and the complete review history (compact + expanded); collapsing returns to five; no second All. The title-bar toggle still opens/closes the sheet. |
| C13 | With no downloads, the review compact/All/expanded behavior is unchanged and no empty download All is shown. With downloads and no review rows, All reveals only later downloads. |
| C14 | A review row whose media id matches a download row is omitted from both review lists; a distinct review row remains; a download without a media id does not drop a review row; no duplicate title/media. |
| C15 | A download row matching an analyzed unread review item shows a visible unread dot/accent and accessible “Unread”; its click posts one `open_details` and one existing `REVIEW_INBOX_OPENED` for that analysis run, then refreshes; the row remains and the marker clears after the refreshed unread state. A row without the match posts no opened; pending/null-media stays inert. |
| C16 | Review-only, download-only, empty, failed and mixed states render correctly. Download-read failure hides all Downloads rows but retains the review list and badge. Review pagination/cursor failure hides all history and clears the badge. |
| C17 | Stale-context handling covers origin, configuration revision, capabilities, history source and identity login; a changed login with identical capabilities discards the whole result as stale. Sidebar refreshes are single-flight; hidden polling stops; reconnect/reset/runtime invalidation clears downloads and the All state; late generations are discarded. |
| C18 | Privacy: only the signed-in requester's own X/YouTube request data appears; the administrator inbox stays separate; no foreign title, URL, thumbnail, request ID, state or failure detail; no raw URL, asset array, media filename, provider payload or failure detail reaches the sidebar; the only linked media is the row's own cataloged media; no download snapshot is persisted. |
| C19 | The badge remains the server `unopened_count` for the active review source; download outcomes never contribute; the alarm makes no download-list calls; no second counter or notifications permission. The existing opened mutation may clear the unread marker/badge after the matched download-row click. |
| C20 | Download documentation truth: `SPEC.md`, `PRODUCT.md`, `docs/X_COMPANION.md`, `SECURITY.md` and `DEVELOPMENT.md` agree on compact five, retained fifty, one All, sixth/last, deduplicated review, unread marker and opened behavior, own-media click, inert no-media rows, latest-update order and review-only badge. ADR-0092 is accepted and indexed; ADR-0090/0091 bodies are unchanged. |
| C21 | Companion-hosted Timeline: status/visibility glyphs hidden; Kind/Status/Visibility readable text; title not clamped; wide page keeps glyph table and two-line clamp. Companion Filter: one button, collapsed default, toggles four filters, no query change; wide page keeps filters visible and the button hidden. |
| C22 | Companion My contributions: row uses available width and title fills it, wrapping on words/spaces; metadata/badges/actions readable; wide multi-column grid unchanged. |
| C23 | Wide/full-page behavior remains unchanged, including the glyph table, filters and contributions grid. The full-page narrow My contributions LEAD remains an out-of-scope residual, not a companion failure. |
| C24 | Independent test evidence at the candidate: focused Python 46, focused Node 118, broader Python 206, broader Node 64, compact UI focused Node 44, affected frontend Node 287, served-shell Python 211. Record actual counts and any failure signature. |
| C25 | `git diff --check` is clean; the worktree is clean after validation; committed path lists match C02; documentation links resolve. |
| C26 | The historical `08_report_00.md` delivery collision and the blocked `02_report_01.md` are trace-history facts, not candidate changes; no foreign `02_rereport_00.md` is in the repository. |
| C27 | The residual YouTube acquisition `INSPECTION_OUTPUT_LIMIT`, the X acquisition failures/«Save to Kronika failed» outcome and the full-page narrow My contributions LEAD are outside this companion acceptance and do not fail it. No acceptance, publication, deployment, production-acceptance or closure claim is made by the report itself. |

## Validation

Run the exact selected checks at the candidate:

```text
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline e64f2b0f92458fac2590e03672e30da62275b345
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline e64f2b0f92458fac2590e03672e30da62275b345 --operation runtime-info
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline e64f2b0f92458fac2590e03672e30da62275b345 --operation test-focus -- tests/contract/test_x_request_api.py tests/contract/test_youtube_request_api.py tests/contract/test_companion_review_api.py -q -p no:cacheprovider
node --test tests/companion_review_extension.test.js tests/x_companion_extension.test.js
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline e64f2b0f92458fac2590e03672e30da62275b345 --operation test-focus -- tests/contract/test_tailscale_ingress_security.py tests/contract/test_requester_private_youtube_details.py tests/unit/application/test_x_acquisition_lifecycle.py tests/integration/test_youtube_acquisition_lifecycle.py tests/unit/infrastructure/persistence/test_companion_review_repository.py tests/unit/domain/test_x_acquisition_domain.py tests/unit/domain/test_youtube_acquisition.py -q -p no:cacheprovider
node --test tests/companion_web_bridge.test.js tests/companion_settings_automatic_analysis.test.js tests/youtube_request_cockpit.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js
node --test tests/kronika_ui.test.js tests/workspace_media_frontend.test.js
node --test tests/upload_cockpit_async_ownership.test.js tests/companion_web_bridge.test.js tests/x_companion_extension.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js tests/kronika_ui.test.js tests/gallery_search_tag_filters.test.js tests/automatic_analysis_lifecycle.test.js tests/cover_frontend.test.js
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline e64f2b0f92458fac2590e03672e30da62275b345 --operation test-focus -- tests/contract/test_local_web_application.py -q -p no:cacheprovider
```

Also run the read-only repository checks:

```text
git status --porcelain=v1 -b
git rev-parse HEAD HEAD^ HEAD^^ HEAD^^^ HEAD^^^^ HEAD^^^^^ HEAD^^^^^^
git show --name-only --format= HEAD
git diff --name-only e64f2b0..2c4f4d8
git diff --name-only e9943b5..2c4f4d8
git diff --check e64f2b0..2c4f4d8
git diff e64f2b0..2c4f4d8 -- extension/manifest.json
git diff --name-only e64f2b0..2c4f4d8 -- src
```

Use synthetic fixtures only. Do not run a full suite, browser evidence, real acquisition, provider calls or NUC commands. Do not modify the repository or tests.

## Report contract

Write the terminal report to the exact report path. Begin it exactly with:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three exchange coordinates exactly once (`11`/`01`). Include status, candidate, start and end commit, changed paths, the full C01–C27 matrix with evidence, exact test counts, defects and residual risks, independence statement, Orchestration critique with MEASURED and LEAD findings or none, and one proposed next step. Use `Phase-qualified result: acceptance-PASS` only if every control passes; otherwise use status `PARTIAL` or `BLOCKED` with `Phase-qualified result: not-applicable` and exact evidence. Use `Logical-whole closure: not-closed` and `Report justification: final-acceptance`.

Direct-write the report, read it all back, verify content, path and SHA-256, and only then send a short separate completion notice. If the report path already exists, including an empty file, stop and report the collision. If the client blocks the exact write, return the complete report and state `File delivery: pending client restriction`.

Do not fix any defect. Do not claim publication, deployment, production acceptance or closure. The Orchestrator owns the accept/correct/escalate decision and closure.

## Stopping conditions

Stop and report the exact blocker if:

- the candidate, a parent, the branch, the worktree or the `.ap` pin does not match;
- a required source or trace input is missing, contradictory or unreadable;
- a selected test fails or a control fails; report the finding and do not fix it;
- answering a control would require repository mutation, a correction, a network call, provider contact, browser automation, NUC access, secrets or another ungranted effect;
- the report path already exists or its parent/symlink resolution is unsafe;
- the client cannot write the report or run a required command.

After a prerequisite stop, only report preparation and necessary cleanup inside this grant may finish. Preserve the first causal failure.

## Authority expiry

This grant expires at the terminal acceptance report, cancellation or supersession. A green test run, a plan approval, the candidate commit or a later conversation is not publication, deployment, production acceptance or closure authority.
