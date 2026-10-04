### Report for ORCHESTRATOR_CHAT

Logical whole identity: `kronika-sole-identity`
Worker session ordinal: `12`
Worker exchange ordinal: `01`
Persistent role identity: WORKER
Worker session profile: Fresh Implementation Worker
Task identity: `KSI-IMPL-C2`
Status: **PASS**
Phase-qualified result: `not-applicable`
Logical-whole closure: `not-closed`
Report justification: `new-mutation`
Start commit: `0b7567598b6378da25d46874b7cb3f42fb1733ae`
End commit: `78c841f34b8ef33bb6a27ff2dc9323fd2f6cdfe4`
Changed files: **14** — 6 production, 8 test/ledger
NUC contact: none in this cut, by design. Published NUC state unchanged; the NUC still serves `0c850996cd2ef17dae4112733fd17fdc732f4699`.
Push: none. Branch deliberately unpublished.

## 1. Repository gate

Verified before any edit: branch `feat/kronika-identity-dual-read`, HEAD `0b75675…`, tree clean, `.ap` gitlink and submodule HEAD both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `./.ap/ap doctor` PASS with governing variant `stable`, `./.ap/ap project check --baseline 0b75675…` PASS. `ap doctor` and `project check` each warned that inherited environment classes were sanitized (`SSH_AUTH_SOCK`, `VIRTUAL_ENV_DISABLE_PROMPT`, `PATH`); both still passed, and the warning is not a failed gate.

## 2. Baselines, reproduced before editing

| Route | Baseline at `0b75675` | Final at `78c841f` |
|---|---|---|
| `./.ap/ap exec --operation test` | **4356 passed, 8 skipped, 3 warnings, 0 failed** (694.40s) | **4358 passed, 8 skipped, 3 warnings, 0 failed** (693.26s, exit 0) |
| `node --test tests/*.test.js` | **554 total, 549 passed, 0 failed, 5 skipped** | **576 total, 571 passed, 0 failed, 5 skipped** (10.19s) |
| retention module | 15 passed | 15 passed |

Both reproduce exactly as the prompt stated. Net +2 Python tests, +22 JavaScript tests. The eight Python skips are the seven real-media-tool tests and one live NVIDIA test; the five JavaScript skips are the gated browser-evidence suites, unchanged.

## 3. Exhaustive classification — 81 distinct identifier groups, all classified

Method: `git grep -o -i 'framenest[a-zA-Z0-9._-]*'` over `extension/` and `src/framenest/adapters/api/web/`, collapsed to distinct `(file, line, identifier)` groups. I re-derived the inventory rather than trusting the issued lead. **Four items in the issued inventory are wrong and one is missing** — corrections in §3.6.

### 3.1 Class 1 — the mutation header, dual-send (in scope, changed)

| Site | Line | Change |
|---|---|---|
| `src/framenest/adapters/api/web/app.js` | 434–444 | `framenestMutationHeaders` keeps its pinned `Object.assign({ "X-FrameNest-Request": "1" }, headers)` line byte-identical, then applies `merged["X-Kronika-Request"] = "1"` **after** the merge so a caller cannot weaken the gate |
| `extension/background/service_worker.js` | 6–13 | new `MUTATION_REQUEST_HEADERS` frozen constant carrying both spellings |
| same, `previewFetch` | 783 | `headers: Object.assign({}, MUTATION_REQUEST_HEADERS)` |
| same, `fetchJson` | 825 | `const headers = Object.assign({}, MUTATION_REQUEST_HEADERS)` |
| same, `transferAttach` | 953 | `headers: Object.assign({}, MUTATION_REQUEST_HEADERS)` |

Consolidating the three extension literals into one constant is what makes `MUTATION_REQUEST_HEADERS` appear exactly four times, which a test now pins.

### 3.2 Class 2 — the companion API version, dual-accept (in scope, changed)

| Site | Line | Change |
|---|---|---|
| `extension/shared/messages.js` | 8–13 | `API_VERSION = "kronika-companion.v1"`, `RETIRED_API_VERSION = "framenest-companion.v1"`, `ACCEPTED_API_VERSIONS`, new `acceptCompanionApiVersion()` |
| `extension/background/service_worker.js` | 300 | `!companion.acceptCompanionApiVersion(response.body.companion_api_version)` → `{ ok: false, error: "version_skew", disable: true }` |

