Logical whole identity: g213-contextdeck-workspace-session-manager
Worker session ordinal: 08
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Acceptance Worker
Phase: acceptance
Task identity: CONTEXTDECK-M4-SLICE-B-CODE-ACCEPTANCE
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to a genuinely fresh independent Worker session
Reasoning recommendation: Maximum (COOPERATOR-selected; ORCHESTRATOR recommended High)
Reasoning basis: independent acceptance must reconcile a live-desktop mutation
transaction, checkpoint/revert ownership, an in-transaction compositor event
trigger, a typed KIO launcher, a compositor placement bridge, and a live-caption
privacy guard; the departure to the client maximum/enhanced mode is an accepted
COOPERATOR decision and does not change any authority boundary
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E3
Internal delegation: prohibited

# ContextDeck M4 Slice B — fresh independent code acceptance

You are a genuinely fresh independent WORKER. You did not plan, implement,
repair, accept, or report any part of M4 and did not participate in M1/M2/M3.
You receive only this complete prompt. Native Plan Mode must be OFF. Do not use
subagents.

Perform one read-only independent acceptance of the immutable public M4 Slice B
candidate. Treat the implementation report as a claim, not as acceptance
evidence. Inspect and test independently, persist one terminal report, and stop.
You have no correction, product publication, host, desktop, launch, or device
authority.

## Acceptance and Correction Record

Acceptance candidate: `50872779c619a97be061d7f0df414ccae6bde7e6`
Acceptance owner map: accepted M4 plan in `01_report_00.md` completed by `01_report_01.md`; Slice A implementation `02_implementation_00.md`/`02_report_00.md` accepted via `05_report_00.md`; Slice B preflight `06_report_00.md` (PASS); Slice B implementation `07_implementation_00.md`/`07_report_00.md`
Acceptance allowlist: read-only inspection of the exact candidate, the 35 changed product paths between `aca6c68…` and `5087277…`, directly referenced unchanged owner paths, pinned AP, and the public M4 continuity records named below
Acceptance risk claims: exact default/opt-in mutation split and ordering; checkpoint/revert ownership and stop rules; in-transaction `desktopCreated` trigger classification; typed launcher with test seam, debounce, and bounded retry; identity-wins placement through the bridge with no `kwinrulesrc`; live-caption privacy guard; truthful scope and documentation
Acceptance control matrix: A1 through A8 below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
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
`50872779c619a97be061d7f0df414ccae6bde7e6`
Required candidate parent (accepted Slice A candidate):
`aca6c68542bbc9f1b8ee891415a04b0a95e8372e`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

