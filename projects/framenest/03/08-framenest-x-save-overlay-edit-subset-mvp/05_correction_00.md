# Authoritative Prompt for Fresh Worker 05

## FrameNest × X Save Overlay — host Enter submits; quiet first input without Title autofocus

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

Worker 04 closed implementation-PASS at
`af348847608fbb1e546d6db5e116e7ee81bacd9e`. That authority is expired. Do not
resume Worker 01–04. Do not enter Native Plan Mode. Do not reopen catalog
handoff, ADR-0065, picker, Attach, Analyze, origins, NUC, companion inbox, or
NVIDIA NIM. Do not reopen Worker 04 hug/padding/`SAVE_FRAME_BORDER_Y` unless a
named assertion must stay green.

The COOPERATOR live-tested Reload-unpacked after Worker 04 (2026-08-22):

1. Brave Errors still shows **Blocked autofocusing on a `<input>` in a
   cross-origin subframe** on `ui/save.html` Title (line 17). One error URL
   still includes `&media=image`. Current `openSavePopup` is `#url=` only —
   that fragment is **stale Brave grouping**, not a restore-`media=` grant.
   The highlighted HTML matches Worker 04 (no `autofocus`, no `tabindex`).
2. **Enter in the open popup does not Save.**

ORCHESTRATOR root cause (do not re-litigate):

- Clicking `+` opens the iframe but **keyboard focus stays on the `+`** on
  `https://x.com`. Overlay `save.js` never sees the key. Host `onKey` handles
  only Escape. Default Enter on a focused `type="button"` **activates `+`**,
  which toggles `openSavePopup` and **closes** the dialog. That is why Enter
  “saves nothing”.
- Chromium then tries to autofocus the first focusable **`<input>`** in the
  `chrome-extension://` subframe. That is the Errors line, not missing Title
  `.focus()`. HTML `autofocus` and iframe-on-load `title.focus()` are blocked
  in this geometry; do not add them. `tabindex="-1"` on the three fields makes
  Title not the first autofocus candidate. Click still focuses a
  `tabindex="-1"` field. No `armOverlayFocus` dance.

The Cooperator asked whether Title focus is required again. **No.** Required:
host-document Enter while the popup is open must submit (and must not toggle
`+`). Title `.focus()` / `autofocus` stay forbidden.

Your task is one bounded local correction of those defects, tests, one commit,
the terminal report, then stop.

If Native Plan Mode is on, stop `BLOCKED`. Do not use Max. Extra High is
requested; if the client does not expose a measurable Extra High SKU, continue
only while Plan Mode stays off and Max is unused, and record that in the
handshake.

```text
Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-x-save-overlay-edit-subset-mvp
Prior logical whole identities:
  framenest-x-meme-browser-companion-mvp
  framenest-x-companion-save-alias-mvp
  framenest-x-companion-save-category-mvp
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: FN-X-SAVE-OVERLAY-HOST-ENTER-QUIET-INPUT-05
Task type: bounded live Save overlay correction
Native planning mode: not-used
Reasoning recommendation: extra-high
Evidence posture: non-independent
Independence required: no
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
Continuity anchor: none — do not resume Worker 04
Prior authorities: expired
Internal delegation posture: not-used
Accountable Worker: one WORKER
Material phase gate: no
Changed material axis: none
Routing reopened for: none
Unchanged axes reopened: none
Ordinary-only trigger: yes
Automatic model selection: off
Enhanced/maximum mode: not requested
Sub-agents/internal delegation: not-used
Worker topology: single-active
Explore-style task: not-used
```

```text
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: af348847608fbb1e546d6db5e116e7ee81bacd9e
Changed-path allowlist: Section 7
Implementation boundaries: Sections 3, 4, 5, and 6
Independence required: no
```

```text
Evidence tier: E1
Evidence tier basis: reversible Save overlay keyboard + quiet first input; no schema; no new route; no production mutation
Authorized implementation stages: host Enter submit + tabindex quiet inputs; tests; one local commit
Combined implementation envelope: allowed
Independent acceptance: not-required
Rollback or recovery checkpoint: local Git commit on feat/x-meme-browser-companion; no push
Activated stricter profile: none
Terminal implementation report point: after the commit and named tests, before visual re-acceptance
```

