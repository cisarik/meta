### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-companion-ai-review-inbox-mvp  
Worker session ordinal: 01  
Worker exchange ordinal: 01

## 1. Terminal status and authority expiry

**Terminal status: BLOCKED**

- Phase-qualified result: implementation-planning-BLOCKED
- Logical-whole closure: not-closed
- Report justification: new-evidence
- No FrameNest, pinned AP, Meta, browser, provider, account, or NUC mutation occurred.
- Planning authority is expired.
- The architecture below is decision-complete. The formal exchange cannot be `PASS` because higher-priority Native Plan Mode prohibits filesystem mutation, while the task requires creating `/home/agile/meta/projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/01_report_00.md`. That file was not created.
- This is a report-delivery authority conflict, not an unresolved implementation decision.

## 2. Capability handshake

| Classification | Result |
|---|---|
| Requested | Fresh Worker; Native Plan Mode required; Extra High reasoning; no Max; single-active Worker; no delegation; E0 read-only planning; FrameNest/AP read-only; exact Meta report write only. |
| Directly observed | Native Plan Mode is active; filesystem exploration is available; no sub-agents were created; no implementation or external-system surface was activated. |
| Inferred | The reasoning route is consistent with the requested high/extra-high planning posture. |
| Unknown | Exact client model/SKU and a measurable “Extra High” state are not self-verifiable. Max was not indicated. |
| Authority law | Capability never grants implementation, browser, provider, deployment, publication, or closure authority. |

Later implementation should target **E3** because the whole introduces a migration, new administrator routes, companion-origin mutations, canonical metadata writes, and readiness-triggered publication. Independent INFOSEC R3 should occur after the behavioral slices converge and before any deploy, not in the first implementation Worker.

## 3. Exact baseline and evidence ledger

### Baseline

| Surface | Classification | Evidence |
|---|---|---|
| FrameNest local | Verified repository fact | `/home/agile/Projects/framenest`, branch `feat/x-meme-browser-companion`, HEAD `c581c0e6fa57391c1da40dd45e4bd224955a7f7d`, parent `af348847608fbb1e546d6db5e116e7ee81bacd9e`, tree `823c5650ac3db39a00b197fc2110c850b2bc0d35`, clean, no upstream configured. |
| FrameNest public | Verified public fact | `origin/main` remains `045f33b44897a6f3949cc515792336396f1d33a1`; no public advancement was found. |
| Pinned AP | Verified repository/public fact | Gitlink and checkout both `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`, detached and clean; AP public `main` is the same SHA. |
| Meta | Verified repository/public fact | Local and public `main` are `6dc659ccc3c93b235ef73431f0587f5ab36d2e4a`; only the expected `00_handout.md` and `01_planning_00.md` are untracked in this whole. |
| NUC | Historical context | Last recorded state: public FrameNest `045f33b`, schema 0029, empty companion origins, therefore live companion mutations fail closed. It was not re-probed. |
| Browser/account/provider | Later requirement | No signed-in browser, extension installation, X session, NIM call, credential probe, or provider readback was authorized or performed. |
| Active mutation | Verified repository fact | None owned by this Worker. |

### Material-claim classification

