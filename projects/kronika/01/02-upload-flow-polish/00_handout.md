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
Restoration date: 2026-11-09
Refreshed: 2026-11-09
Refreshed against: AP d7023cf; Kronika b66ec8f; .ap d7023cf
Handout author: the run-scoped Orchestrator of Kronika run 01 (this session)
Original handout author: Master Orchestrator, AP run 10
Mechanical persister: the same run-scoped Orchestrator
Predecessor whole: projects/kronika/01/01-timeline-and-history-media-thumbnails (E2 acceptance-PASS; publication-PASS; deployment-PASS; Cooperator rendered acceptance carried; formal closure pending)
Run map: /Users/agile/meta/projects/kronika/01/00_RUN_MAP.md
Handout destination: /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/
Restoration grants mutation authority: no
```

This prompt transfers information, never authority. It is a **provisional
seed**: it was refreshed on 2026-11-09, before this whole opened, after the
COOPERATOR explicitly selected `upload-flow-polish` as the next whole. The
receiving per-whole Orchestrator revalidates it in Continuation Bootstrap
Stage 1 and records a Handout Revalidation Record before the first Planner
prompt. It does not edit this handout in place; a material rewrite is a
successor handout that names this one as predecessor
(`.ap/AP.md#run-level-handouts`).

**Refresh note (2026-11-09).** This handout was refreshed in place before its
whole opened. It updates the repository, AP, NUC, predecessor, run-map and
selection state after whole 01 was implemented, accepted at E2, published and
deployed. It also records the COOPERATOR's operating preferences for this
whole: no subagents, manual Cooperator delivery of every Worker prompt, exact
Meta prompt/report archiving, and direct-write Worker reports. Superseded
claims and reasons: HEAD/public `main` `246c9f8` was superseded by `b66ec8f`;
the NUC moved from `7ee4684` to `b66ec8f`; predecessor 01 moved from
`provisional` to accepted/published/deployed with rendered acceptance carried;
the whole is now selected rather than recommended; the former ask-once delivery
route is resolved to manual Cooperator delivery; the former "select this whole
or another" Stage 2 question is already answered by the COOPERATOR. The
recommended scope, strategic continuity and security boundaries remain.

**Run-order note (2026-11-09).** After this handout was prepared, the
COOPERATOR's first rendered-review step on whole 01 found that the approved-only
Timeline did not match the intended complete chronicle. He selected route A: a
new logical whole `timeline-complete-chronicle` (run map entry 09) to run before
this one. This handout remains provisional and prepared, but do not open this
whole until the COOPERATOR confirms after entry 09, unless he explicitly
reorders. Entry 09 is now closed; the Cooperator added a final application-shell
UI/UX consistency whole (entry 10) before this one, so expect to wait for entry
10 instead. Revalidate the run map, whole 01, entry 09 and entry 10 state in
Stage 1.

The COOPERATOR is **Michal**. Chat with him in **Slovak**, address him with
masculine grammatical forms, and refer to yourself with **feminine** forms.
Worker prompts, Worker reports, repository documentation, and Meta artifacts are
professional **English**.

---

## 0. Cooperator operating preferences for this whole

These are project-local operating instructions from the COOPERATOR. They sit
inside AP and do not override it.

```text
No subagents. The Orchestrator must not call the subagent tool or delegate any
  Worker task to a subagent. The Orchestrator prepares prompts and reconciliation
  itself.

Meta is the prompt/report archive. Write every Orchestrator-owned prompt,
  report, note, handout and run-map update into the exact Meta path. Do not keep
  task prompts only in chat.

Manual Worker delivery. The COOPERATOR sends every Worker prompt manually. The
  Orchestrator archives the complete prompt in Meta, presents the delivery
  capsule, and waits for the COOPERATOR to deliver it. The Orchestrator does not
  dispatch Workers directly.

Direct-write Worker reports. Every Worker prompt requires the Worker to write its
  terminal report directly to the exact Meta path and read it back. The
  COOPERATOR never copy-pastes report content. The Orchestrator verifies the
  report from the trace.

Meta Git belongs to the COOPERATOR. The Orchestrator writes files but does not
  stage, commit, push or rewrite Meta history.

Repository and NUC work stay under the exact current Worker grant. The
  Orchestrator may inspect read-only; mutation needs a complete prompt.
```

