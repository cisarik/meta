Logical whole identity: g213-contextdeck-workspace-session-manager
Worker session ordinal: 10
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Acceptance Worker
Phase: acceptance
Task identity: CONTEXTDECK-M4-SLICE-B-FULL-REACCEPTANCE
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to a genuinely fresh independent Worker session
Reasoning recommendation: Maximum (COOPERATOR-selected; ORCHESTRATOR recommended High)
Reasoning basis: full independent re-acceptance must reconcile the corrected
fail-closed desktop mutation step and checkpoint path against the full Slice B
contract, plus the prior non-blocking late-dispatch residual; the departure to
the client maximum/enhanced mode is an accepted COOPERATOR decision and does not
change any authority boundary
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E3
Internal delegation: prohibited

# ContextDeck M4 Slice B — full fresh independent code re-acceptance after correction

You are a genuinely fresh independent WORKER. You did not plan, implement,
repair, accept, or report any part of M4 and did not participate in M1/M2/M3.
You receive only this complete prompt. Native Plan Mode must be OFF. Do not use
subagents.

The original Slice B candidate `5087277…` returned an independent `PARTIAL` in
`08_report_00.md`: A1 and A3–A7 PASS, A2 failed because the optional `current`
step was not fail-closed, and A8 failed on a stale documentation row and a
checkpoint path one directory too high. A bounded corrector then published one
direct-child commit `db9ddc1…` that changed runtime behavior in the mutation
executor and the checkpoint location and updated the documentation. Because the
correction changes runtime behavior, AP requires a **full fresh A1–A8
re-acceptance**, not a scoped re-check. This session is that re-acceptance.

Perform one read-only independent acceptance of the immutable public corrected
candidate. Treat the implementation, acceptance, and correction reports as
claims. Inspect and test independently, persist one terminal report, and stop.
You have no correction, product publication, host, desktop, launch, or device
authority.

## Acceptance and Correction Record

Acceptance candidate: `db9ddc1f923f44e26f7f1d58df7446306bbdf64a`
Acceptance owner map: accepted M4 plan in `01_report_00.md` completed by `01_report_01.md`; Slice A implementation `02_implementation_00.md`/`02_report_00.md` accepted via `05_report_00.md`; Slice B preflight `06_report_00.md` (PASS); Slice B implementation `07_implementation_00.md`/`07_report_00.md`; Slice B independent PARTIAL `08_report_00.md` (A2 current-step gating, A8 documentation/path); bounded correction `09_correction_00.md`/`09_report_00.md`
Acceptance allowlist: read-only inspection of the exact candidate, the cumulative 35 changed product paths between `aca6c68…` and `db9ddc1…`, directly referenced unchanged owner paths, pinned AP, and the public M4 continuity records named below
Acceptance risk claims: corrected fail-closed `current` step; checkpoint placed in the product directory; corrected documentation; and the previously accepted Slice B claims (default/opt-in mutation split and ordering, checkpoint/revert ownership, in-transaction trigger classification, typed launcher, identity-wins placement, live-caption privacy)
Acceptance control matrix: A1 through A8 below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1 (this session is the required full-fresh correction re-acceptance)
Automatic corrections used: 1
Correction re-acceptance: full-fresh
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
`db9ddc1f923f44e26f7f1d58df7446306bbdf64a`
Required candidate parent and prior reviewed candidate:
`50872779c619a97be061d7f0df414ccae6bde7e6`
Required original Slice B baseline:
`aca6c68542bbc9f1b8ee891415a04b0a95e8372e`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

