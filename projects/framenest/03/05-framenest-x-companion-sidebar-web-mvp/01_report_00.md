### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-x-companion-sidebar-web-mvp
Worker session ordinal: 01
Worker exchange ordinal: 01
```

## 1. Terminal status and authority expiry

```text
Status: PASS
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Report justification: new-evidence
FrameNest mutation: none
AP mutation: none
Frozen plan changes: none
Planning cycle effect: none
Automatic targeted revisions used: 0
This repair consumed no second planning cycle and changed no frozen decision.
```

This file is the missing exchange-01 companion for the frozen Native Plan at `/home/agile/.cursor/plans/sidebar_web_mvp_3b064dd6.plan.md`. Exchange 02 granted report-rendering-only authority. It did not reopen planning, did not revise architecture, and did not authorize implementation.

Planning authority from `01_planning_00.md` expired when exchange 01 stopped without this report. Report-rendering authority from `01_planning_01.md` expires on submission of this file. Plan UI approval, `Approve`, `Yes`, `Build`, `Continue`, or this repair do not grant implementation authority.

```text
Start commit (FrameNest): cdb868913a6cee1ef5d801381c38fba58b1b2699
End commit (FrameNest): cdb868913a6cee1ef5d801381c38fba58b1b2699
Changed files (FrameNest/AP): none
Changed files (Meta): projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/01_report_00.md (create; this report)
Tests and validation: read-only repository re-gate and Save-freeze spot-check; no Python, no node --test, no NUC, no signed-in X
Commit and push: not authorized; not performed
```

## 2. Capability handshake

```text
Requested route: current-worker-session, Native planning mode not-used, Extra High, no Max, no NUC, no signed-in X, no provider, read-only FrameNest, Meta report write only
Client and Worker surface: Cursor Worker chat
Model: Extra High reasoning requested; model identity is not self-verified from this prompt. Client-presented identity in this session is Cursor Grok 4.6.
Reasoning effort: extra-high requested because the whole crosses MV3 side-panel hosting, Tailscale Serve identity in an iframe, postMessage spoofing, Gallery thaw in extension context, and reuse of the existing attach pipeline without becoming a generic proxy
Permission mode: Agent mode observed (Plan Mode exited); Native planning mode not-used as routed
Enhanced or maximum mode: not requested; never inferred
Automatic model selection: off; no silent weaker fallback observed
Worker session target: current-worker-session (repair of session 01)
Independence requirement: no
Sub-agents or internal delegation: not-used
Worker topology: single-active
Development envelope activation: not-used
```

Separated:

- **Requested:** Extra High; Native planning mode not-used; current-worker-session; report file only.
- **Directly observed:** Agent mode (system reminder: previous Plan Mode exited); write of this exact Meta path; FrameNest/AP/Meta read-only git and file inspection; `01_report_00.md` absent before this write.
- **Inferred:** Extra High was applied as requested; not independently attested from inside this process.
- **Unknown / not observably exposed:** whether a client reasoning slider was set to Extra High; credentials; NUC live state; Brave/X profile state; live Tailscale Serve response headers.

Native Plan Mode is not on. Extra High was requested and was not silently replaced with a weaker named route. No Max. Capability does not grant authority.

## 3. Exact baseline and evidence ledger

Classified separately:

| Surface | Classification | Evidence |
|---|---|---|
| FrameNest local | matches expected | `/home/agile/Projects/framenest`, branch `feat/x-meme-browser-companion`, HEAD `cdb868913a6cee1ef5d801381c38fba58b1b2699`, parent `ea939734558d7f5391e8d06c561a5cc46bc07b25`, tree `698d14c2a23f15228082d21e30fb46c26255f87e`, subject `fix: restore Save description and right-align companion actions`, working tree clean, origin `https://github.com/cisarik/framenest.git`, no upstream |
| FrameNest public | matches expected | `git ls-remote --heads origin main` → `bfad16b718e135b272a3b0293bb37ddc3101ba49`; no intervening public commits; no fetch |
| Pinned AP | matches expected | consumer gitlink and submodule HEAD `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`, detached HEAD accepted |
| AP public | matches pin | `git ls-remote` AP `main` `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |
| Meta local | expected dirt for this whole | HEAD `436a0107330279bc50ab118fc8452e0916136287` on `main`; untracked `01_planning_00.md` and `01_planning_01.md`; this report created after the re-gate |
| Meta public | matches local HEAD | `git ls-remote` `436a0107330279bc50ab118fc8452e0916136287` |
| NUC/production | historical, not re-probed | last companion-MVP deploy remains public `bfad16b`; empty `FRAMENEST_COMPANION_EXTENSION_ORIGINS`; empty `x_acquisition_root` |
| Browser/account | not authorized | not inspected |
| Active mutation | none owned by this Worker | FrameNest/AP clean; no implementation diff |

Save freeze (Worker 04) reconfirmed as **directly verified repository fact**:

- `extension/ui/save.html`: Description textarea `maxlength="10000"` between Title and Tags; admin button text `Save and analyze by AI`; DOM order analyze then Save; hint `Saves now. Analyze by AI is available in FrameNest after this item is cataloged.`
- `extension/ui/save.css`: `.actions { justify-content: flex-end }`
- `extension/ui/save.js`: `aliasPayload()` includes trimmed `description`; analyze click calls `submitSave()`; runtime messages remain `IDENTITY`, `CANONICAL_TAGS`, `SAVE_POST` only
- `extension/content/x_adapter.js`: Save iframe happy-path still about 360×520; Attach float untouched in this plan

Schema head remains Alembic `0029`. This whole does not invent `0030`.

`docs/AP_UPGRADE_OBSERVATIONS.md` still has untriaged `consumer-declared-execution-and-capability-route-binding`. Parked. Not edited. Not absorbed.

Parent wholes `framenest-x-meme-browser-companion-mvp` and `framenest-x-companion-save-alias-mvp` remain `not-closed`. This whole remains `not-closed`.

Claim labels used below: **repository fact**, **public fact**, **historical context**, **Cooperator decision**, **frozen-plan decision**, **inference**, **proposal**, **unresolved**, **later grant**.

## 4. Current capability and ownership map

All items are **repository fact** at HEAD `cdb8689` unless noted.

- `extension/manifest.json`: `side_panel.default_path` and `action.default_popup` are both `ui/picker.html`. Permissions: `sidePanel`, `storage`. Optional: `downloads`, `https://*.ts.net/*`. No X host permission. WAR: picker + save HTML/CSS/JS to `https://x.com/*` and `https://twitter.com/*` only. Committed public `key` pins unpacked origin `chrome-extension://omiihmnlkmieaafaphohakcgmbggppap`.
- `extension/background/service_worker.js`: `openPanelOnActionClick: true` on `onInstalled`. Service worker is the only FrameNest network client from X. `boundTabId` is assigned from any `sender.tab.id` (see section 7 honesty correction). `ATTACH_BEGIN` fetches `pathFor("content")` on the stored origin, 32 MiB cap, port `framenest-attach`, `fallbackDownload` only on oversize. Origin configure/reset, picker query, and content fetch already exist.
- `extension/ui/picker.js` `renderPreview()` sets `#preview-title` text only (`item.display_title || item.media_id`). `#preview` has title, prev/next, Attach — no `<img>` / `<video>`.
- `extension/shared/messages.js` `pathFor("preview")` already names `/api/media/{mediaId}/locations/{locationId}/gallery-preview` and is unused by `picker.js`.
- Gallery card bottom-right in `src/framenest/adapters/api/web/app.js` `renderCatalogCard` is `<a class="catalog-card__action--open-original">` to `mediaContentUrl`, title “Open original media”. `downloadIcon()` is defined and unused. `.catalog-card__action--download` CSS exists and is unused by that overlay.
- Application code sets neither `X-Frame-Options` nor `frame-ancestors` (repository-wide grep: no matches). Framing against live Tailscale Serve / Brave remains **unresolved** until the named Cooperator probe.
- Gallery still shows canonical `display_title`. Overlay tables exist (ADR-0062 / migration `0029`). Alias editor is backlog.
- ADR-0062 Save-popup Cancel sentence is stale relative to Worker 03/04. Historical ADR text. Do not edit 0062.
- `RoutePolicy.companion_mutation` is true only for `POST /api/x/requests` and `POST /api/x/requests/{claim_id}/retry` (`tests/contract/test_x_route_policy.py`, `tailscale_ingress.py`).
- Gallery preview derivative is JPEG (`GALLERY_PREVIEW_ALGORITHM_VERSION = "gallery-preview-jpeg-v1"`, `GALLERY_PREVIEW_MEDIA_TYPE = "image/jpeg"`).
- In-page Attach popup iframe max height is 420 (`x_adapter.js`). Save iframe remains ~360×520. Attach float from `c5904b4` is frozen.

