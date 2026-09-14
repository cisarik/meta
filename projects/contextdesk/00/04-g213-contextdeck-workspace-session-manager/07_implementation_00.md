Logical whole identity: g213-contextdeck-workspace-session-manager
Worker session ordinal: 07
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: CONTEXTDECK-M4-SLICE-B-IMPLEMENTATION
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to a genuinely fresh Worker session
Reasoning recommendation: Maximum (COOPERATOR-selected; ORCHESTRATOR recommended High)
Reasoning basis: one coherent slice adds live desktop-mutation code, a typed
application launcher with a new KF6 dependency, compositor placement/maximize
through the bridge, checkpoint/revert, and a live-caption privacy guard; the
departure to the client maximum/enhanced mode is an accepted COOPERATOR decision
and does not change any authority boundary
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E3
Evidence-tier basis: code that will mutate live desktop configuration and launch
applications, plus a new build dependency and a compositor bridge change,
requires focused and full-suite evidence, one published candidate, and a
separate fresh acceptance
Internal delegation: prohibited

# ContextDeck M4 Slice B — implement workspace mutation, typed launch, and placement

You are a genuinely fresh WORKER. You did not plan, implement, accept, or repair
M4 and did not participate in M1/M2/M3. Native Plan Mode must be OFF. Do not use
subagents.

This prompt grants one bounded repository-only implementation slice: M4 Slice B.
Implement the accepted plan's mutation/launch/placement design, validate it with
private-bus and pure tests, create and publish one normal product commit, persist
the exact prompt and terminal report in META, then stop. You do not accept your
own candidate and never close the logical whole.

Critical: **no live host mutation, no application launch, no KWin bridge reload,
and no real KWin/OpenRGB/broker/device operation may occur during this
exchange.** Those are COOPERATOR-owned IRL operations for a later, separately
authorized run. This exchange edits and tests repository code only.

## Accepted plan and Plan-to-Execution transition

ORCHESTRATOR reconciliation: accepted
Accepted plan (frozen technical design):
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/01_report_00.md`
Planning pair commit: `6f14316`; completion report `01_report_01.md`, pair `c7e1b73`
Slice A accepted candidate: `aca6c68`, acceptance `05_report_00.md`, pair `977c841`
Slice B preflight: `06_report_00.md`, pair `6c1d6c6`, verdict `PASS`

The plan is decision-complete for M4 including Slice B. Its planning, completion,
and preflight authority have expired. This prompt is the separate
Plan-to-Execution event. Do not reopen planning, change the objective, or treat
retained text as authority beyond the exact implementation envelope below.

Implementation authority: explicit
Exact baseline: `aca6c68542bbc9f1b8ee891415a04b0a95e8372e`
Changed-path allowlist: the exact ceiling in "Exact changed-path allowlist"
Implementation boundaries: implement the accepted Slice B design in repository
code and tests only; no live host mutation, launch, bridge reload, or device
action during implementation or validation
Independence required: no for this implementation; yes for the required later
separate fresh code acceptance

## Authoritative continuity boundary

Use this exact M3 park wording wherever M3 state is restated:

> M3 workspace-aware lighting is code-accepted on `502ae75...`; its physical
> five-zone IRL observation is deferred by explicit COOPERATOR decision. M3 is
> not closed, and code acceptance is not physical acceptance.

Use this exact M2 park wording wherever M2 state is restated:

> The named live G4 slices are accepted, but the M2 logical whole remains open.
> M2 is parked with G3 host-mitigated on the authorized reference host; the
> next bounded whole is M4 workspace session manager.

Do not reopen M2/M3, do not touch input grabbing, and do not issue
`27_deployment_00.md`.

## Exact repositories and immutable gates

Canonical product repository: `https://github.com/cisarik/contextdesk`
Required branch: `main`
Required product HEAD and public `main` before mutation:
`aca6c68542bbc9f1b8ee891415a04b0a95e8372e`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

