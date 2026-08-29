### Report for ORCHESTRATOR_CHAT

Read-only: yes  
Native planning mode: not-used  
Planning result: PASS  
Repository baseline/end: `454f181d8b011ef563ac13a28e8d894dbc497bc4`  
Changes, Git writes, provider/NUC/browser activity: none

The plan below treats current code and tests as operational truth. I did not rerun the reported 212 Node / 58 Python baseline tests and do not claim independent NUC evidence.

## Root-cause and classification summary

| Area | Classification | Planning conclusion |
|---|---|---|
| A1 suggested tags | Confirmed defect plus bounded evidence gap | Existing mapped tags silently no-op because `copySuggestionFieldToCurrent()` returns early. This does not prove the reported remove-then-re-add failure; reproduce that first in a focused test. |
| A2 playback | Confirmed video defect; GIF product amendment; handout contradiction | Video clears its preview before readiness and can flash black. Pointer cursor is a refinement. Plain `<img>` GIF playback cannot pause/resume at a frame; repository history does not support calling this an editor regression. |
| A3 provider response | Confirmed UX defect; environment/root-cause evidence gap | Sanitized HTTP 502 is intentional, but the client discards useful classification and card Analyze does not open Edit until completion. NUC evidence is needed before changing parser/provider behavior. |
| A4 X video Save | Confirmed client reduction defect; environment evidence gap; handout contradiction | Native X video and GIF-like MP4 are supported by PRODUCT and ADR-0064. Do not hide Save. The service worker retains `failureCode`/`canRetry`, but `reduceXSaveOutcome()` discards them. The actual acquisition failure needs sanitized claim evidence. |

## Slice 1 — Editor suggestion state machine, A1, and in-modal analysis UX

**Goal**

Deliver A1, A3’s user-facing behavior, and B as one coherent editor-state slice:

- On Edit open, reveal the newest durable suggestion immediately.
- Remove the Load control.
- Dropdown selection immediately switches the revealed suggestion without a provider call or field promotion.
- Merge new in-session results into the same ordered suggestion-list model.
- Show existing mapped tags already in Current as visibly selected/already-added; clicking may announce that state but must not mutate.
- After removal, the same suggestion must become actionable and re-add exactly once.
- After Gallery-brain confirmation, open Edit immediately, establish the target workspace, then run analysis with an accessible indeterminate spinner inside the modal.
- Resolve success in place; keep sanitized actionable failure and explicit user retry in the modal.
- Retry must be manual, must reconfirm cloud upload, and must never loop automatically.

**Non-goals**

No bulk application, autosave, physical rename, provider selection/cost change, raw payload display, companion overlay revival, movie-flow redesign, or ordinary canonical-tag creation.

**Likely files**

- `src/framenest/adapters/api/web/app.js`
- `src/framenest/adapters/api/web/index.html`
- `src/framenest/adapters/api/web/styles.css`
- If adding sanitized parser-stage telemetry:
  - `src/framenest/infrastructure/ai/nvidia_nim.py`
  - `src/framenest/infrastructure/ai/vercel_gateway.py`

Tests:

- `tests/upload_cockpit_async_ownership.test.js`
- `tests/catalog_card_ai_quick_action.test.js`
- `tests/automatic_analysis_lifecycle.test.js`
- `tests/metadata_alias_edit.test.js`
- `tests/movie_identification_frontend.test.js`
- `tests/contract/test_local_web_application.py`
- `tests/contract/test_media_suggestion_api.py`
- `tests/contract/test_media_ai_suggestions_api.py`
- Telemetry tests, if implemented:
  - `tests/unit/infrastructure/ai/test_nvidia_nim.py`
  - `tests/unit/infrastructure/ai/test_vercel_gateway.py`

**Required behavioral tests before correction**

1. Suggested mapped tag already in Current: selected styling/`aria-pressed`, no duplicate and no dirty revision.
2. Remove that tag, rerender, click suggestion, and verify one re-add plus dirty revision.
3. Repeat click and verify no duplicate.
4. Unmapped tag in alias mode remains non-actionable.
5. Unmapped tag in canonical mode calls the capability-gated creation path and remains draft-only.
6. Newest durable run is revealed on open; dropdown switch changes strips immediately with zero provider POSTs.
7. Dirty workspace refusal results in no provider call.
8. Card confirmation acceptance opens the modal before the deferred provider response resolves.
9. Closing/switching media invalidates the response through request/media/location/workspace-revision/capability-revision fences.
10. Failure remains in-modal; manual retry reconfirms; success does not Save.

**Invariants**

