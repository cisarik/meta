# Authoritative Worker prompt — Kronika whole 09, Worker session 02, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`timeline-complete-chronicle`. It is stored under the Meta filename mapping
`<worker-session>_<phase>_<meta-exchange-index>.md` as `02_preflight_00.md`. The
matching terminal report is `02_report_00.md`.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: timeline-complete-chronicle
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Worker-Executed Preflight
Phase: Preflight
Task identity: KRN-TCC-PREFLIGHT-01 — read-only E3 preflight of the accepted complete Timeline chronicle plan
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — read-only E3 preflight of a privacy/authorization boundary, a multi-source read union, test side effects and deployment rollback
Recommended context capacity: approximately 1M tokens
Independence required: no (preflight; the later acceptance is fresh independent)
Sub-agents or internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
```

Do not create or use subagents, Explore-style tasks, or internal delegation. One
accountable WORKER performs this preflight.

This is a fresh Worker session `02`. The Planner session `01` authority expired
with its terminal report. Do not assume retained Planner context and do not
accept any prior prompt as current authority. This exchange is a read-only
preflight. It does not implement, accept, publish, deploy or close. A separate
complete implementation prompt follows only after this preflight reports PASS.

This prompt declares native planning mode `not-used`; the delivery session must
have the client's native planning mode disabled or absent before you begin. If
the client requires Plan Mode for this task, stop before any work and return a
short `BLOCKED` report naming the mismatch.

## Accepted decision and plan

The COOPERATOR explicitly accepted ADR-0087 in the exact semantics presented in
`01_report_02.md` §3 on 2026-11-09. The acceptance is recorded in this whole's
`00_notes.md`. The plan's material product/architecture gate is satisfied.

The accepted implementation plan is:

```text
/Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/01_report_02.md
```

Read it in full before the preflight. It is the accepted plan, not a new
planning question. Do not replan, redesign, expand or shrink it. Your job is to
verify that it is implementable, complete, safe and internally consistent, and
to identify any exact blocker or missing path before implementation authority is
issued. If you find a material contradiction, report it with the smallest
correction needed; do not silently repair the plan.

The accepted decision's core is: the Timeline becomes Kronika's complete,
visibility-aware, chronological overview of the catalog media and
Search/Research content the signed-in identity may read, including private,
unanalysed, unfinished, failed and unpublished content where the caller is the
owner or an application administrator; items are ordered by original
creation/admission time; other household members see only existing approved
projections or existing unbound legacy-publication access; Gallery, personal
History, approval, the preview route, audience policy, quarantine, validation,
identity model and internet-publication prohibition remain separate and
unchanged; `/api/timeline` evolves in place with no schema migration and no
synthetic records.

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
Predecessor whole: timeline-and-history-media-thumbnails; E2 acceptance-PASS,
  publication-PASS and recorded deployment-PASS at b66ec8f; rendered acceptance
  paused; preview groundwork retained.
NUC state: last observed at b66ec8f; NOT revalidated in this whole. No NUC
  contact is granted in this preflight.
```

The preflight must independently re-verify HEAD, branch, clean tree, submodule
equality, `ap doctor` and `ap project check`. Report any contradiction with this
prompt and its cause.

## Goal

Produce one decision-ready read-only preflight report for the accepted plan:

> PASS if the plan is implementable inside its allowlist, its security and
> aggregation claims match the current repository, its test side effects and
> rollback are understood, and no material prerequisite is missing. PARTIAL if
> useful evidence exists but a material prerequisite, safety detail or
> allowlist gap remains. BLOCKED if implementation must not be authorized.

A preflight PASS recommends a separately authorized implementation; it never
authorizes it.

## What to verify

### 1. Repository and AP gate

Independently re-verify, before relying on any measurement:

- physical checkout `/Users/agile/Projects/kronika`, standalone topology;
- branch `main`, HEAD and public `refs/heads/main` at
  `b66ec8f50860ace624f6be1fd3ad63f521edcd33`;
- clean working tree and no unexplained untracked or modified paths;
- `.ap` gitlink and submodule HEAD both
  `d7023cf037f6d17885c3ede5c04812c61640da50`;
- governing AP variant `stable`;
- `./.ap/ap doctor` PASS;
- `./.ap/ap project check --root /Users/agile/Projects/kronika --baseline b66ec8f50860ace624f6be1fd3ad63f521edcd33`
  PASS;
