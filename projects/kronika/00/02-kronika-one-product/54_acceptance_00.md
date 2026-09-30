# S8 Independent Audit Grant — Exact Candidate 7f7aae9 (kronika-one-product, session 54)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 54
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S8-AUDIT
Delivery route: manual Cooperator delivery
Reasoning recommendation: Extra High — independent R3 acceptance over access-sensitive summary projections, the local identity echo, the submission/polling lifecycle and rendering isolation
Recommended context capacity: approximately 1M tokens
Independence required: yes

## Acceptance and Correction Record

```text
Acceptance candidate: 7f7aae9012d35671b062c8731e9009169501d4d0
  (tree 17a559dff621882ac561a9901d20fe5b824508c4, branch feat/kronika-one-product,
   parent ade1169b4ba079bb1df540a929572ca58e777d16)
Acceptance owner map: delta ade1169b4ba079bb1df540a929572ca58e777d16..7f7aae9012d35671b062c8731e9009169501d4d0
  (one commit, 20 paths, +3311/-40); the frozen plan 52_report_00.md and the
  implementation prompt 53_implementation_00.md are evidence only
Acceptance allowlist: read-only review; the declared focused Python route; the
  bounded JavaScript set below; one temporary probe root
  /tmp/kronika-one-product-s8-audit (mode 0700, synthetic data only, removed)
Acceptance risk claims: the fixed claims C1–C12 below
Acceptance control matrix: the controls in this grant
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none beyond the controls below
Out-of-scope observations: ledger-candidates
```

This session did not implement, correct or plan the audited slice. The
implementation report is a claim, not proof. No correction authority is
granted; do not edit any repository file.

## Security audit record

```text
Security task class: focused defensive audit (R3), with authorization and
  rendering specializations; the provider-boundary specialization is limited to
  the no-live-call posture because S8 makes no provider calls
Owned/authorized target: /Users/agile/Projects/framenest at the candidate,
  read-only
Commit under audit: 7f7aae9012d35671b062c8731e9009169501d4d0
Scope: the one-commit delta from ade1169b4ba079bb1df540a929572ca58e777d16
Exclusions: NUC, SSH, sudo, browser launch, live provider, credentials,
  private/**, broad Python suite, correction
```

```text
Assets: record summaries and titles, private/family visibility decisions,
  owner identity, the local identity context, research submission identity and
  idempotency, rendered question/answer documents, the frozen Gallery/Details UX
Trust boundaries: caller to records HTTP list/detail/render; authenticated
  local loopback identity to audience response; browser to provider-boundary
  forms (no call); untrusted render HTML into a sandboxed frame; administrator
  approval mutation
Attacker-controlled inputs: query filters (kind, content_category, visibility,
  limit, offset), record ids, stored question/answer text and titles, provider
  output later rendered, forged identity headers
Security properties: Timeline approved-only for every caller; approved
  projection titles/categories for every caller; no answer text or documents in
  list payloads; owner isolation for own history; administrator inventory gated;
  local identity echo only from an attached verified IdentityContext; one
  client_request_id per deliberate attempt; render HTML only inside a sandboxed
  frame with effective CSP; versioned approve/withdraw; fail-closed routes
Abuse cases: cross-owner title/count leak; private record on the Timeline;
  working metadata leaking through the approved projection; answer text via
  lists; fabricated local identity; double-charging via a replaced request id;
  script execution via render; stale approval overwrite; administrator routes
  reachable without capability
```

## Candidate and repository gate

```text
Root: /Users/agile/Projects/framenest
Remote: https://github.com/cisarik/framenest.git
Branch: feat/kronika-one-product
Expected HEAD: 7f7aae9012d35671b062c8731e9009169501d4d0
Expected tree: 17a559dff621882ac561a9901d20fe5b824508c4
Expected parent: ade1169b4ba079bb1df540a929572ca58e777d16
AP gitlink and .ap HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
Required state: clean index and worktree including untracked files
Public refs (read-only ls-remote, one call): main and feat/kronika-one-product
are expected to remain ade1169b4ba079bb1df540a929572ca58e777d16; the candidate
is local-only and must not be pushed
```

Independently verify all of it. Classify any difference per RF-12; stop on
unexplained divergence. No Git write of any kind.

## Fixed claims (one verdict per claim)

**C1 — Candidate identity, containment and leak hunt.** SHA, tree, parent and
branch match; the delta is exactly the 20 allowlisted paths (19 modified, 1
added `tests/kronika_ui.test.js`); no protected path, migration, dependency,
lockfile, AP or deployment-path change; worktree clean; no push. Leak hunt on
added production lines finds no secret, credential value, private path or
private payload.

