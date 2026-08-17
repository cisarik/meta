# Authoritative Prompt for Fresh Worker 11

## FrameNest × X Meme Browser Companion MVP — Live reply Attach and Save-glyph honesty

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

Worker 10 claimed `implementation-PASS` at
`cfbc45dbe8627c3b048cca366964467703dd65e5`. That authority is expired. Live
Brave/X from the COOPERATOR:

1. Media hover **+** bottom-right: **PASS**.
2. Reply composer: **no FrameNest button** after clicking into "Post your
   reply": **FAIL**.
3. Clicking **+** (the visible media overlay) turns it into a **red ×**:
   **FAIL** as UX. That is the Save failed glyph after `SAVE_POST`; it must
   not look like a close control. Do not "fix" NUC / `X_REQUEST_NOT_CONFIGURED`.

This is not a continuation of Worker 10. Do not resume any prior Worker chat.
Do not enter Native Plan Mode.

```text
Role: WORKER
Logical whole identity: framenest-x-meme-browser-companion-mvp
Worker session ordinal: 11
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: FN-X-MEME-COMPANION-UX-REPLY-ATTACH-11
Task type: bounded visual-language correction
Native planning mode: not-used
Evidence posture: non-independent
Independence required: no
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
Continuity anchor: none — do not resume Worker 10
Prior authorities: expired
```

```text
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: cfbc45dbe8627c3b048cca366964467703dd65e5
Changed-path allowlist: Section 11
Independence required: no
```

```text
Acceptance candidate: cfbc45dbe8627c3b048cca366964467703dd65e5
Acceptance owner map: composer Attach discovery/re-injection; Save overlay glyph on failure; fixture; tests; operator note
Acceptance allowlist: Section 11
Acceptance risk claims: inline reply Attach survives X re-render and is visible on composer focus; Save overlay keeps a plus glyph (failed uses title/border, not ×); no tweetButton; no Post/auto-submit; SAVE_POST payload unchanged
Acceptance independence: not-required
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: none
```

Reasoning recommendation: High. Live X reply DOM is deep, re-rendered, and
the current `findComposerChrome` / `findComposerTextRow` / WeakSet skip is
the confirmed miss. Do not silently downgrade. Do not use Extra High or Max.

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
/home/agile/meta/projects/framenest/03/03-framenest-x-meme-browser-companion-mvp/11_report_00.md
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

Parked: NUC `X_REQUEST_NOT_CONFIGURED`, static photos, per-asset Save, full
FrameNest web in the side panel.

---

## 3. Capability handshake

Fresh session. Record requested vs observed model, High reasoning, Native
planning mode `not-used`. Push / NUC / Python / AP mutation unauthorized.
Do not print `SSH_AUTH_SOCK`.

---

## 4. Baseline

