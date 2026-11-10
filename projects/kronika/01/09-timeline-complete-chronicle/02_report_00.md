### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: timeline-complete-chronicle
Worker session ordinal: 02
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Worker-Executed Preflight
Phase: Preflight
Task identity: KRN-TCC-PREFLIGHT-01 — read-only E3 preflight of the accepted complete Timeline chronicle plan
status: PASS
Phase-qualified result: not-applicable
Start commit: b66ec8f50860ace624f6be1fd3ad63f521edcd33
End commit: b66ec8f50860ace624f6be1fd3ad63f521edcd33
Report justification: new-evidence
Logical-whole closure: not-closed
```

Preflight verdict: **PASS**. The accepted plan in `01_report_02.md` is implementable inside its allowlist. Its security and aggregation claims match the repository at `b66ec8f50860ace624f6be1fd3ad63f521edcd33`. The inventory-test side effect, the source rollback, and the absence of a schema or host prerequisite are understood. No material prerequisite is missing and no plan correction is required.

This PASS recommends a separately authorized implementation. It does not authorize implementation, publication, deployment, acceptance, or closure.

## Re-measured repository and AP gate

Measured in this exchange, before the plan comparison. The checkout is a standalone directory Git repository at `/Users/agile/Projects/kronika` (`.git` is a directory, not a file or symlink).

| Gate | Measured | Prompt expectation | Result |
|---|---|---|---|
| Branch | `main` | `main` | match |
| HEAD | `b66ec8f50860ace624f6be1fd3ad63f521edcd33` | same | match |
| `refs/remotes/origin/main` | same SHA | same | match |
| Public `refs/heads/main` via `git ls-remote origin refs/heads/main` | same SHA | same | match |
| `git merge-base HEAD origin/main` | same SHA | — | equal |
| Working tree | `git status --porcelain=v1` empty, including untracked | clean | match |
| Containing `.ap` gitlink | `d7023cf037f6d17885c3ede5c04812c61640da50` | same | match |
| `.ap` HEAD | same SHA, detached `HEAD` | same | match |
| `./.ap/ap doctor` | PASS, governing variant `stable`, submodule clean | PASS, `stable` | match |
| `./.ap/ap project check --root /Users/agile/Projects/kronika --baseline b66ec8f50860ace624f6be1fd3ad63f521edcd33` | PASS, CPython 3.13 | PASS | match |
| Index / HEAD / `main` locks | absent | no active mutation | match |
| This report path before the write | absent | absent | match |

`ap project check` printed `WARN sanitized inherited environment classes: GIT_CONFIG_VALUE_0 SSH_AUTH_SOCK PATH GIT_CONFIG_KEY_0 GIT_CONFIG_COUNT` and then `PASS`. The prompt's parenthetical names `SSH_AUTH_SOCK` and `PATH`. This shell also inherited Git config-injection class names. No values were printed. The gate result matches. This is not a repository-state contradiction and it did not stop the preflight.

HEAD subject is `fix: keep card previews across visibility changes`. No deployment lock and no Kronika source mutation were present. NUC state was not contacted and is not revalidated.

The upgrade-ledger file still records `consumer-declared-execution-and-capability-route-binding` as `accepted`, `non-authorizing`, `retain-active`, last revalidated against `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`. This preflight did not revalidate or change that entry.

## Accepted decision and plan integrity

`00_notes.md` records that the Cooperator accepted ADR-0087 in the exact semantics of `01_report_02.md` §3 on 2026-11-09, and that the plan disposition after that acceptance is approved for this preflight. Implementation authority is still absent there. The plan file is present and was read in full. Its technical plan is complete; its own `PARTIAL` records only the earlier Plan Mode write limitation.

The proposed ADR path `docs/adr/0087-complete-visibility-aware-timeline-chronicle.md` is not tracked. `docs/adr/0086-companion-youtube-save-upload-message-and-preview-backfill.md` is the latest numbered Kronika ADR. ADR-0082 through ADR-0086 are tracked. The ADR-0083 sentence at `docs/adr/0083-modular-research-providers-and-administrator-curated-timeline.md` lines 210–211 is the sentence the plan supersedes: the Timeline contains only administrator-approved records, including when the viewer is an administrator.

The four new source and test paths are absent from the index and the worktree. Every existing path the plan names is present, and the behavioral claims checked below match the current source. No unlisted route, migration, dependency, host operation, or acceptance surface is required to implement the plan. `src/kronika/adapters/api/application.py` constructs `RecordService(SqliteRecordRepository(owned_engine))` and does not need an edit: the new reader can be owned by `SqliteRecordRepository`, which already holds the engine.

## Allowlist completeness

`exists at baseline` means tracked at `b66ec8f`. `missing` for a new path is the expected baseline state, not a gap.

| Planned path | Exists at baseline | Purpose | Missing / extra |
|---|---|---|---|
| `src/kronika/application/ports/timeline.py` | no | new Timeline values and reader error | expected missing |
| `src/kronika/infrastructure/persistence/timeline_repository.py` | no | authorized union, snapshot, filters, count, page, locators | expected missing |
| `src/kronika/application/records.py` | yes | argument validation and Timeline return type | present |
| `src/kronika/application/ports/records.py` | yes | Timeline method contract only | present |
| `src/kronika/infrastructure/persistence/record_repository.py` | yes | delegate Timeline; preserve record workflows | present |
| `src/kronika/domain/record_access.py` | yes | remove unused `timeline_includes` | present; helper has no caller |
| `src/kronika/adapters/api/records_api.py` | yes | Timeline parameters, payload, no-store errors | present |
| `src/kronika/adapters/api/web/index.html` | yes | list/filter markup and Review labels | present |
| `src/kronika/adapters/api/web/app.js` | yes | renderer, route state, preview reuse, return focus | present |
| `src/kronika/adapters/api/web/styles.css` | yes | Timeline-scoped list rules | present |
| `tests/integration/persistence/test_timeline_repository.py` | no | new union and budget tests | expected missing |
| `tests/contract/test_timeline_api.py` | no | new wire and audience tests | expected missing |
| `tests/unit/application/test_records.py` | yes | Timeline validation; approval behavior | present |
| `tests/integration/persistence/test_kronika_record_repository.py` | yes | replace old Timeline assumptions | present |
| `tests/contract/test_records_api.py` | yes | Timeline expectations; other contracts stay | present |
| `tests/contract/test_kronika_approved_projection.py` | yes | separate chronicle order from approval timestamp | present |
| `tests/contract/test_kronika_access_inventory.py` | yes | read-only inventory comparison | present |
| `tests/contract/test_local_web_application.py` | yes | served markup and frozen shell checks | present |
| `tests/kronika_ui.test.js` | yes | list behavior and lifecycle negatives | present |
| `docs/adr/0087-complete-visibility-aware-timeline-chronicle.md` | no | accepted decision text | expected missing |
| `docs/adr/README.md` | yes | new row and partial supersession | present |
| `AGENTS.md` | yes | product-boundary restatement | present |
| `SPEC.md` | yes | normative Timeline behavior | present |
| `SECURITY.md` | yes | list/count/search boundary | present |
| `README.md` | yes | overview pointer | present |
| `PRODUCT.md` | yes | experience boundary | present |
| `SERVER.md` | yes | server-owned read model | present |
| `ROADMAP.md` | yes | current successor; historical rows stay | present |
| `DEVELOPMENT.md` | yes | focused commands and rendered route | present |
| `GALLERY.md` | yes | narrow cross-reference | present |
| `docs/KRONIKA_ACCESS_INVENTORY.md` | yes | Timeline inventory row | present |

Regression commands in plan §9.3 also name files that are not mutation targets. All of these exist: `tests/contract/test_gallery_preview_api.py`, `tests/contract/test_content_audience_policy.py`, `tests/contract/test_research_requests_api.py`, `tests/contract/test_workspace_media.py`, `tests/contract/test_public_published_uds.py`, `tests/unit/domain/test_record_access.py`, `tests/unit/application/test_content_audience_requester_private.py`, `tests/contract/test_tailscale_ingress_security.py`, `tests/gallery_still_image_render.test.js`, `tests/gallery_gif_inline_toggle.test.js`, `tests/gallery_details_playback_handoff.test.js`, and `tests/cover_frontend.test.js`. `ap.project.conf` defines `test-focus` with trailing pytest arguments. `node --test` is the contract route in `docs/WORKER_EXECUTION_CONTRACT.md`.

Searches for `/api/timeline`, `list_timeline`, and the Review labels found no additional test file that asserts chronicle membership. `tests/contract/test_cover_api.py` and `tests/unit/application/test_media_cover.py` use a different server-authoritative cover timeline. The plan correctly leaves that terminology alone.

No extra source file is required. The negative allowlist holds: no schema, Alembic, audience-policy, ingress-table, public-composition, identity-definition, upload, provider, deploy, or ADR-0082–0086 body change is needed.

## Visibility and authorization parity

The plan's matrix matches the current decision functions. Tokens are `deny`, `current`, `approved`, and `legacy` (`src/kronika/domain/record_access.py`).

| Plan case | Current decision | Match |
|---|---|---|
| Bound private, withdrawn, or incomplete media for owner | `decide_bound_read`: owner login gets `current` | yes |
| Same bound rows for application administrator | `media.workflow.read` gets `current` before the owner check | yes |
| Same bound rows for another household member | `family` + approved + completed gives `approved`; otherwise `deny`. Withdrawal sets `visibility=private` and keeps the projection (`record_repository.py` `withdraw`) | yes |
| Bound approved family media for another member | `approved` | yes |
| Unbound media for administrator | `ContentAudiencePolicy.read_decision` returns `current` when `media_exists` | yes |
| Unbound unpublished media with live requester access | member gets `legacy`, not `current`. Working title and physical locations are the content. Plan §6.2 assigns physical locations to both `current` and `legacy` | yes |
| Unbound unpublished media without attribution | member `deny`; no owner is invented | yes |
| Unbound legacy-published media | any member gets `legacy`; administrator gets `current`. `media_content_publications.media_id` is the primary key, so publication is one row | yes |
| Binding versus legacy publication or contribution stamps | `read_decision` returns `decide_bound_read` as soon as a binding exists and does not consult publication or requester access | yes |
| Private, approved, and withdrawn questions | same `decide_bound_read` path. Question rows are `search` or `research`, with `final_operation_id` required by `ck_kronika_records_shape` | yes |
| Unfinished, failed, or cancelled request | `GET /api/research-requests/{operation_id}` requires `research.run`, then owner or `_is_admin` (`role == admin` or `records.approve`). Other members are not found | yes |
| Unauthenticated | route returns `401 IDENTITY_REQUIRED` before the service. Both decision functions deny a missing identity. Ingress errors stay `Cache-Control: no-store` | yes |
| Public composition | `public_published_api.py` has no `/api/timeline` route. Public capabilities are only `gallery.read` and `media.original.read` | yes |

Live requester predicates match the plan and are stricter than general attribution:

- Upload: `SqliteMediaAttributionRepository.has_live_requester_media_access` joins `upload_publications` to the caller's `upload_sessions` and does not add a success-state filter.
- YouTube: `cataloged` or `duplicate_resolved` (`_SUCCESS_STATE_VALUES`).
- X: asset state `cataloged` only (`SUCCESS_X_ASSET_STATES`), through `x_post_claims.created_by_login_key`.
- `contributor_match_clause` omits the YouTube and X state filters. `catalog_scope_predicate` for a member includes every unbound `logical_media` row (`member_current_media_predicate`), which is broader than direct read. The plan correctly forbids using either union as the Timeline predicate.

Capability split, with no new capability and no ingress edit:

- `GET /api/timeline` is `RoutePolicy(method="GET", template="/api/timeline")` with no route capability (`tailscale_ingress.py`).
- Ordinary `user` already has `gallery.read` and `research.run`. `admin` adds `media.workflow.read` and `records.approve`.
- Media arm: existing `gallery.read`, then the audience decision above.
- Unfinished request arm: existing `research.run`, then the request owner/administrator decision. That administrator test is `records.approve` or role `admin`, not `media.workflow.read`.
- Completed records: `decide_bound_read` only.
- A synthetic identity missing one of those capabilities fails closed. Mapped roles do not lose rows they can already open.

`GET /api/research-requests/{operation_id}` may call `submit_pending`, `poll_once`, and `release_remote_pending`. The plan forbids per-item request-detail, record-detail, and `read_decision` calls. The SQL reader is what keeps that side effect off the Timeline.

Filters, search, counts, and pagination are specified on the authorized projection. Search uses the existing `NOCASE` literal `LIKE`, with `%`, `_`, and the escape character escaped, over the decision-selected title or question text. It does not search answers. Gallery-preview, content, and download already reauthorize: `READ_DENY` opens nothing, and only `READ_APPROVED` is limited to approved location ids (`gallery_preview_api.py`, `media_content_api.py`). A Timeline locator is not a capability. No route-policy widening is introduced.

Household approved reads use `kronika_approved_media` and `json_extract` of `$.document.question_text` from `ApprovalProjection.canonical_json`. Owner and administrator reads use current `media_metadata` or `kronika_documents.question_text` / request `prompt_text`. Withdrawal leaves `kronika_approved_media` rows in place; the read decision, not the mere presence of those rows, must select the columns.

One pre-existing difference is not copied: the gallery catalog scope can list unbound media that direct read denies. The Timeline plan follows direct read. That is narrower than the catalog list and is the correct parity target.

## Item model, deduplication, and query plan

`logical_media` is an independent row with `created_at_ms` and `media_kind` in `video`, `animated_image`, or `image`. `insert(logical_media)` occurs in `media_repository.py`. A medium can exist with no `kronika_records` row. `bind_media_record` is defined on the port and `SqliteRecordRepository` and is called from tests only. No production caller exists.

`uq_kronika_records_media_id` allows one binding. `ck_kronika_records_shape` makes the arms disjoint: a `media` record has `media_id` and null `final_operation_id`; a `search` or `research` record has null `media_id`, a document, and a non-null `final_operation_id`. `uq_kronika_records_final_operation_id`, `uq_kronika_documents_operation_id`, and `uq_research_requests_record_id` are the deduplication keys. `media_metadata` and `media_content_publications` are one row per medium. Locations, tags, claims, and analysis runs are many-to-one and must be aggregated or excluded from the item join, as the plan says. They do not need new tables.

`SqliteResearchResultCompletion.complete` inserts the document, the private record (`final_operation_id` = the request operation, `created_at_ms` copied from the request), and `research_requests.record_id` in one immediate transaction. It does not update `lifecycle_state`. `ResearchCoordinator._complete_from_checkpoint` sets `saved` afterward. The overlap interval is real. Excluding a request by `final_operation_id` and by a populated `record_id`, and failing a contradictory pair instead of emitting both rows, is implementable with those unique keys. A `saved` request without that relationship has no database constraint forcing `record_id`; the plan's integrity error is the right application check. Research lifecycle names in the schema match §4.3 exactly. Analysis states are `pending`, `analyzing`, `analyzed`, and `failed`. Absence of an `automatic_post_catalog` run is the derived status `not_requested`, which is already the analysis-filter vocabulary in `content_publication.py`. `_latest_run` orders by `created_at_ms DESC, id DESC` for that definition.

The admission writer sets `created_at_ms` and `admitted_at_ms` to the same clock value. Nothing updates `admitted_at_ms` later. Completion copies `created_at_ms` onto the record. Using `logical_media.created_at_ms` for media and the request's `admitted_at_ms` for both question arms, with `kronika_records.created_at_ms` only when a completed record has no request row, keeps one order across the save interval. `create_completed_document` is a repository method used by tests, not by an HTTP route, so production questions come from the request path.

Quarantine, incomplete uploads, and acquisition claims stay out because the media arm starts at `logical_media`. Claims and upload sessions can exist with a null media id. No synthetic record or rewrite is required. Alembic head in the tree is `0035_research_requests_and_accounting.py`. No later revision is present.

The two-or-three SELECT budget fits a CTE/subquery used twice (count and page) plus one page-bounded locator query. Empty and question-only pages skip the locator query. `UNION ALL` of the three arms cannot duplicate a medium or a saved question when the exclusions above are applied. The locator batch matches today's `_summary_preview_locations`: `MIN(location_id)` among available approved locations for `approved`, and `MIN(physical_media_locations.id)` among `available` rows for `current` or `legacy`, only for `video` and `animated_image`. Still images stay null. The batch reads ids only.

SQLite 3.54.0 on this machine, probed with `sqlite3 :memory:` only:

- `json_extract` of `$.document.question_text` returns the question and not a sibling answer.
- `json_valid` is 1 or 0.
- `json_extract` of invalid JSON raises `malformed JSON` (exit 1), so a bad projection fails the statement. Mapping that failure to `500 TIMELINE_UNAVAILABLE` with the fixed message, and not substituting current text, is the plan's rule. `json_valid` can distinguish the bad value before extract.
- `COLLATE NOCASE LIKE` works on extracted text, including an escaped `%`.
- `BEGIN` / `SELECT` / `ROLLBACK` works.
- `row_number()` and `UNION ALL` ordered by `created_at_ms DESC, item_id ASC` produce the binary tie order the plan specifies (`media:` before `question:` at equal time).

`run_in_transaction` calls `connection.begin()` before the callback. `run_in_immediate_transaction` already issues `BEGIN IMMEDIATE` through `exec_driver_sql`. The new reader can issue its own `BEGIN` on one connection before the first SELECT. No journal-mode change is required. A concurrent WAL snapshot was not executed here because a file-backed database is outside this grant. The plan's implementation test owns that proof.

No new index is required for a correct first candidate. `logical_media` has no `created_at_ms` index, and `ix_companion_review_per_media_history` is not ordered by `created_at_ms`. The mixed-source sort and the literal search may scan. That is the plan's accepted foundation-stage residual, with a later index only under an amended allowlist if measurement requires it. It is not a blocker.

`RecordService.list_timeline` is a separate method from `list_own_history` and `list_admin_inventory`. They share `_list` only through the `timeline_only` flag. Removing that flag's branch after delegation leaves the history and inventory branches, `approve`, and `withdraw` in place. `timeline_includes` has no production or test caller. Current list limits are default 24 and maximum 100. Category requires `kind=media`. Unknown query keys are unread. Successful Timeline JSON does not set a cache header today; render and ingress errors already use `no-store`. Adding `Cache-Control: private, no-store` and omitting ETag/`304` on the Timeline responses is compatible. Preview GET keeps its own ETag. The new `TimelineItem` shape stays off `RecordSummary`, so `/api/my/records`, `/api/admin/records`, detail, and render keep their keys, including `owner_login_key` and `timeline_entered_at_ms`.

## UI, accessibility, and frozen surfaces

`#kronika-timeline-results` is a `div.kronika-grid`. The eight kind/category chips, polite status, and pager already exist. Replacing that container with `ol.kronika-chronicle`, keeping `#kronika-timeline-results`, and adding labelled selects plus a local search form is contained in `index.html`, `app.js`, and `styles.css`. `.visually-hidden` exists. The 720 px breakpoint already exists. Hash parsing already keeps `filter` and `offset` and ignores unknown keys, so `q`, `status`, `visibility`, and `publication` can be added in `kronikaParseRoute` without a new router.

