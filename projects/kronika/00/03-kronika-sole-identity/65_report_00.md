### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-sole-identity
Worker session ordinal: 65
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C9B3R — living truth commit under the amended classification
status: PASS
Phase-qualified result: not-applicable
Start commit: 9b291e936e93026ebe540b4a23a11b89721747a8
End commit: ca280c45755e28b6363690c50d7cdaa42187de96
Report justification: new-mutation
Logical-whole closure: not-closed

Gates re-derived before the commit. Local `main` was the expected four-path worktree at `9b291e936e93026ebe540b4a23a11b89721747a8`. `git ls-remote origin refs/heads/main` was `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`. The containing `.ap` gitlink and submodule `HEAD` were both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`. `./.ap/ap doctor` PASS, governing variant stable. `./.ap/ap project check --root /home/agile/Projects/kronika --baseline 9b291e936e93026ebe540b4a23a11b89721747a8` PASS. The lead over public `main` is the unpublished C9-B sequence; this commit adds a third unpublished commit. Primary recovery class for that lead: `unpublished-candidate`. No host contact and no browser. `FROZEN_DOCUMENT_SHA256` has 86 keys. `FROZEN_ALEMBIC_SHA256` has 36 keys, counted from the dict.

## 1. Kept-diff validation against the session-64 report

The pre-commit diff was exactly the four paths in the session-64 report, byte-for-byte.

`DEVELOPMENT.md` now says launcher defaults are already `~/Library/Application Support/Kronika` on macOS and `$XDG_DATA_HOME/Kronika` elsewhere, and that `kronika-dev migrate-identity-paths` remains the workstation copy tool with the refusal safeguard in front of an empty catalog.

`ROADMAP.md` now says ADR-0085 is implemented as an ordered sequence of bounded cuts, and the retained `FrameNest*` class residue is excluded for this whole.

`README.md` now says private Kronika records and administrator approval are accepted and on public `main`. Gallery, desktop, Cover Studio, and publication sentences were not edited.

`tests/contract/test_kronika_identity_retention.py` pins `CAPITALIZED_OCCURRENCE_COUNT = 2328` with the session-64 arithmetic comment. `CAPITALIZED_FILE_COUNT` stays 343.

`git diff --stat` before the commit:

```text
 DEVELOPMENT.md                                    | 8 ++++----
 README.md                                         | 4 ++--
 ROADMAP.md                                        | 3 ++-
 tests/contract/test_kronika_identity_retention.py | 7 ++++++-
 4 files changed, 14 insertions(+), 8 deletions(-)