- **Cooperator decisions:** G2 publication, S1 layout, badge/list without notifications, administrator-only X auto-analysis, generic five-tag cap, movie exclusion, and no NUC deploy.
- **Verified repository facts:** current helper behavior, route capabilities, single-capability `RoutePolicy`, analysis history schema, publication readiness, metadata replacement semantics, sidebar/iframe design, ingest Save contract, and separate generic/movie prompt ownership.
- **Verified public facts:** Manifest V3 service workers can be terminated after inactivity, so ordinary timers are not durable scheduling primitives; Chrome recommends alarms for periodic work. The alarms API requires the `alarms` permission and alarms should be recreated defensively because persistence is not guaranteed across every restart. The existing manifest `action` surface supports badge APIs without adding notification permission. [Service-worker lifecycle](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers/lifecycle), [service-worker migration guidance](https://developer.chrome.com/docs/extensions/develop/migrate/to-service-workers), [alarms API](https://developer.chrome.com/docs/extensions/reference/api/alarms), [action API](https://developer.chrome.com/docs/extensions/reference/api/action).
- **Inference:** `media_analysis_runs.completed_at_ms` is the closest durable completion timestamp available; the provider does not return a distinct authoritative completion timestamp.
- **Selected proposals:** all new schemas, routes, response contracts, tag mapping, extension chrome, and implementation slices below.
- **Unresolved observation:** exact client reasoning SKU only; it does not affect the architecture.

## 4. Conflict ledger C1–C11

| ID | Disposition |
|---|---|
| C1 | Repository HEAD `c581c0e` wins. Workers 04/05 already landed; do not reissue overlay polish. |
| C2 | G2 wins over the handout’s G1 recommendation. |
| C3 | Notifications remain out; per-field checkmark plus review Save is the human publication gate. |
| C4 | Successor ADRs and living docs explicitly supersede the X “no automatic AI” statement for administrator-owned X acquisitions. |
| C5 | ADR-0044’s flag-enabled automatic path already permits standing consent. ADR-0020’s interactive `confirm_cloud_upload: true` remains unchanged. |
| C6 | Successor policy expands `companion_mutation` to review-opened and review-apply routes. Alias PUT is not reused. |
| C7 | G2 narrowly supersedes ADR-0049’s explicit-route-only publication rule after companion review Save; ordinary Gallery remains published-only. |
| C8 | Companion surfaces exclude movie. Website movie identification and genres remain intact. |
| C9 | Generic prompt becomes v4 with 1–5 tags. Catalog capacity remains 32 and movie-identification remains 12. |
| C10 | All six product forks are answered; no further Cooperator question is needed. |
| C11 | G2 is part of the apply transaction. Notifications and deployment remain separately parked. |

## 5. Current ownership map

| Concern | Current owner |
|---|---|
| X automatic-analysis exclusion | `application/x_acquisition.py::automatic_analysis_allowed_for_upload` |
| YouTube exclusion | Equivalent helper in `application/youtube_acquisition.py`; remains unchanged |
| Combined catalog policy | `_combined_analysis_allowed` in `adapters/api/application.py` |
| Durable suggestions | `media_analysis_runs`, migrations 0015/0017/0018, and `media_analysis_lifecycle.py` |
| Generic prompt | `application/media_suggestion.py` and `infrastructure/ai/prompts.py` |
| Movie identification | `application/movie_identification.py`, `domain/media_classification.py`, and `media_genres` |
| Canonical metadata | `application/media_metadata.py` and `persistence/media_metadata_repository.py` |
| Publication | `application/content_publication.py`, its repository, and `domain/content_publication.py` |
| Authorization/Origin/audit | `adapters/api/tailscale_ingress.py::RoutePolicy` |
| Side-panel host | `extension/ui/sidebar.*`; hosted website remains an iframe |
| Network client | `extension/background/service_worker.js` |
| Ingest Save | `extension/ui/save.*` and `extension/content/x_adapter.js`; frozen as a separate contract |

## 6. Selected product slice

In scope:

- Administrator-owned X catalog events may enqueue generic analysis when the global flag is enabled.
- Generic prompt v4 with at most five significant tags.
- Durable administrator inbox, history, opened state, and unopened count.
- S1 native side-panel list above the still-mounted hosted iframe.
- Toolbar badge, without OS notifications.
- Separate review overlay for Title, Tags, and Description.
- Per-field apply, durable provenance receipts, deterministic existing-tag mapping.
- G2 auto-publication after a valid review Save when readiness is met.
- Website Analyze-by-AI successes automatically join the same inbox.
- Movie exclusion and ingest Save regression protection.

Parked: notifications, NUC deployment/configuration, YouTube page `+`, YouTube automatic analysis, W2 taxonomy, ordinary-user analysis, movie companion UX, genres, persistent AI drafts, multi-model selection, CORS, broader host permissions, browser-store publication, and parent-whole closure.

## 7. Selected architecture and rejected alternatives

### Automatic-analysis policy

- Build the validated identity mapping before catalog-coordinator wiring and reuse the same mapping for ingress.
- Refactor the X helper to load the linked claim with `find_post_by_upload_id`.
- Effective law:
  - X-linked upload: allowed only when its normalized `created_by_login_key` currently maps to `ROLE_ADMIN`.
  - Null, unmapped, or ordinary owner: denied.
  - YouTube-linked upload: denied.
  - Unlinked upload: retains ADR-0044 behavior.
  - The existing scheduler’s `enabled` flag remains the final enqueue gate; default is false.
- No ordinary capability is expanded. Mapping is evaluated at catalog time, so demotion before catalog prevents enqueue.
- One run is scheduled per newly cataloged eligible asset, not retroactively when the flag changes.
- Missing provider configuration still creates durable lifecycle truth and finishes as `PROVIDER_NOT_CONFIGURED`; failed runs never enter the companion inbox.

### Durable state

Alembic **0031** will:

1. Add `ContentPublicationOrigin.COMPANION_REVIEW = "companion_review"` and rebuild the publication CHECK constraint.
2. Create `companion_review_open_states`:

   - `actor_login_key TEXT NOT NULL`, normalized login checks, maximum 254.
   - `media_id TEXT NOT NULL`.
   - `opened_run_id TEXT NOT NULL`.
   - `opened_at_ms INTEGER NOT NULL`.
   - Primary key `(actor_login_key, media_id)`.
   - Cascading foreign keys to logical media and analysis run.
   - Index on `opened_run_id`.

3. Create `companion_review_field_sources`:

   - `media_id`, `field_name`, `analysis_run_id`, `applied_by_login_key`, `applied_at_ms`, `value_digest`.
   - Primary key `(media_id, field_name)`.
   - `field_name` restricted to `display_title`, `tags`, or `description`.
   - Cascading media/run foreign keys, login/timestamp checks, and lowercase 64-character SHA-256 digest check.
   - Index on `analysis_run_id`.

4. Add successful-inbox and per-media-history indexes over analysis definition/state/profile/completion/id/media.

Downgrade refuses while either new table contains rows or any publication has origin `companion_review`; it must not silently discard review/publication history.

No second suggestion store is introduced.

### Inbox and history

- One inbox row per media, selected from the latest successful run satisfying:
  - `state = analyzed`
  - `analysis_definition = automatic_post_catalog`
  - result schema v1
  - `analysis_profile = generic_media` or historical `NULL`
  - non-null completion timestamp
  - `COALESCE(content_category, "general") != "movie"`
- A later failed run does not replace the latest earlier successful run.
- Ordering is `(completed_at_ms DESC, analysis_run_id DESC)`.
- Title is current nonblank canonical title, otherwise the stored suggestion title.
- Default limit 25, maximum 100. Fetch `limit + 1`.
- Cursor is opaque base64url canonical JSON containing `{completed_at_ms, id}`; invalid cursors return 422.
- `unopened_count` covers the entire filtered result, not only the returned page.
- A media is unopened when it lacks actor/media state or its latest successful run differs from `opened_run_id`.
- A new successful run therefore makes the media unread again.
- History uses the same successful generic filter for one media and the same keyset ordering/pagination.
- Website durable Analyze-by-AI uses the same definition/profile and therefore appears without a companion-specific enqueue path.

### Tag mapping and apply

For every stored suggested tag:

1. Trim/validate the stored value, then Unicode-casefold.
2. Match canonical display names:
   - one match → mapped;
   - more than one → `ambiguous`, with no key fallback.
3. If no display-name match, match casefolded canonical key:
   - one match → mapped;
   - otherwise `unknown` or `ambiguous`.
4. Deduplicate mapped keys in suggestion order; repeats are `duplicate`.
5. For historical results with more than five eligible mapped values, only the first five are selectable; later ones are `legacy_limit`.
6. Display every dropped value and reason. Never create a tag.

Tags ✅ replaces the complete canonical tag set with the remaining ordered mapped keys; it is not a union. If no mapped chip remains, Tags cannot be checked, preventing accidental clear-all. Explicit clearing remains website Edit behavior.

Title and description are copied server-side from the selected immutable run; the client never submits those strings. Applying tags uses normal `derive_collection_state`, so collection may change only as the catalog’s deterministic consequence of selected canonical tags—not from the NIM `collection` field. Category, source, creator, genres, filename, and other metadata are preserved.

Source digests use SHA-256 over UTF-8 canonical JSON: scalar JSON strings for Title/Description and the ordered JSON array of tag keys for Tags. A normal website metadata Save removes receipts only for fields whose digest changed. Readers additionally suppress any receipt whose digest no longer matches canonical state.

### S1 and review overlay

- Insert a native `review-inbox` section between existing sidebar status/header chrome and the existing iframe.
- Never unmount the hosted iframe; picker/Attach behavior remains intact.
- Show titles only, newest first, with a bounded scrolling list.
- Empty administrator state says “No analyzed items.” Ordinary identities receive 403, causing the section and badge to disappear without title leakage.
- Persist explicit collapse preference in extension storage. An empty inbox collapses automatically; a new item auto-expands only when the user has not explicitly dismissed the section.
- Open a local dialog containing sibling `review.html|js|css`; these files are not web-accessible resources.
- Dropdown copy is local-formatted `completed_at_ms · exact model_id · title`. It must be labelled as run completion time, not a provider-supplied timestamp.
- Switching runs resets checkmarks and removed chips and never writes.
- Save begins disabled; one or more selected fields enables it.
- Success keeps the overlay open, reloads canonical state/provenance/publication state, and clears selections. Error preserves selections.
- Use `textContent`/DOM nodes only. Parent/child messages require exact extension origin and source; network access remains service-worker-only.

### Badge and MV3 scheduling

- Add `"alarms"` and retain `"action"`; do not add `"notifications"`.
- Ensure a named one-minute alarm at service-worker startup, `onInstalled`, and `onStartup` whenever a valid FrameNest origin is configured.
- Reset/disconnect clears the alarm and badge.
- Each alarm performs one bounded inbox request and sets badge text to `1…99` or `99+`; zero, 403, disconnect, or request failure clears it.
- Side panel additionally polls every 15 seconds while visible and immediately after open/apply.
- Do not store titles or suggestion bodies in `chrome.storage`.
- A terminal successful X claim may retain only media IDs and a 30-minute “awaiting analysis” hint; the hint is removed when its media appears or the deadline passes. It is not opened-state truth and does not control the general one-minute badge alarm.

Rejected alternatives:

- G1/G3: conflict with selected G2.
- G4: would expose unpublished work through ordinary Gallery.
- S2: would replace the hosted iframe and threaten Attach.
- S3: would omit the required native list/badge loop.
- Notifications-first: unnecessary permission and UX expansion.
- Timer-only polling: unreliable across MV3 worker suspension.
- Auto-apply at catalog: removes the human gate.
- Reusing ingest `save.js`: conflates two independent contracts.
- Ordinary analysis/canonical/publish capabilities: privilege escalation.
- YouTube auto-analysis: outside the accepted policy.
- Movie/genres in companion: wrong application boundary.
- `chrome.storage`-only opened state: not durable server truth.
- Alias PUT apply: wrong ownership and capability.
- Tag union or tag creation: ambiguous apply semantics and larger trust surface.
- A second suggestions table: duplicates durable run history.

## 8. HTTP, capability, mutation, and audit matrix

Extend `RoutePolicy` with `additional_capabilities: tuple[str, ...] = ()`. Authorization must require the primary capability and every additional capability. Existing policies remain source-compatible. Audit records retain the primary capability; the distinct action identifies companion apply.

| Method/path | Required capability | `companion_mutation` | Audit | Contract |
|---|---|---:|---|---|
| `GET /api/companion/review-inbox?limit=&cursor=` | `media.workflow.read` | false | none, to avoid poll-generated audit floods | Returns `{items, unopened_count, next_cursor}`. Each item has `media_id`, `title`, latest `analysis_run_id`, `completed_at_ms`, and `unopened`. |
| `GET /api/companion/review-inbox/{media_id}?limit=&cursor=` | `media.workflow.read` | false | none | Returns current canonical values, publication state, valid field-source receipts, suggestion history, and cursor. |
| `POST /api/companion/review-inbox/{media_id}/opened` | `media.workflow.read` | true | `companion.review.open` | Body `{analysis_run_id}`. Marks only the run actually displayed; advancement is monotonic and cannot overwrite a newer opened marker with an older one. |
| `POST /api/companion/review-inbox/{media_id}/apply` | primary `media.content.publish`; additional `metadata.canonical.write` | true | `companion.review.apply_publish` | Body `{analysis_run_id, fields, tag_keys}`. Performs partial apply, receipts, readiness, and optional publication atomically. |

Rules:

- New POSTs require exact configured companion Origin or the ordinary hosted origin, plus `X-FrameNest-Request: 1`.
- Empty `companion_extension_origins` fails closed.
- GETs remain identity/capability protected without inventing a second Origin policy.
- Both ingress and handler verify apply capabilities.
- `fields` is a unique nonempty subset of `display_title`, `tags`, `description`.
- `tag_keys` must be empty unless Tags is selected; when selected it must contain 1–5 unique keys forming an ordered subsequence of the server’s current eligible mapping.
- Missing media/run: 404. Malformed request/cursor: 422. Movie, wrong run, or stale mapping: sanitized 409. Catalog unavailable: 503. Repository failure: sanitized 500.
- All responses are `Cache-Control: no-store`.
- No alias PUT and no CORS are involved.

Apply returns HTTP 200 for every valid transaction, including not-ready:

```json
{
  "metadata_status": "created|updated|unchanged",
  "canonical": {
    "display_title": "string|null",
    "description": "string|null",
    "tags": [{"key": "string", "display_name": "string", "position": 0}],
    "field_sources": {
      "display_title": null,
      "tags": {
        "analysis_run_id": "uuid",
        "completed_at_ms": 0,
        "provider_id": "string",
        "model_id": "string",
        "applied_at_ms": 0
      },
      "description": null
    }
  },
  "publication": {
    "status": "published|already_published|not_ready",
    "state": "published|unpublished",
    "origin": "companion_review|null",
    "published_at_ms": null,
    "ready": false,
    "missing_fields": ["display_title", "description", "tags"]
  }
}
```

Suggestion detail includes `analysis_run_id`, `completed_at_ms`, provider/model/prompt identifiers, Title, Description, and tag entries with `mapped`, `unknown`, `ambiguous`, `duplicate`, or `legacy_limit` status. It never exposes collection, filename, source, category, or genres.

## 9. Five-tag prompt and historical compatibility

- New identifier: `framenest-media-suggestion-v4`.
- `TAG_MIN_COUNT = 1`; `TAG_MAX_COUNT = 5`.
- Result schema remains `framenest-media-suggestion-result-v1`.
- Prompt instruction:

  > Return 1 to 5 concise English display tags that are most significant for storing this GIF, image, or video. Quality matters more than quantity. Prefer 3 to 5 only when supported by visual evidence. Prioritize important subjects, actions, emotions, and context; omit weak, redundant, speculative, or filename-derived tags. Never return more than five.

- Existing anti-injection and structured-output requirements remain.
- New provider output rejects zero or more than five tags.
- Historical v3 result JSON remains readable through a dedicated stored-result codec bounded at the historical maximum of 12; it must not be reconstructed through the new `MediaSuggestion` validator.
- Historical tags beyond five remain visible but are marked `legacy_limit` and cannot be applied.
- Update active v3 pins to v4. Preserve v3 strings used deliberately as migration/history fixtures.
- Website non-movie Analyze-by-AI uses the same v4 contract.
- Movie prompt version and its maximum of 12 remain unchanged.

## 10. Movie exclusion

- Exclude `analysis_definition = movie_identification` regardless of category.
- Exclude any media whose current canonical category is `movie`, even if it has an older generic run.
- Recheck category inside the apply transaction; a concurrent change to movie returns 409 without mutation.
- No genre, category, acquisition-source, collection-suggestion, or filename controls appear in the companion.
- Generic X analysis is not given a movie-specialization branch; the companion exclusion is the boundary.
- Future movie identification/genres belong to a separate movie application. The parked W2 meme/still/short/movie taxonomy remains parked.

## 11. G2 transaction and publication origin

`POST .../apply` uses one SQLite `BEGIN IMMEDIATE` transaction:

1. Load and validate current media, category, selected successful generic run, and actor.
2. Decode the stored suggestion with the historical-compatible codec.
3. Recompute canonical tag mapping and validate submitted keys.
4. Apply only selected fields, preserving all others.
5. Upsert receipts for selected fields, including identical-value selection from a newer source run.
6. Derive readiness using the existing domain function and stable missing-field order: `display_title`, `description`, `tags`.
7. If ready and unpublished, insert publication with origin `companion_review`.
8. If already published, preserve its original timestamp/origin.
9. Commit once.

A database failure rolls back metadata, receipts, and publication together. Middleware audit must already have succeeded before entering the transaction.

Not-ready is a successful metadata transaction with no publication. Publication never occurs on analysis completion, X ingest Save, row opening, or run selection. Existing website Publish remains available. Ordinary Gallery remains published-only.

## 12. Successor ADR outlines

All are initially **Proposed** and are new files; accepted ADR bodies remain untouched.

1. **0066 — Administrator-Owned X Automatic Generic Analysis**
   - Supersedes the X-specific no-auto-analysis statement.
   - Allows current administrator-mapped claim owners when the server flag is on.
   - Preserves ordinary/YouTube denial, default-off flag, interactive confirmation, server credentials, and no retroactive backfill.

2. **0067 — Administrator Companion Review Inbox and Mutation Trust**
   - Supersedes the “exactly two companion mutations” freeze in ADR-0061/0064.
   - Defines administrator-only inbox/history/open/apply routes, durable opened state, Origin/header protection, dual apply capabilities, and no CORS/alias reuse.

3. **0068 — Companion Review Save and Readiness-Triggered Publication**
   - Narrow successor to ADR-0049.
   - Defines G2, atomicity, `companion_review` origin, audit-before-write, idempotence, and published-only Gallery.
   - Defers other automatic publication.

4. **0069 — Five-Tag Generic Media Suggestion Contract**
   - Successor note for ADR-0016.
   - Defines v4, 1–5 significant tags, unchanged result schema, and readable v3 history.
   - Leaves movie identification untouched.

5. **0070 — Companion Exclusion of Movie Workflows**
   - Supplements ADR-0045.
   - Excludes movie category, movie-identification runs, and genres from companion routes/UI.
   - Defers them to the future movie application.

6. **0071 — Native Side-Panel Review Inbox Chrome**
   - Narrow successor to ADR-0063’s iframe-only chrome.
   - Keeps the iframe/Attach host while adding native inbox, local review dialog, badge, and alarms.
   - Explicitly excludes notifications.

## 13. Threat model and residual-risk owners

- X DOM text already seeds unpublished canonical metadata; NIM is a second untrusted input channel.
- No NIM value reaches canonical storage without a field checkmark and review Save. The server copies stored run values rather than accepting client text.
- G2 amplifies a deliberately accepted bad selection. Structural readiness is not semantic quality. This residual risk belongs to the **Cooperator**.
- Companion Origin is a CSRF-equivalent control, not authorization. Verified identity and administrator capabilities remain mandatory.
- The **Orchestrator** owns preventing accidental capability expansion to ordinary identities.
- Tag collisions, unknown values, duplicates, historical overflow, and client tampering are resolved by deterministic mapping plus server-side revalidation.
- Opened state is actor-specific and run-specific; the displayed-run request prevents a race from marking an unseen later run as opened.
- Extension messages, UUIDs, fields, cursors, and tag keys are untrusted and validated at every boundary.
- UI uses safe DOM APIs; no provider output enters `innerHTML`.
- Logs and audit events must not include suggestion/canonical title, description, tags, raw result JSON, private media URLs, bytes, cookies, authorization headers, or credentials.
- Badge leakage is limited to a count in the local browser profile and is cleared on disconnect/auth/error.
- Provider cost is real for each newly cataloged eligible admin X asset while enabled. Default-off configuration and no historical backfill are mandatory.
- Receipt invalidation/digest verification prevents stale provenance.
- Independent INFOSEC R3 later owns final adversarial validation of the new trust boundary.

## 14. Tests and verification ladder

### W02 policy/prompt gate

Start with:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline c581c0e6fa57391c1da40dd45e4bd224955a7f7d
```

Then:

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline c581c0e6fa57391c1da40dd45e4bd224955a7f7d --operation test-focus -- tests/unit/application/test_media_suggestion.py tests/unit/application/test_media_analysis_lifecycle.py tests/unit/application/test_x_automatic_analysis_policy.py tests/unit/infrastructure/ai/test_nvidia_nim.py tests/unit/infrastructure/ai/test_vercel_gateway.py tests/unit/test_configuration.py tests/integration/test_youtube_acquisition_lifecycle.py tests/contract/test_media_suggestion_api.py tests/contract/test_automatic_analysis_privacy_contract.py tests/contract/test_local_web_application.py -q -p no:cacheprovider
```

Required cases:

- Flag off plus admin X: no enqueue.
- Flag on plus administrator X: generic enqueue.
- Flag on plus ordinary/null/unmapped X: no enqueue.
- YouTube remains denied; unlinked behavior remains.
- Missing provider becomes durable failed run.
- Prompt/version/cap are exact; zero and six tags fail.
- Movie prompt/version remains unchanged.
- Deliberate historical v3 fixtures remain v3.

### W03 schema/read gate

- Fresh database to 0031; populated 0030 to 0031; foreign-key verification.
- Downgrade empty state succeeds; populated review/publication state refuses.
- Latest successful generic per media, movie exclusion, failed-later behavior, website Analyze inclusion.
- Keyset boundaries, total unopened count, actor isolation, new-run unread behavior.
- Historical v3 decoding and visible drop reasons.
- Admin success, ordinary 403, sanitized malformed/corrupt-result failures.
- Update only assertions meaning “current head” from 0030 to 0031; preserve tests intentionally migrating to historical 0030.

### W04 mutation/G2 gate

- Displayed-run opened state and monotonic stale-open handling.
- Origin/header fail-closed behavior and exact companion mutation set.
- Both apply capabilities required; alias capability insufficient.
- Per-field writes and preservation of unchecked fields.
- Tags replace, ordered subsequence validation, mapping ambiguity, no create-tag, no zero-tag apply.
- Receipt creation, same-value source update, website-change invalidation, digest defense.
- Ready publication, stable missing-field order, already-published idempotence, movie race rejection, and atomic rollback.
- Audit failure prevents DB mutation.

### W05/W06 extension gate

```text
node --test tests/x_companion_extension.test.js tests/x_acquisition_cockpit.test.js tests/companion_review_extension.test.js
```

Cover manifest permissions, alarm lifecycle, badge clearing/counts, ordinary hiding, S1 layout, iframe survival, polling visibility, dialog messaging, dropdown switching, checkmarks, chip removal, disabled Save, stay-open result handling, safe DOM rendering, and ingest Save invariants:

- Title → Tags → Description → Save.
- No radios/Analyze.
- Save enabled.
- Host Enter submits; Description Enter inserts newline; highlighted tag suggestion is accepted.
- `#url=` only and POST remains `{url, alias}`.
- No changes to acquisition-time first-catalog seed behavior.

Do not run `tests/browser_companion_evidence.test.js` in the first Worker. Do not call a live provider or browser.

After all local slices, run the affected Python set and one AP-mediated broad suite once, then the JS suite. Independent INFOSEC R3 follows before deploy consideration.

## 15. Exact proposed paths and owner map

### Policy, prompt, and ADRs

- `docs/adr/README.md`
- `docs/adr/0066-administrator-owned-x-automatic-generic-analysis.md`
- `docs/adr/0067-administrator-companion-review-inbox-and-mutation-trust.md`
- `docs/adr/0068-companion-review-save-and-readiness-triggered-publication.md`
- `docs/adr/0069-five-tag-generic-media-suggestion-contract.md`
- `docs/adr/0070-companion-exclusion-of-movie-workflows.md`
- `docs/adr/0071-native-side-panel-review-inbox-chrome.md`
- `src/framenest/application/media_suggestion.py`
- `src/framenest/infrastructure/ai/prompts.py`
- `src/framenest/application/x_acquisition.py`
- `src/framenest/adapters/api/application.py`
- `src/framenest/adapters/api/web/app.js`

### Companion server and schema

New:

- `src/framenest/application/companion_review.py`
- `src/framenest/application/ports/companion_review_repository.py`
- `src/framenest/infrastructure/persistence/companion_review_repository.py`
- `src/framenest/adapters/api/companion_review_api.py`
- `src/framenest/infrastructure/persistence/alembic_environment/versions/0031_companion_review_inbox.py`

Changed:

- `src/framenest/infrastructure/persistence/catalog_schema.py`
- `src/framenest/domain/content_publication.py`
- `src/framenest/infrastructure/persistence/media_metadata_repository.py`
- `src/framenest/adapters/api/tailscale_ingress.py`
- `src/framenest/adapters/api/application.py`

### Extension

- `extension/manifest.json`
- `extension/shared/messages.js`
- `extension/background/service_worker.js`
- `extension/ui/sidebar.html`
- `extension/ui/sidebar.js`
- `extension/ui/sidebar.css`
- New `extension/ui/review.html`
- New `extension/ui/review.js`
- New `extension/ui/review.css`

`extension/ui/save.*` and `extension/content/x_adapter.js` remain unchanged unless a later Worker proves a CSS-token-only extraction is strictly smaller and passes every ingest regression.

### New principal tests

- `tests/unit/application/test_x_automatic_analysis_policy.py`
- `tests/unit/application/test_companion_review.py`
- `tests/unit/infrastructure/persistence/test_companion_review_repository.py`
- `tests/integration/persistence/test_companion_review_migration.py`
- `tests/contract/test_companion_review_api.py`
- `tests/companion_review_extension.test.js`

Update relevant existing prompt/provider/lifecycle, metadata, publication, route-policy, configuration, and companion regression tests.

Current-head assertions must be updated selectively in:

- `tests/integration/test_persistence_migrations.py`
- `tests/integration/test_process_sigterm_lifecycle.py`
- `tests/integration/persistence/test_device_registry_migration.py`
- `tests/integration/persistence/test_library_registry_migration.py`
- `tests/integration/persistence/test_media_catalog_migration.py`
- `tests/integration/persistence/test_media_cover_migration.py`
- `tests/integration/persistence/test_media_metadata_migration.py`
- `tests/integration/persistence/test_media_user_alias_overlay_migration.py`
- `tests/integration/persistence/test_upload_publication_migration.py`
- `tests/integration/persistence/test_upload_session_migration.py`
- `tests/integration/persistence/test_x_requested_category_migration.py`
- `tests/integration/persistence/test_x_requester_acquisition_migration.py`
- `tests/integration/persistence/test_content_publication_migration.py`
- `tests/integration/persistence/test_populated_0015_upgrade_to_0017.py`
- `tests/unit/infrastructure/backup/test_catalog_backup.py`
- `tests/unit/infrastructure/runtime/test_production_runtime.py`
- `tests/contract/test_persistence_cli.py`

### Living documentation

- `PRODUCT.md`
- `SPEC.md`
- `ROADMAP.md`
- `SERVER.md`
- `SECURITY.md`
- `docs/X_COMPANION.md`

## 16. Causal implementation slices and later grants

1. **W02 — ADRs, policy, prompt, enqueue**
   - Extra High, E3 whole posture, no browser/provider/NUC.
   - Gate: v4 and administrator-owned X policy proven; YouTube/ordinary/default-off unchanged.

2. **W03 — Migration and read model**
   - Add complete 0031 schema, historical codec, repository, list/detail GET routes, and current-head updates.
   - Gate: one-row/media inbox, pagination, history, movie exclusion, actor-specific unopened calculation.

3. **W04 — Open/apply/G2 server mutations**
   - Add opened and apply routes, multi-capability RoutePolicy, receipts, partial writes, transaction, publication, and audit tests.
   - Gate: fail-closed Origin/capabilities and atomic G2 behavior.

4. **W05 — Native inbox and badge**
   - Add alarms, service-worker requests, badge, native S1 list, collapse/empty/error behavior.
   - Gate: ordinary identities hidden, iframe/Attach preserved, no notifications.

5. **W06 — Review overlay**
   - Add local review files, history dropdown, field controls, mapped chips, apply result/provenance/publication state.
   - Gate: stay-open workflow and all ingest regressions.

6. **W07 — Living-doc convergence**
   - Update product, spec, roadmap, server, security, and companion docs from implemented truth.
   - Gate: no contradictory “X never auto-analyzes,” “two mutations only,” “explicit publication only,” “iframe-only,” or “4–10 tags” wording remains.

7. **Later INFOSEC R3**
   - Independent review after W06, before production configuration/deploy.

8. **G — Notifications**
   - Parked; requires a separate product and permission decision.

9. **K — NUC deployment**
   - Parked; requires a separate deployment prompt and acceptance evidence.

Each implementation Worker starts from the exact accepted predecessor HEAD, a clean canonical checkout, and the same AP gitlink. A baseline change affecting these owners triggers re-planning rather than silent adaptation.

## 17. Recommended routes and first implementation allowlist

### Immediate report-completion repair

Because this exchange could not write the required report, the first routing action after approval is a mechanical report-rendering repair:

- Same healthy planning Worker context, next exchange.
- Native planning mode: `not-used`.
- Authority limited to copying this frozen artifact to the exact Meta report path.
- No new planning, repository edits, tests, implementation, or external access.
- No second architecture decision is required.

### First implementation Worker

- Route: `fresh-worker-session`
- Native planning mode: `not-used`
- Reasoning: Extra High
- Max: off
- Topology: single-active, no delegation
- Checkout: canonical `/home/agile/Projects/framenest`
- Starting baseline: `c581c0e6fa57391c1da40dd45e4bd224955a7f7d`, unless the approved report-render step records a clean descendant; any descendant must be explicitly substituted.
- Live provider, browser, NUC, deploy, push, and INFOSEC R3: not authorized.

Exact first allowlist:

```text
docs/adr/README.md
docs/adr/0066-administrator-owned-x-automatic-generic-analysis.md
docs/adr/0067-administrator-companion-review-inbox-and-mutation-trust.md
docs/adr/0068-companion-review-save-and-readiness-triggered-publication.md
docs/adr/0069-five-tag-generic-media-suggestion-contract.md
docs/adr/0070-companion-exclusion-of-movie-workflows.md
docs/adr/0071-native-side-panel-review-inbox-chrome.md
src/framenest/application/media_suggestion.py
src/framenest/infrastructure/ai/prompts.py
src/framenest/application/x_acquisition.py
src/framenest/adapters/api/application.py
src/framenest/adapters/api/web/app.js
tests/unit/application/test_media_suggestion.py
tests/unit/application/test_media_analysis_lifecycle.py
tests/unit/application/test_x_automatic_analysis_policy.py
tests/unit/infrastructure/ai/test_nvidia_nim.py
tests/unit/infrastructure/ai/test_vercel_gateway.py
tests/unit/test_configuration.py
tests/integration/test_youtube_acquisition_lifecycle.py
tests/contract/test_media_suggestion_api.py
tests/contract/test_automatic_analysis_privacy_contract.py
tests/contract/test_local_web_application.py
```

The Worker must preserve deliberate v3 migration/history fixtures and may not expand the allowlist without returning to the Orchestrator.

## 18. Parked scope, assumptions, deploy annex, and stop conditions

### Assumptions/defaults frozen

- Current role mapping at catalog time decides X administrator eligibility.
- One-minute alarm cadence is selected for broad Chrome/Brave compatibility.
- Opened state is per normalized administrator login and media, referencing the displayed run.
- Tags replace rather than union; zero-tag companion apply is forbidden.
- `companion_review` is the publication origin.
- No architectural question remains open.

### Deploy annex — checklist only, not authorized

A future deployment grant must:

1. Run `framenest-release status`.
2. Confirm the chosen release SHA, backup, migration path through 0030 to 0031, companion origin, `x_acquisition_root`, and NIM systemd credential presence without exposing secrets.
3. Run `framenest-release check --release <SHA>`.
4. Use a separate `deploy --yes` action.
5. Keep automatic analysis disabled until local UX and INFOSEC acceptance.
6. Enable the flag only in a separate configuration turn with restart and sanitized readback.
7. Inspect `~/framenest_routine.fish` read-only only if that later prompt grants it.

### Stop conditions

Stop without repair if the FrameNest checkout becomes dirty, the AP gitlink changes, migration head advances, a conflicting companion/review implementation lands, identity/capability semantics change, or any Worker would need browser/provider/NUC authority not present in its prompt.

## 19. Smallest next Orchestrator action

Issue one decision only: **approve this frozen architecture or request one targeted revision**. Approval routes the mechanical Meta report-render repair described above; it does not authorize implementation.

## 20. Execution issues and pre-existing failures

### Resolved Execution Issues / Near-Misses

- Reconciled the stale handout baseline with actual clean HEAD `c581c0e`; no overlay work will be reissued.
- Separated new v4 validation from historical v3 decoding, preventing durable history from becoming unreadable.
- Changed mark-opened from an empty request to the displayed `analysis_run_id`, closing the unseen-new-run race.
- Kept G2 inside one metadata/receipt/publication transaction.
- Detected and obeyed the Native Plan Mode/report-write authority conflict; no unauthorized Meta mutation occurred.

### Pre-Existing Failure Classification

`none` — no test or runtime failure was observed. The historical fail-closed NUC state is expected configuration, not a defect in this planning exchange.
