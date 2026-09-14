Logical whole identity: code-health-and-refactoring
Worker session ordinal: 01
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Planner
Phase: planning
Task identity: CONTEXTDECK-CODE-HEALTH-REFACTORING-PLAN
Native planning mode: required
Delivery route: manual COOPERATOR delivery to a genuinely fresh Worker session
Reasoning recommendation: High
Reasoning basis: the plan must choose durable decomposition boundaries for a
large `AppController`, a 1483-line `Persistence.cpp`, two D-Bus receivers, and
the build/test infrastructure while proving behavior preservation across QML
bindings, IPC schemas, and 21 registered tests; a wrong boundary becomes durable
structure that the later UI/UX whole inherits, and no later session reconstructs
the reasoning cheaply. Standard reasoning cannot settle the cross-file ownership
questions with the required confidence.
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: the eventual whole is cross-cutting but reversible source
refactoring with strong registered tests, no production or durable-data
migration, no security-boundary or trust-boundary change, no host, device,
desktop, launch, broker-semantics, packaging, or dependency mutation; the full
registered CTest suite (21 tests, roughly 70 s at the candidate) is the named
broad gate for behavior preservation. This planning exchange itself is
read-only.
Internal delegation: prohibited

# ContextDeck — plan the code health & refactoring whole

You are a genuinely fresh WORKER assigned only to repository-grounded
implementation planning. Use the client's actual Native Plan Mode. You did not
participate in M1–M4 implementation or acceptance, and you inherit no authority
from any previous session. Do not dispatch subagents.

This is a planning grant only. It authorizes no product implementation, no
source mutation, no host operation, no deployment, no acceptance execution, and
no Git publication. Stop at the terminal planning report.

The whole exists because ContextDeck's code must be clean, cohesive, and
tractable before a later UI/UX whole run by another Orchestrator. The accepted
architecture, behavior, visuals, product claims, and safety boundaries are not
in question; only internal structure may change. The COOPERATOR has approved
this whole with the direction: any verifiable improvement is welcome, go as deep
as the evidence supports, change nothing observable, and make no unverified
claim.

## Planning record and Plan-to-Execution gate

Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: every accepted M1–M4 code decision and
deferral; the M2 park claims and named accepted G4 slices; the five-zone,
G213-only, event-driven-KWin, typed-action, disabled-broker, and one-OpenRGB-
connection invariants; the 21 registered CTest names; the META trace grammar;
the current `ChatOrchestrator` access-profile declaration (a separate
COOPERATOR policy item — do not change those lines)
Automatic targeted revisions used: 0

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: one repository-grounded, decision-complete plan for
`code-health-and-refactoring` that (a) selects and orders behavior-preserving
refactoring slices from the candidate set below, (b) gives each slice an exact
changed-path allowlist, focused tests, and the full registered suite as its
broad gate, (c) designs the cumulative implementation exchange and commit
sequence and one fresh independent acceptance (or returns a justified proposal
to split the work into several logical wholes with their own identities and
acceptance), and (d) states per slice exactly what must remain observably
unchanged and how that is evidenced
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: a separate complete ORCHESTRATOR implementation
prompt whose native planning-mode value is `not-used`
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1

The ORCHESTRATOR reconciles the plan before any implementation prompt. Native
Plan approval, "continue", retained context, or the existence of this prompt
never grants execution authority.

## Verified public candidate

Canonical product repository: `https://github.com/cisarik/contextdesk`
Expected branch: `main`
Exact product candidate:
`235d467c752958694dad4be7bcc31e66406dbdcc`
Required parent:
`293158887e4228a42b9c64bda7d4f0bd32fb4ec9`
M4 accepted Slice A candidate: `aca6c68542bbc9f1b8ee891415a04b0a95e8372e`
M4 accepted Slice B candidate: `db9ddc1f923f44e26f7f1d58df7446306bbdf64a`
M3 code-accepted candidate: `502ae75571358ec95d33c836084b5e2253850731`
M2 inactive-install candidate (historical; do not reopen):
`cb72ae0388307b514182efc6936712e3da42cda4`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

