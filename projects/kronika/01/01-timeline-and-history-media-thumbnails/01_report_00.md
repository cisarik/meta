### Report for ORCHESTRATOR_CHAT

# Timeline and History media thumbnails — implementation plan

```text
Logical whole identity: timeline-and-history-media-thumbnails
Worker session ordinal: 01
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Task identity: KRN-THT-PLAN-01 — plan-only — Timeline and History media thumbnails on the existing gallery preview pipeline

Status: PARTIAL
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Start commit: 246c9f86b72e652cd36ed0d9f4e19e77f972df91
End commit: 246c9f86b72e652cd36ed0d9f4e19e77f972df91
Report justification: new-evidence
Repository changes: none
Git writes, commit and push: none
NUC, browser and provider contact: none
```

**Planning content is complete; required file delivery is incomplete.** Native Plan Mode is enabled, but the governing client instructions prohibit file writes, including trace persistence. The complete report is preserved here. `/Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/01_report_00.md` was absent at both checks and was not created. No saved-file readback is claimed. AP’s Planning Budget and Expiry and Planner-Artifact Report Completion Repair provide the completion route: persist this exact report through a permitted, positively authorized route without replanning.

## 1. Summary and verified baseline

Add one nullable preview location identifier to the Timeline and personal-record list responses. Resolve it in one page-bounded repository query. Render the existing JPEG preview over the card’s existing kind-icon position, revealing it only after successful loading. Preserve the icon during loading and after every failure.

Use the existing preview endpoint, authorization policy, server cache and browser HTTP cache. Preserve Gallery, Details, question History, Review, approval rules and preview generation.

Recommended implementation acceptance is **E2 plus Cooperator rendered acceptance on the exact public-main NUC release**. This recommendation applies only to the safe-locator design below. Changing the preview route, audience guard or response beyond that locator requires fresh independent acceptance.

### Planning record

```text
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
```

This was a fresh session for this whole. No sub-agents were used.

### Re-measured repository gate

| Check | Observation |
|---|---|
| Physical checkout and topology | `/Users/agile/Projects/kronika`, standalone Git checkout |
| Branch | `main`, tracking `origin/main` |
| HEAD and local `origin/main` | `246c9f86b72e652cd36ed0d9f4e19e77f972df91` |
| Public `refs/heads/main` | Same SHA, observed through `git ls-remote` |
| Working tree | Clean before inspection and at finishing |
| Containing `.ap` gitlink | `d7023cf037f6d17885c3ede5c04812c61640da50` |
| `.ap` HEAD | Same SHA; clean submodule |
| `./.ap/ap doctor` | PASS; stable governing variant |
| Bound `ap project check` | PASS; CPython 3.13 |
| Report destination | Absent; no overwrite attempted |

The project check sanitized inherited `SSH_AUTH_SOCK`, `PATH` and `GIT_PAGER` classes. No values were exposed. The additional `GIT_PAGER` warning is an environment difference from the prompt’s example, not a failed gate.

`git diff --stat cb5fa4d 246c9f8 -- src extension alembic migrations` was empty. HEAD changes only the AP pin and its integration-test expectation. `app.js` is exactly **15,322 lines**.

AP public `main` was not contacted: this exchange grants public network verification of Kronika only. The governing AP pin and its local equality were verified.

## 2. Re-measured current-state map

### Rendering and presentation

| Surface | Exact path and behavior |
|---|---|
| Timeline | `src/kronika/adapters/api/web/app.js`: `kronikaLoadTimeline` at line 14129 calls `/api/timeline`, then `kronikaRenderCards` at line 14104. |
| Shared card builder | Creates `<a class="kronika-card">`, calls `kronikaTagCardKind`, appends `<strong>` title and `<small>` kind. Timeline subsequently adds the formatted approval-entry day to `<small>`. |
| Timeline links | Media with `media_id` links to `#/details/{media_id}`; other records link to `#/records/{record_id}`. |
| Personal record History | `kronikaLoadHistory` at line 14194 selects `kronikaLists.records` and `/api/my/records` for `#/history/records`. It builds cards directly rather than calling `kronikaRenderCards`. Media and document links follow Timeline’s distinction. Metadata contains kind plus `kronikaVisibilityLabel`. |
| Personal question History | The same loader selects `kronikaLists.questions` and `/api/research-requests` for `#/history`. Cards link to a saved `record_id`, otherwise to `operation_id`. Metadata contains kind plus request state. These are Search/Research requests, including unfinished and failed work. |
| Title | `kronikaCardTitle` at line 14060: nonblank `display_title`; otherwise “Untitled media” for media; otherwise `prompt`; otherwise “Untitled”. |
| Kind label | `kronikaKindLabel` at line 14067 maps Search, Research and media categories to existing English labels. |
| Kind attribute | `kronikaTagCardKind` at line 14081 sets `data-kronika-kind` from media `content_category`, falling back to `media`, or from non-media `kind`. |
| Other caller | Administrator Review also calls `kronikaTagCardKind`; it must remain icon-only in this whole. |
| Templates | `index.html`: `#kronika-timeline-results` at line 865 and `#kronika-history-results` at line 886, both `.kronika-grid`, with `data-kronika-list="timeline"` or `"history"`. Cards are generated in JavaScript; no card template exists in HTML. |
| CSS | `styles.css` contains layered `.kronika-card` rules at lines 5395, 5443 and 5958. The effective experience-layer rule reserves left padding of 64 px. |
| Icon | `.kronika-card::before` at line 5969 supplies a 36×36 px box at top/left 14 px. Default 📄; selectors at lines 5984–5990 provide Search 💬, Research 🔬, Media 🎞️, General 📁, Meme 😂, Movie 🎬 and YouTube ▶️. |

