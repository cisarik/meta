### Report for ORCHESTRATOR_CHAT

# Companion download notifications — implementation plan

Logical whole identity: companion-download-notifications  
Worker session ordinal: 01  
Worker exchange ordinal: 01  

## 1. Status and summary

**Status: PARTIAL — implementation planning is complete; file delivery remains blocked by native Plan Mode.**

File delivery: pending client restriction  
Intended report path: `/Users/agile/meta/projects/kronika/01/03-companion-download-notifications/01_report_00.md`

The destination is absent, and its inspected parent directories are not symlinks. No file was written; no saved-file hash is claimed.

Start commit: `e64f2b0f92458fac2590e03672e30da62275b345`  
End commit: `e64f2b0f92458fac2590e03672e30da62275b345`  
Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50`  
Changed files: none  
Phase-qualified result: not-applicable  
Logical-whole closure: not-closed  
Report justification: new-evidence  

Recommend a small **Recent downloads** block inside the existing companion history sheet. It displays the latest five own X/YouTube request states, using existing authenticated request-list APIs and the existing visible-panel poll.

The Cooperator selected during this planning exchange:

- A separate Downloads block, preserving review ordering.
- Static status rows without an unseen marker, counter, acknowledgement or persistence.
- Download-read failures hide the entire Downloads block while retaining successfully loaded review history.
- YouTube labels use the video identifier; download rows have no click action.

These selections leave no open product decision.

## 2. Current behavior evidence

### History and ownership

[service_worker.js:736](/Users/agile/Projects/kronika/extension/background/service_worker.js:736), functions `historyListRoute()` and `reviewInbox()`, supply the sidebar through existing message `review_inbox`:

| Caller | Current read | Membership |
|---|---|---|
| Administrator with `media.workflow.read` | `GET /api/companion/review-inbox` | Global analyzed, non-movie pool |
| Ordinary identity with `x.request` | `GET /api/companion/own-history` | Own cataloged X Saves, including pending analysis |
| Neither capability | No history | Hidden and disabled |

`reviewInbox()` aggregates sequential 100-row pages, detects cursor cycles, prefers analyzed replacements for duplicate media IDs, and fails the complete review list without partial titles.

Server enforcement resides in [companion_review_api.py:139](/Users/agile/Projects/kronika/src/kronika/adapters/api/companion_review_api.py:139), `list_review_inbox()`, `list_own_history()` and their identity guards. `ListCompanionReviewInbox.execute()` selects the appropriate repository query.

[companion_review_repository.py:651](/Users/agile/Projects/kronika/src/kronika/infrastructure/persistence/companion_review_repository.py:651), `_own_history_rows()` and `_owned_cataloged_x_predicates()`, establish that:

- Own-history membership requires an actor-owned X claim and a cataloged asset linked to catalog media.
- Movie workflows are excluded.
- Without a qualifying successful generic analysis, an eligible medium is pending.
- After analysis, its analyzed projection replaces the pending projection.
- Acquisition state and analysis state are separate. There is no one-to-one mapping from request phase to a history row.

The sidebar’s `partitionHistoryItems()`, `renderReviewCollections()` and `onReviewListClick()` preserve the existing compact/All behavior and hosted Details clicks. Analyzed clicks also request opened; pending clicks do not.

### X request states

[x_acquisition.py:87](/Users/agile/Projects/kronika/src/kronika/domain/x_acquisition.py:87), `XAcquisitionState` and `derive_x_requester_phase()`, define:

| Durable state | Requester phase | Acquisition meaning |
|---|---|---|
| `submitted`, `queued` | `queued` | Active |
| `extracting`, `acquiring`, `handing_off` | `processing` | Active |
| `completed` | `completed` | Successful terminal request |
| `completed_partial` | `completed` | Terminal with partial success |
| `duplicate_resolved` | `completed` | Terminal reuse/duplicate disposition |
| `failed` | `failed` | Failed terminal request |
| `catalog_removed` | `unavailable` | Later unavailable disposition |

`completed_private` is declared in the X vocabulary but is not emitted by this derivation. X `completed` does **not** establish household publication.

[x_request_api.py:225](/Users/agile/Projects/kronika/src/kronika/adapters/api/x_request_api.py:225), `list_x_requests()` and `get_x_request()`, require `x.request` and call `list_owned()`/`get_owned()` with the verified identity’s login key. Both administrators and ordinary identities use this ownership filter.

The responses contain request ID, raw state, requester phase, source URLs, optional claim title, timestamps and asset projections. Foreign/missing detail is 404. The requester snapshot redacts inaccessible linked media IDs.

Current own-history may contain successful assets from a partially completed or still active request; a failed request without cataloged assets is absent. Duplicate and removed requests cannot be represented reliably by treating catalog-history membership as download completion.

### YouTube request states

[youtube_acquisition.py:63](/Users/agile/Projects/kronika/src/kronika/domain/youtube_acquisition.py:63), `YouTubeAcquisitionState` and `derive_requester_phase()`, define:

| Underlying state | Requester phase |
|---|---|
| `claimed` | `queued` |
| `inspecting`, `downloaded`, `handoff`, `handed_off` | `processing` |
| `download_pending`, `downloading` | `downloading` |
| `cataloged`, `duplicate_resolved` | `completed` or `completed_private`, subject to readable linked media |
| `failed` | `failed` |
| `catalog_removed`, or unavailable linked result | `unavailable` |

`YouTubeRequestService._request_snapshot()` additionally suppresses a linked result belonging to another bound owner.

[youtube_request_api.py:180](/Users/agile/Projects/kronika/src/kronika/adapters/api/youtube_request_api.py:180), `list_requests()` and `get_request()`, require `youtube.request` and delegate to requester-owned service reads. List limits are 1–50.

The projection contains request ID, phase, source URLs, optional media ID, sanitized failure categories/codes, retry parent and timestamps. **It contains no video title.**

YouTube is absent from companion own-history because that query is explicitly X-only; administrator inbox is an analysis pool rather than request history.

`youtube_adapter.js`, functions `save()`, `applySnapshot()` and `poll()`, polls through the service worker every four seconds, with a 30-minute budget. This scheduler lives in the content-script document and ends when its tab/document closes. The service worker has no independent YouTube recovery scheduler. X polling is likewise page-driven, with bounded persisted inflight recovery.

### Badge and polling

`refreshReviewInboxBadge()` uses the active review source with `limit=1`, deriving the toolbar badge exclusively from server `unopened_count`. `badgeTextForUnopenedCount()` formats positive values as `1`–`99` or `99+`.

Badge refresh occurs through:

- The one-minute `kronika.review-inbox` alarm.
- Configuration/connect.
- Successful visible history refresh, including refresh after opened.
- Reset and failure paths, which clear it as appropriate.

[sidebar.js:543](/Users/agile/Projects/kronika/extension/ui/sidebar.js:543), `startInboxPoll()`, refreshes immediately and every 15 seconds while visible; visibility changes stop/restart polling.

The manifest permissions are exactly `alarms`, `sidePanel`, `storage`. No notification permission exists.

### Existing test pins

[companion_review_extension.test.js](/Users/agile/Projects/kronika/tests/companion_review_extension.test.js) pins:

- Permissions and protocol: tests beginning at lines 733 and 766.
- Badge formatting, routing, alarm and clearing: lines 867–1012.
- Complete pagination and fail-closed behavior: lines 1015–1185.
- History DOM, safe rendering, closed-by-default behavior, compact ordering and clicks: lines 1241–1910.

`x_companion_extension.test.js` pins exact permissions, fixed API paths, X terminal outcomes, interactive YouTube submission and composer isolation. `companion_web_bridge.test.js` pins origin/source checks, hosted Details, Upload and Attach. Settings and YouTube cockpit suites pin adjacent capability and request behavior.

Python evidence includes:

- `test_own_history_opened_alice_bob_admin_isolation`.
- `test_own_history_opened_isolation_does_not_use_global_unopened_count`.
- YouTube request field allowlists and uniform missing/foreign detail handling.
- Real requester-private YouTube list/detail isolation.
- X requester lifecycle ownership and idempotent reuse.

`browser_companion_evidence.test.js` is an opt-in synthetic Chrome/CDP Origin/Attach test. It does not establish download-history rendering or Brave acceptance.

## 3. Options and recommendation

| Option | Assessment |
|---|---|
| Merge request rows into existing review ordering | Requires heterogeneous row identities, click rules and a changed ordering contract. Rejected by the Cooperator. |
| Separate Downloads block inside existing history | Reuses existing requests and polling, accommodates failures without media IDs, and preserves review ordering. **Selected.** |
| Transient completion highlight | Requires transition memory; without persistence it misses closed-panel completions, and with persistence it adds acknowledgement and identity lifecycle work. Rejected for this slice. |
| Extend server own-history to YouTube | Changes its X-only contract, still does not naturally represent failed requests, and does not solve administrator own-download coexistence by itself. Unnecessary. |
| Decorate existing catalog rows only | Cannot cover failed/uncataloged X requests or YouTube requests. Insufficient. |
| Forward existing content-script polling outcomes | Depends on open source tabs and introduces a second observation channel. Insufficient. |

The selected design displays durable request outcomes rather than creating an event-notification system.

## 4. Recommended design

### Visible behavior

Add `#download-history` as the first child of `#review-history`, containing:

