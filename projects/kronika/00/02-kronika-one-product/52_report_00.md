### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product  
Worker session ordinal: 52  
Worker exchange ordinal: 01  

# S8 — Unified Kronika UI/UX implementation plan

## 1. Result and verified baseline

**Status: PARTIAL — the implementation plan is complete; required file delivery is incomplete.**

The active client Plan Mode prohibits filesystem writes. This complete terminal report is therefore delivered in chat under the grant’s explicit fallback. No report file was created, no saved-file readback occurred, and no saved-file SHA-256 is available.

Intended destination: `/Users/agile/meta/projects/kronika/00/02-kronika-one-product/52_report_00.md`. The destination was absent at both checks.

| Field | Result |
|---|---|
| Persistent role / profile | WORKER / Planner |
| Task identity | `KRONIKA-ONE-PRODUCT-S8-PLAN` |
| Phase-qualified result | `not-applicable` |
| Logical-whole closure | `not-closed` |
| Report justification | `new-evidence` |
| Native planning mode | Requested: `required`; observed: active client Plan Mode |
| Repository | `/Users/agile/Projects/framenest` |
| Remote | `https://github.com/cisarik/framenest.git` |
| Branch | `feat/kronika-one-product` |
| Start and end commit | `ade1169b4ba079bb1df540a929572ca58e777d16` |
| Tree | `f266df7205ddea5b83de7e6cd8313512ce70bcb1` |
| Parent | `7be040eb99901d0ae0b1327bb42de614e9192f17` |
| AP gitlink and checkout | `73e20ef80b88700d5fcbc397cd8edd4fc425869f` |
| Repository gate | PASS; index, worktree and AP checkout clean, including untracked files |
| Changed files | None, including no report-file write |
| Tests, builds, application/browser runs | None |
| Git writes, network, provider, NUC and credential operations | None |
| Subagents | None |

Public `main` and NUC equality with the baseline, and NUC revision `0035`, remain accepted grant context. They were not independently re-observed; no network was authorized.

No repository divergence required RF-12 recovery classification.

**Smallest next step:** the Cooperator persists this exact report, then the Orchestrator reconciles the plan and issues a complete fresh-session implementation grant. Neither this report nor client plan approval authorizes implementation.

### Planning Record — unchanged

```text
Planning cycle: initial
Prior planning report: 25_report_00.md (kronika-one-product 25/01)
Targeted revision basis: none
Changed decision boundary: the S8 unified UI/UX design (shared Timeline landing, personal history, Search and Research forms, administrator review) inside the existing packaged shell over the published S7-P APIs
Preserved unaffected decisions: ADR-0082 and ADR-0083 product decisions (private/family/administrator rules, administrator approval for the shared Timeline, separate personal history, Gallery as a separate working view, research disabled by default, no new framework); the published baseline ade1169…; capture parked; the S9/S10 sequence; testing economy; frozen Gallery/Details behavior
Automatic targeted revisions used: 0
```