`kronikaAttachCardPreview` already builds one lazy decorative 36×36 image, fences it by identity, page, and list generation, and uses `mediaGalleryPreviewUrl`. It can attach to a row slot. `kronikaCancelListRequest`, `kronikaBeginListController`, `pagehide` retirement, and `visibilitychange` preservation are present (`kronikaOnVisibility` pauses polling and does not retire previews). History continues through `kronikaRenderCards`. Gallery and Details renderers stay outside the change.

`kronikaReleaseDetailsAddress` restores `kronikaDetailsReturn` and then always marks the gallery view. Extending that glue so a Timeline-originated close restores the Timeline route and focuses the originating title, or the Timeline heading if the row is gone, is the bounded `app.js` change the plan names. Gallery-originated Details behavior stays on the existing fallback.

Review copy is in `index.html` (`Not on Timeline`, `On Timeline`, `Approve for Timeline`, `Withdraw from Timeline`) and in `app.js` (`Approve for Timeline` versus `Approve current version`). Relabelling those strings does not change the approval endpoints. The frozen Gallery, Details, player, and History card visuals are outside the allowlist except that return-navigation glue. No frontend framework or asset pipeline is required.

Cover Studio uses a different "timeline" in `SECURITY.md` around the `metadata.canonical.write` cover endpoints, in `GALLERY.md` cover prose, and in the cover tests. The plan already says not to rewrite that terminology.

