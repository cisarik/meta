All validations complete. Final report:

### Report for ORCHESTRATOR_CHAT

| Field | Value |
|---|---|
| Logical whole identity | `framenest-web-client-contract-and-testability-convergence` |
| Worker role / profile | `WORKER` / Implementation Worker |
| Worker session target | `fresh-worker-session` |
| Worker session ordinal | `02` |
| Worker exchange ordinal | `00` |
| Native planning mode | `not-required` |
| Standard terminal status | **implementation-PASS** |
| Phase-qualified result | Slices 0, 2 (RED+GREEN), 1, 3 implemented and green on exact committed state; Slice 4 deliberately not performed (reserved for a separate Worker) |
| Start commit | `8c7858b62beca3c4ee92bb8f1f095b98063e2c94` |
| End commit | `1f355a8433331beef3410bf807b247a5b8155919` |
| Result artifacts | Commits `0f4500ad7463d7428f377097aea224a268b321e2`, `6371bc00cb686c80e735330b308494ba552b94bc`, `1f355a8433331beef3410bf807b247a5b8155919` |
| Logical-whole closure | **Not closed** — Slice 4 (dead/test-only frontend artifact retirement) remains outstanding by explicit non-scope |
| Report justification | All authorized slices implemented, all suites green on the exact committed tree, worktree clean; unchanged residuals recorded below |
| Authority expiry | Implementation authority from this prompt expires at this terminal report |

---

## Baseline

Independently verified before any mutation:

- Repository root: `/home/agile/Projects/framenest` (canonical remote `https://github.com/cisarik/framenest.git`).
- Branch: `feat/x-meme-browser-companion`.
- Local HEAD: `8c7858b62beca3c4ee92bb8f1f095b98063e2c94` — matched the approved baseline exactly.
- Public `origin/main`: `a4193d4f520a30aafa333987f2e6b846a5425d27`; public `origin/feat/x-meme-browser-companion`: `a4193d4f520a30aafa333987f2e6b846a5425d27`.
- Local/public relationship: local `8c7858b` was ahead by exactly one unpublished commit whose entire diff is the `.ap` gitlink `7ef45da…` → `7478ddb…`; nothing else unpublished.
- `.ap` gitlink: `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`; `.ap` checkout HEAD identical; `.ap` worktree clean.
- `./.ap/ap doctor`: **PASS** (strict pinned AP commit OK, managed AGENTS.md block OK, stable variant).
- Initial worktree/index state: clean (`git status --porcelain` empty).
- Independently reproduced F1 before fixing: focused `tests/contract/test_ap_integration.py` → `1 failed, 1 passed`, `AssertionError: assert '7478ddb07d2c3911f79e1aa1441f0115a31c45d8' == '7ef45da756ed3cc14808e89bf25d0a9f9aba5d26'`.

No material baseline difference from the approved plan was found. No stop condition triggered.

---

## Slice 0

Active current-state AP references changed:

- `tests/contract/test_ap_integration.py:10` — `EXPECTED_AP_COMMIT` `7ef45da…` → `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- `README.md:620` — current AP gitlink block `7ef45da…` → `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.

Historical references intentionally preserved (verified truthful historical records, not active-current state):

- `docs/AP_UPGRADE_OBSERVATIONS.md` lines 11 and 14 (`Last revalidated against: 7ef45da…`, `Disposition evidence: 7ef45da…`).
- `tests/contract/test_worker_execution_contract.py` lines 83 and 86 (pins that ledger text).

Residual proof: `git grep -l 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` now returns exactly those two files and nothing else; both contain historical revalidation evidence, and the pin update to `7478ddb` was not a revalidation of that ledger entry, so rewriting it would have fabricated evidence.

Focused validation:

```text
./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline 8c7858b62beca3c4ee92bb8f1f095b98063e2c94 \
  --operation test-focus -- \
  tests/contract/test_ap_integration.py tests/contract/test_worker_execution_contract.py -q -p no:cacheprovider
→ 6 passed
```

Commit A: **`0f4500ad7463d7428f377097aea224a268b321e2`** — `Rebaseline FrameNest AP integration pin` (2 files, +2/−2).

---

## Authentic RED evidence

The parity mechanism was written and executed **before any production change**. At RED time the only repository mutation was commit A (README + AP test pin; verified by `git show --stat 0f4500a` → only those two files), and the three new test files existed untracked. No file under `src/` had been modified.

Commands and exact pre-fix results:

```text
node --test tests/metadata_form_contract.test.js
→ 31 passed, 4 failed

./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline 0f4500ad7463d7428f377097aea224a268b321e2 \
  --operation test-focus -- tests/contract/test_metadata_field_contract_parity.py -q -p no:cacheprovider
→ 35 passed
```

