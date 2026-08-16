### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-x-meme-browser-companion-mvp
Worker session ordinal: 01
Worker exchange ordinal: 01

## 1. Terminal status and authority expiry

**PASS.** One architecture is selected; every material decision is resolved to an
exact owner/path/interface or to one named, smallest separately authorized spike.
No repository file was edited, created, deleted, or formatted; no Git write
operation, dependency change, provider contact, X access, browser-profile
access, NUC access, or production mutation was performed. The only writes were
to the host plan file designated by the planning harness, outside the
repository. Planning authority granted by prompt FN-X-MEME-COMPANION-PLAN-01 is
expired by this terminal report. Plan approval is a decision only and does not
grant implementation authority.

## 2. Exact baseline and evidence ledger

Baseline gate (all read-only; `git rev-parse`, `git status`, `git ls-tree`,
`git submodule status`, `git ls-remote`; no fetch):

| State | Result | Classification |
| --- | --- | --- |
| Local consumer checkout | `/home/agile/Projects/framenest`, branch `main`, HEAD `3cf22b8aaff61ed71093207d5b24aae622f394ac`, status clean (no modified/untracked output), origin `https://github.com/cisarik/framenest.git` | directly verified repository fact |
| Local AP checkout | `.ap` HEAD `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`, matches consumer gitlink `160000 commit 9c5cc44f…`, clean | directly verified repository fact |
| Consumer public ref | `git ls-remote …/framenest.git refs/heads/main` → `3cf22b8aaff61ed71093207d5b24aae622f394ac` | directly verified public fact |
| AP public ref | `git ls-remote …/ap.git refs/heads/main` → `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | directly verified public fact |
| Deployed/production state | **not re-probed under current authority**; issuance-time anchor (release artifact `5abb2ad…`, schema `0028`, healthy production evidence) preserved as historical context only | historical context |

All five gate states are non-contradictory. No active mutation owned by this
Worker exists.

Directly verified repository sources (read in full or at the cited symbol):
`.ap/AP.md` (RF map), `.ap/AP_WORKER.md`, `docs/WORKER_EXECUTION_CONTRACT.md`,
`src/framenest/adapters/api/tailscale_ingress.py` (full),
`src/framenest/domain/identity_access.py` (full),
`src/framenest/adapters/api/x_request_api.py` (full),
`src/framenest/adapters/api/x_admin_api.py` (header/route surface),
`src/framenest/application/x_acquisition.py` (full, 1342 lines),
`src/framenest/infrastructure/x/downloader.py` (full),
`src/framenest/domain/x_acquisition.py` (URL/state/media-type sections),
`src/framenest/adapters/api/media_catalog_api.py` (full),
`src/framenest/application/media_catalog.py` (full),
`src/framenest/adapters/api/content_audience_api.py` (full),
`src/framenest/application/content_publication.py` (full),
`src/framenest/adapters/api/media_content_api.py` (full),
`src/framenest/application/media_content.py` (full),
`src/framenest/application/ports/media_content.py` (full),
`src/framenest/adapters/api/gallery_preview_api.py` (audience gate confirmed),
`src/framenest/domain/media_classification.py` (full),
`src/framenest/domain/media.py` (`MediaKind`),
`src/framenest/configuration.py` (settings keys/validators),
`src/framenest/adapters/api/application.py` (wiring points, grep-targeted),
`src/framenest/infrastructure/persistence/x_acquisition_claim_repository.py`
(`has_live_requester_media_access`, `private_successful_quota`),
`src/framenest/infrastructure/persistence/alembic_environment/versions/0028_x_requester_acquisition.py`
(header, columns, indexes), ADR-0048/0049/0055 (headers and decision sections),
`docs/AP_UPGRADE_OBSERVATIONS.md` (stale entry header only, not edited),
`src/framenest/adapters/api/web/app.js:307` (web UI mutation header),
test tree listing (`tests/contract/test_x_request_api.py`,
`test_x_route_policy.py`, `test_tailscale_ingress_security.py`,
`test_media_catalog_api.py`, `test_content_audience_policy.py`, etc.).

Directly verified public/primary sources:
[Chrome cross-origin network requests](https://developer.chrome.com/docs/extensions/develop/concepts/network-requests),
[Chrome content scripts](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts),
[Chrome sidePanel API](https://developer.chrome.com/docs/extensions/reference/api/sidePanel),
[Chrome messaging](https://developer.chrome.com/docs/extensions/develop/concepts/messaging),
[Tailscale Serve (identity headers)](https://tailscale.com/docs/features/tailscale-serve),
[Chromium: content-script fetch changes](https://www.chromium.org/Home/chromium-security/extension-content-script-fetches/).

Limitations (labeled): the Brave support article URL returned HTTP 403 to the
fetch tool — Brave compatibility claims below are labeled inference/spike-gated,
not directly verified. Brave `chrome.sidePanel` behavior has historical public
bug reports (brave-browser issues #31328, #32132, 2023); current behavior is an
unresolved question isolated behind the Section 11 spike. The exact `Origin`
header value emitted by an extension-origin fetch is established Chromium
behavior (`chrome-extension://<id>`, forbidden header name, not settable by web
pages) but is labeled inference here and made a deterministic gate in Slice A
of the verification ladder.

## 3. Current capability and ownership map

- **Identity/capabilities** — owner `src/framenest/domain/identity_access.py`.
  Roles `admin`/`user`. Ordinary capabilities: `gallery.read`,
  `media.original.read`, `media.download`, `upload.submit`, `youtube.request`,
  `x.request`. Admin adds `x.acquire`, `media.content.publish`,
  `media.workflow.read`, `media.catalog.remove`, and others. Identity mapping
  is config-backed (`identity_map`), max 64 entries.
- **Ingress/CSRF** — owner `src/framenest/adapters/api/tailscale_ingress.py`.
  Trusted only in `tailscale_uds` mode on a permission-restricted UDS written
  solely by root-owned `tailscaled`; Serve strips and reinjects identity
  headers (confirmed by Tailscale doc). Fail-closed route policy table;
  unclassified remote route → 404. Unsafe methods require `Origin` exactly equal
  to configured `external_origin` **and** `X-FrameNest-Request: 1`
  (lines 628–647), else `MUTATION_ORIGIN_FORBIDDEN` /
  `MUTATION_HEADER_REQUIRED`. The packaged web UI sets that header
  (`web/app.js:307`). Privileged mutations are audit-recorded.
