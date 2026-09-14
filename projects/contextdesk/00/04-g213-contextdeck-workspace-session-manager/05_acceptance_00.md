Logical whole identity: g213-contextdeck-workspace-session-manager
Worker session ordinal: 05
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Acceptance Worker
Phase: acceptance
Task identity: CONTEXTDECK-M4-SLICE-A-SCOPED-REACCEPTANCE
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to a genuinely fresh independent Worker session
Reasoning recommendation: Maximum (COOPERATOR-selected; ORCHESTRATOR recommended High)
Reasoning basis: independent scoped re-acceptance must confirm the correction
closes the A7 diagnostics-privacy finding meaningfully, changed no production
file, and leaves the previously accepted rows valid; the departure to the client
maximum/enhanced mode is an accepted COOPERATOR decision and does not change any
authority boundary
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E3
Internal delegation: prohibited

# ContextDeck M4 Slice A — scoped fresh independent code re-acceptance

You are a genuinely fresh independent WORKER. You did not plan, implement,
repair, accept, or report any part of this candidate and did not participate in
M1/M2/M3. You receive only this complete prompt. Native Plan Mode must be OFF.
Do not use subagents.

The original M4 Slice A candidate `c7c8eb9…` returned an independent `PARTIAL`
in `03_report_00.md`: A1–A6 and A8 passed, and A7 failed only because the
required durable diagnostics-privacy regression was absent. A bounded corrector
then published exactly one direct-child commit `aca6c68…` that adds one test
file and changes no production, build, schema, resolver, receiver, controller,
UI, or documentation path. Because the correction changes no semantic owner,
validator semantics, runtime behavior, independence assumption, authority
routing, or security boundary, AP permits a **scoped** re-acceptance. This
session is that scoped re-acceptance.

Perform one read-only independent scoped re-acceptance of the immutable public
corrected candidate. Treat the implementation, acceptance, and correction
reports as claims, not as acceptance evidence. Inspect and test independently,
persist one terminal report, and stop. You have no correction, product
publication, host, desktop, launch, or device authority.

## Acceptance and Correction Record

Acceptance candidate: `aca6c68542bbc9f1b8ee891415a04b0a95e8372e`
Acceptance owner map: accepted M4 plan in `01_report_00.md`, completed by `01_report_01.md`; implementation under `02_implementation_00.md`; independent PARTIAL in `03_report_00.md` (A7 missing diagnostics-privacy regression); bounded test-only correction under `04_correction_00.md`
Acceptance allowlist: read-only inspection of the exact candidate, the cumulative 28 changed product paths between `502ae75…` and `aca6c68…`, directly referenced unchanged owner paths, pinned AP, and the public M4 continuity records named below
Acceptance scope: scoped to the correction delta and its effect on the prior verdict. Confirm the A7 finding is closed meaningfully, that no production file changed between the prior candidate and this candidate, that the focused and full suites pass, and that the previously accepted A1–A6/A8 rows remain valid because their code is byte-identical to the already-reviewed candidate
Acceptance risk claims: the new regression is present, registered, non-vacuous, and privacy-tight; the corrected candidate introduces no runtime, schema, resolver, receiver, controller, UI, validator, or security change; scoped re-acceptance is valid
Acceptance control matrix: S1 through S4 below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: scoped
Named missing-evidence probe: none at issuance; classify any discovered missing evidence in the report
Out-of-scope observations: ledger-candidates only

Implementation authority: none
Product mutation allowlist: empty
META Git mutation authority: none
Temporary probe authority: bounded as specified below
Independence required: yes

## Immutable public identities

Canonical product: `https://github.com/cisarik/contextdesk`
Required public branch: `main`
Candidate and required public `main`:
`aca6c68542bbc9f1b8ee891415a04b0a95e8372e`
Required candidate parent and prior reviewed candidate:
`c7c8eb90d31947bc32c498691ec926885f43cb64`
Required prior candidate parent (original baseline):
`502ae75571358ec95d33c836084b5e2253850731`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

