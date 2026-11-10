# Era 01 Whole Notes — Kronika application-shell UI/UX consistency

Classification: private local historical/evidentiary projection for this
logical whole. Orchestrator-owned, append-only during the whole, frozen at
closure. Public-safe by default. Michal owns any Meta Git commit.

Working identity:

```text
ui-ux-consistency
```

Trace:

```text
/Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/
```

Run map:

```text
/Users/agile/meta/projects/kronika/01/00_RUN_MAP.md
```

Opening date: 2026-11-10.

Opening Orchestrator: the run-scoped Orchestrator of Kronika run 01, continuing
as this whole's Orchestrator with `logical-whole` scope. The Cooperator selected
this final application-shell consistency pass before the deferred
`upload-flow-polish` whole.

Predecessor wholes:

- `projects/kronika/01/01-timeline-and-history-media-thumbnails` — closed
  2026-11-10 at `e6b26eb`; History Questions-only correction accepted and
  deployed.
- `projects/kronika/01/09-timeline-complete-chronicle` — closed 2026-11-10 at
  `65772c6`; complete Timeline chronicle and UI polish accepted and deployed.

## Restoration status — 2026-11-10

- Continuation Bootstrap Stage 1 is complete for this whole.
- The Cooperator's selection of the final UI/UX consistency pass is preserved.
- No Worker prompt has been delivered yet. The first Planner prompt is prepared
  and archived; the Cooperator delivers it manually.
- No Kronika repository, Git, NUC, deployment, browser, provider, account or
  filesystem mutation was performed by this opening. The only writes are this
  Meta notes record and the Planner prompt.
- The whole is not closed.

Verified anchors:

```text
Kronika local HEAD / public main:
  e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd
Kronika branch: main
Kronika working tree: clean
AP pin (superproject gitlink and .ap HEAD):
  d7023cf037f6d17885c3ede5c04812c61640da50
AP public main:
  d7023cf037f6d17885c3ede5c04812c61640da50
Governing AP variant: stable
./.ap/ap doctor: PASS
./.ap/ap project check --root /Users/agile/Projects/kronika \
  --baseline e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd: PASS
  (standard sanitized-environment warning for inherited SSH_AUTH_SOCK and PATH)
```

NUC state was last observed at the `e6b26eb` deployment: active/web
`e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd`, service active, database revision
`0035`, backup restore readiness `ready`, capture release unchanged. The
post-deploy terminal `sudo -K` revoked the Cooperator timestamp; a later
deployment needs a fresh `sudo -v`.

Upgrade ledger `docs/AP_UPGRADE_OBSERVATIONS.md` is declared outside the managed
block and structurally valid. Its single active entry
`consumer-declared-execution-and-capability-route-binding` remains `accepted`,
non-authorizing and `retain-active`; `Last revalidated against` `7ef45da` is an
ancestor of the current pin, and the ADR-0012/ADR-0018 disposition evidence is
present at `d7023cf`. No contradiction was found. The ledger was not mutated.

## Handout Revalidation Record

```text
Handout revalidation: /Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/00_handout.md
Received handout status: provisional
Revalidated against: Kronika e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd (local HEAD = public main, branch main, clean); AP d7023cf037f6d17885c3ede5c04812c61640da50 (Kronika .ap gitlink = .ap HEAD = AP public main; governing variant stable; ap doctor PASS; ap project check --baseline e6b26eb PASS); closed whole 01 notes and reports at e6b26eb; closed whole 09 notes and reports at 65772c6; run map /Users/agile/meta/projects/kronika/01/00_RUN_MAP.md; declared upgrade ledger docs/AP_UPGRADE_OBSERVATIONS.md
Usable facts: repository identity cisarik/kronika main, local checkout /Users/agile/Projects/kronika, HEAD and public main e6b26eb, clean tree; AP pin d7023cf, .ap gitlink/HEAD equality, public main matching, stable variant, ap doctor PASS, ap project check --baseline e6b26eb PASS with only the standard sanitized-environment warning; closed whole 01 and 09 state and their publication/deployment evidence; run map entry 01 closed, entry 02 handed-off and deferred, entry 09 closed; upgrade ledger entry accepted, non-authorizing, retain-active; Cooperator's requested UI/UX consistency changes and operating preferences; current Timeline/History/Gallery implementation and test surfaces as Planner reading targets; security, privacy, Gallery/Details freeze and internet-publication boundaries
Stale facts and corrections: none
Not revalidated: the Cooperator's rendered observations of the deployed UI are his observations, not independently re-measured here; NUC current state was last observed at the e6b26eb deployment before terminal sudo -K and was not recontacted during this opening; the exact current selectors, functions, classes, test pins and durable-document sentences are Planner work, not handout facts
Handout disposition: adopted
```