Canonical META repository: `https://github.com/cisarik/meta.git`
Verified public META baseline at preparation:
`f4f93e2c8bed9009bca5c16755bd9413b54aa951`
This whole's trace destination:
`projects/contextdesk/00/06-code-health-and-refactoring/`
Closed predecessor trace:
`projects/contextdesk/00/05-m4-state-and-ledger-reconciliation/`
M4 trace:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/`
M3 trace:
`projects/contextdesk/00/03-g213-contextdeck-workspace-aware-lighting/`
M2 trace:
`projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/`
M1 trace:
`projects/contextdesk/00/01-g213-contextdeck-mvp-context-lighting/`

Before planning, verify without changing repository state:

1. Product root, canonical remote, active `main`, clean worktree, exact HEAD
   `235d467c...`, exact parent `2931588...`, AP gitlink/checkout equality
   `0cf2cff...`, and `./.ap/ap doctor` PASS with variant `stable`.
2. Direct `git ls-remote` for product `main` equals the exact candidate. Do not
   fetch, pull, switch, reset, clean, stash, rebase, merge, or retarget the
   COOPERATOR-owned checkout.
3. Direct `git ls-remote` for META `main` equals the exact baseline above or a
   verified later descendant. The COOPERATOR may commit this whole's opening
   artifacts (`00_handout.md`, `00_notes.md`) and the prepared prompt at any
   time; the prompt and the report are first-added together only after the
   report exists. If the public META head is later, inspect its changed paths
   and accept it only if it does not contradict this prompt.
4. This whole's trace directory exists as a real directory containing the
   ORCHESTRATOR-authored `00_notes.md` and the opening `00_handout.md` (the
   predecessor full-Orchestrator continuity record). If readable, the opening
   handout's SHA-256 is
   `7c4031d49b8acecc6f1ac40ca37afaadcdcca632677c74eb328711672937f26e`. Do not
   alter `00_notes.md` or `00_handout.md`.
5. Apart from the exact report preparation authorized below, preserve all owner
   work and stop on unexplained state.

If the product candidate, parent, AP pin, public ref, trace identity, or
repository state differs materially, stop before planning and return `BLOCKED`.
Do not silently use a nearby commit or an old clone.

## Objective and depth

Make the session-app, core, and UI-facing code clean and tractable through
behavior-preserving refactoring only. "Behavior-preserving" means: no observable
change to behavior, visuals, user-visible strings, QML bindings, property or
signal names, IPC or wire formats, persisted file formats, log event semantics,
timing characteristics that a user or test can observe, product claims, or
safety boundaries. A slice that changes a semantic validator, a structural
field, or runtime behavior is not behavior-preserving and must not be planned
as such.

The COOPERATOR has approved maximal depth within those bounds. Do not minimize
scope artificially; do not exceed the bounds. Prefer cohesive, testable units
with clear ownership over clever abstraction.

## Candidate slices (ORCHESTRATOR observations at the candidate; re-verify all)

These are evidence-backed candidates, not decisions. You select, merge, split,
order, and bound them. Every file size and count below is an observation to
re-verify at the exact candidate.

S1 — Build and test infrastructure (lowest risk; likely first).
`CMakeLists.txt` (283 lines) repeats 21 near-identical
`add_executable`/`target_link_libraries`/`add_test` triples. Propose a small
`contextdeck_add_test()` helper or equivalent, keeping the 21 registered test
names and their command lines byte-stable unless a registered test's exact
definition is part of the plan. Broker test doubles (`FakeSink`, `FakeSource`,
`FakeGrabber` in `src/broker/`) are compiled into `contextdeck_broker_core` and
are used by in-tree selftests (`src/broker/Selftest.cpp`,
`src/broker/WatchdogSelftest.cpp`) as well as by tests; decide, with a
documented rationale, whether to keep them or move them to a test-support
target linked by both. There is no `.clang-format` or `.clang-tidy`; adding
configuration is optional. A codebase-wide reformat commit is prohibited;
format only files a slice actually touches.

S2 — Split `src/core/Persistence.cpp` (1483 lines). A large anonymous
namespace holds roughly 30 parse/serialize helpers (`parseChord`,
`parseAssignment`, `parseKeys`, zone parsers v2/v3, `parseLightingV1/Common`,
`parseMatch`, `parseTitleFallback`, `parseWorkspaceAssignment/Session`,
`parsePreferences`; `assignmentToJson`, `keysToJson`, `lightingToJson`,
`titleFallbackToJson`, `workspaceAssignmentToJson`, `workspaceSessionToJson`).
`ProfileStore::parseDocument` is roughly 265 lines, `validate` roughly 108,
`toJson` roughly 60, IO roughly 90. Proposed: cohesive `src/core/persistence/`
units behind the existing public API in `src/core/Persistence.h`, with no
schema or behavior change. `tests/unit/test_profile_persistence.cpp` (1098
lines) plus the full suite is the gate.

S3 — Decompose `AppController` (god object). `src/app/AppController.h` is 277
lines with 48 `Q_PROPERTY`, 52 `Q_INVOKABLE`, and 71 public accessors;
`src/app/AppController.cpp` is 2285 lines with roughly 134 function
definitions. Mixed responsibilities: QML presentation strings, hero, and
diagnostics; lighting resolution and OpenRGB push; document/profile editing;
workspace session editing; workspace preview/apply/revert/launch orchestration;
broker lease; power actions; context/identity handling. 83 unique `app.*`
bindings exist across 9 QML files (`app.diagnostics` ×34; `workspace*` ≈45;
lighting/zone ≈20; profile/inventory ≈10). Propose a decomposition (for
example `LightingController`, `ProfileEditor`, `WorkspaceSessionEditor` +
`WorkspaceApplyController`, `PresentationModel`, `BrokerLeaseController`) with
`AppController` as thin composition or several QML context properties. Preserve
every `app.*` binding name and behavior; update QML mechanically only if
unavoidable and prove no visual change. `tests/unit/test_workspace_lighting.cpp`
(811 lines) drives the controller directly and must keep equivalent behavioral
coverage.

S4 — Receivers: extract pure codecs, reduce mixed D-Bus concerns.
`src/context/WorkspaceReceiver.cpp` (834 lines) implements subscription, owner
resolution, coalescing, request ownership, deadlines, and recovery, plus a pure
`decodeSnapshot` (roughly 197 lines within roughly 577–773) that can become a
`WorkspaceStateCodec` testable without D-Bus. `src/context/ContextReceiver.cpp`
(676 lines) similarly mixes transport lifecycle and parsing; extract pure parts
only where duplication is real and avoid over-abstraction. Keep receiver
semantics identical; `tests/unit/test_workspace_receiver.cpp` (1324 lines,
private `dbus-run-session` fake manager) remains the gate.

S5 — Types and dead API. `src/core/Types.h` (476 lines) mixes enums, structs,
and inline helpers; an optional split into focused headers is acceptable if it
lowers include coupling. `AppController::remappingState` is a placeholder
constant (`"inactive-until-M2"`) with no QML consumer; remove it or wire it.
Sweep for other unused controller members by generating a QML usage table.

S6 — Test organization. Largest tests: `test_workspace_receiver.cpp` 1324,
`test_profile_persistence.cpp` 1098, `test_workspace_mutator.cpp` 1015,
`test_workspace_lighting.cpp` 811, `test_profile_resolver.cpp` 624,
`test_broker_ipc.cpp` 643, `test_broker_watchdog.cpp` 553. `FakeDesktopManager`
is duplicated in two test files; extract shared helpers under a tests-support
location while keeping registered test names stable (`CMakeLists.txt` owns
them).

S7 — Documentation accuracy. Re-verify and correct the `ROADMAP.md` M2
"production safety gaps already visible in source" list (silent uinput write
errors; virtual-device capabilities from `passthroughCapabilities()` rather
than measured source bits / LED return path; logind `sd_pid_get_session` vs
user-manager-launched session apps) against the exact candidate with exact
evidence; an opening spot-check indicates the first two are already addressed
(`src/broker/ForwardingEngine.cpp` fails closed on a sink write failure;
`src/broker/Acquisition.cpp` applies measured capabilities before virtual
creation and `RealSink::passthroughCapabilities()` is test-only; re-verify,
including whether the third remains truthful). Also fix or park, with evidence,
the carried lines: the `ROADMAP.md` M2-backlog sleep-hook bullet ending "Not
autostart. Not live suspend evidence. ADR 0001." and the `docs/testing-m2.md`
remaining-G4 lists naming LED return / all-control / live suspend /
input-remapper; and update the transient "current whole" wording in
`ROADMAP.md` and `README.md` now that the predecessor whole is closed. Do not
change the `AGENTS.md`/`ROADMAP.md` access-profile lines; that is a separate
open COOPERATOR policy item.

## Required planning outcome

Return exactly one decision-complete plan (the terminal report) containing at
least:

1. The selected slices with an explicit order and, for each: the refactoring
   objective; the exact changed-path allowlist; the cohesive units and their
   responsibilities; the interfaces preserved; and the rollback story.
2. For each slice, the unchanged-observable matrix: behavior, visuals, strings,
   QML binding/property/signal names, IPC/wire formats, persisted schemas, log
   events, and test-visible timing; plus the exact focused tests that evidence
   the preservation and the full-suite checkpoint.
3. A build/test infrastructure decision (S1): the exact helper shape, the
   21 registered test names and command lines as invariants, the test-double
   placement decision with rationale, and whether any optional formatter/linter
   configuration is added (with the no-global-reformat rule).
4. The implementation exchange and commit sequence: which slices share one
   Worker exchange, the expected commit subjects, the cumulative candidate
   definition at each exchange, and where the full registered suite runs.
5. The cumulative acceptance design: one fresh independent acceptance after the
   final slice (plus at most one correction re-audit), or a justified proposal
   to split the work into several logical wholes with their own identities,
   scopes, final candidates, and acceptance routes. If you propose a split,
   state the exact boundary between wholes and why one acceptance cannot cover
   the whole tractably.
6. The exact final-acceptance control matrix: what the fresh acceptance worker
   must verify (suite from an exact candidate, focused evidence, unchanged-
   observable checks, public equality) and the evidence that would falsify the
   behavior-preservation claim.
7. A risk register: the largest risks (QML binding regression, persistence
   parse regression, receiver lifecycle regression, hidden coupling, test
   changes masking behavior), their detection, and rollback.
8. The exact planning assumptions and any named missing evidence; if one
   material design choice cannot be settled from repository evidence, return
   `PARTIAL` naming it — do not guess.

The plan must be sufficient for the ORCHESTRATOR to issue bounded
implementation prompts without another planning cycle. It must not propose any
change outside behavior-preserving refactoring and the S7 documentation
corrections.

## Reading and inspection list

Read the pinned AP Worker minimum spine and, at minimum:

- `.ap/AP.md` — Semantic Authority, RF-03/RF-06/RF-12/RF-16/RF-18/RF-19,
  orchestration and implementation planning, Plan-to-Execution, Worker
  responsibilities, validation, stopping conditions;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md` — Worker report header, Planning Record, Worker
  Session Target, exchange and trace contract, validation ladder, delivery
  record, Session-and-Mode, Plan-to-Execution;