There is no existing Timeline/History thumbnail element, preview state or preview locator consumption.

### List APIs and repository path

`src/kronika/adapters/api/records_api.py` owns `_summary_payload`, `_page_payload`, `/api/timeline` and `/api/my/records`.

Both lists return:

```text
items, total, limit, offset
```

Each item currently contains exactly:

```text
record_id
kind
owner_login_key
visibility
created_at_ms
completed_at_ms
timeline_entered_at_ms
version
media_id
read_decision
display_title
content_category
```

For media, `media_id` is present but no location identifier or preview URL exists. Search/Research summaries have no media locator and no answer text.

The summary type is **`RecordSummary` in `src/kronika/application/ports/records.py`**, not in `domain/records.py`. `RecordService` delegates lists to `SqliteRecordRepository`.

`record_repository.py`:

- `list_own_history` supplies the caller’s `login_key`, including for an administrator.
- `list_timeline` selects the approved-family list.
- `_list` applies filters before counting and pagination. Timeline uses entry time descending and stable record ID; History uses creation time descending and stable record ID.
- `_summary_labels` batches title/category reads. Timeline labels come from `kronika_approved_media`; personal labels come from current metadata.
- `_summary` builds `RecordSummary`.
- Timeline summaries deliberately report `READ_APPROVED` for every caller.
- Personal summaries use `decide_bound_read`; ownership means current state.

Existing page construction already selects complete record rows. The proposed change must not add per-record projection parsing, detail reads or filesystem inspection.

Question History has a separate response owner: `research_api.py::_summary`. Its fields include `operation_id`, `kind`, `state`, `error_code`, `prompt`, lifecycle timestamps, `record_id`, provider/model identifiers, configuration version and accounting state. It has no media reference and needs no API change.

### Existing preview route and audience

`gallery_preview_api.py` serves:

```text
GET /api/media/{media_id}/locations/{location_id}/gallery-preview
```

The decision path is:

1. Validate UUIDv4 route parameters.
2. Check catalog availability.
3. Call `content_audience_decision`.
4. Deny before `preview_service.open_ready` when the audience decision denies.
5. For `READ_APPROVED`, load the frozen approval projection and require the requested location ID to occur in its locations.
6. Call `GalleryPreviewService.open_ready`, which validates the media/location relationship, library, availability, supported format and current derivative readiness.

`content_audience_api.py` denies missing policy or verified identity and treats policy failures as unavailable. `ContentAudiencePolicy.read_decision` checks a common-record binding first:

| Caller and record | Existing decision |
|---|---|
| Owner | Current working media |
| Application administrator | Current working media |
| Other household member, completed and approved family record | Approved projection |
| Other household member, private or unfinished record | Deny |
| No verified identity | Deny |
| Unbound legacy media | Existing published/requester policy, unchanged |

`tailscale_ingress.py` additionally requires `gallery.read` for the preview route. Both mapped ordinary users and administrators have that capability. Record list routes require verified identity.

**No new audience guard is required for this design.** Timeline locator selection will use approved locations even for owners and administrators. Direct preview requests retain the existing caller-specific decision.

This does not introduce an immutable snapshot of JPEG bytes at approval. The existing endpoint restricts approved location membership and opens the current valid derivative for that location.

### Cache and failure behavior

| Result | Current behavior |
|---|---|
| Ready | JPEG, `200`, quoted payload-digest ETag, `Content-Disposition: inline`, `nosniff`, content length |
| Ready cache policy | `private, max-age=0, must-revalidate` |
| Matching `If-None-Match` | `304`, empty body, after audience and readiness checks |
| Denied/missing/mismatched location | Sanitized `404 GALLERY_PREVIEW_NOT_FOUND` |
| Missing, stale, unavailable or unsupported derivative | Sanitized `409 GALLERY_PREVIEW_UNAVAILABLE` |
| Audience/cache/repository failure | Sanitized `500 GALLERY_PREVIEW_FAILED` |
| Catalog unavailable | Sanitized `503 CATALOG_UNAVAILABLE` |
| Invalid route identifiers | Framework validation rejection |
| Route-generated errors | `Cache-Control: no-store` |

`GalleryPreviewService.open_ready` never invokes generation. Cache identity includes algorithm, media/location identity, media kind, source size and modification time. A source change makes an old derivative stale.

The derivative pipeline supports video/animated-image media. Still images use original content in Gallery and are explicitly excluded from this derivative pipeline.

The separate public-published composition has a preview route, but its publication repository excludes every common-record-bound medium. Its preview response uses `no-store`. It must remain untouched.

### Existing tests and their limits