The side panel does **not** already host FrameNest web. The picker does **not** already render memes. Gallery does **not** already display per-user aliases.

## 5. Selected product slice

**Frozen-plan decision** / **Cooperator decision**. One bounded closure path.

### In scope

| Surface | Role |
|---|---|
| A Save popup | Frozen at Worker 04. Not restyled. Description kept. Analyze execution remains backlog. |
| B In-page Attach / Search memes | Compact quick attach. Render the selected hit as one JPEG preview at a time. Arrows cycle the current hit list. Keep Search memes, kind filter, Attach, Settings / origin Connect. Do not replace this popup with the full website. Do not inject Attach into the X text row. |
| C Side panel / toolbar | Replace the picker clone with the complete FrameNest website at the stored Tailscale origin. First-run Connect/Reset remains in the shell. Toolbar opens the side panel (`openPanelOnActionClick`); remove `action.default_popup`. |
| Gallery Attach | Only when FrameNest web is companion-hosted: replace the bottom-right open-original control with an Attach emoji that uses the existing SW attach pipeline. Ordinary tabs stay frozen. |
| Overlay | ADR-0062 remains. Canonical `media_metadata` is not an ordinary-user write path. |

### Parked (section 12.2 still visible; not first Implementation Worker)

1. Gallery per-user alias editor (`framenest-gallery-per-user-alias-editor-mvp`).
2. Settings → General → Language (`framenest-settings-general-language-mvp`).
3. Analyze by AI execution after catalog.
4. Picker / Gallery reading the caller’s alias (still canonical `display_title`).
5. Static X photographs; per-asset Save targeting; NUC `FRAMENEST_COMPANION_EXTENSION_ORIGINS` and `x_acquisition_root`; Save-alias independent INFOSEC R3; push / publication of `feat/x-meme-browser-companion`; Web Store packaging / rotating the extension key; AP upgrade ledger; closing parent wholes; desktop app, Cover Studio, collections, sync, second-copy backup; persistent AI drafts as a product; public Internet / VPS; signed-in X scraping, DMs, cookies.