## Tests, side effects, and validation

Every existing test identity the plan names is present and does what the plan says:

| Identity | Current assertion the plan replaces |
|---|---|
| `test_records_api.py::test_timeline_membership_is_approved_for_every_caller` | approved family only, including owner and administrator; withdrawal removes the row |
| `test_record_list_filters_reject_invalid_combinations` | Timeline `visibility=family` is 422 |
| `test_media_list_preview_locator_is_additive_and_path_free` | private owner media absent from Timeline |
| `test_working_only_preview_location_is_not_disclosed_on_timeline` | household cannot see a working-only location |
| `test_list_filters_apply_before_count_and_keep_order` | owner/admin Timeline totals are zero for the unapproved fixture |
| `test_timeline_titles_stay_on_the_approved_projection` | approved title for every Timeline caller |
| `test_timeline_preview_locator_uses_only_approved_locations_for_every_caller` | approved locator for every caller |
| `test_kronika_approved_projection.py` Timeline timestamp assertions | chronicle order is tied to `timeline_entered_at_ms` |
| `tests/kronika_ui.test.js` "personal history keeps failed requests out of the timeline" | failed requests are excluded from Timeline |
| `test_inventory_matches_both_compositions_and_route_policies` | rewrites the inventory when it differs |

`tests/contract/test_kronika_access_inventory.py` lines 287–289 call `INVENTORY.write_text` when the file is absent or its text differs from the rendered route table. The Timeline row is hardcoded as approved-family for every caller, with the capability cell `records.approve for administrator routes`, although the route policy has no capability. Replacing the write with an exact comparison, and updating the row in the allowlisted inventory file, is necessary. A later read-only acceptance then fails on drift instead of dirtying the tree.

