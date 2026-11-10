# Era 01 Whole Notes — Kronika timeline and history media thumbnails

Classification: private local historical/evidentiary projection for this
logical whole. Orchestrator-owned, append-only during the whole, frozen at
closure. Public-safe by default. Michal owns any Meta Git commit.

Working identity:

```text
timeline-and-history-media-thumbnails
```

Trace:

```text
/Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/
```

Run map:

```text
/Users/agile/meta/projects/kronika/01/00_RUN_MAP.md
```

Opening date: 2026-11-09.

Opening Orchestrator: fresh Orchestrator instance, continuation of the
provisional handout restoration under AP Continuation Bootstrap Stage 1.

Predecessor whole: `projects/kronika/01/00-ux-refresh-acceptance-and-promotion`
(closed 2026-11-08; result `7ee4684f529b3d2cdf15ce30902ba01a2b39992c`).

## Restoration status — 2026-11-09

- Continuation Bootstrap Stage 1 is complete for this whole.
- Stage 2 has not started. The COOPERATOR has not selected this whole. Run map
  entry 01 remains `provisional`.
- No Worker prompt was issued; no Worker session or exchange coordinate was
  consumed.
- No active Worker or in-progress mutation was found for this whole.
- No Kronika repository, Git, NUC, deployment, browser, provider, account, or
  filesystem mutation was performed. The only write is this Meta notes record.
- The provisional handout remains frozen and unedited.

Verified anchors:

```text
Kronika local HEAD / public main:
  246c9f86b72e652cd36ed0d9f4e19e77f972df91
Kronika working tree: clean
AP pin (superproject gitlink and .ap HEAD):
  d7023cf037f6d17885c3ede5c04812c61640da50
AP public main:
  d7023cf037f6d17885c3ede5c04812c61640da50
Governing AP variant: stable
./.ap/ap doctor: PASS
./.ap/ap project check --root /Users/agile/Projects/kronika \
  --baseline 246c9f86b72e652cd36ed0d9f4e19e77f972df91: PASS
  (standard sanitized-environment warning for inherited SSH_AUTH_SOCK and PATH)
```

`246c9f8` is the pin-only commit whose parent is `7ee4684`; it changes only
the `.ap` gitlink and one line in `tests/contract/test_ap_integration.py`.
`git diff --stat cb5fa4d 246c9f8 -- src extension alembic migrations` is
empty, so the E3-accepted runtime remains `cb5fa4d`.

The predecessor closure record confirms: E3 acceptance-PASS at `cb5fa4d`,
implementation-PASS, publication at `7ee4684`, NUC deploy PASS,
Cooperator-declared rendered acceptance, and
`Logical-whole closure: closed-by-ORCHESTRATOR`. Carried residuals A6, R7, R9
(`app.js` measured 15322 lines) and R10 were re-read.

Upgrade ledger `docs/AP_UPGRADE_OBSERVATIONS.md` is structurally valid and
declared in `AGENTS.md` outside the managed block. Its single active entry
`consumer-declared-execution-and-capability-route-binding` is `accepted`,
non-authorizing and `retain-active`; `Last revalidated against` `7ef45da` is
an ancestor of the current pin, and its disposition evidence ADR-0012 and
ADR-0018 are present and unchanged at `d7023cf`. No contradiction was found.
The ledger was not mutated.

NUC state was not revalidated because NUC contact was not authorized. R10
item presence and the underlying Cooperator rendered-acceptance event were
also not independently observed. The run map's recommendation remains
`timeline-and-history-media-thumbnails`, supported by the accepted
`GalleryPreviewBackfillCoordinator`, the existing gallery-preview route and
the `docs/UX_AUDIT.md` recommendation; it is a recommendation, not a
selection.

## Handout Revalidation Record

