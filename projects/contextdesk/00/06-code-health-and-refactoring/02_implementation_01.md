Logical whole identity: code-health-and-refactoring
Worker session ordinal: 02
Worker exchange ordinal: 02
Persistent role identity: WORKER
Worker session target: current-worker-session
Worker session profile: Implementation Worker
Phase: implementation
Task identity: CONTEXTDECK-CODE-HEALTH-REFACTORING-S7-DOCS
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to the exact current Worker session
Continuity anchor: terminal implementation report `02_report_00.md` for Worker
exchange `01` (S3+S5, accepted) written in this same session, and the accepted
plan report `01_report_01.md` corrected by `01_report_02.md`
Authority renewal: prior implementation authority expired at the S3+S5
terminal report; this prompt is a complete renewed implementation grant to the
same session
Reasoning recommendation: Medium
Reasoning basis: bounded documentation corrections using exact replacement text
from the accepted plan plus three repository evidence re-checks before any
correction is written; no design question and no runtime behavior.
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: documentation-only corrections inside the accepted E2
logical whole whose cumulative fresh independent acceptance still applies; the
slice itself is reversible and evidence-checked, with the full registered suite
as a no-code-change checkpoint and one normal non-force product commit and push.
Internal delegation: prohibited

# ContextDeck — implement S7: documentation accuracy

You are the WORKER session that implemented S3+S5. Native Plan Mode must be OFF
for this exchange. Do not use subagents.

This prompt grants one bounded repository-only implementation slice: correct the
three documentation files below with the exact replacement text, re-verify the
evidence that supports the corrections at the exact candidate first, create and
push one normal product commit, persist the terminal report in META, then stop.
You do not accept your own candidate and never close the logical whole.

Continuity and renewal: prior implementation authority expired at the S3+S5
terminal report. Retained context and this conversation are convenience and
evidence, not authority; re-verify repository and environment state before
acting and stop on any conflict with current repository evidence. Evidence
produced in this session is non-independent.

Critical: no live host mutation, no application launch, no KWin/OpenRGB/broker/
device operation, no desktop mutation, no service change, no packaging change,
no dependency change, and no suspend/DPMS behavior may occur during this
exchange. Broker and input-remapper paths are inspected as files only, never
executed or probed. This exchange edits, tests, commits, and pushes repository
content only.

Client note (not a product issue): if distro `cmake` fails with a `CMAKE_ROOT`
lookup error because the client injects bundled library paths, run the granted
`cmake`/`ctest` commands with a cleaned distro `PATH`. Do not record host-local
paths anywhere.

## Accepted plan and Plan-to-Execution transition

ORCHESTRATOR reconciliation: accepted
Accepted plan: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_01.md`
Accepted correction: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_02.md`

Prior slices S1, S2, S4, S6, S3, and S5 are reconciled and accepted as
implementation-PASS: public `main` =
`58a10bb71d697a48b5a94e63e5a8c0f9eacc4a9b`, with the parent chain through
`4ec3732...`, `a130b06...`, `1e7e9d5...`, `308aaa2...`, and `5b2b25b...`. This
prompt is the separate implementation grant for S7, the final implementation
slice; the cumulative fresh independent acceptance follows separately.

## Implementation Authority Record

Implementation authority: explicit
Exact baseline: `58a10bb71d697a48b5a94e63e5a8c0f9eacc4a9b`
Changed-path allowlist: `ROADMAP.md`; `README.md`; `docs/testing-m2.md`
Implementation boundaries: documentation corrections only, with the exact
replacement text below; no source, test, CMake, UI, ADR, operations, or other
documentation change; `AGENTS.md` access-profile lines and `ROADMAP.md` line 7
stay byte-identical; `docs/architecture.md` is not touched; no new claim
Independence required: no for this implementation slice; the cumulative fresh
independent acceptance for the whole is a later separate exchange

## Verified candidate and preflight gates

Canonical product repository: `https://github.com/cisarik/contextdesk`
Expected branch: `main`
Exact baseline HEAD: `58a10bb71d697a48b5a94e63e5a8c0f9eacc4a9b`
Required parent: `4ec37320d9d18b615b926d910af1e07a4a985a6d`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

This whole's trace destination:
`projects/contextdesk/00/06-code-health-and-refactoring/`
Report destination: `projects/contextdesk/00/06-code-health-and-refactoring/02_report_01.md`

