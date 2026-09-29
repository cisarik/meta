# KRONIKA-ONE-PRODUCT-S7-P-PLAN — frozen implementation plan for common completion and rendering (autonomy mode)

## Identity and route

Persistent role identity: ORCHESTRATOR (planning and execution under the
Cooperator's 2026-09-28 autonomy directive)
Logical whole identity: kronika-one-product
Worker session ordinal: 49
Worker exchange ordinal: 01
Phase: planning (implementation plan freeze)
Task identity: KRONIKA-ONE-PRODUCT-S7-P-PLAN

## Basis

`ROADMAP.md` S7-P: common completion and rendering — atomic Q/A save,
personal-history APIs, media-success/approval integration, safe document
rendering. `25_report_00.md` owns the HTTP contract, access policy and
rendering requirements. S6 already provides the durable records, the
owner/admin/household policy, approval/withdrawal and the record read models
(`RecordService`/`SqliteRecordRepository`) — none of them are exposed over
HTTP yet. S4-B provides the research runtime and coordinator; completion
currently stops at the `PendingResearchResultCompletion` placeholder.

## Scope of S7-P

In scope: research request submission/status/cancel APIs; personal-history,
Timeline, record-detail, admin-inventory and administrator-approval APIs; the
atomic Q/A completion adapter binding documents, records and research
requests; a safe bounded Markdown renderer for completed documents; the two
new capabilities; router composition; the executable access inventory update;
tests.

Out of scope: any UI (S8); provider live calls and credentials; media
analysis runtime changes; capture; the S9 database reset; publication and
deployment.

## Work packages

W1. Capabilities (`domain/identity_access.py`): add `research.run` (user and
admin) and `records.approve` (admin). Membership assertions stay valid; audit
tests updated only if they assert an exact set.

W2. Atomic completion (`application/records.py`,
`infrastructure/persistence/record_repository.py`): implement the
`ResearchResultCompletion` port as an adapter that, in one `BEGIN IMMEDIATE`
transaction, creates the `kronika_documents` row (question = request prompt,
answer = validated answer text, citations and completion evidence JSON from
`ResearchAnswer`), creates the `kronika_records` row (kind `search`/`research`,
server-derived owner from the stored request, final operation id = request
operation id) and sets `research_requests.record_id`; an exact replay returns
the existing binding without a second document. The coordinator's placeholder
is replaced; `VALIDATING` checkpoints retry safely.

W3. Research APIs (`adapters/api/research_api.py`, new):
- `GET /api/research/capabilities` — enabled/selected provider status,
  supported kinds, limits and retention notice; no live probe, no credential
  values; safe when the runtime is disabled.
- `POST /api/research-requests` — `{kind, prompt, client_request_id,
  consent_version}`; identity required with `research.run`; owner derived
  server-side; returns 202 with the request summary; typed refusals
  (`E_DISABLED`, `E_NOT_CONFIGURED`, `E_BUSY`, `E_IDEMPOTENCY_CONFLICT`,
  `E_BUDGET_EXCEEDED`, `E_INVALID_REQUEST`).
- `GET /api/research-requests` — caller history (pending, failed, complete).
- `GET /api/research-requests/{id}` — owner or administrator.
- `POST /api/research-requests/{id}/cancel` — owner or administrator.
- `GET /api/admin/research-requests` — administrator inventory.
The admission route also nudges the coordinator
(`submit_pending()`), so a single-process runtime makes progress without a
background loop; failures are surfaced as request state, not HTTP errors.

W4. Records APIs (`adapters/api/records_api.py`, new):
- `GET /api/my/records` — caller's records (owned media and completed Q/A),
  paged.
- `GET /api/timeline` — approved household records only, including for
  administrators.
- `GET /api/records/{id}` — owner/admin current state or the approved
  household projection.
- `GET /api/records/{id}/render` — the same authorization; returns the safe
  rendered HTML of the question/answer document.
- `GET /api/admin/records` — administrator inventory.
- `POST /api/admin/records/{id}/approval` — `{action, expected_version}`;
  explicit administrator mutation with the S6 approval rules.
All routes use the existing `SCOPE_IDENTITY` seam and the S6 policy; missing
identity fails closed.

W5. Safe rendering (`application/document_rendering.py`, new): bounded
Markdown subset (headings, paragraphs, lists, emphasis, inline code, fenced
code, blockquotes, links) converted to escaped HTML with safe URL schemes
only (`http`, `https`, `mailto`); raw HTML is escaped, never passed through;
output size bounded by the answer limit. No new dependency.

W6. Composition (`adapters/api/application.py`): register both routers, pass
the record service and the research runtime, replace the completion
placeholder with the W2 adapter. Disabled/unconfigured research stays inert:
capabilities says disabled, submission is refused with `E_DISABLED`, other
routes are unaffected.

W7. Inventory (`docs/KRONIKA_ACCESS_INVENTORY.md`,
`tests/contract/test_kronika_access_inventory.py`): regenerate the inventory
with the new routes, identity source, capability, policy, projection, and one
positive and one negative behavioral test per route; no generic placeholders.

W8. Tests:
- `tests/contract/test_research_requests_api.py` — submission, idempotency,
  capability denial, anonymous denial, history separation, cancel, admin
  read-all, disabled-runtime refusal.
- `tests/contract/test_records_api.py` — own history, admin inventory,
  timeline approved-only, detail owner/admin/household/denied, render
  authorization and injection safety, approval mutation rules.
- `tests/contract/test_research_completion.py` — atomic document+record+
  binding, replay idempotency, coordinator integration with a fake provider
  through the completion adapter.
- `tests/unit/application/test_document_rendering.py` — rendering cases and
  injection vectors.

## Exact path allowlist

```text
src/framenest/domain/identity_access.py
src/framenest/application/records.py
src/framenest/application/document_rendering.py
src/framenest/infrastructure/persistence/record_repository.py
src/framenest/adapters/api/research_api.py
src/framenest/adapters/api/records_api.py
src/framenest/adapters/api/application.py
docs/KRONIKA_ACCESS_INVENTORY.md
tests/unit/test_identity_access.py
tests/contract/test_kronika_access_inventory.py
tests/contract/test_kronika_record_authorization.py
tests/contract/test_research_requests_api.py
tests/contract/test_records_api.py
tests/contract/test_research_completion.py
tests/unit/application/test_document_rendering.py
```

No other path may change. Any required expansion is recorded in the trace
before the edit.

## Validation

Targeted only; no full suite. Declared route with the current baseline
`0a7d3f0`; focused files from the matrix above plus the S6 record
authorization and inventory tests. Implementation evidence tier E2,
non-independent under the autonomy directive.

## Stops

Out-of-allowlist edit; any live provider call or credential value handling;
weakening of the S6 authorization gate; raw HTML or script passthrough;
unexplained failing gate; client mode blocking writes.

## Next step

Implement in bounded commits: (1) capabilities + rendering + tests;
(2) completion adapter + tests; (3) research APIs + tests; (4) records APIs +
inventory + tests; (5) composition wiring + final validation; then the S7-P
trace report `50_report_00.md`.

## Allowlist amendment 1 (recorded during implementation)

The `0035` migration-head ripple additionally requires the production
public-composition schema gate:

```text
src/framenest/adapters/api/public_published_application.py
```

Progress: WP1 (capabilities + rendering) commit `8a277a3`; WP2 (atomic
completion adapter, placeholder replacement, ripple fix) commit `f1ec367`.
