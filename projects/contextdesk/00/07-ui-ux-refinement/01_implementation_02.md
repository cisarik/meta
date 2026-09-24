Logical whole identity: ui-ux-refinement
Worker session ordinal: 01
Worker exchange ordinal: 03
Persistent role identity: WORKER
Worker session target: current-worker-session
Worker session profile: Implementation Worker
Phase: implementation
Task identity: CONTEXTDECK-UI-UX-REFINEMENT-S1-S2-S9
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to the exact current Worker session
Continuity anchor: terminal report `01_report_01.md` for Worker exchange `02`
(the rendered, accepted plan for this whole) and the exchange-01 planning
content — all produced in this same session
Authority renewal: prior report-rendering authority expired at the exchange-02
terminal report; this prompt is a complete renewed implementation grant to the
same session
Reasoning recommendation: Medium
Reasoning basis: bounded mechanical execution of an accepted decision-complete
plan (an exact-text documentation reconciliation, one QML shell navigation
change, and one tray signal connection) with the full registered suite and a
binding-set invariant as gates; no open design question and no live host
mutation.
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: cross-cutting but reversible documentation and
presentation work with no production, durable-data, security-boundary, broker,
packaging, dependency, or license mutation; one normal non-force product push
per slice commit; the cumulative fresh independent acceptance for the whole is
a later separate exchange.
Internal delegation: prohibited

# ContextDeck — implement S1, S2, and S9 of the accepted UI/UX plan

You are the WORKER session that produced the accepted plan. Native Plan Mode
must be OFF for this exchange. Do not use subagents.

This prompt grants one bounded repository-only implementation exchange covering
three accepted slices in order: S1 (documentation reconciliation), S2 (shell
navigation), S9 (tray presentation). Apply the accepted plan exactly, validate
each slice, create and push one normal product commit per slice, persist the
terminal report in META, then stop. You do not accept your own candidate and
never close the logical whole.

Continuity and renewal: prior report-rendering authority expired at the
exchange-02 terminal report. Retained context, the plan text, and this
conversation are convenience and evidence, not authority; re-verify repository
and environment state before acting and stop on any conflict with current
repository evidence. Evidence produced in this session is non-independent.

Critical: no live host mutation, no application launch, no KWin/OpenRGB/broker/
device operation, no desktop mutation, no service change, no packaging change,
no dependency change, and no suspend/DPMS behavior may occur during this
exchange. This exchange edits, tests, commits, and pushes repository content
only; `build/` is git-ignored.

## Accepted plan and Plan-to-Execution transition

ORCHESTRATOR reconciliation: accepted
Accepted plan:
`projects/contextdesk/00/07-ui-ux-refinement/01_report_01.md` (the rendered
frozen plan; no revision was issued)

The planning budget is exhausted. This prompt is the separate complete
implementation grant; the accepted plan supplies no execution authority by
itself.

Two reconciliation precisions are recorded by the ORCHESTRATOR and are part of
this grant's exact scope:

1. `AGENTS.md:129-130` also contains the stale phrase `in this ChatOrchestrator
   workflow` in the trace-policy bullet. The accepted S1 validation requires
   zero `ChatOrchestrator` matches across the three documentation files, so S1
   includes this line: replace `in this` + newline + two spaces +
   `ChatOrchestrator workflow.` with `in this` + newline + two spaces +
   `Orchestrator workflow.` Keep the surrounding sentence byte-identical.
2. The `README.md` status-block replacement applies to the anchor text only.
   The existing continuation on the same line — ` **Full G4 remains open**: the
   named live slices` and the following G4 sentences — must remain immediately
   after the new block's last line (`> license change.`), unchanged in wording
   and order. The replacement must not delete, reorder, or reword the G4 text.

## Implementation Authority Record

Implementation authority: explicit
Exact baseline: `ba87ba08c17ad965d008c4fc1d59f42a7c7700c9`
Changed-path allowlist: `AGENTS.md`; `ROADMAP.md`; `README.md`;
`ui/Main.qml`; `src/app/TrayController.cpp`
Per-slice allowlists: S1 = `AGENTS.md`, `ROADMAP.md`, `README.md`; S2 =
`ui/Main.qml`; S9 = `src/app/TrayController.cpp`
Implementation boundaries: apply the accepted S1 exact-text edits, the accepted
S2 shell change, and the accepted S9 tray signal connection; no other content,
no behavior, no binding, no string, no schema, no IPC, no broker, no packaging,
no dependency, and no license change
Independence required: no for this implementation exchange; the cumulative
fresh independent acceptance for the whole is a later separate exchange

## Verified candidate and preflight gates

