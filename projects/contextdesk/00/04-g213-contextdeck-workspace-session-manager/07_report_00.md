### Report for ORCHESTRATOR_CHAT

Logical whole identity: g213-contextdeck-workspace-session-manager
Worker session ordinal: 07
Worker exchange ordinal: 01
Persistent role identity: WORKER

```text
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: CONTEXTDECK-M4-SLICE-B-IMPLEMENTATION
Native planning mode: not-used
status: PASS
Phase-qualified result: implementation-PASS
Result artifact or commit: 50872779c619a97be061d7f0df414ccae6bde7e6
Result evidence: one public product commit implementing M4 Slice B; focused 8/8 and full 21/21 registered CTest passed from the committed tree; direct public-ref, parent, and changed-path equality verified
Report justification: new-mutation
```

M3 state: M3 workspace-aware lighting is code-accepted on `502ae75...`; its
physical five-zone IRL observation is deferred by explicit COOPERATOR decision.
M3 is not closed, and code acceptance is not physical acceptance.

M2 state: The named live G4 slices are accepted, but the M2 logical whole
remains open. M2 is parked with G3 host-mitigated on the authorized reference
host; the next bounded whole is M4 workspace session manager.

## Preflight gates (all verified before mutation)

- Genuinely fresh Worker session; Native Plan Mode not used; no subagents; one
  accountable Worker; implementation authority, exact baseline, and allowlist
  matched the issued prompt.
- Canonical product `https://github.com/cisarik/contextdesk`, branch `main`,
  standalone checkout. HEAD and parent before mutation =
  `aca6c68542bbc9f1b8ee891415a04b0a95e8372e`; direct `git ls-remote` equality;
  clean tracked/untracked state; no Git locks or active operations.
- AP gitlink and `.ap` checkout both `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`;
  `./.ap/ap doctor` = PASS, resolved variant `stable`, `.ap` clean.
- Canonical META `https://github.com/cisarik/meta.git`: local HEAD and public
  `refs/heads/main` both `f4d2d37d5edc18570efd4af04c530a9527427bc5`, a verified
  descendant of the required baseline `6c1d6c6` whose only changed paths are
  under `projects/ap/09/...`; no M4 artifact changed. The M4 trace directory
  and its parents are real directories, not symlinks. The persisted prompt
  `07_implementation_00.md` was read back completely (560 lines) and matched
  the delivered prompt; its SHA-256 is
  `48d20c7be5f0a95555fc4b61abe58e4f146adad1867df5f56a03b76ad758ed48`. The
  report destination `07_report_00.md` was absent.
- Required tools present without installing anything: `dbus-run-session`,
  CMake 4.4.3, Ninja 1.13.2, `KF6Service` and `KF6KIO` CMake packages
  (KF6::Service, KF6::KIOGui), Node.js for a JavaScript syntax check.
- `callDBus` reply-form verification (required implementation-time check):
  installed `kwin` 6.7.5-1.1; `/usr/lib/libkwin.so.6.7.5` SHA-256
  `02737e1fb3a6b5923fdfc37de2d57dc65d19f9bfbe5f33b6dedb41dc7203da61`. The
  shipped metaobject string table for `KWin::Script` declares `callDBus` with
  `service`, `path`, `interface`, `method`, and `arg1`–`arg9` typed `QJSValue`.
  The binary's implementation calls `QDBusConnection::asyncCall`, constructs a
  `QDBusPendingCallWatcher`, connects `finished` via `QObject::connectImpl`,
  checks `QJSValue::isCallable`, and invokes `QJSValue::call` on the reply
  arguments (with error handling via `QDBusPendingCall::isError`). The
  trailing-callback reply form is supported; no unsupported mechanism was
  needed.

## Implementation summary

### Desktop mutation executor and ordering

`DesktopMutator` executes exactly one explicit transaction against
`org.kde.KWin` `/VirtualDesktopManager` (`createDesktop(u,s)`,
`setDesktopName(s,s)`, `removeDesktop(s)`, and `Properties.Set` on
`org.kde.KWin.VirtualDesktopManager`). Order: verify preconditions (controller)
→ write and verify checkpoint → create trailing ordinals ascending
(position = ordinal − 1) → conditional rename ascending using the observed
ordinal-to-live-UUID map → `rows` → `navigationWrappingAround` → optional
`current` → explicit opted-in `removeDesktop` for extras (descending) →
transaction end. Every step gates the next; any D-Bus error or per-call timeout
stops the sequence and runs the revert path. D-Bus calls are awaited with a
bounded local event loop so in-transaction `desktopCreated` signals are
dispatched while the transaction is still active; there is no polling and no
mutation on `currentChanged` or on user-initiated desktop changes.

