# Authoritative Prompt for Fresh Worker 08

## FrameNest × X Companion — quick meme picker: search-first, no kind dropdown, no lie-on-clear

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

Worker 07 produced local `7e854d251af841b3ef4a2ddaf130081e330c6f8d`
(`implementation-PASS`). The COOPERATOR live-accepted Gallery 📎: shell
**Attached** and the meme appears in **Post your reply**. That authority is
expired. Do not resume Worker 07. Do not deploy NUC. Do not enter Native Plan
Mode. Do not restyle Save, side-panel chrome, or Gallery cards.

The COOPERATOR classified Cardano-not-in-picker as **correct**: the in-page
popup is meme-category only (`GET /api/x/companion/media` /
`ContentCategory.MEME`). GIF, static image, and video are all eligible **when
cataloged as Meme**. Do not widen to Gallery-wide search. Do not replace this
popup with the website. Do not put Settings back.

He attached the live picker (search `Gif`, preview “Acceptance animated GIF”,
**All kinds** dropdown, inner scrollbar, header ✕, Attach). Required UX:

1. Remove **All kinds**. Kind filter is redundant; memes already include gif /
   static / video.
2. **No inner scrolling.** Removing the dropdown should free height; size the
   host/iframe and picker document so one search + one preview + Attach fit
   without a scrollbar.
3. After **+**, **focus the search input** immediately.
4. **Enter** attaches the current hit (first result is fine when it is the
   selection). Keyboard-first quick find.
5. **Bug:** he searched, then clicked the search-field **X** (native
   `type="search"` clear). Picker showed “Regal Portrait of a Queen”. Empty
   or cleared query must show **no preview and must not list the catalog**.
   Query the API only when the user has typed a real search string. “No
   eligible memes” is for a non-empty query with zero hits, not for blank
   search.

If Extra High cannot be provided, or Native Plan Mode is on, stop `BLOCKED`.

```text
Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-x-companion-sidebar-web-mvp
Worker session ordinal: 08
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: FN-X-COMPANION-SIDEBAR-PICKER-SEARCH-FIRST-08
Task type: bounded in-page meme picker UX (no kind dropdown, empty-query blank, autofocus, Enter attach, no scroll)
Native planning mode: not-used
Reasoning recommendation: extra-high
Evidence posture: non-independent
Independence required: no
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
Continuity anchor: none — do not resume Worker 07
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
Exact baseline: 7e854d251af841b3ef4a2ddaf130081e330c6f8d
Changed-path allowlist: Section 7
Implementation boundaries: Sections 3, 4, 5, and 6
Independence required: no
```

```text
Evidence tier: E1
Evidence tier basis: reversible local in-page picker UX; meme audience unchanged; no NUC; no new companion_mutation
Authorized implementation stages: picker UX + tests + local commit
Combined implementation envelope: allowed
Independent acceptance: not-required
Rollback or recovery checkpoint: local Git commit on feat/x-meme-browser-companion; no push
Activated stricter profile: none
Terminal implementation report point: after commit and focused tests
```

```text
Development envelope activation: activated
Development envelope identity: FrameNest canonical checkout
Declared reversible class: local extension picker UX
Working-copy topology: canonical-checkout
Topology rationale: unpublished correction on feat/x-meme-browser-companion after Worker 07
Irreversible exclusions: secrets, accounts, publication, NUC, push, signed-in X, Save freeze, Gallery thaw, meme-audience widen
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
Downloadable prompt filename: 08_correction_00.md
Destination path: projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/08_correction_00.md
Archival: wait-for-report
```

Write only:

```text
/home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/08_report_00.md
```

Do not stage or commit Meta.

---

## 2. Handshake and baseline

Fresh session. Compact capability handshake. Extra High; Native planning mode
`not-used`; no push/NUC/provider/signed-in X.

```text
Expected canonical root: /home/agile/Projects/framenest
Expected branch: feat/x-meme-browser-companion
Exact baseline: 7e854d251af841b3ef4a2ddaf130081e330c6f8d
Parent: 045f33b44897a6f3949cc515792336396f1d33a1
.ap gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Working tree: expected clean
```

If HEAD is not `7e854d2…`, stop `BLOCKED` unless the only difference is this
Worker’s own later commits. Do not `git fetch`. Do not switch local `main`.
Do not revert Worker 07 attach ACK.

```text
node --test tests/x_companion_extension.test.js tests/companion_web_bridge.test.js
```

Python: not required unless you touch a Python owner (you must not).
NUC gate: not activated.

---

## 3. Required correction

Keep: floating **+** on Post your reply; closed-shadow picker iframe; one JPEG
preview at a time; prev/next arrows; Attach button; meme-only
`PICKER_QUERY`; `framenest.companion.v1`; no `targetOrigin *`; no auto-Post;
Save freeze; Gallery 📎 honesty from Worker 07.