| File | Exact existing identities and relevance |
|---|---|
| `tests/kronika_ui.test.js` | “shell markup keeps the gallery and sandboxed answer frame”; “empty hash selects Timeline and details stay reachable”; “timeline requests only its endpoint, including for an administrator”; “personal history keeps failed requests out of the timeline”; “a failed refresh keeps only the previous authorized page”; “identity loss clears private content and dirty navigation can be cancelled”. |
| `tests/contract/test_records_api.py` | `test_household_member_sees_only_the_approved_projection`; `test_anonymous_is_denied_everywhere`; `test_summaries_keep_hostile_titles_and_omit_answers`; `test_timeline_membership_is_approved_for_every_caller`; `test_record_list_filters_reject_invalid_combinations`; `test_unready_media_cannot_be_approved`. |
| `tests/integration/persistence/test_kronika_record_repository.py` | `test_list_filters_apply_before_count_and_keep_order`; `test_timeline_titles_stay_on_the_approved_projection`. |
| `tests/contract/test_gallery_preview_api.py` | `test_preview_denial_does_not_open_the_cache`; `test_gallery_preview_returns_jpeg_etag_and_no_paths`; `test_gallery_preview_matching_if_none_match_returns_304`; `test_missing_derivative_is_not_generated_by_get_and_error_is_sanitized`; `test_endpoint_validates_relationship_error_as_not_found`; `test_catalog_unavailable_returns_503_without_path_disclosure`. |
| `tests/contract/test_kronika_approved_projection.py` | `test_household_http_reads_keep_the_approved_media_projection`; `test_withdrawal_keeps_timeline_position_and_snapshot`; `test_household_keeps_approved_answer_until_reapproval`. The media test checks new working-location denial for content/download, but does not establish the complete new list-to-preview path. |
| `tests/contract/test_content_audience_policy.py` | `test_every_direct_surface_denies_unpublished_like_unknown` includes gallery-preview; principally legacy audience evidence. |
| `tests/contract/test_kronika_access_inventory.py` | `test_inventory_matches_both_compositions_and_route_policies` and parametrized workspace/public reachability and refusal tests. These are route coverage, not a substitute for bound-record preview audience tests. |
| `tests/unit/test_gallery_preview.py` | Missing-until-generated, source-change staleness, unavailable/unsupported media, cache symlink rejection and source-root write protection. |
| `tests/contract/test_research_requests_api.py` | `test_submission_progress_and_owner_separation`; `test_cancel_confirms_and_history_reflects_state`; preserve question History behavior. |
| `tests/contract/test_local_web_application.py` | `test_kronika_shell_adds_timeline_without_replacing_gallery`; persistent-preview, identity-only URL, initial-render, Details attributes, cleanup and stale-event tests. |
| Gallery Node suites | `gallery_still_image_render`, `gallery_gif_inline_toggle`, `gallery_details_playback_handoff` and `cover_frontend` pin the frozen presentation and playback behavior. |

Only `kronika_ui.test.js` matched the searched Timeline/History/card selectors among the inspected tests. Its harness pins child positions, copy and endpoint selection. It does **not** currently prove Timeline/History thumbnail CSS or image lifecycle. New behavioral coverage is necessary.

## 3. Proposed smallest design

### Server data flow and interface

Add:

```text
RecordSummary.preview_location_id: str | None = None
```

Expose `preview_location_id` only in items returned by `/api/timeline` and `/api/my/records`. The JSON value is a canonical location identifier or `null`. Existing `media_id` supplies the other URL component.

Use an explicit serialization option on `_page_payload`/`_summary_payload` so administrator inventory and detail response shapes do not change incidentally.

Implement a page-level repository helper, `_summary_preview_locations`, returning a record-ID-to-location-ID mapping:

- Call it after audience filtering and pagination.
- Execute at most one additional SQL query for a page containing eligible media.
- Select identifiers only; use grouped `MIN(location_id)` for deterministic lexical selection.
- For Timeline, select from `kronika_approved_media_locations`, joined through the approved medium, restricted to approved `availability="available"`.
- For personal History, select current `physical_media_locations` belonging to the page’s media, restricted to `availability="available"`.
- Restrict technical media kind to `video` or `animated_image`.
- Return `null` for non-media, still images, missing candidates and all unavailable candidates.
- Do not compute preview readiness, open files, inspect the cache, parse each approval JSON or call a media-detail service.
- Do not populate locators for administrator inventory or record detail.

The locator is a candidate, not a readiness assertion. An unsupported extension or changed filesystem state may still cause the existing preview route to reject it.

No migration, persistent column, new endpoint, configuration setting or service wiring is needed.

### Location and fallback policy

Select exactly one deterministic eligible location. Do not search locations in the browser or retry another location after a failure.

| Situation | Client result |
|---|---|
| Authorized ready video/GIF preview | Reveal JPEG in the existing icon position |
| Non-media or question History | Existing kind icon |
| Still image | Existing kind icon; no original-content request |
| Null/missing locator | Existing kind icon; no preview request |
| Loading | Existing kind icon remains visible |
| Missing/stale/not-ready/unavailable preview | Existing kind icon |
| Unauthorized, withdrawn, deleted or mismatched preview | Existing kind icon |
| Server/network/decode failure | Existing kind icon |
| Unsupported format | Existing kind icon |

There is no automatic retry, alternate-location cascade, generation request or cover/original-content fallback. A later explicit navigation, page load or refresh can make a new attempt.

### Rendering and CSS

Add one helper, `kronikaAttachCardPreview`, called:

- By `kronikaRenderCards` for Timeline media cards.
- In the personal-record branch of `kronikaLoadHistory`.
- Never in question History or Review.

Keep `kronikaTagCardKind` and all existing kind selectors.

Append an `<img class="kronika-card__preview">` after the existing title and metadata so their child order remains intact. Use:

```text
alt=""
aria-hidden="true"
loading="lazy"
decoding="async"
width=36
height=36
```

Build the same-origin URL through existing `mediaGalleryPreviewUrl(media_id, preview_location_id)`. Do not accept a server-supplied URL, host or path.

Use `data-kronika-preview` states `loading`, `ready` and `fallback`. Install load/error handlers before assigning `src`.

Scope all new CSS to the two results containers:

- Place the image over the existing 36 px icon box with the same border/radius.
- Use `object-fit: cover`.
- Keep the loading image transparent rather than `display:none`, so lazy loading can proceed.
- Reveal the image and hide the pseudo-icon only in `ready`.
- On error, detach handlers, remove the image source/element and retain the pseudo-icon.

Preserve padding, text, card size, links, hover/focus treatment and navigation. The existing title and metadata remain the accessible link name. The image is decorative and adds no focus target or announcement.