Default Apply is exactly create + conditional rename + rows/wrapping **only on
a non-empty preview diff**. Excluded from default Apply and only performed as
separately disclosed opt-ins: the `current` switch (first desktop of the
session) and `removeDesktop(id)` for opted-in extras. `removeDesktop` is never
implicit and never drift-triggered.

### Checkpoint, revert, and stop rules

`WorkspaceCheckpoint` writes `$XDG_CONFIG_HOME/contextdeck/workspace-checkpoint.json`
(fallback `$HOME/.config/...`) with atomic `QSaveFile`, no direct-write
fallback, and user-only permissions (`ReadOwner|WriteOwner`); it stores the
pre-Apply ordinals/UUIDs/names, `rows`, wrapping, current UUID, and appends the
UUIDs this Apply created. Write and verify happen before the first mutation.
Revert removes exactly the created UUIDs (never a desktop it did not create,
including user-created extras) and restores names by UUID, `rows`, and
wrapping. The `current` restore happens only when the checkpoint UUID still
exists in the observed state; otherwise it is skipped with the bounded residual
`current-restore-skipped`. The checkpoint is retained until a successful revert
or the next Apply and deleted on successful revert; a hard step failure keeps
it and reports a bounded residual. Revert is desktop-configuration-only:
applications are not killed and open windows are not moved back. Fail-closed
controller preconditions: explicit user Apply, `workspace_management_enabled`,
valid session, observation `Available` with no in-flight receiver request and
no pending refresh, unchanged service-owner generation, unchanged live-preview
fingerprint, verified checkpoint, and explicit option booleans.

### In-transaction trigger event surface

`WorkspaceReceiver` now emits a payload-free
`desktopCreatedObserved(id, position)` parsed from the existing subscription
(no second `GetAll`, no polling). The controller routes it to the mutator only
while a transaction is active; the mutator records the created UUID in the
checkpoint and re-emits `desktopCreatedInTransaction`, which launches only
profiles assigned to that ordinal. Events outside the transaction (user-created
desktops) and `currentChanged` launch nothing. No desktop identity is logged.

### Typed launcher

`ApplicationLauncher` accepts only a validated `.desktop` id and uses
`KService::serviceByStorageId` plus `KIO::ApplicationLauncherJob`; shell
strings, `QProcess` of `Exec=`, `systemd-run`, and `kstart` are rejected by
construction and by test. A `LaunchInvoker` seam allows unit tests to observe
decisions without starting anything. Triggers: explicit Apply (after the
mutation sequence) and the matching in-transaction `desktopCreated`; inventory
matches skip (`already_running`), one attempt per profile per transaction is
debounced (2 s), and one bounded retry is allowed only after a job failed
before a window appeared. Outcomes are bounded strings.

### Placement and the KWin bridge

`PlacementResolver` maps identity (winning) or the opt-in title fallback to
`(desktop_id, maximize)`, with an empty id as no-op; it is gated on
`workspace_management_enabled` and an `Available` observation.
`ContextReceiver` exposes `PlacementHint(desktop_file_name, resource_class,
resource_name) -> (desktop_id, maximize)` to the bridge. The bridge's
`windowAdded` handler skips docks/splashes as before, calls `PlacementHint`,
sets `window.desktops = [matched id]`, and calls `window.setMaximize(true,
true)` when requested. The existing `ContextReport` six input arguments are
unchanged; its reply now carries the `title_fallback_enabled` boolean so the
bridge learns the flag event-driven. `kwinrulesrc` is never written.

### Live-caption privacy guard

When the global flag is on, the bridge sends `TitleHint(bridge_id, sequence,
caption)` immediately before the identity report; when off, no caption is sent.
`ContextReceiver` bounds the caption to 256 bytes, holds it only until the next
resolution consumes it, and never logs it; it is discarded after the call and
never stored or persisted. The regression
`contextReceiverDoesNotLogTitleHintArguments` installs a Qt message handler,
runs the hint flow with a synthetic sentinel caption, and asserts no captured
message contains it; `liveCaptionPrivacyGuard` drives the full controller flow
(title fallback selection, then a second focus event without a hint) and
asserts the caption is discarded, absent from diagnostics, and absent from all
captured log messages. The existing
`diagnosticsOmitWorkspacePrivacySentinels` regression still passes.

