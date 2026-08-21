### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-x-companion-save-category-mvp
Worker session ordinal: 01
Worker exchange ordinal: 01

Task identity: FN-X-COMPANION-SAVE-CATEGORY-PLAN-01-REPORT
Repair identity: report-rendering-only exchange 02 for the missing exchange-01 terminal companion
Frozen planner artifact: `/home/agile/meta/projects/framenest/03/06-framenest-x-companion-save-category-mvp/01_plan_00.md`
Frozen planner SHA-256: `578349a0edecc8028cfc1b48bde1f131cb085b3c2496c5dd472c478959bdd36e`
Frozen planner size: 30,632 bytes
Planning-cycle effect: none; this repair consumed no second planning cycle, reopened no decision, and changed no frozen plan content.

#### 1. Terminal outcome

Status: PASS
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Implementation performed: no

The frozen artifact is a decision-complete implementation plan for public X video, animated-GIF-as-provider-MP4, and ordinary JPEG/PNG photos; explicit canonical category choice; honest outcomes; keyboard-first Save UX; durable request/retry/deduplication semantics; proportional validation; security review; documentation; migration; rollout; and acceptance gates. This report renders that plan into AP's required terminal form without re-planning or extending authority. The logical whole remains open pending consolidated plan acceptance, later implementation, validation, independent INFOSEC R3, human acceptance, and separately authorized publication and deployment work.

#### 2. Capability and repository gate

Capability handshake:

- Requested for the frozen planning exchange: Native Plan Mode, `gpt-5.6-sol`, and Extra High reasoning.
- Directly observed now: Native Plan Mode is disabled; report-rendering-only filesystem authority is active; the frozen artifact is present with the exact required hash and byte size; the original planning prompt is present with SHA-256 `eb200ba664c75e09f8633f621869c584242fb6f8e0dc671fe343c6a770871c62`; the exact report target was absent before this write.
- Inferred from retained context and the exact continuity artifact: this is the same concrete Worker session that produced the frozen exchange-01 plan, so no fresh-session reconstruction was required.
- Unknown/not observably exposed: the hidden runtime model identity and reasoning-slider value. No false attestation is made for either.
- Internal delegation: not used. Evidence posture: non-independent.

Read-only repository re-gate:

- FrameNest `/home/agile/Projects/framenest` remains on `feat/x-meme-browser-companion` at `226d6e26fedea94927a6a0ab92b3f02c4fbeb4b8`, with parent `d8f0fc96098d343ecc6bd781bc1b2ff7a98aa327` and tree `4208e8711d2589d61dd21e2529a5a9ad548db8c3`. Its tracked tree is clean and it has no configured upstream.
- Local and public FrameNest `origin/main` are both `045f33b44897a6f3949cc515792336396f1d33a1`; public state was checked with `git ls-remote`, without fetch.
- The three commits above public `main`—`7e854d251af841b3ef4a2ddaf130081e330c6f8d`, `d8f0fc96098d343ecc6bd781bc1b2ff7a98aa327`, and `226d6e26fedea94927a6a0ab92b3f02c4fbeb4b8`—remain accepted-continuation and unpublished-candidate evidence, not unexplained divergence and not publication authority.
- FrameNest's `.ap` gitlink, detached checkout, local `origin/main`, and public `main` all resolve to `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`; the checkout is clean.
- Meta HEAD, local `origin/main`, and public `main` all resolve to `696381c331859c0a818da660faf38e4907e23322`. Before this write, the only Meta differences were the expected untracked continuity artifacts `01_planning_00.md`, `01_plan_00.md`, and `01_planning_01.md`; the report target was absent.
- No implementation or FrameNest/AP mutation occurred after the plan froze. The re-gate found no evidence drift that changes a frozen decision.
- NUC release `045f33b`, schema `0029`, active service, empty companion origins, and empty X staging root remain historical 2026-08-20 claims. They were not probed and are not current acceptance evidence.

#### 3. Verified current data-flow map

The current Surface A Save path is:

```text
extension/ui/save.html + extension/ui/save.js
  -> SAVE_POST {url, alias}
  -> extension/background/service_worker.js::savePost()
  -> POST /api/x/requests {url, alias}
  -> src/framenest/adapters/api/x_request_api.py::XRequestCreateBody
  -> src/framenest/application/x_acquisition.py::XAcquisitionRequestService.submit()
  -> x_post_claims + x_claim_pending_aliases
  -> src/framenest/application/x_acquisition.py::XAcquisitionCoordinator
  -> src/framenest/infrastructure/x/downloader.py::YtDlpXExtractor.inspect()
  -> x_assets
  -> download by permalink + filtered ordinal
  -> src/framenest/infrastructure/x/staging.py claim-owned staging
  -> upload quarantine + BoundedUploadMediaValidator
  -> upload publication/catalog
  -> x_classification_for_upload(default_x_category(media_type))
  -> canonical media_metadata
  -> owner-scoped GET claim polling
  -> extension/content/x_adapter.js::pollClaim()
  -> per-control terminal rendering
```

Verified current facts:

- `XRequestCreateBody` forbids unknown fields and has no category field.
- Category is selected only at catalog handoff: image becomes General; video/GIF becomes Meme. Claim and asset processing are durable, but category intent is not.
- `selected_variant` is persisted on `x_assets` but is not supplied to `download()`.
- The pinned Twitter extractor filters `type == photo`; production acquisition therefore does not support ordinary photos despite image support in the domain.
- The current downloader reselects by filtered ordinal, so retry or post edits can select a different provider media row.
- Requester uploads use `SILENT_KEEP_SEPARATE`; cross-user exact-byte matches remain separate logical media.
- `pollClaim()` currently renders every terminal response as “Saved to FrameNest,” including `failed`.

#### 4. Contradictions and acceptance-blocking gaps

- Repository comments and tests claim a photo-only post becomes `X_NO_SUPPORTED_MEDIA`; the pinned CLI actually exits nonzero and currently maps that path to `X_EXTRACTOR_FAILED`.
- Domain support for `XMediaType.IMAGE` is not production photo support.
- `artifact.mp4` is treated as a universal staging name despite image-domain support.
- `catalog_removed` is terminal in the domain but absent from the service-worker terminal-state set.
- Failure-code-based terminal detection is redundant and incomplete.
- A terminal failed claim receives a success checkmark and success copy.
- Inflight recovery retains claim IDs but cannot reconnect them to controls found by a later page scan.
- Each tile displays a separate `+` although Save is permalink-wide; only the initiating control receives status.
- The popup lacks initial focus transfer and focus restoration.
- Plain Enter can submit from a single-line field. Tag Enter is handled, but category and general Save keyboard behavior are not fully defined.
- Same-requester successful and active claims are reused without category-conflict semantics.
- `_asset_retryable()` treats every failed asset as retryable, contrary to the domain failure-code table.
- Non-retryable asset failure currently terminates the whole claim immediately, preventing honest mixed-media partial completion.
- X metadata currently protects category as source-derived immutable data, contradicting ADR-0055's administrator-override rule.

These are in scope because each directly affects the requested Save promise or the truthfulness and durability of its outcome.

#### 5. Recommended product contract

Category and defaults:

- Add a compact native `<fieldset>` with legend `Category` and radio choices `General`, `Meme`, `Movie`, and `YouTube`, represented as `general`, `meme`, `movie`, and `youtube` on the wire and in persistence.
- Offer all four choices. `youtube` is a semantic category under ADR-0055, not an acquisition-source proxy.
- Display: `Category describes the content and applies to every media item in this post. Movie genres can be added later in FrameNest.`
- Movie is valid with zero genres at ingest; do not add a genre picker.
- A photo tile defaults to General. A video tile, including X animated-GIF-as-video, defaults to Meme. An unknown synthetic media host defaults to General.
- For a mixed post, the clicked tile supplies the initial default, but one final category applies to every asset in the post. Backend inspection never silently changes the visible selection.
- The new UI always supplies a category; the API field remains optional for old clients.

Keyboard, focus, and busy-state behavior:

- Opening the popup moves focus into the iframe and then to Title.
- Forward focus order is Title → Description → checked category radio → Tags → selected-tag removal buttons → capability-gated Analyze → Save. Shift+Tab from Title reaches header Close.
- Native radio behavior owns Arrow keys and Space. Enter on a radio is suppressed and never submits.
- Enter in Tags accepts the highlighted suggestion; with no suggestion, it does nothing.
- Plain Enter in Title does not submit. Description retains newline behavior.
- Enter or Space on Save submits. Ctrl+Enter or Cmd+Enter submits from elsewhere.
- Escape closes an open tag list first; otherwise it closes the popup.
- Header Close, Escape, outside click, and completed submission restore focus to the initiating `+`.
- During submission, mark the form `aria-busy`, disable mutable fields and Save actions, and leave header Close usable. Use polite status for progress and alert semantics for validation failures.
- No mouse-only category interaction is introduced.

Media promise:

- Native X video remains MP4-backed.
- X `animated_gif` remains user-visible as GIF while normally storing the provider's MP4 representation. A literal GIF is accepted only when explicitly identified and validated by the existing GIF validator.
- Ordinary X photos are supported only when the provider-native representation is JPEG or PNG. WebP and other still formats are rejected without transcoding.
- A post may contain at most four native assets; the selected category applies to all of them.
- Unsupported, private, deleted, live, external-link, oversized, overlong, malformed, or changed media fails with a sanitized stable code.

Duplicate, conflict, retry, and correction ownership:

- Same requester, successful post, explicit category matching every live cataloged asset: reuse the claim, apply alias changes, and report `Already saved to FrameNest`.
- Same requester, successful post, different or internally mixed canonical category: return HTTP 409 `X_REQUEST_CATEGORY_CONFLICT`; do not mutate category or alias.
- Same requester, active claim, same persisted category: active reuse.
- Same requester, active claim with another category, or a legacy `NULL` category against an explicit request: return 409 rather than racing or overwriting intent.
- An old client omitting category asserts no category and retains existing reuse behavior.
- A create race compares the transactionally selected active winner before returning `active_reuse`.
- Another requester receives an independent private claim and logical media under the current keep-separate policy.
- Retry preserves the original claim category, including `NULL` legacy semantics; successful assets are not re-downloaded.
- Administrator correction uses the existing capability-gated metadata API and changes only canonical media rows. It does not rewrite claim intent, acquisition source, or X creator provenance.
- If an administrator corrects only part of a multi-asset claim, a later explicit duplicate Save detects mixed canonical categories and fails honestly.
- Every `+` for the same permalink mirrors the same pending and terminal state.

Terminal presentation:

- Active states: busy spinner and `Saving to FrameNest…`.
- `completed`: green check and `Saved to FrameNest`.
- Create disposition reuse or `duplicate_resolved`: green check and `Already saved to FrameNest`.
- `completed_partial`: amber warning and `Partially saved to FrameNest (S of N)`.
- `failed`: danger-border plus and `Save to FrameNest failed`, optionally followed by a fixed friendly explanation mapped from the sanitized code.
- `catalog_removed`: danger-border plus and `Saved item is no longer available in FrameNest`.
- Ambiguous POST transport: amber `Save status unknown—check FrameNest`; never claim definite failure or success.
- Poll transport failure: retain inflight recovery, retry with bounded exponential backoff for two minutes, then retain an unknown warning and recheck during later page recovery.
- Unknown server state: fail closed as status unknown and retain recovery.
- A single hidden `aria-live="polite"` region announces post-level changes.

Asset-scoped terminal failures continue to later assets. Some cataloged plus some failed becomes `completed_partial`; one failed asset preserves its specific code; multiple assets with none successful becomes `X_MULTI_ASSET_FAILED` while retaining individual sanitized asset codes. Claim-wide failures still fail immediately. Retry eligibility is determined only by `is_retryable_x_failure(asset.failure_code)`.

#### 6. Selected technical architecture

Durable category path:

```text
UI contentCategory
  -> extension SAVE_POST allowlist validation
  -> API content_category
  -> ContentCategory parsing
  -> XPostClaim.requested_content_category
  -> durable x_post_claims column
  -> restart/retry/recovery
  -> x_classification_for_upload()
  -> canonical media_metadata.content_category
```

- Extension messages use camel-case `contentCategory`; the service worker accepts exactly the four allowed values and emits API `content_category`.
- `XAliasBody` remains unchanged.
- Invalid category returns sanitized 422 `X_REQUEST_INVALID_CATEGORY`.
- Add `XAcquisitionCategoryConflictError`, mapped to 409 `X_REQUEST_CATEGORY_CONFLICT`.
- Extend claim snapshots with `requested_content_category`, counts, `can_retry`, and create-only `submission_result`.
- Catalog classification uses `claim.requested_content_category` when non-`NULL`, otherwise the current media-kind default.
- Inject the existing metadata repository into the request service so successful-claim conflict checks inspect actual canonical categories, including administrator corrections.