Not touched, by negative authority: `src/framenest/application/companion_picker.py:30`, `src/framenest/adapters/api/x_companion_api.py:163`. This is the single authorised deviation from the accepted plan.

### 3.3 Class 3 — the internal protocol strings, atomic rename (in scope, changed)

| Identifier | Site | New |
|---|---|---|
| `framenest.companion.v1` (`PROTOCOL`) | `messages.js:8` | `kronika.companion.v1` |
| `framenest.companion.review.v1` (`REVIEW_OVERLAY.protocol`) | `messages.js:54` | `kronika.companion.review.v1` |

**Persistence check performed before renaming, as required.** `framenest.companion.v1` occurs in exactly one place, `messages.js`, and is consumed only through `isProtocolMessage`'s `value.v === PROTOCOL` and as the `v` field of `chrome.runtime` messages and ports. `framenest.companion.review.v1` occurs in exactly one place, `messages.js:49`, and is consumed by `review.js:487` `window.parent.postMessage(..., extensionOrigin())` and `acceptReviewOverlayMessage` in `sidebar.js:945`. `review.html` is loaded in the `#review-frame` iframe inside `sidebar.html` (verified in `sidebar.html:88`), so both ends are the extension's own origin. Neither string appears in any `chrome.storage`, `localStorage` or `sessionStorage` call, and neither crosses the extension boundary. No fallback was needed and none was added. Consumers in `sidebar.js`, `review.js`, `x_adapter.js`, `save.js`, `picker.js` and `service_worker.js` reference the constants, not literals, so no consumer file changed.

### 3.4 Class 4 — persisted keys, migrate on read (in scope, changed)

| Retired name | Current name | Store | Read sites | Write site | Consume/clear site |
|---|---|---|---|---|---|
| `frameNestOrigin` | `kronikaOrigin` | `chrome.storage.local` | `service_worker.js` 180, 424; `picker.js` 325; `sidebar.js` 1059 | `service_worker.js` 173 | `service_worker.js` 195 (reset) |
| `framenest.review-inbox` | `kronika.review-inbox` | `chrome.alarms` | `service_worker.js` 69 (`onAlarm`) | `service_worker.js` 452 (`create`) | `service_worker.js` 473–483 |
| `framenest.youtube.currentClaim.v1` | `kronika.youtube.currentClaim.v1` | **`sessionStorage`** | `app.js` 1160 | `app.js` 1142 | `app.js` 1151 |
| `framenest.upload.recovery.v1` | `kronika.upload.recovery.v1` | `localStorage` | `app.js` 3079 | `app.js` 3071 | `app.js` 2740 |
| `framenest.catalog.pageSize` | `kronika.catalog.pageSize` | `localStorage` | `app.js` 631 | `app.js` 10084 | none |

Shared resolver added to `messages.js` (`STORAGE.origin`, `storageKeyRequest`, `storageValue`, `storageChangeFor`), used by the service worker, the picker and the side panel so all three read sites share one implementation. `picker.js` also had to watch **both** key names in `chrome.storage.onChanged`, because the worker's write now lands on the current name; `storageChangeFor` does that. In `app.js` the mirror helpers are `readMigratedStorageItem` and `clearMigratedStorageItem`.

`STORAGE_KEYS` in the worker now carries `retiredOrigin` alongside `origin`, so the pre-existing `chrome.storage.local.remove(Object.values(STORAGE_KEYS))` in `resetState` removes both spellings without a second call.

**One rule refinement I had to make, and why.** Class 4 says leave the retired entry in place. For the three *consume* paths that is not merely undesirable, it is a defect: `clearYouTubeClaimRecovery`, `clearUploadRecovery` and `clearReviewInboxAlarmAndBadge` exist to mark a record consumed. If a consume removed only the current key, the fallback read would resurrect the retired entry on the next load — a consumed YouTube claim would be recovered forever, and a dead upload would be restored. So consume removes **both** spellings. That is the existing feature's semantics applied to both names, not a migration, and it is the only deletion in the cut. I flag it explicitly because it is the one place I read past the literal wording of the rule.

### 3.5 Class 5 — cosmetic and mirrored identifiers (out of scope, untouched)

Verified byte-identical by comparing the occurrence multiset of every Class 5 token at `0b75675` against `78c841f`:

| Identifier | Sites | Result |
|---|---|---|
| `framenest-media.bin` | `service_worker.js` ×2, `sidebar.js` ×1, `picker.js` ×1, `x_adapter.js` ×1 | identical |
| `framenest-attach` (port name) | `service_worker.js` ×2, `x_adapter.js` ×8 | identical |
| manifest `name`, `description`, `action.default_title` | `manifest.json` | identical |
| `EXTENSION_CONTEXT_RECOVERY_COPY` | `messages.js` | identical |
| all `data-framenest-*` CSS/DOM hooks | `x_adapter.js`, `x_adapter_contract_v1.js`, `save.js` | files not in the diff at all |
| `PINNED_EXTENSION_ORIGIN` | `companion_host.js` | identical |

`extension/content/x_adapter.js`, `extension/content/x_adapter_contract_v1.js`, `extension/ui/review.js`, `extension/ui/save.js`, every `.css`, every `.html` and `src/framenest/adapters/api/web/companion_host.js` are **absent from `git diff --name-only`**. `review.js` and `save.js` were in my positive authority and my classification found nothing in them that must change, so I left them untouched rather than editing for symmetry.

### 3.6 Corrections to the issued inventory

Four of the issued lead's parentheticals are wrong. None changes the scope; all are reported because the next cut will rely on this list.

1. **`framenest.youtube.currentClaim.v1` is `sessionStorage`, not `localStorage`.** `youtubeClaimStorage()` at `app.js:1132` returns `window.sessionStorage`. Lower stakes than the issue implied: the key does not survive a browser restart.
2. **`framenest.companion.v1` is not a `chrome.storage` key.** It is the `PROTOCOL` constant, used only in runtime messages and ports. The rename is therefore genuinely atomic, which is what §3.3 verified.
3. **`framenest.companion.review.v1` is not a `chrome.storage` key either.** It is an intra-bundle `postMessage` protocol string. Same consequence: Class 3, renamed atomically.
4. **`framenest-companion.v1` is not a port name.** It occurs in exactly one place, `messages.js`, as `API_VERSION` — which is precisely the validated cross-boundary contract the Orchestrator's own verification section identified. The only port name in the bundle is `framenest-attach`.
5. **Missing from the inventory: `framenest.review-inbox` is a `chrome.alarms` name, not `chrome.storage`.** It is persisted browser state, so Class 4 applies, but the storage semantics differ: there is no `get`/`set`, only `create`/`clear` and name matching in `onAlarm`.

**Found but not in the issued inventory at all:** the web shell already carried a Kronika-branded persisted key at baseline. `app.js:13406` has `KRONIKA_ATTEMPT_KEY = "kronika.research.attempt.v1"` in `sessionStorage`, inside a `/* KRONIKA_SHELL_START */` block, with 19 pre-existing `KRONIKA_` identifiers. The Research Cockpit was already named. I matched that file's existing `KRONIKA_*` constant convention for the three new keys. No migration is needed for `KRONIKA_ATTEMPT_KEY`; it is already current.

### 3.7 Newly discovered cross-boundary contract — deferred, needs a decision

`framenest.companion.web.v1` is **not** an internal protocol string. It is a validated cross-boundary `postMessage` contract:

- `src/framenest/adapters/api/web/companion_host.js:8` defines `PROTOCOL` and gates on `data.v !== PROTOCOL` at line 75, replying with `host_ack` at 80 and `attach_request` at 121. That file is served by the NUC.
- `extension/ui/sidebar.js:3` defines its own `WEB_PROTOCOL`, gates on it at line 28, and sends it at 127, 884, 980, 994.
- `tests/companion_web_bridge.test.js:47` and `tests/companion_review_extension.test.js:1495` pin the literal on both sides, and `tests/contract/test_local_web_application.py:267` pins it in the served asset.

If the extension renamed its copy alone, `companion_host.js` would never see `host_hello`, `hosted` would stay `false`, `attach()` would return `{ ok: false, error: "not_hosted" }` and the meme-attach composer control would silently stop working — against any NUC that had not also been refreshed. This is the same hazard class as the API version, and `companion_host.js` is outside this cut's edit authority.

**I changed nothing.** It belongs in the same paired decision the Cooperator already made for the API version, and that decision needs to cover both strings at once. This is the single most important finding for the next Orchestrator.

