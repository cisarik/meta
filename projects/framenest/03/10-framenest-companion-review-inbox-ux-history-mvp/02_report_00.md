[Archival note by ORCHESTRATOR, not part of the Worker report: Native Plan Mode
was active in the Worker client during session 02 / exchange 01, so the Worker
delivered its terminal report in chat. The Cooperator relayed a PARTIAL
transcription covering the frozen implementation plan (Worker report section 7)
and per-slice allowlists/validation ladders (section 8). Earlier sections
(coordinates echo, status line, gate evidence, capability statement, recon
citations) and the closing fields (justification, authority expiry) were not
included in the relay. The ORCHESTRATOR independently verified the plan's
load-bearing repository claims at baseline 0c71d07f before acceptance review.
Nothing below this note was added, removed, or edited.]

## 7. Frozen implementation plan

### Summary

Implement four commits in order: D1 merged pending/analyzed history, D2 best-effort `𝕏` seed and Save preselection, D3 union Apply with durable per-tag provenance, and D4 successor ADR/living documentation. D1 and D2 remain E2 and migration-free. Exact R4 provenance requires migration `0032`, so D3 is an E3 slice with migration rehearsal and independent staged-diff audit.

### 1. Merged-list DOM and CSS

- Remove `#review-inbox` and `#review-inbox-list`. Retain one title-bar `<button id="review-history-toggle">` with `aria-label="Toggle companion history"`, `aria-expanded`, and `aria-controls="review-history"`.
- Retain `<section id="review-history" hidden>` immediately below the title bar, containing only `<ol id="review-history-list" aria-label="Companion history">`.
- History starts collapsed on panel load. Expanding/collapsing changes only `aria-expanded` and the section’s `hidden` state. If the list becomes empty, force collapse, disable the toggle, and render no copy or layout height.
- Render native row buttons with base class `review-history-button` and exactly one state modifier:
  - `review-history-button--analyzed`: background `var(--accent)`/FrameNest `#00ff41`, dark text.
  - `review-history-button--pending`: existing dark/black row surface and light text.
- Keep Settings and Connect/Disconnect stacked above the full-title-bar toggle. Retain `#shell-status`, `.sidebar-main`, and the existing `#frame` node and flex behavior.
- Rendering, polling, 403 handling, and toggle operations must never call `clearFrame`, change `frame.src`, change `frame.hidden`, replace/move the iframe, or mount the review overlay inside it.

Rationale: the existing title-bar/iframe structure already supports a single zero-height collapsible section without touching iframe lifecycle.

### 2. Client predicates, dedupe, clicking, and badge

- Extend inbox sanitization to accept:
  - analyzed item: `analyzed === true`, UUID `analysis_run_id`, non-negative integer `completed_at_ms`, boolean `unopened`;
  - pending/failed item: `analyzed === false`, `analysis_run_id === null`, `completed_at_ms === null`, `unopened === false`;
  - every item: UUID `media_id`, non-empty `title`, non-negative integer `created_at_ms`.
- The service worker continues fetching all 100-row pages. It defensively deduplicates by `media_id`; an analyzed row replaces a pending duplicate. The server remains authoritative for row order, and the client does not independently sort.
- The sidebar renders every sanitized row exactly once. Green/dark is driven only by `analyzed`, not `unopened`, rendered position, or awaiting state.
- Any row opens the existing `ui/review.html#media=<uuid>` overlay. An analyzed detail follows the existing durable opened flow; a pending detail with no successful suggestion renders canonical/publication state, disables run selection, all Apply controls, and Save, displays `No successful analysis yet.`, and sends no opened mutation.
- A race in which analysis completes between list click and detail load follows the returned detail: a non-empty successful suggestion is treated as analyzed and marked opened.
- After analyzed opened success, refresh the merged list and badge. The row remains because there is no unread-only collection.
- Badge source remains only first-page `unopened_count`, with existing `1`…`99`/`99+` formatting. Pending rows never affect it. A 403 hides/collapses/disables history and clears the badge.

Rationale: explicit `analyzed` and nullable run fields avoid inferring row state from presentation data while preserving current badge semantics.

### 3. Server payload, query, ordering, and migration decision

Extend the existing `GET /api/companion/review-inbox`; add no route.

Each item becomes:

```json
{
  "media_id": "uuid",
  "title": "display or fallback title",
  "created_at_ms": 123,
  "analyzed": true,
  "analysis_run_id": "uuid-or-null",
  "completed_at_ms": 456,
  "unopened": true
}
```

- `analysis_run_id` and `completed_at_ms` are null only when `analyzed=false`; pending `unopened` is always false.
- Analyzed candidates remain the current latest successful generic v4 run per non-movie medium.
- Pending/dark candidates are cataloged X assets whose claim has `created_by_login_key == requesting administrator`, claim category is `meme`, media is not a movie, and no successful generic run exists. A failed or still-running run does not exclude the item.
- Deduplicate in SQL by excluding pending rows with an analyzed candidate. Analyzed wins for the same medium.
- `created_at_ms` is `logical_media.created_at_ms`, which the existing companion picker already treats as the catalog-created timestamp.
- Analyzed title fallback remains canonical display title then stored successful suggestion title. Pending fallback is canonical display title, then saved X claim title, then `X post <x_post_id>`.
- Define `activity_at_ms = completed_at_ms` for analyzed rows and `created_at_ms` otherwise. Order by `(activity_at_ms DESC, analyzed DESC, sort_id DESC)`, where `sort_id` is the analysis run ID for analyzed rows and media ID otherwise.
- Introduce a dedicated inbox cursor codec containing `{v:2, at_ms, analyzed, id}`. Continue accepting the legacy `{completed_at_ms,id}` cursor as an analyzed position; always emit v2. Keep the existing per-media suggestion-history cursor codec unchanged.
- Keep limits 25 default/100 maximum. `unopened_count` retains the current independent query, integer shape, and meaning on every page.

No D1 migration is needed: `logical_media`, `media_metadata`, `x_post_claims`, `x_assets`, and `media_analysis_runs` already contain ownership, category, catalog timestamp, titles, state, and run data.

Rationale: one mixed keyset query gives true global newest-first paging; concatenating two independently paginated sources would not.

### 4. `𝕏` seed and preselection

- Use fixed canonical pair `key="x"`, `display_name="𝕏"` (U+1D54F). No validator changes.
- Extend the existing `GET /api/canonical-tags` with optional enum query `surface=x-companion-save`; the response body remains unchanged.
- When that fixed surface is requested, invoke an application-level `EnsureCompanionXTag` use case before listing. It calls existing idempotent canonical creation with fixed constants only; the caller cannot provide a key/display.
- A matching existing definition is success. Concurrent identical creation remains idempotent.
- A conflicting existing `x` definition or seed-only repository failure is logged with sanitized context and does not fail the list request. The route still attempts the ordinary tag list. If listing itself fails, preserve the existing tags-unavailable response.
- Change the extension’s existing `CANONICAL_TAGS` path to `/api/canonical-tags?surface=x-companion-save`; add no message type or new route.
- After catalog load, Save finds the exact key/display pair and prepends it to `chosen` once. It renders as an ordinary removable chip and is submitted first unless deselected.
- If the fixed definition is absent because seeding conflicted/failed, do not synthesize a selected tag client-side; show the ordinary catalog result and keep Save usable without tags.
- Preserve Title→Tags→Description→Save, no category/source radios, no Analyze action, and no automatic focus change.
- Record explicitly that no future YouTube surface receives an analogous tag.

Rationale: a fixed first-use internal rule preserves “existing tags only” and avoids an operator prerequisite or generic caller-driven creation.

### 5. Union Apply and durable provenance

- Retain the request contract: `tag_keys` are the administrator-selected, mapped AI keys in suggestion order; at most five, distinct, and an ordered subsequence of that run’s eligible mapped keys.
- When Tags is selected:
  1. Load current canonical keys in stored position order.
  2. Start the result with all current keys unchanged.
  3. Append submitted AI keys not already present, in submitted/suggestion order.
  4. Re-enumerate positions from zero.
