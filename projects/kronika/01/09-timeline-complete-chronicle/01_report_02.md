### Report for ORCHESTRATOR_CHAT

# Kronika complete Timeline chronicle — implementation plan

```text
Logical whole identity: timeline-complete-chronicle
Worker session ordinal: 01
Worker exchange ordinal: 03
Persistent role identity: WORKER
Worker session target: current-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: KRN-TCC-PLAN-01R2 — corrected initial plan-only — complete, visibility-aware Timeline chronicle on the existing Kronika record, media, research and preview foundations
Status: PARTIAL
Phase-qualified result: not-applicable
Start commit: b66ec8f50860ace624f6be1fd3ad63f521edcd33
End commit: b66ec8f50860ace624f6be1fd3ad63f521edcd33
Report justification: new-evidence
Logical-whole closure: not-closed
Planning cycle: initial
Prior planning report: 01_report_01.md
Automatic targeted revisions used: 0
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
```

The technical plan is complete. `PARTIAL` records missing file persistence under the client’s active Plan Mode; it does not identify an unresolved implementation choice. No implementation or acceptance PASS is claimed.

Report persistence: client-prohibited; complete exact content returned for authorized persistence

Intended report destination:

`/Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/01_report_02.md`

No report file was written or read back. The report body inside this plan block is the complete content for authorized persistence.

## 1. Summary and verified baseline

Replace the approved-only Timeline with one chronological read model covering all existing catalog media and Search/Research content the verified caller may read. Render it as a compact list with aligned desktop columns and 36 px media thumbnails.

Keep `/api/timeline`, the existing record and research detail routes, Gallery, personal History, administrator approval, direct-media audience policy and preview delivery. Introduce no database migration, synthetic common records, provider calls, dependency or deployment-system change.

| Gate | Observation in this exchange |
|---|---|
| Physical checkout | `/Users/agile/Projects/kronika` |
| Branch and HEAD | `main`, `b66ec8f50860ace624f6be1fd3ad63f521edcd33` |
| Public `refs/heads/main` | Same SHA, directly observed using `git ls-remote origin refs/heads/main` |
| Working tree | Clean at opening and final inspection |
| Containing `.ap` gitlink and submodule HEAD | Both `d7023cf037f6d17885c3ede5c04812c61640da50` |
| Governing AP variant | Stable |
| `./.ap/ap doctor` | PASS |
| Baseline-bound `ap project check` | PASS; CPython 3.13 |
| Environment warning | Sanitized inherited classes `SSH_AUTH_SOCK`, `PATH`, `GIT_PAGER`; no values reported |
| Received prompt | Byte-identical to archived `01_planning_02.md` |
| Session continuity | Matches terminal exchange 01/02 and the actual current session |
| Report destination | Absent when checked, including final inspection |
| ADR allocation | No tracked ADR-0087; ADR-0086 is the latest existing numbered decision |
| Tests executed | None; source and test inspection sufficed for planning |
| Repository and Meta writes | None |
| Git writes | None |
| NUC, browser, provider or secret contact | None |

The previous source observations were checked against the freshly verified unchanged commit. They remain non-independent planning evidence.

The recorded NUC release, service, schema, backup readiness and sudo state were not revalidated. Whole 01’s deployment and rendered-review events remain historical or Cooperator-owned evidence.

## 2. Re-measured current-state map

### 2.1 API, application and persistence

| Owner | Current behavior |
|---|---|
| `src/kronika/adapters/api/records_api.py` | `GET /api/timeline` requires verified identity, parses pagination, accepts kind/category filters and calls `RecordService.list_timeline`. `_list_filters` currently rejects Timeline visibility filters. |
| `src/kronika/application/records.py` | `RecordService.list_timeline` constructs `RecordPageQuery`; it has no media/request aggregation. History and administrator inventory are separate methods. |
| `src/kronika/application/ports/records.py` | `RecordSummary` requires a common record ID and owner. It cannot correctly represent unbound media or an unfinished research request. |
| `src/kronika/infrastructure/persistence/record_repository.py` | `list_timeline` delegates to `_list(... timeline_only=True)`. Membership requires family visibility, non-null approval JSON and non-null `timeline_entered_at_ms`. Ordering is approval-entry time descending, record ID ascending. |
| Same repository, `_summary_labels` | Timeline media labels come from `kronika_approved_media`; History uses working metadata. Completed-question labels currently join `kronika_documents`. |
| Same repository, `_summary_preview_locations` | Timeline selects the minimum eligible approved location; History selects the minimum eligible current location. No preview-cache or filesystem readiness probe occurs. |
| Same repository, `approve` and `withdraw` | Approval preserves the first Timeline timestamp, stores the projection and increments version. Withdrawal sets visibility private and retains the approval snapshot and timestamp. |
| Same repository, result completion | Completion inserts one document and private common record and links the request within one immediate transaction. The request’s lifecycle update can follow that durable save. |
| `src/kronika/infrastructure/persistence/research_request_repository.py` | Request lists select full request rows, with owner or administrator list methods and separate count methods. These are unsuitable as per-row Timeline calls. |

### 2.2 Item sources and relationships

| Entity | Timeline significance |
|---|---|
| `logical_media` | Canonical identity and creation time of a cataloged medium. Exists before analysis and may have no common record. |
| `physical_media_locations` | Zero or more source locations for a medium. Locations are not separate Timeline items. |
| `media_metadata` | Optional current title/category. Missing metadata does not exclude a readable medium. |
| `media_analysis_runs` | Analysis lifecycle evidence. Runs are not separate Timeline items. |
| `kronika_records` | Bound media ownership/visibility or a completed Search/Research record. Unique media binding prevents two common records for one medium. |
| `kronika_documents` | Completed question and answer content. Its common record supplies ownership and visibility. A document alone is not an additional item. |
| `research_requests` | Durable admitted, active, failed, cancelled and saved question attempts. Saved requests also have common-record/document representation. |
| `kronika_approved_media` and approved-location/tag tables | Frozen household projection for another owner’s approved media. |
| Record approval columns | Household approval and withdrawal evidence; not separate chronicle events. |
| `media_content_publications` | Existing publication truth for unbound legacy media. It must not override a common-record binding. |
| Upload, YouTube and X attribution | Existing requester access to unbound media; attribution is not a new common-record owner. |

Production source contains the `bind_media_record` definition and port declaration, but no production invocation. The implementation must therefore support unbound media directly.

Upload quarantine, incomplete transfers and acquisition jobs without a `logical_media` row are workflow attempts rather than catalog content. They remain in their existing workflows. This whole does not bypass quarantine or manufacture a media item for them.

### 2.3 Authorization and delivery

`domain/record_access.py::decide_bound_read` returns:

- `current` for the verified owner or a caller with `media.workflow.read`;
- `approved` for another member only when the record is family-visible, approved and completed;
- `deny` otherwise.

`scope_for_identity` derives the caller scope. It does not accept client ownership claims.

`ContentAudiencePolicy.read_decision` checks a common-record binding first. Only unbound media can use existing publication or live requester access. Consequently, a historical publication or contribution cannot bypass a private bound record.

Live unbound requester predicates differ from general contribution attribution:

- Upload: linked `upload_publications` joined to the caller’s upload session.
- YouTube: caller’s linked claim in `cataloged` or `duplicate_resolved`.
- X: caller’s linked asset in `cataloged`.

The general attribution union does not apply all those success-state restrictions. Neither that union nor `catalog_scope_predicate` alone is the complete direct-read authorization predicate.

`content_audience_api.py` carries the decision into direct media routes. `gallery_preview_api.py` denies before cache access and limits `approved` reads to approved location identities. Content and download routes apply the corresponding approved-location restriction.

The public composition has its own explicit route allowlist, excludes common records and does not install `/api/timeline`. It remains disabled for internet publication.

### 2.4 Shell and predecessor reuse

The current Timeline container is a `.kronika-grid`. `kronikaLoadTimeline` calls `kronikaRenderCards`; media links open existing Details, and document links open existing record views.

