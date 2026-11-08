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
Original handout author: the Orchestrator of Kronika era 01, logical whole 00-ux-refresh-acceptance-and-promotion (also its original mechanical persister)
Mechanical persister: Fresh Implementation Worker session 07
Predecessor whole: projects/kronika/01/00-ux-refresh-acceptance-and-promotion (closed 2026-11-08)
Run map: /Users/agile/meta/projects/kronika/01/00_RUN_MAP.md
Handout destination: /Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/
Restoration grants mutation authority: no
```

This prompt transfers information, never authority. It does not authorize
repository, Git, NUC, deployment, browser, provider, account or filesystem
mutation. You derive every grant afresh from the governing AP, the repository
and an explicit current COOPERATOR decision.

This handout is a **provisional seed**, not authority. The receiving per-whole
Orchestrator revalidates it in Continuation Bootstrap Stage 1 and records a
Handout Revalidation Record before the first Planner prompt. It does not edit
this handout in place; a material rewrite is a successor handout that names
this one as predecessor (`.ap/AP.md#run-level-handouts`).

**Refresh note (2026-11-08).** This handout was refreshed in place before its
whole opened, under the Cooperator-accepted AP run 10 refresh, following the AP
run 10 pilot probe's Handout Revalidation Record
(`/Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/06_report_00.md`,
verdict `yes-with-corrections`). The refresh updates state facts, metadata and
the AP operating rules to AP `d7023cf`. The recommended whole, scope questions,
strategic continuity and risk content are unchanged. Superseded claims and
reasons: the former restoration classification and readiness verdict were not
AP values; HEAD/public main `7ee4684` and AP pin `73e20ef` were superseded by
the pin-only commit `246c9f8`; the former §4.1 report-field block, the §4.2
check owner, the §4.3 restart sentence and the §4.5 rule sources were replaced
by pointers to their AP `d7023cf` owners. Mechanical persistence: AP run 10,
logical whole `master-orchestrator-and-report-persistence`, Worker session 07,
exchange 01.

---

## 0. Read this first

This handout is the opening context for a new logical whole. It is **not** a
task grant, not a plan, and not a substitute for the governing AP. It records
state last observed at the 2026-11-08 refresh, the previous whole's closure,
the recommended next objective, and the project-specific operating rules that
the previous whole measured, each pointing to its current AP owner.

The COOPERATOR is **Michal**. Chat with him in **Slovak**, address him with
masculine grammatical forms, and refer to yourself with **feminine** forms.
Worker prompts, Worker reports, repository documentation, and Meta artifacts are
professional **English**.

Read this handout together with:

- `AGENTS.md` at the Kronika repository root and its managed AP block;
- `.ap/AP.md`, `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md` at the pinned AP
  commit, per the ORCHESTRATOR minimum-reading spine;
- `.ap/PROMPT_CONTRACTS.md` for the prompt, planning, acceptance, report and
  trace structures you will issue, including the Run Map Record, Provisional
  Handout Marker and Handout Revalidation Record;
- the upgrade ledger declared in `AGENTS.md`, `docs/AP_UPGRADE_OBSERVATIONS.md`;
- the run map `/Users/agile/meta/projects/kronika/01/00_RUN_MAP.md`;
- the predecessor whole's `00_notes.md`, `02_report_00.md`, `03_report_00.md`
  and `04_report_00.md` under
  `/Users/agile/meta/projects/kronika/01/00-ux-refresh-acceptance-and-promotion/`.

The predecessor notes are frozen historical evidence. Read them for continuity;
do not rewrite them.

Meta `/Users/agile/meta/AP_DEFECTS.md` (§0.0, D-17b, D-19, D-20, D-21) and
`/Users/agile/meta/AP_DESTILLED.md` (§17) remain citable consumer evidence of
what the predecessor whole measured. They are not rule sources: the
direct-write default, the mutation axes, the satisfiability check, consumed
coordinates and the standing maintenance duty are owned by AP at `d7023cf`.

---

## 1. Continuation Bootstrap, Stage 1 — restore and reconcile read-only

Follow `.ap/AP_ORCHESTRATOR.md` § Continuation Bootstrap. Verify, do not trust
this handout.

### 1.1 Canonical repository

```text
Repository: https://github.com/cisarik/kronika (main)
Local checkout: /Users/agile/Projects/kronika
Exact HEAD: 246c9f86b72e652cd36ed0d9f4e19e77f972df91
Public main: 246c9f86b72e652cd36ed0d9f4e19e77f972df91
Commit subject: docs: update analytic programming
Working tree: clean at the 2026-11-08 refresh
```