- `AGENTS.md` including the managed AP block;
- `README.md`;
- `ROADMAP.md`, especially the current-state, M2/M3/M4, and production-safety
  sections;
- `docs/specification.md`;
- `docs/architecture.md`;
- `docs/operations.md`;
- `docs/testing-m1.md` through `docs/testing-m4.md` only as needed to preserve
  their boundaries;
- `docs/adr/` (all current ADRs and `README.md`);
- `CMakeLists.txt`;
- all of `src/` needed to ground the slices, especially
  `src/core/Persistence.{h,cpp}`, `src/core/Types.h`, `src/app/AppController.{h,cpp}`,
  `src/context/WorkspaceReceiver.{h,cpp}`, `src/context/ContextReceiver.{h,cpp}`,
  `src/broker/` build wiring and test doubles, and `src/workspace/`;
- all of `ui/` for the `app.*` binding inventory;
- `tests/unit/` for test structure and duplication;
- this whole's `00_handout.md` and `00_notes.md`;
- the closed predecessor plan `05-m4-state-and-ledger-reconciliation/01_report_00.md`
  (§3.2/§3.3) for the access-profile item that must remain unchanged;
- older traces only as needed to preserve M2/M3/M4 boundaries.

You may inspect the exact candidate in a fresh disposable clone or in a clean
checkout at the exact candidate. Every finding must be tied to the exact
candidate. No host reconnaissance: do not inspect device nodes, private
configuration values, logs, home paths, other repositories, credentials, or
unrelated host state. Do not configure, build, or execute tests in this
planning exchange; read source, tests, and build definitions only.