```text
Handout revalidation: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/00_handout.md
Received handout status: provisional
Revalidated against: Kronika 246c9f86b72e652cd36ed0d9f4e19e77f972df91 (local HEAD = public main, clean); AP d7023cf037f6d17885c3ede5c04812c61640da50 (Kronika .ap gitlink = .ap HEAD = AP public main, governing variant stable); predecessor closure record in projects/kronika/01/00-ux-refresh-acceptance-and-promotion/00_notes.md (closed-by-ORCHESTRATOR, result 7ee4684f529b3d2cdf15ce30902ba01a2b39992c); run map projects/kronika/01/00_RUN_MAP.md; declared upgrade ledger docs/AP_UPGRADE_OBSERVATIONS.md at the same pin
Usable facts: repository identity cisarik/kronika main and local checkout path; clean tree; 246c9f8 is the pin-only commit with parent 7ee4684 changing only the .ap gitlink and one line in tests/contract/test_ap_integration.py; runtime paths unchanged from cb5fa4d to 246c9f8; AP pin d7023cf with AP public main matching; governing variant stable; ap doctor PASS; ap project check --baseline 246c9f8 PASS with only the standard sanitized-environment warning; predecessor closure (E3 acceptance-PASS at cb5fa4d, implementation-PASS, publication 7ee4684, deploy PASS, Cooperator-declared closure); carried residuals A6, R7, R9 (app.js 15322 lines) and R10 with the R1-R4 mapping; recommended-whole evidence (GalleryPreviewBackfillCoordinator at src/kronika/application/gallery_preview_backfill.py; gallery-preview route in src/kronika/adapters/api/gallery_preview_api.py, public_published_api.py and the ingress policy; tests/contract/test_gallery_preview_api.py; docs/UX_AUDIT.md "Recommendations not yet implemented" lists Timeline/History thumbnails); ADR-0082 through ADR-0086 present; ROADMAP active order S4-D -> S4-A -> S6 -> S4-B -> S7-P -> S8 -> S9 -> S10 with S10 complete; security and execution rules in AGENTS.md, ap.project.conf and docs/WORKER_EXECUTION_CONTRACT.md; run map entry 00 closed and entry 01 provisional with this handout locator; author and persister metadata consistent with the Meta trace; sections 2.2-2.4 framed as scope questions and candidates, not answers or grants; section 7 no-authority statements; ledger entry consumer-declared-execution-and-capability-route-binding structurally valid, accepted, non-authorizing, retain-active, last revalidated 7ef45da (ancestor of d7023cf), disposition evidence ADR-0012 and ADR-0018 present at the pin
Stale facts and corrections: none
Not revalidated: section 1.4 NUC state (active_release and web_release 7ee4684f529b3d2cdf15ce30902ba01a2b39992c; capture_release 5b86d896b3ea03f89fef2c90f7af2c121d0ef915; layout canonical; service_active active; database_revision 0035; backup_restore_readiness ready) - NUC contact not authorized, and the consequent claim that the NUC no longer serves current public main is a consistent inference, not a measurement; R10 verification item jNQXAC9IVRw presence and requester-private state - requires application or NUC access; R7 live X-button clearance - a Cooperator observation, not independently measured; the underlying Cooperator-declared rendered acceptance - recorded in the frozen predecessor notes, not independently observed
Handout disposition: adopted
```

