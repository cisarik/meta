# Kronika — Fresh Orchestrator Handoff

```text
Restoration classification: PARTIAL
Handout status: provisional
Capability profile: Orchestrator
Initialization signal: You are a fresh Orchestrator instance assigned to the ORCHESTRATOR role for the Kronika project.
Orchestrator session scope: logical-whole
Development run identity: kronika-run-01
Current phase: Restoration (Continuation Bootstrap Stage 1 not yet performed)
Reasoning recommendation: selecting a Worker is premature
Restoration date: 2026-11-08
Refreshed: 2026-11-08
Refreshed against: AP d7023cf; Kronika 246c9f8; .ap d7023cf
Handout author: Master Orchestrator, AP run 10
Original handout author: the Master Orchestrator of Kronika development run 01 (also its original mechanical persister)
Mechanical persister: Fresh Implementation Worker session 07
Predecessor whole: projects/kronika/01/01-timeline-and-history-media-thumbnails (provisional at the refresh; not opened, not closed)
Run map: /Users/agile/meta/projects/kronika/01/00_RUN_MAP.md
Handout destination: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/
Restoration grants mutation authority: no
```

This prompt transfers information, never authority. It is a **provisional
seed**: it was written, and refreshed on 2026-11-08, before the predecessor
whole opened. The per-whole Orchestrator revalidates it in Continuation
Bootstrap Stage 1 and records a Handout Revalidation Record before the first
Planner prompt. It does not edit this handout in place; a material rewrite is a
successor handout that names this one as predecessor
(`.ap/AP.md#run-level-handouts`). A stale handout is evidence, not authority.

**Refresh note (2026-11-08).** This handout was refreshed in place before its
whole opened, under the Cooperator-accepted AP run 10 refresh, applying the
corrections that the AP run 10 pilot probe recorded for the sibling handout 01
(`/Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/06_report_00.md`)
where this handout's own content required them. The refresh updates state
facts, metadata and the AP operating rules to AP `d7023cf`. The recommended
whole, scope questions, strategic continuity and risk content are unchanged.
Superseded claims and reasons: the former restoration classification and
readiness verdict were not AP values; the former "may rewrite this handout"
instruction contradicted the AP freeze-on-open rule; the predecessor label
"handed off" collided with the run-entry status vocabulary; HEAD/public main
`7ee4684` and AP pin `73e20ef` were superseded by the pin-only commit
`246c9f8`; the former §4.1 report-field block, the §4.2 check owner, the §4.3
restart sentence and the §4.5 rule sources were replaced by pointers to their
AP `d7023cf` owners. Mechanical persistence: AP run 10, logical whole
`master-orchestrator-and-report-persistence`, Worker session 07, exchange 01.

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
  structures, including the Run Map Record, Provisional Handout Marker and
  Handout Revalidation Record;
- the upgrade ledger declared in `AGENTS.md`, `docs/AP_UPGRADE_OBSERVATIONS.md`;
- the run map `/Users/agile/meta/projects/kronika/01/00_RUN_MAP.md` and the
  predecessor handouts under `/Users/agile/meta/projects/kronika/01/`;
- the previous whole's closure record and reports under
  `/Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/`
  when they exist.

The Master Orchestrator's handouts are **provisional seeds**. They do not
replace Stage 1 verification, the per-whole Planner, or the COOPERATOR's
selection.

Meta `/Users/agile/meta/AP_DEFECTS.md` (§0.0, D-17b, D-19, D-20, D-21) and
`/Users/agile/meta/AP_DESTILLED.md` (§17) remain citable consumer evidence of
what the predecessor run measured. They are not rule sources: the direct-write
default, the mutation axes, the satisfiability check, consumed coordinates and
the standing maintenance duty are owned by AP at `d7023cf`.

---

## 1. Continuation Bootstrap, Stage 1 — restore and reconcile read-only

Verify, do not trust this handout. The state below is **last observed** at the
2026-11-08 refresh; the predecessor whole is expected to change it.

### 1.1 Repository

```text
Repository: https://github.com/cisarik/kronika (main)
Local checkout: /Users/agile/Projects/kronika
Last observed HEAD: 246c9f86b72e652cd36ed0d9f4e19e77f972df91
Last observed public main: 246c9f86b72e652cd36ed0d9f4e19e77f972df91
Last observed commit subject: docs: update analytic programming
Last observed working tree: clean
```

`246c9f8` is a pin-only commit over `7ee4684`; it changes no runtime path.

Re-verify with `git rev-parse HEAD`, `git ls-remote origin refs/heads/main`,
and `git status --short`. A different HEAD or dirty tree is a new state;
reconcile it before selecting the whole. If the predecessor whole has not
closed, stop and wait for its closure.

### 1.2 Governing AP

```text
AP pin last observed: d7023cf037f6d17885c3ede5c04812c61640da50
Governing variant: stable
```

AP public main was `d7023cf` at the refresh (ADR-0026 run-scoped orchestration
and direct-write report persistence, with its correction).

