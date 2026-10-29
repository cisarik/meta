### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-sole-identity
Worker session ordinal: 66
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-CORR-C9B16A — retire the category-16 active spellings, part A
status: PASS
Phase-qualified result: not-applicable
Start commit: ca280c45755e28b6363690c50d7cdaa42187de96
End commit: 063b045c0e431760cfc48996bec1160c4d4b7e0b
Report justification: new-mutation
Logical-whole closure: not-closed

Gates re-derived before any edit. Local `main` was clean at `ca280c45755e28b6363690c50d7cdaa42187de96`. `git ls-remote origin refs/heads/main` was `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`. The containing `.ap` gitlink and submodule `HEAD` were both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`. `./.ap/ap doctor` PASS, governing variant stable. `./.ap/ap project check --root /home/agile/Projects/kronika --baseline ca280c45755e28b6363690c50d7cdaa42187de96` PASS. The lead over public `main` remains the unpublished C9-B sequence; this commit adds one more unpublished commit. Primary recovery class for that lead: `unpublished-candidate`. No host contact and no browser. `FROZEN_ALEMBIC_SHA256` has 36 keys, counted from the dict (`0001` through `0035` plus `__init__.py`).

Changed files, one purpose: the shell sends only the canonical mutation header; the fourteen runtime producer strings and the public socket default use the canonical spelling; the mirrors and the three non-obvious pins found by parse move with them; the retention scalars are the measured re-pin.

The parse, before editing, found three test modules outside the seven named mirrors that pin a changed string: `tests/unit/test_configuration_ingress.py` (the default path), `tests/unit/application/test_upload_validation_coordinator.py` (the executor prefix), and `tests/unit/infrastructure/media_analysis/test_movie_contact_sheet_selection.py` (the temporary-directory glob). `tests/unit/infrastructure/media_analysis/test_process.py` imports the reader-name constants and was not edited.

## 1. Header matrix

`framenestMutationHeaders` still has that name. It now does `Object.assign({}, headers)` and then sets `X-Kronika-Request` to `"1"`. The comment is one sentence: the shell sends only the canonical mutation header, applied after the merge so a caller cannot weaken it. The retired header literal is absent from `app.js`.

| Mirror | Assertion change |
|---|---|
| `tests/admin_batch_actions_frontend.test.js` | Both call assertions require `X-Kronika-Request` `=== "1"` and `X-FrameNest-Request` `=== undefined`. |
| `tests/ai_providers_admin_frontend.test.js` | Source count of the canonical literal is 1. Source count of the retired literal is 0. |
| `tests/catalog_card_ai_quick_action.test.js` | The harness helper applies the canonical value after the merge. Both preview assertions require the canonical value and the retired key absent. The source pattern matches `const merged = Object.assign({}, headers);` and the post-merge assignment, and rejects the old `Object.assign` literal. |
| `tests/tailscale_identity_frontend.test.js` | Normal, bare, and hostile results require the canonical value `1` and the retired key absent. The hostile input is `{ "X-Kronika-Request": "0" }`. Source order is merge, then the canonical assignment. Retired source count is 0. Canonical source count is 1. |
| `tests/contract/test_local_web_application.py` | `test_served_shell_sends_only_the_canonical_mutation_header` requires retired count 0, canonical count 1, the new merge literal, absence of the old literal, and the assignment after `Object.assign`. |
| `tests/kronika_ui.test.js` | The harness helper applies the canonical value after the merge. The POST assertion requires that value and the retired key absent. |
| `tests/youtube_acquisition_cockpit.test.js` | The harness helper applies the canonical value after the merge. This file had no assertion of the header value; it no longer contains the retired literal. |

`tests/contract/test_kronika_mutation_header.py`, `tests/companion_review_extension.test.js`, and `tests/companion_settings_automatic_analysis.test.js` were not edited. The mutation-header suite passed inside the full run.

A caller who passes the retired header into the helper still receives it, because `Object.assign` copies caller fields and the emitter does not name that header. No call site in `app.js` passes it. The hostile case proves the canonical value cannot be weakened, and every updated emission assertion sees the retired key absent.

## 2. Thread and temporary-prefix matrix

The repository convention used here is the lowercase brand component already recorded as `CANONICAL_LOWER_DIRECTORY_NAME` (`kronika`) and `CANONICAL_TEMP_DIRECTORY_NAME` (`kronika-development`): the `framenest-` producer prefix becomes `kronika-`.

| Module | Old producer string | New producer string | Pin |
|---|---|---|---|
| `media_analysis_coordinator.py` | `framenest-media-analysis-coordinator` | `kronika-media-analysis-coordinator` | none |
| `media_analysis_coordinator.py` | `framenest-media-analysis` | `kronika-media-analysis` | none |
| `upload_catalog_coordinator.py` | `framenest-upload-catalog-coordinator` | `kronika-upload-catalog-coordinator` | none |
| `upload_catalog_coordinator.py` | `framenest-upload-catalog` | `kronika-upload-catalog` | none |
| `upload_publication_coordinator.py` | `framenest-upload-publication-coordinator` | `kronika-upload-publication-coordinator` | none |
| `upload_publication_coordinator.py` | `framenest-upload-publication` | `kronika-upload-publication` | none |
| `upload_validation_coordinator.py` | `framenest-upload-validation-coordinator` | `kronika-upload-validation-coordinator` | none for the task name |
| `upload_validation_coordinator.py` | `framenest-upload-validation` | `kronika-upload-validation` | `test_upload_validation_coordinator.py` prefix, both sites |
| `x_acquisition.py` | `framenest-x-acquisition` | `kronika-x-acquisition` | none |
| `youtube_acquisition.py` | `framenest-youtube-acquisition-coordinator` | `kronika-youtube-acquisition-coordinator` | none |
| `catalog_backup_workstation.py` | `framenest-ssh-stderr-drain` | `kronika-ssh-stderr-drain` | none |
| `process.py` | `framenest-media-analysis-stdout-reader` | `kronika-media-analysis-stdout-reader` | constant import only |
| `process.py` | `framenest-media-analysis-stderr-reader` | `kronika-media-analysis-stderr-reader` | constant import only |
| `contact_sheet.py` | `framenest-contact-` | `kronika-contact-` | glob updated; see section 8 |

No `src` producer of these fourteen strings still emits a retired runtime name.

## 3. Socket default

`DEFAULT_PUBLIC_PUBLISHED_UDS_PATH` is now `Path("/run/kronika/kronika-public.sock")`. That spelling is already the default in `scripts/operator/infosec/kronika_socket_permissions_check.sh`. `WORKSPACE_UDS_PATH` is still `Path("/run/framenest/framenest.sock")`. The diff of `configuration.py` is that one line.

`test_public_published_uds_mode_defaults_distinct_socket` now pins `/run/kronika/kronika-public.sock` and still asserts inequality with `/run/framenest/framenest.sock`. `test_public_published_uds_mode_rejects_workspace_socket` is unchanged and still raises on the workspace path. Both passed inside the full suite. Explicit-path fixtures and the workspace-path hostile input were left in place.

## 4. Measured retention re-pin

The first retention run, before any scalar edit, failed three tests and passed the other twelve in that module. Pytest reported:

- per-tree occurrences: `src` 1587 against 1604, `tests` 987 against 999; deploy, scripts, docs, and extension were identical
- mutation-header occurrences: 31 against 37
- capitalized occurrences: 2321 against 2328

The file-count asserts sit after those occurrence asserts, so pytest did not reach them. `git grep -I` occurrence counts matched those pytest numbers (2321 and 31). The same command's file lists are the file movement: capitalized files 343 to 341, mutation-header files 16 to 14. `git grep -I -l FrameNest` at `HEAD` listed 343 files, matching the old pin.

Re-pin, with the cause:

- `src` 1604−17=1587. `app.js` −1 (the header literal). `configuration.py` −2 (both components of the public default). Fourteen producer strings, one each.
- `tests` 999−12=987. Ingress default pin −2, validation prefix −2, contact-sheet glob −2, catalog-card header literal −1, `kronika_ui` header literal −1, tailscale header literals −2, YouTube cockpit header literal −1, and the renamed tailscale test title −1.
- Mutation header 37−6=31 and files 16−2=14. The six literals are `app.js` −1, catalog card −1, `kronika_ui` −1, tailscale −2, YouTube cockpit −1. `app.js` and `tests/youtube_acquisition_cockpit.test.js` leave the file set.
- Capitalized occurrences 2328−7=2321 and files 343−2=341. Six are the removed header literals. The seventh is the renamed tailscale test title. The two file exits are `app.js` and `tests/youtube_acquisition_cockpit.test.js`.

Per-tree file counts, content paths, environment tokens, host paths, unit accounts, and console scripts did not fail on the pre-pin run. After the re-pin the retention module passed 15 tests in 0.35s, including the file-count asserts.

## 5. Mutation demonstrations

(a) The helper was temporarily restored to `Object.assign({ "X-FrameNest-Request": "1" }, headers)`. `node --test --test-name-pattern 'canonical literal stays single' tests/ai_providers_admin_frontend.test.js` failed at `tests/ai_providers_admin_frontend.test.js:486`: `1 !== 0`. The helper was restored to `Object.assign({}, headers)`.

(b) `thread_name_prefix` in `upload_validation_coordinator.py` was temporarily restored to `framenest-upload-validation`. `test_shutdown_after_runner_cancellation_cleans_owned_resources_and_reraises` failed at `tests/unit/application/test_upload_validation_coordinator.py:657`: `assert []` where `[] = _live_validation_threads()`. The prefix was restored to `kronika-upload-validation`.

## 6. Suites

Touched JavaScript, one `node --test` of the six edited frontend modules, before the commit: 142 passed, 0 failed, `duration_ms` 708.907.

Touched Python, through `ap exec --operation test-focus` against baseline `ca280c45755e28b6363690c50d7cdaa42187de96`, before the re-pin: the shell-header test, the mutation-header suite, ingress, upload validation, the contact-sheet cleanup test, and `test_process.py` passed. Retention supplied the only three failures. 138 passed, 3 failed, 20.87s.

Retention after the re-pin: 15 passed, 0.35s. It also passed inside the full suite.

Full Python, through `ap exec --operation test` against the same baseline, on the tree that was committed: 4713 passed, 8 skipped, 3 warnings, 0 failed, 720.39s. Difference from `4713/8/3/0`: none. The eight skips are the five real-tool cover cases, the two real-tool media-analysis cases, and the NVIDIA smoke case. The three warnings are the existing Pydantic non-serializable-default warnings.

JavaScript sanity, ordinary `node --test` from the worktree root. Counts match the declared baselines. No suite count moved.

| Suite | Result | duration_ms |
|---|---|---:|
| `tests/companion_web_bridge.test.js` | 23 passed, 0 failed | 75.722 |
| `tests/companion_review_extension.test.js` | 41 passed, 0 failed | 191.810 |
| `tests/x_companion_extension.test.js` | 55 passed, 0 failed | 121.853 |
| `tests/companion_settings_automatic_analysis.test.js` | 6 passed, 0 failed | 10066.440 |
| `tests/kronika_ui.test.js` | 12 passed, 0 failed | 92.539 |
| `tests/catalog_card_ai_quick_action.test.js` | 30 passed, 0 failed | 221.277 |
| `tests/*_frontend.test.js tests/*_cockpit.test.js tests/gallery_*.test.js` | 212 passed, 0 failed | 746.132 |

The four middle summaries were recaptured because the first combined transcript was truncated. Both runs exited 0. The table is the captured count for each suite.

## 7. Diff, commit, Part A, Part B, Part C

Commit `063b045c0e431760cfc48996bec1160c4d4b7e0b` on `main`, subject `Retire the active mutation-header mirror, runtime names, and public socket default.` One `git add` of the twenty-two paths and one non-amended commit. No push. The working tree is clean.

`git diff --stat HEAD~1`:

```text
 src/kronika/adapters/api/web/app.js                |  8 +---
 .../application/media_analysis_coordinator.py      |  4 +-
 .../application/upload_catalog_coordinator.py      |  4 +-
 .../application/upload_publication_coordinator.py  |  4 +-
 .../application/upload_validation_coordinator.py   |  4 +-
 src/kronika/application/x_acquisition.py           |  2 +-
 src/kronika/application/youtube_acquisition.py     |  2 +-
 src/kronika/configuration.py                       |  2 +-
 .../infrastructure/media_analysis/contact_sheet.py |  2 +-
 .../infrastructure/media_analysis/process.py       |  4 +-
 .../persistence/catalog_backup_workstation.py      |  2 +-
 tests/admin_batch_actions_frontend.test.js         |  6 ++-
 tests/ai_providers_admin_frontend.test.js          |  5 ++-
 tests/catalog_card_ai_quick_action.test.js         | 17 +++++++--
 tests/contract/test_kronika_identity_retention.py  | 43 +++++++++++++++++++---
 tests/contract/test_local_web_application.py       | 11 +++---
 tests/kronika_ui.test.js                           |  9 ++++-
 tests/tailscale_identity_frontend.test.js          | 32 ++++++++--------
 .../test_upload_validation_coordinator.py          |  4 +-
 .../test_movie_contact_sheet_selection.py          |  4 +-
 tests/unit/test_configuration_ingress.py           |  2 +-
 tests/youtube_acquisition_cockpit.test.js          |  6 ++-
 22 files changed, 113 insertions(+), 64 deletions(-)
```

Part A is byte-unmoved. No frozen path is in the diff, and the frozen-hash tests passed inside the 4713. Part B is still empty: the basename test passed. Part C movement is the four scalars in section 4, from the pre-pin pytest failures and the matching `git grep -I` file counts.

## 8. Sites no test exercises

These renamed producer strings have no spelling assertion:

- `kronika-media-analysis-coordinator` and `kronika-media-analysis`
- `kronika-upload-catalog-coordinator` and `kronika-upload-catalog`
- `kronika-upload-publication-coordinator` and `kronika-upload-publication`
- `kronika-upload-validation-coordinator` (the asyncio task name; the executor prefix is pinned)
- `kronika-x-acquisition`
- `kronika-youtube-acquisition-coordinator`
- `kronika-ssh-stderr-drain`

`test_process.py` compares live reader threads with the imported constants, so a spelling change that keeps those bindings does not fail. The contact-sheet test globs `kronika-contact-*` and asserts the set is unchanged after cleanup. A reverted prefix that is still deleted leaves that equality true. `tests/youtube_acquisition_cockpit.test.js` updates the harness helper and does not assert the header on a recorded call.

## 9. Deviations, risks, missing evidence, smallest next step

Deviation: the hostile helper case no longer supplies the retired header. Putting that literal in the emitter, including a delete, would violate the canonical-only source contract. Caller-supplied pass-through is the remaining behavior, and no `app.js` call site supplies it.

Risk: `default_ai_config_path` is still the part B fallback and was not edited. `src/kronika/infrastructure/ai/configuration.py` is absent from the diff.

Missing evidence: none of the required suites. Rendered UI was outside this grant.

Smallest next step: part B, the `default_ai_config_path` switch with its migration-coherence proof.

Resolved Execution Issues / Near-Misses

One accidental `/usr/bin` `python3 -c` printed `skip` during a count command and was not used as evidence. The counts in section 4 are pytest and `git grep -I`. No forbidden interpreter was used for the suites. Python evidence used `./.ap/ap exec` and `./.ap/ap project check`.

Pre-Existing Failure Classification

none

Authority expiry: submission of this report expires all authority under the session-66 exchange-01 prompt.

Orchestration critique:
MEASURED: none
LEAD: none