Repository checkout topology: standalone product checkout on `main`
Working-copy topology: canonical product checkout
Topology rationale: one accountable Worker owns one coherent documentation
correction and one commit; `build/` is git-ignored

Execution route: this repository declares no `ap.project.conf` operation; the
exact `cmake` / `ctest` commands below are the project-owned commands from
`AGENTS.md` and `CMakeLists.txt`.

Before any mutation:

1. Verify the complete prompt, the exact current Worker session, Native Plan
   Mode OFF, coordinates `02/02`, the renewed authority, and no subagents.
2. Verify canonical remote, active `main`, exact HEAD, exact parent, clean
   state, no Git lock, matching AP gitlink/checkout, and `./.ap/ap doctor` PASS
   (variant `stable`).
3. Prove public product `main` equals the exact baseline with direct
   `git ls-remote`. Do not pull, merge, rebase, switch, reset, clean, stash, or
   retarget.
4. Verify META public `main` is
   `afad43dc202fc9782cca56b152c97e91eee7dd79` or a verified later descendant
   whose changed paths do not contradict this exchange.
5. Verify the trace directory is real and contains `00_handout.md`,
   `00_notes.md`, `01_planning_00.md`, `01_completion_01.md`,
   `01_planning_02.md`, the `01_report_01.md` through `01_report_05.md`
   reports, and `02_report_00.md`; the report destination `02_report_01.md`
   must be absent before the write.
6. Read the accepted plan report S7 section completely; read `ROADMAP.md`,
   `README.md`, and `docs/testing-m2.md` before editing; every needed path must
   be inside the allowlist.

## Evidence re-checks (required before writing any replacement)

Re-verify each claim at the exact baseline and record the exact evidence in the
report. If any claim is not supported, stop with `PARTIAL` and do not write the
corresponding replacement:

1. Sink write failures fail closed:
   `src/broker/ForwardingEngine.cpp` logs `sink-write-failed` and returns
   false; `tests/unit/test_broker_forwarding.cpp` exercises a failing sink.
2. Production ARM measures capabilities before virtual creation:
   `src/broker/Acquisition.cpp` computes the union of the two source
   capability sets and calls `applyMeasuredCapabilities` before
   `createVirtual`; `passthroughCapabilities()` in `src/broker/RealSink.cpp`
   is used only by `tests/unit/test_broker_production.cpp`.
3. logind session resolution:
   `src/broker/SessionIpc.cpp` uses `sd_pid_get_session` first and, on
   `-ENODATA`/`-ENXIO`/`-ENOENT`, enumerates `sd_uid_get_sessions` and accepts
   exactly one eligible active local seated graphical session; this matches
   `docs/architecture.md` around lines 210-218.
4. The live suspend/resume slice is Session 22: read the M2 trace
   `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/22_report_00.md`
   profile line and the `ROADMAP.md` G4 paragraph; cite the session number only
   if both agree.

## S7 corrections (exact replacement text)

### A. `ROADMAP.md` current-whole bullet

Replace this text:

```text
- Current whole: **M4 state and ledger reconciliation** — documentation-only
  reconciliation of the accepted M1–M4 state and disposition of the carried M4
  ledger candidates; no host, device, desktop, launch, broker, packaging, or
  license mutation. Ledger dispositions are recorded in the M4 backlog section.
```

with:

```text
- Closed documentation whole: **M4 state and ledger reconciliation** — accepted
  on `235d467...`; ledger dispositions recorded in the M4 backlog section.
- Current whole: **code health and refactoring** — behavior-preserving
  internal structure on the session app, core, receivers, and tests. No
  behavior, visuals, product-claim, or safety-boundary change. No host, device,
  desktop, launch, broker, packaging, or license mutation.
```

### B. `README.md` status block

Replace this sentence:

```text
M2 is parked with G3 host-mitigated on the authorized reference host; the current
bounded whole reconciles the accepted M1–M4 state and disposes of the carried
M4 ledger candidates.
```

with:

```text
M2 is parked with G3 host-mitigated on the authorized reference host. The M4
state and ledger reconciliation is closed on `235d467...`. The current bounded
whole is behavior-preserving code health and refactoring.
```

Leave the rest of the README status block, including the existing G4
remaining-work sentence, unchanged.

