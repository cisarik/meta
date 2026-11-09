# Kronika — Fresh Orchestrator Handoff

```text
Restoration classification: PARTIAL
Handout status: provisional
Capability profile: Orchestrator
Initialization signal: You are a fresh Orchestrator instance assigned to the ORCHESTRATOR role for the Kronika project.
Orchestrator session scope: logical-whole
Development run identity: kronika-run-01
Current phase: Restoration (Continuation Bootstrap Stage 1 not yet performed)
Reasoning recommendation: selecting a Worker is premature
Restoration date: 2026-11-09
Refreshed: 2026-11-09
Refreshed against: AP d7023cf; Kronika b66ec8f; .ap d7023cf
Handout author: the run-scoped Orchestrator of Kronika run 01 (this session)
Original handout author: not-applicable (new whole)
Mechanical persister: the same run-scoped Orchestrator
Predecessor whole: projects/kronika/01/01-timeline-and-history-media-thumbnails (E2 acceptance-PASS; publication-PASS; deployment-PASS; rendered acceptance paused by this new product objective; preview groundwork retained)
Run map: /Users/agile/meta/projects/kronika/01/00_RUN_MAP.md
Handout destination: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/
Restoration grants mutation authority: no
```

This prompt transfers information, never authority. It is a **provisional
seed** for a newly selected whole. The receiving per-whole Orchestrator
revalidates it in Continuation Bootstrap Stage 1 and records a Handout
Revalidation Record before the first Planner prompt. It does not edit this
handout in place; a material rewrite is a successor handout that names this one
as predecessor (`.ap/AP.md#run-level-handouts`).

**Creation note (2026-11-09).** This whole was created after the Cooperator's
first rendered-review step on whole 01 found that the approved-only Timeline did
not match the intended complete chronicle. The Cooperator chose **route A**: a
new logical whole that makes the Timeline a complete, visibility-aware
chronological overview of everything added to Kronika that the signed-in
identity may see, including private, unanalysed and unpublished items, presented
as a compact table/list with small media thumbnails rather than a Gallery. This
handout is the fresh Orchestrator seed for that whole.

The COOPERATOR is **Michal**. Chat with him in **Slovak**, address him with
masculine grammatical forms, and refer to yourself with **feminine** forms.
Worker prompts, Worker reports, repository documentation, and Meta artifacts are
professional **English**.

---

## 0. Cooperator operating preferences for this whole

These are project-local operating instructions from the COOPERATOR. They sit
inside AP and do not override it.

```text
No subagents. The Orchestrator must not call the subagent tool or delegate any
  Worker task to a subagent. The Orchestrator prepares prompts and reconciliation
  itself.

Meta is the prompt/report archive. Write every Orchestrator-owned prompt,
  report, note, handout and run-map update into the exact Meta path. Do not keep
  task prompts only in chat.

Manual Worker delivery. The COOPERATOR sends every Worker prompt manually. The
  Orchestrator archives the complete prompt in Meta, presents the delivery
  capsule, and waits for the COOPERATOR to deliver it. The Orchestrator does not
  dispatch Workers directly.

Direct-write Worker reports. Every Worker prompt requires the Worker to write its
  terminal report directly to the exact Meta path and read it back. The
  COOPERATOR never copy-pastes report content. The Orchestrator verifies the
  report from the trace.

Meta Git belongs to the COOPERATOR. The Orchestrator writes files but does not
  stage, commit, push or rewrite Meta history.

Repository and NUC work stay under the exact current Worker grant. The
  Orchestrator may inspect read-only; mutation needs a complete prompt.
```

The prompt/report pair is archived together in Meta only after the report
exists. The COOPERATOR owns that Git action.

---

## 1. Read this first

Read this handout together with:

- `AGENTS.md` at the Kronika repository root and its managed AP block;
- `.ap/AP.md`, `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md` at the pinned AP
  commit, per the ORCHESTRATOR minimum-reading spine;
- `.ap/PROMPT_CONTRACTS.md` for the planning, implementation, acceptance, report
  and trace structures, including the Run Map Record, Provisional Handout
  Marker and Handout Revalidation Record;
- the upgrade ledger declared in `AGENTS.md`,
  `docs/AP_UPGRADE_OBSERVATIONS.md`;