The prompt/report pair is archived together in Meta only after the report
exists. The COOPERATOR owns that Git action.

---

## 1. Read this first

Read this handout together with:

- `AGENTS.md` at the Kronika repository root and its managed AP block;
- `.ap/AP.md`, `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md` at the pinned AP
  commit, per the ORCHESTRATOR minimum-reading spine;
- `.ap/PROMPT_CONTRACTS.md` for the planning, implementation, acceptance, report
  and trace structures, including the Run Map Record, Provisional Handout
  Marker and Handout Revalidation Record;
- the upgrade ledger declared in `AGENTS.md`,
  `docs/AP_UPGRADE_OBSERVATIONS.md`;
- the run map `/Users/agile/meta/projects/kronika/01/00_RUN_MAP.md`;
- the predecessor whole's `00_notes.md`, `01_planning_00.md`,
  `01_report_00.md`, `02_implementation_00.md`, `02_report_00.md`,
  `02_correction_01.md` and `02_report_01.md` under
  `/Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/`;
- the closed 00 whole's `00_notes.md` and the closed 00 handout's §9.2
  candidate list under
  `/Users/agile/meta/projects/kronika/01/00-ux-refresh-acceptance-and-promotion/`.

The predecessor notes and reports are frozen historical evidence. Read them for
continuity; do not rewrite them.

Meta `/Users/agile/meta/AP_DEFECTS.md` (§0.0, D-17b, D-19, D-20, D-21) and
`/Users/agile/meta/AP_DESTILLED.md` (§17) remain citable consumer evidence of
what the predecessor run measured. They are not rule sources: the direct-write
default, the mutation axes, the satisfiability check, consumed coordinates and
the standing maintenance duty are owned by AP at `d7023cf`.

---

## 2. Continuation Bootstrap, Stage 1 — restore and reconcile read-only

Verify, do not trust this handout. The state below was observed on 2026-11-09
after whole 01 was published and deployed; revalidate every material fact.

### 2.1 Repository

```text
Repository: https://github.com/cisarik/kronika (main)
Local checkout: /Users/agile/Projects/kronika
Last observed HEAD: b66ec8f50860ace624f6be1fd3ad63f521edcd33
Last observed public main: b66ec8f50860ace624f6be1fd3ad63f521edcd33
Last observed tip subject: fix: keep card previews across visibility changes
Last observed working tree: clean
```

The tip is the correction commit over the implementation commit `72e8bb0`;
both are published. The change set is the fourteen-path Timeline/History
thumbnail slice recorded in whole 01. `b66ec8f` is the public baseline for this
whole. Verify with `git rev-parse HEAD`, `git ls-remote origin
refs/heads/main`, and `git status --short`.

### 2.2 Governing AP

```text
AP pin last observed: d7023cf037f6d17885c3ede5c04812c61640da50
Governing variant: stable
```

AP public `main` was `d7023cf` at the refresh. Verify `git ls-tree HEAD .ap`,
`git -C .ap rev-parse HEAD`, and `./.ap/ap doctor`. Do not upgrade the pin as
part of this whole unless the COOPERATOR explicitly selects that separate task.

### 2.3 Repository gate

```text
./.ap/ap project check --root /Users/agile/Projects/kronika \
  --baseline b66ec8f50860ace624f6be1fd3ad63f521edcd33
```

Expected: PASS. Python evidence and tests go only through the declared
`./.ap/ap exec --operation test-focus` route. JavaScript tests use `node --test`.
Cursor/AppImage Workers must never invoke `.venv/bin/python`, `python`,
`python3`, or `poetry run` for evidence.

### 2.4 NUC state — observed after the 2026-11-09 deployment

```text
layout: canonical
active_release: b66ec8f50860ace624f6be1fd3ad63f521edcd33
web_release: b66ec8f50860ace624f6be1fd3ad63f521edcd33
capture_release: 5b86d896b3ea03f89fef2c90f7af2c121d0ef915
service_active: active
database_revision: 0035
backup_restore_readiness: ready
```

Whole 01 completed a same-schema routine deployment at `b66ec8f`; the deployed
shell contains the Timeline/History preview implementation. Terminal `sudo -K`
was run and a following `sudo -n true` required a password, so the Cooperator's
timestamp is revoked. A later deployment needs a fresh Cooperator `sudo -v`.
Revalidate with `deploy/ubuntu/kronika-release status` only when NUC access is
granted; do not assume the timestamp persists.

