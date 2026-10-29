### Report for ORCHESTRATOR_CHAT

Logical whole identity: `kronika-sole-identity`  
Worker session ordinal: `44`  
Worker exchange ordinal: `01`  
Task identity: `KSI-IMPL-C7AS`  
Status: **PASS** — local implementation, non-independent evidence  
Phase-qualified result: `not-applicable`  
Logical-whole closure: `not-closed`  
Report justification: `new-mutation`

Start commit: `e9413dff98605443e7d17557f498c87433c93e92`  
End commit: `7c1cee299e14dbccaca10fe0ce749b4dc7553420`  
AP pin: `73e20ef80b88700d5fcbc397cd8edd4fc425869f`

Exactly one non-amended commit was created on `main`. The worktree is clean. No push, publication, deployment, NUC contact, browser contact, or provider contact occurred.

**1. Implemented emission/reader matrix**

[companion_host.js](/home/agile/Projects/kronika/src/kronika/adapters/api/web/companion_host.js:13) emits the canonical protocol and exports a frozen dual-acceptance set.

Captured through the real host’s `postMessage`:

| Trigger | Outbound type | Captured `v` |
|---|---|---|
| `createHost()` → `start()` | `web_ready` | `kronika.companion.web.v1` |
| Retired `host_hello` | `host_ack` | `kronika.companion.web.v1` |
| `attach()` | `attach_request` | `kronika.companion.web.v1` |

Every captured target equals the pinned extension origin. The real extension bridge accepts all three captured messages.

| Host inbound branch | Retired spelling | Canonical spelling | Invalid protocol |
|---|---|---|---|
| `HOST_HELLO` | Accepted | Accepted | No hosted transition or acknowledgment |
| `ATTACH_RESULT` | Accepted | Accepted | Pending waiter remains intact |
| `OPEN_DETAILS` | Accepted | Accepted | No Details notification |

The shared refusal matrix contains 23 invalid values, including near-miss versions, whitespace, case changes, unknown strings, arrays, objects, and non-string primitives. Host refusal returns `undefined`; bridge refusal retains `null`/`false`.

Both valid spellings also exercise origin/source refusal, malformed messages, unknown types, listener failure containment, and Attach/Details behavior. UUID checks independently reject invalid media and location IDs. Positive controls prove refusal tests cannot pass merely because the host is inactive.

The extension remains unchanged: it accepts both spellings and emits the retired spelling. Existing live-sidebar tests cover `HOST_HELLO`, valid-request `ATTACH_RESULT`, and invalid-request `ATTACH_RESULT`; the replacement bridge test exercises the real `OPEN_DETAILS` message constructor and delivers its retired message to the host.

**2. Deleted assertions and behavioral replacements**

Both source-expression multiset assertions were deleted:

```js
assert.deepEqual(sidebarOutbound, [
  "v: WEB_PROTOCOL",
  "v: companion.PROTOCOL",
  "v: WEB_PROTOCOL",
  "v: WEB_PROTOCOL",
  "v: WEB_PROTOCOL",
]);

assert.deepEqual(hostOutbound, ["v: PROTOCOL", "v: PROTOCOL", "v: PROTOCOL"]);
```

Their regex extraction, literal-occurrence checks, and unused counting helper were also removed.

[Behavioral replacements](/home/agile/Projects/kronika/tests/companion_web_bridge.test.js:367) assert actual captured messages:

```js
assert.deepEqual(posted.map(({ message }) => message.type), [
  "web_ready", "host_ack", "attach_request",
]);
assert.equal(message.v, CURRENT_WEB_PROTOCOL);
assert.equal(targetOrigin, PIN);
assert.equal(accepted, message);
```

The extension replacement asserts its actual message:

```js
assert.equal(message.v, RETIRED_WEB_PROTOCOL);
assert.equal(message.type, "open_details");
send(message.v, message.type, message.payload);
assert.deepEqual(opened, [MEDIA_ID]);
```

Test names now describe the asymmetric transition truthfully.

**3. Served asset and public composition**

The [served-asset contract](/home/agile/Projects/kronika/tests/contract/test_local_web_application.py:262) now asserts:

```js
const PROTOCOL = "kronika.companion.web.v1";
const ACCEPTED_WEB_PROTOCOLS = Object.freeze([PROTOCOL, "framenest.companion.web.v1"]);
```

Pinned-origin and no-wildcard assertions remain unchanged.

Neither public-composition file required editing:

- `test_public_published_uds.py` checks that the host asset returns uniform 404 and that public HTML excludes its script reference.
- `public_published_api.py` uses `_INDEX_COMPANION_SCRIPT` as an exclusion marker and removes it from public HTML. Its public asset allowlist excludes the host script.

Additional consumers found beyond the prompt’s named files were `application.py`’s asset registration, `web/index.html`’s script ordering, and `web/app.js`’s hosted-state, Gallery Attach, catalog-refresh, and Details callbacks. Related coverage also exists in `catalog_card_ai_quick_action.test.js` and `kronika_ui.test.js`; both were run.

**4. Reproduction against the unchanged asset**

Before changing `companion_host.js`, the new JS expectations produced **19 passed, 8 failed** in **77.24 ms**:

- Exported emitter: retired value instead of canonical.
- `WEB_READY`, `HOST_ACK`, and `ATTACH_REQUEST`: each captured the retired value.
- Canonical `HOST_HELLO`: hosted state remained `false`.
- Canonical `ATTACH_RESULT`: result remained `undefined`.
- Canonical `OPEN_DETAILS`: callback list remained empty.
- The emission parent test additionally reported its failed subtests.