- the run map `/Users/agile/meta/projects/kronika/01/00_RUN_MAP.md`;
- the predecessor whole's frozen evidence under
  `/Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/`,
  especially `00_notes.md`, `01_report_00.md`, `02_report_00.md` and
  `02_report_01.md`;
- the closed 00 whole's `00_notes.md` and the closed 00 handout's §9.2
  candidate list under
  `/Users/agile/meta/projects/kronika/01/00-ux-refresh-acceptance-and-promotion/`;
- the prepared but deferred `upload-flow-polish` handout under
  `/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/00_handout.md`,
  only to understand the deferred order; do not open that whole.

The predecessor notes and reports are frozen historical evidence. Read them for
continuity; do not rewrite them.

Meta `/Users/agile/meta/AP_DEFECTS.md` (§0.0, D-17b, D-19, D-20, D-21) and
`/Users/agile/meta/AP_DESTILLED.md` (§17) remain citable consumer evidence of
what the predecessor run measured. They are not rule sources: the direct-write
default, the mutation axes, the satisfiability check, consumed coordinates and
the standing maintenance duty are owned by AP at `d7023cf`.

---

## 2. Continuation Bootstrap, Stage 1 — restore and reconcile read-only

Verify, do not trust this handout. The state below was observed on 2026-11-09;
revalidate every material fact.

### 2.1 Repository

```text
Repository: https://github.com/cisarik/kronika (main)
Local checkout: /Users/agile/Projects/kronika
Last observed HEAD: b66ec8f50860ace624f6be1fd3ad63f521edcd33
Last observed public main: b66ec8f50860ace624f6be1fd3ad63f521edcd33
Last observed tip subject: fix: keep card previews across visibility changes
Last observed working tree: clean
```

`b66ec8f` is the published whole 01 preview implementation plus its correction.
It contains the safe preview locator and the Timeline/History card preview
lifecycle that this whole may reuse. It does **not** contain the new complete
Timeline model. Verify with `git rev-parse HEAD`, `git ls-remote origin
refs/heads/main`, and `git status --short`.

### 2.2 Governing AP

```text
AP pin last observed: d7023cf037f6d17885c3ede5c04812c61640da50
Governing variant: stable
```

AP public `main` was `d7023cf` at the refresh. Verify `git ls-tree HEAD .ap`,
`git -C .ap rev-parse HEAD`, and `./.ap/ap doctor`. Do not upgrade the pin as
part of this whole unless the COOPERATOR explicitly selects that separate task.

### 2.3 Repository gate

```text
./.ap/ap project check --root /Users/agile/Projects/kronika \
  --baseline b66ec8f50860ace624f6be1fd3ad63f521edcd33
```

Expected: PASS. Python evidence and tests go only through the declared
`./.ap/ap exec --operation test-focus` route. JavaScript tests use `node --test`.
Cursor/AppImage Workers must never invoke `.venv/bin/python`, `python`,
`python3`, or `poetry run` for evidence.

### 2.4 NUC state — observed after the 2026-11-09 deployment

```text
layout: canonical
active_release: b66ec8f50860ace624f6be1fd3ad63f521edcd33
web_release: b66ec8f50860ace624f6be1fd3ad63f521edcd33
capture_release: 5b86d896b3ea03f89fef2c90f7af2c121d0ef915
service_active: active
database_revision: 0035
backup_restore_readiness: ready
```

The predecessor deployment revoked the Cooperator's sudo timestamp with
`sudo -K`; a later deployment needs a fresh Cooperator `sudo -v`. Revalidate
with `deploy/ubuntu/kronika-release status` only when NUC access is granted; do
not assume the timestamp persists. The NUC currently serves the approved-only
Timeline, not the new complete chronicle.

### 2.5 Predecessor whole state and the new selection

Whole 01 `timeline-and-history-media-thumbnails` is:

- E2 acceptance-PASS at `b66ec8f` after one pre-acceptance correction;
- publication-PASS on public `main` at `b66ec8f`;
- deployment-PASS on the NUC at `b66ec8f`;
- **rendered acceptance paused** because the Cooperator's first review found
  that the approved-only Timeline did not match the intended complete
  chronicle. Its Timeline-membership scope is superseded by this new whole; its
  preview implementation, publication and deployment remain useful groundwork.

