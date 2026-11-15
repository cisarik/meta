# 03 companion-download-notifications — Orchestrator notes

```text
Logical whole identity: companion-download-notifications
Development run identity: kronika-run-01
Orchestrator session scope: logical-whole
Opened: 2026-11-11
Opening actor: fresh per-whole Orchestrator
Handout: /Users/agile/meta/projects/kronika/01/03-companion-download-notifications/00_handout.md
Handout status at opening: provisional, then frozen on open; never edited in place
Predecessor whole: 02-upload-flow-polish (closed 2026-11-10 at e64f2b0)
Run map: /Users/agile/meta/projects/kronika/01/00_RUN_MAP.md (entry 03 provisional at opening; run-scoped Orchestrator owns run status)
Repository: https://github.com/cisarik/kronika
Local checkout: /Users/agile/Projects/kronika
Baseline: e64f2b0f92458fac2590e03672e30da62275b345
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50
```

## Opening decision

On 2026-11-11 the COOPERATOR selected `companion-download-notifications` as the
next bounded logical whole. The whole opens under the logical-whole
Orchestrator session scope. The run map entry remains `provisional` until the
run-scoped Orchestrator refreshes it from this whole's own evidence; this note
does not edit the run map or the frozen handout.

The COOPERATOR's instruction was to implement this whole to the best achievable
quality without errors in this session or in the generated professional
prompts. No repository, host, NUC, publication or deployment authority is
created by this opening.

## Handout Revalidation Record

```text
Handout revalidation: /Users/agile/meta/projects/kronika/01/03-companion-download-notifications/00_handout.md
Received handout status: provisional
Revalidated against: Kronika e64f2b0f92458fac2590e03672e30da62275b345; AP d7023cf037f6d17885c3ede5c04812c61640da50; .ap gitlink and submodule HEAD d7023cf037f6d17885c3ede5c04812c61640da50; public main e64f2b0f92458fac2590e03672e30da62275b345; predecessor closure record in 02-upload-flow-polish/00_notes.md; ADR-0076, ADR-0086, ADR-0087, ADR-0088; docs/X_COMPANION.md; docs/UX_AUDIT.md; docs/AP_UPGRADE_OBSERVATIONS.md
Usable facts: worktree clean; HEAD equals public main; AP doctor PASS; ap project check --baseline e64f2b0 PASS; predecessor 02 closed with production-acceptance-PASS at e64f2b0; entries 01, 09 and 10 also closed; no active Worker or mutation; companion title-bar history, ordinary own-history, administrator inbox and server unopened badge exist; own-history is requester-private cataloged X Saves in every analysis state; pending rows never increment the badge; YouTube terminal phases completed, completed_private, failed and unavailable exist; GET /api/youtube/requests and request-detail routes exist; docs/UX_AUDIT.md recommendation 3 asks for completed companion downloads in the side-panel history; the declared upgrade ledger has one active accepted non-authorizing entry
Stale facts and corrections: HEAD/public main 246c9f8 -> e64f2b0; predecessor "provisional: not opened and not closed" -> closed 2026-11-10 at e64f2b0 with production-acceptance-PASS; NUC 7ee4684 -> not observed, last recorded deployment e64f2b0 in the predecessor closure record, current SSH transport timeout; "Timeline is administrator-approved; History is personal" -> ADR-0087 complete visibility-aware chronicle and ADR-0088 Timeline as the single overview with History removed; "upload flow polish" listed among other candidates -> already closed; handout premise that the existing own-history read path carries X and YouTube -> own-history is X-only, while YouTube requests use GET /api/youtube/requests and the content-script request poll
Not revalidated: NUC active/web/capture release, service state, database revision and backup restore-readiness (SSH transport timeout; no NUC access); rendered UI/UX state on the NUC (same reason); the COOPERATOR's delivery-route selection for this whole (to be asked once around the first Planner)
Handout disposition: adopted-with-corrections
```

## Stage 1 evidence

- Repository gate: `git status --porcelain=v1 -b` reports only
  `## main...origin/main`; `git rev-parse HEAD` and `git ls-remote origin
  refs/heads/main` both return `e64f2b0f92458fac2590e03672e30da62275b345`.
- AP gate: `.ap` gitlink `d7023cf037f6d17885c3ede5c04812c61640da50`, submodule
  HEAD equal, `./.ap/ap doctor` PASS, `./.ap/ap project check --root
  /Users/agile/Projects/kronika --baseline e64f2b0...` PASS.
- Predecessor: `02-upload-flow-polish/00_notes.md` records production
  acceptance PASS at `e64f2b0` and `Logical-whole closure:
  closed-by-ORCHESTRATOR`; the notes are frozen.