- The v4 five-tag limit continues to constrain only submitted AI keys. Manual/current tags survive, so the combined result may exceed five but never the canonical schema maximum of 32.
- If the deduplicated union exceeds 32, reject the entire transaction with HTTP 409 and code `COMPANION_REVIEW_TAG_LIMIT_CONFLICT`; do not truncate or remove manual tags.
- Keep the zero-tag rule exactly: selecting Tags requires at least one submitted AI key. Title/description-only Apply remains valid with an empty `tag_keys` array. If every submitted key already exists, Apply succeeds as a tag no-op.
- Add migration `0032_companion_review_tag_sources` with table `companion_review_tag_sources`:
  - primary key `(media_id, tag_key)`;
  - foreign keys to `media_metadata.media_id` with cascade, `canonical_tags.key` with restrict, and `media_analysis_runs.id` with cascade;
  - `analysis_run_id`, `applied_by_login_key`, and `applied_at_ms` checks matching existing receipt constraints.
- Do not reference `media_canonical_tags` directly: manual metadata saves currently delete/reinsert assignments, which would wrongly erase retained provenance.
- On Apply, insert a source row only for each newly appended key. Never attribute a pre-existing manual tag to the new run and never overwrite an older source when a later run proposes the same retained key.
- On manual web metadata Save, delete source rows only for keys removed from the submitted canonical vector. Preserve sources through reordering, unrelated field edits, and retained tags. Manual additions receive no AI source.
- Add `canonical.tag_sources`, keyed by tag key, to detail and Apply responses. Each value exposes run ID, run completion, provider/model, and applied time using the existing receipt presentation shape. Historical pre-0032 tags have no backfill and therefore no per-tag source.
- Retain the existing whole-field `field_sources.tags` receipt as “last successful Tags-field application against this final vector”; `tag_sources` is authoritative for which run added each surviving AI tag.
- Render tag-source entries in the existing review receipt panel.

Rationale: the current single tags-field receipt is overwritten and hashes the whole vector, so a narrow new relation is required to distinguish preserved manual tags from run-supplied additions.

### 6. ADR-0073 and living documentation

Create `ADR-0073: Companion Merged History Chrome, Pending Visibility, 𝕏 Seed Tag, and Preserving Apply`, dated 2026-08-24, with:

1. Context and accepted Cooperator revisions.
2. Mixed inbox payload/query, ordering, cursor, badge, privacy, and pending overlay behavior.
3. Single merged title-bar history and iframe guarantees.
4. Fixed `x`/`𝕏` first-use seed, best-effort failure behavior, and no YouTube analogue.
5. Preserve-and-append Apply algorithm, 5-versus-32 limits, zero-tag rule, 409 overflow, and migration `0032` provenance.
6. Preserved four `companion_mutation` routes, G2 readiness/publication, movie exclusion, ingest form, and hosted iframe.
7. Consequences, migration/backfill limits, compatibility, and operational risks.

Explicitly supersede only:

- ADR-0072 decisions 1–4 insofar as they prescribe separate unread/history lists, duplicate rows, analyzed-only history, and marking every row opened; also its “no JSON/schema change” consequence.
- ADR-0068 §1’s sentence “Tags replace, they do not union.” Preserve checkmarked-field behavior and zero-tag prohibition.
- Matching two-list and replace wording in `docs/X_COMPANION.md`, `SPEC.md`, `PRODUCT.md`, and `ROADMAP.md`.

Do not edit accepted ADR-0068 or ADR-0072. Update only the ADR index and living schema-head statements from `0031` to `0032`.

Rationale: successor treatment preserves immutable accepted history while narrowing supersession to the revised decisions.

### 7. Test scenarios

- D1 repository/API: mixed analyzed/pending population, other-user pending exclusion, failed/running dark rows, analyzed-over-pending dedupe, movie exclusion, title fallbacks, equal-timestamp ordering, mixed page boundaries, v2 and legacy cursor handling, unchanged unopened total, nullability, admin 403.
- D1 Node/MiniDom: one-list DOM/ARIA, green/dark classes, defensive dedupe, no client sorting, pending overlay disabled/no opened call, analyzed click/opened refresh, retained row, badge invariance, empty/403 state, cursor aggregation, and iframe identity/source survival.
- D2 Python: `x`/`𝕏` validator proof, created/already-exists behavior, concurrent idempotency, conflict and repository-error best effort, pure bare GET, fixed-surface query, unchanged response.
- D2 Node: fixed query path, exactly one default chip, first position, deselect/re-add, submitted key order, missing seed degradation, no form/radio/Analyze regression, no YouTube behavior.
- D3 repository/API: ordered union, duplicate suppression, retained manual tags, submitted maximum five plus combined greater than five, exactly-32 success, overflow atomic 409, zero-tag rule, no-op duplicate Apply, readiness/publication invariants, source insertion and response.
- D3 metadata/migration: retained/reordered source preservation, manual removal cleanup, manual re-add without source, rollback atomicity, empty and populated upgrade, no historical backfill, foreign-key behavior, downgrade to `0031`, and restored head.
- D3 Node: tag-source receipt rendering and unchanged selection/error retention.
- D4: ADR index/link review, exact supersession search, schema-head consistency, and stale two-list/replace wording removed only from living documents.