### C. `ROADMAP.md` sleep-hook bullet

In the suspend/resume hook bullet, replace:

```text
Not autostart. Not live suspend evidence. ADR 0001.
```

with:

```text
Not autostart. One named live suspend/resume slice is recorded (Session 22).
Hibernate and hybrid-sleep remain open. ADR 0001.
```

### D. `ROADMAP.md` production-safety paragraph

Replace:

```text
does not choose which remainder comes next. Production safety gaps already
visible in source (silent uinput write errors; virtual-device capabilities from
`passthroughCapabilities()` rather than measured source bits / LED return
path; logind `sd_pid_get_session` vs user-manager-launched session apps) stay
in that remainder unless a later prompt names them.
```

with:

```text
does not choose which remainder comes next. Previously listed source gaps are
addressed in tree: `ForwardingEngine` fails closed on `sink-write-failed`;
production ARM measures the live capability union and applies it before
virtual creation (`passthroughCapabilities()` is a test helper, not the ARM
path); `LogindSeatAuthorizer` uses `sd_pid_get_session` first and, on no
session, accepts exactly one eligible active local seated graphical session.
Those items are not remaining source defects. Remaining M2 work is still
production/autostart readiness (G8/M5), hibernate/hybrid-sleep, and general
input-remapper coexistence.
```

### E. `docs/testing-m2.md` opening remaining-G4 list

Replace:

```text
**Full G4 remains open:** LED-return
behavior, all-control fidelity, live host suspend/resume, input-remapper
coexistence beyond those samples, and production/autostart readiness.
```

with:

```text
**Full G4 remains open:** production/autostart readiness (G8/M5),
hibernate/hybrid-sleep, and general input-remapper coexistence. Named slices
from Workers 16, 19, 22, 23, and 24 are recorded as accepted and are not
rerun.
```

### F. `docs/testing-m2.md` closing remaining-claims paragraph

Replace:

```text
held modifier. Remaining G4 claims: LED return, all-control fidelity,
input-remapper coexistence beyond those samples, and live host suspend/resume.
Autostart (G8) stays forbidden until those pass.
```

with:

```text
held modifier, one live suspend/resume cycle, LED return and all-control
fidelity, and one bounded input-remapper mapping. Remaining G4 claims:
production/autostart readiness (G8/M5), hibernate/hybrid-sleep, and general
input-remapper coexistence. Autostart (G8) stays forbidden until those pass.
```

Do not change any other text, heading, or claim. In particular, do not claim
M2, G4, G3, M3, or M4 closure, production readiness, autostart safety, or
general input-remapper coexistence.

## Invariants (must hold exactly)

- The three changed files contain only the replacements above; every other byte
  is unchanged.
- `AGENTS.md` access-profile lines (`Access profile: **ChatOrchestrator** ...`)
  and `ROADMAP.md` line 7 stay byte-identical to the baseline.
- `docs/architecture.md` is not touched.
- No source, test, or CMake change; the full registered suite stays 21/21.
- No new claim about hardware, live behavior, closure, or readiness.

## Mandatory reading

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-12, RF-16, RF-18, RF-19,
  implementation authority, Git safety, validation, stopping conditions;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Implementation Authority
  Record, exchange/trace contract, validation ladder, delivery record,
  Session-and-Mode;
- the accepted plan report `01_report_01.md`, especially the S7 section, and
  the accepted revision report `01_report_02.md`;
- `ROADMAP.md`, `README.md`, `docs/testing-m2.md`;
- `docs/architecture.md` around lines 210-218 (read-only reference);
- `src/broker/ForwardingEngine.cpp`, `src/broker/Acquisition.cpp`,
  `src/broker/RealSink.cpp`, `src/broker/SessionIpc.cpp`,
  `tests/unit/test_broker_forwarding.cpp`, `tests/unit/test_broker_production.cpp`
  (read-only evidence);
- the M2 trace `22_report_00.md` profile line (read-only evidence);
- `AGENTS.md`.

## Product invariants

- G213 only; five RGB zones, never per-key.
- Session app never opens raw keyboard nodes; broker stays static/inactive; no
  grab, ARM, device probe, or input-remapper operation.
- Behavior preservation is the slice claim: documentation text changes only as
  specified.
- Repository documentation stays English, public-facing, and scannable.

## Commands and side-effect authority