- Upgrade ledger: `docs/AP_UPGRADE_OBSERVATIONS.md` declares
  `upgrade https://github.com/cisarik/ap.git`, storage version 1, with one
  active `accepted` entry, `consumer-declared-execution-and-capability-route-binding`.
  The entry remains consistent with current `.ap` RF-16, the project
  `ap.project.conf` execution operations, the canonical Worker execution
  contract and the NUC SSH gate. It is non-authorizing and was not written.
- NUC: `deploy/ubuntu/kronika-release status` failed at transport (exit 20).
  The project gate reports `ssh-agent: ready`, but a bounded BatchMode SSH
  connection timed out. The last recorded deployment is `e64f2b0` from the
  predecessor closure record; this is a recorded claim, not independent current
  observation.
- Active mutation and Workers: none. No repository, host, NUC, Git, publication
  or deployment mutation occurred in Stage 1.

## Companion evidence relevant to the first Planner

- `docs/X_COMPANION.md` describes one title-bar history
  (`#review-history-toggle`, `#review-history`, `#review-history-list`,
  `#review-history-all`) above the hosted iframe.
- Administrators (`media.workflow.read`) use
  `GET /api/companion/review-inbox`; ordinary `x.request` identities use
  `GET /api/companion/own-history`; otherwise history chrome hides.
- Ordinary own-history rows are actor-owned cataloged X Saves in every analysis
  state, movies excluded. Pending rows are plain, never carry `--unopened`, and
  never increment the badge.
- The toolbar badge is the server `unopened_count` rendered as `1`…`99` /
  `99+`; administrators refresh it from inbox `limit=1`, ordinary identities
  from own-history `limit=1`; alarm `kronika.review-inbox` runs every 1 minute.
  There is no `notifications` permission and no second counter.
- YouTube request terminal phases `completed`, `completed_private`, `failed`
  and `unavailable` exist in the web shell and in
  `GET /api/youtube/requests`; the companion YouTube content script polls its
  own request detail while the player control is active, but the side-panel
  own-history read path does not include YouTube requests.
- `docs/UX_AUDIT.md` recommendation 3 is the product origin of this whole:
  "Surface completed companion downloads (X and YouTube) as a notification in
  the side panel history."

## Next step

Ask the COOPERATOR once for the delivery route, then issue the first Planner
prompt under `01/01`, `fresh-worker-session`, `Native planning mode: required`,
and the direct-write report at `01_report_00.md`. The Planner is read-only for
the repository and produces one decision-complete implementation plan; it does
not implement.

## Delivery route — 2026-11-11

The COOPERATOR selected **manual copy-paste delivery** for this whole. He will
deliver each complete Worker prompt to the selected Worker session himself.
The selection is preserved for subsequent grants unless a materially changed
capability, cost, security or independence axis reopens it. The first Planner
prompt is `01_planning_00.md`; its report destination is `01_report_00.md`.
The recommended Planner route is High reasoning with approximately 250k
context and native Plan Mode ON. No repository or host mutation occurred.

## Trace restoration note and reconciled record — 2026-11-13

The working-tree `00_notes.md` was found restored to its 2026-11-11 committed
version (109 lines). The later uncommitted Orchestrator entries were lost from
the working tree. The exact prompt/report pairs and the conversation remain the
evidence. This consolidated record reconstructs the Orchestrator decisions; it
does not invent new authority or rewrite the surviving early entries.

- First Planner report `01_report_00.md` was received after native Plan Mode
  blocked the Worker's direct write; the COOPERATOR persisted the plan. The plan
  was accepted after the COOPERATOR confirmed the four product choices: a
  separate Recent downloads block, static rows without unseen/counter/
  acknowledgement/persistence, independent Downloads failure hiding with review
  history and badge retained, and inert YouTube rows labelled by video id.
- Implementation prompt `02_implementation_00.md` added `PRODUCT.md` for the
  same stale "every history row" claim; implementation PASS was reported at
  `cc8f67965213ee9b22d113cc200776c42f6503ba` across the 15 allowlisted paths.
- Orchestrator review found C1: the final aggregation context check did not
  compare the identity login. Correction `02_correction_01.md` was misdelivered
  to a different session and returned `02_report_01.md` BLOCKED with no change.
  Reissued `02_correction_02.md` succeeded at
  `647e6da11416559f1bef52d53e9743acbd2bb688` (parent `cc8f679`) across
  `extension/background/service_worker.js` and
  `tests/companion_review_extension.test.js`.
- Independent fresh acceptance `03_report_00.md` returned acceptance-PASS for
  `647e6da` with C01–C22 PASS and focused/broader counts 46 / 110 / 206 / 64.
