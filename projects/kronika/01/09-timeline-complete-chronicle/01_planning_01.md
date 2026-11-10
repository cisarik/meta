# Authoritative Worker prompt — Kronika whole 09, Worker session 01, exchange 02

Activation: this file is the exact issued Worker prompt for the logical whole
`timeline-complete-chronicle`. It is stored under the Meta filename mapping
`<worker-session>_<phase>_<meta-exchange-index>.md` as `01_planning_01.md`. The
matching terminal report is `01_report_01.md`.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: timeline-complete-chronicle
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: KRN-TCC-PLAN-01R — corrected initial plan-only — complete, visibility-aware Timeline chronicle on the existing Kronika record, media, research and preview foundations
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — the plan must reconcile a superseding product/privacy decision, a multi-table item model, owner/administrator/household visibility, a new main-page table/list, a read API and query plan, existing test pins, durable documentation owners, and the later acceptance/publication/NUC sequence
Recommended context capacity: approximately 1M tokens
Independence required: no (planning); the plan must recommend the later acceptance route
Sub-agents or internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Continuity anchor: terminal PARTIAL report 01_report_00.md for task KRN-TCC-PLAN-01, which stopped on a prompt-defect prerequisite before any plan existed
Authority renewal: prior planning authority expired; this exchange grants a complete new planning authority for the corrected initial plan
Evidence posture: non-independent; retained context is convenience, not authority
Repository and environment re-gating: required before any substantive planning
Conflict rule: stop on conflict between retained context and current repository evidence
```

Do not create or use subagents, Explore-style tasks, or internal delegation. One
accountable WORKER performs this planning exchange.

This is the **corrected initial Planner** for this logical whole. The first
exchange stopped on a prompt defect before any plan existed. This exchange keeps
`Planning cycle: initial`; it is not a targeted revision and it does not consume
a second planning cycle. The prior terminal report is retained as
`Prior planning report: 01_report_00.md`; its source observations are
preliminary context, not a plan and not authority.

This prompt declares native planning mode `required`; the delivery session must
have the client's actual native planning mode enabled before you begin. If it is
not enabled at your client boundary, stop before any work and return a short
`BLOCKED` report naming the missing client mode. This is a `current-worker-session`
renewal: first re-gate the repository and environment, confirm that the
continuity anchor matches this session's actual history, and stop on any
conflict between retained context and current repository evidence.

## Prompt-defect correction

The first prompt required a direct report write under `Native planning mode:
required` without naming the client completion route required by
`.ap/PROMPT_CONTRACTS.md#cooperator-delivery-and-trace-destination-record`
(P4). The Worker correctly stopped before producing a plan. This prompt corrects
that defect prospectively and preserves the blocked report.

The corrected completion route is stated in **Client completion route (P4)**
below. The client's Plan Mode write prohibition must not be bypassed. If the
client permits a write, use the direct-write path; if it does not, return the
complete exact report in the session for authorized persistence under the AP
Planner-Artifact Report Completion Repair route.

## Implementation-planning contract

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded technical planning for replacing the approved-only Timeline with a complete, visibility-aware, chronological overview of every item the signed-in identity may read, presented as a compact table/list with small media thumbnails: exact item model and aggregation, visibility and status matrices, read API and query plan, UI and accessibility, test and documentation changes, a new ADR that explicitly supersedes ADR-0083's Timeline-membership rule, the smallest coherent implementation slice, and the later acceptance/publication/NUC/rendered-acceptance sequence
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
```

## Planning record

```text
Planning cycle: initial
Prior planning report: 01_report_00.md
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

## Client completion route (P4)

This is the named client completion route for `Native planning mode: required`
with a direct-write report destination:

1. Keep the complete terminal report in the client's Plan output.
2. If, within this same unexpired grant, the client permits a file write after
   the plan output is complete, write the exact report to
   `/Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/01_report_01.md`
   if and only if that path is absent, then read the complete file back and
   verify content, identity and path. Do not use another path.
3. If the client still prohibits the write, do **not** bypass Plan Mode, switch
   modes, or use another tool to evade the control. Return the complete exact
   report in the session and state exactly:
   `Report persistence: client-prohibited; complete exact content returned for authorized persistence`.
   Do not claim saved-file readback. The Cooperator or an authorized persister
   will persist the exact content under the AP Planner-Artifact Report
   Completion Repair route, preserving this terminal report's status and
   identity.
4. Do not implement, do not approve the plan, and do not treat the Plan output
   as an accepted decision. The plan remains approval-gated.

The prior `01_report_00.md` is preserved unchanged. This exchange's report is
`01_report_01.md`; the report path was absent when this prompt was prepared.

## Goal

Produce one decision-complete implementation plan for this bounded whole:

> Make the Timeline the complete, chronological, visibility-aware overview of
> everything added to Kronika that the signed-in identity may see, including
> media, Search/Research records and other catalog items the identity may read,
> and including private, unanalysed, unfinished and unpublished items where the
> identity is the owner or an application administrator. Present the result as a
> compact table/list with small media thumbnails, not as a Gallery. Preserve
> Gallery as a separate media browser, personal History as the research/question
> history, and administrator-controlled household publication.