### 2.5 Predecessor whole state and the selection

Whole 01 `timeline-and-history-media-thumbnails` is:

- E2 acceptance-PASS at `b66ec8f` after one pre-acceptance correction;
- publication-PASS on public `main` at `b66ec8f`;
- deployment-PASS on the NUC at `b66ec8f`;
- **formally not closed**, because the COOPERATOR's rendered UI/UX acceptance
  has not been recorded. The Cooperator directed publication and deployment and
  then selected whole 02; he did not declare a rendered verdict.

The COOPERATOR explicitly selected `upload-flow-polish` on 2026-11-09 and
directed it to proceed while whole 01's rendered acceptance remains a carried
Cooperator-owned item. Do not reopen whole 01, do not rewrite its notes or
reports, and do not stop solely because its formal closure is pending. Read its
notes and reports for continuity, then proceed with this whole.

The run map currently records entry 01 as `active` and entry 02 as
`handed-off`. Run-map status changes belong to the run-scoped Orchestrator; do
not change them unless the COOPERATOR grants that role explicitly.

### 2.6 Upgrade ledger

`AGENTS.md` declares the AP upgrade ledger outside the managed block
(`Ledger path: docs/AP_UPGRADE_OBSERVATIONS.md`). Validate the declared file and
revalidate every active entry against the current repository and the governing
pin before relying on it (`.ap/AP.md#continuation-bootstrap`,
`.ap/PROMPT_CONTRACTS.md#upgrade-observation-ledger-contract`).

### 2.7 Handout Revalidation Record

Before the first Planner prompt, revalidate every material fact in this handout
against current evidence and record the Handout Revalidation Record
(`.ap/PROMPT_CONTRACTS.md#handout-revalidation-record`) in this whole's
`00_notes.md` (`.ap/AP.md#run-level-handouts`; Meta `README.md`, Run Maps and
Provisional Handouts). Name every material fact you could not observe under
`Not revalidated`, including NUC state when NUC access is not granted and the
Cooperator's unrecorded rendered acceptance for whole 01.

---

## 3. Continuation Bootstrap, Stage 2 — preserve the selected whole

The COOPERATOR has already selected **`upload-flow-polish`**. Preserve that
selection; do not ask him to choose the whole again. Present the restored state
and proceed to the first Planner prompt after the Handout Revalidation Record.

### 3.1 Objective

Make the ordinary upload flow smoother without weakening duplicate review,
validation, capability gates, quarantine, or privacy:

- optionally start an upload automatically after the file is chosen, while
  preserving the existing duplicate review;
- show upload progress and terminal state from the companion side panel;
- keep the current upload capability, quarantine, validation, and publication
  semantics.

The COOPERATOR's own framing from the closed 00 handout: *"Upload flow polish —
optional automatic start after choosing a file while preserving duplicate
review; progress visible from the companion."*

### 3.2 Scope shape (for the Planner, not a grant)

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

### 3.3 Questions the Planner must answer with repository evidence

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
7. What is the exact NUC refresh and rendered-acceptance sequence, given the
   current public baseline `b66ec8f` and the revoked sudo timestamp?
8. What is the smallest change that improves the flow without turning the
   upload dialog into a second upload manager?
9. What did whole 01 change in the shell and card surfaces that could affect the
   upload dialog, the companion bridge, or their tests? Re-measure; do not
   assume the predecessor's scope is unrelated.

### 3.4 Other candidate wholes

These entries remain provisional in the run map, which is discovery-only; do
not start one without the COOPERATOR's explicit selection:

1. Companion download notifications.
2. Household onboarding.
3. Humanized error copy.
4. Accessibility pass.
5. `app.js` modularization planning.
6. Product language decision.

---

## 4. Strategic continuity — what Kronika is

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
- Whole 01 added safe Timeline/History preview locators and client preview
  lifecycle. It did not change the upload route, upload capabilities, quarantine,
  duplicate disposition, publication semantics, or the Gallery/Details renderer.

---

## 5. Operating rules

This handout grants nothing. AP precedence (RF-19) and the AP owners at the
governing pin govern every prompt. Each rule below records what the predecessor
run measured and points to the AP owner that now holds it; if a pointer and its
owner disagree, the owner wins.

### 5.1 Manual Worker prompt delivery and direct-write reports

