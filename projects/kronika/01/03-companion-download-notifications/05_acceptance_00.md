# Companion download notifications — fresh independent re-acceptance

## Routing and authority

Persistent role identity: WORKER
Logical whole identity: companion-download-notifications
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: ACCEPT-COMPANION-DOWNLOAD-NOTIFICATIONS-02
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — own-media privacy, an interactive companion row, latest-update ordering and the corrected identity-context boundary
Recommended context capacity: approximately 250k tokens
Independence required: yes
Acceptance candidate: b5436029c66da69c1d14c0f378cbea07bdc74a40
Acceptance owner map: companion-download-notifications-v2 — accepted plan `01_report_00.md`, `SPEC.md`, ADR-0089, ADR-0090, `docs/X_COMPANION.md`, `PRODUCT.md`, `SECURITY.md`, the four original Cooperator choices and the two rendered amendments
Acceptance allowlist: exactly these 16 whole-diff paths and no others: `DEVELOPMENT.md`; `PRODUCT.md`; `SECURITY.md`; `SPEC.md`; `docs/X_COMPANION.md`; `docs/adr/0089-companion-own-download-status-history.md`; `docs/adr/0090-companion-download-row-details-and-latest-update-order.md`; `docs/adr/README.md`; `extension/background/service_worker.js`; `extension/shared/messages.js`; `extension/ui/sidebar.css`; `extension/ui/sidebar.html`; `extension/ui/sidebar.js`; `tests/companion_review_extension.test.js`; `tests/contract/test_x_request_api.py`; `tests/contract/test_youtube_request_api.py`
Acceptance risk claims: R1 own-download privacy and no foreign data; R2 review-only badge and no second counter; R3 no new backend, route, schema, permission, message type, alarm, storage key or mutation; R4 download-read failure isolation, polling and stale-context behavior; R5 companion test pins and manifest permissions; R6 documentation truth and the confirmed/amended choices; R7 identity-login correction C1; R8 clickable own-media rows and latest-update order; R9 no acceptance, publication or closure claim
Acceptance control matrix: C01–C23 below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates

This is a genuinely fresh independent acceptance session. You did not implement the candidate, the identity correction or the amended download-row correction. Do not rely on any implementation session's retained context or on this Orchestrator's conclusions. Verify the candidate, the reports, the repository and the test evidence independently. Do not fix any finding; report it. A correction requires a new Orchestrator grant.

## Candidate and accepted inputs

Candidate `b5436029c66da69c1d14c0f378cbea07bdc74a40` contains:

- `cc8f67965213ee9b22d113cc200776c42f6503ba` — implementation, parent `e64f2b0`;
- `647e6da11416559f1bef52d53e9743acbd2bb688` — identity-login correction, parent `cc8f679`;
- `b5436029c66da69c1d14c0f378cbea07bdc74a40` — clickable own-media rows and latest-update correction, parent `647e6da`.

Read and reconcile these accepted inputs as claims, not proof:

- `01_report_00.md` — the decision-complete plan.
- `02_report_00.md` — implementation report at `cc8f679`.
- `02_report_01.md` — a blocked correction exchange delivered to a different session; no repository change.
- `02_report_02.md` — identity-login correction at `647e6da`.
- `03_report_00.md` — independent acceptance of `647e6da` (superseded for the amended boundary).
- `04_report_00.md` — amended download-row correction at `b543602`.
- `00_notes.md` — Orchestrator reconciliation, including the rendered amendments.
- `00_handout.md` — the frozen provisional seed.
- `02_correction_03.md` — the prepared, unissued predecessor correction; design context only.

The COOPERATOR confirmed the original four choices and then amended two of them after rendering `647e6da`:

1. A separate Recent downloads block inside the existing history sheet, preserving review ordering.
2. Static status rows with no unseen marker, counter, acknowledgement, expiry or persistence.
3. If either capability-enabled download read fails, hide the entire Downloads block while retaining review history and its badge count.
4. **Amended from inert rows:** a download row with an own cataloged media id opens hosted Details through the existing `open_details` message, including after the save was read. Rows without a media id remain inert.
5. **Amended from newest creation:** order by the most recent request update, newest to oldest. The read window is the first page at `limit=50` per source and retains five rows.

The residual YouTube acquisition failure with sanitized `INSPECTION_OUTPUT_LIMIT` and the full-page Timeline/My contributions layout findings are separate logical wholes. They are not candidate defects and must not fail this acceptance.

## Repository and route

Repository identity: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Repository checkout topology: standalone checkout with pinned `.ap` submodule
Expected branch: main
Expected HEAD: b5436029c66da69c1d14c0f378cbea07bdc74a40
Expected parent: 647e6da11416559f1bef52d53e9743acbd2bb688
Expected grandparent: cc8f67965213ee9b22d113cc200776c42f6503ba
Expected great-grandparent: e64f2b0f92458fac2590e03672e30da62275b345
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50 at `/Users/agile/Projects/kronika/.ap`

