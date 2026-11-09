# Authoritative Worker prompt — Kronika whole 01, Worker session 02, exchange 02

Activation: this file is the exact issued Worker prompt for the logical whole
`timeline-and-history-media-thumbnails`. It is stored under the Meta filename
mapping `<worker-session>_<phase>_<meta-exchange-index>.md` as
`02_correction_01.md`. The matching terminal report is `02_report_01.md`.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: timeline-and-history-media-thumbnails
Worker session ordinal: 02
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Correction
Task identity: KRN-THT-CORR-02 — correct visibility-change preview retirement and add its regression test
Delivery route: direct session dispatch
Reasoning recommendation: Medium — one bounded lifecycle correction in app.js plus one causal UI test
Recommended context capacity: approximately 250k tokens
Independence required: no
Continuity anchor: terminal PASS report 02_report_00.md and candidate commit 72e8bb0b912eadcb0a51e66ff276b4448a266bde
Authority renewal: prior implementation authority expired; this prompt grants a new bounded correction grant for one concrete finding
Evidence posture: non-independent; the correction cannot self-certify, and the Orchestrator re-verifies
```

You are continuing the healthy same Worker session that produced commit
`72e8bb0b912eadcb0a51e66ff276b4448a266bde`. The prior implementation authority
expired. This prompt grants a new, complete, bounded correction grant. Retained
context is convenience, not authority; re-gate the repository and stop on any
conflict with current evidence.

Before substantive work, confirm that `Native planning mode: not-used` is the
actual client state (native Plan mode OFF). If it is enabled, stop and return
`BLOCKED` naming the contradiction.

## 1. Concrete finding

The implementation correctly retires previews and cancels list requests on
accepted navigation, page/filter/tab replacement, identity change and page
teardown. However, it placed the new `kronikaRetirePreviews()` call and the
three `kronikaCancelListRequest(...)` calls inside `kronikaPauseForHide()`.

`kronikaPauseForHide()` is invoked from both:

- `kronikaOnVisibility()` when `document.hidden` becomes true; and
- the `pagehide` listener.

As a result, merely switching away from the browser tab retires every Timeline
and personal-record History preview and aborts any in-flight list request. When
the user returns to the tab, the list is not reloaded, so the cards keep only
their kind icons and a request that was in flight may remain incomplete. That
is broader than the accepted plan's "document teardown" retirement and is a
user-visible regression.

The accepted design requires retirement on accepted navigation, page/filter/tab
replacement, identity change and page/document teardown. It does not require
retirement on ordinary tab-visibility changes.

## 2. Exact correction

Change only these two repository paths:

```text
src/kronika/adapters/api/web/app.js
tests/kronika_ui.test.js
```

Required behavior:

1. `kronikaPauseForHide()` keeps its existing polling behavior (`clearTimeout`,
   `kronikaRuntime.hiddenHold = true`) but no longer retires previews or cancels
   Timeline/History list requests.
2. Add a separate page-teardown function, for example
   `kronikaRetireListsForPageHide()`, that calls `kronikaRetirePreviews()` and
   cancels the `timeline`, `questions` and `records` list controllers.
3. Bind that separate function to the existing `pagehide` lifecycle, alongside
   the existing `kronikaPauseForHide` pagehide binding. Keep
   `kronikaPauseForHide()` bound to `visibilitychange` through
   `kronikaOnVisibility()` with its polling-only behavior.
4. Do not change any other function, selector, API field, route, test
   expectation or document. Preserve all existing behavior and the accepted
   design.
5. Add one causal regression test in `tests/kronika_ui.test.js` proving that a
   `visibilitychange` to hidden and back does not remove a ready preview, does
   not clear its `src`, and does not abort the list request, while the existing
   page/navigation/identity retirement tests still pass. Use the existing
   harness's `documentListeners`, `document.hidden`, preview image and fetch
   call records; do not invent production behavior.

If the correct fix requires a change outside these two paths, stop and report;
do not expand the allowlist.

## 3. Baseline and gate

```text
Repository: https://github.com/cisarik/kronika
Working directory: /Users/agile/Projects/kronika
Repository checkout topology: standalone checkout
Working-copy topology: canonical checkout; one active mutator
Expected branch: main
Baseline commit under test: 72e8bb0b912eadcb0a51e66ff276b4448a266bde
Parent of the correction commit: 72e8bb0b912eadcb0a51e66ff276b4448a266bde
Public main: 246c9f86b72e652cd36ed0d9f4e19e77f972df91 (the candidate is local and unpushed)
Containing-repository .ap gitlink: d7023cf037f6d17885c3ede5c04812c61640da50
Submodule HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
```

Verify with:

```text
git rev-parse HEAD
git status --short
git log --oneline -2
./.ap/ap doctor
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 72e8bb0b912eadcb0a51e66ff276b4448a266bde
```

Stop if the worktree is not clean or HEAD is not the candidate commit.

## 4. Validation

Run the exact gate and the UI regression set:

```text
# [MacBook / fish]
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 72e8bb0b912eadcb0a51e66ff276b4448a266bde
node --test tests/kronika_ui.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js
git diff --check
git status --short
#------------------------------------------------------
```

The corrected candidate must pass the existing 43 Node tests plus the new
regression test. Do not run the full Python suite. If a failure is pre-existing,
classify it with exact evidence; do not repair unrelated behavior.

## 5. Authority

```text
Positive authority: edit exactly src/kronika/adapters/api/web/app.js and
  tests/kronika_ui.test.js; read-only inspection of the repository, the accepted
  plan report, this whole's notes and the existing report; run the exact gate and
  Node tests above; stage exactly the two paths and create exactly one normal
  corrective local commit on main; direct-write the terminal report below if it
  is absent, followed by a complete readback.