## 4. Exact diff of every path

`git diff --stat 0b75675..78c841f`:

| Path | ± | Purpose |
|---|---|---|
| `extension/shared/messages.js` | +70 −5 | Class 2 version accept set; Class 3 both protocol renames; Class 4 alarm names, `STORAGE`, and the three resolver helpers; all exported |
| `extension/background/service_worker.js` | +49 −7 | Class 1 shared header constant at three sites; Class 2 accept call; Class 4 origin read/write/reset, dual alarm name on create, listen and clear |
| `extension/ui/picker.js` | +12 −6 | Class 4 origin read through the shared resolver; `onChanged` watches both spellings |
| `extension/ui/sidebar.js` | +4 −4 | Class 4 origin read through the shared resolver |
| `extension/manifest.json` | +1 −1 | `version` `0.1.0` → `0.2.0`, nothing else |
| `src/framenest/adapters/api/web/app.js` | +54 −8 | Class 1 dual-send in the shared helper; Class 4 three key pairs plus `readMigratedStorageItem` and `clearMigratedStorageItem` |
| `tests/companion_review_extension.test.js` | +310 | 9 new tests; harness extended additively (companion-media branch, media response with `arrayBuffer`/`getReader`, `chrome.tabs.connect` port stub, captured `onMessage` listener, `btoa`) |
| `tests/x_companion_extension.test.js` | +61 | 3 new tests |
| `tests/tailscale_identity_frontend.test.js` | +75 | 2 new tests |
| `tests/upload_cockpit_async_ownership.test.js` | +96 | 2 new tests, plus one assertion repointed at the current write target |
| `tests/youtube_acquisition_cockpit.test.js` | +84 | 2 new tests, existing recovery test updated for the migration |
| `tests/gallery_filter_controls.test.js` | +39 | 1 new test |
| `tests/contract/test_local_web_application.py` | +72 | 2 new tests; 1 existing assertion updated |
| `tests/contract/test_kronika_identity_retention.py` | +40 −12 | 4 Part C scalars re-pinned with causes |

Every changed path is inside the granted set. `git diff --name-only` shows no path outside it.

**Two pre-existing tests had to be repointed**, because they asserted the exact behaviour this cut changes by design. `tests/contract/test_local_web_application.py:2762` pinned `window.localStorage.setItem(UPLOAD_RECOVERY_STORAGE_KEY` and the matching `getItem`; it now pins the current constant and asserts the retired one is *not* a write or read target. `tests/upload_cockpit_async_ownership.test.js` read the persisted recovery through the retired key at one observation point; it now reads the current key. Both edits widen the assertion rather than weaken it.

## 5. Named tests per behaviour, each demonstrated failing

Every violation was applied to the working tree, the focused test run, and the file restored from a `/tmp` copy. No Git write other than the final commit.

| # | Test | Violation applied | Result |
|---|---|---|---|
| 1 | `Class 1: every extension send site carries both mutation header spellings` | drop `"X-Kronika-Request"` from the shared constant | **failed** |
| 2 | `Class 1: the web shell mutation helper injects both header spellings` | delete `merged["X-Kronika-Request"] = "1";` | **failed** |
| 2p | `test_served_shell_sends_both_mutation_header_spellings` | same, at the served-asset boundary | **failed** (`0 == 1` for the current literal) |
| 3 | `Class 2: the retired companion API version is accepted` | accept only the current version | **failed** |
| 4 | `Class 2: the current companion API version is accepted` | accept only the retired version | **failed** |
| 5 | `Class 2: any other companion API version still disables the picker` | accept any string containing `companion` | **failed** (6 cases: two near-miss versions, empty, null, undefined, number) |
| 6 | `Class 3: the internal protocol names carry the current spelling and no retired copy` | revert `PROTOCOL` | **failed** |
| 6b | same | revert `REVIEW_OVERLAY.protocol` | **failed** |
| 7 | `Class 4: the origin key is read from the retired spelling only when the current one is absent` | remove the retired fallback | **failed** |
| 7b | `Class 4: the shared origin resolver takes the current key, then the retired key, then nothing` | remove the retired fallback | **failed** |
| 8 | same | delete the current-key branch so the retired key wins | **failed** |
| 9 | `Class 4: configuring the origin writes the current key and leaves the retired key untouched` | write to the retired key | **failed** |
| 10 | `Class 4: an explicit reset removes the retired origin and the retired alarm` | reset removes only the current key | **failed** |
| 11 | `Class 4: the review-inbox alarm … the retired name still refreshes` | listen only for the current alarm name | **failed** |
| 12 | `Class 4: the picker and the side panel both read the origin through the shared resolver` | picker reads only the current key | **failed** |
| 13 | `Class 4: the catalog page-size key reads the retired spelling only when the current one is absent` | drop the web-shell fallback | **failed** |
| 14 | `Class 4: upload recovery reads the retired key only when the current key is absent` | drop the fallback | **failed** |
| 14b | `Class 4: a rejected recovery removes both spellings so the fallback cannot resurrect it` | drop the fallback | **failed** |
| 15 | same | consume removes only the current key | **failed** |
| 16 | `Class 4: upload recovery writes the current key and leaves the retired key untouched` | write back to the retired key | **failed** |
| 17 | `test_served_shell_persisted_keys_…` | a retired key becomes a write target | **failed** |
| 18 | `claim recovery reads the retired session key only when the current key is absent` and `… write creates the current key …` | web-shell fallback removed / write to the retired key | **failed** |
| 19 | `Extension version is at least the dual-send revision so a reload is observable` | revert to `0.1.0` | **failed** |