Canonical META: `https://github.com/cisarik/meta.git`
Required public META baseline:
`f64c63487e2f55bda78976678ffd759dfb475e6a`
Required correction-pair parent:
`06439c943d196c336e3997ecf079a31e3cb8b639`
Required M4 trace:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/`

Required implementation prompt SHA-256:
`b8fa2a274185c1bf784d444f50935fb82dd199e3b638ba7e3a0e736773469d38`
Required implementation report SHA-256:
`7570ee7999e684bb037fed63c7a2edc79f15fde1f2afe3a44ae1f2d69d7f8ce6`
Required prior acceptance report SHA-256:
`8dce3dc3f98848c230c75b9e9f004430be78253b1c60aea60de01e043ba0c3d3`
Required correction prompt SHA-256:
`2e75ad46f995e83e8313580fd7d6c0693a8e52640a6b08cd1e659df72c359d9f`
Required correction report SHA-256:
`2498af6f0f3b47181b121608623b44c5506b3c77d2c418913ce29e02dd475b13`

No alternate commit, mirror, stale remote-tracking ref, or local retained clone
may substitute for these identities. If public `main` has moved, stop before
testing and report the exact discrepancy; do not silently retarget.

## Read-only preflight

Use fresh disposable inspection clones in the Worker container, never a
COOPERATOR checkout. Before substantive acceptance:

1. Verify this is a genuinely fresh session with no implementation ancestry,
   Native Plan Mode OFF, exact 05/01 coordinates, and no subagents.
2. Clone the canonical product with submodules and META over HTTPS. Fetch
   `main`, compare direct `git ls-remote` with the required public tips, and
   detach at the exact required commits.
3. If transport or cache state is stale, discard only the Worker-owned clone
   and retry the canonical HTTPS remote in a new disposable location. A safe
   retry may use `git -c http.version=HTTP/1.1`. Do not change host DNS or Git
   configuration and do not use credentials or a mirror.
4. Verify clean worktrees, candidate parent, candidate subject, exact AP
   gitlink and checkout, and `./.ap/ap doctor` PASS (variant `stable`).
5. Verify META ancestry: `06439c9` adds the `03` pair, `f64c634` adds the `04`
   pair, byte identity of prompt/report hashes above, and no changed earlier
   accepted-plan/completion artifact.
6. Verify the correction commit `aca6c68` changes exactly one path,
   `tests/unit/test_workspace_lighting.cpp`, and the cumulative candidate set is
   exactly the 28 paths listed below.
7. Verify existing required build tools and `dbus-run-session`. Install nothing.

Use detached read-only source inspection. Put all build products outside the
product checkout in a newly created Worker-owned temporary directory. The
product worktree must remain clean throughout.

## Mandatory reading

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-07, RF-12, RF-18, RF-19,
  acceptance/correction and escalation, phase-qualified results, stopping;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Acceptance and Correction
  Record, Phase Result and Closure Record, external trace, report expiry;
- `.ap/INFOSEC.md` only as advisory defensive review guidance;
- product `AGENTS.md`, `README.md`, `ROADMAP.md`, `docs/specification.md`,
  `docs/architecture.md`, `docs/operations.md`, `docs/testing-m4.md`, and
  `docs/adr/`;
- the complete public M4 artifacts `01_planning_00.md`, `01_report_00.md`,
  `01_completion_01.md`, `01_report_01.md`, `02_implementation_00.md`,
  `02_report_00.md`, `03_acceptance_00.md`, `03_report_00.md`,
  `04_correction_00.md`, and `04_report_00.md`;
- `tests/unit/test_workspace_lighting.cpp`, `src/app/AppController.{h,cpp}`, and
  any unchanged adjacent owner needed to judge diagnostics privacy.

## Continuity and product invariants

Use this exact M3 park wording wherever M3 state is restated:

> M3 workspace-aware lighting is code-accepted on `502ae75...`; its physical
> five-zone IRL observation is deferred by explicit COOPERATOR decision. M3 is
> not closed, and code acceptance is not physical acceptance.

Use this exact M2 park wording wherever M2 state is restated:

> The named live G4 slices are accepted, but the M2 logical whole remains open.
> M2 is parked with G3 host-mitigated on the authorized reference host; the
> next bounded whole is M4 workspace session manager.

Preserve these limits while reviewing:

- Logitech G213 Prodigy only, USB `046d:c336`; five RGB zones, never per-key.
- Session app observes virtual desktops directly and never opens raw input.
- Broker stays static/inactive: no LEASE, ARM, grab, pass-through, or capture.
- Captions, titles, desktop names, and desktop UUIDs are sensitive: never logged
  or persisted; no secrets or private paths in the report or META.
- Slice A is observational: no live desktop mutation, launch, placement, or
  `kwinrulesrc` write.

This acceptance does not cover M2/G4 closure, physical visibility, M3 closure,
deployment, autostart, hibernate/hybrid sleep, M4 Slice B behavior, remapping,
a deck layer, M5 integration, production packaging, or general coexistence.

## Cumulative candidate changed paths

The cumulative candidate `502ae75…` → `aca6c68…` must change only these 28
paths, and the correction commit `c7c8eb9…` → `aca6c68…` must change only
`tests/unit/test_workspace_lighting.cpp`:

```text
CMakeLists.txt
README.md
ROADMAP.md
docs/adr/0002-host-desktop-mutation-authority.md
docs/adr/0003-workspace-assignment-schema.md
docs/adr/0004-typed-application-launch.md
docs/adr/README.md
docs/architecture.md
docs/operations.md
docs/specification.md
docs/testing-m4.md
src/app/AppController.cpp
src/app/AppController.h
src/context/WorkspaceReceiver.cpp
src/core/Persistence.cpp
src/core/Resolver.cpp
src/core/Resolver.h
src/core/Types.h
src/workspace/WorkspacePlan.cpp
src/workspace/WorkspacePlan.h
tests/unit/test_profile_persistence.cpp
tests/unit/test_profile_resolver.cpp
tests/unit/test_workspace_lighting.cpp
tests/unit/test_workspace_plan.cpp
tests/unit/test_workspace_receiver.cpp
ui/ApplicationsPage.qml
ui/Main.qml
ui/WorkspacePage.qml
```

This is an inspection scope, not mutation authority.

## Scoped acceptance matrix

Return one independent scoped verdict on whether the correction closes the A7
finding meaningfully and leaves the prior verdict valid. Mark every row `PASS`,
`FAIL`, or `NOT TESTED`, with direct evidence.

### S1 — Identity, provenance, and correction scope

- exact product/AP/META public identities and ancestry;
- correction commit changes exactly `tests/unit/test_workspace_lighting.cpp`,
  `+115/-0`, with no production, build, schema, resolver, receiver, controller,
  UI, documentation, or dependency path;
- cumulative candidate set is exactly the 28 paths above;
- `git diff --quiet c7c8eb9 aca6c68 -- <every non-test path>` is empty, proving
  the previously accepted A1–A6/A8 code is byte-identical to the reviewed
  candidate.

### S2 — Finding closure and regression meaningfulness

- the new test `diagnosticsOmitWorkspacePrivacySentinels` exists in
  `tests/unit/test_workspace_lighting.cpp`, inside the existing registered
  `test_workspace_lighting` target, with no new file/target/dependency;
- it genuinely seeds a workspace session with a user-authored desktop name and
  an application profile with title fallback enabled and a user-authored
  pattern, and asserts that sensitive state was actually established;
- it reads `AppController::diagnostics()` and asserts no key or value contains
  the seeded sentinels and no pattern/caption/desktop-name/desktop-UUID key
  category appears;
- independently judge whether the test is non-vacuous: confirm it would fail if
  a sentinel were placed into the diagnostics map under a recognized key, and
  assess the corrector's stated LEAD limitation (an unrecognized alias carrying
  a live value). State whether that limitation blocks scoped acceptance.

### S3 — No-regression validation

- focused `test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_plan|test_openrgb_protocol`
  and the full registered CTest suite pass from the detached corrected
  candidate, with counts from actual output;
- receiver/UI tests still run through the private `dbus-run-session` fake and no
  real KWin/OpenRGB/broker/device/host operation occurs;
- no previously passing behavior regressed.

### S4 — Scoped-acceptance validity and bounded claims

- confirm that no semantic owner, validator semantics, runtime behavior,
  independence assumption, authority routing, or security boundary changed, so
  scoped re-acceptance is the correct route rather than full-fresh;
- confirm the changed test and documentation do not overclaim acceptance and the
  M2/M3 park wording is preserved;
- confirm no Slice B, live desktop, launch, or physical behavior is claimed.

Acceptance-PASS requires S1–S4 PASS and the mandatory lead resolved. A confirmed
runtime/semantic change, a vacuous or absent regression, a required-suite
failure, or an unresolved material discrepancy prohibits acceptance-PASS.

## Mandatory adversarial lead

### Lead L1 — non-vacuous privacy regression under an alias

Independently confirm or disprove that `diagnosticsOmitWorkspacePrivacySentinels`
cannot pass vacuously: that the seeded document is actually loaded and the
sensitive state established (verified by explicit assertions), that the
key-normalization check is neither so permissive that a real leak key would be
missed nor so strict that it always fails, and that the test genuinely inspects
the diagnostics map. Assess whether a future leak under an unrecognized key
alias carrying a live caption/UUID (the corrector's stated residual) is a
blocking gap for Slice A code acceptance or an acceptable scoped residual.
Report `confirmed`, `disproved`, or `unresolved`, with exact code/test evidence
and consequence.

## Allowed validation

Use only existing tools. Run from the exact detached candidate with the build
directory outside the checkout:

```sh
env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH cmake -S . -B <owned-temp>/build -G Ninja
env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH cmake --build <owned-temp>/build

