Logical whole identity: code-health-and-refactoring
Worker session ordinal: 01
Worker exchange ordinal: 05
Persistent role identity: WORKER
Worker session target: current-worker-session
Worker session profile: Implementation Worker
Phase: implementation
Task identity: CONTEXTDECK-CODE-HEALTH-REFACTORING-S2-PERSISTENCE
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to the exact current Worker session
Continuity anchor: terminal implementation report `01_report_03.md` for Worker
exchange `04` (S1 CMake helper, accepted) and the accepted plan report
`01_report_01.md` corrected by `01_report_02.md` — all written in this same
session
Authority renewal: prior implementation authority expired at the S1 terminal
report; this prompt is a complete renewed implementation grant to the same
session
Reasoning recommendation: Medium
Reasoning basis: bounded mechanical split of one 1483-line translation unit
behind an unchanged public API, driven by an accepted decision-complete plan,
with `test_profile_persistence` plus the full registered suite as the gate; no
open design question and no behavior change.
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: cross-cutting reversible source refactoring under one
cumulative fresh independent acceptance later in this logical whole; this slice
is mechanical and reversible with the full registered suite as the behavior
gate and one normal non-force product commit and push.
Internal delegation: prohibited

# ContextDeck — implement S2: split Persistence into cohesive codec units

You are the WORKER session that implemented S1. Native Plan Mode must be OFF
for this exchange. Do not use subagents.

This prompt grants one bounded repository-only implementation slice: apply the
accepted S2 decision exactly, validate against the exact baseline, create and
push one normal product commit, persist the terminal report in META, then stop.
You do not accept your own candidate and never close the logical whole.

Continuity and renewal: prior implementation authority expired at the S1
terminal report. Retained context, the plan text, and this conversation are
convenience and evidence, not authority; re-verify repository and environment
state before acting and stop on any conflict with current repository evidence.
Evidence produced in this session is non-independent.

Critical: no live host mutation, no application launch, no KWin/OpenRGB/broker/
device operation, no desktop mutation, no service change, no packaging change,
no dependency change, and no suspend/DPMS behavior may occur during this
exchange. This exchange edits, tests, commits, and pushes repository content
only; `build/` is git-ignored.

Client note from S1 (not a product issue): if distro `cmake` fails with a
`CMAKE_ROOT` lookup error because the client injects bundled library paths, run
the granted `cmake`/`ctest` commands with a cleaned distro `PATH`. Do not record
host-local paths anywhere.

## Accepted plan and Plan-to-Execution transition

ORCHESTRATOR reconciliation: accepted
Accepted plan: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_01.md`
Accepted correction: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_02.md`
(The correction changed only the S4 ContextReceiver extraction target; S4 is
not in this slice.)

S1 is reconciled and accepted as implementation-PASS: public `main` =
`5b2b25bc64c86f1ea568d82b94da2b3271b10c85`, diff limited to the S1 allowlist,
full registered suite 21/21 from the exact candidate. This prompt is the next
separate implementation grant; the plan and reports supply no execution
authority by themselves.

## Implementation Authority Record

Implementation authority: explicit
Exact baseline: `5b2b25bc64c86f1ea568d82b94da2b3271b10c85`
Changed-path allowlist: `src/core/Persistence.cpp`; `src/core/persistence/`
(new internal headers and sources); `CMakeLists.txt` (`contextdeck_core`
sources only); `src/core/Persistence.h` only if a purely mechanical change is
unavoidable, with no declaration or signature change
Implementation boundaries: split the existing implementation into cohesive
internal units behind the unchanged public API; no signature, semantics,
schema, error-string, serialization, or log change; no new test; no other
source, UI, documentation, or broker change
Independence required: no for this implementation slice; the cumulative fresh
independent acceptance for the whole is a later separate exchange

## Verified candidate and preflight gates

Canonical product repository: `https://github.com/cisarik/contextdesk`
Expected branch: `main`
Exact baseline HEAD: `5b2b25bc64c86f1ea568d82b94da2b3271b10c85`
Required parent: `235d467c752958694dad4be7bcc31e66406dbdcc`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