- **X requester lifecycle** — owners `adapters/api/x_request_api.py`,
  `application/x_acquisition.py`, `domain/x_acquisition.py`,
  `infrastructure/x/downloader.py`, `infrastructure/x/staging.py`,
  `infrastructure/persistence/x_acquisition_claim_repository.py`, migration
  `0028`. Endpoints: `POST/GET /api/x/requests`, `GET/POST retry
  /api/x/requests/{claim_id}` (capability `x.request`), admin review `GET
  /api/admin/x/requests/{claim_id}` (`x.acquire`). Submission validates
  x.com/twitter.com status URLs with numeric IDs (`accept_x_post_url`),
  preserves `created_by_login_key`, returns `new` / `active_reuse` / `reuse`,
  enforces admission limits (1 active/requester, 8 global, 6 submits/h, 10
  failed/24h, free-space gate), ≤4 assets, ≤300 s video, ≤1 GiB/asset, per-asset
  lifecycle with partial success and bounded retry. Cataloged assets become
  media with `AcquisitionSource.X_MANUAL_CLAIM`, default category `meme`
  (`default_x_category`; `image` would default to `general`), `x_author`
  attribution (`x_classification_for_upload`). Automatic AI analysis fails
  closed for X-linked uploads.
- **Static-photo gap** — pinned `yt-dlp==2026.7.4` TwitterIE filters photo
  media; `_media_type_from_raw` returns `None` for still-image markers, so
  photo-only posts terminate with `X_NO_SUPPORTED_MEDIA`. `XMediaType.IMAGE`
  exists for fake-fixture use only. Directly verified; matches anchor 8.
- **Catalog listing** — owner `application/media_catalog.py`
  (`ListMediaCatalog`, hardcoded `published_only=True`), API
  `adapters/api/media_catalog_api.py` (`GET /api/media`, capability
  `gallery.read`; search over title, AND tag keys, category, acquisition
  source, creator filters; limit ≤100, offset). **No requester-private listing
  exists.** `GET /api/media/{media_id}` is audience-gated with 404 semantics.
- **Audience** — owner `application/content_publication.py`
  (`ContentAudiencePolicy.may_read`): admin (`media.workflow.read`) OR published
  OR requester's own live YouTube/X media
  (`x_acquisition_claim_repository.has_live_requester_media_access`, join
  `x_assets.state IN success` × `x_post_claims.created_by_login_key`). Applied
  to item, content, download, and gallery-preview routes
  (`content_audience_allows`; gallery-preview gate confirmed at
  `gallery_preview_api.py:87`).
- **Content delivery** — owners `adapters/api/media_content_api.py`,
  `application/media_content.py`, `application/ports/media_content.py`.
  `SUPPORTED_MEDIA_CONTENT`: video/mp4, image/gif, image/jpeg, image/png.
  Availability + supported-pair enforced, byte ranges, `nosniff`, sanitized
  ASCII download filenames, `Cache-Control: private, no-store`.
- **Wiring** — `adapters/api/application.py`: builds `ContentAudiencePolicy`
  with `x_requester_private_access=owned_x_claim_repository`, installs
  `TailscaleIngressMiddleware` with `external_origin` only in `tailscale_uds`
  mode, includes `create_x_request_api_router`.
- **Config** — `configuration.py`: `external_origin` (exact https origin
  validator), `identity_map`, `x_request_max_*` admission knobs.

## 4. Selected extension architecture

**Selected: one Manifest V3 Chromium extension, zero runtime dependencies, no
build step, three contexts, one versioned X adapter seam.**

- `extension/manifest.json` — MV3; pinned `key` for a stable extension ID
  (Section 5); static content script on `https://x.com/*` and
  `https://twitter.com/*` only.
- `extension/background/service_worker.js` — the **only** FrameNest network
  client. Owns the versioned API client (`framenest.companion.v1`), request
  submission/polling, picker queries, and bounded byte fetch for attachment.
  Extension-origin `fetch` with host permission is not CORS-constrained (Chrome
  network-requests doc); content scripts remain CORS-constrained (Chromium
  content-script fetch doc), which is why content scripts never fetch
  cross-origin themselves.
- `extension/content/x_adapter.js` + `extension/content/x_adapter_contract_v1.js`
  — data-driven descriptor module (selector/signal table with explicit
  `adapterVersion`) executed against a frozen DOM contract. Injects the Save
  affordance on the focused post and the Attach affordance on detected
  composers; performs the attachment; fails closed with a "stale adapter" state
  when required signals are absent. Fixture-driven: synthetic X DOM fixtures
  under `tests/support/x_fixtures/` drive repository tests.
- `extension/ui/picker.html|picker.js|picker.css` — picker UI, used as **side
  panel** (primary) and as action **popup** (degraded fallback when
  `chrome.sidePanel` is unavailable — same document, feature-detected). Opened
  only by user gesture (`chrome.sidePanel.open`, Chrome 116+, allowed from a
  content-script user interaction per the sidePanel doc).
- `extension/shared/messages.js` — the only message schema; every message
  carries `v: "framenest.companion.v1"`, a `type` enum, and a bounded payload;
  unknown versions/types are dropped. Content-script messages are treated as
  attacker-craftable (Chrome messaging security guidance) and carry opaque
  handles, never URLs to fetch (the SW constructs URLs from allowlisted path
  templates and validated IDs — the exact anti-pattern the Chrome doc warns
  against is avoided by never accepting a URL from a content script).

Rejected alternatives:

- **Popup-primary picker** — popup is destroyed on focus loss; search → preview
  → select → attach is a multi-step flow that cannot survive focus transitions.
  Retained only as degraded fallback for the side-panel-capability risk.
- **In-page overlay picker (content-script-rendered UI)** — rejected: UI would
  live inside the untrusted X DOM where page scripts can observe/tamper with it,
  CSS isolation is fragile against X's own SPA rerenders, and media previews
  would be injected into page-managed layout. Violates least-trust placement.
- **Offscreen document for media handling** — no DOM parsing or long-lived
  media decoding need exists in the SW design; adds a process and permissions
  surface without payoff.
- **Native Messaging host** — last-resort only; excluded from MVP (install
  surface, NUC/packaging coupling, no demonstrated need).

Lifecycle: MV3 service worker is event-driven; long work (claim polling) uses
bounded alarm-less `setTimeout` chains re-armed only while a tracked submission
is active, and terminates idle. All extension state lives in
`chrome.storage.local` limited to: configured FrameNest origin, adapter version
acknowledgement, and UI prefs. Explicit "Reset companion" control clears it.
No secrets, cookies, or tokens are ever stored (none exist extension-side —
identity is established per-connection by Tailscale Serve).

Save surfacing: on a post permalink page the post URL is derived from
`location` (matched against `/^https:\/\/(x|twitter)\.com\/[^/]+\/status\/\d+/`);
in feed contexts the injected per-post affordance resolves the enclosing
`article` element's timestamp permalink anchor via the adapter contract. No
feed scraping: only the user-focused post is read, on click.

