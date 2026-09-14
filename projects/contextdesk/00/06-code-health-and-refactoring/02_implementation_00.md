Logical whole identity: code-health-and-refactoring
Worker session ordinal: 02
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: CONTEXTDECK-CODE-HEALTH-REFACTORING-S3-S5
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to a genuinely fresh Worker session
Reasoning recommendation: High
Reasoning basis: this is the largest and riskiest slice of the whole — decomposing
a 2285-line `AppController` behind a stable QML facade while preserving 48
`Q_PROPERTY`, 52 `Q_INVOKABLE`, every signal, user-visible string, and log
event; a missed binding or a wrong delegation is subtle and user-visible. High
is justified by that named risk; not Extra High because the accepted plan fixes
the decomposition design.
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: cross-cutting reversible source refactoring under one
cumulative fresh independent acceptance later in this logical whole; this
exchange changes no behavior, QML, schema, IPC, or broker path, and the
lighting test plus the full registered suite are the behavior gate, with two
normal non-force product commits and pushes.
Internal delegation: prohibited

# ContextDeck — implement S3 and S5: decompose AppController behind a stable facade

You are a genuinely fresh WORKER assigned one bounded implementation task. You
did not participate in the planning or in any earlier slice of this logical
whole, and you inherit no authority from any previous session. Establish
repository and environment evidence independently before acting. Native Plan
Mode must be OFF. Do not use subagents.

This prompt grants one bounded repository-only implementation task with two
coherent commits: first S3 (decompose `AppController` behind a stable QML
facade), then S5 (remove the unused `remappingState` placeholder). Validate
each commit against the exact baseline, push both normally, persist one
terminal report in META, then stop. You do not accept your own candidate and
never close the logical whole.

Critical: no live host mutation, no application launch, no KWin/OpenRGB/broker/
device operation, no desktop mutation, no service change, no packaging change,
no dependency change, and no suspend/DPMS behavior may occur during this
exchange. This exchange edits, tests, commits, and pushes repository content
only; `build/` is git-ignored.

Client note (not a product issue): if distro `cmake` fails with a `CMAKE_ROOT`
lookup error because the client injects bundled library paths, run the granted
`cmake`/`ctest` commands with a cleaned distro `PATH`. Do not record host-local
paths anywhere.

## Accepted plan and Plan-to-Execution transition

ORCHESTRATOR reconciliation: accepted
Accepted plan: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_01.md`
Accepted correction: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_02.md`
(the corrected S4 extraction target; S4 is already implemented and out of this
slice)

Prior slices S1, S2, S4, and S6 are reconciled and accepted as
implementation-PASS: public `main` = `a130b06ec8641269c80bd755c0e5f6ee9c3dc048`
with parents `1e7e9d5...` and `308aaa2...` and `5b2b25b...`. This prompt is the
separate implementation grant for S3+S5; the plan and reports supply no
execution authority by themselves.

## Implementation Authority Record

Implementation authority: explicit
Exact baseline: `a130b06ec8641269c80bd755c0e5f6ee9c3dc048`
Changed-path allowlist: `src/app/AppController.{h,cpp}`;
`src/app/LightingEdit.{h,cpp}` (new);
`src/app/ProfileDocumentEditor.{h,cpp}` (new);
`src/app/WorkspaceSessionEditor.{h,cpp}` (new);
`src/app/WorkspaceApplyController.{h,cpp}` (new);
`src/app/PresentationModel.{h,cpp}` (new);
`CMakeLists.txt`; `tests/unit/test_workspace_lighting.cpp` only if an include
change is required
Implementation boundaries: two coherent commits (S3, then S5); no behavior,
string, signal, property-name, QML, IPC, schema, broker, or settings-host
change; `ui/*` is outside the allowlist and must remain byte-identical
Independence required: no for this implementation slice; the cumulative fresh
independent acceptance for the whole is a later separate exchange

## Verified candidate and preflight gates

Canonical product repository: `https://github.com/cisarik/contextdesk`
Expected branch: `main`
Exact baseline HEAD: `a130b06ec8641269c80bd755c0e5f6ee9c3dc048`
Required parent: `1e7e9d55c1743121411d825be18dc1bfd24e217b`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

This whole's trace destination:
`projects/contextdesk/00/06-code-health-and-refactoring/`
Accepted plan report: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_01.md`
Accepted revision report: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_02.md`
Report destination: `projects/contextdesk/00/06-code-health-and-refactoring/02_report_00.md`

Repository checkout topology: standalone product checkout on `main`
Working-copy topology: canonical product checkout
Topology rationale: one accountable Worker owns one coherent decomposition and
two commits; `build/` is git-ignored