## 6. Selected hosting architecture

**One selected path:** thin MV3 extension shell + iframe of the stored Tailscale origin after origin grant.

1. New `extension/ui/sidebar.html|js|css` as `side_panel.default_path`. **Proposal** owned by later implementation; MV3-legal because `default_path` must be a local extension resource (Chrome `chrome.sidePanel` reference, retrieved 2026-08-17: “This must be a local resource within the extension package”).
2. Remove `action.default_popup`. Keep `chrome.sidePanel.setPanelBehavior({ openPanelOnActionClick: true })` on `onInstalled` **and** service-worker startup. Chrome side-panel guidance: a defined `default_popup` takes priority over `setPanelBehavior`. **Public fact** from Chrome docs, 2026-08-17.
3. Empty `frameNestOrigin`: shell shows Connect/Reset (first-run). Iframe `src` is set only after successful `CONFIGURE_ORIGIN` (existing exact-origin optional host grant `origin + /*`) and `acceptFrameNestOrigin`.
4. Shell is **not** WAR. Do not add FrameNest web HTML to WAR. Do not broaden WAR matches.
5. No `externally_connectable`. Chrome docs: that key exposes `chrome.runtime.sendMessage` to every matching web origin. A `*.ts.net` match would be broader than the stored FrameNest origin. Parent-shell `postMessage` is the tighter path.
6. No sandbox page. Sandboxed pages lose `chrome.*`. Default MV3 `extension_pages` CSP is `script-src 'self'; object-src 'self'` without `default-src` / `frame-src`, so an https iframe is allowed (Chrome Manifest CSP reference, 2026-08-17). Do **not** add manifest `frame-src https://*.ts.net`: CSP `*` matches one DNS label, while Serve origins are `https://<node>.<tailnet>.ts.net`. Control is the JS origin allowlist, not a broken CSP wildcard.
7. Identity: FrameNest has no application session cookies (ADR-0048). Tailscale Serve injects `Tailscale-User-Login` / `Tailscale-User-Name` / `Tailscale-User-Profile-Pic` on tailnet requests and strips inbound spoofed copies (official Serve docs, retrieved 2026-08-17). Chrome “Storage and cookies”: if a `chrome-extension://` page includes an iframe and the extension has host permissions for that site, the embedded site gets its top-level storage partition; third-party cookies are not blocked in subframes of a `chrome-extension://` page. After Connect, the iframe document should authenticate the same way a normal tab does. **Residual:** Brave Shields may still block the iframe — named Cooperator probe, not a silent new-tab fallback.
8. If Serve, CSP, or Brave blocks the iframe: the shell shows an honest error. A new tab is not the side panel. No CORS. No `all_urls`. No stripping of security headers.