- Publication PASS: normal push `e64f2b0..647e6da`, direct public readback
  `647e6da`. NUC deployment PASS: `kronika-release check --release 647e6da`
  PASS; `deploy --release 647e6da --yes` exit 0; post-deploy status active/web
  `647e6da`, capture `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`, service active,
  database revision `0035`, backup restore-readiness ready. Terminal `sudo -K`
  returned 0; `sudo -n true` requires a password.
- Rendered acceptance returned PARTIAL on 2026-11-13 with the amendments below.

## Amended Cooperator expectations — 2026-11-13

The COOPERATOR owns these amendments. They supersede only the named earlier
choices; the rest of the accepted design remains.

1. **Superseded:** all download rows are inert and do not open Details.
   **Amended:** a download row with an own cataloged media id opens hosted
   Details, including when the save was already read. Rows without a media id
   remain inert.
2. **Superseded:** newest creation first. **Amended:** most recently downloaded
   or updated first, newest to oldest, using the request's last update.

Residuals outside this companion block:

- YouTube acquisition failed in inspection with sanitized
  `INSPECTION_OUTPUT_LIMIT`. The COOPERATOR classifies it as a separate logical
  whole, not a correction of the download-status surface.
- The full-page Timeline clips text and spaces status/visibility emoji oddly;
  My contributions shows a severe vertical-text layout. The COOPERATOR
  classifies this as a separate UI/UX whole.

The correction is `02_correction_03.md` for clickable own-media rows and
latest-update ordering, followed by a fresh independent re-acceptance,
republication, NUC refresh and a new rendered acceptance. The whole remains
open; `647e6da` remains the published notification foundation, but its rendered
acceptance does not cover the amended boundary.

## Fresh correction session — 2026-11-13

The implementation/correction session 02 is no longer available. The prepared
`02_correction_03.md` was not issued, so coordinates `02/04` are not consumed.
A genuinely fresh Bounded Correction Worker session is selected at `04/01`:
prompt `04_correction_00.md`, report `04_report_00.md`.

The correction scope and design are unchanged from the prepared amendment:
clickable own-media download rows that open hosted Details even after read,
inert rows when no own media id exists, latest-update ordering, the bounded
50/5 read window, tests and the matching documentation plus ADR-0090. The
fresh Worker must establish the repository and code evidence independently and
must not rely on session 02 context. No repository or host mutation occurred.

## Amendment correction PASS — 2026-11-13

Fresh correction `04_report_00.md` reports implementation-PASS at
`b5436029c66da69c1d14c0f378cbea07bdc74a40` (parent
`647e6da11416559f1bef52d53e9743acbd2bb688`) across exactly 12 paths. The
projection now carries an own `media_id` and `sort_at_ms`; X selects the first
cataloged asset by ordinal; YouTube uses the request media id; rows with an own
media id open hosted Details through the existing `open_details` message and
stay clickable after read; rows without a media id are inert; the read window is
first page `limit=50` and retains five newest updates. ADR-0090 records the
amendment and supersedes only ADR-0089's inert-row and creation-order
statements.

Independent Orchestrator re-verification at `b543602`:
`ap project check --baseline 647e6da` PASS; focused Python 46; focused Node 114;
broader Python 206; broader Node 64; `git diff --check` clean; manifest and
`src` unchanged; whole diff `e64f2b0..b543602` is 16 paths; correction
`647e6da..b543602` is 12 paths. Public `main` remains `647e6da`; local `main`
is ahead 1.

The candidate is accepted for a fresh independent full re-acceptance. The next
prompt is `05_acceptance_00.md` for fresh Worker session 05/01 with
`Acceptance independence: required-fresh-independent`; report
`05_report_00.md`. The residual YouTube acquisition and full-page
Timeline/My contributions findings remain separate logical wholes and are not
acceptance blockers for this companion block. No publication, deployment or
closure is claimed.

## Fresh re-acceptance PASS — 2026-11-13

`05_report_00.md` records a genuinely fresh independent acceptance of
`b5436029c66da69c1d14c0f378cbea07bdc74a40` with all C01–C23 controls PASS,
defects none, and the exact selected counts: focused Python 46, focused Node
114, broader Python 206, broader Node 64. The report confirms the own-media
click, inert no-media rows, latest-update order and the 50/5 window, and keeps
the identity-login, badge and privacy controls intact.