env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH \
  ctest --test-dir <owned-temp>/build --output-on-failure \
  -R '^(test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_plan|test_openrgb_protocol)$'

env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH \
  ctest --test-dir <owned-temp>/build --output-on-failure

git diff --check 502ae75571358ec95d33c836084b5e2253850731..aca6c68542bbc9f1b8ee891415a04b0a95e8372e
git diff --name-only c7c8eb90d31947bc32c498691ec926885f43cb64..aca6c68542bbc9f1b8ee891415a04b0a95e8372e
git status --short
```

Record real counts and the first causal failure. Do not weaken, skip, or loop
tests to manufacture green output.

If L1 cannot be settled statically and the existing toolchain suffices, you may
create one minimal synthetic mutation only in a separate Worker-owned disposable
copy outside the canonical product checkout, to confirm the test would fail on a
planted leak. It must not become a product or META diff, and the owned temporary
copy must be deleted after evidence is captured. Report the probe design, result,
and cleanup without exposing a private absolute path.

## Forbidden actions

- no product or AP edits, patches, staging, commit, push, branch switch, reset,
  clean, stash, rebase, merge, ref/tag/remote/config change, or force operation;
- no META history/ref mutation and no edits outside the exact prompt/report
  trace paths;
- no package installation, sudo, service management, udev, input-remapper,
  OpenRGB process, broker start/connect/ARM, KWin session-bus probe, power
  action, device open/probe/grab, application launch, desktop mutation, or host
  configuration;
- no secrets, credentials, host identifiers, or private paths in the report;
- no implementation, correction, speculative redesign, M2/M3 reopening,
  physical acceptance, deployment, or closure.

## Verdict rules

- `status: PASS` and `Phase-qualified result: acceptance-PASS` only when the
  independence gate, S1–S4, the mandatory lead, focused tests, full suite,
  cleanliness, and public identity all pass with no blocking defect;
- `status: PARTIAL` and `Phase-qualified result: not-applicable` when the review
  completes but finds or leaves unresolved a candidate defect or required
  evidence gap; identify the smallest correction boundary without implementing
  it;
- `status: BLOCKED` and `Phase-qualified result: not-applicable` when a
  prerequisite prevents a meaningful decision.

A negative verdict is useful evidence but is not acceptance-PASS.

## Exact META trace persistence

External trace disposition: configured
Trace discovery: META README and exact M4 trace
Trace project key: contextdesk
Trace logical-whole projection identity: 04-g213-contextdeck-workspace-session-manager
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Downloadable prompt filename: `05_acceptance_00.md`
Destination:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/05_acceptance_00.md`
Report filename: `05_report_00.md`
Report destination:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/05_report_00.md`
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
META Git publication owner: COOPERATOR
Archival: wait-for-report

The ORCHESTRATOR persists this exact prompt bytes to its destination before
delivery. Verify byte identity and read it back completely. At the end, write
and completely read back the terminal report. The WORKER may prepare only the
report file and may not stage, commit, push, pull, merge, rebase, switch, or
alter META history. The COOPERATOR archives the exact pair together afterward.

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo the opening persistent-role and three coordinate fields exactly once with
values unchanged. Include:

- status and phase-qualified result under the verdict rules;
- exactly one `Report justification: final-acceptance`;
- fresh-session independence evidence and `Primary fresh acceptances used`;
- product candidate/parent, AP pin/doctor, META identity, direct public refs,
  ancestry, cumulative and correction changed paths, prompt/report hashes, and
  clean states;
- an S1–S4 matrix with `PASS`, `FAIL`, or `NOT TESTED`, evidence, and blocking
  classification;
- L1 as `confirmed`, `disproved`, or `unresolved`, with exact evidence and
  consequence;
- focused/full validation commands, exit results, actual test counts, private
  bus classification, and any first causal failure;
- temporary-probe identity, design, result, and cleanup, or `not-used`;
- confirmed defects, missing persistent tests, disproved concerns, residual
  risks, deviations, and out-of-scope ledger candidates;
- `Resolved Execution Issues / Near-Misses` and
  `Pre-Existing Failure Classification`, each truthfully populated or `none`;
- exact META prompt/report persistence and complete-readback evidence, while
  stating META Git publication remains COOPERATOR-owned;
- one smallest next step: ORCHESTRATOR reconciliation; if PASS, name only the
  separately authorized Slice B or COOPERATOR-owned decision as not yet granted;
  if non-PASS, name one bounded correction without granting it;
- compact `Orchestration critique` with `MEASURED:` and `LEAD:`;
- exactly one `Logical-whole closure: not-closed` line;
- the exact authority-expiry sentence below.

Explicitly state that code acceptance is not live desktop or physical acceptance
and does not prove M2/G4 closure, M3 closure, deployment, production readiness,
G3 re-audit, autostart, hibernate/hybrid sleep, general input-remapper
coexistence, M4 Slice B behavior, M5 behavior, per-key RGB, or measured
control-to-zone placement.

Authority for this Worker expires at this terminal report.

## Fail-closed stop conditions

Stop before substantive review on non-fresh or inherited implementation context,
Native Plan Mode mismatch, coordinate/authority contradiction,
identity/public-ref/ancestry/hash failure, dirty or unsafe checkout, prompt
collision, required tool absence, or need for product, host, device, secret, or
subagent authority.

During review, preserve the first causal failure. Continue read-only inspection
only when safe and useful to bound the verdict; never correct the candidate or
expand the task. A confirmed blocking defect or required-evidence gap yields a
truthful `PARTIAL`, not an improvised patch.

Stop immediately after the terminal report. Do not implement a correction, start
Slice B, deploy, reopen M2/M3, or begin another M4 phase.
