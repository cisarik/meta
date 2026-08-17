# Authoritative Prompt for Fresh Worker 04

## FrameNest × X Companion Save Popup — Description restore and action-row alignment

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

Worker 03 produced local candidate `ea939734558d7f5391e8d06c561a5cc46bc07b25`.
That authority is expired. Do not resume Worker 03. Do not enter Native Plan
Mode. Do not reopen overlay schema, companion_mutation, NUC, publication,
Attach, Gallery, or the side-panel architecture.

The COOPERATOR live-accepted: compact green header, red header **X**, Search
tags, selected tag pills. He now wants three visual amendments while this
popup is still being dressed:

1. Restore the **Description** textarea. There is empty space; UX is better
   with it.
2. Pin the action row to the **bottom-right**. Ordinary user: only **Save**,
   right-aligned.
3. Admin (`analysis.run`): a second control to the **left** of Save, labelled
   **Save and analyze by AI** (not “Analyze by AI”).

Analyze still **must not** call a provider, analysis HTTP path, or new
`companion_mutation` route. There is still no `media_id` on first save.
Clicking the admin control **does Save** (same `SAVE_POST` + alias payload,
including description). It does not run AI. Honest `title` / `aria-label`:
`Saves now. Analyze by AI is available in FrameNest after this item is cataloged.`

```text
Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-x-companion-save-alias-mvp
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: FN-X-COMPANION-SAVE-POPUP-UX-04
Task type: bounded visual correction
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
```

```text
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: ea939734558d7f5391e8d06c561a5cc46bc07b25
Changed-path allowlist: Section 8
Implementation boundaries: Sections 6, 7, 9, and 13
Independence required: no
```

```text
Evidence tier: E1
Evidence tier basis: reversible Save-iframe visual amendment; no new authZ route
Authorized implementation stages: HTML/CSS/JS visual, tests, X_COMPANION sentence, local commit
Combined implementation envelope: allowed
Independent acceptance: not-required
Rollback or recovery checkpoint: local Git commit on feat/x-meme-browser-companion; no push
Activated stricter profile: none
Terminal implementation report point: after commit and focused tests
```

Reasoning: Extra High (whole default). Do not use Max. If Extra High cannot be
provided, stop `BLOCKED`.

```text
COOPERATOR: Michal
ORCHESTRATOR: ORCHESTRATOR_CHAT
WORKER: this fresh bounded correction session
```

Professional English in code, tests, docs, and the report. Czech forbidden.
Begin the report exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Do not claim live X looks correct. Michal Reload-unpacked remains his visual
step.

---

## 1. Trace and Meta

```text
External trace disposition: configured
Trace discovery: cisarik/meta repository path projects/framenest/03/04-framenest-x-companion-save-alias-mvp
Trace project key: framenest
Trace logical-whole projection identity: 03/04-framenest-x-companion-save-alias-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR after the outcome exists
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 04_correction_00.md
Destination path: projects/framenest/03/04-framenest-x-companion-save-alias-mvp/04_correction_00.md
Archival: wait-for-report
```

Write only:

```text
/home/agile/meta/projects/framenest/03/04-framenest-x-companion-save-alias-mvp/04_report_00.md
```

You may read `03_report_00.md` as historical evidence. Do not edit other Meta
paths. Do not commit Meta.

---

## 2. Handshake and envelope