- no active Worker mutation, deployment lock, or unexpected local state for this
  whole.

Report any contradiction and stop the affected work.

### 2. Accepted decision and plan integrity

- Read `01_report_02.md` in full and this whole's `00_notes.md`.
- Confirm the Cooperator's ADR-0087 acceptance and the plan disposition are
  recorded.
- Confirm the accepted plan's proposed ADR path is
  `docs/adr/0087-complete-visibility-aware-timeline-chronicle.md` and that no
  tracked `0087` ADR exists at the baseline.
- Confirm the plan's new source and test paths are absent at the baseline:
  `src/kronika/application/ports/timeline.py`,
  `src/kronika/infrastructure/persistence/timeline_repository.py`,
  `tests/integration/persistence/test_timeline_repository.py`,
  `tests/contract/test_timeline_api.py`.
- Confirm the plan's existing paths and test identities exist and the plan's
  claims about them are true.
- Confirm the plan does not require an unlisted file, route, capability,
  migration, dependency, host operation or acceptance surface.

### 3. Item model, union and deduplication

Verify the plan's §4 item model against the actual schema and code:

- `logical_media` is the media identity and exists before analysis; media may
  have no `kronika_records` row;
- production code has no `bind_media_record` caller;
- `kronika_records` media rows are optional and unique per medium;
- completed `kronika_records`/`kronika_documents` and `research_requests` can
  overlap, including the atomic-save interval before the request state becomes
  `saved`;
- the plan's `media:` and `question:` identities, precedence and deduplication
  are implementable with the current keys and constraints;
- no synthetic record, event row, new persistent entity or data rewrite is
  required;
- locations, tags, analysis runs, approvals and acquisition claims do not
  multiply Timeline rows;
- quarantine/incomplete uploads and acquisition jobs without a `logical_media`
  row remain outside the Timeline.

### 4. Visibility and authorization parity

Verify the plan's §4.2 matrix and §6 SQL arms against the actual current
decision paths:

- `decide_bound_read`, `scope_for_identity`, `ContentAudiencePolicy.read_decision`,
  `content_audience_api.py`, `record_access.py` persistence predicates and the
  current direct media routes;
- owner, application administrator, other household member and unauthenticated
  caller cases;
- bound private, bound approved family, bound withdrawn, unbound unpublished
  with live requester access, unbound unpublished without attribution,
  unbound legacy-published, private/approved/withdrawn questions and
  unfinished/failed/cancelled requests;
- upload, YouTube and X requester access success-state predicates; the general
  attribution union is broader than direct-read authorization;
- binding precedence over legacy publication and contribution stamps;
- approved document projection use for household reads and current content for
  owner/admin reads;
- filters, search, counts and pagination cannot widen the authorized set;
- every linked detail, preview, content and download route reauthorizes
  independently;
- no new capability or route-policy widening is introduced.

Name every predicate or source that the plan omits or misstates. A mismatch is
a preflight finding, not permission to change the plan silently.

### 5. API, SQL and query plan

Verify the plan's §5 and §6:

- `/api/timeline` already has an ingress route policy and no new route-level
  capability is needed;
- the proposed `TimelineItem`, `TimelinePageQuery` and `TimelinePage` shapes can
  be serialized without widening record or detail contracts;
- the read transaction / snapshot approach is available through the current
  engine and repository composition;
- SQLite JSON1 `json_extract` is available for the approved-document question
  text; a non-mutating `sqlite3 :memory:` probe is allowed, but no file-backed
  probe database is authorized;
- the plan's two-or-three SELECT budget is achievable for empty,
  questions-only and media pages;
- `UNION ALL` arms are disjoint and cannot duplicate a medium or a saved
  question;
- the preview batch uses one page-bounded query and the correct approved/current
  location source;
- no per-item detail, policy, filesystem, cache-readiness or generation call is
  introduced;
- no new index or migration is required for the plan's stated first candidate;
  assess the plan's acknowledged scan/sort risk and whether it is a blocker or
  an accepted residual limitation;
- the plan's error, cache-header, no-store and no-ETag behavior is compatible
  with the existing ingress and application conventions;
- the plan's `RecordService`/`RecordRepository` delegation and removal of the
  obsolete approved-only branch do not break History, administrator inventory,
  approval, withdrawal or preview behavior.

