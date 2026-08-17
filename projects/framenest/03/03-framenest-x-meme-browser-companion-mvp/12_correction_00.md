# Authoritative Prompt for Fresh Worker 12

## FrameNest × X Meme Browser Companion MVP — Float reply Attach; no host spinners

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

Worker 11 claimed `implementation-PASS` at
`3e354b0785556235d26943470689a7bd0bddbb9d`. That authority is expired.

Live Brave/X from the COOPERATOR:

- Clicking into "Post your reply" did **not** show the green **+** at first.
  Strange **up/down spinner arrows** appeared in that row instead.
- After clicking around that spot, the **+** appeared.
- Clicking **+** opened the **correct** in-page Search memes popup. Keep that.
- Side panel unchanged: expected. Do not restyle it.
- The second popup (Save-to-gallery alias form + admin "Analyze by AI") still
  does not open: **out of scope**. Do not build it.

The spinner is a live defect from injecting Attach **into** X's text row and
setting `position: relative` on that host node (`ensureContainingBlock(textRow)`),
which can reveal a native number-input spinner. The delayed **+** is the same
class of defect: visibility depends on `focusin` on composer chrome after a
fragile in-row mount.

This is not a continuation of Worker 11. Do not resume any prior Worker chat.
Do not enter Native Plan Mode.

```text
Role: WORKER
Logical whole identity: framenest-x-meme-browser-companion-mvp
Worker session ordinal: 12
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: FN-X-MEME-COMPANION-UX-FLOAT-ATTACH-12
Task type: bounded visual-language correction
Native planning mode: not-used
Evidence posture: non-independent
Independence required: no
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
Continuity anchor: none — do not resume Worker 11
Prior authorities: expired
```

```text
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: 3e354b0785556235d26943470689a7bd0bddbb9d
Changed-path allowlist: Section 11
Independence required: no
```

```text
Acceptance candidate: 3e354b0785556235d26943470689a7bd0bddbb9d
Acceptance owner map: Attach mount/position/visibility; injected companion CSS; fixture/tests; operator note
Acceptance allowlist: Section 11
Acceptance risk claims: Attach is not a child of the X text row; no position:relative on X composer nodes for Attach; + visible on first focus of Post your reply; click still opens the existing in-page picker popup; no tweetButton; no metadata/Save-alias popup
Acceptance independence: not-required
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: none
```

Reasoning recommendation: High. This is live X composer CSS leakage. Do not
silently downgrade. Do not use Extra High or Max.

```text
COOPERATOR: Michal
ORCHESTRATOR: ORCHESTRATOR_CHAT
WORKER: this fresh bounded correction session
```

Internal delegation is inactive. Report begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

---

## 1. Meta write

Write only:

```text
/home/agile/meta/projects/framenest/03/03-framenest-x-meme-browser-companion-mvp/12_report_00.md
```

Do not read Meta. Do not stage or commit Meta.

---

## 2. Communication

```text
Orchestrator: ORCHESTRATOR_CHAT
Worker prompt language: professional English
Worker report language: professional English
Direct-user Slovak presentation: Orchestrator-owned
Report header: ### Report for ORCHESTRATOR_CHAT
```

Parked (do not implement): Save-to-gallery alias popup; per-user title/tags;
Analyze by AI in the extension; NUC `X_REQUEST_NOT_CONFIGURED`; static photos;
per-asset Save; full FrameNest web in the side panel.

---

## 3. Capability handshake

Fresh session. High reasoning. Native planning mode `not-used`. Push / NUC /
Python / AP mutation unauthorized. Do not print `SSH_AUTH_SOCK`.

---

## 4. Baseline