```text
Canonical repository: /home/agile/Projects/framenest
Branch: feat/x-meme-browser-companion
Exact baseline: cfbc45dbe8627c3b048cca366964467703dd65e5
Baseline parent: 9cec59803a0c00d15e6a1fb84a651ec667236508
Baseline tree: 9298bc7c1f34eb44243a82b1c7b13dc1d48e7a1e
Baseline subject: fix: open attach picker as an in-page popup above the composer
Pinned AP gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

`git fetch` forbidden. Stop if HEAD is not the baseline. Do not push.

---

## 5. Confirmed live defects (read the code)

Read `extension/content/x_adapter.js` `findComposerChrome`,
`findComposerTextRow`, `injectAttach`, `scan`, Save `failed` SVG.

Causal hypotheses the Worker must address (not optional):

1. **React wipe:** `injected` WeakSet skips a composer after the first
   inject even if X replaced the textarea tree and the button is gone.
   Re-inject when the attach node is no longer in `document`.
2. **Chrome miss:** ancestor walk `hops < 12` plus requiring
   `[data-testid='toolBar']` fails on inline reply. Raise the hop budget.
   Treat chrome as an ancestor that contains the editable **and** either a
   toolbar, a file input, or the native media-button row. Do not require
   the fixture-only `[data-framenest-composer-chrome]` in production.
3. **Text-row miss:** `findComposerTextRow` returns null when the walk
   lands on the editable itself (`isEditableComposerNode` → null). Live X
   often has the contenteditable as the only row child. Use the
   **non-editable parent** of the textbox (avatar + "Post your reply"
   row). Never append inside `contenteditable`. Insert the button as a
   sibling of the textbox, `position: absolute; right: 0` on that parent.
4. **Do not `markStale` the whole page** because one reply composer has no
   file input. Skip that composer.
5. **Save failed glyph:** `kind === "failed"` draws an × in danger red.
   Keep the **plus** glyph. Communicate failure with `aria-label` / `title`
   and optional danger border/color. Busy may dim or spin without replacing
   the plus with ×. Do not change SAVE_POST.

Keep: in-page popup above Attach (`openAttachPopup`), WAR as already
committed, media Save bottom-right hover, no `openPicker` on attach click,
no `tweetButton`.

---

## 6–7. Gate and routes

Record Git identity. JS only:

```text
node --test tests/x_companion_extension.test.js
```

No pytest, no `ap exec`, no live x.com scrape.

---

## 8. Goal

One local commit so a focused inline reply shows a green **+** on the right
of "Post your reply", click still opens the in-page picker popup, and media
Save never turns into a red ×.

---

## 9. Required behavior

Keep adapter contract version `1`. You may add frozen selectors (e.g.
`[aria-label='Post your reply']`, richer toolbar signals) without a Post
selector.

Attach visibility remains **focus-based, not hover**: show when the
composer chrome or editable receives `focusin`, or while the popup is open.

Tests must fail if:

- `injectAttach` still returns permanently after WeakSet without checking
  that the attach node is still in the document;
- `findComposerTextRow` still returns null when the editable's parent is
  the only row (add a fixture case: chrome contains only contenteditable +
  toolbar, no `data-framenest-composer-text-row`);
- Save `failed` SVG path still draws the × pair (`M8 8l8 8` / `M16 8l-8 8`)
  as the overlay glyph;
- `tweetButton` / `form.submit` / `openPicker` on attach click returns;
- media Save is no longer `bottom`/`right`.

Short `docs/X_COMPANION.md` note only.

---

## 10–11. Authority and allowlist

```text
extension/content/x_adapter.js
extension/content/x_adapter_contract_v1.js
tests/x_companion_extension.test.js
tests/support/x_fixtures/composer.html
docs/X_COMPANION.md
```

Optional fixture-only extra file is not allowed. Do not edit
`manifest.json` unless a selector change requires it — it should not.

---

## 12. Negative authority

No Python, NUC, SAVE_POST shape change, X CDN fetch, Gallery files, WAR
expansion, auto-Post, push, fetch, amend, `git add .`, `.ap/` mutation,
Meta except the report, logical-whole closure.

---

## 13. Git

One commit on existing `feat/x-meme-browser-companion`. Example:

```text
fix: keep reply Attach after X re-renders the composer
```

---

## 17. Report and expiry

`11_report_00.md` starts with `### Report for ORCHESTRATOR_CHAT`, echoes
coordinates, SHAs, how re-inject and text-row/chrome discovery work, that
failed Save keeps a plus, commands/exits, `Logical-whole closure:
not-closed`, `Report justification: new-mutation`.

Next step: Michal reloads, clicks into inline reply, looks for + on the
right of the placeholder, clicks it for the popup; media + must stay a
plus after click (title may say failed).

---

## 18. Stop

Stop if HEAD is not baseline, allowlist is insufficient, or a Post selector
/ live x.com scrape / NUC fix appears required.

---

## 19. Authority summary

Worker 11 may correct live reply Attach discovery/re-injection and Stop
painting Save failure as a red ×, from
`cfbc45dbe8627c3b048cca366964467703dd65e5`, one local commit,
`11_report_00.md`. It may not enable X acquisition on the NUC or close the
whole.
