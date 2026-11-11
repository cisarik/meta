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