The COOPERATOR explicitly selected this new whole as **route A** on
2026-11-09. Do not reopen whole 01, do not rewrite its notes or reports, and do
not treat its approved-only Timeline rule as a fixed constraint for this whole.
Preserve its preview helper, safe locator and test lessons where they fit.

The run map records entry 01 as `active` with acceptance paused, entry 02
`upload-flow-polish` as `handed-off` but deferred, and entry 09
`timeline-complete-chronicle` as `handed-off` and selected next. Run-map status
changes belong to the run-scoped Orchestrator; do not change them unless the
COOPERATOR grants that role explicitly.

### 2.6 Upgrade ledger

`AGENTS.md` declares the AP upgrade ledger outside the managed block
(`Ledger path: docs/AP_UPGRADE_OBSERVATIONS.md`). Validate the declared file and
revalidate every active entry against the current repository and the governing
pin before relying on it (`.ap/AP.md#continuation-bootstrap`,
`.ap/PROMPT_CONTRACTS.md#upgrade-observation-ledger-contract`).

### 2.7 Handout Revalidation Record

Before the first Planner prompt, revalidate every material fact in this handout
against current evidence and record the Handout Revalidation Record
(`.ap/PROMPT_CONTRACTS.md#handout-revalidation-record`) in this whole's
`00_notes.md` (`.ap/AP.md#run-level-handouts`; Meta `README.md`, Run Maps and
Provisional Handouts). Name every material fact you could not observe under
`Not revalidated`, including NUC state when NUC access is not granted and the
Cooperator's unrecorded rendered acceptance for whole 01.

---

## 3. Continuation Bootstrap, Stage 2 — preserve the selected whole

The COOPERATOR has already selected **`timeline-complete-chronicle`**. Preserve
that selection; do not ask him to choose the whole again. Present the restored
state and proceed to the first Planner prompt after the Handout Revalidation
Record.

### 3.1 Objective

Make the **Timeline** the complete, chronological, visibility-aware overview of
everything added to Kronika that the signed-in identity may see:

- include media, Search/Research records and other catalog items the identity
  may read, not only administrator-approved household records;
- include private, unanalysed, unfinished and unpublished items where the
  identity is the owner or an application administrator;
- show each item's kind, title, date, status and visibility clearly;
- present the result as a compact chronological table/list with small media
  thumbnails, not as a Gallery grid;
- preserve Gallery as a separate media browser, personal History as the
  research/question history, and administrator-controlled household publication;
- preserve the existing preview route, audience policy, quarantine, validation,
  identity model and internet-publication prohibition.

The Cooperator's direction, in his own words: *"Timeline má obsahovať všetko, čo
sa do Kroniky dalo, aj neanalyzované, nezverejnené… prehľadne všetko… pod sebou
v tabuľke a s malými náhľadmi, nie Galéria."*

### 3.2 Decision this whole must obtain

ADR-0083 currently says the Timeline is the main page and contains only
administrator-approved records. This whole is explicitly asked to **supersede
that Timeline-membership rule** with a new accepted decision. The Planner must
propose the new ADR, the exact new Timeline semantics, and the migration from
the current approved-only list. It must preserve the other ADR-0083 principles:
modular research providers, personal History, Gallery as a separate view,
administrator approval for household publication, privacy, and internet
publication disabled.

Do not silently reinterpret ADR-0083. The new decision must be explicit,
durable and owned by the appropriate document.

### 3.3 Scope shape (for the Planner, not a grant)

Likely in scope:

- the Timeline data model and read API: what constitutes an item, which source
  tables/records feed it, how unanalysed media and unfinished research appear;
- identity-aware visibility and status: owner, administrator, household,
  private, shared/approved, unfinished, unanalysed, failed, withdrawn;
- chronological ordering, pagination, total counts, filters, search and status
  filters;
- a compact desktop/mobile table/list layout with small media thumbnails and
  kind/status/visibility indicators;
- reuse of the existing safe preview locator/route and fallback icon behavior;
- accessibility, keyboard paths, focus, responsive behavior and inert text;
- tests for visibility, aggregation, ordering, pagination, previews, fallbacks
  and the UI;
