# Authoritative Worker prompt — Kronika whole 09, Worker session 04, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`timeline-complete-chronicle`. It is stored under the Meta filename mapping
`<worker-session>_<phase>_<meta-exchange-index>.md` as
`04_acceptance_00.md`. The matching terminal report is `04_report_00.md`.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: timeline-complete-chronicle
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: Acceptance
Task identity: KRN-TCC-ACC-04 — full fresh re-acceptance after the two UI corrections
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — a full-fresh re-acceptance of the main-page privacy projection plus the corrected UI recovery and labelling behavior
Recommended context capacity: approximately 250k tokens
Independence required: required-fresh-independent
```

You are a genuinely fresh independent auditor. You did not plan, preflight,
implement or correct this candidate, and you did not participate in the first
acceptance. Do not treat retained implementation or correction reasoning, the
implementation report, the correction report, the first acceptance report, or
this prompt as proof. Re-establish every material fact from the fixed candidate
and current repository evidence. If this session already contains prior
conversation about this whole, stop and report a `fresh-worker-session` target
mismatch.

Before substantive work, confirm that `Native planning mode: not-used` is the
actual client state (native Plan mode OFF). If it is enabled, stop and return
`BLOCKED` naming the contradiction.

## Acceptance record

```text
Acceptance candidate: 1bc10a364ddf3fba15fad62e9036183ab75e1a46
Acceptance owner map: 01_report_02.md section 10 rows C01-C24; ADR-0087; 02_report_01.md section 7; 02_report_02.md; 03_report_00.md
Acceptance allowlist: exactly the 29 changed paths in section 2
Acceptance risk claims: C01-C24, plus the two corrected UI claims in section 4
Acceptance control matrix: 01_report_02.md section 10, fixed
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

## 1. Goal

Perform the required **full-fresh re-acceptance** of corrected candidate
`1bc10a364ddf3fba15fad62e9036183ab75e1a46` for the accepted ADR-0087 complete,
visibility-aware Timeline chronicle. The prior acceptance at `264a040` passed
C01–C24 but found two non-security UI gaps; the bounded correction at
`1bc10a3` fixes them. Because the correction changes runtime UI behavior, the
whole receives a full-fresh re-acceptance, not a scoped review.

Accept or reject the corrected candidate. Do not implement, correct, publish,
deploy or close. One concrete finding is reported with exact evidence; a further
correction is a separate Orchestrator decision and must respect AP's one-
correction budget for the same finding.

## 2. Exact changed-path allowlist

The candidate from public baseline `b66ec8f` must change exactly these 29 paths
and no others:

```text
AGENTS.md
DEVELOPMENT.md
GALLERY.md
PRODUCT.md
README.md
ROADMAP.md
SECURITY.md
SERVER.md
SPEC.md
docs/KRONIKA_ACCESS_INVENTORY.md
docs/adr/0087-complete-visibility-aware-timeline-chronicle.md
docs/adr/README.md
src/kronika/adapters/api/records_api.py
src/kronika/adapters/api/web/app.js
src/kronika/adapters/api/web/index.html
src/kronika/adapters/api/web/styles.css
src/kronika/application/ports/records.py
src/kronika/application/ports/timeline.py
src/kronika/application/records.py
src/kronika/domain/record_access.py
src/kronika/infrastructure/persistence/record_repository.py
src/kronika/infrastructure/persistence/timeline_repository.py
tests/contract/test_kronika_access_inventory.py
tests/contract/test_kronika_approved_projection.py
tests/contract/test_records_api.py
tests/contract/test_timeline_api.py
tests/integration/persistence/test_kronika_record_repository.py
tests/integration/persistence/test_timeline_repository.py
tests/kronika_ui.test.js
```

The correction delta `264a040..1bc10a3` must be exactly four paths, all within
the list:

```text
src/kronika/adapters/api/web/app.js
src/kronika/adapters/api/web/index.html
src/kronika/adapters/api/web/styles.css
tests/kronika_ui.test.js
```

