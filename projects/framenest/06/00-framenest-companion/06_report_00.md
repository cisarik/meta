### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 06
Worker exchange ordinal: 01
Task identity: FRAMENEST-COMPANIE-ITEM9DIAG-01
```

Status: **PASS**  
Phase-qualified result: not-applicable (diagnostic)  
Logical-whole closure: not-closed  
Report justification: `new-evidence`

This session did not implement `977a7af80afed16745adb0ef8e939555e5e21cce`. Prior Worker 04/05 authorities are expired. No Edit/AI per-field apply UX, no R4, no correction.

## Capability handshake

| Material row | Requested | Observed or unknown | Evidence class |
|---|---|---|---|
| Product/client | Cursor Worker | Cursor Grok 4.6; not independently attested | requested; client-presented identity |
| Reasoning | High | Effective reasoning SKU not exposed | requested; unknown/not observably exposed |
| Native planning mode | `not-used` | Plan Mode off; report write only | directly observed |
| Permission mode | not named | unknown/not observably exposed | unknown |
| Repository | Canonical checkout of `977a7af…` | `/home/agile/Projects/framenest`; branch `feat/x-meme-browser-companion`; HEAD `977a7af80afed16745adb0ef8e939555e5e21cce`; `git status --porcelain=v1` empty | directly observed |
| AP pin | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | `.ap` HEAD equals pin | directly observed |
| Python evidence | `./.ap/ap project check` and `./.ap/ap exec` with exact baseline | Used; `ap project check --baseline: PASS`; `runtime-info` PASS; `.venv/bin/python` 3.13.9; provenance `__file__` `/home/agile/Projects/framenest/src/framenest/__init__.py` | directly observed |
| Focused tests | Re-run only if inspection cannot dispose H3–H5 | Not re-run; inspection disposed H3–H5 | directly observed |
| Network, NUC, SSH, sudo, live catalog, providers | Forbidden | Unused | directly observed |
| Git | Read-only | No commits, no `git add`, no push, no checkout of another SHA | directly observed |
| Browser / Node | Node only if required for H5/hosted-hide | Unused | directly observed |

Capability, permission, and client identity did not expand task authority.

## Repository gate

```text
HEAD:     977a7af80afed16745adb0ef8e939555e5e21cce
Branch:   feat/x-meme-browser-companion
Porcelain: empty
.ap HEAD: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Commit:   977a7af feat: hosted companion history with analyzed inbox and ordinary own-history
```

RF-12: clean; no classification stop. Canonical not mutated. Start commit equals end commit.

`ap project check` and `ap exec --operation runtime-info` both PASS. Inherited ambient classes `APPIMAGE`, `APPDIR`, `LD_LIBRARY_PATH`, `PATH`, `SSH_AUTH_SOCK` were sanitized by the envelope (see Near-Misses). Operation interpreter is the Poetry-owned `.venv`, not ambient Python.

Changed files (this exchange): only this report, outside the canonical tree.

Git write result: not authorized; not performed.

## Primary hypothesis

**H3.** Website Manage-media **Analyze by AI** (and Gallery 🧠) POST `…/ai-suggestion-preview`. That path returns suggestion JSON only and never writes `media_analysis_runs`. Companion `analyzed` / `unopened` / `unopened_count` require a latest generic analyzed run. Canonical Save after preview updates metadata only. ADR-0067 §5 and ADR-0076 R2 “website Analyze-by-AI successes join” are **not implemented on this path**.

Item 9: **candidate defect** (persistence-join missing on the interactive Analyze path), which is also an **ADR-implementation gap**. Not primarily fixture/operator. H1 remains a secondary, unconfirmable fixture risk for this episode (live catalog forbidden).

## Probe answers

### 1. Does successful website Analyze by AI persist a companion-visible generic run?

**No.**

Browser (standalone Manage media / metadata editor):

- `mediaAiSuggestionEndpoint` → `POST /api/media/{media_id}/locations/{location_id}/ai-suggestion-preview`
- `handleAnalyzeMetadataByAi` (editor **Analyze by AI**)
- `handleAnalyzeCatalogCard` (Gallery 🧠; same POST, then canonical PUT)

API: `preview_imported_media_suggestion` in `media_suggestion_api.py` calls `PreviewImportedMediaSuggestion.execute` and returns `_imported_preview_response(result)`.

Application: `PreviewImportedMediaSuggestion.execute` and `ImportedMediaSuggestionPreviewResult` are documented **non-persistent**. The method prepares frames, calls `provider.suggest`, returns the dataclass. It never touches `MediaAnalysisRunRepository`.

`record_analyzed` callers on this SHA:

- `ExecuteAutomaticMediaAnalysisRun.execute` in `media_analysis_lifecycle.py` (automatic/manual durable lifecycle)
- `movie_identification_lifecycle.py` (movie profile; companion-excluded)

Preview never calls either.

The durable join path that **does** persist is separate: admin batch “Analyze selected” → `executeAdminAnalysisEnqueue` → `POST …/durable-analysis` → `request_durable_analysis` → `RequestManualMediaAnalysis.execute` → `create_manual_pending`, later `ExecuteAutomaticMediaAnalysisRun.record_analyzed` with `analysis_definition=automatic_post_catalog` and `analysis_profile=generic_media`. Manage-media **Analyze by AI** does not use that endpoint.

Save after Analyze: `handleSaveMetadata` `PUT …/metadata`. Canonical fields only. No run.

Cooperator narrative fits: durable **Load AI suggestion** (`durableAnalysisLoadAvailable` requires `metadataDurableAnalysis.state === "analyzed"`) stays empty; preview fills draft via `applyResolvedAiSuggestionToMetadataWorkspace`; Save persists those drafts.

### 2. Would that run satisfy `_analyzed_inbox_predicates` and `_own_analyzed_latest`?

There is no run to satisfy them.

Quoted `_analyzed_inbox_predicates`:

- `media_analysis_runs.state == "analyzed"`
- `analysis_definition == automatic_post_catalog` (`AUTOMATIC_POST_CATALOG_ANALYSIS_DEFINITION`)
- `analysis_definition != movie_identification`
- `analysis_profile == generic_media` **or** `NULL`
- `completed_at_ms IS NOT NULL`
- coalesced `media_metadata.content_category != movie`

`_latest_successful_generic()` ranks those rows per `media_id` (newest `completed_at_ms`, then `id`). Own-history analyzed rows are that latest subquery **inner-joined** to `_owned_cataloged_x_media_ids(actor)`. `_own_analyzed_latest` is the same join used as the `unopened_count` latest set (not the global inbox subquery).

Extra gates for ordinary own-history (not on admin inbox):

- `x_assets.state == "cataloged"`
- `x_assets.media_id IS NOT NULL`
- `x_post_claims.created_by_login_key == actor_login_key`
- requested category null or not movie; canonical category not movie

Admin inbox is the global analyzed pool (no `created_by_login_key`). A preview-only success satisfies none of the run predicates.

### 3. If the ordinary user “downloaded” from Gallery rather than owning an X Save, can own-history list it?

**No.** Own-history is requester-private **cataloged X**, not workspace/gallery downloads. `_own_history_rows` unions (a) latest generic runs restricted to owned cataloged X media ids with (b) pending owned cataloged X with no latest generic run. A Gallery `media.download` / workspace item without that actor’s `x_post_claims` + cataloged `x_assets` never appears. Tests already assert website-origin analyzed media (`WEBSITE`) is in admin inbox and **absent** from own-history (`WEBSITE not in own_ids`).

In this project “downloaded” is also used for X-Save acquisition completion. Without live catalog this episode’s fixture cannot be proven. Even with a correct own X Save, H3 still yields pending/plain and no badge from Analyze by AI.

### 4. Does Save-after-Analyze change unopened/badge?

**No.** Unopened is open-state vs latest generic run, not “canonical metadata equals AI”. `_inbox_item_from_row`: `unopened` is false unless `analyzed`; if analyzed, `unopened` iff `opened_run_id` is null or ≠ `analysis_run_id`. `_unopened_count_statement` counts latest-generic rows (own-analyzed for ordinary) where opened is missing or stale. Canonical PUT does not insert a run and does not upsert `companion_review_open_states`.

### 5. Hosted Edit hiding Load (`companionWebHosted()`)

**Out of scope for item 9.** `updateMetadataControls` hides Analyze by AI and Load AI suggestion when `companionWebHosted()` is true. Cooperator used administrator **Manage media** (standalone). Hide does not causally prevent a run: the Analyze button that is shown still POSTs preview, which never records a run. Edit/AI per-field apply remains the next whole.

### 6. Existing tests: website Analyze joins inbox/own-history?

**Coverage gap, not a license to add tests here.**

Executed-or-inspectable coverage:

- Inbox/own-history **given a pre-inserted** `media_analysis_runs` row: `tests/unit/infrastructure/persistence/test_companion_review_repository.py` (`test_latest_successful_generic_exclusions_and_unopened_empty_table` seeds `WEBSITE_RUN` titled “Website Analyze-by-AI”; `test_own_history_opened_isolation_does_not_use_global_unopened_count`; pending vs analyzed own-history). `tests/contract/test_companion_review_api.py` (`test_own_history_opened_alice_bob_admin_isolation` and related).
- Preview HTTP JSON only: `tests/contract/test_media_suggestion_api.py`, `tests/integration/test_local_web_media_suggestion_review.py`. No assertion that preview writes `media_analysis_runs`.
- Durable lifecycle `record_analyzed`: `tests/unit/application/test_media_analysis_lifecycle.py`.
- Manual durable enqueue: `RequestManualMediaAnalysis` unit tests; admin-batch JS uses `durable-analysis`, not preview.

No test drives `POST …/ai-suggestion-preview` and then asserts companion inbox/own-history `analyzed=true` / `unopened_count`. Named gap: interactive website Analyze join is specified, not proven.

Inspection was sufficient to dispose H3–H5; focused pytest was not re-run.

## Disposition H1–H7

| Id | Disposition |
|---|---|
| **H3** | **Primary, confirmed from repository path mapping.** Preview never `record_analyzed`. |
| H1 | Possible contributing fixture if the ordinary identity did not own a cataloged X Save. Unconfirmable without live catalog. Insufficient as the sole cause: a correct own-X fixture would still fail H3. |
| H2 | Unlikely primary. Badge alarm period can lag; row accent comes from list JSON `analyzed && unopened`. Wrong identity / stale extension cannot create a missing run. |
| H4 | Not reached. No run to filter. (Movie / omitted category / wrong definition would matter only after a durable write.) |
| H5 | Refuted as primary. Own-history `unopened_count` uses `_own_analyzed_latest`, not the global latest subquery. Isolation tests cover Alice/Bob/admin **when runs exist**. |
| H6 | Not reached. Pending rows never set `unopened`. No latest run ⇒ no open-state comparison. |
| H7 | Not used. Closest named sibling is the **implemented** durable-analysis batch path, which this episode did not use. |

Ordered shortlist: **H3** (join unimplemented) ≫ **H1** (possible non-owned fixture) ≫ H2 (operator lag).

## ADR-0067 / ADR-0076 join on Manage-media Analyze

Normative R3′ (`02_report_01.md`) and accepted ADR-0076: website Analyze-by-AI successes on in-scope non-movie media **join** the analyzed pool; ordinary `unopened_count` is **own-analyzed** cataloged X only. ADR-0067 §5: “Website Analyze by AI successes on in-scope (non-movie) media join the same inbox. There is no second suggestion store.”

On SHA `977a7af…` that sentence is implemented for **durable** generic runs (automatic post-catalog enqueue when enabled; `POST …/durable-analysis` / `RequestManualMediaAnalysis`; tests that insert analyzed rows). It is **not** implemented for interactive Manage-media **Analyze by AI** or Gallery 🧠, which share the non-persistent preview store. There is a second, ephemeral suggestion path. Companion never sees `analyzed=true` from that success.

## Item 9 classification

**Candidate defect** (missing persistence-join on the Analyze-by-AI preview path), concurrently an **ADR gap** relative to 0067/0076 as implemented on that path. Not classified as fixture/operator-primary. A Cooperator re-spot-check of the **same** Analyze-by-AI → ordinary own-history sequence would reproduce FAIL even on an ordinary-owned cataloged X Save after unpacked reload.

## Deviations, risks, missing evidence

- Live NUC catalog not inspected (forbidden). H1 for this episode remains inference from Cooperator wording (“downloaded”), not SQL.
- Automatic post-catalog scheduler, if enabled, can still create a generic run by a **different** path. That would not make preview itself join; it also would not explain “badge +1 **after** this Analyze” if no new run was written.
- No product, ADR-body, or SECURITY.md edits.

## One smallest next step (ORCHESTRATOR)

Authorize one bounded correction of the **persistence-join**: on successful interactive website Analyze by AI (editor button and Gallery 🧠, same preview POST), persist a companion-visible generic run (`automatic_post_catalog` / `generic_media` / `analyzed`) using the existing durable lifecycle (`RequestManualMediaAnalysis` + `ExecuteAutomaticMediaAnalysisRun.record_analyzed`, or equivalent persist-from-preview-success), without opening Edit/AI per-field apply or R4. Do **not** first send the Cooperator to re-spot-check the same Analyze-by-AI fixture; that path cannot pass R3′ until the join exists. Optional later confirmation: ordinary-owned cataloged X Save, unpacked reload, then Analyze (or durable batch) and own-history accent/badge.

## Authority expiry

This report terminates FRAMENEST-COMPANIE-ITEM9DIAG-01. No follow-on action, correction, Git write, NUC access, provider call, R4, Edit/AI apply UX, or logical-whole closure is authorized.

```text
Resolved Execution Issues / Near-Misses: ambient AppImage/loader classes (`APPIMAGE`, `APPDIR`, `LD_LIBRARY_PATH`, inherited `PATH`, `SSH_AUTH_SOCK`) present in the parent; cause: Cursor/AppImage untrusted ambient boundary; resolution: `./.ap/ap` sanitized-v1 re-exec, check and runtime-info PASS on `.venv` CPython 3.13.9 with `src/framenest/__init__.py` provenance; residual risk: none for this diagnostic (no ambient Python used for evidence).
Pre-Existing Failure Classification: none
```