Authoritative photo inspection uses a FrameNest-owned isolated status bridge with the exact pinned `yt-dlp==2026.7.4` and runtime `2026.07.04`:

- Invoke `sys.executable -I -m framenest.infrastructure.x.status_bridge`.
- Instantiate pinned `TwitterIE` with an empty cookie jar and no `.netrc`, browser cookies, CLI config, or plugin discovery.
- Call the pinned `_extract_status(post_id)` seam.
- Normalize only bounded post metadata and native `extended_entities.media` rows.
- Emit video, `animated_gif`, and photo rows in provider order, each with a required `source_media_key`.
- Never expose raw status JSON or raw media URLs outside infrastructure.
- Fail startup/attestation if the pinned version or required seam changes.

This is preferred over a yt-dlp upgrade/plugin, gallery-dl, an official credentialed X API, or DOM-derived URLs because it adds no dependency or credential and preserves server-side authority.

Inspect-to-download continuity persists:

- `source_media_key`: authoritative provider media ID.
- `ordinal`: initial display order only.
- `selected_variant`: a stable policy identifier, never a signed URL: `x-photo-orig-jpeg-v1`, `x-photo-orig-png-v1`, `x-video-default-mp4-v1`, or `x-animated-gif-mp4-v1`; literal GIF only when actually present.

Expand `XExtractor.download()` to require `selected_variant`. Every download and retry reinspects through the bridge, matches the exact `source_media_key`, requires unchanged media type and a representation compatible with the persisted policy, and treats ordinal as non-authoritative. A missing key, changed type, or unavailable representation fails terminally as `X_SOURCE_MEDIA_CHANGED`.

For video/GIF, download the re-resolved provider position through yt-dlp with bounded info output and verify that the resulting media ID equals `source_media_key` before committing staged bytes. Delete the artifact and fail on mismatch. For photos, the bridge re-resolves and downloads in one bounded subprocess, so the candidate URL is neither persisted nor placed on a command line.

Strict photo transport accepts only HTTPS to exact host `pbs.twimg.com`, no user information, fragment, non-443 port, backslash, or non-`/media/` path, and only `name=orig` plus an optional agreeing `format=jpg|jpeg|png` query. Redirects are forbidden. DNS resolution occurs in the bounded subprocess; every non-global address is rejected; connection uses a selected vetted address while retaining TLS SNI/certificate verification and `Host: pbs.twimg.com`. Send `Accept-Encoding: identity`.

Require status 200, expected `Content-Type`, positive optional `Content-Length`, JPEG/PNG magic agreement, 30-second connect/read limits, and a 64 MiB photo ceiling. Stream to a claim-owned `0600` partial, hash while writing, `fsync`, and atomically promote only a complete file. Never log URLs, query strings, response bodies, or bytes.

Use neutral fixed X staging name `artifact.bin`. Extend shared descriptor-safe staging with a configurable artifact name; the YouTube default remains `artifact.mp4`. Derive display extension from validated expected MIME, not `XMediaType`.

The existing `BoundedUploadMediaValidator` remains authoritative for complete decoding: JPEG/PNG stills, maximum dimension 8,192, maximum 33,177,600 decoded pixels, and existing GIF/MP4 rules. Map downstream validation rejection to a stable X asset failure rather than generic catalog failure.

Backward and forward compatibility:

- New backend with old extension works because category omission remains valid.
- New extension against old backend receives 422, fails closed with an upgrade message, and never retries by dropping category.
- Deploy schema/backend before reloading the extension.
- The existing three local commits remain ancestors of the implementation candidate.
- Companion origins and X acquisition root remain separate configuration grants; production acceptance is not claimed.

The extension uses one explicit outcome reducer for initial and polled responses. The service worker recognizes all terminal states including `catalog_removed`, never infers terminality from failure code, persists only nonterminal claims, forwards post ID/disposition/counts/retryability/sanitized code, and retains inflight records on ambiguous transport failures. The content script keys controls by post ID to support recovery and permalink-wide state mirroring.