Named Cooperator probe (**later grant**, not this exchange, not run):

```text
# [MacBook / fish]
curl -sI https://<node>.<tailnet>.ts.net/ | string match -ri '^(HTTP/|x-frame-options|content-security-policy)'
#------------------------------------------------------
```

Framing unknown is an allowed named residual. It does not block architecture selection.

Brave: official Brave documentation states MV3 extensions work as in Chrome (Brave “Can I use extensions in Brave?”, retrieved 2026-08-17). Side-panel + iframe behavior under Shields remains **unresolved** until probe or visual acceptance.

### Rejected alternatives (stay rejected)

- Keeping the side-panel picker clone.
- Putting the full FrameNest website into the in-page Attach popup.
- CORS.
- `all_urls`.
- Content-script FrameNest or `pbs.twimg.com` fetch.
- `externally_connectable`.
- Treating a new tab as the side panel if the iframe is blocked.
- Adding a second Gallery Attach button beside open-original.
- Expanding `companion_mutation` onto Gallery or analysis routes.
- Sandbox page (loses `chrome.*`).
- Editing ADR-0061 or ADR-0062 in place.
- Restoring Share-row Save or injecting Attach into the X text row.

## 7. Bridge

New postMessage channel **`v: "framenest.companion.web.v1"`**. Do not mix with X/extension `framenest.companion.v1`.

| Type | Direction | Purpose |
|---|---|---|
| `WEB_READY` | web → shell | iframe announces readiness; `targetOrigin` is the pinned extension origin |
| `HOST_HELLO` | shell → web | shell proves it is the companion host |
| `HOST_ACK` | web → shell | web accepted the pin |
| `ATTACH_REQUEST` | web → shell | UUID `mediaId` + `locationId` only |
| `ATTACH_RESULT` | shell → web | success or fail-closed error, including `composer_unbound` |

Origin checks:

- Web (`companion_host.js`) sends `WEB_READY` only when `parent !== window`, with `targetOrigin = chrome-extension://omiihmnlkmieaafaphohakcgmbggppap` (pin from the committed manifest `key`; not a secret).
- Shell accepts only `event.source === iframe.contentWindow` and `event.origin === stored frameNestOrigin` after `acceptFrameNestOrigin`.
- Web sets `companionHosted = true` **only** after `HOST_HELLO` whose `event.origin` equals the pinned extension origin.
- `?companion=1`, `parent !== window` alone, and a random https parent are insufficient. A random page cannot spoof `event.origin` as the pinned `chrome-extension://` origin.

Attach authorization:

- `ATTACH_REQUEST` carries only UUID `mediaId` and `locationId`.
- Shell forwards existing `TYPES.ATTACH_BEGIN` over `chrome.runtime.sendMessage`.
- Service worker builds the URL solely via `pathFor("content")` on the stored origin. The web cannot ask the SW to fetch arbitrary URLs.
- Audience matches today’s picker: 32 MiB, port `framenest-attach`, fill composer file input, never click Post, no new `companion_mutation` on GET content.