```text
Canonical repository: /home/agile/Projects/framenest
Branch: feat/x-meme-browser-companion
Exact baseline: 3e354b0785556235d26943470689a7bd0bddbb9d
Baseline parent: cfbc45dbe8627c3b048cca366964467703dd65e5
Baseline tree: e58e46800d0f7abb34fb61bad72bf01a96aaf970
Baseline subject: fix: keep reply Attach after X re-renders the composer
Pinned AP gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

`git fetch` forbidden. Stop if HEAD is not the baseline. Do not push.

---

## 5. Required correction

Read `extension/content/x_adapter.js` (`injectAttach`,
`ensureContainingBlock`, `bindComposerAttachVisibility`, attach CSS in
`COMPANION_STYLE`).

### 5.1 Do not mount Attach inside the X text row

Stop `textRow.appendChild(button)` and stop `ensureContainingBlock(textRow)`
for Attach. That relative containing block is the live cause of the up/down
spinner beside the field.

Mount the Attach control on `document.documentElement` (or a dedicated
companion layer node), **not** inside the contenteditable and **not** inside
the X placeholder row.

Position with `position: fixed` using `getBoundingClientRect` of the focused
reply/compose textbox: vertically centered on that field, flush to its
**right** edge (a few px inset). Reposition on `resize`, capturing `scroll`,
and on the existing MutationObserver scan while visible. Same black / green
plus language as today (`appearance` / `-webkit-appearance: none`; also hide
`::-webkit-inner-spin-button` / `::-webkit-outer-spin-button` on the control
if any stylesheet could apply).

Keep `data-framenest-companion="attach"`, `aria-label` `Attach from FrameNest`,
halt host click, ACK then `openAttachPopup` (existing in-page picker). Do not
send `openPicker`.

### 5.2 First-focus visibility

Show the **+** on the **first** `focusin` / focus of
`[data-testid='tweetTextarea_0']` or `[aria-label='Post your reply']` (capture
on the editable, not only a distant chrome node). Keep it visible while that
composer holds focus or the picker popup is open. Hide when focus leaves and
the popup is closed.

Re-bind if X replaces the textarea; do not skip forever because of WeakSet if
the floating button is gone.

Missing file input: skip that composer; do not `markStale` the page.

### 5.3 Do not touch

- Media hover Save (bottom-right plus; no × glyph).
- Picker popup internals except if a tiny CSS tweak is required for the
  floating button.
- Side panel / full Gallery iframe.
- Metadata / alias / Analyze by AI popup.
- `manifest.json` WAR (already match-limited).
- SAVE_POST payload.
- `tweetButton`.

### 5.4 Tests

Update `tests/x_companion_extension.test.js` and the fixture so they fail if
Attach is still `textRow.appendChild` / `ensureContainingBlock(textRow)` for
the attach path; if attach CSS is still `position: absolute` inside the host
row as the only placement; if `openPicker` / `tweetButton` / `form.submit`
returns.

Short `docs/X_COMPANION.md` note: Attach floats on the focused reply field;
it is not inserted into the X input row.

---

## 6–7. Gate and routes

```text
node --test tests/x_companion_extension.test.js
```

No pytest, no `ap exec`, no live x.com scrape.

---

## 8. Goal

One local commit: first click into "Post your reply" shows only the green **+**
on the right of that field (no spinner), and that **+** still opens the
existing Search memes popup.

---

## 9–11. Allowlist

```text
extension/content/x_adapter.js
extension/content/x_adapter_contract_v1.js
tests/x_companion_extension.test.js
tests/support/x_fixtures/composer.html
docs/X_COMPANION.md
```

---

## 12. Negative authority

No Python, NUC, metadata popup, Gallery files, WAR expansion, auto-Post,
push, fetch, amend, `git add .`, `.ap/` mutation, Meta except the report,
logical-whole closure.

---

## 13. Git

One commit on existing `feat/x-meme-browser-companion`. Example:

```text
fix: float reply Attach instead of injecting into the X text row
```

---

## 17. Report

`12_report_00.md` starts with `### Report for ORCHESTRATOR_CHAT`, echoes
coordinates, SHAs, mount/position/focus rules, commands/exits,
`Logical-whole closure: not-closed`, `Report justification: new-mutation`.

Next step: Michal reloads, clicks once into Post your reply, expects the +
immediately and no up/down arrows, then clicks + for the search popup.

---

## 18–19. Stop and summary

Stop if HEAD is not baseline or a Post selector / live scrape / metadata
popup appears required.

This prompt authorizes Worker 12 to float the reply Attach control off the X
text row from `3e354b0785556235d26943470689a7bd0bddbb9d`, one local commit,
`12_report_00.md`. It does not authorize the Save-alias popup or closure.