History has Questions and Records modes. Its record mode uses `/api/my/records`; Questions uses `/api/research-requests`. Gallery retains its separate renderer, search and player.

Whole 01 changed fourteen paths between `246c9f8` and `b66ec8f`. Reuse:

- `preview_location_id` as a nullable candidate locator;
- `mediaGalleryPreviewUrl`;
- `kronikaAttachCardPreview` and its identity/page/list generation fences;
- `kronikaCancelListRequest`, `kronikaBeginListController` and request aborting;
- preview retirement on accepted navigation, identity change and `pagehide`;
- preservation of previews and in-flight lists across `visibilitychange`;
- the existing lazy image, icon fallback and no automatic retry behavior.

Replace the Timeline card renderer and its approved-only locator selection. Preserve History’s card layout and current-location behavior.

Current Review labels such as “Not on Timeline”, “Approve for Timeline” and “Withdraw from Timeline” will become misleading. Relabel them around household sharing while preserving their existing endpoints and actions.

## 3. Proposed ADR-0087 and transition

Proposed path:

`docs/adr/0087-complete-visibility-aware-timeline-chronicle.md`

Proposed title:

**ADR-0087: Complete Visibility-Aware Timeline Chronicle**

Status in this report: **Proposed**.

Acceptance event: Michal explicitly accepts the decision below, and the Orchestrator records that acceptance before issuing implementation authority. The implementation grant must identify that accepted decision. Client plan approval alone does not grant implementation authority.

### Proposed decision text

The Timeline remains Kronika’s landing page. It is the complete chronological overview of existing catalog media and Search/Research content that the signed-in identity is already authorized to read.

This supersedes ADR-0083’s sentence:

> It contains only administrator-approved records, including when the viewer is an administrator.

Timeline membership is no longer a household-publication gate. It includes readable private, unanalysed, unfinished, failed and unpublished content.

The Timeline is a read projection, not a new persistent content entity or an event log. One logical medium appears once. One submitted question appears once throughout its durable request and completed-document lifecycle.

The owner and application administrator see current authorized content. Other household members see only the content already available through existing approved projections or existing unbound legacy-publication access. Approval, withdrawal and binding precedence retain their existing effects.

The chronicle orders items by their original catalog/request creation time, newest first, then stable item identity. Approval does not move an item to the top. Existing `timeline_entered_at_ms` values retain their historical first-household-approval meaning and are not rewritten.

The compact Timeline list shows kind, title, creation date, lifecycle status and visibility/publication state. Gallery remains the media working view. Personal History remains the caller’s question/research history and existing personal-record view.

Administrator approval remains required for household publication of completed common records and successfully analyzed bound media. Private work does not become household-visible merely because it appears on its owner’s or administrator’s Timeline.

The preview route, audience policy, quarantine, validation, identity model and internet-publication prohibition remain unchanged. Timeline reads neither start generation nor request derivative generation.

### Transition and compatibility

- No content migration, backfill, reset, binding creation or historical-row rewrite.
- Existing media becomes visible through the read union when already authorized.
- Existing saved questions collapse to their completed-record representation.
- Withdrawal removes cross-owner household access; the item remains visible to its owner and administrator as private/withdrawn.
- Reapproval changes household projection and publication state without changing chronicle identity or creation ordering.
- Reanalysis may change the owner/administrator’s current status while the household retains its approved result.
- Existing unbound publication access is preserved as a legacy path. Listing an item neither grants approval nor invokes publication.
- `/api/timeline` keeps its URL and page envelope but receives a new item contract. This is a coordinated pre-alpha API change. Repository search found the packaged shell and tests as its current consumers; no compatibility adapter or second Timeline endpoint is proposed.
- `/api/my/records`, administrator records, record detail/render and research request contracts retain their existing behavior.

The new ADR must state these chronological consequences explicitly. ADR-0083’s other decisions and its historical body remain unchanged. The ADR index identifies the partial supersession.

Rejected alternatives:

| Alternative | Reason |
|---|---|
| Keep the approved-only Timeline and add another “All items” destination | Does not implement the selected route A objective. |
| Insert synthetic common records for every medium | Changes ownership/write behavior and risks approval/publication regressions. |
| Merge Gallery and History in the browser | Produces incomplete totals, unstable pagination and unauthorized client-side aggregation. |
| Append every location, analysis run and approval as an item | Creates an activity log rather than one overview of added content. |
| Broaden household access to achieve completeness | Violates the accepted privacy boundary. |

## 4. Exact item, visibility and status model

### 4.1 Canonical item union

| Source arm | Canonical identity | Inclusion and precedence |
|---|---|---|
| Media | `media:<logical_media.id>` | One row per logical medium, whether bound or unbound. A binding controls authorization and projection. |
| Completed Search/Research | `question:<kronika_records.final_operation_id>` | One row per completed common record joined to its document. |
| Request without completed record | `question:<research_requests.operation_id>` | One row per durable request not represented by a completed common record. |

Completed-record existence takes precedence over the request’s lifecycle label. This handles the interval after atomic document save but before the request state is updated to `saved`.

Deduplicate requests against `kronika_records.final_operation_id`; also validate any populated request `record_id` against that relationship. A contradictory relationship is an integrity error, not permission to show both representations or fall back to another owner.

Media binding does not change the stable `media:` identity. Additional locations, acquisition claims, analysis runs, approval or withdrawal do not create additional items.

No future record kinds are invented. The current supported kinds remain `media`, `search` and `research`.

### 4.2 Visibility matrix

“Owner” below means common-record owner. An unbound requester retains existing requester access without being assigned invented ownership.

| Content | Owner / authorized requester | Application administrator | Other household member | Unauthenticated |
|---|---|---|---|---|
| Bound private media, including unfinished/failed | Current | Current | Denied | Denied |
| Bound approved family media | Current | Current | Approved snapshot | Denied |
| Bound withdrawn media | Current | Current | Denied | Denied |
| Unbound unpublished media with live requester access | Existing legacy/current working read | Current | Denied unless independently entitled | Denied |
| Unbound unpublished media without attribution | No inferred owner | Current | Denied | Denied |
| Unbound legacy-published media | Existing legacy read | Current | Existing legacy read | Denied by workspace Timeline |
| Private completed question | Current | Current | Denied | Denied |
| Approved family question | Current | Current | Approved document snapshot | Denied |
| Withdrawn question | Current | Current | Denied | Denied |
| Unfinished/failed/cancelled request | Own request | Existing administrator request read | Denied | Denied |

Apply existing route capabilities as well as object authorization:

- Media rows require the caller’s existing Gallery-read capability.
- Unfinished request rows require `research.run` and the existing request owner/administrator decision.
- Completed records follow the existing common-record read decision.
- No new capability is introduced.

Normal mapped user/admin roles already carry the corresponding read capabilities. Synthetic restricted-capability cases must still fail closed.

Every linked detail, preview, content and download request reauthorizes independently. A Timeline locator or item ID is not a capability.

### 4.3 Status vocabulary

`status` describes the authorized lifecycle view. `visibility` and `publication_state` describe sharing separately.

| Source state | Display label |
|---|---|
| Media with no `automatic_post_catalog` analysis run | Unanalysed |
| Media latest run `pending` | Analysis queued |
| Media latest run `analyzing` | Analysing |
| Media latest run `analyzed` | Analysed |
| Media latest run `failed` | Analysis failed |
| Request `admitted` | Queued |
| Request `submitting` | Submitting |
| Request `running` | Working |
| Request `validating` | Validating |
| Completed common question record | Saved |
| Request `refused` | Refused |
| Request `failed` | Failed |
| Request `incomplete` | Incomplete |
| Request `cancel_requested` | Cancellation requested |
| Request `cancelled` | Cancelled |
| Request `timeout` | Timed out |
| Request `submission_unknown` | Submission unknown |

For current media reads, select the latest run for `AUTOMATIC_POST_CATALOG_ANALYSIS_DEFINITION`, ordered by `created_at_ms DESC, id DESC`, matching the existing workflow’s recency rule.