Use only `textContent`/DOM construction. Preserve canonical-vs-alias Save ownership, dirty-switch confirmation, per-field copy, `metadata.canonical.write` for tag creation, `analysis.run` for provider invocation, confirmation before every invocation, no auto-save, and informational-only suggested filename.

User retryability is not root-cause diagnosis. A safe UI grouping is:

- Retry offered after `AI_PROVIDER_INVALID_RESPONSE`, unavailable, rate-limited, and generic provider failure, with context-appropriate copy.
- Configuration, missing credential, authentication, or model selection says operator action is needed; no claim that retry will repair it.
- Never expose raw provider text or parser exceptions.

**Provider evidence Michal would need later**

A single bounded failure episode, and at most one explicitly confirmed retry, should preserve:

- Exact deployed SHA and schema revision.
- Sanitized capability result: provider/model identifiers, configured/credential-available/status categories, prompt version, last safe status/test categories and timestamps.
- Browser response HTTP status and stable `error.code`, plus safe correlation identifier if present.
- A sanitized response-classification event containing only fixed enums such as HTTP status class, content type class, parser stage (`envelope_json`, `message_content`, `suggestion_json`, `suggestion_schema`), schema category, and terminal domain error.
- No response body, prompt, media identity/path, frame data, URL, header, or credential.

Interpretation:

- Configuration/capability issue: capability or auth/model error already classifies it.
- Likely transient provider output: one invalid-response classification followed by success under unchanged SHA/provider/model/prompt.
- Parser/schema drift: repeated failure at the same safe parser/schema stage under unchanged configuration, followed by a synthetic local fixture reproducer. Current generic-provider logs may not contain enough stage detail; absence of that evidence blocks a parser correction, not the UX slice.

**Verification**

```text
node --test tests/upload_cockpit_async_ownership.test.js tests/catalog_card_ai_quick_action.test.js tests/automatic_analysis_lifecycle.test.js tests/metadata_alias_edit.test.js tests/movie_identification_frontend.test.js
```

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline <EXACT_SLICE_BASELINE>
./.ap/ap exec --root /home/agile/Projects/framenest --baseline <EXACT_SLICE_BASELINE> --operation test-focus -- tests/contract/test_local_web_application.py tests/contract/test_media_suggestion_api.py tests/contract/test_media_ai_suggestions_api.py -q -p no:cacheprovider
```

**Docs/ADR**

A successor ADR is required because ADR-0077 explicitly prescribes Load and hide-on-dropdown-change, while ADR-0078 prescribes analyze before opening Edit. Update `README.md`, `PRODUCT.md`, `SPEC.md`, `GALLERY.md`, `ROADMAP.md`, `AI_WORKSPACE.md`, and `docs/X_COMPANION.md` where those living descriptions occur.

**Dependency, rollback, NUC acceptance**

No schema dependency. One frontend/contract commit is a clean rollback boundary; optional sanitized telemetry should be a separate commit. Michal should render-test newest-on-open, immediate dropdown switching, existing/remove/re-add tags under admin and ordinary identities, dirty-switch refusal, spinner timing, success, failure, manual retry, Cancel/no-Save, focus, keyboard behavior, and reduced motion.

The A1 remove/re-add reproducer is mandatory before broadening the tag correction. NUC provider evidence is not required for the editor UX but blocks any provider/parser root-cause patch.

## Slice 2 — Compact video handoff and honest animated pause/resume

**Goal**

- Keep the existing static preview visible while a video loads; hand off only after `loadeddata`/seek readiness, with error returning to the existing preview.
- Preserve video `currentTime` across pause/resume.
- Apply default cursor to video while preserving `role`, `tabindex`, keyboard activation, focus visibility, and `aria-pressed`.
- Implement true animated-image pause/resume through decoded frames rendered to canvas, retaining current frame and remaining delay while paused.

**Technical approach**

Prefer the browser-native `ImageDecoder`/canvas path for GIF animation, with sequential frame decoding, duration-based scheduling, explicit `VideoFrame.close()`, cancellation on teardown, and one active compact player. Pause cancels scheduling but retains decoder/frame/canvas state; resume continues from that state.

Do not use the representative-frame preview timer: it is not faithful animation playback. Do not describe native `<img>` source removal as pause.

If target Brave lacks usable animated `ImageDecoder`, the honest fallback is replay-from-start with truthful control wording. Cross-browser true resume would then require Michal to choose between:

- An audited client decoder dependency, increasing bundle/security/performance scope.
- Server media normalization/transcoding, which conflicts with current no-transcoding direction and needs a separate architecture decision.

**Likely files/tests**

- `src/framenest/adapters/api/web/app.js`
- `src/framenest/adapters/api/web/styles.css`
- `tests/gallery_gif_inline_toggle.test.js`
- `tests/gallery_details_playback_handoff.test.js`
- New focused decoder/controller Node test if existing harness cannot fake `ImageDecoder`
- `tests/contract/test_local_web_application.py`

**Invariants**

Identity-only content URLs, one active compact playback surface, no path exposure, bounded cleanup, no source-media mutation, no fake frame position, keyboard accessibility, and no new npm toolchain.

**Verification**

```text
node --test tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/<new-animated-controller-test>.test.js
```

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline <EXACT_SLICE_BASELINE> --operation test-focus -- tests/contract/test_local_web_application.py -q -p no:cacheprovider
```