**C2 — Summary projection.** `display_title` and `content_category` are
derived as frozen: Search/Research from the immutable question (whitespace
collapsed, at most 240 Unicode code points, ellipsis within the limit); media
from persisted metadata; absent stays null. List payloads carry no answer text,
full document, citations, filenames or location paths. Hostile title text
remains data (escaped where rendered as HTML).

**C3 — Timeline approved-only for every caller.** `/api/timeline` returns only
approved family records for owner, ordinary household member and administrator;
withdrawal removes them for every caller; Timeline summaries use the approved
projection for every caller (`read_decision` approved) while detail/Gallery
authorization is unchanged; a post-approval working-metadata change does not
alter the Timeline title/category/filter until reapproval.

**C4 — Filter validation and query correctness.** `kind` and
`content_category` are validated; `content_category` requires `kind=media`;
invalid or unauthorized combinations return sanitized 422 `INVALID_REQUEST`;
`visibility` filtering exists only on the administrator inventory; own history
retains the caller-owner predicate even for administrators; the administrator
gate is retained; filters apply before count and pagination; limit/offset bounds
(default 24, maximum 100) and stable ordering are preserved.

**C5 — Local identity echo.** `/api/audience/me` echoes the attached verified
`IdentityContext` and mapped capabilities only for the configured local-owner
(trusted-loopback) composition; the previous no-local-owner response and all
Tailscale/public boundaries are unchanged; forged headers, missing identity or
non-loopback callers cannot manufacture identity or administrator authority.

**C6 — Shell routing and state isolation.** Timeline is the landing view on the
workspace composition; Gallery remains reachable and its state/player behavior
is retained; `#/details/{id}` and the companion hooks still work; late
responses from older routes or identities cannot overwrite current view state;
administrator/own data cannot populate the Timeline; identity loss clears
protected content; no new HTTP route exists and `ROUTE_POLICIES` is unchanged
with the fail-closed fallback intact.

**C7 — Submission idempotency.** The shell freezes one `client_request_id` per
deliberate attempt before its first POST; a transport-failure retry reuses the
identical frozen body and id; editing or a new attempt requires a new id; double
submission is prevented; `consent_version` (`kronika-research-v1`) is sent only
after acknowledgement and is not claimed to be stored; the prompt byte bound
(16,384 UTF-8 bytes) is enforced with `TextEncoder`.

**C8 — Polling and cancellation.** Active states are exactly `admitted`,
`submitting`, `running`, `validating`, `cancel_requested`; terminal states are
exactly `saved`, `refused`, `failed`, `incomplete`, `cancelled`, `timeout`,
`submission_unknown`; polling is serial (five seconds after the previous settle,
no overlap, detail GET only); it pauses on hidden/identity loss and stops on
unknown states; three consecutive transport failures pause with a resume path; a
failed status fetch is not presented as a failed operation; `cancel_requested`
keeps polling; `saved` requires `record_id` and does not auto-navigate or mutate
the Timeline.

**C9 — Rendering isolation.** The render response is fetched first and assigned
only to a sandboxed iframe (`sandbox=""`, `referrerpolicy="no-referrer"`)
`srcdoc` inside a trusted wrapper with the CSP meta
`default-src 'none'; style-src 'unsafe-inline'; img-src data:; base-uri 'none'; form-action 'none'`;
citations are DOM-built validated `http`/`https`/`mailto` links with
`noopener noreferrer` and are never prefetched; generated HTML never enters the
application DOM; a render failure preserves the question and offers retry, and
never presents a partial answer as complete.

**C10 — Approval flow.** The review UI offers only approve/withdraw using the
displayed `expected_version`; `changed: false` is accepted; a 409 shows a
conflict, disables the stale action and requires reload plus a second deliberate
action; no automatic resubmit or version substitution; `reject` is not offered;
unready records are not approvable.

**C11 — Route policies and inventory.** The route set is unchanged; the
regenerated `docs/KRONIKA_ACCESS_INVENTORY.md` states the Timeline projection
truthfully (approved projection for every caller) and contains no generic
placeholders; the public composition still excludes record/research routes; the
fail-closed fallback is intact.

**C12 — Non-regression.** The declared focused Python set exits 0 on the
candidate (independently re-run); the bounded JavaScript set exits 0; existing
Gallery/Details/player selectors are not restyled (verified from the diff
scope); no sanctioned test was weakened; the new `tests/kronika_ui.test.js`
harness extracts and executes production functions rather than reproducing the
production state machine.

