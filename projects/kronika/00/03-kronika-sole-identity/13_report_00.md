### Report for ORCHESTRATOR_CHAT

Client-surface disclosure: this client emits short progress/status lines to the terminal while I work, so the report is not the first text of the session. Nothing precedes this line inside the report itself.

Logical whole identity: kronika-sole-identity
Worker session ordinal: 13
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-05 — dual-accept the companion web protocol, and record the ordering constraint at both sites
status: PASS
Phase-qualified result: not-applicable
Start commit: 78c841f34b8ef33bb6a27ff2dc9323fd2f6cdfe4
End commit: 9c71bfb0a06cb30c5d747816e9067f6a25350c58
Report justification: new-mutation
Logical-whole closure: not-closed

## 1. Gate before editing

Branch `feat/kronika-identity-dual-read`, HEAD `78c841f34b8ef33bb6a27ff2dc9323fd2f6cdfe4`, tree clean, `.ap` gitlink and submodule HEAD both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `ap doctor: PASS` (governing variant `stable`), `ap project check --baseline 78c841f: PASS`. Public `main` = `18c357cf6f8c5ff9cc3b2c28e638510fc73a3672`, unchanged by me; the branch is absent from `git ls-remote --heads origin`, so it remains deliberately unpublished.

## 2. Exact diff of every path

`git diff --stat 78c841f..HEAD`:

| Path | ± | Purpose |
|---|---|---|
| `extension/ui/sidebar.js` | +24 −1 | ordering-constraint comment; `CURRENT_WEB_PROTOCOL` + `ACCEPTED_WEB_PROTOCOLS`; `acceptCompanionWebProtocol`; receive gate widened; three additive bridge exports |
| `src/framenest/adapters/api/web/companion_host.js` | +9 −0 | **comment only** |
| `tests/companion_web_bridge.test.js` | +121 −1 | 4 new tests; `loadSidebarBridge` split so a new test can reach `FrameNestReviewInbox` |
| `tests/companion_review_extension.test.js` | +130 −1 | 1 new end-to-end test; `loadSidebarShell` extended additively and opt-in |
| `tests/contract/test_kronika_identity_retention.py` | +14 −7 | 4 Part C scalars re-pinned with causes |

No path outside the granted set. `extension/shared/messages.js` was **not** touched (see §7). No ADR, `docs/**`, root Markdown, `deploy/**`, `pyproject.toml`, `ap.project.conf`, `manifest.json`, `src/kronika_capture/**` or Alembic revision is in the diff.

`extension/ui/sidebar.js`, the only changed logic:

```diff
+  // The companion web protocol below is a validated cross-boundary contract,
+  // not an internal identifier: the companion host served by the NUC gates on
+  // it as well, so renaming it on one side only would leave that host never
+  // seeing `host_hello`, keep it unhosted and make attach() answer
+  // "not_hosted", which breaks meme attach silently against every NUC that has
+  // not been refreshed. The receive side therefore accepts both spellings,
+  // while every send site below keeps emitting the retired
+  // `framenest.companion.web.v1` on purpose, because the host gates on exactly
+  // that spelling. The rename lands in the removal cut, on both sides at once.
   const WEB_PROTOCOL = "framenest.companion.web.v1";
+  const CURRENT_WEB_PROTOCOL = "kronika.companion.web.v1";
+  const ACCEPTED_WEB_PROTOCOLS = Object.freeze([WEB_PROTOCOL, CURRENT_WEB_PROTOCOL]);
   const WEB_TYPES = Object.freeze({
@@
+  function acceptCompanionWebProtocol(value) {
+    return ACCEPTED_WEB_PROTOCOLS.indexOf(value) !== -1;
+  }
+
   function acceptIncomingWebMessage(event, iframeWindow, storedOrigin) {
@@
-    if (!data || typeof data !== "object" || data.v !== WEB_PROTOCOL || typeof data.type !== "string") {
+    if (
+      !data ||
+      typeof data !== "object" ||
+      !acceptCompanionWebProtocol(data.v) ||
+      typeof data.type !== "string"
+    ) {
       return null;
     }
     return data;
@@
   globalThis.FrameNestSidebarBridge = {
     WEB_PROTOCOL,
+    CURRENT_WEB_PROTOCOL,
+    ACCEPTED_WEB_PROTOCOLS,
+    acceptCompanionWebProtocol,
     WEB_TYPES,
```

The four emit sites are untouched and still read `v: WEB_PROTOCOL` (now lines 150, 907, 1003, 1017); line 502 remains `v: companion.PROTOCOL` for the runtime message. The refusal shape, the `null` return and the surrounding origin/source/typeof gating are unchanged.