## Authority and side-effect boundary

Product source mutation: prohibited
Product Git mutation: prohibited
Product commit/push: prohibited
AP mutation/update: prohibited
Host mutation: prohibited
Desktop create/remove/rename: prohibited
`kwinrulesrc` write: prohibited
Application launching: prohibited
Host service operation: prohibited
Broker start/stop/ARM/grab/probe: prohibited
Input-remapper operation: prohibited
OpenRGB/KWin installation or runtime operation: prohibited
Physical-device probing or physical acceptance: prohibited
Dependency installation/update: prohibited
Secrets/credentials/private data: prohibited
Network authority: reads from the two canonical HTTPS remotes only
(`https://github.com/cisarik/contextdesk.git`,
`https://github.com/cisarik/meta.git`): `git ls-remote`, read-only fetches or
clones into Worker-owned temporary directories, and direct public content
reads. No alternate mirror, no external research, no provider calls.
Side effects: read-only inspection plus the exact META trace-file preparation
below only

No raw input, raw event lines, key names, scan values, typed content, serials,
host addresses, host keys, passwords, private paths, desktop names/IDs, window
captions, or unredacted tool logs may appear in the prompt, report, or trace.
Use only semantic state and public repository-relative paths.

No recovery route is required because this exchange must not start, open, probe,
or grab a device. If any step would cross that boundary, stop.

