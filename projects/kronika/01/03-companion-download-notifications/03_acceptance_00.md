# Companion download notifications — independent full acceptance

## Routing and authority

Persistent role identity: WORKER
Logical whole identity: companion-download-notifications
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: ACCEPT-COMPANION-DOWNLOAD-NOTIFICATIONS-01
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — own-download privacy, companion protocol guard and corrected identity-context boundary
Recommended context capacity: approximately 250k tokens
Independence required: yes
Acceptance candidate: 647e6da11416559f1bef52d53e9743acbd2bb688
Acceptance owner map: companion-download-notifications-v1 — accepted plan `01_report_00.md`, `SPEC.md` companion requirements, ADR-0089, `docs/X_COMPANION.md`, `PRODUCT.md`, `SECURITY.md`, and the four confirmed Cooperator choices
Acceptance allowlist: exactly these 15 whole-diff paths and no others: `DEVELOPMENT.md`; `PRODUCT.md`; `SECURITY.md`; `SPEC.md`; `docs/X_COMPANION.md`; `docs/adr/0089-companion-own-download-status-history.md`; `docs/adr/README.md`; `extension/background/service_worker.js`; `extension/shared/messages.js`; `extension/ui/sidebar.css`; `extension/ui/sidebar.html`; `extension/ui/sidebar.js`; `tests/companion_review_extension.test.js`; `tests/contract/test_x_request_api.py`; `tests/contract/test_youtube_request_api.py`
Acceptance risk claims: R1 own-download privacy and no foreign data; R2 review-only badge and no second counter; R3 no new backend, route, schema, permission, message type, alarm, storage key or mutation; R4 download-read failure isolation, polling and stale-context behavior; R5 companion test pins and manifest permissions; R6 documentation truth and the four product choices; R7 identity-login correction C1; R8 no acceptance, publication or closure claim
Acceptance control matrix: C01–C22 below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates

This is a genuinely fresh independent acceptance session. You did not implement this candidate or participate in its correction. Do not rely on the implementation Worker's retained context or on this Orchestrator's conclusions. Verify the candidate, the plan, the repository and the test evidence independently. Do not fix any finding; report it. A correction requires a new Orchestrator grant.

## Candidate and accepted inputs

Candidate `647e6da11416559f1bef52d53e9743acbd2bb688` contains the implementation commit `cc8f67965213ee9b22d113cc200776c42f6503ba` (parent `e64f2b0f92458fac2590e03672e30da62275b345`) and the corrected commit `647e6da11416559f1bef52d53e9743acbd2bb688` (parent `cc8f67965213ee9b22d113cc200776c42f6503ba`).

Read and reconcile these accepted inputs as claims, not proof:

- `01_report_00.md` — the decision-complete plan.
- `02_report_00.md` — the implementation report at `cc8f679`.
- `02_report_01.md` — a blocked correction exchange delivered to a different session; it made no repository change and is not the candidate.
- `02_report_02.md` — the correction report at `647e6da`.
- `00_notes.md` — Orchestrator reconciliation.
- `00_handout.md` — the provisional seed, frozen historical evidence.

The COOPERATOR confirmed four product choices on 2026-11-11:

1. A separate Recent downloads block inside the existing history sheet, preserving review ordering.
2. Static status rows with no unseen marker, counter, acknowledgement, expiry or persistence.
3. If either capability-enabled download read fails, hide the entire Downloads block while retaining review history and its badge count.
4. YouTube rows use the video identifier; all download rows are inert, with no click, Details, retry or opened action. X rows use the claim title with the `X post <id>` fallback.

The implementation commit's own status is `implementation-PASS`; the correction adds the identity-login comparison. This acceptance decides whether the whole candidate is accepted, not whether to close the whole.

## Repository and route

Repository identity: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Repository checkout topology: standalone checkout with pinned `.ap` submodule
Expected branch: main
Expected HEAD: 647e6da11416559f1bef52d53e9743acbd2bb688
Expected parent: cc8f67965213ee9b22d113cc200776c42f6503ba
Expected grandparent: e64f2b0f92458fac2590e03672e30da62275b345
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50 at `/Users/agile/Projects/kronika/.ap`

The Orchestrator observed public `main` equal to `e64f2b0` on 2026-11-11; do not use the network. Verify the local repository gate:

- `git -C /Users/agile/Projects/kronika status --porcelain=v1 -b` is clean and reports `## main...origin/main [ahead 2]`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD` equals the candidate;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^` equals `cc8f679`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^^` equals `e64f2b0`;
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
Downloadable prompt filename: 03_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/01/03-companion-download-notifications
Report filename: 03_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/03-companion-download-notifications/03_report_00.md

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
| C01 | Repository identity, branch, candidate HEAD, both parents, clean worktree, `.ap` gitlink/HEAD and public-main observation match the declared values. |
| C02 | The whole diff `e64f2b0..647e6da` is exactly the 15-path allowlist. The correction commit `cc8f679..647e6da` is exactly `extension/background/service_worker.js` and `tests/companion_review_extension.test.js`. |
| C03 | `extension/manifest.json` is unchanged; permissions are exactly `alarms`, `sidePanel`, `storage`; no `notifications`, `host_permissions`, `externally_connectable` or new optional permission. |
| C04 | No backend, schema, migration, API route, `tailscale_ingress.py` policy, `companion_mutation` route, alarm, message type or persisted storage key changed. Exactly six `companion_mutation` routes remain. |
| C05 | `review_inbox` keeps its message type and request shape. A successful response adds `downloads: {ok, items}`; download failure is exactly `{ok:false, items:[]}`; successful empty is `{ok:true, items:[]}`. No second message type or transport is introduced. |
| C06 | `review_inbox` is restricted to the extension's own sidebar sender: `sender.id`, `sender.url` and `sender.origin` match the sidebar document. Missing or mismatched metadata makes no network call and does not clear the badge. Other message branches retain their behavior. |
| C07 | The X and YouTube download reads use the existing fixed `pathFor()` templates and configured origin, with `limit=5`, one first page per available capability, no caller-controlled URL/path/ID/cursor, and no cursor following. Capability absence skips that source. |
| C08 | Merge is deterministic: deduplicate by `(source, request_id)` keeping the first occurrence; order by `created_at_ms` descending, source ascending, request ID descending; retain at most five. Labels are the X claim title or `X post <id>`, and `YouTube video <id>`, bounded to 240 code points; no media-detail fetch. |
| C09 | State mapping is complete: X active states and YouTube `queued`/`processing`/`downloading` -> `Saving…`; X/YouTube `completed` -> `Saved`; YouTube `completed_private` -> `Saved privately`; X `completed_partial` -> `Partly saved`; X `duplicate_resolved` -> `Already saved`; terminal failed -> `Download failed`; X `catalog_removed`/YouTube `unavailable` -> `Unavailable`. Unknown or malformed rows produce no row. Analysis, publication and catalog presence never create a completion claim. |
| C10 | The sidebar has a separate `#download-history` block inside `#review-history`, a Recent downloads heading, an inert `#download-history-list`, and no button/link/Details/retry/opened action. The `#review-history::before` caption is `Companion history`; review-list labels are `Recent review history` and `Full review history`; `All` says `Show full review history`; visible `All` text is unchanged. |
| C11 | The history toggle is enabled when either review rows or download rows exist, starts closed on panel load, preserves the user's expanded choice across refreshes, and hides `All` for download-only history. Empty or failed Downloads occupies no height. |
| C12 | Review-only, download-only, empty, failed, and mixed states render correctly. A download-read failure hides all Downloads rows but retains the complete review list and its server badge count. A review-list/pagination/cursor failure still hides all history and clears the badge. |
| C13 | Stale-context handling covers origin, configuration revision, capabilities, history source and identity login. A changed login with identical capabilities discards the whole result as `stale`, with no review rows, no download rows and no new badge application. |
| C14 | Sidebar refreshes are single-flight; overlapping timer ticks are skipped; hidden-panel polling is stopped; reconnect, reset and runtime invalidation clear displayed downloads; late responses from an older generation are discarded. |
| C15 | Privacy: only the signed-in requester's own X/YouTube request data appears. The administrator's global analyzed inbox remains separate; no foreign analyzed title becomes download activity. The projection has no foreign title, URL, thumbnail, request ID, state or failure detail; no raw URL, asset array, media filename, provider payload or failure detail reaches the sidebar; no download snapshot is persisted. |
| C16 | The badge remains the server `unopened_count` for the active review source; download outcomes never contribute; the one-minute alarm makes no download-list calls; no second counter or notification permission exists. |
| C17 | Correction C1 is present and exercised: the identity login is captured in the route context, required in `aggregationContextMatches()`, and the same-capability login-change regression asserts `stale`, `ok:false`, empty review/download items and unchanged badge. The capability-change regression remains distinct. |
| C18 | Documentation truth: `SPEC.md` preserves X-only own-history and review-only badge semantics, adds the bounded Downloads block, narrows `open_details` to review rows and keeps review pagination fail-closed. `PRODUCT.md`, `docs/X_COMPANION.md`, `SECURITY.md` and `DEVELOPMENT.md` agree. ADR-0089 is accepted and indexed; ADR-0076 is supplemented, not rewritten. `docs/UX_AUDIT.md` is untouched. No changed document still says every history row opens Details. |
| C19 | Independent focused Python selection passes at the candidate baseline: 46 tests. Independent focused Node selection passes: 110 tests across the two files. Independent broader Python selection passes: 206 tests. Independent broader Node selection passes: 64 tests. Record actual counts and any failure signature. |
| C20 | `git diff --check` is clean; the worktree is clean after validation; the staged/committed path lists match C02; documentation links resolve. |
| C21 | The blocked exchange `02_report_01.md` is a delivery failure in a different session, not a candidate change. The foreign `02_rereport_00.md` is another whole's trace artifact, is not in the repository, and was not modified by this whole. Neither changes the candidate. |
| C22 | No acceptance, publication, deployment, production-acceptance or closure claim is made by this report; only the independent acceptance phase result is reported. |

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
git rev-parse HEAD HEAD^ HEAD^^
git show --name-only --format= HEAD
git diff --name-only e64f2b0..647e6da
git diff --name-only cc8f679..647e6da
git diff --check e64f2b0..647e6da
git diff e64f2b0..647e6da -- extension/manifest.json
git diff --name-only e64f2b0..647e6da -- src
```

Use synthetic fixtures only. Do not run a full suite, browser evidence, real acquisition, provider calls or NUC commands. Do not modify the repository or tests.

## Report contract

Write the terminal report to the exact report path. Begin it exactly with:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three exchange coordinates exactly once (`03`/`01`). Include status, candidate, start and end commit, changed paths, the full C01–C22 matrix with evidence, exact test counts, defects and residual risks, independence statement, Orchestration critique with MEASURED and LEAD findings or none, and one proposed next step. Use `Phase-qualified result: acceptance-PASS` only if every control passes; otherwise use status `PARTIAL` or `BLOCKED` with `Phase-qualified result: not-applicable` and exact evidence. Use `Logical-whole closure: not-closed` and `Report justification: final-acceptance`.

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
