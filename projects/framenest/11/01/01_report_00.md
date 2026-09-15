### Report for ORCHESTRATOR_CHAT

**AP coordinates**

| Field | Value |
|---|---|
| Role | `WORKER` |
| Profile | `Planner` (native planning mode, required) |
| Session | `fresh-worker-session` / ordinal `01` |
| Exchange | `01` |
| Planning layer | `implementation-planning` |
| Orchestration planning owner | `ORCHESTRATOR` |
| Implementation in this session | **prohibited** (none performed) |
| Plan disposition | `approval-gated` |
| Delivery route | manual Cooperator delivery through ChatOrchestrator |
| Reasoning expectation | High |
| Terminal planning status | **COMPLETE — plan ready, approval-gated** |

---

## 1. Verified baseline

*Read-only. No repository mutation. Working tree clean (`git status --porcelain` empty).*

| Item | Verified value |
|---|---|
| Physical repository root | `/home/agile/Projects/framenest` |
| Current branch | `feat/x-meme-browser-companion` |
| Current HEAD | `8c7858b62beca3c4ee92bb8f1f095b98063e2c94` |
| Public `origin/main` | `a4193d4f520a30aafa333987f2e6b846a5425d27` |
| Public `origin/feat/x-meme-browser-companion` | `a4193d4f520a30aafa333987f2e6b846a5425d27` |
| Local vs public | `8c7858b` is **local-only** (ahead 1). Its entire diff is `.ap` gitlink `7ef45da…` → `7478ddb…`. Nothing else is unpublished. |
| Canonical origin | `https://github.com/cisarik/framenest.git` |
| `.ap` gitlink | `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` |
| `.ap` checkout HEAD | `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`, clean |
| `./.ap/ap doctor` | `PASS` (strict pinned AP commit OK, managed block OK, stable variant) |
| `./.ap/ap project check --baseline 8c7858b…` | `PASS` (warn: sanitized inherited env classes only) |
| Runtime | `.venv` CPython 3.13.9 (via AP envelope); Node v26.8.1 |
| Worktrees/branches | 57 registered worktrees, 41 local branches (local hygiene only, not a product defect) |
| External trace/report | No FrameNest trace directory or restoration handout was provided or discoverable. No external artifact was consumed; nothing external was mutated. |

**Executed baseline evidence (exact commands):**

```text
./.ap/ap doctor
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 8c7858b62beca3c4ee92bb8f1f095b98063e2c94
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 8c7858b62beca3c4ee92bb8f1f095b98063e2c94 --operation test-focus -- tests -q -p no:cacheprovider
node --test tests/*.test.js
```

| Suite | Result |
|---|---|
| Full Python suite | **1 failed, 3356 passed, 8 skipped** in 524.22 s (8m44s) |
| The single failure | `tests/contract/test_ap_integration.py::test_ap_submodule_gitlink_and_configuration_are_pinned` — expects `7ef45da…`, actual `7478ddb…` |
| Full JS suite | **426 pass, 0 fail, 5 skipped** (gated browser evidence) in 10.1 s |

The repository is otherwise green, including the 224-test packaged-web contract suite. The sole red test is a stale AP-pin expectation left behind by local commit `8c7858b`.

---

## 2. Audit methodology

What was actually inspected and executed (not exhaustive):

1. **Repository archaeology** — `git log/show/rev-parse/ls-remote/worktree`, `git log -S` on every disputed symbol (`applyMovieIdentificationToMetadataWorkspace`, `movieSuggestionFromResult`, `metadataTagKeysFromSuggestion`, `resetMetadataWorkspaceAfterDiscard`, `describeCatalogItem`, `downloadIcon`, `mediaDownloadUrl`, `library-card-template`, `library-browser`), reading `22352c9`, `2e39c4d`, `6b957be`, `db665e7`, `3b98b8c`, `460b37b`.
2. **Source reading** — full or region reads of `app.js` (constants block, validation cluster 2424–2633, classification/genres 10436–10500, AI suggestion/durable analysis 6519–7100, dead clusters 9933–10434, 2347–2422, 4664–5004), `index.html` (all `id`/`maxlength` occurrences), `application.py` (composition + `_x_forbidden_roots`), `companion_review.py`, `identities.py`, `media_analysis_runs.py`, `media_metadata.py`, `media_classification.py`, `youtube_acquisition.py`, `media_metadata_api.py`, `SECURITY.md`.
3. **Test topology** — full inventory of 237 Python test files (87,805 lines) / 28 JS test files (20,386 lines); source-scraping helper census; skip/xfail/TODO census; duplication census.
4. **Parallel explore agents** (research-only) — frontend architecture map, test topology map, composition-root audit, filesystem-residual audit.
5. **Execution** — canonical AP test route (full suite, focused suites), `node --test`, and Node in-memory reproductions for UTF-16/code-point counting and C1 control semantics.
6. **Verification discipline** — every material defect below was reproduced at source level; the *reachability* of Lead E's original reproducer was corrected (see F2).

Not inspected deeply (honest classification): NUC/operator network scripts, backup engines, YouTube/X adapters beyond contract-relevant validation, and Alembic migration bodies beyond head/shim scan. These were not implicated by any lead and are out of this whole's scope.

---

## 3. Architecture map

**Python backend** (`src/framenest/`, ~48k lines)
- `domain/` — typed value objects and StrEnums (`identities.py` UUIDv4 wrappers; `media_metadata.py` title/description/tag/creator values with limits; `media_classification.py` `MovieGenre`/`ContentCategory`/`AcquisitionSource`; `uploads.py` 12-state `UploadSessionState`; `media_analysis_runs.py` opaque `MediaAnalysisRunId`).
- `application/` — use cases (`companion_review.py`, `media_metadata.py`, `upload_transport.py`, acquisition lifecycles).
- `infrastructure/` — SQLite/Alembic persistence (head `0033`), filesystem storage (`media_content.py` reader, `published_media_storage.py` writer), AI, YouTube, X adapters.
- `adapters/api/` — 25 routers composed by `application.py::create_app` (defined at `application.py:346`, ~1,073 lines, 30 all-optional parameters, 17+ `app.state` entries, 25 `include_router`); a second `public_published_application.py` composition for the public reader.

