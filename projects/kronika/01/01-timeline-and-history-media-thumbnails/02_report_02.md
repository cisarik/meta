### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: timeline-and-history-media-thumbnails
Worker session ordinal: 02
Worker exchange ordinal: 03
Persistent role identity: WORKER
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded UI Polish Worker
Phase: Correction
Task identity: KRN-THT-UI-02 — History Questions-only Timeline-style list
status: PASS
Phase-qualified result: implementation-PASS
Start commit: 65772c6028c07edcab47b6928dbb31e30876c70a
End commit: e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd
Report justification: new-mutation
Logical-whole closure: not-closed
```

History is now one personal-question chronicle in the Timeline list language. Native Plan mode was off. This exchange does not accept, publish, deploy, or close the logical whole.

## Finding

The Cooperator tested History at `65772c6`. Questions and Records showed the same personal items twice, and the History cards did not match the Timeline chronicle. The direction was to keep only Questions, remove the Records tab and its second list, and present History as the same compact row language: header, separators, emoji status and visibility, subtle green hover, and room for the question text. No visible Added date. Timeline, Gallery, Details, the API, authorization, and stored data stay as they are.

`SPEC.md` named personal-record History as the existing cards, so that one normative sentence now names the question chronicle. `tests/contract/test_local_web_application.py` does not pin the History markup and was not edited.

## Design

The Questions and Records tab pair is gone. The heading and the lede stay: personal questions, answers, and saved records, private until an administrator shares them.

`#/history/records` parses as the History route with path `/history`, keeping any offset. Following that address replaces the hash with `#/history` or `#/history?offset=N` and loads the Questions list. There is no second list and no link to the old address.

The list is one ordered chronicle. Desktop header, `aria-hidden` like Timeline: Question, Kind, Status, Visibility. Each row is a question link, a Kind label, a status glyph, and a visibility glyph. The question column is `minmax(0, 1fr)` and the title clamps at two lines. There is no preview column and no date. At 720 px the header hides, the row becomes one flexible column, and Kind, Status, and Visibility wrap under the question. History does not scroll horizontally. Kind, status, and visibility targets stay at least 44 px.

Saved questions link to the existing record route. Unfinished questions link to the existing request route. The page reads only `/api/research-requests`. It does not call `/api/my/records`.

## Glyphs and accessible text

Status reuses the Timeline vocabulary from the request `state`:

| State | Glyph | Accessible text |
| --- | --- | --- |
| saved | ✅ | Saved |
| running and the other in-progress states | ⏳ | Working, and the existing in-progress labels |
| failed and the other failure states | ⚠️ | Failed, and the existing failure labels |
| cancelled | 🚫 | Cancelled |

The research-request payload has no visibility or publication field. Those rows show 🔒 with the accessible text `Private`. If an item already carries `visibility` or `publication_state`, the row uses the Timeline share glyph and label, including Household · Approved. The glyph is `aria-hidden`. The words stay in `visually-hidden` text and the cell `title`.

## Hover

History rows use `kronika-chronicle__item`, so they take the Timeline hover and focus-within treatment: 160 ms background and an inset green accent, no transform and no layout shift. `prefers-reduced-motion: reduce` still clears that transition and the menu animation.

## Changed paths

Parent `65772c6028c07edcab47b6928dbb31e30876c70a`. Commit `e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd`, subject `fix: make History a Questions-only chronicle list`. Working tree clean. Push: none.

```text
SPEC.md                                 |   4 +-
src/kronika/adapters/api/web/app.js     | 100 +++++++++++----------
src/kronika/adapters/api/web/index.html |  12 +--
src/kronika/adapters/api/web/styles.css |  31 +++++++
tests/kronika_ui.test.js                | 148 +++++++++++++++++++++++++++-----
5 files changed, 215 insertions(+), 80 deletions(-)
```

## Validation

`git diff --check` was clean before the commit, and `git diff --cached --check` was clean. `git status --short` after the commit is empty.

```text
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 65772c6028c07edcab47b6928dbb31e30876c70a
```

PASS. The gate also printed `WARN sanitized inherited environment classes: GIT_CONFIG_VALUE_0 SSH_AUTH_SOCK PATH GIT_CONFIG_KEY_0 GIT_CONFIG_COUNT`. That warning did not fail the gate.

```text
node --test tests/kronika_ui.test.js tests/gallery_still_image_render.test.js tests/gallery_gif_inline_toggle.test.js tests/gallery_details_playback_handoff.test.js tests/cover_frontend.test.js
```

55 passed, 0 failed.

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 65772c6028c07edcab47b6928dbb31e30876c70a --operation test-focus -- tests/contract/test_local_web_application.py -k 'kronika_shell or details or persistent_preview or initial_card or available_cards or gallery' -q -p no:cacheprovider
```

43 passed, 164 deselected.

## Tests

Updated:

- `personal history and the timeline use separate endpoints`
- `question history and non-media cards never request previews`
- `superseded Timeline and History requests cannot repaint a departed view`

Added:

- `History is one Questions chronicle and the records address folds back`
- `History question rows keep links, glyphs and private text`

The fold test checks that `#/history/records?offset=24` is the History route at `/history` with that offset, that the markup has one chronicle and no Records tab, and that the History grid, narrow wrap, hover, and reduced-motion rules are present. The row test follows `#/history/records?offset=24` to `#/history?offset=24`, focuses the History heading, requests only `/api/research-requests` with that offset, and checks saved and unfinished links, Search and Research, the status glyphs, Private, and a carried Household · Approved value. Timeline preview, Retry, identity, and pagination tests still pass.

## Residual risk

The node harness does not paint 320 px or 390 px. Rendered acceptance remains the Cooperator's after a later deployment. The personal-request payload cannot show a real publication state, so the ordinary row says Private. The old History card-preview CSS remains because the thumbnail selector contract still counts those History-prefixed rules; the Questions list does not render those previews.

## Smallest next step

Orchestrator verifies commit `e6b26eb9ae16f1b67f8f23e55dfb20c7c6f218dd`. A later separate grant can publish it and refresh the NUC so the Cooperator can judge the rendered History page. This PASS is not that deployment and not acceptance.

Resolved Execution Issues / Near-Misses: none

Pre-Existing Failure Classification: none

Authority expiry: submission of this terminal report ends this exchange's authority. No autonomous continuation, acceptance, publication, deployment, or logical-whole closure is granted.

Orchestration critique:
MEASURED: none
LEAD: none