### Build dependency and UI

Added only `find_package(KF6Service REQUIRED)` and
`find_package(KF6KIO REQUIRED)`, linking `KF6::Service` and `KF6::KIOGui` into
a new `contextdeck_launch` static library. No umbrella `KF6`, no
`extra-cmake-modules`, no install, no lockfile/toolchain change. The
`Plochy` page now has a truthful preview, Apply and checkpoint-revert buttons,
separate opt-in checkboxes for the `current` switch and extra removals (with a
"no undo for removed desktops" confirmation), and status/residual labels;
`workspaceApplyAvailable` is no longer `CONSTANT`. Diagnostics gained bounded
apply/launch fields with no desktop/caption/UUID categories. `ui/Main.qml`,
`src/app/SessionApplication.*`, `src/core/Types.h`, `src/core/Persistence.*`,
`src/context/DBusNames.h`, `docs/adr/0003-*`, and `docs/adr/README.md` were not
needed and were not touched.

## Changed product paths (35, exactly the authorized subset)

```text
 CMakeLists.txt                                    KF6Service/KF6KIO, new launch lib, three new tests
 README.md                                         M4 Slice B status truth; park wordings preserved
 ROADMAP.md                                        M4 Slice B section; milestone row; park wordings
 docs/adr/0002-host-desktop-mutation-authority.md  status and mutation/checkpoint/revert decision
 docs/adr/0004-typed-application-launch.md          status, trigger set, retry, typed-only posture
 docs/architecture.md                              M4 component map (mutator/checkpoint/launcher/placement)
 docs/operations.md                                section 10 explicit-Apply operation and checkpoint
 docs/specification.md                             mutation set, opt-ins, checkpoint/revert, triggers, D-Bus
 docs/testing-m4.md                                IRL checklist updated for Slice B; no host authority
 kwin/contextdeck-bridge/contents/code/main.js     PlacementHint, TitleHint, flag reply callback
 kwin/contextdeck-bridge/metadata.json             version/description truth
 src/app/AppController.cpp                         apply/revert preconditions, launch wiring, placement provider
 src/app/AppController.h                           new properties/invokables, launcher/mutator members
 src/context/ContextReceiver.cpp                   TitleHint/PlacementHint, flag reply, caption lifecycle
 src/context/ContextReceiver.h                     provider seam, pending caption, cleanup flags
 src/context/WorkspaceReceiver.cpp                 desktopCreatedObserved payload classification
 src/context/WorkspaceReceiver.h                   new signal and ownerGeneration accessor
 src/workspace/WorkspacePlan.cpp                   launch desktop-file id, bounded retry helper
 src/workspace/WorkspacePlan.h                     launch plan field, tryBoundedRetry declaration
 src/workspace/ApplicationLauncher.{h,cpp}         typed KIO launcher with test seam (new)
 src/workspace/DesktopMutator.{h,cpp}              mutation transaction, gating, revert (new)
 src/workspace/PlacementResolver.{h,cpp}           identity-wins placement decision (new)
 src/workspace/WorkspaceCheckpoint.{h,cpp}         atomic user-only checkpoint state (new)
 tests/unit/test_workspace_lighting.cpp            apply/refusal/launch/privacy-guard regressions
 tests/unit/test_workspace_receiver.cpp            event-surface and ContextReceiver hint tests
 tests/unit/test_workspace_mutator.cpp             mutation ordering/gating/revert/checkpoint tests (new)
 tests/unit/test_placement_resolver.cpp            placement gating/mapping tests (new)
 tests/unit/test_application_launcher.cpp          launcher seam/debounce/retry tests (new)
 ui/ApplicationsPage.qml                           truthful launch/maximize opt-in wording
 ui/DiagnosticsPage.qml                            bounded apply/revert status fields
 ui/WorkspacePage.qml                              Apply/revert controls, opt-ins, confirmation, status
```

Proof other paths stayed unchanged: `git diff --name-only
aca6c68..5087277` returns exactly those 35 paths and no others. The `.ap`
gitlink, `src/broker/`, broker IPC, `src/rgb/`, `src/core/ControlCatalog.*`,
`packaging/`, license files, lockfiles, generated files, M1/M2/M3 test
procedures, hardware evidence, `src/app/SessionApplication.*`,
`src/core/Persistence.*`, `src/core/Types.h`, `src/context/DBusNames.h`,
`docs/adr/0003-*`, `docs/adr/README.md`, and `ui/Main.qml` are untouched.
Dependencies beyond the two authorized KF6 components are unchanged. No host
state was changed.

