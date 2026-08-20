# Authoritative Prompt for Fresh Worker 07

## FrameNest × X Companion Side Panel — Gallery 📎 must not lie “Attached”

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

Worker 06 produced NUC `deployment-PASS` at `045f33b…` / Alembic `0029`. That
authority is expired. Do not resume Worker 06. Do not deploy NUC. Do not enter
Native Plan Mode. Do not restyle Save, Attach float, picker, or side-panel
chrome.

The COOPERATOR focused **Post your reply**, then clicked Gallery **📎**. The
side panel printed **Attached**. The X reply composer received **no media**.

Root cause (do not relitigate): two separate “bound” notions.

1. Service worker `boundTabId` is set on **any** bindable X content-script
   message (including `RECOVER_INFLIGHT` on tab load). That is enough for
   `startAttach` to proceed.
2. Content-script `boundComposer.fileInput` is set **only when the user clicks
   the in-page floating Attach `+`**. Focus of Post your reply injects and
   shows that control but does **not** assign `boundComposer`.
3. Gallery 📎 streams via `chrome.tabs.connect` `framenest-attach`. On
   `phase: "end"`, a missing `boundComposer` posts `composer_unbound` **on the
   port**. `startAttach` **does not wait** for ACK/ERROR. It always
   `return { ok: true }` after `transferAttach`. Sidebar then paints
   **Attached**.

In-page picker Attach still goes through the same `DataTransfer` path, but it
opens only after the `+` click that sets `boundComposer`. Gallery 📎 is the
first path that claims attach without that click. Do not “fix” this by making
Gallery open the picker.

If Extra High cannot be provided, or Native Plan Mode is on, stop `BLOCKED`.

```text
Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-x-companion-sidebar-web-mvp
Worker session ordinal: 07
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: FN-X-COMPANION-SIDEBAR-GALLERY-ATTACH-ACK-07
Task type: bounded attach honesty + live composer file-input bind for Gallery 📎
Native planning mode: not-used
Reasoning recommendation: extra-high
Evidence posture: non-independent
Independence required: no
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
Continuity anchor: none — do not resume Worker 06
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
Exact baseline: 045f33b44897a6f3949cc515792336396f1d33a1
Changed-path allowlist: Section 7
Implementation boundaries: Sections 3, 4, 5, and 6
Independence required: no
```

```text
Evidence tier: E1
Evidence tier basis: reversible local companion attach honesty; no authZ change; no NUC mutation; no new companion_mutation
Authorized implementation stages: live composer bind + SW ACK wait + tests + local commit
Combined implementation envelope: allowed
Independent acceptance: not-required
Rollback or recovery checkpoint: local Git commit on feat/x-meme-browser-companion; no push
Activated stricter profile: none
Terminal implementation report point: after commit and focused tests
```

```text
Development envelope activation: activated
Development envelope identity: FrameNest canonical checkout
Declared reversible class: local extension attach path
Working-copy topology: canonical-checkout
Topology rationale: unpublished correction on feat/x-meme-browser-companion at public main SHA
Irreversible exclusions: secrets, accounts, publication, NUC, push, signed-in X, Save freeze, Attach float CSS, picker-as-gallery
```

```text
COOPERATOR: Michal
ORCHESTRATOR: ORCHESTRATOR_CHAT
WORKER: this fresh bounded correction session
```

Professional English in repository artifacts and the terminal report. Czech
forbidden. Report begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

---

## 1. Trace and Meta write

```text
External trace disposition: configured
Trace discovery: cisarik/meta repository path projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp
Trace project key: framenest
Trace logical-whole projection identity: 03/05-framenest-x-companion-sidebar-web-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR after the outcome exists
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 07_correction_00.md
Destination path: projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/07_correction_00.md
Archival: wait-for-report
```

Write only:

```text
/home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/07_report_00.md
```

Do not stage or commit Meta.

---

## 2. Handshake and baseline

Fresh session. Compact capability handshake. Extra High; Native planning mode
`not-used`; no push/NUC/provider/signed-in X.

```text
Expected canonical root: /home/agile/Projects/framenest
Expected branch: feat/x-meme-browser-companion
Exact baseline: 045f33b44897a6f3949cc515792336396f1d33a1
.ap gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Working tree: expected clean
```

If HEAD is not `045f33b…`, stop `BLOCKED` unless the only difference is this
Worker’s own later commits. Do not `git fetch`. Do not switch local `main`.

```text
node --test tests/x_companion_extension.test.js tests/companion_web_bridge.test.js
```

Python: not required unless you touch a Python owner (you should not).
NUC gate: not activated.

---

## 3. Required correction

Keep: green chrome, Connect-in-Settings, 📎 top-left + open-original
bottom-right, in-page Attach float, picker as quick attach, UUID-only
`ATTACH_REQUEST`, `targetOrigin` never `*`, no silent `fallbackDownload` on
unbound composer, no auto-Post.