### Plan-to-Execution fields — unchanged

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded implementation planning for the S8 unified Kronika UI/UX inside the existing packaged web shell
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
```

## 2. Frozen outcome, evidence and presentation choices

S8 adds a Timeline landing page, separate personal history, Search and Research forms, completed-document viewing, and administrator review within the existing HTML/CSS/JavaScript shell.

Gallery remains a separate working view. Its cards, filters, Details, metadata review and player retain their existing behavior. S8 introduces no framework, dependency, migration, research activation, provider call or capture integration.

The two requested Cooperator decisions were presented during this exchange and answered:

| Decision | Recommended default and confirmed choice | Alternative remains technically bounded |
|---|---|---|
| New UI copy | **English**, consistent with the existing shell | Slovak would change new-view strings and their language annotation; Gallery/Details would remain untranslated |
| Shell branding | **Kronika** in the title, accessible header labels and visible wordmark | Retaining FrameNest would change only those presentation strings |

There are **no unanswered Cooperator product questions**. Preserve the existing brand-mark graphic, including its current `FN` monogram, as described in the selected option. Do not rename packages, headers, storage keys, deployment identities or repositories. The later implementation grant must carry the confirmed choices.

### Material repository findings

| Evidence | Consequence for S8 |
|---|---|
| [records_api.py](/Users/agile/Projects/framenest/src/framenest/adapters/api/records_api.py:98), `_summary_payload`, `_detail_payload` | Record summaries lack titles and categories. Detail JSON supplies question text and `{title, url}` citations, but **does not supply answer text**. Use `/render` for the complete answer. |
| [record_repository.py](/Users/agile/Projects/framenest/src/framenest/infrastructure/persistence/record_repository.py:402), `SqliteRecordRepository._list` | Timeline membership is already approved-only. Existing list queries have pagination but no kind/category filters. Add filtering before count and pagination. |
| Same repository, `_media_projection`, `prepare_approval`, `approve`, `withdraw` | Approval already validates analysis, persisted metadata readiness and version. A `RECORD_CONFLICT` can also mean an unready record, so the UI must not describe every conflict solely as concurrent editing. |
| [application.py](/Users/agile/Projects/framenest/src/framenest/adapters/api/application.py:1545), `audience_me`; `local_identity_api.py`, `LocalIdentityMiddleware` | A configured local owner reaches request scope, but the loopback audience response currently returns `identity: null`. Echo the verified scope identity so new UI gates work locally. |
| [research_api.py](/Users/agile/Projects/framenest/src/framenest/adapters/api/research_api.py:139), `research_capabilities`, `create_research_request`, `read_research_request` | `enabled` does not prove credentials or provider readiness. Submission may return a terminal error in a 202 summary. Detail GET nudges existing admitted/running work. |
| [app.js](/Users/agile/Projects/framenest/src/framenest/adapters/api/web/app.js:11187), `identityReady`, legacy view open/close functions | Startup currently loads Gallery and focuses its search. Introduce one navigation owner while retaining the existing Gallery and modal functions. |
| Same shell, `openPrivateDetails`; `FrameNestCompanionWeb.onOpenDetails` | Preserve the `#/details/{media_id}` address shape and companion message entry. The current shell contains that hash fallback but no general hash router. |
| `tailscale_ingress.py`, `ROUTE_POLICIES`, `find_route_policy` | All required HTTP endpoints already have explicit policies; unclassified routes fail closed. |

The older “not shipped” or “documentation-only” descriptions in living product documents are stale relative to the baseline’s implemented APIs. Update their S8 status paragraphs without reopening accepted ADRs.

The historical audit’s F01 is corrected in baseline ancestry by `8e5c374`: `MAX_QUOTE_DEPTH` and its regression exist. Its historical hardcoded Python-path observation is also superseded by subsequent baseline changes. Neither is carried forward as an open S8 defect.

## 3. Exact implementation allowlist

All paths below are relative to `/Users/agile/Projects/framenest`.

Read-only verification against commit `ade1169b4ba079bb1df540a929572ca58e777d16` and the checkout found **20 unique paths: 19 existing regular files and one proposed new file**. No listed file is a symlink; the inspected containing directories exist.

| Status | Exact path | Purpose |
|---|---|---|
| Existing | `src/framenest/adapters/api/web/index.html` | Navigation, new sections, forms, document frame and branding |
| Existing | `src/framenest/adapters/api/web/styles.css` | Scoped S8 layout, responsive and accessible presentation |
| Existing | `src/framenest/adapters/api/web/app.js` | Routing, view state, API integration and regression-safe legacy bridges |
| Existing | `src/framenest/adapters/api/application.py` | Verified local identity in the existing audience response |
| Existing | `src/framenest/adapters/api/records_api.py` | Summary fields and validated list filters |
| Existing | `src/framenest/application/ports/records.py` | Additive summary/query fields |
| Existing | `src/framenest/application/records.py` | Validated forwarding of record filters |
| Existing | `src/framenest/infrastructure/persistence/record_repository.py` | Authorized summary selection and filtering before pagination |
| Existing | `tests/contract/test_local_web_application.py` | Page, navigation, branding and retained-shell contracts |
| Existing | `tests/contract/test_records_api.py` | Summary/filter, access, Timeline and approval contracts |
| Existing | `tests/contract/test_local_record_identity.py` | Audience echo and local identity boundaries |
| Existing | `tests/contract/test_kronika_access_inventory.py` | Accurate Timeline projection description and inventory regeneration |
| Existing | `tests/integration/persistence/test_kronika_record_repository.py` | Filter counts, ordering and approved-summary stability |
| **New** | `tests/kronika_ui.test.js` | Thin production-function UI regression harness |
| Existing | `README.md` | Implemented versus accepted/deployed status |
| Existing | `PRODUCT.md` | Delivered S8 experience and retained boundaries |
| Existing | `SPEC.md` | Implemented navigation, summaries and UI behavior |
| Existing | `ROADMAP.md` | S8 candidate/evidence status; preserve S9/S10 |
| Existing | `SERVER.md` | Existing-server UI/API integration and disabled research |
| Existing | `docs/KRONIKA_ACCESS_INVENTORY.md` | Committed regenerated inventory |

