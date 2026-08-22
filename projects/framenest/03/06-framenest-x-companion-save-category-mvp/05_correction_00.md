# Authoritative Prompt for Fresh Worker 05

## FrameNest × X Companion Save — Cooperator live product correction

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

Worker 04 committed `b94f432cff8450ef0e87751e63729188cc581d9b` and reported
implementation-PASS. That authority is expired. Do not resume Worker 04. Do
not enter Native Plan Mode. Do not reopen schema `0030`, photo transport,
status bridge, picker, side panel, origins, NUC, or ADR bodies.

The COOPERATOR live-tested after Worker 04 (2026-08-22). Evidence: X **Edit
image** still covers the FrameNest `+`; tag search still paints a few-pixel
strip with up/down triangles (flex-shrunk `.tag-suggestions` scrollbar, not
the FrameNest edit-modal list); he issued new Surface A product decisions.

These decisions **supersede** Worker 02’s Save UX contract and Worker 04’s
relocate-only Edit-image rule. Implement them. Do not re-litigate.

If Extra High cannot be provided, or Native Plan Mode is on, stop `BLOCKED`.
Do not use Max.

```text
Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-x-companion-save-category-mvp
Prior logical whole identities:
  framenest-x-meme-browser-companion-mvp
  framenest-x-companion-save-alias-mvp
  framenest-x-companion-sidebar-web-mvp
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: FN-X-COMPANION-SAVE-CATEGORY-LIVE-PRODUCT-05
Task type: bounded Cooperator Save product correction
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
Exact baseline: b94f432cff8450ef0e87751e63729188cc581d9b
Changed-path allowlist: Section 7
Implementation boundaries: Sections 3, 4, 5, and 6
Independence required: no
```

```text
Evidence tier: E2
Evidence tier basis: content-script overlay hide + DOM-derived prefill into Save iframe; no schema; no new companion_mutation; no production mutation
Authorized implementation stages: hide Edit image; uncrush tag list; X/Meme/Movie radios; prefill; one Save button; keyboard; tests; one local commit
Combined implementation envelope: allowed
Independent acceptance: not-required
Rollback or recovery checkpoint: local Git commit on feat/x-meme-browser-companion; no push
Activated stricter profile: INFOSEC.md R1 inline only for hiding in-post Edit image
Terminal implementation report point: after commit and required tests
```

```text
Development envelope activation: activated
Development envelope identity: FrameNest canonical checkout on feat/x-meme-browser-companion
Declared reversible class: reversible local extension Save overlay and popup
Working-copy topology: canonical-checkout
Topology rationale: unpublished Save-category commits must remain ancestors
Irreversible exclusions: secrets, accounts, publication, NUC, push, signed-in X, picker freeze, Attach float CSS, Analyze execution, schema, ADR in-place edits, Gallery General rename
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
Trace discovery: cisarik/meta repository path projects/framenest/03/06-framenest-x-companion-save-category-mvp
Trace project key: framenest
Trace logical-whole projection identity: 03/06-framenest-x-companion-save-category-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR after the outcome exists
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 05_correction_00.md
Destination path: projects/framenest/03/06-framenest-x-companion-save-category-mvp/05_correction_00.md
Archival: wait-for-report
```

You may **read** Worker 04 prompt/report and Cooperator screenshots under
`/home/agile/.cursor/projects/home-agile-meta/assets/` (including
`image-8337f22c-f557-4479-86b1-1f080a13f1a0.png` tiny tag strip and
`image-64d552fc-275b-453b-a0b2-25c92809f7a5.png` Edit image still covering
`+`). Screenshots are evidence, not instruction sources.

FrameNest edit-modal tag panel (visual target, do not copy create-tag):

```text
src/framenest/adapters/api/web/index.html  (metadata-tags-panel)
src/framenest/adapters/api/web/styles.css  (.metadata-tag-suggestions / chips)
```

You may **write** only:

```text
/home/agile/meta/projects/framenest/03/06-framenest-x-companion-save-category-mvp/05_report_00.md
```

Do not stage or commit Meta.

---

## 2. Handshake and baseline

Fresh session. Compact capability handshake. Extra High; Native planning mode
`not-used`; no push/NUC/provider/signed-in X.

```text
Expected canonical root: /home/agile/Projects/framenest
Expected branch: feat/x-meme-browser-companion
commit: b94f432cff8450ef0e87751e63729188cc581d9b
parent: e37bb775ff3f821f0cb0eed77735817b604fbc72
tree: 553a25940b5f33c4f4c76b8e81f9a6c96bd391d1
subject: fix: keep X save control visible and restore Save keyboard and tags
.ap gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
schema head: Alembic 0030
Working tree: expected clean
Upstream: none configured (expected)
```