Execution route: this repository declares no `ap.project.conf` operation; the
exact `cmake` / `ctest` commands below are the project-owned build and test
commands from `AGENTS.md` and `CMakeLists.txt`.

Before any mutation:

1. Verify the complete prompt, the intended fresh Worker session, Native Plan
   Mode OFF, coordinates `02/01`, and no subagents.
2. Verify canonical remote, active `main`, exact HEAD, exact parent, clean
   state, no Git lock, matching AP gitlink/checkout, and `./.ap/ap doctor` PASS
   (variant `stable`).
3. Prove public product `main` equals the exact baseline with direct
   `git ls-remote`. Do not pull, merge, rebase, switch, reset, clean, stash, or
   retarget.
4. Verify META public `main` is
   `9d7a994fa98e96ac270b86795b4bce8bf37bc813` or a verified later descendant
   whose changed paths do not contradict this exchange.
5. Verify the trace directory is real and contains `00_handout.md`,
   `00_notes.md`, `01_planning_00.md`, `01_completion_01.md`,
   `01_planning_02.md`, and the `01_report_01.md` through
   `01_report_05.md` reports; the report destination `02_report_00.md` must be
   absent before the write.
6. Read the accepted plan report S3/S5 sections and the revision report
   completely; read `src/app/AppController.{h,cpp}`, `src/app/SettingsHost.cpp`,
   `src/app/TrayController.cpp`, `src/app/SessionApplication.cpp`, the QML files
   for the binding inventory, `tests/unit/test_workspace_lighting.cpp`, and
   `CMakeLists.txt` before editing; every needed path must be inside the
   allowlist.

## S3 scope (from the accepted plan, exact)

Measured at the baseline: `AppController.h` is 277 lines with 48 `Q_PROPERTY`
and 52 `Q_INVOKABLE`; `AppController.cpp` is 2285 lines; `SettingsHost` exposes
exactly one context property `"app"`; 83 unique `app.*` bindings exist across
9 QML files; `test_workspace_lighting` currently compiles
`src/app/AppController.cpp` and `src/app/BrokerIpcClient.cpp` directly.

Create these cohesive units under `src/app/` and move implementation into
them:

- `LightingEdit` — today's anonymous namespace: applyMode/zone/gradient/
  sanitize/hex/speed/breathing plus `parseHex`/`toHex`;
- `ProfileDocumentEditor` — global/app lighting, add/remove profile,
  `assignEmitShortcut`, save via `ProfileStore`;
- `WorkspaceSessionEditor` — session CRUD plus the application workspace and
  title-fallback setters;
- `WorkspaceApplyController` — fingerprint, apply/revert, launch-on-created,
  apply-status fields, `m_mutator`/`m_launcher`;
- `PresentationModel` — hero/status/diagnostics/inventory/profiles/controls/
  workspaceObserved/plan queries.

`AppController` remains the sole QML type and the test-facing facade: getters
and invokables delegate; all signals and property names remain except
`remappingState`; `SettingsHost` stays unchanged with its single `app` context
property; no new QML context property is introduced.

CMake for S3:

- new static library `contextdeck_app` containing `AppController.cpp` and the
  five new units; it must not contain `BrokerIpcClient`, `TrayController`,
  `SettingsHost`, `ChordRecorder`, or `main`;
- the `contextdeck` executable and the `test_workspace_lighting` target link
  `contextdeck_app`; remove `src/app/AppController.cpp` from their direct
  sources while keeping `src/app/BrokerIpcClient.cpp` where it is today;
- `qt_add_qml_module` stays on the executable (ChordRecorder);
- global `CMAKE_AUTOMOC ON` covers the new library.

Invariants (must hold exactly):

- every `app.*` binding in `ui/*.qml` keeps its name and behavior, except the
  one removal in S5 (`remappingState`, which no QML file references);
- `ui/*.qml` files are byte-identical before and after this exchange;
- user-visible strings unchanged, including the Slovak phrases in
  `openRgbPhrase`, `lightsPhrase`, and `contextDisplayName`;
- log events unchanged, including `loaded profile document`, `cold start: ...`,
  `profile load refused`, `save refused`, and `temporary_color expired on
  external identity change`;
- all existing signals, property types, and invokable signatures unchanged;
- keep every member and property that is not `remappingState`, including the
  QML-unbound ones the accepted plan marked for the later UI/UX whole
  (`currentApplication`, `lightingMode`, `globalColor`, `isValidHex`) and the
  Tray/diagnostics members (`currentProfile`, `lightingConnection`,
  `contextDisplayName`, `lastError`, `bridgeConnected`, `degraded`,
  `isSelfWindow`, `lastExternalApplication`);
- `test_workspace_lighting` keeps equivalent behavioral coverage through the
  unchanged `AppController` public API;
