# Authoritative Prompt for Fresh Worker 04

## FrameNest × X Save Overlay — kill leftover iframe scroll, Enter submits, strip focus machinery

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

Worker 03 closed implementation-PASS at
`143c1e475046580627cb4e7859d5c73555ae5d58`. That authority is expired. Do not
resume Worker 01–03. Do not enter Native Plan Mode. Do not reopen catalog
handoff, ADR-0065, picker, Attach, Analyze, origins, NUC, companion inbox, or
NVIDIA NIM.

The COOPERATOR live-tested Reload-unpacked Save on 2026-08-22 after Worker 03.
Three remaining overlay defects, and only these, are in scope:

1. **Outer iframe scrollbar of a few pixels.** Description’s inner scrollbar is
   wanted. The host iframe must not scroll. Tighten header / form chrome
   (the “Save to FrameNest” title padding is the named example) and make the
   host height match true content including the green frame border so the
   leftover outer bar disappears.
2. **Enter must submit Save.** Title already maps Enter → `submitSave`. That is
   not enough if focus is elsewhere. Enter must save except where a newline or
   tag-accept is required (Section 4.2).
3. **Remove focus machinery completely.** Brave still logs **Blocked
   autofocusing on a `<input>` element in a cross-origin subframe** pointing at
   `ui/save.html` Title. The Cooperator does not want another tabindex dance,
   `iframe.tabIndex`, on-open `.focus()`, or `armOverlayFocus`. Delete that
   logic. Do not invent a replacement focus strategy. Honest residual: Brave
   may still log the same warning if the browser itself tries to focus the
   first text control in a `chrome-extension://` iframe on `https://x.com`.
   That residual is accepted for this correction if FrameNest no longer
   requests focus.

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
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: FN-X-SAVE-OVERLAY-SCROLL-ENTER-NOFOCUS-04
Task type: bounded live Save overlay correction
Native planning mode: not-used
Reasoning recommendation: extra-high
Evidence posture: non-independent
Independence required: no
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
Continuity anchor: none — do not resume Worker 03
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
Exact baseline: 143c1e475046580627cb4e7859d5c73555ae5d58
Changed-path allowlist: Section 7
Implementation boundaries: Sections 3, 4, 5, and 6
Independence required: no
```

```text
Evidence tier: E1
Evidence tier basis: reversible Save overlay UX; no schema; no new route; no production mutation
Authorized implementation stages: hug height + Enter submit + strip focus; tests; one local commit
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
Downloadable prompt filename: 04_correction_00.md
Destination path: projects/framenest/03/08-framenest-x-save-overlay-edit-subset-mvp/04_correction_00.md
Archival: wait-for-report
```

Write only:

```text
/home/agile/meta/projects/framenest/03/08-framenest-x-save-overlay-edit-subset-mvp/04_report_00.md
```

Do not edit `03/07-*`, `03/09-*`, `00_handout.md`, Worker 01–03 files, or
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
commit: 143c1e475046580627cb4e7859d5c73555ae5d58
parent: d7fa9352285651018dd4c5e3bcdb04e2975e74f5
tree: 8d802cc29c3884a357b3652a0890d487b266dc27
subject: fix: keep X save title off the plus and hug tag chips
.ap gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Working tree: expected clean
Upstream: none
```

Do not fetch, switch, stash, reset, or clean. Stop `BLOCKED` if HEAD is not
`143c1e4` (unless only this Worker’s later commit). Preserve unrelated dirty
state.

Public refs (ls-remote only, no fetch) expected:

```text
cisarik/framenest refs/heads/main  045f33b44897a6f3949cc515792336396f1d33a1
cisarik/ap        refs/heads/main  9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

If public `main` advanced, inspect read-only; stop only on material conflict.

Canonical Python route (`--baseline` is `143c1e4…` until your commit, then the
new SHA):

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline <EXACT_AUTHORIZED_COMMIT>
```

This correction is JS-only. Do **not** run the full Python suite. Do not invoke
raw `python` / `.venv` / `poetry run`. Do not use `ap exec` unless a named
Python test becomes necessary; it should not.

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
- `extension/ui/save.html`, `save.js`, `save.css`
- `extension/content/x_adapter.js` (`openSavePopup`, `positionSavePopup`,
  `action === "size"`)
- `tests/x_companion_extension.test.js` (overlay hug, tabindex, Enter)

Spot-check before mutation: `save.html` still has `tabindex="-1"` on Title,
tag-search, and Description; `save.js` still has `armOverlayFocus`;
`x_adapter.js` still sets `iframe.tabIndex = -1`; `.header` padding is
`10px 10px 8px 12px`; host `.frame` has `border: 1px solid #00ff41` while
`contentHeight` is the inner form box.

---

## 4. Accepted correction contract

Do not invent a second architecture. Field order stays **Title → Tags
(search + chips) → Description → Save**. Do not swap Tags and Description
again. Radios stay absent. POST stays `{url, alias}` without
`content_category`. Iframe hash stays `#url=` only.

### 4.1 Kill the few-pixel outer scrollbar

The Cooperator screenshot shows a vertical scrollbar on the Save iframe that
moves only a few pixels. Description’s own scrollbar is correct and must
remain (`textarea` fixed `120px`, `overflow-y: auto`, `resize: none`).

Binding:

- Reduce overlay chrome just enough that the compact empty-Tags baseline fits
  the host without an outer bar. The named lever is the “Save to FrameNest”
  header padding; you may also tighten `.fields` / `.actions` padding by a
  few pixels if measurement still overflows. Do not shrink Description below
  `120px`. Do not drop the green `#00ff41` frame.