Composer detection: a bounded `MutationObserver` (subtree on `document.body`,
attribute-filtered) evaluates adapter-contract signals; each detected composer
gets an instance token (tabId + monotonically assigned composer id + a weak
element reference). Inline, modal, and reply variants are distinct descriptor
entries. The picker can bind only to the composer whose injected button the
user clicked. Teardown (element removal / SPA navigation) invalidates tokens;
attach against an invalid token fails closed.

Accessibility/states: loading, success (+ "View in picker"), retry (bounded,
surfacing `can_retry`), empty, permission-denied (`CAPABILITY_DENIED`),
unavailable (off-tailnet/server down), unsupported-media
(`X_NO_SUPPORTED_MEDIA` shown as "this post's media isn't supported yet" —
never claimed as acquired), partial success (n of m assets), and stale-adapter
states are all first-class, keyboard-reachable, `role="status"`/`aria-live`
announced.

## 5. Permission, origin, identity, CSRF, and CORS model

Proposed manifest (planning precision):

```json
{
  "manifest_version": 3,
  "name": "FrameNest X Companion",
  "version": "0.1.0",
  "key": "<pinned base64 dev key — stable ID>",
  "permissions": ["sidePanel", "storage"],
  "optional_permissions": ["downloads"],
  "host_permissions": ["https://x.com/*", "https://twitter.com/*"],
  "optional_host_permissions": ["https://*.ts.net/*"],
  "background": { "service_worker": "background/service_worker.js" },
  "content_scripts": [
    { "matches": ["https://x.com/*", "https://twitter.com/*"],
      "js": ["content/x_adapter_contract_v1.js", "content/x_adapter.js"],
      "run_at": "document_idle" }
  ],
  "side_panel": { "default_path": "ui/picker.html" },
  "action": { "default_title": "FrameNest companion" }
}
```

Justification per permission: `sidePanel` (picker surface); `storage`
(non-secret config only); `downloads` is **optional**, requested at first
fallback use (bounded fallback attach path, Section 10); host permissions for
X/Twitter are the content-script surface and also let the SW read the active
post URL context; the FrameNest origin itself is **not** hardcoded — the
tailnet hostname is host-specific private configuration. At onboarding the user
enters/pastes their FrameNest origin; the extension requests an optional host
permission for that exact origin via `chrome.permissions.request` (user
gesture). `optional_host_permissions` must be declared as a pattern, hence
`https://*.ts.net/*` — bounded to Tailscale's owned domain; the runtime grant
is narrowed to the exact origin. No `<all_urls>`, no `cookies`, no `tabs`
(SW never enumerates tabs; it answers messages from its own content script),
no `externally_connectable` (web pages cannot message the extension).

Cross-origin fetch owner: the service worker only (Section 4 evidence).
Identity continuity: the SW fetches `https://<framenest-host>.ts.net/...` from
the user's browser; the connection terminates at root-owned `tailscaled` on the
NUC, which strips client-supplied identity headers and reinjects the verified
`Tailscale-User-Login`/`Tailscale-User-Name` (Tailscale doc). FrameNest trusts
them only on the UDS ingress (ADR-0048). No credential is copied anywhere.

Mutation-origin conflict resolution (anchor 14) — **selected design**:

1. New config key `companion_extension_origins: list[str]` in
   `src/framenest/configuration.py`, default `[]`; validator accepts only exact
   `chrome-extension://` + 32-char `[a-p]` origins, max 4 entries.
2. `RoutePolicy` gains `companion_mutation: bool = False`. Only
   `POST /api/x/requests` and `POST /api/x/requests/{claim_id}/retry` are
   flagged `True`.
3. In `TailscaleIngressMiddleware`'s unsafe-method gate (validation order
   unchanged: singleton/conflict → forwarded proto/host → route policy →
   identity presence → origin/header → capability → audit): accept when
   `origin == external_origin` (existing web UI, unchanged) **or**
   (`policy.companion_mutation` and `origin in companion_extension_origins`).
   `X-FrameNest-Request: 1` remains required in both branches. Everything else
   still yields `MUTATION_ORIGIN_FORBIDDEN`.
4. Trust proof: `Origin` is a forbidden header — X page scripts and arbitrary
   web origins cannot set it; the browser sets it to `chrome-extension://<id>`
   only for requests genuinely initiated by that extension (inference,
   deterministic gate in Slice A). Tailscale identity, route capability
   (`x.request`), admission limits, and audit recording all still apply.
   Residual: a *malicious installed extension* could spoof the Origin via
   `declarativeNetRequest`, but it would still act under the user's own
   verified tailnet identity and capabilities — no privilege expansion beyond
   what the user's own browser already has; recorded in Section 15.
5. Web UI contract preserved byte-for-byte: same header, same origin value,
   same routes.

CORS: **no CORS headers are added**. Extension-origin fetches with host
permission do not require `Access-Control-Allow-Origin` (Chrome
network-requests doc); content scripts never fetch FrameNest. `Origin` absence
or mismatch on mutations remains forbidden.

Stable extension identity: unpacked developer-mode loads derive the ID from the
manifest `key`; pinning `key` (dev keypair generated once, public key in repo,
private key held by Michal — never committed) keeps the ID stable across
reloads and machines, making the server allowlist durable. Version skew:
`GET /api/x/companion/media` responses carry `companion_api_version:
"framenest-companion.v1"`; the extension refuses operation with an explicit
"upgrade companion/server" state on mismatch.

Off-tailnet / error behavior: DNS/TCP failure → "FrameNest unreachable — are
you on the tailnet?"; `401 IDENTITY_REQUIRED` → "identity not recognized"
(signed-in identity not provisioned); `403 IDENTITY_NOT_AUTHORIZED` /
`CAPABILITY_DENIED` → permission-denied state; no retry storms (bounded
backoff, max 3 automatic retries on 5xx, none on 4xx).

## 6. Canonical eligible-meme server predicate

**Owner: new module `src/framenest/application/companion_picker.py`** —
application-layer composed policy, translated once into the repository query.
The extension never re-derives eligibility; the web Gallery query is untouched.

Predicate `companion_eligible(media)` (all conjunctive):

1. `content_category == ContentCategory.MEME`;
2. `media.kind in {IMAGE, ANIMATED_IMAGE, VIDEO}`;
3. at least one location with `availability == available` whose
   `(kind, extension)` pair is in `SUPPORTED_MEDIA_CONTENT`;
4. audience: `is_published(media_id)` **OR** requester-private live X ownership
   (`x_assets` success join `x_post_claims.created_by_login_key = <caller>`);
