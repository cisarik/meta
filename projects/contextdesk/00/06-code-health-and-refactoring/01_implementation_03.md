Logical whole identity: code-health-and-refactoring
Worker session ordinal: 01
Worker exchange ordinal: 04
Persistent role identity: WORKER
Worker session target: current-worker-session
Worker session profile: Implementation Worker
Phase: implementation
Task identity: CONTEXTDECK-CODE-HEALTH-REFACTORING-S1-CMAKE
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to the exact current Worker session
Continuity anchor: terminal revision report `01_report_02.md` for Worker
exchange `03`, which corrected the S4 extraction target of the accepted plan,
and the accepted plan report `01_report_01.md` for Worker exchange `02` — all
written in this same session
Authority renewal: prior planning authority expired at the revision report;
this prompt is a complete renewed implementation grant to the same session
Reasoning recommendation: Medium
Reasoning basis: bounded mechanical execution of an accepted decision-complete
plan (one new CMake helper file plus a refactor of 18 test registrations with
byte-stability invariants and the full registered suite as the gate); no open
design question and no live host mutation.
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: cross-cutting reversible build/test infrastructure change
under one cumulative fresh independent acceptance later in this logical whole;
this slice itself is mechanical and reversible with the full registered suite
as the behavior gate and one normal non-force product commit and push.
Internal delegation: prohibited

# ContextDeck — implement S1: the CMake unit-test helper

You are the WORKER session that produced the accepted plan. Native Plan Mode
must be OFF for this exchange. Do not use subagents.

This prompt grants one bounded repository-only implementation slice: apply the
accepted S1 decision exactly, validate against the exact baseline, create and
push one normal product commit, persist the terminal report in META, then stop.
You do not accept your own candidate and never close the logical whole.

Continuity and renewal: prior planning authority expired at the revision
report. Retained context, the plan text, and this conversation are convenience
and evidence, not authority; re-verify repository and environment state before
acting and stop on any conflict with current repository evidence. Evidence
produced in this session is non-independent.

Critical: no live host mutation, no application launch, no KWin/OpenRGB/broker/
device operation, no desktop mutation, no service change, no packaging change,
no dependency change, and no suspend/DPMS behavior may occur during this
exchange. This exchange edits, tests, commits, and pushes repository content
only; `build/` is git-ignored.

## Accepted plan and Plan-to-Execution transition

ORCHESTRATOR reconciliation: accepted
Accepted plan: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_01.md`
Accepted correction: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_02.md`
(the S4 ContextReceiver extraction target only; S4 is not in this slice and the
correction changes nothing here)

The planning budget is exhausted: one targeted revision was used. This prompt
is the separate complete implementation grant; the accepted plan and the
revision report supply no execution authority by themselves.

## Implementation Authority Record

Implementation authority: explicit
Exact baseline: `235d467c752958694dad4be7bcc31e66406dbdcc`
Changed-path allowlist: `CMakeLists.txt`; `cmake/contextdeck-tests.cmake` (new
file)
Implementation boundaries: add the shared unit-test registration helper and
refactor only the test-registration block of `CMakeLists.txt`; no test source,
no product source, no target-name, no link-library, no behavior, and no
documentation change
Independence required: no for this implementation slice; the cumulative fresh
independent acceptance for the whole is a later separate exchange

## Verified candidate and preflight gates

Canonical product repository: `https://github.com/cisarik/contextdesk`
Expected branch: `main`
Exact baseline HEAD: `235d467c752958694dad4be7bcc31e66406dbdcc`
Required parent: `293158887e4228a42b9c64bda7d4f0bd32fb4ec9`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