## Validation evidence

From the committed tree (build products inside the ignored local `build/`
checkout; all test runs under `dbus-run-session` where registered):

```text
cmake -S . -B build -G Ninja                 -> exit 0
cmake --build build                          -> exit 0, no errors or warnings

focused (exact required route):
  ctest --test-dir build --output-on-failure \
    -R '^(test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_plan|test_openrgb_protocol|test_workspace_mutator|test_placement_resolver|test_application_launcher)$'
  => 100% tests passed out of 8
     test_profile_resolver 0.01 s, test_profile_persistence 0.01 s,
     test_workspace_plan 0.01 s, test_openrgb_protocol 0.01 s,
     test_workspace_receiver 65.95 s, test_placement_resolver 0.01 s,
     test_workspace_mutator 0.68 s, test_application_launcher 0.02 s;
     total 66.69 s

full registered suite:
  ctest --test-dir build --output-on-failure
  => 100% tests passed out of 21; total 68.86 s
     (includes test_workspace_lighting with the new apply/launch/refusal/
      privacy-guard regressions and the three new targets)

diff gates: git diff --check -> clean (pre-commit staged check clean)
            git diff --name-only / git status --short -> exactly the 35
            authorized paths before commit; clean after commit
extra: node --check kwin/.../main.js -> OK; metadata.json parses as JSON
```

New causal coverage: mutation ordering and step gating; abort-on-error revert;
revert removing only this-Apply UUIDs; checkpoint write-before-mutation,
permissions, overwrite-per-Apply, and delete-on-successful-revert;
`current`-restore skip when the UUID is absent; in-transaction
`desktopCreated` trigger versus user-created and `currentChanged`
non-triggers; launcher skip/missing/invalid/debounce/bounded-retry decisions
through the injected seam; placement identity-wins/gating/empty-no-op/maximize;
controller refusals (`management-disabled`, `preview-stale`); and the
live-caption no-logging/discard guard.

Private-bus and no-side-effect statement: `test_workspace_receiver`,
`test_workspace_mutator`, and `test_workspace_lighting` ran through the
registered `dbus-run-session` route with synthetic fake desktop-manager
services on the private session bus (`QT_QPA_PLATFORM=offscreen;
QT_DISABLE_SESSION_MANAGER=1`); `test_profile_*`,
`test_placement_resolver`, and `test_application_launcher` are pure. No real
KWin connection, KWin replacement, bridge reload, desktop mutation,
application launch, OpenRGB connection or CLI, device open, broker
start/ARM/grab, service change, package install, `/etc`/udev change, or host
operation occurred in this exchange. The launcher was exercised only through
its test seam.

## Publication evidence

- `git diff --cached --check` clean; the complete staged diff reviewed; 35
  exact allowlisted paths staged (no `git add .`/`-A`).
- Exactly one commit: `50872779c619a97be061d7f0df414ccae6bde7e6`, subject
  `Implement M4 Slice B workspace mutation and typed launch`.
- Push: `aca6c68..5087277  main -> main`, normal non-force fast-forward to
  canonical origin.
- Equality verified after push and by direct public readback: local `HEAD` =
  `origin/main` = public `refs/heads/main` =
  `50872779c619a97be061d7f0df414ccae6bde7e6`. Parent =
  `aca6c68542bbc9f1b8ee891415a04b0a95e8372e`. Public changed-path set = the
  authorized 35-path subset. Product worktree clean; `.ap/ap doctor` PASS.

## META trace persistence

- Prompt `projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/07_implementation_00.md`
  was persisted by the ORCHESTRATOR before delivery; this Worker verified the
  destination is a real regular file (not a symlink), read it back completely
  (560 lines, 27287 bytes), matched it to the delivered prompt field by field,
  and computed its SHA-256 as
  `48d20c7be5f0a95555fc4b61abe58e4f146adad1867df5f56a03b76ad758ed48`. No
  differing content existed and nothing was overwritten.
- Report `.../07_report_00.md` was written once after publication, is the only
  file this exchange prepared, and was read back completely immediately after
  the write. The M4 trace and all parents are real directories.
