Logical whole identity: code-health-and-refactoring
Worker session ordinal: 03
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: CONTEXTDECK-CODE-HEALTH-REFACTORING-CUMULATIVE-ACCEPTANCE
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to a genuinely fresh Worker session
Reasoning recommendation: High
Reasoning basis: cumulative independent acceptance of a cross-cutting
behavior-preserving refactor across 39 changed paths; the central risk claim
(no observable change) is broad and must be falsified adversarially, not
confirmed by rerunning the suite alone. Medium cannot settle the moved-code
equivalence and facade-surface claims with the required confidence.
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: cross-cutting reversible source, test, and documentation
refactoring whose cumulative behavior-preservation claim requires this separate
fresh independent acceptance; no production, durable-data, security-boundary,
host, device, or broker-semantics change is claimed.
Internal delegation: prohibited

# ContextDeck — cumulative fresh independent acceptance

You are a genuinely fresh WORKER assigned only to independent acceptance. You
did not participate in the planning or in any implementation or correction of
this logical whole, and you inherit no authority from any previous session. Your
own work here is independent only if you establish repository and environment
evidence yourself and audit adversarially. Native Plan Mode must be OFF. Do not
use subagents.

This is a read-only acceptance grant. You mutate nothing in the product
repository, run no host, desktop, device, broker, KWin, OpenRGB, or
input-remapper operation, and start no application. Your only write is the
terminal report in META. You do not correct findings and never close the
logical whole.

## Acceptance and Correction Record

Acceptance candidate: `ba87ba08c17ad965d008c4fc1d59f42a7c7700c9`
Acceptance owner map: the accepted plan's slice ownership — build/test
infrastructure (S1); core persistence codecs (S2); context receivers and pure
codecs (S4); shared test helper (S6); application facade and units (S3, S5);
documentation accuracy (S7)
Acceptance allowlist: the exact 39 paths changed across
`235d467c752958694dad4be7bcc31e66406dbdcc..ba87ba08c17ad965d008c4fc1d59f42a7c7700c9`
listed in this prompt
Acceptance risk claims: (1) no observable change to behavior, user-visible
strings, signals, properties, QML bindings, IPC/wire formats, persisted
schemas, or log events; (2) the full registered suite passes from the exact
candidate; (3) every slice stayed inside its allowlist; (4) the access-profile
lines, `docs/architecture.md`, `ui/*`, and `src/broker/IpcProtocol.*` are
unchanged
Acceptance control matrix: the checks and probes below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates

## Verified candidate and preflight gates

Canonical product repository: `https://github.com/cisarik/contextdesk`
Expected branch: `main`
Exact candidate: `ba87ba08c17ad965d008c4fc1d59f42a7c7700c9`
Required parent: `58a10bb71d697a48b5a94e63e5a8c0f9eacc4a9b`
Whole baseline for comparison: `235d467c752958694dad4be7bcc31e66406dbdcc`
Full parent chain to verify:
`235d467` -> `5b2b25b` -> `308aaa2` -> `1e7e9d5` -> `a130b06` -> `4ec3732`
-> `58a10bb` -> `ba87ba0`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