#### 7. Schema decision

Create Alembic revision `0030_x_claim_requested_content_category.py` with `down_revision = "0029"`. Add to `x_post_claims`:

```sql
requested_content_category TEXT NULL
CHECK (
  requested_content_category IS NULL OR
  requested_content_category IN ('general', 'meme', 'movie', 'youtube')
)
```

- No server default and no historical backfill. `NULL` means an old client/legacy claim and retains media-kind defaults.
- Repository serialization and hydration use `ContentCategory | None`.
- Use a SQLite batch rebuild with foreign-key enforcement disabled only through the existing helper, then re-enable it and run `foreign_key_check`.
- Preserve every row, self-FK, active-requester uniqueness rule, index, alias, asset, and version.
- Downgrade refuses if any row has non-`NULL` `requested_content_category`. If all rows are `NULL`, batch-drop the column, restore the exact 0029 table/index contract, and verify foreign keys.
- After real category use, operational rollback runs the previous application against additive schema 0030; it does not downgrade the database.
- Deployment migrates 0029→0030 before starting the new backend. An old backend remains compatible with the already-upgraded additive schema.

#### 8. Implementation slices and exact path allowlists

One later implementation Worker should produce four reviewable commits. No implementation was performed here.

Slice 1 — category, persistence, API, and correction ownership

Allowed paths:

```text
src/framenest/domain/x_acquisition.py
src/framenest/application/ports/x_acquisition.py
src/framenest/application/ports/media_metadata_repository.py
src/framenest/application/x_acquisition.py
src/framenest/adapters/api/x_request_api.py
src/framenest/adapters/api/application.py
src/framenest/infrastructure/persistence/catalog_schema.py
src/framenest/infrastructure/persistence/x_acquisition_claim_repository.py
src/framenest/infrastructure/persistence/media_metadata_repository.py
new src/framenest/infrastructure/persistence/alembic_environment/versions/0030_x_claim_requested_content_category.py
directly affected category/API/repository tests
new tests/integration/persistence/test_x_requested_category_migration.py
existing migration tests containing literal schema-head 0029 assertions discovered in planning evidence
```

Recommended commit: `feat: persist canonical category on X save claims`

Stop if the populated migration loses rows, indexes, or foreign keys, or requires a backfill.

Slice 2 — authoritative media continuity and photo acquisition

Allowed paths:

```text
src/framenest/application/ports/x_extractor.py
src/framenest/domain/x_acquisition.py
src/framenest/application/x_acquisition.py
src/framenest/infrastructure/x/downloader.py
new src/framenest/infrastructure/x/status_bridge.py
src/framenest/infrastructure/x/staging.py
src/framenest/infrastructure/youtube/staging.py only for configurable artifact-name support with unchanged YouTube default
src/framenest/adapters/api/application.py
tests/support/x_fake_demo.py
tests/browser/x_browser_server.py
directly affected downloader, lifecycle, and staging tests
new tests/unit/infrastructure/test_x_status_bridge.py
new tests/unit/infrastructure/test_x_photo_transport.py
new tests/integration/test_x_photo_acquisition_vertical_slice.py
```

Recommended commit: `feat: acquire public X photos with source continuity`

Stop rather than widen hosts, redirects, cookies, dependencies, or provider representations.

Slice 3 — Surface A category and truthful status

Allowed paths:

```text
extension/shared/messages.js
extension/ui/save.html
extension/ui/save.css
extension/ui/save.js
extension/background/service_worker.js
extension/content/x_adapter.js
tests/x_companion_extension.test.js
tests/x_acquisition_cockpit.test.js
API/ingress contract tests needed to pin the new body and unchanged route policy
```

Recommended commit: `fix: make X save category-aware and outcome-truthful`

Stop if category requires alias mutation, another HTTP route, new host permissions, or Surface B/C changes.

Slice 4 — durable decision and documentation

Allowed paths:

```text
new docs/adr/0064-x-save-category-and-public-photo-acquisition.md
docs/adr/README.md
docs/X_COMPANION.md
README.md
PRODUCT.md
SPEC.md
SECURITY.md
SERVER.md
ROADMAP.md
```

Recommended commit: `docs: record X category and photo acquisition contract`

Do not edit ADR-0061, ADR-0062, or ADR-0063. No dependency or lockfile change is authorized; discovery of a need for either stops implementation for a new decision.