- durable documentation: a new ADR, `SPEC.md`, `SECURITY.md`, and the exact
  owners for any changed Timeline/History/Gallery boundary;
- the routine NUC refresh and the COOPERATOR's rendered acceptance.

Likely out of scope:

- Gallery or Details visual redesign (frozen);
- a new media pipeline, provider call, acquisition flow or upload backend;
- the deferred `upload-flow-polish` whole (entry 02);
- companion notifications, onboarding, accessibility pass, localization or
  `app.js` modularization as separate wholes;
- identity/authorization model changes, public internet publication, new
  secrets or host mutation;
- resumable, multi-file or background uploads;
- deleting or rewriting historical records, approvals or whole-01 evidence.

### 3.4 Questions the Planner must answer with repository evidence

1. What exactly is an "item" in the requested complete Timeline? Map
   `logical_media`, `physical_media_locations`, `media_metadata`,
   `media_analysis_runs`, `kronika_records`, `kronika_documents`,
   `research_requests`, approvals, withdrawal and publication rows. Which
   entities exist before analysis, and how can the Timeline show an unanalysed
   media item without inventing a record?
2. What is the exact visibility matrix for owner, administrator, household
   member and unauthenticated caller? Which existing `decide_bound_read`,
   `ContentAudiencePolicy`, record visibility and approved-projection rules can
   be reused? Where must the new Timeline not widen access?
3. How does the new Timeline coexist with Gallery and personal History? Which
   view owns media browsing, which owns research/question history, and which
   owns the complete chronological overview? Avoid a second Gallery and a
   second semantic owner.
4. What is the exact status vocabulary and visual treatment for private,
   shared/approved, household-published, unanalysed, analysing, failed,
   unfinished, withdrawn and public-published-disabled items?
5. What is the exact read API shape and query plan? How many queries per page,
   how are totals counted, how is ordering stable, and how are media previews
   and non-media rows batched without N+1?
6. What is the exact table/list layout on desktop and narrow screens? Which
   columns, thumbnails, status badges, filters and pagination? Which existing
   CSS/test pins must change?
7. Which existing tests pin the approved-only Timeline, the record list APIs,
   the preview route, the Gallery/History presentation and the shell? Which
   must change, which must stay, and what new causal tests prove the new
   visibility and aggregation behavior?
8. Which durable documents own the new decision: a new ADR superseding
   ADR-0083's Timeline membership sentence, `SPEC.md`, `SECURITY.md`,
   `README.md`, `DEVELOPMENT.md`, or another exact owner? Do not create a second
   semantic owner.
9. What is the exact acceptance route? The change supersedes a core
   product/privacy decision and the main page; expect to recommend fresh
   independent acceptance for the visibility/authorization surface rather than
   assuming E2. Justify from the actual boundary.
10. What is the smallest safe implementation slice? If the full complete
    chronicle cannot be one bounded candidate, propose the smallest coherent
    first slice and the exact follow-on slices, with no fake partial acceptance.
11. What is the exact NUC refresh and Cooperator rendered-acceptance sequence,
    including a fresh `sudo -v`, exact release SHA, post-deploy checks and
    rollback?
12. What did whole 01 change in the preview helper, list controllers, CSS and
    tests that this whole should reuse, preserve or deliberately replace?

### 3.5 Deferred and other candidate wholes

`upload-flow-polish` (entry 02) is prepared but deferred until after this whole
unless the COOPERATOR explicitly reorders. The remaining run-map entries stay
provisional and discovery-only. Do not start any of them without an explicit
Cooperator selection.

---

## 4. Strategic continuity — what Kronika is

Kronika is a local-first, privacy-conscious household archive for video,
images and GIFs: archive, search, upload and download (YouTube and X), with
AI-assisted metadata, a premium Gallery, an administrator-curated Timeline,
personal History and provider-backed Search/Research. One authoritative FastAPI
server (SQLite + Alembic) runs on an Ubuntu Intel NUC reached only over
Tailscale; clients are the served web shell and a Chromium side-panel companion
extension.

Authoritative product truth:

- `README.md`, `PRODUCT.md`, `SPEC.md`, `ROADMAP.md`, `SECURITY.md`, `SERVER.md`;
- `docs/adr/README.md`, ADR-0082 through ADR-0086;
- `docs/UBUNTU_NUC_DEPLOYMENT.md`, `docs/WORKER_EXECUTION_CONTRACT.md`,
  `DEVELOPMENT.md`, `GALLERY.md`.