The Orchestrator observed public `main` equal to `647e6da` on 2026-11-13; do not use the network. Verify the local repository gate:

- `git -C /Users/agile/Projects/kronika status --porcelain=v1 -b` is clean and reports `## main...origin/main [ahead 1]`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD` equals the candidate;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^` equals `647e6da`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^^` equals `cc8f679`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^^^` equals `e64f2b0`;
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
Downloadable prompt filename: 05_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/01/03-companion-download-notifications
Report filename: 05_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/03-companion-download-notifications/05_report_00.md

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
| C01 | Repository identity, branch, candidate HEAD, all three parents, clean worktree, `.ap` gitlink/HEAD and public-main observation match the declared values. |
| C02 | The whole diff `e64f2b0..b543602` is exactly the 16-path allowlist. The amendment commit `647e6da..b543602` is exactly the 12 allowed correction paths. No `src`, Alembic or manifest change. |
| C03 | `extension/manifest.json` is unchanged; permissions are exactly `alarms`, `sidePanel`, `storage`; no `notifications`, `host_permissions`, `externally_connectable` or new optional permission. |
| C04 | No backend, schema, migration, API route, `tailscale_ingress.py` policy, `companion_mutation` route, alarm, message type or persisted storage key changed. Exactly six `companion_mutation` routes remain. |
| C05 | `review_inbox` keeps its message type and request shape. A successful response adds `downloads: {ok, items}`; download failure is exactly `{ok:false, items:[]}`; successful empty is `{ok:true, items:[]}`. No second message type or transport is introduced. |
| C06 | `review_inbox` is restricted to the extension's own sidebar sender: `sender.id`, `sender.url` and `sender.origin` match the sidebar document. Missing or mismatched metadata makes no network call and does not clear the badge. Other message branches retain their behavior. |
| C07 | The X and YouTube download reads use the existing fixed `pathFor()` templates and configured origin, with `limit=50`, one first page per available capability, no caller-controlled URL/path/ID/cursor, and no cursor following. Capability absence skips that source. |
| C08 | The projection adds exactly an own `media_id` (UUID or null) and `sort_at_ms`, replacing `created_at_ms`. X selects the first asset by ascending ordinal whose state is `cataloged` and whose media id is a UUID; YouTube uses the request media id when it is a UUID; an invalid non-null media id becomes null. No foreign or unknown media id is linked. |
| C09 | `sort_at_ms` prefers a valid nonnegative `updated_at_ms`, falls back to a valid `created_at_ms`, and omits a row when neither is valid. Merge deduplicates by `(source, request_id)` keeping the first occurrence, sorts by `sort_at_ms` descending, then source ascending and request ID descending, and retains five rows. An older-created/newer-updated row sorts above an older-created row. |
| C10 | State mapping is complete: X active states and YouTube `queued`/`processing`/`downloading` -> `Saving…`; X/YouTube `completed` -> `Saved`; YouTube `completed_private` -> `Saved privately`; X `completed_partial` -> `Partly saved`; X `duplicate_resolved` -> `Already saved`; terminal failed -> `Download failed`; X `catalog_removed`/YouTube `unavailable` -> `Unavailable`. Unknown or malformed rows produce no row. Analysis, publication and catalog presence never create a completion claim. |
| C11 | A download row with an own media id renders a `button.download-history-row.download-history-row--action` with the three visible spans and an accessible name that includes the label and an explicit open action. Clicking posts exactly one `open_details` with that media id via the existing hosted bridge, posts no `REVIEW_INBOX_OPENED`, does not retry or remove the row, and remains clickable after the save was read. A row with a null media id renders a non-focusable `div.download-history-row` with no click/link/button/mutation. No nested interactive elements, `innerHTML`, `aria-live` or new animation; button hover/focus uses existing tokens and non-action rows do not look clickable. |
| C12 | The sidebar has the separate `#download-history` block inside `#review-history`, the Recent downloads heading, the inert list, the `Companion history` caption, the `Recent review history`/`Full review history` labels, and the `All` accessible name `Show full review history` with visible `All` text unchanged. The toggle is enabled when either review or download rows exist, starts closed, preserves the user's expanded choice, and hides `All` for download-only history. Empty or failed Downloads occupies no height. |
| C13 | Review-only, download-only, empty, failed, and mixed states render correctly. A download-read failure hides all Downloads rows but retains the complete review list and its server badge count. A review-list/pagination/cursor failure still hides all history and clears the badge. |
| C14 | Stale-context handling covers origin, configuration revision, capabilities, history source and identity login. A changed login with identical capabilities discards the whole result as `stale`, with no review rows, no download rows and no new badge application. Sidebar refreshes are single-flight; overlapping timer ticks are skipped; hidden-panel polling is stopped; reconnect, reset and runtime invalidation clear displayed downloads; late responses from an older generation are discarded. |
| C15 | Privacy: only the signed-in requester's own X/YouTube request data appears. The administrator's global analyzed inbox remains separate; no foreign analyzed title becomes download activity. The projection has no foreign title, URL, thumbnail, request ID, state or failure detail; no raw URL, asset array, media filename, provider payload or failure detail reaches the sidebar; the only linked media is the row's own cataloged media; no download snapshot is persisted. |
| C16 | The badge remains the server `unopened_count` for the active review source; download outcomes never contribute; the one-minute alarm makes no download-list calls; no second counter or notification permission exists. |
| C17 | Documentation truth: `SPEC.md` preserves X-only own-history and review-only badge semantics, adds the separate Downloads block, states the own-media click, inert no-media rows, no opened mutation, latest-update order and the 50/5 read window, narrows `open_details` to review/own-media rows, and keeps review pagination fail-closed. `PRODUCT.md`, `docs/X_COMPANION.md`, `SECURITY.md` and `DEVELOPMENT.md` agree. ADR-0090 is accepted and indexed; ADR-0089's body is unchanged and only its inert-row and creation-order statements are superseded. `docs/UX_AUDIT.md` is untouched. No changed document still says every download row is inert or that order is by creation. |
| C18 | Independent focused Python selection passes at the candidate baseline: 46 tests. Independent focused Node selection passes: 114 tests across the two files. Independent broader Python selection passes: 206 tests. Independent broader Node selection passes: 64 tests. Record actual counts and any failure signature. |
| C19 | `git diff --check` is clean; the worktree is clean after validation; the staged/committed path lists match C02; documentation links resolve. |
| C20 | The blocked exchange `02_report_01.md` is a delivery failure in a different session, not a candidate change. The foreign `02_rereport_00.md` is another whole's trace artifact, is not in the repository, and was not modified by this whole. Neither changes the candidate. |
| C21 | The rendered amendments are actually implemented: read/opened saves remain clickable when an own media id exists, no-media rows stay inert, and latest-update order is visible in the merge and tests. No residual of the superseded inert/creation behavior remains in the changed code or docs. |
| C22 | The residual YouTube acquisition `INSPECTION_OUTPUT_LIMIT` and the full-page Timeline/My contributions layout findings are correctly left outside this candidate; they do not fail the companion acceptance. |
| C23 | No acceptance, publication, deployment, production-acceptance or closure claim is made by this report; only the independent acceptance phase result is reported. |