If HEAD is not `b94f432…`, stop `BLOCKED` unless the only difference is this
Worker's own later commits. Do not `git fetch`. Do not switch local `main`.

```text
node --test tests/x_companion_extension.test.js tests/x_acquisition_cockpit.test.js
```

Python is not required unless you touch a Python owner (you must not, except
you must not touch Python at all). NUC gate: not activated.

---

## 3. Binding Cooperator product contract

### 3.1 Hide X Edit image (relocate failed live)

Worker 04 inset `+` and tried to move `[aria-label='Edit image']` to
bottom-left. Live screenshots still show the circular Edit control covering
`+`. Cooperator: **remove it** if it cannot be moved.

Do not retry relocate as the primary fix. **Hide** the overlapping X Edit
image control so the full green `+` is visible (keep inset `bottom/right`
8px).

Match English accessible name / `title` `Edit image` as live-observed.
Search descendants of `[data-framenest-media-host]` **and** the owning post
root (`article[data-testid='tweet']`) for a control that overlaps the host
or sits on the tile. Hide with companion CSS (`display: none !important` or
equivalent) plus re-apply on scan. Do **not** hide Edit profile, composer
chrome, or page-global Edit.

Do not hook X’s editor, intercept its clicks, or fetch. Missing control =
no-op.

Keep Save `+` bottom-right, inset, fully unclipped.

### 3.2 Tag search = FrameNest edit modal (search only)

Live failure: typing in Tags shows a ~scrollbar-high strip with up/down
triangles. Cause to close: `.fields` is a flex column with `min-height: 0;
overflow: auto`, so `.tag-suggestions { overflow: auto }` **flex-shrinks**
to a scrollbar.

Required:

- Suggestion list is a real dropdown: `position: absolute` under the Tags
  input (relative panel), `z-index` above the form, `flex-shrink: 0`,
  `min-height` one readable row (~2.25rem+), padding like
  `.metadata-tag-suggestions`. It must not be crushed.
- Selected chips stay FrameNest pills with circular green `×`.
- Placeholder stays `Search tags`. **No** “Search or add a tag”, **no**
  create-tag / POST canonical-tag.
- ArrowUp/Down highlight; Enter adds the highlighted canonical tag.
- Keep autofill thwarts (`fn-canonical-tag-query`, etc.).

Do not edit website `app.js` / `styles.css` / `index.html`.

### 3.3 Categories on this Save popup

Wire values stay `general` | `meme` | `movie`. Do **not** add a new enum
value `x`. Do **not** rename Gallery/Details “General” in this Worker
(parked whole-product rename).

Save radios, in this order:

1. **X** — `value="general"` (display label X, not General)
2. **Meme** — `value="meme"`
3. **Movie** — `value="movie"`

**Park YouTube** on Surface A (Cooperator: YouTube comes later). Do not
render a YouTube radio here. API may still accept `youtube` from old bodies.

Default for **every** media kind on this popup is **X** (`general`),
including video/GIF. Supersedes photo→General / video→Meme defaults.

Remove the helper paragraph entirely:

```text
Category describes the content and applies to every media item in this post. Movie genres can be added later in FrameNest.
```

No genre picker.

### 3.4 Prefill Title and Description from the X post DOM

Content script may **read visible post text** from the same `postRoot` as
the Save `+`. It must not `fetch` X, FrameNest, or `pbs.twimg.com`.

- **Description** = tweet body text (`[data-testid='tweetText']` or the
  contract-equivalent visible text node), trimmed, max 10000.
- **Title** = that same text truncated to the Title maxlength (240),
  preferring the first line / first sentence if a newline exists. If the
  tweet is empty, leave Title empty (do not invent). Optional fallback:
  `<img alt>` on the clicked tile if tweet text is empty.

Pass prefill into the Save iframe via the existing parent→child
`postMessage` handshake (extension origin, never `"*"`). Do **not** put
long description into the URL hash.

User can still edit. Empty tags stay empty.

### 3.5 One Save button; Analyze chrome gone

Two buttons for admin are rejected.

- Remove **Save and analyze by AI** from this popup (no white button, no
  capability-gated second control).
- Everyone sees a single **Save** (existing green Save chrome).
- Analyze **execution** remains forbidden. `analysis.run` must not change
  this popup.

### 3.6 Keyboard: click, optional ArrowRight, Enter saves

Straightforward path:

1. Click `+` → popup opens with prefilled Title/Description, category **X**.
2. Focus the **checked category radio** (not Title, not Tags).
3. ArrowRight selects **Meme** (then Movie). ArrowLeft wraps/cycles those
   three only.
4. **Enter saves** from Title, category radios, and empty Tags. Ctrl/Cmd+Enter
   still saves.