#### 9. Validation ladder

Future Python execution must use AP baseline `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` from FrameNest baseline `226d6e26fedea94927a6a0ab92b3f02c4fbeb4b8`.

1. Run the AP project check and runtime provenance gate.
2. Run focused domain/application tests for category validation, serialization, restart, catalog handoff, retry preservation, same/different-category successful reuse, active conflict and create race, old-client omission, cross-requester keep-separate behavior, partial/all-failed multi-asset behavior, retryability by failure code, and administrator category correction while creator/source remain immutable.
3. Run extractor/transport/staging tests proving photo-only and mixed synthetic status normalization; exact source-key/variant matching after reorder/edit; deleted post and missing key; JPEG/PNG success; WebP, MIME mismatch, malformed bytes, oversize, redirects, foreign hosts, non-global DNS, timeout, and partial-file cleanup; runtime/seam attestation for `2026.07.04`; absence of cookies, `.netrc`, config, plugins, shell interpolation, and real-provider contact; and unchanged YouTube staging behavior.
4. Run migration tests for populated 0029 upgrade, `NULL` legacy rows, invalid SQL values, persistence hydration, FK/index preservation, guarded downgrade, and schema-head 0030 assertions.
5. Run API/ingress tests for optional category, all four values, invalid category 422, conflict 409, counts/disposition, old omission, unchanged two-route mutation policy, and fail-closed companion origins.
6. Run JavaScript tests for radio semantics, default hints, Enter suppression, Ctrl/Cmd+Enter, Escape layers, focus restoration, busy state, same-post mirroring, inflight recovery, every terminal mapping, and failed-never-saved.
7. Run a zero-network synthetic vertical slice from status fixture through staged JPEG/PNG, the real upload validator, and catalog metadata, including restart/retry coverage.
8. After focused success, run the full Python test operation because schema head and shared staging behavior are repository-wide risks. Then run `node --test tests/x_companion_extension.test.js tests/x_acquisition_cockpit.test.js`.
9. Finish with `git diff --check` and exact status/diff review.

No Python or JavaScript tests were run in the planning exchange or this report-rendering repair.

#### 10. Security and privacy analysis

Protected assets are requester identity, private claim/media visibility, canonical metadata, staging and catalog files, host filesystem/network, and X provenance. Trust boundaries are the extension/content-script bridge, service worker/API boundary, owner-scoped claim service, untrusted provider response into the isolated bridge, bridge-to-staging handoff, and upload quarantine/catalog handoff.

Attacker-controlled inputs include submitted permalinks, extension messages, API bodies, claim IDs, provider status JSON, media IDs, URLs, redirects, DNS answers, headers, lengths, formats, filenames, image bytes, and provider ordering. Relevant abuse cases include SSRF and DNS rebinding, redirect escape, signed-in/private extraction, MIME and magic confusion, decompression or decoded-pixel abuse, oversized/partial files, path/symlink attacks, process escape, media reorder TOCTOU, cross-requester disclosure/deduplication, and false-success UI state.

Required controls are:

- Strict X permalink validation and public-post extraction only.
- No user cookies, browser profiles, private posts, DMs, `.netrc`, provider credentials, or content-script media URL authority.
- Exact server-side CDN scheme/host/path/port/query allowlist, verified TLS identity, globally routable pinned destination IP, and no redirects.
- Bounded subprocess time/output/process groups and fail-closed version/seam attestation.
- Four-asset, per-photo 64 MiB, per-asset 1 GiB, duration, claim, and staging limits.
- Neutral fixed staging name, `0700` directories, `0600` partial files, no-follow/exclusive opens, `fsync`, atomic promotion, checksum, and deterministic cleanup.
- Downstream signature, decoded-format, dimension, pixel, and media-kind validation.
- Owner-scoped reads and unchanged keep-separate duplicate mode.
- No raw URL, provider message, response body, bytes, or credential logging; expose only sanitized stable failure codes.

Evidence tier: planning and static repository/dependency-source evidence only; no real-provider, runtime acceptance, production, or independent-audit evidence.