The new test names in §9.2 cover the positive and negative matrix, deduplication, ordering, pagination and counts, one snapshot, the SELECT budget, preview round-trip, fallback, accessibility, inert text, and frozen surfaces. They use synthetic catalogs. They do not require live providers, real private media, NUC fixtures, a browser toolchain, or a full suite. The §9.3 commands use `./.ap/ap exec --operation test-focus` and `node --test`. The literal baseline in that block is the pre-change SHA; the same section says the later grant must bind the candidate commit. That substitution is an implementation-prompt detail, not a missing path.

`test_records.py` uses the real repository. Its household Timeline assertion is an approved question and can keep `record_id` if the new item carries it. Domain decision tests do not call `timeline_includes`. No tracked file needs to be written by the test run after the inventory change. Implementation itself writes only the allowlisted files, and only in the later grant.

The plan's E3 fresh independent acceptance, one primary acceptance, and at most one correction with fresh re-acceptance match the authorization boundary: direct guards stay, and the new SQL list is the new exposure. This preflight is not that acceptance.

## Documentation and rollback

ADR-0087 and `docs/adr/README.md` are the architecture owner. ADR-0082 through ADR-0086 bodies stay unchanged; the index records the partial supersession, which is the existing ADR-0084 pattern. The current restatements the plan names are present:

- `AGENTS.md` Product Boundaries: Timeline contains only administrator-approved records; media enters only after analysis and approval.
- `SPEC.md` "Timeline, Personal History and Completion": approved-only landing, pending/failed work outside it, approved titles for every caller, approved locations only.
- `SPEC.md` privacy restatement repeats the approved-only sentence.
- `SECURITY.md` privacy boundary and "Timeline And History Preview Locators": approved-only Timeline, approved locations for every caller.
- `README.md` Accepted Transition: approved-only main page.
- `PRODUCT.md`: newest approved entry first.
- `SERVER.md` Records and ingress: household members see a record on the shared Timeline only after approval.
- `ROADMAP.md` active proofs: shared Timeline exclusion until approval.
- `DEVELOPMENT.md`: Timeline media cards reuse the kind-icon slot.
- `GALLERY.md`: SPEC owns Timeline and History card reuse.
- `docs/KRONIKA_ACCESS_INVENTORY.md` `GET /api/timeline`: approved family only; approved projection for every caller.

`docs/UX_AUDIT.md` says to show thumbnails on Timeline and History cards. It is an audit note, not the membership rule. The plan preserves it. No second normative owner is created. Unrelated cover "timeline" prose stays.

Source rollback is a revert of the allowlisted candidate. There is no migration, data rewrite, fixture mutation, secret, provider call, or deployment in the implementation slice. Schema head stays `0035`. NUC rollback remains the later `kronika-release rollback --release <previous>` under its own grant. The predecessor `sudo -K` means that later deployment needs a fresh Cooperator `sudo -v`. This preflight does not prepare that timestamp.

