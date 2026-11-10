# Kronika run 01 — Run Map

```text
Run map author: Master Orchestrator, AP run 10
Mechanical persister: Fresh Implementation Worker session 07
Created: 2026-11-08
Observed against: AP d7023cf; Kronika 246c9f8; .ap d7023cf
```

The run is open. This run map is discovery and decision support only. It is not a roadmap,
selection, plan, grant or second semantic owner. Kronika's `ROADMAP.md`,
accepted ADRs and the COOPERATOR's decisions keep their owners. The COOPERATOR
may reorder, add or drop entries at any time; the order below is a
recommendation, never a selection. AP owns the meaning
(`.ap/AP.md#run-level-handouts`) and the record spelling
(`.ap/PROMPT_CONTRACTS.md#run-map-record`); the Meta `README.md` section Run
Maps and Provisional Handouts owns only this file's location.

```text
Run map: kronika-run-01
Run objective: after the closed UX refresh, deliver the bounded household-product improvements proposed in the closed 00 handout §9.2, one Cooperator-selected logical whole at a time; exclusions: Gallery/Details visual redesign (frozen), internet publication, new provider or acquisition pipelines, identity or authorization model changes, deployment beyond the routine release helper, and the parked roadmap rows
Run map authority: discovery-only
Run entry: 00 | ux-refresh-acceptance-and-promotion | closed | depends on: none | handout: /Users/agile/meta/projects/kronika/01/00-ux-refresh-acceptance-and-promotion/00_handout.md | evidence: Closed-by-ORCHESTRATOR on 2026-11-08 with Cooperator-declared production acceptance at 7ee4684 after E3 acceptance-PASS at cb5fa4d, per the closure record in that whole's 00_notes.md.
Run entry: 01 | timeline-and-history-media-thumbnails | closed | depends on: ux-refresh-acceptance-and-promotion | handout: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/00_handout.md | evidence: Closed-by-ORCHESTRATOR on 2026-11-10 with Cooperator-declared production acceptance for the History Questions-only correction at e6b26eb; E2, publication and deployment PASS; original Timeline-membership scope superseded by closed entry 09; notes frozen.
Run entry: 02 | upload-flow-polish | active | depends on: timeline-and-history-media-thumbnails | handout: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/00_handout.md | evidence: Selected by the COOPERATOR on 2026-11-09 and opened by the run-scoped Orchestrator on 2026-11-10 after entries 01, 09 and 10 closed; handout revalidated against Kronika 8646146 and AP d7023cf, with stale predecessor/NUC/History facts corrected in 00_notes.md; first Planner report 01_report_00.md received and reconciled; Cooperator approved the decision-complete plan with per-dialog default-off auto-start, companion progress in the existing hosted dialog, a nine-path UI/test/docs allowlist and no API/auth/schema/protocol change; implementation prompt 02_implementation_00.md prepared for fresh session 02/01; its delivered report 02_report_00.md is a byte-identical copy of the planning report, with no implementation commit at 8646146, so the session is rejected as a delivery mismatch and preserved; corrected implementation prompt 03_implementation_00.md prepared for fresh session 03/01 with report 03_report_00.md; implementation, acceptance, publication, deployment and rendered acceptance pending.
Run entry: 03 | companion-download-notifications | provisional | depends on: upload-flow-polish | handout: /Users/agile/meta/projects/kronika/01/03-companion-download-notifications/00_handout.md | evidence: Proposed in the closed 00 handout §9.2 to surface completed X/YouTube downloads in the companion side-panel history and toolbar badge, reusing the existing own-history and request-detail read paths.
Run entry: 04 | household-onboarding | provisional | depends on: companion-download-notifications | handout: /Users/agile/meta/projects/kronika/01/04-household-onboarding/00_handout.md | evidence: Proposed in the closed 00 handout §9.2 as a first-run explainer of roles, privacy and sharing for ordinary members plus a plain-language install guide, without changing the identity or authorization model.
Run entry: 05 | humanized-error-copy | provisional | depends on: household-onboarding | handout: /Users/agile/meta/projects/kronika/01/05-humanized-error-copy/00_handout.md | evidence: Proposed in the closed 00 handout §9.2 to replace raw user-facing codes such as http_403 with actionable text after an inventory, keeping machine codes for diagnostics.
Run entry: 06 | accessibility-pass | provisional | depends on: humanized-error-copy | handout: /Users/agile/meta/projects/kronika/01/06-accessibility-pass/00_handout.md | evidence: Proposed in the closed 00 handout §9.2 for keyboard paths, focus, screen-reader names and glass-button contrast, with the Cooperator's rendered review as acceptance and the Gallery/Details freeze respected.
Run entry: 07 | app-js-modularization-planning | provisional | depends on: accessibility-pass | handout: /Users/agile/meta/projects/kronika/01/07-app-js-modularization-planning/00_handout.md | evidence: Proposed in the closed 00 handout §9.2 as planning only for the app.js monolith (predecessor residual R9), requiring an asset-allowlist decision and a vm-harness test strategy before any implementation.
Run entry: 08 | product-language-decision | provisional | depends on: app-js-modularization-planning | handout: /Users/agile/meta/projects/kronika/01/08-product-language-decision/00_handout.md | evidence: Proposed in the closed 00 handout §9.2 as a Cooperator product decision on UI language (the UI is English and the Cooperator communicates in Slovak), discovery and decision only.
Run entry: 09 | timeline-complete-chronicle | closed | depends on: timeline-and-history-media-thumbnails | handout: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/00_handout.md | evidence: Closed-by-ORCHESTRATOR on 2026-11-10 with Cooperator-declared production acceptance at 65772c6 after E3 acceptance-PASS, publication-PASS and NUC deployment-PASS; custom Timeline dropdowns and filtering rendered PASS; two non-blocking ADR/Tab findings carried to a future documentation/accessibility task.
Run entry: 10 | ui-ux-consistency | closed | depends on: timeline-complete-chronicle | handout: /Users/agile/meta/projects/kronika/01/10-ui-ux-consistency/00_handout.md | evidence: Closed-by-ORCHESTRATOR on 2026-11-10 with Cooperator-declared production acceptance at 8646146 after final E2 acceptance-PASS, publication-PASS and NUC deployment-PASS; header-search consistency, Timeline trim, complete History removal with ADR-0088, request/record current marking and the prior grouping/filter/listbox/link/glyph work rendered PASS; prompt-list surplus recorded as a non-blocking orchestration near-miss; notes frozen.
```

