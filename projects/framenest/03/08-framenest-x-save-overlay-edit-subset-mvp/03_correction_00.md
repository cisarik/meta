# Authoritative Prompt for Fresh Worker 03

## FrameNest × X Save Overlay — live Title leak, compact Tags-first layout, quiet iframe

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

Worker 02 closed implementation-PASS at
`d7fa9352285651018dd4c5e3bcdb04e2975e74f5`. That authority is expired. Do not
resume Worker 01–02. Do not enter Native Plan Mode. Do not reopen catalog
handoff, ADR-0065 meaning, picker, Attach, Analyze, origins, NUC, or W2.

The COOPERATOR live-tested Reload-unpacked Save on 2026-08-22. Screenshots
show: Title field value **Save to FrameNest** on image posts; Description above
Tags with a large empty region above Save; Description already has a scrollbar
(keep that); Brave Errors **Blocked autofocusing on a `<input>` in a
cross-origin subframe** pointing at `ui/save.html` Title (line 17). One error
URL still showed `&media=image` (stale unpacked hash from the previous whole;
current `openSavePopup` is `#url=` only — keep it that way).

Root cause already verified by the ORCHESTRATOR (do not re-litigate):

1. **Title leak.** `postTextPrefillFrom(..., button.parentElement)` then
   `accessibleNameFrom(host)` rejects generic `img[alt]` (`Image`) and next
   queries `[aria-label]` / `[title]` on that host. The FrameNest Save control
   lives in that host with `aria-label="Save to FrameNest"` (`SAVE_NAME`).
   Image posts therefore prefill the overlay Title with the **button name**,
   not alt and not the tweet. Existing tests never placed a companion Save
   button inside the photo host.
2. **Tall modal.** `positionSavePopup` sets host height to
   `max(240, min(720, viewport, 400 + descriptionHeight))` with
   `descriptionHeight` 120–320. Inner `.fields` is `flex: 1 1 auto` against
   `html, body, main, form { height: 100% }`, so unused space collects above
   Save. Cooperator: hug content; grow only when selected **tag chips** wrap;
   Description stays a **fixed** scrollable field.
3. **Field order.** Cooperator: Title → Tags (search + chips) → Description →
   Save so the tag dropdown overlays Description, not empty chrome.
4. **Autofocus Errors.** HTML `autofocus` and on-open `.focus()` were already
   removed; Brave still focuses the first text control when the
   `chrome-extension://` iframe loads on `https://x.com`. Stop that without a
   shadow-DOM rewrite.

Your task is one bounded local correction of those live defects, tests, one
commit, the terminal report, then stop.

If Extra High cannot be provided, or Native Plan Mode is on, stop `BLOCKED`.
Do not use Max.

```text
Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-x-save-overlay-edit-subset-mvp
Prior logical whole identities:
  framenest-x-meme-browser-companion-mvp
  framenest-x-companion-save-alias-mvp
  framenest-x-companion-save-category-mvp
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: FN-X-SAVE-OVERLAY-LIVE-COMPACT-03
Task type: bounded live Save overlay correction
Native planning mode: not-used
Reasoning recommendation: extra-high
Evidence posture: non-independent
Independence required: no
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
Continuity anchor: none — do not resume Worker 02
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
Exact baseline: d7fa9352285651018dd4c5e3bcdb04e2975e74f5
Changed-path allowlist: Section 7
Implementation boundaries: Sections 3, 4, 5, and 6
Independence required: no
```

```text
Evidence tier: E1
Evidence tier basis: reversible Save overlay UX and content-script prefill filter; no schema; no new route; no production mutation
Authorized implementation stages: Title leak + compact Tags-first layout + quiet iframe; tests; one local commit
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
Downloadable prompt filename: 03_correction_00.md
Destination path: projects/framenest/03/08-framenest-x-save-overlay-edit-subset-mvp/03_correction_00.md
Archival: wait-for-report
```

Write only:

```text
/home/agile/meta/projects/framenest/03/08-framenest-x-save-overlay-edit-subset-mvp/03_report_00.md
```

Do not edit `03/07-*` duplicates, `00_handout.md`, Worker 02 files, or FrameNest
paths outside Section 7. If the report file cannot be written, return it in
chat verbatim.

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
commit: d7fa9352285651018dd4c5e3bcdb04e2975e74f5
parent: 5c5e29c018fee829a4f42b68293bb12239743238
tree: e6c076e307a4349c7f64cb9ccdb0117733db55cb
subject: docs: record X save overlay canonical seed
.ap gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Working tree: expected clean
Upstream: none
```

Do not fetch, switch, stash, reset, or clean. Stop `BLOCKED` if HEAD is not
`d7fa935` (unless only this Worker’s later commit). Preserve unrelated dirty
state.

Public refs (ls-remote only, no fetch) expected:

```text
cisarik/framenest refs/heads/main  045f33b44897a6f3949cc515792336396f1d33a1
cisarik/ap        refs/heads/main  9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

If public `main` advanced, inspect read-only; stop only on material conflict.

Canonical Python route (`--baseline` is `d7fa935…` until your commit, then the
new SHA):

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline <EXACT_AUTHORIZED_COMMIT>
./.ap/ap exec --root /home/agile/Projects/framenest --baseline <EXACT_AUTHORIZED_COMMIT> --operation test-focus -- <tests> -q -p no:cacheprovider
```

This correction is JS-only. Do **not** run the full Python suite. Do not invoke
raw `python` / `.venv` / `poetry run`.

```text
node --test tests/x_companion_extension.test.js tests/x_acquisition_cockpit.test.js
```

NUC gate is not activated. No browser Reload, no signed-in X.

If Extra High or Plan Mode `not-used` cannot be observed, stop `BLOCKED`.

---

## 3. Required reading

- `AGENTS.md`
- `.ap/AP.md`, `.ap/AP_WORKER.md`
- `docs/WORKER_EXECUTION_CONTRACT.md`
- `extension/content/x_adapter.js` (`SAVE_NAME`, `accessibleNameFrom`,
  `postTextPrefillFrom`, `openSavePopup`, `positionSavePopup`)
- `extension/ui/save.html`, `save.js`, `save.css`
- `tests/x_companion_extension.test.js` (prefill + Edit-media subset tests)

Spot-check before mutation: `save.html` still Title then Description then Tags;
`accessibleNameFrom` still queries `[aria-label]` without skipping
`[data-framenest-companion]`; `positionSavePopup` still uses `400 + textareaHeight`.

---

## 4. Accepted correction contract

Do not invent a second architecture.

### 4.1 Title must not be SAVE_NAME

When collecting accessible names from the clicked media host:

- Ignore nodes with `data-framenest-companion` (the Save `+` and any companion
  chrome).
- Ignore `aria-label` / `title` / `alt` equal to `SAVE_NAME` (`Save to FrameNest`)
  or the failed-Save names from `reduceXSaveOutcome`.
- Keep the accepted chain: non-generic tile alt / media accessible name, else
  useful tweet sentence, else **empty** Title (server `x_title_from_post_post`
  after catalog). Never fall back to the popup heading, `document.title`,
  iframe `title`, or the Save button name.

Add a MiniDom test: photo host contains `img[alt=Image]` **and** a
`button[data-framenest-companion=save][aria-label=Save to FrameNest]` **and**
tweet text. Title must be the useful tweet sentence, **not** `Save to FrameNest`.
A second case with generic alt, companion button, and **no** tweet text must
yield empty Title.

### 4.2 Order: Title, Tags, Description, Save

Swap Description and Tags in `save.html` (labels, inputs, selected-chips,
status). Keep website-like labels. Tag dropdown remains `position: absolute`
on `.tag-search-panel` so it overlays Description, not a scrolling fieldset.
Do not clip `.fields` with `overflow: hidden`.

### 4.3 Compact host; chips grow; Description does not

Cooperator: the modal is unnecessarily tall. Description that is long must
**scroll inside the textarea**. Selected tags wrapping may grow the popup.

Binding:

- Description textarea is a **fixed** height (use **120px**; keep
  `overflow-y: auto; resize: none`). Do **not** set textarea height from tweet
  `getBoundingClientRect`. Do not grow the iframe when Description is long.
- Remove the `400 + descriptionHeight` host formula. Inner layout must **hug
  content** (`html/body/main/form` must not force `height: 100%` empty flex
  growth). `.fields` must not eat leftover viewport.
- After load, after adding/removing tag chips, and on chip wrap, the iframe
  measures its content height and `postMessage`s a bounded `size` (or reuse
  the existing handshake envelope with `action: "size"`) to the parent. Parent
  sets the host box to that height, clamped to `viewport - 16`, width unchanged
  (280–360). Dropdown open state must **not** expand the host (absolute overlay).
- Empty Tags (search only, no chips) is the compact baseline. Each row of chips
  may increase host height.
- Keep the green `#00ff41` frame, one filled Save, failed-Save plus, hidden
  Edit image, picker/Attach freeze.