- Host height comes from overlay `action: "size"`. Today `notifySize` sends
  `Math.ceil(form.getBoundingClientRect().height)`. The shadow `.frame` also
  has a 1px border, so the iframe viewport is smaller than the host box and
  the inner document scrolls by approximately that remainder. Fix the
  handshake so the **visible iframe client height is ≥ content height**.
  Legal tactics (use the smallest coherent set): include frame border in the
  parent height; send content height that the parent applies to the iframe
  content box rather than the bordered host; set overlay `html, body {
  overflow: hidden }` so subpixel remainder cannot show a bar; add at most
  2px slack if rounding still clips. Do not go back to
  `max(240, 400 + descriptionHeight)`.
- Dropdown open still must **not** expand the host (absolute overlay).
- Selected tag chips wrapping may still grow host height.
- Width unchanged (280–360). Clamp to `viewport - 16` remains.
- Pre-measure fallback `240` until the first positive `size` may remain if
  the first `size` then hugs.

Update MiniDom / source assertions that encode the old header padding or that
assume inner form height is applied 1:1 onto a bordered host.

### 4.2 Enter submits Save

Cooperator: Save must be possible with Enter.

Binding:

- **Description** (`textarea#description`): Enter inserts a newline. Do not
  submit. Keep existing Ctrl/Cmd+Enter on the form as submit.
- **Tag search**: if the suggestion list is open and a highlighted option
  exists, Enter still **adds that tag** (current behavior). Otherwise Enter
  **submits Save**.
- **Title**: Enter still submits (already implemented).
- **Everywhere else in the overlay** (Save button, close is not Enter, empty
  chrome, selected-tag chips): Enter submits Save unless the event target is
  Description without a modifier.
- Do not submit while `formBusy`.
- Escape still closes the tag list first, else cancels the overlay.

### 4.3 Strip focus machinery

Delete, do not comment-out:

- HTML `tabindex="-1"` on Title, Description, and tag-search.
- `overlayArmed`, `armOverlayFocus`, and the capturing `pointerdown` /
  `keydown` listeners that arm tabindex.
- `iframe.tabIndex = -1` in `openSavePopup`.
- Any remaining `iframe.focus()`, `title.focus()`, `description.focus()`, or
  `tagSearch.focus()` in the Save overlay path (`save.js` and `openSavePopup`).
  That includes `tagSearch.focus()` after `addTag`.
- Do **not** add HTML `autofocus`. `autocomplete="off"` stays.

Keep `tabindex="0"` on picker preview if it already exists; picker is out of
allowlist.

Tests must flip:

- `save.html` has no `autofocus` and no `tabindex="-1"` on the three Save
  fields.
- `save.js` does not contain `armOverlayFocus`, `title.focus`,
  `description.focus`, or `tagSearch.focus`.
- Adapter Save path does not assign `iframe.tabIndex` and does not call
  `iframe.focus()`.
- Hash builder still has no `media=`.

Do not rewrite WAR to shadow DOM. Do not promise keyboard-only Save without a
click inside the overlay. Do not treat a remaining Brave autofocus **log** as
a fail if FrameNest no longer requests focus.

---

## 5. Negative authority

Picker HTML/JS/CSS, Attach, side panel, website `#metadata-dialog`, backend,
Alembic, ADR bodies, PRODUCT/SPEC/ROADMAP/X_COMPANION, push, NUC, provider,
signed-in X, Reload-unpacked, Max, Plan Mode, sub-agents, new companion
routes, create-tag, Analyze, companion inbox, notifications, badge.

---

## 6. Git

One local commit on `feat/x-meme-browser-companion`. No amend of `143c1e4`.
No push, fetch, rebase, stash, reset, clean, or hook skip. HEREDOC message,
for example:

```text
fix: hug X save overlay height and submit on Enter
```

You may amend only that new commit if a hook auto-modifies files after it
succeeds.

---

## 7. Allowlist

- `extension/content/x_adapter.js`
- `extension/ui/save.html`
- `extension/ui/save.js`
- `extension/ui/save.css`
- `tests/x_companion_extension.test.js`
- Meta report path in Section 1

Run also (do not modify unless a named assertion must change because of
Section 4):

```text
node --test tests/x_companion_extension.test.js tests/x_acquisition_cockpit.test.js
```

Cockpit/picker tests must still pass. Do not change picker files.

---

## 8. Stop / report

Stop `BLOCKED`/`PARTIAL` if you would need backend, docs ADR, picker thaw, a
second commit, Plan Mode, live X, or a new focus workaround.

`PASS` only if: parent is `143c1e4`; working tree clean; JS owners all pass;
radios stay gone; POST still omits `content_category`; no HTML autofocus; no
`armOverlayFocus`; no Save-path `.focus()`; hash has no `media=`; Title →
Tags → Description → Save order unchanged.

```text
Logical whole identity: framenest-x-save-overlay-edit-subset-mvp
Worker session ordinal: 04
Worker exchange ordinal: 01
```

Phase-qualified result: implementation-PASS (correction). Closure: not-closed.
Justification: `new-mutation`. Authority expires at the terminal report.

INFOSEC R1 inline only. Independent R3 is not authorized.

Smallest next step: Orchestrator asks Michal to Reload unpacked and confirm
the outer scrollbar is gone and Enter saves.

After `04_report_00.md`, stop.