### Request bounds, cancellation and caching

Keep the client page size at 24. Do not add prefetching or load all records.

The implementation eliminates **N+1 locator/detail discovery**: one list request already carries every needed locator. Rendering separate images through the fixed per-location endpoint necessarily permits one image GET per eligible card. The bound is **one list request plus at most 24 preview attempts per mounted page**, often fewer because of native lazy loading. A claim of zero per-image HTTP requests would require a different endpoint or transport and is not part of this design.

Use native `<img>` delivery:

- Browser HTTP caching performs conditional revalidation under the existing private cache policy.
- Do not add cache-busting parameters, `fetch(..., cache:"no-store")` for images, object URLs, persistent browser storage or a second preview cache.
- A browser normally resolves a network `304` using its cached representation; the image handler need not parse `304`.

Add teardown for the two list surfaces:

- Detach handlers and remove image `src` on accepted navigation, page/filter/tab replacement, identity change and document teardown.
- Fence image callbacks with identity and page generations.
- Invalidate outstanding Timeline/History list generations when leaving them.
- Give these list JSON requests an `AbortController`, passed through an optional signal argument to `kronikaReadJson`; abort on supersession or departure.
- Preserve the dirty-navigation refusal: cancellation occurs only after navigation is accepted.
- Do not change other `kronikaReadJson` callers.

Removing an image source releases the client’s image request, but server-side completion after dispatch is browser-dependent. Do not claim a guaranteed server abort. The safety invariant is no late image revelation, no newly scheduled work for the departed page and a fixed page request bound.

### Rejected alternatives

| Alternative | Reason rejected |
|---|---|
| Fetch each media detail to find locations | Adds N+1 discovery and exposes a larger payload |
| Return complete locations or approval projections | Unnecessary paths and metadata; larger response/privacy surface |
| New thumbnail/batch endpoint | Duplicates the accepted delivery boundary |
| Read cache readiness during every list | Filesystem work on list requests; cache/application coupling |
| Retry all locations | Multiplies requests and complicates approved-location handling |
| Reuse Gallery card renderer | Imports playback, cover preference and frozen presentation |
| Use still-image `/content` fallback | Transfers original media and changes the bounded derivative policy |
| Fetch JPEGs as blobs with a custom queue/cache | More lifecycle state than the 24-item native-image design requires |
| Enlarge cards or add a new preview panel | Reopens presentation beyond replacing the kind-icon slot |

## 4. Exact implementation changed-path allowlist

This is a proposed allowlist for a later complete implementation grant, not current mutation authority.

| Path | Purpose |
|---|---|
| `src/kronika/application/ports/records.py` | Nullable summary locator field |
| `src/kronika/infrastructure/persistence/record_repository.py` | One page-batched, audience-source-specific locator query |
| `src/kronika/adapters/api/records_api.py` | Locator serialization on the two selected list endpoints |
| `src/kronika/adapters/api/web/app.js` | Card preview helper and bounded list/image lifecycle |
| `src/kronika/adapters/api/web/styles.css` | Scoped replacement of the icon slot |
| `tests/integration/persistence/test_kronika_record_repository.py` | Deterministic selection, approved/current source separation and constant query count |
| `tests/contract/test_records_api.py` | Additive response contract and end-to-end list-to-preview audience evidence |
| `tests/contract/test_gallery_preview_api.py` | Strengthen cache/error/conditional-request negatives without route changes |
| `tests/kronika_ui.test.js` | Preview lifecycle, request bounds, fallback, accessibility and CSS contracts |
| `SPEC.md` | Normative card behavior and safe-locator contract |
| `SECURITY.md` | Locator disclosure boundary and unchanged authorization-before-cache rule |
| `GALLERY.md` | Reuse cross-reference and narrowly correct preview-generation wording |
| `DEVELOPMENT.md` | Focused validation and synthetic/manual acceptance guidance |
| `README.md` | One concise status pointer to implemented card previews and SPEC |

**No new files are required.**

Negative allowlist:

- `.ap/**`, `AGENTS.md`, `ap.project.conf`, dependency manifests and lockfiles.
- Schema definitions, Alembic files and migration history.
- Preview route, audience-policy and record-access implementations.
- Public-published composition and route-policy tables.
- Gallery/Details renderers, playback, cover selection and their CSS.
- `index.html`, asset packaging and framework/toolchain files.
- Research, provider, upload, acquisition and capture implementations.
- `extension/**`, deployment helpers, systemd and host configuration.
- Existing ADR bodies and ADR index.
- Frozen `docs/UX_AUDIT.md`, access inventory, AP upgrade ledger and repository handoffs.
- All Meta files except a separately permitted exact report-persistence operation.

A need to edit a negative-allowlisted boundary stops implementation for Orchestrator review.

## 5. Tests and validation plan

### Existing tests to preserve

Preserve every existing assertion listed in §2. In particular:

- Timeline still uses `/api/timeline`, including for administrators.
- Personal History stays owner-filtered, including an administrator’s personal view.
- Pending/failed questions never become Timeline cards.
- Titles remain inert text; answer text stays out of summaries.
- Approval, withdrawal, ordering, totals and pagination remain unchanged.
- Preview GET never generates.
- Gallery’s cover preference, still-image original-content behavior, GIF toggle and Details playback remain unchanged.

The existing “timeline requests only its endpoint…” fixture contains Search, so its current assertion remains correct. Add a separate media case distinguishing image requests from forbidden detail discovery.

Extend the UI harness to model image properties/events, source removal and `AbortController`. Evaluate the actual existing `mediaGalleryPreviewUrl` helper alongside the shell extraction; do not duplicate its URL logic as a fake implementation.