```text
COOPERATOR: Michal
ORCHESTRATOR: ORCHESTRATOR_CHAT
WORKER: this fresh correction session
```

```text
Canonical repository identity: https://github.com/cisarik/ap.git
Immutable version identity: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Declared variant: stable
Governing variants in effect: one
Declaration location: project governing rules
Rules from non-governing variants: none
Migration required: no
```

---

## 1. Trace and Meta write

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 05_correction_00.md
Destination path: projects/framenest/03/08-framenest-x-save-overlay-edit-subset-mvp/05_correction_00.md
Archival: wait-for-report
```

Write only:

```text
/home/agile/meta/projects/framenest/03/08-framenest-x-save-overlay-edit-subset-mvp/05_report_00.md
```

Do not edit `03/07-*`, `03/09-*`, `00_handout.md`, Worker 01–04 files, or
FrameNest paths outside Section 7. If the report file cannot be written, return
it in chat verbatim.

Terminal report begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Professional English. No Czech. No Slovak capsule.

---

## 2. Baseline gate

```text
Expected canonical root: /home/agile/Projects/framenest
Branch: feat/x-meme-browser-companion
commit: af348847608fbb1e546d6db5e116e7ee81bacd9e
parent: 143c1e475046580627cb4e7859d5c73555ae5d58
tree: 68f5e09eb7922f7c8dbac77941be22702b4573d3
subject: fix: hug X save overlay height and submit on Enter
.ap gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Working tree: expected clean
Upstream: none
```

Do not fetch, switch, stash, reset, or clean. Stop `BLOCKED` if HEAD is not
`af34884` (unless only this Worker’s later commit). Preserve unrelated dirty
state.

Public refs (ls-remote only, no fetch) expected:

```text
cisarik/framenest refs/heads/main  045f33b44897a6f3949cc515792336396f1d33a1
cisarik/ap        refs/heads/main  9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

If public `main` advanced, inspect read-only; stop only on material conflict.

Canonical Python route (`--baseline` is `af34884…` until your commit, then the
new SHA):

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline <EXACT_AUTHORIZED_COMMIT>
```

This correction is JS-only. Do **not** run the full Python suite. Do not invoke
raw `python` / `.venv` / `poetry run`.

```text
node --test tests/x_companion_extension.test.js tests/x_acquisition_cockpit.test.js
```

NUC gate is not activated. No browser Reload, no signed-in X, no provider.

If Native Plan Mode cannot stay `not-used`, stop `BLOCKED`.

---

## 3. Required reading

- `AGENTS.md`
- `.ap/AP.md`, `.ap/AP_WORKER.md`
- `docs/WORKER_EXECUTION_CONTRACT.md`
- `extension/content/x_adapter.js` (`createSaveControl`, `openSavePopup`,
  `closeSavePopup`, `requestSavePopupHandshake`, popup `onKey`)
- `extension/ui/save.html`, `save.js` (capturing Enter, host `message`)
- `tests/x_companion_extension.test.js`

Spot-check before mutation: popup `onKey` handles only Escape; `+` is
`type="button"` and keeps focus after click; `save.html` Title has no
`tabindex`; `openSavePopup` hash is `#url=` only; `save.js` already captures
Enter inside the iframe.

---

## 4. Accepted correction contract

Do not invent a second architecture. Keep Title → Tags → Description → Save,
radios absent, POST `{url, alias}` without `content_category`, hash `#url=`
only, hug height + `SAVE_FRAME_BORDER_Y`, Description `120px` inner scroll,
`html, body { overflow: hidden }`.

### 4.1 Host Enter must Save, must not toggle `+`

While the Save popup is open, the **x.com** capturing `keydown` (the existing
popup `onKey` next to Escape) must:

- On **Escape**: keep current behavior (close).
- On **Enter** (not composing): `preventDefault` + `stopPropagation` so the
  focused `+` is **not** activated, then ask the overlay to submit.

Reuse the existing handshake envelope. Add `action: "submit"` from
`source: "framenest-save-host"` via `iframe.contentWindow.postMessage` with
the same target origin as `requestSavePopupHandshake` (never `*`). Do not
invent a new `v:` protocol. `save.js` already accepts
`source === "framenest-save-host"`; handle `action === "submit"` by calling
existing `submitSave()` (no-op when `formBusy` or invalid URL, same as today).

