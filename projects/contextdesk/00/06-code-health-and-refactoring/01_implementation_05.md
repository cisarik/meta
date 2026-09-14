Logical whole identity: code-health-and-refactoring
Worker session ordinal: 01
Worker exchange ordinal: 06
Persistent role identity: WORKER
Worker session target: current-worker-session
Worker session profile: Implementation Worker
Phase: implementation
Task identity: CONTEXTDECK-CODE-HEALTH-REFACTORING-S4-S6
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to the exact current Worker session
Continuity anchor: terminal implementation report `01_report_04.md` for Worker
exchange `05` (S2 Persistence split, accepted) and the accepted plan report
`01_report_01.md` corrected by `01_report_02.md` — all written in this same
session
Authority renewal: prior implementation authority expired at the S2 terminal
report; this prompt is a complete renewed implementation grant to the same
session
Reasoning recommendation: Medium
Reasoning basis: two coherent mechanical extractions inside accepted
boundaries (a pure D-Bus codec plus a pure payload parser, then a shared test
helper) with the receiver tests and the full registered suite as the gate; no
open design question and no behavior change.
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: cross-cutting reversible source and test refactoring under
one cumulative fresh independent acceptance later in this logical whole; this
exchange is mechanical and reversible with the receiver, lighting, and full
suites as the behavior gate and two normal non-force product commits and
pushes.
Internal delegation: prohibited

# ContextDeck — implement S4 and S6: codecs and shared test helper

You are the WORKER session that implemented S1 and S2. Native Plan Mode must
be OFF for this exchange. Do not use subagents.

This prompt grants one bounded repository-only implementation task with two
coherent commits: first S4 (extract the Workspace state codec and the inventory
payload parser), then S6 (extract the shared virtual-desktop test helper).
Validate each commit against the exact baseline, push both normally, persist
one terminal report in META, then stop. You do not accept your own candidate
and never close the logical whole.

Continuity and renewal: prior implementation authority expired at the S2
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
(the corrected S4 ContextReceiver extraction target; use the corrected text,
not the original wording)

S1 and S2 are reconciled and accepted as implementation-PASS: public `main` =
`308aaa267e02c4ba77ddd9b8782a97482184e020`, parent `5b2b25b...`, allowlists
exact, full registered suite 21/21 from each candidate. This prompt is the next
separate implementation grant; the plan and reports supply no execution
authority by themselves.

## Implementation Authority Record

Implementation authority: explicit
Exact baseline: `308aaa267e02c4ba77ddd9b8782a97482184e020`
Changed-path allowlist: `src/context/WorkspaceReceiver.{h,cpp}`;
`src/context/WorkspaceStateCodec.{h,cpp}` (new);
`src/context/InventoryPayload.{h,cpp}` (new);
`src/context/ContextReceiver.cpp`; `CMakeLists.txt` (`contextdeck_context`
sources and the test-target include directory for the shared helper);
`tests/support/FakeVirtualDesktopMap.h` (new);
`tests/unit/test_workspace_receiver.cpp`;
`tests/unit/test_workspace_lighting.cpp`
Implementation boundaries: two coherent commits (S4, then S6); no behavior,
public API, log message, IPC, schema, QML, or broker change; no new `add_test`
name; `src/context/ContextReceiver.h` unchanged
Independence required: no for this implementation slice; the cumulative fresh
independent acceptance for the whole is a later separate exchange

## Verified candidate and preflight gates

Canonical product repository: `https://github.com/cisarik/contextdesk`
Expected branch: `main`
Exact baseline HEAD: `308aaa267e02c4ba77ddd9b8782a97482184e020`
Required parent: `5b2b25bc64c86f1ea568d82b94da2b3271b10c85`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