Required:

1. **Remove `#kind` / All kinds** from `picker.html|css|js`. Do not send
   `kind` from the UI. Server kind filter may remain unused. Do not add a
   replacement chip row.

2. **Empty query is blank.** Trimmed search empty (initial open, native search
   clear **X**, or user deletes all text) must **not** call `PICKER_QUERY` as
   a list-all. Clear items, hide preview, do not show a first catalog meme.
   Status: empty or a short search hint — not “No eligible memes”.
   Non-empty query with zero hits: “No eligible memes” as today.
   Refresh `↻` follows the same empty-vs-query rule.

3. **Autofocus search** when the picker iframe loads after **+**. Use the
   picker document (`autofocus` and/or `search.focus()`). The host page is
   cross-origin `x.com`; do not read iframe DOM from the content script.

4. **Enter attaches** the selected hit when one exists (already on search
   `keydown`; keep it working with focus in the input). Empty query + Enter
   must not attach. ArrowLeft/ArrowRight from the search field may cycle
   hits when more than one exists (same as the on-screen arrows).

5. **Escape from the focused search closes the popup.** Keydown inside the
   iframe does not reach the X-page capture listener. Add one
   `framenest.companion.v1` dismiss path: picker `chrome.runtime.sendMessage`
   → service worker → `chrome.tabs.sendMessage(boundTabId)` → existing
   `closeAttachPopup()`. Do not `postMessage` with `targetOrigin: "*"`.
   Unknown versions/types still drop.

6. **No inner scrollbar.** Compact the picker document (`html, body, #picker`
   overflow hidden as needed) and the host size in `positionAttachPopup` /
   `openAttachPopup` so search + one preview + Attach fit. Existing tests pin
   `Math.min(500)` for attach popup height; update that pin to the new compact
   height. Do not clip Attach or the search field.

Do not change `GET /api/x/companion/media` audience. Do not search non-meme
Gallery items.

---

## 4. Out of scope

- NUC deploy, migrate, companion origins
- Save popup, Analyze, alias editor, language tab
- Side-panel chrome, Gallery 📎 layout
- Replacing picker with the full website
- Injecting Attach into the X text row
- ADR body edits, INFOSEC R3

---

## 5. Negative authority

No push, fetch, branch switch, stash, reset, clean, amend, NUC, Python/Alembic,
Save-popup edits, Attach-float CSS rewrite, picker Settings restoration,
ordinary-tab Gallery thaw, meme-category widen.

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
fix: make in-page meme picker search-first and compact
```

---

## 7. Allowlist

```text
extension/ui/picker.html
extension/ui/picker.js
extension/ui/picker.css
extension/content/x_adapter.js
extension/background/service_worker.js
extension/shared/messages.js
tests/x_companion_extension.test.js
docs/X_COMPANION.md
```

`messages.js` / `service_worker.js` / `x_adapter.js` only for dismiss-on-Escape
and compact popup sizing. Do not rewrite Worker 07 attach ACK.

`docs/X_COMPANION.md` only if one operator sentence must say the in-page picker
searches memes after the user types, Enter attaches, and clearing search shows
no hit. Prefer one or two sentences.

Tests must prove:

- picker HTML has no `#kind` / All kinds select
- picker still has no Settings dialog
- empty / cleared search does not treat blank `q` as list-all (source contract
  on `picker.js`: no `PICKER_QUERY` until trimmed query is non-empty)
- Enter on search still calls attach when a hit exists
- search is focused on load
- dismiss type is in `TYPES` and unknown types still drop
- attach popup height pin matches the compact host
- Save files and Gallery 📎 ACK path remain untouched

---

## 8. Report and stop

Echo once:

```text
Logical whole identity: framenest-x-companion-sidebar-web-mvp
Worker session ordinal: 08
Worker exchange ordinal: 01
```

`Phase-qualified result: implementation-PASS` or `not-applicable`.
`Logical-whole closure: not-closed`. Justification `new-mutation`. Name the
new local commit. Residual: unpublished (Worker 07 + 08); NUC still `045f33b`
until a later grant; meme audience unchanged (Cardano stays out unless tagged
Meme).

Smallest next step: Michal Reload unpacked, open **+** on Post your reply,
confirm search focused, type a meme query, Enter attaches, clear **X** shows
blank, no All kinds, no inner scrollbar.

After the report, stop.

Slovak capsule data for Orchestrator presentation (not Worker instructions):

```text
🆕 PROMPT PRE FRESH WORKERA 08 • EXTRA HIGH 🧠🧠🧠
Native Plan Mode musí byť vypnutý.
▶️ Otvor nový Worker chat, vypni Plan Mode, vlož tento súbor, počkaj na 08_report_00.md.
📦 Prompt: /home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/08_correction_00.md
📦 Report: /home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/08_report_00.md
✅ Archival: wait-for-report
```