Bound-tab rule and **honesty correction** (does not change architecture):

The frozen plan’s phrase that `boundTabId` “already binds only from the content-script sender” is imprecise. Live `extension/background/service_worker.js` is:

```text
if (sender && sender.tab && typeof sender.tab.id === "number") {
  boundTabId = sender.tab.id;
}
```

**Repository fact:** any protocol message with a numeric `sender.tab.id` overwrites `boundTabId`, not only content-script senders. Side-panel and other extension pages typically have no `sender.tab`, so they do not overwrite today. That is live-code fact, not a proven allowlist.

**Fail-closed rule (frozen):** extension-page messages must not overwrite `boundTabId`. If no bound X composer tab exists, Attach returns `composer_unbound`, the UI says so, and there is no silent `fallbackDownload`.

**Implementation hardening inside the already-selected bridge slice:** add an explicit sender check (content-script / X-tab only) so a future extension page that did carry `sender.tab` cannot rebind Attach. Not a new architecture fork.

## 8. In-page picker visual preview

- Keep `ui/picker.html` as Surface B. Keep Search memes, kind filter, arrows, Attach, hamburger Settings / Connect / Reset.
- Add `<img id="preview-media" alt="">` in `#preview`. Still one result at a time. Arrows cycle the current list. No multi-card Gallery in the popup.
- New `TYPES.PREVIEW_FETCH` on `framenest.companion.v1`. Payload: UUID `mediaId` + `locationId` only.
- Service worker GET `pathFor("preview")` as binary (not `fetchJson`), modest cap about 2 MiB, response `{ mediaType, base64 }`. Prefer SW-mediated preview over content-script fetch. Do not load `pbs.twimg.com` from the adapter. Do not invent CORS so the iframe can fetch preview itself.
- Gallery preview is always JPEG (`gallery-preview-jpeg-v1`). Render as `<img>`. Video/GIF items still show the JPEG derivative, not full content playback.
- Preview failure: keep title text. Honest degradation.
- Slight increase of the in-page picker iframe height (today max 420) is in-scope. Save iframe 360×520 and Attach float remain frozen.

## 9. Gallery thaw

Detection: `companionHosted === true` only after the handshake in section 7. Ordinary browser tabs never set it.

DOM: in `renderCatalogCard`, when hosted and a supported location exists, **replace** the bottom-right `<a class="catalog-card__action--open-original">` with `<button type="button">` showing 📎, `title` and `aria-label` **Attach to X composer**, classes `catalog-card__action--overlay catalog-card__action--bottom-right catalog-card__action--attach`. `--attach` copies the existing `--open-original` tokens. No global `styles.css` restyle. `downloadIcon()` stays unused.

Default: replace, not both. Ordinary tabs keep “Open original media”.

If handshake completes after first catalog render, re-render catalog results.

Details visual behavior, alias editor, lightbulb, model dropdown, and Analyze execution stay frozen / parked.

New local asset `companion_host.js` loaded before `app.js`. `index.html` must remain free of `https://` (existing `test_root_document_references_only_local_application_assets`). Pin lives in the JS asset as `chrome-extension://…`, not in HTML.

## 10. ADR recommendation

**New ADR-0063 is required.** The side-panel web host plus `framenest.companion.web.v1` postMessage bridge plus Gallery visual thaw in extension context is a new trust surface. It is not a silent rewrite of ADR-0061 (origin trust, companion_mutation, SW-only X client) or ADR-0062 (overlay, Save popup). Accepted ADRs are not edited in place.

Next number after live `docs/adr/README.md` index ending at 0062 is **0063**. Proposed path: `docs/adr/0063-companion-side-panel-web-host.md`. Record: shell+iframe host, web bridge, Gallery Attach only when companion-hosted, zero new `companion_mutation`, WAR not broadened, `externally_connectable` rejected, CSP `frame-src https://*.ts.net` rejected, iframe-blocked fallback is honest error not a new tab. Note ADR-0062 Cancel sentence as historical stale text; do not “fix” 0062.