## Required controls (minimum)

```text
git rev-parse HEAD 'HEAD^{tree}' HEAD^; git status --porcelain --untracked-files=all
git log --oneline -3; git diff --name-status ade1169…..HEAD; git show HEAD
GIT_TERMINAL_PROMPT=0 git ls-remote <remote> refs/heads/main refs/heads/feat/kronika-one-product
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 7f7aae9012d35671b062c8731e9009169501d4d0

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 7f7aae9012d35671b062c8731e9009169501d4d0 --operation test-focus -- tests/contract/test_local_web_application.py tests/contract/test_records_api.py tests/contract/test_research_requests_api.py tests/contract/test_local_record_identity.py tests/contract/test_kronika_access_inventory.py tests/contract/test_kronika_record_authorization.py tests/contract/test_kronika_approved_projection.py tests/contract/test_web_package_resources.py::test_web_resources_are_available_from_package_resource_boundary tests/contract/test_public_published_uds.py::test_unlisted_routes_and_methods_are_uniform_404 tests/contract/test_public_published_uds.py::test_workspace_tcp_audience_bootstrap_is_trusted_loopback tests/integration/persistence/test_kronika_record_repository.py tests/unit/application/test_records.py tests/unit/application/test_document_rendering.py -q -p no:cacheprovider

node --test tests/kronika_ui.test.js tests/gallery_loading_states.test.js tests/gallery_filter_controls.test.js tests/gallery_search_tag_filters.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/metadata_form_contract.test.js tests/metadata_alias_edit.test.js tests/catalog_card_ai_quick_action.test.js tests/tailscale_identity_frontend.test.js
```

The bounded JavaScript set is the acceptance control; a full JS run is not
required unless a named unresolved concern appears. The broad Python suite is
not run. Do not set `FRAMENEST_RUN_BROWSER_EVIDENCE`; browser suites stay
skipped. No NUC, sudo, browser or provider activity.

Dynamic probes are permitted only under the declared synthetic probe root with
synthetic identities, records and metadata (no real private data, no live
database, no provider). Prefer the repository's existing local-identity test
harness (`tests/contract/test_local_record_identity.py`) and a synthetic SQLite
catalog. Intended probe outcomes: audience echo on/off; Timeline approved
projection for owner/member/admin with a changed working title; list payloads
without answer fields; invalid filter 422; cross-owner exclusion.

## Evidence and verdict rules

- Baseline and final mutable state must be recorded; recheck after probes.
- Each claim receives `established`, `not established`, or `partial` with its
  exact evidence; unsupported inference is not evidence.
- A finding uses the full security finding record (ID, severity, confidence,
  evidence class, reachability, preconditions, privileges, impact, CWE/ASVS
  none-or-versioned, reproduction, false-positive analysis, exploitability,
  smallest safe correction direction, residual risk, acceptance-blocking
  decision). An audit never repairs.
- Out-of-scope observations are recorded as non-authorizing ledger candidates.
- Verdict: `acceptance-PASS` only when all claims are established; otherwise
  `PARTIAL` or `BLOCKED` with the exact missing evidence.
- Report `Phase-qualified result: acceptance-PASS | not-applicable`,
  `Logical-whole closure: not-closed`, `Report justification: final-acceptance`.

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
Downloadable prompt filename: 54_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 54_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Stopping conditions

Stop and report (PARTIAL/BLOCKED) on a failed repository gate, unexplained
divergence, any need to mutate the candidate, a required capability that is
unavailable through the declared routes, or a finding that requires correction
authority. Do not audit an audit; do not expand into unknown-unknown hunting.
Missing browser-rendered evidence is expected (rendered acceptance belongs to
Michal after the NUC serves the exact public main) and must be stated as
missing, never converted to PASS.

## Completion and report contract

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 54, 01), and includes the compact core,
the Acceptance and Correction Record, the Security audit record with threat
model, per-claim verdicts C1–C12 with evidence, the control matrix results, the
containment ledger, limitations, residual-risk summary, compact critique, and
authority expiry. Save the report exactly at the report path if the client
permits; read back the full saved content and verify first line, coordinates and
path; otherwise preserve the complete content in chat and mark the delivery
limitation PARTIAL. Send a short separate completion notice with status,
location and SHA-256. No correction, publication, deployment or further audit
is authorized by the report.

Authority expiry: the terminal report ends this audit exchange.