The plan must be executable by a fresh Implementation Worker under a new
complete grant. It must define the path through implementation, verification,
acceptance, publication, routine NUC refresh and the Cooperator's rendered
acceptance. It is a plan, not an implementation, not an acceptance, and not a
second design authority.

## The decision this whole must obtain

ADR-0083 currently says, in its `Shared Timeline and Gallery` section:

> The main page is the Timeline. It contains only administrator-approved
> records, including when the viewer is an administrator.

That Timeline-membership sentence is the decision this whole is explicitly
asked to supersede. The Planner must propose a new accepted ADR that supersedes
that sentence and only that sentence, with a precise statement of the new
Timeline semantics and the migration from the current approved-only list. The
new ADR must preserve the other ADR-0083 principles:

- modular research providers;
- personal History as a separate view of the caller's questions, answers,
  unfinished work and complete Research reports;
- Gallery as a separate media working view with the existing shell, CSS,
  controls and player;
- administrator approval as the household-publication gate;
- owner/administrator private reading, with no household widening;
- internet publication disabled;
- the existing preview route, audience policy, quarantine, validation and
  identity model.

Do not silently reinterpret ADR-0083. Do not edit an accepted ADR in place. The
new decision must be explicit, durable and owned by the appropriate document.
The Planner must identify every downstream restatement that must change,
including at least `AGENTS.md` product boundaries, `SPEC.md`, `SECURITY.md` and
`README.md`, and any other exact owner it finds.

## Verified current state

Verified read-only by the ORCHESTRATOR before this prompt was issued. Re-verify
the repository gate; do not trust this section blindly.

```text
Repository identity: https://github.com/cisarik/kronika
Repository checkout topology: standalone checkout
Working directory: /Users/agile/Projects/kronika
Exact baseline: b66ec8f50860ace624f6be1fd3ad63f521edcd33
Expected branch: main
Expected HEAD: b66ec8f50860ace624f6be1fd3ad63f521edcd33
Public main: b66ec8f50860ace624f6be1fd3ad63f521edcd33 (git ls-remote verified)
Working tree: clean
Containing-repository .ap gitlink: d7023cf037f6d17885c3ede5c04812c61640da50
Submodule HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
AP public main: d7023cf037f6d17885c3ede5c04812c61640da50
Governing AP variant: stable
ap doctor: PASS
ap project check --baseline b66ec8f50860ace624f6be1fd3ad63f521edcd33: PASS
  (standard sanitized-environment warning for inherited SSH_AUTH_SOCK and PATH)
```

Predecessor whole state, recorded in its frozen notes and reports:

```text
Whole 01: timeline-and-history-media-thumbnails
E2 acceptance-PASS at b66ec8f after one pre-acceptance correction
Publication-PASS on public main at b66ec8f
Deployment-PASS recorded at b66ec8f (NUC not revalidated by this whole)
Rendered acceptance paused: the approved-only Timeline did not match the
  intended complete chronicle; the COOPERATOR chose route A (this whole)
Whole 01 preview implementation, safe locator and test lessons are retained
```

NUC state was not revalidated because no NUC access was granted to this
Orchestrator. The recorded post-deployment values are:

```text
layout: canonical
active_release: b66ec8f50860ace624f6be1fd3ad63f521edcd33
web_release: b66ec8f50860ace624f6be1fd3ad63f521edcd33
capture_release: 5b86d896b3ea03f89fef2c90f7af2c121d0ef915
service_active: active
database_revision: 0035
backup_restore_readiness: ready
```

Treat those as unverified recorded evidence. Do not contact the NUC in this
planning exchange.

The Planner must independently re-verify HEAD, branch, clean tree, submodule
equality, `ap doctor` and `ap project check` before relying on any measurement.
Report any contradiction with this prompt and its cause.

## Starting evidence map — hypotheses to verify, not conclusions

The Orchestrator inspected these read-only; the Planner must re-measure and
correct the map.

- Timeline API and service: `src/kronika/adapters/api/records_api.py`
  (`/api/timeline`, `/api/my/records`, `_summary_payload`, `_page_payload`,
  `_list_filters`); `src/kronika/application/records.py`;
  `src/kronika/application/ports/records.py`;
  `src/kronika/infrastructure/persistence/record_repository.py`
  (`_list`, `_summary_labels`, `_summary_preview_locations`).
- Current Timeline membership: `RecordService.list_timeline` →
  `SqliteRecordRepository.list_timeline` → `_list(... timeline_only=True)`,
  filtering `visibility = family`, non-null `approved_projection_json` and
  non-null `timeline_entered_at_ms`, ordered by entry time descending then ID.
- Access decisions: `src/kronika/domain/record_access.py`
  (`decide_bound_read`, `timeline_includes`, `scope_for_identity`);
  `src/kronika/application/content_publication.py`
  (`ContentAudiencePolicy.read_decision`);
  `src/kronika/adapters/api/content_audience_api.py`.
- Media and attribution: `logical_media`, `physical_media_locations`,
  `media_metadata`, `media_analysis_runs`, `media_content_publications` in
  `src/kronika/infrastructure/persistence/catalog_schema.py`;
  `src/kronika/infrastructure/persistence/media_attribution_repository.py`
  (`list_workspace_media`, `_attributed_media_ids`, contribution stamps);
  `src/kronika/infrastructure/persistence/media_catalog_repository.py`
  (`catalog_scope_predicate` use); `src/kronika/adapters/api/media_catalog_api.py`;
  `src/kronika/adapters/api/workspace_media_api.py`.