### 11. Risks and preserved contracts

- Mixed activity timestamps may reorder a saved row when analysis completes; this is intentional “newest activity” behavior.
- Fully aggregated history polling grows with catalog history and may observe concurrent inserts on the next poll; 100-row keyset pages, cursor-cycle protection, and fail-closed aggregation remain.
- Best-effort seeding uses an existing GET with a fixed surface-triggered internal write. A conflicting pre-existing `x` definition degrades to no default selection rather than overwriting user catalog data or blocking Save.
- Migration `0032` adds no historical per-tag backfill because old whole-field digests cannot safely distinguish manual from AI tags.
- D3’s E3 posture is mandatory despite the requested general E2 posture; weakening provenance to fit E2 would not satisfy R4.
- Ordinary identity 403 hiding and badge clearing remain intact.
- Hosted iframe identity/source and Gallery Attach remain intact.
- Ingest Save remains Title→Tags→Description→Save, with no radios or Analyze.
- G2 readiness-triggered publication, already-published preservation, movie exclusion, and generic v4 mapped-tag eligibility remain intact.
- Exactly four `companion_mutation` routes remain. The seed is a fixed behavior on the existing canonical-tag GET, not a new companion mutation route.
- No notification permission, manifest change, provider flag, NUC action, or YouTube tag is introduced.

Open implementation questions: none.

### 12. Public interface impact

- `GET /api/companion/review-inbox`: existing route; items add `created_at_ms` and `analyzed`; run/completion fields become nullable for pending rows. `unopened_count` remains byte-compatible.
- Inbox cursor: emitted opaque cursor becomes v2; legacy analyzed cursors remain accepted. Per-media history cursors are unchanged.
- `GET /api/canonical-tags`: optional `surface=x-companion-save`; unchanged response. No caller-controlled tag definition.
- Review detail and Apply responses: `canonical.tag_sources` added.
- Review Apply: tag semantics change from replacement to preserving union; new 409 code `COMPANION_REVIEW_TAG_LIMIT_CONFLICT`.
- Database: schema head `0032` adds `companion_review_tag_sources`; no D1/D2 migration.
- Extension internals: remove `#review-inbox`/`#review-inbox-list`; `#review-history` becomes the sole merged collection. No new message type, route, permission, or manifest entry.

Assumptions: automatic administrator analysis is enabled operationally as instructed; implementation remains local and unpublished until separately authorized.

## 8. Per-slice allowlists and validation ladders

### D1 allowlist

- `src/framenest/application/companion_review.py`
- `src/framenest/application/ports/companion_review_repository.py`
- `src/framenest/infrastructure/persistence/companion_review_repository.py`
- `src/framenest/adapters/api/companion_review_api.py`
- `extension/shared/messages.js`
- `extension/background/service_worker.js`
- `extension/ui/sidebar.html`
- `extension/ui/sidebar.js`
- `extension/ui/sidebar.css`
- `extension/ui/review.js`
- `tests/unit/application/test_companion_review.py`
- `tests/unit/infrastructure/persistence/test_companion_review_repository.py`
- `tests/contract/test_companion_review_api.py`
- `tests/companion_review_extension.test.js`

Validation commands use exact baseline `0c71d07f39026503268a90d4799aad6a27bfc0f7` for D1 and each slice's exact accepted parent SHA thereafter (symbolic placeholders are never passed to AP). Focused suites per slice, Node suites, diff checks, staged-path review, one commit per slice, no push.

### D3 audit gate

Before committing D3 (schema migration `0032`), stage the allowlist and obtain a fresh independent read-only audit of the staged migration, rollback, provenance cleanup, API compatibility, test evidence, and path set. Commit only after audit PASS.