**Frontend** (`src/framenest/adapters/api/web/`)
- Single classic script `app.js` (12,776 lines, 564 top-level functions, no modules/classes/IIFE), `index.html` (1,002 lines, no inline handlers), `styles.css` (5,063 lines), `companion_host.js` (195 lines).
- ~263 top-level DOM constants; ~55 direct `fetch(` call sites with only one wrapper (`fetchUploadJson`, upload-only); no central router; per-feature request-token ownership as the concurrency model; no `console.*`.
- Distinct live clusters: identity/capability gates, health/status, upload cockpit, catalog query/cards, metadata workspace/editor + AI suggestions, admin catalog/batch, workspace media, proposals, cover chooser, YouTube claim/request cockpits, X cockpit.
- **Two whole dead clusters**: a legacy "development library + AI review" cluster (~40 functions, 2347–2422 / 4683–4860 / 9933–10434) made unreachable by `db665e7` when `#library-list`/`#library-card-template` were intentionally removed from `index.html`; and scattered test-only artifacts in live clusters.

**Tests**
- Python: 2,648 tests, no `conftest.py`, no CI config; `contract/` (72 files) dominates; `tests/contract/test_local_web_application.py` is a 3,051-line source-scraper of `app.js`/`index.html`/`styles.css`.
- JS: 28 `node:test` suites; 16 extract named functions from `app.js` and execute them in `node:vm`; 4 gated Chrome/CDP browser-evidence suites (no Playwright).
- There is **no behavioral coverage whatsoever** of the metadata form validators (F5).

---

## 4. Finding register

Severity: S1 critical … S4 informational. Confidence: high/medium/low.

### F1 — Local AP pin update leaves an executable contract test red
- **Location:** `tests/contract/test_ap_integration.py:10` (`EXPECTED_AP_COMMIT = "7ef45da…"`), local commit `8c7858b`.
- **Evidence:** canonical focused run fails: `assert '7478ddb…' == '7ef45da…'`. Full suite: 1 failed / 3356 passed.
- **Reproduction:** `./.ap/ap exec … --operation test-focus -- tests/contract/test_ap_integration.py -q`.
- **Severity:** S2 (blocks a green baseline; blocks any "full suite green" claim). **Confidence:** high.
- **Current tests:** the failing test itself. **Why not detected earlier:** the pin commit updated `.ap` only.
- **Disposition:** prerequisite slice 0.

### F2 — Title length contract divergence: UTF-16 code units vs Unicode code points
- **Location:** `app.js:64`, `app.js:2484` (`rawTitle.length > MAX_METADATA_TITLE_CODE_POINTS`), `index.html:596` (`maxlength="240"`); backend `domain/media_metadata.py:22` + `MediaDisplayTitle` (`len(value) > 240`).
- **Evidence:** constant is named `…CODE_POINTS`, frontend counts UTF-16 units; backend counts code points. Node reproduction: `"😀".repeat(240).length === 480`, `[...s].length === 240`.
- **Reachability correction (important):** the previously supplied "240 × 😀 typed by user" reproducer is **not directly reachable** because `maxlength="240"` also counts UTF-16 units and truncates typed/pasted input at 120 astral characters. The reachable path is programmatic assignment: `copySuggestionFieldToCurrent` (`app.js:6804`) sets `metadataWorkspace.current.displayTitle` and `renderMetadataWorkspace` assigns `metadataTitleInput.value` directly; `maxlength` does not constrain programmatic values. A 130-emoji AI-suggested title (260 UTF-16, 130 code points) is accepted by the server and rejected client-side with "Title must be 240 characters or fewer.", disabling Save. Symmetrically, the input cannot represent legitimately server-valid titles above 120 astral characters.
- **Severity:** S3 (misleading rejection of server-valid data on the exact surface the Cooperator will test on NUC). **Confidence:** high (code + Node), reachability medium-high.
- **Current tests:** none behaviorally; `test_local_web_application.py:386–389` pins only the *description* path. **Why not detected:** no behavioral test executes the title validator.
- **Disposition:** in scope, slice 1.

### F3 — Control-character divergence: C1 controls accepted client-side, rejected server-side
- **Location:** `app.js:2428` `hasControlCharacter` rejects only `<= 0x1f` and `0x7f`, used at `app.js:2481` (title) and `app.js:2557` (tag display name). Backend `_has_control_character` uses `unicodedata.category(ch) == "Cc"`, which includes C1 `U+0080–U+009F`; used by `MediaDisplayTitle`, `CanonicalTagDisplayName`, creator normalizers.
- **Evidence:** Node reproduction: frontend `hasControlCharacter("\u009f") === false`; Python `unicodedata.category("\u009f") == "Cc"`. The sibling description helper `hasForbiddenDescriptionControlChar` (`app.js:2440`) **does** cover `0x7f–0x9f` — the frontend is internally inconsistent, proving intent.
- **Impact:** a title or new-tag display name containing e.g. U+0085/U+009F passes client validation, then the server returns the uniform sanitized 422 and the UI shows generic "Save failed."/generic tag-create error.
- **Severity:** S3. **Confidence:** high.
- **Current tests:** none; no behavioral test for title/tag-name controls.
- **Disposition:** in scope, slice 1.

### F4 — Genre-count divergence: client has no cap, server caps at 8
- **Location:** `app.js:10431` `MOVIE_GENRE_OPTIONS` (14 display names), change handler `app.js:10464–10476` (no limit), `normalizedMetadataFormState` no genre validation; backend `MAX_MEDIA_GENRES = 8` (`media_classification.py:96`), enforced in `media_metadata_api.py:177–182` (`> 8` → request validator → uniform 422 `VALIDATION_FAILED`).
- **Evidence:** Node reproduction: 9 selectable options, backend constant 8. No `MAX_MEDIA_GENRES`/`8` guard anywhere in `app.js`.
- **Impact:** user selects 9 genres (movie category), Save is enabled, server rejects, UI shows generic "Save failed." with no corrective message.
- **Severity:** S3. **Confidence:** high.
- **Current tests:** none behavioral.
- **Disposition:** in scope, slice 1.