Accepted direction to preserve:

- **ADR-0082** one Kronika, private records by verified owner. **ADR-0083**
  modular research providers; personal History is separate; Gallery is a
  separate working view; administrator approval governs household publication.
  Its approved-only Timeline membership sentence is the decision this whole is
  asked to supersede. **ADR-0084** administrator-managed research settings,
  four exact catalog models, default `gpt-5.5-2026-04-23`, no network model
  discovery, research disabled by default. **ADR-0085** sole Kronika identity;
  bounded cuts, no mass rename. **ADR-0086** companion YouTube save,
  `open_upload`, and in-process preview backfill.
- **ADR-0075** the NUC is the development-and-testing machine; routine refresh
  to the exact public `main` SHA via `deploy/ubuntu/kronika-release` is normal
  operation. **ADR-0060** immutable release contract.
- Security: loopback-first backend, Tailscale-only ingress, no port forwarding;
  Tailscale membership is not administrator authority; `/srv/media` is read-only
  to the service; ordinary clients never receive provider secrets;
  administrator read-all is application content only; household publication is
  an administrator approval; internet publication stays disabled.
- Rendered UI/UX acceptance belongs to the COOPERATOR and requires the code on
  public `main` refreshed onto the NUC first.
- Whole 01 added safe Timeline/History preview locators and client preview
  lifecycle. It did not change upload, quarantine, approval, publication or the
  Gallery/Details renderer.

---

## 5. Operating rules

This handout grants nothing. AP precedence (RF-19) and the AP owners at the
governing pin govern every prompt. Each rule below records what the predecessor
run measured and points to the AP owner that now holds it; if a pointer and its
owner disagree, the owner wins.

### 5.1 Manual Worker prompt delivery and direct-write reports

The COOPERATOR delivers every Worker prompt manually. The Orchestrator's job is
to prepare one complete authoritative prompt, archive it in Meta at the exact
filename, present the delivery capsule, and wait. It must not dispatch a Worker
or use a subagent.

The Worker writes its terminal report directly to the exact Meta path, reads it
back, and only then sends its terminal notice. The Orchestrator verifies the
report from the trace; the COOPERATOR never copy-pastes report content. The
COOPERATOR or authorized Git owner commits the prompt/report pair only after the
report exists.

For every Worker prompt, use these AP spellings, each line exactly once. This
is a spelling projection only; the AP owners above govern:

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: <exact prompt filename>
Destination path: <exact whole directory>
Report filename: <exact report filename>
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: none | <exact repository paths>
Host/remote mutation: none | <exact targets and operations>
Trace persistence: direct-write <exact report path>
```

Resolve every placeholder and alternative to one value. For an authorized
Planner, `Trace persistence` also names the exact received prompt path (P1),
and the prompt names the client completion route (P4). In-session relay is
exceptional: it requires an explicit COOPERATOR selection or a recorded missing
Worker capability, names that other `Report persistence owner`, states the relay
basis, sets `Trace persistence: none`, and the Worker returns the complete
report in the session (P2).

### 5.2 Prompt satisfiability before delivery

Before presenting a prompt for manual delivery, apply the four comparisons owned
by `.ap/AP.md#prompt-satisfiability-check` to the complete prompt:

```text
VALIDATION–AUTHORITY  every required command, observation, generated output and
                      completion write fits the positive authority; no negative
                      clause forbids it
ROUTING               every identity, coordinate, route, mode and destination
                      field holds exactly one concrete value
PERSISTENCE           persistence owners, the three mutation axes, positive
                      authority and the client's permitted completion route
                      agree (delivery record P1–P5)
SPELLING              every path, tool, environment variable, field and command
                      comes from its current durable owner, not memory or an
                      earlier handout
```

A validation command that the prompt's own negative authority forbids is a
prompt defect. Do not issue it and wait for a Worker to block.

### 5.3 First Planner and coordinates

- Every new logical whole starts with a Planner in Worker session `01`,
  exchange `01`, `fresh-worker-session`, `Native planning mode: required`
  (`.ap/AP.md#orchestration-planning-and-implementation-planning`).