Verify `git ls-tree HEAD .ap`, `git -C .ap rev-parse HEAD`, and
`./.ap/ap doctor`. Do not upgrade the pin as part of this whole unless the
COOPERATOR explicitly selects that separate task.

### 1.3 Repository gate

```text
./.ap/ap project check --root /Users/agile/Projects/kronika \
  --baseline <current public main SHA>
```

Expected: PASS. Public `main` was `246c9f8` at the refresh; the predecessor
whole is expected to move it, so use the exact SHA observed in Stage 1. Python
evidence and tests go only through the declared
`./.ap/ap exec --operation test-focus` route. JavaScript tests use
`node --test`. Cursor/AppImage Workers must never invoke `.venv/bin/python`,
`python`, `python3`, or `poetry run` for evidence.

### 1.4 NUC state — last observed, NOT revalidated

The predecessor run last observed the NUC at `7ee4684` (docs/tests on top of
the E3-accepted `cb5fa4d` runtime). The 2026-11-08 refresh did **not**
revalidate it; NUC contact was not authorized. The NUC is expected to stay at
`7ee4684` until a separate routine refresh. Re-verify through
`deploy/ubuntu/kronika-release status`; the helper needs the COOPERATOR's
active global sudo timestamp. Never assume it persists across a Worker's
terminal `sudo -K`.

### 1.5 Previous whole closure

At the 2026-11-08 refresh the previous whole
`01-timeline-and-history-media-thumbnails` was **provisional: not opened and not
closed**; no closure evidence exists. This whole depends on its closure in the
run map's recommended order (see also risk U6). Read its closure record when it
exists. Do not assume its scope, files, or residuals. If it is still active,
stop; this whole waits. If the COOPERATOR reorders the run, revalidate the
dependency instead of assuming it.

### 1.6 Upgrade ledger

`AGENTS.md` declares the AP upgrade ledger outside the managed block
(`Ledger path: docs/AP_UPGRADE_OBSERVATIONS.md`). Validate the declared file and
revalidate every active entry against the current repository and the governing
pin before relying on it (`.ap/AP.md#continuation-bootstrap`,
`.ap/PROMPT_CONTRACTS.md#upgrade-observation-ledger-contract`).

### 1.7 Handout Revalidation Record

Before the first Planner prompt, revalidate every material fact in this handout
against current evidence and record the Handout Revalidation Record
(`.ap/PROMPT_CONTRACTS.md#handout-revalidation-record`) in this whole's
`00_notes.md` (`.ap/AP.md#run-level-handouts`; Meta `README.md`, Run Maps and
Provisional Handouts). Name every material fact you could not observe under
`Not revalidated`, including the NUC state when NUC access is not granted.

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

These entries are provisional in the run map, which is discovery-only; do not
start one without the COOPERATOR's explicit selection:

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

This handout grants nothing. AP precedence (RF-19) and the AP owners at the
governing pin govern every prompt. Each rule below records what the
predecessor run measured and points to the AP owner that now holds it; if a
pointer and its owner disagree, the owner wins.

### 4.1 Reports are written by the Worker, not ferried by the COOPERATOR

AP `d7023cf` owns the direct-write default
(`.ap/AP.md#direct-write-report-persistence`), the three mutation axes
(`.ap/AP.md#mutation-axes`, `.ap/PROMPT_CONTRACTS.md#mutation-axes-record`),
and the delivery record with its consistency rules P1–P5
(`.ap/PROMPT_CONTRACTS.md#cooperator-delivery-and-trace-destination-record`).
The Worker writes its terminal report to the exact trace path, reads it back,
and only then sends its terminal notice; the Orchestrator verifies the report
from the trace; the COOPERATOR or authorized Git owner commits the
prompt/report pair only after the report exists.

For the default route, a newly issued Worker prompt uses these AP spellings,
each line exactly once. This is a spelling projection only; the owners above
govern:

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: <exact prompt filename>
Destination path: <exact whole directory>
Report filename: <exact report filename>
Prompt persistence owner: <named actor>
Report persistence owner: assigned WORKER
Git publication owner: <named actor>
Archival: wait-for-report
Repository mutation: none | <exact repository paths>
Host/remote mutation: none | <exact targets and operations>
Trace persistence: direct-write <exact report path>
```

An issued prompt resolves every placeholder and alternative to one value. For
an authorized Planner, `Trace persistence` also names the exact received prompt
path (P1), and the prompt names the client completion route (P4). In-session
relay is exceptional: it requires an explicit COOPERATOR selection or a
recorded missing Worker capability, names that other `Report persistence owner`,
states the relay basis, sets `Trace persistence: none`, and the Worker returns
the complete report in the session (P2).

### 4.2 Prompt satisfiability before dispatch

Before delivery, apply the four comparisons owned by
`.ap/AP.md#prompt-satisfiability-check` to the complete prompt:

```text
VALIDATION–AUTHORITY  every required command, observation, generated output and
                      completion write fits the positive authority; no negative
                      clause forbids it
ROUTING               every identity, coordinate, route, mode and destination
                      field holds exactly one concrete value
PERSISTENCE           persistence owners, the three mutation axes, positive
                      authority and the client's permitted completion route
                      agree (delivery record P1–P5)
SPELLING              every path, tool, environment variable, field and command
                      comes from its current durable owner, not memory or an
                      earlier handout
```

A validation command that the prompt's own negative authority forbids is a
prompt defect. Do not issue it and wait for a Worker to block.

### 4.3 First Planner and coordinates

- Every new logical whole starts with a Planner in Worker session `01`,
  exchange `01`, `fresh-worker-session`, `Native planning mode: required`
  (`.ap/AP.md#orchestration-planning-and-implementation-planning`).
- The Planner is read-only for the repository; under the direct-write default
  it still writes its own report to the exact trace path.
- Coordinates are consumed once their prompt is issued, whatever the outcome
  (`.ap/AP.md#consumed-coordinates`). If the first exchange stops on a prompt
  defect and a fresh session is selected, the corrected initial Planner is
  `02/01`; the Meta files are `02_planning_00.md` and `02_report_00.md`, not the
  expected `01_planning_00.md`
  (`.ap/PROMPT_CONTRACTS.md#blocked-first-exchange-example`). Tell the
  COOPERATOR explicitly.
- Meta filenames follow the trace-local mapping
  (`.ap/PROMPT_CONTRACTS.md#trace-local-filename-mapping-example` and the Meta
  `README.md`): `<session>_<phase>_<exchange-index>.md` and
  `<session>_report_<exchange-index>.md`; the exchange index is the AP exchange
  ordinal minus one.

### 4.4 Delivery route

Ask the COOPERATOR once around the first Planner to select direct session
dispatch or manual copy-paste; preserve the selection through the whole (AP §3
delivery selection; the Cooperator Presentation Profile in `AGENTS.md`). The
previous whole used manual copy-paste. The report itself is still direct-write
by the Worker; the COOPERATOR does not ferry the report file.

### 4.5 AP maintenance is part of normal work

AP §13 owns the standing duty (`.ap/AP.md#standing-ledger-maintenance`):
revalidate the declared upgrade ledger in Stage 1 (§1.6); record newly measured
friction against AP as `untriaged` entries in `docs/AP_UPGRADE_OBSERVATIONS.md`
only under an exact write grant, otherwise as non-authorizing ledger candidates
in the closure or handoff record. A pin update remains its own explicit AP
update task (`AGENTS.md`). Meta `AP_DEFECTS.md` and `AP_DESTILLED.md` are
citable consumer evidence only, not AP rule sources or ledger discovery
sources. Do not ask the COOPERATOR to re-explain friction already recorded
there or in the ledger.

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
2. Validate the declared upgrade ledger `docs/AP_UPGRADE_OBSERVATIONS.md` and
   revalidate every active entry at the current pin (§1.6).
3. Verify the repository gate, AP pin, `ap doctor`, `ap project check`, public
   `main`, and the NUC status through the canonical helper when NUC access is
   granted; otherwise carry the NUC state as not revalidated.
4. Read the predecessor whole's closure record and reports when they exist,
   and the run map.
5. Revalidate this handout's material facts and prepare its Handout
   Revalidation Record (§1.7).
6. Present the restored state and this recommended whole to the COOPERATOR in
   his presentation profile. Ask one decision: select this whole or another.
7. Only after selection, create this whole's `00_notes.md`, record the Handout
   Revalidation Record there, ask once for the delivery route, and issue the
   first Planner prompt for session `01`, exchange `01`, with `Native planning
   mode: required` and `Report persistence owner: assigned WORKER` under the
   direct-write default.
8. Freeze `00_notes.md` only at closure.

The Meta directory is:

```text
/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/
```

---

## 7. Readiness review of this handout

| Review | Result |
|---|---|
| Contradiction | No contradiction found between this handout and the state observed at the 2026-11-08 refresh; the predecessor whole has not opened, so the state will change |
| Omission | The whole is a recommendation, not a selected objective; the COOPERATOR must select it |
| Stale state | Repository and AP pin observed at the 2026-11-08 refresh; NUC not revalidated; predecessor not closed; revalidate all |
| Authority | No mutation authority transferred; every next action needs a new grant |
| Active mutation | None |
| Active Worker | None for this whole |
| Security boundary | Upload capability, quarantine, validation and privacy must not widen |
| Strategic direction | ADR-0082 through ADR-0086 preserved |
| Next-step executability | Executable after Stage 1 verification, the Handout Revalidation Record, predecessor closure, and the COOPERATOR's selection |

Overall: **PARTIAL** — useful continuity exists, but the whole has not opened,
the predecessor whole is not closed, and the NUC state is not revalidated. This
is a prepared handoff, not a current-state authority.

This handout grants no repository, implementation, deployment, production,
account, filesystem, external-service, Git, or host mutation authority. Verify
independently, then ask Michal one decision.