## Stage 2 — preserved selection and first Planner

The Cooperator selected the final application-shell UI/UX consistency pass as
the next whole. The objective is preserved: unify Timeline search with Gallery,
separate browsing tabs from the Search/Research/Review action group, remove
timeline/history link underlines, reorder and align Timeline filters with
Publication first and a green-border treatment, correct the public/private
visibility glyph, and finish the eye-candy, accessible responsive result without
changing API, authorization, privacy or data behavior.

First Planner exchange prepared:

```text
Logical whole identity: ui-ux-consistency
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Planning cycle: initial
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Delivery route: manual Cooperator delivery
Prompt: /Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/01_planning_00.md
Report: /Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/01_report_00.md
```

The Cooperator delivers the prompt manually into a fresh Planner session with
Native Plan Mode ON. The Worker writes the terminal report directly to the exact
Meta path and reads it back. The Orchestrator does not dispatch, does not use a
subagent, and does not commit Meta.

## Next step

Await the Cooperator's manual delivery of `01_planning_00.md`. When
`01_report_00.md` appears, read it back, reconcile it as a claim, and continue
with the next complete prompt. This record grants no authority.

## Reconciliation — first Planner blocked by prompt defect, 2026-11-10

`01_report_00.md` is present and was read back in full. It is a terminal
`PARTIAL` planning report, not a plan. The Worker stopped before producing any
decision-complete plan because the first prompt required `Native planning mode:
required` plus a direct report write but did not name a permitted client
completion route. The Worker cited AP `PROMPT_CONTRACTS.md` requirement P4 and
the prompt-satisfiability check. The finding is confirmed: the Orchestrator's
first whole-10 prompt repeated the known P4 omission.

The Worker did not bypass the client's Plan Mode write prohibition and did not
claim saved-file readback. The report's preliminary source observations remain
unverified context, not an accepted plan.

Coordinate and budget disposition:

- AP coordinates `01/01` are consumed by the blocked exchange.
- The initial planning cycle is **not** consumed because no plan existed.
- The corrected initial Planner keeps `Planning cycle: initial`, names
  `01_report_00.md` as `Prior planning report`, and does not use a targeted
  revision.
- The current Worker session `01` is healthy and did useful preliminary source
  mapping; independence is not required for planning. The corrected prompt uses
  `current-worker-session`, session `01`, exchange `02`, with a continuity
  anchor, complete authority renewal, repository/environment re-gating, and
  retained context classified as convenience rather than authority.
- Meta files are `01_planning_01.md` and `01_report_01.md`.
- The corrected prompt names the actual client completion route (P4): the
  Planner keeps the complete terminal report in the client's Plan output; if the
  client permits a write within the same unexpired grant, it writes and reads
  back `01_report_01.md`; if the client prohibits the write, it returns the
  complete exact content in the session, does not claim saved-file readback, and
  the Cooperator or an authorized persister stores it under the AP
  Planner-Artifact Report Completion Repair route. The client's Plan Mode
  control is not bypassed.

No Kronika repository, Git, NUC, deployment, browser, provider, account or
filesystem mutation was performed. The only writes are Meta records. The next
step is one corrected initial Planner prompt, archived as `01_planning_01.md`;
its report destination is `01_report_01.md`; the Cooperator delivers it
manually to the same session `01`.

## Plan reconciliation and implementation grant — 2026-11-10