- The Planner is read-only for the repository; under the direct-write default
  it still writes its own report to the exact trace path.
- Coordinates are consumed once their prompt is issued, whatever the outcome
  (`.ap/AP.md#consumed-coordinates`). If the first exchange stops on a prompt
  defect and a fresh session is selected, the corrected initial Planner is
  `02/01`; the Meta files are `02_planning_00.md` and `02_report_00.md`, not the
  expected `01_planning_00.md`
  (`.ap/PROMPT_CONTRACTS.md#blocked-first-exchange-example`). Tell the
  COOPERATOR explicitly.
- Meta filenames follow the trace-local mapping
  (`.ap/PROMPT_CONTRACTS.md#trace-local-filename-mapping-example` and the Meta
  `README.md`): `<session>_<phase>_<exchange-index>.md` and
  `<session>_report_<exchange-index>.md`; the exchange index is the AP exchange
  ordinal minus one.

### 5.4 No subagents

The Orchestrator must not use the `subagent` tool or any equivalent internal
delegation for Worker tasks. It may use read-only shell and file tools itself for
restoration and reconciliation. Every planning, implementation, acceptance,
correction, audit, deployment or probe task goes into a complete archived Worker
prompt that the COOPERATOR delivers manually.

### 5.5 AP maintenance is part of normal work

AP §13 owns the standing duty (`.ap/AP.md#standing-ledger-maintenance`):
revalidate the declared upgrade ledger in Stage 1 (§2.6); record newly measured
friction against AP as `untriaged` entries in
`docs/AP_UPGRADE_OBSERVATIONS.md` only under an exact write grant, otherwise as
non-authorizing ledger candidates in the closure or handoff record. A pin update
remains its own explicit AP update task (`AGENTS.md`). Meta `AP_DEFECTS.md` and
`AP_DESTILLED.md` are citable consumer evidence only, not AP rule sources or
ledger discovery sources. Do not ask the COOPERATOR to re-explain friction
already recorded there or in the ledger.

### 5.6 Security boundaries and execution routes

- NUC SSH for Workers goes only through
  `scripts/operator/network/kronika_nuc_worker_gate.fish` (`--probe` first).
  Do not reconstruct `gpgconf` or print agent sockets.
- The canonical operator variables are `KRONIKA_NUC_SSH_TARGET`,
  `KRONIKA_NUC_SSH_USER`, `KRONIKA_NUC_SSH_IDENTITY`, and
  `KRONIKA_NUC_SSH_COMMAND`. The release helper requires the identity as a
  private-key path. The predecessor deployment used the private key, not the
  `.pub` file, and revoked the sudo timestamp with `sudo -K`.
- The COOPERATOR runs `sudo -v` outside the Worker; Workers verify with
  `sudo -n true`, never handle a password, and follow the grant's terminal
  `sudo -K` rule. A timestamp is global and a Worker `sudo -K` revokes it. This
  whole needs a fresh Cooperator `sudo -v` before any later deployment.
- Deployment is only `deploy/ubuntu/kronika-release status` → `check --release
  <40-hex>` → explicit authority → `deploy --release <40-hex> --yes`. A check
  never deploys. Schema jumps use the documented `migration-required` (exit 13)
  continuation.
- No secret, credential, token, cookie, private media filename, host-specific
  identifier, disk serial, UUID, SSH fingerprint, or private network value
  enters repository artifacts or reports.

---

## 6. Forward risk register

| ID | Item | Class | Owner |
|---|---|---|---|
| C1 | Complete Timeline could expose private/unpublished records to the wrong identity | privacy/security | Planner/fresh audit |
| C2 | ADR-0083 approved-only Timeline rule must be explicitly superseded, not silently reinterpreted | product/architecture | Planner/Cooperator |
| C3 | Unanalysed media may have no common record; a union/aggregation design could invent records or duplicate items | data model | Planner |
| C4 | All-items aggregation and totals could add N+1 queries or slow the main page | performance | Planner |
| C5 | Table/list UI could become a second Gallery or an unusable data dump | UI/UX | Planner/Cooperator |
| C6 | Existing test pins on approved-only Timeline, card grid, previews and filters will churn | test/implementation | Planner |
| C7 | Approval/publication semantics could be weakened by showing everything in one view | product/security | Planner/fresh audit |
| C8 | Whole 01 preview groundwork and deferred whole 02 upload flow interact with the new page | cross-whole | Planner |