- Records and documents: `kronika_records`, `kronika_documents`,
  `kronika_approved_media`, `kronika_approved_media_tags`,
  `kronika_approved_media_locations` in `catalog_schema.py`;
  `src/kronika/domain/records.py`; the record repository's approval and
  projection methods.
- Research: `research_requests` in `catalog_schema.py`;
  `src/kronika/adapters/api/research_api.py`; the research request repository;
  `kronika_documents` and `kronika_records` creation on completion.
- Preview: `src/kronika/adapters/api/gallery_preview_api.py`;
  `src/kronika/application/gallery_preview.py`;
  `src/kronika/application/gallery_preview_backfill.py`;
  `src/kronika/adapters/api/tailscale_ingress.py` route policies; the
  public-published composition and preview route.
- Web shell: `src/kronika/adapters/api/web/index.html` Timeline/History
  sections; `src/kronika/adapters/api/web/app.js` (`kronikaLoadTimeline`,
  `kronikaRenderCards`, `kronikaAttachCardPreview`, `kronikaLoadHistory`,
  list controllers, preview lifecycle, route/view state);
  `src/kronika/adapters/api/web/styles.css` (`.kronika-card`, `.kronika-grid`,
  preview rules).
- Tests: `tests/contract/test_records_api.py`,
  `tests/integration/persistence/test_kronika_record_repository.py`,
  `tests/contract/test_kronika_approved_projection.py`,
  `tests/contract/test_kronika_access_inventory.py`,
  `tests/contract/test_gallery_preview_api.py`,
  `tests/contract/test_local_web_application.py`,
  `tests/kronika_ui.test.js`, `tests/contract/test_research_requests_api.py`,
  and any other exact Timeline, History, media-list, preview or route-policy
  tests found by search.
- Durable documents: `AGENTS.md`, `SPEC.md`, `SECURITY.md`, `README.md`,
  `PRODUCT.md`, `ROADMAP.md`, `SERVER.md`, `GALLERY.md`, `DEVELOPMENT.md`,
  `docs/adr/README.md`, ADR-0082 through ADR-0086,
  `docs/KRONIKA_ACCESS_INVENTORY.md`, `docs/UX_AUDIT.md`.
- Historical evidence: the predecessor whole's `00_notes.md`,
  `01_report_00.md`, `02_report_00.md`, `02_report_01.md`; the closed 00
  whole's `00_notes.md` and handout §9.2; the run map; this whole's frozen
  handout. These are historical claims and context, not current authority.

Measured facts the Planner must verify rather than assume:

- Production code in this checkout does not call `bind_media_record`; only
  tests and the repository port reference it. Media rows in `logical_media`
  therefore may exist without a `kronika_records` row. The complete Timeline
  must be able to show an unanalysed media item without inventing a record.
- Unbound media attribution comes from upload sessions/publications, YouTube
  acquisition claims and X assets/claims; bound media ownership comes from
  `kronika_records.owner_login_key`. Some media may have no attribution at all.
- A saved Search/Research request has both a `research_requests` row and a
  `kronika_records` row plus a `kronika_documents` row. A union of sources must
  not double-count it.
- The current Timeline is approved-family only for every caller, including
  administrators. The current shell Timeline is a card grid, not a table/list.
- Whole 01 added a nullable `preview_location_id` to `/api/timeline` and
  `/api/my/records`, with approved locations for Timeline and current locations
  for personal History; its route, audience policy and fallback behavior are
  reusable but its Timeline-membership scope is superseded.

## Fixed decisions and the decision to supersede

Treat as fixed:

- One Kronika identity in `cisarik/kronika` on `main`; the former capture
  repository remains separate. ADR-0082, ADR-0084, ADR-0085 and ADR-0086 remain
  authoritative.
- Personal History remains a separate view of the caller's questions, answers,
  unfinished work and complete Research reports.
- Gallery remains a separate working media view with the existing shell, CSS,
  controls and player. The accepted Gallery and Details MVP visual behavior
  remains frozen except for a concrete defect.
- Administrator approval remains the household-publication gate. Owners do not
  publish directly to the shared household page. Withdrawal removes the shared
  card and keeps personal history.
- Private records remain visible only to their owner and authenticated
  application administrators, never to other ordinary household members.
  Administrator read-all is application content only and grants no host,
  credential or browser-profile access. A client-supplied identity is not
  owner authority.
- Internet publication remains disabled; the public composition stays off and
  must not expose the new Timeline or its records.
- The existing preview route, audience decision, safe locator, GET-never-
  generates rule, quarantine, validation and identity model are preserved.
- No new media pipeline, provider call, acquisition flow, upload backend,
  secrets, dependency, host mutation or deployment-system change is in scope.
- The deferred `upload-flow-polish` whole and the other provisional run-map
  entries are not in scope.
- Rendered UI/UX acceptance belongs to the COOPERATOR and requires the exact
  accepted code on public `main` refreshed onto the NUC first.