The persistence repository is the sole production path outside the shell/API/application categories. Its inclusion is necessary: correct category filtering, totals and approved Timeline titles must come from the authorized SQL projection before pagination. Browser filtering of a fetched page would be incorrect. This is a read-query change, not a schema or approval-lifecycle change.

No other path is implicitly editable. In particular, `research_api.py`, `tailscale_ingress.py`, the renderer, migrations, AP, dependencies and deployment sources remain outside this proposed edit allowlist.

## 4. Routes, APIs and minimal interface changes

### Client routes

All new addresses are fragments of the existing `/` page. Refreshes therefore continue to request the packaged shell.

| Client address | View and API mapping |
|---|---|
| `/`, empty fragment, `#/timeline` | Timeline: `GET /api/timeline` |
| `#/gallery` | Existing Gallery and its existing APIs |
| `#/history` | Own question/request history: `GET /api/research-requests` |
| `#/history/records` | Own saved/common records: `GET /api/my/records` |
| `#/search` | Search form: capabilities GET, then explicit research-request POST with `kind: "search"` |
| `#/research` | Research form: same endpoints with `kind: "research"` |
| `#/requests/{operation_id}` | Request detail, active polling and cancellation through existing request endpoints |
| `#/records/{record_id}` | Record detail and authorized render GET |
| `#/review` | Administrator records, initially `visibility=private` |
| `#/review/shared` | Administrator records with `visibility=family`; withdrawal and reapproval |
| `#/review/requests` | `GET /api/admin/research-requests`; request inspection/cancellation |
| `#/details/{media_id}` | Existing Gallery backing view and `openDetailsDialog` |

Use fragment query parameters for active list filters and offset. Parse identifiers defensively, encode each API path segment, and show a local unavailable-address state for malformed routes. Unknown routes offer Timeline and Gallery links; `#main` remains the skip-link anchor.

Existing Manage media, My contributions and Analysis proposals stay reachable through their existing controls. Their open/close functions participate in the shared view switch so two main sections never remain visible. Preserve their loading and workflow behavior.

**No new HTTP route is needed.** No new `ROUTE_POLICIES` entry or static asset registration is required. Regenerate the access inventory because its Timeline projection description changes, even though the route set does not.

If implementation discovers a genuinely necessary new HTTP route, stop for an amended grant naming its method, template, capability/audit policy and inventory change.

### Additive record interfaces

Extend `RecordSummary` and its HTTP serialization with:

- `display_title: string | null`
- `content_category: "general" | "meme" | "movie" | "youtube" | null`

Use optional/defaulted fields in the Python value object to preserve existing constructors.

Derive Search/Research titles from the immutable question: collapse whitespace, retain at most 240 Unicode code points, using an ellipsis within that limit when truncated. Do not make a naming provider call. Media titles come from persisted metadata; absent titles remain null and display as “Untitled media,” without filename fallback.

Add optional `kind` and `content_category` to record-list queries. Add `visibility` filtering only to the administrator inventory. Validate enum values; category filtering requires `kind=media`. Invalid supplied combinations receive a sanitized 422 `INVALID_REQUEST`. Preserve existing limit/offset bounds: default 24, maximum 100.

Apply these rules in `RecordPageQuery`, `RecordService` and `SqliteRecordRepository._list`:

- Own history always retains the caller-owner predicate, including for administrators.
- Administrator inventory retains its administrator gate.
- Timeline always retains family visibility, an approved projection and first-entry timestamp.
- Timeline media title/category comes from `kronika_approved_media` for **every caller**. Its summary `read_decision` is `approved`; detail/Gallery authorization remains unchanged.
- Own/admin summaries use current authorized metadata. Search/Research uses immutable question text.
- Apply filters before the count and pagination; retain existing chronological ordering and stable ID tie-breaks.
- Select summary columns and title/category sources without loading answers or hydrating each card through detail calls.

Do not add answer text, full documents, citations, filenames or location paths to list payloads.

### Identity and mutation integration