Failing client cases and why each proves real client/server divergence:

| Case | Fixture expected | Pre-fix client | Divergence proof |
|---|---|---|---|
| `title-240-astral-code-points` (`"😀"×240`) | accepted | **rejected** | Client `rawTitle.length` counts 480 UTF-16 units against `MAX_METADATA_TITLE_CODE_POINTS = 240`; server `MediaDisplayTitle` counts 240 code points and accepts. Reachable via programmatic assignment (AI suggestion copy), which bypasses `maxlength`. |
| `title-c1-control` (`"Bad\u009fTitle"`) | rejected | **accepted** | Client `hasControlCharacter` only rejected `<= 0x1f` and `0x7f`; Python `unicodedata.category(ch) == "Cc"` includes `U+0080–U+009F` and rejects. Would surface as generic server `"Save failed."` |
| `tag-c1-control` (`"Bad\u009fTag"`) | rejected | **accepted** | Same predicate used by `tagDisplayNameError`; the sibling description helper already covered `0x7f–0x9f`, proving internal inconsistency. |
| `genres-nine` (9 genre displays) | rejected | **accepted** | Client had no cap; server caps at `MAX_MEDIA_GENRES = 8` in the request validator and `MediaMetadata` domain. Save would fail generically server-side. |

The Python parity suite was green pre-fix, proving the fixture encodes actual backend behavior rather than desired behavior. No production code was mutated to manufacture the failures; no intentionally-red commit was created.

---

## Production corrections

**F2 — title length semantics**
- Files: `src/framenest/adapters/api/web/app.js` (`normalizedMetadataFormState`), `src/framenest/adapters/api/web/index.html`.
- Prior: `rawTitle.length > MAX_METADATA_TITLE_CODE_POINTS` (UTF-16), and `#metadata-title-input` carried `maxlength="240"` (also UTF-16).
- New: `unicodeCodePointLength(rawTitle) > MAX_METADATA_TITLE_CODE_POINTS`; `maxlength="240"` removed from the title input so the explicit validator owns the contract (mirroring the accepted description precedent). No layout/CSS change.
- Rationale: converge on the server's Unicode code-point semantics without weakening it.
- Regression protection: parity cases `title-240-astral-code-points`, `title-241-astral-code-points`, `title-240/241-ascii-code-points` plus a static `test_browser_title_input_has_no_maxlength` guard.

**F3 — Cc control-character semantics**
- File: `app.js:hasControlCharacter`.
- Prior: `(codePoint >= 0 && codePoint <= 31) || codePoint === 127`.
- New: `codePoint <= 0x1f || (codePoint >= 0x7f && codePoint <= 0x9f)`, exactly matching Python `Cc` for BMP. Description helper left untouched.
- Rationale: match existing backend behavior; do not invent new policy.
- Regression protection: title/tag C0, DEL, C1 parity cases.

**F4 — genre-count parity**
- File: `app.js`.
- Prior: no limit; 14 selectable options; 9 selections enabled Save and failed server-side generically.
- New: `const MAX_METADATA_GENRES = 8;` and, in `normalizedMetadataFormState` after title checks and before the blank-title branch, `return { error: \`Select at most ${MAX_METADATA_GENRES} genres.\` }` when `genres.length > 8`. The existing `updateMetadataControls` path disables Save and surfaces the message in both status/validation surfaces before any request; no new UI chrome or styling.
- Regression protection: parity `genres-empty`, `genres-eight`, `genres-nine`.

**F13 — analysis-run domain-ID type correctness**
- File: `src/framenest/application/companion_review.py`.
- Prior: `return MediaId.from_string(value)` while annotated `MediaAnalysisRunId`.
- New: `MediaAnalysisRunId` imported at runtime; `_parse_analysis_run_id` validates the existing UUIDv4 canonical shape via `MediaId.from_string`, then returns `MediaAnalysisRunId(parsed.to_string())`. Sanitized `CompanionReviewAnalysisRunNotFoundError` mapping preserved for invalid values.
- Rationale: least invasive fix preserving the current UUIDv4 contract; no identity redesign.
- Regression protection in `tests/contract/test_companion_review_api.py`: `test_analysis_run_id_parsing_returns_analysis_run_identity` asserts `isinstance(parsed, MediaAnalysisRunId)` and `not isinstance(parsed, MediaId)` (would fail on the old code), and `test_analysis_run_id_parsing_keeps_sanitized_failure_contract` covers three invalid forms.

Commit B: **`6371bc00cb686c80e735330b308494ba552b94bc`** — `Align metadata client-server validation contracts` (7 files, +578/−5).

---

## Parity mechanism