## Blockers and required plan corrections

No material blocker. Non-blocking notes are implementation constraints already stated by the plan or direct readings of the current predicates. They do not require a revised plan.

| Finding ID | Exact repository evidence | Effect on implementation or safety | Smallest correction | Blocking |
|---|---|---|---|---|
| F1 | `decide_bound_read` uses `media.workflow.read`. Request `_is_admin` uses role `admin` or `records.approve`. `gallery.read` and `research.run` are separate ordinary capabilities. `GET /api/timeline` has no route capability. | One collapsed "administrator" flag would mis-classify a synthetic identity. Mapped admin/user roles already hold the matching set. | none. Implement the three existing decisions the plan already names. Fail closed when a capability is absent. | no |
| F2 | `decide_unbound_legacy` returns `legacy` for a member requester, and `current` for an administrator. `read_decision` checks the binding first. | The matrix phrase "legacy/current working read" means token `legacy` plus current working columns for the member, and token `current` for the administrator. | none. §6.2 already selects physical locations for both tokens. | no |
| F3 | SQLite 3.54.0 `json_extract` of invalid JSON raises `malformed JSON`. `json_valid` returns 0. | A bad approved projection must become `TIMELINE_UNAVAILABLE`, not current question text. | none. The plan already requires that failure. | no |
| F4 | Admission sets `created_at_ms == admitted_at_ms`. Completion copies `created_at_ms`. No writer updates `admitted_at_ms`. | Using different clocks on the two question arms would move a row at save only if those clocks diverge. They do not diverge in current writers. | none. Use the request admission time on both question arms, and `kronika_records.created_at_ms` when no request row exists. | no |
| F5 | No `logical_media.created_at_ms` index. Analysis history index is not ordered by `created_at_ms`. | First candidate may scan and sort. | none. Accepted residual in plan §6.3 and §13. A new index needs a later allowlist. | no |
| F6 | `kronikaReleaseDetailsAddress` restores the saved hash and then marks gallery. | Timeline return focus is not the current behavior. | none. The plan already puts that glue in `app.js`. | no |
| F7 | `INVENTORY.write_text` runs when the rendered inventory differs. | An acceptance run can dirty a tracked file. | none. The plan's read-only comparison is the required change and is inside the allowlist. | no |
| F8 | `SECURITY.md` cover endpoints and cover tests use a different "timeline". | A broad replace would change Cover Studio requirements. | none. The plan already excludes that terminology. | no |