Change only the existing `audience_me` response behavior for a verified `IdentityContext` already attached to request scope: return that identity and its mapped capabilities for configured loopback callers. Preserve the existing no-local-owner response and the Tailscale/public boundaries.

New UI predicates require a resolved workspace audience, a nonempty verified login, and the appropriate capability:

- `research.run` for submission and request operations.
- `records.approve` for administrator review.
- Verified identity for Timeline and own-record reads.

Do not infer administrator authority from loopback or from the legacy capability-only response.

Every new POST uses `framenestMutationHeaders`, same-origin fetch and JSON where required. Client bodies never supply owner, model, endpoint, tools or credentials.

## 5. Components, state and failure behavior

### Navigation and shared state

Keep implementation in the existing `app.js`, with a clearly bounded group of named `kronika…` functions and state objects. Reuse the repository’s request-generation/token pattern.

Initialize the router after `identityReady`. Timeline becomes the normal workspace landing view; Gallery loads when selected. Public composition retains its existing Gallery-only behavior and makes no new research/record requests.

Maintain separate state for Timeline, own requests, own records, administrator records, administrator requests, document detail and the submission attempt. Each paginated view owns its offset, filters, request generation and displayed data. Do not reuse administrator results as Timeline or personal-history data.

On navigation:

- Hide inactive sections and the Gallery search when outside Gallery.
- Preserve Gallery query/page state and existing playback cleanup.
- Use the existing dirty-metadata confirmation before a transition that would discard edits.
- Ignore late responses from an older route, identity or filter generation.
- Handle browser back/forward and Details close without route loops.
- Preserve companion `onOpenDetails` and `onHostedChange` behavior.
- Restore focus to the originating control; use the destination heading or Gallery container when that control no longer exists.

Identity loss clears private content, document frames and active controllers immediately.

### Timeline

Use a responsive grid of lightweight summary cards: title, Search/Research/media-category label and first Timeline-entry date. Media cards link to existing Details; document cards open the record view. Do not add another media preview/player implementation.

Provide a single filter group: All, Search, Research, Media, General, Memes, Movies and YouTube. Categories map to `kind=media` plus the category parameter. GIF remains a format, not a Timeline category.

Use server totals and 24-item pagination. Never merge in own/admin records or unfinished requests. Completion alone never adds a card.

States:

- Initial load: existing spinner/status language.
- Empty: “No records have been approved for the Timeline yet.”
- Filtered empty: “No approved records match this filter.”
- Initial error: sanitized explanation and Retry.
- Refresh/page failure: retain only already authorized data for that same query, clearly marked as not refreshed. Do not present it as the requested page.

### Personal history

Use two explicit tabs with independent pagination:

- **Questions:** own request summaries, including active, saved, refused, failed, incomplete, cancelled, timed-out and submission-unknown attempts. Saved rows link through `record_id`.
- **Records:** `/api/my/records`, including the caller’s saved documents and media.

This avoids an incorrectly merged, partially paginated feed. The two tabs may reference the same completed question, but the active list renders it once and never claims a combined total.

Show “Private — visible to you and administrators” or “On the household Timeline” from actual record visibility. Owners receive no sharing/approval control. Administrators’ personal history is still their own history; cross-owner work belongs in Review.

### Search and Research forms

Use the same form component with a fixed route-selected kind, labelled question textarea, explicit consent checkbox and submit action.

- Fetch `/api/research/capabilities`; distinguish loading, unavailable, disabled and enabled.
- While disabled, retain the explanatory view and history link but disable submission.
- Do not present enabled as provider readiness or issue a readiness probe.
- Show returned retention notice and available budget/reservation information. Do not describe reservations as guaranteed invoice caps.
- Accept only nonblank question text within 16,384 UTF-8 bytes, using `TextEncoder`; preserve the exact submitted text.
- Consent is initially unchecked. Send a bounded UI version, `kronika-research-v1`, after acknowledgement. Do not claim that acknowledgement is durably stored.
- No attachments, media selection, model selection, provider configuration or credentials.

Consent copy:

> I agree to send this question to the configured provider. The answer is stored locally; provider retention may still apply.

Generate one `client_request_id` per deliberate attempt, before its first POST. Freeze `{kind, prompt, client_request_id, consent_version}` for that attempt. Disable double submission.

A transport failure offers **Retry the same submission**, using identical content and ID. It never creates a replacement ID automatically. Editing the question or explicitly starting another attempt requires a new ID and renewed consent.