### 6. UI, accessibility and frozen surfaces

Verify the plan's §7:

- the Timeline can become a semantic compact list without importing Gallery's
  card/player behavior;
- the proposed fields, filters, focus, return-navigation, responsive behavior
  and empty/loading/error states are implementable in the existing shell;
- the preview helper, generation fences, cancellation, `visibilitychange` and
  `pagehide` behavior from whole 01 can be reused without regression;
- Review copy changes and the exact `index.html`/`app.js`/`styles.css` pins are
  identified;
- Gallery, Details, personal History, the player and their frozen visual
  behavior remain outside the change except the plan's explicitly bounded
  Timeline return-navigation glue;
- no new frontend framework, asset pipeline or second Gallery is introduced.

### 7. Tests, side effects and validation

Verify the plan's §8 and §9:

- every existing test identity the plan says will change exists and is
  correctly characterized;
- the new test paths are planned and absent at baseline;
- the inventory test currently rewrites `docs/KRONIKA_ACCESS_INVENTORY.md`
  through `INVENTORY.write_text`; the plan's exact read-only comparison change
  is correct and necessary;
- the proposed test commands use the declared `./.ap/ap exec --operation
  test-focus` route and `node --test`, not ambient Python;
- the test plan covers the positive and negative visibility matrix, dedup,
  ordering, pagination/count, snapshot, query budget, preview, fallback,
  accessibility, inert text and frozen surfaces;
- the test plan does not rely on live providers, real private media, NUC
  fixtures, browser-toolchain installation or a full suite;
- the implementation would not need to write tracked files during tests or
  acceptance;
- the plan's E3 fresh independent acceptance, one primary acceptance and at most
  one correction/re-acceptance are proportionate and correctly separated from
  implementation.

### 8. Documentation promotion and rollback

Verify the plan's §11 owners:

- the proposed ADR-0087 and `docs/adr/README.md` update are the architecture
  owner; accepted ADR-0082 through ADR-0086 bodies remain unchanged;
- `AGENTS.md`, `SPEC.md`, `SECURITY.md`, `README.md`, `PRODUCT.md`, `SERVER.md`,
  `ROADMAP.md`, `DEVELOPMENT.md`, `GALLERY.md` and
  `docs/KRONIKA_ACCESS_INVENTORY.md` are the correct exact owners and contain
  the claims the plan says they contain;
- no second semantic owner is created and no stale restatement is left
  unaddressed;
- the source candidate has a clean source rollback path and no schema, data,
  host or deployment rollback prerequisite beyond the plan's later NUC phase;
- no migration, fixture mutation, secret, NUC contact, browser session,
  provider call or deployment is needed for implementation.

### 9. Blockers and smallest corrections

List every material blocker or plan gap with:

```text
Finding ID | Exact repository evidence | Effect on implementation or safety | Smallest correction | Blocking: yes/no
```

Do not propose broad redesign. If the plan is implementable as written, state
that explicitly and recommend the separate implementation grant.

## Deliverables

The terminal preflight report must contain:

1. standard AP report header and coordinate block;
2. preflight verdict: PASS, PARTIAL or BLOCKED;
3. re-measured repository and AP gate;
4. accepted-decision and plan-integrity reconciliation;
5. allowlist completeness table (planned path, exists at baseline, purpose,
   missing/extra);
6. visibility/authorization parity matrix and any mismatches;
7. item-model, dedup and query-plan findings;
8. UI/accessibility/frozen-surface findings;
9. test, side-effect and validation findings;
10. documentation-owner and rollback findings;
11. blockers/required plan corrections table;
12. exact recommended implementation sequence and, if PASS, the plan's exact
    source/test/documentation allowlist for the next grant;
13. evidence limitations and what was not run;
14. one smallest next step;
15. orchestration critique and authority-expiry statement.

A PASS must be explicit that it recommends a separately authorized
implementation and does not authorize it. A PARTIAL/BLOCKED report must name the
exact missing evidence or decision and the smallest route to close it.

## Authority