- A small **Recent downloads** heading.
- `#download-history-list`, an ordinary list labelled **Your latest five download requests**.
- At most five read-only rows across X and YouTube.

Change the sheet’s CSS-generated caption from “Recently saved & analyzed” to **Companion history**. Keep the existing review lists and All control in their current relative order beneath Downloads.

The history toggle is enabled when either review rows or download rows exist. It still starts closed on each panel load and preserves the user’s current expanded/collapsed choice across refreshes. An empty/failed Downloads block occupies no height.

Download rows:

- Have no button, link, retry, Details or opened action.
- Use source label, bounded request label and explicit status text.
- Use existing dark surfaces and theme tokens; status remains understandable without color.
- Have no animation, unseen styling, counter or `aria-live`.
- Stay within the existing bounded, scrollable sheet.

Keep the visible **All** text; change its accessible name to **Show full review history**, because it controls the existing review collection only.

### Read window and labels

For each available request capability, read the first page with `limit=5`:

- `GET /api/x/requests?limit=5`
- `GET /api/youtube/requests?limit=5`

Do not follow these cursors: this block explicitly represents a recent window, not complete request history. Both repositories order by creation timestamp and request ID descending.

Deduplicate by `(source, request_id)`, keeping the first occurrence. Merge by `created_at_ms` descending, then source ascending and request ID descending; retain five rows.