The handout's receipt-time `Current phase: Restoration (Continuation Bootstrap
Stage 1 not yet performed)` is superseded by this record: Stage 1 is complete
and Stage 2 has not started. No substantive handout fact changed.

## Next step

Await the COOPERATOR's selection. Stage 2, the first Planner prompt, the
delivery-route selection and every mutation remain unstarted. This record
grants no authority.

---

## Session log — 2026-11-09

- **Whole selected.** The COOPERATOR selected
  `timeline-and-history-media-thumbnails` (run map entry 01) and directed work
  under the governing AP with Meta prompt archiving. Stage 2 selection is
  recorded. The run-scoped Orchestrator opened this whole itself under
  `AP_ORCHESTRATOR.md` Run-Scoped Orchestration step 5 because the selection
  arrived in the same session that completed Stage 1; a fresh per-whole
  Orchestrator would duplicate the revalidation already recorded above.
- **First Planner prompt issued and archived.** Worker session `01`, exchange
  `01`, profile Planner, `fresh-worker-session`, `Native planning mode:
  required`, `Planning cycle: initial`, approval-gated, implementation
  prohibited in the same session, post-plan implementation session
  `fresh-worker-session`. Delivery route: manual Cooperator delivery; direct
  dispatch with actual client-native planning mode is unavailable in this
  Orchestrator environment, and the predecessor whole used the same manual
  route. Prompt `01_planning_00.md`; report destination `01_report_00.md`.
- **No project mutation.** No Kronika repository, Git, NUC, deployment, browser,
  provider, account or filesystem mutation was performed. No Worker
  implementation authority, acceptance, publication or closure was issued. No
  Worker coordinates were consumed by a failed exchange.

## Plan acceptance — 2026-11-09

- The terminal planning report is present at `01_report_00.md` and was read
  back in full. Its historical `Status: PARTIAL` recorded a client write
  prohibition, not incomplete planning content. The Cooperator persisted the
  exact report through the AP completion route; the required file-delivery gap
  is closed. The planning content is complete.
- **Plan disposition: accepted.** The Orchestrator accepts the plan's explicit
  defaults: preserve the existing 36 px icon slot; add a nullable
  `preview_location_id` only to `/api/timeline` and `/api/my/records`; select
  the lexical first eligible location with no readiness probing or
  alternate-location retry; interpret "no N+1" as no per-record locator/detail
  discovery with explicitly bounded individual image delivery; use E2
  implementation verification plus the Cooperator's rendered acceptance while
  the audience boundary remains unchanged.
- **Acceptance route:** E2 implementation verification and direct Orchestrator
  acceptance, then publication and the Cooperator's rendered acceptance on the
  exact public-main NUC release. A fresh independent acceptance is mandatory
  only if the candidate changes the preview route, the audience guard, or the
  response beyond the safe locator.
- **Next step:** implementation session `02`, exchange `01`, fresh
  Implementation Worker, `Native planning mode: not-used`, prompt
  `02_implementation_00.md`, report `02_report_00.md`. The Cooperator granted
  NUC SSH access and an active `sudo -v` timestamp; the implementation exchange
  does not contact the NUC. A separate deployment grant will use that access
  after publication.
- **Implementation prompt issued.** The prompt `02_implementation_00.md` was
  issued for fresh Worker session `02`, exchange `01`, with the exact baseline
  `246c9f8`, the fourteen-path allowlist from the accepted plan, one normal
  local commit and no push, and direct-write report `02_report_00.md`. Direct
  session dispatch is the selected route because the implementation does not
  require native planning mode. No NUC, browser, provider or host access is
  granted in this exchange.
- **Implementation report received.** `02_report_00.md` reports
  implementation-PASS at local commit
  `72e8bb0b912eadcb0a51e66ff276b4448a266bde`, with the focused Python and Node
  suites passing. The Orchestrator re-ran the same 223 Python, 35 selected
  local-web and 43 Node tests independently; all passed. The diff is exactly
  the fourteen allowlisted paths and the preview route, audience policy,
  public composition and Gallery/Details renderers are untouched.
- **One concrete finding — bounded correction granted.** The implementation
  placed preview retirement and list cancellation inside
  `kronikaPauseForHide()`, which is also called on ordinary
  `visibilitychange` to hidden. That retires all card previews and aborts
  in-flight list requests merely when the tab is backgrounded; returning to the
  tab does not reload them. This is broader than the accepted "document
  teardown" behavior. Correction prompt `02_correction_01.md` was issued to the
  same healthy Worker session `02`, exchange `02`, profile Bounded Correction
  Worker, limited to `src/kronika/adapters/api/web/app.js` and
  `tests/kronika_ui.test.js`, report `02_report_01.md`. The correction must
  keep polling pause on visibility change but retire previews only on page
  teardown, and add the causal visibility regression test.
- **Correction report received.** `02_report_01.md` reports implementation-PASS
  at correction commit `b66ec8f50860ace624f6be1fd3ad63f521edcd33` on parent
  `72e8bb0b912eadcb0a51e66ff276b4448a266bde`. The Orchestrator inspected the
  two-path diff: `kronikaPauseForHide()` is polling-only again, a separate
  `kronikaRetireListsForPageHide()` performs preview/list retirement on
  `pagehide`, and the new visibility regression test passes.

## Acceptance — 2026-11-09

The Orchestrator independently re-ran the final candidate evidence at baseline
`246c9f86b72e652cd36ed0d9f4e19e77f972df91`: the focused Python suite passed
223 tests, the selected local-web suite passed 35 tests, the Node suite passed
44 tests, and `ap project check` passed. The final diff is exactly the
fourteen allowlisted paths; the preview route, audience policy, public
composition, route-policy tables and Gallery/Details renderers are untouched.
The correction preceded acceptance, so the final candidate received one initial
E2 acceptance, not a post-acceptance re-acceptance.

```text
Acceptance candidate: b66ec8f50860ace624f6be1fd3ad63f521edcd33
Acceptance owner map: 01_report_00.md section 6 control matrix T1-T16; 02_report_00.md section 7; 02_report_01.md section 4
Acceptance allowlist: the fourteen implementation paths in 02_implementation_00.md section 2; the correction is a subset
Acceptance risk claims: T1-T15 accepted at E2; T16 deployment identity pending
Acceptance control matrix: 01_report_00.md section 6
Acceptance independence: not-required
Primary fresh acceptances used: 0
Automatic corrections used: 1
Correction re-acceptance: not-applicable (the correction preceded acceptance)
Named missing-evidence probe: none
Out-of-scope observations: none
```

**Acceptance-PASS at E2** for candidate `b66ec8f`. Publication has not occurred:
the candidate is two local commits ahead of public `main` `246c9f8`. Deployment,
NUC refresh and the Cooperator's rendered acceptance remain pending. The
Cooperator granted NUC SSH access and an active `sudo -v` timestamp for the
later deployment exchange; the whole has not yet used it.

## Publication and deployment — 2026-11-09

- **Publication PASS.** The accepted candidate was pushed normally:
  `246c9f8..b66ec8f` on `main`, no force. Direct `git ls-remote` readback
  returned `b66ec8f50860ace624f6be1fd3ad63f521edcd33` for
  `refs/heads/main`; local HEAD and `origin/main` match; the tree is clean.
- **Deployment PASS.** The canonical helper sequence was used against
  `framenest-nuc` through the read-only transport arguments:
  `status` -> `check --release b66ec8f...` -> `deploy --release b66ec8f...
  --yes`. The deploy completed with exit 0. Post-deploy `status` reports:
  `layout: canonical`, `active_release` and `web_release`
  `b66ec8f50860ace624f6be1fd3ad63f521edcd33`, `capture_release`
  `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`, `service_active: active`,
  `database_revision: 0035`, `backup_restore_readiness: ready`. A bounded
  read-only check confirmed the deployed shell `app.js` contains the
  `kronika-card__preview` implementation.
- **Terminal privilege release.** `sudo -K` was run on the NUC through the
  canonical operator gate. A subsequent `sudo -n true` requires a password,
  confirming the Cooperator's timestamp is revoked. A later deployment needs a
  fresh Cooperator `sudo -v`.
- **Production acceptance remains Cooperator-owned.** The Cooperator directed
  publication and deployment and selected whole 02 next; he did not provide a
  rendered UI/UX verdict. This whole therefore records
  publication-PASS and deployment-PASS, not a fabricated
  production-acceptance-PASS. Its formal closure remains pending the
  Cooperator's rendered verdict; the publication/deployment evidence is
  available for the next whole and for a later closure record.
- **Active mutation: none.** The deployment lock completed and the helper
  reported a clean completion. No capture transition, provider call, secret
  change or public listener was introduced.

## Acceptance pause — product-scope finding, 2026-11-09

The Cooperator's first rendered-review step found a product-scope mismatch, not
an implementation defect in the approved-only thumbnail slice:

- The current Timeline is the accepted ADR-0083 Timeline: it contains only
  administrator-approved household records. `GET /api/timeline` filters
  `visibility = family`, a non-null approved projection and a non-null
  `timeline_entered_at_ms`.
- The "All" chip is a kind filter over those approved records, not a
  visibility/source filter. The two visible research cards are approved; media
  that is private, unanalysed or not yet approved is intentionally absent.
- Whole 01 added safe previews to the cards that already belong to that
  approved Timeline and to personal-record History. It did not change Timeline
  membership.

The Cooperator expects the Timeline itself to be a complete chronological
overview of everything added to Kronika, including unanalysed and unpublished
items, presented as a compact table/list with small thumbnails rather than a
Gallery. That is a new product objective which changes ADR-0083's
approved-only Timeline and its privacy/approval boundary. It is not a defect
correction inside whole 01.

Acceptance of whole 01 is therefore paused. No implementation change was made
in response to this finding. The Cooperator must choose the product route:
a new complete-chronicle Timeline whole, a separate Library/All-media view that
preserves the approved-only Timeline, or a smaller label-only clarification.

## Cooperator decision — route A, 2026-11-09

The COOPERATOR chose **route A**: a new logical whole
`timeline-complete-chronicle` (run map entry `09`). It supersedes ADR-0083's
approved-only Timeline membership with a complete, visibility-aware
chronological Timeline of everything added to Kronika that the signed-in
identity may see, including private, unanalysed and unpublished items, presented
as a compact table/list with small media thumbnails rather than a Gallery.
Gallery/Details, personal History, administrator-controlled household
publication, the preview route and the privacy boundary remain separate
constraints and must not be widened.

Whole 01's thumbnail implementation, publication and deployment remain
groundwork. Its formal closure stays paused, not PASS, because the rendered
product expectation changed. The new whole's provisional handout is:

```text
/Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/00_handout.md
```

The 02 `upload-flow-polish` handout remains prepared but is deferred until after
the new whole unless the COOPERATOR explicitly reorders.

## History rendered finding and UI polish grant — 2026-11-10

The Cooperator tested the deployed `65772c6` History view and found a UX
problem: the **Questions** and **Records** tabs show effectively the same
personal items, so the split is duplicate and confusing. The current History
cards are also visually inconsistent with the new eye-candy Timeline chronicle
list.

Cooperator direction:

- keep **only Questions**; remove the duplicate Records tab and its separate
  history view;
- use the same compact table/list visual language as the new Timeline: header,
  rows, separators, emoji status/visibility, subtle green hover/focus;
- give the question text the available width; show no Added/created date;
- keep the page consistent, user-friendly and attractive;
- do not reopen the Timeline, Gallery/Details, API, authorization or stored
  data.

Whole 01's Timeline-membership scope remains superseded by the now-closed whole
09. This correction covers the remaining History presentation. Bounded UI
polish prompt `02_correction_02.md` was issued to whole 01's healthy Worker
session `02`, exchange `03`, with a UI-only allowlist, one local commit and
report `02_report_02.md`. After the report, the Orchestrator verifies the diff,
publishes and deploys the corrected release, and the Cooperator renders the
History result. Whole 01 remains open until that rendered acceptance.

## History correction reconciliation and publication — 2026-11-10

`02_report_02.md` is present and was read back in full. It is a terminal
`implementation-PASS` report at commit
`e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd`, parent
`65772c6028c07edcab47b6928dbb31e30876c70a`, on local `main` with no push. The
correction changes five paths: the History UI in `app.js`, `index.html`,
`styles.css`, the Node tests and one normative `SPEC.md` sentence. The worktree
is clean.

The Orchestrator inspected the diff: the Questions/Records tab pair is gone;
`#/history/records` resolves to `#/history` with any offset; History reads only
`/api/research-requests`; the list uses the Timeline chronicle row language with
Question, Kind, Status and Visibility, no preview or Added date, glyph status and
visibility with accessible text, and the Timeline hover/reduced-motion rules.
The API, authorization, stored data, Timeline, Gallery and Details are unchanged.
The Orchestrator independently re-ran the gate at baseline `65772c6`, the Node
suite: **55 passed**, and the selected local-web suite: **43 passed**.