5. short-video constraint: videos acquired via X are already bounded at
   acquisition (≤300 s, downloader/domain constants); no additional duration
   filter is applied at listing time because catalog listing projections do not
   currently carry duration — labeled inference; if the implementation Worker's
   schema check finds a durable duration column, the predicate adds
   `duration_seconds <= 300` for videos, else the acquisition-time bound stands
   as the enforcement point (recorded as an implementation-time verification
   step, not an open architecture question).

Query contract — new endpoint `GET /api/x/companion/media` (capability
`x.request`, `RoutePolicy` GET, no audit action — consistent with existing GET
routes):

- Parameters: `q` (title search, same normalization/240-code-point bound as
  catalog), `tag` (repeated, AND semantics), `kind` (`image|animated_image|video`,
  optional), `limit` (1–50, default 24), `cursor` (opaque
  `<created_at_ms>:<media_id>`, same convention as X request list).
- Response (planning precision): `{ items: [{ media_id, media_kind,
  display_title, content_category, acquisition_source, creator_handle,
  creator_display_name, ownership: "own"|"published", location_id,
  preview_path, content_path, download_path, byte_size? }], next_cursor,
  companion_api_version }`. Paths are relative; the SW absolutizes them against
  the configured origin. No absolute URLs, no other users' identifiers.
- Sorting: `created_at_ms DESC, media_id ASC` (stable). Headers:
  `Cache-Control: no-store`. Empty state: `items: []`, `next_cursor: null`.
- Errors: 422 invalid query; 503 catalog unavailable; 401/403 via ingress and
  route capability.

Non-enumeration guarantee: the SQL predicate is
`(published) OR (own X success)`, with `<caller>` taken only from the verified
ingress identity — there is **no** request parameter that widens audience; the
query cannot express "another user's private media" at all (contrast with a
generic `?owner=` filter, explicitly rejected). Requester-private items appear
in the picker the moment their asset reaches `CATALOGED` (they are category
`meme` by default) without any change to the published-only Gallery contract;
others see them only after administrator publication (ADR-0049 unchanged).

Repository seam: extend `MediaCatalogQuery`/`list_media`
(`application/ports/media_catalog_repository.py`,
`infrastructure/persistence/media_catalog_repository.py`) with an explicit
`companion_audience: str | None` (login key) field used **only** by
`ListCompanionMedia`; when set, `published_only` semantics become the OR-clause
above. The existing public path keeps `published_only=True` untouched.

## 7. Save sequence: ordinary user

1. User clicks the injected "Save to FrameNest" affordance on the focused X
   post (explicit gesture; nothing happens on passive browsing).
2. Content script resolves the post URL (permalink `location` match or the
   article's permalink anchor via adapter contract) and sends
   `{v, type:"save.submit", url}` to the SW. The SW re-validates the URL shape
   (host allowlist + numeric status id) before any network call — defense in
   depth; server-side `accept_x_post_url` remains authoritative.
3. SW: `POST /api/x/requests` with JSON body `{"url": …}`,
   `X-FrameNest-Request: 1`; browser sets `Origin: chrome-extension://<id>`;
   Serve injects identity; ingress validates origin-allowlist + header +
   capability `x.request`; `XAcquisitionRequestService.submit` runs unchanged.
4. Response mapping (existing surface): `submission_result` `new` →
   "Saving…"; `active_reuse` → "Already saving"; `reuse` → "Already in your
   library" with the picker affordance; 429 codes (`X_REQUEST_ACTIVE_LIMIT`,
   `X_REQUEST_GLOBAL_QUEUE_FULL`, `X_REQUEST_RATE_LIMIT`,
   `X_REQUEST_FAILED_24H_LIMIT`) → bounded, human-readable busy/limit states;
   507 → insufficient-storage state.
5. SW polls `GET /api/x/requests/{claim_id}` (bounded: 1 s → 5 s backoff, max
   90 s, then "continuing in background — check picker"); phase/state drive
   the content-script badge: `completed`, `completed_partial` ("n of m saved",
   per-asset failure codes surfaced generically), `failed` with retry
   affordance → `POST /api/x/requests/{claim_id}/retry` (same mutation trust
   path; `X_REQUEST_STATE_CONFLICT` → re-fetch state).
6. Terminal `X_NO_SUPPORTED_MEDIA` (photo-only posts today) is shown as an
   honest unsupported-media state, never as success. Multi-asset posts: ≤4
   assets, per-asset states from the claim response; partial success keeps
   cataloged assets and offers retry for the rest.
7. Newly cataloged items become picker-eligible for the requester immediately
   (Section 6 predicate, ownership `"own"`); for everyone else only after admin
   publication.

**Static X photo resolution (anchor, decisive classification):** named
MVP-blocking-for-photos spike **X-PHOTO-01** (separately authorized,
read-only): inspect the pinned `yt-dlp==2026.7.4` `yt_dlp/extractor/twitter.py`
in the canonical `.venv` (read-only file inspection; no execution) plus the
upstream yt-dlp changelog/source for a conforming photo path (extractor args or
API modes emitting photo entries, or a version where TwitterIE stops filtering
`m['type'] != 'photo'`). Outcomes: (a) conforming path exists in the pin →
bounded `YtDlpXExtractor` extension behind the existing normalized contract
with fake-fixture tests, no dependency change; (b) requires a yt-dlp upgrade →
returned to ORCHESTRATOR as a separate dependency decision (pin is load-bearing
and commented as verified contract in `downloader.py`); (c) no conforming path
→ static photos stay excluded; the extension and picker are already
image-capable (`SUPPORTED_MEDIA_CONTENT` serves jpg/png), so a later photo
ingestion lands with **zero** extension or picker changes. The MVP plan does
not advertise static-X-photo acquisition.

## 8. Save sequence: administrator

Identical to Section 7 in every network respect: the administrator submits
through the ordinary `POST /api/x/requests` route under their own verified
identity. This matches current repository truth — admins hold `x.request`
(ordinary set) plus `x.acquire`; no privileged submit route exists and none is
invented. Differences: (1) admission limits apply to the admin's own login key
the same way (no admin bypass exists today; preserved); (2) the admin may
additionally review any claim via `GET /api/admin/x/requests/{claim_id}` —
not surfaced in the extension MVP; (3) publication of an acquired item for all
users remains the existing admin web UI flow (`PUT
/api/admin/media/{id}/content-publication`), outside the extension.

## 9. Picker/search/preview design

- **Opening gesture:** user clicks the injected FrameNest attach button inside
  the chosen composer → content script sends `picker.open` with the composer
  token → SW calls `chrome.sidePanel.open({tabId})` (user gesture), fallback
  action popup. The picker binds to that one composer token; switching targets
  requires a new gesture.