Use X’s existing claim title after `canonicalizeCompanionAliasTitle()` normalization, with fallback **X post <post ID>**. Use **YouTube video <video ID>**, derived through the existing canonical URL validator. Do not fetch media details for labels.

This includes own requests initiated through other existing Kronika surfaces: the APIs do not distinguish companion initiation.

### State mapping

| Source evidence | Display |
|---|---|
| X active states; YouTube `queued`, `processing`, `downloading` | Saving… |
| X `completed`; YouTube `completed` | Saved |
| YouTube `completed_private` | Saved privately |
| X `completed_partial` | Partly saved |
| X `duplicate_resolved` | Already saved |
| X/YouTube failed terminal state | Download failed |
| X `catalog_removed`; YouTube `unavailable` | Unavailable |

Use raw durable X state, not X `phase` alone, to preserve partial/duplicate distinctions. For YouTube use the existing requester phase; that API does not expose duplicate disposition. **Saved** therefore reports the terminal Save result and never asserts that new bytes were transferred.

Analysis, review opening, publication and catalog presence alone never produce a download-completion claim. `Unavailable` is neutral, not a success signal.

Unknown states, malformed rows or unreadable results produce no download row.

### Observation, deduplication and lifecycle

There is no event “fire” operation. The current status appears on first successful observation and changes in place on subsequent snapshots.