Canonical META repository: `https://github.com/cisarik/meta.git`
Required public META baseline:
`6c1d6c6` (a later verified descendant is acceptable after ancestry and
changed-path review proves no M4 artifact changed)
Required M4 trace:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/`

Repository checkout topology: standalone product checkout on `main`
Working-copy topology: canonical product checkout
Topology rationale: one accountable Worker owns one coherent Slice B change and
one commit

Before any product or META file mutation:

1. Verify the complete prompt, genuinely fresh session, Native Plan Mode OFF,
   coordinates, implementation authority, and no subagents.
2. Verify canonical remote, active `main`, exact HEAD, clean state, no Git locks,
   matching AP gitlink/checkout, and `./.ap/ap doctor` PASS (variant `stable`).
3. Prove public product `main` equals the exact baseline with direct
   `git ls-remote`. Do not pull, merge, rebase, switch, reset, clean, stash, or
   retarget.
4. Verify META public `main` is the baseline or a later verified descendant;
   review ancestry and changed paths.
5. Verify the M4 trace directory and parents are real directories; the Slice B
   prompt/report destinations must be absent or byte-identical.
6. Verify `dbus-run-session`, CMake, Ninja, and the KF6 packages below without
   installing anything.
7. Read current source and tests before editing; every needed path must be inside
   the allowlist.

## Mandatory reading

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-12, RF-16, RF-18, RF-19, implementation
  authority, Git safety, validation, stopping;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Implementation Authority
  Record, exchange/trace, validation ladder, delivery record;
- `AGENTS.md`, `README.md`, `ROADMAP.md`;
- the complete M4 artifacts `01_report_00.md`, `01_report_01.md`,
  `02_implementation_00.md`, `02_report_00.md`, `03_report_00.md`,
  `04_correction_00.md`, `04_report_00.md`, `05_report_00.md`, `06_report_00.md`;
- `docs/specification.md`, `docs/architecture.md`, `docs/operations.md`,
  `docs/testing-m4.md`, `docs/adr/0002-*`, `docs/adr/0004-*`, `docs/adr/README.md`;
- `src/workspace/WorkspacePlan.{h,cpp}`, `src/context/WorkspaceReceiver.{h,cpp}`,
  `src/context/ContextReceiver.{h,cpp}`, `src/context/DBusNames.h`,
  `src/app/AppController.{h,cpp}`, `src/app/SessionApplication.{h,cpp}`,
  `src/core/Types.h`, `src/core/Persistence.h`;
- `kwin/contextdeck-bridge/contents/code/main.js` and `metadata.json`;
- `CMakeLists.txt` and directly included owners.

## Product invariants

- G213 only, USB `046d:c336`; five RGB zones, never per-key.
- Session app never opens raw keyboard nodes; broker stays static/inactive.
- Event-driven KWin identity; never `xdotool`/`wmctrl`/`xprop`; no title polling.
- Typed action/launch model only; no shell strings and no `QProcess` of `Exec=`.
- Captions, titles, desktop names, and desktop UUIDs are sensitive: never logged,
  never persisted in diagnostics, prompts, reports, or META.
- `kwinrulesrc` is never written by M4.
- No autostart, no M5 system integration, no input-remapper, no suspend/DPMS
  behavior, no external source copying while licensing is unresolved.

## Accepted Slice B implementation contract

### 1. Desktop mutation executor

Add a bounded executor (for example `src/workspace/DesktopMutator.{h,cpp}`) that
performs only the accepted mutation set against the live session-bus
`org.kde.KWin` `/VirtualDesktopManager` interface, driven by pure input from
`WorkspacePlan` and an observed `WorkspaceState`:

- default Apply is exactly: trailing-only `createDesktop(position, name)` for
  each missing ordinal up to the desired count; conditional `setDesktopName(id,
  name)` only when the live name differs (matched by ordinal-to-live-UUID);
  `rows` and `navigationWrappingAround` `Properties.Set` only when the preview
  diff is non-empty;
- excluded from default Apply and only ever performed as separately disclosed
  opt-ins: optional `current` switch when the user chose "switch to session";
  explicit `removeDesktop(id)` for opted-in extras after preview;
- `removeDesktop` is never implicit and never triggered by drift;
- exact ordering: verify preconditions → write and verify checkpoint → create
  ascending → rename ascending → set rows → set wrapping → optional `current` →
  explicit `removeDesktop` for opted-in extras only → transaction end;
- every step gates the next; any error stops the sequence and triggers the revert
  path;
- use the receiver's one-in-flight observation discipline; never poll; never
  mutate on `currentChanged` or on user-initiated desktop changes outside an
  explicit transaction.

### 2. Checkpoint, revert, and stop rules

Add a user-local checkpoint (for example `src/workspace/WorkspaceCheckpoint.*`)
under the product config root, never the profile document, never META, never
logs. Pin and implement:

- atomic `QSaveFile` write, user-only permissions, overwrite per Apply,
  checkpoint-write-success **before** the first mutation;
- revert removes exactly the UUIDs this Apply created (never a desktop it did
  not create, including user-created extras) and restores names/rows/wrapping
  from the checkpoint;
- `current` restore happens only if the checkpoint UUID still exists; otherwise
  skip and report as a bounded residual instead of guessing by ordinal;
- assignment rebinding stays ordinal-based (no UUID in the profile document);
- checkpoint lifecycle: retain until a successful revert or the next Apply;
  delete on successful revert;
- revert is desktop-configuration-only: launch and placement effects are never
  reverted and no application is killed; an already-open window is not moved
  back (disclosed limitation);
- fail-closed preconditions: explicit user Apply; `workspace_management_enabled`;
  a valid saved session; observation `Available` and fresh for the exact preview
  shown; no service-owner change; no drift; checkpoint verified; explicit
  per-option decisions for any opt-in in use.

### 3. In-transaction launch trigger event surface

The existing `WorkspaceReceiver` subscribes the desktop signals but discards
payloads. Add a bounded, testable event surface (for example a receiver signal
or snapshot-diff classification) so the applier can distinguish a
`desktopCreated` that occurred **during the in-flight Apply transaction** from a
user-created desktop, without adding a second `GetAll` or polling, and without
logging desktop identity.

### 4. Typed application launcher

Add a typed launcher (for example `src/workspace/ApplicationLauncher.*`) using
`KService`/`KApplicationTrader` plus `KIO::ApplicationLauncherJob` for a typed
`.desktop` id. Requirements:

- reject shell, `QProcess` of `Exec=` lines, `systemd-run`, and `kstart`;
- launch only on explicit `applyWorkspaceSession` and on an in-transaction
  `desktopCreated` for profiles assigned to that ordinal; never on Plasma login,
  session-app start, `currentChanged`, or user-created desktops;
- skip when the bridge inventory already matches the profile; one attempt per
  profile per transaction with a 2 s debounce; at most one bounded retry on the
  matching in-transaction `desktopCreated` when the first job failed before
  `windowAdded`; bounded error classes only;
- provide a testable seam so the launch decision can be unit-tested without
  launching anything; never call the real job in tests.

### 5. Placement and maximize

- Add a pure `PlacementResolver`-style decision (for example
  `src/workspace/PlacementResolver.{h,cpp}`) mapping application identity
  (or the opt-in title fallback) to `(desktop_id, maximize)` with an empty id as
  no-op; identity wins over title fallback.
- Expose it to the bridge through a new `PlacementHint` method on the existing
  ContextDeck D-Bus interface, returning the decision. Update
  `src/context/ContextReceiver.{h,cpp}` (and `DBusNames.h` if needed).
- Extend `kwin/contextdeck-bridge/contents/code/main.js` on `windowAdded`: skip
  docks/splashes as today, call `PlacementHint(desktop_file_name,
  resource_class, resource_name)`, set `window.desktops = [matched id]`, and call
  `setMaximize(true, true)` when requested, with an empty id as no-op. Keep the
  existing `ContextReport` signature compatible. Never send captions.
- **Before committing to `callDBus` with a reply callback, verify the installed
  KWin scripting reference supports it.** If it does not, stop `PARTIAL` and
  name the exact alternative; do not improvise an unsupported mechanism.
- The bridge change is code only in this exchange; reloading the bridge is a
  COOPERATOR-owned IRL step.

### 6. Apply UI and opt-ins

- Enable Apply in `ui/WorkspacePage.qml` with an explicit preview (create/rename
  intent), truthful opt-in toggles, and clear "no undo for removed desktops"
  wording.
- Default path shows only create + conditional rename + rows/wrapping.
  `removeDesktop`, the optional `current` switch, launch, and maximize are
  separate opt-ins.
- Keep `workspaceApplyAvailable` semantics truthful; no navigation redesign; do
  not change accepted M1/M3 lighting semantics.

### 7. Live-caption privacy guard

When the `TitleHint` producer is introduced, add the live-caption-path privacy
guard required by `05_report_00.md`: a regression (or explicit diagnostics
key-category coverage plus the no-argument-logging guarantee) proving captions
are compared only in memory, discarded after the call, and never logged or
persisted. Extend `tests/unit/test_workspace_lighting.cpp` or a suitable test.

### 8. Tests and validation

Add and register new tests (for example `test_workspace_mutator`,
`test_placement_resolver`, `test_application_launcher`) and extend existing
workspace tests. Required causal coverage:

- mutator: default create/rename/no-remove diff; conditional rename by ordinal;
  rows/wrapping set only on diff; excluded `removeDesktop`/`current`; ordering
  and step gating; abort on error; revert removes only this-Apply UUIDs;
- checkpoint: atomic write, permissions, write-before-mutation, overwrite,
  cleanup, `current`-restore skip when UUID absent;
- trigger classification: in-transaction `desktopCreated` triggers launch;
  user-created desktop does not; `currentChanged` does not;
- launcher decisions through the injected seam: skip-if-already-running,
  missing desktop file, debounce keys, retry bound;
- placement: identity wins, fallback gating, empty id no-op, maximize flag;
- live-caption privacy guard.

All D-Bus tests must use a fake desktop-manager service on a private
`dbus-run-session` bus and must never connect to or replace real KWin. Never
start the session application, broker, OpenRGB, or any device. The launcher must
be exercised only through its test seam.

Run, in order:

```sh
cmake -S . -B build -G Ninja
cmake --build build