Two demonstrations initially did **not** fail, and both were real:

- My first attempt at the Class 2 "anything else" violation added `kronika-companion.v2` to the accept set, which is not a value the test probes. The violation was untested, not the test. Redone with three genuine violations (rows 3–5), which all fail.
- My first reset test passed under a violation. Cause: I had added `retiredOrigin` to `STORAGE_KEYS`, so `Object.values(STORAGE_KEYS)` already covered both spellings and my extra `.concat(RETIRED_STORAGE_KEYS)` was dead code. I removed the redundancy and redid the violation against the real removal list (row 10), which fails.

Also worth recording: while strengthening the upload write test I found that `resetUploadForFile` calls `clearUploadRecovery`, so a harness using `setActiveUpload` cannot observe "write leaves the retired key untouched" — the clear legitimately removes both first. The test now drives `saveUploadRecovery` directly.

## 6. Order-independence, demonstrated against a modelled pre-C1 server

Two tests model the gate from `tailscale_ingress` at both revisions and assert the **actual header object the production code produces**:

- `Order independence: both spellings are authorised by the pre-C1 gate and by the C1 gate` (`companion_review_extension.test.js`)
- `Order independence: the shell request is authorised by the pre-C1 gate and by the C1 gate` (`tailscale_identity_frontend.test.js`), which runs the real extracted `framenestMutationHeaders`

`preC1Gate` compares only its own spelling and ignores an unknown header. `c1Gate` accepts either spelling and requires every present spelling to be `1`. Both tests assert the produced request is authorised under each, that a pre-cut single-spelling sender stays authorised under both, and that the two gates agree on this request. The pre-C1 shape comes from the C1 cut's own description of the change in `test_kronika_mutation_header.py` and from the Orchestrator's finding that the current server "compares only its own spelling and ignores the extra header".

## 7. Ledger discipline

**`EXPECTED_FRAMENEST_CONTENT_PATHS` did not move.** `test_framenest_content_path_ledger_matches_exactly` passed untouched at every point. This constrained where tests could go: a new test file containing a `framenest` literal would have forced the set to grow, so **every new test was added to an existing file already in the set** rather than to a new one. Every file I touched still carries the brand, as expected.

Part A and Part B did not move — not touched, and they pass.

Four Part C scalars moved. Each is re-pinned with its cause recorded in a comment beside the value.

| Scalar | Was | Now | Exact cause |
|---|---|---|---|
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["extension"]` | 199 | **189** | `service_worker.js` −3 (inline `frameNestOrigin` → `companion.STORAGE.origin`; three inline header literals → one constant); `messages.js` −1 (both protocol literals became `kronika.*`, while `framenest-companion.v1` and `framenest.review-inbox` each survive once as the retained spelling); `picker.js` −4; `sidebar.js` −2 |
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["tests"]` | 4446 | **4505** | +59, all new assertions naming the retired spellings they pin: companion_review +27, tailscale_identity +13, x_companion +10, test_local_web_application +7, gallery_filter +3, youtube_acquisition −1 (its vm preamble now reuses the shared constant instead of repeating the literal) |
| `MUTATION_HEADER_OCCURRENCE_COUNT` | 59 | **73** | −2 from the extension consolidation, +9 `tailscale_identity_frontend`, +5 `companion_review_extension`, +2 `test_local_web_application` |
| `MUTATION_HEADER_FILE_COUNT` | 29 | **30** | `test_local_web_application.py` names the header for the first time |
| `CAPITALIZED_OCCURRENCE_COUNT` | 3381 | **3396** | −2 from the worker, +17 across the same four test files |