- META Git was not staged, committed, pushed, pulled, merged, rebased,
  switched, or otherwise mutated; no META ref or history changed. First-add
  archival of this exact prompt/report pair remains COOPERATOR-owned. Public
  META `main` remains `f4d2d37...`.

## Deviations, resolved issues, risks, missing evidence

- Deviations: none from the implementation contract. The allowlisted
  `docs/adr/README.md`, `ui/Main.qml`, and `src/app/SessionApplication.{h,cpp}`
  were not needed, and the conditional `src/core/Persistence.{h,cpp}` was
  untouched; all are ceiling paths, not required touches.
- Resolved execution issues / near-misses: (1) an early mutator design let the
  apply-failure result reuse the revert result's `ok` value; the failure path
  was made explicit and the abort test now passes. (2) A test's blocking D-Bus
  call from the main thread deadlocked against the in-process fake; it was
  replaced with a direct fake signal path. (3) A test-only pattern did not
  occur in the synthetic caption; the pattern was aligned with the synthetic
  sentinel. (4) A stale in-memory-vs-file checkpoint preference was fixed so a
  revert during the same session uses the most complete in-memory checkpoint.
  All corrections are inside the allowlist and the final tree is green.
- Pre-existing failure classification: none. No registered test was failing at
  the baseline and none fails now; the full suite is 21/21. The Qt harness's
  `org.kde.kscreen.dpms` "Platform is not Wayland or X11" warning on
  `PowerActions` construction is pre-existing library noise unrelated to this
  change and does not affect any test result.
- Residual risks: launch/placement/desktop behavior has no live evidence (all
  tests use fakes); the retry-on-`desktopCreated` path is exercised through the
  seam and unit tests, not a live KWin dispatch ordering; KWin may deliver
  `desktopCreated` after the method reply in unusual scheduling, in which case
  the controller's in-transaction classification is bounded by
  `m_applyRunning` and the launcher could miss a create-triggered launch while
  the explicit-apply launch phase still covers `would_launch` profiles; the
  checkpoint cannot distinguish a remove error from an already-removed desktop
  and reports a bounded residual instead of guessing; QML runtime was validated
  only by build-time compilation.
- Missing evidence: none required by this envelope. Live desktop/launch/
  placement behavior, M3 physical five-zone observation, full G4, and M5
  remain separate owner routes.
- Plan fidelity: the accepted plan's Slice B design (mutation set,
  default/opt-in split, checkpoint/revert/stop, trigger set, typed launch,
  placement, title-fallback privacy, M4/M5 boundary, no `kwinrulesrc`) is
  implemented as written; the `callDBus` reply form was verified before use.

## Smallest next step

ORCHESTRATOR reconciliation of this implementation-PASS for public candidate
`50872779c619a97be061d7f0df414ccae6bde7e6`, followed only if accepted by a
separate fresh independent code-acceptance Worker for that exact public
commit. No live run, bridge reload, deployment, host enablement, or closure is
authorized by this report.

Orchestration critique:

MEASURED: The installed KWin 6.7.5 scripting implementation supports the
`callDBus` trailing `QJSValue` callback (metaobject signature plus
`isCallable`/`QDBusPendingCallWatcher`/`QJSValue::call` at the reply lambda),
so the `PlacementHint -> (desktop_id, maximize)` and
`ContextReport -> title_fallback_enabled` reply forms are supported; effect is
the planned bridge change is implementable as specified; evidence is the
shipped `libkwin.so.6.7.5`; smallest correction: none.

LEAD: The controller's in-transaction launch classification depends on signal
dispatch during the mutator's bounded per-step waits; a KWin scheduling change
could deliver `desktopCreated` after the transaction flag drops. The explicit
Apply launch phase still launches `would_launch` profiles, so the cheapest
useful check in the later independent acceptance is whether a created-desktop
launch can be missed when the event arrives late.

Explicit non-claims: no acceptance-PASS, deployment-PASS, production
readiness, physical acceptance, M2/G4 closure, M3 closure, autostart,
hibernate/hybrid sleep, general input-remapper coexistence, live
desktop/launch/placement behavior, remapping, deck behavior, M5 integration,
per-key RGB, or measured control-to-zone placement. Tests do not prove live
desktop, compositor, or physical device behavior. This report does not claim
that Session 27 was an independent Worker result.

Logical-whole closure: not-closed

Authority for this Worker expires at this terminal report.
