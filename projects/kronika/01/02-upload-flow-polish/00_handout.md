# Kronika — Fresh Orchestrator Handoff

```text
Restoration classification: PROVISIONAL
Capability profile: Orchestrator
Initialization signal: You are a fresh Orchestrator instance assigned to the ORCHESTRATOR role for the Kronika project.
Restoration date: 2026-11-08
Handout author: the Master Orchestrator of Kronika development run 01
Mechanical persister: the same instance, writing this file outside the repository
Predecessor whole: projects/kronika/01/01-timeline-and-history-media-thumbnails (handed off, not yet executed)
Handout destination: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/
Restoration grants mutation authority: no
```

This prompt transfers information, never authority. It is **provisional**: it
was written before the predecessor whole executed. The per-whole Orchestrator
must revalidate current state and may rewrite this handout before the first
Planner prompt. A stale handout is evidence, not authority.

The COOPERATOR is **Michal**. Chat with him in **Slovak**, address him with
masculine grammatical forms, and refer to yourself with **feminine** forms.
Worker prompts, Worker reports, repository documentation, and Meta artifacts are
professional **English**.

---

## 0. Read this first

Read this handout together with:

- `AGENTS.md` at the Kronika repository root and its managed AP block;
- `.ap/AP.md`, `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md` at the pinned AP
  commit, per the ORCHESTRATOR minimum-reading spine;
- `.ap/PROMPT_CONTRACTS.md` for prompt, planning, acceptance, report and trace
  structures;
- `/Users/agile/meta/AP_DEFECTS.md` §0.0 and D-17b, D-19, D-20, D-21;
- `/Users/agile/meta/AP_DESTILLED.md` §17;
- the run map and the predecessor handouts under
  `/Users/agile/meta/projects/kronika/01/`;
- the previous whole's closure record and reports under
  `/Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/`
  when they exist.

The Master Orchestrator's handouts are **provisional seeds**. They do not
replace Stage 1 verification, the per-whole Planner, or the COOPERATOR's
selection.

---

## 1. Continuation Bootstrap, Stage 1 — restore and reconcile read-only

Verify, do not trust this handout. The state below is **last observed** at
handout creation; the predecessor whole may have changed it.

### 1.1 Repository

```text
Repository: https://github.com/cisarik/kronika (main)
Local checkout: /Users/agile/Projects/kronika
Last observed HEAD: 7ee4684f529b3d2cdf15ce30902ba01a2b39992c
Last observed public main: 7ee4684f529b3d2cdf15ce30902ba01a2b39992c
Last observed working tree: clean
```

Re-verify with `git rev-parse HEAD`, `git ls-remote origin refs/heads/main`,
and `git status --short`. A different HEAD or dirty tree is a new state;
reconcile it before selecting the whole. If the predecessor whole has not
closed, stop and wait for its closure.

### 1.2 Governing AP

```text
AP pin last observed: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
Governing variant: stable
```

Verify `git ls-tree HEAD .ap`, `git -C .ap rev-parse HEAD`, and
`./.ap/ap doctor`. Do not upgrade the pin as part of this whole unless the
COOPERATOR explicitly selects that separate task.

### 1.3 Repository gate

```text
./.ap/ap project check --root /Users/agile/Projects/kronika \
  --baseline <current public main SHA>
```

Expected: PASS. Python evidence and tests go only through the declared
`./.ap/ap exec --operation test-focus` route. JavaScript tests use
`node --test`. Cursor/AppImage Workers must never invoke `.venv/bin/python`,
`python`, `python3`, or `poetry run` for evidence.

### 1.4 NUC state

The predecessor run last observed the NUC at `7ee4684` (docs/tests on top of
the E3-accepted `cb5fa4d` runtime). Re-verify through
`deploy/ubuntu/kronika-release status`; the helper needs the COOPERATOR's
active global sudo timestamp. Never assume it persists across a Worker's
terminal `sudo -K`.

### 1.5 Previous whole closure

The previous whole `01-timeline-and-history-media-thumbnails` is **handed off,
not necessarily executed**. Read its closure record when it exists. Do not
assume its scope, files, or residuals. If it is still active, stop; this whole
waits.

---

## 2. Continuation Bootstrap, Stage 2 — select one bounded whole