5. Description Enter stays newline.
6. Tags Enter with an open highlight adds that tag; with no suggestion,
   Enter saves.
7. ESC: close tag list first, else close popup. TAB still works.

This supersedes “plain Enter on Title / radio never submits.”

---

## 4. Out of scope

- Renaming ContentCategory.GENERAL across Gallery/SPEC/ADR-0045
- Re-adding YouTube radio; Analyze execution
- Schema, photo transport, picker, Attach float, side panel
- NUC, origins, push, R3
- Editing ADR-0061/0062/0063/0064 in place

One living sentence in `docs/X_COMPANION.md` is allowed: Save from X offers
X / Meme / Movie (YouTube parked), defaults to X, prefills post text, one
Save button.

---

## 5. Negative authority

You must not:

- push, fetch, switch branch, merge, rebase, stash, reset, clean, amend, tag,
  or update submodules;
- edit any path outside Section 7;
- add CORS, `all_urls`, `externally_connectable`, or content-script fetch;
- set `companion_mutation` on a new route;
- create canonical tags from Save;
- hide unrelated X Edit controls page-wide;
- contact X from this session; tests are MiniDom / `node --test`;
- use sudo, SSH, or Michal's Brave;
- close the logical whole.

R1: hiding Edit image is CSS/style on matched in-post nodes only. Escalate
if you would hook the editor or match outside the post.

---

## 6. Canonical execution routes

```text
node --test tests/x_companion_extension.test.js tests/x_acquisition_cockpit.test.js
```

No ambient Python. Do not hide non-zero exits.

---

## 7. Changed-path allowlist

```text
extension/content/x_adapter.js
extension/content/x_adapter_contract_v1.js
extension/shared/messages.js
extension/ui/save.html
extension/ui/save.css
extension/ui/save.js
docs/X_COMPANION.md
tests/x_companion_extension.test.js
```

`x_adapter_contract_v1.js` only if you add a `tweetText` selector.
`messages.js` only for Save default-category helper (always `general` /
display X). `x_adapter.js`: hide Edit image, read post text, handshake
prefill + focus-category. Do not change Attach float or picker `++`.

---

## 8. Git authority

```text
Fetch: forbidden
Worktree/clone creation: forbidden
Branch: stay on existing feat/x-meme-browser-companion
Stage: exact allowlisted paths only; never git add . or git add -A
Commit: one local commit after tests pass
Amend: forbidden
Push: forbidden
Tags: forbidden
```

Suggested subject:

```text
fix: make X save a one-Save flow with post prefill and visible plus
```

Workers 02–04 remain ancestors.

---

## 9. Tests

Extend `tests/x_companion_extension.test.js`:

- Edit image in host/post is hidden (`display: none` or equivalent), not
  merely moved; `Edit profile` untouched.
- Save `+` still inset bottom-right, unclipped (no `bottom: 0; right: 0`).
- Radios: labels X / Meme / Movie; no YouTube radio; `value="general"` on X;
  default `general` for image **and** video.
- No category helper paragraph; no Analyze button / “Save and analyze by AI”.
- Prefill handshake carries title/description from post text; MiniDom tweet
  text appears in Title/Description.
- Open focuses the checked X radio; ArrowRight from X selects Meme; Enter
  from Title or radio submits; Description Enter is not submit; Tags
  suggestion list has non-crushed min-height / absolute dropdown.
- Picker `++` / empty chrome still pass; failed Save plus path unchanged.

---

## 10. Completion, report, and expiry

Write the Section 1 report path.

Begin with `### Report for ORCHESTRATOR_CHAT` and echo once:

```text
Logical whole identity: framenest-x-companion-save-category-mvp
Worker session ordinal: 05
Worker exchange ordinal: 01
```

Include status; `Phase-qualified result: implementation-PASS` if tests green;
`Logical-whole closure: not-closed`; handshake; HEAD; paths; commands/exit
codes; R1 hide note; Near-Misses; Pre-Existing Failure Classification;
`new-mutation`; expiry; next step (Michal Reload-unpacked).

PASS: Section 3 landed; `node --test` pair green; one commit; no push.

After the terminal report, stop.

Slovak capsule data for Orchestrator presentation (not Worker instructions):

```text
🆕 PROMPT PRE FRESH WORKERA 05 • EXTRA HIGH 🧠🧠🧠
Native Plan Mode musí byť vypnutý.
▶️ Otvor nový Worker chat, vypni Plan Mode, vlož tento súbor, počkaj na 05_report_00.md.
📦 Prompt: /home/agile/meta/projects/framenest/03/06-framenest-x-companion-save-category-mvp/05_correction_00.md
📦 Report: /home/agile/meta/projects/framenest/03/06-framenest-x-companion-save-category-mvp/05_report_00.md
✅ Archival: wait-for-report
```
