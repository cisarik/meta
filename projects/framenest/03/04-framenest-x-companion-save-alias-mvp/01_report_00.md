### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-x-companion-save-alias-mvp
Worker session ordinal: 01
Worker exchange ordinal: 01

## 1. Terminal status and authority expiry

**PASS.** One architecture is selected: name-before-catalog Save popup, pending alias on the X claim, per-user overlay after `media_id`, no ordinary-user write into canonical `media_metadata`, and no expansion of `companion_mutation` beyond the two existing X POST routes. Every material decision is resolved to an exact owner, path, and interface, or to a named later grant. No FrameNest or AP file was edited, created, deleted, renamed, formatted, or generated. No Git write, dependency change, provider contact, signed-in X access, browser-profile access, NUC access, SSH, sudo, publication, or production mutation was performed. The only write is this report.

Planning authority granted by prompt `FN-X-COMPANION-SAVE-ALIAS-PLAN-01` is expired by this terminal report. Plan UI approval is a decision only and does not grant implementation authority.

```text
Status: PASS
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Start commit (FrameNest): c5904b47914fe376733e50ca8d0f4b9173dadb22
End commit (FrameNest): c5904b47914fe376733e50ca8d0f4b9173dadb22
Changed paths: /home/agile/meta/projects/framenest/03/04-framenest-x-companion-save-alias-mvp/01_report_00.md (create; planning report only)
Validation: inspection and provenance; no Python, no `node --test`, no NUC, no browser
Authorized Git result: none (FrameNest none; AP none; Meta untracked report only; no stage/commit/push)
Deviations: none that change the selected architecture
Material risks: residual WAR fingerprinting; unpublished feature branch vs NUC on public main; Gallery remains canonical
Missing evidence: none that blocks architecture selection
Smallest next step: Orchestrator presents this plan to Michal for accept-or-revise; do not issue an implementation prompt until that decision
Report justification: new-evidence
Authority expiry: this terminal report expires the current planning authority
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
Independent acceptance: not-required (this planning exchange)
Evidence tier: E0
Activated stricter profile: INFOSEC.md planning-only threat model; no audit execution, no finding ledger, no containment
```

Parent whole `framenest-x-meme-browser-companion-mvp` remains not-closed. This whole is also not-closed.

## 2. Capability handshake

Requested route (Orchestrator recommendation, Cooperator-selected by the handoff):

```text
Recommended route: fresh-worker-session, Native planning mode required, Extra High, no Max, no NUC, no signed-in X, no provider, read-only FrameNest, Meta report write only
Client and Worker surface: Cursor Worker chat
Model: Extra High reasoning requested; model identity is not self-verified from this prompt
Reasoning effort: extra-high
Permission mode: requested Plan Mode on
Native planning mode: required
Enhanced or maximum mode: not requested; never infer Max
Automatic model selection: off; no silent weaker fallback
Worker session target: fresh-worker-session
Independence requirement: no for this planning exchange
Sub-agents or internal delegation: not-used
Worker topology: single-active
```

Directly observed:

- Client surface is a Cursor Worker chat. Native Plan Mode produced a frozen planner artifact; this exchange renders that architecture into the required AP terminal report. No implementation mutation occurred.
- This assistant is identified in the client as Cursor Grok 4.6. That label is not an independent attestation of Extra High, Max, or a specific reasoning-budget measurement.
- Extra High / Max / automatic weaker fallback were not observably switched as a routing change inside this session.
- NUC, provider, signed-in X, and browser-profile surfaces were not activated.
- Sub-agents were not used.

Inferred: Plan Mode was on for the planning cycle because a Native Plan artifact existed and the Cooperator attached it as the execute-report signal.

Unknown / not observably exposed: exact reasoning-token budget; whether the client billed Extra High; credential stores; Brave profile state; NUC live state.

Capability does not grant authority. Requested Extra High was treated as available enough to complete planning; it is not self-certified. Native Plan Mode was used for the one authorized planning cycle and is not an implementation grant.

## 3. Exact baseline and evidence ledger

Baseline gate (read-only; `git rev-parse`, `git status`, `git log`, `git ls-tree`, `git ls-remote`; no fetch):