## Notes on the record

**Run objective provenance.** This refresh derived the objective and
exclusions from the closed 00 handout §9.2, which lists the eight candidates as
"proposals, not adopted direction", and from the eight provisional handouts'
scope and out-of-scope lists. The parked roadmap rows are the S3 host
remainder, capture-mode Search and Research, S5 ZIP activation and S7-C capture
integration (`AGENTS.md`). The evidence available to this refresh records no
Cooperator-selected run objective. The COOPERATOR confirms, narrows or replaces
it before the run map informs a recommendation.

**Dependencies.** Entry 01 builds on the closed 00 whole's accepted preview
backfill. Entry 02 depends on 01 through the recorded UI-context risk U6.
Entries 03–08 preserve each handout's stated predecessor-wait rule (the
predecessor closes before the whole opens); that rule records the prepared
order, not a measured product dependency. The COOPERATOR selects the final
order. A reorder refreshes the affected unopened handouts' predecessor lines or
replaces them with successor handouts.

**Status vocabulary.** A run entry's status is one of `provisional`,
`handed-off`, `active`, `closed`, `superseded` or `dropped`
(`.ap/PROMPT_CONTRACTS.md#run-map-record`). Only the run-scoped Orchestrator
changes a status, from the whole's own selection, revalidation and closure
evidence; closure remains that whole's Orchestrator decision.

**Handouts.** Entries 01–08 point to provisional handouts refreshed on
2026-11-08 against AP `d7023cf`, Kronika `246c9f8` and `.ap` `d7023cf`. Each is
a seed, not authority; its receiving Orchestrator records a Handout
Revalidation Record in that whole's `00_notes.md` before the first Planner
prompt. Entry 00's handout is frozen historical evidence.

**Relationship to AP run 10.** These entries are Kronika wholes. They are not
wholes of AP run 10, whose only whole is
`master-orchestrator-and-report-persistence`.