- **Query/filter model:** search box (`q`, debounced ≥300 ms), kind chips
  (image / animated / video), tag filters from `GET /api/canonical-tags`
  (existing, `gallery.read`), pagination via cursor ("Load more"). Every
  request goes SW → `GET /api/x/companion/media` (Section 6).
- **Preview:** images and GIF-style media render via `<img>` /
  `<video muted loop>` pointed at the existing relative
  `…/gallery-preview` / `…/content` paths — plain no-cors subresource GETs,
  audience-enforced server-side (`content_audience_allows` already gates
  gallery-preview and content; requester-private X items pass for their owner).
  Videos preview with `preload="none"` + poster; playback on click streams via
  byte ranges (supported by the content route). No bytes are proxied through
  extension storage; no unbounded transfer (server streams, client caps
  concurrent previews at 6).
- **Empty/error states:** empty library (with save-from-X hint), no-results,
  off-tailnet/unreachable, permission-denied, server-version-mismatch,
  stale-adapter. All text from the extension; server strings are never rendered
  as HTML (`textContent` only, per Chrome XSS guidance).
- **Attach target data:** selecting an item sends `attach.request` with
  `media_id` + `location_id` only; the SW constructs
  `/api/media/{id}/locations/{loc}/content` itself (no caller-supplied URLs).

## 10. Composer detection and attachment design

Adapter seam: `x_adapter_contract_v1.js` is a pure-data module:
`{ adapterVersion: "x-dom.v1", signals: { composer: [...], fileInput: [...],
postPermalink: [...], actionBar: [...] } }` with per-signal fallback chains and
a `validate()` that returns failure codes. `x_adapter.js` interprets it; a
descriptor mismatch disables features with the stale-adapter state (fail
closed). Repository fixtures snapshot representative X DOM structures
(synthetic, hand-authored — no signed-in capture) under
`tests/support/x_fixtures/`.

Mechanism comparison (evidence: Chrome messaging doc — JSON serialization,
64 MiB max; Chromium content-script fetch doc):

- **Direct `File`/`DataTransfer` assignment to the composer's file input —
  SELECTED primary.** SW fetches bytes from the audience-gated content route
  (bounded, below), transfers them to the content script as chunked base64 over
  a `runtime.Port` (JSON-only channel; chunk ≤ 4 MiB base64; total binary cap
  **32 MiB** → ≈43 MB base64, under the 64 MiB message cap; larger items route
  to the fallback), content script builds `new File([bytes], sanitizedName,
  {type})`, assigns via `DataTransfer.items.add` + `input.files = dt.files` +
  `input.dispatchEvent(new Event("change", {bubbles:true}))`. Whether X's React
  state honors a synthetic assignment is exactly what Slice D proves against a
  synthetic React fixture and the Section 11 spike proves against real X.
- **Explicit user download + manual attach — SELECTED bounded fallback.** SW
  calls `chrome.downloads.download({url: <absolute content-or-download URL>,
  saveAs: true})` (optional permission, requested on first use); the user drops
  the file into the composer themselves. Always available, zero DOM coupling.
- Clipboard: rejected (image-only semantics, requires extra permission and
  focus choreography, unreliable for video).
- Drag/drop synthesis: retained as an in-spike experiment only if file-input
  assignment fails (synthetic `DragEvent` with `DataTransfer` onto the composer
  drop zone); not an MVP commitment.
- Extension-page transfer bridge / Native Messaging: rejected for MVP (surface
  and install complexity without demonstrated need).

Constraints: 32 MiB attach cap (client-enforced pre-flight via
`Content-Length`, plus hard read cap during streaming); one transfer in flight;
60 s transfer timeout; cancellation on picker close/composer teardown; memory
freed by dropping chunk references and revoking nothing global (no object URLs
persist). **No-submit guarantee:** the extension contains no code path that
clicks, programmatically submits, or keyboard-dispatches Enter into the
composer — repository tests assert the absence of any Post-button selector in
the adapter contract, and the adapter never resolves one.