Canonical product repository: `https://github.com/cisarik/contextdesk`
Expected branch: `main`
Exact baseline HEAD: `ba87ba08c17ad965d008c4fc1d59f42a7c7700c9`
Required parent: `58a10bb71d697a48b5a94e63e5a8c0f9eacc4a9b`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

This whole's trace destination:
`projects/contextdesk/00/07-ui-ux-refinement/`
Accepted plan report:
`projects/contextdesk/00/07-ui-ux-refinement/01_report_01.md`
Report destination:
`projects/contextdesk/00/07-ui-ux-refinement/01_report_02.md`

Repository checkout topology: standalone product checkout on `main`
Working-copy topology: canonical product checkout
Topology rationale: one accountable Worker owns one coherent three-slice
exchange with one commit per slice; `build/` is git-ignored

Execution route: this repository declares no `ap.project.conf` operation; the
exact `cmake` / `ctest` commands below are the project-owned build and test
commands from `AGENTS.md` and `CMakeLists.txt`.

Before any mutation:

1. Verify the complete prompt, the exact current Worker session, Native Plan
   Mode OFF, coordinates `01/03`, the renewed authority, and no subagents.
2. Verify canonical remote, active `main`, exact HEAD, exact parent, clean
   state, no Git lock, matching AP gitlink/checkout, and `./.ap/ap doctor` PASS
   (variant `stable`).
3. Prove public product `main` equals the exact baseline with direct
   `git ls-remote`. Do not pull, merge, rebase, switch, reset, clean, stash, or
   retarget.
4. Verify META public `main` is `a2c11ad...` or a verified later descendant
   whose changed paths do not contradict this exchange.
5. Verify the trace directory is real and contains `00_handout.md`,
   `00_notes.md`, `01_planning_00.md`, `01_completion_01.md`, `01_report_00.md`,
   and `01_report_01.md`; the report destination `01_report_02.md` must be
   absent before the write. Do not read or copy `01_report_00.md`: it is the
   retired frozen artifact and contains non-public local paths.
6. Read the accepted plan report `01_report_01.md` completely; confirm the
   S1, S2, and S9 sections match this prompt's scope, including the two
   reconciliation precisions above.
7. Read `AGENTS.md`, `ROADMAP.md`, `README.md`, `ui/Main.qml`, and
   `src/app/TrayController.{h,cpp}` before editing; every needed path must be
   inside the allowlist.

## S1 scope (accepted plan section 8, exact)

Changed-path allowlist: `AGENTS.md`, `ROADMAP.md`, `README.md`.

- `AGENTS.md` access-profile bullet — replace the whole bullet:
  old:
  `- Access profile: **ChatOrchestrator** (mediated through the COOPERATOR; an inspection clone is not the COOPERATOR’s uncommitted worktree). Selected delivery for this project remains **manual** across subsequent exchanges. Dispatch availability in a client does not change that selection.`
  new:
  `- Access profile: **Orchestrator** (full project orchestration when the session environment exposes those capabilities; an inspection clone is not the COOPERATOR’s uncommitted worktree). Selected delivery for this project remains **manual** across subsequent exchanges. Dispatch availability in a client does not change that selection.`
- `AGENTS.md` hard-rule bullet — replace:
  old:
  `- This project’s access profile is **ChatOrchestrator** with **manual** delivery preserved: the COOPERATOR carries every prompt and report.`
  new:
  `- This project’s access profile is **Orchestrator** with **manual** delivery preserved: the COOPERATOR carries every prompt and report.`
- `AGENTS.md` trace-policy bullet — the precision above: `in this
  ChatOrchestrator workflow.` becomes `in this
  Orchestrator workflow.` with the surrounding sentence unchanged.
- `ROADMAP.md:7` — change `profile: ChatOrchestrator; delivery remains manual.`
  to `profile: Orchestrator; delivery remains manual.`
- `ROADMAP.md` current-whole bullet — replace the `code health and refactoring`
  current-whole bullet with these two bullets:
  `- Closed whole: **code health and refactoring** — behavior-preserving internal structure on the session app, core, receivers, and tests; closed by the ORCHESTRATOR (acceptance-PASS on `ba87ba08...`; publication-PASS; QML runtime validation parked). No behavior, visuals, product-claim, or safety-boundary change. No host, device, desktop, launch, broker, packaging, or license mutation.`
  `- Current whole: **ui-ux-refinement** — presentation-only refinement of the session application's six sections, shared scaffold, flows and states, accessibility, and tray presentation, plus one bounded COOPERATOR-executed runtime QML validation and a small forward documentation reconciliation. No product-semantics, behavior, persistence, IPC, broker, packaging, launch, or license change; physical testing and G6 licensing remain deferred.`