`01_report_01.md` is present and was read back in full. It is a complete
technical plan. Its `PARTIAL` status records the client's Plan Mode write
prohibition, not an incomplete plan; the Cooperator persisted the exact content,
so the required file-delivery gap is closed. The plan's own `Report persistence:
client-prohibited; complete exact content returned for authorized persistence`
is preserved as history.

Plan disposition: **accepted**. The plan's explicit defaults are accepted:
body-level navigation with browsing/action groups, native action links with
square styling, shared Gallery search presentation with Timeline-local query
semantics, Publication-first filter order, wide alignment at 1100 px, the
listbox Tab/Enter focus correction selected by the Cooperator, explicit
underline removal, the eye legacy-publication glyph, the ten-path allowlist and
the E2 acceptance route. No targeted revision is required.

The implementation prompt `02_implementation_00.md` was prepared for fresh
Worker session `02`, exchange `01`, profile Fresh Implementation Worker,
`Native planning mode: not-used`, exact baseline `e6b26eb`, the ten-path
allowlist, one normal local commit, no push, no NUC/browser/provider, and
direct-write report `02_report_00.md`. The Cooperator delivers it manually.
After the implementation report, the Orchestrator verifies the candidate and
prepares the fresh E2 acceptance in session `03`. No repository, Git, NUC,
browser, provider or host mutation was performed by this reconciliation.

## Implementation reconciliation — 2026-11-10

`02_report_00.md` is present and was read back in full. It is a terminal
`implementation-PASS` report at commit
`bbf776c462e1eb5eccb91eb027a85eee9055d2ec`, parent
`e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd`, on local `main` with no push. The
candidate changes exactly the ten allowlisted paths (690 insertions, 111
deletions) and leaves the worktree clean.

The Orchestrator inspected the diff: navigation is grouped into body-level
browsing/action groups; Timeline uses the shared Gallery search presentation
with its own explicit submit/clear semantics; Publication is first; the listbox
focus correction and presentation roles are present; title underlines are
removed; the legacy glyph is the eye; the SPEC/README/GALLERY/DEVELOPMENT
sentences are updated. No API, authorization, payload, schema, route-policy or
Gallery/Details change was introduced.

The Orchestrator independently re-ran the exact selected evidence:
`ap project check --baseline e6b26eb` PASS, the full local-web suite **208
passed**, and the Node suite **85 passed**. The implementation report's counts
match.

Implementation reconciliation disposition: **accepted for fresh E2
acceptance**, not final acceptance. Prompt `03_acceptance_00.md` was prepared
for fresh Worker session `03`, exchange `01`, profile Fresh Independent Audit,
against fixed candidate `bbf776c`, with the ten-path allowlist, the A-I matrix
and the exact selected tests. Report destination `03_report_00.md`; the
Cooperator delivers it manually. No repository, Git, NUC, browser, provider or
host mutation was performed by this reconciliation.

## Acceptance reconciliation, publication and deployment — 2026-11-10

`03_report_00.md` is present and was read back in full. It is a terminal
**acceptance-PASS** report for candidate
`bbf776c462e1eb5eccb91eb027a85eee9055d2ec`, with all A-I claims PASS. The
auditor independently re-ran the selected gates: 208 local-web tests and 85 Node
tests passed; the ten-path diff and negative allowlist were verified; no
authorization, API, payload, schema or Gallery/Details change was found.

- **Publication PASS.** The accepted candidate was pushed normally:
  `e6b26eb..bbf776c` on `main`, no force. Direct `git ls-remote` readback
  returned `bbf776c462e1eb5eccb91eb027a85eee9055d2ec`; local HEAD and
  `origin/main` match; tree clean.
- **Deployment PASS.** The canonical helper sequence was used with explicit
  transport arguments: `status` -> `check --release bbf776c...` -> `deploy
  --release bbf776c... --yes`. The deploy completed with exit 0. Post-deploy
  `status` reports `layout: canonical`, `active_release` and `web_release`
  `bbf776c462e1eb5eccb91eb027a85eee9055d2ec`, `capture_release`
  `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`, `service_active: active`,
  `database_revision: 0035` and `backup_restore_readiness: ready`. Bounded
  read-only checks confirmed the deployed shell contains the grouped nav, the
  Timeline search and the eye glyph.
- **Terminal privilege release.** `sudo -K` was run through the canonical gate;
  a following `sudo -n true` requires a password. A later deployment needs a
  fresh Cooperator `sudo -v`.
- **Whole 10 state.** Acceptance-PASS, publication-PASS and deployment-PASS at
  `bbf776c`. The Cooperator's rendered acceptance of the new shell remains the
  only pending closure input. Whole 02 remains deferred until then.

## Rendered acceptance findings and correction grant — 2026-11-10

The Cooperator tested the deployed `bbf776c` shell and declared **PASS** for the
implemented navigation grouping, Timeline/Gallery search presentation, filter
order/alignment, listbox Tab/Enter correction, underline removal and eye glyph.
He then requested three further consistency changes:

1. **Timeline search belongs in the header toolbar**, in the same slot/position
   as Gallery search, so switching Timeline ↔ Gallery does not move the search
   field. The filter bar should contain only Publication/Kind/Status/Visibility.
2. **Remove the visible Timeline hero, lede and note.** Gallery has no
   equivalent; trim the Timeline page and keep only a hidden heading if needed
   for focus/accessibility.
3. **Remove History entirely.** The Timeline already contains the personal
   search/research history; remove the History tab and page. The browsing group
   becomes Timeline and Gallery only. `#/history` and `#/history/records` resolve
   to the Timeline. Search/Research/Review actions remain.

