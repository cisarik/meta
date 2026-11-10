# Authoritative Worker prompt — Kronika whole 09, Worker session 02, exchange 03

Activation: this file is the exact issued Worker prompt for the logical whole
`timeline-complete-chronicle`. It is stored under the Meta filename mapping
`<worker-session>_<phase>_<meta-exchange-index>.md` as
`02_correction_02.md`. The matching terminal report is `02_report_02.md`.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: timeline-complete-chronicle
Worker session ordinal: 02
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Correction
Task identity: KRN-TCC-CORR-02 — restore Timeline Retry and add chronicle header/field labels
Delivery route: manual Cooperator delivery
Reasoning recommendation: Medium — one bounded UI correction in the existing shell, its markup and its Node contract
Recommended context capacity: approximately 250k tokens
Independence required: no
Continuity anchor: terminal implementation-PASS report 02_report_01.md and candidate commit 264a040e104e7495ce649fa583c4f0f3c1241b7c
Authority renewal: prior implementation authority expired; this prompt grants a new bounded correction grant for two confirmed non-security UI gaps
Evidence posture: non-independent correction; the correction cannot self-certify, and a fresh independent re-acceptance follows
```

You are continuing the healthy same Worker session that produced candidate
`264a040e104e7495ce649fa583c4f0f3c1241b7c`. The prior implementation authority
expired. This prompt grants a new, complete, bounded correction grant. Retained
context is convenience, not authority; re-gate the repository and stop on any
conflict with current evidence.

Before substantive work, confirm that `Native planning mode: not-used` is the
actual client state (native Plan mode OFF). If it is enabled, stop and return
`BLOCKED` naming the contradiction.

## 1. Confirmed findings

The independent acceptance report `03_report_00.md` passed C01–C24 but recorded
two non-security UI gaps against the accepted plan §7.1–§7.2:

1. **Retry is hidden after a same-query refresh failure.** `kronikaAcceptList`
   marks the exact same query stale and clears `list.error`; `kronikaLoadTimeline`
   then hides `#kronika-timeline-retry`. The plan requires retaining the last
   page for the exact same identity and query, clearly marked stale, with Retry.
2. **The chronicle lacks its desktop visual header and per-field labels.**
   Rows have no `aria-hidden` column header and no per-field accessible labels
   using the existing `visually-hidden` utility; at 720 px and below the row
   values have no visible field labels. The plan §7.1 requires a desktop visual
   header, per-field accessible labels, and visible labels on narrow screens.

Neither gap changes authorization, the payload, the route or the stored data.

## 2. Exact correction

Change only the following paths, and only where needed:

```text
src/kronika/adapters/api/web/app.js
src/kronika/adapters/api/web/index.html
src/kronika/adapters/api/web/styles.css
tests/kronika_ui.test.js
tests/contract/test_local_web_application.py
```

Required behavior:

### 2.1 Timeline Retry on stale same-query refresh

- When a Timeline refresh for the exact same identity and query fails at the
  transport or response level, keep the last authorized page, keep the existing
  stale status text, and expose the existing `#kronika-timeline-retry` control.
- Retry must retry the exact current route/query and must not steal focus.
- A first-load failure keeps its existing error and Retry behavior.
- A changed-query failure must not retain another query's rows; preserve the
  existing clearing/error behavior.
- Do not add automatic retries, polling or a second retry control.

### 2.2 Chronicle header and field labels

- Add one desktop visual header adjacent to the chronicle list, outside the
  `<ol>` so the list remains valid HTML. It is `aria-hidden="true"` and aligns
  with the row grid. Columns: Preview, Item, Kind, Added, Status, Visibility.
- Each row keeps its accessible field labels using the existing
  `visually-hidden` utility: Kind, Added, Status and Visibility. The preview is
  decorative; the title link remains the row's primary accessible name.
- At 720 px and below, those field labels become visible beside the wrapped
  values, the header is hidden, and rows remain one item per row. No horizontal
  page scrolling at 320 px; preserve 44 px interactive targets.
- Keep the existing compact list, preview slot, status/visibility text, links,
  focus behavior and Gallery/Details freeze. Do not apply `.kronika-card`,
  Gallery hover transforms or large cover imagery to chronicle rows.
- Do not simulate an ARIA grid or add custom arrow-key navigation.

### 2.3 Tests

Update or add causal Node tests in `tests/kronika_ui.test.js` proving:

- a same-query refresh failure keeps the previous rows and exposes Retry, and
  activating Retry reuses the exact current route/query without focus theft;
- a changed-query failure does not retain another query's rows;
- the desktop header is `aria-hidden` and the row field labels are present and
  accessible; at the narrow breakpoint the labels are visible and the header is
  hidden;
- existing preview, stale-response, identity-loss, dirty-navigation,
  visibilitychange and pagehide regressions remain intact.