Existing tests need harness support, not weakened expectations. New CSS assertions belong in `kronika_ui.test.js`, which currently lacks that coverage.

### New causal tests

The following are proposed exact identities.

| File | New test identity and causal invariant |
|---|---|
| Repository integration | `test_history_preview_locator_selects_one_current_available_location` — insertion order cannot change the selected identifier |
| Repository integration | `test_timeline_preview_locator_uses_only_approved_locations_for_every_caller` — adding a lexically earlier working-only location cannot leak it into Timeline |
| Repository integration | `test_preview_locators_are_null_for_nonmedia_still_images_and_unavailable_locations` |
| Repository integration | `test_record_preview_locator_queries_are_constant_per_page` — compare 1, 24 and 100 media rows; at most one added locator query, no per-row lookup |
| Records API | `test_media_list_preview_locator_is_additive_and_path_free` — field is ID/null; no locations, paths, cache keys or answers |
| Records API | `test_list_preview_locator_round_trip_preserves_record_audience` — real binding/policy with synthetic preview service; owner/admin private success, household denial, approval success |
| Records API | `test_working_only_preview_location_is_not_disclosed_on_timeline` — approved versus later working location |
| Records API | `test_withdrawn_preview_is_denied_even_with_a_cached_etag` — withdrawal must defeat conditional cache access |
| Records API | `test_preview_locator_does_not_change_admin_or_detail_response_shapes` |
| Preview API | `test_preview_errors_are_no_store_and_sanitized` — include failed service and audience-policy failure |
| Preview API | `test_preview_denial_with_if_none_match_does_not_open_cache` |
| Preview API | `test_preview_not_ready_with_if_none_match_does_not_return_304` |
| Node UI | “media cards use one lazy decorative preview and preserve their link names” |
| Node UI | “question history and non-media cards never request previews” |
| Node UI | “preview load reveals the image and every error retains the kind icon” |
| Node UI | “24 media cards require no media detail discovery or automatic retries” |
| Node UI | “navigation and identity changes retire previews and ignore late events” |
| Node UI | “superseded Timeline and History requests cannot repaint a departed view” |
| Node UI | “cancelled dirty navigation preserves the current preview page” |
| Node UI | “thumbnail CSS changes only the Timeline and History icon slots” |

Use synthetic identifiers, temporary catalogs and harmless fixture bytes. No real provider, private media or browser credentials are needed.

### Exact later command routes

For an implementation granted against the current baseline, run from the repository root:

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

If baseline changes before the implementation grant, the Orchestrator must bind a newly verified exact baseline. The Worker must not substitute HEAD autonomously.

Review the exact diff, path allowlist, serialization field set, CSS scope and unchanged security owners. Run the selected regression set once per materially changed candidate; diagnose failures narrowly before repeating. No full suite or browser automation is required by this plan.

### Evidence actually used in this exchange

Only repository/public provenance gates and static source/test/document inspection were used. No focused Python or Node tests were executed: reading established the planning claims. Existing test names are evidence coverage, not a claim that those suites passed in this exchange.

## 6. Acceptance control matrix

All implementation tests below remain **not executed/new evidence pending**. Current evidence is static planning evidence at the verified baseline.

| Claim ID | Surface | Exact claim, positive and negative | Evidence type | Exact test/command/observation | Tier | Acceptance owner | Pass criteria | Current gap |
|---|---|---|---|---|---|---|---|---|
| T1 | Media card | Ready authorized JPEG appears; link and text retain meaning | DOM behavior + rendered | New “media cards use one lazy decorative preview…”; NUC checklist | E2 + rendered | Orchestrator; Cooperator visual | Image replaces icon only after load | Not implemented |
| T2 | Non-media/questions | Existing kind icons remain; no preview request | DOM/network harness | New “question history and non-media cards never request previews” | E2 | Orchestrator | Zero preview sources for these cards | New test needed |
| T3 | Missing/not-ready | Icon survives null locator, 404 and 409; GET never repairs cache | API + DOM | Existing missing-derivative contract; new UI error test | E2 | Orchestrator | No broken image, generation or retry | Card coverage absent |
| T4 | Failed/unauthorized | Network/decode/500/503/authorization failures retain icon | API + DOM | New preview error tests and UI error test | E2 | Orchestrator | No sensitive error copy or alternate resource | New cases needed |
| T5 | Owner/admin | Both may read authorized private media previews; privilege grants no host/secrets access | Synthetic bound-policy contract + diff | `test_list_preview_locator_round_trip_preserves_record_audience` | E2 | Orchestrator | Correct private read and unchanged policy | Existing tests do not join list and preview |
| T6 | Household | Approved locations readable; private, unfinished and working-only locations denied | Contract + repository | New round-trip and approved-locator tests | E2 | Orchestrator | Denial before cache open; no locator leakage | New tests needed |
| T7 | Timeline | Approved-family records only for every caller | Existing API + new locator test | `test_timeline_membership_is_approved_for_every_caller`; approved-locator test | E2 | Orchestrator | Membership/order/count unchanged | Preserve existing coverage |
| T8 | Personal History | Lists only caller’s records, including administrator’s own history | API + repository | Existing summaries test; new round-trip test | E2 | Orchestrator | No administrator-wide inventory substitution | Media fixture needed |
| T9 | Generation | GET opens ready derivative only; no generation/provider call | Existing real-service unit + route inspection | `test_missing_derivative_is_not_served_until_generated`; missing-GET contract | E2 | Orchestrator | No generation call or generation-path diff | Preserve evidence |
| T10 | N+1/bounds | One locator query per page; no per-card details; ≤24 image attempts per mounted page | SQL instrumentation + DOM harness | Constant-query test; new 24-card test | E2 | Orchestrator | Counts independent of record count; no automatic retries | New tests needed |
| T11 | Cache | Authorized ready response revalidates; denied/not-ready response cannot return 304 | HTTP contract | Existing ETag test; new denial/not-ready ETag tests | E2 | Orchestrator | Private cache policy; correct 200/304/errors | Negative conditional cases absent |
| T12 | Lifecycle | Departed/changed identity cannot reveal late previews or repaint old lists | Deferred promises/events | New navigation, identity and supersession UI tests | E2 | Orchestrator | Aborted list signal and ignored late events | New lifecycle coverage |
| T13 | Accessibility | Decorative image; meaningful card link name; no new focus target | DOM/CSS + rendered keyboard check | New lazy/decorative test; Cooperator checklist | E2 + rendered | Orchestrator; Cooperator visual | Empty alt, hidden image semantics, intact focus/link | New image coverage |
| T14 | Gallery/Details | Existing visuals, covers and playback unchanged | Diff + existing regressions + rendered comparison | Listed Gallery/Details Node suites; selected web contracts | E2 + rendered | Orchestrator; Cooperator visual | No renderer/CSS change outside selected cards | Candidate pending |
| T15 | Disclosure/public | Only safe IDs added; no paths, secrets or public access to records | Payload/diff + public inventory | New path-free test; access-inventory tests | E2 | Orchestrator | Exact added field; public composition unchanged | Candidate pending |
| T16 | Deployment identity | Rendered acceptance uses accepted public-main SHA on NUC | Public Git + helper status + Cooperator | Later `status → check → authorized deploy → status` | Operational + rendered | Deployment Worker; Cooperator | Exact release equality, readiness and explicit visual verdict | No NUC contact granted |