For an approved household media read, display the approved successful state, not a newer private failure or in-progress run. For an approved document, display `saved`.

A request in `saved` state without its required completed-record relationship is an integrity error; do not manufacture a completed answer.

### 4.4 Visibility/publication vocabulary

| Derived value | Persisted evidence | Display |
|---|---|---|
| `visibility=private`, `publication_state=unpublished` | Private bound record without prior approval, private request, or unpublished unbound medium | Private · Unpublished |
| `visibility=private`, `publication_state=withdrawn` | Bound record private with retained approval evidence | Private · Withdrawn |
| `visibility=family`, `publication_state=approved` | Completed family common record with valid approval evidence | Household · Approved |
| `visibility=family`, `publication_state=legacy_published` | Unbound medium with existing publication row | Household · Legacy publication |

For unbound media, these are derived audience labels, not new `kronika_records` values. Do not reconstruct an unpublication history that the legacy tables do not retain.

Use generic private copy—“Visible only to authorized readers”—rather than “visible to you”, which is incorrect for an administrator reading another owner’s content.

An owner may see “Analysis failed · Household · Approved” after a failed reanalysis: the household still receives the prior approved projection. Explain that distinction in accessible descriptive text.

Internet publication remains a global disabled boundary, not a fabricated per-item lifecycle state. Show a short page note: **“Household sharing does not publish to the internet.”**

## 5. Current and proposed API contracts

### 5.1 Current contracts relevant to the change

| Endpoint | Current contract |
|---|---|
| `GET /api/timeline` | Verified identity; kind/category filters; page envelope; approved family common-record summaries only. |
| `GET /api/my/records` | Caller’s common records, current labels and current preview locator; administrator sees their own History here. |
| `GET /api/admin/records` | `records.approve`; common-record inventory, optional private/family filter; no preview field. |
| `GET /api/records/{record_id}` | Verified identity and bound-record decision; current or approved document metadata. |
| `GET /api/records/{record_id}/render` | Same object decision; sanitized HTML, `no-store`, restrictive CSP and `nosniff`. |
| `GET /api/research-requests/{operation_id}` | `research.run`, owner or existing administrator rule; existing request-view lifecycle behavior. |
| Gallery-preview/content/download routes | Existing capability plus shared media audience decision; approved-location restriction where applicable. |

The current Timeline item fields are:

`record_id`, `kind`, `owner_login_key`, `visibility`, `created_at_ms`, `completed_at_ms`, `timeline_entered_at_ms`, `version`, `media_id`, `read_decision`, `display_title`, `content_category`, `preview_location_id`.

The current JSON list route does not explicitly set a successful-response cache policy. Ingress-generated errors and rendered documents have their own existing headers.

### 5.2 Proposed `GET /api/timeline`

Keep the existing route policy entry with no new route-level capability. Require verified identity inside the adapter and derive all source decisions server-side.

| Parameter | Exact semantics |
|---|---|
| `limit` | Default 24, maximum 100; retain existing integer parsing/clamping behavior. |
| `offset` | Default 0; retain existing nonnegative normalization. |
| `kind` | Optional `media`, `search`, `research`. |
| `content_category` | Optional `general`, `meme`, `movie`, `youtube`; requires `kind=media`. |
| `q` | Optional trimmed text, maximum 240 code points; reject control characters. Literal substring search over the authorized title/question source. |
| `visibility` | Optional `private` or `family`, now allowed for every verified caller but only within that caller’s readable set. |
| `status` | Optional group: `unanalysed`, `in_progress`, `complete`, `failed`, `cancelled`. |
| `publication` | Optional `unpublished`, `approved`, `withdrawn`, `legacy_published`. |

Empty optional values mean absent. Unsupported values and invalid combinations return `422 INVALID_REQUEST`. Unrelated query parameters retain existing ignore behavior and never supply caller identity.

Status groups are fixed:

- `unanalysed`: media `not_requested`.
- `in_progress`: media `pending`/`analyzing`; request `admitted`, `submitting`, `running`, `validating`, `cancel_requested`.
- `complete`: media `analyzed`; completed question `saved`.
- `failed`: media `failed`; request `refused`, `failed`, `incomplete`, `timeout`, `submission_unknown`.
- `cancelled`: request `cancelled`.

Use the existing SQLite `NOCASE` literal-substring convention, escaping `%`, `_` and the escape character. Do not promise Unicode accent folding or full-text search. Question search operates on the authorized question text, including text beyond the shortened display title; it never searches answers.

Response envelope remains:

```text
items: TimelineItem[]
total: integer
limit: integer
offset: integer
```

Exact item contract:

| Field | Type / nullability |
|---|---|
| `item_id` | Non-null stable namespaced string defined in §4.1 |
| `kind` | `media` / `search` / `research` |
| `media_kind` | `video` / `animated_image` / `image`; null for questions |
| `record_id` | Common-record ID or null |
| `media_id` | Media ID or null |
| `operation_id` | Question operation ID or null for media |
| `display_title` | Authorized normalized title, at most 240 code points, or null |
| `content_category` | Existing category or null |
| `created_at_ms` | Nonnegative UTC epoch milliseconds |
| `status` | Exact media/request state from §4.3; completed questions use `saved` |
| `visibility` | `private` / `family`, persisted or derived as specified |
| `publication_state` | Exact value from §4.4 |
| `read_decision` | `current` / `approved` / `legacy` |
| `preview_location_id` | One eligible location ID or null |

For title normalization, collapse whitespace and truncate to 240 code points including the ellipsis. Null media titles use the existing “Untitled media” fallback. No provider naming request occurs.

Do not return owner/contributor identities, answer text, citations, provider configuration, errors from providers, approval JSON, location arrays, paths, filenames, cache keys or readiness state.

Ordering: `created_at_ms DESC`, then `item_id ASC` using deterministic binary ordering. Dates mean original media creation or original question admission, not approval time.

`total` is the count of distinct authorized items after every selected filter and before pagination. An offset beyond the end returns an empty `items` array and the correct total.

Response handling:

- `200`: valid page, including empty pages.
- `401 IDENTITY_REQUIRED`: no verified identity.
- Existing ingress identity/mapping denials remain unchanged.
- `422 INVALID_REQUEST`: invalid filters.
- `500 TIMELINE_UNAVAILABLE`: sanitized persistence/integrity failure; fixed message “The Timeline is unavailable.”
- All Timeline responses use `Cache-Control: private, no-store`.
- No Timeline ETag or `304`.
- No new mutation endpoint or action.

Use Timeline-specific serialization and error handling. Do not make the new item shape a nullable extension of `RecordSummary`, and do not alter other record response key sets.

### 5.3 Internal interfaces

Add `TimelinePageQuery`, `TimelineItem`, `TimelinePage` and a sanitized reader-error type in `application/ports/timeline.py`.

Retain `RecordService.list_timeline` as the application entry point, extending its arguments for the new filters and returning `TimelinePage`.

Change `RecordRepository.list_timeline` to accept/return the Timeline types. `SqliteRecordRepository.list_timeline` delegates to a new `SqliteTimelineReader` in `timeline_repository.py`.

This preserves current composition and dependency injection. No `application.py` composition change is needed.

Remove the obsolete approved-only branch from the record list implementation once Timeline delegates to its reader. History and administrator inventory continue using their existing record-specific query and summary types. Remove the unused `timeline_includes` helper; preserve all actual domain read and approval decisions.

## 6. Exact SQL and performance plan

### 6.1 Read strategy

Perform the read on one connection inside an explicit SQLite **read transaction**. Issue `BEGIN` before the first SELECT; do not assume SQLAlchemy’s logical transaction alone establishes a SQLite snapshot under the current sqlite3 connection behavior.

Use a SQLAlchemy Core CTE/subquery pipeline:

1. Build distinct live requester media IDs for the caller from the exact upload, successful YouTube and successful X predicates.
2. Rank automatic analysis runs once by medium and select rank one.
3. Build the media arm from `logical_media`, optional binding, current metadata, approved metadata and legacy publication truth.
4. Derive media read decision with binding precedence. Select current or approved label/status columns with that decision.
5. Build the completed-question arm from common records/documents. Current reads select current question text. Approved reads extract the approved document’s question text from the stored projection using SQL JSON extraction; never fall back to current question text.
6. Build the request arm for owner/administrator-readable requests lacking a completed common record. Exclude completed operations before union.
7. `UNION ALL` the three already-disjoint arms. Apply query, kind, category, visibility, status and publication filters to that authorized projection.
8. Count the filtered union.
9. Select the ordered page.
10. Resolve preview locators for eligible page media in one additional batch.

Use bound parameters. Never call record detail, request detail or `ContentAudiencePolicy.read_decision` once per item in the production reader.

Binding, document, metadata and publication joins are one-to-one. Requester IDs are deduplicated before joining. Locations, tags and analysis history must not multiply page rows.

Approved document SQL extracts only needed question fields. It does not transfer the whole approval blob or answer into Python. Invalid required projection data returns the sanitized integrity failure; it does not expose working content.

### 6.2 Preview batch

For page items with `media_kind` `video` or `animated_image`:

- `approved`: select `MIN(location_id)` from available approved locations, joined through the matching approved medium.
- `current` or `legacy`: select `MIN(physical_media_locations.id)` for that medium with availability `available`.
- Combine these branches into one grouped, page-bounded SELECT.
- Select IDs only.
- Return null for still images, non-media and media without an eligible location.
- Do not read the preview cache, probe files, select a second location after failure or generate a derivative.

The existing preview GET remains the final audience, relationship and readiness check.

### 6.3 Query budget and indexes

| Page | Data SELECT budget |
|---|---|
| Empty or questions-only | Two: count and page |
| Page with eligible video/GIF media | Three: count, page, locator batch |
| Page size 1, 24 or 100 | Same SELECT count for the corresponding composition |

Transaction control statements are recorded separately from the data SELECT count.

No new index or migration is proposed. Existing primary/unique keys support common-record media/document/operation joins; existing requester, physical-location, approved-location and analysis-history indexes support the component reads. The mixed-source order and literal substring search may require scans and temporary sorting. This is an explicit foundation-stage tradeoff.

Validate plans with synthetic mixed data and `EXPLAIN QUERY PLAN`; record representative timings without claiming a production-scale latency guarantee. Reject an implementation that introduces repeated full-source work per output item. A measured need for a new index is a bounded follow-up requiring an amended allowlist and migration decision before publication.

The read transaction makes count, page and locator selection consistent within one response. Offset pagination is deterministic for unchanged data; it does not promise a frozen catalog across separate HTTP requests.

## 7. UI and accessibility specification

### 7.1 Structure

Replace only the Timeline results presentation with a semantic ordered list:

- `#kronika-timeline-results` becomes `<ol class="kronika-chronicle">`.
- Each item is one `<li>` with aligned fields.
- A desktop visual header is `aria-hidden`; each row retains accessible field labels using the existing `visually-hidden` utility.
- Do not simulate an ARIA grid or introduce custom arrow-key navigation.

Desktop layout above 720 px:

| Field | Treatment |
|---|---|
| Preview | Fixed 36 × 36 px decorative slot |
| Item | Flexible title link, at most two visible lines |
| Kind | Search, Research, or current media-category label |
| Added | UTC date/time |
| Status | Text label from §4.3 |
| Visibility | Private/Household and publication-state text |

Use compact horizontal separators and existing palette, typography and focus tokens. Do not apply `.kronika-card`, Gallery hover transforms or large cover imagery.

At 720 px and below, keep one list row per item. Place thumbnail beside title; wrap kind, date, status and visibility below it with visible labels. No horizontal page scrolling at 320 px. Preserve 44 px interactive targets.

### 7.2 Filters and states

Replace the Timeline kind chips with a labelled select containing the same eight choices: All, Search, Research, Media, General, Memes, Movies, YouTube.

Add labelled Status, Visibility and Publication selects, plus a Timeline-local search form with explicit submit and clear controls. Do not repurpose Gallery’s command search.

The hash route retains the existing `filter` and `offset` spelling and adds `q`, `status`, `visibility`, `publication`. Existing kind/category links remain valid. Filter/search changes reset offset to zero. Pagination preserves every filter. All query fields participate in request identity and stale-response checks.

No localStorage or other persistent list cache is added.

Page copy:

- Lede: “Everything you can access in Kronika — newest first.”
- Empty unfiltered: “Nothing has been added that you can access yet.”
- Empty filtered: “No items match these filters.”
- Loading: existing polite status plus `aria-busy`.
- Transport refresh failure: retain only the last page for the exact same identity and query, clearly marked stale, with Retry.
- Identity loss or permission denial: clear rows, previews and cached list state immediately.
- Changed-query failure: do not retain another query’s rows.
- Show range and filtered total beside pagination.
- When withdrawal or filtering leaves an out-of-range page, offer an explicit return to the first page; do not repeatedly refetch automatically.

### 7.3 Links and focus

- Media title → existing `#/details/<media_id>`.
- Completed question → existing `#/records/<record_id>`.
- Request → existing `#/requests/<operation_id>`.
- Encode identifiers and set all content through text nodes.
- No inline playback, approval, download or provider controls are added to rows.

For Timeline-originated Details navigation, retain the complete originating hash and stable item ID. Extend only the existing navigation glue so closing Details restores the Timeline route and focuses the originating title link after reload; fall back to the Timeline heading if the row is gone. Gallery-originated Details behavior stays unchanged.

Browser back/forward preserves Timeline filters. Ordinary route changes focus the destination heading. Filter/search submissions retain focus on their initiating control; pagination moves focus to the Timeline heading. Retry must not steal focus.

The row’s title link has a descriptive accessible name. Use `<time datetime="…">` with visible UTC formatting and a full timestamp. Status and visibility use text, not color alone.

### 7.4 Preview and lifecycle preservation

Reuse `kronikaAttachCardPreview` on the dedicated row preview slot and retain its existing runtime buckets and generation checks. Keep the helper’s lazy decorative image attributes and URL builder.

Adapt Timeline-scoped CSS to the new slot. Keep History’s existing card selectors and dimensions unchanged.

Preserve:

- icon while loading and after every error;
- image reveal only on successful load;
- no extra focus target;
- no automatic retries or detail discovery;
- retirement on accepted navigation, identity change and `pagehide`;
- no retirement merely on `visibilitychange`;
- no teardown when dirty-navigation confirmation is cancelled.

Timeline loading makes one list request plus eligible image requests. It introduces no per-row request polling. Existing request-detail behavior remains in the explicit request view.

Review copy changes:

- “Not on Timeline” → “Private”
- “On Timeline” → “Shared with household”
- “Approve for Timeline” → “Approve for household”
- “Withdraw from Timeline” → “Withdraw household sharing”

Preserve the existing approval actions, version checks and inventory endpoints.

## 8. Exact implementation changed-path allowlist

This is the proposed later implementation allowlist, not current write authority.

### Source

| Path | Purpose |
|---|---|
| `src/kronika/application/ports/timeline.py` — new | Timeline query/page/item values and sanitized reader error. |
| `src/kronika/infrastructure/persistence/timeline_repository.py` — new | Authorized union, snapshot, filters, count/page and batched locators. |
| `src/kronika/application/records.py` | Timeline argument validation and new return type. |
| `src/kronika/application/ports/records.py` | Update only the Timeline method’s contract. |
| `src/kronika/infrastructure/persistence/record_repository.py` | Delegate Timeline reads; remove obsolete Timeline-only list branches while preserving record workflows. |
| `src/kronika/domain/record_access.py` | Remove unused approved-only `timeline_includes`; retain read/approval decisions. |
| `src/kronika/adapters/api/records_api.py` | Timeline-specific parameters, payload and sanitized no-store responses. |
| `src/kronika/adapters/api/web/index.html` | Timeline list/filter markup and household Review labels. |
| `src/kronika/adapters/api/web/app.js` | Timeline renderer, filter/route state, preview reuse, return-focus glue and sharing copy. |
| `src/kronika/adapters/api/web/styles.css` | Timeline-scoped compact/responsive list rules. |

