# S8 Implementation Grant — Unified Kronika UI/UX (kronika-one-product, session 53)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 53
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S8-IMPLEMENTATION
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risks: navigation/state integration across a large vanilla shell, access-sensitive summary projections and the local identity echo, and the Gallery/Details regression surface. The Planner's Extra High suggestion is noted; Extra High remains reserved for a genuine unresolved cross-cutting contradiction.
Recommended context capacity: approximately 1M tokens
Independence required: no

## Implementation authority record

```text
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: ade1169b4ba079bb1df540a929572ca58e777d16
Changed-path allowlist: the exact 20 paths in "Exact allowlist" below
Implementation boundaries: the positive and negative authority in this grant
Independence required: no
```

## Accepted plan (frozen)

The frozen S8 plan is `52_report_00.md` in the activated trace
(`/Users/agile/meta/projects/kronika/00/02-kronika-one-product/52_report_00.md`,
persisted by the Orchestrator from the Planner's exact relayed content;
SHA-256 `d064848b72833db8c0ae8ae525d03fd9242393c419e468e21e2d86f67ccc430f`).
The Planner's report status remains PARTIAL as written (its file-delivery gap
was closed by the Orchestrator persisting the exact content); the plan itself
is complete and the Orchestrator accepts and freezes it.

**Sections 3–8 of the frozen plan are binding design.** Section 9's proposed
grant is superseded by this grant, which is the sole execution authority. Read
the plan in full before editing.

Cooperator-confirmed decisions to carry: new UI copy is **English**, consistent
with the existing shell; shell branding is **Kronika** in the title, accessible
header labels and a visible wordmark, while preserving the existing brand-mark
graphic including its `FN` monogram. No package, header, storage-key,
deployment-identity or repository renames.

## Goal (one coherent outcome)

Implement the complete S8 unified Kronika UI/UX exactly as frozen in the plan:
the Timeline landing (administrator-approved records only), the separate
personal history, the Search and Research forms, the completed-document view,
and the administrator review queue, inside the existing packaged web shell,
together with the minimal additive record-summary/list-filter and
local-identity changes the plan requires, plus the causal tests and the
regenerated access inventory.

## Exact allowlist (20 paths; no additions, no wildcards)

```text
src/framenest/adapters/api/web/index.html
src/framenest/adapters/api/web/styles.css
src/framenest/adapters/api/web/app.js
src/framenest/adapters/api/application.py
src/framenest/adapters/api/records_api.py
src/framenest/application/ports/records.py
src/framenest/application/records.py
src/framenest/infrastructure/persistence/record_repository.py
tests/contract/test_local_web_application.py
tests/contract/test_records_api.py
tests/contract/test_local_record_identity.py
tests/contract/test_kronika_access_inventory.py
tests/integration/persistence/test_kronika_record_repository.py
tests/kronika_ui.test.js
README.md
PRODUCT.md
SPEC.md
ROADMAP.md
SERVER.md
docs/KRONIKA_ACCESS_INVENTORY.md
```

`tests/kronika_ui.test.js` is the only new file. Every other path exists at the
baseline. Any required change outside this list is a stop: report it and wait
for an amended grant; do not edit beyond the list.

## Required implementation (binding design summary)

Follow the frozen plan's sections 3–8 exactly. Key points repeated here for the
grant's self-containment (the plan remains the detailed owner):

- Client routes are hash fragments of the existing `/` page
  (`#/timeline`, `#/gallery`, `#/history`, `#/history/records`, `#/search`,
  `#/research`, `#/requests/{operation_id}`, `#/records/{record_id}`,
  `#/review`, `#/review/shared`, `#/review/requests`, `#/details/{media_id}`).
  Timeline is the normal landing view; Gallery stays reachable and frozen.
- **No new HTTP route.** No `ROUTE_POLICIES` change is expected; if a new route
  turns out to be genuinely necessary, stop for an amended grant.
- Additive record interfaces: `display_title: string | null` and
  `content_category: "general" | "meme" | "movie" | "youtube" | null` on
  summaries; optional `kind` and `content_category` filters for lists;
  `visibility` filter only for the administrator inventory; filters applied
  before count and pagination; Timeline titles/categories from the approved
  projection for every caller; no answers, documents, citations, filenames or
  location paths in list payloads.
- Identity: echo the verified `IdentityContext` in the existing `audience_me`
  response for configured loopback callers; preserve the no-local-owner
  response and all Tailscale/public boundaries.
- Shell: one navigation owner after `identityReady`; separate state per view;
  generation/guards against late responses; serial polling controller for the
  active request; sandboxed iframe (`sandbox=""`, `referrerpolicy="no-referrer"`)
  receiving render HTML via `srcdoc` with the trusted CSP meta
  (`default-src 'none'; style-src 'unsafe-inline'; img-src data:; base-uri 'none'; form-action 'none'`);
  citations only as user-activated validated links; stable error copy as
  specified; approve/withdraw only with `expected_version` and reload-on-409.
- Accessibility and responsive behavior per plan section 6; no restyle of
  Gallery, Details or player selectors.
- Docs: update the five living documents only to distinguish implemented
  S6/S4-B/S7-P foundations, the S8 candidate's actual validation, separate
  acceptance/publication/deployment, and research-disabled/S9 status; do not
  claim acceptance.

## Positive authority

- Read any repository, AP, trace and test file needed for this task.
- Edit exactly the 20 allowlisted paths.
- Create only `tests/kronika_ui.test.js` (and the regenerated inventory content
  inside its allowlisted path).