```text
Phase-qualified result: acceptance-PASS
Result artifact or commit: b5436029c66da69c1d14c0f378cbea07bdc74a40
Result evidence: independent fresh re-acceptance 05_report_00.md; C01–C23 PASS;
  focused Python 46; focused Node 114; broader Python 206; broader Node 64;
  ap project check PASS; git diff --check clean; manifest and src unchanged
Required preceding results: implementation-PASS at b543602; acceptance-PASS
Cooperator-owned decisions: four original choices plus two rendered amendments
  confirmed; publication, deployment and rendered acceptance remain open
Residual-risk disposition: open for rendered companion and NUC phase; the
  residual YouTube acquisition and Timeline/My contributions findings remain
  separate logical wholes
Upgrade-ledger reconciliation: complete for this phase — the one active
  accepted non-authorizing entry remains unchanged and retain-active
Active mutation: none
Closure actor: ORCHESTRATOR
Logical-whole closure: not-closed
```

Two non-blocking process observations:

- The acceptance report discloses a `python3 -c` symlink probe for the report
  destination. That is outside the Cursor Worker raw-interpreter prohibition,
  but the same check was already established with `ls -ld`; the probe did not
  run tests, touch the repository or alter the acceptance evidence. It is
  recorded as a Worker-execution near-miss, not a candidate defect.
- `02_rereport_00.md` is no longer present in this trace directory or under
  `/Users/agile/meta`; it was another whole's artifact and was not part of this
  candidate. Its relocation or removal is outside this whole's authority. The
  candidate diff and `git ls-files` contain neither it nor `02_report_01.md`.

Publication to public `main`, NUC deployment and the COOPERATOR's rendered
acceptance remain separate later grants. The whole remains open.

## Amendment publication and deployment PASS — 2026-11-13

The COOPERATOR authorized publication and the routine NUC deployment of the
amended candidate. Publication was a normal non-force push
`647e6da..b543602` on `main`; direct `git ls-remote origin refs/heads/main`
readback returned `b5436029c66da69c1d14c0f378cbea07bdc74a40`; local `HEAD`,
`origin/main` and the public ref match; the worktree is clean.

`kronika-release check --release b543602...` PASS: public main `b543602`, AP
gitlink `d7023cf`, backup restore-readiness ready. The canonical helper
completed `deploy --release b543602... --yes` with exit 0. Post-deploy `status`
reports `active_release` and `web_release`
`b5436029c66da69c1d14c0f378cbea07bdc74a40`, capture release unchanged
`5b86d896b3ea03f89fef2c90f7af2c121d0ef915`, `service_active: active`,
`database_revision: 0035` and `backup_restore_readiness: ready`.

Terminal `sudo -K` through the operator gate returned exit 0; a following
`sudo -n true` reports that a password is required, the expected released
lifecycle state. No host identifier, credential or secret is recorded.

The final rendered acceptance of the amended companion remains. The NUC refresh
alone does not reload the unpacked extension; the COOPERATOR must reload it from
the published `b543602` revision and refresh the source tabs.

## Final rendered acceptance PARTIAL — 2026-11-13

The COOPERATOR reloaded `b543602` and returned: 1 PASS, 2 PASS, 3 PASS, 4 PASS,
5 NOT TESTED, 6 RESIDUAL (YouTube inspection `INSPECTION_OUTPUT_LIMIT`), 7 PASS,
8 FAIL, 9 PASS, 10 "no separate logical whole; fix all mentioned defects here",
11 PARTIAL.

The companion download block itself passed the click/read and latest-update
checks. The remaining FAIL is the **companion-rendered Timeline and My
contributions narrow layout**:

- The Timeline card still shows the visibility/status emoji stack and hides the
  status/visibility text; the title is clipped at two lines. The COOPERATOR wants
  no visibility emoji, readable status/visibility text and an uncut title in the
  companion.
- The four Timeline filters (Publication, Kind, Status, Visibility) are always
  expanded. The COOPERATOR wants them behind one **Filter** button in the
  companion, expanding on click for a compact panel.
- The My contributions page renders the title as one character per line at the
  companion width; it must use the full row width and wrap normally.

The COOPERATOR explicitly refused a separate logical whole for these defects:
"10) NIE NECHCEM TO AKO SAMOSTATNY LOGICKY CELOK VYRIESME TO TU TAK AKO CHCEM
VYRIESIT VSETKY SPOMINANE NEDOSTATKY/BUGY KTORE SPOMINAM". This is a
Cooperator-directed scope amendment of the current whole, not a new feature
objective. It supersedes the plan's earlier "no web-shell implementation
change" exclusion for this bounded companion-rendered UI closeout only.

The correction is `06_correction_00.md` for fresh Worker session 06/01 at
baseline `b543602`: the served web shell's Timeline/My contributions narrow
layout, the compact Filter disclosure, tests and matching documentation. The
download block's 16-path candidate remains accepted at `b543602`; the new
correction is a local commit on top. A fresh re-acceptance follows, then
publication, NUC refresh and another rendered acceptance. YouTube acquisition
remains the separate residual; item 5 remains NOT TESTED but its control is
already covered by tests. No repository or host mutation occurred.