**E2 Orchestrator acceptance of the History correction: PASS.** The correction
is published: `65772c6..e6b26eb` on public `main`, no force; direct `git
ls-remote` readback returned `e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd`; local
HEAD and `origin/main` match. Deployment is pending a fresh Cooperator
`sudo -v`; the previous timestamp was revoked after the `65772c6` deploy. The
History rendered acceptance remains the Cooperator's; whole 01 stays open until
that verdict.

## History correction deployment — 2026-11-10

The Cooperator refreshed the NUC sudo timestamp and the canonical helper
completed the routine deployment at
`e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd` with exit 0. Post-deploy `status`
reports `layout: canonical`, `active_release` and `web_release`
`e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd`, `capture_release`
`5b86d896b3ea03f89fef2c90f7af2c121d0ef915`, `service_active: active`,
`database_revision: 0035` and `backup_restore_readiness: ready`. Bounded
read-only checks confirmed the deployed shell has the History chronicle header
and no old Records tab markup. Terminal `sudo -K` was run; a following
`sudo -n true` requires a password. A later deployment needs a fresh Cooperator
`sudo -v`.

Whole 01 is now E2 acceptance-PASS, publication-PASS and deployment-PASS at
`e6b26eb` for the History Questions-only correction; its Timeline-membership
scope remains superseded by closed whole 09. The Cooperator's History rendered
acceptance is the remaining closure input. Whole 02 `upload-flow-polish` remains
prepared and deferred.