## Run log

- **2026-11-09 — entry 01 selected and opened.** The COOPERATOR selected
  `timeline-and-history-media-thumbnails`. The run-scoped Orchestrator opened the
  whole itself under `AP_ORCHESTRATOR.md` Run-Scoped Orchestration step 5
  because the selection arrived in the same session that completed the whole's
  Continuation Bootstrap Stage 1; the departure and reason are recorded in the
  whole's `00_notes.md`. Entry 01 status changed from `provisional` to `active`.
  The first Planner prompt is `01_planning_00.md`; the report destination is
  `01_report_00.md`. No Kronika repository, Git, NUC or host mutation occurred.
- **2026-11-09 — implementation accepted at E2.** The corrected implementation
  candidate `b66ec8f50860ace624f6be1fd3ad63f521edcd33` passed the focused
  Python, local-web and Node suites and is accepted at E2. The candidate is
  local only, two commits ahead of public `main` `246c9f8`; publication, NUC
  refresh and the Cooperator's rendered acceptance remain pending. The
  Cooperator granted NUC SSH access and an active `sudo -v` timestamp for the
  later bounded deployment exchange.
- **2026-11-09 — publication and deployment PASS.** The accepted candidate was
  pushed normally to public `main` (`246c9f8..b66ec8f`, no force) and direct
  `ls-remote` readback matched. The canonical NUC helper completed a same-schema
  `deploy --release b66ec8f --yes` with exit 0; post-deploy status reports
  active/web release `b66ec8f`, `service_active: active`, database revision
  `0035` and backup restore-readiness `ready`. The capture release is unchanged.
  Terminal `sudo -K` was run through the operator gate; a later deployment needs
  a fresh Cooperator `sudo -v`. The Cooperator's rendered acceptance remains
  pending; formal 01 closure is therefore pending, not fabricated.
- **2026-11-09 — entry 02 selected and handed off.** The COOPERATOR selected
  `upload-flow-polish` and directed the next fresh Orchestrator to proceed while
  01's rendered acceptance remains a carried Cooperator-owned item. The 02
  handout was refreshed in place before opening with the current repository,
  AP, NUC, predecessor, run-map and operating-preference state. Entry 02 status
  is `handed-off`; the next Orchestrator opens it after its own Stage 1.
- **2026-11-09 — route A selected; entry 09 added.** The Cooperator's first
  rendered-review step found that the approved-only Timeline did not match the
  intended complete chronicle. He chose route A: a new logical whole
  `timeline-complete-chronicle` (entry 09) that supersedes ADR-0083's
  approved-only Timeline membership with a complete, visibility-aware
  chronological table/list including private, unanalysed and unpublished items
  the signed-in identity may see. Whole 01's thumbnail implementation,
  publication and deployment remain groundwork; its rendered acceptance and
  formal closure are paused, not PASS. Entry 09 is `handed-off` and selected
  next; entry 02 is deferred until after entry 09 unless the Cooperator
  reorders.
- **2026-11-10 — entry 09 opened; implementation candidate ready.** The fresh
  whole Orchestrator completed Stage 1, accepted ADR-0087, and drove the
  preflight and implementation. Candidate `264a040` (parent `b66ec8f`) changes
  exactly 29 allowlisted paths and is local only. The Orchestrator reconciled
  the implementation report and independently re-ran the selected suites:
  258 Python, 43 local-web, 3 tailscale and 48 Node tests passed; the gate
  passed. Independent E3 acceptance prompt `03_acceptance_00.md` is prepared
  for fresh Worker session 03; report `03_report_00.md` is pending. Entry 09
  status is `active`; publication, NUC deployment and rendered acceptance
  remain pending.
- **2026-11-10 — entry 09 independent acceptance PASS.** Fresh auditor session
  03 returned acceptance-PASS at fixed candidate `264a040`; all C01-C24 rows
  passed and the selected suites again produced 258 Python, 43 local-web, 3
  tailscale and 48 Node passing tests. Two non-blocking UI gaps are carried:
  a same-query refresh hides the Retry control, and chronicle rows omit the
  planned column header/per-field labels. Publication, NUC deployment and the
  Cooperator's rendered acceptance remain pending.
