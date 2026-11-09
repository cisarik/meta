### Report for ORCHESTRATOR_CHAT

Logical whole identity: timeline-and-history-media-thumbnails
Worker session ordinal: 02
Worker exchange ordinal: 02
Persistent role identity: WORKER
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Correction
Task identity: KRN-THT-CORR-02 — correct visibility-change preview retirement and add its regression test
Status: PASS
Phase-qualified result: implementation-PASS
Start commit: 72e8bb0b912eadcb0a51e66ff276b4448a266bde
End commit: b66ec8f50860ace624f6be1fd3ad63f521edcd33
Report justification: new-mutation
Logical-whole closure: not-closed

## 1. Concrete finding

The implementation correctly retired previews and cancelled Timeline/History
list requests on accepted navigation, page/filter/tab replacement and identity
change. It also placed the same retirement and cancellation inside
`kronikaPauseForHide()`.

`kronikaPauseForHide()` is invoked from two callers:

- `kronikaOnVisibility()` when `document.hidden` becomes true; and
- the `pagehide` listener.

Consequently, merely backgrounding the browser tab retired every Timeline and
personal-record History preview and aborted any in-flight list request. When
the user returned to the tab, the list was not reloaded, so the cards kept only
their kind icons. That was broader than the accepted “page/document teardown”
requirement and was a user-visible regression.

## 2. Exact correction

Changed only the two allowlisted paths.

Production change in `src/kronika/adapters/api/web/app.js`:

- `kronikaPauseForHide()` now performs only its original polling behavior:
  `kronikaClearPollTimer()` and `kronikaRuntime.hiddenHold = true`.
- Added `kronikaRetireListsForPageHide()`, which calls
  `kronikaRetirePreviews()` and cancels the `timeline`, `questions` and
  `records` list controllers.
- Bound `kronikaRetireListsForPageHide` to the existing `pagehide` lifecycle
  alongside the existing `kronikaPauseForHide` binding.
- `kronikaOnVisibility()` still delegates to `kronikaPauseForHide()` through
  `visibilitychange` and therefore no longer retires previews or aborts list
  requests.

No other function, selector, API field, route, test expectation or document
changed.

Test change in `tests/kronika_ui.test.js`:

- Exposed the harness's existing `documentListeners`;
- recorded non-`hashchange` window listeners in `windowListeners` so the test
  can fire the two real `pagehide` bindings;
- added one causal regression test.

## 3. Changed paths and diff stat

```text
 src/kronika/adapters/api/web/app.js |  8 +++-
 tests/kronika_ui.test.js            | 76 +++++++++++++++++++++++++++++++++++++
 2 files changed, 82 insertions(+), 2 deletions(-)
```

No other path was created, deleted, renamed or changed. The API, repository,
CSS, documentation, preview route, audience policy, public composition,
Gallery/Details renderer, `index.html`, extension, deployment and host state
are untouched.

## 4. New regression test

Identity:

```text
visibility changes keep card previews and in-flight lists while pagehide retires
```

What it proves, using the existing harness's `documentListeners`,
`document.hidden`, preview image and fetch call records:

- A loaded Timeline media card reaches `data-kronika-preview="ready"`.
- A `visibilitychange` to hidden and back leaves the preview in the card, keeps
  its non-empty `src`, keeps it `ready`, and leaves the settled list signal
  un-aborted.
- A second Timeline page request is held in flight; `visibilitychange` to hidden
  and back leaves its `AbortController` signal un-aborted.
- Resolving that request renders its card normally.
- Firing the two recorded `pagehide` listeners still removes the preview source
  and element and aborts the tracked list controller.

All pre-existing page/navigation/identity retirement tests still pass.

## 5. Gate and validation evidence

Baseline revalidation before mutation:

```text
git rev-parse HEAD
git status --short
git log --oneline -2
```

Observations: HEAD `72e8bb0b912eadcb0a51e66ff276b4448a266bde`, branch `main`,
clean working tree, parent `246c9f86b72e652cd36ed0d9f4e19e77f972df91`, `.ap`
gitlink and submodule HEAD `d7023cf037f6d17885c3ede5c04812c61640da50`.

```text
./.ap/ap doctor
```

Result: PASS.

```text
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 72e8bb0b912eadcb0a51e66ff276b4448a266bde
```

Result: PASS. It reported sanitized inherited environment classes
(`SSH_AUTH_SOCK`, `PATH`) without values; this is a warning, not a failed gate.

```text
node --test tests/kronika_ui.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js
```

Result: **44 passed, 0 failed, 0 cancelled, 0 skipped**. This is the existing 43
Node tests plus the new regression test. `tests/kronika_ui.test.js` alone:
**21 passed, 0 failed** (20 preserved plus 1 new).

```text
git diff --check
git status --short
```

Result: `git diff --check` clean; `git status --short` clean after the
corrective commit.

No full Python suite was run, as directed.

## 6. Correction commit

```text
Commit: b66ec8f50860ace624f6be1fd3ad63f521edcd33
Message: fix: keep card previews across visibility changes
Parent: 72e8bb0b912eadcb0a51e66ff276b4448a266bde
Branch: main
Push: none
```

Exactly one normal corrective local commit was created on top of the candidate.
No amend, history rewrite, tag, branch, remote, fetch or config write occurred.

## 7. Deviations and residual risk

Deviations from the correction prompt: **none**.

The only supporting change beyond the production fix is the two-line harness
exposure in the allowlisted test file, needed to invoke the real
`visibilitychange` and `pagehide` listeners rather than inventing behavior.

Residual risks:

- Real-browser `visibilitychange`/`pagehide` ordering and bfcache restoration
  remain unverified; rendered acceptance requires the exact accepted release.
- `pagehide` still retires previews and aborts list controllers, as the accepted
  design requires. A bfcache-restored page therefore keeps icons until the next
  reload or navigation; this behavior is unchanged from the candidate.
- No acceptance, publication, deployment or rendered claim is made.

## 8. Resolved Execution Issues / Near-Misses

The correction prompt assumed the existing harness exposed `documentListeners`.
The baseline harness kept them private and discarded non-`hashchange` window
listeners. The test file now exposes the document listeners and records window
listener types. This is bounded test support inside the allowed path; no
production behavior was invented and no unrelated expectation was weakened.

## 9. Pre-Existing Failure Classification

None. No product-test failure was observed, and no pre-existing failure was
classified or modified.

## 10. Smallest next step

Orchestrator re-verifies the two-path correction at commit
`b66ec8f50860ace624f6be1fd3ad63f521edcd33` against the 44-test Node evidence
and the separation of visibility polling from pagehide teardown. Publication,
NUC refresh and rendered acceptance require separate grants.

## 11. Orchestration critique

```text
Orchestration critique:
MEASURED: The correction prompt assumes the baseline harness exposes `documentListeners`, but it kept them private; the allowed test file needed a minimal exposure to fire the real listeners. Evidence: harness diff and 44 passing Node tests. Effect: test-only support, no production change. Smallest correction: none beyond recording the assumption.
LEAD: Real-browser visibility/pagehide ordering and bfcache restoration remain unverified; the cheapest useful check is one Cooperator rendered Timeline/History pass on the exact accepted release.
```

Authority expires on submission of this terminal report. No acceptance,
correction, publication, deployment, production or closure authority remains.
A later phase requires a new complete authoritative prompt.