**Docs/ADR**

Update `GALLERY.md`, `PRODUCT.md`, `SPEC.md`, and `README.md`. No ADR is necessary for a dependency-free browser-capability implementation. A decoder dependency or media-normalization change requires a separate ADR.

**Dependency, rollback, NUC acceptance**

Video handoff/cursor and GIF decoder should be separate commits within the slice so either can roll back independently. Michal must verify:

- No black frame before video readiness.
- Pause/resume continues near the stored video time.
- Default video cursor but retained keyboard/focus behavior.
- GIF freezes on a non-initial visible frame, stays frozen, and resumes from the following frame rather than frame zero.
- Fallback copy is truthful if decoder capability is absent.

NUC/Brave `ImageDecoder` capability blocks claiming true GIF acceptance, but not the video fix.

## Slice 3 — X terminal outcome truth and supported-video diagnosis

**Goal**

Reduce known, sanitized claim failures into useful messages and use `canRetry` honestly. Save remains available on native video/GIF-like MP4.

Where `canRetry=true`, wire an explicit retry through the existing server-owned retry route; never retry automatically. Unknown codes remain generic and sanitized.

**Likely files/tests**

Always:

- `extension/shared/messages.js`
- `extension/background/service_worker.js`
- `extension/content/x_adapter.js`
- `tests/x_companion_extension.test.js`

Conditional backend seam selected by terminal evidence:

- `src/framenest/domain/x_acquisition.py`
- `src/framenest/application/x_acquisition.py`
- `src/framenest/infrastructure/x/downloader.py`
- `src/framenest/infrastructure/x/status_bridge.py`
- `src/framenest/adapters/api/x_request_api.py`
- `tests/unit/application/test_x_acquisition_lifecycle.py`
- `tests/unit/infrastructure/test_x_downloader_adapter.py`
- `tests/unit/infrastructure/test_x_status_bridge.py`
- `tests/contract/test_x_request_api.py`
- `tests/contract/test_x_companion_api.py`
- `tests/integration/test_x_photo_acquisition_vertical_slice.py`

**Invariants**

Content script sends only the post URL and alias; service worker remains the FrameNest network client; server owns extraction/download targets; exact X/CDN allowlists remain; no caller-supplied fetch URL, cookies, X credentials, CORS widening, raw extractor output, or unsupported-video reclassification.

**Required NUC readback**

Michal needs a sanitized projection of the failed terminal claim:

- `state`, `phase`, `failure_code`, `can_retry`
- `discovered_asset_count`, `success_count`, `failure_count`
- Per asset: `ordinal`, `media_type`, `state`, `failure_code`
- Exact release SHA/schema and bounded structured-log events from the same time window

Exclude claim/media IDs unless needed for local correlation, and exclude URL, title, post text, author, filesystem path, raw extractor output, headers, and host details.

Failure code selects the correction seam:

- Inspect/status normalization: `X_NO_SUPPORTED_MEDIA`, `X_EXTRACTOR_MALFORMED`, post/protection classifications.
- Representation continuity: `X_SOURCE_MEDIA_CHANGED`.
- Acquisition: `X_DOWNLOAD_TIMEOUT`, `X_EXTRACTOR_FAILED`.
- Validation/policy: media type, codec, dimension, size.
- Handoff: `X_CATALOG_HANDOFF_FAILED`.
- Multi-asset: inspect asset-level codes before changing claim-wide aggregation.

**Verification**

```text
node --test tests/x_companion_extension.test.js
```

Then only the evidence-selected Python set through canonical AP execution.

**Docs/ADR**

Update `docs/X_COMPANION.md` and, if outcome wording is summarized there, `README.md`. No new ADR: ADR-0064 already owns native video and honest terminal outcomes.

**Dependency, rollback, NUC acceptance**