## Validation ladder

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: identify exact existing tests per slice from
`CMakeLists.txt` and `tests/unit/`; do not configure, build, or execute them in
this planning exchange
Affected tests: propose exact focused tests per slice, including any new causal
regression with the named behavior or uncovered gap it closes
New causal regression: required where a slice creates a behavior-preservation
risk that no existing test covers; otherwise none, with the reason and the
counterevidence
Broad or full suite: the full registered 21-test CTest suite is the planned
broad gate for every implementation slice, because behavior preservation across
a god-object decomposition and persistence/receiver splits is the named
decision risk; state the exact commands from the candidate
Runtime or testbed: not-used in this planning exchange
Independent acceptance: stated by the plan from the accepted implementation
content (cumulative fresh acceptance, or the split proposal's per-whole
acceptance)

The planning result is non-implementation evidence. It does not accept code or
behavior.

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
Downloadable prompt filename: 01_planning_00.md
Destination path: projects/contextdesk/00/06-code-health-and-refactoring/
Report filename: 01_report_00.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

The ORCHESTRATOR persists this exact prompt bytes to
`projects/contextdesk/00/06-code-health-and-refactoring/01_planning_00.md`
before delivery. The WORKER may write only the report file at
`projects/contextdesk/00/06-code-health-and-refactoring/01_report_00.md` in the
COOPERATOR-owned META working tree.