- **Shared fixture** `tests/support/metadata_field_contract_cases.json`: 35 cases, each `{id, field, value, expected}` with `field ∈ {title, description, tag_display_name, genre_set}` and `expected ∈ {accepted, rejected}`. Boundary values use a compact `{"repeat": ["unit", count]}` form so 240/241 astral, 240/241 ASCII, 10000/10001 description, and 80/81 tag boundaries are readable. Field semantics (blank-clears behavior, whitespace rules, Cc rejection, 8-genre cap) are documented in the fixture itself. It is acceptance data only: no production code, packaging, or runtime request loads it; there is no schema generation, fetch, bundler, framework, or new dependency.
- **Server executor** `tests/contract/test_metadata_field_contract_parity.py`: executes the real `MediaMetadataSaveRequest` and `CanonicalTagRequest` pydantic request models used by the API plus the real application `_parse_genres` mapping (for genre display-name membership). Fixture expectations must match actual server behavior or the test fails.
- **Client executor** `tests/metadata_form_contract.test.js`: extracts the real production `normalizedMetadataFormState`, `normalizedDescriptionState`, `tagDisplayNameError`, `normalizedTagDisplayName`, `uniqueTagKeyForDisplayName`, `tagSlugFromDisplayName`, `hasControlCharacter`, and `unicodeCodePointLength`, plus the real `MAX_METADATA_TITLE_CODE_POINTS`, `MAX_METADATA_DESCRIPTION_CODE_POINTS`, `MAX_METADATA_GENRES`, and `TAG_KEY_PATTERN` declarations from `app.js`, runs them in a bounded `node:vm` context with stub field inputs, and compares executable acceptance with the fixture. No validator is reimplemented in the test; no constants are duplicated; string/constant-presence assertions are not used.
- Case families: title (11), description (12), tag display name (9), genre set (3).

**GREEN parity after corrections:** Node `35 pass / 0 fail`; Python `35 passed`. The four RED cases became green because production behavior changed; the fixture was not edited after the RED run.

---

## Test convergence

Exactly these source-text assertions were retired from `tests/contract/test_local_web_application.py`:

| Removed | Superseding behavioral evidence |
|---|---|
| `test_browser_defines_unicode_code_point_length_helper` (`[...value].length` spelling) | Parity astral/ASCII boundary cases for title, description and tag execute the helper through real validators (240 code points accepted, 241 rejected). |
| `test_browser_description_uses_code_point_length_instead_of_utf16` (source spelling) | Parity `description-10000-code-points` accepted / `description-10001-code-points` rejected. |
| `test_browser_description_rejects_c1_controls_and_allows_line_feed` (source scan for `0x1f`/`0x7f`/`0x9f`/`0x0a`) | Parity `description-c1-control` rejected, `description-single-line-feed` accepted, `description-tab`/`description-carriage-return` rejected, leading/trailing line-feed rejected. |
| Two lines inside `test_javascript_metadata_workspace_tracks_sparse_baseline_dirty_and_discard` (`rawTitle.trim() !== rawTitle`, `hasControlCharacter(rawTitle)`) | Parity `title-outer-whitespace`, `title-c0-control`, `title-del-control`, `title-c1-control`. The rest of that dirty/discard test was retained. |

Added (static absence guard where source-level absence is the contract): `test_browser_title_input_has_no_maxlength`, matching the existing description-textarea precedent.

Deliberately retained: description counter source check (the `updateDescriptionStatus` counter has no executable test), `MAX_METADATA_TAGS` assertions (tag-count parity not in this fixture), dirty-state/collection assertions, and all static security/absence guards (`innerHTML`/`insertAdjacentHTML` absence, external-URL absence, secret absence, dialog structure). `test_local_web_application.py` went from 209 to 207 test functions; nothing else was rewritten.

Commit C: **`1f355a8433331beef3410bf807b247a5b8155919`** — `Replace metadata source assertions with behavior tests` (1 file, +5/−22).

---

## Validation

All commands ran through the canonical AP route with the verified session baseline `8c7858b62beca3c4ee92bb8f1f095b98063e2c94` (commit A/B validation used the then-current commit A as `--baseline`; terminal runs use the session baseline).