Claiming no new ADR would be false: this is a new trust surface.

## 11. companion_mutation and allowlist proof

**Repository fact:** flagged mutation remains exactly:

- `POST /api/x/requests`
- `POST /api/x/requests/{claim_id}/retry`

`GET /api/x/companion/media`, `GET /api/media/{id}/locations/{id}/content`, `GET /api/media/{id}/locations/{id}/gallery-preview`, and alias GET/PUT are not `companion_mutation`. Companion Origin PUT alias remains `MUTATION_ORIGIN_FORBIDDEN`.

This whole adds **zero** new flagged mutation routes. Gallery Attach and picker preview are GETs of already-unflagged content/preview on the stored origin, constructed only from UUIDs. Empty `FRAMENEST_COMPANION_EXTENSION_ORIGINS` remains fail-closed for the two flagged POSTs (historical NUC; not written here).

No CORS middleware. No allowlist change in this planning exchange or in the later first implementation whole unless a later grant says otherwise.

## 12. Threat model and residual-risk owners

INFOSEC.md activated for **planning-only** threat model. No audit execution, no finding ledger mutation, no containment action. This report does **not** self-certify.

**Assets:** Tailscale identity headers; catalog media bytes; bound X composer file input; stored `frameNestOrigin`; pinned extension origin; overlay vs canonical metadata; operator private key (gitignored; not printed).

**Actors / abuse cases:**

| Actor / case | Control |
|---|---|
| Malicious X page | Content scripts match only x.com/twitter.com; they do not `fetch` FrameNest or `pbs.twimg.com`; unknown `v`/types drop; WAR residual is picker/save only, no X cookies, talk only to SW |
| Malicious extension | Out of scope to fully defeat; pin and unpacked ID remain operator custody |
| Spoofed `postMessage` | Exact `event.origin` + `event.source` checks; distinct protocol string; `targetOrigin` never `*` for HOST_HELLO / ATTACH |
| Spoofed `companion_hosted` | Flag set only after HOST_HELLO from pinned extension origin |
| Arbitrary URL fetch via Attach | UUIDs only; `pathFor("content")` / `pathFor("preview")` reject non-UUIDs |
| Cross-origin iframe clickjacking of FrameNest | Pre-existing: app has no `frame-ancestors`. Companion Attach is not enabled without the pin. Do not add a conflicting app header before the Serve probe |
| Cookie / identity leakage | No app session cookies; Serve identity is per-request headers; shell does not read iframe `document.cookie`; SW fetch uses stored origin + `X-FrameNest-Request: 1` |
| Log leakage | Do not log identity headers, media bytes, private URLs, or the private key |
| Unbound composer | `composer_unbound`; no silent download |
| XSS in FrameNest web | Can at most request attach of UUID catalog items already visible to that identity; still cannot fetch arbitrary URLs |

**Trust boundaries:** X page | content script | SW | extension shell | iframe (Tailscale web origin) | FrameNest Unix-socket ingress | catalog/media filesystem.

**Tests that later own regressions:** extension `node --test`, MiniDom handshake tests, Gallery ordinary-tab freeze tests, route-policy companion_mutation set equality, WAR resource list, `script_srcs` local-asset contract. Dynamic signed-in X is not a repository gate.

**Residual-risk owner:** Cooperator (Michal) for unpublished branch, framing unknown, Brave Shields, bound-tab requirement, empty NUC allowlist, WAR residual, canonical titles until a later whole.

**Independent acceptance:** `required-separate-fresh-worker`. **INFOSEC route R3** for the later implementation whole (new postMessage trust surface + Gallery thaw in extension context; novel attack surface). This planning report does **not** certify that future acceptance.

## 13. Tests and verification ladder (later slices)

This exchange ran no tests. Later implementation:

- **Inspection and provenance:** required.
- **Extension `node --test`:** `tests/x_companion_extension.test.js` (WAR still picker+save only and must not include sidebar; no `all_urls`; `PREVIEW_FETCH` added; `default_popup` removed; `side_panel.default_path` is sidebar; origin pattern unchanged). New MiniDom / `node --test` owner `tests/companion_web_bridge.test.js` (name may be refined) for handshake origin checks, UUID-only attach, spoofed parent rejected, ordinary `companionHosted=false`.
- **Web:** `tests/catalog_card_ai_quick_action.test.js` ordinary path still has open-original; hosted path has Attach and not both. `tests/contract/test_local_web_application.py` `script_srcs` includes `/assets/companion_host.js` then `/assets/app.js`; HTML still has no `https://`. `tests/gallery_still_image_render.test.js` / `tests/cover_frontend.test.js` only if Gallery card DOM for ordinary tabs would change (it must not).
- **Python via `./.ap/ap exec --root /home/agile/Projects/framenest --baseline <exact HEAD> --operation test-focus`:** `tests/contract/test_x_route_policy.py` (still exactly two companion_mutation routes), `tests/contract/test_gallery_preview_api.py`, `tests/contract/test_tailscale_ingress_security.py` as needed. Ambient Python forbidden.
- **`tests/browser_companion_evidence.test.js`:** inspect; do not run signed-in X. Loopback synthetic evidence only if a later grant sets `FRAMENEST_RUN_BROWSER_EVIDENCE=1`.
- **Michal visual acceptance:** Reload unpacked, then refresh X; step-by-step; separate from repository tests, publication, and NUC.
- **Broad/full suite:** not required for this whole’s first implementation unless a slice proves otherwise.
- **Causal invariants later tests must own:** three surfaces remain distinct; handshake cannot be spoofed by random https; Attach cannot fetch arbitrary URLs; extension-page messages do not overwrite `boundTabId`; ordinary-tab Gallery unchanged; WAR not broadened; zero new `companion_mutation`; Save freeze; Attach float freeze.

## 14. Exact proposed paths and owner map

### New

| Path | Owner |
|---|---|
| `extension/ui/sidebar.html` | Side-panel shell document; Connect/Reset; iframe host |
| `extension/ui/sidebar.js` | Origin grant, iframe `src` allowlist, `postMessage` bridge, `ATTACH_BEGIN` forward |
| `extension/ui/sidebar.css` | Shell chrome only |
| `src/framenest/adapters/api/web/companion_host.js` | Handshake, `companionHosted`, `ATTACH_REQUEST` |
| `docs/adr/0063-companion-side-panel-web-host.md` | New trust-surface ADR |
| `tests/companion_web_bridge.test.js` | Handshake / spoof / UUID-only tests (name refinable) |

### Changed

| Path | Change |
|---|---|
| `extension/manifest.json` | `side_panel.default_path` → sidebar; remove `default_popup`; do not add WAR or `externally_connectable` |
| `extension/background/service_worker.js` | `PREVIEW_FETCH`; `setPanelBehavior` on startup; explicit `boundTabId` sender hardening; no new mutation routes |
| `extension/shared/messages.js` | `PREVIEW_FETCH` on `framenest.companion.v1` |
| `extension/ui/picker.html\|js\|css` | One `<img>` preview via SW |
| `extension/content/x_adapter.js` | Slight picker iframe height only; Save size and Attach float frozen |
| `src/framenest/adapters/api/web/app.js` | Hosted Gallery Attach replace |
| `src/framenest/adapters/api/web/index.html` | Load `companion_host.js` before `app.js`; no `https://` |
| `src/framenest/adapters/api/web/styles.css` | `--attach` token copy only |
| `src/framenest/adapters/api/application.py` | `_ASSET_MEDIA_TYPES` entry for `companion_host.js` |
| `docs/X_COMPANION.md` | Side panel hosts real web; picker is quick attach with preview |
| `docs/adr/README.md` | Index 0063 |
| `tests/x_companion_extension.test.js` | Manifest/WAR/preview/popup assertions |
| `tests/catalog_card_ai_quick_action.test.js` | Ordinary freeze + hosted Attach |
| `tests/contract/test_local_web_application.py` | `script_srcs` |

### Untouched

Save HTML/CSS/JS; overlay schema / Alembic `0029`; `companion_mutation` table contents; WAR resource list except the proof that sidebar is absent; ADR-0061 and ADR-0062 bodies.

## 15. Causal implementation slices and later grants

Later Implementation Worker only. Separately grantable. This report authorizes none of them.