```text
Positive authority: read-only inspection inside /Users/agile/Projects/kronika,
  including .ap at its pinned commit; optional read-only public verification of
  https://github.com/cisarik/kronika.git through git ls-remote when available;
  read-only inspection of
  /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/
  (this prompt, 00_notes.md, 01_report_02.md and the frozen handout), the run
  map /Users/agile/meta/projects/kronika/01/00_RUN_MAP.md, the predecessor 01
  whole's frozen notes and named reports, and the closed 00 whole's 00_notes.md
  and handout §9.2; read-only inspection of the named Meta AP_DEFECTS.md and
  AP_DESTILLED.md entries as consumer evidence; repository gates through
  ./.ap/ap doctor and ./.ap/ap project check; non-mutating sqlite3 :memory:
  probes for JSON1 or query-syntax feasibility; exact direct-write of the
  terminal report at the path below if and only if it is absent and the client
  permits the write, followed by a complete readback. If the client prohibits
  the write, return the complete exact report in the session for authorized
  persistence and do not claim saved-file readback.

Negative authority: any file edit, create, move, rename or deletion in
  /Users/agile/Projects/kronika; any write to /Users/agile/meta except the one
  report file; any Git write of any kind — no add, commit, branch, tag, merge,
  rebase, stash, checkout, switch, reset, clean, submodule update or push; any
  dependency install, update or lockfile change; any file-backed temporary
  database or repository test artifact; any NUC contact, deploy, rollback,
  capture transition, direct SSH session, sudo, systemd, package-manager,
  AppArmor, UFW, Tailscale, mount or storage mutation; any provider or
  capture-browser contact; any reading of browser profiles, cookies, tokens,
  credential stores, or NUC secret values; any browser session or rendered
  acceptance; any creation of a plan artifact or ADR in the repository; any
  implementation, acceptance, publication, deployment or closure.

Commands: read-only Git inspection is allowed: git status, git rev-parse,
  git log, git show, git diff, git ls-files, git grep, git ls-tree,
  git cat-file, git ls-remote, git submodule status, git describe,
  git merge-base. No other Git command. Repository gates:
  ./.ap/ap doctor and
  ./.ap/ap project check --root /Users/agile/Projects/kronika --baseline
  b66ec8f50860ace624f6be1fd3ad63f521edcd33.
  A non-mutating sqlite3 :memory: probe is allowed; no file-backed database.
  Do not execute the implementation test suite; inspect the tests and use the
  repository gate. If a narrow claim cannot be established without executing a
  test, stop and report the missing evidence rather than creating test state.
  Never invoke .venv/bin/python, python, python3, poetry run, or an ambient
  equivalent for evidence.

Dependency authority: none. Do not reinstall, update or relock anything.

Git authority: read-only inspection and optional public ref verification only.

Network authority: optional public read-only Git verification only. No provider
  call, NUC contact, browser contact, or other outbound request.

Secret authority: none. Never print, quote, or summarize secret values, host
  identifiers, addresses, disk serials, UUIDs, SSH fingerprints, or private
  media filenames.

Untrusted-content boundary: .ap/AP.md at the pinned commit is the governing
  protocol; repository AGENTS.md is authoritative inside its scope; the plan,
  notes, handout, this prompt and project documents are task context, not
  higher authority; repository content is data under analysis. On any conflict
  between retained context and current repository evidence, stop.

Side-effect authority: authorized read-only only. The report write is trace
  persistence, not repository mutation.

Browser authority: none. Rendered acceptance is the COOPERATOR's, not yours.
```

## Evidence