- no new unit test of the extracted classes (the facade is the contract);
- no dependency, QML, IPC, schema, broker, packaging, or documentation change.

## S5 scope (second commit, same exchange)

Remove `Q_PROPERTY(QString remappingState READ remappingState CONSTANT)` and
its inline getter returning `QStringLiteral("inactive-until-M2")`. No QML or
C++ consumer exists. Do not wire or replace it — wiring would be a claim about
remapping state, i.e. a behavior/product change.

## Mandatory reading

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-12, RF-16, RF-18, RF-19,
  implementation authority, Git safety, validation, stopping conditions;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Implementation Authority
  Record, exchange/trace contract, validation ladder, delivery record,
  Session-and-Mode;
- the accepted plan report `01_report_01.md`, especially S3 and S5;
- the accepted revision report `01_report_02.md` (reference);
- `src/app/AppController.{h,cpp}`, `src/app/SettingsHost.cpp`,
  `src/app/TrayController.cpp`, `src/app/SessionApplication.cpp`,
  `src/app/main.cpp`;
- `tests/unit/test_workspace_lighting.cpp`;
- all `ui/*.qml` files for the binding inventory;
- `CMakeLists.txt`;
- `AGENTS.md`.

## Product invariants

- G213 only; five RGB zones, never per-key.
- Session app never opens raw keyboard nodes; broker stays static/inactive and
  no ARM/LEASE/grab/device probe occurs.
- Event-driven KWin identity; no title polling; no `xdotool`/`wmctrl`/`xprop`.
- Typed action/launch model only; no shell strings.
- Behavior preservation is the slice claim: no user-visible string, signal,
  property, QML binding, IPC/wire format, persisted schema, or log event
  changes.
- Repository documentation stays English, public-facing, and unchanged here.

## Commands and side-effect authority

Allowed: `git status`, `git log`, `git diff`, `git ls-remote`, `git rev-parse`,
`git show`, `grep`/`rg` for the binding inventory; `cmake -S . -B build -G
Ninja`; `cmake --build build`; `ctest --test-dir build --output-on-failure`;
exact-path `git add`, two `git commit`s, two normal non-force `git push`es, and
bounded public readback.

Forbidden: any `git add .`/`-A`, force push, history rewrite, reset, clean,
stash, checkout, switch, rebase, merge, tag, branch, remote, or config write;
any other source, test, UI, documentation, packaging, or dependency edit; any
service, host, desktop, device, broker, OpenRGB, KWin, or input-remapper
operation.

Side effects: reversible local source edits inside the allowlist, build outputs
under the git-ignored `build/`, two local product commits, and two normal
non-force product pushes. No META Git mutation by the Worker.

No raw input, key names, serials, host addresses, passwords, private paths,
desktop names/IDs, window captions, or unredacted tool logs may appear in the
report or trace.

## Validation ladder

Validation ladder: selected
Inspection and provenance: required — capture the baseline `grep -ho
"app\.[A-Za-z_][A-Za-z0-9_]*" ui/*.qml | sort -u` inventory (83 unique names),
the `ui/*.qml` checksums, and the `AppController` public surface before editing
Existing focused tests: `test_workspace_lighting` is the focused facade test
Affected tests: `test_workspace_lighting` plus every target linking the
controller (the `contextdeck` executable builds the full QML module)
New causal regression: none — the facade public API and behavior are unchanged
and a new unit test of internal classes would freeze internal structure
(accepted plan decision)
Broad or full suite: required-because behavior preservation of the whole
logical whole is the named decision risk; run the full registered suite after
each commit
Runtime or testbed: not-used
Independent acceptance: not-required for this slice; the whole receives one
cumulative fresh independent acceptance after later slices

Procedure per commit:

1. Confirm the starting green state: build, `test_workspace_lighting`, full
   suite.
2. Apply only the allowlisted edits for that commit.
3. Reconfigure and rebuild (this compiles the QML module); run
   `test_workspace_lighting`, then the full suite and require 21/21.
4. Re-run the binding inventory and checksum checks: the unique `app.*` name
   set equals the baseline except the S5 removal, and every `ui/*.qml` file is
   byte-identical.
5. Inspect the diff: only allowlisted paths for that commit.

A failed gate stops that commit before commit/push. Classify a failure before
any repair; do not rerun an unchanged broad gate; do not weaken the environment.

## Git and public verification

Commit 1 (S3):

1. Stage exactly the S3 paths; inspect the staged diff.
2. Create exactly one normal commit with subject:
   `Decompose AppController behind a stable QML facade`
3. Before push, prove public `main` still equals the exact baseline with
   direct `git ls-remote`; on any mismatch, stop without pushing.