## Recommended implementation sequence and allowlist

This sequence recommends the next grant. It does not issue it.

1. Orchestrator issues one complete implementation prompt to this healthy session as Worker session `02`, exchange `02`, `current-worker-session`, `Native planning mode: not-used`, with explicit implementation authority, this allowlist, and the accepted ADR-0087 semantics.
2. Implement the full union, API, list UI, tests, and documentation owners in one candidate. Do not ship a private-media-only or approved-plus-media intermediate as completion of this whole.
3. Bind `ap exec --baseline` to the candidate commit the grant names. Do not execute the §9.3 block against `b66ec8f` after the tree has changed.
4. Fresh session `03` performs the independent E3 acceptance. Publication, NUC preflight, deployment, and rendered acceptance stay separate. NUC contact remains unauthorized until that later grant. Target schema head remains `0035`.

Exact source, test, and documentation allowlist for that grant, unchanged from the accepted plan:

```text
src/kronika/application/ports/timeline.py
src/kronika/infrastructure/persistence/timeline_repository.py
src/kronika/application/records.py
src/kronika/application/ports/records.py
src/kronika/infrastructure/persistence/record_repository.py
src/kronika/domain/record_access.py
src/kronika/adapters/api/records_api.py
src/kronika/adapters/api/web/index.html
src/kronika/adapters/api/web/app.js
src/kronika/adapters/api/web/styles.css
tests/integration/persistence/test_timeline_repository.py
tests/contract/test_timeline_api.py
tests/unit/application/test_records.py
tests/integration/persistence/test_kronika_record_repository.py
tests/contract/test_records_api.py
tests/contract/test_kronika_approved_projection.py
tests/contract/test_kronika_access_inventory.py
tests/contract/test_local_web_application.py
tests/kronika_ui.test.js
docs/adr/0087-complete-visibility-aware-timeline-chronicle.md
docs/adr/README.md
AGENTS.md
SPEC.md
SECURITY.md
README.md
PRODUCT.md
SERVER.md
ROADMAP.md
DEVELOPMENT.md
GALLERY.md
docs/KRONIKA_ACCESS_INVENTORY.md
```