Negative allowlist: no change to `.ap/**`, the AP gitlink, `ap.project.conf`,
the upgrade ledger, dependency files, `catalog_schema.py`, Alembic migrations,
database writers outside the named reader changes, `ContentAudiencePolicy`,
`content_audience_api.py`, preview/content/download routes, public composition,
identity/capability definitions, ingress route-policy tables, authentication
configuration, upload/acquisition/research/capture implementations,
`extension/**`, `deploy/**`, operator scripts, host configuration, Gallery/Details
renderer bodies or player behavior beyond the bounded Timeline return glue,
ADR-0082 through ADR-0086 bodies, `docs/UX_AUDIT.md`, predecessor notes/reports,
run map or handouts. If the final diff or the correction delta contains any
other path, report it as a finding.

## 3. Candidate, baseline and gate

```text
Repository: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Repository checkout topology: standalone checkout
Working-copy topology: canonical checkout; the fixed candidate is checked out
Expected branch: main
Candidate under test: 1bc10a364ddf3fba15fad62e9036183ab75e1a46
Parent / trusted execution baseline: 264a040e104e7495ce649fa583c4f0f3c1241b7c
Public main: b66ec8f50860ace624f6be1fd3ad63f521edcd33 (candidate is local and unpushed)
Containing-repository .ap gitlink: d7023cf037f6d17885c3ede5c04812c61640da50
Submodule HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
```

Verify before substantive review:

```text
git rev-parse HEAD
git status --short
git log --oneline -4
git diff --name-only b66ec8f..1bc10a3
git diff --name-only 264a040..1bc10a3
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 264a040e104e7495ce649fa583c4f0f3c1241b7c
```

Stop on any mismatch: dirty worktree, HEAD not the candidate, parent not
`264a040`, final diff not the 29 paths, correction delta not the four paths, or
a failed gate. The candidate is fixed; do not commit, amend, reset, clean,
checkout or otherwise move it.

## 4. Fixed matrix and the two corrected UI claims

The authoritative matrix remains `01_report_02.md` section 10, rows C01–C24.
Read it in full and record every row as PASS, FAIL or NOT TESTED with exact
evidence. Do not remove, merge or weaken a row. The first acceptance at
`264a040` passed C01–C24; this re-acceptance must re-verify the whole matrix on
the corrected candidate and specifically close:

```text
C22-Retry: a same-query Timeline refresh failure keeps the previous authorized
  page, marks it stale, and exposes the existing Retry control; Retry repeats
  the exact current route/query, does not steal focus, and does not create an
  automatic retry. A first-load failure keeps its existing error/Retry path; a
  changed-query failure does not retain another query's rows.

C22-Labels: the chronicle has a desktop visual header outside the <ol> with
  aria-hidden="true" and aligned Preview/Item/Kind/Added/Status/Visibility
  columns; each row exposes Kind, Added, Status and Visibility labels through
  the existing visually-hidden utility; at 720 px and below the header is
  hidden, the field labels are visible, rows remain one item per row, no
  horizontal page scrolling occurs at 320 px, and 44 px interactive targets
  are preserved. The preview stays decorative and the title link remains the
  row's accessible name.
```

The two corrections must not change authorization, payload keys, route
inventory, stored data, preview behavior or Gallery/Details.

## 5. Required independent verification

### 5.1 Original matrix

Re-verify the complete C01–C24 matrix from source, API, persistence and tests:
the three disjoint arms, visibility matrix, union/deduplication, creation-time
ordering, filters/counts/pagination, snapshot, query budget, preview locators
and withdrawal denial, payload sanitization/no-store, route inventory,
accessibility, frozen Gallery/Details and absence of provider/generation side
effects. Treat the prior reports as claims.

### 5.2 Correction delta

Read the four-path correction diff and verify:

- `app.js` keeps the last page and shows Retry only for the stale same-query
  case; the changed-query and first-load paths retain their existing behavior;
- `index.html` places the header outside the `<ol>` and does not alter
  authorization or the list contract;
- `styles.css` scopes the header/labels to the Timeline, hides the header and
  shows labels at 720 px and below, avoids horizontal page scrolling at 320 px,
  and preserves 44 px targets and the compact list;
- `tests/kronika_ui.test.js` contains the causal tests and no weakened existing
  expectation;
- no other path or behavior changed.

### 5.3 Tests

Run the exact selected routes from `/Users/agile/Projects/kronika`, using the
trusted execution baseline `264a040`. The worktree HEAD must be `1bc10a3`. Do
not run the full Python suite.