The decision to supersede is the approved-only Timeline membership in
ADR-0083 and every downstream restatement of it. The Planner must state the old
rule, the new rule, the reason, the migration, the affected owners and the
compatibility consequences. It must not weaken the other privacy, publication
or audience rules while doing so.

## What the plan must answer with repository evidence

1. **Item model.** What exactly is an "item" in the requested complete
   Timeline? Map `logical_media`, `physical_media_locations`, `media_metadata`,
   `media_analysis_runs`, `kronika_records`, `kronika_documents`,
   `research_requests`, approvals, withdrawal, publication and attribution
   rows. Which entities exist before analysis, and how can the Timeline show an
   unanalysed media item without inventing a record? Define the union, the
   deduplication key, the stable item identity, the source precedence when a
   media item is both a `logical_media` row and a bound record, and the
   treatment of unattributed media. Do not create a second Gallery and do not
   create a synthetic record merely to fill the list.
2. **Visibility matrix.** State the exact matrix for owner, application
   administrator, other household member and unauthenticated caller across
   media, Search/Research records, unfinished requests and legacy/published
   media. Which existing `decide_bound_read`, `ContentAudiencePolicy`,
   `scope_for_identity`, record visibility and approved-projection rules can be
   reused? Where must the new Timeline not widen access? Cover list, detail,
   preview, playback, download and direct APIs.
3. **View boundaries.** How does the new Timeline coexist with Gallery and
   personal History? Which view owns media browsing, which owns
   research/question history, and which owns the complete chronological
   overview? Avoid a second Gallery, duplicate navigation, and a second
   semantic owner. Define what a Timeline row links to for each item type.
4. **Status and visibility vocabulary.** Define the exact status vocabulary and
   visual treatment for private, shared/approved, household-published,
   unanalysed, analysing, failed, unfinished, withdrawn and
   public-published-disabled items, and for the research lifecycle states that
   already exist. Map every display label to the exact persisted state and to
   the identity that may see it. Status and visibility must be distinct,
   accessible, and not conveyed by colour alone.
5. **Read API and query plan.** Define the exact read API shape and query plan:
   endpoint(s), filters, search, status/visibility filters, stable ordering,
   pagination, total counts, response fields and nullability. How many queries
   per page? How are media previews and non-media rows batched without N+1?
   Which indexes are needed? How are tie-breakers, time zones/epoch values and
   mixed media/document dates handled? Decide whether to evolve `/api/timeline`
   or introduce a new endpoint, and justify the compatibility and route-policy
   consequences.
6. **Table/list UI.** Define the exact desktop and narrow-screen layout:
   columns, small thumbnails, kind/status/visibility indicators, title/date
   treatment, filters, search, pagination, empty/loading/error states,
   keyboard paths, focus behavior, screen-reader names, inert text and
   responsive behavior. Which existing CSS and UI-test pins must change? Keep
   Gallery and Details frozen. The result must be a compact chronological
   table/list, not a card grid that duplicates Gallery.
7. **Tests.** Which existing tests pin the approved-only Timeline, the record
   list APIs, the preview route, the Gallery/History presentation and the
   shell? Which must change, which must stay, and what new causal tests prove
   the new visibility and aggregation behavior? Cover owner, administrator,
   other household member, unauthenticated caller, private, approved,
   withdrawn, unanalysed, analysing, failed, unfinished, saved, legacy-published
   and cross-source deduplication. Name exact test files and test identities
   after inspection. Include route-inventory tests if a route or policy
   changes.
8. **Durable documents.** Which durable documents own the new decision: a new
   ADR superseding ADR-0083's Timeline-membership sentence, `SPEC.md`,
   `SECURITY.md`, `README.md`, `AGENTS.md`, `DEVELOPMENT.md`, `GALLERY.md`, the
   ADR index, or another exact owner? Give each file's exact current claim, the
   exact replacement claim, the section/heading, and the validation. Do not
   create a second semantic owner. Do not edit accepted ADRs in place.
9. **Acceptance route.** What is the exact acceptance route? This change
   supersedes a core product/privacy decision and the main page. Recommend
   fresh independent acceptance for the visibility/authorization surface
   unless the actual boundary justifies otherwise, and justify from the
   boundary. Define the evidence tier, control matrix, independence, correction
   budget, publication verification and Cooperator rendered acceptance.
10. **Smallest safe slice.** What is the smallest safe implementation slice?
    If the full complete chronicle cannot be one bounded candidate, propose the
    smallest coherent first slice and the exact follow-on slices, with no fake
    partial acceptance. Each slice must be independently acceptable and must
    preserve the complete-chronicle objective. State what the first slice does
    not yet deliver and why that is honest.
11. **NUC refresh and rendered acceptance.** What is the exact later NUC refresh
    and Cooperator rendered-acceptance sequence, including a fresh Cooperator
    `sudo -v`, exact release SHA, `status` → `check --release <sha>` → explicit
    authority → `deploy --release <sha> --yes`, post-deploy checks, rollback and
    the statement that a check never deploys automatically? Keep NUC contact
    out of this planning exchange; define the later grant.