| State | Result | Classification |
| --- | --- | --- |
| FrameNest local | `/home/agile/Projects/framenest`, branch `feat/x-meme-browser-companion`, HEAD `c5904b47914fe376733e50ca8d0f4b9173dadb22`, parent `3e354b0785556235d26943470689a7bd0bddbb9d`, tree `ef57b08190521943557f3944eeade4207d8ba85a`, subject `fix: float reply Attach instead of injecting into the X text row`, working tree clean, no upstream | directly verified repository fact |
| FrameNest public `main` | `git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` → `bfad16b718e135b272a3b0293bb37ddc3101ba49` (unchanged vs restore) | directly verified public fact |
| Pinned AP | consumer gitlink `160000 commit 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`; submodule HEAD same; detached HEAD accepted; submodule status clean | directly verified repository fact |
| AP public `main` | `git ls-remote https://github.com/cisarik/ap.git refs/heads/main` → `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | directly verified public fact |
| Meta local | `/home/agile/meta`, branch `main`, HEAD `2e19f6be19b9f8e7ff513907bf533db237820ec4`, `ahead 3` of `origin/main` | directly verified repository fact |
| Meta public `main` | `07ccbbe0baa9c1955935fafe00b57f86ac7889be` | directly verified public fact |
| Meta untracked | parent-whole 06–12 pairs plus `00_handout_01.md`; this whole directory including `00_handout.md` and `01_planning_00.md` | directly verified repository fact; historical trace debt; not FrameNest contamination |
| NUC / production | not re-probed; parent-whole Worker 05 historical: public `bfad16b`, empty companion allowlist, empty `x_acquisition_root` → 503 | historical context |
| Browser / account | not authorized | not probed |
| Active mutation owned by this Worker | none in FrameNest/AP; this report file only | directly verified |

Public `main` did not advance past `bfad16b`. No intervening public commits to inspect. All gate states are non-contradictory. `00_handout.md` in this whole was not executed and was not overwritten.

Directly verified repository sources (read at the cited symbol, not merely listed):

- `.ap/AP.md`, `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md`, `.ap/INFOSEC.md` §3 and §5
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`
- `docs/AP_UPGRADE_OBSERVATIONS.md` header only (untriaged `consumer-declared-execution-and-capability-route-binding`; parked; not edited)
- `PRODUCT.md` §9 (server authoritative for canonical title/description/tags and per-user visibility)
- `docs/adr/0023-manual-first-metadata-and-multi-model-ai-drafts.md`, `0027-persistent-display-title-and-canonical-tags.md`, `0049-durable-content-publication-boundary.md` (per-user visibility still deferred), `0061-x-meme-browser-companion.md`
- `docs/X_COMPANION.md`, `docs/adr/README.md` (0061 is current last ADR; in-place supersession rule)
- `src/framenest/domain/identity_access.py` (ordinary capabilities; no `metadata.canonical.write`, no `analysis.run`)
- `src/framenest/domain/media_metadata.py` (`MAX_DISPLAY_TITLE_CODE_POINTS = 240`, `MAX_DESCRIPTION_CODE_POINTS = 10000`, `MAX_MEDIA_TAGS = 32`, `CanonicalTagKey`, `MediaDisplayTitle`, `MediaDescription`)
- `src/framenest/adapters/api/tailscale_ingress.py` (`companion_mutation=True` only at POST `/api/x/requests` and retry; `_mutation_origin_allowed`; unsafe-method Origin + `X-FrameNest-Request: 1`)
- `src/framenest/adapters/api/x_request_api.py` (`XRequestCreateBody` is `{ url }` with `extra=forbid`; retry has no body)
- `src/framenest/adapters/api/media_metadata_api.py` (GET/PUT `/api/media/{media_id}/metadata`; GET/POST `/api/canonical-tags`; audience 404)
- `src/framenest/application/content_publication.py` (`ContentAudiencePolicy.may_read`: published or admin workflow or live requester X/YouTube access)
- `src/framenest/application/x_acquisition.py` (`submit` reuse / `active_reuse` / `new`; `_complete_asset`; `_imported_display_title`; `DUPLICATE_PENDING` → `X_CATALOG_HANDOFF_FAILED`)
- `src/framenest/adapters/api/application.py` (X coordinator only when `x_acquisition_root` set and bind host is loopback)
- `src/framenest/infrastructure/persistence/alembic_environment/versions/0028_x_requester_acquisition.py` (schema head; `title` is tweet title; `ck_x_post_claims_created_by_login_key`)
- `src/framenest/infrastructure/persistence/catalog_schema.py` (`media_metadata` PK `media_id`; description 1–10000)
- `src/framenest/infrastructure/persistence/catalog_removal_repository.py` (`_delete_metadata_graph`)
- `src/framenest/infrastructure/persistence/x_acquisition_claim_repository.py` (`has_live_requester_media_access`)
- `extension/manifest.json` (WAR picker only; committed public `key`; unpacked origin already documented)
- `extension/shared/messages.js` (`SAVE_POST`, `pathFor("canonicalTags")` already mapped, no `CANONICAL_TAGS` type)
- `extension/background/service_worker.js` (`savePost` POSTs `{ url }`; `fetchJson` sets `X-FrameNest-Request: 1`)
- `extension/content/x_adapter.js` (`createSaveControl` click → silent `SAVE_POST`; failed state is plus + danger border, not ×; Attach closed-shadow iframe)
- `extension/ui/picker.html|css|js` (picker talks to SW via `chrome.runtime.sendMessage`)
- `src/framenest/adapters/api/web/index.html` (workspace labels Title, Description, Tags, Analyze by AI)
- Tests: `tests/contract/test_x_route_policy.py`, `test_tailscale_ingress_security.py`, `test_x_request_api.py`, `tests/x_companion_extension.test.js` (asserts `TYPES.SAVE_POST, { url: accepted.submittedUrl }`)

Directly verified public/primary sources (retrieval date 2026-08-17):