For reload recovery, persist only the opaque attempt ID, a SHA-256 fingerprint binding identity/kind/exact prompt/consent, and a known operation ID in session storage. Do not persist question/answer text. A restored known operation is recovered by GET; otherwise the user checks history or re-enters matching text before an explicit same-ID retry. If recovery storage is unavailable, preserve in-memory retry and explain that reload loses that recovery.

Handle both error envelopes and 202 summaries carrying a terminal `error_code`.

### Active requests and cancellation

Use one serial polling controller for the active request known to the current session. Poll detail GET five seconds after the previous request settles; never overlap polls or use list GET as the progress mechanism.

Active states are exactly:

`admitted`, `submitting`, `running`, `validating`, `cancel_requested`.

Terminal states are exactly:

`saved`, `refused`, `failed`, `incomplete`, `cancelled`, `timeout`, `submission_unknown`.

Keep polling across main-view navigation while the page remains visible. Pause on hidden/pagehide, identity loss or disabled runtime; resume with a fresh authorized read when appropriate. Explain that processing depends on application polling and that closing the page pauses this UI’s updates.

After three consecutive transport failures, pause and offer Resume updates. Do not translate a failed status fetch into a failed research operation. Unknown lifecycle values stop automatic polling and show an unavailable-status message.

Cancellation calls the existing cancel POST once. `cancel_requested` means cancellation is pending; continue polling until the server supplies a terminal state.

On `saved`, require `record_id`, invalidate personal-record data and offer “Open answer.” Do not navigate away automatically or update Timeline membership.

### Completed-document view

Fetch record detail, then the render endpoint. Clear the previous frame before switching records.

Use a **sandboxed iframe with `sandbox=""` and `referrerpolicy="no-referrer"`**. Fetching render HTML first permits correct status/error handling. Assign it only to the iframe’s `srcdoc`, within a trusted document wrapper.

Because fetched response CSP headers do not automatically govern `srcdoc`, put a trusted CSP meta element before the rendered content, reproducing:

`default-src 'none'; style-src 'unsafe-inline'; img-src data:; base-uri 'none'; form-action 'none'`.

Add only fixed local styling for the existing dark/green palette, readable text and wrapping. Never insert generated HTML into the application DOM, enable scripts/same-origin privileges, or truncate the answer.

Render `{title, url}` citations separately with DOM-created text nodes and validated absolute `http:`, `https:` or `mailto:` links. Use `noopener noreferrer`, no-referrer and user activation. Never prefetch citations, images or source previews.

A render failure preserves the question and a Retry answer control; it does not show a partial response as complete. The frame has an accessible title and a bounded viewport with scrolling for the full report.

### Administrator review

Keep household approval separate from legacy internet-publication controls.

Provide:

- **Not on Timeline:** private records, including withdrawn and unready records.
- **On Timeline:** family records, with withdrawal and explicit review/reapproval.
- **Requests:** administrator request inventory, including unfinished work.

Do not invent owner labels for administrator request summaries: that endpoint does not return ownership.

Review loads the current record detail and retains its exact version. Documents use the safe render view. Media links to existing Details and metadata review.

Offer only:

- **Approve for Timeline**, or **Approve current version** for an already shared record.
- **Withdraw from Timeline** for a shared record.

Disable approval when completion is absent. For completed media, explain that the server still checks successful analysis and saved metadata readiness; the UI does not claim eligibility from completion alone.

POST the displayed version as `expected_version`. On success, refresh/invalidate relevant lists; accept `changed: false` as a successful unchanged result. Withdrawal removes the shared card while retaining personal history.

On 409, show the conflict, disable the stale action and require Reload followed by another explicit review/action. Never silently substitute a newer version and resubmit. An uncertain mutation response also requires readback, not automatic replay.

### Stable error copy

Map codes from `{"error":{"code":…,"message":…}}` and request-summary `error_code` to controlled UI text.