This whole's trace destination:
`projects/contextdesk/00/06-code-health-and-refactoring/`
Accepted plan report: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_01.md`
Accepted revision report: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_02.md`
Report destination: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_04.md`

Repository checkout topology: standalone product checkout on `main`
Working-copy topology: canonical product checkout
Topology rationale: one accountable Worker owns one coherent codec split and
one commit; `build/` is git-ignored

Execution route: this repository declares no `ap.project.conf` operation; the
exact `cmake` / `ctest` commands below are the project-owned build and test
commands from `AGENTS.md` and `CMakeLists.txt`.

Before any mutation:

1. Verify the complete prompt, the exact current Worker session, Native Plan
   Mode OFF, coordinates `01/05`, the renewed authority, and no subagents.
2. Verify canonical remote, active `main`, exact HEAD, exact parent, clean
   state, no Git lock, matching AP gitlink/checkout, and `./.ap/ap doctor` PASS
   (variant `stable`).
3. Prove public product `main` equals the exact baseline with direct
   `git ls-remote`. Do not pull, merge, rebase, switch, reset, clean, stash, or
   retarget.
4. Verify META public `main` is `56baa3d3b4cc210d9a1d65cf5a5622bc60f408d5` or
   a verified later descendant whose changed paths do not contradict this
   exchange.
5. Verify the trace directory is real and contains `00_handout.md`,
   `00_notes.md`, `01_planning_00.md`, `01_completion_01.md`,
   `01_planning_02.md`, `01_report_01.md`, `01_report_02.md`, and
   `01_report_03.md`; the report destination `01_report_04.md` must be absent
   before the write.
6. Read the accepted plan report S2 section completely; read
   `src/core/Persistence.h` and `src/core/Persistence.cpp` before editing; every
   needed path must be inside the allowlist.

## S2 scope (from the accepted plan, exact)

Split `src/core/Persistence.cpp` (1483 lines at baseline) into cohesive units
under `src/core/persistence/` behind the unchanged public API in
`src/core/Persistence.h`:

- `JsonCommon` — `makeError`, `isInteger`, `checkObjectKeys`,
  `hasControlCharacters`, `boundedUtf8`, `looksLikeDesktopId`;
- `KeysJson` — chord, assignment, and keys parse and serialize;
- `LightingJson` — zone v2/v3, lighting v1/common, lighting JSON;
- `MatchJson` — match and title fallback;
- `WorkspaceJson` — workspace assignment and session;
- `DocumentCodec` — `ProfileStore::parseDocument` / `validate` / `toJson` /
  `parsePreferences`;
- `Persistence.cpp` — path resolution plus `ProfileStore::load` / `save` /
  `toJsonBytes` only.

No shared helper with the D-Bus receivers: different bounds and error model.

Invariants (must hold exactly):

- `src/core/Persistence.h` declarations and public API unchanged; if the file
  is touched at all, the change is purely mechanical and is reported;
- `kSchemaVersion` unchanged;
- every parse/serialize semantic unchanged, including schema v2/v3 zone
  parsing, v1 lighting, match, title fallback, workspace assignment and
  session, and preferences;
- every parse error string and code unchanged (tests assert them);
- serialization output unchanged for all inputs the tests cover;
- log events unchanged;
- no behavior change and no new test (the plan forbids a new test here: it
  would freeze internal structure);
- CMake changes are limited to the `contextdeck_core` source list.

## Mandatory reading

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-12, RF-16, RF-18, RF-19,
  implementation authority, Git safety, validation, stopping conditions;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Implementation Authority
  Record, exchange/trace contract, validation ladder, delivery record,
  Session-and-Mode;
- the accepted plan report `01_report_01.md`, especially the S2 section;
- `src/core/Persistence.h`, `src/core/Persistence.cpp`;
- `tests/unit/test_profile_persistence.cpp` (behavior anchor; do not modify);
- `CMakeLists.txt` (`contextdeck_core` sources);
- `AGENTS.md`.

## Product invariants

- G213 only; five RGB zones, never per-key.
- Session app never opens raw keyboard nodes; broker stays static/inactive and
  no ARM/LEASE/grab/device probe occurs.
- Behavior preservation is the slice claim: no user-visible string, signal,
  property, QML binding, IPC/wire format, persisted schema, or log event
  changes.
- Repository documentation stays English, public-facing, and unchanged here.

## Commands and side-effect authority

Allowed: `git status`, `git log`, `git diff`, `git ls-remote`, `git rev-parse`,
`git show`; `cmake -S . -B build -G Ninja`; `cmake --build build`;
`ctest --test-dir build --output-on-failure`; exact-path `git add`, one
`git commit`, one normal non-force `git push`, and bounded public readback.

Forbidden: any `git add .`/`-A`, force push, history rewrite, reset, clean,
stash, checkout, switch, rebase, merge, tag, branch, remote, or config write;
any other source, test, UI, documentation, packaging, or dependency edit; any
service, host, desktop, device, broker, OpenRGB, KWin, or input-remapper
operation.

Side effects: reversible local source edits inside the allowlist, build outputs
under the git-ignored `build/`, one local product commit, and one normal
non-force product push. No META Git mutation by the Worker.

No raw input, key names, serials, host addresses, passwords, private paths,
desktop names/IDs, window captions, or unredacted tool logs may appear in the
report or trace.

## Validation ladder

Validation ladder: selected
Inspection and provenance: required — read `Persistence.h` and `Persistence.cpp`
before editing and preserve the public declarations byte-for-byte
Existing focused tests: `test_profile_persistence` is the focused behavior
anchor
Affected tests: `test_profile_persistence` plus every test that links
`contextdeck_core` (build linkage regression)
New causal regression: none — the public API and behavior are unchanged and a
new test would freeze internal structure (accepted plan decision)
Broad or full suite: required-because behavior preservation of the whole
logical whole is the named decision risk; run the full registered suite
Runtime or testbed: not-used
Independent acceptance: not-required for this slice; the whole receives one
cumulative fresh independent acceptance after later slices

Procedure:

1. Build the exact baseline and run `test_profile_persistence` and the full
   suite to confirm the starting green state.
2. Apply only the allowlisted split edits.
3. Reconfigure and rebuild; run `test_profile_persistence`, then the full
   suite and require 21/21.
4. Inspect the diff: only allowlisted paths; prove
   `git diff -- src/core/Persistence.h` is empty or purely mechanical with no
   declaration change.

A failed gate stops the exchange before commit. Classify a failure before any
repair; do not rerun an unchanged broad gate; do not weaken the environment.

## Git and public verification

After a green suite:

1. Stage exactly the allowlisted paths; inspect the staged diff.
2. Create exactly one normal commit with subject:
   `Split ProfileStore codecs into src/core/persistence`
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
Downloadable prompt filename: 01_implementation_04.md
Destination path: projects/contextdesk/00/06-code-health-and-refactoring/
Report filename: 01_report_04.md
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
- changed files and purpose, including the new unit list;
- tests and validation, including the focused test, the full-suite result, and
  the `Persistence.h` diff check;
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
acceptance has happened; no claim that refactoring beyond this Persistence
slice is complete; no claim that the META trace privacy correction has been
performed (that is a COOPERATOR decision and action).

## Stop conditions

Stop and report `BLOCKED` before mutation if: the session is not the healthy
continuation session, Native Plan Mode is on, coordinates or authority are
contradictory, product/AP/META identity fails, the worktree has unexplained
changes, the trace path collides or is unsafe, the accepted plan is unreadable,
or the task would need a non-allowlisted path, a dependency change, private
data, host/device access, or subagents.

Stop with `PARTIAL` without committing when a unit boundary or an anonymous
namespace helper cannot be moved without changing a declaration, a semantic, an
error string, or a serialization observable, and name the exact obstacle. Do
not widen the allowlist.

Stop with `PASS` only when the focused test and the full suite pass, one normal
non-force push is publicly verified, and the terminal report is persisted and
read back. Then submit the terminal report and do no further work under this
grant.

Authority for this Worker expires at this terminal report.