```

No other path was modified. Nothing in those four paths was edited in this session.

## 2. Classification

Scan command, ledger file excluded, same tracked set the retention counter uses:

```text
git grep -I -n -i framenest -- . ':(exclude)tests/contract/test_kronika_identity_retention.py'
```

That command returns 3239 lines and 3375 occurrences. Every occurrence was classified from the line text in this session. The session-64 tables were a starting inventory, not a pin. `.ap` was scanned separately with `git -C .ap grep -n -I -i framenest` and is out of scope (16 lines, listed below).

| Category | Occurrences |
|---|---:|
| 1 Frozen document or frozen revision | 673 |
| 2 Durable-reader historical spelling | 20 |
| 3 Existing historical backup/sidecar/snapshot/offdevice/analysis identities | 18 |
| 4 Frozen tooling | 11 |
| 5 Frozen mount | 12 |
| 6 Frozen state-directory name | 12 |
| 7 Retained live host identity | 4 |
| 8 Alembic shim | 12 |
| 9 Accepted Python class/module names, source comments and docstrings | 1848 |
| 10 Negative test assertions and retained-spelling fixtures | 569 |
| 11 Non-operational code-local identifier | 56 |
| 12 Historical ADR bodies/citations and historical artifacts | 72 |
| 13 Retired-prefix strip safeguard | 2 |
| 14 Log sanitizer needle | 1 |
| 15 Stored key retained for read/migration | 8 |
| 16 Active-production defect with a scheduled correction | 42 |
| 17 Parked budget path | 1 |
| 18 Retained ignore/guard entry | 2 |
| 19 Explicit historical prose | 12 |
| Scan total | 3375 |

Category 20, the ledger file `tests/contract/test_kronika_identity_retention.py`, is excluded by the scan. It contains 281 occurrences. Those are not inside the 3375. Zero occurrences in the scan sit outside categories 1–19.

Categories 1, 9, and 10 are not pasted line by line. That omission is disclosed. Category 1 is every hit whose path is one of the 86 frozen documents or one of the 36 Alembic revision names; the occurrence total is 673. Category 9 is the 1811 uses of the 61 `class FrameNest…` identifiers outside Part A, plus 36 source comments and docstrings, plus the one ROADMAP class-residue label. Category 10 is every remaining test and test-support hit after the more specific rules above. Their totals are in the table and are part of the 3375 sum. Every other category is listed below.

The ROADMAP label is `ROADMAP.md:80`, the new `` `FrameNest*` `` sentence. Its literal use is the living statement of plan §4, which excludes that class residue. It is counted in category 9 on that clause. It is not itself a class, comment, or docstring.

Owned rows other than Part A, class residue, comments/docstrings, and test fixtures:

```text
20	marker filenames .framenest-release-sha, .framenest-release-manifest.json, and key framenest_release_sha	2
18	COMPATIBLE_* backup, sidecar, snapshot, off-device, and analysis identity values, plus the README sidecar sentence and the backup-runbook off-device marker name	3
11	/opt/framenest/tooling/	4
12	/mnt/framenest-catalog-offdevice	5
12	framenest-chatgpt-page	6
4	framenest-nuc	7
12	the four aliased module names in alembic_compat.py and the ADR-0085 citation of the helper module	8
56	app.js helper and DOM-property identifiers	11
72	ADR-0085 remaining prose, docs/adr/README.md, docs/provenance/kronika-capture.json, and WORKSPACE_UDS_PATH	12
2	src/kronika/identity_env.py FRAMENEST_	13
1	deploy/ubuntu/kronika_release.py:2594 /etc/framenest/credentials inside _assert_logs_sanitized	14
8	three localStorage retired keys, two retired catalog labels, three legacy directory names	15
42	listed in section 4	16
1	src/kronika/infrastructure/ai/chatgpt_page/budget.py DEPLOYMENT_STATE_DIR	17
2	.gitignore comment and /.framenest/	18
12	dated release paths, the completed acceptance title, removed-wrapper sentences, and the completed S10 row	19
```

Category 3 values, one each unless noted: `.framenest.json` in `media_sidecar_store.py` and `README.md`; `framenest-media-suggestion-v4`; `framenest-media-suggestion-result-v1`; both movie-identification compatible versions; `framenest-media-sidecar`; `.framenest-backup-` and application name `framenest`; `.framenest-catalog-offdevice.json`, `.framenest-offdevice-stage-`, purpose `framenest-catalog-offdevice`, and the same marker name in `docs/BACKUP_AND_RECOVERY.md`; `.framenest-pull-stage-`, `.framenest-workstation-snapshot-store.json`, `framenest-catalog-backup-export`, `framenest-workstation-catalog-snapshot`, `framenest-workstation-snapshot-store`. Each production constant is the `COMPATIBLE_*` member. The paired canonical constant is what the writer uses: `PROMPT_VERSION`, `RESULT_SCHEMA_VERSION`, `SIDECAR_FORMAT`, `TEMP_PREFIX`, `APPLICATION_NAME`, `STAGE_PREFIX`, `MARKER_NAME`, `SNAPSHOT_PURPOSE`, `TRANSFER_PROTOCOL_NAME`, and the movie-identification canonical versions. Off-device marker reading walks `ACCEPTED_MARKER_NAMES` with the canonical name first.

`.ap/` out of scope, 16 lines:

```text
.ap/CHANGELOG.md:72, 92, 111, 122 FrameNest
.ap/README.md:98 ap bundle framenest
.ap/docs/adr/0016-universal-continuation-and-upgrade-ledger-storage.md:153, 169 FrameNest
.ap/docs/adr/0017-cooperator-ergonomics-cost-proportional-execution.md:61, 62, 100 FrameNest
.ap/docs/adr/0021-followable-spine-and-restatement-conversion.md:75, 77, 114, 150 FrameNest
.ap/docs/adr/0022-default-agent-dispatch-trace-integrity-and-pin-presentation.md:34 FrameNest
.ap/docs/adr/README.md:83 FrameNest
```

## 3. Strict verification for categories 11 and 15

Category 11 is only `src/kronika/adapters/api/web/app.js`. A search of that file for those names inside quotes returned no hits. Each hit is an identifier: a function declaration, a call, or a property access.

| Identifier | Occurrences | Parse |
|---|---:|---|
| `framenestMutationHeaders` | 33 | function at line 436; every other hit is a call |
| `framenestJSONHeaders` | 8 | function at line 11593; calls only |
| `framenestResponseRevision` | 3 | function at line 12141; calls only |
| `framenestRevisionHeader` | 4 | function at line 12154; calls only, including spread calls |
| `__framenestCleanup` | 3 | property reads and one assignment on a DOM element, lines 4241–4243 |
| `__framenestGifImage` | 5 | property reads and one assignment, lines 4255–4259 |

None of these identifiers is passed to `fetch`, `localStorage`, `sessionStorage`, or `JSON.stringify`. The header string those helpers may place in an object is a different hit and is category 16. The three storage-key strings in the same file are category 15.

Category 15, eight hits, each with the canonical writer:

| Hit | Read | Canonical writer |
|---|---|---|
| `app.js:20` `framenest.youtube.currentClaim.v1` | `readMigratedStorageItem` at line 1161 | `setItem(KRONIKA_YOUTUBE_CLAIM_RECOVERY_STORAGE_KEY, …)` at line 1142, value `kronika.youtube.currentClaim.v1` |
| `app.js:22` `framenest.catalog.pageSize` | read at line 632 | `setItem(KRONIKA_CATALOG_PAGE_SIZE_STORAGE_KEY, …)` at line 10084 |
| `app.js:23` `framenest.upload.recovery.v1` | read at lines 3079–3082 | `setItem(KRONIKA_UPLOAD_RECOVERY_STORAGE_KEY, …)` at line 3071 |
| `identity_labels.py:36` `FrameNest NUC` | selected with `display_name == RETIRED_DEVICE_LABEL` | `new_label=CANONICAL_DEVICE_LABEL` (`Kronika NUC`) at line 395; the receipt parser rejects any other new label at line 777 |
| `identity_labels.py:38` `FrameNest` | `instr(display_name, RETIRED_BRAND)` | `label.replace(RETIRED_BRAND, CANONICAL_BRAND)` at line 617, canonical brand `Kronika` |
| `local_state_migration.py:62` `FrameNest` | source side of the migration pair and of the macOS/XDG source paths | destinations use `CANONICAL_APP_DIRECTORY_NAME` (`Kronika`) |
| `local_state_migration.py:63` `framenest` | XDG AI source via `LEGACY_LOWER_DIRECTORY_NAME` | destination uses `CANONICAL_LOWER_DIRECTORY_NAME` (`kronika`) at line 443 |
| `local_state_migration.py:64` `framenest-development` | temp source via `LEGACY_TEMP_DIRECTORY_NAME` | destination uses `CANONICAL_TEMP_DIRECTORY_NAME` (`kronika-development`) at line 504 |

## 4. Category 16

The known defect stands. `framenestMutationHeaders` in `src/kronika/adapters/api/web/app.js:437` still builds `X-FrameNest-Request: 1`. Line 443 then also sets `X-Kronika-Request: 1`. `MUTATION_HEADERS` in `src/kronika/adapters/api/tailscale_ingress.py` is only `x-kronika-request`. The retired header is still sent. The correction remains a separate grant.

Header mirrors classified here, because they assert that emission:

```text
1	src/kronika/adapters/api/web/app.js	X-FrameNest-Request
2	tests/admin_batch_actions_frontend.test.js	X-FrameNest-Request
1	tests/ai_providers_admin_frontend.test.js	X-FrameNest-Request
6	tests/catalog_card_ai_quick_action.test.js	X-FrameNest-Request
9	tests/tailscale_identity_frontend.test.js	X-FrameNest-Request
2	tests/contract/test_local_web_application.py	X-FrameNest-Request
2	tests/kronika_ui.test.js	X-FrameNest-Request
1	tests/youtube_acquisition_cockpit.test.js	X-FrameNest-Request
```

`tests/companion_review_extension.test.js` and `tests/companion_settings_automatic_analysis.test.js` assert the retired header is absent. `tests/contract/test_kronika_mutation_header.py` asserts the server returns 403 for `X-FrameNest-Request` alone. Those are category 10 negative assertions.

Further members, found because the category-11 proof fails or because the value is the live default:

```text
1	src/kronika/application/media_analysis_coordinator.py:114	name="framenest-media-analysis-coordinator"
1	src/kronika/application/media_analysis_coordinator.py:403	thread_name_prefix="framenest-media-analysis"
1	src/kronika/application/upload_catalog_coordinator.py:136	name="framenest-upload-catalog-coordinator"
1	src/kronika/application/upload_catalog_coordinator.py:383	thread_name_prefix="framenest-upload-catalog"
1	src/kronika/application/upload_publication_coordinator.py:119	name="framenest-upload-publication-coordinator"
1	src/kronika/application/upload_publication_coordinator.py:372	thread_name_prefix="framenest-upload-publication"
1	src/kronika/application/upload_validation_coordinator.py:145	name="framenest-upload-validation-coordinator"
1	src/kronika/application/upload_validation_coordinator.py:464	thread_name_prefix="framenest-upload-validation"
1	src/kronika/application/x_acquisition.py:722	thread_name_prefix="framenest-x-acquisition"
1	src/kronika/application/youtube_acquisition.py:882	name="framenest-youtube-acquisition-coordinator"
1	src/kronika/infrastructure/media_analysis/process.py:24	stored as the stdout reader thread name, passed at line 449
1	src/kronika/infrastructure/media_analysis/process.py:25	stored as the stderr reader thread name, passed at line 460
1	src/kronika/infrastructure/persistence/catalog_backup_workstation.py:427	name="framenest-ssh-stderr-drain"
1	src/kronika/infrastructure/media_analysis/contact_sheet.py:280	tempfile.mkdtemp(prefix="framenest-contact-")
2	src/kronika/configuration.py:82	/run/framenest/framenest-public.sock
1	src/kronika/infrastructure/ai/configuration.py:173	Application Support/FrameNest/ai/config.json
1	src/kronika/infrastructure/ai/configuration.py:179	config_home/framenest/ai/config.json
```

Evidence for the extra members: each thread string is the `name` or `thread_name_prefix` argument, so the runtime stores it. The contact-sheet prefix is written as a directory name. `DEFAULT_PUBLIC_PUBLISHED_UDS_PATH` is assigned to `uds_path` when public-published ingress has no explicit path (`configuration.py:578–582`). It does not occur in ADR-0048 or ADR-0074, so category 12 does not own it. The workspace constant `/run/framenest/framenest.sock` does match those ADR bodies and stays in category 12; tailscale ingress still requires an explicit path. `default_ai_config_path` returns the `FrameNest` / `framenest` path when no `KRONIKA_AI_CONFIG_PATH` override is set, and `registry.py`, `adapters/cli/ai.py`, `ai_admin_api.py`, and `application.py` use that return value as the config path. The migration module's canonical destinations are `Kronika` and `kronika`, but this function does not write them.

Tests that pin the public socket and the AI default path remain category 10 fixtures. A correction of those production constants has to update those fixtures in the same grant. This grant did not edit them.

## 5. Suites

Focused run through `ap exec --operation test-focus` against baseline `9b291e936e93026ebe540b4a23a11b89721747a8`, on the four-path worktree before the commit: 47 passed in 1.53s. That run was the retention module, `tests/contract/test_nuc_release_docs.py`, `tests/contract/test_adr_0073.py::test_current_schema_head_is_0035`, `tests/contract/test_team_alias_api.py::test_schema_head_sentences_are_0035`, and `test_sidecar_store_observes_both_filename_spellings`. No baseline difference inside that set.

Full Python suite through `ap exec --operation test` against the same baseline, on the committed tree: 4713 passed, 8 skipped, 3 warnings, 0 failed, in 719.56s. Difference from `4713/8/3/0`: none. The eight skips are the five real-tool cover cases, the two real-tool media-analysis cases, and the NVIDIA smoke case. The three warnings are the existing Pydantic non-serializable-default warnings. Retention is inside that suite: 15 passed. An independent `git grep -o FrameNest` outside the ledger counted 2328.

JavaScript, ordinary `node --test` from the worktree root. The files are not in the commit, so the counts are the worktree that was committed.

| Suite | Result | duration_ms |
|---|---|---:|
| `tests/companion_web_bridge.test.js` | 23 passed, 0 failed | 75.827 |
| `tests/companion_review_extension.test.js` | 41 passed, 0 failed | 186.095 |
| `tests/x_companion_extension.test.js` | 55 passed, 0 failed | 124.579 |
| `tests/companion_settings_automatic_analysis.test.js` | 6 passed, 0 failed | 10068.156 |
| `tests/kronika_ui.test.js` | 12 passed, 0 failed | 94.222 |
| `tests/catalog_card_ai_quick_action.test.js` | 30 passed, 0 failed | 208.322 |
| `tests/*_frontend.test.js tests/*_cockpit.test.js tests/gallery_*.test.js` | 212 passed, 0 failed | 726.313 |

No baseline difference. The four middle summaries were recaptured in a second run because the first combined transcript was truncated; both runs exited 0, and the table is the recaptured count.

## 6. Diff, commit, Part A, Part B, Part C

Commit `ca280c45755e28b6363690c50d7cdaa42187de96` on `main`, subject `Finalize living truth and classify the remaining retired spellings.` One `git add` of the four paths and one non-amended commit. No push. The working tree is clean.

`git diff --stat HEAD~1` matches the pre-commit stat in section 1.

Part A is byte-unmoved. None of the frozen paths are in the diff, and the retention module's frozen-hash tests passed inside the 4713. Part B is still empty: the basename test passed. Part C movement is the capitalized occurrence scalar only, 2327 to 2328. The cause is the one new `FrameNest` in `ROADMAP.md:80`. `ROADMAP.md:43` already held the other capitalized spelling, so the file count stays 343. Independent count outside the ledger: 2328.

## 7. Sites no test exercises

No test asserts the new DEVELOPMENT launcher-default paragraph, the README public-main clause, or the ROADMAP exclusion wording. The retention counter notices the extra capitalized spelling and does not check the sentence. The sidecar reader test exercises the suffix, not the README sentence.

The category-16 thread names, the contact-sheet prefix, the public-socket default, and the AI config default are exercised only insofar as existing tests pin the current spelling. No test in this grant asserts that those spellings are defects.

## 8. Deviations, risks, missing evidence, smallest next step

Deviation: none. The commit contains only the four session-64 paths. Category 16 was listed and not edited.

Risk: category 16 is larger than the one header the grant named in advance. A correction that changes only `X-FrameNest-Request` leaves the public-socket default, the AI config default, the thread names, and the contact-sheet prefix in place. Tests that pin those values are category 10 and will fail if a later grant changes the production constants without updating the fixtures.

Missing evidence: none of the required suites. Rendered UI was outside this grant.

Smallest next step: one bounded correction for the category-16 header emission and the further members in section 4, including the category-10 fixtures that pin them.

Resolved Execution Issues / Near-Misses

The first attempt to time the suites called `/usr/bin/time`, which is not installed. Those processes did not start. The evidence above is the rerun, using the shell `time` keyword and `node`'s `duration_ms`. No forbidden Python interpreter was invoked. Python evidence used `./.ap/ap exec` and `./.ap/ap project check`.

Pre-Existing Failure Classification

none

Orchestration critique:
MEASURED: `default_ai_config_path` still returns `FrameNest` / `framenest` when no canonical override is set, and `DEFAULT_PUBLIC_PUBLISHED_UDS_PATH` is still `/run/framenest/framenest-public.sock`; evidence is `configuration.py:173–179` and `configuration.py:82` with the assignment at `578–582`; effect is two live defaults in category 16 beyond the known header; smallest correction is to include both in the already scheduled category-16 grant, together with the fixtures that pin them.
LEAD: none