| Code | English copy / action |
|---|---|
| `E_DISABLED` | “Search and Research are turned off. Your history is still available.” |
| `E_NOT_CONFIGURED` | “Search and Research are not ready. An administrator needs to finish setup.” |
| `E_BUSY` | “Another request is running. Try again when it finishes.” Do not disclose another owner’s request. |
| `E_IDEMPOTENCY_CONFLICT` | “This submission ID belongs to different content. Check your history before starting a new request.” No automatic replacement ID. |
| `E_BUDGET_EXCEEDED` | “The research budget has been reached. Try again after it resets.” Do not invent a reset time. |
| `IDENTITY_REQUIRED` | “A verified account is required. Reconnect to your workspace.” Clear protected state. |
| `CAPABILITY_DENIED` | “Your account is not allowed to perform this action.” |
| `RECORD_CONFLICT` | “This record changed or is not ready for approval. Reload and review it before trying again.” |
| `NOT_FOUND` | “This item is unavailable.” Identical presentation for missing and inaccessible records. |

Also handle validation errors, unknown submission status, cancellation and generic service/network failures without showing raw provider bodies, tracebacks or arbitrary server messages. No error starts generation, activates a provider or applies a fallback.

## 6. Accessibility, responsive behavior and documentation

Reuse existing `styles.css` tokens: background `#0a0e0a`, existing surface/text colors, green accent/focus and warning/danger colors. Add scoped `.kronika-*` selectors; do not restyle Gallery, Details or player selectors.

- Retain the skip link and one main landmark; make its target focusable.
- Use primary-navigation links with `aria-current`, semantic headings, labelled controls and real buttons.
- Use `aria-busy` and a polite status region for loading/progress; announce state transitions rather than every poll.
- Associate validation and consent explanations with their controls. Move focus to the first invalid field after failed validation.
- Keep errors readable without relying on color.
- Use visible keyboard focus and at least 44px new action targets.
- Let navigation/actions wrap. Use a two-column card grid on wider layouts and one column below 720px.
- Support the existing 320px minimum width without page-level horizontal scrolling.
- Respect reduced motion; add no animated previews, automatic scrolling or celebratory animation.
- Preserve existing modal Escape, focus restoration and dirty-edit confirmation behavior.

Update the five living product/status documents only where needed to distinguish:

1. implemented S6/S4-B/S7-P foundations;
2. the S8 candidate and its actual validation;
3. independent acceptance, publication and deployment still awaiting their separate evidence;
4. research disabled and live acceptance/reset remaining in S9.

Do not revise historical ADRs or claim S8 acceptance before Michal’s rendered acceptance.

## 7. Causal validation plan

No tests were executed in this planning exchange.

### Python contracts and persistence

Add these causal scenarios to the allowlisted tests:

| Test area | Required scenario |
|---|---|
| Timeline membership | Owner, another household member and administrator all receive only approved records; withdrawal removes them for every caller |
| Summary projection | Approve media A, change working title/category to B: Timeline title, filter results and totals remain A for all callers until reapproval |
| Pagination | Mixed record kinds/categories across more than one page; filtering precedes count/limit/offset; stable ordering and bounds remain correct |
| Personal isolation | Administrator own history excludes other owners; ordinary callers cannot obtain foreign titles, counts, detail or render |
| Summary limits | Lists contain bounded titles and no answers/full documents; hostile title text remains data |
| Approval | Stale approve and stale withdraw return `RECORD_CONFLICT`; unready media cannot bypass analysis/metadata review; `reject` remains unsupported |
| Local identity | Configured local user/admin is echoed with actual mapped capabilities; missing owner, non-loopback caller and spoofed headers do not manufacture identity |
| Shell contract | Timeline entry, Gallery reachability, retained Details/companion hooks, local assets, skip link and safe frame markup |
| Inventory/public boundary | Route set remains unchanged; Timeline projection documentation is regenerated; public composition excludes new record/research routes |

Continue to use the existing research contract tests for capabilities, owner separation, idempotent replay/conflict, cancellation and disabled admission. Use the existing renderer tests, including deep-quote regression.

### Thin JavaScript harness

Create `tests/kronika_ui.test.js` using `node:test`, `node:vm`, source reads and production-function execution, following `gallery_loading_states.test.js` and `metadata_form_contract.test.js`. Stub DOM, fetch, timers, crypto and storage; do not reproduce the production state machine in test code.

Required behavioral tests:

- Empty hash selects Timeline; Gallery and `#/details/{id}` remain reachable; companion Details dispatch still works.
- Timeline requests only its endpoint, including for administrators; own/admin responses cannot populate it.
- Personal history retains active, failed and cancelled requests and separates them from Timeline.
- Capability-disabled, unavailable and enabled-but-not-configured responses produce distinct truthful states.
- Double click, lost POST response and explicit retry preserve the same attempt ID/body; changed content requires a new attempt.
- Active polling is serial, stops for every terminal state and resumes safely; late responses cannot overwrite another identity/route.
- `cancel_requested` keeps polling and does not display premature cancellation.
- Render HTML reaches only a sandboxed frame with an effective embedded CSP; citations never trigger fetch.
- Approval sends the viewed `expected_version`; stale conflict requires reload and a second deliberate action.
- Partial list/detail failures preserve only correctly labelled authorized content.
- Navigation/focus, Escape, identity loss and dirty metadata behave correctly.

Run focused JS checks while editing. After the final change, run `node --test tests/*.test.js` once with real-browser evidence gates unset. Existing gated browser suites remain skipped; that is not rendered acceptance.

Retain existing Gallery loading, filtering, still-image, GIF, playback-handoff, metadata and companion behavior tests. Stop on a causal regression rather than weakening them.

### Exact Python route and focused targets

Use `./.ap/ap project check` followed by `./.ap/ap exec --operation test-focus`, both with root `/Users/agile/Projects/framenest` and baseline `ade1169b4ba079bb1df540a929572ca58e777d16`. Append `-q -p no:cacheprovider`.

The final focused target set is:

- `tests/contract/test_local_web_application.py`
- `tests/contract/test_records_api.py`
- `tests/contract/test_research_requests_api.py`
- `tests/contract/test_local_record_identity.py`
- `tests/contract/test_kronika_access_inventory.py`
- `tests/contract/test_kronika_record_authorization.py`
- `tests/contract/test_kronika_approved_projection.py`
- `tests/contract/test_web_package_resources.py::test_web_resources_are_available_from_package_resource_boundary`
- `tests/contract/test_public_published_uds.py::test_unlisted_routes_and_methods_are_uniform_404`
- `tests/contract/test_public_published_uds.py::test_workspace_tcp_audience_bootstrap_is_trusted_loopback`
- `tests/integration/persistence/test_kronika_record_repository.py`
- `tests/unit/application/test_records.py`
- `tests/unit/application/test_document_rendering.py`

Run narrower affected targets during implementation, then this focused set once. Do not run the broad Python suite. The inventory test may rewrite its allowlisted document; inspect and include that exact generated change.

Validation uses disposable synthetic data and fake providers only. No ambient Python, environment reconstruction or live service/provider is permitted.

## 8. Acceptance and release route

1. **Implementation candidate.** Complete the allowlisted changes, focused validation, final diff review and one local commit. Record exact commit/tree, unchanged AP pin, changed paths and test results. Implementation evidence is non-independent.

2. **One fresh independent audit.** A separate authoritative grant targets that exact candidate in a session that did not implement it. Review the delta, authorized summaries/counts, local identity echo, submission idempotency, polling, iframe/CSP isolation, versioned approval, public exclusion and Gallery/Details regressions. No corrections are made inside the audit. Any accepted defect receives separate correction authority and the required independent recheck.

3. **Publication.** After audit reconciliation, a separately authorized publication step places the accepted candidate on GitHub `main`. Verify the exact public SHA. If publication changes the candidate, reconcile that change before deployment.

4. **Routine NUC refresh.** Under separate bounded operational authority, use only `deploy/ubuntu/framenest-release`. Run `status` and `check --release <exact-public-main-SHA>` before deployment. A check never authorizes deployment. Use the existing pinned tooling and privilege lifecycle. S8 expects schema `0035`; a schema mismatch follows the documented `migration-required` continuation under appropriate authority, without importing S9 reset authority.

5. **Michal’s rendered acceptance.** Request it only after final release status proves that the NUC serves the exact public `main` candidate and is healthy. Verify Timeline landing/filtering, private-history separation, disabled forms, approved document rendering, review/withdrawal/stale-version UX, keyboard/mobile behavior and unchanged Gallery, image, GIF, Details and playback.

Use owner-designated or separately authorized synthetic records for rendered scenarios. If required fixture states are unavailable, record the missing scenario; do not create them through an unauthorized live provider call or host/database mutation.

Enabled submission and lifecycle behavior are proven with fake-provider automated evidence in S8. Live-provider acceptance remains S9. Research and internet publication stay disabled. No S8 step activates capture or performs an empty-database reset.

## 9. Proposed first implementation grant — non-authoritative

**This is a proposal, not an issued Worker prompt or execution authority. Only a later complete Orchestrator grant authorizes the following work.**