### Tests

| Path | Purpose |
|---|---|
| `tests/integration/persistence/test_timeline_repository.py` — new | Union, authorization parity, deduplication, ordering, snapshot and query-budget evidence. |
| `tests/contract/test_timeline_api.py` — new | New wire contract and list-to-direct-route audience matrix. |
| `tests/unit/application/test_records.py` | Timeline validation and preservation of approval behavior. |
| `tests/integration/persistence/test_kronika_record_repository.py` | Deliberately replace old Timeline assumptions; preserve History and transaction tests. |
| `tests/contract/test_records_api.py` | Update Timeline expectations; preserve non-Timeline response contracts. |
| `tests/contract/test_kronika_approved_projection.py` | Separate chronicle visibility from retained approval timestamp/snapshot invariants. |
| `tests/contract/test_kronika_access_inventory.py` | Correct Timeline inventory projection and make inventory verification read-only. |
| `tests/contract/test_local_web_application.py` | Served Timeline markup and frozen Gallery/Details checks. |
| `tests/kronika_ui.test.js` | New list/filter behavior and preserved lifecycle/fallback behavior. |

### Documentation

| Path | Purpose |
|---|---|
| `docs/adr/0087-complete-visibility-aware-timeline-chronicle.md` — new | Accepted decision after explicit Cooperator approval. |
| `docs/adr/README.md` | New ADR row and partial-supersession relationship. |
| `AGENTS.md` | Current product boundary and decision pointer. |
| `SPEC.md` | Normative Timeline/API/preview behavior. |
| `SECURITY.md` | Authorized list union and projection boundary. |
| `README.md` | Concise current-source overview and canonical pointers. |
| `PRODUCT.md` | Experience and view boundaries. |
| `SERVER.md` | Server-owned read model and route responsibility. |
| `ROADMAP.md` | Current chronicle successor while preserving completed historical rows. |
| `DEVELOPMENT.md` | Focused validation and rendered-acceptance guidance. |
| `GALLERY.md` | Narrow cross-reference distinguishing Timeline list from Gallery. |
| `docs/KRONIKA_ACCESS_INVENTORY.md` | Exact revised Timeline inventory row. |

Negative allowlist:

- `.ap/**`, AP gitlink, `ap.project.conf`, upgrade ledger and dependency files.
- `catalog_schema.py`, all Alembic migrations and database writers outside the named record reader changes.
- `ContentAudiencePolicy`, `content_audience_api.py`, preview/content/download routes and public composition.
- Identity/capability definitions, ingress route-policy table and authentication configuration.
- Upload/acquisition pipelines, research coordinator/provider adapters and capture module.
- `extension/**`, `deploy/**`, operator scripts and host configuration.
- Gallery/Details renderer bodies, player behavior and their visual selectors, except the explicitly bounded Timeline return-navigation glue.
- Accepted ADR-0082 through ADR-0086 bodies.
- `docs/UX_AUDIT.md`, predecessor notes/reports, run map and handouts.
- All other paths.

Any required expansion returns to the Orchestrator before mutation.

## 9. Tests and validation

### 9.1 Existing tests deliberately updated

| Existing identity | Required change |
|---|---|
| `test_records_api.py::test_timeline_membership_is_approved_for_every_caller` | Replace with owner/admin current membership and cross-owner approved-only membership. After withdrawal, owner/admin retain the row; the other member loses it. |
| `test_record_list_filters_reject_invalid_combinations` | Timeline private/family filters now succeed within caller scope. Invalid values and invalid category combinations still fail. History restrictions remain. |
| `test_media_list_preview_locator_is_additive_and_path_free` | Retain History contract; replace the assertion that private owner media is absent from Timeline. |
| `test_working_only_preview_location_is_not_disclosed_on_timeline` | Retain its household-negative assertion and add owner/admin current-locator assertions. |
| Repository `test_list_filters_apply_before_count_and_keep_order` | Retain History/inventory checks; replace owner/admin empty-Timeline assumptions. |
| Repository `test_timeline_titles_stay_on_the_approved_projection` | Require approved title/category only for another household member; owner/admin receive working values. |
| Repository `test_timeline_preview_locator_uses_only_approved_locations_for_every_caller` | Replace the all-caller rule with per-decision locator selection. |
| Approval tests referencing Timeline timestamps | Verify retained first-approval timestamp through record detail/storage; separately verify creation-time chronicle order. |
| UI “personal history keeps failed requests out of the timeline” | Replace semantic exclusion with separate-endpoint behavior plus owner-visible failed Timeline rows. |
| UI card/thumbnail tests | Adapt Timeline assertions to list rows while keeping History card assertions and all lifecycle negatives. |

These are product-decision changes only after ADR-0087 acceptance. They are not blanket permission to weaken privacy or ignore failures.

Preserve unchanged behavioral coverage for:

- owner/stranger/admin domain decisions;
- approval conflict, replay, rollback and concurrency;
- approved answers/media surviving working changes until reapproval;
- History’s current locator and constant query count;
- preview denial before cache access, conditional-request denial and GET-never-generates;
- sandboxed document rendering and citation behavior;
- research request lifecycle/idempotency/cancellation;
- workspace requester access and public route exclusion;
- Gallery still-image/GIF/Details/player behavior.

Change `test_inventory_matches_both_compositions_and_route_policies` from automatic `INVENTORY.write_text(...)` to an exact comparison assertion. The authorized implementation updates the inventory file explicitly. A read-only acceptance run must fail on drift rather than rewrite tracked evidence.

### 9.2 New causal tests

In `tests/integration/persistence/test_timeline_repository.py`:

- `test_timeline_union_deduplicates_media_and_saved_requests`
- `test_timeline_item_identity_survives_binding_and_save`
- `test_timeline_sql_matches_existing_audience_policy`
- `test_timeline_binding_precedes_legacy_publication_and_contributions`
- `test_timeline_household_uses_only_approved_labels_and_status`
- `test_timeline_filters_counts_and_tie_order_use_authorized_projection`
- `test_timeline_count_page_and_locators_share_one_snapshot`
- `test_timeline_page_query_count_is_constant`
- `test_timeline_read_does_not_probe_files_or_load_answer_payloads`

The snapshot regression uses a synthetic WAL-mode temporary database solely in the test fixture so a writer can commit between count and page SELECTs. The explicit reader snapshot must preserve one consistent response. Do not change production journal configuration.

In `tests/contract/test_timeline_api.py`:

- `test_timeline_visibility_matches_direct_reads`
- `test_timeline_filters_cannot_widen_identity_scope`
- `test_timeline_request_lifecycle_and_saved_transition`
- `test_timeline_preview_locator_round_trip_and_withdrawal`
- `test_timeline_contract_is_bounded_sanitized_and_no_store`
- `test_timeline_denies_anonymous_and_is_absent_from_public_composition`
- `test_timeline_loading_never_calls_research_or_preview_generation`

Parametrize the real persistence/policy matrix across bound/unbound, attribution sources and their unsuccessful states, publication, withdrawal, analysis states and every research lifecycle state. Use synthetic identities/catalogs and harmless fixture bytes.

In `tests/kronika_ui.test.js`, add:

- “Timeline renders a compact chronicle with distinct status and visibility”
- “Timeline filters preserve route state and reset pagination”
- “Timeline rows link media, saved records and unfinished requests”
- “Timeline text stays inert and list loading performs no detail fan-out”
- “Timeline Details return restores the originating row or heading”

Retain and adapt the existing preview, stale-response, identity-loss, dirty-navigation, `visibilitychange` and `pagehide` regressions.

### 9.3 Later command routes

These commands are for a separately authorized implementation/acceptance exchange, not execution in this planning exchange. Use the canonical checkout and the exact trusted execution-contract baseline below; the later grant must also bind the actual candidate commit.