Residual risks remain in the private pinned `TwitterIE._extract_status` maintenance seam and future provider/CDN shape changes. The implementation Worker owns version/seam attestation and negative tests; the independent security Worker owns the later adversarial review; the release operator owns current NUC/schema/backup/config readback; the Orchestrator and Michal own acceptance and grant decisions. Host, redirect, format, or seam drift must fail closed.

Independent acceptance: required-separate-fresh-worker

Fresh independent INFOSEC R3 is required after implementation and before publication or deployment. Its scope includes the existing companion bridge/origin/alias Save path plus the new category body, terminal reducer, status bridge, photo transport, staging, requester isolation, and migration rollback. This Planner and repair do not certify security.

#### 11. Acceptance plan

Automated evidence in Section 9 precedes human acceptance. After a configured HTTPS FrameNest origin and X acquisition root receive separate grants, Michal's small Brave/X checklist is:

1. Reload the unpacked extension; keyboard-focus a photo `+`; open with Enter; verify Title focus, General default, Arrow-key category change, no Save on plain Enter, and focus restoration on Escape.
2. Save a public JPEG/PNG photo with a non-default category and verify canonical Gallery category plus image media kind.
3. Save a public video and X animated GIF; verify Meme default and honest provider-MP4 representation for animated GIF.
4. Save a multi-photo or mixed post; verify one category across all assets and mirrored pending/final state on every tile.
5. Save the same post/category again and see `Already saved`; choose a conflicting category and see an honest conflict without canonical overwrite.
6. Exercise or synthetically inject partial and failed terminal outcomes; confirm neither renders generic success; verify Tags Enter, Ctrl/Cmd+Enter Save, Close, and focus restoration.

Configured-origin/NUC production acceptance is separate. It cannot be claimed until current release, schema 0030, service health, backup readiness, exact extension origin, and X staging root are directly read back. None of that evidence exists in this report.

#### 12. Proposed publication and deployment sequence

1. Complete the four implementation commits and local automated validation.
2. Complete independent INFOSEC R3 and any required correction/re-audit.
3. Obtain Michal's rendered UX acceptance where locally feasible.
4. Obtain a distinct non-force publication grant; publish the existing three accepted unpublished commits followed by the new candidate.
5. Obtain a distinct NUC migration/deployment grant.
6. Verify current NUC release, schema, backup state, service state, companion origin, and X acquisition root through the canonical gate.
7. Prepare the new release, take and verify the required backup, migrate 0029→0030 from the new release tree, and then start the new backend.
8. Verify old-extension `{url, alias}` submission against the new backend.
9. Only after backend/schema readiness, reload the new extension. A new extension against an old backend must fail closed with an upgrade message and must not retry after deleting category.
10. Treat companion-origin and X acquisition-root mutations as separate exact host-configuration grants. Run production acceptance only after direct readback.

Rollback uses the previous application against additive schema 0030 and reloads the previous extension. Do not downgrade a database containing category intent. This is a proposed later sequence only; no publication, deployment, migration, or configuration action is authorized here.

#### 13. Durable decisions and documentation

Create ADR-0064, `docs/adr/0064-x-save-category-and-public-photo-acquisition.md`, to supersede only ADR-0061's static-photo deferral, ADR-0061/0062's implicit fixed-category Surface A behavior, and ADR-0055's future-X default where explicit choice now exists. Preserve their extension trust, alias, picker, Gallery, and side-panel decisions. Do not edit accepted ADR-0061, ADR-0062, or ADR-0063.

Reconcile `docs/adr/README.md`, `docs/X_COMPANION.md`, `README.md`, `PRODUCT.md`, `SPEC.md`, `SECURITY.md`, `SERVER.md`, and `ROADMAP.md` to state:

- schema head 0030;
- explicit four-category Save contract;
- claim-wide category and retry semantics;
- public JPEG/PNG photo support and WebP rejection;
- animated GIF as provider MP4;
- authoritative source-key/variant continuity;
- terminal, partial, and duplicate behavior;
- administrator category correction with immutable acquisition/creator provenance;
- no provider credentials, redirects, DOM URLs, transcoding, dependency/pin change, or new companion route;
- independent R3 and production-configuration gates.

Remove static-photo deferral from current status/backlog text without rewriting historical accepted ADRs.

#### 14. Decision ledger

Accepted repository/product facts preserved by the plan:

- Surface A is post/permalink-wide, owner-scoped, and uses the existing two-route companion/API trust boundary.
- Cross-requester media stays logically separate under `SILENT_KEEP_SEPARATE`.
- Canonical category is metadata and is correctable by the existing capability-gated administrator path, while acquisition source and X creator provenance remain immutable.
- Existing local FrameNest commits are continuation/candidate evidence only; current NUC/config claims are historical; publication and deployment need later grants.

Planner recommendations awaiting one consolidated Michal acceptance:

- Offer General, Meme, Movie, and YouTube.
- Default photo to General, video/GIF to Meme, and unknown to General.
- Persist one claim-level category through migration 0030.
- Reject same-requester category conflicts with 409; preserve cross-requester keep-separate behavior.
- Allow the existing administrator metadata Save to correct canonical category only.
- Acquire public JPEG/PNG photos through the pinned isolated status bridge and strict transport, with stable source-key/variant continuity.
- Continue after asset-scoped failures and report completed, duplicate, partial, failed, removed, and ambiguous states honestly.
- Require fresh independent INFOSEC R3 before publication/deployment.

Parked adjacent scope:

- Per-asset category or Save targeting.
- Gallery alias editor and alias-aware Gallery/picker.
- Analyze execution.
- Picker audience widening.
- Companion-origin or X acquisition-root mutation.
- Publishing, deployment, Web Store work, AP upgrade, and parent-whole closure.

Rejected alternatives:

- Category encoded in alias or a general canonical-write grant.
- Category retained only in memory.
- Silent category overwrite or silently ignored conflict.
- Trusting X DOM/CDN URLs supplied by the content script.
- Cookies, signed-in scraping, official credentialed X API, or private-post access.
- Dependency/pin update or arbitrary yt-dlp plugins for this MVP.
- WebP transcoding.
- Cross-user canonical deduplication.
- Silently dropping category when an old backend rejects it.

No additional Cooperator architecture choice remains beyond accepting or rejecting this consolidated recommendation. The whole remains open.

#### 15. Smallest next step

The exact next Orchestrator action is to review this frozen plan with Michal and obtain one consolidated plan acceptance. Only after acceptance should the Orchestrator issue a complete, bounded implementation prompt to the current Worker session with Native Plan Mode disabled, the four slices and path allowlists above, no push/NUC/configuration authority, and independent INFOSEC R3 reserved as a later acceptance gate. This report itself grants no implementation authority.

#### 16. Standard report closeout

Start commit (FrameNest): 226d6e26fedea94927a6a0ab92b3f02c4fbeb4b8
End commit (FrameNest): 226d6e26fedea94927a6a0ab92b3f02c4fbeb4b8
Changed files (FrameNest/AP): none
Changed files (Meta): projects/framenest/03/06-framenest-x-companion-save-category-mvp/01_report_00.md (create; this report)
Tests run: none; read-only report-completion re-gate only
Validation performed: frozen-plan and prompt SHA-256/size checks; read-only FrameNest/AP/Meta status, identity, gitlink, upstream, and public-main checks
Implementation: none
Commit/push/publication/deployment/configuration/provider/browser/NUC activity: none
Git result: no stage, commit, amend, push, fetch, branch, tag, worktree, or configuration mutation
Deviations: none
Report justification: new-evidence

Risks and missing evidence: no real-provider behavior, rendered Brave UX, current NUC state, configured origin/root, deployment, or independent audit evidence exists. The pinned private yt-dlp seam requires an intentional maintenance gate on every future pin change. Exact CDN behavior must fail closed if X changes host, redirect, or format conventions.

Resolved Execution Issues / Near-Misses: distinguished the actual photo-only `X_EXTRACTOR_FAILED` behavior from stale `X_NO_SUPPORTED_MEDIA` comments; identified failed-terminal false success, broken inflight-to-control recovery, the category/administrator immutability contradiction, and the unused `selected_variant`/ordinal TOCTOU before implementation; repaired the missing standard terminal-report wrapper without altering the frozen plan.

Pre-Existing Failure Classification: acceptance-blocking product defects and unimplemented capability; no test or environment failure was generated during planning or report completion.

Authority from this report-rendering task expires with this terminal report. No implementation, further Meta mutation, FrameNest/AP mutation, acceptance, audit certification, publication, deployment, migration, configuration, provider/browser/NUC activity, or logical-whole closure is authorized.