### F5 — No behavioral coverage of metadata form validation; the accidental contract is source text
- **Location:** `tests/contract/test_local_web_application.py` (209 tests; 167 touch web-asset text by a conservative awk count; 112 `_javascript_function` extractions; 93 tests contain only source-substring assertions); no JS suite references `normalizedMetadataFormState`, `normalizedDescriptionState`, or `tagDisplayNameError`.
- **Evidence:** `rg "normalizedMetadataFormState|normalizedDescriptionState" tests/*.test.js` → no matches. Python tests that pin the description code-point behavior (386–400) have no title/tag/genre analogue — precisely why F2–F4 survived.
- **Severity:** S2 (test-debt root cause of F2–F4 and F9). **Confidence:** high.
- **Disposition:** in scope — this is the whole's testability problem.

### F6 — Dead movie-identification apply path and write-only `movieResult` state
- **Location:** `app.js:5404 applyMovieIdentificationToMetadataWorkspace`, `5464 movieSuggestionFromResult`, `5448 movieIdentificationHasLoadableFields` (only called by 5464), `7174 metadataTagKeysFromSuggestion`; write-only `metadataDurableAnalysis.movieResult` (`app.js:266, 6548, 6923, 6946, 6970, 7004–7027`) — assigned and reset but never read; the live path is the durable suggestion list (`refreshMetadataSuggestionList`/`renderMetadataSuggestionStrips`).
- **Evidence:** whole-word grep shows zero production callers; `git log -S` shows commit `6b957be` ("copy AI suggestion fields one at a time") removed all call sites but not the functions.
- **Severity:** S4 (dead residual; confuses future work). **Confidence:** high.
- **Current tests:** `tests/movie_identification_frontend.test.js` executes them (lines 123–431); `tests/catalog_card_ai_quick_action.test.js:532,1140` asserts `metadataTagKeysFromSuggestion` is not called.
- **Disposition:** in scope, slice 4.

### F7 — Unreachable legacy development-library cluster kept alive by tests
- **Location:** `app.js` ~40 functions spanning 2347–2422, 4683–4860, 9933–10434 (`renderLibraries`, `loadLibraries`, `showLibraryState`, `handleInspectClick`, `handleImportClick`, `renderScanResult`, `renderAnalysisSuccess`, `renderEditableReview`, `validateReview`, `handleAnalyzeClick`, `handlePreviewClick`, `previewElements`, `aiElements`, `resetAiReview`, …), plus `libraryList`/`libraryCardTemplate` (`app.js:681,686`), `MAX_REVIEW_TEXT` (`:68`), `LIBRARIES_ENDPOINT` (`:3`), and the startup call `loadLibraries();` (`app.js:12144`, which returns immediately because the anchors are null).
- **Evidence:** `#library-list`/`#library-card-template` do not exist in `index.html` or anywhere in the repository; commit `db665e7` ("apply rendered acceptance feedback", 2026-07-01) removed the library browser from `index.html` and rewrote tests to assert its absence, but left the JavaScript. `renderLibraries` early-returns at `app.js:10393`.
- **Severity:** S3 (dead mass that future UI/UX work must reason around; tests preserve it). **Confidence:** high (only a hypothetical external host page could reactivate it; none exists in-repo).
- **Current tests:** `test_local_web_application.py` asserts `"function handlePreviewClick"`, `"loadLibraries();"`, `"handleInspectClick"` etc. are present.
- **Disposition:** in scope, slice 4b.

### F8 — Zero-caller live-cluster helpers
- **Location:** `app.js:2400 downloadIcon`, `app.js:4448 mediaDownloadUrl`, `app.js:6056 describeCatalogItem`, `app.js:11 COMPANION_REVIEW_INBOX_ENDPOINT`.
- **Evidence:** repo-wide whole-word search finds definitions only (plus a negative test at `test_local_web_application.py:1814/1816` pinning that `mediaDownloadUrl` is *not* used on cards). Git history: `downloadIcon`/`mediaDownloadUrl` from commit `bdffa23` after the download UI was removed; `describeCatalogItem` from `74fc43b` never wired.
- **Severity:** S4. **Confidence:** high.
- **Disposition:** in scope, slice 4a.

### F9 — Production helpers whose only consumers are tests
- **Location:** `app.js:4664 buildProcessedTimeElement`, `app.js:5002 openPlaybackDetails`, `app.js:7631 resetMetadataWorkspaceAfterDiscard`.
- **Evidence:** zero production callers; tests extract and assert their bodies (`test_local_web_application.py:1018–1023, 1054–1103, 2197–2209`). The tests prove nothing about production because nothing calls the functions.
- **Severity:** S3 (test-only production artifacts). **Confidence:** high.
- **Disposition:** in scope, slice 4a.

### F10 — Python source-scraping test architecture
- **Location:** `tests/contract/test_local_web_application.py` (helpers `_javascript_function` L68–81 with 112 call sites; `_evaluate_upload_should_poll` L84–111; `_css_rule_declarations` L114–131; fragile `script.index("\n}\n")` body slicing; negative absence assertions). `tests/contract/test_youtube_creator_taxonomy_frontend.py` (4 tests, all source scraping).
- **Evidence:** representative assertions pin formatting-sensitive source: `assert "rawTitle.trim() !== rawTitle" in script` (L484), `assert "unicodeCodePointLength(rawDescription) > MAX_METADATA_DESCRIPTION_CODE_POINTS" in script` (L388), `assert "buildProcessedTimeElement" in script` (L1069). Any behavior-preserving rename/reformat breaks them; conversely F2–F4 prove they cannot detect semantic drift.
- **Duplicate coverage verified:** `uploadShouldPoll` (Python Node-executed L2995–3051 vs `tests/upload_cockpit_async_ownership.test.js:3531–3577`); catalog card AI action (Python L1938–1963 + taxonomy file vs `tests/catalog_card_ai_quick_action.test.js:1116–1288`); YouTube filter/chips (taxonomy file vs `tests/gallery_filter_controls.test.js`, `gallery_search_tag_filters.test.js`).
- **Severity:** S2 (test brittleness + false confidence). **Confidence:** high.
- **Disposition:** in scope — narrow convergence around the metadata-form seam; no wholesale rewrite.