`PER_TREE_FRAMENEST_FILE_COUNT` (255/321/19/7/88/12), `CAPITALIZED_FILE_COUNT` (482), `ENV_PREFIX_*`, `HOST_PATH_*`, `UNIT_ACCOUNT_*` and `CONSOLE_SCRIPT_ENTRY_COUNT` are all unmoved and verified unmoved by independent count. No name and no test was contorted to hold a counter.

**One correction to the prompt's expectation.** The prompt anticipated that "Part C scalars will move, because new `kronika.` strings appear". No Part C scalar counts `kronika`, so new `kronika.` strings cannot move any of them. Every movement above is caused by `framenest`/`FrameNest` text that my own tests and code add or remove. The prediction was wrong in mechanism, right in outcome.

I also re-pinned once mid-task after adding further tests, which briefly left the ledger red on a full run (`3 failed, 4355 passed`). That was my sequencing error, not a pre-existing failure: I had pinned before the test set was final. Re-pinned from measurement, not from the failure output, and the final full run is green.

## 8. Class 5 byte-identity confirmation

Every check in §3.5 returned `IDENTICAL`. No `.css` file and no `.html` file appears in `git diff --name-only`. The four Class 5 identifier families the issue flagged as most tempting — CSS/DOM hooks, the mirrored download filename, the manifest display name, the recovery prose — are all unchanged, as is the intra-bundle port name.

## 9. Branch and commits

Branch `feat/kronika-identity-dual-read`, one new local commit, no push, no new branch.

```
18c357cf6f8c5ff9cc3b2c28e638510fc73a3672  docs: record the Kronika sole identity in ADR-0085   (pre-C1 reference, not on this branch)
90c93eac94171182039a76fbb1c956e42b44da2c  feat(identity): read both KRONIKA_ and FRAMENEST_ spellings, write only the old
c02c6753694d5d4958045bb79f80b5eb94b9c75c  fix(identity): exit 2 on an identity-environment conflict at every entry point
24bea56daca28603d81cac8d7ed7e3888ba90671  fix(identity): restore pre-cut process-environment parity for old spellings
02a80485206eeeb33c43393d25514a30d7fe297f  docs(identity): state the resolver's measured precedence and per-channel conflict rule
0b7567598b6378da25d46874b7cb3f42fb1733ae  test(retention): pin the content-path membership set so a partial rename fails
78c841f34b8ef33bb6a27ff2dc9323fd2f6cdfe4  feat(companion): send both mutation headers and migrate browser keys on read
```

Seven commits now sit on this branch; the issue said six, counting only through `0b75675`. My commit is the seventh. Post-commit `./.ap/ap project check --baseline 78c841f…`: **PASS**. Tree clean.

## 10. The Cooperator-visible step, stated accurately

After this cut is published and the NUC is refreshed through the routine release update, Michal reloads the Brave companion, including an open side panel, so the running extension is this revision. `chrome://extensions` must then show **version 0.2.0**.

**This reload cannot be verified by observed behaviour before the removal cut.** Both header spellings are accepted by the pre-C1 server and by the C1 server, so a successful save proves nothing about which extension is loaded — the pre-cut extension also succeeds. The picker also keeps working against either API version. Its only verification is the manifest version visible in the browser. I am not claiming a behavioural proof exists, and the routine NUC refresh does not create one.

## 11. Recommendation for the deferred Class 5 items

Defer all of Class 5 to the removal cut as instructed; none was changed. My recommendations when that cut is granted:

- **CSS and DOM hooks (`data-framenest-*`, `framenest-composer*`, `framenest-companion*`, `framenest-save*`, `framenest-attach*`, `framenest-post*`, `framenestSaveKind`, `framenest-reload-notice`).** Rename them, but only with a paired style-rule edit in the same commit and with rendered acceptance afterwards. They are pure intra-bundle hooks with no server counterpart, so the risk is purely visual regression. Note that `x_adapter.js` carries 32 `framenest-companion` occurrences across ~20 selector and attribute sites — this is the largest single rename in the whole and deserves its own bounded cut with the Cooperator looking at the composer, not a footnote inside C7.
- **Mirrored `framenest-media.bin`.** Rename to `kronika-media.bin`. User-visible only in the download fallback that fires when `content-length` is unusable; the normal path takes the server's own `Content-Disposition` filename. Low risk, but it is a filename the Cooperator has seen, so it belongs to him rather than to a rename sweep.
- **Manifest display name, description, action title, and `EXTENSION_CONTEXT_RECOVERY_COPY`.** These are Cooperator-facing wording decisions, not engineering. They need his explicit choice, and the manifest `name` in particular appears in Brave's extension list and in the side-panel header. Do not fold them into a mechanical cut.

## 12. Deviations, risks, missing evidence

**Deviations from the issued prompt, all deliberate:**

1. **Added `extension/ui/picker.js` and `extension/ui/sidebar.js` to the changed set.** The issue's inventory listed them but the explicit edit list named only `sidebar.js`, `review.js`, `picker.js` and `save.js` under `extension/ui/`, and both files are covered by "any additional file under `extension/` that your exhaustive classification shows must change, each reported explicitly". `picker.js` and `sidebar.js` are named here explicitly. `review.js` and `save.js` needed no change and were not touched.
2. **Modified two pre-existing test assertions and one pre-existing test body** (§4), where they pinned the exact write target this cut moves by design.
3. **Added an additive extension to the `companion_review_extension` test harness** and `btoa` to its worker context, both inert unless a new test asks for them. All 27 pre-existing tests in that file passed unchanged after each addition.
4. **Consume paths delete both spellings** (§3.4), a deliberate reading of Class 4.
5. **Did not touch `framenest.companion.web.v1`** despite it being a genuine internal/protocol-looking string, because it is cross-boundary and its web-shell side is outside this cut.

**Risks and residual exposure:**

- **The `framenest.companion.web.v1` ordering constraint is now a known, unrecorded dependency.** Nothing breaks today because neither side changed. But the next person to touch that string may not know it is cross-boundary. It is recorded in my commit message and reported here; it deserves a line in ADR-0085's frozen-residue list or in the removal cut's prompt.
- **The dual-accept on the API version is permanent until the removal cut.** If the removal cut ships while an old extension is still loaded, that extension will disable the picker against a new server. That is the intended fail-closed direction and is why the reload confirmation is a removal-cut precondition.
- **A dual alarm name means a possible duplicate badge poll.** After this cut both `kronika.review-inbox` and the left-in-place `framenest.review-inbox` exist, and `onAlarm` honours both, so the inbox can be fetched twice per minute until the retired alarm is cleared. I chose this over clearing the retired alarm because Class 4 forbids deletion and the negative authority forbids destructive migration. Cost is one extra GET per minute; the effect is idempotent. **The removal cut should clear the retired alarm**, and that is the one cleanup this cut could not perform.
- **The dual-alarm and dual-key state accumulates in the Cooperator's real profile.** By design and bounded: two extra `chrome.storage` entries and one extra alarm, all inert, all removable in the removal cut. Nothing pre-existing is lost.

**Missing evidence, stated plainly:**

- No browser was opened and no real profile was touched, per the prompt's browser authority. All extension behaviour is proven against synthetic in-memory storage under `node --test`. The Cooperator's actual existing `frameNestOrigin`, in-flight upload recovery and alarm state are **not** exercised here — only equivalents.
- `transferAttach` had never been executed functionally before this cut; it was only source-asserted. I added the `chrome.tabs.connect` and `getReader` stubs so its header is now proven functionally too, but its full streaming path is still only as covered as those stubs make it.
- No NUC contact, no deployment, no read-only status observation. The NUC still serves `0c850996…`, which predates C1 entirely.
- Scratch files remain under `/tmp/opencode` (violation backups, a probe script, suite logs). The client denies `rm`, and they are outside the repository. Nothing in the worktree or the commit depends on them.

## 13. Smallest next step