1. **Host shell.** Sidebar pages, Connect/Reset, iframe after origin grant, remove `default_popup`, `openPanelOnActionClick` on install and SW startup, WAR/manifest tests. Observable: empty origin shows Connect; granted origin attempts iframe. If iframe blocked: honest error, stop for new grant — do not open a tab.
2. **Bridge + Gallery Attach.** `companion_host.js`, handshake, replace open-original when hosted, `ATTACH_BEGIN` reuse, `boundTabId` sender hardening, MiniDom tests without signed-in X. Observable: hosted Gallery 📎; ordinary tab unchanged; unbound composer reports `composer_unbound`.
3. **Picker preview.** `PREVIEW_FETCH`, JPEG `<img>`, arrows, title fallback, modest iframe height. Observable: first hit draws; arrows cycle; Attach still works.
4. **ADR-0063 + `docs/X_COMPANION.md`.** Operator-visible truth. No NUC write.

**Later grants, not this whole’s first implementation prompt:**

- Independent acceptance: `required-separate-fresh-worker` after implementation exists.
- INFOSEC R3: later, not self-certified here.
- Publication / push of `feat/x-meme-browser-companion`.
- NUC: companion-origin allowlist, `x_acquisition_root`, `framenest-release`.
- Cooperator framing probe (section 6).
- Backlog wholes in section 5 parked list.

Candidate topology for implementation: canonical checkout `/home/agile/Projects/framenest` on `feat/x-meme-browser-companion` unless a later prompt proves otherwise. Baseline at this report: `cdb868913a6cee1ef5d801381c38fba58b1b2699`.

## 16. Recommended next Worker route

```text
Worker session target: fresh-worker-session
Native planning mode: not-used
Reasoning: Extra High unless a later Orchestrator names Medium/High with a reason
Independence: not for implementation; required-separate-fresh-worker for later acceptance
INFOSEC: R3 recommended for the implementation whole; not executed in that first implementation session unless the prompt activates audit
NUC: not activated
Push / publication: not activated
First allowlist: slices 1–4 paths in section 14; Save freeze; Attach float freeze; no CORS; no all_urls; no companion_mutation expansion; no ADR-0061/0062 in-place edits
Python evidence: ./.ap/ap exec --root /home/agile/Projects/framenest --baseline <exact authorized HEAD> --operation test-focus
```

Do not treat this planning report as that implementation prompt.

## 17. Parked scope, unresolved facts, stop conditions

Parked: section 5 parked list (original prompt section 12.2) remains visible.

Unresolved:

- Live Serve/Brave `X-Frame-Options` / `Content-Security-Policy` on the operator origin (named probe).
- Brave Shields iframe behavior.
- Whether a given Brave build treats the side panel as a `chrome-extension://` top-level page for cookie partitioning (Chrome docs language says “tab”; side panel is an extension page — identity still rests primarily on Serve headers, not cookies).

Stop conditions for a later Implementation Worker: dirty unexplained FrameNest tree; Save freeze broken; public `main` material to this UX; request to use a new tab as the side panel; request to add CORS/`all_urls`/content-script fetch; request to thaw ordinary-tab Gallery; iframe blocked without a new grant.

## 18. Smallest next Orchestrator action

One decision only: **accept or reject this frozen architecture as rendered here** (including the `boundTabId` honesty correction and named framing probe as residual, not as a silent architecture change). Acceptance still does not start implementation. Implementation requires a new complete `fresh-worker-session` prompt with `Native planning mode: not-used`.

## 19. Near-misses and pre-existing classification

```text
Resolved Execution Issues / Near-Misses: Exchange 01 froze a decision-complete Native Plan UI artifact and stopped without writing this AP terminal report. Cause: Native Plan Mode UI was treated as sufficient. Resolution: exchange 02 rendered the frozen plan into this file without re-planning or mutating FrameNest. Residual: Plan UI approval still must not be mistaken for implementation authority.
Pre-Existing Failure Classification: none
```

Historical context only: Meta commit `436a0107` subject/body mention a Save-popup Worker 05 that does not exist. Tree added this whole’s `00_handout.md`. Not repaired here.