Fresh session. Record requested vs observed Extra High, Native planning mode
`not-used`, filesystem, tests, local commit, and that push/NUC/provider/
signed-in X remain unused.

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: tests/x_companion_extension.test.js
Affected tests: tests/x_companion_extension.test.js
New causal regression: Description present and submitted; actions flex-end; admin label Save and analyze by AI; ordinary Save only; Analyze click saves, does not call analysis
Broad or full suite: not-used
Runtime or testbed: node --test
Independent acceptance: not-required
Development envelope activation: activated
Working-copy topology: canonical-checkout
Topology rationale: unpublished Save-alias candidate already on this branch
Irreversible exclusions: secrets, publication, NUC, push, signed-in X, Gallery thaw, Attach thaw
```

---

## 3. Baseline gate

```text
Expected canonical root: /home/agile/Projects/framenest
Expected branch: feat/x-meme-browser-companion
Expected HEAD: ea939734558d7f5391e8d06c561a5cc46bc07b25
Expected parent: 72b8507fa0c7af627c8c60fe5fbae611bdb759f6
Expected tree: 94cc24fb24b1920358ef9ca617561bb8bb51f2dd
Expected subject: test: retarget live Alembic head pins to 0029
.ap gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Working tree: expected clean
```

Revalidate public `main` with `git ls-remote` (no fetch). Expected
`bfad16b718e135b272a3b0293bb37ddc3101ba49`. Behind the feature branch is
expected. Stop `BLOCKED` if HEAD is not `ea93973` or the tree is dirty with
unexplained overlap.

---

## 4. Execution routes

No ambient Python. This correction should need **no** `ap exec` unless you
touch a Python file (you must not).

```text
node --test tests/x_companion_extension.test.js
```

NUC gate is not activated.

---

## 5. Required reading

- `extension/ui/save.html`, `save.css`, `save.js` at HEAD
- `extension/content/x_adapter.js` only if the Description field needs a
  slightly taller iframe; do not change Attach `positionAttachPopup`
- `docs/X_COMPANION.md` Save-popup paragraph
- `tests/x_companion_extension.test.js` Save visual assertions

---

## 6. Binding visual contract

Keep: green “Save to FrameNest” header, red header X, Search tags, pills,
black background, green border, no checkbox forest, no Cancel button, Attach
frozen, no CORS, no content-script fetch, `companion_mutation` unchanged.

Change:

1. **Description** textarea between Title and Tags. `maxlength="10000"`,
   `id="description"`, several rows (about 4). Include non-empty description
   in `aliasPayload()` as `description`. Empty omits the field.
2. **`.actions`:** `justify-content: flex-end`. DOM order: admin control
   (if present) then **Save**, so Save is the rightmost control.
3. Ordinary user (`analysis.run` absent or identity fail-closed): only Save,
   right-aligned. Admin control stays `hidden`.
4. Admin: unhide **Save and analyze by AI** to the left of Save. Keep mint
   filled style (`#f5f8f5` / `#0c1a10`). It may stay `disabled=false` for
   click-to-save. Click runs the **same save path** as Save (do not duplicate
   broken logic). It must not `fetch` analysis, must not add message types,
   must not enable a provider. `title` / `aria-label` as in the preamble.
5. Do not execute Analyze. Do not queue analysis. Residual stays parked.

If Description needs height, you may raise `positionSavePopup` happy-path
height slightly (still clamp to the viewport). Do not edit Attach positioning.

---

## 7. Negative authority

No push, fetch, branch switch, stash, reset, clean, amend, NUC, sudo,
provider, signed-in X, Gallery/Details CSS, picker/Attach functions, ADR
edits, overlay schema/API, Alembic tests, side-panel replacement, or
`companion_mutation` expansion.

---

## 8. Allowlist

```text
extension/ui/save.html
extension/ui/save.css
extension/ui/save.js
extension/content/x_adapter.js
docs/X_COMPANION.md
tests/x_companion_extension.test.js
```

`x_adapter.js` only for Save iframe size if required.

---

## 9. Tests

`node --test tests/x_companion_extension.test.js` must prove:

- `save.html` has Description textarea, Search tags, header Close, Save;
- no Cancel button; no checkbox tag forest;
- admin control text is `Save and analyze by AI`;
- `.actions` uses `flex-end`;
- `save.js` sends `description` when the field is non-empty;
- admin click does not introduce an analysis message type or analysis path;
- no `innerHTML` in `save.js`;
- Attach/picker assertions still green.

Invert Worker 03 assertions that required Description to be absent or the
label `Analyze by AI` without “Save and”.

---

## 10. Git

```text
Fetch: forbidden
Branch: stay on feat/x-meme-browser-companion
Stage: exact allowlisted paths only; never git add . or git add -A
Commit: one local commit after the JS test passes
Amend: forbidden
Push: forbidden
```

Suggested subject:

```text
fix: restore Save description and right-align companion actions
```

---

## 11. Report and stop

Write `04_report_00.md`. Echo once:

```text
Logical whole identity: framenest-x-companion-save-alias-mvp
Worker session ordinal: 04
Worker exchange ordinal: 01
```

Include PASS/PARTIAL/BLOCKED; `implementation-PASS` or `not-applicable`;
`Logical-whole closure: not-closed`; handshake; baseline and final HEAD;
changed paths; proof no analysis HTTP / no companion_mutation change;
commands and exit codes; residuals; near-misses; justification
`new-mutation`; expiry; next step = Michal Reload unpacked, then a **new**
Agent Orchestrator for the side-panel web whole — not this Worker.

After the report, stop.

Slovak capsule data for Orchestrator presentation (not Worker instructions):

```text
🆕 PROMPT PRE FRESH WORKERA 04 • EXTRA HIGH 🧠🧠🧠
Native Plan Mode musí byť vypnutý.
▶️ Otvor nový Worker chat, vypni Plan Mode, vlož tento súbor, počkaj na 04_report_00.md.
📦 Prompt: /home/agile/meta/projects/framenest/03/04-framenest-x-companion-save-alias-mvp/04_correction_00.md
📦 Report: /home/agile/meta/projects/framenest/03/04-framenest-x-companion-save-alias-mvp/04_report_00.md
✅ Archival: wait-for-report
```
