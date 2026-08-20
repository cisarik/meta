# Authoritative Prompt for Fresh Worker 09

## FrameNest × X Companion — picker chrome only after a hit; keyboard `++` opens attach

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

Worker 08 produced local `d8f0fc96098d343ecc6bd781bc1b2ff7a98aa327`
(`implementation-PASS`). That authority is expired. Do not resume Worker 08.
Do not deploy NUC. Do not push. Do not enter Native Plan Mode. Do not restyle
Save, side-panel chrome, or Gallery cards. Do not widen picker audience beyond
`ContentCategory.MEME`.

The COOPERATOR live-attached the empty picker. Three required UX facts:

1. The copy **"Type to search memes"** is redundant. Placeholder
   `"Search memes"` is enough. Empty search must not paint instructional chrome.
2. With **zero hits**, the green preview box still shows **`<` `>`** and
   **Attach**. Root cause in current CSS: `.picker-preview { display: flex }`
   overrides the HTML `[hidden]` attribute (`display: none`). `preview.hidden
   = true` therefore still paints an empty bordered box. Fix the cascade and
   keep preview chrome unpainted until a real hit exists.
3. Arrow keys must cycle hits when more than one meme is found. Worker 08
   already listens on the search field; keep that working live after the
   `[hidden]` fix. On-screen arrows exist only when there are two or more hits.

New Cooperator product: typing **`++`** in the same **Post your reply**
composer that already owns the floating **`+`** opens the quick picker so a
meme can be attached **keyboard-only**. Do **not** inject Attach into the X
text row. Do **not** false-trigger on `C++`. Consume those two characters so
they are not posted.

If Extra High cannot be provided, or Native Plan Mode is on, stop `BLOCKED`.

```text
Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-x-companion-sidebar-web-mvp
Worker session ordinal: 09
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: FN-X-COMPANION-SIDEBAR-PICKER-KEYBOARD-09
Task type: bounded in-page meme picker chrome + composer ++ trigger
Native planning mode: not-used
Reasoning recommendation: extra-high
Evidence posture: non-independent
Independence required: no
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
Continuity anchor: none — do not resume Worker 08
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
Exact baseline: d8f0fc96098d343ecc6bd781bc1b2ff7a98aa327
Changed-path allowlist: Section 7
Implementation boundaries: Sections 3, 4, 5, and 6
Independence required: no
```

```text
Evidence tier: E1
Evidence tier basis: reversible local picker chrome + composer keyboard trigger; meme audience unchanged; no NUC; no new companion_mutation
Authorized implementation stages: picker/composer UX + tests + local commit
Combined implementation envelope: allowed
Independent acceptance: not-required
Rollback or recovery checkpoint: local Git commit on feat/x-meme-browser-companion; no push
Activated stricter profile: none
Terminal implementation report point: after commit and focused tests
```

```text
Development envelope activation: activated
Development envelope identity: FrameNest canonical checkout
Declared reversible class: local extension picker and X adapter UX
Working-copy topology: canonical-checkout
Topology rationale: unpublished correction on feat/x-meme-browser-companion after Worker 08
Irreversible exclusions: secrets, accounts, publication, NUC, push, signed-in X, Save freeze, Gallery thaw, meme-audience widen, category picker, Python/Alembic
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
Downloadable prompt filename: 09_correction_00.md
Destination path: projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/09_correction_00.md
Archival: wait-for-report
```

Write only:

```text
/home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/09_report_00.md
```

Do not stage or commit Meta.

---

## 2. Handshake and baseline

Fresh session. Compact capability handshake. Extra High; Native planning mode
`not-used`; no push/NUC/provider/signed-in X.

```text
Expected canonical root: /home/agile/Projects/framenest
Expected branch: feat/x-meme-browser-companion
Exact baseline: d8f0fc96098d343ecc6bd781bc1b2ff7a98aa327
Parent: 7e854d251af841b3ef4a2ddaf130081e330c6f8d
.ap gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Working tree: expected clean
```

