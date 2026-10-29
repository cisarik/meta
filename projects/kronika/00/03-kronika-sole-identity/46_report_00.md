### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-sole-identity
Worker session ordinal: 46
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C7AC — canonical companion emissions and stored-state completion
status: PASS
Phase-qualified result: not-applicable
Start commit: c152a178dcfbbe6e8f04f98d1b9f3f8cb7aea209
End commit: aee0a60a04b78685608ec5a65ec5780c7d9884e7
Report justification: new-mutation
Logical-whole closure: not-closed
NUC contact: none

Starting gates, re-derived: standalone checkout on `main` at `/home/agile/Projects/kronika`, clean, `HEAD` and public `main` both `c152a178dcfbbe6e8f04f98d1b9f3f8cb7aea209`, `.ap` gitlink and submodule HEAD both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`. `ap project check --baseline` PASS. `FROZEN_ALEMBIC_SHA256` key count computed from the dict: 36.

Origin-helper names follow the existing FrameNest-to-Kronika prefix: `canonicalizeKronikaOrigin` and `acceptKronikaOrigin`. No aliases. The bridge field `CURRENT_WEB_PROTOCOL` remains and is equal to the emitted `kronika.companion.web.v1`.

The only application-owned browser pairs with a retired counterpart are the origin key `kronikaOrigin` / `frameNestOrigin` and the alarm `kronika.review-inbox` / `framenest.review-inbox`. `inflightClaims`, `adapterAcknowledged`, `reviewInboxExplicitCollapsed`, `reviewInboxSeenRunId`, and `reviewInboxAwaitingAnalysis` have no retired counterpart and were not given one.

Consumers the prompt did not name, found by parse and edited before the commit: `tests/browser_companion_evidence.test.js` and `tests/support/x_fixtures/composer.html`.

## 1. Emission and reader tables

Counts were regenerated with `git grep -I -F -c` on `c152a178dcfbbe6e8f04f98d1b9f3f8cb7aea209` and on `aee0a60a04b78685608ec5a65ec5780c7d9884e7`. Output was not truncated.

| Retired token | Before | After | Remaining classification |
|---|---:|---:|---|
| `framenest.companion.web.v1` | 12 | 10 | Retained readers, removal cut C7-B: `extension/ui/sidebar.js` (`RETIRED_WEB_PROTOCOL`), `companion_host.js` (`ACCEPTED_WEB_PROTOCOLS`). Acceptance and near-miss fixtures: `companion_web_bridge.test.js` (3), `companion_review_extension.test.js` (1), `test_local_web_application.py` (1, the host accepted-list pin). Ledger comment: retention file (1). Frozen documents: ADR-0063, ADR-0076. |
| `X-FrameNest-Request` | 74 | 71 | No extension emission remains. Server emission stays in `app.js` (`framenestMutationHeaders`) until C7-B. Tests that pin server dual-acceptance, absence on the extension, or the server-gate model stay. Documents and `SECURITY.md` stay out of scope. |
| `framenest-attach` | 11 | 0 | Moved to `kronika-attach`. |
| `framenest-save-popup` | 5 | 0 | Moved to `kronika-save-popup`. |
| `framenest-save-host` | 6 | 0 | Moved to `kronika-save-host`. |
| `FrameNestSidebarBridge` | 2 | 0 | Moved to `KronikaSidebarBridge`. |
| `FrameNestReviewInbox` | 4 | 0 | Moved to `KronikaReviewInbox`. |
| `FrameNestReviewOverlay` | 2 | 0 | Moved to `KronikaReviewOverlay`. |
| `FrameNestXAdapterContractV1` | 3 | 0 | Moved to `KronikaXAdapterContractV1`. |
| `FrameNestXAdapterTestHooks` | 27 | 0 | Moved to `KronikaXAdapterTestHooks`. |
| `canonicalizeFrameNestOrigin` | 7 | 0 | Moved to `canonicalizeKronikaOrigin`. |
| `acceptFrameNestOrigin` | 14 | 2 | Both remaining are ADR-0063, a frozen document. |
| `FrameNestCompanionWeb` | 13 | 1 | The one remaining hit is the retention cause comment. Definition and consumers are `KronikaCompanionWeb`. |
| `data-framenest-` | 140 | 1 | The one remaining hit is the negative agreement assertion in `x_companion_extension.test.js`. No attribute, selector, or style remains. |
| `framenest-save-live` | 5 | 1 | Same negative assertion. Product spelling is `kronika-save-live`. |
| `framenestSaveKind` | 1 | 0 | Moved to `dataset.kronikaSaveKind`. |
| `framenest-companion.v1` | 4 | 4 | Retained reader, removal cut C7-B: `messages.js` `RETIRED_API_VERSION`. Acceptance fixtures: `companion_review_extension.test.js` (2). Ledger comment (1). |
| `framenest.review-inbox` | 8 | 15 | Retained reader, removal cut C7-B: `messages.js` `retiredAlarmName`. The increase is new tests that still name the retired alarm. Frozen documents: `ROADMAP.md`, `docs/X_COMPANION.md`. Ledger comment (1). |
| `frameNestOrigin` | 39 | 53 | Retained reader, removal cut C7-B: `messages.js` `STORAGE.origin.retiredName`. The increase is the migration matrix. ADR-0063 stays. |

`FrameNestCompanion` fell from 58 to 28. The 28 that remain are Python product identifiers (`FrameNestCompanionReviewRepositoryError` and its repository neighbors in `companion_review_api.py`, `media_analysis_lifecycle_api.py`, `companion_review_repository.py`, the persistence adapter, and `test_companion_review_repository.py`) plus the retention comment. They are not the JavaScript global and were not renamed.

Every outbound web message in `sidebar.js` uses `WEB_PROTOCOL = "kronika.companion.web.v1"`. The receive side accepts that spelling and `framenest.companion.web.v1`, and refuses any other. Extension mutation requests send only `X-Kronika-Request: 1`. A whole-extension search for `X-FrameNest-Request`, `framenest-attach`, `framenest-save-`, `data-framenest-`, `FrameNestCompanion`, `acceptFrameNestOrigin`, and `canonicalizeFrameNestOrigin` is empty.

Corrected probe against the unmodified tree, before editing. The first probe used an origin outside the tailnet pattern and evaluated `messages.js` without `URL`; those two misses were probe defects and are not product failures. After correction, the new expectations failed as follows:

- Outbound `WEB_PROTOCOL` was `framenest.companion.web.v1`.
- `open_details` emitted the retired spelling.
- The identity request carried `X-FrameNest-Request: 1`.
- An old-only origin left `kronikaOrigin` undefined.
- After `ensureReviewInboxAlarm`, `framenest.review-inbox` was still present.
- The root global was `FrameNestCompanion`, and `KronikaSidebarBridge` was absent.
- `x_adapter.js` still contained `data-framenest-`.
- `framenest-attach` was still present.

Receive-side acceptance of retired, canonical, and unknown was already the required split on the unmodified tree, so that check passed before the edit. The temporary probe stayed outside the repository and is not in the commit.

## 2. DOM and style agreement

`data-framenest-` is 140 before and 1 after, and that one is the absence assertion. Companion attributes, selectors, and the inline style block in `x_adapter.js` use `data-kronika-*`. The contract file and `composer.html` use the same prefix. `.kronika-save-live` and `id="kronika-save-live"` agree with each other. `dataset.kronikaSaveKind` agrees with `data-kronika-save-kind`.

`data-kronika-` is 38 before and 187 after. The before count already includes canonical shell attributes in `app.js` and `index.html` that this cut did not touch. The increase is the moved companion family plus the new agreement assertions.

The agreement test loads the adapter, contract, `save.js`, and the service worker and checks that an attribute token, its selector, the live-region class and id, and `ATTACH_PORT` against `port.name` are the same spelling.

## 3. Storage and alarm matrix

`completeStoredEntryMigration` re-reads immediately before copying a retired-only value, writes the canonical value, reads it back, and removes the retired key only when the readback matches. A failed readback does not remove. Canonical wins when both exist. `copied` is true only for the old-only write.

Observed on the service-worker fake:

- Old-only writes canonical, verifies, then removes, and keeps an unrelated key. Operation order is `get`, `get`, `set`, `get`, `remove`.
- Canonical-only does not remove a key that is already absent and does not write.
- Both-same and both-conflicting keep the canonical value and remove the retired value.
- Neither leaves both absent.
- A third `get` that hides the canonical value returns `verified: false` and does not remove.
- Configure writes `kronikaOrigin` and then drops a retired duplicate.
- Reset removes both origin spellings and both alarms. A later `configuredOrigin()` does not recreate `frameNestOrigin`.
- The listener still refreshes the badge for a manually re-added `framenest.review-inbox`.

When an origin is configured, `ensureReviewInboxAlarm` creates `kronika.review-inbox` and then clears only `framenest.review-inbox`. A second call leaves the canonical alarm and the badge text unchanged. If `chrome.alarms.create` throws, the retired alarm is not cleared. Disconnect and reset still clear both names and the badge. The not-configured path still clears both.

## 4. Mutation demonstrations

Each mutation was restored before the final suites. The committed tree is the restored tree.

- Web protocol set back to `framenest.companion.web.v1`. `extension open_details emits the canonical spelling` failed at `tests/companion_web_bridge.test.js:405`: actual `framenest.companion.web.v1`, expected `kronika.companion.web.v1`.
- `"X-FrameNest-Request": "1"` restored beside the canonical header. Class 1 failed at `tests/companion_review_extension.test.js:2493`: actual `{ retired: '1', current: '1' }`, expected `{ retired: undefined, current: '1' }`.
- `storage.remove(retiredName)` inserted before the verifying read. The migration test failed at `tests/companion_review_extension.test.js:2651`: actual `['get','get','set','remove','get','remove']`, expected `['get','get','set','get','remove']`.
- The retired-alarm `clear` removed from `ensureReviewInboxAlarm`. The alarm test failed at `tests/companion_review_extension.test.js:2792`: actual `{ name: 'framenest.review-inbox', periodInMinutes: 1 }`, expected `undefined`.
- Only `setAttribute("data-kronika-companion", "save")` reverted to `data-framenest-companion`. The agreement test failed at `tests/x_companion_extension.test.js:2636` because `source.includes("data-framenest-")` became true.

## 5. Suites

| Suite | Result | Runner time | Baseline difference |
|---|---|---|---|
| `companion_web_bridge.test.js` | 27 passed, 0 failed | 87.18ms | count unchanged |
| `companion_review_extension.test.js` | 42 passed, 0 failed | 293.75ms | +2 (migration matrix, retired-alarm clear) |
| `x_companion_extension.test.js` | 54 passed, 0 failed | 117.52ms | +1 (DOM agreement) |
| `companion_settings_automatic_analysis.test.js` | 6 passed, 0 failed | 10063.37ms | count unchanged |
| `kronika_ui.test.js` | 12 passed, 0 failed | 91.90ms | count unchanged |
| `catalog_card_ai_quick_action.test.js` | 30 passed, 0 failed | 207.28ms | count unchanged |
| Bounded non-browser glob | 213 passed, 0 failed | 759.49ms | count unchanged |
| Focused local web + public published | 225 passed | 43.84s | count unchanged |
| Full declared Python suite | 4955 passed, 8 skipped, 3 warnings | 689.72s | count unchanged |
| Retention module | 15 passed | 0.37s | count unchanged |

The three warnings are the existing `PydanticJsonSchemaWarning` on `test_health_contract_is_present_in_openapi`, `test_api_key_not_disclosed_in_health_response_openapi_or_app_repr`, and `test_database_path_absent_from_settings_repr_logs_api_and_openapi`. The eight skips are the same real-tool and NVIDIA smoke skips. The settings runner time is about 10s while its six test bodies finish in about 11ms; the count matches the baseline and the process exits 0.

`tests/browser_companion_evidence.test.js` was updated and was not executed.

## 6. Commit and retention

Commit `aee0a60a04b78685608ec5a65ec5780c7d9884e7` on `main`, parent `c152a178dcfbbe6e8f04f98d1b9f3f8cb7aea209`. Not pushed. The post-commit working tree is clean, so `git diff --stat` is empty. The commit itself is:

```text
 extension/background/service_worker.js             |  93 +++++----
 extension/content/x_adapter.js                     | 186 +++++++++---------
 extension/content/x_adapter_contract_v1.js         |  20 +-
 extension/shared/messages.js                       |  85 +++++++--
 extension/ui/picker.js                             |   9 +-
 extension/ui/review.js                             |   4 +-
 extension/ui/save.js                               |   8 +-
 extension/ui/sidebar.js                            |  43 +++--
 src/kronika/adapters/api/web/app.js                |  16 +-
 src/kronika/adapters/api/web/companion_host.js     |   8 +-
 tests/browser_companion_evidence.test.js           |   2 +-
 tests/catalog_card_ai_quick_action.test.js         |   4 +-
 tests/companion_review_extension.test.js           | 209 ++++++++++++++++----
 tests/companion_settings_automatic_analysis.test.js |   7 +-
 tests/companion_web_bridge.test.js                 |  26 ++-
 tests/contract/test_kronika_identity_retention.py  |  85 +++++++--
 tests/contract/test_local_web_application.py       |   2 +-
 tests/kronika_ui.test.js                           |   2 +-
 tests/support/x_fixtures/composer.html             |  16 +-
 tests/x_companion_extension.test.js                | 211 +++++++++++++--------
 20 files changed, 681 insertions(+), 355 deletions(-)