- `README.md` status block — replace the anchor text
  `> state and ledger reconciliation is closed on `235d467...`. The current bounded` + newline + `> whole is behavior-preserving code health and refactoring.`
  with:
  `> state and ledger reconciliation is closed on `235d467...`. The code health`
  `> and refactoring whole is closed on `ba87ba08...` (acceptance-PASS;`
  `> publication-PASS; QML runtime validation parked). The current bounded whole is`
  `> **ui-ux-refinement**: presentation-only refinement of the session`
  `> application's six sections, tray, accessibility, and one bounded`
  `> COOPERATOR-executed runtime QML validation; no behavior, broker, packaging, or`
  `> license change.`
  and preserve the existing G4 continuation exactly as stated in precision 2.

S1 focused validation: read back every changed line; `rg -n
"ChatOrchestrator" AGENTS.md ROADMAP.md README.md` must return no match; `rg -n
"G6|license" README.md ROADMAP.md` must show the licensing statements unchanged
(G6 stays deferred); no code path touched; full registered suite green.

## S2 scope (accepted plan section 3, exact)

Changed-path allowlist: `ui/Main.qml`.

- Put the six `Kirigami.Action` drawer entries in an exclusive action group so
  exactly one is checked at a time.
- Keep `currentSection`, section identifiers, page URLs, icon names, window
  sizes, `showSection()`, and `pageStack.replace()` semantics unchanged.
- No user-visible string change.

S2 focused validation: build (QML compiles through `qt_add_qml_module`) and the
full registered suite; the `app.*` binding set in `ui/` is unchanged (83 unique
names before and after).

## S9 scope (accepted plan section 3, exact)

Changed-path allowlist: `src/app/TrayController.cpp` (touch
`src/app/TrayController.h` only if strictly unavoidable; if it is, state the
reason).

- Add the `presentationChanged` connection so the tray tooltip and menu track
  `statusSummary` and `contextDisplayName` changes:
  `connect(m_controller, &AppController::presentationChanged, this, &TrayController::rebuildMenu);`
- Keep every menu label, menu order, checkability, `showSettingsRequested`, and
  confirmation behavior byte-identical. No string change.

S9 focused validation: build and the full registered suite.

## Mandatory reading

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-12, RF-16, RF-18, RF-19,
  implementation authority, Git safety, validation, stopping conditions;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Implementation Authority
  Record, exchange/trace contract, validation ladder, delivery record,
  Session-and-Mode;
- the accepted plan report `01_report_01.md`, especially sections 3, 4, 7, 8,
  and the S1/S2/S9 scopes and the acceptance control matrix;
- `AGENTS.md` including the managed AP block;
- `README.md`, `ROADMAP.md`;
- `ui/Main.qml`, `src/app/TrayController.{h,cpp}`, `src/app/AppController.h`;
- `CMakeLists.txt` and `cmake/contextdeck-tests.cmake` for the registered test
  names.

## Product invariants

- G213 only; five RGB zones, never per-key RGB.
- Session app never opens raw keyboard nodes; broker stays static/inactive and
  no ARM/LEASE/grab/device probe occurs.
- All 83 `app.*` binding names remain unchanged; no QML behavior, property,
  signal, or user-visible string changes in this exchange.
- The five-zone, event-driven-KWin, typed-action, no-autostart, and
  one-OpenRGB-connection invariants stay untouched.
- Repository documentation stays English; the only documentation changes are
  the S1 exact-text edits.
- No license text and no G6 statement changes; G6 stays open and deferred.

## Commands and side-effect authority

Allowed: `git status`, `git log`, `git diff`, `git ls-remote`, `git rev-parse`,
`git show`; `cmake -S . -B build -G Ninja`; `cmake --build build`;
`ctest --test-dir build --output-on-failure`; `ctest -N`; `rg`/`grep` source
searches; exact-path `git add`, one `git commit` per slice (three total), one
normal non-force `git push` per slice commit, and bounded public readback.

Forbidden: any `git add .`/`-A`, force push, history rewrite, reset, clean,
stash, checkout, switch, rebase, merge, tag, branch, remote, or config write;
any non-allowlisted path; any dependency, packaging, service, host, desktop,
device, broker, OpenRGB, KWin, or input-remapper operation; any application
launch.

Side effects: reversible local edits inside the per-slice allowlists, build
outputs under the git-ignored `build/`, three local product commits, and three
normal non-force product pushes. No META Git mutation by the Worker.

No raw input, key names, serials, host addresses, passwords, private paths,
desktop names or IDs, window captions, or unredacted tool logs may appear in the
report or trace.