Allowed: `git status`, `git log`, `git diff`, `git ls-remote`, `git rev-parse`,
`git show`, `grep`/`rg` for the evidence re-checks; `cmake -S . -B build -G
Ninja`; `cmake --build build`; `ctest --test-dir build --output-on-failure`;
exact-path `git add`, one `git commit`, one normal non-force `git push`, and
bounded public readback.

Forbidden: any `git add .`/`-A`, force push, history rewrite, reset, clean,
stash, checkout, switch, rebase, merge, tag, branch, remote, or config write;
any source, test, CMake, UI, ADR, operations, packaging, or dependency edit;
any service, host, desktop, device, broker, OpenRGB, KWin, or input-remapper
operation; any build or execution of broker or input-remapper paths.

Side effects: reversible local documentation edits inside the allowlist, build
outputs under the git-ignored `build/`, one local product commit, and one
normal non-force product push. No META Git mutation by the Worker.

No raw input, key names, serials, host addresses, passwords, private paths,
desktop names/IDs, window captions, or unredacted tool logs may appear in the
report or trace. Never paste ordinary typed text, key names, scan codes, raw
event payloads, or per-event timing into reports.

## Validation ladder

Validation ladder: selected
Inspection and provenance: required — the four evidence re-checks above, each
tied to the exact baseline
Existing focused tests: none for documentation; the suite is a no-code-change
checkpoint
Affected tests: none
New causal regression: none — documentation-only slice with exact replacement
text
Broad or full suite: required-because the checkpoint proves the docs commit did
not touch code; run the full registered suite before commit
Runtime or testbed: not-used
Independent acceptance: not-required for this slice; the whole receives one
cumulative fresh independent acceptance after this final implementation slice

Procedure:

1. Run the four evidence re-checks and record their exact results.
2. Apply only the six replacements above.
3. Run the full registered suite and require 21/21.
4. Inspect the diff: exactly three documentation files; verify the
   access-profile lines and `docs/architecture.md` are unchanged
   (`git diff --name-only` plus `git diff -- AGENTS.md docs/architecture.md`
   both empty).

A failed gate stops the exchange before commit. Classify a failure before any
repair; do not write an unverified claim.

## Git and public verification

1. Stage exactly `ROADMAP.md`, `README.md`, and `docs/testing-m2.md`; inspect
   the staged diff.
2. Create exactly one normal commit with subject:
   `Correct M2 source-gap docs and current-whole wording`
3. Before push, prove public `main` still equals the exact baseline with
   direct `git ls-remote`; on any mismatch, stop without pushing.
4. Push once, normal non-force, to `origin main`; verify local `HEAD`,
   remote-tracking state, and direct public `ls-remote` all equal the new
   commit; parent equals the exact baseline; changed paths are exactly the
   three allowlisted files.

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
Downloadable prompt filename: 02_implementation_01.md
Destination path: projects/contextdesk/00/06-code-health-and-refactoring/
Report filename: 02_report_01.md
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
- changed files and purpose, one line per replacement A–F;
- the four evidence re-checks with their exact findings;
- tests and validation, including the full-suite result and the unchanged-path
  checks;
- commit and push result plus direct public-ref verification;
- deviations, risks, or missing evidence;
- exactly one smallest next step: ORCHESTRATOR reconciliation and, if accepted,
  the cumulative fresh independent acceptance exchange;
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
acceptance has happened; no claim that the META trace privacy correction has
been performed (that is a COOPERATOR decision and action).

## Stop conditions

Stop and report `BLOCKED` before mutation if: the session is not the healthy
continuation session, Native Plan Mode is on, coordinates or authority are
contradictory, product/AP/META identity fails, the worktree has unexplained
changes, the trace path collides or is unsafe, the accepted plan is unreadable,
or the task would need a non-allowlisted path, a dependency change, private
data, host/device access, or subagents.

Stop with `PARTIAL` without committing when an evidence re-check fails or a
replacement cannot be applied exactly as specified, and name the exact
obstacle. Do not widen the allowlist and do not write an unverified claim.

Stop with `PASS` only when the six replacements are applied exactly, the suite
passes 21/21, one normal non-force push is publicly verified, and the terminal
report is persisted and read back. Then submit the terminal report and do no
further work under this grant.

Authority for this Worker expires at this terminal report.