These values were observed at the 2026-11-08 refresh. `246c9f8` is a pin-only
commit whose parent is the predecessor's result `7ee4684`: it changes the `.ap`
gitlink and one line in `tests/contract/test_ap_integration.py`. Verify with
`git rev-parse HEAD`, `git ls-remote origin refs/heads/main`, and
`git status --short`. A different HEAD or a dirty tree is a new state; reconcile
it before selecting a whole.

### 1.2 Governing AP

```text
AP pin (superproject gitlink and .ap HEAD):
  d7023cf037f6d17885c3ede5c04812c61640da50
Governing variant: stable
```

AP public main was `d7023cf` at the refresh: `fe1e58d` (run-scoped
orchestration and direct-write report persistence, ADR-0026) and `d7023cf`
(report persistence scope and trace neutrality correction) over the former
pin `73e20ef`. Verify `git ls-tree HEAD .ap`, `git -C .ap rev-parse HEAD`, and
`./.ap/ap doctor`. Do not upgrade the pin as part of this whole unless the
COOPERATOR explicitly selects that separate task.

### 1.3 Repository gate

```text
./.ap/ap project check --root /Users/agile/Projects/kronika \
  --baseline 246c9f86b72e652cd36ed0d9f4e19e77f972df91
```

Expected: PASS. The AP run 10 pilot probe (06/01) observed PASS at this
baseline on 2026-11-08; the refresh did not rerun the gate. If public `main`
has moved, use the then-current exact SHA. Python evidence and tests go only
through the declared `./.ap/ap exec --operation test-focus` route. JavaScript tests use
`node --test`. Cursor/AppImage Workers must never invoke `.venv/bin/python`,
`python`, `python3`, or `poetry run` for evidence.

### 1.4 NUC state — last observed, NOT revalidated

The predecessor deployed the accepted release through
`deploy/ubuntu/kronika-release`. Its last observed post-deploy status:

```text
active_release: 7ee4684f529b3d2cdf15ce30902ba01a2b39992c
web_release: 7ee4684f529b3d2cdf15ce30902ba01a2b39992c
capture_release: 5b86d896b3ea03f89fef2c90f7af2c121d0ef915
layout: canonical
service_active: active
database_revision: 0035
backup_restore_readiness: ready
```

These values were **not revalidated** by the 2026-11-08 refresh; NUC contact
was not authorized. The NUC is expected to stay at `7ee4684` until a separate
routine refresh. Public `main` is now `246c9f8`, so the NUC no longer serves
current public `main`; a routine refresh to the then-current public `main`
precedes any rendered acceptance.

The runtime code is the E3-accepted `cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738`;
`7ee4684` adds documentation and tests only, and `246c9f8` changes no runtime
path (`git diff --stat cb5fa4d 246c9f8 -- src extension alembic migrations` is
empty). Re-verify with
`kronika-release status` and, before any later release, `check --release <SHA>`.
The helper needs the COOPERATOR's active global sudo timestamp. Never assume it
persists across a Worker's terminal `sudo -K`.

### 1.5 Previous whole closure

The predecessor whole `00-ux-refresh-acceptance-and-promotion` is closed:

- the UX refresh, companion YouTube save, gallery preview backfill, and ingress
  change were independently accepted at `cb5fa4d`;
- ADR-0086 and the living documentation were published at `7ee4684`;
- the NUC was refreshed to `7ee4684`;
- the COOPERATOR declared the whole closed after the NUC refresh.

Read the closure record in
`projects/kronika/01/00-ux-refresh-acceptance-and-promotion/00_notes.md`
(`Logical-whole closure: closed-by-ORCHESTRATOR`, result `7ee4684`). The AP run
10 pilot probe confirmed this closure from the frozen predecessor evidence; it
remains a Stage 1 fact for you to re-read.
Rendered acceptance is **Cooperator-declared**, not an item-by-item
Orchestrator observation. Carry these residuals forward:

- A6 info interval: a pinned-extension `open_upload` arriving before
  `applyIdentityCapabilities` could see the upload control as visible. A
  hostile page origin is rejected earlier; POST `/api/uploads` stays
  capability-checked. Info, not reproduced.
- R7: X-button clearance on a live logged-in X post remains a Cooperator
  observation, not a separate measurement.
- R9: `app.js` remains a large monolith; every UI change carries collateral
  and test-pin risk.