Data exposure: once the user attaches, the X page can observe the file (it is
in X's own input) — acceptable: the explicit purpose of the action is to give
that media to a post the user will manually review and send. Nothing else
(media bytes of non-selected items, catalog metadata) ever enters page context;
preview stays in the extension-origin side panel.

Failure recovery: composer disappeared → token invalid, attach aborted with
notice; file input replaced → one re-resolution, then fail closed; type/size
rejected by X → surface X's own UI state, no retry loop; adapter drift →
stale-adapter state and disabled affordances.

## 11. Volatile X feasibility spike

**SPIKE-X-01 (requires separate Michal authorization; not authorized now).**
Smallest real-environment probe, one bounded session, Michal's Brave, his
signed-in X account:

1. *Brave surface check (read-only):* load the MVP extension unpacked in a
   disposable Brave profile (or Michal's profile with explicit consent);
   verify `chrome.sidePanel.open` opens and persists for ≥60 s on x.com, and
   the fallback popup renders. Historical Brave sidePanel bugs make this a
   hard gate for the primary surface.
2. *Origin-header readback:* with the NUC dev/staging path or a loopback test
   server, record the `Origin` header received for SW-initiated GET/POST —
   confirms the `chrome-extension://<id>` allowlist premise in the real target
   browser. (The deterministic equivalent runs earlier in Slice A under system
   Chrome via the repository CDP harness; this step re-confirms in Brave.)
3. *Composer attachment:* on a real composer, execute the
   file-input/`DataTransfer` assignment with one small synthetic test image
   (≤1 MiB, repository fixture, no real X media saved or downloaded by the
   probe). Success criteria: X renders the media attachment preview chip and
   enables (but the probe NEVER clicks) Post. Failure criteria: preview absent
   after assignment+change event; then exactly one fallback experiment
   (synthetic drop event). Max two meaningful recovery attempts total (AP
      browser annex discipline).
4. *No-mutation boundary:* the probe never submits a post, never saves real X
   media, never reads DMs/private accounts; drafts are discarded, not posted.
5. *Cleanup:* discard composer content, unload/remove the probe extension if a
   disposable profile was not used, clear any downloaded test file, report
   evidence (versions, observed signals, pass/fail per criterion).

Consequences for implementation ordering: Slices A–D do not depend on
SPIKE-X-01 (synthetic fixtures + system Chrome cover them). SPIKE-X-01 gates
only the final packaged-Brave acceptance tier (Section 19). If criterion 3
fails unrecoverably, MVP ships with the download-fallback attach path as
primary — a product-noticeable but safe degradation, decided by Michal.

## 12. Minimal backend/API/configuration delta

Reused unchanged: `POST /api/x/requests`, `GET /api/x/requests`,
`GET /api/x/requests/{id}`, `POST …/retry`, `GET /api/admin/x/requests/{id}`,
`GET /api/identity/me` (setup/capability probe — implementation verifies its
payload includes role/capabilities; if not, the companion list response's
version field plus 403 behavior is the capability signal, no new endpoint),
`GET /api/canonical-tags`, `GET /api/media/{id}` (audience-gated hydration),
`GET …/gallery-preview`, `GET …/content`, `GET …/download`.

New/changed (complete list):

1. `src/framenest/configuration.py` — add `companion_extension_origins:
   list[str] = []` with exact-origin validator (`chrome-extension://` + 32
   `[a-p]`, max 4).
2. `src/framenest/adapters/api/tailscale_ingress.py` — `RoutePolicy` field
   `companion_mutation`; origin-gate branch per Section 5; flag the two X
   mutation policies.
3. `src/framenest/adapters/api/x_companion_api.py` — NEW router: `GET
   /api/x/companion/media`; pydantic response models (`extra="forbid"`),
   `_NO_STORE_HEADERS`, error envelope identical to catalog API conventions.
4. `src/framenest/application/companion_picker.py` — NEW: predicate constants,
   `ListCompanionMedia` (normalization mirroring `media_catalog.py` bounds),
   response projection builder.
5. `src/framenest/application/ports/media_catalog_repository.py` +
   `src/framenest/infrastructure/persistence/media_catalog_repository.py` —
   add `companion_audience` to `MediaCatalogQuery`; SQL OR-clause
   (`published` OR own-X-success join) using existing tables/indexes.
6. `src/framenest/adapters/api/application.py` — wire the new router and
   service; pass `companion_extension_origins` into `TailscaleIngressMiddleware`.
7. Route policy entries: `GET /api/x/companion/media` (capability
   `x.request`).

Security rationale: one purpose-specific read contract instead of widening
`GET /api/media`; mutation trust extended by exact-origin allowlist scoped to
two X routes only; no generic proxy, no CORS, no new capability.

Request/response shapes at planning precision are in Sections 6 and 5.

## 13. Exact proposed paths and owner map

| Path | Status | Responsibility | Why this owner |
| --- | --- | --- | --- |
| `extension/manifest.json` | new | MV3 declaration, pinned key, least-privilege permissions | extension root artifact |
| `extension/background/service_worker.js` | new | sole FrameNest API client, polling, bounded byte transfer | extension origin required for cross-origin fetch (Chrome doc) |
| `extension/content/x_adapter.js` | new | DOM observation, affordance injection, attach execution | content-script boundary |
| `extension/content/x_adapter_contract_v1.js` | new | versioned selector/signal descriptor | volatility isolation seam |
| `extension/ui/picker.html`, `picker.js`, `picker.css` | new | side-panel/popup picker UI | extension-page surface |
| `extension/shared/messages.js` | new | versioned message schema + validation | single protocol owner |
| `extension/icons/` | new | action/panel icons | packaging |
| `src/framenest/adapters/api/x_companion_api.py` | new | picker list endpoint | API adapter layer owns HTTP contract |
| `src/framenest/application/companion_picker.py` | new | canonical eligibility predicate + query normalization | application layer owns policy |
| `src/framenest/application/ports/media_catalog_repository.py` | change | `companion_audience` query field | existing catalog query port |
| `src/framenest/infrastructure/persistence/media_catalog_repository.py` | change | SQL audience OR-clause | persistence owns SQL |
| `src/framenest/adapters/api/tailscale_ingress.py` | change | companion mutation origin branch | sole ingress trust owner |
| `src/framenest/configuration.py` | change | `companion_extension_origins` setting | settings owner |
| `src/framenest/adapters/api/application.py` | change | wiring only | composition root |
| `tests/contract/test_x_companion_api.py` | new | endpoint contract + non-enumeration | mirrors `test_x_request_api.py` |
| `tests/contract/test_tailscale_ingress_security.py` | change | companion origin allow/deny matrix | existing ingress security suite |
| `tests/unit/test_companion_picker.py` | new | predicate/query unit tests | unit tier |
| `tests/contract/test_media_catalog_repository.py` | change | audience SQL semantics | existing repository suite |
| `tests/x_companion_extension.test.js` | new | SW protocol + adapter fixtures (node:test) | project JS test convention |
| `tests/browser_companion_evidence.test.js` | new | gated CDP evidence: unpacked extension vs. local server, Origin readback, synthetic attach | mirrors `browser_*_evidence` pattern |
| `tests/support/x_fixtures/` | new | synthetic X DOM + React-attach fixtures | fixture ownership |
| `docs/adr/0061-x-meme-browser-companion.md` | new | decision record | ADR convention |
| `docs/X_COMPANION.md` | new | operator + user doc | doc ownership |
| `README.md`, `SERVER.md`, `SECURITY.md` | change | living status/boundary notes | truth-map docs |
| `deploy/ubuntu/` env example + runbook section | change | new config key, extension artifact relation | deployment doc ownership |

No changes to: YouTube surfaces, Gallery/Details frozen UX, X cockpit redesign,
`.ap/`, `docs/AP_UPGRADE_OBSERVATIONS.md`, deployment helper logic.

## 14. Migration and durable-state implications

**No migration required.** Proof: the companion predicate and flows read only
existing durable truth — `x_post_claims.created_by_login_key` and
`x_assets.{media_id, media_location_id, state}` (migration 0028, with index
`ix_x_assets_media(media_id, media_location_id)`), `media_content_publications`
(0021), catalog `content_category`/`acquisition_source` (0023/0027/0028).
Eligibility is a read-time join, not stored state, so there is no backfill, no
downgrade concern, and no new privacy surface at rest (nothing new is
persisted; requester-private linkage already exists and already powers
`has_live_requester_media_access`).

One verification gate, not a schema change: Slice B includes an `EXPLAIN
QUERY PLAN` integration assertion for the own-private OR-clause. If the plan
shows a full scan regression beyond the bounded test fixture scale, the result
is returned to ORCHESTRATOR as a candidate index-only migration `0029` with
separate authority — it is **not** silently added. Extension durable state is
`chrome.storage.local` config only (Section 4), cleared by the reset control;
no media bytes are persisted extension-side.

## 15. Privacy, secret, authentication, and abuse matrix

| Asset / threat | Boundary | Control | Test (tier) | Residual risk / owner |
| --- | --- | --- | --- | --- |
| Tailscale identity headers | Serve → UDS only | provenance-bound trust (unchanged); extension carries no credentials | existing ingress suite (contract) | none new |
| Mutation from arbitrary web page / X page script | unsafe-method gate | `Origin` is a forbidden header; allowlist exact `chrome-extension://` ID + `X-FrameNest-Request: 1`, scoped to 2 routes | ingress unit + Slice A browser readback | malicious *installed* extension can spoof Origin but stays within user's own identity/capabilities — owner: Michal (extension hygiene) |
| Malicious extension / compromised renderer | content-script → SW messages | opaque handles only; SW builds URLs; message schema version + type enum; payload bounds | JS fixture tests | X page could trick content script into wrong post URL — user-visible target shown before submit; owner: extension |
| Private-media enumeration | picker query | audience OR-clause server-side, no widening parameter; 404 semantics on direct routes | `test_x_companion_api` negative cases | none identified beyond authenticated self-listing (intended) |
| Arbitrary proxying | SW fetch surface | fixed path templates + validated IDs; no caller-supplied URLs; host permission is exact origin | JS unit + code review gate | none |
| Hostile metadata (titles, filenames, post text) | UI + headers | `textContent` rendering; existing ASCII-safe download filenames; bounded field lengths server-side | existing content tests + new UI test | none new |
| Oversized media | attach path | 32 MiB cap, Content-Length pre-flight, hard read cap, one transfer, 60 s timeout, cancellation | JS fixture + browser evidence | memory pressure within bound; accepted |
| Stale X adapter | DOM coupling | versioned descriptor, fail-closed disable, no silent guessing | fixture tests incl. drifted-DOM fixture | X can break detection silently → degraded, not dangerous |
| Log leakage | logs/audit | no URLs/titles/media bytes/identity beyond existing audit actor fields; extension has zero telemetry | code review + existing audit tests | none new |
| X credentials/cookies | never touched | extension never reads X storage/cookies; no `cookies` permission | manifest static check in JS test | none |
| Auto-submission | composer | no Post selector exists in adapter contract; attach only into user-selected composer | static assertion test + acceptance matrix | none |

## 16. Dependency decision

- **Backend: no new runtime or dev dependencies.** FastAPI/pydantic/SQLAlchemy
  already carry every proposed change. Lockfile untouched.
- **Extension: zero dependencies, no npm toolchain, no bundler** — consistent
  with the project's existing JS convention (`node:test`, no `package.json`
  test script; WORKER_EXECUTION_CONTRACT forbids inventing a JS toolchain).
- **yt-dlp pin `2026.7.4` unchanged for MVP.** X-PHOTO-01 outcome (b) would be
  a separate, explicitly authorized dependency decision — the pin is a
  documented verified contract (`downloader.py` header) and is not casually
  moved.
- Rejected dependency-free alternatives considered and kept: none needed —
  every required capability is native (MV3 APIs, `fetch`, `DataTransfer`).
- Later dependency authority explicitly needed only if X-PHOTO-01 lands on
  outcome (b).

## 17. Causal implementation slices and gates

Each slice is independently gateable; nothing depends on unproven later
assumptions. Rollback for all server slices: config defaults
(`companion_extension_origins: []`, picker endpoint inert without identities)
make the change a no-op until configured.

- **Slice A — mutation-trust proof (retires the riskiest server premise).**
  Paths: `configuration.py`, `tailscale_ingress.py`, `application.py`,
  `test_tailscale_ingress_security.py`, `test_x_route_policy.py`,
  `tests/browser_companion_evidence.test.js` (harness seed), minimal
  `extension/` skeleton. Behavior: Section 5 origin branch. Tests: unit matrix
  (allowed extension origin on flagged route; rejected on unflagged route;
  rejected spoof/absent; web UI path unchanged) + gated CDP evidence: unpacked
  skeleton extension POSTs to a local test server, server records
  `Origin: chrome-extension://<id>`. Exit gate: suite green incl. negative
  paths. Rollback: empty allowlist.
- **Slice B — picker backend.** Paths: `companion_picker.py`,
  `x_companion_api.py`, repository port+impl, `application.py` wiring, tests
  (`test_x_companion_api.py`, `test_companion_picker.py`,
  `test_media_catalog_repository.py`). Behavior: Section 6 contract. Gate:
  contract tests incl. non-enumeration (user B never sees user A's private
  item; published visible to both), pagination/sorting stability, `EXPLAIN
  QUERY PLAN` assertion. Rollback: route not wired.
- **Slice C — extension core.** Paths: `service_worker.js`, `messages.js`,
  `picker.*`, `x_adapter*.js` save path, `tests/x_companion_extension.test.js`,
  fixtures. Behavior: save flow + picker against a fixture server (Node
  `node:test` mock) and Slice A/B real server. Gate: JS tests + local
  integration green; save state machine covers every Section 7 state.
- **Slice D — attach mechanism proof (synthetic).** Paths: attach module in
  `x_adapter.js`, React-like synthetic composer fixture,
  `browser_companion_evidence.test.js` extension. Behavior: chunked transfer +
  `DataTransfer` assignment on fixture; cap/timeout/cancel. Gate: CDP evidence
  green in system Chrome. Note: proves the *mechanism*, not X's live DOM.
- **Slice E — SPIKE-X-01** (Section 11; separately authorized, Michal-owned
  steps). Gate for packaged-Brave acceptance tier only.
- **Slice F — packaging/docs/rollout.** Paths: Section 13 docs/deploy rows.
  Gate: doc/contract tests (`test_nuc_release_docs`-style conventions), Michal
  UX acceptance scheduling.

## 18. Verification ladder

1. **Unit/domain (deterministic):** predicate normalization, ingress origin
   matrix, config validators, message schema, adapter descriptor validation.
   `./.ap/ap exec … --operation test-focus` / `node --test`.
2. **API contract:** `test_x_companion_api.py`, ingress security suite,
   catalog repository suite — positive + negative + enumeration attempts.
3. **Persistence/migration:** repository tests on 0028 schema; explicit
   assertion that no new Alembic revision is introduced (tree check) plus the
   Slice B query-plan gate.
4. **Ingress security:** spoofed/missing Origin, wrong extension origin,
   flagged vs unflagged route, web UI regression, capability denial, audit
   recording preserved.
5. **Extension fixtures:** node:test against mock server + synthetic DOM
   fixtures incl. drifted fixture (fail-closed proof).
6. **Local integration (repository browser evidence):** gated
   `FRAMENEST_RUN_BROWSER_EVIDENCE=1` CDP suite: real unpacked extension +
   local server; Origin readback; save flow against fake extractor; synthetic
   attach. Exact-source provenance per WORKER_EXECUTION_CONTRACT.
7. **Packaged Brave + signed-in X:** SPIKE-X-01 then Section 19 — human,
   separately authorized, never conflated with repository evidence.
8. **Production readback:** after any separately authorized release: deployed
   SHA/manifest, config presence, one real Save + one real picker session per
   Section 19 identity set. Not part of implementation authority.

## 19. Real Brave acceptance matrix (Michal-owned, post-spike)

Prerequisites: released server with companion config (allowlist contains the
pinned-key extension ID), identity_map contains admin + two ordinary tailnet
identities, extension loaded unpacked in Michal's Brave, tailnet connected.

| Case | Admin | User A | User B |
| --- | --- | --- | --- |
| Save video post → appears in own picker as `own` | ✓ | ✓ | ✓ |
| Save GIF-style post | ✓ | ✓ | ✓ |
| Save photo-only post → honest unsupported state | ✓ | ✓ | ✓ |
| Save same post twice → `reuse` messaging | ✓ | ✓ | ✓ |
| Multi-asset post with one failure → partial + retry | ✓ | ✓ | ✓ |
| Picker search/filter/preview (image, GIF, short video) | ✓ | ✓ | ✓ |
| Own-private item visible to owner | ✓ | ✓ | ✓ |
| Other-private denied: B never sees A's unpublished item; direct URL 404 | ✓ | ✓ | ✓ |
| Published item visible to all after admin publication | ✓ | ✓ | ✓ |
| Attach ≤32 MiB item → composer preview, manual review, manual Post by user | ✓ | ✓ | ✓ |
| Attach >32 MiB item → download fallback offered | ✓ | ✓ | ✓ |
| Off-tailnet → unreachable state, no hang | ✓ | ✓ | ✓ |
| Capability-denied identity (temporarily unmapped) → denied state | ✓ | ✓ | ✓ |
| X DOM drift simulation (disable a signal) → stale-adapter state | ✓ | ✓ | ✓ |
| No auto-submit: extension never posts; only the user posts | ✓ | ✓ | ✓ |

Michal owns: account selection, Brave profile, all X interactions, posting
decisions, and rendered-UX acceptance. The Worker never touches signed-in X.

## 20. Rollout, packaging, loading, rollback, and recovery

- **Artifact relation:** the extension lives in-repo at `extension/`, versioned
  by the repository commit and its own `manifest.version`
  (`companion_api_version` couples to the server contract). It is **not** part
  of the NUC release payload — the immutable release contract
  (`deploy/ubuntu/framenest-release`, ADR-0060) is untouched; the NUC side
  changes are config keys only, shipped by the normal release process under
  separate deployment authority.
- **Stable ID:** manifest `key` pins the ID; the public key is committed, the
  private key stays with Michal (documented in `docs/X_COMPANION.md`, never
  committed). Server allowlist entry: `chrome-extension://<derived-id>`.
- **Loading:** Brave `brave://extensions` developer mode, "Load unpacked" —
  MVP distribution is developer loading only; Web Store packaging is not
  required and not pursued.
- **Activation order:** (1) release server (inert defaults), (2) add
  `companion_extension_origins` + restart per runbook, (3) load extension,
  (4) onboarding grants the exact-origin host permission, (5) acceptance
  matrix. Rollback: remove the config key (mutations from the extension
  immediately fail closed), unload the extension; picker endpoint remains a
  harmless authenticated read. Version skew: extension detects
  `companion_api_version` mismatch and disables with an upgrade prompt;
  server-old/extension-new skew fails closed the same way. Recovery from a bad
  server release follows the existing immutable-release rollback (previous
  release directory + `.framenest-release-sha`), unchanged.

## 21. Owner documentation updates

- **New ADR-0061** (`docs/adr/0061-x-meme-browser-companion.md`): extension
  origin-trust model, side-panel selection, attach mechanism, eligibility
  predicate ownership, scope exclusions. Required because this is an
  architecture decision with security weight, matching repository convention.
- **`docs/X_COMPANION.md`** (new): operator setup (config keys, allowlist,
  key pinning), user guide (Save/Use flows, states), troubleshooting,
  privacy/storage/clearing behavior.
- **`README.md` / `SERVER.md` / `SECURITY.md`**: living-status and boundary
  notes (tailnet-only preserved, no new exposure) per the AGENTS.md truth map.
- **`deploy/ubuntu/` env example + `docs/UBUNTU_NUC_DEPLOYMENT.md`:** new
  `FRAMENEST_COMPANION_EXTENSION_ORIGINS` key (example values only, no real
  IDs/hosts) and one runbook paragraph; release helper logic untouched.
- **`ROADMAP.md`:** one line for the companion MVP stage.
- Docs are not a substitute for code/test ownership: every doc row maps to
  Slice F after the code slices land.

## 22. Parked scope, residual risks, and stop conditions

Parked (explicitly non-MVP): static X photo acquisition (X-PHOTO-01 outcome
pending); YouTube browser actions; Web Store distribution; native messaging;
multi-item attach; background/scheduled anything; admin X review inside the
extension; generic companion for other sites.

Residual risks and owners: Brave `sidePanel` stability (owner: SPIKE-X-01 →
Michal decision if degraded to popup); X DOM volatility (owner: adapter
contract + stale state; recurring maintenance is a product cost Michal
accepts); malicious installed extensions sharing the browser (owner: Michal's
extension hygiene; bounded by identity/capability enforcement); `Origin`-header
premise is inference until Slice A/Spike readback (owner: implementation
Worker, gate-defined).

Stop conditions for later implementation/acceptance: Slice A readback shows no
reliable extension Origin → stop, return to ORCHESTRATOR (design re-open);
SPIKE-X-01 criterion 3 fails after two recoveries → attach degrades to
download-fallback, Michal decides MVP viability; any request for CORS
relaxation, broader host permissions, X credential use, or auto-submit →
immediate stop, out of scope; baseline drift (public main ≠ planned baseline)
→ re-gate before implementation.

## 23. Recommended implementation Worker route

**One route:** `current-worker-session` continuation of this healthy session,
with a new complete implementation prompt carrying `Native planning mode:
not-used`, the exact baseline `3cf22b8aaff61ed71093207d5b24aae622f394ac`, the
slice allowlist (Sections 13/17), and explicit boundaries (no push, no
deployment, no provider/X contact, no signed-in browser access; SPIKE-X-01 and
any release/deploy require their own later grants). Rationale: session is
healthy, full evidence context is retained, no independence trigger exists, and
the planning contract prefers the same-session route under exactly these
conditions. Reasoning: high for Slice A (security-sensitive ingress change),
standard for B–F. Independence: the ingress/mutation-trust change warrants a
later Fresh Independent Audit before production acceptance; Michal's UX
acceptance (Section 19) is separately required regardless. If the Orchestrator
judges retained context stale or independence preferable, a
`fresh-worker-session` with this report as evidence is the fallback — not a
parallel route.

## 24. Smallest next Orchestrator action

Approve this plan as the execution basis (or request one targeted revision).
No technical choice is left open for Michal: architecture, predicate, trust
model, attach mechanism, and spike boundaries are selected; the only later
human decisions are the separately authorized SPIKE-X-01 execution and the
implementation grant itself.