- Repeated polls do not create additional rows or announcements.
- X retry reuses its request ID: the same row can return to Saving and later reach a terminal state.
- YouTube retry creates a new request ID: it remains a distinct request.
- Reusing a request or resolving duplicates does not manufacture a new download event.
- Publication changes may change YouTube’s private label without creating attention.
- No seen state, acknowledgement, expiry timer or new storage key exists.
- Rows leave the block when displaced from the latest-five window.
- Panel/extension/browser reload and reconnection read current server state again.
- Closing the source tab does not prevent later observation through the sidebar.
- With the sidebar closed, this feature produces no alert. The existing toolbar badge remains review-only.

### Privacy and authorization

| Subject | X Downloads | YouTube Downloads |
|---|---|---|
| Ordinary owner | Own request projection only | Own request projection only |
| Administrator viewing own Downloads | Own request projection only | Own request projection only |
| Another household member | No foreign request fields | No foreign request fields |

The administrator’s existing global analyzed inbox remains separately authorized and unchanged. Its existing foreign analyzed titles must never be converted into another owner’s download activity.

The new Downloads projection contains no foreign title, URL, thumbnail, request ID, state or failure detail. Raw source URLs, asset arrays, media filenames, provider data and failure details are not forwarded to the sidebar.

Use capability `x.request` for X and `youtube.request` for YouTube. Skip absent capabilities without making that read. Existing history eligibility still follows `media.workflow.read`, then `x.request`; current ordinary and administrator roles have both request capabilities.

### Failure and stale-response behavior

- Review-list failure, including later-page failure or cursor cycle: preserve existing whole-history hide, collapse/disable and badge clearing.
- Failure of either capability-enabled download read: return no Downloads rows from either source; retain the complete review result and its server badge count.
- Download 403, 404, 503, network failure, malformed response or unknown vocabulary: same hidden Downloads outcome; never turn transport failure into “Unavailable”.
- Missing configured origin or failed identity: existing whole-history failure.
- Missing additive Downloads data from a skewed extension component: hide Downloads; preserve valid review data.
- Reconnect/reset/runtime invalidation clears displayed Downloads immediately.
- Serialize sidebar refreshes within a connection generation; skip overlapping timer ticks and discard responses from older generations.
- Capture configured origin and an in-memory configuration revision for aggregation. Fixed-origin reads and a final identity/capability check must match the initial context; otherwise discard the whole result. Do not persist identity or download snapshots.

The Cooperator explicitly selected this independent Downloads failure behavior to avoid hiding functioning review history when acquisition is disabled.

## 5. Exact changed-path allowlist

| Path | Reason |
|---|---|
| `extension/background/service_worker.js` | Aggregate bounded own-request reads, guard the sidebar caller and discard stale contexts. |
| `extension/shared/messages.js` | Shared download constants, normalization and bounded response sanitization. |
| `extension/ui/sidebar.js` | Render Downloads, handle combined emptiness/failure and prevent stale refreshes. |
| `extension/ui/sidebar.html` | Add the read-only block and refine All’s accessible name. |
| `extension/ui/sidebar.css` | Style the block and update the sheet caption. |
| `tests/companion_review_extension.test.js` | Add behavioral regressions and update affected harness/DOM assertions. |
| `tests/contract/test_x_request_api.py` | Pin list/detail requester delegation for ordinary and administrator callers. |
| `tests/contract/test_youtube_request_api.py` | Pin equivalent requester delegation and safe list/detail fields. |
| `docs/X_COMPANION.md` | Document behavior, labels, recent-window limits and failure recovery. |
| `SPEC.md` | Distinguish review-row requirements from the new read-only request block. |
| `SECURITY.md` | Document the own-request projection, sender boundary and absence of new stored data. |
| `DEVELOPMENT.md` | Add focused validation and the later acceptance checklist. |
| `docs/adr/0089-companion-own-download-status-history.md` | Record the additive history/response contract and the selected product decisions. |
| `docs/adr/README.md` | Index ADR-0089 and annotate only its narrow supplementation of ADR-0076. |