- R10: the verification YouTube item `jNQXAC9IVRw` remains requester-private.
  The plan recommends removal through the administrator removal workflow; the
  COOPERATOR has not decided.

Do not reopen the closed UX information architecture, the appended CSS
experience layer, the `data-icon` pattern, the companion message protocol
additions, or the backfill design without new evidence.

### 1.6 Upgrade ledger

`AGENTS.md` declares the AP upgrade ledger outside the managed block
(`Ledger path: docs/AP_UPGRADE_OBSERVATIONS.md`). Validate the declared file and
revalidate every active entry against the current repository and the governing
pin before relying on it (`.ap/AP.md#continuation-bootstrap`,
`.ap/PROMPT_CONTRACTS.md#upgrade-observation-ledger-contract`). The predecessor
closure recorded the ledger reconciliation as complete with its entry accepted /
retain-active; that disposition predates the `d7023cf` pin and is evidence to
revalidate, not a current result.

### 1.7 Handout Revalidation Record

Before the first Planner prompt, revalidate every material fact in this handout
against current evidence and record the Handout Revalidation Record
(`.ap/PROMPT_CONTRACTS.md#handout-revalidation-record`) in this whole's
`00_notes.md` (`.ap/AP.md#run-level-handouts`; Meta `README.md`,
Run Maps and Provisional Handouts). Name every material fact you could not
observe under `Not revalidated`, including the §1.4 NUC state when NUC access is
not granted.

---

## 2. Continuation Bootstrap, Stage 2 — select one bounded whole

Present the restored state and **one evidence-backed recommendation** to the
COOPERATOR. Obtain his selection before issuing the first Planner prompt. Do not
treat this handout's recommendation as selection.

### 2.1 Recommended next whole

**`timeline-and-history-media-thumbnails`**

Use the now-working gallery preview pipeline to show a media record's preview
on Timeline and History cards instead of a generic kind icon, with a graceful
kind-icon fallback.

Why this whole:

- The predecessor's `GalleryPreviewBackfillCoordinator` now fills missing
  previews in-process; the Gallery preview endpoint exists and is tested.
- `docs/UX_AUDIT.md` already lists "Show media thumbnails on Timeline and
  History cards for media records" as an unimplemented recommendation.
- It is a bounded, visible product improvement that builds directly on the
  accepted backfill work.
- It does not reopen the Gallery and Details MVP presentation, which remains
  frozen except for concrete defects.

The new whole's Planner must map the exact current rendering path before any
implementation. Do not assume the Gallery card code can be copied wholesale:
Timeline and History have different audience, privacy and data shapes.

### 2.2 Scope shape (for the Planner, not a grant)

Likely in scope:

- media records rendered in the Timeline and in personal History;
- preview presentation on those cards, using the existing server preview
  endpoint and cache;
- fallback to the existing kind icon when a preview is missing, not ready, or
  not authorized;
- audience/privacy behavior: Timeline contains only administrator-approved
  records; History is personal; private records remain visible only to their
  owner and application administrators; household rules must not widen;
- performance: lazy loading and bounded requests; no N+1 preview fetches;
- tests and the durability documentation the behavior needs;
- the routine NUC refresh and the COOPERATOR's rendered acceptance at the end.

Likely out of scope:

- Gallery or Details visual redesign (frozen);
- a new preview generation path on GET;
- a new media pipeline or provider call;
- upload-flow polish, companion notifications, onboarding, accessibility pass,
  localization, or `app.js` modularization;
- deployment beyond the routine release helper;
- internet publication.

### 2.3 Questions the Planner must answer with repository evidence

1. Where are Timeline and History cards rendered today? Which functions,
   templates, CSS classes and data fields carry the kind icon?
2. What exactly do the Timeline and History list/detail APIs return for a media
   record? Is a preview locator already available, or is a small read-side
   addition required?
3. Does the existing gallery-preview route enforce the same audience rules as
   the Timeline/History record? If not, what is the smallest correct guard?
4. What happens when a record is not a media record (question/answer,
   unfinished work, unavailable media)? The kind-icon fallback must be explicit.
5. Which existing tests pin the Timeline/History markup, CSS and copy? Which
   tests pin the preview route and its audience?
6. What is the smallest implementation that preserves the frozen Gallery and
   Details presentation?
7. What docs own the new behavior: `SPEC.md`, `SECURITY.md`, `GALLERY.md`,
   `docs/UX_AUDIT.md`, `DEVELOPMENT.md`, or a new ADR? Do not create a second
   semantic owner.