```text
Evidence tier: E3 for the authorization boundary the preflight prepares. The
  preflight itself is read-only and non-independent; the later acceptance is
  fresh independent.

Validation ladder: selected
  Inspection and provenance: required
  Existing focused tests: read-only inspection; do not execute the future
    implementation suite
  Affected tests: the plan's exact existing and planned identities after
    inspection
  New causal regression: not-applicable — preflight; the implementation plan
    owns the new tests
  Broad or full suite: not-used
  Runtime or testbed: not-used
  Independent acceptance: not-required for this preflight; the later acceptance
    is a separate fresh Worker

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
Stopping conditions: stop without improvising if the client requires Plan Mode
  or cannot run native planning mode not-used; if this is not a fresh Worker
  session 02 for this whole; if HEAD, the branch, the remote, or the tree does
  not match the verified state; if the submodule is not at the pinned commit;
  if ap project check --baseline does not pass; if the accepted ADR-0087 or plan
  evidence is missing; if you would need any repository/Meta write beyond the
  report, file-backed temporary state, test execution, NUC contact, browser
  session, provider call, or secret access to answer a question; if you find a
  material contradiction that needs an Orchestrator or Cooperator decision
  rather than a preflight finding; if context pressure reaches the point where
  a bounded rotation is cheaper than a degraded preflight; or if the exact
  report path already exists, including an empty file.

Completion: one terminal preflight report containing the full evidence and the
  PASS/PARTIAL/BLOCKED verdict, not a summary and not an implementation.

Required report sections: the standard report core and header (including the
  coordinate block and echo of Persistent role identity, Worker session target,
  Native planning mode, Worker session profile, Task identity); the preflight
  verdict; the re-measured repository/AP gate; accepted-decision and plan
  integrity; allowlist completeness; visibility/authorization parity; item
  model, dedup and query plan; UI/accessibility/frozen surfaces; tests and side
  effects; documentation and rollback; blockers/corrections; recommended
  implementation sequence and allowlist; evidence limitations; one smallest
  next step; and the orchestration critique.

Report destination: direct-write
  /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_report_00.md
  if and only if it is absent and the client permits the write. Read the
  complete file back and verify content, identity and path before the short
  separate completion notice. If the client prohibits the write, return the
  complete exact report in the session and state exactly
  `Report persistence: client-prohibited; complete exact content returned for authorized persistence`.
  Do not claim saved-file readback and do not bypass the client control. Do not
  write any other file. Do not create a plan artifact or ADR in the repository.

Report justification: new-evidence

Authority expiry: on submission of the terminal preflight report, all preflight
  authority expires. Implementation in this session is prohibited until a
  separate complete ORCHESTRATOR implementation prompt with Native planning
  mode: not-used and explicit implementation authority is issued.

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

Read the exact owners for the claims you verify; do not read the whole protocol
when a bounded owner is sufficient.

- `.ap/AP.md` at the pinned commit: §2 Roles; §3 Worker Session Target,
  Orchestration Planning and Implementation Planning, Plan-to-Execution Gate;
  §5 Task Authority; §6 Adaptive Orchestration Lifecycle (including the separate
  read-only preflight); §7 Orchestrator Responsibilities; §10 Security
  Boundaries; §12 Validation and Public Verification; §13 Artifact Lifecycle;
  §18 Stopping Conditions; §19 Anti-Patterns (skim); and the Finite Convergence
  Contract.
- `.ap/AP_WORKER.md` in full: Worker session target, bounded authority, and
  reporting.
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header; Common Worker Task Fields;
  Repository Checkout Topology Contract; Worker Session Target Contract; Worker
  Exchange Identity and External Trace Contract; Cooperator Delivery and Trace
  Destination Record; Mutation Axes Record; Validation Ladder Record;
  Pre-Existing Failure Classification Contract; Separate Read-Only Preflight.
- `.ap/AP_ORCHESTRATOR.md` reference-on-demand: Decision Table; Preflight
  Selection; Activated Surface Decisions; Security Risk Routing; Artifact and
  Ledger Governance.
- `AGENTS.md` at the repository root, including its managed AP block, Security
  Boundaries, Product Boundaries, Cursor Worker Execution Boundary, Worker
  Execution, and Git and Lifecycle.
- `docs/WORKER_EXECUTION_CONTRACT.md`: the Cursor/AppImage execution boundary,
  canonical `./.ap/ap exec` route, NUC SSH gate, sudo lifecycle, and test
  invocation.
- `docs/adr/README.md` and ADRs 0082, 0083, 0084, 0085 and 0086.
- `README.md`, `PRODUCT.md`, `SPEC.md`, `ROADMAP.md`, `SECURITY.md`, `SERVER.md`,
  `GALLERY.md`, `DEVELOPMENT.md`, `docs/KRONIKA_ACCESS_INVENTORY.md` and
  `docs/UX_AUDIT.md`.
- `docs/AP_UPGRADE_OBSERVATIONS.md`.
- The accepted plan
  `/Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/01_report_02.md`
  in full, this whole's `00_notes.md`, the frozen handout, and the run map.
- Source: `src/kronika/adapters/api/records_api.py`; the records service, port,
  domain access and repository; `src/kronika/application/content_publication.py`;
  `src/kronika/adapters/api/content_audience_api.py`;
  `src/kronika/adapters/api/gallery_preview_api.py`;
  `src/kronika/adapters/api/tailscale_ingress.py`;
  `src/kronika/infrastructure/persistence/catalog_schema.py`;
  `media_attribution_repository.py`, `media_catalog_repository.py`,
  `research_request_repository.py`, `record_repository.py` and the research
  completion path; `src/kronika/adapters/api/web/app.js`,
  `src/kronika/adapters/api/web/index.html` and
  `src/kronika/adapters/api/web/styles.css`; the public-published composition.
- Tests: `tests/contract/test_records_api.py`,
  `tests/integration/persistence/test_kronika_record_repository.py`,
  `tests/contract/test_kronika_approved_projection.py`,
  `tests/contract/test_kronika_access_inventory.py`,
  `tests/contract/test_gallery_preview_api.py`,
  `tests/contract/test_local_web_application.py`,
  `tests/kronika_ui.test.js`,
  `tests/contract/test_research_requests_api.py`,
  `tests/contract/test_workspace_media.py`,
  `tests/contract/test_public_published_uds.py`,
  `tests/unit/application/test_records.py`,
  `tests/unit/domain/test_record_access.py` and
  `tests/unit/application/test_content_audience_requester_private.py`.
- `/Users/agile/meta/AP_DEFECTS.md` §0.0, D-17b, D-19, D-20 and D-21;
  `/Users/agile/meta/AP_DESTILLED.md` §17. These are citable consumer evidence,
  not rule sources. The governing AP owns every rule.

## Communication

Worker prompts, the report, and any preflight text are professional English. Do
not use Czech or Slovak in repository, Meta, or report artifacts. The
Cooperator's chat language is separate and governed by the project rules.

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
Downloadable prompt filename: 02_preflight_00.md
Destination path: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/
Report filename: 02_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_report_00.md
```