No backend implementation, manifest, migration, dependency, accepted ADR body, Gallery/Details or web-shell implementation change is needed.

## 6. Protocol/API delta

**HTTP route/schema delta: none. New message type: none.**

Retain request:

`{ v: "kronika.companion.v1", type: "review_inbox", payload: {} }`

Extend its successful response with:

```text
downloads:
  ok: boolean
  items: DownloadHistoryItem[]  // maximum five

DownloadHistoryItem:
  source: "x" | "youtube"
  request_id: UUID
  label: nonempty normalized text, maximum 240 code points
  status: "saving" | "saved" | "saved_private" | "partial"
          | "already_saved" | "failed" | "unavailable"
  created_at_ms: nonnegative safe integer
```

Download failure is exactly `{ok: false, items: []}`. A successful empty window is `{ok: true, items: []}`. Unknown properties and raw API fields are discarded.

Restrict handling of `review_inbox` to a sender whose:

- `sender.id` equals `chrome.runtime.id`.
- `sender.url` equals `chrome.runtime.getURL("ui/sidebar.html")`.
- `sender.origin` equals that extension URL’s origin.

Missing or mismatched sender metadata returns an empty `invalid_sender` failure before network access, without clearing an existing badge. Pass `sender` through `handle()` for this check. Other message branches retain their behavior.

Reads use fixed existing `pathFor()` templates, configured/granted tailnet origin and existing request headers. Caller-supplied URLs, paths, IDs or cursors do not control these reads. Validate response request UUIDs, timestamps, source identities and known state vocabulary. No new detail-path parameters are introduced.

The 15-second sidebar poll carries the additive data. The one-minute badge alarm continues to read only the original review source with `limit=1`.

## 7. Test plan

**No tests, builds, AP commands, Node or Python were executed during planning. Evidence tier remains E0.**

### New causal regression

Add a behavioral test in `companion_review_extension.test.js`:

**“history shows own terminal X and YouTube request states without source tabs or catalog history.”**

Run the actual service-worker message listener with a valid sidebar sender, synthetic identity, empty review history, completed X and private-completed YouTube list responses. Feed its result into the sidebar harness and assert:

- Both source states render.
- The history toggle is enabled despite empty review items.
- The badge remains empty.
- No content-script poll, media-detail fetch or mutation occurs.

The baseline lacks this response and renderer, so this regression must fail before implementation. Existing tests prove X overlays and review history separately; they do not prove this tab-independent combined path.

### Additional behavioral assertions

Cover:

- Every mapping above, including partial success, duplicate reuse and neutral unavailable.
- Unknown/malformed state rejection; safe text rendering and label bounds.
- Latest-five merge, deterministic ties and `(source, request_id)` deduplication.
- Repeated snapshots, X same-ID retry and YouTube new-ID retry without event replay.
- Ordinary own-history and administrator global inbox each coexisting with own Downloads.
- Capability omissions causing no prohibited request.
- Spoofed/missing sender metadata causing no network access.
- Caller URL/cursor payloads never influencing request construction.
- One download source failing after the other succeeds: no partial Downloads; review and badge preserved.
- Review pagination/cursor failure continuing to erase all history and clear the badge.
- Reset/reconnect and late responses never restoring previous-context rows.
- No overlapping visible-panel refreshes; hidden-panel polling remains stopped.
- Download-only, review-only, empty and failed states.
- Read-only rows issuing no opened, retry or Details action.
- Alarm refresh making no download-list calls.
- Exact manifest permission assertions remaining unchanged.

Update the existing “last fetch is review list” assertion to identify the review call by route; retain its fixed-path security assertion. Update the sidebar harness for new optional DOM nodes and All’s accessible name. Keep the original ordering, iframe-survival and badge assertions.

Add API contract cases for ordinary owner, another ordinary identity and administrator identity. Verify the exact actor passed to owned list/detail services, identical foreign/missing detail denial, no-store responses and safe fields. These supplement existing persistence/lifecycle isolation; they are boundary pins, not claimed causal failures on baseline.

### Focused implementation commands