This explicitly supersedes the accepted plan's decision to preserve personal
History as a separate view. It does not remove the question/answer data model or
API. The durable owners must record the decision, including a new ADR that
supersedes the removed-view parts of ADR-0083/ADR-0087; accepted ADR bodies stay
unedited.

Bounded correction prompt `02_correction_01.md` was issued to the same healthy
Worker session `02`, exchange `02`, baseline `bbf776c`, with a UI/docs/ADR
allowlist, one local commit and report `02_report_01.md`. A fresh independent E2
re-acceptance follows the correction because it changes runtime UI and the
product view model. Whole 10 remains active; the `bbf776c` publication and
deployment remain the functional baseline, not the final release.

## Correction reconciliation and micro-correction — 2026-11-10

`02_report_01.md` is present and was read back in full. It is a terminal
**implementation-PASS** report for local candidate
`27aa5fd29f259ee27de109f37bb7cf88f255b93f`, parent
`bbf776c462e1eb5eccb91eb027a85eee9055d2ec`, changing exactly 14 allowlisted
paths (243 insertions, 521 deletions). Public `main` remains `bbf776c`; the
candidate is local and unpushed. The worktree is clean.

The Orchestrator independently re-ran the exact selected evidence:
`ap project check --baseline bbf776c` PASS, the full local-web suite **208
passed**, and the Node suite **84 passed**. The report counts match. Diff review
confirmed the header search slot, the trimmed Timeline page, the History removal
and Timeline fold, the Publication-first filter bar, ADR-0088 and the owner-doc
updates. No API, authorization, payload, schema, route-policy or stored-data
change was introduced; accepted ADR-0082 through ADR-0087 bodies are unedited.
`SECURITY.md` and `SERVER.md` were left unchanged because their surviving
"history" references are API-payload, retention or dated operational history,
not the removed UI view.

One consistency gap was found in `kronikaMarkCurrent`: deleting the History
branch also removed current marking from `#/requests/...` and `#/records/...`,
although those pages remain reachable from Timeline rows and still render the
navigation; Details still marks Gallery. The Timeline is the single overview
under ADR-0088, so request and record details must keep Timeline current.
Bounded prompt `02_correction_02.md` was issued to the same Worker session `02`,
exchange `03`, baseline `27aa5fd`, allowlisting only
`src/kronika/adapters/api/web/app.js` and `tests/kronika_ui.test.js`, with one
local commit and report `02_report_02.md`. No repository, Git, NUC, browser,
provider or host mutation was performed by this reconciliation.

## Final candidate and E2 acceptance preparation — 2026-11-10

`02_report_02.md` is present and was read back in full. It is a terminal
**implementation-PASS** report for local candidate
`8646146b7dfd50a9a99ec94dbd696102cbe5ca4e`, parent
`27aa5fd29f259ee27de109f37bb7cf88f255b93f`, changing only
`src/kronika/adapters/api/web/app.js` and `tests/kronika_ui.test.js` (39
insertions, 2 deletions). `kronikaMarkCurrent` maps `request` and `record` to
`timeline`; a regression test asserts request/record keep Timeline current,
Details keeps Gallery current and the review subroutes keep Review current. No
History link, route, section or `aria-current` value is restored.

The Orchestrator independently re-ran the exact selected evidence at both the
immediate parent `27aa5fd` and the published baseline `bbf776c`: project check
PASS, **208** local-web tests passed, and the Node suite **85 passed**. The
worktree is clean and public `main` remains `bbf776c`; the candidate is local and
unpushed. The whole-change set `bbf776c..8646146` is exactly the fourteen
allowlisted paths (278 insertions, 519 deletions); the final micro-correction
`27aa5fd..8646146` is exactly the two paths above.

Fresh E2 acceptance prompt `04_acceptance_00.md` was prepared for Worker session
`04`, exchange `01`, profile Fresh Independent Audit, against fixed candidate
`8646146`, with the fourteen-path allowlist, the two-path correction check, the
A-I matrix, the exact gate and Node/local-web tests, and report destination
`04_report_00.md`. The Cooperator delivers it manually. No repository, Git,
NUC, browser, provider or host mutation was performed by this preparation.

## Final acceptance — 2026-11-10

