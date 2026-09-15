### Report for ORCHESTRATOR_CHAT

| Field | Value |
|---|---|
| Logical whole identity | `framenest-web-client-contract-and-testability-convergence` |
| Worker role / profile | `WORKER` / Fresh Acceptance Worker |
| Worker session target | `fresh-worker-session` |
| Worker session ordinal | `04` |
| Worker exchange ordinal | `00` |
| Native planning mode | `not-required` |
| Standard terminal status | **acceptance-PASS** |
| Phase-qualified result | Independent acceptance of candidate `33946e0`: all material gates pass; candidate accepted |
| Candidate commit | `33946e08447dc92621ed6844b4b5d13a19ec29f1` |
| Candidate parent / baseline | parent `fe5e38b8bfb986e68a9714d709267e3d19be1575`; logical-whole baseline `8c7858b62beca3c4ee92bb8f1f095b98063e2c94` |
| Logical-whole closure | **Not closed** — publication/deployment authority was not granted; closure belongs to the Orchestrator |
| Report justification | Independent, read-only verification of the exact candidate against the governing AP, the approved plan, both implementation prompts, and the acceptance matrix; all suites executed on the exact committed tree; no source, index, Git, or Meta mutation performed |
| Authority expiry | All Acceptance Worker authority expires at this terminal report |

## Verified candidate

Independently observed (not copied from reports):

```text
Repository root  /home/agile/Projects/framenest
HEAD             33946e08447dc92621ed6844b4b5d13a19ec29f1   (exact expected)
branch           feat/x-meme-browser-companion
origin           https://github.com/cisarik/framenest.git  (canonical)
public refs      refs/heads/feat/x-meme-browser-companion = 33946e0844... (ls-remote, independent)
                 refs/heads/main = a4193d4f520a30aafa333987f2e6b846a5425d27
local/public     branch ref equals local HEAD; branch is 6 commits ahead of origin/main, 0 behind
worktree/index   git status --short empty before, during (after both full suites), and after acceptance
.ap gitlink      160000 7478ddb07d2c3911f79e1aa1441f0115a31c45d8  (exact expected)
.ap HEAD         7478ddb07d2c3911f79e1aa1441f0115a31c45d8, clean
ap doctor        PASS (strict pinned commit, managed block, resolved variant stable)
ap project check PASS --baseline 8c7858b... (only WARN: sanitized inherited env classes SSH_AUTH_SOCK/VIRTUAL_ENV_DISABLE_PROMPT/PATH)
git diff --check exit 0
```

No acceptance run mutated source or index; both complete suites were run and the tree remained clean.

## Evidence-chain review

Read and reconciled: `01_planning_00.md` + `01_report_00.md` (Planner); `02_implementation_00.md` + `02_report_00.md` (Slices 0, 2-RED, 1, 2-GREEN, 3); `03_implementation_00.md` + `03_report_00.md` (Slice 4a/4b); `04_acceptance_00.md`.

Reconciliation results:

- Worker 02's claims match repository evidence: slice `8c7858b..1f355a8` is exactly 10 files, +585/−29; `EXPECTED_AP_COMMIT` now names the pinned AP while both historical files preserve `7ef45da`; the parity mechanism is real dual-language execution (verified below).
- Worker 03's claims match repository evidence: slice `1f355a8..33946e0` is exactly 6 files, **+38/−1323** (matches its report including app.js −970); 564→515 top-level functions (49 removed, 0 added); 12,780→11,810 app.js lines; `git status` empty.
- **Contradiction found and resolved in favor of Worker 03:** implementation prompt 03 §10 asserted the catalog-card-preview cluster was "production-live" and used that premise to protect `LIBRARIES_ENDPOINT`. Worker 03 correctly reported that `handleCardPreview` lost its last external caller in `a15dfef` ("feat: make gallery playback content-first"), retained the protected cluster anyway under the "retain and report when ambiguous" rule, and recorded the contradiction. My independent check confirms Worker 03's finding (see R1 below). No report claim contradicted repository truth; the contradiction is between an implementation-prompt premise and later-discovered evidence, and was correctly deferred as a residual rather than silently acted upon.
- Non-blocking observation: the archived Worker 02 report (`02_report_00.md` lines 1–2) begins with two lines of preamble before the required `### Report for ORCHESTRATOR_CHAT` heading, and the archived Worker 03 report likewise has one opening line before the heading. This is a report-format defect at archival time, not a repository-correctness defect; recorded as non-blocking.