## Compact companion UI correction PASS — 2026-11-13

Fresh correction `06_report_00.md` reports implementation-PASS at
`35c58b693bc885dc115d91df3c6e64680d0c79aa` (parent
`b5436029c66da69c1d14c0f378cbea07bdc74a40`) across exactly 10 paths. The
companion-hosted Timeline now shows Kind/Status/Visibility as text without
status or visibility glyphs and without the two-line title clamp; one Filter
button toggles the existing four filters with `aria-expanded`/`is-collapsed`;
the wide page keeps its glyph table and always-visible filters; companion My
contributions gives the title the row width and normal word wrapping, while the
wide grid remains.

Independent Orchestrator re-verification at `35c58b6`: the focused UI checks
44 pass, the affected frontend selection 287 pass, the served-shell Python
contract 211 pass; the earlier whole suites remain green (46/114/206/64) and
will be re-run in the fresh re-acceptance. The whole diff `e64f2b0..35c58b6` is
22 paths; the correction `b543602..35c58b6` is 10. Public `main` remains
`b543602`; local `main` is ahead 1.

One non-blocking LEAD from the correction report: the full-page My
contributions at a viewport below 720 px can still collapse the title because
`.workspace-media-browser .admin-media-row` outranks the 720 px rule. The
companion-hosted rule is specific enough and fixes the reported companion
screenshot. The Cooperator's rendered acceptance should test the companion; if
he also wants the narrow full page fixed, that is a bounded follow-up.

The next prompt is `07_acceptance_00.md` for fresh Worker session 07/01 with
`Acceptance independence: required-fresh-independent`; report
`07_report_00.md`. The YouTube acquisition residual remains separate. No
publication, deployment or closure is claimed.

## Compact UI re-acceptance PASS — 2026-11-13

`07_report_00.md` records a genuinely fresh independent re-acceptance of
`35c58b693bc885dc115d91df3c6e64680d0c79aa` with all C01–C26 controls PASS,
defects none, and the declared counts: previous whole focused Python 46,
focused Node 114, broader Python 206, broader Node 64; compact UI focused Node
44, affected frontend 287, served-shell Python 211. The report confirms the
download block, identity-login discard, clickable own-media rows, latest-update
order, compact companion Timeline text, Filter disclosure, companion My
contributions wrapping, and the unchanged wide page.

```text
Phase-qualified result: acceptance-PASS
Result artifact or commit: 35c58b693bc885dc115d91df3c6e64680d0c79aa
Result evidence: independent fresh re-acceptance 07_report_00.md; C01–C26 PASS;
  focused Python 46; focused Node 114; broader Python 206; broader Node 64;
  compact UI Node 44; affected frontend 287; served-shell Python 211;
  ap project check PASS; git diff --check clean; manifest unchanged
Required preceding results: implementation-PASS at 35c58b6; acceptance-PASS
Cooperator-owned decisions: original four choices, two download-row amendments
  and compact companion UI confirmed; publication, deployment and rendered
  acceptance remain open
Residual-risk disposition: open — rendered companion behavior and NUC phase;
  YouTube acquisition INSPECTION_OUTPUT_LIMIT and the full-page narrow My
  contributions LEAD remain outside this companion boundary
Upgrade-ledger reconciliation: complete for this phase — the one active
  accepted non-authorizing entry remains unchanged and retain-active
Active mutation: none
Closure actor: ORCHESTRATOR
Logical-whole closure: not-closed
```

Publication to public `main`, NUC deployment and the COOPERATOR's rendered
acceptance remain separate later grants. The whole remains open.

## Compact UI publication and deployment PASS — 2026-11-13

The COOPERATOR authorized publication and the routine NUC deployment. The
candidate was pushed normally without force: `b543602..35c58b6` on `main`.
Direct `git ls-remote origin refs/heads/main` readback returned
`35c58b693bc885dc115d91df3c6e64680d0c79aa`; local `HEAD`, `origin/main` and the
public ref match; the worktree is clean.

The NUC became reachable and `kronika-release check --release 35c58b6...` PASS:
public main `35c58b6`, AP gitlink `d7023cf`, backup restore-readiness ready.
The canonical helper completed `deploy --release 35c58b6... --yes` with exit 0.
Post-deploy `status` reports `active_release` and `web_release`
`35c58b693bc885dc115d91df3c6e64680d0c79aa`, capture release unchanged
`5b86d896b3ea03f89fef2c90f7af2c121d0ef915`, `service_active: active`,
`database_revision: 0035` and `backup_restore_readiness: ready`.