## Validation

Run the exact selected checks at the candidate:

```text
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline e64f2b0f92458fac2590e03672e30da62275b345
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline e64f2b0f92458fac2590e03672e30da62275b345 --operation runtime-info
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline e64f2b0f92458fac2590e03672e30da62275b345 --operation test-focus -- tests/contract/test_x_request_api.py tests/contract/test_youtube_request_api.py tests/contract/test_companion_review_api.py -q -p no:cacheprovider
node --test tests/companion_review_extension.test.js tests/x_companion_extension.test.js
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline e64f2b0f92458fac2590e03672e30da62275b345 --operation test-focus -- tests/contract/test_tailscale_ingress_security.py tests/contract/test_requester_private_youtube_details.py tests/unit/application/test_x_acquisition_lifecycle.py tests/integration/test_youtube_acquisition_lifecycle.py tests/unit/infrastructure/persistence/test_companion_review_repository.py tests/unit/domain/test_x_acquisition_domain.py tests/unit/domain/test_youtube_acquisition.py -q -p no:cacheprovider
node --test tests/companion_web_bridge.test.js tests/companion_settings_automatic_analysis.test.js tests/youtube_request_cockpit.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js
```

Also run the read-only repository checks:

```text
git status --porcelain=v1 -b
git rev-parse HEAD HEAD^ HEAD^^ HEAD^^^
git show --name-only --format= HEAD
git diff --name-only e64f2b0..b543602
git diff --name-only 647e6da..b543602
git diff --check e64f2b0..b543602
git diff e64f2b0..b543602 -- extension/manifest.json
git diff --name-only e64f2b0..b543602 -- src
```

Use synthetic fixtures only. Do not run a full suite, browser evidence, real acquisition, provider calls or NUC commands. Do not modify the repository or tests.

## Report contract

Write the terminal report to the exact report path. Begin it exactly with:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three exchange coordinates exactly once (`05`/`01`). Include status, candidate, start and end commit, changed paths, the full C01–C23 matrix with evidence, exact test counts, defects and residual risks, independence statement, Orchestration critique with MEASURED and LEAD findings or none, and one proposed next step. Use `Phase-qualified result: acceptance-PASS` only if every control passes; otherwise use status `PARTIAL` or `BLOCKED` with `Phase-qualified result: not-applicable` and exact evidence. Use `Logical-whole closure: not-closed` and `Report justification: final-acceptance`.

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