## 3. The three acceptance cases, each demonstrated failing

Focused runs after each violation: `node --test tests/companion_web_bridge.test.js tests/companion_review_extension.test.js`.

| # | Test | Violation applied | Result |
|---|---|---|---|
|1 | `the extension accepts the retired companion web protocol the NUC host still emits` | accept set reduced to `[CURRENT_WEB_PROTOCOL]` | **failed** |
| 2 | `the extension also accepts the current companion web protocol spelling` | accept set reduced to `[WEB_PROTOCOL]` | **failed** |
| 3 | `any other companion web protocol spelling is refused with the existing shape` | accept anything whose string contains `companion` | **failed** |

Exact outcomes:

- Violation A `[CURRENT_WEB_PROTOCOL]`: `ℹ fail 3` — the case-1 test, the end-to-end test, **and the pre-existing** `shell accepts only the framed stored origin and UUID attach ids`, which pins the retired spelling as the accepted one.
- Violation B `[WEB_PROTOCOL]`: `ℹ fail 3` — the case-2 test, the end-to-end test, **and the case-1 test**, whose `ACCEPTED_WEB_PROTOCOLS` multiset assertion catches the dropped spelling.
- Violation C substring accept: `ℹ fail 2` — the refusal test (16 probed values: two near-miss `v2` versions, three other `framenest.*` protocol strings, a bare `companion.web.v1`, a trailing-space and a leading-space variant, an uppercase variant, `""`, `null`, `undefined`, `1`, `true`, an array and an object) and the end-to-end refusal loop.

Every violation was reverted immediately and the tree restored; the final committed state was re-verified green.

## 4. The emit-spelling test, demonstrated failing

`the extension and the NUC host both keep emitting the retired web protocol` in `tests/companion_web_bridge.test.js` pins:

- the exact multiset of every outbound protocol expression — sidebar `["v: WEB_PROTOCOL", "v: companion.PROTOCOL", "v: WEB_PROTOCOL", "v: WEB_PROTOCOL", "v: WEB_PROTOCOL"]`, host `["v: PROTOCOL", "v: PROTOCOL", "v: PROTOCOL"]`;
- `countOccurrences(sidebarSource, "kronika.companion.web.v1") === 1` and `countOccurrences(hostSource, "kronika.companion.web.v1") === 0`, so the current spelling exists only as the constant the receive set reads;
- behaviourally, `FrameNestReviewInbox.openDetailsMessage(uuid).v === "framenest.companion.web.v1"`.

Violation D — a single well-meaning edit, line 1003 `postToFrame({ v: CURRENT_WEB_PROTOCOL, … })` — produced `ℹ fail 2`, with the diff naming the exact site:

```
    [
 'v: WEB_PROTOCOL',
      'v: companion.PROTOCOL',
      'v: WEB_PROTOCOL',
+   'v: CURRENT_WEB_PROTOCOL',
      'v: WEB_PROTOCOL',
-   'v: WEB_PROTOCOL'
```

and the end-to-end test failing on `hello[0].message.v` as well. The edit was reverted; all four sites verified back on `WEB_PROTOCOL`.

`tests/companion_review_extension.test.js` adds the stronger end-to-end proof through the sidebar's own registered `window` message listener, with synthetic in-memory messages only: a `web_ready` in the retired spelling yields exactly one `host_hello` carrying the retired spelling to the pinned origin; a `web_ready` in the current spelling is accepted and still answered with the retired spelling; `host_ack` posts nothing; `attach_request` with a non-UUID yields `attach_result {ok:false, error:"invalid_attach"}` carrying the retired spelling; a full `attach_request` round trip yields `attach_result {ok:false, error:"composer_unbound"}` carrying the retired spelling; and each of eight non-spelling values is refused with nothing posted at all.

## 5. Comment-only proof for `companion_host.js`

`git diff -U0` on that file is a single hunk `@@ -7,0 +8,9 @@`: a pure insertion. Removed lines: **0**. Added lines that do not begin with `  // `: **0** (verified by `grep -vc "^  // "` over added lines → 0 non-comment lines; the count of 9 printed is all-comment lines). The gate at line 75, the emit sites at 80/121/135 and `PINNED_EXTENSION_ORIGIN` are byte-identical. `tests/contract/test_local_web_application.py:267` (`assert "framenest.companion.web.v1" in body`) was **not** edited and passes.

## 6. Exact comment text added at each site

`extension/ui/sidebar.js`, lines 3–11, above `WEB_PROTOCOL`:

```js
  // The companion web protocol below is a validated cross-boundary contract,
  // not an internal identifier: the companion host served by the NUC gates on
  // it as well, so renaming it on one side only would leave that host never
  // seeing `host_hello`, keep it unhosted and make attach() answer
  // "not_hosted", which breaks meme attach silently against every NUC that has
  // not been refreshed. The receive side therefore accepts both spellings,
  // while every send site below keeps emitting the retired
  // `framenest.companion.web.v1` on purpose, because the host gates on exactly
  // that spelling. The rename lands in the removal cut, on both sides at once.
```

`src/framenest/adapters/api/web/companion_host.js`, lines 8–16, above `PROTOCOL`:

```js
  // The companion web protocol below is a validated cross-boundary contract,
  // not an internal identifier, and this asset is served by the NUC while the
  // extension holds the other side of it. Both sides gate on the spelling, so
  // renaming it here alone would leave the extension's `host_hello` unread,
  // keep `hosted` false and make attach() answer "not_hosted", which breaks
  // meme attach silently against a refreshed extension. The host therefore
  // keeps emitting the retired `framenest.companion.web.v1` on purpose while
  // the extension accepts both spellings and also keeps sending this one; the
  // rename lands in the removal cut, on both sides at once.
```

Each states, once and without length: cross-boundary validated contract, not an internal name; both sides gate, so a one-sided rename breaks meme attach silently against an unrefreshed peer; the extension dual-accepts but keeps sending the retired spelling; the host keeps emitting it; the rename lands in the removal cut on both sides together. No ADR was amended; ADR-0085 is untouched and is not in the diff.

## 7. Helper reuse decision

The prompt prefers reusing an exported acceptance helper. I did **not** reuse `acceptCompanionApiVersion` from `extension/shared/messages.js`: its accept list is `ACCEPTED_API_VERSIONS` (`kronika-companion.v1`, `framenest-companion.v1`), so reusing it would mean mutating the Class2 API-version acceptance, which the same prompt forbids. `messages.js` is therefore unmodified and needed no reported exception. `acceptCompanionWebProtocol` mirrors session 12's shape (`indexOf` over a frozen accept list) and lives beside its only caller, since no existing exported helper covers this value.

## 8. Membership set and every Part C movement

`EXPECTED_FRAMENEST_CONTENT_PATHS` **did not move** — `test_framenest_content_path_ledger_matches_exactly` passes untouched; no new file was created and every file I touched already carries the token. Part A and Part B did not move and pass.

Four Part C scalars moved, each re-pinned beside a cause comment. Measured per-file deltas (`git show HEAD:<path>` vs working file):