This whole's trace destination:
`projects/contextdesk/00/06-code-health-and-refactoring/`
Accepted plan report: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_01.md`
Accepted revision report: `projects/contextdesk/00/06-code-health-and-refactoring/01_report_02.md`
Report destination: `projects/contextdesk/00/06-code-health-and-refactoring/03_report_00.md`

Working-copy topology: fresh disposable clone of the exact candidate, detached
at the candidate commit (for the suite, comparison reads, and probes); the
COOPERATOR-owned canonical checkout may be inspected read-only only if the
clone is insufficient, and must not be mutated.
Topology rationale: independence and exact-candidate evidence without touching
the canonical worktree.

Execution route: this repository declares no `ap.project.conf` operation; the
exact `cmake` / `ctest` commands below are the project-owned build and test
commands from `AGENTS.md` and `CMakeLists.txt`.

Before any audit work:

1. Verify the complete prompt, the intended fresh Worker session, Native Plan
   Mode OFF, coordinates `03/01`, and no subagents.
2. Verify the trace directory exists and contains `00_handout.md`,
   `00_notes.md`, `01_planning_00.md`, `01_completion_01.md`,
   `01_planning_02.md`, the `01_report_01.md` through `01_report_05.md`
   reports, `02_report_00.md`, and `02_report_01.md`; the report destination
   `03_report_00.md` must be absent before the write.
3. Prove public product `main` equals the exact candidate with direct
   `git ls-remote`, and the parent chain above with a fresh clone or read-only
   fetch.
4. Verify the prepared prompt file
   `projects/contextdesk/00/06-code-health-and-refactoring/03_acceptance_00.md`
   exists and is byte-identical to the received prompt; read it back
   completely. Stop on a non-identical or unsafe collision.
5. Read the accepted plan report and the revision report completely; treat all
   implementation reports as claims, not proof.

## Control matrix (each item must be independently established)

1. Public `main` = exact candidate; candidate parent = exact parent; the seven
   commits after the whole baseline exist with the subjects claimed by the
   implementation reports.
2. Fresh clone, detached at the candidate, worktree clean; AP gitlink and
   checkout `0cf2cff...`; `./.ap/ap doctor` PASS with variant `stable`.
3. `git diff --name-status 235d467..ba87ba0` equals exactly these 39 paths and
   nothing else:
   `CMakeLists.txt`, `README.md`, `ROADMAP.md`, `cmake/contextdeck-tests.cmake`,
   `docs/testing-m2.md`, `src/app/AppController.{h,cpp}`,
   `src/app/LightingEdit.{h,cpp}`,
   `src/app/PresentationModel.{h,cpp}`,
   `src/app/ProfileDocumentEditor.{h,cpp}`,
   `src/app/WorkspaceApplyController.{h,cpp}`,
   `src/app/WorkspaceSessionEditor.{h,cpp}`,
   `src/context/ContextReceiver.cpp`,
   `src/context/InventoryPayload.{h,cpp}`,
   `src/context/WorkspaceReceiver.cpp`,
   `src/context/WorkspaceStateCodec.{h,cpp}`,
   `src/core/Persistence.cpp`,
   `src/core/persistence/DocumentCodec.{h,cpp}`,
   `src/core/persistence/JsonCommon.{h,cpp}`,
   `src/core/persistence/KeysJson.{h,cpp}`,
   `src/core/persistence/LightingJson.{h,cpp}`,
   `src/core/persistence/MatchJson.{h,cpp}`,
   `src/core/persistence/WorkspaceJson.{h,cpp}`,
   `tests/support/FakeVirtualDesktopMap.h`,
   `tests/unit/test_workspace_lighting.cpp`,
   `tests/unit/test_workspace_receiver.cpp`.
   No `ui/`, `src/broker/`, `packaging/`, `.ap/`, `AGENTS.md`,
   `docs/architecture.md`, `LICENSE`, or dependency path may appear.
4. Build and run the full registered suite from the candidate clone:
   `cmake -S . -B build -G Ninja`; `cmake --build build`;
   `ctest --test-dir build --output-on-failure` must be 21/21, and
   `ctest -N` must list exactly the 21 known registered names with their known
   COMMAND spellings.
5. `grep -rn remappingState src ui tests` returns no hit.
6. `git diff 235d467..ba87ba0 -- ui/` is empty; `sha256sum` of the nine
   `ui/*.qml` files equals the candidate's bytes (equivalently, the candidate
   and baseline files are byte-identical).
7. `git diff 235d467..ba87ba0 -- src/broker/IpcProtocol.h src/broker/IpcProtocol.cpp`
   is empty; `src/broker/` has no other change.
8. `sha256sum` of `src/core/Persistence.h` is identical at baseline and
   candidate (`1e37e82bc9125ed35af9d86bcd8b80792f6d6beb3bfe4f84009dfa874fcb14c1`).
9. `kSchemaVersion` is unchanged between baseline and candidate (compare the
   declaration and value), and the Persistence parse-error reason strings are
   unchanged (compare the string literals moved into the codec units against
   the baseline translation unit).
10. `git diff 235d467..ba87ba0 -- AGENTS.md docs/architecture.md` is empty;
    `ROADMAP.md` line 7 and the `AGENTS.md` access-profile lines are
    byte-identical to baseline.
11. Documentation anchors A–F from the accepted plan are present in
    `ROADMAP.md`, `README.md`, and `docs/testing-m2.md`, and the corrected text
    claims no M2/G4/G3/M3/M4 closure, production readiness, autostart safety,
    or general input-remapper coexistence.
12. Re-verify the four S7 evidence claims independently against the candidate:
    fail-closed `sink-write-failed`; measured capability union applied before
    virtual creation with `passthroughCapabilities()` test-only; logind
    `sd_pid_get_session`-first with the exactly-one eligible-session fallback
    matching `docs/architecture.md`; and Session 22 as the live
    suspend/resume slice in the M2 trace and `ROADMAP.md`.

## Adversarial probes (bounded, required)

P1. Moved-code equivalence. For each refactor slice, select a bounded sample of
the largest moved functions (at least two per unit: Persistence codecs,
WorkspaceStateCodec, InventoryPayload, AppController units) and compare their
baseline and candidate bodies after normalizing whitespace, includes,
namespace wrappers, and access qualifiers. Report any semantic difference as a
finding; a pure move with identical logic is PASS. Do not attempt to prove
global equivalence of every line; state the sample and its coverage.

P2. Facade surface equivalence. Extract the normalized `Q_PROPERTY`,
`Q_INVOKABLE`, and `signals:` declarations from `AppController.h` at baseline
and candidate; require that every baseline declaration is present and
byte-equivalent at candidate except the single `remappingState` removal. Then
spot-check at least five getters across at least three new units to confirm
they delegate without changing return expressions, defaults, or side effects.

P3. String and log inventory. Extract user-visible and log string literals from
the app implementation files at baseline and candidate (normalize includes and
new file boundaries); require that no baseline runtime string is missing and
that no new runtime string was added. Report any difference as a finding.

P4. Test-helper equivalence. For the shared `FakeVirtualDesktopMap` helper,
compare the extracted producers with the former inline implementations in both
test files (bounded textual comparison) and require behavioral equivalence of
the desktop maps, stream operators, and introspection; report any difference.

P5. Optional causal probe. If a control-matrix item leaves material
uncertainty, run one focused parent-overlay probe: build the baseline
`235d467` in a separate disposable directory, run one affected test, and
compare its behavior with the candidate's. Record the results; do not expand
into a second audit.

## Authority and side-effect boundary

Product source mutation: prohibited
Product Git mutation: prohibited
Product commit/push: prohibited
AP mutation/update: prohibited
Host mutation: prohibited
Desktop/service/device/broker/KWin/OpenRGB/input-remapper operation: prohibited
Application launch: prohibited (the QML runtime load is parked as an
out-of-scope observation; do not start `contextdeck` or any built binary)
Dependency installation/update: prohibited
Secrets/credentials/private data: prohibited
Network authority: reads from the two canonical HTTPS remotes and a clone of
the exact candidate only; no external research, no provider calls
Side effects: read-only inspection, disposable fresh clone and build outputs
under Worker-owned temporary paths, plus the exact report-file write below

Cleanup: if you created a disposable clone or build directory, name it exactly
and remove only that owned path at the end; report the cleanup outcome. A
cleanup failure is secondary evidence and must never overwrite a primary
result.

If distro `cmake` fails with a `CMAKE_ROOT` lookup error because the client
injects bundled library paths, run the granted `cmake`/`ctest` commands with a
cleaned distro `PATH`. Do not record host-local paths anywhere.

No raw input, key names, serials, host addresses, passwords, private paths,
desktop names/IDs, window captions, or unredacted tool logs may appear in the
report or trace.

## Mandatory reading

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-07, RF-12, RF-16, RF-18, RF-19,
  independent acceptance, validation, public verification, stopping conditions;
- `.ap/AP_WORKER.md`, especially the Fresh Independent Audit profile;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Acceptance and Correction
  Record, exchange/trace contract, validation ladder, delivery record,
  Session-and-Mode;
- the accepted plan report `01_report_01.md` (all slices, the control matrix,
  the risk register, the acceptance section) and the revision report
  `01_report_02.md`;
- the implementation reports `01_report_03.md`, `01_report_04.md`,
  `01_report_05.md`, `02_report_00.md`, `02_report_01.md` — as claims to test;
- the candidate files touched by the whole, plus `AGENTS.md`, `ui/*.qml`, and
  `docs/architecture.md` as read-only references.

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

It must echo the four opening identity fields (persistent role and the three
coordinates) exactly once, with their values unchanged.

Include:

- status: `PASS`, `PARTIAL`, or `BLOCKED`;
- phase-qualified result: `acceptance-PASS` or `not-applicable`;
- the exact candidate and every control-matrix item with its observed result;
- the adversarial probes P1–P4 (and P5 if used), with exact findings and
  coverage statements;
- discrepancies, disproven concerns, unresolved risks, and missing evidence;
- an explicit statement separating what you verified yourself from what you
  accepted only as a report claim;
- exactly one smallest next step: ORCHESTRATOR closure evaluation or one
  bounded correction if a concrete finding exists;
- exactly one `Report justification: final-acceptance`;
- `Resolved Execution Issues / Near-Misses: none` or a complete entry;
- `Pre-Existing Failure Classification: none` or a complete entry;
- compact critique:

  `Orchestration critique:`

  `MEASURED: none | <verified finding; evidence; effect; smallest correction>`

  `LEAD: none | <unverified possibility; cheapest useful check>`

- exactly one `Logical-whole closure: not-closed` line;
- the authority-expiry sentence below.

Explicit non-claims: no publication-PASS beyond verifying the candidate is the
public `main`; no deployment-PASS; no production readiness, M2/G4/G3 closure,
autostart, hibernate/hybrid-sleep, input-remapper coexistence, M3/M4 closure or
physical behavior, M5, remapping, deck layer, per-key RGB, license selection,
or hardware acceptance; no claim that QML runtime behavior was exercised; no
claim that the META trace privacy correction has been performed (that is a
COOPERATOR decision and action).

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
Downloadable prompt filename: 03_acceptance_00.md
Destination path: projects/contextdesk/00/06-code-health-and-refactoring/
Report filename: 03_report_00.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR for META; no product Git authority
Archival: wait-for-report

After the audit, write the complete terminal report first to the exact report
path, read it back completely, and verify the header, coordinates, content, and
filename. Do not overwrite a non-identical existing report. Do not stage,
commit, push, pull, merge, rebase, or otherwise mutate META Git history or refs.
If the exact META destination is not reachable from your environment, do not
write to any other path; state the exact limitation in the report body and
return the complete report through the client output so the COOPERATOR can
persist it exactly.

## Stop conditions

Stop and report `BLOCKED` before auditing if: the session is not genuinely
fresh, Native Plan Mode is on, coordinates or authority are contradictory,
product/AP identity fails, the candidate is not the public `main`, the parent
chain is broken, the trace path collides or is unsafe, or the audit would need
a prohibited mutation, application launch, private data, host/device access, or
subagents.

Stop with `PARTIAL` when the audit cannot establish a control-matrix item or a
probe, naming exactly what could not be established and what evidence would
close it. Do not correct anything and do not widen the audit.

Stop with `PASS` only when every control-matrix item and required probe is
established, the terminal report is persisted and read back, and no concrete
finding remains. Then submit the terminal report and do no further work under
this grant.

Authority for this Worker expires at this terminal report.