- **2026-11-10 — bounded UI correction granted; deployment delegated.** The
  COOPERATOR required both UI gaps to be fixed before publication, confirmed a
  fresh NUC `sudo -v`, and authorized the Orchestrator to perform the later
  deployment. Correction prompt `02_correction_02.md` is prepared for Worker
  session 02, exchange 03, limited to five UI paths. A fresh independent
  re-acceptance follows, then publication and deployment. Whole 01's paused
  rendered acceptance and whole 09's rendered acceptance remain separate
  Cooperator checks.
- **2026-11-10 — UI correction PASS; full-fresh re-acceptance ready.** The
  bounded correction at `1bc10a3` (parent `264a040`) changed exactly four UI
  paths and added the stale Retry control plus the chronicle header/labels.
  The Orchestrator re-ran the gate and selected Node/local-web tests: 51 Node
  and 43 local-web passed. Because runtime UI behavior changed, prompt
  `04_acceptance_00.md` is prepared for a fresh independent full-fresh
  re-acceptance in session 04. Publication, NUC deployment and rendered
  acceptance remain pending.
- **2026-11-10 — full-fresh re-acceptance PASS; one doc correction.** Fresh
  session 04 returned acceptance-PASS at `1bc10a3`; all C01-C24 and both C22
  UI claims passed, with 258 Python, 43 local-web, 3 tailscale and 51 Node tests
  passing. One stale `SERVER.md` sentence still equates shared Timeline entry
  with approval; bounded documentation correction prompt `02_correction_03.md`
  is prepared for session 02/04. After its report, the Orchestrator will verify
  the one-sentence diff, publish `main` and deploy the exact release to the NUC
  under the Cooperator's delegation; rendered acceptance for 09 and the paused
  01 check remain with the Cooperator.
- **2026-11-10 — publication and deployment PASS at 5be63b1.** The one-sentence
  `SERVER.md` documentation correction was verified and the final candidate was
  published normally (`b66ec8f..5be63b1`), with direct public-main readback.
  The canonical NUC deploy completed at `5be63b1`; post-deploy status reports
  active/web release `5be63b1`, service active, database revision `0035` and
  backup restore-readiness ready. Terminal `sudo -K` was run and the timestamp
  is revoked. Whole 09's rendered acceptance remains pending; whole 01's paused
  check can now be finished against the same deployed release.
- **2026-11-10 — rendered UX finding; Timeline polish correction.** The
  Cooperator tested the deployed `5be63b1` and accepted the functional/privacy
  model but rejected the visual result: native dropdowns, visible `Added` date,
  text-heavy status/visibility, cramped header and insufficient eye candy. A
  bounded UI polish correction `02_correction_04.md` is prepared for session
  02/05: custom Matrix-style filter dropdowns, removed Added column, emoji
  status/visibility with accessible text, clearer header spacing and a subtle
  green hover animation. A fresh full re-acceptance, publication, deployment and
  rendered acceptance follow. Whole 09 remains active; `5be63b1` is the
  functional baseline, not the final visual candidate.
- **2026-11-10 — Timeline polish PASS; full-fresh re-acceptance ready.** The
  bounded UI polish at `65772c6` (parent `5be63b1`) changed exactly four UI
  paths: custom keyboard listbox filters, removed Added column/date, glyph
  status/visibility with accessible text, clearer header spacing and a subtle
  reduced-motion-aware green hover. The Orchestrator re-ran the gate at
  `5be63b1`, the Node suite: 53 passed, and the selected local-web suite: 43
  passed. Prompt `05_acceptance_00.md` is prepared for a fresh independent
  full-fresh re-acceptance in session 05. Publication, deployment and rendered
  acceptance remain pending.
- **2026-11-10 — polished Timeline accepted and published; deploy waits for sudo.**
  Fresh session 05 returned acceptance-PASS at `65772c6`; all C01-C24 and the
  C22 presentation claims passed, with 258 Python, 43 local-web, 3 tailscale and
  53 Node tests. The polished candidate was published normally
  (`5be63b1..65772c6`) with direct public-main readback. The NUC is still at
  `5be63b1`; the previous `sudo -K` revoked the timestamp, so deployment waits
  for a fresh Cooperator `sudo -v`. Two non-blocking findings are carried: a
  stale ADR-0087 presentation sentence and a Tab/Enter listbox index near-miss.