```text
# [MacBook / fish]
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline b66ec8f50860ace624f6be1fd3ad63f521edcd33
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline b66ec8f50860ace624f6be1fd3ad63f521edcd33 --operation test-focus -- tests/integration/persistence/test_timeline_repository.py tests/integration/persistence/test_kronika_record_repository.py tests/contract/test_timeline_api.py tests/contract/test_records_api.py tests/contract/test_kronika_approved_projection.py tests/contract/test_kronika_access_inventory.py tests/contract/test_gallery_preview_api.py tests/contract/test_content_audience_policy.py tests/contract/test_research_requests_api.py tests/contract/test_workspace_media.py tests/contract/test_public_published_uds.py tests/unit/application/test_records.py tests/unit/domain/test_record_access.py tests/unit/application/test_content_audience_requester_private.py -q -p no:cacheprovider
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline b66ec8f50860ace624f6be1fd3ad63f521edcd33 --operation test-focus -- tests/contract/test_local_web_application.py -k 'kronika_shell or details or persistent_preview or initial_card or available_cards or gallery' -q -p no:cacheprovider
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline b66ec8f50860ace624f6be1fd3ad63f521edcd33 --operation test-focus -- tests/contract/test_tailscale_ingress_security.py -k 'route_policies_match_the_application_route_inventory or requester_private_media_detail_reaches_application_through_ingress or missing_identity_login_is_rejected' -q -p no:cacheprovider
node --test tests/kronika_ui.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js
git diff --check
git status --short
#------------------------------------------------------
```

Run each selected gate once per materially changed candidate. Diagnose failures narrowly before repeating a broader selection. No full suite, browser-toolchain install or live-provider test is prescribed.

Baseline evidence actually used here is source/test inspection plus the repository/AP gates in §1. Historical test counts from whole 01 are not fresh test results for this whole.

## 10. Acceptance control matrix

Exact test-file aliases used below:

- **TR** = `tests/integration/persistence/test_timeline_repository.py`
- **TA** = `tests/contract/test_timeline_api.py`
- **UI** = `tests/kronika_ui.test.js`
- **GP** = `tests/contract/test_gallery_preview_api.py`
- **AI** = `tests/contract/test_kronika_access_inventory.py`

The later fresh auditor owns automated E3 acceptance. Michal owns rendered acceptance. All new tests below are planned and have not run.

| Claim ID | Surface | Exact positive and negative claim | Evidence type | Exact test/command/observation | Tier | Acceptance owner | Pass criteria | Current gap |
|---|---|---|---|---|---|---|---|---|
| C01 | Private media | Owner sees private media; another member does not | Real SQL + API | TA::test_timeline_visibility_matches_direct_reads | E3 | Fresh auditor | Correct list/count and direct-read outcomes | New reader absent |
| C02 | Administrator | Administrator sees all authorized content, including unattributed media; no host/secrets privilege added | SQL/API + diff | Same TA test; allowlist review | E3 | Fresh auditor | Complete content coverage, no privileged expansion | New aggregation absent |
| C03 | Household | Another member sees approved projection only; working title/status/location cannot leak | SQL/API | TR::test_timeline_household_uses_only_approved_labels_and_status | E3 | Fresh auditor | Snapshot values and filters stay frozen | Current tests assume all callers approved |
| C04 | Anonymous/public | Workspace Timeline denies anonymous; public composition has no Timeline route | Composed API | TA::test_timeline_denies_anonymous_and_is_absent_from_public_composition | E3 | Fresh auditor | No items/counts disclosed | New explicit case needed |
| C05 | Unanalysed | Readable catalog media without run/record appears once; no synthetic record is written | SQL + storage comparison | TR::test_timeline_union_deduplicates_media_and_saved_requests | E3 | Fresh auditor | One row, `not_requested`, unchanged stored rows | Absent today |
| C06 | Analysing | Current reader sees pending/analyzing; household cannot infer private reanalysis | State matrix | TA::test_timeline_visibility_matches_direct_reads | E3 | Fresh auditor | Correct current/snapshot statuses | New cases |
| C07 | Failed | Failed media/request visible to authorized caller only | State matrix | Same TA test | E3 | Fresh auditor | Failure states do not widen sharing | New cases |
| C08 | Unfinished request | Own/admin admitted and active requests appear; other member denied | Real request rows | TA::test_timeline_request_lifecycle_and_saved_transition | E3 | Fresh auditor | Every nonterminal state covered | Absent today |
| C09 | Saved question | Save produces one completed item with unchanged identity | Atomic-save integration | Same TA test; TR identity test | E3 | Fresh auditor | No duplicate during validating→saved interval | Union absent |
| C10 | Withdrawal | Owner/admin retain private withdrawn item; household loses item and cached preview access | API transition | TA::test_timeline_preview_locator_round_trip_and_withdrawal | E3 | Fresh auditor | Denial precedes cache/304 | Existing partial coverage |
| C11 | Approval | Approval shares without moving chronicle creation order | Approval transition | TR::test_timeline_filters_counts_and_tie_order_use_authorized_projection | E3 | Fresh auditor | Stable identity/date, explicit sharing | New ordering |
| C12 | Legacy publication | Unbound publication remains readable; bound private record takes precedence | SQL/policy parity | TR::test_timeline_binding_precedes_legacy_publication_and_contributions | E3 | Fresh auditor | Legacy path preserved without bypass | New combined case |
| C13 | Attribution | Success-state requester rules match direct media policy; mere stamp does not grant access | Policy parity | TR::test_timeline_sql_matches_existing_audience_policy | E3 | Fresh auditor | Upload/YT/X positive and negative states agree | General attribution is broader |
| C14 | Deduplication | Multiple claims/locations/runs do not duplicate media; saved request not duplicated | SQL | TR::test_timeline_union_deduplicates_media_and_saved_requests | E3 | Fresh auditor | One canonical item | New union |
| C15 | Ordering | Equal timestamps have deterministic cross-source order; approval/save does not reorder identity | SQL | TR::test_timeline_item_identity_survives_binding_and_save; tie-order test | E2 | Fresh auditor | Repeatable binary tie order | New key |
| C16 | Pagination/totals | Every filter applies before count/page; unauthorized matches contribute zero | SQL/API | TR filter/count test; TA::test_timeline_filters_cannot_widen_identity_scope | E3 | Fresh auditor | Correct totals and bounded pages | New filters |
| C17 | Snapshot | Count/page/locator read one database snapshot | Concurrent synthetic test | TR::test_timeline_count_page_and_locators_share_one_snapshot | E3 | Fresh auditor | No mixed response during concurrent mutation | New transaction |
| C18 | Query budget | 1/24/100-item pages use fixed SELECT count; no filesystem/detail fan-out | SQL instrumentation/spies | TR::test_timeline_page_query_count_is_constant; read-probe test | E2 | Fresh auditor | Two or three SELECTs as specified | New reader |
| C19 | Preview | Correct current/approved locator; null/error retains icon and never generates | API + DOM | TA preview round-trip; GP denial/generation tests; preserved UI preview tests | E3/E2 | Fresh auditor | No unauthorized cache open or retry | Timeline selection changes |
| C20 | Payload | No answers, paths, filenames, cache state, provider errors or identities in summaries | Exact keys + sentinels | TA::test_timeline_contract_is_bounded_sanitized_and_no_store | E3 | Fresh auditor | Exact bounded shape and headers | New contract |
| C21 | Route inventory | Route/capability set unchanged; documented Timeline predicate matches implementation | Composition inventory | AI::test_inventory_matches_both_compositions_and_route_policies | E3 | Fresh auditor | Exact inventory equality without writes | Inventory text stale for proposal |
| C22 | Accessibility | Semantic list, labelled controls, inert text, useful focus and narrow layout | DOM + rendered | New UI chronicle/filter/return tests; NUC checklist | E2 + rendered | Fresh auditor / Michal | Keyboard and 320/390 px behavior accepted | Rendered evidence missing |
| C23 | Frozen views | Gallery/Details visuals/player and History preview behavior preserved | Focused regressions + diff | §9.3 Node/web selection; NUC comparison | E2 + rendered | Fresh auditor / Michal | No unintended visual/player change | Candidate absent |
| C24 | Side effects/leakage | Timeline reads do not call provider/generation or expose host/secret values | Spies + diff/report review | TA generation test; exact allowlist and report review | E3 | Fresh auditor | Zero new side effects; public-safe evidence | Implementation pending |