12. **Whole 01 reuse.** What did whole 01 change in the preview helper, list
    controllers, CSS and tests that this whole should reuse, preserve or
    deliberately replace? Name exact paths and functions. Do not reopen whole
    01, rewrite its notes or reports, or treat its approved-only Timeline rule
    as a fixed constraint.

## Deliverables

### 1. Re-measured current-state map

A file-by-file and function-by-function map of:

- the exact Timeline list path, filters, ordering and response fields;
- the exact media, record, research, approval and attribution tables and their
  relationships, including which rows exist before analysis;
- the exact audience and preview decision path for owner, administrator,
  household member and unauthenticated caller;
- the exact shell Timeline, History and Gallery render paths and their test
  pins;
- the exact durable documents that currently state or restate the
  approved-only rule;
- the exact whole 01 preview additions that are reusable.

Report contradictions with this prompt explicitly.

### 2. Proposed decision and migration

A decision-complete proposed ADR, including:

- proposed ADR number (verify the next free number; `0087` is the apparent next
  number) and title;
- status `Proposed` for the plan, with the exact acceptance event that would
  make it `Accepted`;
- the precise superseded sentence and the precise new Timeline rule;
- the item model, visibility model and status model at decision level;
- the migration from the current approved-only list, including compatibility,
  historical rows, withdrawal, reapproval, saved research, legacy publication
  and no-data-rewrite behavior;
- every durable document that must be updated and the exact claim it owns;
- consequences and rejected alternatives.

The plan may propose the ADR text, but it must not create or edit the ADR file
in this exchange.

### 3. Exact current and proposed API contract

For each affected endpoint: method, path, capability/identity requirement,
query parameters, response shape, nullability, error codes, cache headers,
ordering, pagination and total semantics. Include the exact route-policy and
access-inventory consequences. Define how list responses avoid answer text,
paths, cache state, filesystem data and unauthorized fields.

### 4. Exact query and performance plan

The SQL/read strategy per page, including source unions, deduplication,
audience predicates, deterministic ordering, count strategy, preview locator
batching, index needs and expected query count. State the page-size and maximum
limits. Prove how the design avoids N+1 detail reads and per-item filesystem
probes. If a schema change or new index is proposed, justify it and define the
migration and rollback.

### 5. Exact UI and accessibility specification

Desktop and narrow-screen layout, columns/rows, thumbnail slot, badges, filters,
search, pagination, empty/loading/error states, keyboard and focus behavior,
screen-reader names, inert text and responsive rules. Name the exact files and
test pins that change. Preserve the Gallery and Details freeze.

### 6. Exact changed-path allowlist

Every repository path the implementation would change, with a one-line purpose,
and the negative allowlist (paths that must not change). If the design requires
a new test file or documentation file, name it exactly. Include the proposed
ADR path and the ADR index path if the decision is accepted.

### 7. Test and validation plan

Existing tests to preserve, existing tests to update with reason, new causal
tests, exact commands through the declared routes, and the evidence tier for
each claim. Include JavaScript and Python routes separately. Identify the exact
tests that pin the approved-only Timeline and explain why each change is a
deliberate product decision, not a weakened expectation.

### 8. Acceptance control matrix

```text
Claim ID | Surface | Exact claim (positive and negative) | Evidence type | Exact test/command/observation | Evidence tier | Acceptance owner | Pass criteria | Current gap
```

At minimum cover: owner/private media; administrator all-content read; other
household member approved-only; unauthenticated denial; unanalysed media;
analysing; failed; unfinished research; saved research; withdrawn; approved;
legacy published; cross-source deduplication; stable ordering; pagination and
totals; preview locator and fallback; no answer text or private paths; no
visibility widening; route inventory; accessibility; frozen Gallery/Details;
no secret or host-value leakage.

### 9. Acceptance route recommendation

Recommend the exact route, including whether fresh independent acceptance is
required for the visibility/authorization surface, the evidence tier, the
primary acceptance and correction budgets, and the Cooperator's rendered
acceptance. Justify from the actual boundary. The Planner does not perform or
claim acceptance.

### 10. Documentation-promotion inventory

For each target: exact file, current gap, exact claim to add or replace,
proposed section/heading, validation, and owner. Include the new ADR, the ADR
index, `AGENTS.md`, `SPEC.md`, `SECURITY.md`, `README.md`, `DEVELOPMENT.md`,
`GALLERY.md`, and any other exact owner. Do not create a second semantic owner.

### 11. NUC refresh and rendered-acceptance sequence

The exact later sequence, not an execution in this exchange:

- preconditions: accepted commit on public `main`, matching `.ap` pin, clean
  checkout, fresh Cooperator `sudo -v`, backup readiness, no active mutation,
  exact release SHA;
- `kronika-release status` → `check --release <sha>` → explicit authority →
  `deploy --release <sha> --yes`;
- schema-jump handling through the documented `migration-required` (exit 13)
  continuation;
- post-deploy checks and rollback path;
- Cooperator rendered-acceptance checklist for the complete Timeline on the
  NUC, including private/approved/unanalysed/unfinished/failed/withdrawn,
  preview fallback, keyboard and narrow-screen cases;
- the statement that a check never deploys automatically.

### 12. Execution sequence and budgets

The smallest safe sequence after plan approval: implementation, verification,
acceptance, publication, NUC refresh, rendered acceptance and closure. Name
which steps may share a session, which require a fresh session, and why. Do not
create an audit-of-an-audit or a second automatic correction.