## Commit-chain review

All five expected commits exist with exact subjects, form a linear chain, and are ancestors of the candidate HEAD (independently verified with `git merge-base --is-ancestor` and `git log --format='%H %P %s'`):

```text
0f4500ad7463d7428f377097aea224a268b321e2  Rebaseline FrameNest AP integration pin
6371bc00cb686c80e735330b308494ba552b94bc  Align metadata client-server validation contracts
1f355a8433331beef3410bf807b247a5b8155919  Replace metadata source assertions with behavior tests
fe5e38b8bfb986e68a9714d709267e3d19be1575  Retire test-only frontend artifacts
33946e08447dc92621ed6844b4b5d13a19ec29f1  Remove unreachable legacy library browser client
```

Ancestry: `8c7858b` (baseline) → `0f4500a` → `6371bc0` → `1f355a8` → `fe5e38b` → `33946e0`; each commit's recorded parent matches the predecessor exactly. Publication state was determined independently with `git ls-remote`; acceptance did not require it and was not affected by it.

## Acceptance matrix

| Gate | Verdict | Evidence |
|---|---|---|
| A — baseline and Git integrity | **PASS** | Root/branch/HEAD exact; clean worktree/index before, during, after; origin canonical; public branch ref equals HEAD; gitlink and checkout both `7478ddb`; `ap doctor` PASS; `ap project check` PASS on baseline `8c7858b`; `git diff --check` clean |
| B — AP-pin consumer rebaseline | **PASS** | `test_ap_integration.py` pins `7478ddb` and asserts gitlink==checkout; `README.md` current gitlink updated; `docs/AP_UPGRADE_OBSERVATIONS.md` and `test_worker_execution_contract.py` still truthfully record `7ef45da` (historical revalidation evidence, not rewritten); focused AP + worker-contract tests: 52 passed (incl. parity+companion in the same run); no blanket SHA replacement (`7ef45da` remains only in the two historical files) |
| C — metadata client/server parity | **PASS** | Fixture has 35 meaningful cases; Python executes real `MediaMetadataSaveRequest`, `CanonicalTagRequest`, `_parse_genres`; JS executes real `normalizedMetadataFormState`, `normalizedDescriptionState`, `tagDisplayNameError`, `normalizedTagDisplayName`, `uniqueTagKeyForDisplayName`, `hasControlCharacter`, `unicodeCodePointLength` plus real constants extracted from `app.js` in `node:vm`; no test-local validator reimplementation; no constant-duplication (the test extracts, does not restate); both languages consume the same case set. Required cases all present: title 240/241 ASCII and astral, C0/DEL/C1, description LF allowed + tab/CR/C1 rejected, tag C1, genres 8/9 |
| D — F2 Unicode title correction | **PASS** | `unicodeCodePointLength` uses `[...value].length`; title validator uses it; `maxlength="240"` removed from `#metadata-title-input` only (the other three `maxlength` attributes at lines 26/211/743 in `index.html` are unrelated fields, untouched); parity executes `title-240-astral` accepted / `title-241-astral` rejected against real client code and real server request model |
| E — F3 control-character correction | **PASS** | `hasControlCharacter` rejects `codePoint <= 0x1f || (0x7f..0x9f)`, matching Python `unicodedata.category == "Cc"` for BMP; description helper unchanged and still permits LF only; parity covers C0/DEL/C1 accept-reject on title and tag plus LF/tab/CR/C1 on description |
| F — F4 genre-count correction | **PASS** | `MAX_METADATA_GENRES = 8`; `normalizedMetadataFormState` returns existing `{error: "Select at most 8 genres."}` before the blank-title branch, disabling Save through the existing `updateMetadataControls` mechanism — no layout/styling/chrome added; server limit unchanged (`MAX_MEDIA_GENRES = 8` pre-existing); parity `genres-eight` accepted / `genres-nine` rejected |
| G — MediaAnalysisRunId correctness | **PASS** | `_parse_analysis_run_id` validates via `MediaId.from_string` (retained UUIDv4 shape + sanitized error mapping) then returns `MediaAnalysisRunId(parsed.to_string())`; regression asserts `isinstance(parsed, MediaAnalysisRunId)`, `not isinstance(parsed, MediaId)`, and value equality, plus a sanitized-failure test over three invalid forms; repository consumers call `.to_string()`, preserving downstream behavior |
| H — metadata source-test convergence | **PASS** | Slice `8c7858b..1f355a8` in `test_local_web_application.py`: only metadata-form spelling assertions retired (exact `[...value].length` spelling test, description UTF-16 source scan, description-control source scan, two lines inside the dirty/discard test), each superseded by executable parity cases; added one static absence guard (`test_browser_title_input_has_no_maxlength`); all `innerHTML`/`insertAdjacentHTML`/external-URL/secret/dialog structural guards preserved; count 209→207 |
| I — Slice 4a reachability and deletion | **PASS** | All named symbols deleted; whole-word residual scan across `src/`, `tests/`, `extension/` returns 0 obsolete references for every deleted symbol. The only apparent hits (`currentTags`, `addTag`, `renderList`) are confirmed test-local fixture fields in `upload_cockpit_async_ownership.test.js` and extension-local identifiers in `extension/ui/save.js`/`sidebar.js` — not app.js references. Deleted helpers verified caller-free or cluster-internal before deletion |
| J — movie-identification behavior preservation | **PASS** | `movieIdentificationIsPureUnknown` retained with live production caller `applyAnalysisStatusPayload` (app.js:6581); `applyAnalysisStatusPayload` still distinguishes pending/analyzing/analyzed/failed/not_requested/incomplete and still validates the local `movieResult` temporary feeding the unknown-detection and status message; the durable-state `movieResult` property is genuinely removed from all six object shapes and the return object, and its only prior reference was a browser-test manual seed (now removed); suggestion-strip renderers untouched, and the retired JS test's live absence guards (`handleSaveMetadata`, `method: "PUT"`) were migrated into the retained `durable renderer does not concatenate genres into tags` test |
| K — legacy library-browser reachability | **PASS** | At pre-deletion `1f355a8`: `index.html` contains 0 occurrences of `#library-list`/`#library-card-template`; the sole root `loadLibraries();` called a function whose first statement early-returns on those nulls; `renderLibraries` (the only event-handler registration site) repeated the guard; `db665e7` verifiably removed `<details id="library-browser">`, `<div id="library-list">`, `<template id="library-card-template">` from `index.html` while leaving JS behind; `extension/` and `companion_host.js` contain zero references to the anchors, functions, or any DOM injection path; no dynamic selector construction reaches the removed ids/classes. The cone was unreachable in the packaged application |
| L — shared/live dependency preservation | **PASS** | `LIBRARIES_ENDPOINT` present and used at app.js:4242 (retained preview-cluster fetch); `movieIdentificationIsPureUnknown`, `mediaContentUrl`, `mediaGalleryPreviewUrl`, `mediaCoverThumbnailUrl`, `coverTimeline/Frame/MutationEndpoint` (with live callers at 10559/10708/10794), `openOriginalIcon`, `editIcon`, `applyAnalysisStatusPayload`, `movieIdentificationStatusMessage` all present and used. Worker 03 did not delete the protected preview cluster or `LIBRARIES_ENDPOINT` |
| M — test retirement quality | **PASS** | Python 3392→3381 (11 retired: 1 in 4a, 10 in 4b after slice 4a's own 1; exact per-file counts: 207→196); JavaScript 461→460 (1 retired). Every retired test exclusively protected unreachable functionality, test-only production artifacts, or removed source structure. The one meaningful migration (no-Save/no-PUT strip guards) was relocated to a live test. The Tailscale change from an exact `28` count to `length > 0` + `mutationSites === wrappedSites` preserves the real safety invariant (every unsafe fetch site still carries the header; 23===23 verified) and the numeric pin was legitimately invalidated by deletion of 5 wrapped sites — an improvement in semantics, not a weakening |
| N — complete regression execution | **PASS** | JS: 465 tests, 460 pass, 5 skipped (all five are documented gated real-browser evidence suites), 0 fail. Python: 3381 passed, 8 skipped, 0 failed (520.00s) via the canonical AP route (the 8 skips are the pre-existing real-tool/live-provider gates). Focused runs separately below |
| O — candidate diff boundary | **PASS** | Full diff = 14 files, +623/−1352. Slice boundary `8c7858b..1f355a8` = 10 files, +585/−29. Slice boundary `1f355a8..33946e0` = 6 files, +38/−1323 (independently reproduced, matches Worker 03). No `styles.css`, no `pyproject.toml`, no migration/schema, no dependency change, no `.ap` change, no deployment file; `index.html` diff is exactly the one authorized `maxlength` attribute removal (2-line diff) |
| P — before/after architecture evidence | **PASS** | Independently measured: app.js 12,780→11,810 lines; top-level functions 564→515 (−49, 0 added). Answer to the acceptance question: **yes** — the deletion simplified the production client by removing behavior independently proven unreachable or test-only, without altering supported user-visible behavior, without framework/styling/module changes, and while the live card-media path (`renderCatalogCardMediaSurface` → `renderPersistentPreview`/`renderPreviewFallback`) and all metadata/AI/suggestion behavior remained intact and behaviorally covered |

## Contract correctness

- **F2 (title length):** client now counts Unicode code points (`[...value].length`) against server `len()` semantics; the compatible-UTF-16 `maxlength` attribute is gone so the explicit validator owns the contract. Astral 240 accepted / 241 rejected verified by executing the real client validator and the real server request model against the same fixture case.
- **F3 (controls):** client title/tag rejection now covers C0, DEL, and C1 (`U+0080–U+009F`), matching Python `Cc`; description semantics preserved (LF allowed, tab/CR/C1 rejected, outer whitespace rejected). No new policy invented; the change aligns one predicate with the pre-existing backend semantics and the sibling description helper.
- **F4 (genre count):** 8 accepted / 9 rejected client-side through the existing validation/status mechanism before any Save request; no backend or API limit was modified to satisfy the client.
- **F13 (run ID type):** successful parse returns a genuine `MediaAnalysisRunId`; UUIDv4 shape validation and sanitized not-found error contract retained; regression asserts the actual type behavior (`isinstance`/negative `isinstance`), not merely `.to_string()` equivalence. Downstream repositories call `.to_string()`, so runtime behavior is preserved.

## Test architecture

The parity mechanism genuinely executes both languages. The Python executor instantiates the real pydantic request models and the real `_parse_genres` used by the application; the Node executor extracts the real production functions and real constant declarations from `app.js` with a bounded brace-matching extractor and runs them in `node:vm` with only input stubs (`metadataTitleInput`, `metadataDescriptionInput`, `metadataWorkspace`, `canonicalTagDefinitions`). No validator is reimplemented in test code, no constants are restated, and no string-presence assertions are used for these cases. Both sides read the same 35-case fixture, so a drift on either side fails the corresponding suite. The source-text assertions retired in Gate H are exactly the ones whose guarantee is now behavioral; static security/absence assertions (dangerous HTML insertion, external URLs, secrets, dialog structure) were preserved because there the source-level absence is the contract.

## Slice 4 reachability

- **Slice 4a:** `COMPANION_REVIEW_INBOX_ENDPOINT`, `downloadIcon`, `mediaDownloadUrl`, `describeCatalogItem`, `buildProcessedTimeElement`, `openPlaybackDetails`, `resetMetadataWorkspaceAfterDiscard`, `ensureMetadataTagKey`/`metadataTagKeysFromSuggestion` — each verified definition-only (or cluster-internal) with zero production callers before deletion; the only test references were source-extraction pins or negative assertions, retired with the artifacts. Residual search: 0 obsolete production references, 0 obsolete test references.
- **Movie-identification path:** the superseded whole-result apply path (`applyMovieIdentificationToMetadataWorkspace`, `movieIdentificationHasLoadableFields`, `movieSuggestionFromResult`) is deleted; the live durable per-field suggestion-strip workflow is untouched; `movieIdentificationIsPureUnknown` remains live and behavior-tested (pure-unknown true; title-bearing unknown false; identified false; genre-bearing unknown false; null false).
- **`metadataDurableAnalysis.movieResult`:** independently confirmed write-only — the only property reads anywhere in `app.js` are `statusMessage` and `errorMessage`; the property was removed from all state shapes and the return object, while the local `movieResult` validation temporary in `applyAnalysisStatusPayload` is retained and still feeds unknown-detection and status messaging.
- **Legacy library browser cone:** independently proven unreachable at the pre-deletion commit through missing DOM anchors, the early-returning sole startup root, handler registration only inside the unreachable `renderLibraries`, `db665e7` history, and the absence of any extension/host/dynamic-selector mechanism to recreate the anchors; deleted as a coherent cone (38 functions plus DOM constants, request tokens, `MAX_REVIEW_TEXT`, `MEDIA_IMPORTS_ENDPOINT`, and the startup call), with all backend routes preserved.

## Preserved live behavior

- `movieIdentificationIsPureUnknown` — present, live caller `applyAnalysisStatusPayload`, behavior test retained/rewritten.
- `LIBRARIES_ENDPOINT` — present at app.js:4 and used at app.js:4242; Worker 03 did not delete it despite its own finding that the consumer cluster may be dead.
- Mutation-header invariant — `framenestMutationHeaders` injects `X-FrameNest-Request` exactly once; all 23 remaining unsafe fetch sites (`method: POST/PUT/PATCH/DELETE`) are wrapped (`23 === 23`), and the JS invariant test enforces both non-zero sites and full wrapping.
- Metadata parity — both executors green (35 Python / 35 JS) on the final tree; fixture unchanged after the RED→GREEN cycle.
- HTML insertion safety — `innerHTML`/`insertAdjacentHTML` count in `app.js` is 0; no external `http(s)://` URL literals in `app.js`; persistent storage remains limited to page-size preference and upload-recovery session data.

## Validation

Exact results on the exact committed tree (`33946e0`):

```text
ap doctor                        PASS (exit 0)
ap project check (baseline)      PASS (exit 0; sanitized-env WARN only)
Focused Python (AP integration + worker execution contract +
  metadata parity + companion review)   52 passed, 0 failed
Parity JavaScript                35 pass, 0 fail
Focused Python (local web application + parity)   239 passed, 0 failed
Focused JS (movie id + catalog card AI + browser evidence files)
                                 38 tests: 37 pass, 1 skipped (gated), 0 fail
Full Python (AP route, tests -q -p no:cacheprovider)
                                 3381 passed, 8 skipped, 0 failed (520.00s)
Full JavaScript (node --test tests/*.test.js)
                                 465 tests: 460 pass, 5 skipped, 0 fail (10.1s)
git diff --check                 clean (exit 0)
worktree/index                   clean before, during, after (0 entries)
Residual searches                every deleted symbol: 0 obsolete refs; remaining
                                 hits are test-local fixtures / extension-local names
```

The 8 Python skips are the pre-existing real-media-tool and live-provider gates; the 5 JS skips are the documented gated real-browser evidence suites (`FRAMENEST_RUN_BROWSER_EVIDENCE` not enabled in the standard environment). Neither class represents a collection gap introduced by this whole.

## Diff boundary

Changed files (14 total): `README.md`, `src/framenest/adapters/api/web/app.js`, `src/framenest/adapters/api/web/index.html`, `src/framenest/application/companion_review.py`, `tests/contract/test_ap_integration.py`, `tests/contract/test_companion_review_api.py`, `tests/contract/test_local_web_application.py`, `tests/contract/test_metadata_field_contract_parity.py`, `tests/metadata_form_contract.test.js`, `tests/movie_identification_frontend.test.js`, `tests/catalog_card_ai_quick_action.test.js`, `tests/browser_movie_identification_evidence.test.js`, `tests/tailscale_identity_frontend.test.js`, `tests/support/metadata_field_contract_cases.json`.

```text
styles.css                 absent (0 diff)
index.html                 only the authorized title maxlength attribute removal (1 line)
backend/API behavior       absent beyond the F13 parser fix (companion_review.py, +3/−2)
database/schema/migrations absent
dependencies/pyproject     absent
deployment/NUC/VPS         absent
.ap pin                    absent (gitlink unchanged at 7478ddb)
```

## Test retirement assessment

The reduction is justified. Python 3392→3381 (−11) and JavaScript 461→460 (−1) exactly match the implementation reports and map one-for-one to deleted unreachable or test-only functionality: the retired tests either asserted the existence/source spelling of deleted functions, executed deleted helpers that nothing called, or pinned a removed DOM surface. The one test whose body contained a live safety guarantee (no Save call, no `PUT`) had that guarantee migrated into a retained live renderer test, and the pure-unknown behavior survives in a rewritten behavior test. No meaningful guarantee was removed without replacement, and the Tailscale mutation-site change preserves the semantic invariant while removing a now-invalid hardcoded count.

## Residuals

- **R1 — catalog-card-preview cluster (`handleCardPreview`, `selectPreviewableLocation`, `getCachedPreview`, `setCachedPreview`, `renderCardPreviewState`, `renderCardPreviewFrames`, `startCardPreviewCycling`, `decodeBase64Png`):** classified **future-whole**. Independently confirmed: `handleCardPreview`'s only remaining caller is its recursive retry callback inside the cluster itself, and the live gallery path is `renderCatalogCardMediaSurface` → `renderPersistentPreview`/`renderPreviewFallback`; the former external caller was removed in `a15dfef`. Worker 03 correctly retained the cluster and `LIBRARIES_ENDPOINT` under the "retain ambiguous" rule after discovering the prompt premise was wrong. Deserves a separate bounded follow-up (delete the cluster, then re-evaluate `LIBRARIES_ENDPOINT` and the tests that assert its source shape).
- **R2 — `metadataDurableAnalysis.result`:** classified **parked**. Confirmed write-only (only `statusMessage`/`errorMessage` are ever read); outside the authorized deletion set; same class as the removed `movieResult`. Non-blocking; candidate for a future cleanup.
- **R3 — `previewObjectUrls`/`revokePreviewObjectUrls`:** classified **parked**. Confirmed no remaining producer after slice 4b (the only push site was in the deleted `renderAnalysisSuccess`); the live `pagehide` listener clears an always-empty array; removal was not authorized and leaving it is harmless.
- **R4 — dead legacy CSS (`.library-*` selectors in `styles.css`):** classified **parked**. Explicitly outside this implementation; `styles.css` untouched; suitable for later UI/UX-related cleanup.
- **New non-blocking observation:** the archived Worker 02 and Worker 03 reports carry a small preamble before the required report heading (archival-format defect only, no repository impact). Also noted: `metadataDurableAnalysis.result` and the retained preview cluster are the only remaining residuals that could interact with `LIBRARIES_ENDPOINT`'s future disposition.
- No residual was classified blocking.

## Acceptance verdict

The candidate satisfies the approved plan, both implementation prompts, and the acceptance matrix: current AP consumer state is coherent; the three verified client/server contract defects (F2/F3/F4) are corrected with executable cross-language parity protection; `MediaAnalysisRunId` parsing returns the correct domain type with a real type-behavior regression; the test-only and unreachable frontend artifacts were removed only after independently demonstrated reachability analysis; the legacy development-library cone was genuinely unreachable at the pre-deletion commit and could not be recreated by any supported host mechanism; live movie-identification, suggestion-strip, metadata, catalog, cover, gallery, and mutation-header behavior is preserved; and both complete suites are green on the exact reviewed commit with a clean worktree. The newly discovered residuals are correctly classified as future work or parked and do not block this acceptance.

The implementation candidate is accepted. The logical whole is not yet publication-closed. Publication/deployment authority was not granted.

```text
acceptance-PASS
```