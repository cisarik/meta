### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-sole-identity
Worker session ordinal: 67
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-CORR-C9B16B — the AI-config default switch
status: PASS
Phase-qualified result: not-applicable
Start commit: 063b045c0e431760cfc48996bec1160c4d4b7e0b
End commit: 22615a7721d89777bf1614b03baec220c80d3782
Report justification: new-mutation
Logical-whole closure: not-closed

Gates re-derived before mutation. Local `main` was clean at `063b045c0e431760cfc48996bec1160c4d4b7e0b`. `git ls-remote origin refs/heads/main` was `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`. Primary class for that lead: `unpublished-candidate`. Secondary fact: `accepted-continuation` of the unpublished C9-B sequence. No unexplained remainder. The containing `.ap` gitlink and submodule `HEAD` were both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`. `./.ap/ap doctor` PASS, governing variant stable. `./.ap/ap project check --root /home/agile/Projects/kronika --baseline 063b045c0e431760cfc48996bec1160c4d4b7e0b` PASS. `FROZEN_ALEMBIC_SHA256` has 36 keys, counted from the dict. No host contact and no browser.

Changed files, one purpose: the unset AI-config default now returns the canonical directory, the migration tool still reads the legacy AI sources, and the pins that the switch moved were re-measured.

## 1. Default matrix

`default_ai_config_path` is otherwise unchanged: the canonical override, the absolute-path check, the conflict handler, and the function shape stay. With no override:

| Shape | Return |
|---|---|
| `platform="darwin"` | `home/Library/Application Support/Kronika/ai/config.json` |
| Linux with `XDG_CONFIG_HOME` | `resolved(XDG_CONFIG_HOME)/kronika/ai/config.json` |
| Linux with no `XDG_CONFIG_HOME` | `home/.config/kronika/ai/config.json` |

`tests/unit/infrastructure/ai/test_ai_configuration_storage.py` was not edited. `test_config_path_override_is_absolute` still accepts an absolute `KRONIKA_AI_CONFIG_PATH` and still rejects a relative one. `tests/contract/test_kronika_direct_reader_routing.py` was not edited. A retired `FRAMENEST_AI_CONFIG_PATH` alone still equals the no-override call, and a mixed pair still returns the canonical path.

The four callers only pass the function's return value through. None embeds a directory literal, and none was edited:

- `src/kronika/adapters/cli/ai.py` calls `default_ai_config_path()` when the CLI has no config path
- `src/kronika/infrastructure/ai/registry.py` calls `default_ai_config_path(source)` when no config path is passed
- `src/kronika/adapters/api/ai_admin_api.py` calls `default_ai_config_path(dependencies.environ)`
- `src/kronika/adapters/api/application.py` calls `default_ai_config_path()` for the research configuration path

## 2. Coherence test

Extended `test_development_destinations_equal_the_public_default_functions` in `tests/contract/test_local_state_migration.py`. Legacy locations are built from `LEGACY_APP_DIRECTORY_NAME` or `LEGACY_LOWER_DIRECTORY_NAME` plus `AI_DIRECTORY_NAME` and `AI_CONFIG_FILENAME`. The assertions are:

- Darwin destination of `macos_ai_configuration` equals `default_ai_config_path({}, platform="darwin", home=home)`.
- That default equals `home/Library/Application Support/CANONICAL_APP_DIRECTORY_NAME/ai/config.json`.
- The migration source equals the same shape with `LEGACY_APP_DIRECTORY_NAME`.
- Darwin test-state and status-snapshot destinations equal the helpers of the new default; their sources equal the legacy parent plus `AI_TEST_STATE_FILENAME` and `AI_STATUS_SNAPSHOT_FILENAME`.
- With `XDG_CONFIG_HOME` set, the `xdg_ai_configuration` destination equals the Linux default, and that default equals `resolved(XDG_CONFIG_HOME)/CANONICAL_LOWER_DIRECTORY_NAME/ai/config.json`.
- That migration source equals `resolved(XDG_CONFIG_HOME)/LEGACY_LOWER_DIRECTORY_NAME/ai/config.json`.
- The XDG sibling destinations follow the new default; the sibling sources follow the legacy parent.
- The new default's directory name and the destination's directory name equal `CANONICAL_LOWER_DIRECTORY_NAME`. The legacy source's directory name equals `LEGACY_LOWER_DIRECTORY_NAME`.
- With no XDG variables, the Linux destination equals `default_ai_config_path({}, platform="linux", home=home)`, that default equals `home/.config/CANONICAL_LOWER_DIRECTORY_NAME/ai/config.json`, and the source equals `home/.config/LEGACY_LOWER_DIRECTORY_NAME/ai/config.json`.

## 3. Migration-intact proof and pins

`src/kronika/infrastructure/runtime/local_state_migration.py` is absent from the commit. Its diff was empty before the commit. `LEGACY_APP_DIRECTORY_NAME`, `LEGACY_LOWER_DIRECTORY_NAME`, `LEGACY_TEMP_DIRECTORY_NAME`, the canonical constants, the replacement pairs, and both AI source readings are untouched. The mapping tests still assert the literal legacy sources `.../FrameNest/ai/config.json` and `.../framenest/ai/config.json`, and those tests passed inside the focused run and the full suite. The refusal safeguard is not in the diff.

Pins:

- `tests/contract/test_local_state_migration.py` — extended as above. Named in the grant before the edit.
- `tests/unit/infrastructure/ai/test_ai_configuration_storage.py` — verified, not edited.
- `tests/contract/test_kronika_direct_reader_routing.py` — verified, not edited.
- `tests/contract/test_kronika_identity_retention.py` — measured re-pin in section 4.
- `tests/contract/test_kronika_product_string_agreement.py` — found by the first full suite, then pinned from that measurement. See the near-miss.

## 4. Measured retention re-pin

The first retention run, before any scalar edit, failed four tests. Pytest reported:

- per-tree files: `src` 182 against 183; the other five trees were identical
- per-tree occurrences: `src` 1585 against 1587, `tests` 986 against 987; deploy, scripts, docs, and extension were identical
- content paths: `unexpected=[]`, `missing=['src/kronika/infrastructure/ai/configuration.py']`
- capitalized occurrences: 2320 against 2321

The capitalized file-count assert sits after the occurrence assert, so pytest did not reach it. `git grep -I -l FrameNest`, with the ledger excluded, listed 340 files. The same command's occurrence count was 2320, matching pytest. `git grep -I -o -i framenest` was 1585 under `src` and 986 under `tests` excluding the ledger. `configuration.py` itself had zero remaining hits.

Re-pin, with the cause:

- `src` files 183−1=182. `infrastructure/ai/configuration.py` lost its last retired token and left the content set.
- `src` occurrences 1587−2=1585. Both fallback directory literals left that file.
- `tests` occurrences 987−1=986. The old default pin `== "framenest"` in `test_local_state_migration.py` was replaced by the legacy-constant comparison. No test file lost its last occurrence, so the tests file count stays 173.
- Content path: one removal, no addition, `src/kronika/infrastructure/ai/configuration.py`.
- Capitalized occurrences 2321−1=2320 and files 341−1=340. The one departure is the darwin fallback literal. That file leaves the capitalized file set.

Environment tokens, the mutation header, host paths, unit accounts, and console scripts did not fail. After the re-pin the retention module passed, including the file-count asserts, and it passed again inside the final 4713.

## 5. Mutation demonstration

The darwin fallback was temporarily restored to `FrameNest`. `test_development_destinations_equal_the_public_default_functions` failed at `tests/contract/test_local_state_migration.py:412`:

`assert darwin_plan.by_key("macos_ai_configuration").destination == darwin_ai`

The destination ended in `Application Support/Kronika/ai/config.json`. The reverted default ended in `Application Support/FrameNest/ai/config.json`. One failure, 0.41s. The literal was restored to `Kronika` before any later suite.

## 6. Suites

Focused, through `ap exec --operation test-focus` against baseline `063b045c0e431760cfc48996bec1160c4d4b7e0b`, before the retention re-pin: `test_local_state_migration.py`, `test_ai_configuration_storage.py`, `test_kronika_direct_reader_routing.py`, and the retention module. 96 passed, 4 failed, 0.98s. The four failures are the retention tests in section 4. The migration, storage, and routing modules passed.

Retention after the re-pin, with the coherence test, the override test, and the two retired-prefix routing tests: 19 passed, 1.07s.

After the product-string pin, that module plus retention plus the coherence test: 35 passed, 2.09s.

The first full Python suite, on the tree before the product-string pin, was 4 failed, 4709 passed, 8 skipped, 3 warnings, 728.81s. Those four failures are the inventory in the near-miss. The candidate then changed, so the suite was run again.

Final full Python suite, through `ap exec --operation test` against the same baseline, on the tree that was committed: 4713 passed, 8 skipped, 3 warnings, 0 failed, 723.83s. Difference from `4713/8/3/0`: none. The eight skips are the five real-tool cover cases, the two real-tool media-analysis cases, and the NVIDIA smoke case. The three warnings are the existing Pydantic non-serializable-default warnings. Retention passed inside that suite.

JavaScript, ordinary `node --test` from the worktree root. Counts match the declared baselines. No suite count moved.

| Suite | Result | duration_ms |
|---|---|---:|
| `tests/companion_web_bridge.test.js` | 23 passed, 0 failed | 80.542 |
| `tests/companion_review_extension.test.js` | 41 passed, 0 failed | 186.884 |
| `tests/x_companion_extension.test.js` | 55 passed, 0 failed | 126.018 |
| `tests/companion_settings_automatic_analysis.test.js` | 6 passed, 0 failed | 10068.489 |
| `tests/kronika_ui.test.js` | 12 passed, 0 failed | 92.147 |
| `tests/catalog_card_ai_quick_action.test.js` | 30 passed, 0 failed | 212.821 |
| `tests/*_frontend.test.js tests/*_cockpit.test.js tests/gallery_*.test.js` | 212 passed, 0 failed | 749.897 |

## 7. Diff, commit, Part A, Part B, Part C

Commit `22615a7721d89777bf1614b03baec220c80d3782` on `main`, subject `Point the unset AI config default at the canonical migration destination.` Parent `063b045c0e431760cfc48996bec1160c4d4b7e0b`. One `git add` of the four paths and one non-amended commit. No push. The working tree is clean.

`git diff --stat HEAD~1`:

```text
 src/kronika/infrastructure/ai/configuration.py     |  4 +-
 tests/contract/test_kronika_identity_retention.py  | 26 +++++--
 .../test_kronika_product_string_agreement.py       | 15 ++--
 tests/contract/test_local_state_migration.py       | 83 +++++++++++++++++++---
 4 files changed, 105 insertions(+), 23 deletions(-)
```

Part A is byte-unmoved. No frozen path is in the diff, and the frozen-hash tests passed inside the 4713. Part B is still empty: the basename test passed. Part C movement is the five retention pins in section 4. The product-string inventory is a separate pin: occurrences 63+1=64, in-scope 61+1=62, and the duplicate literal `Kronika` 8+1=9. The one new row is `('src/kronika/infrastructure/ai/configuration.py', 'default_ai_config_path', 'Constant', 0)` with value `Kronika`. The lowercase XDG fallback is not a brand-bearing node.

## 8. Sites no test exercises

Both fallback literals are asserted by the named test, including the unset-`XDG_CONFIG_HOME` shape. No moved or removed production site lacks a test. The four callers in section 1 do not themselves assert the fallback spelling; they use the function the named test covers.

The literal legacy AI sources in `test_macos_plan_covers_exactly_the_owned_classes_and_brand_components` and `test_xdg_plan_uses_xdg_roots_and_the_lowercase_ai_directory` were left in place. They pin the migration sources, which this grant retains.

## 9. Deviations, risks, missing evidence, smallest next step

Deviation: the retention edit removed one content-path membership in addition to the numeric scalars, because the measured failure named that path. The product-string inventory was not in the initial path-literal parse; it was pinned after the first full suite measured it.

Risk: the migration module's opening still says it resolves the legacy locations the current defaults use. That sentence is now stale for the AI config default. Negative authority forbids editing the module. The coherence test is the live binding.

Missing evidence: none of the required suites. Rendered UI, publication, and the NUC were outside this grant.

Smallest next step: Orchestrator acceptance of this commit. Publication, the NUC refresh, and rendered acceptance each stay separately authorized.

Resolved Execution Issues / Near-Misses: one discarded `python3 -c` ran beside the Alembic key count and was not used as evidence; the count of 36 came from an awk scan of the dict. The brand-bearing Constant inventory was missed by the path-literal grep; the first full suite measured one unexpected `Constant` in `default_ai_config_path`, occurrence 64 against 63, and duplicate `Kronika` 9 against 8. The pin was written from that measurement and the full suite was re-run to 4713/8/3/0.

Pre-Existing Failure Classification: none

Authority expiry: this terminal report ends the grant; no autonomous continuation.

Orchestration critique:
MEASURED: `tests/contract/test_kronika_product_string_agreement.py` was outside the named paths, and a grep for the old directory literals does not find it; evidence is the first full suite (unexpected `Constant` 0 in `default_ai_config_path`, 64 against 63, `Kronika` 9 against 8); effect was four failures until the measured row was added; smallest correction is to name that inventory in any later grant that adds a capitalized brand constant under `src/kronika`.
LEAD: none