### 13. Open decisions, risks and protocol friction

List every question requiring an Orchestrator or Cooperator decision. Map the
forward risks C1-C8 from the handout. Name residual risks and owners. Add a
short `AP protocol friction observed` section (maximum five bullets) with
measured evidence only; it is not an AP change request in this exchange.

## Authority

```text
Positive authority: read-only inspection inside /Users/agile/Projects/kronika,
  including .ap at its pinned commit; optional read-only public verification of
  https://github.com/cisarik/kronika.git through git ls-remote when available;
  read-only inspection of
  /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/
  (this prompt and 00_notes.md), the run map
  /Users/agile/meta/projects/kronika/01/00_RUN_MAP.md, the predecessor 01
  whole's frozen notes and named reports, and the closed 00 whole's 00_notes.md
  and handout §9.2; read-only inspection of the named Meta AP_DEFECTS.md and
  AP_DESTILLED.md entries as consumer evidence; repository gates through
  ./.ap/ap doctor and ./.ap/ap project check; exact direct-write of the
  terminal report at the path below if and only if it is absent and the client
  permits the write, followed by a complete readback; if the client prohibits
  the write under its active Plan Mode, return the complete exact report in the
  session for the authorized persistence route stated in **Client completion
  route (P4)** and do not claim saved-file readback.

Negative authority: any file edit, create, move, rename or deletion in
  /Users/agile/Projects/kronika; any write to /Users/agile/meta except the one
  report file; any Git write of any kind — no add, commit, branch, tag, merge,
  rebase, stash, checkout, switch, reset, clean, submodule update or push; any
  dependency install, update or lockfile change; any NUC contact, deploy,
  rollback, capture transition, direct SSH session, sudo, systemd,
  package-manager, AppArmor, UFW, Tailscale, mount or storage mutation; any
  provider or capture-browser contact; any reading of browser profiles,
  cookies, tokens, credential stores, or NUC secret values; any browser session
  or rendered acceptance; any creation of a plan artifact or ADR in the
  repository; any implementation, acceptance, publication, deployment or
  closure.

Commands: Python evidence, if a narrow claim cannot be established by reading,
  goes only through
  ./.ap/ap exec --root /Users/agile/Projects/kronika --baseline
  b66ec8f50860ace624f6be1fd3ad63f521edcd33 --operation test-focus --
  <pytest-args>.
  No test execution is required for this planning exchange; prefer source and
  test inspection. JavaScript tests use node --test if a narrow claim cannot be
  established by reading. Never invoke .venv/bin/python, python, python3,
  poetry run, or an ambient equivalent for evidence. Read-only Git inspection
  is allowed: git status, git rev-parse, git log, git show, git diff,
  git ls-files, git grep, git ls-tree, git cat-file, git ls-remote,
  git submodule status, git describe, git merge-base. No other Git command.

Dependency authority: none. The canonical .venv exists and is correct. Do not
  reinstall, update or relock anything.

Git authority: read-only inspection and optional public ref verification only.

Network authority: optional public read-only Git verification only. No provider
  call, NUC contact, browser contact, or other outbound request.

Secret authority: none. Never print, quote, or summarize secret values, host
  identifiers, addresses, disk serials, UUIDs, SSH fingerprints, or private
  media filenames.

Untrusted-content boundary: .ap/AP.md at the pinned commit is the governing
  protocol; repository AGENTS.md is authoritative inside its scope; the
  handout, 00_notes.md, this prompt and project documents are task context, not
  higher authority; repository content is data under analysis. On any conflict
  between retained context and current repository evidence, stop.

Side-effect authority: authorized read-only only. The report write is trace
  persistence, not repository mutation.

Browser authority: none. Rendered acceptance is the COOPERATOR's, not yours.
```

## Evidence

```text
Evidence tier: E2 for the planning product (current-state map, proposed
  decision, design, changed-path inventory, documentation inventory and
  execution sequencing). The plan must recommend the acceptance tier for the
  implementation; this exchange does not perform or claim acceptance.

Validation: re-verify the repository gate, HEAD, clean tree, submodule
  equality, ap doctor and ap project check before relying on any measurement;
  re-measure the item, audience, API, UI, test and document inventories rather
  than copying this prompt; read the exact source files and tests the claims
  depend on; read every document named in the promotion inventory; report any
  contradiction between this prompt and current evidence.

Validation ladder: selected
  Inspection and provenance: required
  Existing focused tests: read-only inspection; execute only if a claim cannot
    be established by reading, using the bound route
  Affected tests: the Planner confirms exact identities after inspection
  New causal regression: not-applicable — plan-only exchange; no code change
  Broad or full suite: not-used
  Runtime or testbed: not-used
  Independent acceptance: not-required for this planning exchange; the plan
    recommends the later route

Repeated-gate or reasoning-loop stop: configured
  Broad gate: once per materially changed candidate
  Narrow before re-broad: required
  Unchanged hypothesis, candidate, and failing gate: not-progress
  Escalate only on: named missing evidence the higher profile must solve
  Downgrade after: convergence or named risk removal
  Cost cannot falsify evidence: yes
```

## Finishing