Terminal `sudo -K` through the operator gate returned exit 0; a following
`sudo -n true` reports that a password is required, the expected released
lifecycle state. No host identifier, credential or secret is recorded.

The final rendered acceptance of the compact companion UI remains. The NUC
refresh alone does not reload the unpacked extension; the COOPERATOR must
reload it from the published `35c58b6` revision and refresh the source tabs.
Known residuals remain the YouTube acquisition `INSPECTION_OUTPUT_LIMIT` and
the full-page narrow My contributions LEAD; the companion-hosted rule fixes the
reported companion screenshot.

## Compact UI rendered acceptance PARTIAL — 2026-11-13

The COOPERATOR rendered `35c58b6` and returned: 1 PASS, 2 PASS, 3 PASS,
4 PARTIAL, 5 PASS, 6 PASS, 7 PASS, 8 PASS with a necessary separate whole for
the residual, 9 PARTIAL.

The remaining item 4 defect is the companion history list behavior:

- The compact sheet shows the five Recent downloads and then the review-history
  compact rows, including the unread review row that duplicates the latest
  download title. There must be no duplicate between downloads and review
  history.
- The COOPERATOR wants one **All** control immediately after the five downloads,
  not the inline review rows. After All, the sixth download must appear; the
  last retained download must be visible, not truncated at five.
- The latest download stays at the top; the review history remains accessible
  but must not duplicate a download media/title and must not precede the All in
  the compact view.

The compact companion UI itself (Timeline text, Filter disclosure, My
contributions) passed. The YouTube acquisition `INSPECTION_OUTPUT_LIMIT` remains
a separate logical whole. The full-page narrow My contributions LEAD remains
outside the companion.

The correction is `08_correction_00.md` for fresh Worker session 08/01 at
baseline `35c58b6`: retain the expanded download window, add the compact
five-plus-All layout, deduplicate review rows against downloads, keep the rest
of the review/badge behavior, tests and matching documentation. This is a
Cooperator-directed closeout of the same whole, not a new feature objective.
The whole remains open. No repository or host mutation occurred.

## History list correction PASS — 2026-11-13

Fresh correction `08_report_00.md` reports implementation-PASS at
`e9943b56b0bb97402fd64ac2143f1cf2fe07401f` (parent
`35c58b693bc885dc115d91df3c6e64680d0c79aa`) across exactly 11 paths. The
download projection now returns up to the retained fifty rows; the compact
sheet shows five downloads and one All; All reveals the sixth and later
retained downloads and then the review history; a review row whose media id
matches a download row is omitted; the review-only badge and existing click/
read/failure behavior remain. ADR-0091 supplements ADR-0090 and supersedes only
its at-most-five and single-window presentation.

Independent Orchestrator re-verification at `e9943b5`: focused Node 116 pass,
broader Node 64 pass, `ap project check` PASS, `git diff --check` clean, manifest
unchanged. The whole diff `e64f2b0..e9943b5` is 23 paths; the correction
`35c58b6..e9943b5` is 11. Public `main` remains `35c58b6`; local `main` is
ahead 1.

The report's delivery note says an empty `08_report_00.md` already existed and
the Worker did not overwrite it. The COOPERATOR persisted the complete report
content; the file is intact and the collision is a delivery-history fact, not a
content defect.

The next prompt is `09_acceptance_00.md` for fresh Worker session 09/01 with
`Acceptance independence: required-fresh-independent`; report
`09_report_00.md`. The YouTube acquisition residual and the full-page narrow My
contributions LEAD remain outside the companion. No publication, deployment or
closure is claimed.

## History expansion re-acceptance PASS — 2026-11-13

`09_report_00.md` records a genuinely fresh independent re-acceptance of
`e9943b56b0bb97402fd64ac2143f1cf2fe07401f` with all C01–C27 controls PASS,
defects none, and the declared counts: focused Python 46, focused Node 116,
broader Python 206, broader Node 64, compact UI Node 44, affected frontend
Node 287, served-shell Python 211. The report confirms the compact five plus
one All, the sixth and last retained download, deduplicated review history,
the review-only badge and the prior download/compact-UI/privacy controls.

```text
Phase-qualified result: acceptance-PASS
Result artifact or commit: e9943b56b0bb97402fd64ac2143f1cf2fe07401f
Result evidence: independent fresh re-acceptance 09_report_00.md; C01–C27 PASS;
  focused Python 46; focused Node 116; broader Python 206; broader Node 64;
  compact UI Node 44; affected frontend 287; served-shell Python 211;
  ap project check PASS; git diff --check clean; manifest unchanged
Required preceding results: implementation-PASS at e9943b5; acceptance-PASS
Cooperator-owned decisions: original choices and all amendments confirmed;
  publication, deployment and rendered acceptance remain open
Residual-risk disposition: open — rendered companion behavior and NUC phase;
  YouTube acquisition INSPECTION_OUTPUT_LIMIT and the full-page narrow My
  contributions LEAD remain outside this companion boundary
Upgrade-ledger reconciliation: complete for this phase — the one active
  accepted non-authorizing entry remains unchanged and retain-active
Active mutation: none
Closure actor: ORCHESTRATOR
Logical-whole closure: not-closed
```