Negative allowlist remains the plan's §8 negative list, including `.ap/**`, `catalog_schema.py`, Alembic, audience policy, ingress route table, public composition, upload and research adapters, `deploy/**`, Gallery/Details/player bodies except the named return glue, and ADR-0082 through ADR-0086 bodies.

## Evidence limitations

Not run, and not authorized: the implementation test suite, any file-backed or WAL database, NUC or SSH contact, browser or rendered acceptance, provider or capture-browser contact, secret inspection, and any repository Git write. Concurrent snapshot behavior is specified and left to the planned synthetic test. Gallery catalog-list breadth was inspected only as the predicate the Timeline must not copy. The sanitized `ap project check` warning listed additional Git config class names; their values were not read.

AP consumer notes `AP_DEFECTS.md` §0.0, D-17b, D-19, D-20, and D-21, and `AP_DESTILLED.md` §17, were read as consumer evidence. The direct-write report route in this prompt is permitted trace persistence under D-20. The governing rules remain the pinned AP.

## Tests and validation

Repository gates: `ap doctor` PASS and baseline-bound `ap project check` PASS. SQLite `:memory:` probes above passed after one quoting failure that was rerun cleanly. No pytest, no `node --test`, and no application process was started. Source at the end of inspection was still `b66ec8f50860ace624f6be1fd3ad63f521edcd33` with an empty porcelain status.

Changed files: this report only, `/Users/agile/meta/projects/kronika/01/09-timeline-complete-chronicle/02_report_00.md`. Kronika source is unchanged.

Git result: read-only inspection and one `git ls-remote`. No stage, commit, or push.

## Deviations, risks, and missing evidence

No plan deviation and no missing evidence that blocks an implementation grant. Residual risks are the ones the plan already accepts: scan/sort cost, offset pages moving between HTTP requests, unbound attribution not becoming common-record ownership, NUC state unvalidated, and rendered behavior belonging to the Cooperator after publication.

## Smallest next step

Issue the separate implementation prompt described above. Do not treat this preflight PASS as implementation authority.

Resolved Execution Issues / Near-Misses: The first `sqlite3 :memory:` probe embedded a backslash escape in a heredoc. SQLite reported `malformed JSON` for two statements and the process exited 1. A second probe used separate statements and proved SQLite 3.54.0 `json_extract`, `json_valid`, invalid-JSON failure, `NOCASE LIKE`, and `BEGIN`. No file or repository state was created. Residual risk: none for those probed facts.

Pre-Existing Failure Classification: none

Authority expiry: submission of this terminal preflight report ends this exchange's authority. Implementation, acceptance, publication, deployment, and logical-whole closure are not granted. A later implementation needs a new complete Orchestrator prompt for session 02, exchange 02, with native planning mode not used and explicit implementation authority.

Orchestration critique:
MEASURED: `ap project check` PASS included sanitized classes `GIT_CONFIG_VALUE_0`, `GIT_CONFIG_KEY_0`, and `GIT_CONFIG_COUNT` in addition to `SSH_AUTH_SOCK` and `PATH`; the prompt's parenthetical names only the latter pair; the gate still passed; future prompts should treat PASS as the gate and not require the inherited class list to repeat the previous session.
LEAD: none