8. What is the exact NUC refresh and rendered-acceptance sequence?

### 2.4 Other candidate wholes (not selected)

These remain proposals from the predecessor handout; do not start one without
the COOPERATOR's explicit selection. Each has a provisional handout listed in
the run map `/Users/agile/meta/projects/kronika/01/00_RUN_MAP.md`:

1. Upload flow polish (automatic start after file choice, duplicate review
   preserved, companion progress visible).
2. Companion download notifications (completed X/YouTube downloads in the
   side-panel history and toolbar badge).
3. Household onboarding (first-run explainer for ordinary members; plain
   language install guide).
4. Humanized error copy (replace raw codes with actionable text; inventory
   first).
5. Accessibility pass (keyboard paths, contrast on glass buttons,
   screen-reader names; Cooperator rendered review).
6. `app.js` modularization planning (Discovery/Planner first; asset-serving and
   `vm` test strategy required).
7. Product language decision (the UI is English; localization is a Cooperator
   product decision).

---

## 3. Strategic continuity — what Kronika is

Kronika is a local-first, privacy-conscious household archive for video,
images and GIFs: archive, search, upload and download (YouTube and X), with
AI-assisted metadata, a premium Gallery, an administrator-curated Timeline,
personal History and provider-backed Search/Research. One authoritative FastAPI
server (SQLite + Alembic) runs on an Ubuntu Intel NUC reached only over
Tailscale; clients are the served web shell and a Chromium side-panel companion
extension that also injects save buttons into X and YouTube.

Authoritative product truth:

- `README.md`, `PRODUCT.md`, `SPEC.md`, `ROADMAP.md`, `SECURITY.md`, `SERVER.md`;
- `docs/adr/README.md`, ADR-0082 through ADR-0086;
- `docs/UBUNTU_NUC_DEPLOYMENT.md`, `docs/WORKER_EXECUTION_CONTRACT.md`,
  `DEVELOPMENT.md`, `GALLERY.md`.

Accepted direction to preserve:

- **ADR-0082** one Kronika in this repository; private records by verified
  owner. **ADR-0083** modular research providers; Timeline is the main page and
  contains only administrator-approved records; personal History is separate;
  Gallery is a separate working view. **ADR-0084** administrator-managed
  research settings, four exact catalog models, default
  `gpt-5.5-2026-04-23`, no network model discovery, research disabled by
  default. **ADR-0085** sole Kronika identity; bounded cuts, no mass rename.
  **ADR-0086** companion YouTube save, `open_upload`, and in-process preview
  backfill.
- **ADR-0075** the NUC is the development-and-testing machine; routine refresh
  to the exact public `main` SHA via `deploy/ubuntu/kronika-release` is normal
  operation. **ADR-0060** immutable release contract.
- Roadmap S4-D through S10 is complete. Parked rows (S3 host remainder,
  capture-mode S4, S5 ZIP, S7-C) have no authority. One grant covers one row or
  one bounded whole; the roadmap grants nothing.
- Security: loopback-first backend, Tailscale-only ingress, no port forwarding;
  Tailscale membership is not administrator authority; `/srv/media` is read-only
  to the service; ordinary clients never receive provider secrets;
  administrator read-all is application content only; household publication is
  an administrator approval; internet publication stays disabled.
- Rendered UI/UX acceptance belongs to the COOPERATOR and requires the code on
  public `main` refreshed onto the NUC first.

---

## 4. Project-specific operating rules measured in the predecessor whole

This handout grants nothing. AP precedence (RF-19) and the AP owners at the
governing pin govern every prompt. Each rule below records what the
predecessor whole measured and points to the AP owner that now holds it; if a
pointer and its owner disagree, the owner wins.

### 4.1 Reports are written by the Worker, not ferried by the COOPERATOR

The predecessor whole measured the human courier trap twice. AP `d7023cf` now
owns the remedy: the direct-write default
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
predecessor whole used manual copy-paste. The report itself is still
direct-write by the Worker; the COOPERATOR does not ferry the report file.

### 4.5 AP maintenance is part of normal work