The report write is trace persistence, not repository mutation. If the report
path exists, including an empty file, stop `BLOCKED` without overwriting it.
The verified parent directory exists. Do not create a placeholder or use another
path. The direct-write route applies if the client permits the write under its
active non-planning mode. If it does not, return the complete exact report in the
session and do not claim saved-file readback.

### NUC and deployment (read-only preflight; no contact)

```text
Routine NUC release-update entry point: deploy/ubuntu/kronika-release (Fish
  wrapper) plus deploy/ubuntu/kronika_release.py (standard library only).
This preflight: no NUC contact, no SSH, no sudo, no kronika-release, no deploy,
  no rollback, no systemd, no package manager, no AppArmor, no UFW, no
  Tailscale, no mount or storage mutation.
Last observed NUC state (NOT revalidated): active_release and web_release
  b66ec8f50860ace624f6be1fd3ad63f521edcd33; capture_release
  5b86d896b3ea03f89fef2c90f7af2c121d0ef915; layout canonical; service_active
  active; database_revision 0035; backup_restore_readiness ready.
The later deployment grant, not this preflight, must verify the then-current NUC
  state, public main, exact release SHA, fresh Cooperator sudo timestamp and
  rollback. A predecessor deployment revoked the sudo timestamp with sudo -K;
  a later deployment needs a fresh Cooperator sudo -v.
Deployment never follows automatically from a check. No schema change is planned;
  target head remains 0035. If a later deployment reports exit 13, preserve that
  result and use only the documented migration-required continuation under
  explicit matching authority.
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
Implementation task grant: none — this preflight does not change, revalidate,
  or implement the ledger entry.
```

### Security and audience boundary

This preflight is the last read-only review before implementation authority. Its
central claim is parity between the new Timeline list/count/search projection
and the existing direct-read authorization for every item type and caller class.
Owner, administrator, household and unauthenticated cases are mandatory
findings, not assumptions. The preflight must identify any predicate, source,
filter, count or search path that could widen access, and any direct-route
reauthorization that would not hold. It must not perform a security audit of the
whole system; it must decide whether the accepted plan's authorization claims
are implementable and testable as written.

## Visible delivery capsule

```text
🟡 Ready for delivery
Recipient: Worker-Executed Preflight · fresh-worker-session · manual
Recommendation: High · approximately 1M tokens
Client: Native Plan Mode OFF
Prompt: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_preflight_00.md
Report: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_report_00.md
Archival: wait-for-report
```