You may drop `descriptionHeight` from prefill if unused. Update tests that
currently assert `descriptionHeight === 320` from a tall tweet rect.

### 4.4 Quiet cross-origin iframe

- Keep iframe `src` as `save.html#url=` only. Never restore `&media=`.
- `iframe.tabIndex = -1`. Never call `iframe.focus()`, Title `.focus()`, or
  Description `.focus()` on open, on `ready`, or on `prefill`.
- Give Title, Description, and tag-search `tabindex="-1"` until the **first
  pointerdown or keydown inside the overlay**, then set `tabindex="0"` (or
  remove the attribute). User-initiated `tagSearch.focus()` after choosing a
  tag may remain **after** that gesture.
- No HTML `autofocus`. `autocomplete="off"` stays.
- Tests: `save.html` has no `autofocus`; `save.js` does not call
  `title.focus` / `description.focus` / `focusCheckedCategory`; adapter has no
  `iframe.focus()`; hash builder has no `media=`.

Do not rewrite WAR to shadow DOM. Do not promise keyboard-only Save without a
click inside the overlay.

---

## 5. Negative authority

Picker, Attach, side panel, website `#metadata-dialog`, backend, Alembic,
ADR bodies, PRODUCT/SPEC/ROADMAP (no living-doc pass unless a one-line
X_COMPANION sentence is strictly required — default: **do not** edit docs),
push, NUC, provider, signed-in X, Reload-unpacked, Max, Plan Mode, sub-agents,
new companion routes, create-tag, Analyze.

---

## 6. Git

One local commit on `feat/x-meme-browser-companion`. No amend of `d7fa935`.
No push, fetch, rebase, stash, reset, clean, or hook skip. HEREDOC message,
for example:

```text
fix: keep X save title off the plus and hug tag chips
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

Run also (do not modify unless a named assertion must change because of 4.3):

```text
node --test tests/x_companion_extension.test.js tests/x_acquisition_cockpit.test.js
```

Cockpit/picker tests must still pass. Do not change picker files.

---

## 8. Stop / report

Stop `BLOCKED`/`PARTIAL` if you would need backend, docs ADR, picker thaw, a
second commit, Plan Mode, or live X.

`PASS` only if: parent is `d7fa935`; working tree clean; JS owners  all pass
including the new Title-leak MiniDom cases; radios stay gone; POST still omits
`content_category`; no `iframe.focus` / HTML autofocus; hash has no `media=`.

```text
Logical whole identity: framenest-x-save-overlay-edit-subset-mvp
Worker session ordinal: 03
Worker exchange ordinal: 01
```

Phase-qualified result: implementation-PASS (correction). Closure: not-closed.
Justification: `new-mutation`. Authority expires at the terminal report.

Smallest next step: Orchestrator asks Michal to Reload unpacked again.

After `03_report_00.md`, stop.