Publication to public `main`, NUC deployment and the COOPERATOR's rendered
acceptance remain separate later grants. The whole remains open.

## History expansion publication and deployment PASS — 2026-11-13

The COOPERATOR authorized publication and the routine NUC deployment. The
candidate was pushed normally without force: `35c58b6..e9943b5` on `main`.
Direct `git ls-remote origin refs/heads/main` readback returned
`e9943b56b0bb97402fd64ac2143f1cf2fe07401f`; local `HEAD`, `origin/main` and the
public ref match; the worktree is clean.

`kronika-release check --release e9943b5...` PASS: public main `e9943b5`, AP
gitlink `d7023cf`, backup restore-readiness ready. The canonical helper
completed `deploy --release e9943b5... --yes` with exit 0. Post-deploy `status`
reports `active_release` and `web_release`
`e9943b56b0bb97402fd64ac2143f1cf2fe07401f`, capture release unchanged
`5b86d896b3ea03f89fef2c90f7af2c121d0ef915`, `service_active: active`,
`database_revision: 0035` and `backup_restore_readiness: ready`.

Terminal `sudo -K` through the operator gate returned exit 0; a following
`sudo -n true` reports that a password is required, the expected released
lifecycle state. No host identifier, credential or secret is recorded.

The final rendered acceptance of the compact five + All + deduplicated review
history remains. The NUC refresh alone does not reload the unpacked extension;
the COOPERATOR must reload it from the published `e9943b5` revision and refresh
the source tabs. The YouTube acquisition `INSPECTION_OUTPUT_LIMIT` and the
full-page narrow My contributions LEAD remain outside the companion.

## Final history rendered acceptance PARTIAL — 2026-11-14

The COOPERATOR rendered `e9943b5` and returned: 1 FAIL, 2 PASS, 3 the first
All collapses and the second makes no sense, 4 PASS, 5 PASS, 6 PASS, 7 PASS,
8 PASS as residual, 9 PARTIAL.

The remaining item 1 UI defects:

- Two All controls appear. The download All should be the only All when
  downloads exist; the review All should not appear behind it. The one All must
  reveal the later downloads and the complete review history, and collapse them
  again.
- A downloaded post that is still unread is not visually marked unread in the
  download row. The unread review row is deduplicated away, so the download row
  must carry the unread marker. Opening that download row must use the existing
  review opened mutation for the matching analyzed unread item so the marker
  and badge can clear.
- The «Save to Kronika failed» message and the failed X download rows are
  acquisition outcomes, not history-list defects. Some X saves succeeded and
  some failed. This is a separate acquisition residual/whole, like the YouTube
  `INSPECTION_OUTPUT_LIMIT`; the history UI correctly shows `Download failed`.

The correction is `10_correction_00.md` for fresh Worker session 10/01 at
baseline `e9943b5`: one All, unread marker and opened behavior on matched
download rows, tests and matching documentation plus ADR-0092. It is a
Cooperator-directed closeout of the same whole. The whole remains open; the X
and YouTube acquisition failures remain separate residuals. No repository or
host mutation occurred.

## Unread/one-All re-acceptance PASS — 2026-11-14

`11_report_00.md` records a genuinely fresh independent re-acceptance of
`2c4f4d89375628df28926060aba305e5d80bacff` with all C01–C27 controls PASS,
defects none, and the declared counts: focused Python 46, focused Node 118,
broader Python 206, broader Node 64, compact UI Node 44, affected frontend
Node 287, served-shell Python 211. The report confirms one download All, no
second review All while downloads exist, the complete review history behind
All, the unread marker and the existing opened mutation on matched analyzed
download rows, and all prior download/compact-UI/privacy controls.

```text
Phase-qualified result: acceptance-PASS
Result artifact or commit: 2c4f4d89375628df28926060aba305e5d80bacff
Result evidence: independent fresh re-acceptance 11_report_00.md; C01–C27 PASS;
  focused Python 46; focused Node 118; broader Python 206; broader Node 64;
  compact UI Node 44; affected frontend 287; served-shell Python 211;
  ap project check PASS; git diff --check clean; manifest unchanged
Required preceding results: implementation-PASS at 2c4f4d8; acceptance-PASS
Cooperator-owned decisions: all choices and amendments confirmed; publication,
  deployment and rendered acceptance remain open
Residual-risk disposition: open — rendered companion behavior and NUC phase;
  YouTube/X acquisition failures and the full-page narrow My contributions LEAD
  remain outside this companion boundary
Upgrade-ledger reconciliation: complete for this phase — the one active
  accepted non-authorizing entry remains unchanged and retain-active
Active mutation: none
Closure actor: ORCHESTRATOR
Logical-whole closure: not-closed
```