## 7. Acceptance route and documentation promotion

### Acceptance recommendation

Use **E2 implementation verification followed by direct Orchestrator acceptance and Cooperator rendered acceptance**.

The design adds a locator selected from rows the caller may already read. It neither changes object authorization nor opens a new delivery route. Household locations come from the existing approved projection; the preview endpoint rechecks authorization on every request, including conditional requests.

A fresh independent security acceptance session becomes mandatory if the candidate:

- Changes `gallery_preview_api.py`, `content_audience_api.py`, `ContentAudiencePolicy` or record-access decisions.
- Returns full location data, arbitrary URLs, readiness/state beyond the proposed safe locator, or otherwise expands the response boundary.
- Alters public projection, route capabilities or cache authorization order.

Do not silently expand the allowlist to accommodate such a change. This Planner performs and claims no implementation acceptance.

### Documentation promotion inventory

| File and section | Current gap | Exact promotion | Validation and owner |
|---|---|---|---|
| `SPEC.md` — “Timeline, Personal History and Completion” | Defines lists and titles, not thumbnails | Own the normative preview-locator, icon fallback, approved/current selection, 24-card client bound and no-detail-discovery behavior | Compare with new API/repository/UI tests; product requirements owner |
| `SECURITY.md` — “Accepted Kronika Privacy and Research Boundary” | General preview policy exists; locator disclosure is unstated | Only opaque location identity is added after list authorization; Timeline uses approved locations; preview request still reauthorizes before cache/304 | Payload and audience tests; security-policy owner |
| `GALLERY.md` — current persistent-preview description | Reuse boundary absent; generation wording still says operator-only | Add a short link to SPEC for Timeline/History reuse; narrowly replace operator-only wording with a reference to accepted ADR-0086 backfill and explicit operator generation | Source/ADR comparison; Gallery reference owner; no new thumbnail semantics |
| `DEVELOPMENT.md` — “Companion And Gallery Preview Backfill” | No thumbnail verification guidance | Add selected tests and synthetic acceptance cases; explain still-image/icon behavior and that current NUC publication precedes rendered acceptance | Verify command paths and links; development workflow owner |
| `README.md` — published shell/status prose | Omits the bounded capability | One concise sentence that Timeline and personal Records cards reuse ready media previews with icon fallback; link to SPEC | Final accepted diff and publication identity; repository overview owner |
| `docs/UX_AUDIT.md` | Historical “not yet implemented” recommendation | **No edit.** Its Status requires frozen historical retention. Current implementation truth belongs in SPEC/README | Preserve historical authority and cleanup contract |
| `PRODUCT.md`, `SERVER.md`, `ROADMAP.md` | Omit this small presentation addition | **No edit.** Existing direction already permits it; no closed slice or architecture changes | Confirm no contradictory claim is introduced |
| Existing ADRs and `docs/adr/README.md` | No missing architecture decision | **No new ADR.** Reuse follows ADR-0083/0086 without changing architecture | Orchestrator verifies boundary |
| Access inventory, env example, AP ledger | No new route/config/protocol behavior | **No edit** | Inventory regression and exact diff |

The stale operator-only sentence in GALLERY is superseded by ADR-0086 and current code. This is a narrow correction relevant to explaining preview availability, not a reopening of the predecessor whole. Other unrelated stale stage prose remains outside this change.

## 8. Later NUC refresh and rendered acceptance

**No command in this section was executed. No NUC contact is authorized by this report.**

### Preconditions and later grant

The later bounded deployment grant must name:

- Exact accepted release SHA `T`, published as GitHub `main`.
- Clean local checkout at `T`, matching `.ap` gitlink/submodule, and public-ref equality.
- One active accountable deployment session, no competing mutation.
- Fresh current-release observation and retained rollback SHA `P`.
- Verified catalog backup/restore readiness and checkpoint/recovery handling.
- Canonical layout and accepted pinned Poetry/CPython tooling.
- Explicit authority to deploy `T`; conditional schema-jump continuation if needed.
- Exact permitted rollback and terminal privilege release.
- Sanitized output and no provider, capture or credential changes.