Negative authority: any other file edit, creation, deletion or rename; any
  change to the API, repository, CSS, docs, tests other than the one allowed
  test file, preview route, audience policy, public composition, Gallery/Details,
  index.html, extension, deployment or host; any Git push, fetch, pull, merge,
  rebase, reset, restore, clean, stash, checkout, switch, branch, tag, remote,
  config write or amend; any dependency, migration, NUC, SSH, sudo, deploy,
  browser, provider, secret or private-media access; any acceptance,
  publication, deployment or closure claim.

Git authority: read-only inspection plus exactly one normal corrective commit
  on main of the two exact paths; no push and no amend.
Network authority: none.
Secret authority: none.
```

## 6. Commit and report

After the corrected Node suite passes and `git diff --check` is clean, stage
exactly the two paths and create one corrective commit:

```text
git add -- src/kronika/adapters/api/web/app.js tests/kronika_ui.test.js
git diff --cached --check
git commit -m "fix: keep card previews across visibility changes"
git show --stat --oneline HEAD
```

Do not push. The final candidate is the correction commit on top of
`72e8bb0b912eadcb0a51e66ff276b4448a266bde`; report both SHAs.

Write the terminal report to:

```text
/Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/02_report_01.md
```

The report starts exactly with `### Report for ORCHESTRATOR_CHAT`, echoes the
coordinates and role fields, and contains:

```text
Status: PASS
Phase-qualified result: implementation-PASS
Start commit: 72e8bb0b912eadcb0a51e66ff276b4448a266bde
End commit: <correction commit SHA>
Report justification: new-mutation
Logical-whole closure: not-closed
```

Include: the concrete finding; the exact correction; the changed paths and diff
stat; the gate and Node test commands with exact pass/fail counts; the new
regression test identity and what it proves; the correction commit SHA; any
deviation or residual risk; `Resolved Execution Issues / Near-Misses`;
`Pre-Existing Failure Classification`; one smallest next step; and the
orchestration critique. Do not claim acceptance, publication or deployment.

## 7. Delivery and trace

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/
Trace project key: kronika
Trace logical-whole projection identity: 01-timeline-and-history-media-thumbnails
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_correction_01.md
Destination path: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/
Report filename: 02_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: src/kronika/adapters/api/web/app.js and tests/kronika_ui.test.js only
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/02_report_01.md
```

If the report path exists, including an empty file, stop `BLOCKED` without
overwriting it.

## Visible delivery capsule

```text
🟡 Ready for delivery
Recipient: Bounded Correction Worker · current-worker-session · direct dispatch
Recommendation: Medium · approximately 250k tokens
Client: Native Plan Mode OFF
Prompt: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/02_correction_01.md
Report: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/02_report_01.md
Archival: wait-for-report
```