`04_report_00.md` is present and was read back in full. It is a terminal
**acceptance-PASS** report for candidate
`8646146b7dfd50a9a99ec94dbd696102cbe5ca4e`, start
`bbf776c462e1eb5eccb91eb027a85eee9055d2ec`, with all A-I claims PASS. The
auditor independently re-ran the exact gate and tests: 208 local-web tests and
85 Node tests passed, the worktree remained clean, HEAD stayed at the
candidate, and the whole diff was exactly the fourteen measured paths (278
insertions, 519 deletions) with the two-path micro-correction (39 insertions, 2
deletions). No API, authorization, payload, schema, stored-data or
Gallery/Details change was found. Rendered alignment, contrast, 320/390 px
geometry, layout-jump absence, popup visibility, touch and assistive-technology
output remain the Cooperator's rendered acceptance.

The auditor recorded one prompt-text near-miss: `04_acceptance_00.md` section 2
said "fourteen" but enumerated fifteen paths, including
`tests/gallery_search_tag_filters.test.js`, which is unchanged from `bbf776c`
but remains a required regression test. The measured diff and the enumerated
set minus that unchanged path agree; the auditor confirmed the surplus path has
an empty diff and empty log and continued. The issued prompt is historical and
is not retroactively edited; future changed-path enumerations must list only
modified paths and keep this test in the test command.

Final acceptance disposition: **accepted**. The candidate is ready for
publication, NUC deployment and the Cooperator's rendered acceptance.

## Publication and deployment — 2026-11-10

- **Publication PASS.** The accepted candidate was pushed normally:
  `bbf776c..8646146` on `main`, no force. Direct `git ls-remote` readback
  returned `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e`; local HEAD and
  `origin/main` match; the worktree is clean.
- **Deployment PASS.** The canonical helper sequence was used with explicit
  transport arguments: `status` -> `check --release 8646146...` -> `deploy
  --release 8646146... --yes`. The deploy completed with exit 0. Post-deploy
  `status` reports `layout: canonical`, `active_release` and `web_release`
  `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e`, `capture_release`
  `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`, `service_active: active`,
  `database_revision: 0035` and `backup_restore_readiness: ready`. Bounded
  read-only checks confirmed the deployed shell contains the header Timeline
  search, one browsing group and no History markup.
- **Terminal privilege release.** `sudo -K` was run through the canonical gate;
  a following `sudo -n true` requires a password. A later deployment needs a
  fresh Cooperator authorization.
- **Whole 10 state.** Acceptance-PASS, publication-PASS and deployment-PASS at
  `8646146`. The Cooperator's rendered acceptance of the final shell remains the
  only pending closure input. Whole 02 remains deferred until then.

## Rendered acceptance and closure — 2026-11-10

The COOPERATOR tested the deployed `8646146` shell and declared the final
rendered result **PASS**: the header Timeline search, the trimmed Timeline, the
History-free browsing group and address fold, request/record current marking,
Publication-first filters, listbox keyboard activation, title-link underlines,
the legacy eye glyph, Gallery search and the narrow layout. He authorized
closure of whole 10.

```text
Phase-qualified result: production-acceptance-PASS (Cooperator-declared)
Result artifact or commit: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
Result evidence: Cooperator rendered PASS for the final shell at 8646146;
  final E2 acceptance-PASS with all A-I claims; publication-PASS; NUC
  deployment-PASS with active/web 8646146, service active, database revision
  0035 and backup restore-readiness ready
Required preceding results: satisfied
Cooperator-owned decisions: satisfied — final rendered acceptance and closure
  declared; the header-search slot, Timeline trim, History removal, current
  marking and prior grouping/filter/listbox/link/glyph work are accepted
Residual-risk disposition: satisfied — no medium or higher residual; the
  acceptance prompt's fifteen-name enumeration against the measured fourteen
  paths is a historical prompt-text defect, not a candidate scope escape;
  rendered geometry, contrast, touch and assistive-technology output are covered
  by the Cooperator's PASS
Upgrade-ledger reconciliation: complete — entry
  consumer-declared-execution-and-capability-route-binding remains accepted,
  non-authorizing, retain-active; no ledger mutation
Active mutation: none
Closure actor: ORCHESTRATOR
Logical-whole closure: closed-by-ORCHESTRATOR
```

The prompt-text near-miss is retained as an orchestration lesson: changed-path
enumerations must list only modified paths, while regression test files that are
unchanged remain in the test command. The issued prompt and terminal report are
historical evidence and are not retroactively edited.

These notes are frozen at closure. The deferred `upload-flow-polish` whole now
opens as a separate record.