The revised served-asset test also failed as expected: **1 failed in 1.34 s**, because the canonical emitter declaration was absent.

These were deliberate negative demonstrations, not baseline-suite debt. No temporary probe files were created.

**5. Validation**

Repository identity, branch, clean baseline, AP gitlink/submodule equality, `ap doctor`, and baseline-bound `ap project check` passed.

All Python execution used the authorized AP route and starting baseline. JavaScript used ordinary `node --test` invocations.

| Suite | Result | Elapsed | Difference from supplied baseline |
|---|---:|---:|---|
| `companion_web_bridge.test.js`, final | 27 passed | 79.15 ms | +13: ten additional top-level tests and three send-site subtests |
| `companion_review_extension.test.js` | 40 passed | 178.47 ms | None |
| Bounded frontend/cockpit/Gallery group | 213 passed | 721.42 ms | None |
| `catalog_card_ai_quick_action.test.js` + `kronika_ui.test.js` | 42 passed | 212.31 ms | Additional consumer coverage |
| Focused local-web + public-published Python modules | 225 passed | 43.50 s | No supplied focused count |
| Full declared Python suite | 4,955 passed; 8 skipped; 3 warnings; 0 failed | 700.53 s | None |
| Retention module, final | 15 passed | 0.35 s | None |

An earlier green bridge run passed all 27 tests in **77.14 ms**, before strengthening same-window and independent UUID checks.

The bounded JS invocation expanded to these 18 suites, all under `tests/`:

```text
admin_batch_actions_frontend.test.js
admin_catalog_removal_frontend.test.js
admin_content_publication_frontend.test.js
ai_providers_admin_frontend.test.js
cover_frontend.test.js
movie_identification_frontend.test.js
research_settings_admin_frontend.test.js
tailscale_identity_frontend.test.js
workspace_media_frontend.test.js
x_acquisition_cockpit.test.js
youtube_acquisition_cockpit.test.js
youtube_request_cockpit.test.js
gallery_details_playback_handoff.test.js
gallery_filter_controls.test.js
gallery_gif_inline_toggle.test.js
gallery_loading_states.test.js
gallery_search_tag_filters.test.js
gallery_still_image_render.test.js
```

The eight Python skips comprise seven opt-in real-media-tool tests and one live-provider test. The three warnings report Pydantic’s non-serializable `OMITTED` default.

**6. Commit, diff, and retention**

Commit: `7c1cee299e14dbccaca10fe0ce749b4dc7553420`

```text
 src/kronika/adapters/api/web/companion_host.js    |  20 +-
 tests/companion_web_bridge.test.js                | 270 +++++++++++++++++-----
 tests/contract/test_kronika_identity_retention.py |  12 +-
 tests/contract/test_local_web_application.py      |   6 +-
 4 files changed, 235 insertions(+), 73 deletions(-)
```

Final measurements were regenerated after committing:

- Part A declarations are byte-unmoved; all **86 document hashes** and **36 parsed Alembic hashes** match.
- Part B declarations are byte-unmoved; basename membership still measures **20**.
- Part C file membership remains **516** paths.

| Tree | Matching files | Retired-name occurrences |
|---|---:|---:|
| `src` | 186 | 1706 → **1705** |
| `tests` | 186 | 2283 → **2282** |
| `deploy` | 22 | 248 |
| `scripts` | 11 | 98 |
| `docs` | 88 | 1206 |
| `extension` | 8 | 145 |

Per-file arithmetic:

- Host: **3 → 2**. The old emitter literal moves to the compatible reader, while the rewritten comment removes one retired-name occurrence.
- Bridge test: **13 → 12**. The hardcoded retired-emitter assertion disappears; behavioral tests reuse existing fixtures.
- Local-web contract: **30 → 30**. Its retired literal now identifies the compatible reader.

Only those two Part C scalars were re-pinned, after behavioral suites passed. One running ledger entry records the causes. Capitalized counts remain **2773/399 files**, environment counts **702/114 distinct/53 bare**, mutation-header counts **73/30 files**, and retired console entries **14**. Host-path and unit-account counts also remain unchanged.

Counter controls verified zero matches for a known-impossible input and two for a mixed-case positive input. Final checks confirmed the deleted multiset machinery is absent.

**7. Unexercised sites**

No changed executable protocol site lacks behavioral coverage: all three host sends and all three inbound branches are exercised. The transition comment was reviewed statically.

Rendered Gallery/Details acceptance and a real served NUC/extension pairing were not exercised; they are outside this grant. Existing extension transition comments remain untouched as required.

**8. Deviations, risks, missing evidence, and next step**

No implementation-scope deviation or missing required evidence remains. Additional verification covered the two discovered Gallery/shell suites. All extension files, mutation-header code/tests, documents, dependencies, and AP configuration remain unchanged.

Public branch state was not independently observed; this is an unpublished local candidate. Publication and exact-main NUC refresh remain prerequisites for the companion cut and rendered acceptance.

Smallest next step: Orchestrator review of this commit for C7-A/S acceptance.

**Resolved Execution Issues / Near-Misses**

Initial bulk protocol/ledger reads and verbose bounded-JS output exceeded tool display limits. Required passages were reread in bounded ranges; final inventories and terminal test summaries were captured without truncation. One empty nested-instruction search skipped a chained source read, which was then issued directly. These were inspection-method issues with no repository effect or residual evidence gap.

**Pre-Existing Failure Classification**

None. The deliberate negative demonstrations are recorded above; all required final suites passed.

This report is delivered in chat only. Submission expires all authority under this prompt.

Orchestration critique:  
MEASURED: none  
LEAD: none