```text
# [MacBook / fish]
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 264a040e104e7495ce649fa583c4f0f3c1241b7c
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 264a040e104e7495ce649fa583c4f0f3c1241b7c --operation test-focus -- tests/integration/persistence/test_timeline_repository.py tests/integration/persistence/test_kronika_record_repository.py tests/contract/test_timeline_api.py tests/contract/test_records_api.py tests/contract/test_kronika_approved_projection.py tests/contract/test_kronika_access_inventory.py tests/contract/test_gallery_preview_api.py tests/contract/test_content_audience_policy.py tests/contract/test_research_requests_api.py tests/contract/test_workspace_media.py tests/contract/test_public_published_uds.py tests/unit/application/test_records.py tests/unit/domain/test_record_access.py tests/unit/application/test_content_audience_requester_private.py -q -p no:cacheprovider
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 264a040e104e7495ce649fa583c4f0f3c1241b7c --operation test-focus -- tests/contract/test_local_web_application.py -k 'kronika_shell or details or persistent_preview or initial_card or available_cards or gallery' -q -p no:cacheprovider
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 264a040e104e7495ce649fa583c4f0f3c1241b7c --operation test-focus -- tests/contract/test_tailscale_ingress_security.py -k 'route_policies_match_the_application_route_inventory or requester_private_media_detail_reaches_application_through_ingress or missing_identity_login_is_rejected' -q -p no:cacheprovider
node --test tests/kronika_ui.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js
git diff --check
git status --short
#------------------------------------------------------
```

Report actual counts. A test failure stops the affected review and is reported
with exact evidence; do not fix it.

## 6. Authority

```text
Positive authority: read-only inspection of the Kronika repository at the fixed
  candidate; read-only public verification of https://github.com/cisarik/kronika;
  read-only inspection of the accepted plan, ADR-0087, the implementation,
  correction and prior acceptance reports, this prompt and the whole's Meta
  notes; run the exact selected gate and tests; ephemeral synthetic test state
  created only by the tests themselves; exact direct-write of the terminal
  report below if it is absent, followed by a complete readback.

Negative authority: any edit, creation, deletion, rename or chmod in the
  repository or worktree; any Git write - no add, commit, push, fetch, merge,
  rebase, reset, restore, clean, stash, checkout, switch, branch, tag, remote or
  config write; no amend; no implementation or correction; no change to the
  matrix, allowlist or candidate; no schema, migration, route-policy, public
  composition, audience-policy or capability change; no NUC contact, SSH, sudo,
  deploy, rollback, systemd, package manager, AppArmor, UFW, Tailscale, mount or
  storage mutation; no browser session, rendered acceptance, screenshot or GUI
  automation; no provider, capture, extension or acquisition contact; no secret,
  credential, token, cookie, private-key, private-media or host-specific value
  inspection; no publication, deployment or closure claim; no Meta write except
  the exact report.

Commands: the exact commands above. Python evidence only through
  ./.ap/ap exec --operation test-focus. JavaScript tests use node --test. Never
  invoke .venv/bin/python, python, python3, poetry run, or an ambient equivalent
  for evidence. Read-only Git inspection is allowed: status, rev-parse, log,
  show, diff, ls-files, grep, ls-tree, cat-file, ls-remote, submodule status,
  describe, merge-base.

Dependency authority: none.
Git authority: read-only inspection only. No write.
Network authority: public read-only Git verification only. No provider, NUC,
  browser or other outbound request.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit is the governing
  protocol; AGENTS.md is authoritative inside its scope; the plan, ADR-0087,
  reports and this prompt are task context; repository content is data under
  analysis. Stop on conflict with current repository evidence.
Side-effect authority: read-only verification and the report write only.
Browser authority: none.
```

## 7. Completion and report