The Cooperator establishes `sudo -v`, then verifies `sudo -n true` outside the Worker. The Worker uses noninteractive privilege only. A password-required result after predecessor `sudo -K` is expected lifecycle state.

Use the project SSH capability gate when the later Worker needs SSH transport. Do not reconstruct agent sockets or invent transport variables.

### Routine sequence

1. Verify local/public artifact identity and AP pin.
2. Run canonical helper `status`; record current `P`, schema, service and backup readiness.
3. Run `check --release T`; require success.
4. Obtain/issue the explicit bounded deployment authority for that exact reviewed target.
5. Run `deploy --release T --yes`.
6. On success, run `status` and complete post-deploy checks.
7. Release privilege through the supported terminal route.
8. Only then request Cooperator rendered acceptance.

The exact helper invocation shape is:

```text
# [MacBook / fish]
deploy/ubuntu/kronika-release status
deploy/ubuntu/kronika-release check --release <T>
#------------------------------------------------------
```

After the separate explicit deployment grant:

```text
# [MacBook / fish]
deploy/ubuntu/kronika-release deploy --release <T> --yes
deploy/ubuntu/kronika-release status
#------------------------------------------------------
```

`T` must be substituted with the granted full 40-hex SHA. The existing `KRONIKA_NUC_SSH_*` transport mechanism supplies private connection values without printing them.

**A check never deploys automatically.** `--yes` is confirmation syntax, not authority. Routine refresh uses the accepted Poetry 2.4.1 and CPython 3.13.14 tooling; it does not invoke `uv`.

### Schema-jump continuation

No migration is planned for this feature; packaged schema head remains `0035`. Nevertheless, the later grant must preserve the documented generic continuation.

If deploy exits exactly **13, `migration-required`**:

1. Preserve the primary exit. Verify old current release/service remain active.
2. Verify the complete target tree and release marker equal `T`.
3. Read target-tree `kronika-db status` to establish actual live revision `C` and packaged target head `H`. Do not invent a revision pair or assume `check` reported the target schema.
4. Verify the residual release-lock contents exactly as the runbook annex specifies.
5. Remove only the three named residual artifacts, then the empty lock directory, then owner record; unexpected contents or failed `rmdir` stops the continuation.
6. Under the separately granted migration authority, run target-tree `kronika-db migrate` and target-tree status as service identity, with explicit release working directory and environment-file reference.
7. Require `current_revision=head_revision=H`.
8. Complete cutover with canonical `rollback --release T --yes`, which selects the already-complete target tree.
9. Run final status and health checks.

Do not rerun deploy against the now-existing target, migrate from `/opt/kronika/current`, improvise a downgrade or restore the catalog. Any other nonzero deploy result stops for classification.

The exact owner is `docs/UBUNTU_NUC_DEPLOYMENT.md`, “Annex: Schema-jump continuation after migration-required (exit 13)”. The later grant must carry its exact cleanup and service-account commands with Worker `sudo -n` discipline.

### Post-deploy and rollback

Require:

- Canonical active/web release equals `T`.
- Service active, database at target head, backup restore-readiness ready.
- Release-local health succeeds.
- Served shell/assets correspond to the accepted release.
- Sanitized logs contain no new failures or sensitive disclosure.
- No new public listener, provider activity or capture transition.
- Terminal sudo release is observed, or explicitly classified unknown if the connection is lost.

Before activation, retain `P` and verify that its installed tree and schema compatibility support rollback. For a same-schema failure, use canonical `rollback --release P --yes` under explicit rollback authority, then verify status/readiness/health. The helper also has automatic rollback behavior; verify its actual outcome rather than assuming recovery.

After a schema migration, failed cutover requires explicit triage. No automatic database downgrade, deletion or restore is authorized.

### Cooperator rendered checklist

After `T` is public `main` and active on the NUC, the Cooperator checks:

- Timeline ready video/GIF thumbnails replace the existing icon without changing card layout.
- Personal **Records** History shows authorized private media thumbnails.
- Questions History retains its current icons, text, state and links.
- Search/Research, still images and missing/not-ready/failed previews retain kind icons without broken-image chrome.
- Thumbnail clicks retain the existing Details route.
- Filters, paging, History tabs and rapid navigation do not reveal late images.
- Identity loss/change clears private cards and previews.
- Another household member cannot see private media; approved media works; withdrawal removes the card and denies later preview access.
- Desktop and narrow layouts remain usable; keyboard focus and link names remain clear.
- Gallery, cover preference, GIF toggle and Details playback retain their accepted behavior.

Use prearranged synthetic or expressly authorized fixtures. Do not delete real cache entries, withdraw real records, change identities or access private media merely to manufacture acceptance cases. Fixture setup requiring mutation belongs in the later explicit grant. Server-side denial/cache cases remain covered by automated evidence.

Record the exact release and the Cooperator’s explicit verdict. Missing visual observations remain gaps.

## 9. Execution sequence and budgets