- [Chrome cross-origin network requests](https://developer.chrome.com/docs/extensions/develop/concepts/network-requests) — content-script fetch is page-origin; SW fetch needs host permissions; do not let content scripts specify arbitrary URLs
- [Chrome web-accessible resources](https://developer.chrome.com/docs/extensions/reference/manifest/web-accessible-resources) — WAR is opt-in; matching origins may iframe; `use_dynamic_url` uses a session-dynamic resource ID
- [Chrome content scripts](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts)
- [Chrome MV3 service workers](https://developer.chrome.com/docs/extensions/develop/migrate/to-service-workers) — ephemeral SW; persist via `chrome.storage`
- [chrome.storage](https://developer.chrome.com/docs/extensions/reference/api/storage) — `storage` permission already declared; SW cannot rely on `window.localStorage`
- [Tailscale Serve identity headers](https://tailscale.com/docs/features/tailscale-serve) — Serve strips and reinjects `Tailscale-User-Login` / `Tailscale-User-Name`; Funnel does not; listen on localhost
- [Brave MV3 / Shields](https://brave.com/blog/brave-shields-manifest-v3) — Brave remains Chromium-extension compatible for MV3; unpacked MV3 load is the accepted companion path

Issuance-time anchors 1–17 revalidated: all hold. Overlay tables still absent. Schema head remains `0028`.

## 4. Current capability and ownership map

Canonical metadata is one row per `media_id` (`media_metadata` PK). Ordinary users cannot write it. `PUT /api/media/{media_id}/metadata` requires `metadata.canonical.write`, audit `metadata.save`, and is **not** `companion_mutation`. Companion Origin therefore receives `MUTATION_ORIGIN_FORBIDDEN` (403) on that PUT. GET metadata uses `gallery.read` plus `ContentAudiencePolicy` (published, or admin `media.workflow.read`, or live requester X/YouTube access). Unpublished foreign items 404.

X submit body is only `{ url }`. `submit(url, login_key=...)` returns `reuse` (own successful claim), `active_reuse` (own in-flight claim), or `new`. Tweet/claim `title` is copied into canonical `display_title` by `_imported_display_title` during catalog classification. That path is canonical import, not a user alias.

`companion_mutation` is true solely for `POST /api/x/requests` and `POST /api/x/requests/{claim_id}/retry`. GET routes, including `GET /api/canonical-tags` (`gallery.read`) and `GET /api/x/companion/media`, are not origin-gated by the companion allowlist. Unsafe methods still require exact `Origin` (web `external_origin` or flagged companion origin) and `X-FrameNest-Request: 1`. Empty `companion_extension_origins` remains fail-closed. No CORS.

Hover `+` still calls `SAVE_POST` with `{ url: accepted.submittedUrl }` immediately. Failed Save already uses the plus glyph plus `#ff4d4d` border and `title`/`aria-label`; it does not use a red × (`tests/x_companion_extension.test.js`). Attach popup is live-accepted (`c5904b4`): closed shadow + iframe `ui/picker.html`, `position: fixed` on `document.documentElement`. Picker iframe is extension-origin WAR and talks only to the service worker via `chrome.runtime.sendMessage`.

Ordinary role: `gallery.read`, `media.original.read`, `media.download`, `upload.submit`, `youtube.request`, `x.request`. Not `metadata.canonical.write`, not `analysis.run`. Analyze by AI in `web/index.html` is gated on `analysis.run`.

`DUPLICATE_PENDING` currently fails the X asset with `X_CATALOG_HANDOFF_FAILED`. No overlay can apply without `media_id`. Parked.

No `media_user_aliases` table exists. ADR-0049 per-user Hide/Trash is a different deferred concept and must not be reused as an alias store.

## 5. Selected product slice

**In-scope for the later implementation Worker (one whole, separately granted):**

1. Popup 1 Save / Add to FrameNest: click hover `+` opens an in-page dialog (Title, Description, Tags, Save, Cancel) in the language of the web metadata workspace. Cancel does not submit. Save then submits.
2. Per-user alias overlay (title, description, existing canonical tag keys) keyed by `(media_id, login_key)`.
3. Pending alias on the X claim so naming happens before `media_id`.
4. Apply pending overlay on cataloged `media_id` and on `reuse` of an already-successful own claim. Do not change `_imported_display_title`.
5. New ordinary capability `metadata.alias.write`. GET/PUT `/api/media/{media_id}/alias` for Tailscale web origin. Companion does **not** call PUT alias in this whole.
6. Optional `alias` object on existing `POST /api/x/requests` under existing capability `x.request`. `companion_mutation` set unchanged.
7. ADR-0062 (overlay) plus a non-superseding bounded clarification of ADR-0061 (Save WAR + optional alias on the already-flagged POST).
8. Operator/product docs for the Save popup and overlay contract. Tests named in section 14.

**Parked / later grants (not this implementation Worker):**

| Item | Disposition |
| --- | --- |
| NUC `x_acquisition_root` + companion origin allowlist | later ops grant; empty allowlist stays fail-closed |
| Static X photographs (`yt-dlp==2026.7.4` photo filter → `X_NO_SUPPORTED_MEDIA`) | later pin/extractor whole |
| Per-asset Save targeting | parked; payload remains post permalink; one alias applied to every successful asset of the claim |
| Analyze by AI on the Save popup | rejected for this whole |
| Multi-model suggestion dropdown | parked |
| Picker search using caller alias | parked |
| Gallery / Details UX thaw to show alias | parked; they remain canonical |
| Web Details editor for the overlay | parked; API exists, UI does not change |
| AP upgrade ledger entry | parked; do not edit `docs/AP_UPGRADE_OBSERVATIONS.md` |
| Web Store, key rotation, CORS, `all_urls`, content-script fetch | rejected |
| Hide/Trash (ADR-0049) | stays deferred; not this overlay |

Four Save “failures”, classified separately:

1. Silent `SAVE_POST` — **in-scope** product defect.
2. NUC 503 (`X_REQUEST_NOT_CONFIGURED` / empty allowlist) — **parked ops**.
3. Static X photo extractor — **parked**.
4. Per-asset targeting — **parked**.

## 6. Selected lifecycle and rejected alternatives

**Selected: name-before-catalog.**

User fills Title / Description / Tags on X, clicks Save, then `POST /api/x/requests` carries `{ url, alias? }`. Pending alias is stored on the claim. After each asset reaches CATALOGED `media_id`, the overlay is upserted for `(media_id, claim.created_by_login_key)`. Canonical tweet title import remains.

Rejected wait-for-import-then-open-web-form: download may take minutes; NUC may 503; the user leaves the tweet; Analyze by AI before bytes exist would be a lie; there is no `media_id` to PUT.

```text
User → Save iframe (Title, Description, Tags, Save, Cancel)
Save → content script → SW SAVE_POST { url, alias }
SW → POST /api/x/requests (companion_mutation already true)
API persists pending alias on claim (identity login_key, never a body login_key)
Acquisition → catalog → _complete_asset media_id
Apply overlay, not canonical metadata
SW ← GET claim poll (unchanged)
```

**Rejected alternatives (with why):**

- Write aliases through canonical `PUT .../metadata`: ordinary users lack `metadata.canonical.write`; two users would overwrite one canonical row; companion Origin cannot call it under ADR-0061.
- Grant ordinary users `metadata.canonical.write` as a shortcut: violates least privilege and publication integrity.
- Broaden `companion_mutation` to `/api/media/**` or PUT alias: turns the companion into a generic metadata proxy from X.
- JSON in `x_post_claims.title`: that column is the source tweet title used by `_imported_display_title`.
- Columns on `media_metadata` for alias: PK is `media_id` only; cannot isolate two users.
- CORS, `all_urls`, content-script FrameNest or `pbs.twimg.com` fetch: Chrome docs forbid arbitrary URL fetch from content scripts; ADR-0061 already rejected this.
- Side-panel Save: Attach acceptance is in-page popup; Save must match that product language.
- Shared popup-shell extraction from Attach: not necessary (section 11).
- `use_dynamic_url` on WAR: diverges from the live-accepted picker; session-dynamic resource IDs are not required for this isolation bar. Unpacked extension origin remains the committed public `key`.
- Analyze by AI on the popup: no `media_id`, ordinary users lack `analysis.run`.
- Reopen Attach placement (`c5904b4`): Cooperator live-accepted; frozen.

## 7. Data model and migration `0029`

Schema head is `0028`. Next revision is `0029`, `down_revision = "0028"`. No backfill. Rollback drops the four new tables.

Also update `catalog_schema.py` SQLAlchemy `Table` definitions in the same slice (repositories use those objects, not Alembic SQL alone).

### `media_user_aliases`

- PK `(media_id, login_key)`
- `media_id` TEXT FK `logical_media.id` ON DELETE RESTRICT, length 36
- `login_key` TEXT NOT NULL, same checks as `ck_x_post_claims_created_by_login_key` **without** the NULL branch (length 1–254, lower, no space/TAB/LF/CR)
- `display_title` nullable, length 1–240 when present (same as canonical)
- `description` nullable, length 1–10000 when present
- `created_at_ms`, `updated_at_ms` non-negative, `updated_at_ms >= created_at_ms`
- Empty alias (all of title, description, tags absent) means **no row**

### `media_user_alias_tags`

- PK `(media_id, login_key, tag_key)`
- FK `(media_id, login_key)` → `media_user_aliases` RESTRICT
- FK `tag_key` → `canonical_tags.key` RESTRICT
- `position` INTEGER 0–31 inclusive
- UNIQUE `(media_id, login_key, position)`
- Max 32 tags per alias, unique keys (domain `MAX_MEDIA_TAGS`)

### `x_claim_pending_aliases`

- PK `claim_id` FK `x_post_claims.id` RESTRICT
- `login_key` NOT NULL, same checks, and must equal `x_post_claims.created_by_login_key` (enforced in application; optional CHECK via trigger is not required if tests own it)
- `display_title`, `description` nullable with the same limits
- timestamps

### `x_claim_pending_alias_tags`

- Analogous PK `(claim_id, tag_key)`, position 0–31, FK to pending alias row and `canonical_tags.key` RESTRICT

Catalog removal: extend `_delete_metadata_graph` to delete `media_user_alias_tags` then `media_user_aliases` for that `media_id` **before** the existing metadata graph. Overlay is not Hide/Trash. Pending rows stay on claims (claims are not deleted by catalog removal).

Do not store alias in `media_metadata`. Do not alter `x_post_claims.title`.

## 8. API, capabilities, audit, error codes

### Capability

Add `CAPABILITY_METADATA_ALIAS_WRITE = "metadata.alias.write"` to `_ORDINARY_CAPABILITIES` (and therefore also to admin). Do not add it to admin-only. Do not grant `metadata.canonical.write` to ordinary users.

### `POST /api/x/requests` (existing)

Capability `x.request`. Audit `x.request.submit` unchanged. `companion_mutation` remains true.

```text
XRequestCreateBody (extra=forbid)
  url: str
  alias: XAliasBody | omitted

XAliasBody (extra=forbid)
  display_title: str | null | omitted
  description: str | null | omitted
  tag_keys: list[str] | omitted   # max 32, CanonicalTagKey each
```

Omitted `alias` → today’s submit, no pending row. Present but empty (no title, no description, no tags) → no pending row / delete pending on that claim if last-write-wins empty. Present with fields → validate then upsert pending for this claim. `login_key` is **only** ingress identity, never a body field.

Unknown tag key → 422 `ALIAS_TAG_NOT_FOUND` (do not create canonical tags). Domain type failure → 422 `ALIAS_INVALID`. Existing X errors unchanged (`X_REQUEST_NOT_CONFIGURED` 503, `X_REQUEST_INVALID_URL` 422, limits 429, storage 507).

Retry POST body unchanged (no alias). Pending already on the claim survives retry.

### `GET /api/media/{media_id}/alias`

Capability `gallery.read`. Not `companion_mutation`. Safe method: companion Origin may call it later, but this whole’s companion does not need to. Response is **caller-private**: the overlay for `identity.login_key` only, or an empty alias object if no row. Never another user’s overlay.

Audience: same as GET metadata (published 404 for foreign unpublished) **plus** own live cataloged X `media_id` via existing `has_live_requester_media_access` (already inside `ContentAudiencePolicy`). 404 `MEDIA_NOT_FOUND` on deny (do not leak existence beyond current metadata policy).

### `PUT /api/media/{media_id}/alias`

Capability `metadata.alias.write`. Audit `metadata.alias.save`. **Not** `companion_mutation`. Companion Origin → 403 `MUTATION_ORIGIN_FORBIDDEN`. Web `external_origin` + `X-FrameNest-Request: 1` + Tailscale identity required. Same audience as GET. Body = `XAliasBody`. Empty body deletes the overlay row and tags. Unknown tag → 422 `ALIAS_TAG_NOT_FOUND`. Invalid domain values → 422 `ALIAS_INVALID`.

Why not reuse canonical PUT: ordinary users must not write canonical publication metadata; companion must not mutate `/api/media/**` as a class.

`GET /api/canonical-tags` already exists (`gallery.read`). Ordinary Save form uses it. `POST /api/canonical-tags` stays admin `metadata.canonical.write`.

## 9. Companion trust, ADR, WAR residual

`companion_mutation` membership **does not change**. Optional alias fields ride the already-flagged POST. GET `/api/canonical-tags` is a safe method and needs no companion flag. PUT alias is web-origin only.

Empty `FRAMENEST_COMPANION_EXTENSION_ORIGINS` / `companion_extension_origins` remains fail-closed. No CORS headers. `X-FrameNest-Request: 1` remains required on unsafe methods. Identity headers remain UDS/Serve-injected only (Tailscale Serve strips spoofed values). Loopback-first backend unchanged.

**ADR-0062** `docs/adr/0062-per-user-media-alias-overlay.md`: Proposed in the implementation commit until the slice lands, then Accepted in that same implementation commit (project pattern). Owns overlay tables, pending-alias, GET/PUT alias, `metadata.alias.write`, apply-on-import, caller-private read policy, and the Save WAR.

**ADR-0061 bounded clarification (non-superseding):** add a dated “Later clarification” subsection that does **not** rewrite Decision items 1–5. It states: (a) Save uses WAR `ui/save.html|css|js` with the same `matches` as picker; (b) `POST /api/x/requests` may include optional alias fields; (c) `companion_mutation` remains those two POST routes only. Also add ADR-0062 to `docs/adr/README.md`. This is an additive clarification, not a supersession. If Orchestrator prefers zero edits to accepted ADR-0061, put (a)–(c) solely in ADR-0062 and leave 0061 frozen — architecture is the same.

**WAR residual (same class as live picker):** `https://x.com/*` and `https://twitter.com/*` may iframe `ui/save.html`. Official Chrome WAR: matching origins can load declared resources. Save page has no X cookies (extension origin). Network remains SW-only (`chrome.runtime.sendMessage`, same as `picker.js`). Content script does not `fetch` FrameNest. Residual owner: Cooperator (fingerprinting of the unpacked ID and WAR path). Do not ship `use_dynamic_url` in this whole.

Pinned unpacked origin remains `chrome-extension://omiihmnlkmieaafaphohakcgmbggppap` from the committed public `key`. Do not rotate. Do not print the gitignored private key.

## 10. X request / pending-alias lifecycle

1. **Cancel** dialog: no request, no pending, hover `+` returns to idle.
2. **Save** → `submit(url, login_key, alias=...)`:
   - `new`: create claim, upsert pending on that `claim_id`.
   - `active_reuse`: upsert pending on the live claim (last write wins). Apply when assets later receive `media_id`.
   - `reuse` (own already-successful claim): upsert pending and **immediately** apply overlay to each existing successful asset `media_id`.
3. **Apply hook:** `_complete_asset` after CATALOGED `media_id` — upsert overlay for `(media_id, claim.created_by_login_key)` from that claim’s pending row if present. Do **not** change `_imported_display_title` / `x_classification_for_upload`.
4. **Retry:** pending remains on the claim; retry body unchanged.
5. **New submit after FAILED claim:** today’s new-claim behavior; new pending on the new claim. Do not migrate pending across claims.
6. **Multi-asset:** one alias payload (permalink) applied to every successful asset of the claim. Per-asset targeting parked.
7. **`DUPLICATE_PENDING`:** still fails the asset (`X_CATALOG_HANDOFF_FAILED`); no `media_id`; no overlay. Out of this whole.
8. **Idempotency:** last pending write wins per claim. Overlay upsert is idempotent on `(media_id, login_key)`.
9. **Hostile alias strings:** validate with `MediaDisplayTitle` / `MediaDescription` / `CanonicalTagKey` before persist. Treat X DOM and form fields as untrusted.

## 11. Extension UX, message types, Attach-freeze proof

Mount: **parallel** to Attach, not extracted from it. Click hover `+` calls `openSavePopup` (new), not `savePost`. Closed shadow on a host under `document.documentElement` + iframe `chrome.runtime.getURL("ui/save.html")`. Position near the media-tile `+` (bottom-right of the eligible host). Escape / outside mousedown / Cancel close without submit.

**Attach-freeze proof that shared-shell extraction is not necessary:** Attach’s mount is composer-specific (`positionAttachPopup`, flush to the reply textarea, `aria-label` Search memes, iframe `ui/picker.html`). Save’s mount is media-host-specific and a different WAR document. Extracting a shared shell would require editing `openAttachPopup` / positioning — that is a thaw of a live-accepted control. Duplicating the ~80-line closed-shadow iframe pattern is the smaller, safer change.

New WAR entries (same matches as picker): `ui/save.html`, `ui/save.css`, `ui/save.js`. Picker WAR unchanged. Side panel remains picker; not the Save surface.

Fields (copy of web workspace language, no category, no provenance, no AI): Title, Description, Tags, Save, Cancel. Tags are a chooser of `GET /api/canonical-tags` keys, not free strings.

Protocol `v: "framenest.companion.v1"`. Unknown versions/types drop (`dropUnknown`).

New message type `CANONICAL_TAGS`. `SAVE_POST` payload becomes `{ url, alias }` where `alias` matches `XAliasBody`. SW remains the only FrameNest client. `pathFor("canonicalTags")` already exists; SW must handle the new type. Inflight poll (`POLL_CLAIM`) unchanged.

`+` states: idle / busy (`Saving to FrameNest`, `aria-busy`) / saved / failed. Failed remains plus glyph + danger border + `title`/`aria-label` (`Save to FrameNest failed`). Do not introduce a red ×. Visual: black background, `#00ff41` / `#39ff14`. Do not edit `web/styles.css` or Gallery/Details.

`save.html` uses `chrome.runtime.sendMessage` like `picker.js` (extension-origin WAR). Content script only mounts/unmounts the iframe and later updates `+` state from SW responses.

## 12. Analyze by AI gate

Ordinary Save form has **no** Analyze by AI control. `analysis.run` is admin-only. Automatic analysis is already fail-closed for X-linked uploads (`automatic_analysis_allowed_for_upload`). Admin Analyze remains on the FrameNest metadata page **after** a real `media_id` exists. Do not copy the web AI button onto X. Do not imply bytes exist before catalog handoff.

## 13. Threat model and residual-risk owners

INFOSEC planning only (route recommendation for later implementation: R3 authN/Z). No findings ledger, no containment, no exploit steps.

**Assets:** caller-private overlay; canonical metadata integrity; requester-private X claims; Tailscale identity binding; companion origin allowlist; unpublished media existence.

**Trust boundaries:** X page DOM (untrusted) → content script → extension SW → Tailscale Serve (identity headers) → FrameNest UDS/loopback → SQLite. WAR iframe is extension origin inside an X tab. Web origin is a separate mutation Origin.

**Attacker-controlled inputs:** permalink strings, Save form fields, extension messages, spoofed `Origin`, spoofed Tailscale headers on non-UDS, hostile tag keys, log fields.

**Actors and controls:**

| Actor | Control |
| --- | --- |
| Malicious X page | cannot `fetch` FrameNest from the content script; messages are typed and URL-validated; WAR iframe has no X cookies; SW does not fetch arbitrary URLs (Chrome network-requests guidance) |
| WAR iframe fingerprint / clickjack | residual same as picker; Cooperator-owned; no `use_dynamic_url` this whole |
| Spoofed Origin | unsafe methods require allowlisted Origin; empty allowlist fail-closed; PUT alias not companion-flagged |
| Spoofed Tailscale headers | Serve strips/reinjects; FrameNest trusts them only on the remote/UDS channel already enforced |
| Cross-user alias read | PK `(media_id, login_key)`; GET returns caller row only; tests must prove isolation |
| Canonical overwrite shortcut | ordinary role still lacks `metadata.canonical.write`; apply hook does not call canonical save |
| Generic metadata proxy | `companion_mutation` set not enlarged; PUT alias 403 from companion Origin |
| Hostile metadata | domain types; unknown tags 422; no canonical tag create from Save |
| Log leakage | audit records action/outcome/ids, not alias body text or media filenames |

**Security properties:** requester privacy, canonical integrity, origin allowlist integrity, least privilege, fail-closed empty allowlist, no CORS.

**Residual-risk owner: Cooperator** for WAR fingerprinting, unpublished feature branch vs NUC still on `bfad16b`, and Gallery showing canonical rather than alias. Overlay privacy bugs found in later R3 are correction-required, not silently accepted.

Recommended later implementation envelope: Evidence **E3**, `Independent acceptance: required-separate-fresh-worker`, INFOSEC **R3** (authN/Z) because this adds a capability, overlay isolation, and a companion-origin body expansion even though the flagged-route set is unchanged. This planning exchange: E0, independent acceptance not-required.

## 14. Tests and verification ladder for later slices

Do not run tests in this exchange. Later Python evidence uses only:

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline <exact HEAD> --operation test-focus -- <nodeid>
```

JavaScript: `node --test`. No ambient `.venv/bin/python`, `python`, `poetry run`, npm, or bundler.

Causal owners (production failures, not a ritual pyramid):

| Invariant | Owner |
| --- | --- |
| `companion_mutation` set does not grow; PUT alias is not flagged; GET alias is not flagged | `tests/contract/test_x_route_policy.py` |
| Companion Origin POST with alias succeeds; companion Origin PUT alias 403; web Origin PUT alias 200; ordinary canonical PUT still 403; empty allowlist fail-closed | `tests/contract/test_tailscale_ingress_security.py` |
| `XRequestCreateBody` optional alias; extra=forbid; unknown tag 422 `ALIAS_TAG_NOT_FOUND`; omitted alias preserves today’s body | `tests/contract/test_x_request_api.py` |
| New overlay GET/PUT contract, audience 404, caller isolation, empty-deletes | new `tests/contract/test_media_alias_api.py` |
| Ordinary role has `metadata.alias.write`, still lacks canonical write and `analysis.run` | `tests/contract/test_x_route_policy.py` / identity tests |
| Migration `0029` tables, checks, FK, rollback drop | new persistence test beside `test_x_requester_acquisition_migration.py` |
| Overlay isolation; pending last-write-wins; catalog removal deletes overlay tags then rows | new persistence tests |
| Apply on `_complete_asset` and `reuse`; canonical `display_title` unchanged | `tests/unit/application/test_x_acquisition_lifecycle.py` |
| Click opens Save popup; does **not** send `SAVE_POST` with bare `{ url }` on click; failed state remains plus not ×; WAR lists save.html | `tests/x_companion_extension.test.js` (today asserts the silent `{ url }` payload — that assertion must invert) |
| MiniDom picker tests remain green; Attach selectors untouched | `tests/unit/test_companion_picker.py` |

Validation ladder for later implementation: inspection + focused tests above. Broad suite only if the implementation prompt requires it. Michal visual acceptance (Reload unpacked, refresh X) is **not** a repository test and is a separate Cooperator step after implementation, not after this report.

## 15. Exact proposed paths and owner map

| Path | Change |
| --- | --- |
| `src/framenest/infrastructure/persistence/alembic_environment/versions/0029_media_user_alias_overlay.py` | new migration |
| `src/framenest/infrastructure/persistence/catalog_schema.py` | four tables |
| `src/framenest/domain/identity_access.py` | `metadata.alias.write` ordinary |
| `src/framenest/domain/media_user_alias.py` | new domain types (or extend `media_metadata.py` with alias value objects only — prefer a new module so canonical MediaMetadata stays one-row-per-media) |
| `src/framenest/application/media_user_alias.py` | get/put/apply/pending ports |
| `src/framenest/infrastructure/persistence/media_user_alias_repository.py` | new |
| `src/framenest/infrastructure/persistence/x_acquisition_claim_repository.py` | pending alias persistence |
| `src/framenest/infrastructure/persistence/catalog_removal_repository.py` | delete overlay before metadata graph |
| `src/framenest/application/x_acquisition.py` | `submit(..., alias=)`; apply in `_complete_asset` and `reuse` |
| `src/framenest/adapters/api/x_request_api.py` | optional alias body |
| `src/framenest/adapters/api/media_alias_api.py` | new GET/PUT router |
| `src/framenest/adapters/api/application.py` | wire router |
| `src/framenest/adapters/api/tailscale_ingress.py` | two new RoutePolicy rows; **do not** set `companion_mutation` on them |
| `extension/manifest.json` | WAR save.html\|css\|js |
| `extension/ui/save.html` | new |
| `extension/ui/save.css` | new (copy gallery tokens like picker; do not edit `web/styles.css`) |
| `extension/ui/save.js` | new |
| `extension/shared/messages.js` | `CANONICAL_TAGS`; SAVE_POST alias |
| `extension/background/service_worker.js` | handle tags + alias POST body |
| `extension/content/x_adapter.js` | `openSavePopup`; stop silent SAVE_POST; do not edit Attach functions except zero coupling |
| `docs/adr/0062-per-user-media-alias-overlay.md` | new |
| `docs/adr/0061-x-meme-browser-companion.md` | bounded clarification only |
| `docs/adr/README.md` | index 0062 |
| `docs/X_COMPANION.md` | Save popup operator text |
| `PRODUCT.md` / `SPEC.md` / `ROADMAP.md` | living overlay sentence; no Gallery thaw |
| Tests listed in section 14 | new and updated |

Do not touch: Attach positioning, `web/styles.css`, Gallery/Details UX, `docs/AP_UPGRADE_OBSERVATIONS.md`, yt-dlp pin, NUC deploy scripts, parent-whole Meta files, `00_handout.md`.

## 16. Causal implementation slices and later grants

Do **not** authorize these grants in this report. Order for a later Orchestrator:

1. **Domain + `0029` + persistence tests** — overlay isolation, pending, removal. Allowlist: domain, alembic 0029, catalog_schema, alias repository, claim repository pending, catalog_removal, persistence tests.
2. **HTTP + capability + ingress** — companion POST with alias 200; companion PUT alias 403; ordinary web PUT overlay 200; ordinary canonical PUT 403; empty allowlist unchanged. Allowlist: identity_access, tailscale_ingress, x_request_api, media_alias_api, application wiring, contract tests.
3. **Apply pending** in `_complete_asset` + `reuse`; assert canonical title unchanged. Allowlist: x_acquisition.py + lifecycle tests.
4. **Extension Save iframe + `CANONICAL_TAGS`**; invert silent `SAVE_POST`. Allowlist: extension/* named above + `tests/x_companion_extension.test.js`. Attach freeze: no edits to `openAttachPopup` / `positionAttachPopup` / picker WAR.
5. **Docs** — ADR-0062, ADR-0061 clarification, X_COMPANION, PRODUCT/SPEC/ROADMAP living status.

**Separate later grants (not this whole’s implementation prompt):**

- Independent acceptance: required-separate-fresh-worker, INFOSEC R3, after slices 1–4 exist as a candidate SHA.
- Publication / push of `feat/x-meme-browser-companion`.
- NUC enablement: `x_acquisition_root` + companion origin allowlist, only after publication authority. Never from check-alone.
- Static photos; per-asset targeting; picker alias search; Gallery thaw; AP upgrade.

Candidate topology for implementation: canonical checkout `/home/agile/Projects/framenest` on `feat/x-meme-browser-companion`, revalidate baseline (today `c5904b4`). Isolated worktree only if the implementation prompt requires exact-source provenance for tests.

## 17. Recommended next Worker route

```text
Worker session target: fresh-worker-session
Native planning mode: not-used
Reasoning recommendation: Extra High
Max: not requested
Independence required: no for implementation; yes for later acceptance
INFOSEC during implementation: R1 inline; do not self-certify R3
Exact baseline: revalidate feat/x-meme-browser-companion HEAD (expected c5904b47914fe376733e50ca8d0f4b9173dadb22 unless the branch moved)
Changed-path allowlist: section 15
NUC / SSH / sudo / push / provider / signed-in X / browser-profile install: not granted
Python evidence: ./.ap/ap exec --root /home/agile/Projects/framenest --baseline <HEAD> --operation test-focus
JavaScript: node --test
Post-plan implementation session: must be a new complete Orchestrator prompt
```

This planning session ends with this report. Plan UI approval does not start slice 1.

## 18. Parked scope, unresolved facts, and stop conditions

Parked: NUC enablement, static X photos, per-asset targeting, popup AI, multi-model dropdown, picker alias search, Gallery/Details alias display, web overlay editor UX, AP upgrade, Web Store, key rotation, CORS/`all_urls`/content-script fetch, Hide/Trash, `DUPLICATE_PENDING` catalog handoff.

Unresolved facts that do **not** block this architecture:

- Live Brave unpacked WAR iframe behavior on signed-in X (not authorized). Residual same as accepted picker; smallest later probe is Cooperator Reload-unpacked on one tweet, not a Worker spike.
- Exact `Origin` header bytes of an extension-origin `fetch` are established Chromium behavior (`chrome-extension://<id>`) and already gated by parent-whole tests; not re-probed here.

Stop conditions for a later Worker: dirty unexpected FrameNest tree; public `main` advanced with a material conflict; schema head no longer `0028`; attempt to thaw Attach; attempt to flag PUT alias as `companion_mutation`; attempt to write overlay into `media_metadata`.

## 19. Smallest next Orchestrator action

One decision only: **accept this plan as written, or name one targeted revision boundary.**

Do not issue an implementation prompt until Michal accepts. Do not treat this file or Plan UI approval as implementation authority. If accepted, the next prompt is a `fresh-worker-session` with `Native planning mode: not-used` and the section 15 allowlist, starting at slice 1.

## 20. Resolved Execution Issues / Near-Misses and Pre-Existing Failure Classification

```text
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
```

`00_handout.md` already present in this whole’s untracked directory was not executed. Parent-whole untracked 06–12 files were not staged. `docs/AP_UPGRADE_OBSERVATIONS.md` untriaged entry remains parked.