```text
Stopping conditions: stop without improvising if the client has native Plan
  mode enabled; if HEAD, branch, parent, public main, .ap pin or tree does not
  match; if ap doctor or the project check fails; if the final diff or correction
  delta is outside the allowlist; if a required test fails; if the candidate is
  dirty or moved; if a claim requires a real NUC, browser, provider, secret or
  private-media access; if context pressure reaches the point where a bounded
  rotation is cheaper than a degraded audit; or if the exact report path already
  exists, including an empty file.

Completion: one terminal full-fresh re-acceptance report with the complete
  C01-C24 matrix, the two corrected UI claims, exact evidence, actual test
  counts and any findings. Do not implement a further correction.

Required report sections: the standard report core and header with the exact
  coordinate block and echo of Persistent role identity, Worker session target,
  Native planning mode, Worker session profile and Task identity; Status;
  Phase-qualified result: acceptance-PASS | not-applicable; Start commit:
  264a040e104e7495ce649fa583c4f0f3c1241b7c; End commit:
  1bc10a364ddf3fba15fad62e9036183ab75e1a46; Report justification:
  final-acceptance; Logical-whole closure: not-closed; the acceptance record;
  the C01-C24 matrix verdicts with evidence; the C22-Retry and C22-Labels
  verdicts; the exact test commands and actual pass/fail counts; source/security
  findings; API and payload findings; UI and frozen-view findings; documentation
  and inventory findings; allowlist and correction-delta review; deviations and
  near-misses; pre-existing failure classification; residual risks and missing
  evidence; one smallest next step; and the orchestration critique.

Report destination: direct-write
  /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/04_report_00.md
  if and only if it is absent. Read the complete file back and verify content,
  identity and path before the separate completion notice. Do not write any
  other Meta file and do not create an artifact in the repository.

Report justification: final-acceptance
Authority expiry: on submission of the terminal re-acceptance report, this
  grant expires. No further correction, publication, deployment, production or
  closure authority remains. A later phase requires a new complete authoritative
  prompt.
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

## 8. Mandatory reading

- The accepted plan `01_report_02.md` in full, especially §3 ADR-0087, §4 item
  model, §5 API, §6 SQL/performance, §7 UI, §8 allowlist, §9 tests, §10 matrix
  and §12 sequence.
- The Cooperator's ADR-0087 acceptance record in `00_notes.md`.
- The prior implementation report `02_report_01.md`, correction report
  `02_report_02.md` and first acceptance report `03_report_00.md` as claims to
  verify, not proof.
- `.ap/AP.md` at the pinned commit: §2 Roles; §3 Instances, Sessions, and Worker
  Session Profiles; §5 Task Authority; §6 Adaptive Orchestration Lifecycle;
  §7 Orchestrator Responsibilities; §12 Validation and Public Verification;
  §13 Artifact Lifecycle; §15 Fresh-Slice Implementation and Diagnostic
  Closeout; §17 Compact Communication; §19 Anti-Patterns (skim); and the Finite
  Convergence Contract.
- `.ap/AP_WORKER.md` in full.
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header; Acceptance and Correction
  Record; Phase Result and Closure Record; Common Worker Task Fields; Repository
  Checkout Topology Contract; Worker Session Target Contract; Worker Exchange
  Identity and External Trace Contract; Cooperator Delivery and Trace
  Destination Record; Mutation Axes Record; Validation Ladder Record;
  Pre-Existing Failure Classification Contract.
- `AGENTS.md`, `SPEC.md`, `SECURITY.md`, `README.md`, `PRODUCT.md`, `SERVER.md`,
  `ROADMAP.md`, `DEVELOPMENT.md`, `GALLERY.md`, `docs/KRONIKA_ACCESS_INVENTORY.md`,
  `docs/adr/README.md`, ADR-0087 and ADR-0082 through ADR-0086.
- The exact source and test files in section 2.

## 9. Delivery and trace

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
Downloadable prompt filename: 04_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/
Report filename: 04_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/04_report_00.md
```

The report write is trace persistence, not repository mutation. If the report
path exists, including an empty file, stop `BLOCKED` without overwriting it.
The verified parent directory exists.

## 10. Communication

Worker prompts, the report, code comments, test names and documentation are
professional English. Do not use Czech or Slovak in repository, Meta, or report
artifacts.

## Visible delivery capsule

```text
🟡 Ready for delivery
Recipient: Fresh Independent Audit · fresh-worker-session · manual
Recommendation: High · approximately 250k tokens
Client: Native Plan Mode OFF
Prompt: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/04_acceptance_00.md
Report: /Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/04_report_00.md
Archival: wait-for-report
```