ctest --test-dir build --output-on-failure \
  -R '^(test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_plan|test_openrgb_protocol|test_workspace_mutator|test_placement_resolver|test_application_launcher)$'

ctest --test-dir build --output-on-failure

git diff --check
git diff --name-only
git status --short
```

The full registered suite is required. Do not install packages, skip a required
test, or weaken a gate.

### 9. Documentation

Update the allowed documents to describe the implemented Slice B code: the
mutation set and default/opt-in split, checkpoint/revert/stop rules, typed launch
and trigger set, placement/maximize through the bridge, the new build
dependency, the live-caption privacy guard, and the unchanged `kwinrulesrc`
rejection and M4/M5 boundary. Update `docs/testing-m4.md` only as the IRL
checklist (it must not authorize host mutation by itself). Update ADR 0002/0004
statuses truthfully if needed. Fix any M4/M5 documentation drift.

## Exact changed-path allowlist

Modify or create only the necessary subset of this ceiling:

```text
CMakeLists.txt
README.md
ROADMAP.md
docs/adr/0002-host-desktop-mutation-authority.md
docs/adr/0004-typed-application-launch.md
docs/adr/README.md
docs/architecture.md
docs/operations.md
docs/specification.md
docs/testing-m4.md
src/core/Types.h
src/context/ContextReceiver.h
src/context/ContextReceiver.cpp
src/context/DBusNames.h
src/context/WorkspaceReceiver.h
src/context/WorkspaceReceiver.cpp
src/workspace/WorkspacePlan.h
src/workspace/WorkspacePlan.cpp
src/workspace/DesktopMutator.h
src/workspace/DesktopMutator.cpp
src/workspace/WorkspaceCheckpoint.h
src/workspace/WorkspaceCheckpoint.cpp
src/workspace/ApplicationLauncher.h
src/workspace/ApplicationLauncher.cpp
src/workspace/PlacementResolver.h
src/workspace/PlacementResolver.cpp
src/app/AppController.h
src/app/AppController.cpp
src/app/SessionApplication.h
src/app/SessionApplication.cpp
kwin/contextdeck-bridge/contents/code/main.js
kwin/contextdeck-bridge/metadata.json
ui/Main.qml
ui/WorkspacePage.qml
ui/ApplicationsPage.qml
ui/DiagnosticsPage.qml
tests/unit/test_workspace_plan.cpp
tests/unit/test_workspace_receiver.cpp
tests/unit/test_workspace_lighting.cpp
tests/unit/test_workspace_mutator.cpp
tests/unit/test_placement_resolver.cpp
tests/unit/test_application_launcher.cpp
```

The ceiling is a maximum, not a requirement. New files must be justified by the
accepted design. `src/core/Persistence.{h,cpp}` may be touched only if the
checkpoint or trigger classification genuinely requires it; otherwise leave it
unchanged.

Do not change `.ap/`, `src/broker/`, broker IPC, `src/rgb/`, `src/core/ControlCatalog.*`,
`packaging/`, license files, dependencies beyond the exact KF6 components named
below, lockfiles, generated files, M1/M2/M3 test procedures, hardware evidence,
or host configuration.

If one additional product path is genuinely required, stop `PARTIAL`, preserve
the coherent state without committing, and name the exact path and reason. Do
not silently widen the allowlist.

## Command, dependency, host, and data authority

Allowed commands: read-only source/Git inspection; existing CMake/Ninja build;
the exact test routes above; `git diff`, `git status`, exact-path staging, one
commit, one normal push, direct public-ref readback
Forbidden commands: destructive Git recovery; force push; history rewrite;
branch/tag/remote/config changes; package manager; sudo; service/device tools;
live D-Bus calls to KWin; application launch; OpenRGB CLI; broker operations
Dependency authority: edit `CMakeLists.txt` to add
`find_package(KF6Service REQUIRED)` and `find_package(KF6KIO REQUIRED)` and link
`KF6::Service` and `KF6::KIOGui`; no install, no manifest/lockfile/toolchain
change, no `extra-cmake-modules`, no umbrella `KF6`, no other package
Host authority: none; no live desktop mutation, application launch, service, or
bridge reload
Device authority: none
Secret authority: none
Network authority: canonical product/META Git public verification and the one
authorized normal product push only

No raw input, raw event lines, key names, scan values, typed content, serials,
host addresses, host keys, passwords, private paths, desktop IDs/names, window
captions, or unredacted logs may enter code logs, documentation, prompts,
reports, or META.

## Git publication authority

After all focused and full tests pass and exact-path review proves the diff is
inside the allowlist:

1. Inspect `git diff --check`, `git diff --name-only`, `git status --short`, and
   the complete diff.
2. Stage only exact changed allowlisted product paths. Never `git add .`/`-A`.
3. Create exactly one normal commit with subject:
   `Implement M4 Slice B workspace mutation and typed launch`
4. Push only `main` to canonical origin with a normal non-force fast-forward.
5. Verify local HEAD, `origin/main`, and direct public `ls-remote` all equal the
   new commit; parent equals the exact baseline; changed paths are the authorized
   subset.

If commit/push auth is unavailable, report `PARTIAL` with exact state. Product
publication grants no host mutation, launch, deployment, acceptance, or closure.

## Validation and acceptance envelope

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: workspace plan/receiver/lighting, persistence, resolver
Affected tests: new mutator/placement/launcher tests plus extended workspace tests
New causal regression: required for mutation ordering/revert, checkpoint,
in-transaction trigger classification, launcher decisions, placement, and
live-caption privacy
Broad or full suite: required-because shared context/session/app and CMake changes
Runtime or testbed: local CMake/Ninja build and private `dbus-run-session` test
bus only
Independent acceptance: required-separate-fresh-worker

Evidence tier: E3
Authorized implementation stages: sources/CMake → tests → docs → one commit →
one normal push → public verification
Combined implementation envelope: allowed
Implementation stage gates: focused tests pass; full CTest passes; diff inside
allowlist; no host/desktop/launch/bridge/device side effect occurs
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: the exact public baseline `aca6c68…`; one
revertable commit
Activated stricter profile: none
Terminal implementation report point: one terminal report after commit, push, and
public-ref verification

Implementation-PASS is non-independent repository evidence. A separate fresh
Worker must accept the immutable public candidate before any COOPERATOR IRL run.
Only the COOPERATOR can establish live desktop/launch/placement behavior.

Do not claim acceptance-PASS, deployment-PASS, production readiness, physical
acceptance, M2/G4 closure, M3 closure, autostart, hibernate/hybrid sleep,
coexistence, live desktop/launch/placement behavior, remapping, M5, per-key RGB,
or measured control-to-zone placement.

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

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 07_implementation_00.md
Destination path: projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/
Report filename: 07_report_00.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR for META; WORKER for the one product commit
Archival: wait-for-report

The ORCHESTRATOR persists this exact prompt bytes to
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/07_implementation_00.md`
before delivery. The WORKER may write only the report file at
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/07_report_00.md`.
Verify the persisted prompt is byte-identical and read it back completely. Do not
alter earlier M4 pairs or `00_notes.md`. After publication, write and completely
read back the terminal report. Do not mutate META Git; the COOPERATOR owns
first-add archival.

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo the opening persistent-role and three coordinate fields exactly once with
values unchanged, and include:

- status `PASS`, `PARTIAL`, or `BLOCKED`;
- phase-qualified result: `implementation-PASS` only when every gate, focused and
  full validation, one commit/push, and public-ref verification pass;
- exactly one `Report justification: new-mutation`;
- start/end commit, baseline, AP pin, public META baseline, and accepted
  plan/Slice A acceptance/preflight identities;
- exact changed product paths with purpose and proof that all other paths, `.ap`,
  broker, RGB transport, packaging, dependencies beyond the two KF6 components,
  and host state remained unchanged;
- the mutation set implemented with the default/opt-in split and the exact
  checkpoint/revert/stop rules;
- the trigger event surface, launcher seam, placement path, bridge change, and
  the KWin `callDBus` reply-form verification result;
- the live-caption privacy guard and its test;
- focused and full CTest results with counts from actual output;
- private-bus evidence and explicit statement that no real KWin/OpenRGB/device/
  broker/host/desktop/launch/bridge-reload operation ran;
- exact commit, push, public-ref equality, parent, and changed-path evidence;
- META prompt/report persistence and readback, with META Git publication
  remaining COOPERATOR-owned;
- deviations, resolved issues/near-misses, pre-existing failure classification,
  residual risks, missing evidence, and plan fidelity;
- exactly one smallest next step: ORCHESTRATOR reconciliation followed, only if
  accepted, by a separate fresh independent code-acceptance Worker;
- compact `Orchestration critique` with `MEASURED:` and `LEAD:`;
- exactly one `Logical-whole closure: not-closed` line;
- the exact authority-expiry sentence below.

Explicit non-claims: no acceptance-PASS, deployment-PASS, production readiness,
physical acceptance, M2/G4 closure, M3 closure, autostart, hibernate/hybrid
sleep, general input-remapper coexistence, live desktop/launch/placement
behavior, remapping, deck behavior, M5 integration, per-key RGB, or measured
control-to-zone placement; no claim that tests prove live behavior; no claim
that Session 27 was an independent Worker result.

Authority for this Worker expires at this terminal report.

## Stop conditions

Stop before mutation on a non-fresh/contaminated session, Native Plan Mode
mismatch, coordinate/authority contradiction, product/AP/META identity or
public-ref failure, dirty/unexplained worktree, unsafe trace path/collision,
missing required tool/private-bus runner or KF6 component, unavailable accepted
plan, or need for a non-allowlisted path, an additional dependency, host/desktop
mutation, launch, device access, secret, or subagent.

After mutation, stop `PARTIAL` without committing when a required design cannot
be implemented faithfully inside the allowlist, when `callDBus` reply form is
unsupported and no bounded alternative is authorized, or when a required test
fails and cannot be corrected in scope. Preserve the first causal failure; do not
weaken, skip, or endlessly rerun gates.

If validation passes but commit/push/public verification fails, preserve the
exact safe state and report `PARTIAL`. Use `PASS` only for one fully validated
and publicly verified implementation commit.

Stop immediately after the terminal report. Do not perform any live desktop
mutation, launch, bridge reload, acceptance, deployment, or host enablement
under this authority.