## 11. Documentation-promotion inventory

ADR-0087 owns the architecture decision; SPEC owns normative product behavior. Other documents summarize or operationalize those owners.

| Target and heading | Exact current claim or gap | Replacement/addition | Validation and owner |
|---|---|---|---|
| New ADR-0087 | No complete-chronicle decision exists | Decision text and transition in §3; accepted only after explicit Cooperator event | Cooperator decision; Orchestrator reconciliation |
| `docs/adr/README.md` — relationship and ADR table | ADR-0083 current except fixed-model correction | Add ADR-0087 and identify only approved-only Timeline membership as superseded, with explicit chronology consequence | ADR cross-links/status review; architecture index |
| `AGENTS.md` — Accepted Direction / Product Boundaries | “Timeline … contains only administrator-approved records”; completion alone does not enter Timeline | Timeline includes all caller-readable content; approval governs household sharing, not personal/admin membership | Compare ADR/SPEC/security matrix; project-rule owner |
| `SPEC.md` — “Timeline, Personal History and Completion” | Approved-only landing; pending/failed outside shared Timeline; all Timeline titles/locators approved | Normative union, stable identity, original creation order, caller-specific projection, filters, new item contract and compact list | API/SQL/UI tests; normative product owner |
| `SPEC.md` — Gallery/privacy and publication restatements | “The shared Timeline contains only administrator-approved records” | Timeline membership follows existing read access; cross-owner household visibility remains administrator-controlled | Contradiction search and matrix; SPEC |
| `SECURITY.md` — Accepted Privacy Boundary / Preview Locators | Approved-only Timeline and approved locations for every caller | Same existing authorization predicates govern list/count/search; approved versus current locator follows read decision; no-store summaries | Fresh E3 matrix; security-policy owner |
| `README.md` — Accepted Transition / preview overview | Approved-only main page and Timeline cards | Compact complete authorized chronicle, separate Gallery/History, ready-preview fallback; link to SPEC/ADR | Source/diff and eventual public ref; overview owner |
| `PRODUCT.md` — Accepted Experience / Security Principles | “newest approved entry first”; completion/failure do not create shared card | Newest added readable item first; completion/failure affects lifecycle, while household approval remains separate | ADR/SPEC comparison; product owner |
| `SERVER.md` — Application Boundary / Records and Ingress | Timeline receives no card before approval | Server-owned authorized union; pure read path, no per-item coordinator calls; same content guards | Source/query-plan review; server architecture owner |
| `ROADMAP.md` — Active Sequence/current proofs | Shared Timeline exclusion until approval; completed S4-D/S8 history | Add current ADR-0087 successor and replace active proof with cross-owner exclusion until approval. Keep completed rows as historical accomplishments, not reopened tasks | Historical/current distinction and link review; roadmap owner |
| `DEVELOPMENT.md` — Preview Backfill/validation | Timeline media cards reuse icon slot | Compact Timeline rows and unchanged History cards; updated focused commands and NUC-first rendered route | Commands/path inspection; developer guide |
| `GALLERY.md` — persistent-preview paragraph | SPEC owns Timeline/History card reuse | SPEC owns Timeline-row and History-card reuse; Gallery/Details remain separate | Existing Gallery tests and narrow diff; Gallery reference |
| `docs/KRONIKA_ACCESS_INVENTORY.md` — GET `/api/timeline` row | Approved family only; approved projection for every caller; misleading administrator capability wording | Verified identity; no added route capability; exact source predicates and caller-specific projection; explicit positive/negative Timeline tests | Exact read-only inventory test; implementation inventory |

Update all current restatements of the changed rule within these allowlisted owners, including publication paragraphs that equate Timeline entry with household sharing. Do not replace unrelated cover-selection “timeline” terminology.

Preserve accepted ADR bodies, `docs/UX_AUDIT.md` and frozen Meta evidence. Existing stale provider, stage or host prose unrelated to this decision is not a cleanup grant.

Document source behavior without claiming publication, deployment or rendered acceptance before evidence exists.

## 12. Acceptance, execution and NUC sequence

### 12.1 Smallest coherent candidate and acceptance route

Implement one coherent source candidate covering the full union, authorization projection, API, list UI, tests and durable owners. Shipping a private-media-only or approved-plus-media intermediate Timeline would leave unfinished research and deduplication incomplete; it must not be presented as completion of this whole.

No additional product slices are required by this design. Publication, deployment and rendered acceptance remain separately authorized phases.

Recommend **E3 fresh focused authorization acceptance**, corresponding to the focused R3 route if the later security profile is activated. Although direct guards remain unchanged, the main-page list now exposes private content through newly written SQL predicates, counts and search. Implementation self-tests alone do not establish that boundary.

Use one primary fresh independent acceptance and at most one correction/re-acceptance cycle for the same finding. A security/runtime/projection correction requires fresh acceptance of the full affected matrix. No audit-of-an-audit and no second automatic correction.

### 12.2 Sequence and session decisions

| Step | Route and completion gate |
|---|---|
| Preserve report | Authorized persister stores this exact report; do not replan or change its status. |
| Accept decision | Michal accepts ADR-0087 semantics; Orchestrator reconciles the plan and accepted boundary. |
| Separate source preflight | Fresh Worker session 02, native planning not used; read-only E3 preflight verifies baseline, exact allowlist, security predicates, test side effects and rollback. |
| Implementation | Healthy session 02 may continue under a complete renewed grant. Implement all source behavior, tests and documentation; one normal local candidate commit on explicitly granted `main`; no push/deploy implied. |
| Independent acceptance | Fresh session 03 with no material implementation participation or inherited implementation reasoning. Fixed candidate, matrix and paths; read-only source plus authorized synthetic temporary test state. |
| Correction if needed | One smallest authorized correction; no self-certification. Fresh independent re-acceptance follows AP. |
| Publication | Complete separate grant or Cooperator action; ordinary non-force publication of the exact accepted commit. Verify public `main` equality. Healthy implementation session may perform this mechanical step under renewal. |
| NUC preflight | Separate bounded host-read grant, canonical helper status/check and rollback verification. No deployment follows automatically. |
| NUC deployment | Explicit exact-SHA release grant after preflight and fresh sudo preparation. A healthy operational session may continue under renewal. |
| Rendered acceptance | Michal tests the exact public-main release now served by the NUC. |
| Closure | Orchestrator reconciles source acceptance, publication, deployment, rendered verdict, residual risk and ledger disposition. Worker does not close. |

All Worker prompts are manually delivered by Michal. No subagents. Each prompt/report uses actual next coordinates and the configured Meta filename mapping. Each capable Worker writes and reads back its report when client controls permit. Meta Git remains Michal’s responsibility.

### 12.3 NUC preconditions and routine commands

The later grant must bind:

- **T**: exact accepted commit then verified on public `main`.
- **P**: exact previous complete release observed during fresh status, retained as rollback target.
- Matching accepted AP pin, clean checkout, ready backup/restore evidence, no active mutation and usable canonical tooling.
- Existing private transport configuration through `KRONIKA_NUC_SSH_TARGET`, `KRONIKA_NUC_SSH_USER`, `KRONIKA_NUC_SSH_IDENTITY`; no values enter reports.
- Worker gate capability probe and permitted BatchMode transport.
- Fresh Cooperator sudo timestamp.

Michal performs sudo preparation outside the Worker in an already-open NUC session:

```text
# [NUC / bash]
sudo -v
sudo -n true
#------------------------------------------------------
```

Workers never run `sudo -v` or handle a password. They verify `sudo -n true` through the authorized canonical gate.

The exact later helper sequence is:

1. `deploy/ubuntu/kronika-release status`
2. `deploy/ubuntu/kronika-release check --release <T>`
3. Stop for the explicit exact-release deployment authority.
4. `deploy/ubuntu/kronika-release deploy --release <T> --yes`
5. `deploy/ubuntu/kronika-release status`

The later prompt substitutes actual 40-hex values before delivery. **A check never deploys automatically.**

Reuse exactly the runbook tooling:

- Poetry: `/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry`
- CPython: `/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13`

No `uv`, bootstrap, capture transition or host redesign is included.

No schema change is proposed; target head remains `0035`. If a future deployment reports exit 13, preserve that result and use only the runbook’s “Schema-jump continuation after migration-required” under explicit matching authority:

- confirm the complete target tree and that the previous release remains active;
- observe actual current/target revisions;
- inspect and remove only exact documented residual lock objects;
- migrate from the target release tree;
- verify target schema equality;
- use the documented `rollback --release <T> --yes` cutover to the already-complete target;
- verify final status and release privilege.

Do not improvise downgrade or catalog restore after a schema-related failure.

### 12.4 Post-deploy and rollback evidence

Require:

- `active_release = web_release = T`;
- capture release unchanged from its freshly observed preflight value;
- service active, health/database readiness successful;
- schema equal to target head;
- backup restore readiness `ready`;
- release provenance from canonical release markers/manifests, not `.git`;
- served shell contains the new chronicle markup;
- bounded authenticated API checks use supported identity access and report only sanitized counts/statuses.

On same-schema cutover/readiness failure, preserve the helper’s automatic recovery result. If an explicit rollback is required, use only `deploy/ubuntu/kronika-release rollback --release <P> --yes` under its bounded authority, then status/readiness checks. Never invent an `/opt/kronika/rollback` tree or a manual symlink deployment route.

The privileged Worker runs terminal `sudo -K` through the canonical gate. If the session is lost first, report privilege release unknown.

### 12.5 Michal’s rendered checklist

After release identity is verified, request itemized `PASS`, `FAIL` or `NOT TESTED`:

1. Timeline is a compact chronological list with small thumbnails, rather than a Gallery grid.
2. Own private, unanalysed and unpublished catalog media are present with accurate labels.
3. Administrator view includes authorized other-owner/unattributed content; ordinary household view does not disclose private work.
4. Queued/running, failed, cancelled and saved questions have clear distinct states; saving does not duplicate a row.
5. Approval changes household sharing without moving creation order; withdrawal retains personal/admin visibility and removes other-member access.
6. Ready previews reveal correctly; missing/offline/denied/failed previews retain icons.
7. Search, filters, totals and pagination preserve state through navigation and browser back/forward.
8. Keyboard focus, Details return and controls work; no color-only meaning or narrow-screen overflow at 390 px and 320 px.
9. Backgrounding/restoring the tab preserves previews; identity change clears private content.
10. Gallery, Details playback and History retain their accepted behavior.

Use existing suitable content only under Michal’s authority. Missing state examples remain `NOT TESTED`; do not create failures through live provider calls. Any required NUC fixture preparation needs a separate exact-object grant. Michal decides whether remaining visual gaps are covered by accepted synthetic evidence or require that bounded fixture work.

Whole 01’s paused rendered acceptance remains carried historical context; this report does not declare it satisfied.

## 13. Decisions, risks, deltas and closeout

### Required decisions and chosen defaults

There is no unresolved technical choice needed to implement this plan.

Required material gate: Michal accepts the exact ADR-0087 semantics before implementation. Publication, host access, deployment, any fixture mutation and rendered acceptance require their own later authority.

Defaults fixed by this plan:

- “Everything added” means existing catalog content plus durable question requests, not pre-catalog staging operations.
- One current-content row per medium/question, not an event log.
- Original creation/admission chronology, UTC display, stable namespaced identity.
- Existing requester access for unbound media; no fabricated ownership.
- One evolved `/api/timeline`; no second endpoint or client aggregation.
- Default 24, maximum 100; offset pagination.
- One full source candidate, no schema migration or new dependency.
- Gallery/Details visual freeze and personal History preserved.
- E3 fresh independent authorization acceptance.

### C1–C8 risk mapping

| Risk | Control and owner |
|---|---|
| C1 — private/unpublished disclosure | Exact SQL/policy parity, binding precedence, filtered counts/search and direct-route matrix; fresh auditor. |
| C2 — silent ADR reinterpretation | Explicit ADR-0087 acceptance and downstream promotion; Michal/Orchestrator. |
| C3 — invented/duplicated records | Read-only union and stable source identities; atomic-save/binding regressions; implementation Worker/auditor. |
| C4 — N+1 or main-page cost | Two/three SELECT budget, set-based joins, explicit snapshot and query-plan inspection; implementation Worker/auditor. |
| C5 — second Gallery/data dump | Compact semantic list, dedicated scoped CSS and Cooperator rendered checklist. |
| C6 — test-pin churn | Named deliberate expectation changes; preserve approval, privacy and player invariants; auditor. |
| C7 — weakened publication semantics | Separate status/visibility/publication fields, corrected Review copy and unchanged mutation path; auditor. |
| C8 — predecessor/deferred interaction | Preserve preview lifecycle correction and History behavior; do not open upload-flow-polish; Orchestrator. |

Residual limitations:

- Unbound attribution remains existing access evidence rather than a completed common-record ownership implementation.
- Mixed-source substring search and sorting have no production-scale latency guarantee.
- Separate HTTP pages can shift when the catalog changes.
- Real rendering and browser lifecycle behavior require Michal’s NUC acceptance.
- NUC state, transport capability, current sudo timestamp and suitable rendered fixtures remain unobserved here.
- No bfcache redesign, global accessibility pass, localization, companion change or `app.js` modularization is included.

### Inventory deltas against the prompt

- Confirmed the absence of production `bind_media_record` callers.
- Confirmed the saved-request/common-record/document overlap.
- Refined attribution: live YouTube/X success predicates are stricter than general contribution stamps.
- Refined catalog reuse: the generic catalog scope predicate alone is insufficient for Timeline parity with direct reads.
- Identified completed-record precedence during the save-to-`saved` lifecycle interval.
- Identified misleading Review copy that must change with Timeline membership.
- Identified the inventory test’s tracked-file rewrite behavior; planned exact read-only comparison instead.
- Preserved the actual `visibilitychange` correction at `b66ec8f`.
- Found no new session-routing or P4 contradiction in this issued prompt.

### AP protocol friction observed

- Exchanges 01/01 and 01/02 consumed coordinates on different prompt defects before a plan existed. The current prompt fixes both and correctly preserves `Planning cycle: initial`.
- Active native Plan Mode still prohibits the trace write. The current P4 route permits exact-content return, so this is a delivery limitation rather than another planning stop.
- No AP modification or ledger implementation is proposed. The existing ledger entry remains accepted/non-authorizing/retain-active; this exchange did not revalidate or mutate it.

### Resolved Execution Issues / Near-Misses

The current prompt’s route, continuity and completion checks passed before substantive planning resumed.

The inventory test’s automatic tracked-document write was detected through source inspection. It was not executed in this read-only exchange. Its conversion to an assertion is included in the proposed implementation allowlist.

### Pre-Existing Failure Classification

none. No tests failed or were executed in this exchange. Historical test results are not promoted into current evidence.

### Smallest next step

Persist this complete exact report through the authorized completion route, then let the Orchestrator reconcile it and obtain Michal’s explicit ADR-0087 acceptance. No further planning cycle or implementation in this session is authorized.

### Authority expiry

Submission of this terminal report expires this exchange’s planning authority. The plan remains approval-gated. A fresh Implementation Worker needs a complete new grant with native planning mode not used. No publication, deployment, acceptance or logical-whole closure is granted here.

Orchestration critique:  
MEASURED: The two preceding prompt defects consumed exchanges without producing a plan; the current prompt corrects routing and P4 and allowed the initial plan to complete. Future grants should compare routing, stopping conditions and the actual client completion route together before issue.  
LEAD: none.
