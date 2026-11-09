# Authoritative Worker prompt — Kronika whole 01, Worker session 02, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`timeline-and-history-media-thumbnails`. It is stored under the Meta filename
mapping `<worker-session>_<phase>_<meta-exchange-index>.md` as
`02_implementation_00.md`. The matching terminal report is `02_report_00.md`.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: timeline-and-history-media-thumbnails
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: Implementation
Task identity: KRN-THT-IMPL-02 — implement the accepted Timeline and History media thumbnail plan
Delivery route: direct session dispatch
Reasoning recommendation: High — the accepted design spans a repository query, an additive list contract, a 15k-line shell with lifecycle/abort behavior, scoped CSS, tests, and durable documentation
Recommended context capacity: approximately 250k tokens
Implementation authority: explicit
Exact baseline: 246c9f86b72e652cd36ed0d9f4e19e77f972df91
Changed-path allowlist: exactly the fourteen repository paths in section 2
Implementation boundaries: the positive and negative authority in section 5
Independence required: no
```

You are a genuinely fresh Implementation Worker. The plan is accepted; do not
re-plan it. Read the accepted plan report in full before editing:

```text
/Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/01_report_00.md
```

The plan report is the design of record. This prompt supplies the implementation
authority, the exact allowlist, the exact baseline, and the completion contract.
If the plan and this prompt conflict, stop and report the contradiction rather
than improvising.

Before substantive work, confirm that `Native planning mode: not-used` is the
actual client state (native Plan mode OFF). If the client has native Plan mode
enabled, do not start; return `BLOCKED` naming the contradiction.

## 1. Accepted design and fixed decisions

Implement the accepted "safe locator plus existing preview route" design:

- Add one nullable `preview_location_id` to `RecordSummary`.
- Populate it only for the Timeline and personal-record History list responses.
  Do not populate it for administrator inventory, record detail, question
  History, Review, or any other surface.
- Resolve the locator in at most one additional page-bounded repository query.
  Do not add per-record detail reads, filesystem probes, cache reads or
  readiness checks to list requests.
- Timeline locations come only from `kronika_approved_media_locations` joined
  through the approved medium, restricted to `availability = 'available'`.
- Personal-record History locations come only from current
  `physical_media_locations` belonging to the page's media, restricted to
  `availability = 'available'`.
- Restrict eligible technical media kind to `logical_media.media_kind` values
  `video` and `animated_image`. Still images (`image`), non-media records,
  question History and missing/unavailable candidates return `null`.
- Choose exactly one deterministic eligible location. Use a grouped
  `MIN(location_id)` (or an equally deterministic lexical selection) and do not
  probe readiness, retry another location, or search locations in the client.
- Keep the existing preview route, audience policy, cache behavior and
  authorization-before-cache order unchanged. Do not add a new endpoint,
  route, capability, guard, migration, persistent column or configuration
  setting.
- Render the existing JPEG preview over the existing 36 px kind-icon slot on
  Timeline media cards and personal-record History media cards only. Keep the
  kind icon visible while loading and after every failure. Use one
  `<img class="kronika-card__preview">` with `alt=""`, `aria-hidden="true"`,
  `loading="lazy"`, `decoding="async"`, `width=36`, `height=36`.
- Build the same-origin URL through the existing `mediaGalleryPreviewUrl`
  helper. Do not accept a server-supplied URL, host or path.
- Use `data-kronika-preview` states `loading`, `ready` and `fallback`. Install
  load/error handlers before assigning `src`. Reveal the image only in `ready`;
  hide the pseudo-icon only in `ready`; on error detach handlers, remove the
  source/element and retain the pseudo-icon.
- Scope new CSS to the Timeline and History results containers. Preserve card
  padding, text, size, links, hover/focus treatment and navigation. The image
  is decorative and adds no focus target.
- Keep the client page size at 24. Do not add prefetching, cache-busting,
  custom blob caches, object URLs, persistent browser storage, a second preview
  cache, automatic retries, generation requests or still-image/original-content
  fallback.
- Add the bounded list/image lifecycle: optional `AbortController` signal
  through `kronikaReadJson` for Timeline/History list requests only; fence image
  callbacks with identity and page generations; detach handlers and remove image
  sources on accepted navigation, page/filter/tab replacement, identity change
  and document teardown; preserve the dirty-navigation refusal and abort only
  after navigation is accepted. Do not change other `kronikaReadJson` callers.
- Preserve every existing behavior and test listed in plan §2 and §5. Do not
  reopen Gallery/Details, the preview route, the audience policy, approval,
  withdrawal, ordering, pagination, Search/Research, upload, companion or
  deployment behavior.
- Use E2 implementation verification followed by Orchestrator acceptance and
  the Cooperator's rendered acceptance. The Worker does not claim acceptance.
  If the implementation would require changing the preview route, audience
  guard, record-access decision, or response beyond the safe locator, stop and
  report; do not expand the allowlist.

## 2. Exact repository allowlist

Modify exactly these fourteen paths:

```text
src/kronika/application/ports/records.py
src/kronika/infrastructure/persistence/record_repository.py
src/kronika/adapters/api/records_api.py
src/kronika/adapters/api/web/app.js
src/kronika/adapters/api/web/styles.css
tests/integration/persistence/test_kronika_record_repository.py
tests/contract/test_records_api.py
tests/contract/test_gallery_preview_api.py
tests/kronika_ui.test.js
SPEC.md
SECURITY.md
GALLERY.md
DEVELOPMENT.md
README.md
```

No new files are required. Add the new tests to the existing test files above.

Negative allowlist — do not edit:

```text
.ap/**
AGENTS.md
ap.project.conf
any dependency manifest or lockfile
any schema, Alembic file or migration history
src/kronika/adapters/api/gallery_preview_api.py
src/kronika/adapters/api/content_audience_api.py
src/kronika/application/content_publication.py
src/kronika/domain/record_access.py
src/kronika/infrastructure/persistence/content_publication_repository.py
src/kronika/adapters/api/tailscale_ingress.py
src/kronika/adapters/api/public_published_api.py and the public-published composition
src/kronika/adapters/api/web/index.html
any Gallery/Details renderer, playback, cover selection or their CSS
extension/**
deploy/**
scripts/operator/**
docs/adr/** and docs/adr/README.md
docs/UX_AUDIT.md
docs/AP_UPGRADE_OBSERVATIONS.md
docs/WORKER_EXECUTION_CONTRACT.md
deploy/systemd/kronika.env.example
tests/contract/test_kronika_access_inventory.py
all other tests not named above
all Meta files except the exact report below
```

A need to edit a negative-allowlisted boundary stops implementation for
Orchestrator review. Do not silently expand the allowlist.

## 3. Repository gate and baseline — revalidate, do not trust

```text
Repository identity: https://github.com/cisarik/kronika
Repository checkout topology: standalone checkout
Working-copy topology: canonical checkout; one active mutator
Working directory: /Users/agile/Projects/kronika
Expected branch: main
Baseline commit under test: 246c9f86b72e652cd36ed0d9f4e19e77f972df91
Public main: 246c9f86b72e652cd36ed0d9f4e19e77f972df91 (git ls-remote verified)
Working tree: clean before implementation
Containing-repository .ap gitlink: d7023cf037f6d17885c3ede5c04812c61640da50
Submodule HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
AP public main: d7023cf037f6d17885c3ede5c04812c61640da50
Governing AP variant: stable
```

Run and report:

```text
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 246c9f86b72e652cd36ed0d9f4e19e77f972df91
git status --short
```

Stop on any mismatch. Do not substitute HEAD for the exact baseline. If the
baseline has moved, stop and report; the Orchestrator must bind a newly verified
baseline.

## 4. Required implementation detail

Follow plan §3 and §4 exactly. The following are the mandatory points the
candidate must satisfy.

### 4.1 Summary and repository

- `RecordSummary` gains `preview_location_id: str | None = None`.
- `record_repository.py` gains one page-level helper returning a
  record-ID-to-location-ID mapping. Call it once after audience filtering,
  pagination and the existing label batch, only for the Timeline and
  personal-record History list paths.
- Timeline query: join `kronika_approved_media_locations` through
  `kronika_approved_media` to the page's `record_id` values and through
  `logical_media` on `media_id`; require `availability = 'available'` and
  `media_kind IN ('video', 'animated_image')`; group by record and select
  `MIN(location_id)`.
- Personal History query: join `physical_media_locations` through
  `logical_media` on `media_id` and `kronika_records` on the page's `media_id`
  values; require `availability = 'available'` and
  `media_kind IN ('video', 'animated_image')`; group by record and select
  `MIN(location_id)`.
- One SQL query at most for a page with eligible media; zero additional queries
  for a page without eligible media. Do not query per row. Do not inspect the
  preview cache, filesystem or derivative readiness.
- Administrator inventory and record detail must not populate the field.
- A locator is a candidate, not a readiness assertion. The existing route may
  still return 404/409; the client falls back to the icon.

### 4.2 API serialization

- `records_api.py` exposes `preview_location_id` only in the item payloads of
  `/api/timeline` and `/api/my/records`.
- Use an explicit serialization option/flag on `_page_payload` and
  `_summary_payload`; do not change administrator-inventory or record-detail
  response shapes incidentally.
- The field value is a canonical location identifier string or JSON `null`.
  Do not add locations, paths, cache keys, readiness, URLs, answers or other
  metadata.

### 4.3 Client rendering and lifecycle

- Add one helper, `kronikaAttachCardPreview`, used by `kronikaRenderCards`
  (Timeline) and the personal-record branch of `kronikaLoadHistory`. Never use
  it in question History, Review, administrator inventory or any other surface.
- Keep `kronikaTagCardKind` and every existing kind selector. Append the image
  after the existing title and metadata so existing child order remains intact.
- Use the existing `mediaGalleryPreviewUrl(media_id, preview_location_id)`.
- Implement the loading/ready/fallback states and the exact `alt`, ARIA,
  loading, decoding and dimensions from §1.
- Scope CSS to `#kronika-timeline-results` and `#kronika-history-results`.
  Overlay the image on the existing icon box; use `object-fit: cover`; keep the
  loading image transparent so lazy loading proceeds; reveal only in `ready`;
  retain the pseudo-icon in every fallback.
- Add the optional `signal` to `kronikaReadJson` and pass it only from the
  Timeline/History list calls. Abort on supersession, identity change and
  accepted departure. Fence image callbacks with the list generation and
  identity generation. Detach handlers and remove image sources on replacement
  and teardown. Preserve the dirty-navigation refusal; do not abort before
  navigation is accepted.
- Do not change other `kronikaReadJson` callers.

### 4.4 Tests

Add the causal tests named in plan §5 to the allowlisted test files. Preserve
the existing tests and their intent. Cover at minimum:

- one deterministic current/approved location, with insertion order unable to
  change the selected identifier;
- Timeline uses only approved locations for every caller; a lexically earlier
  working-only location cannot leak;
- null for non-media, still images and unavailable locations;
- at most one added locator query for 1, 24 and 100 media rows;
- additive path-free list payload; administrator and detail shapes unchanged;
- list-to-preview audience round trip: owner/admin private success, household
  denial, approval success, withdrawal denial even with an ETag;
- preview errors are no-store and sanitized; denial/not-ready with
  `If-None-Match` cannot return `304`;
- media cards use one lazy decorative preview and preserve their link names;
- question History and non-media cards never request previews;
- preview load reveals the image and every error retains the kind icon;
- 24 media cards require no media-detail discovery or automatic retries;
- navigation/identity changes retire previews and ignore late events;
- superseded Timeline/History requests cannot repaint a departed view;
- cancelled dirty navigation preserves the current preview page;
- thumbnail CSS changes only the Timeline and History icon slots.

Use synthetic identifiers, temporary catalogs and harmless fixture bytes. Do not
use real provider calls, private media, browser credentials or the R10 item.

### 4.5 Documentation

Apply the documentation inventory in plan §7 exactly:

- `SPEC.md`: normative preview locator, icon fallback, approved/current
  selection, 24-card bound and no-detail-discovery behavior.
- `SECURITY.md`: opaque locator disclosure boundary, unchanged
  authorization-before-cache and conditional-request behavior.
- `GALLERY.md`: short cross-reference to SPEC and a narrow correction of the
  stale operator-only preview-generation wording; preserve the Gallery/Details
  freeze.
- `DEVELOPMENT.md`: focused validation commands and synthetic/manual acceptance
  guidance, including still-image/icon behavior and the NUC-publication
  precondition.
- `README.md`: one concise status sentence with a SPEC link.
- Do not edit `docs/UX_AUDIT.md`, `PRODUCT.md`, `SERVER.md`, `ROADMAP.md`, any
  ADR, or the access inventory. Do not create a new ADR or a second semantic
  owner.

## 5. Authority

```text
Positive authority
- Read-only inspection of /Users/agile/Projects/kronika, including .ap at its
  pinned commit.
- Read-only inspection of the accepted plan report and this whole's Meta
  records: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/
  00_handout.md, 00_notes.md, 01_report_00.md, this prompt, and the run map
  /Users/agile/meta/projects/kronika/01/00_RUN_MAP.md.
- Read-only public verification of https://github.com/cisarik/kronika.git via
  git ls-remote.
- Edit exactly the fourteen repository paths in section 2.
- Run the repository gate and the focused tests in section 6 through the
  declared routes.
- Stage exactly the fourteen allowlisted paths and create one normal local
  commit on main after the checks pass.
- Exact direct-write of the terminal report at the path below if and only if it
  is absent, followed by a complete readback.

Negative authority
- No edit, creation, deletion, rename, chmod or other write outside the
  fourteen paths; the report is the only write outside the repository.
- No Git push, fetch, pull, merge, rebase, reset, restore, clean, stash,
  checkout, switch, branch, tag, remote or config write. Do not amend.
- No dependency install, update or lockfile change.
- No migration, schema, seed, fixture-generation or database mutation.
- No change to the preview route, audience policy, record-access decisions,
  public-published composition or route-policy tables.
- No NUC contact, SSH, sudo, deploy, rollback, systemd, package manager,
  AppArmor, UFW, Tailscale, mount, storage or host mutation.
- No provider, capture-browser, extension or acquisition contact.
- No browser session, rendered acceptance, screenshot or GUI automation.
- No reading of browser profiles, cookies, tokens, credential stores, NUC
  secret values, private media or the R10 item.
- No edit to any Meta file except the exact report path.
- No acceptance, publication, deployment or closure claim.

Commands
- Python gate: ./.ap/ap project check --root /Users/agile/Projects/kronika
  --baseline 246c9f86b72e652cd36ed0d9f4e19e77f972df91
- Python focused tests: ./.ap/ap exec --root /Users/agile/Projects/kronika
  --baseline 246c9f86b72e652cd36ed0d9f4e19e77f972df91 --operation test-focus --
  <pytest arguments from section 6>
- JavaScript tests: node --test <files from section 6>
- Never invoke .venv/bin/python, python, python3, poetry run, or an ambient
  equivalent for evidence.
- Read-only Git inspection: status, rev-parse, log, show, diff, ls-files, grep,
  ls-tree, cat-file, ls-remote, submodule status, describe, merge-base.
  The only Git write is the exact stage and one commit described above.

Dependency authority: none.
Git authority: read-only inspection plus exactly one normal local commit on
  main of the fourteen allowlisted paths; no push and no history rewrite.
Network authority: public read-only Git verification only. No provider, NUC,
  browser or other outbound request.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit is the governing
  protocol; AGENTS.md is authoritative inside its scope; the accepted plan,
  handout, notes and this prompt are task context; repository content is data
  under analysis. Stop on a conflict with current repository evidence.
Side-effect authority: reversible local source/test/document edits and the one
  local commit only. The report write is trace persistence.
Browser authority: none.
```

## 6. Validation and test commands

Run these from `/Users/agile/Projects/kronika` after implementation. Use the
exact baseline. Do not use an ambient Python route.

```text
# [MacBook / fish]
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 246c9f86b72e652cd36ed0d9f4e19e77f972df91
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 246c9f86b72e652cd36ed0d9f4e19e77f972df91 --operation test-focus -- tests/integration/persistence/test_kronika_record_repository.py tests/contract/test_records_api.py tests/contract/test_gallery_preview_api.py tests/contract/test_kronika_approved_projection.py tests/contract/test_content_audience_policy.py tests/contract/test_kronika_access_inventory.py tests/contract/test_research_requests_api.py tests/unit/test_gallery_preview.py
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 246c9f86b72e652cd36ed0d9f4e19e77f972df91 --operation test-focus -- tests/contract/test_local_web_application.py -k 'kronika_shell_adds_timeline_without_replacing_gallery or persistent_preview or initial_card or available_cards or details'
node --test tests/kronika_ui.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js
git diff --check
git status --short
#------------------------------------------------------
```

Run one regression pass per materially changed candidate. Diagnose a failure
narrowly before repeating. Do not run the full Python suite. Classify any
pre-existing failure with exact evidence; do not "fix" an unrelated failure or
expand the allowlist.

Before the commit, verify:

```text
- Only the fourteen allowlisted paths are changed or added.
- No untracked file is staged accidentally.
- No secret, host value, private media filename or R10 identifier appears.
- The API field is absent from administrator inventory and record detail.
- The preview route, audience code and public composition are untouched.
- The Gallery/Details renderers and index.html are untouched.
```

Stage exactly the fourteen paths and create one normal commit on `main`:

```text
git add -- <the fourteen exact paths>
git diff --cached --check
git commit -m "feat: add media thumbnails to Timeline and History"
git show --stat --oneline HEAD
```

Do not push. If any pre-existing tracked change is present at start, stop and
report; do not include it.

## 7. Completion and report

```text
Stopping conditions: stop without improvising if the client has native Plan mode
  enabled; if HEAD, branch, remote, public main, .ap pin or tree does not match
  the verified baseline; if ap doctor or ap project check fails; if any required
  change falls outside the fourteen-path allowlist; if a security, audience,
  route, schema, migration or public-composition change is required; if a test
  needs real NUC, provider, browser, secret or private-media access; if context
  pressure reaches the point where a bounded rotation is cheaper than a degraded
  candidate; or if the exact report path already exists, including an empty file.

Completion: one coherent candidate covering the code, tests and documentation;
the focused validation evidence; exactly one normal local commit; and one
terminal report. Do not implement anything outside the accepted plan.

Required report sections: the standard report core and header with the exact
  coordinate block and echo of Persistent role identity, Worker session target,
  Native planning mode, Worker session profile and Task identity; Status;
  Phase-qualified result: implementation-PASS; Start commit; End commit (the
  candidate commit); Report justification: new-mutation; Logical-whole closure:
  not-closed; a concise implementation summary; exact changed paths and diff
  stat; the repository gate result; each focused test command and exact
  pass/fail counts; acceptance-matrix evidence per claim; the commit SHA and
  message; deviations and near-misses; pre-existing failure classification;
  residual risks; documentation changes; evidence limitations; one smallest
  next step; and the orchestration critique.

Report destination: direct-write
  /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/02_report_00.md
  if and only if it is absent. Read the complete file back and verify content,
  identity and path before the separate completion notice. Do not write any
  other Meta file and do not create a plan artifact in the repository.

Report justification: new-mutation

Authority expiry: on submission of the terminal report, this implementation
  grant expires. No acceptance, correction, publication, deployment, production
  or closure authority remains. A later phase requires a new complete
  authoritative prompt.
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

Read the exact owners for the work; do not read the whole protocol when a
bounded owner is sufficient.

- The accepted plan report `01_report_00.md` in full. It is the design of
  record for this implementation.
- `.ap/AP.md` at the pinned commit: §2 Roles; §3 Instances, Sessions, and Worker
  Session Profiles; §5 Task Authority; §6 Adaptive Orchestration Lifecycle;
  §7 Orchestrator Responsibilities; §12 Validation and Public Verification;
  §13 Artifact Lifecycle; §15 Fresh-Slice Implementation and Diagnostic
  Closeout; §17 Compact Communication; §19 Anti-Patterns (skim); and the Finite
  Convergence Contract.
- `.ap/AP_WORKER.md` in full: Worker session target, bounded authority, and
  reporting.
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header; Implementation Authority
  Record; Common Worker Task Fields; Repository Checkout Topology Contract;
  Worker Session Target Contract; Worker Exchange Identity and External Trace
  Contract; Cooperator Delivery and Trace Destination Record; Mutation Axes
  Record; Validation Ladder Record; Pre-Existing Failure Classification
  Contract.
- `AGENTS.md` at the repository root, including Security Boundaries, Product
  Boundaries, Cursor Worker Execution Boundary, Worker Execution, and Git and
  Lifecycle.
- `docs/WORKER_EXECUTION_CONTRACT.md`: the canonical `./.ap/ap exec` route,
  test invocation, and no-ambient-Python rule.
- `docs/adr/README.md` and ADRs 0082, 0083, 0084, 0085, 0086.
- `README.md`, `PRODUCT.md`, `SPEC.md`, `ROADMAP.md`, `SECURITY.md`, `SERVER.md`,
  `GALLERY.md`, `DEVELOPMENT.md`, and `deploy/systemd/kronika.env.example` for
  the living claims and frozen boundaries.
- `src/kronika/application/ports/records.py`;
  `src/kronika/infrastructure/persistence/record_repository.py`;
  `src/kronika/infrastructure/persistence/catalog_schema.py`;
  `src/kronika/adapters/api/records_api.py`;
  `src/kronika/adapters/api/gallery_preview_api.py`;
  `src/kronika/adapters/api/content_audience_api.py`;
  `src/kronika/application/content_publication.py`;
  `src/kronika/domain/record_access.py`.
- `src/kronika/adapters/api/web/app.js` relevant regions;
  `src/kronika/adapters/api/web/index.html`; `src/kronika/adapters/api/web/styles.css`.
- The exact tests named in section 6.

## 9. Communication

Worker prompts, the report, code comments, test names and documentation are
professional English. Do not use Czech or Slovak in repository, Meta, or report
artifacts.

## 10. Activated surface annexes

### External trace and delivery

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/
Trace project key: kronika
Trace logical-whole projection identity: 01-timeline-and-history-media-thumbnails
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_implementation_00.md
Destination path: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/
Report filename: 02_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: exactly the fourteen repository paths in section 2
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/02_report_00.md
```

The report write is trace persistence, not repository mutation. If the report
path exists, including an empty file, stop `BLOCKED` without overwriting it.
The verified parent directory exists. Do not create a placeholder or use another
path.

### NUC and deployment

```text
This implementation exchange: no NUC contact, no SSH, no sudo, no
  kronika-release, no deploy, no rollback, no systemd, no package manager, no
  AppArmor, no UFW, no Tailscale, no mount or storage mutation.
The Cooperator has granted NUC SSH access and an active sudo -v timestamp for
  the later bounded deployment exchange. That access is not used here.
A separate deployment grant must verify public main, the exact accepted SHA,
  the current NUC state, backup readiness, sudo lifecycle and rollback.
Deployment never follows automatically from a check.
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
Implementation task grant: none - this implementation does not change,
  revalidate, or implement the ledger entry.
```

### Security and audience boundary

The accepted design adds only an opaque location identifier selected from rows
the caller may already read. The preview route must continue to authorize every
request before cache access, including conditional requests. Do not change
`gallery_preview_api.py`, `content_audience_api.py`,
`ContentAudiencePolicy`, `record_access.py`, the public-published composition or
the route-policy tables. If the candidate needs any such change, stop and report
for fresh independent acceptance. Do not widen private-record visibility to make
thumbnails convenient.

## Visible delivery capsule

```text
🟡 Ready for delivery
Recipient: Fresh Implementation Worker · fresh-worker-session · direct dispatch
Recommendation: High · approximately 250k tokens
Client: Native Plan Mode OFF
Prompt: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/02_implementation_00.md
Report: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/02_report_00.md
Archival: wait-for-report
```