- **2026-11-10 — polished Timeline deployed PASS at 65772c6.** The Cooperator
  refreshed the NUC sudo timestamp and the canonical helper deployed the
  accepted polished release. Post-deploy status reports active/web release
  `65772c6`, service active, database revision `0035` and backup restore-
  readiness ready; capture release unchanged. Terminal `sudo -K` was run and
  the timestamp is revoked. Whole 09 now has acceptance, publication and
  deployment PASS; only the Cooperator's rendered acceptance remains. Whole 01's
  paused check can use the same release.
- **2026-11-10 — entry 09 closed.** The Cooperator declared the deployed
  polished Timeline's custom dropdowns and filtering as rendered acceptance and
  authorized closure. The whole's notes record
  `production-acceptance-PASS (Cooperator-declared)` at `65772c6`, with
  `Logical-whole closure: closed-by-ORCHESTRATOR`; the notes are frozen. The two
  non-blocking ADR-0087 and Tab/Enter findings are carried to a future
  documentation/accessibility task. Entry 09 is `closed`; whole 01's paused
  rendered check and the deferred whole 02 remain separate.
- **2026-11-10 — History UX finding; Questions-only correction.** The
  Cooperator tested History on the deployed `65772c6`: the Questions and
  Records tabs showed effectively the same items and the cards were inconsistent
  with the new Timeline list. He directed History to keep only Questions and to
  use the Timeline chronicle list visual language, with question text space and
  no Added date. Bounded whole-01 UI correction `02_correction_02.md` is
  prepared for session 02/03. After its report: Orchestrator verification,
  publication, NUC deployment and Cooperator rendered acceptance. Entry 01
  remains active; entry 09 is closed.
- **2026-11-10 — History Questions-only correction accepted and published.**
  Whole 01's correction at `e6b26eb` (parent `65772c6`) removed the duplicate
  Records tab/view, folded `#/history/records` to `#/history`, and rendered
  personal questions as a Timeline-style chronicle list with glyph status and
  visibility, no Added date, and the same hover/reduced-motion treatment. The
  Orchestrator verified the five-path diff and re-ran the gate at `65772c6`,
  the Node suite: 55 passed, and the selected local-web suite: 43 passed.
  E2 acceptance of the correction PASS; publication PASS
  (`65772c6..e6b26eb`). NUC deployment waits for a fresh Cooperator `sudo -v`;
  History rendered acceptance remains pending. Entry 01 stays active.
- **2026-11-10 — History correction deployed PASS at e6b26eb.** The Cooperator
  refreshed the NUC sudo timestamp and the canonical helper deployed
  `e6b26eb`. Post-deploy status reports active/web `e6b26eb`, service active,
  database revision `0035` and backup restore-readiness ready; the deployed
  shell has the History chronicle header and no old Records tab. Terminal
  `sudo -K` was run and the timestamp is revoked. Whole 01 now has E2,
  publication and deployment PASS for the History correction; only the
  Cooperator's History rendered acceptance remains before closure.
- **2026-11-10 — entry 01 closed.** The Cooperator declared the deployed History
  Questions-only correction PASS and authorized closure. The whole's notes
  record `production-acceptance-PASS (Cooperator-declared)` at `e6b26eb` with
  `Logical-whole closure: closed-by-ORCHESTRATOR`; the notes are frozen. The
  original Timeline-membership scope remains superseded by closed entry 09.
  Entry 01 is `closed`.
- **2026-11-10 — entry 10 selected; final UI/UX consistency pass prepared.**
  The Cooperator requested a final shell consistency pass before the deferred
  upload-flow whole: unify Timeline search with Gallery, separate browsing tabs
  from the Search/Research/Review action group, remove table underlines, move
  Publication first with green-border emphasis and right-align Kind/Status/
  Visibility, and use an eye-style public visibility glyph. The whole's Stage 1
  revalidation is recorded, the handout is at
  `10-ui-ux-consistency/00_handout.md`, and the first Planner prompt
  `01_planning_00.md` is ready for manual delivery. Entry 10 is `active`;
  entry 02 remains `handed-off` and deferred until entry 10 finishes.