If HEAD is not `d8f0fc9…`, stop `BLOCKED` unless the only difference is this
Worker’s own later commits. Do not `git fetch`. Do not switch local `main`.
Do not revert Worker 07 attach ACK or Worker 08 search-first picker.

Python: not required unless you touch a Python owner (you must not).
NUC gate: not activated.

Authorized tests:

```text
node --test tests/x_companion_extension.test.js tests/companion_web_bridge.test.js
```

---

## 3. Required correction

Keep: floating **+** on Post your reply; closed-shadow picker iframe; one JPEG
preview at a time; meme-only `PICKER_QUERY` only after a trimmed query;
autofocus search; Enter attaches a hit; Escape `DISMISS_PICKER`;
`framenest.companion.v1`; no `targetOrigin *`; no auto-Post; Save freeze;
Gallery 📎 honesty from Worker 07; empty query does not list the catalog.

### 3.1 Empty chrome

1. Remove the status copy **"Type to search memes"** and the
   `blankSearchStatus()` helper. Empty trimmed search: no `PICKER_QUERY`,
   no items, **no preview chrome**, empty `#picker-status` (or omit the
   node’s text so `:empty` can collapse it). Do not reserve a hint row.
   Disconnected copy **"Connect FrameNest in the side panel"** may remain
   when origin is missing. Non-empty query with zero hits still uses
   **"No eligible memes"**.

2. **Zero hits:** `#preview` (title, media, arrows, Attach, green border box)
   must not be visible. The HTML `hidden` attribute must actually win over
   `.picker-preview { display: flex }`. Add an explicit
   `.picker-preview[hidden]` / `#preview[hidden] { display: none; }` rule
   (or equivalent that cannot be overridden by the flex rule). Do not leave
   an empty bordered rectangle.

3. **One hit:** show preview + **Attach**. Hide the on-screen `<` `>` nav
   (or keep the nav node `hidden`). Arrow keys in the search field must
   **not** steal caret movement when there is only one hit.

4. **Two or more hits:** show preview + **Attach** + on-screen arrows.
   `ArrowLeft` / `ArrowRight` cycle hits. Keep this on the search field
   (Worker 08). Also handle those keys on the picker document when focus is
   inside the picker iframe (preview, Attach, arrows, refresh) so cycling
   does not depend on clicking the chevrons. `preventDefault` only when
   actually cycling. Enter still attaches the current hit.

### 3.2 Compact host when chrome is hidden

Worker 08 pins attach-popup height at `Math.min(360)`. With preview hidden,
that leaves a tall empty iframe under the search field.

When preview chrome is hidden, shrink the X-page popup host to search-only
(close control + search row; no empty green box). When a hit exists, expand
to the current compact preview height.

Use one `framenest.companion.v1` message, same family as `DISMISS_PICKER`
(new type such as `PICKER_LAYOUT` with a boolean compact/expanded payload,
or an equivalent ACK forwarded through the service worker to the bound tab).
Unknown versions/types still drop. Do not `postMessage` with
`targetOrigin: "*"`. Update the height pin(s) in tests.

### 3.3 Keyboard `++` opens the picker

On the **same reply composer** that already receives the floating Attach
`+` (do not invent a second composer matcher; do not match the X site
search box):

1. Detect a `++` **token** immediately before the caret: the two characters
   are `+` `+`, and the character before them is start-of-field, whitespace,
   or a newline. That includes the field containing only `++`.
2. Do **not** trigger on `C++`, `foo++`, or any `++` preceded by a
   non-whitespace character. `C++` is the explicit false-positive to
   prevent.
3. When the token matches, **consume/remove those two `+` characters** from
   the composer so they are not posted. Then open the existing picker
   (`openAttachPopup` / equivalent) and leave search focused (picker already
   autofocuses).
4. If the picker is **already open** for that composer, do **not** toggle it
   closed. Current `openAttachPopup` closes when invoked on the same button.
   Keyboard `++` must open-or-focus, not close. A second click on floating
   `+` may still toggle closed.