Put the `framenest.companion.web.v1` decision to the Cooperator in the same question that covers the already-agreed dual-accept of the companion API version: either the extension dual-accepts that protocol string as well, keeping the NUC-served `companion_host.js` as the only writer of the retired spelling, or the rename is deferred to the removal cut and lands on both sides at once. Do not let a later cut rename the sidebar's `WEB_PROTOCOL` unilaterally — that silently breaks meme attach against any NUC that has not been refreshed.

## Resolved Execution Issues / Near-Misses

- **A first Class 2 violation demonstration did not fail.** I widened the accepted-version set to a value my test did not probe, so the run stayed green. Cause: I picked a violation from imagination instead of from the test's own case list. Resolution: replaced it with three violations drawn from the tested cases (drop-retired, drop-current, accept-anything-companion-shaped); all three fail. Residual risk: none, but it is a reminder that a green violation run means the violation was untested, not that the behaviour is pinned.
- **A first reset demonstration did not fail, and exposed dead code.** `STORAGE_KEYS` already contained `retiredOrigin`, so the `.concat(RETIRED_STORAGE_KEYS)` I had added was unreachable as a behaviour change. Resolution: deleted the redundant constant and the redundant `.concat`, and re-aimed the violation at the real removal list. Residual risk: none.
- **The ledger went red on a full Python run because I re-pinned before the test set was final** (`3 failed, 4355 passed`). Resolution: re-measured each scalar with independent `git grep` counting and re-pinned from measurement. Residual risk: none; the lesson is that the pin is only valid once no further test will be added.
- **My first upload write test could not observe its own invariant**, because `setActiveUpload` routes through `resetUploadForFile` → `clearUploadRecovery`, which legitimately removes both spellings first. Resolution: the test now drives `saveUploadRecovery` directly. Residual risk: none.
- **Two harness gaps surfaced as confusing failures rather than clear ones**: the worker vm context lacked `btoa`, so `previewFetch` returned `network_failed`; and `assert.deepEqual` rejects objects created in a `vm` realm because their prototype differs. Resolution: added `btoa` to the context and switched the assertion to field-by-field. Residual risk: none, but `deepEqual` against vm-realm objects will bite again in this suite.
- **My classification contradicted four parentheticals in the issued inventory**, and in each case the issued classification would have produced a wrong or unsafe edit — in particular treating `framenest-companion.v1` as a port name rather than the validated API-version contract. Resolution: re-derived the whole inventory and reported the corrections in §3.6. Residual risk: the issued inventory is a lead only; the next cut should re-derive rather than inherit it.

## Pre-Existing Failure Classification

none. Both baselines reproduced exactly as stated before any edit, and no failure observed during the task was pre-existing. The three ledger failures in the mid-task full run were caused by my own out-of-sequence re-pin and are classified under Resolved Execution Issues.

Orchestration critique:
MEASURED: `framenest.companion.web.v1` is a validated cross-boundary contract, not an internal protocol string, and the plan's C2 inventory files it under chrome.storage. Evidence: `src/framenest/adapters/api/web/companion_host.js:8,75,80,121` defines and gates on it while `extension/ui/sidebar.js:3,28,127,884,980,994` defines and gates on its own copy; `tests/companion_web_bridge.test.js:47` and `tests/contract/test_local_web_application.py:267` pin the literal on both sides; a unilateral extension rename leaves `hosted` false and `attach()` returning `not_hosted`. Effect: meme attach to the X composer breaks against any NUC that has not been refreshed, with no error the Cooperator would notice. Smallest correction: decide `framenest.companion.web.v1` in the same Cooperator question that settled the API version, before any cut touches it, and record it in ADR-0085's frozen-residue list.
LEAD: the issued inventory's parentheticals are unreliable in at least four places and its file-count framing may hide further misclassifications. Evidence: `framenest-companion.v1` is filed as a port name but is the API version; `framenest.youtube.currentClaim.v1` is filed as localStorage but is sessionStorage; `framenest.companion.v1` and `framenest.companion.review.v1` are filed as chrome.storage keys but are message protocols; and the already-Kronika `KRONIKA_ATTEMPT_KEY = "kronika.research.attempt.v1"` is absent entirely. Effect: a later cut could apply a destructive or unilateral change by trusting a label. Smallest useful check: have the Orchestrator re-derive the C3, C4, C5 and C7 inventories from `git grep` before issuing those grants, rather than carrying the plan's lists forward.