### F11 — X request audit recorder wired to the wrong (unresolved) recorder
- **Location:** `application.py:1067–1075` passes the raw `security_audit_recorder` into `XRequestApiDependencies`; `resolved_audit_recorder` is computed later at `application.py:1189–1196` and used by YouTube bundles (`:1206, :1216`).
- **Evidence:** under Tailscale ingress with no injected recorder, `x_request_api.py:316–317` returns without recording the supplemental `x.request.*` classification detail, while middleware still records the action (`tailscale_ingress.py:565–581`).
- **Severity:** S4 (data completeness, not access control). **Confidence:** high on wiring, medium on intent.
- **Disposition:** out of this whole; parked as follow-up (composition/audit wiring whole).

### F12 — `_x_forbidden_roots` fails open with a no-op except
- **Location:** `application.py:1573–1580` — `except Exception: forbidden_roots = forbidden_roots`; compare `_resolve_youtube_staging` (`:1546–1556`) which raises `ValueError` (fails closed).
- **Evidence:** self-assignment is a no-op; on library-enumeration failure X staging is constructed without registered library roots in the forbidden set.
- **Severity:** S3 (requires `x_acquisition_root` configured plus catalog enumeration failure). **Confidence:** high on code, medium reachability.
- **Disposition:** out of this whole; parked (same follow-up as F11).

### F13 — Domain-ID type confusion: analysis-run IDs parsed as media IDs
- **Location:** `application/companion_review.py:621–631` `_parse_analysis_run_id` returns `MediaId.from_string(value)` while annotated `MediaAnalysisRunId`; used at `:658` and `:696`.
- **Evidence:** `MediaAnalysisRunId` is an opaque `str` wrapper with only `to_string()`; `MediaId` is a UUIDv4 wrapper. Run IDs are generated as `str(uuid.uuid4())` (`media_analysis_run_repository.py:544`), so the wrong parser produces a correct string by accident. `_UuidIdentity.__hash__` includes the concrete type, so the substitution is invisible only because the repository calls `.to_string()`.
- **Severity:** S3 latent (would surface as soon as run IDs are not UUIDv4 or if values are compared as typed objects). **Confidence:** high.
- **Current tests:** focused companion-review tests pass — they assert behavior, not types. **Why not detected:** permissive runtime typing plus identical `to_string()` surfaces across ID wrappers.
- **Disposition:** in scope as a minimal correctness fix (return `MediaAnalysisRunId(value)` after a UUIDv4 shape check, or add `from_string` to `MediaAnalysisRunId`), with a regression test asserting the parsed type. Keep bounded to this parser; no type-system redesign.

### F14 — No CI and an 8m44s full Python suite
- **Evidence:** no `.github/workflows`, no Makefile, no `package.json`; suite runtime measured. Not a defect; an operational constraint for future whole sizing.
- **Disposition:** follow-up candidate only.

### F15 — Local branch/worktree sprawl
- **Evidence:** 41 local branches, 57 registered worktrees, many acceptance/publish snapshots. Not a product defect; no remote impact.
- **Disposition:** parked, Cooperator-owned hygiene.

---

## 5. Previous ChatOrchestrator lead disposition

| Lead | Disposition | Evidence |
|---|---|---|
| **A — frontend monolith growth** | **Partially confirmed** | Size/function counts confirmed (12,776 lines / 564 functions). The measurable problems are not size: dead clusters (F7, F9), test-only artifacts (F6, F9), 8 clusters writing `catalogState`, 55 unwrapped `fetch` sites, 263 top-level DOM constants. No framework migration is justified by any evidence found. |
| **B — Python source-scraping JS tests** | **Confirmed (refined)** | 209 tests, 112 function extractions, 93 pure substring tests, 2 files scrape JS, fragile body slicing, verified duplication with JS suites. The smallest high-value seam is metadata form validation (F5), where zero behavioral coverage exists and three defects hide. |
| **C — recent stale frontend assertions** | **Confirmed with nuance** | `22352c9` realigned 340 lines of `movie_identification_frontend.test.js` to changed editor surfaces; `2e39c4d` realigned Python API tests to the accepted 422 contract and ledger state. The first supports refactor-coupling; the second is legitimate behavior drift. Neither alone proves behavior-preserving refactors break tests; the source-text assertions in F10 do. |
| **D — helpers without production callers** | **Confirmed and extended** | All four verified zero-caller; additionally `mediaDownloadUrl`, `COMPANION_REVIEW_INBOX_ENDPOINT`, `buildProcessedTimeElement`, `openPlaybackDetails`, `resetMetadataWorkspaceAfterDiscard`, `metadataTagKeysFromSuggestion`, `movieIdentificationHasLoadableFields`, and the whole F7 cluster. All are test-referenced or unambiguously unreferenced; none is a browser-global API (`window.*` exposure absent). |
| **E — Unicode title contract drift** | **Confirmed; reachability corrected** | Defect real (F2). The supplied 240-emoji *typing* reproducer is blocked by `maxlength`; the reachable path is programmatic (AI copy). Same class extended to C1 controls (F3) and genre count (F4). |
| **F — domain type confusion** | **Confirmed** | F13 exactly as reported; tests pass because both wrappers expose identical `to_string()`/`from_string()` and run IDs happen to be UUIDv4. |
| **G — composition root size** | **Partially confirmed** | 1,073-line function, 30 parameters, 165 assignments, 25 routers, 17+ repositories, no unused locals, no cross-app state leak. Two real but minor wiring defects (F11, F12) discovered; the dominant issue is verbosity, not broken wiring. Parked. |
| **H — secure media TOCTOU residual** | **Confirmed, still live, accepted** | `SECURITY.md:298–309` (recorded by `3b98b8c`); `media_content.py` resolve-then-`os.open` with `O_NOFOLLOW` final component only; no dirfd/lstat/re-validation; no race test exists. Requires local write access inside a registered root. Deserves its own security whole — not this one. |
| **I — unused Python scaffolding** | **Confirmed as unreferenced; classified** | `MediaAnalysisLifecycleDisabledError`, `MediaSuggestionConnectionTester`, `YouTubeRequesterPrivateAccess`, `YouTubeStagingLimitExceededError`, `default_classification_fields()` have zero references beyond their definitions. Classified as dormant API/scaffolding, not proven dead. Recommended out of this whole (Python cleanup would add review surface without behavior value); follow-up candidate. |
| **J — AP pin rebaseline drift** | **Confirmed** | Executable defect: `test_ap_integration.py:10` is red. Stale active doc: `README.md:620` still names `7ef45da…`. Historical record: `docs/AP_UPGRADE_OBSERVATIONS.md` + `test_worker_execution_contract.py:83–86` — these truthfully record the last revalidation SHA and should not be silently rewritten. Exactly a tiny prerequisite, as suspected. |