| Scalar | Before → after | Exact cause |
|---|---|---|
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["src"]` | 2984 → **2985** | +1: `companion_host.js` lower-case `framenest` 2 → 3, the single retired spelling named in the new comment |
| `["extension"]` | 189 → **190** | +1: `sidebar.js` 19 → 20, the single retired spelling named in the new comment |
| `["tests"]` | 4505 → **4517** | +12: `companion_web_bridge.test.js` 7 → 16 (+9: two new protocol constants, the three acceptance tests, the emit test and its probed literals); `companion_review_extension.test.js` 51 → 54 (+3: the retired spelling in the end-to-end test) |
| `CAPITALIZED_OCCURRENCE_COUNT` | 3396 → **3397** | +1: `companion_web_bridge.test.js` capitalized2 → 3, from the new `loadSidebarBridgeContext` helper returning the bridge object beside its context |

Unmoved and verified: `PER_TREE_FRAMENEST_FILE_COUNT` (all six), `CAPITALIZED_FILE_COUNT` 482, `MUTATION_HEADER_OCCURRENCE_COUNT`/`_FILE_COUNT`, `HOST_PATH_OCCURRENCE_COUNT`, `UNIT_ACCOUNT_OCCURRENCE_COUNT`, `ENV_PREFIX_*`, `CONSOLE_SCRIPT_ENTRY_COUNT`.

## 9. Exact counts, both routes

| Route | Baseline `78c841f` | Final `9c71bfb` |
|---|---|---|
| `node --test tests/*.test.js` | 576 total, 571 passed, 0 failed, 5 skipped | **581 total, 576 passed, 0 failed, 5 skipped** (+5 new tests) |
| `ap exec --operation test` | 4358 passed, 8 skipped, 3 warnings, 0 failed (686.03s) | **4358 passed, 8 skipped, 3 warnings, 0 failed** (671.59s) |
| retention module focus | 15 passed | **15 passed** |

`ap project check --baseline 9c71bfb0a06cb30c5d747816e9067f6a25350c58: PASS`. `ap doctor: PASS`. Working tree clean.

## 10. GitOne additional local commit, parent `78c841f`, no push, no new branch:

```text
9c71bfb0a06cb30c5d747816e9067f6a25350c58 fix(companion): dual-accept the web protocol so the rename cannot be one-sided
```

Branch `feat/kronika-identity-dual-read` holds **seven** commits above public `main` `18c357c` (the prompt asked for eight; see MEASURED):

```text
9c71bfb  fix(companion): dual-accept the web protocol so the rename cannot be one-sided
78c841f  feat(companion): send both mutation headers and migrate browser keys on read
0b75675  test(retention): pin the content-path membership set so a partial rename fails
02a8048  docs(identity): state the resolver's measured precedence and per-channel conflict rule
24bea56  fix(identity): restore pre-cut process-environment parity for old spellings
c02c675  fix(identity): exit 2 on an identity-environment conflict at every entry point
90c93ea  feat(identity): read both KRONIKA_ and FRAMENEST_ spellings, write only the old
```

## 11. Deviations, risks, missing evidence

- **One undeclared command.** I used `sed -i` once, on the authorized path `tests/companion_web_bridge.test.js`, to drop an unused parameter from a test helper I had just written. It mutated only that authorized file, was verified by `grep` afterwards, changed no ledger occurrence count, and was re-covered by a full JS run. No other undeclared command ran; no command wrote outside the repository or `/tmp`, and I created no `/tmp` files.
- **No rendered or browser evidence.** By design: this correction has no authority for a browser or a profile, and the prompt requires synthetic in-memory message objects under `node --test`. Consequence: the two non-emitted, non-gated paths of the live panel (the `open_details` composer flow and the review overlay) are covered only by the source-level pins that already existed. Nothing about the shipped runtime was observed.
- **No NUC contact.** The host asset was not served, so the cross-boundary claim is proven against the module loaded from source by `tests/companion_web_bridge.test.js`, not against a NUC response. The served-asset path stays pinned by the untouched `test_local_web_application.py` assertion.
- **Risk carried forward by design.** Both header spellings are accepted until the removal cut, so a NUC refresh will not make the companion reload observable. Nothing in this cut is a migration and nothing is deleted.
- **`extension/shared/messages.js` untouched**, so the Class 2 acceptance, the storage keys, the alarm names and the mutation headers are exactly as session 12 left them.

Resolved Execution Issues / Near-Misses: 1) The first version of the end-to-end test asserted its message payloads with `deepEqual` under `node:assert/strict`, which failed with "same structure but not reference-equal" because payloads are constructed inside the `vm` realm and carry a foreign prototype. Cause: cross-realm object identity, not a candidate defect; resolution: replaced both with field-level `equal` assertions, and used `Array.from` for the frozen accept list in the bridge suite. Residual risk: none, no assertion was weakened. 2) I initially read `extension/ui/sidebar.js` as running its whole DOM-dependent tail in the minimal harness and briefly expected `chrome.storage` to throw; a probe showed the IIFE returns at the existing null guard (lines 390–414), which is why the minimal harness works. No code change resulted; recorded because it shaped the harness choice.

Pre-Existing Failure Classification: none. Both baselines reproduced exactly on the first run with zero failures, and no failure was excluded or reclassified at any point.

## 12. Smallest next step

Orchestrator publishes `feat/kronika-identity-dual-read` at `9c71bfb` — the branch is complete and green, and no further correction is needed before that.

Orchestration critique:
MEASURED: The prompt asks me to report "all eight commit SHAs on this branch", but the branch holds seven commits above public `main`; evidence: `git rev-list --count 18c357c..HEAD` →7, and the prompt's own lineage enumerates six pre-existing commits plus mine; effect: an off-by-one in the issued inventory that would mis-state the branch contents in the acceptance record; smallest correction: read the count from `git rev-list --count` when the next grant enumerates commits. This is the second instance of the session-12 LEAD about unreliable inventory labels, now measured rather than assumed.
LEAD: The static `v: <expr>` multiset pins in `companion_web_bridge.test.js` are deliberately brittle — they will fail on any unrelated edit that adds or renames an outbound protocol expression anywhere in `sidebar.js` or `companion_host.js`; cheapest useful check: when the removal cut moves these constants on both sides, delete those two multiset assertions in the same commit rather than re-pinning them, since their whole purpose expires with the retired spelling.

Authority expiry: this terminal report ends the KSI-CORR-05 grant. No push, publication, NUC contact, deployment or later cut is authorized by it.