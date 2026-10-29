### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-sole-identity
Worker session ordinal: 45
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-C7AS-API — complete the C7-A/S server companion API emission
status: PASS
Phase-qualified result: not-applicable
Start commit: 7c1cee299e14dbccaca10fe0ce749b4dc7553420
End commit: c152a178dcfbbe6e8f04f98d1b9f3f8cb7aea209
Report justification: new-mutation
Logical-whole closure: not-closed
NUC contact: none

Starting gates, re-derived: standalone `main` at `/home/agile/Projects/kronika`, clean, `HEAD` and `origin/main` both `7c1cee299e14dbccaca10fe0ce749b4dc7553420`, `.ap` gitlink and submodule HEAD both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`. `ap doctor` PASS, governing variant stable. `ap project check --baseline` PASS. `FROZEN_ALEMBIC_SHA256` key count computed from the dict: 36.

Changed files: `src/kronika/application/companion_picker.py` (emission constant), `tests/contract/test_x_companion_api.py` and `tests/contract/test_tailscale_ingress_security.py` (the only two emitted-literal pins), `tests/contract/test_kronika_identity_retention.py` (Part C occurrence scalars and the arithmetic ledger). No `extension/**`, document, dependency, or frozen blob was edited.

## 1. Inventory

Case-insensitive `framenest-companion` and `framenest_companion`, excluding `.git` and `.venv`. `rg` stats: 92 matches, 92 matched lines, 15 files, 856 files searched. Output was not truncated. Counts below sum to 92.

| Class | Path | Lines | Action |
|---|---|---|---|
| Emission constant | `src/kronika/application/companion_picker.py` | 30 | Flipped to `kronika-companion.v1` |
| Emitted-literal pin | `tests/contract/test_x_companion_api.py` | 245 | Flipped |
| Emitted-literal pin | `tests/contract/test_tailscale_ingress_security.py` | 1635 | Flipped |
| Retired reader | `extension/shared/messages.js` | 13 (`RETIRED_API_VERSION`) | Kept. Comment at 9–11 kept |
| Reader acceptance | `tests/companion_review_extension.test.js` | 2544, 2552 (retired body and assertion), 2570 (`framenest-companion.v2` inside the unknown-version refusal list) | Kept, no edit |
| Ledger prose, not a pin | `tests/contract/test_kronika_identity_retention.py` | 334 | Kept. The file is excluded from its own count |
| Other: temp-directory prefix, not a version pin | `tests/browser_companion_evidence.test.js` | 190 | Reported, not edited |
| Other: `FRAMENEST_COMPANION_EXTENSION_ORIGINS` | `SECURITY.md` | 261, 270 | Reported, not edited |
| Other: same environment key | `deploy/systemd/framenest.env.example` | 60 | Reported, not edited |
| Other: same environment key | `docs/UBUNTU_NUC_DEPLOYMENT.md` | 1320 | Reported, not edited |
| Other: same environment key | `docs/X_COMPANION.md` | 170, 179 | Reported, not edited |
| Other: same environment key | `tests/unit/test_configuration_ingress.py` | 260 | Reported, not edited |
| Other: same environment key | `tests/contract/test_fedora_systemd_service.py` | 207, 214 | Reported, not edited |
| Other: DOM/CSS `data-framenest-companion`, not the API version | `extension/content/x_adapter.js` | 32, 66, 67, 68, 69, 73, 74, 77, 78, 82, 86, 87, 98, 101, 126, 127, 133, 134, 135, 248, 249, 257, 259, 452, 456, 491, 698, 798, 845, 946, 1137, 1458, 1486, 1541, 1606, 1636, 1744, 1888 (38) | Kept for the later companion cut |
| Other: DOM acceptance of that attribute | `tests/x_companion_extension.test.js` | 252, 270, 272, 278, 282, 291, 292, 343, 522, 530, 538, 547, 1061, 1062, 1063, 1064, 1093, 1100, 1105, 1112, 1278, 1281, 1283, 1286, 1307, 1310, 1311, 1330, 1331, 1914, 1943, 2007, 2024, 2039, 2152, 2216 (36) | Kept |

No further repository assertion pins the emitted retired literal. `tests/unit/test_companion_picker.py:78` compares the page field to the `COMPANION_API_VERSION` symbol, so it follows the constant and is not a literal pin. The exact string `framenest-companion.v1` occurred in seven places before the edit: the constant, the two pins, the extension reader, the two reader-acceptance lines, and the ledger comment.

## 2. Emission

Before the edit the constant and both pins were the literal `framenest-companion.v1`. The focused companion modules then passed 97 in 47.69s (wall 49s), which is the behavior those pins require.

After the edit the constant and both pins are `kronika-companion.v1`. `ListCompanionPickerMedia.execute` still assigns that constant onto the page, and `_page_dict` still emits `page.companion_api_version`. Remaining `framenest-companion.v1` literals are only the extension reader, its two acceptance lines, and the historical ledger comment. The unknown-version JS case still refuses `framenest-companion.v2`, `kronika-companion.v0`, empty, null, undefined, and `7`.

## 3. Mutation demonstration

With the pins already canonical, the constant was temporarily restored to `framenest-companion.v1` and the two pin tests were run. Both failed in 2.06s:

- `test_owner_sees_published_jpeg_and_own_private_x_meme` at `test_x_companion_api.py:245`: `AssertionError: assert 'framenest-companion.v1' == 'kronika-companion.v1'`
- `test_companion_picker_route_is_readable_without_mutation_origin` at `test_tailscale_ingress_security.py:1635`: the same mismatch

The constant was restored to `kronika-companion.v1` before the final suites. The final tree contains that canonical spelling.

## 4. Verification

All counts match the baseline. No count difference from 97, 40, 4955/8/3/0, or 15.

| Suite | Result | Runner time | Wall |
|---|---|---|---|
| Focused companion modules, final tree | 97 passed, exit 0 | 47.91s | 48s |
| `node --test tests/companion_review_extension.test.js` | 40 passed, 0 failed, 0 skipped | 190.77ms | 1s |
| Full declared Python suite | 4955 passed, 8 skipped, 3 warnings, exit 0 | 684.62s | 686s |
| Retention module | 15 passed, exit 0 | 0.36s | 1s |

The three warnings are the same `PydanticJsonSchemaWarning` on `test_health_contract_is_present_in_openapi`, `test_api_key_not_disclosed_in_health_response_openapi_or_app_repr`, and `test_database_path_absent_from_settings_repr_logs_api_and_openapi`. The JS run includes the retired acceptance, the canonical acceptance, and the unknown-version refusal, with no JS edit.

## 5. Commit and retention

`git diff --stat` for `c152a178dcfbbe6e8f04f98d1b9f3f8cb7aea209` (parent `7c1cee299e14dbccaca10fe0ce749b4dc7553420`):

```text
 src/kronika/application/companion_picker.py       |  2 +-
 tests/contract/test_kronika_identity_retention.py | 21 +++++++++++++++++++--
 tests/contract/test_tailscale_ingress_security.py |  2 +-
 tests/contract/test_x_companion_api.py            |  2 +-
 4 files changed, 22 insertions(+), 5 deletions(-)
```

Local non-amended commit on `main`. Not pushed. Worktree clean. `main` is ahead of `origin/main` by 1.

Part A is byte-unmoved: the frozen-document and frozen-Alembic tests are inside the green retention module, and this commit does not touch those paths. Part B still measures 20 (the basename set has 20 entries and `test_framenest_basename_path_ledger_matches_exactly` passed).

Part C movement, measured before the re-pin, with the companion suite already green. `test_per_tree_framenest_occurrence_counts_match` failed and the other probed Part C checks passed, including file counts, content-path membership, capitalized counts, the Alembic set, and the basename ledger:

```text
{'src': 1704} != {'src': 1705}
{'tests': 2280} != {'tests': 2282}
```

Cause: one retired literal left `src/kronika/application/companion_picker.py` (1705 → 1704). Four `FrameNest` identifiers remain there, so the file stays in the content set. One emitted pin left each of `tests/contract/test_x_companion_api.py` and `tests/contract/test_tailscale_ingress_security.py` (2282 → 2280). The first still contains `framenest.sock`; the second had 12 case-insensitive hits before the edit and lost only the version pin, so neither file leaves the content set. File counts stay 186 and 186. No other Part C scalar moved. The re-pin records that arithmetic on both scalars. Retention then passed 15.

## 6. Untested sites and unnamed consumers

No moved site lacks a test. The constant is read by the unit equality and emitted through both HTTP pins. The ledger numbers are read by the occurrence test.

The falsy arm of `_page_dict`, `page.companion_api_version or COMPANION_API_VERSION`, is not taken by any test. The page constructor always sets the constant, and both HTTP tests observe that truthy value.

Consumers of `COMPANION_API_VERSION` this prompt did not name:

- `src/kronika/application/companion_picker.py:117`, the page assignment
- `src/kronika/adapters/api/x_companion_api.py:163`, the fallback emission (the module was named; this expression was not)
- `tests/unit/test_companion_picker.py:8` and `:78`, symbol comparison

## 7. Deviations, risks, missing evidence, next step

Deviations: none. The extension comment at `messages.js:9–11` still says the server emits the retired spelling until a later cut moves `COMPANION_API_VERSION`. This cut was forbidden to edit `extension/**`, so that sentence is now stale on purpose.

Risk: this commit is local only. A refreshed extension still accepts the retired spelling, so the unpushed tree does not break the current served API. Both canonical emissions are together only after a separate publication and exact-main NUC refresh.

Missing evidence: no live HTTP response and no browser. This cut forbids host contact.

Smallest next step: Orchestrator acceptance of this commit, then a separate publication and exact-main NUC refresh before C7-A/C.

Git result: one local commit, no push, no branch, no tag.
Validation: gates, inventory, pre-edit focused run, mutation failure, final focused run, JS, full Python suite, retention.
Changed files purpose: canonical API emission, matching pins, measured Part C re-pin.

Resolved Execution Issues / Near-Misses: `/usr/bin/time` is not installed. Elapsed figures are `date` wall-clock seconds plus the runner duration line. The mutation edit was restored before the final suites; the restored constant was read back as `kronika-companion.v1`.
Pre-Existing Failure Classification: none

Orchestration critique:
MEASURED: `extension/shared/messages.js:9–11` still says the server emits `framenest-companion.v1` until `COMPANION_API_VERSION` moves; this commit moved that constant and was forbidden to edit the extension; the comment is stale once this commit is served; smallest correction is to update that comment in the cut allowed to touch `extension/**`.
LEAD: none

Authority expiry: this terminal report ends the grant. No further implementation, no second commit, no push, no publication, no refresh, no host contact, and no later cut is authorized.