## Validation ladder

Validation ladder: selected
Inspection and provenance: required — read every file before editing and
capture the baseline `app.*` binding set from `ui/` before the first edit
Existing focused tests: none exist for QML presentation or the tray; the 21
registered CTest names are the suite evidence
Affected tests: all 21 (full suite after each slice commit)
New causal regression: none — no slice changes a semantic validator, structural
field, wire/IPC format, persistence, or the `app` facade; the QML surface has
no registered test target, and adding one would require a `CMakeLists.txt`
change outside the allowlist
Broad or full suite: required-because binding and behavior preservation across
presentation changes is the named decision risk; run the full registered suite
after each slice
Runtime or testbed: not-used in this exchange; the one bounded
COOPERATOR-executed runtime QML validation is planned after the final
cumulative candidate
Independent acceptance: not-required for this exchange; the whole receives one
cumulative fresh independent acceptance after the later slices

Procedure:

1. Capture baseline evidence before edits: the sorted unique `app.*` name set
   from `ui/*.qml`; the sorted set of string literals in the five allowlisted
   files as needed for the drift check; and a clean `git status`.
2. Apply S1 only; validate; commit; push; verify.
3. Apply S2 only; validate; commit; push; verify.
4. Apply S9 only; validate; commit; push; verify.
5. Inspect each commit's changed paths against its per-slice allowlist.

A failed gate stops the exchange before the affected commit. Classify a failure
before any repair; do not rerun an unchanged broad gate; do not weaken the
environment. If S2 or S9 cannot be done without changing a binding, a string, or
behavior, stop with `PARTIAL` and name the exact obstacle; do not widen the
allowlist.

## Git and public verification

For each slice, after a green suite:

1. Stage exactly that slice's allowlisted paths; inspect the staged diff.
2. Create exactly one normal commit with the exact subject:
   - S1: `docs: reconcile current-whole state and access-profile wording`
   - S2: `ui: establish consistent shell scaffold and drawer navigation`
   - S9: `tray: track presentation changes for tooltip/menu`
3. Before each push, prove public `main` still equals the previous local commit
   with direct `git ls-remote`; on any mismatch, stop without pushing.
4. Push once, normal non-force, to `origin main`.
5. Verify local `HEAD`, remote-tracking state, and direct public `ls-remote` all
   equal the new commit; the parent equals the previous commit; changed paths
   are exactly that slice's allowlist.

If commit or push is unavailable or fails, report `PARTIAL` with the exact
state; never force or bypass.

## Trace persistence contract

External trace disposition: configured
Trace discovery: META README and the exact destination below
Trace project key: contextdesk
Trace logical-whole projection identity: 07-ui-ux-refinement
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_implementation_02.md
Destination path: projects/contextdesk/00/07-ui-ux-refinement/
Report filename: 01_report_02.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR for META; WORKER for the three product commits
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
- start and end product commit (baseline and the final commit, plus each
  intermediate commit);
- changed files and purpose per slice;
- tests and validation, including the full-suite result per slice and the
  baseline-vs-candidate `app.*` binding-set comparison;
- commit and push result per slice plus direct public-ref verification;
- the documentation read-back evidence for S1, including the zero
  `ChatOrchestrator` matches and the preserved G4 text;
- deviations, risks, or missing evidence;
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

Explicit non-claims: no acceptance-PASS, publication-PASS beyond the three
pushed commits, deployment-PASS, production readiness, M2/G4/G3 closure,
autostart, hibernate/hybrid sleep, input-remapper coexistence, M3/M4 closure or
physical behavior, M5, remapping, deck layer, per-key RGB, license selection, or
hardware acceptance; no claim that any UI/UX or QML runtime behavior was
exercised; no claim that the application was launched; no claim that the
cumulative behavior-preservation acceptance has happened; no claim that later
slices are complete.

## Stop conditions

Stop and report `BLOCKED` before mutation if: the session is not the healthy
continuation session, Native Plan Mode is on, coordinates or authority are
contradictory, product/AP/META identity fails, the worktree has unexplained
changes, the trace path collides or is unsafe, the accepted plan is unreadable,
or the task would need a non-allowlisted path, a dependency change, private
data, host/device access, an application launch, or subagents.

Stop with `PARTIAL` without committing when a slice cannot be completed inside
its exact scope without changing a name, a COMMAND, a string, a binding, or
behavior, and name the exact obstacle. Do not widen the allowlist.

Stop with `PASS` only when all three slices are validated, each normal non-force
push is publicly verified, and the terminal report is persisted and read back.
Then submit the terminal report and do no further work under this grant.

Authority for this Worker expires at this terminal report.