5. Do not inject a control into the X text row. Do not click Post. Do not
   attach a meme until the user searches and confirms (Enter / Attach).
6. Prefer `beforeinput` / `input` so IME composition does not insert a stray
   `++`. Bound the listener to the known composer editable, not `window`.

Empty origin: opening the picker is still allowed; existing disconnected
status inside the picker remains the honest path. Do not invent a new
Connect UI inside the picker.

---

## 4. Out of scope

- NUC deploy, migrate, companion origins, `x_acquisition_root`
- Save popup, Analyze, content-category picker, alias editor, language tab
- Side-panel chrome, Gallery 📎 layout
- Replacing picker with the full website
- Injecting Attach into the X text row
- Widening `GET /api/x/companion/media` beyond Meme
- ADR body edits, INFOSEC R3, Python/Alembic
- Static X photo acquisition

---

## 5. Negative authority

No push, fetch, branch switch, stash, reset, clean, amend, NUC, Python,
Save-popup edits, Attach-float CSS rewrite, picker Settings restoration,
ordinary-tab Gallery thaw, meme-category widen, new `companion_mutation`.

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
fix: hide empty picker chrome and open attach from ++
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

`messages.js` / `service_worker.js` / `x_adapter.js` only for picker layout
resize and the `++` open path. Do not rewrite Worker 07 attach ACK.
Do not restyle Save.

`docs/X_COMPANION.md` only if one operator sentence must say: empty search
shows no preview chrome; arrows appear after two or more hits; typing `++`
in the reply composer opens the picker and consumes the token. Prefer one
or two sentences.

Tests must prove:

- picker JS/HTML/CSS no longer contain `"Type to search memes"` /
  `blankSearchStatus`
- `#preview` / `.picker-preview[hidden]` actually `display: none` (the flex
  rule must not win)
- empty / cleared search still does not call `PICKER_QUERY` as list-all
- arrows / Attach markup stay inside `#preview` (hidden with it when empty)
- `ArrowLeft` / `ArrowRight` still cycle when `items.length > 1`
- `++` token helper or adapter source: triggers after whitespace/start;
  does not trigger on `C++`; consumes the two characters; opens picker
  without toggle-close when already open
- layout type is in `TYPES` if you add one; unknown types still drop
- compact vs expanded host height pins match the implementation
- Save files and Gallery 📎 ACK path remain untouched
- picker still has no Settings dialog and no `#kind`

Existing test `in-page picker is search-first, compact, and dismisses on
Escape` currently pins `"Type to search memes"` and `blankSearchStatus()`.
Update that pin. Do not delete the search-first contracts.

---

## 8. Report and stop

Echo once:

```text
Logical whole identity: framenest-x-companion-sidebar-web-mvp
Worker session ordinal: 09
Worker exchange ordinal: 01
```

`Phase-qualified result: implementation-PASS` or `not-applicable`.
`Logical-whole closure: not-closed`. Justification `new-mutation`. Name the
new local commit. Residual: unpublished (Worker 07 + 08 + 09); NUC still
`045f33b` until a later grant; meme audience unchanged.

Smallest next step: Michal Reload unpacked, open **Post your reply**, type
`++`, confirm picker opens with search focused and **no** empty Attach box;
type a meme query; Left/Right cycle; Enter attaches; clear search hides
preview chrome again. Confirm `C++` in the composer does not open the
picker.

After the report, stop.

Slovak capsule data for Orchestrator presentation (not Worker instructions):

```text
🆕 PROMPT PRE FRESH WORKERA 09 • EXTRA HIGH 🧠🧠🧠
Native Plan Mode musí byť vypnutý.
▶️ Otvor nový Worker chat, vypni Plan Mode, vlož tento súbor, počkaj na 09_report_00.md.
📦 Prompt: /home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/09_correction_00.md
📦 Report: /home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/09_report_00.md
✅ Archival: wait-for-report
```
