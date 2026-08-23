### Report for ORCHESTRATOR_CHAT

1. Coordinate echo

- Logical-whole identity: `framenest-companion-review-inbox-ux-history-mvp`
- Worker session ordinal: 01
- Worker exchange ordinal: 03
- Worker session target: current-worker-session
- Internal delegation: not-used

2. Status

PASS

3. Phase-qualified result

- Result: `implementation-PASS`
- Result artifact: commit `0c71d07f39026503268a90d4799aad6a27bfc0f7`
- Result evidence: post-commit focused Node suites passed, with `tests/x_companion_extension.test.js` at 46/46 and `tests/companion_review_extension.test.js` at 20/20; zero failures, skips, cancellations, or todos.

4. Logical-whole closure

`Logical-whole closure: not-closed`

5. Gate evidence

- Branch at start and end: `feat/x-meme-browser-companion`.
- HEAD at start: `a154b694d88c54e05a93012103e2811abeb26555`.
- HEAD at end: `0c71d07f39026503268a90d4799aad6a27bfc0f7`.
- Commit parent: `a154b694d88c54e05a93012103e2811abeb26555`, matching the required exact baseline.
- `.ap` gitlink at start/end: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.
- `.ap` checkout at start/end: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.
- Pre-mutation gate: exact branch, exact HEAD, clean worktree, and matching submodule pin all passed before mutation.
- End gate: `git status --short` produced no output; the worktree is clean.
- Native planning mode: off, as required.

6. Changed files and purpose

The commit contains exactly the nine allowlisted paths:

- `extension/shared/messages.js` — defines and exports the single exact invalidation classifier, signature, and recovery copy.
- `extension/content/x_adapter.js` — centralizes runtime URL/message/listener operations behind targeted guards; adds idempotent stale teardown, alert, control disabling, scan/injection stops, and pre-append URL checks.
- `extension/ui/save.js` — guards synchronous and callback request failures, preserves ordinary unavailability behavior, shows the shared recovery copy, and disables Save form actions on stale context.
- `extension/ui/picker.js` — guards request failures, cancels stale async rendering, shows the shared recovery copy, and disables search/navigation/attach actions.
- `extension/ui/sidebar.js` — guards review URL and request operations, preserves unrelated-error propagation, shows the shared recovery copy, and disables affected sidebar actions.
- `extension/ui/review.js` — guards review URL and request operations, propagates stale state through the controller, shows the shared recovery copy, and disables review field/tag/Save actions.
- `tests/x_companion_extension.test.js` — covers falsy runtime ID, exact invalidation throws/callback errors, idempotent single alert, disabled controls, partial-host prevention, valid behavior, helper routing, scan stops, and unrelated-error propagation.
- `tests/companion_review_extension.test.js` — covers the shared exact classifier and sidebar/review stale, ordinary-error, and unrelated-error behavior.
- `docs/X_COMPANION.md` — documents the shipped reload recovery behavior and exact user-facing copy.

7. Guard coverage

Shared evidence: `extension/shared/messages.js:13-15` owns the exact signature/copy, and `extension/shared/messages.js:89-94` classifies only a missing/falsy runtime ID or an Error/lastError message containing the exact `Extension context invalidated` signature.

| X adapter runtime site | Helper routing evidence |
| --- | --- |
| `extension/content/x_adapter.js:289` | The sole direct `chrome.runtime` acquisition is isolated in `runtimeObject()`; operations consume this object only after `guardInvalidatedRuntime` classification. |
| `extension/content/x_adapter.js:313` | The sole `runtime.getURL` operation is inside `runtimeUrl()`, with pre-operation missing-ID classification, exact-signature catch handling, and unrelated-error rethrow. |
| `extension/content/x_adapter.js:944` | Save iframe URL is obtained through `runtimeUrl("ui/save.html")` before any host is created or appended. |
| `extension/content/x_adapter.js:1061` | Save popup target-origin resolution uses the same guarded `runtimeUrl()` helper. |
| `extension/content/x_adapter.js:1743` | Picker iframe URL is obtained through `runtimeUrl("ui/picker.html")` before any host is created or appended. |
| `extension/content/x_adapter.js:331` | The sole listener-registration operation is inside `addRuntimeListener()`, with pre-operation classification, exact-signature catch handling, and unrelated-error rethrow. |
| `extension/content/x_adapter.js:2072` | `onMessage` registration routes through `addRuntimeListener("onMessage", ...)`. |
| `extension/content/x_adapter.js:2094` | `onConnect` registration routes through `addRuntimeListener("onConnect", ...)`. |
| `extension/content/x_adapter.js:353` | The sole `runtime.sendMessage` operation is inside `request()`, with missing-ID short-circuit, synchronous exact-signature handling, and unrelated-error rejection. |
| `extension/content/x_adapter.js:358` | The sole `runtime.lastError` read is inside the guarded callback; exact invalidation becomes stale while unrelated callback errors retain `extension_unavailable`. |