```fish
# [MacBook / fish]
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline e64f2b0f92458fac2590e03672e30da62275b345
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline e64f2b0f92458fac2590e03672e30da62275b345 --operation runtime-info
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline e64f2b0f92458fac2590e03672e30da62275b345 --operation test-focus -- tests/contract/test_x_request_api.py tests/contract/test_youtube_request_api.py tests/contract/test_companion_review_api.py -q -p no:cacheprovider
node --test tests/companion_review_extension.test.js tests/x_companion_extension.test.js
#------------------------------------------------------
```

### Broader affected selection

Run once after focused checks pass, to cover the newly consumed ownership/state boundaries and adjacent companion surfaces:

```fish
# [MacBook / fish]
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline e64f2b0f92458fac2590e03672e30da62275b345 --operation test-focus -- tests/contract/test_tailscale_ingress_security.py tests/contract/test_requester_private_youtube_details.py tests/unit/application/test_x_acquisition_lifecycle.py tests/integration/test_youtube_acquisition_lifecycle.py tests/unit/infrastructure/persistence/test_companion_review_repository.py tests/unit/domain/test_x_acquisition_domain.py tests/unit/domain/test_youtube_acquisition.py -q -p no:cacheprovider
node --test tests/companion_web_bridge.test.js tests/companion_settings_automatic_analysis.test.js tests/youtube_request_cockpit.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js
#------------------------------------------------------
```

Use synthetic fixtures only. No full suite, browser execution, real acquisition or provider call is selected. Browser geometry and shipping-Brave behavior remain later acceptance evidence.

## 8. Documentation plan

- **SPEC.md:** Preserve X-only server own-history and review-only badge semantics. Add the separate bounded Downloads block and its failure isolation. Narrow “Every history row MUST post hosted `open_details`” to existing **review rows**; its current unrestricted wording would forbid the selected inert request rows. Clarify that complete review pagination remains fail-closed.
- **ADR-0089:** Record block membership, administrator own-request coexistence, status-only behavior, additive response, sender guard and failure isolation. Supplement ADR-0076 without rewriting historical bodies.
- **docs/X_COMPANION.md:** Explain labels, latest-five creation ordering, no closed-panel alert, tab-independent refresh and disappearance on source failure. Correct its stale “starts collapsed only when empty” statement to match SPEC, implementation and the existing closed-by-default test.
- **SECURITY.md:** Describe ownership-filtered request reads, sanitized native-only projection and no new download persistence. Keep six mutation routes, permissions, CORS and residuals unchanged.
- **DEVELOPMENT.md:** Include the selected checks and later rendered-acceptance scenarios.
- **docs/UX_AUDIT.md:** Leave frozen as historical evidence.

README, PRODUCT, ROADMAP and SERVER require no amendment for a new backend foundation or broader feature claim.

## 9. Implementation sequence

For one separately authorized fresh Implementation Worker:

1. Verify clean `main`, exact baseline, remote identity and matching AP pin. Confirm the renewed exact allowlist and absent trace destination.
2. Add the causal Node regression and record its expected baseline failure.
3. Implement shared normalization and the guarded service-worker aggregation. Retain existing review pagination, badge and awaiting-analysis behavior.
4. Add the sidebar block and connection-generation handling. New DOM nodes must remain optional to core shell initialization so skewed markup hides Downloads without disabling existing functions.
5. Add ownership/failure regressions and the two API contract extensions.
6. Update the six documentation paths, including ADR/index, to the final implemented behavior.
7. Run focused checks, then the selected broader affected checks. Inspect documentation links, exact diff, allowlist and `git diff --check`.
8. Under the later grant, stage explicit allowed paths and create one local commit on `main`, suggested subject: `Surface own download status in companion history`.
9. Do not push or deploy. Direct-write and fully read back the implementation report at `/Users/agile/meta/projects/kronika/01/03-companion-download-notifications/02_report_00.md`, only if the later prompt explicitly grants that path and it is absent.

The future prompt is prepared by the Orchestrator. This plan grants no execution or Git writes.

## 10. Validation and rollback