Required:

1. **Live composer file input for port attach.** When the `framenest-attach`
   port reaches `phase: "end"`, assign files onto a **live** composer
   `input[type=file]` for the focused **Post your reply** /
   `tweetTextarea_0` composer (same discovery `injectAttach` already uses).
   Do not require a prior click of the in-page `+`. If the stored
   `boundComposer.fileInput` is still in `document`, it may be used; if it is
   missing or detached, resolve from the focused composer. If none exists,
   port-ERROR `composer_unbound` and do not invent a download.

2. **Honest `startAttach`.** After `boundTabId` is present, wait for the
   content script ACK `{ attached: true }` or ERROR on that port. Return
   `{ ok: true }` **only** after ACK. Return `{ ok: false, error: ... }` for
   `composer_unbound`, transfer failure, timeout, or missing listener. Do not
   `return { ok: true }` immediately after posting chunks. Sidebar **Attached**
   must remain the success string; it must become true only when attach
   actually targeted a live file input.

3. **Focus is enough to bind the composer for Gallery 📎.** After
   `onComposerFocusIn` injects/shows the floating `+`, the port path must be
   able to find that composer’s file input without opening the picker.

Do not change `framenest-media.bin` in this slice unless a test proves the
File constructor name is why X drops the item; in-page picker uses the same
name today and is not the reported defect. Prefer `content-type` from the
content response as today.

Do not add CORS, `all_urls`, `externally_connectable`, or content-script
`fetch`.

---

## 4. Out of scope

- NUC deploy, migrate, companion origins, `x_acquisition_root`
- Save popup freeze, Analyze execution, alias editor, language tab
- Replacing in-page picker with the website
- Injecting Attach into the X text row
- Grey-black chrome, ADR-0061/0062/0063 body edits
- Independent INFOSEC R3

---

## 5. Negative authority

No push, fetch, branch switch, stash, reset, clean, amend, NUC, Save-popup
edits, Attach-float CSS/position rewrite, picker Settings restoration,
ordinary-tab Gallery thaw, Python/Alembic edits.

---

## 6. Git

```text
Branch: feat/x-meme-browser-companion
Stage: allowlisted paths only; never git add -A
Commit: one local commit after tests
Amend: forbidden
Push: forbidden
```

Suggested subject:

```text
fix: wait for composer ACK before claiming Gallery Attach
```

---

## 7. Allowlist

```text
extension/background/service_worker.js
extension/content/x_adapter.js
tests/x_companion_extension.test.js
tests/companion_web_bridge.test.js
docs/X_COMPANION.md
```

`docs/X_COMPANION.md` only if one operator sentence must say Gallery 📎
attaches after the reply composer is focused, and the shell reports Attached
only when the composer file input accepted the bytes. Prefer one or two
sentences. Do not rewrite the guide.

`tests/companion_web_bridge.test.js` only if the sidebar success path must
assert it still keys off `result.ok` from `ATTACH_BEGIN` (honesty stays in
the service worker).

Tests must prove, as source contracts and/or existing adapter test hooks:

- `startAttach` does not unconditionally `return { ok: true }` after
  `transferAttach` without an ACK/ERROR wait.
- Port `phase: "end"` can resolve a file input from a focused Post your
  reply composer without the in-page `+` click handler being the sole writer
  of `boundComposer`.
- Unbound / missing live file input still yields `composer_unbound` (no
  `fallbackDownload`).
- `isBindableComposerSender` still rejects non-X origins.
- Picker still has no Settings dialog. Save files are untouched.

---

## 8. Report and stop

Echo once:

```text
Logical whole identity: framenest-x-companion-sidebar-web-mvp
Worker session ordinal: 07
Worker exchange ordinal: 01
```

`Phase-qualified result: implementation-PASS` or `not-applicable`.
`Logical-whole closure: not-closed`. Justification `new-mutation`. Name the
new local commit. Residual: unpublished; NUC still `045f33b` until a later
grant; live X DOM remains Cooperator Reload evidence.

Smallest next step: Michal Reload unpacked, focus Post your reply, Gallery 📎,
confirm a media chip appears in the reply composer (not only the shell word
Attached).

After the report, stop.

Slovak capsule data for Orchestrator presentation (not Worker instructions):

```text
🆕 PROMPT PRE FRESH WORKERA 07 • EXTRA HIGH 🧠🧠🧠
Native Plan Mode musí byť vypnutý.
▶️ Otvor nový Worker chat, vypni Plan Mode, vlož tento súbor, počkaj na 07_report_00.md.
📦 Prompt: /home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/07_correction_00.md
📦 Report: /home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/07_report_00.md
✅ Archival: wait-for-report
```