| Check | Exact command | Result |
|---|---|---|
| `ap doctor` | `./.ap/ap doctor` | **PASS** |
| `ap project check` | `./.ap/ap project check --root /home/agile/Projects/framenest --baseline 8c7858b62beca3c4ee92bb8f1f095b98063e2c94` | **PASS** |
| Focused prerequisite Python | `… --operation test-focus -- tests/contract/test_ap_integration.py tests/contract/test_worker_execution_contract.py -q -p no:cacheprovider` | **6 passed, 0 failed** |
| Parity Python | `… --operation test-focus -- tests/contract/test_metadata_field_contract_parity.py -q -p no:cacheprovider` | **35 passed, 0 failed** |
| Parity JS | `node --test tests/metadata_form_contract.test.js` | **35 pass, 0 fail** (pre-fix: 31 pass / 4 fail) |
| Companion regression | `… --operation test-focus -- tests/contract/test_companion_review_api.py tests/contract/test_metadata_field_contract_parity.py -q -p no:cacheprovider` | **46 passed, 0 failed** (11 companion incl. 2 new) |
| Metadata web contract file | `… --operation test-focus -- tests/contract/test_local_web_application.py -q -p no:cacheprovider` | **215 passed, 0 failed** |
| Full JS | `node --test tests/*.test.js` | **461 pass, 0 fail, 5 skipped (gated browser evidence), 466 tests** |
| Full Python (terminal HEAD) | `… --operation test-focus -- tests -q -p no:cacheprovider` | **3392 passed, 8 skipped, 0 failed** in 526.28 s (baseline: 3356 passed, 1 failed, 8 skipped; new tests account for +35 net after −2 retired functions and +37 added) |

No suite is reported as PASS if it failed; the only skipped tests are the pre-existing gated real-tool/browser evidence classes.

Residual searches proving old incorrect forms no longer control behavior:

- `rawTitle.length` — 0 occurrences in `app.js`.
- `codePoint === 127` / `codePoint >= 0 && codePoint <= 31` — 0 occurrences.
- `maxlength` on the `#metadata-title-input` tag — absent (other unrelated inputs untouched).
- `MAX_METADATA_GENRES` — defined (line 67) and used in the validator (lines 2488–2489) with message `Select at most 8 genres.`
- `_parse_analysis_run_id` returns `MediaAnalysisRunId(...)`; `return MediaId.from_string(value)` remains only in `_parse_media_id` (correct).
- Old AP SHA `7ef45da…` remains only in the two intentional historical files.

---

## Git result

```text
0f4500ad7463d7428f377097aea224a268b321e2 Rebaseline FrameNest AP integration pin
6371bc00cb686c80e735330b308494ba552b94bc Align metadata client-server validation contracts
1f355a8433331beef3410bf807b247a5b8155919 Replace metadata source assertions with behavior tests
```

- Final HEAD: `1f355a8433331beef3410bf807b247a5b8155919`
- `git status --short`: **empty** (0 entries); `git diff HEAD` empty.
- `git diff 8c7858b62beca3c4ee92bb8f1f095b98063e2c94..HEAD --stat`: 10 files changed, 585 insertions(+), 29 deletions(-) — `README.md`, `src/framenest/adapters/api/web/app.js`, `src/framenest/adapters/api/web/index.html`, `src/framenest/application/companion_review.py`, `tests/contract/test_ap_integration.py`, `tests/contract/test_companion_review_api.py`, `tests/contract/test_local_web_application.py`, `tests/contract/test_metadata_field_contract_parity.py`, `tests/metadata_form_contract.test.js`, `tests/support/metadata_field_contract_cases.json`. No `styles.css`, no `pyproject.toml`, no migration, no API-schema file touched.
- Local branch is `ahead 4` of `origin/feat/x-meme-browser-companion` (the pre-existing unpublished `8c7858b` plus these three commits).

Explicit statements:

```text
no push performed
no publication performed
no deployment performed
Meta was not mutated
Slice 4 was not performed
```

---

## Residuals / observations

- `test_browser_description_counter_uses_code_point_length` remains a source-text test: the `updateDescriptionStatus` counter has no executable test, so retiring it would lose an uncovered guarantee. Candidate for a future behavioral test.
- `MAX_METADATA_TAGS` and tag-count source assertions remain for the same reason; the fixture intentionally covers only the six field families required by the prompt (adding tag-count cases would have broadened the fixture).
- The fixture documents blank-clears semantics: empty/whitespace-only title and description clear the field (client sends null; server accepts absence). The server executor reproduces the request model's own blank handling; this is documented in the fixture, not hidden.
- No unrelated defect was found that required intervention. F11/F12 and the accepted TOCTOU residual remain out of scope and untouched as directed; Slice 4 dead/test-only clusters (`F6`, `F7`, `F8`, `F9`) are still present and now more safely changeable because the parity suites protect live metadata behavior.
- All implementation authority from this prompt expires at this report.

**implementation-PASS** — the authorized slices (0, 2 RED+GREEN, 1, 3) are implemented, authentically reproduced RED before correction, verified green across both complete suites on the exact committed tree, committed locally in three bounded commits, with no push, publication, deployment, Meta mutation, or Slice 4 work.