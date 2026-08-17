# Authoritative Prompt for Fresh Worker 05

## FrameNest × X Companion Side Panel — Connect lives in Settings

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

Worker 04 produced local candidate `5b84046a054b35393860c1a2d811f1a0ca9b9959`
(`implementation-PASS`). That authority is expired. Do not resume Worker 04.
Do not enter Native Plan Mode. Do not deploy NUC. Do not chase Gallery 📎
against `bfad16b`.

The COOPERATOR after Disconnect saw `Cleared`, then `Connect FrameNest to
open the library`. Title-bar **Connect** then showed red `Enter a FrameNest
origin in Settings`. Settings has an empty origin field and a note to use
Connect in the title bar. He cannot complete reconnect. He wants a **Connect
button inside Settings**.

Root cause (do not relitigate): Disconnect runs `RESET`, which clears
`frameNestOrigin`. Title-bar Connect calls `connect()` which refuses an empty
origin and only opens Settings. The grant click is still on the title bar,
which is unusable after Reset.

```text
Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-x-companion-sidebar-web-mvp
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: FN-X-COMPANION-SIDEBAR-SETTINGS-CONNECT-05
Task type: bounded visual correction of first-run / reconnect Connect
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
```

```text
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: 5b84046a054b35393860c1a2d811f1a0ca9b9959
Changed-path allowlist: Section 7
Implementation boundaries: Sections 6, 8, and 11
Independence required: no
```

```text
Evidence tier: E1
Evidence tier basis: reversible local side-panel chrome; no authZ change; no production mutation
Authorized implementation stages: Settings Connect + reconnect flow + tests + local commit
Combined implementation envelope: allowed
Independent acceptance: not-required
Rollback or recovery checkpoint: local Git commit on feat/x-meme-browser-companion; no push
Activated stricter profile: none
Terminal implementation report point: after commit and focused tests
```

If Extra High cannot be provided, or Native Plan Mode is on, stop `BLOCKED`.

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
Downloadable prompt filename: 05_correction_00.md
Destination path: projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/05_correction_00.md
Archival: wait-for-report
```

Write only:

```text
/home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/05_report_00.md
```

You may read `03_report_00.md` and `04_report_00.md` as historical evidence.
Do not stage or commit Meta.

---

## 2. Handshake and baseline

Fresh session. Compact capability handshake. Extra High; Native planning mode
`not-used`; no push/NUC/provider/signed-in X.

```text
Expected canonical root: /home/agile/Projects/framenest
Expected branch: feat/x-meme-browser-companion
Exact baseline: 5b84046a054b35393860c1a2d811f1a0ca9b9959
.ap gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Working tree: expected clean
```

If HEAD is not `5b84046`, stop `BLOCKED` unless the only difference is this
Worker’s own later commits. Do not `git fetch`. Do not edit Save files, Attach
float, picker Settings (picker must stay without a Settings dialog), or ADR
bodies.

```text
Development envelope activation: activated
Working-copy topology: canonical-checkout
Topology rationale: correction of unpublished Worker 04 chrome
Irreversible exclusions: secrets, accounts, publication, NUC, push, signed-in X
```

```text
node --test tests/x_companion_extension.test.js
```

Python: not required unless you touch a Python owner (you should not).
NUC gate: not activated.

---

## 3. Product correction

Keep Worker 03/04 chrome: green title bar, black `FrameNest`, gear, Settings
**sheet under the title bar** (not a centered modal), origin field only in
Settings, honest handshake copy, iframe visible when connected.

Required:

1. **Connect button inside Settings**, next to the origin field (same
   `CONFIGURE_ORIGIN` path as today’s `connect()`). After success: store
   origin, close Settings, title bar reads **Disconnect**, host the iframe.
2. Title bar when **connected**: **Disconnect** still runs existing `RESET`.
   After Reset: clear origin, hide iframe, **open Settings automatically**
   with focus on the origin field so reconnect is one place.
3. Title bar when **disconnected**: keep a **Connect** control. If origin
   input is empty, it must **open Settings** (not only paint a red error).
   If origin input already has a valid URL, it may Connect directly. Do not
   leave the user with a title-bar Connect that cannot grant.
4. Replace the note `Enter it here, then use Connect in the title bar.` with
   copy that the Connect **in Settings** saves the origin. Origin remains
   the FrameNest tailnet URL (`https://<node>.<tailnet>.ts.net`).
5. Empty-origin shell status may stay professional English such as `Connect
   FrameNest in Settings` rather than sending the user to a title-bar click
   that then fails.

Do not put the origin input back on the main chrome outside Settings.
Do not restore picker Settings.
Do not add a second Reset in the title bar.

---

## 4. Out of scope

- Gallery 📎 on NUC `bfad16b`
- Picker Cardano / meme audience
- Deploy, push, `companion_mutation`, CORS, `all_urls`

---

## 5. Negative authority

No push, fetch, branch switch, stash, reset, clean, amend, NUC, Save-popup
edits, Attach-float edits, ordinary-tab Gallery thaw, alias editor.

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
fix: put companion Connect in Settings so reconnect works
```

---

## 7. Allowlist

```text
extension/ui/sidebar.html
extension/ui/sidebar.js
extension/ui/sidebar.css
tests/x_companion_extension.test.js
docs/X_COMPANION.md
```

`docs/X_COMPANION.md` only if one operator sentence must say first-run /
reconnect Connect is in Settings. Prefer a one-line update if the current
text still says to Connect only from the title bar.

Tests must prove: Settings contains a Connect control; empty origin does not
dead-end on the title bar; Disconnect still exists when connected; picker
still has no Settings dialog.

---

## 8. Report and stop

Echo once:

```text
Logical whole identity: framenest-x-companion-sidebar-web-mvp
Worker session ordinal: 05
Worker exchange ordinal: 01
```

`Phase-qualified result: implementation-PASS` or `not-applicable`.
`Logical-whole closure: not-closed`. Justification `new-mutation`. Proof
Settings Connect exists and Reset opens Settings. Residual: NUC still cannot
show 📎. Smallest next step: Michal Reload unpacked, Disconnect, type origin
in Settings, Connect there.

After the report, stop.

Slovak capsule data for Orchestrator presentation (not Worker instructions):

```text
🆕 PROMPT PRE FRESH WORKERA 05 • EXTRA HIGH 🧠🧠🧠
Native Plan Mode musí byť vypnutý.
▶️ Otvor nový Worker chat, vypni Plan Mode, vlož tento súbor, počkaj na 05_report_00.md.
📦 Prompt: /home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/05_correction_00.md
📦 Report: /home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/05_report_00.md
✅ Archival: wait-for-report
```