If `tests/contract/test_local_web_application.py` pins the served Timeline
markup, update its exact expected markup/selectors only for the new header and
labels; do not weaken unrelated shell, Gallery or Details assertions.

## 3. Baseline, allowlist and negative scope

```text
Repository: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Expected branch: main
Baseline commit under test: 264a040e104e7495ce649fa583c4f0f3c1241b7c
Parent of the correction commit: 264a040e104e7495ce649fa583c4f0f3c1241b7c
Public main: b66ec8f50860ace624f6be1fd3ad63f521edcd33 (candidate is local and unpushed)
Containing-repository .ap gitlink: d7023cf037f6d17885c3ede5c04812c61640da50
Submodule HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
```

Verify before editing:

```text
git rev-parse HEAD
git status --short
git log --oneline -2
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 264a040e104e7495ce649fa583c4f0f3c1241b7c
```

Stop if the worktree is not clean or HEAD is not the candidate. Negative
allowlist: no change to any API/repository/domain/audience/route-policy/schema/
migration/public-composition path, any documentation or ADR, `index.html`
content outside the Timeline header/labels, Gallery/Details renderer bodies or
player behavior, `AGENTS.md`, the access inventory, the plan/notes/reports, or
any other path. If a required change falls outside the five allowlisted paths,
stop and report.

## 4. Validation

Run from `/Users/agile/Projects/kronika`:

```text
# [MacBook / fish]
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 264a040e104e7495ce649fa583c4f0f3c1241b7c
node --test tests/kronika_ui.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 264a040e104e7495ce649fa583c4f0f3c1241b7c --operation test-focus -- tests/contract/test_local_web_application.py -k 'kronika_shell or details or persistent_preview or initial_card or available_cards or gallery' -q -p no:cacheprovider
git diff --check
git status --short
#------------------------------------------------------
```

The corrected candidate must pass all selected tests. Do not run the full
Python suite. Classify any pre-existing failure with exact evidence; do not
repair unrelated behavior.

## 5. Authority

```text
Positive authority: edit exactly the five paths above; read-only inspection of
  the repository, the accepted plan, ADR-0087, the implementation and acceptance
  reports, and this whole's Meta notes; run the exact gate and tests above;
  stage exactly the changed allowlisted paths and create exactly one normal
  corrective local commit on main; exact direct-write of the terminal report
  below if it is absent, followed by a complete readback.

Negative authority: any other file edit, creation, deletion or rename; any
  change to API, repository, domain, audience, route, schema, migration,
  public composition, docs, ADRs, Gallery/Details, index.html outside the
  Timeline header/labels, or tests other than the two allowed test files; any
  Git push, fetch, pull, merge, rebase, reset, restore, clean, stash, checkout,
  switch, branch, tag, remote, config write or amend; any dependency, NUC, SSH,
  sudo, deploy, browser, provider, secret or private-media access; any
  acceptance, publication, deployment or closure claim.

Git authority: read-only inspection plus exactly one normal corrective commit
  on main of the changed allowlisted paths; no push and no amend.
Network authority: none.
Secret authority: none.
```

## 6. Commit and report

After the tests pass and `git diff --check` is clean, stage exactly the changed
paths and create one corrective commit:

```text
git add -- <the changed allowlisted paths>
git diff --cached --check
git commit -m "fix: restore Timeline retry and chronicle labels"
git show --stat --oneline HEAD
```

Do not push. Report the correction commit SHA and its parent.

Write the terminal report to:

```text
/Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_report_02.md
```

The report starts exactly with `### Report for ORCHESTRATOR_CHAT`, echoes the
coordinates and role fields, and contains:

```text
status: PASS
Phase-qualified result: implementation-PASS
Start commit: 264a040e104e7495ce649fa583c4f0f3c1241b7c
End commit: <correction commit SHA>
Report justification: new-mutation
Logical-whole closure: not-closed
```

Include the two findings, the exact correction, the changed paths and diff stat,
the gate and Node/local-web test commands with actual pass/fail counts, the new
or updated test identities and what they prove, the correction commit, any
deviation or residual risk, `Resolved Execution Issues / Near-Misses`,
`Pre-Existing Failure Classification`, one smallest next step, and the
orchestration critique. Do not claim acceptance, publication, deployment or
closure.

## 7. Delivery and trace

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/
Trace project key: kronika
Trace logical-whole projection identity: 09-timeline-complete-chronicle
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_correction_02.md
Destination path: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/
Report filename: 02_report_02.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: exactly the changed paths among the five UI allowlisted paths
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_report_02.md
```

If the report path exists, including an empty file, stop `BLOCKED` without
overwriting it.

## Visible delivery capsule

```text
🟡 Ready for delivery
Recipient: Bounded Correction Worker · current-worker-session · manual
Recommendation: Medium · approximately 250k tokens
Client: Native Plan Mode OFF
Prompt: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_correction_02.md
Report: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_report_02.md
Archival: wait-for-report
```