This whole's trace destination:
`projects/contextdesk/00/06-code-health-and-refactoring/`
Accepted plan report: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_01.md`
Accepted revision report: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_02.md`
Report destination: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_03.md`

Repository checkout topology: standalone product checkout on `main`
Working-copy topology: canonical product checkout
Topology rationale: one accountable Worker owns one coherent CMake refactor and
one commit; `build/` is git-ignored

Execution route: this repository declares no `ap.project.conf` operation; the
exact `cmake` / `ctest` commands below are the project-owned build and test
commands from `AGENTS.md` and `CMakeLists.txt`.

Before any mutation:

1. Verify the complete prompt, the exact current Worker session, Native Plan
   Mode OFF, coordinates `01/04`, the renewed authority, and no subagents.
2. Verify canonical remote, active `main`, exact HEAD, exact parent, clean
   state, no Git lock, matching AP gitlink/checkout, and `./.ap/ap doctor` PASS
   (variant `stable`).
3. Prove public product `main` equals the exact baseline with direct
   `git ls-remote`. Do not pull, merge, rebase, switch, reset, clean, stash, or
   retarget.
4. Verify META public `main` is `f4f93e2...` or a verified later descendant
   whose changed paths do not contradict this exchange.
5. Verify the trace directory is real and contains `00_handout.md`,
   `00_notes.md`, `01_planning_00.md`, `01_completion_01.md`,
   `01_planning_02.md`, `01_report_01.md`, and `01_report_02.md`; the report
   destination `01_report_03.md` must be absent before the write.
6. Read the accepted plan report and the revision report completely; confirm
   the S1 section matches this prompt's scope.
7. Read `CMakeLists.txt` and `cmake/contextdeck-warnings.cmake` before editing;
   every needed path must be inside the allowlist.

## S1 scope (from the accepted plan, exact)

Add `cmake/contextdeck-tests.cmake` and include it from `CMakeLists.txt`. It
defines `contextdeck_add_unit_test(<name>)` using `cmake_parse_arguments`
(PARSE_ARGV) with these options and one-value/multi-value arguments:

- `NO_AUTOMOC` — set `AUTOMOC OFF AUTOUIC OFF AUTORCC OFF` on the target;
- `DBUS_SESSION` — wrap the test command in `dbus-run-session` and set the
  offscreen Qt environment exactly as today;
- `SOURCES` (default `tests/unit/${name}.cpp`);
- `LIBRARIES`;
- `COMPILE_DEFINITIONS`;
- `INCLUDE_DIRECTORIES`;
- `COMMAND_ARGS`;
- `ENVIRONMENT`.

Refactor the 18 executable test registrations (`test_profile_resolver` through
`test_broker_ipc_client`) to use the helper. Keep the three non-executable
tests (`test_udev_verify`, `test_trial_cutoff`, `test_sleep_hook`) explicit and
byte-identical to today.

Invariants (must hold exactly):

- the 21 registered test names stay unchanged;
- every `add_test` COMMAND keeps today's exact spelling: plain tests
  `COMMAND <name>` (plus `COMMAND_ARGS` where present), dbus tests
  `COMMAND "${DBUS_RUN_SESSION_EXECUTABLE}" -- $<TARGET_FILE:<name>>` with
  `ENVIRONMENT "QT_QPA_PLATFORM=offscreen;QT_DISABLE_SESSION_MANAGER=1"` on
  `test_workspace_receiver`, `test_workspace_lighting`, and
  `test_workspace_mutator`;
- broker tests keep `AUTOMOC OFF AUTOUIC OFF AUTORCC OFF`;
- `test_udev_policy` keeps
  `target_compile_definitions(... CONTEXTDECK_SOURCE_DIR="${CMAKE_SOURCE_DIR}")`;
- `test_broker_ipc_client` keeps its extra source
  `src/app/BrokerIpcClient.cpp` and `-nocrashhandler`;
- every target keeps its exact `target_link_libraries` set;
- broker test doubles (`FakeSink`, `FakeSource`, `FakeGrabber`) stay compiled
  into `contextdeck_broker_core`; add a short CMake comment at those sources
  stating they are selftest/unit-only and not part of the ARM path;
- no test file, product source file, or documentation file changes.

## Mandatory reading

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-12, RF-16, RF-18, RF-19,
  implementation authority, Git safety, validation, stopping conditions;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Implementation Authority
  Record, exchange/trace contract, validation ladder, delivery record,
  Session-and-Mode;
- the accepted plan report `01_report_01.md`, especially the S1 section, the
  invariants, and the acceptance control matrix;
- the revision report `01_report_02.md` (S4 correction; reference only);
- `CMakeLists.txt` and `cmake/contextdeck-warnings.cmake`;
- `AGENTS.md` (test-suite ownership and project rules).

## Product invariants

- G213 only; five RGB zones, never per-key.
- Session app never opens raw keyboard nodes; broker stays static/inactive and
  no ARM/LEASE/grab/device probe occurs.
- Behavior preservation is the slice claim: no user-visible string, signal,
  property, QML binding, IPC/wire format, persisted schema, or log event changes.
- Repository documentation stays English, public-facing, and unchanged here.

## Commands and side-effect authority

Allowed: `git status`, `git log`, `git diff`, `git ls-remote`, `git rev-parse`,
`git show`; `cmake -S . -B build -G Ninja`; `cmake --build build`;
`ctest --test-dir build --output-on-failure`; `ctest -N`; exact-path
`git add`, one `git commit`, one normal non-force `git push`, and bounded
public readback.

Forbidden: any `git add .`/`-A`, force push, history rewrite, reset, clean,
stash, checkout, switch, rebase, merge, tag, branch, remote, or config write;
any product source/test/documentation edit; any dependency, packaging, service,
host, desktop, device, broker, OpenRGB, KWin, or input-remapper operation.

Side effects: reversible local source edits inside the allowlist, build outputs
under the git-ignored `build/`, one local product commit, and one normal
non-force product push. No META Git mutation by the Worker.

No raw input, key names, serials, host addresses, passwords, private paths,
desktop names/IDs, window captions, or unredacted tool logs may appear in the
report or trace.

## Validation ladder

Validation ladder: selected
Inspection and provenance: required — read `CMakeLists.txt` and the existing
`cmake/contextdeck-warnings.cmake` include pattern before editing
Existing focused tests: the 21 registered CTest names and their exact COMMAND
shapes are the focused evidence
Affected tests: all 21 (test registration itself changes)
New causal regression: none — the slice changes build wiring, not behavior; the
existing suite proves the registered tests still run and pass unchanged
Broad or full suite: required-because behavior preservation of the whole
logical whole is the named decision risk; run the full registered suite
Runtime or testbed: not-used
Independent acceptance: not-required for this slice; the whole receives one
cumulative fresh independent acceptance after later slices

Procedure:

1. Before edits, capture baseline evidence: configure and build the exact
   baseline, run `ctest -N`, and save `ctest -N` output plus the exact
   `add_test` COMMAND lines for one plain test, one broker `NO_AUTOMOC` test,
   one dbus test, `test_udev_policy`, and `test_broker_ipc_client` from
   `build/CTestTestfile.cmake` to a Worker-owned temporary location (for
   example under `/tmp`).
2. Apply only the allowlisted edits.
3. Reconfigure and rebuild; run `ctest -N` and prove exactly the same 21 names
   and byte-identical COMMAND lines against the baseline capture; run the full
   suite and require 21/21.
4. Inspect the diff: only `CMakeLists.txt` and the new
   `cmake/contextdeck-tests.cmake` may appear.

A failed gate stops the exchange before commit. Classify a failure before any
repair; do not rerun an unchanged broad gate; do not weaken the environment.

## Git and public verification

After a green suite:

1. Stage exactly `CMakeLists.txt` and `cmake/contextdeck-tests.cmake`; inspect
   the staged diff.
2. Create exactly one normal commit with subject:
   `Add contextdeck_add_unit_test CMake helper`
3. Before push, prove public `main` still equals the exact baseline with
   direct `git ls-remote`; on any mismatch, stop without pushing.
4. Push once, normal non-force, to `origin main`.
5. Verify local `HEAD`, remote-tracking state, and direct public `ls-remote`
   all equal the new commit; parent equals the exact baseline; changed paths
   are exactly the allowlist.

If commit or push is unavailable or fails, report `PARTIAL` with the exact
state; never force or bypass.

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
Downloadable prompt filename: 01_implementation_03.md
Destination path: projects/contextdesk/00/06-code-health-and-refactoring/
Report filename: 01_report_03.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR for META; WORKER for the one product commit
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
- start and end product commit (baseline and the new commit);
- changed files and purpose;
- tests and validation, including the baseline-vs-candidate `ctest -N` and
  COMMAND-shape comparison and the full-suite result;
- commit and push result plus direct public-ref verification;
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

Explicit non-claims: no acceptance-PASS, publication-PASS beyond the one pushed
commit, deployment-PASS, production readiness, M2/G4/G3 closure, autostart,
hibernate/hybrid sleep, input-remapper coexistence, M3/M4 closure or physical
behavior, M5, remapping, deck layer, per-key RGB, license selection, or
hardware acceptance; no claim that the cumulative behavior-preservation
acceptance has happened; no claim that refactoring beyond this CMake slice is
complete.

## Stop conditions

Stop and report `BLOCKED` before mutation if: the session is not the healthy
continuation session, Native Plan Mode is on, coordinates or authority are
contradictory, product/AP/META identity fails, the worktree has unexplained
changes, the trace path collides or is unsafe, the accepted plan is unreadable,
or the task would need a non-allowlisted path, a dependency change, private
data, host/device access, or subagents.

Stop with `PARTIAL` without committing when a planned registration cannot be
expressed through the helper without changing a name, a COMMAND, a link
library, or a property, and name the exact obstacle. Do not widen the
allowlist.

Stop with `PASS` only when the full suite passes, one normal non-force push is
publicly verified, and the terminal report is persisted and read back. Then
submit the terminal report and do no further work under this grant.

Authority for this Worker expires at this terminal report.