```text
Stopping conditions: stop without improvising if the client has no native
  planning mode enabled; if this is not a fresh session for this whole; if
  HEAD, the branch, the remote, or the tree does not match the verified state;
  if the submodule is not at the pinned commit; if ap project check --baseline
  does not pass; if you would need any mutation, NUC contact, browser session,
  provider call, or secret access to answer a question; if you find a genuine
  cross-cutting contradiction that needs a Cooperator or Orchestrator decision
  rather than a plan; if context pressure reaches the point where a bounded
  rotation is cheaper than a degraded plan; or if the exact report path already
  exists, including an empty file.

Completion: one terminal report containing the full decision-complete plan, not
  a summary of it and not a second implementation.

Required report sections: the standard report core and header (including the
  coordinate block: Logical whole identity, Worker session ordinal, Worker
  exchange ordinal, and echo of Persistent role identity, Worker session target,
  Native planning mode, Worker session profile, Task identity); the re-measured
  current-state map; the proposed decision and migration; the exact current and
  proposed API contract; the exact query and performance plan; the exact UI and
  accessibility specification; the exact changed-path allowlist; the test and
  validation plan; the acceptance control matrix as a table; the acceptance
  route recommendation; the documentation-promotion inventory; the NUC refresh
  and rendered-acceptance sequence; the execution sequence and budgets; open
  decisions; C1-C8 risk mapping; AP protocol friction (maximum five measured
  bullets); your own re-measured inventory with deltas against this prompt and
  the reason for any difference; the test baseline evidence actually used; one
  smallest next step; and the orchestration critique.

Report destination: direct-write
  /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/01_report_01.md
  if and only if it is absent and the client permits the write. Read the
  complete file back and verify content, identity and path before the short
  separate completion notice. If the client prohibits the write under Plan
  Mode, use the exact-content return route in **Client completion route (P4)**
  above; do not bypass the control, switch modes, or use another tool to evade
  it. Do not write any other file. Do not create a plan artifact or ADR in the
  repository.

Report justification: new-evidence

Authority expiry: on submission of the terminal planning report, all planning
  authority expires. Implementation in this session is prohibited. A later
  execution authority event is an explicit ORCHESTRATOR prompt with Native
  planning mode: not-used.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
```

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification.

Finish the terminal report with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

## Mandatory reading

Read the exact owners for the claims you plan; do not read the whole protocol
when a bounded owner is sufficient.

- `.ap/AP.md` at the pinned commit: §2 Roles; §3 Instances, Sessions, and Worker
  Session Profiles (Worker Session Target, Orchestration Planning and
  Implementation Planning, Plan-to-Execution Gate, Communication Routing); §5
  Task Authority; §6 Adaptive Orchestration Lifecycle; §7 Orchestrator
  Responsibilities; §12 Validation and Public Verification; §13 Artifact
  Lifecycle; §14 Session Rotation and Dynamic Prompts; §15 Fresh-Slice
  Implementation and Diagnostic Closeout; §17 Compact Communication; §19
  Anti-Patterns (skim); and the Finite Convergence Contract.
- `.ap/AP_WORKER.md` in full: Worker session target, bounded authority, and
  reporting.
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header; Convergence Records
  (Planning Record, Implementation Authority Record, Acceptance and Correction
  Record, Phase Result and Closure Record); Common Worker Task Fields;
  Repository Checkout Topology Contract; Worker Session Target Contract; Worker
  Exchange Identity and External Trace Contract; Cooperator Delivery and Trace
  Destination Record; Mutation Axes Record; Validation Ladder Record;
  Pre-Existing Failure Classification Contract.
- `.ap/AP_ORCHESTRATOR.md` reference-on-demand: Decision Table; Activated
  Surface Decisions; Security Risk Routing; Artifact and Ledger Governance;
  Run-Scoped Orchestration.
- `AGENTS.md` at the repository root, including its managed AP block, Security
  Boundaries, Product Boundaries, Cursor Worker Execution Boundary, Worker
  Execution, and Git and Lifecycle.
- `docs/WORKER_EXECUTION_CONTRACT.md`: the Cursor/AppImage execution boundary,
  canonical `./.ap/ap exec` route, NUC SSH gate, sudo lifecycle, and test
  invocation.
- `docs/adr/README.md` and ADRs 0082, 0083, 0084, 0085 and 0086.
- `README.md`, `PRODUCT.md`, `SPEC.md`, `ROADMAP.md`, `SECURITY.md`, `SERVER.md`,
  `GALLERY.md`, `DEVELOPMENT.md`, `docs/KRONIKA_ACCESS_INVENTORY.md` and
  `docs/UX_AUDIT.md` for the living prose and accepted limits you must preserve.
- `docs/AP_UPGRADE_OBSERVATIONS.md`.
- `src/kronika/adapters/api/web/app.js` relevant regions: `kronikaRenderCards`,
  `kronikaAttachCardPreview`, `kronikaLoadTimeline`, `kronikaLoadHistory`,
  `kronikaCardTitle`, `kronikaKindLabel`, the list controllers, preview
  lifecycle and route/view state; `src/kronika/adapters/api/web/index.html`
  Timeline and History sections; `src/kronika/adapters/api/web/styles.css`
  `.kronika-card`, `.kronika-grid` and preview rules.