Canonical META: `https://github.com/cisarik/meta.git`
Required public META baseline:
`f4d2d37d5edc18570efd4af04c530a9527427bc5` (a later verified descendant is acceptable only after ancestry and changed-path review proves no M4 artifact changed)
Required M4 trace:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/`

Required implementation prompt SHA-256:
`48d20c7be5f0a95555fc4b61abe58e4f146adad1867df5f56a03b76ad758ed48`
Required implementation report SHA-256:
`910ff7432bea944cce7473e30f2ed66c3fabc48b6cca9dc3d9692fd6d0cc8c93`

Required implementation pair first-add commit:
the commit that adds exactly `07_implementation_00.md` and `07_report_00.md`
together (COOPERATOR-owned). If it is not yet public at review time, verify the
two files by path and SHA-256 and report the archival state truthfully without
retargeting. Earlier pair commits: `6f14316` (01 pair), `c7e1b73` (completion
pair), `640b65d` (02 pair), `06439c9` (03 pair), `f64c634` (04 pair), `977c841`
(05 pair), `6c1d6c6` (06 pair).

No alternate commit, mirror, stale remote-tracking ref, or local retained clone
may substitute for these identities. If public product `main` has moved, stop
before testing and report the exact discrepancy; do not silently retarget.

## Read-only preflight

Use fresh disposable inspection clones in the Worker container, never a
COOPERATOR checkout. Before substantive acceptance:

1. Verify this is a genuinely fresh session with no implementation ancestry,
   Native Plan Mode OFF, exact 08/01 coordinates, and no subagents.
2. Clone the canonical product with submodules and META over HTTPS. Fetch `main`,
   compare direct `git ls-remote` with the required public tips, and detach at
   the exact required commits.
3. If transport or cache state is stale, discard only the Worker-owned clone and
   retry the canonical HTTPS remote in a new disposable location. A safe retry
   may use `git -c http.version=HTTP/1.1`. Do not change host DNS or Git
   configuration and do not use credentials or a mirror.
4. Verify clean worktrees, candidate parent, candidate subject, exact AP gitlink
   and checkout, and `./.ap/ap doctor` PASS (variant `stable`).
5. Verify META ancestry, the implementation-pair changed paths, prompt/report
   hashes and complete readback, and no changed earlier accepted-plan artifact.
6. Verify the candidate changed exactly the 35 paths listed below and no `.ap`,
   broker, broker IPC, RGB transport, `ControlCatalog`, packaging, license,
   hardware-evidence, dependency-beyond-KF6, lockfile, generated, or host file.
7. Verify existing required build tools, `dbus-run-session`, and the
   `KF6Service`/`KF6KIO` packages. Install nothing.

Use detached read-only source inspection. Put all build products outside the
product checkout in a newly created Worker-owned temporary directory. The
product worktree must remain clean throughout.

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
  `07_implementation_00.md`, `07_report_00.md`;
- the complete candidate diff and every changed product file;
- unchanged adjacent owners needed to judge behavior: `src/core/Types.h`,
  `src/core/Persistence.{h,cpp}`, `src/context/DBusNames.h`,
  `src/app/SessionApplication.{h,cpp}`, `src/app/main.cpp`, `src/rgb/*`, and
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
sleep, general input-remapper coexistence, Slice A-only behavior regression
beyond the reviewed diff, remapping, deck, M5, or per-key RGB.

## Exact candidate changed paths

The candidate must have only these 35 changed paths relative to `aca6c68…`:

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

This is an inspection scope, not mutation authority. Any product change,
generated file inside the checkout, commit, branch/ref operation, or push is
forbidden.

## Measurable outcome and acceptance matrix

Return one independent verdict on whether the exact public candidate satisfies
the accepted M4 Slice B code contract and is fit to proceed to a separate
COOPERATOR-owned live IRL run. Mark every row `PASS`, `FAIL`, or `NOT TESTED`,
with direct evidence.

### A1 — Identity, provenance, and scope

- exact product/AP/META public identities and ancestry;
- prompt/report byte hashes and implementation-pair integrity;
- exact 35 changed paths and clean read-only checkouts;
- no scope escape: no `.ap`, broker, RGB transport, `ControlCatalog`, packaging,
  license, hardware, extra dependency, lockfile, or host change.

### A2 — Desktop mutation executor and default/opt-in split

- default Apply is exactly trailing `createDesktop` ascending, conditional
  `setDesktopName` by ordinal, and `rows`/wrapping only on a non-empty diff;
- `removeDesktop` and the optional `current` switch are never in the default
  path and require explicit opt-in; `removeDesktop` is never implicit or
  drift-triggered;
- ordering and step gating are correct; any D-Bus error or timeout stops the
  sequence;
- no mutation on `currentChanged` or on user-initiated desktop changes; no
  polling; the existing request-ownership discipline is preserved;
- no `kwinrulesrc` path exists.

### A3 — Checkpoint, revert, and stop rules

- checkpoint path is user-local, never the profile document/logs/META; atomic
  `QSaveFile`, user-only permissions, overwrite per Apply, write-and-verify
  before the first mutation;
- revert removes exactly the UUIDs this Apply created and never a desktop it did
  not create; names/rows/wrapping restored; `current` restore skipped when the
  UUID is absent with a bounded residual;
- assignment rebinding stays ordinal-based; checkpoint lifecycle (delete on
  successful revert, retain otherwise) is implemented;
- fail-closed preconditions include explicit Apply, management enabled, valid
  session, `Available` fresh observation, unchanged owner generation, unchanged
  live-preview fingerprint, verified checkpoint, and explicit option booleans;
- revert never kills an application and does not move already-open windows back.

### A4 — In-transaction launch trigger classification

- the event surface distinguishes an in-transaction `desktopCreated` from a
  user-created desktop without a second `GetAll` or polling, and without logging
  desktop identity;
- only the in-transaction event and explicit Apply launch; `currentChanged`,
  session-app start, Plasma login, and user-created desktops do not;
- the created UUID is recorded in the checkpoint.

### A5 — Typed launcher

- only a validated `.desktop` id is accepted; shell, `QProcess` of `Exec=`,
  `systemd-run`, and `kstart` are rejected by construction and by test;
- `KService`/`KApplicationTrader` + `KIO::ApplicationLauncherJob` are used;
- the test seam prevents any real launch in tests;
- skip-if-already-running, per-profile debounce, and one bounded retry semantics
  are implemented and tested.

### A6 — Placement, bridge, and live-caption privacy

- `PlacementResolver` implements identity-wins, fallback-only-when-both-flags,
  empty-id no-op, and maximize selection; gated on management enabled and an
  `Available` observation;
- `ContextReceiver.PlacementHint` returns `(desktop_id, maximize)`; the bridge
  sets `window.desktops` and calls `setMaximize(true, true)`; the existing
  `ContextReport` six input arguments are unchanged; empty id is a no-op;
- the bridge never sends captions; `TitleHint` is sent only when the flag is on,
  is bounded, consumed once, discarded, and never logged; the live-caption
  privacy guard test exists and is non-vacuous;
- the KWin `callDBus` trailing-callback reply form claim is independently
  confirmed from the installed KWin build or a bounded synthetic probe;
- `metadata.json` is valid JSON and matches the final bridge behavior.

### A7 — Causal regression evidence

- inspect test bodies, not names or aggregate counts;
- map every required behavior from A2–A6 to a persistent causal regression;
- confirm D-Bus tests use a fake private-bus service and the launcher uses only
  its seam; `dbus-run-session` isolation is real;
- missing persistent coverage required by the implementation prompt is an
  acceptance defect even if the current build is green;
- focused and complete registered CTest suites pass from the detached public
  candidate in the fresh external build directory, with the actual count.

### A8 — Documentation and bounded claims

- specification/architecture/operations/testing-m4 and ADRs match the code:
  mutation set, opt-in split, checkpoint/revert/stop, triggers, typed launch,
  placement, privacy, `kwinrulesrc` rejection, M4/M5 boundary;
- the candidate is described only as an implementation candidate; Slice B is not
  claimed as live-accepted;
- M2/M3 park wording preserved; no physical, deployment, production, autostart,
  M5, per-key, or whole-G4 claim.

Acceptance-PASS requires all A1–A8 PASS and both leads resolved. `NOT TESTED` on
a required row, a confirmed contract defect, inadequate required persistent
regression, or an unresolved material discrepancy prohibits acceptance-PASS.

## Two mandatory adversarial leads

These are unverified leads, not findings. Independently confirm or disprove each.

### Lead L1 — late in-transaction `desktopCreated` dispatch

The implementation report's own LEAD notes that the controller's in-transaction
launch classification depends on signal dispatch during the mutator's bounded
per-step waits, and that a KWin scheduling change could deliver
`desktopCreated` after the transaction flag drops. Trace the exact interleaving:
whether a create-triggered launch for a `would_launch` profile can be missed
while the explicit-Apply launch phase still covers it, whether the checkpoint
and trigger classification stay consistent, and whether the residual is bounded
and disclosed. Report whether this blocks acceptance.

### Lead L2 — revert over-removal and default-remove safety

Independently confirm that revert can never remove a desktop this Apply did not
create (including a user-created extra or a pre-existing desktop), that
`removeDesktop` is excluded from default Apply and gated behind explicit opt-in
plus a confirmation, and that a failed or partial revert preserves the
checkpoint and reports a bounded residual rather than guessing. Report whether
this blocks acceptance.

For each lead report `confirmed`, `disproved`, or `unresolved`, with exact
code/test evidence, behavioral consequence, and whether it blocks acceptance.

## Allowed validation

Use only existing tools. Run from the exact detached candidate with the build
directory outside the checkout:

```sh
env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH cmake -S . -B <owned-temp>/build -G Ninja
env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH cmake --build <owned-temp>/build

env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH \
  ctest --test-dir <owned-temp>/build --output-on-failure \
  -R '^(test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_plan|test_openrgb_protocol|test_workspace_mutator|test_placement_resolver|test_application_launcher)$'

env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH \
  ctest --test-dir <owned-temp>/build --output-on-failure

git diff --check aca6c68542bbc9f1b8ee891415a04b0a95e8372e..50872779c619a97be061d7f0df414ccae6bde7e6
git status --short
```

Record real counts and the first causal failure. Do not weaken, skip, or loop
tests to manufacture green output.

If a lead cannot be settled statically and the existing toolchain suffices, you
may create one minimal synthetic test only in a separate Worker-owned disposable
copy outside the canonical product checkout, using only candidate dependencies
and synthetic data. It must not become a product or META diff, and the owned
temporary copy must be deleted after evidence is captured. Report the probe
design, result, and cleanup without exposing a private path.

## Forbidden actions

- no product or AP edits, patches, staging, commit, push, branch switch, reset,
  clean, stash, rebase, merge, ref/tag/remote/config change, or force operation;
- no META history/ref mutation and no edits outside the exact prompt/report
  trace paths;
- no package installation, sudo, service management, udev, input-remapper,
  OpenRGB process, broker start/connect/ARM, KWin session-bus probe, power
  action, device open/probe/grab, application launch, desktop mutation, bridge
  reload, or host configuration;
- no real display/session application launch if it could contact real KWin,
  OpenRGB, broker, or hardware;
- no secrets, credentials, host identifiers, or private paths in the report;
- no implementation, correction, speculative redesign, M2/M3 reopening,
  physical acceptance, deployment, or closure.

No recovery route is needed because no live input or physical device operation
is authorized. Stop if any proposed validation would require one.

## Verdict rules

- `status: PASS` and `Phase-qualified result: acceptance-PASS` only when the
  independence gate, A1–A8, both leads, focused tests, full suite, cleanliness,
  and public identity all pass with no blocking defect or missing evidence;
- `status: PARTIAL` and `Phase-qualified result: not-applicable` when the review
  completes but finds or leaves unresolved a candidate defect or required
  evidence gap; identify the smallest correction boundary without implementing
  it;
- `status: BLOCKED` and `Phase-qualified result: not-applicable` when a
  prerequisite prevents a meaningful decision.

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

Downloadable prompt filename: `08_acceptance_00.md`
Destination:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/08_acceptance_00.md`
Report filename: `08_report_00.md`
Report destination:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/08_report_00.md`
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
META Git publication owner: COOPERATOR
Archival: wait-for-report

The ORCHESTRATOR persists this exact prompt bytes to its destination before
delivery. Verify byte identity and read it back completely. At the end, write
and completely read back the terminal report. The WORKER may prepare only the
report file and may not mutate META Git. The COOPERATOR archives the exact pair
afterward.

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo the opening persistent-role and three coordinate fields exactly once with
values unchanged. Include:

- status and phase-qualified result under the verdict rules;
- exactly one `Report justification: final-acceptance`;
- fresh-session independence evidence and `Primary fresh acceptances used`;
- product candidate/parent, AP pin/doctor, META identity, direct public refs,
  ancestry, changed paths, prompt/report hashes, and clean states;
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
- exact META prompt/report persistence and complete-readback evidence, while
  stating META Git publication remains COOPERATOR-owned;
- one smallest next step: ORCHESTRATOR reconciliation; if PASS, name only the
  separate COOPERATOR-owned live IRL run as not yet granted; if non-PASS, name
  one bounded correction without granting it;
- compact `Orchestration critique` with `MEASURED:` and `LEAD:`;
- exactly one `Logical-whole closure: not-closed` line;
- the exact authority-expiry sentence below.

Explicitly state that code acceptance is not live desktop or physical acceptance
and does not prove M2/G4 closure, M3 closure, deployment, production readiness,
G3 re-audit, autostart, hibernate/hybrid sleep, general input-remapper
coexistence, live desktop/launch/placement behavior, M5 behavior, per-key RGB, or
measured control-to-zone placement.

Authority for this Worker expires at this terminal report.

## Fail-closed stop conditions

Stop before substantive review on non-fresh or inherited implementation context,
Native Plan Mode mismatch, coordinate/authority contradiction,
identity/public-ref/ancestry/hash failure, dirty or unsafe checkout, prompt
collision, required tool/package absence, or need for product, host, device,
secret, or subagent authority.

During review, preserve the first causal failure. Continue read-only inspection
only when safe and useful; never correct the candidate or expand the task. A
confirmed blocking defect or required-evidence gap yields a truthful `PARTIAL`.

Stop immediately after the terminal report. Do not implement a correction, start
a live IRL run, reload the bridge, deploy, reopen M2/M3, or begin another M4
phase.