---

## 6. Additional findings (not supplied by ChatOrchestrator)

1. **The metadata form validators have zero behavioral tests (F5)** — the root cause that allowed F2–F4.
2. **C1 control divergence (F3)** — a second, independent parity defect, with frontend-internal inconsistency proving intent.
3. **Genre-count divergence (F4)** — a third parity defect, client-permissive, 14 options vs server cap 8.
4. **The dead legacy cluster is a documented consequence of intentional UI removal (F7)** — `db665e7` removed the UI and rewrote acceptance tests, but left the JS and some tests pinning its presence.
5. **Dead-movie-identification path and write-only `movieResult` state (F6)** — superseded by the durable suggestion-strip mechanism in `6b957be`.
6. **Composition wiring defects F11 (X audit recorder) and F12 (no-op except)** — real but minor; parked.
7. **`MediaAnalysisRunId` has no `from_string` at all** — the deeper structural cause of F13 (an opaque wrapper participating in a UUID-parser family with no type discrimination).
8. **Reachability correction to Lead E's reproducer** — the reported 240-emoji typing path is blocked by `maxlength`; the true reachable path is programmatic AI-suggestion copy.
9. **No CI and 8m44s full-suite time** — sizing constraint for future wholes.
10. **Local `8c7858b` is unpublished while public `main` still pins `7ef45da`** — NUC refresh from public `main` would deliver the old pin; the prerequisite slice plus publication decision is required for public consistency.

---

## 7. Accepted / historical residual review

Reviewed and deliberately **not** resurrected:

- Media content reader TOCTOU residual (`SECURITY.md:298–309`, commit `3b98b8c`) — documented accepted position; final-component `O_NOFOLLOW` retained; `openat`/dirfd hardening explicitly not chosen. **Separate future security whole.**
- Analysis tool-execution TOCTOU (ADR-0015:119,173) — accepted, same classification.
- Multiprocess upload/publication ownership (ADR-0042:96–99, ADR-0043:63–96) — deliberate single-process boundary.
- Windows `os.replace`/case-folding evidence incompleteness (ADR-0059, `SECURITY.md:349–350`).
- Companion residuals: Brave framing, `chrome.storage.local`, signed-in X DOM evidence (`docs/X_COMPANION.md:214–225`, ADR-0063/0074).
- `legacy_backfill` publication origin and `UnsupportedLegacyUploadPublicationStateError` — intentional compatibility for historical data.
- ADR-0025 "catalog remains incomplete" prose — historical, superseded by later catalog ADRs.
- Local `8c7858b` and branch/worktree sprawl — local state, not product truth.

---

## 8. Prioritization

| Rank | Finding | Correctness | Security | Operational | Test cost | NUC-test impact | Correction cost/risk |
|---|---|---|---|---|---|---|---|
| 1 | F1 AP pin red test | High (baseline integrity) | None | High | Trivial | Indirect | 2 files, trivial |
| 2 | F5 no behavioral metadata-form coverage | High (root cause) | None | Medium | Medium | Direct | ~2 new tests, low |
| 3 | F2 title UTF-16 | Medium | None | Medium | Low | Direct (AI copy/Save) | 3 lines + input attr |
| 4 | F3 C1 controls | Medium | None | Medium | Low | Direct (Save/tag create) | 3 lines |
| 5 | F4 genre cap | Medium | None | Medium | Low | Direct (Save) | ~4 lines |
| 6 | F13 analysis-run ID type | Low now, latent | None | Low | Low | Indirect | ~6 lines + test |
| 7 | F9 test-only helpers | Low | None | Medium (future change cost) | Medium | Indirect | deletions + test retirement |
| 8 | F7 dead legacy cluster | Low | None | Medium (future change cost) | Medium | Indirect | ~40 function deletions + test retirement |
| 9 | F8 zero-caller helpers | Low | None | Low | Low | Indirect | small deletions |
| 10 | F6 dead movie path / `movieResult` | Low | None | Medium | Medium | Indirect | deletions + JS test surgery |
| 11 | F10 source-scraping architecture | None directly | None | High (long-term) | High | Indirect | bounded seam only |
| 12 | F11/F12 composition wiring | Low | Low-Med | Low | Low | None | 2 small changes (parked) |
| 13 | TOCTOU (F- H) | Low (accepted) | Bounded | None | Medium | None | separate whole |
| 14 | Lead I scaffolding | None | None | Low | Low | None | parked |