| Step | Session and budget |
|---|---|
| Report persistence completion | Persist this exact frozen report through a permitted route. No replanning or implementation. A renewed Worker exchange uses actual next coordinates and an exact persistence grant. |
| Plan disposition | Orchestrator accepts/rejects this design and records the selected E2 route and request-bound interpretation. |
| Implementation | **Fresh Worker required by this prompt.** One coherent candidate covering code, tests and documentation; native planning mode `not-used`. Use the canonical checkout with one active mutator. |
| Verification | Same Implementation Worker; focused commands above, exact diff and allowlist review. One regression pass per materially changed candidate; narrow diagnosis before repetition. |
| Candidate commit | Later grant may authorize one normal commit on `main`, exact allowlisted paths only, after checks; suggested message: `feat: add media thumbnails to Timeline and History`. No push in implementation authority. |
| Acceptance | Orchestrator reviews the fixed commit, matrix and evidence at E2. No separate testing Worker is needed for the selected design. Boundary changes require a fresh independent acceptance session. |
| Publication | Separate complete grant or Cooperator action pushes the accepted commit normally; verify direct public `main` equality. No force or history rewrite. |
| NUC refresh | May reuse a healthy Implementation Worker under a complete renewed deployment grant; no independent-certification claim. One routine deploy attempt plus the specifically authorized exit-13 continuation. |
| Rendered acceptance | Cooperator, after exact release refresh and post-deploy PASS. |
| Closure | Orchestrator reconciles acceptance, publication, deployment, rendered verdict, residual risks, ledger and no-active-mutation state. Worker never closes the whole. |

One concrete finding may receive one bounded correction and appropriate re-acceptance. There is no second automatic correction for the same surviving assumption and no audit-of-an-audit. Follow AP’s full fresh acceptance trigger when a correction changes runtime/security boundaries.

Recommended reasoning: High for the fresh implementation because of the monolithic shell and approved/current locator split; Medium for routine publication/deployment after the candidate and grant are fixed. These are recommendations, not measured model capabilities.

## 10. Decisions, risks, deltas and closeout

### Open decisions and defaults

No unresolved technical decision remains for the implementer.

The Orchestrator’s plan disposition must accept or reject these explicit defaults:

- Preserve the existing 36 px icon slot.
- Use `preview_location_id`, nullable and limited to the two selected list endpoints.
- Choose the lexical first eligible location; no readiness probing or alternate-location retry.
- Interpret “no N+1” as no per-record locator/detail discovery, with explicitly bounded individual image delivery.
- Use E2 plus Cooperator rendered acceptance while the audience boundary remains unchanged.

Publication, deployment, fixture mutation and rendered acceptance require their later grants. R4’s existing item-retention decision remains with the Cooperator and is not a prerequisite to this implementation.

### R1–R6 risk mapping

| Risk | Disposition and owner |
|---|---|
| R1 = A6, pre-identity `open_upload` interval | Carried informational residual; untouched. Orchestrator owns continuity; future explicit upload task owns correction. |
| R2 = R7, live X-button clearance | Carried Cooperator observation; no X/browser test in this whole. |
| R3 = R9, `app.js` monolith/test churn | Mitigate with bounded helper, scoped lifecycle changes, preserved harness expectations and Gallery regressions. Implementation Worker owns candidate evidence; modularization remains parked. |
| R4 = R10, requester-private YouTube verification item | No access or deletion here. Cooperator retains disposition decision; do not use its identifier in new artifacts or depend on it for tests. |
| R5, audience/performance | Approved/current locator separation, authorization-before-cache, one batch query, 24-card image bound and no retries. Orchestrator owns acceptance; boundary deviation triggers independent review. |
| R6, Gallery/Details freeze | New selectors limited to Timeline/History; existing renderers untouched; regression tests and Cooperator comparison. |

Residual limitations: native lazy-load proximity and image network cancellation are browser-controlled; a selected location can become unavailable; a ready alternative location is not tried; still images retain icons; JPEGs are existing current derivatives rather than approval-time byte snapshots.

### Inventory deltas against the issued hypotheses

- Rendering/API paths in the starting map were confirmed.
- The summary type resides in `application/ports/records.py`, not the domain record module.
- Media ID exists; a location locator must be added.
- Existing preview audience already supports bound-record owner/admin/household semantics; no guard change is proposed.
- Timeline and History have distinct location sources, even though they share image presentation.
- Question History is request data, not media-record data, and stays unchanged.
- Still-image media cannot use this existing derivative pipeline.
- Existing tests do not fully pin new thumbnail CSS/lifecycle or the list-to-preview audience chain.
- Per-image GETs remain necessary under the fixed endpoint; the eliminated fan-out is detail/locator discovery.
- `docs/UX_AUDIT.md` is frozen history, not the destination for current implementation claims.
- NUC and underlying Cooperator observations remain historical, not independently revalidated.

These are refinements of the prompt’s hypotheses, not repository-gate contradictions.

### AP protocol friction observed

- The task grants exact trace persistence, while actual native client mode forbids writes. AP’s existing completion-repair route applies; the report remains undelivered to the file.
- The prompt assumes a usable direct-write completion route without establishing that client permission. This affects delivery, not the completed technical plan.

No AP files, upgrade ledger or Meta defect records were changed.

### Resolved Execution Issues / Near-Misses

Bounded discovery encountered guessed nonexistent paths/globs and some truncated command output. Relevant source and test identities were subsequently inspected through targeted reads. No mandatory gate failed, no repair/mutation occurred and no truncated result is presented as executed-test evidence.

The report-write limitation remains unresolved and is the reason for `PARTIAL`.

### Pre-Existing Failure Classification

None. No product-test failure was observed or classified as pre-existing.

### Smallest next step

The Orchestrator arranges positively authorized persistence and complete readback of this exact report at the absent destination, using AP’s completion route without reopening the plan. Then disposition the plan and issue the fresh implementation grant.

Authority expires on submission of this terminal report. Implementation in this session remains prohibited.

Orchestration critique:
MEASURED: The required direct-write report delivery is unavailable under the actual client’s native Plan Mode write prohibition; the prompt’s persistence expectation therefore cannot be fulfilled in this exchange. Effect: complete planning content, missing file delivery. Smallest correction: persist this exact report through AP’s permitted completion route and verify full readback, without replanning.
LEAD: none