The client classification/retry commit is independently reversible. A backend correction must be a later evidence-selected commit, not speculation. Michal must test one supported video success, one retryable synthetic/real safe failure, and one non-retryable failure. Missing terminal evidence blocks the backend fix but not truthful client reduction.

## Slice 4 — One-list unread active slice and refresh diagnosis

**Goal**

Make the visible compact/active slice exactly the unopened analyzed items from the one aggregated history result:

- Render each media row once.
- Active slice contains all unopened analyzed rows within the existing bounded scroll surface.
- `All` exposes the remaining opened and, for ordinary own-history where retained, pending rows.
- Badge continues to use server `unopened_count`; aggregated unread row count must agree.
- Opening marks the exact run, removes it from active only after refresh, but retains it in All.
- A later successful run for the same media becomes unread again.

Retain immediate refresh on side-panel open and the visible 15-second poll. First add focused lifecycle/runtime evidence for open, visibility changes, polling, service-worker suspension, and render replacement. Do not add another timer.

If runtime evidence shows interval throttling or lifecycle loss, prefer a service-worker invalidation message after badge alarm/terminal Save/opened completion, with the visible sidebar performing the full refresh. Keep the timer only as a safety net.

**Likely files/tests**

- `extension/ui/sidebar.js`
- `extension/ui/sidebar.css`
- `extension/ui/sidebar.html`
- Possibly `extension/background/service_worker.js`
- `extension/shared/messages.js` only if adding an invalidation message
- `tests/companion_review_extension.test.js`
- `tests/x_companion_extension.test.js`
- `tests/companion_web_bridge.test.js`

**Invariants**

No duplicate rows, text-safe titles, server ordering, complete-list fail-closed pagination, actor-scoped opened state, badge privacy, hosted Details click, no legacy overlay revival, no new permission, and no opened write from hover/focus.

**Verification**

```text
node --test tests/companion_review_extension.test.js tests/x_companion_extension.test.js tests/companion_web_bridge.test.js
```

**Docs/ADR**

This semantics change supersedes the compact/newest-five parts of ADR-0073/0076 and requires the companion successor ADR described below. Update `docs/X_COMPANION.md`, `README.md`, `PRODUCT.md`, `SPEC.md`, and `ROADMAP.md`.

**Dependency, rollback, NUC acceptance**

This is an extension-only rollback boundary unless runtime evidence selects a service-worker message addition. Michal must test side-panel open refresh, externally completed analysis appearing without reopen, active/badge agreement, open-clears-active-but-retains-history, later-run-unread-again, no duplicates, and ordinary/admin isolation.

The reported staleness mechanism is not yet established. That evidence blocks changing refresh architecture, not the unread rendering semantics.

## Slice 5 — Ordinary contributor-scoped analyzed history

**Recommended interpretation**

Use the smaller, truthful rule:

> An ordinary actor receives an unread companion item when a successful administrator-run generic analysis exists for media attributed to that actor.

This reuses the successful analysis run as durable notification identity, the exact-run opened table, and existing upload/YouTube/X contribution stamps. It does not pretend proposal creation is approval and does not require proposal resolution state.

Under this interpretation, open proposals remain administrator attention records only. They neither run a provider nor gate notification. Ordinary full history may retain their contributed, cataloged items without a successful analysis as pending, but only successful unopened analysis increments the badge/active slice.

**Alternative requiring larger scope**

If “approval through Manage media” must be a distinct product event, add a durable proposal-resolution workflow:

- Admin approve/dismiss mutations and audit actions.
- Resolver/timestamp and resulting `analysis_run_id` linkage.
- Confirmation-before-provider and failure/retry states.
- Manage-media/analysis-proposal actions.
- Migration beyond `0033`.
- Notification only after approved analysis succeeds, not at approval click.

That is a separate architecture and migration slice.

**Likely files/tests for the recommended smaller path**

- `src/framenest/application/ports/companion_review_repository.py`
- `src/framenest/application/companion_review.py`
- `src/framenest/infrastructure/persistence/companion_review_repository.py`
- `src/framenest/infrastructure/persistence/media_attribution_repository.py`
- `src/framenest/adapters/api/companion_review_api.py`
- `src/framenest/adapters/api/tailscale_ingress.py`
- `src/framenest/adapters/api/application.py`
- Extension files from Slice 4 only if routing capability changes

Tests:

- `tests/unit/infrastructure/persistence/test_companion_review_repository.py`
- `tests/unit/application/test_companion_review.py`
- `tests/contract/test_companion_review_api.py`
- `tests/contract/test_tailscale_ingress_security.py`
- `tests/contract/test_x_route_policy.py`
- `tests/contract/test_workspace_media.py`
- `tests/contract/test_analysis_proposal.py`
- Node companion suites from Slice 4

Reuse/refactor the shared attribution query; do not duplicate X-only ownership joins. Own-history/opened authorization should move from X-only ownership to contributor-scoped upload/YouTube/X attribution, with uniform 404 for foreign or missing media.

**Invariants**

- Administrator inbox stays global under `media.workflow.read`.
- Ordinary history is actor-private and contributor-scoped.
- Public callers remain 404/absent.
- Ordinary users gain neither `analysis.run`, canonical write, inbox detail/apply, team aliases, nor publication.
- Opened and badge counts are actor-scoped.
- Movies remain excluded.
- Analysis proposals still call no provider unless the larger workflow is explicitly selected.
- Tailscale membership alone conveys no authority.
- Existing five companion mutations remain five; widening opened ownership/capability must preserve extension-origin and audit controls.

**Verification**

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline <EXACT_SLICE_BASELINE> --operation test-focus -- tests/unit/infrastructure/persistence/test_companion_review_repository.py tests/unit/application/test_companion_review.py tests/contract/test_companion_review_api.py tests/contract/test_tailscale_ingress_security.py tests/contract/test_x_route_policy.py tests/contract/test_workspace_media.py tests/contract/test_analysis_proposal.py -q -p no:cacheprovider
```

Then the Slice-4 Node command.

**Docs/ADR**

A successor companion ADR is required. It should explicitly supersede:

- ADR-0073/0076 newest-five compact semantics.
- ADR-0076’s X-only ordinary own-history and X-only opened ownership.
- Any stale statement equating proposal creation with analysis approval.

It should preserve ADR-0074 contributor-scoped audience extension, ADR-0077 alias boundaries, admin-only inbox/detail/apply, movie exclusion, actor-scoped exact-run opened state, and badge privacy.

**Concrete decision for Michal**

Should ordinary notification mean:

1. **Recommended:** any successful administrator-run generic analysis of media attributed to that user, while proposals remain non-executing attention records; or
2. An explicit Manage-media proposal approval/resolution lifecycle that must be added before analysis runs?

That choice blocks Slice 5 implementation. It does not block Slices 1–4.

**Rollback and NUC acceptance**

The recommended query/capability extension needs no migration and can roll back as one backend/extension/docs commit. Michal must test separate ordinary actors with X, upload, and YouTube contributions; foreign-user denial; admin global visibility; pending badge exclusion; opened isolation; later-run unread; public denial; and movie exclusion.

## Minimal implementation order

1. Slice 1: editor/A1/in-modal analysis, with its successor ADR and living docs.
2. Slice 2: video handoff plus animated decoder, retaining an internal video/GIF commit boundary.
3. Slice 3: X client outcome truth; add only the backend correction selected by NUC claim evidence.
4. Slice 4: unread active rendering plus focused refresh lifecycle evidence.
5. Obtain Michal’s single ordinary-workflow decision and accept the companion successor ADR.
6. Slice 5: contributor-scoped backend/authorization/history implementation, or the larger proposal-resolution workflow as a separately planned migration slice.

This keeps the defects batched by shared state surface and gives Michal small coherent rendered-test batches.

## Living documents likely affected

- `README.md`
- `PRODUCT.md`
- `SPEC.md`
- `GALLERY.md`
- `ROADMAP.md`
- `AI_WORKSPACE.md`
- `docs/X_COMPANION.md`
- `SECURITY.md` if opened capability/attribution or sanitized provider diagnostics change
- `SERVER.md` if the ordinary companion capability/query boundary changes

Do not touch the NUC runbook for this whole.

## Explicit out-of-scope protections

- NUC hardening, host bootstrap, firewall, SSH, storage, systemd, or non-routine deployment work.
- Publication, push, or NUC refresh without a later explicit grant.
- AP pin adoption or `.ap` changes.
- Funnel, router forwarding, public-listener, TLS, DNS, or companion public-origin work.
- Provider selection, model selection, cost policy, hidden fallback, bulk/historical analysis, or automatic retry.
- Secrets, credentials, private host values, raw provider responses, raw extractor output, private media, or private wrapper inspection.
- Caller-supplied X/CDN fetch URLs, content-script FrameNest networking, CORS widening, X cookies, or signed-in scraping.
- Media transcoding/normalization or a new decoder dependency without the named follow-on decision.

Logical whole: not closed. Planning authority expires with this report.