```

Part A was not edited. The retention module's frozen-hash assertion passed. `FROZEN_ALEMBIC_SHA256` has 36 keys. Part B's expected basename set still has 20 entries, and `test_framenest_basename_path_ledger_matches_exactly` passed.

Part C, confirmed by that same passing module. Case-insensitive `framenest`, retention file excluded:

- File counts: `src`  unchanged, `tests` 186 to 185, `extension` 8 to 2, `deploy` 22, `scripts` 11, `docs` 88 unchanged. Six extension files left the set (`service_worker.js`, `x_adapter.js`, `x_adapter_contract_v1.js`, `picker.js`, `review.js`, `save.js`). `composer.html` left the tests set.
- Occurrences: `src` 1704 to 1695 (`app.js` −8, `companion_host.js` −1). `tests` 2280 to 2190 (`x_companion_extension.test.js` −81, `composer.html` −9, `companion_web_bridge.test.js` −3, `catalog_card_ai_quick_action.test.js` −2, `companion_settings_automatic_analysis.test.js` −2, `browser_companion_evidence.test.js` −1, `test_local_web_application.py` −1, `kronika_ui.test.js` −1, `companion_review_extension.test.js` +10). `extension` 145 to 4 (`x_adapter.js` −101, contract −10, `sidebar.js` −9, `service_worker.js` −7, `messages.js` −6, `save.js` −4, `picker.js` −2, `review.js` −2). The four that remain are the API version, the review alarm, and the origin key in `messages.js`, plus the retired web protocol in `sidebar.js`. `deploy` 248, `scripts` 98, `docs` 1206 unchanged.
- `MUTATION_HEADER_OCCURRENCE_COUNT` 73 to 69, files 30 to 29. `service_worker.js` −1 and leaves the set. `companion_review_extension.test.js` −3 and stays.
- `CAPITALIZED_OCCURRENCE_COUNT` 2773 to 2681, files 399 to 389. Ten files lost their last `FrameNest`: `service_worker.js` −5, `x_adapter.js` −28, contract −1, `messages.js` −6, `picker.js` −2, `review.js` −2, `save.js` −1, `sidebar.js` −8, `companion_host.js` −1, `companion_web_bridge.test.js` −3 (57). Stayers: `app.js` −8, `companion_review_extension.test.js` −11, `x_companion_extension.test.js` −10, catalog −2, settings −2, local web −1, `kronika_ui.test.js` −1 (35).

## 7. Sites no test executes

- `picker.js` calls `completeStoredEntryMigration`, and no test evaluates that call. Picker coverage is source inspection of the shared resolver.
- The sidebar call runs inside the settings harness. That harness does not persist `set` or `remove`, so verification fails and the retired value stays. The success, conflict, reset, and failed-readback paths are asserted on the shared helper and the service worker, not on the sidebar call.
- `tests/browser_companion_evidence.test.js` now queries `[data-kronika-composer-file]`. The suite was not activated.
- `framenest-media.bin` in `x_companion_extension.test.js` remains a synthetic filename, not an operational token.

## 8. Deviations, risks, and the next step

No retired reader was removed. No Python product file, server header acceptor, document, dependency, or frozen hash was edited. `app.js` still emits both mutation headers from `framenestMutationHeaders`. `docs/X_COMPANION.md` still says the alarm name is `framenest.review-inbox`; that sentence is now behind the extension and was left because documents are outside this grant.

The worker serializes its own origin reads, configure, and reset. The sidebar and picker migrations are outside that queue. Chrome storage has no compare-and-swap, so a sidebar migration that has already read a retired-only value can write it back after a reset. The required reset test covers the worker's own sequence and does not cover that cross-realm interleaving.

Smallest next step: the Orchestrator verifies this commit, then publication and the exac00000000000000000000000000000000000000000000t-main NUC refresh are a separate grant. Rendered extension reload stays after that refresh. C7-B is after rendered acceptance. This prompt authorizes none of those.

Resolved Execution Issues / Near-Misses: the first baseline probe used `https://kronika.example.ts.net`, which fails `TS_ORIGIN_PATTERN`, and evaluated `messages.js` inside a `vm` without `URL`, so `acceptFrameNestOrigin` returned false. Both were corrected before any product failure was recorded. The corrected probe produced the failures in section 1.

Pre-Existing Failure Classification: none

```text
Orchestration critique:
MEASURED: none
LEAD: a sidebar migration that has already read a retired-only origin can write that origin back after reset, because the UI call is outside the worker origin queue; the cheapest check is one synthetic interleaving of completeStoredEntryMigration with resetState
```