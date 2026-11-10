### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: ui-ux-consistency
Worker session ordinal: 02
Worker exchange ordinal: 03
Persistent role identity: WORKER
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded UI Polish Worker
Phase: Correction
Task identity: KRN-UX-CORR-03 — keep Timeline current on question detail routes
Status: PASS
Phase-qualified result: implementation-PASS
Start commit: 27aa5fd29f259ee27de109f37bb7cf88f255b93f
End commit: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
Report justification: new-mutation
Logical-whole closure: not-closed
Result artifact or commit: 8646146b7dfd50a9a99ec94dbd696102cbe5ca4e
Result evidence: one corrective commit whose parent is 27aa5fd29f259ee27de109f37bb7cf88f255b93f; selected gates below
```

Native planning mode was off. The prior correction authority had expired. This session re-gated a clean `main` at `27aa5fd29f259ee27de109f37bb7cf88f255b93f` with the recorded `.ap` pin `d7023cf037f6d17885c3ede5c04812c61640da50`. No acceptance, publication, deployment, or closure is claimed.

## Finding

Removing History also removed the `request`/`record` branch from `kronikaMarkCurrent`. Those routes still open from Timeline rows and still show the primary navigation, but no browsing tab stayed current. Details still marked Gallery and the review subroutes still marked Review.

## Change

`kronikaMarkCurrent` now maps `request` and `record` to `timeline`, beside the existing `details` → `gallery` and `review-shared`/`review-requests` → `review` mappings. No History link, route, section, or `aria-current` value was restored. The `#/history` fold, routes, search, filters, glyphs, and APIs are unchanged.

## Regression

`question detail routes keep Timeline current` asserts that `#/requests/op-1` marks Timeline and clears Gallery, Search, Research, and Review; `#/records/{id}` marks Timeline; `#/details/media-1` marks Gallery; `#/review/shared` marks Review; and no History browsing link or History current value exists.

## Changed paths

```text
 src/kronika/adapters/api/web/app.js |  5 +++--
 tests/kronika_ui.test.js            | 36 ++++++++++++++++++++++++++++++++++++
 2 files changed, 39 insertions(+), 2 deletions(-)
```

Parent: `27aa5fd29f259ee27de109f37bb7cf88f255b93f`. Commit: `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e`, message `fix: keep Timeline current on question details`. No push.

## Validation

- `./.ap/ap doctor`: PASS
- `./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 27aa5fd29f259ee27de109f37bb7cf88f255b93f`: PASS
- `./.ap/ap exec ... --operation test-focus -- tests/contract/test_local_web_application.py -q -p no:cacheprovider`: 208 passed
- `node --test tests/kronika_ui.test.js tests/gallery_search_tag_filters.test.js tests/gallery_filter_controls.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js`: 85 passed, 0 failed
- `git diff --check` and `git diff --cached --check`: clean
- Post-commit status: empty

## Deviations

None.

Resolved Execution Issues / Near-Misses: none

Pre-Existing Failure Classification: none

## Residual risk

The regression is a Node fixture of `aria-current`, not a rendered check of the tab’s painted state. Public `main` is still `bbf776c462e1eb5eccb91eb027a85eee9055d2ec`; this commit is local and unpushed.

Smallest next step: a fresh read-only E2 re-acceptance of `8646146b7dfd50a9a99ec94dbd696102cbe5ca4e`, including current marking on request and record routes. Publication and NUC refresh remain separately authorized.

Orchestration critique:
MEASURED: none
LEAD: none

Authority expiry: submission of this terminal report ends the correction grant. No acceptance, publication, deployment, production, or closure authority remains.