This whole's trace destination:
`projects/contextdesk/00/06-code-health-and-refactoring/`
Accepted plan report: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_01.md`
Accepted revision report: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_02.md`
Report destination: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_05.md`

Repository checkout topology: standalone product checkout on `main`
Working-copy topology: canonical product checkout
Topology rationale: one accountable Worker owns two tightly related
extractions and two commits; `build/` is git-ignored

Execution route: this repository declares no `ap.project.conf` operation; the
exact `cmake` / `ctest` commands below are the project-owned build and test
commands from `AGENTS.md` and `CMakeLists.txt`.

Before any mutation:

1. Verify the complete prompt, the exact current Worker session, Native Plan
   Mode OFF, coordinates `01/06`, the renewed authority, and no subagents.
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
   `01_planning_02.md`, `01_report_01.md`, `01_report_02.md`,
   `01_report_03.md`, and `01_report_04.md`; the report destination
   `01_report_05.md` must be absent before the write.
6. Read the accepted plan report S4/S6 sections and the revision report's
   corrected S4 subsection completely; read the files before editing; every
   needed path must be inside the allowlist.

## S4 scope (corrected extraction anchors)

### WorkspaceStateCodec

Move into `src/context/WorkspaceStateCodec.{h,cpp}`:

- `WorkspaceReceiver::decodeSnapshot` — the function body from line 577 through
  its closing brace at line 771 (the frozen interval ends at the brace, not at
  the `startDeadline` declaration that follows);
- the pure decode helpers of the same translation unit:
  `hasControlCharacters` (79–87), `boundedUtf8` (89–92), `decodePosition`
  (94–116), `decodeDesktopStructure` (118–130), `unwrapDbusVariant` (132–142),
  `decodeGetAllProperties` (144–171), `decodeCount` (173–…).

Lifecycle (subscribe, owner resolution, coalescing, request ownership,
deadlines, recovery) stays in `WorkspaceReceiver`. `decodeSnapshot` may remain
a thin wrapper that delegates to the codec. The helpers are also used from
lifecycle code (approximately 399–420 and 518); the split must keep those
call sites working with identical semantics.

### InventoryPayload

Extract the pure payload parse of `ContextReceiver::onInventoryReport`
(lines 557–614 at the baseline) into `src/context/InventoryPayload.{h,cpp}`
with exactly this public shape:

```cpp
namespace contextdeck {
[[nodiscard]] std::optional<QVector<InventoryEntry>>
parseInventoryPayload(const QString &payloadJson);
}
```

Semantics that must be preserved exactly:

- the same accepted and rejected inputs; `std::nullopt` means reject and the
  receiver returns without changing `m_inventory`; a `QVector` (including
  empty) means accept;
- the same rejection log messages, level, and category (`qCWarning(lcContext)`):
  `rejected inventory: invalid JSON`, `rejected inventory: entries array
  required`, `rejected inventory: unknown semantic field`, `rejected inventory:
  more than 200 entries`, `rejected inventory: entry must be an object`,
  `rejected inventory: unknown identity field`, `rejected inventory: identity
  field too long`, `rejected inventory: more than 200 unique entries`;
- the same bounds (`kMaxInventoryEntries`, `kMaxDbusStringBytes`), dedup via
  `InventoryEntry::identityKey()`, and unique-count bound;
- no `kMaxInventoryBytes` check is added (the constant exists but is not used
  by this path today);
- empty-payload handling unchanged.

The receiver keeps sequence acceptance (551–556), the heartbeat timestamp, the
`m_inventory` comparison, `std::move`, `bumpPolicy()`, `emit inventoryChanged()`,
and the `qCInfo` apply log (616–621); the info log stays in the receiver.

### S4 allowlist and tests

Allowlist: the paths named in the Implementation Authority Record. In
`tests/unit/test_workspace_receiver.cpp` you may add codec-focused slots that
feed `QVariantMap` inputs directly (no fake manager dependency); do not add a
new registered test name. `src/context/ContextReceiver.h` must remain
unchanged.

## S6 scope (second commit, same exchange)

Do not merge the two `FakeDesktopManager` classes: the receiver fake covers
GetAll/hold/malformed replies and the lighting fake covers
`Set`/`createDesktop`/`setDesktopName` with a different introspection. Extract
only the shared pieces into a new header-only helper:

- `tests/support/FakeVirtualDesktopMap.h` — `DesktopTuple`, the D-Bus stream
  operators, and the GetAll map builder;
- both test classes remain and call the helper; do not split the large test
  executables (Qt `QTEST_MAIN` keeps one name per executable);
- add the include directory to the test targets that need it in `CMakeLists.txt`.

Focused evidence for S6: `test_workspace_receiver` and
`test_workspace_lighting` must pass after the extraction.

## Invariants (must hold exactly)

- Receiver lifecycle, coalescing, deadlines, request ownership, and recovery
  semantics unchanged; receiver signals and public API unchanged.
- Inventory parser semantics and log strings unchanged.
- No IPC/wire, persisted schema, QML, or user-visible string change.
- The 21 registered test names and their COMMAND spellings stay unchanged.
- No new dependency; no `src/broker/` change; no UI change.
- `build/` stays git-ignored.

## Mandatory reading

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-12, RF-16, RF-18, RF-19,
  implementation authority, Git safety, validation, stopping conditions;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Implementation Authority
  Record, exchange/trace contract, validation ladder, delivery record,
  Session-and-Mode;
- the accepted plan report `01_report_01.md` S4/S6 sections;
- the accepted revision report `01_report_02.md` corrected S4 subsection;
- `src/context/WorkspaceReceiver.{h,cpp}`, `src/context/ContextReceiver.{h,cpp}`,
  `src/context/DBusNames.h`;
- `tests/unit/test_workspace_receiver.cpp`,
  `tests/unit/test_workspace_lighting.cpp`, `CMakeLists.txt`;
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
`ctest --test-dir build --output-on-failure`; exact-path `git add`, two
`git commit`s, two normal non-force `git push`es, and bounded public readback.

Forbidden: any `git add .`/`-A`, force push, history rewrite, reset, clean,
stash, checkout, switch, rebase, merge, tag, branch, remote, or config write;
any other source, test, UI, documentation, packaging, or dependency edit; any
service, host, desktop, device, broker, OpenRGB, KWin, or input-remapper
operation.

Side effects: reversible local source/test edits inside the allowlist, build
outputs under the git-ignored `build/`, two local product commits, and two
normal non-force product pushes. No META Git mutation by the Worker.

No raw input, key names, serials, host addresses, passwords, private paths,
desktop names/IDs, window captions, or unredacted tool logs may appear in the
report or trace.

## Validation ladder

Validation ladder: selected
Inspection and provenance: required — read the files before editing and anchor
every extraction to the baseline lines above
Existing focused tests: `test_workspace_receiver` (under `dbus-run-session`),
`test_workspace_lighting`, plus new codec-focused slots in the receiver test
Affected tests: `test_workspace_receiver`, `test_workspace_lighting`, and every
target linking `contextdeck_context`
New causal regression: the codec slots are the named addition — they close the
gap that the pure codec previously could not be tested without the D-Bus fake
manager; no new registered name
Broad or full suite: required-because behavior preservation of the whole
logical whole is the named decision risk; run the full registered suite after
each commit
Runtime or testbed: not-used
Independent acceptance: not-required for this slice; the whole receives one
cumulative fresh independent acceptance after later slices

Procedure per commit:

1. Confirm the starting green state for the affected tests.
2. Apply only the allowlisted edits for that commit.
3. Reconfigure and rebuild; run the affected focused tests, then the full suite
   and require 21/21.
4. Inspect the diff: only allowlisted paths for that commit.

A failed gate stops that commit before commit/push. Classify a failure before
any repair; do not rerun an unchanged broad gate; do not weaken the environment.

## Git and public verification

Commit 1 (S4):

1. Stage exactly the S4 paths; inspect the staged diff.
2. Create exactly one normal commit with subject:
   `Extract WorkspaceStateCodec and inventory payload parser`
3. Before push, prove public `main` still equals the exact baseline with
   direct `git ls-remote`; on any mismatch, stop without pushing.
4. Push once, normal non-force, to `origin main`; verify local `HEAD`,
   remote-tracking state, and direct public `ls-remote` all equal the new
   commit; parent equals the exact baseline; changed paths are exactly the S4
   allowlist.

Commit 2 (S6):

5. Stage exactly the S6 paths; inspect the staged diff.
6. Create exactly one normal commit with subject:
   `Share FakeVirtualDesktopMap test helper`
7. Before push, prove public `main` equals commit 1 with direct
   `git ls-remote`; then push once, normal non-force; verify local `HEAD`,
   remote-tracking state, and direct public `ls-remote` all equal commit 2;
   parent equals commit 1; changed paths are exactly the S6 allowlist.

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
Downloadable prompt filename: 01_implementation_05.md
Destination path: projects/contextdesk/00/06-code-health-and-refactoring/
Report filename: 01_report_05.md
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
- changed files and purpose for both commits;
- tests and validation, including the new codec slots, focused tests, and the
  full-suite result after each commit;
- commit and push results plus direct public-ref verification for both commits;
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

Explicit non-claims: no acceptance-PASS, publication-PASS beyond the two pushed
commits, deployment-PASS, production readiness, M2/G4/G3 closure, autostart,
hibernate/hybrid sleep, input-remapper coexistence, M3/M4 closure or physical
behavior, M5, remapping, deck layer, per-key RGB, license selection, or
hardware acceptance; no claim that the cumulative behavior-preservation
acceptance has happened; no claim that refactoring beyond these slices is
complete; no claim that the META trace privacy correction has been performed
(that is a COOPERATOR decision and action).

## Stop conditions

Stop and report `BLOCKED` before mutation if: the session is not the healthy
continuation session, Native Plan Mode is on, coordinates or authority are
contradictory, product/AP/META identity fails, the worktree has unexplained
changes, the trace path collides or is unsafe, the accepted plan is unreadable,
or the task would need a non-allowlisted path, a dependency change, private
data, host/device access, or subagents.

Stop with `PARTIAL` without committing the affected commit when an extraction
would change a receiver semantic, a log string, a declaration, or a
serialization observable, and name the exact obstacle. Do not widen the
allowlist.

Stop with `PASS` only when both commits are pushed and publicly verified, the
focused tests and the full suite pass after each commit, and the terminal
report is persisted and read back. Then submit the terminal report and do no
further work under this grant.

Authority for this Worker expires at this terminal report.