The COOPERATOR delivers every Worker prompt manually. The Orchestrator's job is
to prepare one complete authoritative prompt, archive it in Meta at the exact
filename, present the delivery capsule, and wait. It must not dispatch a Worker
or use a subagent.

The Worker writes its terminal report directly to the exact Meta path, reads it
back, and only then sends its terminal notice. The Orchestrator verifies the
report from the trace; the COOPERATOR never copy-pastes report content. The
COOPERATOR or authorized Git owner commits the prompt/report pair only after the
report exists.

For every Worker prompt, use these AP spellings, each line exactly once. This
is a spelling projection only; the AP owners above govern:

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: <exact prompt filename>
Destination path: <exact whole directory>
Report filename: <exact report filename>
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: none | <exact repository paths>
Host/remote mutation: none | <exact targets and operations>
Trace persistence: direct-write <exact report path>
```

Resolve every placeholder and alternative to one value. For an authorized
Planner, `Trace persistence` also names the exact received prompt path (P1),
and the prompt names the client completion route (P4). In-session relay is
exceptional: it requires an explicit COOPERATOR selection or a recorded missing
Worker capability, names that other `Report persistence owner`, states the relay
basis, sets `Trace persistence: none`, and the Worker returns the complete
report in the session (P2).

### 5.2 Prompt satisfiability before delivery

Before presenting a prompt for manual delivery, apply the four comparisons owned
by `.ap/AP.md#prompt-satisfiability-check` to the complete prompt:

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

### 5.3 First Planner and coordinates

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

### 5.4 No subagents

The Orchestrator must not use the `subagent` tool or any equivalent internal
delegation for Worker tasks. It may use read-only shell and file tools itself for
restoration and reconciliation. Every implementation, planning, acceptance,
correction, audit, deployment or probe task goes into a complete archived Worker
prompt that the COOPERATOR delivers manually.

### 5.5 AP maintenance is part of normal work

AP §13 owns the standing duty (`.ap/AP.md#standing-ledger-maintenance`):
revalidate the declared upgrade ledger in Stage 1 (§2.6); record newly measured
friction against AP as `untriaged` entries in
`docs/AP_UPGRADE_OBSERVATIONS.md` only under an exact write grant, otherwise as
non-authorizing ledger candidates in the closure or handoff record. A pin update
remains its own explicit AP update task (`AGENTS.md`). Meta `AP_DEFECTS.md` and
`AP_DESTILLED.md` are citable consumer evidence only, not AP rule sources or
ledger discovery sources. Do not ask the COOPERATOR to re-explain friction
already recorded there or in the ledger.

### 5.6 Security boundaries and execution routes

- NUC SSH for Workers goes only through
  `scripts/operator/network/kronika_nuc_worker_gate.fish` (`--probe` first).
  Do not reconstruct `gpgconf` or print agent sockets.
- The canonical operator variables are `KRONIKA_NUC_SSH_TARGET`,
  `KRONIKA_NUC_SSH_USER`, `KRONIKA_NUC_SSH_IDENTITY`, and
  `KRONIKA_NUC_SSH_COMMAND`. The release helper requires the identity as a
  private-key path.
- The COOPERATOR runs `sudo -v` outside the Worker; Workers verify with
  `sudo -n true`, never handle a password, and follow the grant's terminal
  `sudo -K` rule. A timestamp is global and a Worker `sudo -K` revokes it. The
  predecessor deployment revoked the timestamp; a later deployment needs a
  fresh Cooperator `sudo -v`.
- Deployment is only `deploy/ubuntu/kronika-release status` → `check --release
  <40-hex>` → explicit authority → `deploy --release <40-hex> --yes`. A check
  never deploys. Schema jumps use the documented `migration-required` (exit 13)
  continuation.
- No secret, credential, token, cookie, private media filename, host-specific
  identifier, disk serial, UUID, SSH fingerprint, or private network value
  enters repository artifacts or reports.

---

## 6. Forward risk register

| ID | Item | Class | Owner |
|---|---|---|---|
| U1 | `app.js` monolith; UI collateral and test churn | maintainability | Planner |
| U2 | Duplicate review could be bypassed by automatic start | product/security | Planner/audit |
| U3 | Companion progress may require a new message type | protocol/security | Planner |
| U4 | Upload capability and privacy boundaries could widen | security | Planner/audit |
| U5 | Test pins on upload markup, copy and CSS | test churn | Planner |
| U6 | Whole 01 changed Timeline/History card previews and shell lifecycle | cross-whole dependency | Planner |