Present the restored state and **one evidence-backed recommendation** to the
COOPERATOR. Obtain his selection before issuing the first Planner prompt. This
handout is a recommendation, not selection.

### 2.1 Recommended whole

**`upload-flow-polish`**

Make the ordinary upload flow smoother without weakening duplicate review,
validation, capability gates, or privacy:

- optionally start an upload automatically after the file is chosen, while
  preserving the existing duplicate review;
- show upload progress and terminal state from the companion side panel;
- keep the current upload capability, quarantine, validation, and publication
  semantics.

The COOPERATOR's own framing from the predecessor handout: *"Upload flow polish
— optional automatic start after choosing a file while preserving duplicate
review; progress visible from the companion."*

### 2.2 Scope shape (for the Planner, not a grant)

Likely in scope:

- the web shell upload dialog: file selection, validation, duplicate review,
  start, progress, terminal state;
- an optional automatic-start behavior, with a visible choice and a safe
  default;
- companion side-panel progress visibility, using the existing hosted shell
  where possible;
- the smallest companion protocol addition, if any, with pinned-origin and
  capability rules;
- tests for the dialog, the companion bridge, and the upload API behavior;
- durability documentation for the chosen behavior;
- the routine NUC refresh and the COOPERATOR's rendered acceptance.

Likely out of scope:

- a new upload backend, resumable uploads, multi-file batching, background
  uploads, or a new storage pipeline;
- changes to quarantine, validation, duplicate disposition, or publication
  semantics beyond what the UI needs;
- Gallery or Details visual redesign (frozen);
- provider calls, new secrets, or host mutation;
- onboarding, accessibility, localization, or `app.js` modularization.

### 2.3 Questions the Planner must answer with repository evidence

1. Where is the upload dialog rendered and driven today? Which functions,
   elements, state fields and CSS classes carry file selection, validation,
   duplicate review, start and progress?
2. What exactly is "duplicate review" in the current flow? Which capability
   (`upload.submit`, `upload.manage`), duplicate mode, and server response
   drive it? How can automatic start preserve it?
3. Should automatic start be a per-upload checkbox, a persisted setting, or a
   one-time prompt? What is the smallest safe behavior, and what is the default?
4. What progress can the companion side panel show? Is the hosted web shell
   already visible, or does the side panel need a new message type? If a new
   message type is needed, what is the exact protocol, origin, and capability
   guard?
5. Which tests pin the upload markup, CSS, copy, and API behavior? Which tests
   pin the companion bridge? Which assertions would a new behavior break?
6. Which documents own the new behavior: `SPEC.md` upload section, `SECURITY.md`
   upload boundary, `DEVELOPMENT.md`, `docs/X_COMPANION.md`, `docs/UX_AUDIT.md`,
   or a new ADR? Do not create a second semantic owner.
7. What is the exact NUC refresh and rendered-acceptance sequence?
8. What is the smallest change that improves the flow without turning the
   upload dialog into a second upload manager?

### 2.4 Other candidate wholes (not selected)

The run map remains provisional; do not start one without the COOPERATOR's
explicit selection:

1. Companion download notifications (completed X/YouTube downloads in the
   side-panel history and toolbar badge).
2. Household onboarding (first-run explainer for ordinary members; plain
   language install guide).
3. Humanized error copy (replace raw codes with actionable text; inventory
   first).
4. Accessibility pass (keyboard paths, contrast on glass buttons,
   screen-reader names; Cooperator rendered review).
5. `app.js` modularization planning (Discovery/Planner first; asset-serving and
   `vm` test strategy required).
6. Product language decision (the UI is English; localization is a Cooperator
   product decision).

---

## 3. Strategic continuity — what Kronika is

Kronika is a local-first, privacy-conscious household archive for video,
images and GIFs: archive, search, upload and download (YouTube and X), with
AI-assisted metadata, a premium Gallery, an administrator-curated Timeline,
personal History and provider-backed Search/Research. One authoritative FastAPI
server (SQLite + Alembic) runs on an Ubuntu Intel NUC reached only over
Tailscale; clients are the served web shell and a Chromium side-panel companion
extension.

Authoritative product truth:

- `README.md`, `PRODUCT.md`, `SPEC.md`, `ROADMAP.md`, `SECURITY.md`, `SERVER.md`;
- `docs/adr/README.md`, ADR-0082 through ADR-0086;
- `docs/UBUNTU_NUC_DEPLOYMENT.md`, `docs/WORKER_EXECUTION_CONTRACT.md`,
  `DEVELOPMENT.md`, `GALLERY.md`.

Accepted direction to preserve:

- **ADR-0082** one Kronika, private records by verified owner. **ADR-0083**
  modular research providers; Timeline is the main page and contains only
  administrator-approved records; personal History is separate; Gallery is a
  separate working view. **ADR-0084** administrator-managed research settings,
  four exact catalog models, default `gpt-5.5-2026-04-23`, no network model
  discovery, research disabled by default. **ADR-0085** sole Kronika identity;
  bounded cuts, no mass rename. **ADR-0086** companion YouTube save,
  `open_upload`, and in-process preview backfill.
- **ADR-0075** the NUC is the development-and-testing machine; routine refresh
  to the exact public `main` SHA via `deploy/ubuntu/kronika-release` is normal
  operation. **ADR-0060** immutable release contract.
- Security: loopback-first backend, Tailscale-only ingress, no port forwarding;
  Tailscale membership is not administrator authority; `/srv/media` is read-only
  to the service; ordinary clients never receive provider secrets;
  administrator read-all is application content only; household publication is
  an administrator approval; internet publication stays disabled.
- Rendered UI/UX acceptance belongs to the COOPERATOR and requires the code on
  public `main` refreshed onto the NUC first.

---

## 4. Project-specific operating rules measured in the predecessor run

These are binding on your prompts unless the COOPERATOR changes them.

### 4.1 Reports are written by the Worker, not ferried by the COOPERATOR

The corrected default is **direct-write**:

- the authoritative prompt names the exact trace report path;
- the Worker writes the terminal report to that path before its terminal
  notice, reads it back, and writes no other file;
- the Orchestrator reads and verifies the report from the trace;
- the COOPERATOR or authorized Git owner commits the prompt/report pair only
  after the report exists;
- `in-session-only` is an exceptional COOPERATOR choice, not the default.

Every Worker prompt must carry:

```text
Report author: WORKER
Report persister: WORKER
Report persistence: direct-write <exact trace path>
Report destination: <exact trace path>
Trace persistence: direct-write <exact trace path>
```

and the separate axes:

```text
Repository mutation: none | <exact paths>
Host/remote mutation: none | <exact commands>
Trace persistence: none | direct-write <exact trace path> | in-session-only
```

Read `AP_DEFECTS.md` §0.0, D-17b and D-20, and `AP_DESTILLED.md` §17.3 and
§17.6 before issuing the first prompt.

### 4.2 Prompt satisfiability before dispatch

```text
VALIDATION–AUTHORITY  every required command has a named positive authority
ROUTING               exactly one concrete value; no unresolved placeholders
PERSISTENCE           report persistence is direct-write; repository/host/trace
                      authority are separate axes
SPELLING              every path, tool, env var and command name comes from its
                      durable owner
```

A validation command that the prompt's own negative authority forbids is a
prompt defect. Do not issue it and wait for a Worker to block.

### 4.3 First Planner and coordinates

- Every new logical whole starts with a Planner in Worker session `01`,
  exchange `01`, `fresh-worker-session`, `Native planning mode: required`.
- The Planner is read-only for the repository; it still writes its own report
  to the exact trace path.
- If the first exchange is blocked by a prompt defect and its artifacts are
  withdrawn, the coordinates are still consumed. The next fresh session is
  `02/01`; the Meta filename is `02_planning_00.md`, not the expected
  `01_planning_00.md`. Tell the COOPERATOR explicitly. A true restart at
  `01/01` requires a new logical-whole identity.
- Meta filenames follow `<session>_<phase>_<exchange-index>.md` and
  `<session>_report_<exchange-index>.md`; the exchange index is the AP exchange
  ordinal minus one.

### 4.4 Delivery route

Ask the COOPERATOR once around the first Planner to select direct session
dispatch or manual copy-paste; preserve the selection through the whole. The
previous whole used manual copy-paste. The report itself is still direct-write
by the Worker; the COOPERATOR does not ferry the report file.

### 4.5 AP maintenance is part of normal work