## Closure — 2026-11-10

The COOPERATOR declared the deployed History Questions-only correction **PASS**
and authorized closure of whole 01. The Timeline-membership part of the original
objective was superseded by the Cooperator's route A and the now-closed whole 09.

```text
Phase-qualified result: production-acceptance-PASS (Cooperator-declared)
Result artifact or commit: e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd
Result evidence: Cooperator rendered PASS for History on the deployed e6b26eb;
  E2 acceptance of the History correction; publication-PASS; NUC deployment-PASS
  with active/web e6b26eb, service active, database revision 0035 and backup
  restore-readiness ready
Required preceding results: satisfied
Cooperator-owned decisions: satisfied — History rendered acceptance and closure
  declared; Timeline-membership scope superseded by route A and closed whole 09
Residual-risk disposition: satisfied — the original History media-thumbnail
  display was deliberately replaced by the Questions-only decision; no medium or
  higher residual; predecessor R10 remains a separate Cooperator-owned item
Upgrade-ledger reconciliation: complete — entry
  consumer-declared-execution-and-capability-route-binding remains accepted,
  non-authorizing, retain-active; no ledger mutation
Active mutation: none
Closure actor: ORCHESTRATOR
Logical-whole closure: closed-by-ORCHESTRATOR
```

These notes are frozen at closure. The next UI/UX consistency work is a separate
logical whole; the deferred `upload-flow-polish` remains separate.