Planning verification completed:

- Repository origin is `cisarik/kronika`.
- Clean `main...origin/main`; exact expected HEAD.
- AP gitlink and submodule HEAD match the governing pin.
- Received and prepared prompt compare identically.
- Final Git diff is empty; `git diff --check` is clean.
- Report destination remains absent.

Public-main equality and prior AP check results remain Orchestrator observations, not independently repeated findings.

Implementation acceptance requires all selected checks passing, causal-regression evidence, exact allowed paths, unchanged permissions/mutation count, and a single local commit. Unit/contract evidence does not establish rendered acceptance.

Rollback, under separate Git authority, is a revert of that single implementation commit and reload of the unpacked extension. There is no schema or download-data rollback. Existing server requests and media remain intact; the original review history resumes without Downloads.

## 11. Risks N1–N5 and additional risks

| Risk | Treatment |
|---|---|
| **N1 — Notification fatigue** | Static current-state rows; no event replay, live announcements, unseen state or counter. |
| **N2 — Badge collision** | Download outcomes never contribute to `unopened_count`; alarm behavior remains review-only. |
| **N3 — Protocol/polling change** | One existing message and poll; at most two additional bounded list reads. Single-flight refresh and stale-context rejection. Slow reads retain the existing fetch timeout and can delay a refresh. |
| **N4 — Private download visibility** | Owned request endpoints for both roles, exact sidebar sender guard, no foreign inbox-to-download conversion, no new persisted snapshots. |
| **N5 — Companion pins and permissions** | Preserve manifest and security assertions; update only intentional response/DOM/harness expectations. |
| **N6 — Projection limits** | YouTube has no title or duplicate disposition; X completion phase does not imply sharing. Use honest labels and raw X state. |
| **N7 — Bounded visibility** | Only latest five created requests appear; older requests and retries outside that window can remain absent. Label/document this as recent activity, not complete download history. |
| **N8 — Rendered evidence** | Additional rows may affect sheet scrolling. Brave geometry and usability remain untested until later current-NUC acceptance. |

## 12. Open Cooperator decisions

**None.** The four material UI/read-path choices were answered during this exchange.

Implementation approval remains an Orchestrator disposition of this report, followed by a separate complete fresh-worker grant. Client plan approval alone does not authorize implementation.

## 13. What this plan does not do

- No new acquisition pipeline, provider contact or external X/YouTube download.
- No push/OS notification, unseen badge, combined counter or general notification center.
- No backend route, schema, permission, credential or account change.
- No download retry, publication or opened mutation from the new rows.
- No Gallery/Details, upload, onboarding, localization or general accessibility redesign.
- No web-shell modularization, private-media inspection or host/NUC operation.
- No complete request archive or guarantee of noticing a completion while the sidebar is closed.

## 14. Later phases and closeout

After implementation review, separate authority is needed for:

1. Publication of the accepted commit to public GitHub `main`.
2. Routine NUC refresh through `deploy/ubuntu/kronika-release`, with required status and exact-release check before a separately authorized deployment.
3. Reloading the unpacked companion from the matching published revision, refreshing affected source tabs and reopening the panel.
4. Cooperator rendered acceptance on the refreshed NUC: ordinary/admin coexistence, terminal copy, closed-source-tab observation, failure isolation, scrolling, unchanged badge and surviving hosted Attach.

NUC refresh alone does not reload the browser extension. Real acquisition, private data or additional fixture mutations require their own authority.

Resolved Execution Issues / Near-Misses: Initial discovery queries included nonexistent guessed paths; repository path discovery resolved them. No required source remained missing. Native file-write restriction was identified early and the prompt’s plan-output fallback retained.

Pre-Existing Failure Classification: No runtime failures evaluated. One stale history-expansion description was identified and included in the documentation correction.

Orchestration critique:  
MEASURED: none  
LEAD: none  

**Proposed next step:** The Orchestrator reviews this complete report, arranges its permitted persistence, and—if accepted—issues the separate fresh Implementation Worker prompt.

This terminal planning report expires the current grant. The logical whole remains open.
