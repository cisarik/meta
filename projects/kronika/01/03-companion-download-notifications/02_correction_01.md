# Companion download notifications — identity-context correction

## Routing and authority

Persistent role identity: WORKER
Logical whole identity: companion-download-notifications
Worker session ordinal: 02
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: CORRECT-COMPANION-DOWNLOAD-IDENTITY-CONTEXT-01
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — one bounded privacy check and one regression
Recommended context capacity: approximately 250k tokens
Implementation authority: explicit
Exact baseline: cc8f67965213ee9b22d113cc200776c42f6503ba
Changed-path allowlist: exactly these two paths and no others: `extension/background/service_worker.js`; `tests/companion_review_extension.test.js`
Implementation boundaries: identity-login comparison in the existing aggregation context check and its regression only
Independence required: no

Continuity anchor: implementation report `02_report_00.md` and local candidate commit `cc8f67965213ee9b22d113cc200776c42f6503ba`
Authority renewal: prior implementation authority expired at `02_report_00.md`; this exchange grants complete correction-only authority
Evidence posture: non-independent

This prompt continues the exact existing implementation session 02. Retained context is convenience, not authority. Re-gate the repository and environment before acting. If retained context conflicts with current repository evidence, stop and report the conflict. A fresh independent full acceptance follows this correction; this exchange does not grant acceptance, publication or closure.

## Finding

Candidate `cc8f67965213ee9b22d113cc200776c42f6503ba` is the accepted implementation candidate: parent `e64f2b0`, clean worktree, exactly the 15 allowlisted paths, focused and broader checks passing, manifest unchanged, public `main` still `e64f2b0`.

One concrete privacy finding remains:

**C1 — the final aggregation context check does not compare the identity login.**

`historyListRoute()` in `extension/background/service_worker.js` captures the configured origin, the in-memory configuration revision and the identity capabilities, but not the identity login. `aggregationContextMatches()` compares origin, revision, capabilities and history source only. A login change with identical capabilities can therefore pass the final check. Review rows from one identity could be combined with download rows from another identity.

This contradicts the accepted plan's requirement that the final identity/capability check match the initial context and the whole's own-download privacy boundary. The existing test named "changed identity" changes capabilities, not the login; it does not cover this case.

## Required correction

1. In `historyListRoute()`, capture the identity login from the `/api/identity/me` response and carry it in the route context alongside origin, revision and capabilities. Use an empty string when the field is absent so test fixtures remain deterministic.
2. In `aggregationContextMatches()`, fetch the current identity and require its login to equal the captured login in addition to the existing origin, revision, capability and history-source checks. A mismatch returns `false`, so the caller returns the existing stale-context result with no review rows, no download rows and no new badge application.
3. Add a regression in `tests/companion_review_extension.test.js` that changes only the identity login while capabilities stay identical. Assert `stale: true`, `ok: false`, empty review and download items, and the existing badge behavior. Keep or rename the existing capability-change test so the two cases are distinct.
4. Do not change the response shape, UI, documentation, API, badge, permissions, storage, message types or mutation count.

## Repository and route

Repository identity: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Repository checkout topology: standalone checkout with pinned `.ap` submodule
Expected branch: main
Expected HEAD: cc8f67965213ee9b22d113cc200776c42f6503ba
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50 at `/Users/agile/Projects/kronika/.ap`

The Orchestrator observed public `main` still equal to `e64f2b0` on 2026-11-11; do not use the network. Verify:

- `git -C /Users/agile/Projects/kronika status --porcelain=v1 -b` is clean and reports `## main...origin/main [ahead 1]`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD` equals `cc8f67965213ee9b22d113cc200776c42f6503ba`;
- `git -C /Users/agile/Projects/kronika rev-parse HEAD^` equals `e64f2b0f92458fac2590e03672e30da62275b345`;
- `git -C /Users/agile/Projects/kronika/.ap rev-parse HEAD` equals the governing AP pin;
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
Downloadable prompt filename: 02_correction_01.md
Destination path: /Users/agile/meta/projects/kronika/01/03-companion-download-notifications
Report filename: 02_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: exactly the two allowlisted repository paths
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/03-companion-download-notifications/02_report_01.md

## Authority

Positive authority: read-only inspection of the repository, the accepted plan, `02_report_00.md` and this prompt at `/Users/agile/meta/projects/kronika/01/03-companion-download-notifications/02_correction_01.md`; modify exactly `extension/background/service_worker.js` and `tests/companion_review_extension.test.js`; run the selected AP and Node commands below; check the exact report destination; create exactly one local commit on `main` on top of `cc8f679`; and create/read back `02_report_01.md`.

Commands: `./.ap/ap project check`, `./.ap/ap exec` with the exact baseline and declared operations, `node --test` with the selected suites, read-only Git inspection, exact-path `git add`, one local `git commit`, and the native file writer for the exact report path. Do not invoke raw `.venv/bin/python`, `python`, `python3` or `poetry run`.

Git authority: one local commit on `main` on top of `cc8f679`, subject `fix: bind download history to the identity context`. Stage exactly the two allowlisted paths; never `git add .` or `git add -A`. No fetch, push, force, amend, reset, clean, stash, checkout, switch, tag or remote change.

Network authority: none. Secret authority: none. Do not read `private/`, `.venv`, credentials, browser profiles, cookies or unrelated paths.

Negative authority: any change outside the two allowlisted paths; any UI, documentation, API, schema, migration, manifest, permission, badge, storage key, alarm or message-type change; any push, publication, deployment, full suite, browser run, NUC access, provider call or secret access; any edit to the plan, `01_report_00.md`, `02_report_00.md`, notes, handout or run map; any acceptance or closure claim.

## Validation

Run the focused Node selection first:

```text
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline cc8f67965213ee9b22d113cc200776c42f6503ba
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline cc8f67965213ee9b22d113cc200776c42f6503ba --operation runtime-info
node --test tests/companion_review_extension.test.js tests/x_companion_extension.test.js
```

Then the adjacent companion selection:

```text
node --test tests/companion_web_bridge.test.js tests/companion_settings_automatic_analysis.test.js tests/youtube_request_cockpit.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js
```

Run `git diff --check`, `git status --porcelain=v1`, inspect the exact diff and verify the committed path list is exactly the two allowlisted paths. Python tests are not required for this JS-only correction; the project check and runtime-info are the AP envelope evidence. Do not run a full suite, browser evidence, real acquisition, provider calls or NUC commands.

## Report contract

Write the terminal report to `02_report_01.md`. Begin it exactly with:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three exchange coordinates exactly once (`02`/`02` for this exchange). Include the finding, the exact change, the new regression, the test commands and counts, the new commit SHA and parent, the staged and committed path lists, and Orchestration critique with MEASURED and LEAD findings or none. Use `Phase-qualified result: implementation-PASS` only if the correction and all selected checks pass; otherwise `PARTIAL` or `BLOCKED` with exact evidence. Use `Logical-whole closure: not-closed` and `Report justification: new-mutation`.

Direct-write the report, read it all back, verify content, path and SHA-256, and only then send a short separate completion notice. If the report path already exists, including an empty file, stop and report the collision. If the client blocks the exact write, return the complete report and state `File delivery: pending client restriction`.

Do not claim acceptance, publication, deployment or closure. A fresh independent full acceptance follows.

## Stopping conditions

Stop and report the exact blocker if:

- this is not the exact implementation session 02 or its continuity anchor does not match;
- HEAD is not `cc8f679`, the parent is not `e64f2b0`, or the worktree is not clean;
- the finding cannot be reproduced from the current candidate;
- a required change falls outside the two-path allowlist;
- a selected test fails for a reason outside this correction;
- the report path already exists or its parent/symlink resolution is unsafe;
- the client cannot write the report or run a required command;
- secrets, private data, browser state or another ungranted effect would be touched.

After a prerequisite stop, only report preparation and necessary cleanup inside this grant may finish. Preserve the first causal failure.

## Authority expiry

This grant expires at the terminal correction report, cancellation or supersession. Retained context, a green test run, the local commit or a later conversation is not acceptance or closure authority.