- **2026-11-10 — entry 10 first Planner blocked by P4; corrected prompt ready.**
  The first Planner stopped `PARTIAL` without a plan because the prompt required
  a direct report write under Native Plan Mode without naming the client
  completion route (P4). Coordinates `01/01` are consumed; the initial planning
  cycle is not. Corrected initial Planner `01_planning_01.md` is prepared for
  the same healthy session at `01/02`, with the plan-output/exact-content return
  route, prior report `01_report_00.md`, and report destination
  `01_report_01.md`. No repository, Git, NUC or host mutation occurred.
- **2026-11-10 — entry 10 plan accepted; implementation prompt ready.** The
  corrected Planner returned a complete plan for the shell/search/filter/
  listbox/link/glyph consistency pass; the report's `PARTIAL` status reflected
  only the client Plan Mode write prohibition, and the Cooperator persisted the
  exact content. The plan includes the Cooperator-selected Tab/Enter listbox
  correction and a ten-path UI/documentation allowlist. Implementation prompt
  `02_implementation_00.md` is prepared for fresh session 02 with one local
  commit, no push, direct-write report `02_report_00.md`. A fresh E2 acceptance
  follows the implementation. Entry 02 remains deferred.
- **2026-11-10 — entry 10 implementation PASS; E2 acceptance ready.** The
  accepted plan was implemented at local candidate `bbf776c` (parent `e6b26eb`)
  across exactly ten allowlisted UI/documentation paths: grouped browsing/action
  navigation, shared Gallery-style Timeline search, Publication-first aligned
  filters, focused-option listbox correction, no title underlines and the eye
  legacy glyph. The Orchestrator re-ran the gate at `e6b26eb`, the full
  local-web suite: 208 passed, and the Node suite: 85 passed. Prompt
  `03_acceptance_00.md` is prepared for fresh independent E2 acceptance in
  session 03; report `03_report_00.md` is pending. Publication, deployment and
  rendered acceptance remain pending; entry 02 stays deferred.
- **2026-11-10 — entry 10 E2 acceptance, publication and deployment PASS.** Fresh
  session 03 returned acceptance-PASS at `bbf776c`; all A-I claims passed with
  208 local-web and 85 Node tests. The candidate was published normally
  (`e6b26eb..bbf776c`) and deployed through the canonical helper; post-deploy
  status reports active/web `bbf776c`, service active, database revision `0035`
  and backup restore-readiness ready. Terminal `sudo -K` was run. The Cooperator's
  rendered acceptance of the new shell remains the only pending closure input;
  entry 02 stays deferred.
- **2026-11-10 — rendered shell PASS; final consistency correction requested.**
  The Cooperator accepted the implemented grouping/search/filter/listbox/link/
  glyph changes, then required the Timeline search to move into the header
  toolbar, the visible Timeline hero/lede/note to be removed, and the separate
  History tab/page to be removed entirely. Timeline becomes the single personal
  search/research history overview; `#/history` addresses resolve to Timeline;
  the question/answer API and data model remain. Bounded correction
  `02_correction_01.md` is prepared for session 02/02 with a UI/docs/ADR
  allowlist, one local commit and report `02_report_01.md`. A fresh E2
  re-acceptance, publication, deployment and rendered acceptance follow. Entry
  02 stays deferred.
- **2026-11-10 — entry 10 correction PASS; current-marking micro-correction.**
  Session 02/02 returned implementation-PASS at local `27aa5fd` (parent
  `bbf776c`) across 14 UI, documentation and ADR paths. The Orchestrator re-ran
  the gate at `bbf776c`: PASS, 208 local-web tests and 84 Node tests. The
  header search, trimmed Timeline, History removal and fold, ADR-0088 and owner
  documents are consistent, with no API/authorization/payload/schema/data
  change. Review found that deleting the History current-marking branch left
  `#/requests/...` and `#/records/...` with no active browsing tab, although
  those pages remain reachable from Timeline. Bounded prompt
  `02_correction_02.md` is prepared for session 02/03, allowlisting only
  `app.js` and `kronika_ui.test.js`; report `02_report_02.md`. Final E2
  re-acceptance, publication, deployment and rendered acceptance remain; entry
  02 stays deferred.