| Field | Proposed value |
|---|---|
| Coordinates | `kronika-one-product`, session **53**, exchange **01**, if still the next unused fresh-session coordinate |
| Role / profile | WORKER / Fresh Implementation Worker |
| Worker session target | `fresh-worker-session` |
| Native planning mode | `not-used`, verified against actual client mode |
| Phase / task | implementation / `KRONIKA-ONE-PRODUCT-S8-IMPLEMENTATION` |
| Delivery | Manual Cooperator delivery, preserving the selected route |
| Reasoning recommendation | Extra High for navigation/lifecycle integration and access-sensitive projections |
| Outcome | The complete S8 behavior frozen in sections 2–8 |
| Baseline | `ade1169b4ba079bb1df540a929572ca58e777d16`, tree `f266df7205ddea5b83de7e6cd8313512ce70bcb1`, parent `7be040eb99901d0ae0b1327bb42de614e9192f17` |
| Repository / branch | `/Users/agile/Projects/framenest`; `feat/kronika-one-product`; clean checkout |
| AP pin | `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, read-only |
| Exact allowlist | The **20 exact paths in section 3**, with no additions or wildcard expansion; reproduce the table in the issued grant |
| Positive authority | Edit those paths; create only the named JS test; use synthetic temporary fixtures; execute section 7 validation through declared routes; regenerate the named inventory; inspect diffs; explicitly stage accepted allowlisted paths; create one local commit |
| Commit | `feat(kronika): add unified timeline history and review UI` |
| Git exclusions | No fetch, push, merge, rebase, reset, clean, stash, force operations or branch changes |
| Other exclusions | No dependencies/toolchain/AP/migrations, private data, live database, provider/network calls, credentials, browser/server launches outside authorized test execution, NUC/SSH/sudo, deployment, capture, S9/S10 work or subagents |
| Stop rules | Baseline/branch/pin drift; unexplained owner work; required out-of-list changes; new HTTP route; Gallery/Details regression; authorization/projection/rendering failure; unavailable declared execution route; validation requiring forbidden actions |
| Validation | Section 7; no broad Python suite; final source/diff/path review and unchanged AP pin |
| Completion | Exact candidate SHA/tree, changed files, commands and exit statuses, generated-inventory result, residual limitations, no-push evidence and standard terminal Worker report |
| Acceptance | Separate fresh independent audit; no self-certification or rendered-acceptance claim |
| Expiry | Terminal report, cancellation or supersession; no retained implementation authority |

For an actual 53/01 grant, propose prompt `53_implementation_00.md` and report `53_report_00.md` in the activated trace directory. The Orchestrator must verify coordinate availability and grant exact absent-file persistence separately. A report-persistence exchange that consumes session 53 changes the next implementation coordinate; it does not reopen this plan.

## 10. Limitations, critique and expiry

The plan is grounded in repository code and the specified AP/project/trace anchors. It establishes an implementation design, not executed correctness, independent acceptance, current public-ref evidence or NUC readiness.

The proposed SQL-summary and local-identity changes are explicit S8 prerequisites. They are not hidden UI assumptions. No remaining material mapping requires an unresolved Orchestrator design decision.

```text
Orchestration critique:
MEASURED: Active client Plan Mode prohibits the granted report-file write. The destination remains absent. Effect: file delivery, saved-file readback and SHA-256 are unavailable. Smallest correction: the Cooperator or a separately authorized capable persister stores this exact completed report without replanning.
LEAD: none

Resolved Execution Issues / Near-Misses:
Some initial combined reads were truncated; relied-on contracts and code were subsequently inspected in narrower reads. Guessed repository/configuration paths that did not exist were resolved through repository discovery. No mutation or test execution followed those lookup failures.

Pre-Existing Failure Classification:
No runtime or test failure was established because execution was prohibited. Stale living-status prose and the audience-response gap are established static observations addressed by the proposed allowlist. Historical F01 and interpreter-path observations are superseded in the verified baseline.

File delivery:
Intended path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product/52_report_00.md
Saved report: absent
Full saved-file readback: not performed
Saved-file SHA-256: unavailable
Delivery result: PARTIAL
```

**Authority expiry:** this terminal report ends planning exchange 52/01. Planning authority expires. No implementation, publication, deployment, further planning cycle or file write is authorized by this report. The logical whole remains **not closed**.