Publication to public `main`, NUC deployment and the COOPERATOR's rendered
acceptance remain separate later grants. The whole remains open.

## Unread/one-All publication and deployment PASS — 2026-11-14

The COOPERATOR authorized publication and the routine NUC deployment, and
refreshed the Cooperator sudo timestamp. The candidate was pushed normally
without force: `e9943b5..2c4f4d8` on `main`. Direct
`git ls-remote origin refs/heads/main` readback returned
`2c4f4d89375628df28926060aba305e5d80bacff`; local `HEAD`, `origin/main` and the
public ref match; the worktree is clean and no longer ahead.

`kronika-release check --release 2c4f4d8...` PASS: public main `2c4f4d8`, AP
gitlink `d7023cf`, backup restore-readiness ready, capture contract and bridge
protocol unchanged. The canonical helper completed
`deploy --release 2c4f4d8... --yes` with exit 0. Post-deploy `status` reports
`active_release` and `web_release` `2c4f4d89375628df28926060aba305e5d80bacff`,
capture release unchanged `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`,
`service_active: active`, `database_revision: 0035` and
`backup_restore_readiness: ready`.

Terminal `sudo -K` through the operator gate returned exit 0; a following
`sudo -n true` reports that a password is required, the expected released
lifecycle state. No host identifier, credential or secret is recorded.

The final rendered acceptance of one download All, the sixth/last retained
downloads, the complete review history, the deduplicated review rows, the
unread marker and the existing opened mutation remains. The NUC refresh alone
does not reload the unpacked extension; the COOPERATOR must reload it from the
published `2c4f4d8` revision and refresh the source tabs. The YouTube
acquisition `INSPECTION_OUTPUT_LIMIT`, the X acquisition failures/«Save to
Kronika failed» outcome and the full-page narrow My contributions LEAD remain
outside the companion.

## Final rendered PASS and closure — 2026-11-14

The COOPERATOR rendered the deployed `2c4f4d8` companion and declared **PASS**
on all six items: one download All with no review All while downloads exist; All
reveals the sixth/last retained downloads and the complete review history and
collapses again; the matched analyzed unread download row shows the unread
dot/accent and «Unread»; clicking it opens hosted Details and clears the marker
and badge; own-media rows stay clickable after read while no-media rows stay
inert; the badge remains review-only with no second counter.

Combined with the fresh independent acceptance-PASS at `11_report_00.md`
(C01–C27), the whole's rendered acceptance and production acceptance are
satisfied.

```text
Phase-qualified result: production-acceptance-PASS (Cooperator-declared)
Result artifact or commit: 2c4f4d89375628df28926060aba305e5d80bacff
Result evidence: Cooperator rendered PASS on all six final items at 2c4f4d8;
  fresh independent acceptance-PASS 11_report_00.md C01–C27; focused Python
  46; focused Node 118; broader Python 206; broader Node 64; compact UI Node
  44; affected frontend Node 287; served-shell Python 211; ap project check
  PASS; git diff --check clean; manifest unchanged; publication-PASS and NUC
  deployment-PASS at 2c4f4d8 with active/web 2c4f4d8, capture unchanged,
  service active, database revision 0035 and backup restore-readiness ready
Required preceding results: satisfied
Cooperator-owned decisions: satisfied — original four choices, download-row
  amendments, compact UI, five/All expansion, unread marker and one-All
  correction, publication and deployment authorization, and the final
  rendered PASS
Residual-risk disposition: satisfied for this whole — the YouTube acquisition
  INSPECTION_OUTPUT_LIMIT, the X acquisition failures/«Save to Kronika failed»
  outcome and the full-page narrow My contributions LEAD remain open,
  out-of-scope candidates, not defects of this companion whole
Upgrade-ledger reconciliation: complete — entry
  consumer-declared-execution-and-capability-route-binding remains accepted,
  non-authorizing, retain-active; no ledger mutation
Active mutation: none
Closure actor: ORCHESTRATOR
Logical-whole closure: closed-by-ORCHESTRATOR
```

These notes are frozen at closure. The run map entry remains for the run-scoped
Orchestrator to refresh from this whole's evidence. No repository, host or trace
mutation occurred after the recorded deployment.
