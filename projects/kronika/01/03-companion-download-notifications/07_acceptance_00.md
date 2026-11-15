# Companion downloads and compact companion UI — fresh independent re-acceptance

## Routing and authority

Persistent role identity: WORKER
Logical whole identity: companion-download-notifications
Worker session ordinal: 07
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: ACCEPT-COMPANION-DOWNLOAD-NOTIFICATIONS-03
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — own-media privacy, companion protocol, responsive companion layout and the amended rendered boundary
Recommended context capacity: approximately 250k tokens
Independence required: yes
Acceptance candidate: 35c58b693bc885dc115d91df3c6e64680d0c79aa
Acceptance owner map: companion-download-notifications-v3 — accepted plan `01_report_00.md`, `SPEC.md`, ADR-0089, ADR-0090, `docs/X_COMPANION.md`, `PRODUCT.md`, `SECURITY.md`, the four original Cooperator choices, the two download-row amendments and the compact companion UI correction
Acceptance allowlist: exactly these 22 whole-diff paths and no others: `DEVELOPMENT.md`; `PRODUCT.md`; `SECURITY.md`; `SPEC.md`; `docs/X_COMPANION.md`; `docs/adr/0089-companion-own-download-status-history.md`; `docs/adr/0090-companion-download-row-details-and-latest-update-order.md`; `docs/adr/README.md`; `extension/background/service_worker.js`; `extension/shared/messages.js`; `extension/ui/sidebar.css`; `extension/ui/sidebar.html`; `extension/ui/sidebar.js`; `src/kronika/adapters/api/web/app.js`; `src/kronika/adapters/api/web/index.html`; `src/kronika/adapters/api/web/styles.css`; `tests/companion_review_extension.test.js`; `tests/contract/test_local_web_application.py`; `tests/contract/test_x_request_api.py`; `tests/contract/test_youtube_request_api.py`; `tests/kronika_ui.test.js`; `tests/workspace_media_frontend.test.js`
Acceptance risk claims: R1 own-download privacy and no foreign data; R2 review-only badge and no second counter; R3 no new backend, route, schema, permission, message type, alarm, storage key or mutation; R4 download-read failure isolation, polling and stale-context behavior; R5 companion test pins and manifest permissions; R6 documentation truth and the confirmed/amended choices; R7 identity-login correction C1; R8 clickable own-media rows and latest-update order; R9 compact companion-hosted Timeline/Filter/My contributions behavior; R10 no acceptance, publication or closure claim
Acceptance control matrix: C01–C26 below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 2
Automatic corrections used: 0
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates

This is a genuinely fresh independent acceptance session. You did not implement the candidate, the identity correction, the download-row correction or the compact UI correction. Do not rely on any implementation session's retained context or on this Orchestrator's conclusions. Verify the candidate, the reports, the repository and the test evidence independently. Do not fix any finding; report it. A correction requires a new Orchestrator grant.

## Candidate and accepted inputs

Candidate `35c58b693bc885dc115d91df3c6e64680d0c79aa` contains:

- `cc8f67965213ee9b22d113cc200776c42f6503ba` — implementation, parent `e64f2b0`;
- `647e6da11416559f1bef52d53e9743acbd2bb688` — identity-login correction, parent `cc8f679`;
- `b5436029c66da69c1d14c0f378cbea07bdc74a40` — clickable own-media rows and latest-update correction, parent `647e6da`;
- `35c58b693bc885dc115d91df3c6e64680d0c79aa` — compact companion UI correction, parent `b543602`.

Read and reconcile these accepted inputs as claims, not proof:

- `01_report_00.md` — the decision-complete plan.
- `02_report_00.md` — implementation report at `cc8f679`.
- `02_report_01.md` — blocked correction delivery; no repository change.
- `02_report_02.md` — identity-login correction at `647e6da`.
- `03_report_00.md` — independent acceptance of `647e6da` (superseded for the amended boundary).
- `04_report_00.md` — download-row correction at `b543602`.
- `05_report_00.md` — independent re-acceptance of `b543602`.
- `06_report_00.md` — compact companion UI correction at `35c58b6`.
- `00_notes.md` — Orchestrator reconciliation, including the rendered amendments and residuals.
- `00_handout.md` — the frozen provisional seed.

The COOPERATOR confirmed the original four choices, amended the download rows and order, and then required the compact companion-hosted UI:

1. A separate Recent downloads block inside the existing history sheet, preserving review ordering.
2. Static status rows with no unseen marker, counter, acknowledgement, expiry or persistence.
3. If either capability-enabled download read fails, hide the entire Downloads block while retaining review history and its badge count.
4. A download row with an own cataloged media id opens hosted Details through the existing `open_details` message, including after read; rows without a media id stay inert.
5. Order by the most recent request update, newest to oldest; the read window is the first page at `limit=50` per source and retains five.
6. In the companion-hosted shell, the Timeline hides status/visibility glyphs, shows Kind/Status/Visibility as text, wraps the full title, and puts the four filters behind one Filter button. Companion My contributions gives the title the row width and normal word wrapping. The wide page keeps its glyph table, filters and multi-column contributions grid.

The residual YouTube acquisition `INSPECTION_OUTPUT_LIMIT` and the full-page narrow My contributions LEAD are outside the companion acceptance and must not fail it. The Cooperator's rendered acceptance will decide any later follow-up.

## Repository and route

Repository identity: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Repository checkout topology: standalone checkout with pinned `.ap` submodule
Expected branch: main
Expected HEAD: 35c58b693bc885dc115d91df3c6e64680d0c79aa
Expected parent: b5436029c66da69c1d14c0f378cbea07bdc74a40
Expected grandparent: 647e6da11416559f1bef52d53e9743acbd2bb688
Expected great-grandparent: cc8f67965213ee9b22d113cc200776c42f6503ba
Expected fifth: e64f2b0f92458fac2590e03672e30da62275b345
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50 at `/Users/agile/Projects/kronika/.ap`

The Orchestrator observed public `main` equal to `b543602` on 2026-11-13; do not use the network. Verify the local repository gate:

- `git -C /Users/agile/Projects/kronika status --porcelain=v1 -b` is clean and reports `## main...origin/main [ahead 1]`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD` equals the candidate;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^` equals `b543602`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^^` equals `647e6da`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^^^` equals `cc8f679`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^^^^` equals `e64f2b0`;
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
Downloadable prompt filename: 07_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/01/03-companion-download-notifications
Report filename: 07_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/03-companion-download-notifications/07_report_00.md

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
| C01 | Repository identity, branch, candidate HEAD, all four parents, clean worktree, `.ap` gitlink/HEAD and public-main observation match the declared values. |
| C02 | The whole diff `e64f2b0..35c58b6` is exactly the 22-path allowlist. The compact UI commit `b543602..35c58b6` is exactly its 10 allowed paths. No manifest, Alembic or backend API/schema change; the only `src` paths are the three web-shell assets. |
| C03 | `extension/manifest.json` is unchanged; permissions are exactly `alarms`, `sidePanel`, `storage`; no `notifications`, `host_permissions`, `externally_connectable` or new optional permission. |
| C04 | No backend, schema, migration, API route, `tailscale_ingress.py` policy, `companion_mutation` route, alarm, message type or persisted storage key changed. Exactly six `companion_mutation` routes remain. |
| C05 | `review_inbox` keeps its message type and request shape. A successful response adds `downloads: {ok, items}`; download failure is exactly `{ok:false, items:[]}`; successful empty is `{ok:true, items:[]}`. No second message type or transport is introduced. |
| C06 | `review_inbox` is restricted to the extension's own sidebar sender: `sender.id`, `sender.url` and `sender.origin` match the sidebar document. Missing or mismatched metadata makes no network call and does not clear the badge. |
| C07 | The X and YouTube download reads use the existing fixed `pathFor()` templates and configured origin, with `limit=50`, one first page per available capability, no caller-controlled URL/path/ID/cursor, and no cursor following. Capability absence skips that source. |
| C08 | The download projection adds exactly an own `media_id` (UUID or null) and `sort_at_ms`, replacing `created_at_ms`. X selects the first cataloged asset by ascending ordinal with a UUID media id; YouTube uses the request media id when it is a UUID; an invalid non-null media id becomes null. |
| C09 | `sort_at_ms` prefers a valid nonnegative `updated_at_ms`, falls back to a valid `created_at_ms`, and omits a row when neither is valid. Merge deduplicates by `(source, request_id)`, sorts by `sort_at_ms` descending, then source ascending and request ID descending, and retains five. An older-created/newer-updated row sorts above an older-created row. |
| C10 | State mapping is complete for X active/terminal states and YouTube `queued`/`processing`/`downloading`/`completed`/`completed_private`/`failed`/`unavailable`; unknown or malformed rows produce no row; analysis/publication/catalog presence never create a completion claim. |
| C11 | A download row with an own media id renders a `button.download-history-row.download-history-row--action` with the three visible spans and an accessible name that includes the label and an explicit open action. Clicking posts exactly one `open_details` with that media id, posts no `REVIEW_INBOX_OPENED`, does not retry or remove the row, and remains clickable after read. A null-media row renders a non-focusable `div.download-history-row` with no click/link/button/mutation. |
| C12 | The sidebar has the separate `#download-history` block, Recent downloads heading, inert list, `Companion history` caption, `Recent review history`/`Full review history` labels, `All` accessible name `Show full review history`, toggle behavior and empty/failure height behavior as accepted. |
| C13 | Review-only, download-only, empty, failed and mixed states render correctly. A download-read failure hides all Downloads rows but retains the review list and badge count. A review-list/pagination/cursor failure hides all history and clears the badge. |
| C14 | Stale-context handling covers origin, configuration revision, capabilities, history source and identity login. A changed login with identical capabilities discards the whole result as stale. Sidebar refreshes are single-flight; hidden polling stops; reconnect/reset/runtime invalidation clears downloads; late generations are discarded. |
| C15 | Privacy: only the signed-in requester's own X/YouTube request data appears; the administrator inbox stays separate; no foreign title, URL, thumbnail, request ID, state or failure detail; no raw URL, asset array, media filename, provider payload or failure detail reaches the sidebar; the only linked media is the row's own cataloged media; no download snapshot is persisted. |
| C16 | The badge remains the server `unopened_count` for the active review source; download outcomes never contribute; the alarm makes no download-list calls; no second counter or notification permission exists. |
| C17 | Download documentation truth: `SPEC.md`, `PRODUCT.md`, `docs/X_COMPANION.md`, `SECURITY.md` and `DEVELOPMENT.md` agree on the separate block, own-media click, inert no-media rows, no opened mutation, latest-update order and 50/5 window. ADR-0090 is accepted and indexed; ADR-0089's body is unchanged and only its inert-row/creation-order statements are superseded. |
| C18 | Companion-hosted Timeline: status/visibility glyphs are hidden; Kind, Status and Visibility render as readable text labels with values; the title has no line clamp and wraps fully; the wide page keeps the glyph table and two-line clamp. |
| C19 | Companion Filter: one `Filter` button precedes `#kronika-timeline-filters`, has `type=button`, `aria-controls`, initial `aria-expanded=false`, toggles `is-collapsed` and `aria-expanded`; the form is collapsed by default in the companion; the wide page hides the button and keeps the filters visible; filter query semantics and all four menus are unchanged. |
| C20 | Companion My contributions: the row uses the available width and the title control fills it, wrapping on words/spaces, never one character per line; metadata, badges and actions remain readable; the wide multi-column grid is unchanged. |
| C21 | The wide/full-page Timeline and My contributions behavior is unchanged, including the glyph table, always-visible filters and multi-column contributions grid. The correction report's full-page narrow My contributions LEAD is recorded as an out-of-scope residual, not a companion failure. |
| C22 | Independent test evidence at the candidate: previous whole suites focused Python 46, focused Node 114, broader Python 206, broader Node 64; compact UI focused 44, affected frontend 287, served-shell Python contract 211. Record actual counts and any failure signature. |
| C23 | `git diff --check` is clean; the worktree is clean after validation; the staged/committed path lists match C02; documentation links resolve. |
| C24 | The blocked `02_report_01.md` is a delivery failure in a different session, not a candidate change. The foreign `02_rereport_00.md`, if present, is another whole's trace artifact and is not in the repository; neither changes the candidate. |
| C25 | The residual YouTube acquisition `INSPECTION_OUTPUT_LIMIT` and the full-page narrow My contributions LEAD are outside this companion acceptance and do not fail it. |
| C26 | No acceptance, publication, deployment, production-acceptance or closure claim is made by this report; only the independent acceptance phase result is reported. |

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
git rev-parse HEAD HEAD^ HEAD^^ HEAD^^^ HEAD^^^^
git show --name-only --format= HEAD
git diff --name-only e64f2b0..35c58b6
git diff --name-only b543602..35c58b6
git diff --check e64f2b0..35c58b6
git diff e64f2b0..35c58b6 -- extension/manifest.json
git diff --name-only e64f2b0..35c58b6 -- src
```

Use synthetic fixtures only. Do not run a full suite, browser evidence, real acquisition, provider calls or NUC commands. Do not modify the repository or tests.

## Report contract

Write the terminal report to the exact report path. Begin it exactly with:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three exchange coordinates exactly once (`07`/`01`). Include status, candidate, start and end commit, changed paths, the full C01–C26 matrix with evidence, exact test counts, defects and residual risks, independence statement, Orchestration critique with MEASURED and LEAD findings or none, and one proposed next step. Use `Phase-qualified result: acceptance-PASS` only if every control passes; otherwise use status `PARTIAL` or `BLOCKED` with `Phase-qualified result: not-applicable` and exact evidence. Use `Logical-whole closure: not-closed` and `Report justification: final-acceptance`.

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