AP is a living protocol, maintained in parallel with project work. AP §13 owns
the standing duty (`.ap/AP.md#standing-ledger-maintenance`): revalidate the
declared upgrade ledger in Stage 1 (§1.6); record newly measured friction
against AP as `untriaged` entries in `docs/AP_UPGRADE_OBSERVATIONS.md` only
under an exact write grant, otherwise as non-authorizing ledger candidates in
the closure or handoff record. A pin update remains its own explicit AP update
task (`AGENTS.md`). Meta `AP_DEFECTS.md` and `AP_DESTILLED.md` are citable
consumer evidence only, not AP rule sources or ledger discovery sources. Do not
ask the COOPERATOR to re-explain friction already recorded there or in the
ledger. The authoritative AP and the Cooperator's decision still govern any
canonical AP change.

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
- PyPI/tooling: routine updates use the packaged Poetry and CPython under
  `/opt/framenest/tooling/`; never invoke `uv` for routine updates.
- No secret, credential, token, cookie, private media filename, host-specific
  identifier, disk serial, UUID, SSH fingerprint, or private network value
  enters repository artifacts or reports.

---

## 5. Forward risk register

This register renumbers the carried predecessor residuals; the
`Predecessor ID` column states the mapping to §1.5 once.

| ID | Predecessor ID | Item | Class | Owner |
|---|---|---|---|---|
| R1 | A6 | A6 `open_upload` pre-identity interval | info residual | next acceptance record |
| R2 | R7 | X-button clearance on a live X post | evidence gap | COOPERATOR rendered acceptance |
| R3 | R9 | `app.js` monolith; UI collateral and test churn | maintainability | future planning whole |
| R4 | R10 | YouTube verification item `jNQXAC9IVRw` | data hygiene | COOPERATOR |
| R5 | new | Preview audience and performance on Timeline/History | new whole risk | Planner/audit |
| R6 | new | Gallery/Details freeze vs. new thumbnail work | product boundary | COOPERATOR |

The next whole must not widen private-record visibility to make thumbnails
convenient. Audience rules are part of the acceptance matrix, not an
implementation detail.

---

## 6. First actions for the fresh Orchestrator

1. Read `AGENTS.md`, the AP spine, `AP_ORCHESTRATOR.md`, and the named
   `PROMPT_CONTRACTS.md` sections.
2. Validate the declared upgrade ledger `docs/AP_UPGRADE_OBSERVATIONS.md` and
   revalidate every active entry at the current pin (§1.6).
3. Verify the repository gate, AP pin, `ap doctor`, `ap project check`, public
   `main`, and the NUC status through the canonical helper when NUC access is
   granted; otherwise carry the NUC state as not revalidated.
4. Read the predecessor whole's closure notes and reports, and the run map.
5. Revalidate this handout's material facts and prepare its Handout
   Revalidation Record (§1.7).
6. Present the restored state and the recommended whole
   `timeline-and-history-media-thumbnails` to the COOPERATOR in his presentation
   profile. Ask one decision: select this whole or another.
7. Only after selection, create this whole's `00_notes.md`, record the Handout
   Revalidation Record there, ask once for the delivery route, and issue the
   first Planner prompt for session `01`, exchange `01`, with `Native planning
   mode: required` and `Report persistence owner: assigned WORKER` under the
   direct-write default.
8. Freeze `00_notes.md` only at closure.

The next whole's Meta directory is:

```text
/Users/agile/meta/projects/kronika/01/01-timeline-and-history-media-thumbnails/
```

---

## 7. Readiness review of this handout

| Review | Result |
|---|---|
| Contradiction | No contradiction found between this handout and the predecessor closure record or the repository and public state observed at the 2026-11-08 refresh |
| Omission | The next whole is a recommendation, not a selected objective; the COOPERATOR must select it |
| Stale state | Repository, public `main` and AP pin were observed at the 2026-11-08 refresh; the NUC state is last observed and not revalidated; re-verify all |
| Authority | No mutation authority transferred; every next action needs a new grant |
| Active mutation | None |
| Active Worker | None for this whole |
| Security boundary | Closed UX/ingress/backfill boundaries stay closed; the new whole must not widen them |
| Strategic direction | ADR-0082 through ADR-0086 and the roadmap state preserved |
| Next-step executability | Executable after Stage 1 verification, the Handout Revalidation Record and the COOPERATOR's whole selection |

Overall: **PARTIAL** — the predecessor whole is closed and the recommended whole
is bounded and evidence-backed, but the whole has not opened: the NUC state is
not revalidated, and the per-whole Orchestrator must revalidate this handout in
Stage 1 before the first Planner prompt.

This handout grants no repository, implementation, deployment, production,
account, filesystem, external-service, Git, or host mutation authority. Verify
independently, then ask Michal one decision.