Do **not** submit from the host when the key event target is the overlay
iframe itself if that would double-fire with the iframe’s own Enter handler
in a harmful way. `submitSave` is idempotent under `formBusy`; a benign
double call after the user has clicked into Title is acceptable. Stealing
Description newlines cannot happen from the host: those keys stay inside the
iframe and never reach x.com.

Keep iframe-internal Enter from Worker 04: Description newline; open
highlighted tag-suggestion adds the tag; otherwise submit.

Do not restore `media=` on the iframe hash.

### 4.2 Quiet Title without focusing it

Put `tabindex="-1"` back on Title, tag-search, and Description only. Click
still focuses them. Do **not** restore `armOverlayFocus`, `overlayArmed`,
capturing pointer/key arming, `iframe.tabIndex = -1`, `iframe.focus()`,
`title.focus()`, `description.focus()`, `tagSearch.focus()`, or HTML
`autofocus`.

`autocomplete="off"` stays. Close still restores focus to `+` on dismiss
(existing `closeSavePopup`).

Residual: if Brave still logs autofocus after this, record it as residual
only if FrameNest still has no `autofocus` and no overlay `.focus()`. Do not
add a third workaround.

### 4.3 Tests

Flip Worker 04 assertions that forbade `tabindex="-1"`. Require:

- `save.html` has `tabindex="-1"` on the three fields and no `autofocus`.
- `save.js` has no `armOverlayFocus` / `title.focus` / `description.focus` /
  `tagSearch.focus`; host message handles `action === "submit"` →
  `submitSave`.
- `openSavePopup` `onKey` handles Enter; posts `action: "submit"`;
  `openSavePopup` still has `#url=` and no `media=`.
- No `iframe.focus()` / `iframe.tabIndex` in the Save overlay path.

Keep existing hug / order / no-radio / no-`content_category` proofs.

---

## 5. Negative authority

Picker, Attach, side panel, website `#metadata-dialog`, backend, Alembic, ADR
bodies, living docs, push, NUC, provider, signed-in X, Reload-unpacked, Max,
Plan Mode, sub-agents, new companion routes, create-tag, Analyze, inbox,
notifications, badge. Do not change Worker 04 padding/height unless a test
fails for an unrelated reason you must not paper over by reverting hug.

---

## 6. Git

One local commit on `feat/x-meme-browser-companion`. No amend of `af34884`.
No push, fetch, rebase, stash, reset, clean, or hook skip. HEREDOC message,
for example:

```text
fix: submit X save on host Enter without title autofocus
```

You may amend only that new commit if a hook auto-modifies files after it
succeeds.

---

## 7. Allowlist

- `extension/content/x_adapter.js`
- `extension/ui/save.html`
- `extension/ui/save.js`
- `tests/x_companion_extension.test.js`
- Meta report path in Section 1

`save.css` is **not** in the allowlist. Do not touch it.

Run also (do not modify picker files):

```text
node --test tests/x_companion_extension.test.js tests/x_acquisition_cockpit.test.js
```

---

## 8. Stop / report

Stop `BLOCKED`/`PARTIAL` if you would need backend, Title `.focus()`, HTML
`autofocus`, picker thaw, a second commit, Plan Mode, or live X.

`PASS` only if: parent is `af34884`; working tree clean; JS owners all pass;
host Enter submits via `action: "submit"`; `tabindex="-1"` on the three
fields; no overlay `.focus()` / `autofocus` / `media=`; radios stay gone.

```text
Logical whole identity: framenest-x-save-overlay-edit-subset-mvp
Worker session ordinal: 05
Worker exchange ordinal: 01
```

Phase-qualified result: implementation-PASS (correction). Closure: not-closed.
Justification: `new-mutation`. Authority expires at the terminal report.

INFOSEC R1 inline only. Independent R3 is not authorized.

Smallest next step: Orchestrator asks Michal to Reload unpacked, Clear all in
Brave Errors, open Save, press Enter **without** clicking Title, and confirm
Save runs; then click Description and confirm Enter is still a newline.

After `05_report_00.md`, stop.