- Use disposable synthetic fixtures and fake providers only.
- Execute the validation in this grant through the declared routes.
- Inspect diffs; explicitly stage accepted allowlisted paths; create exactly
  one local commit with the exact subject below.
- Persist the terminal report if the client permits it (see delivery record).

## Negative authority

No changes outside the allowlist; no new HTTP routes; no dependencies,
lockfiles, toolchain, migrations, AP pin or managed-block changes; no
`private/**`, credentials, secrets, live provider calls, network calls or API
keys; no NUC/SSH/sudo or capture state; no browser or server launch outside the
authorized test execution; no deployment, publication, push, fetch, merge,
rebase, reset, clean, stash, force operation or branch change; no `git add .`
or `git add -A`; no subagents.

## Validation (declared route; testing economy binding)

Repository gate first: root `/Users/agile/Projects/framenest`, branch
`feat/kronika-one-product`, HEAD `ade1169b4ba079bb1df540a929572ca58e777d16`,
tree `f266df7205ddea5b83de7e6cd8313512ce70bcb1`, clean index and worktree
including untracked files, AP gitlink and `.ap` HEAD
`73e20ef80b88700d5fcbc397cd8edd4fc425869f`. Classify any difference per RF-12
and stop on unexplained divergence.

```text
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline ade1169b4ba079bb1df540a929572ca58e777d16

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline ade1169b4ba079bb1df540a929572ca58e777d16 --operation test-focus -- tests/contract/test_local_web_application.py tests/contract/test_records_api.py tests/contract/test_research_requests_api.py tests/contract/test_local_record_identity.py tests/contract/test_kronika_access_inventory.py tests/contract/test_kronika_record_authorization.py tests/contract/test_kronika_approved_projection.py tests/contract/test_web_package_resources.py::test_web_resources_are_available_from_package_resource_boundary tests/contract/test_public_published_uds.py::test_unlisted_routes_and_methods_are_uniform_404 tests/contract/test_public_published_uds.py::test_workspace_tcp_audience_bootstrap_is_trusted_loopback tests/integration/persistence/test_kronika_record_repository.py tests/unit/application/test_records.py tests/unit/application/test_document_rendering.py -q -p no:cacheprovider
```

JavaScript (declared repository route; there is no `package.json`):

```text
node --test tests/kronika_ui.test.js
node --test tests/gallery_loading_states.test.js tests/metadata_form_contract.test.js
node --test tests/*.test.js          # exactly once, final candidate, browser gates unset
```

- Run narrower affected Python/JS targets while editing; run the focused Python
  set once on the final candidate. Do not run the broad Python suite.
- The inventory contract test may rewrite `docs/KRONIKA_ACCESS_INVENTORY.md`;
  inspect and include that exact generated change.
- Do not set `FRAMENEST_RUN_BROWSER_EVIDENCE`; gated browser suites stay
  skipped and are not rendered acceptance.
- Stop on a causal regression rather than weakening an existing test.
- No ambient Python, `.venv` bypass, environment reconstruction, `poetry run`
  or live service/provider. If an ambient route fails, classify per
  `docs/WORKER_EXECUTION_CONTRACT.md` and retry once through the declared
  `./.ap/ap` route.

## Git authority

Stage only the 20 allowlisted paths by exact path (inspect
`git diff --cached --name-only`, `--check` and the full staged diff). Verify
the AP pin and managed block are unchanged. Create exactly one commit:

```text
feat(kronika): add unified timeline history and review UI
```

Do not push. Report the commit SHA and tree.

## Delivery record

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 53_implementation_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 53_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Stopping conditions

Stop and report (PARTIAL/BLOCKED) on: baseline/branch/pin drift or divergence
requiring classification; client Plan mode being active (native planning mode
must be not-used for this implementation; if Plan mode is active, stop before
editing and report the routing mismatch); any required change outside the
allowlist; a genuinely necessary new HTTP route; a Gallery/Details/player
regression; an authorization, projection or rendering failure; the declared
execution route being unavailable with no lawful alternative; validation that
would require a forbidden action; or a second equivalent blocker cycle. Do not
repair unrelated pre-existing failures; report them.

## Completion and report contract

PASS means: the frozen S8 behavior is implemented inside the allowlist; the
focused Python set exits 0; the one final `node --test tests/*.test.js` run
exits 0 with browser suites skipped; the regenerated inventory is included; one
local commit with the exact subject exists; and the terminal report is
delivered. Implementation evidence is non-independent; do not claim acceptance,
publication or deployment.

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 53, 01), and carries the compact core:
status; `Phase-qualified result: implementation-PASS | not-applicable`; start
commit `ade1169…` and end commit (the created commit); changed files; tests and
validation with exact commands and totals; commit result (local only, no
push); deviations, risks and missing evidence; smallest next step; `Report
justification: new-mutation`; critique; issues or none; `Logical-whole closure:
not-closed`; authority expiry.

Finish: finalize the report, save it exactly at the report path if the client
permits, read back the full saved content, verify first line, coordinates and
path, then send a short separate completion notice with status, location and
SHA-256. If the client prohibits the write, preserve the complete content in
chat, mark the delivery limitation PARTIAL, and stop; do not bypass the
control. If the destination exists, stop and report instead of overwriting.

Authority expiry: the terminal report, cancellation or supersession ends this
grant; no autonomous continuation. The Cooperator archives the exact
prompt/report pair after the report exists; this grant gives no Git publication
authority.