The new Timeline must clearly distinguish personal/private, shared/approved and
unpublished states. It must not turn administrator read-all or owner access into
household visibility, and it must not turn the Gallery/Details freeze into a
redesign.

---

## 7. First actions for the fresh Orchestrator

1. Read `AGENTS.md`, the AP spine, `AP_ORCHESTRATOR.md`, and the named
   `PROMPT_CONTRACTS.md` sections.
2. Validate the declared upgrade ledger `docs/AP_UPGRADE_OBSERVATIONS.md` and
   revalidate every active entry at the current pin (§2.6).
3. Verify the repository gate, AP pin, `ap doctor`, `ap project check`, public
   `main`, the predecessor's publication/deployment evidence, and the NUC status
   through the canonical helper when NUC access is granted; otherwise carry the
   NUC state as not revalidated.
4. Read the predecessor whole's notes and reports, and the run map.
5. Revalidate this handout's material facts and record its Handout Revalidation
   Record in this whole's `00_notes.md` (§2.7).
6. Preserve the COOPERATOR's explicit selection of `timeline-complete-chronicle`.
   Present the restored state in his presentation profile; do not ask him to
   select a whole again. If a material contradiction requires a decision, ask
   exactly one.
7. Create this whole's `00_notes.md` at opening and record the Handout
   Revalidation Record there. The COOPERATOR owns the Meta Git commit.
8. Prepare the first Planner prompt for session `01`, exchange `01`,
   `fresh-worker-session`, `Native planning mode: required`, `Planning cycle:
   initial`, `Plan disposition: approval-gated`, implementation in the same
   session prohibited, `Post-plan implementation session: fresh-worker-session`,
   `Report persistence owner: assigned WORKER`, and direct-write report
   `01_report_00.md`. Archive it as `01_planning_00.md`.
9. Present the delivery capsule to the COOPERATOR and wait for him to deliver
   the prompt manually. Do not dispatch, do not use a subagent, and do not
   commit Meta. When the Worker report appears at `01_report_00.md`, read it
   back, reconcile it as a claim, and continue with the next complete prompt.
10. Freeze `00_notes.md` only at closure. Whole 01's rendered acceptance remains
    a carried Cooperator-owned item; record it as such, not as satisfied.
11. Do not open the deferred `upload-flow-polish` whole until the COOPERATOR
    confirms after this whole, unless he explicitly reorders.

The Meta directory is:

```text
/Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/
```

---

## 8. Readiness review of this handout

| Review | Result |
|---|---|
| Contradiction | The objective intentionally contradicts ADR-0083's approved-only Timeline membership; that is the decision this whole must explicitly supersede, not silently reinterpret |
| Omission | Whole 01's rendered acceptance is paused and carried; the new Timeline's exact visibility/status model is for the Planner, not this handout |
| Stale state | Repository/public `main` and NUC are observed at `b66ec8f`; revalidate. The NUC sudo timestamp is revoked; a later deployment needs a fresh Cooperator `sudo -v` |
| Authority | No mutation authority transferred; every Worker action needs a new complete prompt delivered manually by the COOPERATOR |
| Active mutation | None |
| Active Worker | None for this whole |
| Security boundary | Privacy, owner/admin/household visibility and administrator-controlled household publication must not widen; a fresh independent acceptance is likely |
| Strategic direction | ADR-0082 through ADR-0086 preserved except the explicitly superseded Timeline-membership rule; Gallery/Details freeze preserved |
| Next-step executability | Executable after Stage 1 verification, the Handout Revalidation Record, and the first archived Planner prompt |

Overall: **PARTIAL** — the COOPERATOR has selected the new whole and the
direction is clear, but the whole has not opened, the exact complete-Timeline
model is not planned, the NUC state must be revalidated, and whole 01's rendered
acceptance remains a carried Cooperator-owned item. This is a prepared handoff,
not current-state authority.

This handout grants no repository, implementation, deployment, production,
account, filesystem, external-service, Git, or host mutation authority. Verify
independently, then prepare the first Planner prompt for the COOPERATOR's
manual delivery.