Read `AP_DEFECTS.md` and `AP_DESTILLED.md` during restoration. Capture new
measured protocol friction in `AP_DEFECTS.md`; do not wait for a separate AP
task. The Orchestrator of an AP update must process the open backlog and update
`AP_DESTILLED.md` in the same task. Do not ask the COOPERATOR to re-explain a
recorded defect.

### 4.6 Security boundaries and execution routes

- NUC SSH for Workers goes only through
  `scripts/operator/network/kronika_nuc_worker_gate.fish` (`--probe` first).
  Do not reconstruct `gpgconf` or print agent sockets.
- The canonical operator variables are `KRONIKA_NUC_SSH_TARGET`,
  `KRONIKA_NUC_SSH_USER`, `KRONIKA_NUC_SSH_IDENTITY`, and
  `KRONIKA_NUC_SSH_COMMAND`. The release helper requires the identity as a
  private-key path.
- The COOPERATOR runs `sudo -v` outside the Worker; Workers verify with
  `sudo -n true`, never handle a password, and follow the grant's terminal
  `sudo -K` rule. A timestamp is global and a Worker `sudo -K` revokes it.
- Deployment is only `deploy/ubuntu/kronika-release status` → `check --release
  <40-hex>` → explicit authority → `deploy --release <40-hex> --yes`. A check
  never deploys. Schema jumps use the documented `migration-required` (exit 13)
  continuation.
- No secret, credential, token, cookie, private media filename, host-specific
  identifier, disk serial, UUID, SSH fingerprint, or private network value
  enters repository artifacts or reports.

---

## 5. Forward risk register

| ID | Item | Class | Owner |
|---|---|---|---|
| U1 | `app.js` monolith; UI collateral and test churn | maintainability | Planner |
| U2 | Duplicate review could be bypassed by automatic start | product/security | Planner/audit |
| U3 | Companion progress may require a new message type | protocol/security | Planner |
| U4 | Upload capability and privacy boundaries could widen | security | Planner/audit |
| U5 | Test pins on upload markup, copy and CSS | test churn | Planner |
| U6 | Preview/thumbnail work from whole 01 may change the upload UI context | cross-whole dependency | Planner |

The next whole must not weaken `upload.submit`, quarantine, validation, duplicate
disposition, or publication semantics to make the flow convenient. Those are
acceptance claims, not implementation details.

---

## 6. First actions for the fresh Orchestrator

1. Read `AGENTS.md`, the AP spine, `AP_ORCHESTRATOR.md`, and the named
   `PROMPT_CONTRACTS.md` sections.
2. Read `AP_DEFECTS.md` §0.0 and D-17b/D-19/D-20/D-21; read
   `AP_DESTILLED.md` §17.
3. Verify the repository gate, AP pin, `ap doctor`, `ap project check`, public
   `main`, and the NUC status through the canonical helper.
4. Read the predecessor whole's closure record and reports when they exist.
5. Present the restored state and this recommended whole to the COOPERATOR in
   his presentation profile. Ask one decision: select this whole or another.
6. Only after selection, ask once for the delivery route and issue the first
   Planner prompt for session `01`, exchange `01`, with `Native planning mode:
   required` and direct-write report persistence.
7. Do not create `00_notes.md` until the COOPERATOR selects the whole; then
   create it and freeze it only at closure.

The Meta directory is:

```text
/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/
```

---

## 7. Readiness review of this handout

| Review | Result |
|---|---|
| Contradiction | No contradiction found between this handout and the verified state at creation; the predecessor whole is not yet executed, so the state may change |
| Omission | The whole is a recommendation, not a selected objective; the COOPERATOR must select it |
| Stale state | Marked **PROVISIONAL**; repository, AP pin, NUC and predecessor state must be revalidated |
| Authority | No mutation authority transferred; every next action needs a new grant |
| Active mutation | None |
| Active Worker | None |
| Security boundary | Upload capability, quarantine, validation and privacy must not widen |
| Strategic direction | ADR-0082 through ADR-0086 preserved |
| Next-step executability | Executable after Stage 1 verification, predecessor closure, and the COOPERATOR's selection |

Overall: **PROVISIONAL / READY AFTER REVALIDATION** — this is a prepared handoff,
not a current-state authority.

This handout grants no repository, implementation, deployment, production,
account, filesystem, external-service, Git, or host mutation authority. Verify
independently, then ask Michal one decision.