- **2026-11-10 — entry 10 final candidate; fresh E2 acceptance prepared.**
  Session 02/03 returned implementation-PASS at local
  `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e` (parent `27aa5fd`), mapping
  request and record routes back to the Timeline tab and adding the regression
  test. The Orchestrator re-ran the gate at both `27aa5fd` and the published
  baseline `bbf776c`: PASS, 208 local-web tests and 85 Node tests. The whole
  diff `bbf776c..8646146` is exactly the fourteen allowlisted paths; the final
  micro-correction is exactly two. Fresh final E2 acceptance prompt
  `04_acceptance_00.md` is prepared for session 04/01 against `8646146`, with
  report `04_report_00.md`. Final acceptance, publication, deployment and
  rendered acceptance remain pending; entry 02 stays deferred.
- **2026-11-10 — entry 10 final E2 acceptance, publication and deployment PASS.**
  Fresh session 04 returned acceptance-PASS at
  `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e` with all A-I claims PASS, 208
  local-web tests and 85 Node tests. The auditor recorded one prompt-text
  near-miss: the changed-path list named fifteen paths while the measured diff
  is fourteen; `tests/gallery_search_tag_filters.test.js` is unchanged but
  remains in the test command. The candidate was published normally
  (`bbf776c..8646146`) and deployed through the canonical helper; post-deploy
  status reports active/web `8646146`, capture unchanged, service active,
  database revision `0035` and backup restore-readiness ready. Terminal
  `sudo -K` was run. The Cooperator's rendered acceptance of the final shell is
  the only pending closure input; entry 02 stays deferred.
- **2026-11-10 — entry 10 rendered PASS and closed.** The Cooperator declared the
  deployed `8646146` final shell PASS for the header search, Timeline trim,
  History-free navigation and fold, request/record current marking,
  Publication-first filters, listbox activation, title links, eye glyph, Gallery
  search and narrow layout, and authorized closure. The closure record is in the
  whole's `00_notes.md`; the notes are frozen. The changed-path enumeration
  surplus in `04_acceptance_00.md` is retained as a non-blocking orchestration
  near-miss.
- **2026-11-10 — entry 02 opened; first Planner prepared.** With entries 01, 09
  and 10 closed, the run-scoped Orchestrator opened `upload-flow-polish`. The
  provisional handout was revalidated against Kronika `8646146`, AP `d7023cf`,
  the NUC release and the current ADR-0088 product truth; stale repository,
  predecessor and History facts are corrected in the whole's `00_notes.md`.
  Prompt `01_planning_00.md` is prepared for fresh session 01/01, Native Plan
  Mode required, initial approval-gated planning; report `01_report_00.md`.
  Implementation, acceptance, publication, deployment and rendered acceptance
  remain pending.
- **2026-11-10 — entry 02 plan approved; implementation prepared.** Fresh session
  01/01 returned a decision-complete plan at `01_report_00.md`: per-dialog
  default-off auto-start, companion progress inside the existing hosted dialog,
  preservation of administrator duplicate review and ordinary duplicate
  privacy, two ownership/resume fixes, a nine-path UI/test/docs allowlist and no
  API, authorization, schema or companion-protocol change. The Cooperator
  approved the plan and both product choices. Prompt `02_implementation_00.md`
  is prepared for fresh session 02/01 with Native Plan Mode OFF, the exact
  nine-path allowlist, baseline `8646146` and report `02_report_00.md`.
  Implementation, acceptance, publication, deployment and rendered acceptance
  remain pending.
- **2026-11-10 — entry 02 implementation delivery mismatch; corrected grant.**
  The file `02_report_00.md` is byte-identical to the planning report
  `01_report_00.md` and carries session 01 / Planning coordinates. No
  implementation commit exists; HEAD and public `main` remain `8646146` and the
  worktree is clean. The misdelivered report is preserved unchanged and is not
  accepted. Corrected prompt `03_implementation_00.md` is prepared for a
  genuinely fresh session 03/01 with baseline `8646146`, the same accepted plan
  and nine-path allowlist, and report `03_report_00.md`. Implementation,
  acceptance, publication, deployment and rendered acceptance remain pending.