Before substantive planning, verify the already-persisted prompt file exists and
is byte-identical to the received prompt; read it back completely. Stop on a
non-identical or unsafe collision. Do not alter `00_notes.md` or
`00_handout.md`, create a handout, or write any other META path.

After planning, write the complete terminal report first to the report path,
read it back completely, and verify the header, coordinates, content, and
filename. Do not overwrite a non-identical existing report. Do not stage,
commit, push, pull, merge, rebase, or otherwise mutate META Git history or refs.
The COOPERATOR archives the exact prompt/report pair together in one first-add
commit only after the report exists.

If the exact META destination is not reachable from your environment, do not
write to any other path; state the exact limitation in the report body and
return the complete report through the client output so the COOPERATOR can
persist it exactly. Do not reconstruct or prettify earlier artifacts.

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

It must echo the opening persistent-role and three coordinate fields exactly
once, with their values unchanged.

Include:

- status: `PASS`, `PARTIAL`, or `BLOCKED`;
- phase-qualified result: `not-applicable` (planning is not implementation);
- start and end product commit (expected unchanged exact candidate);
- verified product/AP/META identities and clean-state result;
- source-grounded current-state findings, each tied to the exact candidate;
- the complete decision-ready plan covering all measurable-outcome items above,
  including exact per-slice allowlists and, where documentation text changes,
  exact replacement text or anchor-based edit instructions;
- the implementation exchange and commit sequence and the acceptance design;
- the E2 implementation/acceptance evidence envelope and validation rationale;
- explicit statement that the plan made no product, AP, host, service,
  desktop-configuration, launch, device, dependency, or Git publication
  mutation;
- trace prompt/report persistence and complete-readback result;
- deviations, risks, unresolved decisions, and missing evidence;
- exactly one smallest next step: ORCHESTRATOR reconciliation of this plan and,
  only if accepted, a separate implementation Worker prompt;
- exactly one `Report justification: new-evidence`;
- `Resolved Execution Issues / Near-Misses: none` or a complete entry;
- `Pre-Existing Failure Classification: none` or a complete entry;
- compact critique:

  `Orchestration critique:`

  `MEASURED: none | <verified finding; evidence; effect; smallest correction>`

  `LEAD: none | <unverified possibility; cheapest useful check>`

- exactly one `Logical-whole closure: not-closed` line;
- the exact authority-expiry sentence below.

Explicit non-claims in the report:

- no implementation-PASS, acceptance-PASS, publication-PASS, deployment-PASS,
  production readiness, M2/G4 closure, G3 independent re-audit, autostart,
  hibernate/hybrid sleep, general input-remapper coexistence, M3 closure, M3
  physical five-zone observation, M4 closure, M4 live desktop/launch/placement
  behavior, M5 integration, remapping, deck-layer behavior, per-key RGB, license
  selection, or physical hardware acceptance;
- no claim that refactoring preserved behavior until the later implementation
  and its acceptance actually establish it;
- no claim that any slice improves performance, memory, or startup time unless
  the plan includes evidence to measure it without changing observable
  behavior;
- no claim that Session 27 was a fresh Worker result.

Authority for this Worker expires at this terminal report.

## Stop conditions

Stop and report `BLOCKED` before substantive planning if the session is not
genuinely fresh, Native Plan Mode is not actually enabled, coordinates or
authority are contradictory, product/AP/META identity fails, the worktree has
unexplained changes, the continuity records are missing, the trace path
collides or is unsafe, required repository evidence cannot be read, or
completing the plan would require a prohibited mutation, private data,
host/device/desktop access, an additional dependency, or subagents.

Stop with `PARTIAL` if the repository can be analyzed but one material design
choice or required evidence item remains unresolved, or if a justified split
proposal is the only tractable route. Do not implement, touch the live desktop,
or silently widen scope to force PASS.

Stop with `PASS` only when the complete decision-ready plan, exact slice
boundaries, and exact later implementation boundary are persisted and read
back. Then submit the terminal report and do no further work under this grant.
