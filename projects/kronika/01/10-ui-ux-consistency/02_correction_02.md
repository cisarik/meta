# Authoritative Worker prompt — Kronika whole 10, Worker session 02, exchange 03

Activation: this file is the exact issued Worker prompt for the logical whole
`ui-ux-consistency`. It is stored under the Meta filename mapping
`<worker-session>_<phase>_<meta-exchange-index>.md` as
`02_correction_02.md`. The matching terminal report is `02_report_02.md`.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: ui-ux-consistency
Worker session ordinal: 02
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded UI Polish Worker
Phase: Correction
Task identity: KRN-UX-CORR-03 — keep Timeline current on question detail routes
Delivery route: manual Cooperator delivery
Reasoning recommendation: Low — one bounded current-marking correction and its regression test
Recommended context capacity: approximately 120k tokens
Independence required: no
Continuity anchor: terminal implementation-PASS report 02_report_01.md and local candidate 27aa5fd29f259ee27de109f37bb7cf88f255b93f
Authority renewal: prior correction authority expired; this prompt grants a new bounded correction
Evidence posture: non-independent correction; a fresh independent E2 re-acceptance follows
```

You are continuing the healthy same Worker session that produced
`27aa5fd29f259ee27de109f37bb7cf88f255b93f`. The prior authority expired. This
prompt grants a new, complete, bounded correction. Retained context is
convenience, not authority; re-gate the repository and stop on any conflict.

Before substantive work, confirm that `Native planning mode: not-used` is the
actual client state (native Plan mode OFF). If it is enabled, stop and return
`BLOCKED` naming the contradiction.

## 1. Orchestrator finding

The History removal was implemented by deleting the `request`/`record` branch
from `kronikaMarkCurrent` in `src/kronika/adapters/api/web/app.js`. Those two
routes are still real, reachable from Timeline rows through `#/requests/...`
and `#/records/...`, and they still render the primary navigation. With the
branch deleted, neither Timeline nor Gallery is marked current on those pages,
while `#/details/...` still marks Gallery and `#/review/...` still marks
Review.

This is a visible consistency gap, not a request to restore History. The
Timeline is the single overview under ADR-0088 and question links open from
Timeline rows, so the Timeline browsing tab must remain current on a request or
record detail route.

Required behavior:

- `#/requests/{operation_id}` and `#/records/{record_id}` mark the Timeline
  browsing link `aria-current="page"` and remove it from every other browsing
  or action link.
- `#/details/{media_id}` still marks Gallery.
- `#/review/shared` and `#/review/requests` still mark Review.
- No History link, section, route or `aria-current` value is reintroduced.
- The `#/history` and `#/history/records` fold to Timeline is unchanged.
- No route, API, authorization, payload, schema, stored data, Gallery/Details
  behavior, search behavior, filter order, glyph or documentation change.

## 2. Allowlist and negative scope

Change only these paths, and only for this finding:

```text
src/kronika/adapters/api/web/app.js
tests/kronika_ui.test.js
```

If the fix requires any other path, stop and report `BLOCKED`; do not widen the
correction. Negative allowlist: every other repository path, especially any
API, repository, domain, application service, persistence, authorization,
capability, route-policy, schema, migration, public-composition, preview route,
Gallery/Details renderer, provider, capture, companion, dependency, asset,
deployment or host file; `.ap/**`; the AP gitlink; `AGENTS.md`;
`ap.project.conf`; and all Meta files except the terminal report.

The expected implementation is the smallest one: map `request` and `record` to
`timeline` in `kronikaMarkCurrent`, beside the existing `details` → `gallery`
and `review-shared`/`review-requests` → `review` mappings. Do not add a second
router, stored origin state, or new navigation structure.

## 3. Baseline and gate

```text
Repository: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Expected branch: main
Baseline commit under test: 27aa5fd29f259ee27de109f37bb7cf88f255b93f
Parent of the correction commit: 27aa5fd29f259ee27de109f37bb7cf88f255b93f
Public main: bbf776c462e1eb5eccb91eb027a85eee9055d2ec (27aa5fd is local and unpushed)
Containing-repository .ap gitlink: d7023cf037f6d17885c3ede5c04812c61640da50
Submodule HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
```

Verify before editing:

```text
git rev-parse HEAD
git status --short
git log --oneline -2
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 27aa5fd29f259ee27de109f37bb7cf88f255b93f
```

Stop if the worktree is not clean or HEAD is not `27aa5fd`.

## 4. Tests and validation

Run from `/Users/agile/Projects/kronika`:

```text
# [MacBook / fish]
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 27aa5fd29f259ee27de109f37bb7cf88f255b93f
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 27aa5fd29f259ee27de109f37bb7cf88f255b93f --operation test-focus -- tests/contract/test_local_web_application.py -q -p no:cacheprovider
node --test tests/kronika_ui.test.js tests/gallery_search_tag_filters.test.js tests/gallery_filter_controls.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js
git diff --check
git status --short
#------------------------------------------------------
```

Extend the existing grouping/current-state test or add one focused regression
test that asserts:

- a request route marks Timeline current and removes current from Gallery,
  Search, Research and Review;
- a record route marks Timeline current;
- a Details route still marks Gallery;
- a shared-review route still marks Review;
- no History browsing link or History current state exists.

Do not weaken or delete an existing test. Do not run the full Python suite.
Classify pre-existing failures with evidence; do not repair unrelated behavior.
Rendered alignment and the Cooperator's final visual acceptance remain after a
later deployment.

## 5. Authority

```text
Positive authority: edit exactly the two allowlisted paths; read-only inspection
  of the repository, the accepted plan, the correction and acceptance reports,
  current shell source and this whole's Meta notes; run the exact gate and tests
  above; stage exactly the changed allowlisted paths and create exactly one
  normal corrective local commit on main; exact direct-write of the terminal
  report below if it is absent, followed by a complete readback.

Negative authority: any other file edit, creation, deletion or rename; any API,
  repository, domain, application, persistence, authorization, capability,
  route-inventory, schema, migration, public-composition, preview-route,
  Gallery/Details, provider, capture, companion, dependency, asset, network,
  deployment or host change; any accepted ADR or durable document edit; any Git
  push, fetch, pull, merge, rebase, reset, restore, clean, stash, checkout,
  switch, branch, tag, remote, config write or amend; any NUC, SSH, sudo,
  deploy, browser, provider, secret or private-media access; any acceptance,
  publication, deployment or closure claim.

Git authority: read-only inspection plus exactly one normal corrective commit
  on main of the changed allowlisted paths; no push and no amend.
Network authority: none.
Secret authority: none.
```

## 6. Commit and report

After the selected tests pass and `git diff --check` is clean, stage exactly the
changed allowlisted paths and create one corrective commit:

```text
git add -- src/kronika/adapters/api/web/app.js tests/kronika_ui.test.js
git diff --cached --check
git commit -m "fix: keep Timeline current on question details"
git show --stat --oneline HEAD
git status --short
```

Do not push. Report the commit SHA and its parent.

Write the terminal report to:

```text
/Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/02_report_02.md
```

The report starts exactly with `### Report for ORCHESTRATOR_CHAT`, echoes the
coordinates and role fields, and contains:

```text
status: PASS
Phase-qualified result: implementation-PASS
Start commit: 27aa5fd29f259ee27de109f37bb7cf88f255b93f
End commit: <correction commit SHA>
Report justification: new-mutation
Logical-whole closure: not-closed
```

Include the finding, the exact current-marking change, the regression-test
identity, the changed paths and diff stat, gate and test commands with actual
counts, any deviation or residual risk, `Resolved Execution Issues /
Near-Misses`, `Pre-Existing Failure Classification`, one smallest next step, and
the orchestration critique. Do not claim acceptance, publication, deployment or
closure.

## 7. Delivery and trace

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/
Trace project key: kronika
Trace logical-whole projection identity: 10-ui-ux-consistency
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_correction_02.md
Destination path: /Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/
Report filename: 02_report_02.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: exactly the changed allowlisted paths
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/02_report_02.md
```

If the report path exists, including an empty file, stop `BLOCKED` without
overwriting it.

## 8. Mandatory reading

- `02_report_01.md` and the `kronikaMarkCurrent`, route, shell and navigation
  test regions it names.
- `02_correction_01.md` sections 1-3.
- `.ap/AP.md` at the pinned commit: §2 Roles; §3 Instances, Sessions, and Worker
  Session Profiles; §5 Task Authority; §6 Adaptive Orchestration Lifecycle; §7
  Orchestrator Responsibilities; §12 Validation and Public Verification; §13
  Artifact Lifecycle; §15 Fresh-Slice Implementation and Diagnostic Closeout;
  §17 Compact Communication; and the Finite Convergence Contract.
- `.ap/AP_WORKER.md` in full and `.ap/PROMPT_CONTRACTS.md` Worker Report Header,
  Correction Record, Common Worker Task Fields, Mutation Axes, Validation
  Ladder and Pre-Existing Failure Classification.
- `AGENTS.md`, `SPEC.md`, ADR-0088 and the current navigation tests.

## Visible delivery capsule

```text
🟡 Ready for delivery
Recipient: Bounded UI Polish Worker · current-worker-session · manual
Recommendation: Low · approximately 120k tokens
Client: Native Plan Mode OFF
Prompt: /Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/02_correction_02.md
Report: /Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/02_report_02.md
Archival: wait-for-report
```