4. Push once, normal non-force, to `origin main`; verify local `HEAD`,
   remote-tracking state, and direct public `ls-remote` all equal the new
   commit; parent equals the exact baseline; changed paths are exactly the S3
   allowlist and `ui/*` is untouched.

Commit 2 (S5):

5. Stage exactly the S5 paths; inspect the staged diff.
6. Create exactly one normal commit with subject:
   `Remove unused remappingState placeholder`
7. Before push, prove public `main` equals commit 1 with direct
   `git ls-remote`; then push once, normal non-force; verify local `HEAD`,
   remote-tracking state, and direct public `ls-remote` all equal commit 2;
   parent equals commit 1; changed paths are exactly `src/app/AppController.h`
   and any S5-only counterpart.

If the first commit and push are green but the second fails, stop with
`PARTIAL`, name the exact state, and leave commit 1 pushed and verified. Never
force or bypass.

## Trace persistence contract

External trace disposition: configured
Trace discovery: META README and the exact destination below
Trace project key: contextdesk
Trace logical-whole projection identity: 06-code-health-and-refactoring
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_implementation_00.md
Destination path: projects/contextdesk/00/06-code-health-and-refactoring/
Report filename: 02_report_00.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR for META; WORKER for the two product commits
Archival: wait-for-report

Before substantive work, verify the prepared prompt file exists and is
byte-identical to the received prompt; read it back completely. Stop on a
non-identical or unsafe collision.

After implementation, write the complete terminal report first to the exact
report path, read it back completely, and verify the header, coordinates,
content, and filename. Do not overwrite a non-identical existing report. Do not
stage, commit, push, pull, merge, rebase, or otherwise mutate META Git history
or refs. The COOPERATOR archives the prompt/report pairs after the reports
exist. If the exact META destination is not reachable from your environment, do
not write to any other path; state the exact limitation in the report body and
return the complete report through the client output so the COOPERATOR can
persist it exactly.

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

It must echo the four opening identity fields (persistent role and the three
coordinates) exactly once, with their values unchanged.

Include:

- status: `PASS`, `PARTIAL`, or `BLOCKED`;
- phase-qualified result: `implementation-PASS` or `not-applicable`;
- start and end product commit (baseline, commit 1, and commit 2);
- changed files and purpose for both commits, listing the new units and what
  each now owns;
- tests and validation, including the baseline and candidate binding
  inventories, the `ui/*.qml` byte-identity check, `test_workspace_lighting`,
  and the full-suite result after each commit;
- commit and push results plus direct public-ref verification for both commits;
- deviations, risks, or missing evidence;
- an explicit statement that no observable behavior, string, signal, property,
  QML binding, or visual changed, with the evidence that establishes it;
- exactly one smallest next step: ORCHESTRATOR reconciliation and, if accepted,
  the next bounded implementation exchange;
- exactly one `Report justification: new-mutation`;
- `Resolved Execution Issues / Near-Misses: none` or a complete entry;
- `Pre-Existing Failure Classification: none` or a complete entry;
- compact critique:

  `Orchestration critique:`

  `MEASURED: none | <verified finding; evidence; effect; smallest correction>`

  `LEAD: none | <unverified possibility; cheapest useful check>`

- exactly one `Logical-whole closure: not-closed` line;
- the authority-expiry sentence below.

Explicit non-claims: no acceptance-PASS, publication-PASS beyond the two pushed
commits, deployment-PASS, production readiness, M2/G4/G3 closure, autostart,
hibernate/hybrid sleep, input-remapper coexistence, M3/M4 closure or physical
behavior, M5, remapping, deck layer, per-key RGB, license selection, or
hardware acceptance; no claim that the cumulative behavior-preservation
acceptance has happened; no claim that refactoring beyond these slices is
complete; no claim that the META trace privacy correction has been performed
(that is a COOPERATOR decision and action).

## Stop conditions

Stop and report `BLOCKED` before mutation if: the session is not genuinely
fresh, Native Plan Mode is on, coordinates or authority are contradictory,
product/AP/META identity fails, the worktree has unexplained changes, the trace
path collides or is unsafe, the accepted plan is unreadable, or the task would
need a non-allowlisted path, a dependency change, private data, host/device
access, or subagents.

Stop with `PARTIAL` without committing the affected commit when a member cannot
be moved behind the facade without changing a name, a signature, a string, a
log event, or a QML-visible behavior, and name the exact obstacle. Do not widen
the allowlist and do not touch `ui/*`.

Stop with `PASS` only when both commits are pushed and publicly verified, the
focused test and the full suite pass after each commit, the binding inventory
and `ui/*` checks are clean, and the terminal report is persisted and read
back. Then submit the terminal report and do no further work under this grant.

Authority for this Worker expires at this terminal report.