- `src/kronika/adapters/api/records_api.py`; the records service, port and
  repository; `src/kronika/domain/record_access.py`;
  `src/kronika/application/content_publication.py`;
  `src/kronika/adapters/api/content_audience_api.py`;
  `src/kronika/adapters/api/gallery_preview_api.py`;
  `src/kronika/adapters/api/tailscale_ingress.py` route policies; the
  public-published composition and preview route.
- `src/kronika/infrastructure/persistence/catalog_schema.py` and the media,
  records, research and attribution repositories named above.
- `tests/contract/test_records_api.py`,
  `tests/integration/persistence/test_kronika_record_repository.py`,
  `tests/contract/test_kronika_approved_projection.py`,
  `tests/contract/test_kronika_access_inventory.py`,
  `tests/contract/test_gallery_preview_api.py`,
  `tests/contract/test_local_web_application.py`,
  `tests/kronika_ui.test.js`,
  `tests/contract/test_research_requests_api.py`, and any other tests found by
  exact search for Timeline, History, media-list, preview and route policies.
- `/Users/agile/meta/projects/kronika/01/00_RUN_MAP.md`;
  `/Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/00_handout.md`
  and `00_notes.md`;
  `/Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/00_notes.md`,
  `01_report_00.md`, `02_report_00.md` and `02_report_01.md`;
  `/Users/agile/meta/projects/kronika/01/00-ux-refresh-acceptance-and-promotion/00_notes.md`
  and handout §9.2.
- `/Users/agile/meta/AP_DEFECTS.md` §0.0, D-17b, D-19, D-20 and D-21;
  `/Users/agile/meta/AP_DESTILLED.md` §17. These are citable consumer evidence,
  not rule sources. The governing AP owns every rule.

## Communication

Worker prompts, the report, and any plan text are professional English. Do not
use Czech or Slovak in repository, Meta, or report artifacts. The Cooperator's
chat language is separate and governed by the project rules.

## Activated surface annexes

### External trace and delivery

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
Downloadable prompt filename: 01_planning_01.md
Destination path: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/
Report filename: 01_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/01_report_01.md
```

The report write is trace persistence, not repository mutation. If the report
path exists, including an empty file, stop `BLOCKED` without overwriting it.
The verified parent directory exists. Do not create a placeholder or use another
path. The direct-write route applies only if the client permits the write under
its active Plan Mode. If it does not, use the exact-content return route in
**Client completion route (P4)**; the Cooperator or an authorized persister will
then store the exact content under the AP completion route. Do not claim
saved-file readback unless the file was actually written and read back.

### NUC and deployment (read-only planning; no contact)

```text
Routine NUC release-update entry point: deploy/ubuntu/kronika-release (Fish
  wrapper) plus deploy/ubuntu/kronika_release.py (standard library only).
This planning exchange: no NUC contact, no SSH, no sudo, no kronika-release,
  no deploy, no rollback, no systemd, no package manager, no AppArmor, no UFW,
  no Tailscale, no mount or storage mutation.
Last observed NUC state (NOT revalidated): active_release and web_release
  b66ec8f50860ace624f6be1fd3ad63f521edcd33; capture_release
  5b86d896b3ea03f89fef2c90f7af2c121d0ef915; layout canonical; service_active
  active; database_revision 0035; backup_restore_readiness ready.
The later deployment grant, not this plan, must verify the then-current NUC
  state, public main, exact release SHA, fresh Cooperator sudo timestamp and
  rollback. A predecessor deployment revoked the sudo timestamp with sudo -K;
  a later deployment needs a fresh Cooperator sudo -v.
Deployment never follows automatically from a check. Schema jumps use the
  documented migration-required (exit 13) continuation.
```

### AP upgrade ledger

```text
Project-declared ledger: docs/AP_UPGRADE_OBSERVATIONS.md
Entry: consumer-declared-execution-and-capability-route-binding
Entry state: accepted
Entry authority: non-authorizing
Last revalidated against: 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26
  (ancestor of the pinned d7023cf)
Closure action: retain-active
Implementation task grant: none — this planning exchange does not change,
  revalidate, or implement the ledger entry.
```

### Security and audience boundary

The plan must prove, with exact route and service evidence, that every Timeline
item and every preview, detail, playback or download link is subject to the same
audience decision as the item itself. Owner, administrator, household and
unauthenticated cases are acceptance-matrix items, not implementation details.
The new Timeline must not turn administrator read-all or owner access into
household visibility. It must not turn the Gallery/Details freeze into a
redesign. If the design changes the preview route, the audience guard, a
capability, a route policy or the record/media visibility model, mark it as a
security-boundary change and recommend fresh independent acceptance. This
planning exchange maps the claims; it does not perform a security audit.

## Visible delivery capsule

```text
🟡 Ready for delivery
Recipient: Planner · current-worker-session · manual
Continuity: Worker session 01, exchange 02 — corrected initial Planner
Recommendation: High · approximately 1M tokens
Client: Native Plan Mode ON
Completion route: Plan output plus exact-content return if the client prohibits the report write
Prompt: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/01_planning_01.md
Report: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/01_report_01.md
Archival: wait-for-report
```