Canonical META: `https://github.com/cisarik/meta.git`
Required public META baseline:
`cfd5cee1298b76ad21afd685de9565c8191d6f7b` (a later verified descendant is acceptable only after ancestry and changed-path review proves no M4 artifact changed)
Required M4 trace:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/`

Required implementation prompt SHA-256:
`48d20c7be5f0a95555fc4b61abe58e4f146adad1867df5f56a03b76ad758ed48`
Required implementation report SHA-256:
`910ff7432bea944cce7473e30f2ed66c3fabc48b6cca9dc3d9692fd6d0cc8c93`
Required prior acceptance report SHA-256:
`010fc3e4ba1c864453b2ee0125de2c4946640e08426ba941fb0794d09a098521`
Required correction prompt SHA-256:
`0dc9958cee0ac5dece9581be1c0613d930b469c3af183043f7430bcc3aa8b903`
Required correction report SHA-256:
`1f61475821f9603bc3f4ca40c516c6a843819a159025d4b2a49679e402168b8b`

No alternate commit, mirror, stale remote-tracking ref, or local retained clone
may substitute for these identities. If public product `main` has moved, stop
before testing and report the exact discrepancy; do not silently retarget.

## Read-only preflight

Use fresh disposable inspection clones in the Worker container, never a
COOPERATOR checkout. Before substantive acceptance:

1. Verify this is a genuinely fresh session with no implementation ancestry,
   Native Plan Mode OFF, exact 10/01 coordinates, and no subagents.
2. Clone the canonical product with submodules and META over HTTPS. Fetch `main`,
   compare direct `git ls-remote` with the required public tips, and detach at
   the exact required commits.
3. If transport or cache state is stale, discard only the Worker-owned clone and
   retry the canonical HTTPS remote in a new disposable location; a safe retry
   may use `git -c http.version=HTTP/1.1`. Do not change host DNS or Git config
   and do not use credentials or a mirror.
4. Verify clean worktrees, candidate parent, candidate subject, exact AP gitlink
   and checkout, and `./.ap/ap doctor` PASS (variant `stable`).
5. Verify META ancestry, the correction pair's changed paths, all required prompt
   and report hashes above with complete readback, and no changed earlier
   accepted-plan artifact.
6. Verify the candidate changed exactly the cumulative 35 paths listed below,
   and the correction commit `db9ddc1…` changed exactly five paths relative to
   `5087277…`: `docs/specification.md`, `src/app/AppController.cpp`,
   `src/workspace/DesktopMutator.cpp`, `tests/unit/test_workspace_lighting.cpp`,
   `tests/unit/test_workspace_mutator.cpp`.
7. Verify existing required build tools, `dbus-run-session`, and the
   `KF6Service`/`KF6KIO` packages. Install nothing.

Use detached read-only source inspection. Put all build products outside the
product checkout in a newly created Worker-owned temporary directory.

## Mandatory reading

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-07, RF-12, RF-16, RF-18, RF-19,
  acceptance/correction and escalation, phase-qualified results, stopping;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Acceptance and Correction
  Record, Phase Result and Closure Record, exchange/trace, report expiry;
- `.ap/INFOSEC.md` only as advisory defensive review guidance;
- product `AGENTS.md`, `README.md`, `ROADMAP.md`, `docs/specification.md`,
  `docs/architecture.md`, `docs/operations.md`, `docs/testing-m4.md`,
  `docs/adr/0002-*`, `docs/adr/0004-*`;
- the complete public M4 artifacts `01_report_00.md`, `01_report_01.md`,
  `02_implementation_00.md`, `02_report_00.md`, `03_report_00.md`,
  `04_correction_00.md`, `04_report_00.md`, `05_report_00.md`, `06_report_00.md`,
  `07_implementation_00.md`, `07_report_00.md`, `08_report_00.md`,
  `09_correction_00.md`, `09_report_00.md`;
- the complete candidate diff and every changed product file;
- unchanged adjacent owners as needed: `src/core/Types.h`,
  `src/core/Persistence.{h,cpp}`, `src/context/DBusNames.h`,
  `src/app/SessionApplication.{h,cpp}`, `src/app/main.cpp`, `src/rgb/*`,
  `CMakeLists.txt`.

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

- G213 only, USB `046d:c336`; five RGB zones, never per-key.
- Session app never opens raw keyboard nodes; broker stays static/inactive.
- Event-driven KWin identity; no `xdotool`/`wmctrl`/`xprop`; no title polling.
- Typed launch only; no shell, no `QProcess` of `Exec=`, no `systemd-run`, no
  `kstart`.
- Captions, titles, desktop names, and desktop UUIDs are sensitive: never logged
  or persisted in diagnostics, prompts, reports, or META.
- `kwinrulesrc` is never written; no autostart; no M5 scope.

This acceptance does not cover M2/G4 closure, M3 closure, physical or live
desktop/launch/placement behavior, deployment, autostart, hibernate/hybrid
sleep, general input-remapper coexistence, remapping, deck, M5, or per-key RGB.

## Cumulative candidate changed paths

The cumulative candidate `aca6c68…` → `db9ddc1…` must change only these 35
paths:

```text
CMakeLists.txt
README.md
ROADMAP.md
docs/adr/0002-host-desktop-mutation-authority.md
docs/adr/0004-typed-application-launch.md
docs/architecture.md
docs/operations.md
docs/specification.md
docs/testing-m4.md
kwin/contextdeck-bridge/contents/code/main.js
kwin/contextdeck-bridge/metadata.json
src/app/AppController.cpp
src/app/AppController.h
src/context/ContextReceiver.cpp
src/context/ContextReceiver.h
src/context/WorkspaceReceiver.cpp
src/context/WorkspaceReceiver.h
src/workspace/ApplicationLauncher.cpp
src/workspace/ApplicationLauncher.h
src/workspace/DesktopMutator.cpp
src/workspace/DesktopMutator.h
src/workspace/PlacementResolver.cpp
src/workspace/PlacementResolver.h
src/workspace/WorkspaceCheckpoint.cpp
src/workspace/WorkspaceCheckpoint.h
src/workspace/WorkspacePlan.cpp
src/workspace/WorkspacePlan.h
tests/unit/test_application_launcher.cpp
tests/unit/test_placement_resolver.cpp
tests/unit/test_workspace_lighting.cpp
tests/unit/test_workspace_mutator.cpp
tests/unit/test_workspace_receiver.cpp
ui/ApplicationsPage.qml
ui/DiagnosticsPage.qml
ui/WorkspacePage.qml
```

This is an inspection scope, not mutation authority.

## Measurable outcome and acceptance matrix

Return one independent verdict on whether the exact public corrected candidate
satisfies the accepted M4 Slice B code contract and is fit to proceed to a
separate COOPERATOR-owned live IRL run. Mark every row `PASS`, `FAIL`, or
`NOT TESTED`, with direct evidence.

### A1 — Identity, provenance, and scope

- exact product/AP/META public identities and ancestry;
- prompt/report byte hashes, correction commit scope (exactly five paths), and
  cumulative 35-path set equality;
- clean read-only checkouts; no scope escape or extra dependency.

### A2 — Desktop mutation executor, default/opt-in split, and fail-closed `current`

- default Apply is exactly trailing `createDesktop` ascending, conditional
  `setDesktopName` by ordinal, and `rows`/wrapping only on a non-empty diff;
- `removeDesktop` and the optional `current` switch are opt-in only and never
  drift-triggered;
- **the corrected `current` step is fail-closed**: a failed or timed-out
  `Properties.Set` and a missing target stop the sequence and run the revert
  path, never reaching opted-in removals or the launch phase; confirm the fix
  and its regression;
- ordering/step gating correct; no mutation on `currentChanged` or user-created
  desktop changes; no polling; no `kwinrulesrc`.

### A3 — Checkpoint, revert, and stop rules

- checkpoint path is now the product directory
  (`<config root>/contextdeck/workspace-checkpoint.json`), user-local, never the
  profile document/logs/META; atomic `QSaveFile`, user-only permissions,
  overwrite per Apply, write-and-verify before the first mutation; confirm the
  path regression is real and the docs match the code;
- revert removes exactly the UUIDs this Apply created; names/rows/wrapping
  restored; `current`-restore skip residual preserved; no application kill; no
  open-window move;
- fail-closed preconditions and checkpoint lifecycle preserved.

### A4 — In-transaction launch trigger classification

- in-transaction `desktopCreated` distinguished from user-created desktops
  without a second `GetAll` or polling; only the in-transaction event and
  explicit Apply launch; created UUID recorded; no desktop identity logged.

### A5 — Typed launcher

- only a validated `.desktop` id; shell/`QProcess`/`systemd-run`/`kstart`
  rejected; `KService`/`ApplicationLauncherJob` used; test seam prevents real
  launches; skip/debounce/bounded-retry semantics implemented and tested.

### A6 — Placement, bridge, and live-caption privacy

- identity-wins placement, fallback only when both flags, empty-id no-op,
  maximize selection, management/observation gating;
- `PlacementHint` and `TitleHint` wired as specified; `ContextReport` six input
  arguments unchanged; captions bounded, consumed once, discarded, never logged;
  privacy guard non-vacuous;
- KWin `callDBus` trailing-callback reply form confirmed; `metadata.json` valid.

### A7 — Causal regression evidence

- inspect test bodies, not names or counts; map every required behavior to a
  persistent causal regression, including the two new correction regressions;
- confirm private-bus isolation and that no real launch/KWin/device occurs;
- focused (including `test_workspace_lighting` and `test_workspace_mutator`) and
  full registered suites pass from the detached candidate with actual counts;
- missing coverage required by the contract is a defect.

### A8 — Documentation and bounded claims

- the corrected `Plochy` row and checkpoint path match the code; specification,
  architecture, operations, testing-m4, and ADRs are truthful;
- candidate described only as an implementation candidate; M2/M3 park wording
  preserved; no physical/deployment/production/autostart/M5/per-key/whole-G4
  claim.

Acceptance-PASS requires all A1–A8 PASS and both leads resolved.

## Two mandatory adversarial leads

### Lead L1 — corrected fail-closed `current` and the empty-snapshot abort

Independently confirm that after the correction a failed/timed-out `current`
`Properties.Set` and a missing target both stop and run the revert path without
reaching removals or launch, and that the new regression is causal (would fail
on the un-fixed parent). Then assess the correction report's LEAD: an
`Available` observation with no ordinal-1 desktop (empty snapshot) now aborts
the whole transaction as `current-target-missing` when the user opted in to
switch. Determine whether that abort is acceptable fail-closed behavior or
whether an earlier controller-level precondition refusal would be preferable,
and whether either choice is a blocking gap. Report `confirmed`, `disproved`, or
`unresolved` with exact evidence and consequence.

### Lead L2 — checkpoint path, revert ownership, and late-dispatch residual

Confirm the checkpoint is written to the product directory (not the bare config
root), that the path regression would fail on the un-fixed parent, and that
revert can never remove a desktop this Apply did not create. Reconfirm the prior
non-blocking residual: if KWin delivers `desktopCreated` after the method reply,
the created UUID may be absent from the checkpoint and a later revert could
under-remove that desktop (safe direction, disclosed). State whether any of this
blocks acceptance. Report `confirmed`, `disproved`, or `unresolved`.

## Allowed validation

Use only existing tools. Run from the exact detached candidate with the build
directory outside the checkout:

```sh
env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH cmake -S . -B <owned-temp>/build -G Ninja
env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH cmake --build <owned-temp>/build

env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH \
  ctest --test-dir <owned-temp>/build --output-on-failure \
  -R '^(test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_plan|test_openrgb_protocol|test_workspace_mutator|test_placement_resolver|test_application_launcher|test_workspace_lighting)$'

env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH \
  ctest --test-dir <owned-temp>/build --output-on-failure

git diff --check aca6c68542bbc9f1b8ee891415a04b0a95e8372e..db9ddc1f923f44e26f7f1d58df7446306bbdf64a
git diff --name-only 50872779c619a97be061d7f0df414ccae6bde7e6..db9ddc1f923f44e26f7f1d58df7446306bbdf64a
git status --short
```

Record real counts and the first causal failure. Do not weaken, skip, or loop
tests to manufacture green output.

If a lead cannot be settled statically and the existing toolchain suffices, you
may create one minimal synthetic test only in a separate Worker-owned disposable
copy outside the canonical product checkout, using only candidate dependencies
and synthetic data. It must not become a product or META diff; delete the copy
after evidence capture. Report the probe design, result, and cleanup without a
private path.

## Forbidden actions

- no product or AP edits, patches, staging, commit, push, branch switch, reset,
  clean, stash, rebase, merge, ref/tag/remote/config change, or force operation;
- no META history/ref mutation and no edits outside the exact prompt/report
  trace paths;
- no package installation, sudo, service management, udev, input-remapper,
  OpenRGB process, broker start/connect/ARM, KWin session-bus probe, power
  action, device open/probe/grab, application launch, desktop mutation, bridge
  reload, or host configuration;
- no secrets, credentials, host identifiers, or private paths in the report;
- no implementation, correction, speculative redesign, M2/M3 reopening,
  physical acceptance, deployment, or closure.

## Verdict rules

- `status: PASS` and `Phase-qualified result: acceptance-PASS` only when the
  independence gate, A1–A8, both leads, focused tests, full suite, cleanliness,
  and public identity all pass with no blocking defect or missing evidence;
- `status: PARTIAL` / `not-applicable` when a candidate defect or required
  evidence gap remains; name the smallest correction boundary without
  implementing it;
- `status: BLOCKED` / `not-applicable` when a prerequisite prevents a meaningful
  decision.

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

Downloadable prompt filename: `10_acceptance_00.md`
Destination:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/10_acceptance_00.md`
Report filename: `10_report_00.md`
Report destination:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/10_report_00.md`
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
META Git publication owner: COOPERATOR
Archival: wait-for-report

The ORCHESTRATOR persists this exact prompt bytes before delivery; verify byte
identity and read it back completely. At the end write and completely read back
the terminal report. The WORKER may prepare only the report file and may not
mutate META Git. The COOPERATOR archives the exact pair afterward.

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo the opening persistent-role and three coordinate fields exactly once with
values unchanged. Include:

- status and phase-qualified result under the verdict rules;
- exactly one `Report justification: final-acceptance`;
- fresh-session independence evidence and `Primary fresh acceptances used`;
- product candidate/parent, correction scope, AP pin/doctor, META identity,
  direct public refs, ancestry, changed paths, prompt/report hashes, and clean
  states;
- an A1–A8 matrix with `PASS`, `FAIL`, or `NOT TESTED`, evidence, and blocking
  classification;
- L1 and L2 as `confirmed`, `disproved`, or `unresolved`, with exact evidence and
  consequence;
- focused/full validation commands, exit results, actual test counts, private
  bus classification, and any first causal failure;
- the KWin `callDBus` reply-form confirmation;
- temporary-probe identity, design, result, and cleanup, or `not-used`;
- confirmed defects, missing persistent tests, disproved concerns, residual
  risks, deviations, and out-of-scope ledger candidates;
- `Resolved Execution Issues / Near-Misses` and
  `Pre-Existing Failure Classification`, each truthfully populated or `none`;
- exact META prompt/report persistence and readback, with META Git publication
  remaining COOPERATOR-owned;
- one smallest next step: ORCHESTRATOR reconciliation; if PASS, name only the
  separate COOPERATOR-owned live IRL run as not yet granted; if non-PASS, name
  one bounded correction without granting it;
- compact `Orchestration critique` with `MEASURED:` and `LEAD:`;
- exactly one `Logical-whole closure: not-closed` line;
- the exact authority-expiry sentence below.

Explicitly state that code acceptance is not live desktop or physical acceptance
and does not prove M2/G4 closure, M3 closure, deployment, production readiness,
G3 re-audit, autostart, hibernate/hybrid sleep, general input-remapper
coexistence, live desktop/launch/placement behavior, M5 behavior, per-key RGB,
or measured control-to-zone placement.

Authority for this Worker expires at this terminal report.

## Fail-closed stop conditions

Stop before substantive review on non-fresh or inherited implementation context,
Native Plan Mode mismatch, coordinate/authority contradiction,
identity/public-ref/ancestry/hash failure, dirty or unsafe checkout, prompt
collision, required tool/package absence, or need for product, host, device,
secret, or subagent authority.

During review preserve the first causal failure; never correct the candidate or
expand the task. A confirmed blocking defect yields a truthful `PARTIAL`.

Stop immediately after the terminal report. Do not implement a correction, start
a live IRL run, reload the bridge, deploy, reopen M2/M3, or begin another M4
phase.