U6 is now measured, not speculative: whole 01 added a preview helper, list
cancellation and pagehide retirement in `app.js`, and scoped card CSS. The
upload dialog, upload routes, upload capabilities and companion bridge were not
changed. The Planner must still re-measure any shared shell state, test harness
or lifecycle interaction that the upload flow touches.

The next whole must not weaken `upload.submit`, quarantine, validation, duplicate
disposition, or publication semantics to make the flow convenient. Those are
acceptance claims, not implementation details.

---

## 7. First actions for the fresh Orchestrator

1. Read `AGENTS.md`, the AP spine, `AP_ORCHESTRATOR.md`, and the named
   `PROMPT_CONTRACTS.md` sections.
2. Validate the declared upgrade ledger `docs/AP_UPGRADE_OBSERVATIONS.md` and
   revalidate every active entry at the current pin (§2.6).
3. Verify the repository gate, AP pin, `ap doctor`, `ap project check`, public
   `main`, the predecessor's publication/deployment evidence, and the NUC status
   through the canonical helper when NUC access is granted; otherwise carry the
   NUC state as not revalidated.
4. Read the predecessor whole's notes and reports, and the run map.
5. Revalidate this handout's material facts and record its Handout Revalidation
   Record in this whole's `00_notes.md` (§2.7).
6. Preserve the COOPERATOR's explicit selection of `upload-flow-polish`. Present
   the restored state in his presentation profile; do not ask him to select a
   whole again. If a material contradiction requires a decision, ask exactly one.
7. Create this whole's `00_notes.md` at opening and record the Handout
   Revalidation Record there. The COOPERATOR owns the Meta Git commit.
8. Prepare the first Planner prompt for session `01`, exchange `01`,
   `fresh-worker-session`, `Native planning mode: required`, `Planning cycle:
   initial`, `Plan disposition: approval-gated`, implementation in the same
   session prohibited, `Post-plan implementation session: fresh-worker-session`,
   `Report persistence owner: assigned WORKER`, and direct-write report
   `01_report_00.md`. Archive it as `01_planning_00.md`.
9. Present the delivery capsule to the COOPERATOR and wait for him to deliver
   the prompt manually. Do not dispatch, do not use a subagent, and do not
   commit Meta. When the Worker report appears at `01_report_00.md`, read it
   back, reconcile it as a claim, and continue with the next complete prompt.
10. Freeze `00_notes.md` only at closure. Whole 01's rendered acceptance remains
    a carried Cooperator-owned item; record it as such, not as satisfied.

The Meta directory is:

```text
/Users/agile/meta/projects/kronika/01/02-upload-flow-polish/
```

---

## 8. Readiness review of this handout

| Review | Result |
|---|---|
| Contradiction | No contradiction found between this handout and the 2026-11-09 repository, AP, NUC, predecessor and run-map state |
| Omission | Whole 01's rendered UI/UX acceptance is not recorded; it is carried as a Cooperator-owned item. The whole is selected, not merely recommended |
| Stale state | Repository/public `main` and NUC are observed at `b66ec8f`; revalidate. The NUC sudo timestamp is revoked; a later deployment needs a fresh Cooperator `sudo -v` |
| Authority | No mutation authority transferred; every Worker action needs a new complete prompt delivered manually by the COOPERATOR |
| Active mutation | None |
| Active Worker | None for this whole |
| Security boundary | Upload capability, quarantine, validation, duplicate review and privacy must not widen |
| Strategic direction | ADR-0082 through ADR-0086 preserved; whole 01's preview change is recorded as accepted context, not as reopened scope |
| Next-step executability | Executable after Stage 1 verification, the Handout Revalidation Record, and the first archived Planner prompt |

Overall: **PARTIAL** — useful continuity exists and the COOPERATOR has selected
this whole, but the whole has not opened, the NUC state must be revalidated, and
whole 01's rendered acceptance remains a carried Cooperator-owned item. This is
a prepared handoff, not current-state authority.

This handout grants no repository, implementation, deployment, production,
account, filesystem, external-service, Git, or host mutation authority. Verify
independently, then prepare the first Planner prompt for the COOPERATOR's
manual delivery.