---

## 9. Recommended next logical whole

**Identity (preferred, unchanged):**

```text
framenest-web-client-contract-and-testability-convergence
```

**Problem statement.** The FrameNest web client re-implements server-owned metadata validation in vanilla JavaScript with no behavioral test coverage and no reliable ownership mechanism, and three concrete client/server divergences are verified: title length is measured in UTF-16 code units instead of Unicode code points (while the input's `maxlength` has the same flaw), C1 control characters are accepted by the client and rejected by the server, and movie genres have no client cap against the server's maximum of eight. Because the Python contract suite pins frontend behavior by scraping source text rather than executing it, it could not detect these divergences — and it simultaneously keeps several unreachable or test-only functions alive, so the frontend cannot be changed safely. This whole closes the verified divergences, introduces a bounded cross-language contract mechanism so the metadata field contract can no longer drift silently, gives the metadata form validators real behavioral tests, and retires only the frontend artifacts that are proven dead or test-only.

**Why it should precede UI/UX polish.** UI/UX polish will multiply frontend edits. Today, edits to the metadata editor and AI suggestion surfaces are protected only by text-matching tests, and the divergences produce generic "Save failed." states on the exact surfaces the Cooperator will exercise against the NUC. Making the contract executable and the dead mass explicit first means polish changes land against tests that describe behavior, and the dead-code elimination removes whole regions of the file that would otherwise be re-reviewed during polish. The sequencing constraint (no polishing now) is respected: this whole contains no visual change.

**Prerequisite relationship:** slice 0 (F1) must land first so the baseline is green and public consistency is decided; it is one commit, not part of the whole's substance.

---

## 10. Exact scope

In scope:

1. **Slice 0 prerequisite:** correct the executable AP-pin expectation and the stale README gitlink (F1, Lead J).
2. **Slice 1 verified fixes (F2, F3, F4, F13):**
   - `app.js`: title length validation uses `unicodeCodePointLength`; `hasControlCharacter` rejects C1 as `Cc` does; a bounded genre-count validation (`MAX_METADATA_GENRES = 8`) with a clear status message; remove `maxlength="240"` from `#metadata-title-input` (mirroring the accepted description precedent).
   - `companion_review.py`: `_parse_analysis_run_id` returns a genuine `MediaAnalysisRunId` (with a UUIDv4 shape guard) and a regression test asserts the type.
3. **Slice 2 contract-parity mechanism (F5):** a shared `tests/support/metadata_field_contract_cases.json` fixture plus a Python parity test (server side executes real domain types) and a Node parity test (client side executes the real extracted validators). Fixture must include the F2/F3/F4 families.
4. **Slice 3 metadata-form test convergence:** retire the metadata-form source-text assertions that are now behaviorally covered, keeping static security/absence guards.
5. **Slice 4 dead/test-only frontend artifact retirement:** 4a test-only helpers in live clusters (F9, F6, F8); 4b the unreachable legacy development-library cluster (F7). Slice 4 is independently descopable without invalidating slices 1–3.
6. Documentation touched only where correctness requires (README pin).

## 11. Explicit non-scope

- Any `styles.css` change; any visual redesign, restyling, counter, or layout work.
- React/Vue/Svelte/TypeScript migration; any bundler; any ES-module split of `app.js`.
- Rewriting or retiring the entire Python source-scraping suite; only the metadata-form cluster is converged.
- `create_app()` refactor; composition/DI redesign; F11/F12 wiring fixes.
- TOCTOU/`openat` filesystem hardening; published-media storage changes.
- Database/schema/migration changes; API response-shape changes; new endpoints.
- Python scaffolding removal (Lead I).
- NUC/VPS deployment work, provider calls, media access, Git commits/pushes (unless separately authorized).
- Feature development of any kind.

## 12. Proposed implementation architecture

**Ownership mechanism (the core decision).** Because FrameNest has no bundler, no `package.json`, and serves `app.js` as a static packaged asset, the minimal reliable mechanism is a **shared acceptance-case fixture executed by both languages**:

- `tests/support/metadata_field_contract_cases.json` — canonical cases: `{field, value, expected}` for fields `title`, `description`, `tag_display_name`, `genre_set`; `expected ∈ {accepted, rejected}`; control characters and astral values expressed as JSON escapes.
- `tests/contract/test_metadata_field_contract_parity.py` — for each case, run the real Python domain constructors (`MediaDisplayTitle`, `MediaDescription`, `CanonicalTagDisplayName`, genre limit through `MediaMetadataSaveRequest` semantics) and assert agreement with `expected`. This makes the server the authority and fails if the fixture drifts from server behavior.
- `tests/metadata_form_contract.test.js` — extract `normalizedMetadataFormState`, `normalizedDescriptionState`, `tagDisplayNameError` from `app.js`, execute them in `node:vm` with stub `metadataTitleInput.value` / `metadataDescriptionInput.value` / `metadataWorkspace.current`, and assert agreement with `expected` for every case. This is the cross-language parity gate and the regression guard for F2–F4.

This is deliberately *not* schema generation and adds no runtime fetch, no build step, and no packaging change (fixture lives under `tests/`). A runtime-API alternative (server-advertised limits) was considered and rejected: it would add async ordering and failure modes to client-side validation for negligible benefit.

**Production changes (slice 1), precise:**
- `app.js` constants block: add `const MAX_METADATA_GENRES = 8;` next to the other metadata limits.
- `app.js:2428–2437` `hasControlCharacter`: reject `codePoint <= 31 || (codePoint >= 127 && codePoint <= 159)`; the description helper already does this and stays.
- `app.js:2484`: `unicodeCodePointLength(rawTitle) > MAX_METADATA_TITLE_CODE_POINTS`.
- `normalizedMetadataFormState`: after the title checks and **before** the blank-title branch, return `{ error: "Select at most 8 genres." }` when `(metadataWorkspace.current.genres || []).length > MAX_METADATA_GENRES` so both branches are covered; `updateMetadataControls` already disables Save and surfaces the message.
- `index.html:596`: remove `maxlength="240"` (programmatic value paths already bypass it; the validator is the contract).
- `companion_review.py:621–631`: parse via a UUIDv4 shape check and return `MediaAnalysisRunId(value)`; keep the existing sanitized error mapping.

**Deletion protocol (slice 4):** for each candidate symbol, (1) prove zero references with whole-word search across `src/`, `tests/`, `extension/`, `index.html` including string literals, `window.` exposure, template references, and dynamic dispatch; (2) delete; (3) retire or migrate tests in the same commit; (4) re-run full suites. Symbols with any dynamic reference stay. `formatDuration`/`formatTimestamp`/`addSummaryValue` are deleted only if re-verification confirms they are called solely from the F7 cluster.

**Compatibility constraints:** no API changes, no schema change, no persistence change, no new dependencies, no `styles.css` change, no new asset file, no change to packaged resources (`pyproject.toml` untouched). Governance and UI language stay unchanged; the only new user-visible string is the genre-limit status message.

## 13. Implementation slices

**Slice 0 — AP pin rebaseline (prerequisite)**
- *Goal:* green baseline; public-consistent pin expectation.
- *Files:* `tests/contract/test_ap_integration.py` (line 10), `README.md` (AP gitlink around line 620).
- *Preserve:* `docs/AP_UPGRADE_OBSERVATIONS.md` and `test_worker_execution_contract.py` remain truthful historical records and stay untouched.
- *Validation:* focused `test_ap_integration.py` + `test_worker_execution_contract.py`; then full suite (expect 0 failed).
- *Rollback:* single commit.

**Slice 1 — verified contract fixes**
- *Goal:* client agrees with server for title length, control characters, genre count; analysis-run ID typed correctly.
- *Files:* `app.js`, `index.html`, `application/companion_review.py`, new regression test for the run-ID type.
- *Preserve:* existing validation messages for other fields; description behavior unchanged; no genre behavior change beyond rejecting >8; no visual change.
- *Validation:* new parity tests (slice 2 order may be interleaved: write tests first, record pre-fix failures, then fix).
- *Rollback:* independent commit.

**Slice 2 — contract-parity mechanism**
- *Goal:* executable cross-language contract for metadata fields; regression protection for F2–F4.
- *Files:* `tests/support/metadata_field_contract_cases.json`, `tests/contract/test_metadata_field_contract_parity.py`, `tests/metadata_form_contract.test.js`.
- *Preserve:* fixture acceptance must be authored from the server contract; the Python test must fail if the fixture disagrees with the domain.
- *Validation:* `node --test tests/metadata_form_contract.test.js`; `./.ap/ap exec … test-focus -- tests/contract/test_metadata_field_contract_parity.py`.
- *Rollback:* tests only; no production risk.

**Slice 3 — metadata-form test convergence**
- *Goal:* remove text-pinned metadata-form assertions now covered behaviorally.
- *Files:* `tests/contract/test_local_web_application.py` only.
- *Rule:* delete an assertion only when the JS suite or parity test contains an equivalent behavioral assertion; retain static security guards (`innerHTML`/`insertAdjacentHTML` absence, external-URL absence, secret absence, no persistent storage).
- *Preserve:* total count of behavioral assertions must not decrease.
- *Validation:* full Python + JS suites.
- *Rollback:* tests-only commit.

**Slice 4a — test-only/zero-caller live-cluster helpers**
- *Goal:* remove F8/F9/F6 artifacts and their test pins.
- *Files:* `app.js`; `tests/contract/test_local_web_application.py`; `tests/movie_identification_frontend.test.js`; `tests/catalog_card_ai_quick_action.test.js`.
- *Preserve:* live movie-identification strip rendering and `movieIdentificationIsPureUnknown`; `openDetailsDialog`; card preview/`mediaContentUrl` behavior.
- *Validation:* full suites; residual-reference grep returns 0.
- *Rollback:* per-artifact commits.

**Slice 4b — unreachable legacy development-library cluster**
- *Goal:* delete F7 and its startup call; retire tests that pin it.
- *Files:* `app.js`; `tests/contract/test_local_web_application.py`.
- *Preserve:* backend `/api/libraries`, scan-preview, and `media-imports` endpoints and their contract tests (used by CLI/operator surfaces); `LIBRARIES_ENDPOINT` deletion only after confirming no other consumer.
- *Validation:* full suites; grep for each deleted symbol returns 0; `#library-*` absence assertions still pass.
- *Rollback:* one commit; independently revertible from slices 0–3.

## 14. Validation matrix

Implementation Worker must run and report exact commands/results:

| Purpose | Command | Expected |
|---|---|---|
| Environment/tooling | `./.ap/ap doctor` | PASS |
| Baseline envelope | `./.ap/ap project check --root … --baseline <WORKER_BASELINE>` | PASS |
| Prerequisite contract | `./.ap/ap exec … --operation test-focus -- tests/contract/test_ap_integration.py tests/contract/test_worker_execution_contract.py -q -p no:cacheprovider` | 0 failed |
| New Python parity | `… --operation test-focus -- tests/contract/test_metadata_field_contract_parity.py -q -p no:cacheprovider` | all pass |
| New JS parity | `node --test tests/metadata_form_contract.test.js` | all pass |
| Frontend regression | `node --test tests/*.test.js` | 0 fail (skips = 5 gated browser evidence) |
| Full Python | `… --operation test-focus -- tests -q -p no:cacheprovider` | **0 failed**, 3356+ passed, 8 skipped |
| Pre-fix reproduction (evidence) | run slice-2 tests before slice-1 fix on a disposable branch/copy | the title-240-astral, C1, and 9-genre cases must fail; record exact output in the report |
| Removal proof | `rg -n "<symbol>" src tests extension` for each deleted symbol | only intended remaining references (or none) |
| Visual-safety proof | `git diff --stat` (or worktree equivalent) | no `styles.css`; no `index.html` structural removals beyond the `maxlength` attribute |

## 15. Acceptance matrix

A fresh Acceptance Worker passes only if all are true:

1. Full Python suite 0 failed and full JS suite 0 fail, on the exact accepted baseline.
2. `test_ap_integration.py` passes and README's AP gitlink matches the pinned gitlink; `docs/AP_UPGRADE_OBSERVATIONS.md` is unchanged or intentionally revalidated with its test updated (either is acceptable only if consistent).
3. The parity fixture contains, at minimum: 240 astral code points accepted; 241 astral rejected; a C1 control in `title` and in `tag_display_name` rejected; 8 genres accepted / 9 rejected; description LF accepted / tab or C1 rejected; blank and whitespace-rule cases.
4. The parity tests execute the real client validators and real server domain types (inspection of test bodies, not just green status).
5. The pre-fix reproduction evidence exists in the Implementation Worker report and shows the three defect families failing before the fix.
6. No deleted symbol is referenced anywhere; no new dependency, no new packaged asset, no schema/API change.
7. No `styles.css` diff; no UI copy change other than the genre-limit status message.
8. `git status` contains no unrelated changes; the accepted commit(s) match the authorized baseline.

Blocked if: any suite is red; parity tests assert constants rather than executing validators; dead-code deletions were performed on grep alone without the deletion protocol; or unrelated refactoring appears.

## 16. Risk review

| Dimension | Assessment | Mitigation |
|---|---|---|
| User-visible regression | Low. Three validation paths become *more* permissive/correct; the only new UI string is the genre-limit status. Removing title `maxlength` changes typing behavior (longer input allowed until Save is blocked with a message) | Keep the exact message copy bounded; no chrome/structure changes |
| Browser behavior | Low. `unicodeCodePointLength` already used for description; no new APIs | Node parity execution covers the validators |
| Persistence/data | None | No schema or API change |
| Concurrency | None | No async/ownership code touched |
| Security | Neutral-to-positive. C1-title rejection aligns client with server; no guard removed (security static tests retained) | Keep absence assertions; no CSP/header changes |
| Backward compatibility | Full. No API/schema change; dead frontend code had no consumers | Deletion protocol with full-suite gates |
| Deployment relevance | Positive: removes generic "Save failed." classes from the NUC-tested metadata/AI flow; keeps NUC refresh decision explicit via slice 0 | Publish or revert `8c7858b` deliberately before NUC refresh |
| Rollback | Slices are separate commits; slice 4 is independently revertible | Git authority to be granted explicitly per task |

## 17. Follow-up logical wholes

1. `framenest-composition-and-audit-wiring-convergence` — F11 + F12 (+ optional F13-style parser sweep) plus `create_app` verbosity only if separately justified. Small, no user impact.
2. `framenest-secure-media-traversal-hardening` — the accepted TOCTOU residual; dirfd/`openat` traversal, post-open identity re-validation, a real race test. Security whole.
3. `framenest-python-scaffolding-retirement` — Lead I symbols, migration-shim review, dead public API surface.
4. `framenest-browser-evidence-and-ci-foundation` — no CI, 8m44s suite, gated browser evidence; may be a deployment-readiness whole.
5. `framenest-ui-ux-polish` — explicitly last, immediately before hands-on NUC testing, per Cooperator sequencing.
6. `framenest-nuc-operational-validation` — routine release refresh + hands-on acceptance.
7. Optional later extension of the parity fixture mechanism to the YouTube claim URL validator and catalog query contract — only if drift is observed, never as a platform build-out.

## 18. Recommended Worker profile

- **Implementation Worker 1 (slices 0–3):** fresh session, **High** reasoning, native planning mode **not required** (this plan is the design), subagents not needed. Must use the canonical AP test route with an exact baseline, record pre-fix reproduction output, and make separate commits per slice (Git authority per task).
- **Implementation Worker 2 (slice 4):** fresh session, **High** reasoning (deletion protocol demands careful reference verification), no subagents required. Could be the same session if the Orchestrator prefers one Worker with ~1M context; separate is recommended for boundedness and clean rollback.
- **Acceptance Worker:** fresh session, **High** reasoning, read-only + test execution, independently verifies the acceptance matrix (must inspect test bodies, not just green status).

## 19. Challenge to the hypothesis

**Is `framenest-web-client-contract-and-testability-convergence` genuinely the best next logical whole? Yes — with one prerequisite and one explicit refinement.**

- The alternative candidates fail the scope-quality bar or the evidence bar: the AP pin issue is a two-file prerequisite, not a whole; the TOCTOU residual is an *accepted* security decision requiring a different threat-model decision, so it belongs to a security whole; the composition root has no measured correctness blocker (only two minor wiring defects, now recorded); `app.js` size alone has no defect behind it; a framework/module migration is an explicit anti-goal; UI/UX polish is explicitly late; NUC deployment work cannot begin from the current public state until the pin decision is published.
- The chosen whole has verified failure evidence (three client/server divergences plus a latent ID-type defect), bounded files, no user-visible redesign, testable acceptance, low migration risk, no new dependencies, and a measurable outcome: the metadata field contract becomes executable across languages, the metadata form validators gain their first behavioral tests, and the frontend's dead/test-only mass stops being preserved by the suite.
- The refinement is honesty about reachability (F2's supplied reproducer is blocked by `maxlength`; the reachable path is programmatic AI copy) and about test architecture (Lead C shows test drift in both directions; only the source-text assertion structure in F10 proves refactor-coupling). The plan is built on the corrected evidence, not the original claim.
- The one thing that would change the answer: if the Cooperator declares that NUC hands-on testing must start immediately, then the only true blocker is slice 0 plus publishing the pin; everything else in this whole reduces risk before polish and can wait, but it remains the highest-value engineering work available before UI/UX polish begins.

Terminal planning status: **COMPLETE — approval-gated; no implementation performed, no commits, no pushes.**