Additional X lifecycle coverage: `markStale()` at `extension/content/x_adapter.js:236-286` is idempotent, disconnects the observer, closes/sweeps Save and picker hosts, clears the bound composer, disables existing companion controls, and appends at most one fixed `role="alert"` notice. `injectSave()`, `onComposerFocusIn()`, `injectAttach()`, and `scan()` have stale exits, preventing post-invalidation reinjection/scans.

Equivalent UI coverage:

- Save: `extension/ui/save.js:41-111` classifies request failures and locks the form with the exact recovery copy; stale responses cannot overwrite that status.
- Picker: `extension/ui/picker.js:34-110` classifies request failures, invalidates async tokens, and disables search, refresh, navigation, and attach actions with the exact recovery copy.
- Sidebar: `extension/ui/sidebar.js:131-170` guards runtime URLs; `extension/ui/sidebar.js:305-316` installs the stale UI state; `extension/ui/sidebar.js:324-368` guards request sync/callback failures without swallowing unrelated errors.
- Review: `extension/ui/review.js:338-385` guards runtime URLs; `extension/ui/review.js:409-467` guards request sync/callback failures; `extension/ui/review.js:530-538` and the controller stale state disable affected review actions and retain the exact recovery copy.
- `extension/background/service_worker.js` is untouched. Both `git diff HEAD^ HEAD -- extension/background/service_worker.js` and the recovery-copy/symbol search against that file produced no output.

8. Tests and validation

- `node --test tests/x_companion_extension.test.js`: PASS, 46 tests passed; 0 failed, skipped, cancelled, or todo.
- `node --test tests/companion_review_extension.test.js`: PASS, 20 tests passed; 0 failed, skipped, cancelled, or todo.
- Both suites were rerun after commit and remained green.
- Direct runtime search found only the centralized adapter acquisition/operations and the cited guarded call sites; the test also asserts no raw `chrome.runtime.getURL`, `sendMessage`, `onMessage`, `onConnect`, or `lastError` operation remains outside those helpers.
- Documentation check: `docs/X_COMPANION.md:150-158` contains the exact shipped recovery copy and classifier guidance.
- Scope check: changed and committed paths equal the exact nine-path allowlist; no out-of-allowlist path is present.
- `git diff --check` before staging, on the staged diff, and across `HEAD^..HEAD`: PASS with no output.
- Service-worker check: no diff and no recovery copy/symbol in `extension/background/service_worker.js`.

9. Commit result

- Commit: `0c71d07f39026503268a90d4799aad6a27bfc0f7`
- Subject: `fix: guard invalidated companion extension contexts`
- Parent: `a154b694d88c54e05a93012103e2811abeb26555`
- Commit count for this grant: one.
- `push: not-performed (not authorized)`

10. Deviations, risks, and missing evidence

- Deviations from the Slice B grant: none.
- Known risk/limitation: MiniDom tests exercise exact error classes and rendered state but cannot prove Chromium's real unpacked-extension reload lifecycle.
- Missing evidence: Cooperator UX step 16 remains required to demonstrate the real Chromium reload/recovery behavior. Slice C, live X/NIM interaction, publication, and NUC updates were not authorized and were not performed.
- Secrets, manifest permissions, server routes, migrations, and the service worker were not touched.

11. Smallest next step

ORCHESTRATOR reviews commit `0c71d07f39026503268a90d4799aad6a27bfc0f7` and this evidence, then starts Slice C with the Cooperator for the UX walk, including step 16.

12. Report basis

Report justification: new-mutation

13. Authority expiry

The exchange-03 Slice B implementation authority expires with this terminal report. No push, publication, Slice C activity, NUC update, or further repository mutation is authorized by this grant.

14. Resolved Execution Issues / Near-Misses:

- The first focused X-suite run exposed two assertions that still matched pre-helper source shapes (`getURL(...)` and the pre-stale picker condition). They were updated to assert the intended guarded helper forms; no product regression was involved.
- Final audit identified that the disconnected observer alone did not prevent the already-bound focus listener from attempting a later Attach injection. Stale exits were added at injection/focus entry points and covered by the focused test before commit.

15. Pre-Existing Failure Classification:

none
