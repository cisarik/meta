### Report for ORCHESTRATOR_CHAT

Logical whole identity: g213-contextdeck-workspace-session-manager
Worker session ordinal: 08
Worker exchange ordinal: 01
Persistent role identity: WORKER

```text
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Acceptance Worker
Phase: acceptance
Task identity: CONTEXTDECK-M4-SLICE-B-CODE-ACCEPTANCE
Native planning mode: not-used
status: PARTIAL
Phase-qualified result: not-applicable
Result artifact or commit: 50872779c619a97be061d7f0df414ccae6bde7e6 (reviewed; not accepted)
Result evidence: independent read-only acceptance of the exact public candidate; A1 and A3–A7 PASS; A2 FAIL on one runtime step-gating deviation; A8 FAIL on two documentation mismatches; L1 confirmed non-blocking; L2 disproved; focused 8/8 and full 21/21 registered CTest pass from the detached public candidate
Report justification: final-acceptance
```

Acceptance and Correction Record (as issued and verified; this Worker is the
fresh independent acceptance Worker):

```text
Acceptance candidate: 50872779c619a97be061d7f0df414ccae6bde7e6
Acceptance owner map: accepted M4 plan in 01_report_00.md completed by 01_report_01.md; Slice A implementation 02_implementation_00.md/02_report_00.md accepted via 05_report_00.md; Slice B preflight 06_report_00.md (PASS); Slice B implementation 07_implementation_00.md/07_report_00.md
Acceptance allowlist: read-only inspection of the exact candidate, the 35 changed product paths between aca6c68... and 5087277..., directly referenced unchanged owner paths, pinned AP, and the public M4 continuity records named by the prompt
Acceptance risk claims: exact default/opt-in mutation split and ordering; checkpoint/revert ownership and stop rules; in-transaction desktopCreated trigger classification; typed launcher with test seam, debounce, and bounded retry; identity-wins placement through the bridge with no kwinrulesrc; live-caption privacy guard; truthful scope and documentation
Acceptance control matrix: A1 through A8
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none at issuance; one additional consequence of L1 classified in this report
Out-of-scope observations: ledger-candidates only
```

Code acceptance of any kind is not live desktop or physical acceptance. This
review establishes nothing about M2/G4 closure, M3 closure, deployment,
production readiness, G3 re-audit, autostart, hibernate/hybrid sleep, general
input-remapper coexistence, live desktop/launch/placement behavior, M5 behavior,
per-key RGB, or measured control-to-zone placement.

## Independence and session gate

- Genuinely fresh session: this Worker did not plan, implement, repair, accept,
  or report any part of M4 and did not participate in M1/M2/M3. The only inputs
  were the complete delivered prompt, fresh disposable public clones, the
  pinned AP, and the staged trace artifacts at the exact persistence
  destinations. Exact coordinates 08/01 were verified; no ancestry from the
  implementation session was inherited.
- Native Plan Mode: OFF and not used for any part of this review; no native plan
  approval was claimed as authority.
- Internal delegation / subagents: prohibited and not used. One accountable
  Worker produced this report. Network use was limited to the two canonical
  HTTPS ref reads and one canonical HTTPS clone pair.
- All substantive inspection and validation used fresh disposable Worker-owned
  clones with build products outside the product checkout; no COOPERATOR
  checkout was used as acceptance evidence. One transparent near-miss is
  recorded below.

## Immutable identities, provenance, and scope

- Canonical product `https://github.com/cisarik/contextdesk`, branch `main`.
  Direct `git ls-remote refs/heads/main` readback at preflight and again at the
  final check = `50872779c619a97be061d7f0df414ccae6bde7e6`, equal to the
  detached clone HEAD. Required parent = `aca6c68542bbc9f1b8ee891415a04b0a95e8372e`
  (the accepted Slice A candidate). Candidate subject: `Implement M4 Slice B
  workspace mutation and typed launch`. No alternate commit, mirror, stale
  remote-tracking ref, or local retained clone was used.
- AP gitlink and `.ap` checkout both
  `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`; `./.ap/ap doctor` = PASS, resolved
  governing variant `stable`, `.ap` submodule clean. The gitlink is unchanged
  across `aca6c68...5087277` (empty diff for `.ap`).
- Candidate changed-path set: exactly the 35 required product paths (sorted-set
  equality, no additions or omissions): `CMakeLists.txt`, `README.md`,
  `ROADMAP.md`, `docs/adr/0002-host-desktop-mutation-authority.md`,
  `docs/adr/0004-typed-application-launch.md`, `docs/architecture.md`,
  `docs/operations.md`, `docs/specification.md`, `docs/testing-m4.md`,
  `kwin/contextdeck-bridge/contents/code/main.js`,
  `kwin/contextdeck-bridge/metadata.json`, `src/app/AppController.cpp`,
  `src/app/AppController.h`, `src/context/ContextReceiver.cpp`,
  `src/context/ContextReceiver.h`, `src/context/WorkspaceReceiver.cpp`,
  `src/context/WorkspaceReceiver.h`, `src/workspace/ApplicationLauncher.cpp`,
  `src/workspace/ApplicationLauncher.h`, `src/workspace/DesktopMutator.cpp`,
  `src/workspace/DesktopMutator.h`, `src/workspace/PlacementResolver.cpp`,
  `src/workspace/PlacementResolver.h`, `src/workspace/WorkspaceCheckpoint.cpp`,
  `src/workspace/WorkspaceCheckpoint.h`, `src/workspace/WorkspacePlan.cpp`,
  `src/workspace/WorkspacePlan.h`, `tests/unit/test_application_launcher.cpp`,
  `tests/unit/test_placement_resolver.cpp`,
  `tests/unit/test_workspace_lighting.cpp`,
  `tests/unit/test_workspace_mutator.cpp`,
  `tests/unit/test_workspace_receiver.cpp`, `ui/ApplicationsPage.qml`,
  `ui/DiagnosticsPage.qml`, `ui/WorkspacePage.qml`. Diff totals: 35 files,
  `+3885/-142`; `git diff --check aca6c68..5087277` clean; product worktree
  clean before, during, and after all build/test activity (all build products
  outside the checkout). No `.ap`, broker, broker IPC, RGB transport,
  `ControlCatalog`, packaging, license, hardware-evidence, lockfile, generated,
  or host path changed; no dependency beyond `KF6::Service` and `KF6::KIOGui`
  was added.
- Canonical META `https://github.com/cisarik/meta.git`. Direct public
  `refs/heads/main` readback at preflight and final check =
  `f4d2d37d5edc18570efd4af04c530a9527427bc5`, equal to the detached clone HEAD
  and to the required baseline. Ancestry verified: `6c1d6c6` and `6f14316` are
  ancestors; `f4d2d37` adds only two unrelated `projects/ap/09/...` files; no
  contextdesk M4 artifact changed. Every earlier M4 pair commit (`6f14316`,
  `c7e1b73`, `640b65d`, `06439c9`, `f64c634`, `977c841`, `6c1d6c6`) adds
  exactly its own two files and nothing else. META clone worktree clean; all
  trace directories are real directories, not symlinks.
- Required implementation prompt hash `07_implementation_00.md` =
  `48d20c7be5f0a95555fc4b61abe58e4f146adad1867df5f56a03b76ad758ed48` and
  required implementation report hash `07_report_00.md` =
  `910ff7432bea944cce7473e30f2ed66c3fabc48b6cca9dc3d9692fd6d0cc8c93`: both
  recomputed and equal; both files were read back completely (560 and 376
  lines). The 07 pair first-add archival state: **not public at review time** —
  no public ref contains either file (public M4 trace ends at `06_*`; the only
  later public commit adds unrelated `projects/ap/09/...` paths). The two files
  exist at the exact trace destination as staged regular files in the
  COOPERATOR-owned META working tree, untracked, pending the COOPERATOR-owned
  first-add. No retargeting occurred. The archival state is reported truthfully
  and is consistent with the configured `wait-for-report` contract; it is not a
  candidate defect.
- Issued acceptance prompt `08_acceptance_00.md` is present at its exact
  destination in the same working tree, was read back completely (489 lines),
  and matches the delivered prompt field-for-field including coordinates,
  authority fields, identities, matrix, leads, validation, trace, and terminal
  contracts. Persisted-file SHA-256
  `1036b892930a4e9a31a8b5fd4fd30e4f2c49622921cf33e2d4c5dee3f2904c21` (hash of
  the persisted file, not of the chat transport). No collision and no differing
  content existed.

## A1–A8 acceptance matrix

### A1 — Identity, provenance, and scope: PASS

All identities above verify exactly: product candidate/parent/public ref,
AP pin plus `ap doctor` PASS/`stable` and unchanged gitlink, META baseline
ancestry and pair integrity, implementation prompt/report byte hashes, complete
readbacks, exact 35-path set equality, clean checkouts, and no scope escape
(no `.ap`, broker, RGB transport, `ControlCatalog`, packaging, license,
hardware, lockfile, generated, extra-dependency, or host change; the only new
build dependency is the authorized `KF6Service`/`KF6KIO` pair). The 07 pair and
the 08 prompt are prepared but not yet public, exactly as the prompt anticipated;
archival remains COOPERATOR-owned. Blocking: no.

### A2 — Desktop mutation executor and default/opt-in split: FAIL

- Default Apply is correctly create-only and trailing: `DesktopMutator::apply`
  collects only `plan.desktops` entries with `create`/`rename`, sorts creates
  and renames ascending by ordinal, passes `position = ordinal - 1`, and sets
  `rows`/`wrapping` only when the preview diff flags are true
  (`src/workspace/DesktopMutator.cpp:203-313`; test
  `defaultApplyCreatesConditionalRenamesSetsRowsAndWrapping` asserts ordering
  and `matchingPlanWritesNothing` asserts zero calls when the diff is empty).
- `removeDesktop` is never in the default path and never drift-triggered: it
  runs only when `options.removeExtras` is true and only for observed ordinals
  above the desired count, descending
  (`src/workspace/DesktopMutator.cpp:233-244, 326-333`; tests
  `excludedRemoveAndCurrentByDefault`, `optInCurrentAndRemoveRunLast`). The
  optional `current` switch likewise requires `options.switchCurrent`.
- No mutation on `currentChanged` or user-initiated desktop changes, no
  polling: the only production entry point is
  `AppController::applyWorkspaceSession`; `WorkspaceReceiver` signals are routed
  only to checkpoint recording while `m_applyRunning`, never to a mutation. The
  existing receiver request-ownership discipline is preserved (the Slice B diff
  adds one payload-classification branch inside `onInvalidatingMessage`; no
  change to coalescing, one-in-flight, owner generation, stale-reply rejection,
  or `GetAll`).
- No `kwinrulesrc` code path exists anywhere in the candidate.
- **Confirmed defect (blocking for this row): the `current` step is not
  fail-closed.** In `src/workspace/DesktopMutator.cpp:315-324`, a failed or
  timed-out `Properties.Set` on `current` only records
  `residualClass = "current-switch-skipped"`; it does not stop the sequence and
  does not trigger the revert path. Execution continues to the opted-in
  `removeDesktop` removals and the transaction returns `ok = true`, after which
  the controller still runs `launchPlannedProfiles(plan)`. This contradicts the
  accepted implementation contract (`07_implementation_00.md` §1: "every step
  gates the next; any error stops the sequence and triggers the revert path"),
  the acceptance control ("any D-Bus error or timeout stops the sequence"), and
  the candidate's own changed documentation (`docs/specification.md:188-189`,
  `docs/architecture.md:149-150`). No persistent regression covers this
  behavior (`setFailMethod` exists in the test fake but no test exercises a
  `current` failure). Behavioral consequence: after a `current` D-Bus error the
  desktop configuration is left partially applied, destructive extra removals
  may still proceed, and applications may still be launched under a transaction
  that the contract says must abort and revert. No test failure exists today;
  the defect is the code-versus-contract semantics. Blocking: yes (contract
  defect; a correction here changes runtime behavior, so per the
  acceptance/correction rules it routes to full-fresh re-acceptance, not scoped
  re-acceptance).

### A3 — Checkpoint, revert, and stop rules: PASS

- Checkpoint is user-local and never the profile document, logs, or META:
  `AppController` sets it beside the store root
  (`src/app/AppController.cpp:198`), `WorkspaceCheckpoint` uses atomic
  `QSaveFile` with `setDirectWriteFallback(false)`, user-only permissions
  (`ReadOwner|WriteOwner`), bounded parse, and overwrite-per-Apply
  (`src/workspace/WorkspaceCheckpoint.cpp:163-218`). Path-placement accuracy is
  a separate documentation defect tracked under A8 (the documented path is one
  directory below the actual one); the row's stated criteria — user-local, not
  the profile document/logs/META — are met.
- Write-and-verify happens before the first mutation: `apply()` persists the
  checkpoint before any D-Bus mutation and returns without mutating on failure
  (`DesktopMutator.cpp:255-267`); the test
  `checkpointWrittenBeforeFirstMutationAndUserOnly` registers an
  `onBeforeMutation` probe that observes the file already present and verifies
  group/other permission bits are absent and the created UUID is recorded.
- Revert removes exactly this Apply's created UUIDs and never a desktop it did
  not create: `runRevert` iterates only `data.createdIds`
  (`DesktopMutator.cpp:374-382`); `revertRemovesOnlyThisApplyUuids` lets a
  user-created extra appear after Apply and confirms revert removes only
  `gen-1` and preserves the user desktop. Names/rows/wrapping are restored from
  the checkpoint; the `current` restore is skipped when the checkpoint UUID is
  absent with bounded residual `current-restore-skipped`
  (`DesktopMutator.cpp:384-427`; test `currentRestoreSkippedWhenUuidAbsent`).
  Lifecycle: retained until a successful revert or the next Apply and deleted
  on success (`DesktopMutator.cpp:429-440`; tests
  `checkpointOverwrittenPerApply`, `abortOnRenameErrorRunsRevert`). A failed
  revert preserves the checkpoint and reports a bounded residual class rather
  than guessing; no test exercises a hard revert failure, but the code path is
  explicit and fail-closed.
- Assignment rebinding stays ordinal-based: the profile schema stores
  `desktop_ordinal` only; the mutator and `PlacementResolver` map
  ordinal-to-live-UUID from the fresh observation.
- Fail-closed preconditions are present in `applyWorkspaceSession`: explicit
  invocation, `workspace_management_enabled`, a valid session, `Available`
  observation with no pending refresh and no in-flight logical request,
  unchanged owner generation, unchanged live-preview fingerprint, mutator-side
  verified checkpoint, and explicit option booleans
  (`src/app/AppController.cpp:1697-1760`; tests `applyRefusalsAreFailClosed`
  cover `management-disabled` and `preview-stale`). Revert never kills an
  application and does not move open windows back (no such call exists; the
  behavior is also disclosed in the UI, specification, and operations).
  Blocking: no.

### A4 — In-transaction launch trigger classification: PASS

- The event surface distinguishes an in-transaction `desktopCreated` without a
  second `GetAll` or polling: `WorkspaceReceiver::onInvalidatingMessage` parses
  the existing subscription payload and emits payload-free
  `desktopCreatedObserved(id, position)`
  (`src/context/WorkspaceReceiver.cpp:389-425`; test
  `desktopCreatedEmitsEventSurface`), and `currentChanged` emits nothing
  (`currentChangedDoesNotEmitDesktopCreated`). Position semantics are
  consistent: snapshot ordinals are assigned by sorting raw `position` values
  and adding 1 (`WorkspaceReceiver.cpp:744-757`), the mutator expects
  `ordinal - 1`, and the launch path re-derives `position + 1`.
- Only the in-transaction event and explicit Apply launch: the controller
  routes `desktopCreatedObserved` to the mutator only while `m_applyRunning`,
  the mutator re-emits only for expected create positions while `m_applying`,
  and `onDesktopCreatedInTransaction` launches only for that ordinal
  (`src/app/AppController.cpp:1767-1830`). Session-app start, Plasma login,
  `currentChanged`, and user-created desktops launch nothing
  (`applyLaunchesInTransactionDesktopProfilesOnce` asserts exactly one launch
  and then asserts a user-created desktop and `currentChanged` add none).
- The created UUID is recorded in the checkpoint before the next step
  (`DesktopMutator::recordCreatedDesktop`, `DesktopMutator.cpp:67-81`;
  verified by `checkpointWrittenBeforeFirstMutationAndUserOnly` and
  `checkpointOverwrittenPerApply`). No desktop identity is logged anywhere in
  the new path. Blocking: no.

### A5 — Typed launcher: PASS

- Only a validated `.desktop` id is accepted: `ApplicationLauncher::requestLaunch`
  and `retryForDesktopCreated` reject empty or invalid ids via
  `workspaceDesktopIdLooksValid` (character allow-list, no shell
  metacharacters; `src/core/Types.h:208-229`), and tests
  `invalidDesktopIdsAreRejected` reject `sh -c ...`, `systemd-run --user ...`,
  `kstart ...`, and absolute paths. By construction there is no shell,
  `QProcess` of `Exec=`, `systemd-run`, or `kstart` call anywhere in the
  launcher.
- `KService::serviceByStorageId` plus `KIO::ApplicationLauncherJob` are used in
  the production path (`ApplicationLauncher.cpp:148-163`); `KApplicationTrader`
  is named in the specification but not called — the accepted plan's decision
  is a typed `KService` id, so this is a wording nuance, not a defect. The test
  seam (`setInvokerForTest`) is the only path used by tests; no real job is
  started in tests.
- Skip-if-already-running, per-profile debounce, and one bounded retry are
  implemented and tested: `WorkspaceLaunchDebounce::tryAttempt` /
  `tryBoundedRetry` (`WorkspacePlan.cpp:178-196`), plan intents
  (`AlreadyRunning` skip, `MissingDesktopFile`), and
  `test_application_launcher` cases `nonLaunchIntentsNeverInvoke`,
  `invokesSeamWithTypedIdAndDebounces`, `boundedRetryOnlyAfterFailureBeforeWindow`,
  `transactionEndResetsAttempts`. Blocking: no.

### A6 — Placement, bridge, and live-caption privacy: PASS

- `PlacementResolver` implements identity-wins, fallback-only-when-both-flags,
  empty-id no-op, and maximize selection, gated on management enabled, a valid
  session, and an `Available` observation
  (`src/workspace/PlacementResolver.cpp:9-33`; `test_placement_resolver` covers
  identity-wins, both-flag gating, empty id/unavailable observation, unassigned
  identity, and management disabled).
- `ContextReceiver` exposes `PlacementHint(...) -> (desktop_id, maximize)` and
  the optional `TitleHint`; the bridge sets `window.desktops = [matched id]`
  and calls `window.setMaximize(true, true)`; the `ContextReport` six input
  arguments are unchanged and its reply now carries the title-fallback boolean
  (`src/context/ContextReceiver.cpp:182-320`; `kwin/contextdeck-bridge/contents/code/main.js:104-169`;
  `contextReceiverPlacementHintUsesProviderAndConsumesCaption`,
  `contextReportReplyCarriesTitleFallbackFlag`). Empty id is a no-op in both
  receiver and bridge.
- Captions: `TitleHint` is sent by the bridge only while the learned
  title-fallback flag is true, is bounded at both ends (64 characters in JS,
  256 bytes in D-Bus with rejected oversized input), is held only until the
  next resolution consumes it (`ContextReceiver::takeTitleHint`), is discarded
  on non-matching reports and bridge loss, is never logged (only bounded
  rejection warnings without arguments), and never enters diagnostics or the
  profile document. The live-caption privacy guard exists and is non-vacuous:
  `liveCaptionPrivacyGuard` demonstrates the caption actually reaches and
  selects the fallback profile, then asserts the sentinel is absent from
  diagnostics and every captured log message; `contextReceiverDoesNotLogTitleHintArguments`
  asserts the D-Bus path never logs the caption. Blocking: no.
- KWin `callDBus` trailing-callback reply form: independently re-confirmed from
  the installed build (details in the dedicated section below).
- `metadata.json` is valid JSON, version `0.2.0`, and its description matches
  the final bridge behavior (captions only when title fallback is enabled; no
  PIDs/executable paths). Blocking: no.

### A7 — Causal regression evidence: PASS

- Test bodies were inspected, not names or counts. Required coverage maps to
  persistent regressions: mutation ordering/step gating and abort-on-error
  (`test_workspace_mutator`), no-op on an empty diff, excluded
  remove/current, opt-in ordering, checkpoint write-before-mutation/permissions/
  overwrite/cleanup, revert exactly-this-Apply, `current`-restore skip,
  in-transaction trigger versus user-created/`currentChanged` non-triggers,
  launcher seam decisions/debounce/retry, placement identity/gating/no-op/
  maximize, controller refusals, and both caption-privacy guards.
- D-Bus tests use a fake desktop-manager service on a private
  `dbus-run-session` bus (`test_workspace_receiver`, `test_workspace_mutator`,
  `test_workspace_lighting` are registered under `dbus-run-session` with
  `QT_QPA_PLATFORM=offscreen;QT_DISABLE_SESSION_MANAGER=1`); the launcher is
  exercised only through its injected seam; `test_placement_resolver` and
  `test_application_launcher` are pure. No test starts the session
  application, OpenRGB, the broker, a device, a real KWin connection, or a real
  application launch.
- The focused and complete registered suites pass from the detached public
  candidate in a fresh external build directory with real counts (focused
  `100% tests passed out of 8`, total 66.34 s; full `100% tests passed out of
  21`, total 68.56 s; configure and build exit 0, 158/158 targets, zero
  compiler warnings).
- No persistent coverage required by the implementation prompt is missing.
  Note: the A2 defect (current-step soft failure) has no regression; a
  correction should add one. Blocking: no for this row.

### A8 — Documentation and bounded claims: FAIL

- Positive evidence: specification, architecture, operations, testing-m4, and
  the ADRs describe the implemented mutation set, default/opt-in split,
  checkpoint/revert/stop, triggers, typed launch, placement, privacy,
  `kwinrulesrc` rejection, and the M4/M5 boundary. The exact M2 park wording is
  preserved in `README.md` and the exact M3 park wording in `README.md` and
  `ROADMAP.md`:
  > The named live G4 slices are accepted, but the M2 logical whole remains
  > open. M2 is parked with G3 host-mitigated on the authorized reference host;
  > the next bounded whole is M4 workspace session manager.
  > M3 workspace-aware lighting is code-accepted on `502ae75...`; its physical
  > five-zone IRL observation is deferred by explicit COOPERATOR decision. M3
  > is not closed, and code acceptance is not physical acceptance.
  The candidate is described only as an implementation candidate ("not accepted
  and not live-verified"); no physical, deployment, production, autostart, M5,
  per-key, or whole-G4 claim appears.
- **Confirmed documentation defect 1 (stale UI claim).**
  `docs/specification.md:555` still states for the `Plochy` page: "Apply
  hidden/disabled until a later authorized slice". Slice B implements and
  enables Apply (with preconditions) plus checkpoint revert; the same document
  and `ui/WorkspacePage.qml` contradict this row. This is exactly the
  documentation-drift class the implementation prompt required to fix.
- **Confirmed documentation defect 2 (wrong checkpoint path).**
  `docs/specification.md:196-197` and `docs/operations.md:664-665` state the
  checkpoint as `$XDG_CONFIG_HOME/contextdeck/workspace-checkpoint.json`
  (fallback `$HOME/.config/contextdeck/workspace-checkpoint.json`), and the
  implementation report states the same. The code writes
  `m_store.configRoot() + "/workspace-checkpoint.json"`
  (`src/app/AppController.cpp:198`) while `ProfileStore::configRoot()` is the
  configuration root itself (`src/core/Persistence.cpp:932-942`, with
  `documentPath()` adding `/contextdeck/profiles.json` at
  `src/core/Persistence.cpp:944-947`). The actual production path is therefore
  `<config root>/workspace-checkpoint.json`, one directory above the documented
  and preflight-intended product directory. The file is still user-local with
  user-only permissions and is not the profile document, logs, or META, but the
  documented identity is false and the preflight intent ("under the product
  config root") is not met. No test covers the production path because the
  tests set their own temporary checkpoint path.
- Both defects require a documentation correction; defect 2 also implies a
  runtime placement decision (either move the file under the product directory
  or amend the documented path), which is a COOPERATOR/ORCHESTRATOR decision
  because it changes runtime behavior. Blocking: yes (documentation does not
  match the code as required by this row).

## Mandatory adversarial leads

### L1 — late in-transaction `desktopCreated` dispatch: confirmed (non-blocking)

- Exact interleaving: the D-Bus method call is awaited inside a local event
  loop (`DesktopMutator::call`, `DesktopMutator.cpp:83-106`). The created UUID
  is recorded and the launch trigger fires only if the `desktopCreated` signal
  is dispatched while `m_applying` is true and before `m_expectedCreatePositions`
  is cleared (`recordCreatedDesktop`, `DesktopMutator.cpp:67-81`;
  `AppController::onWorkspaceDesktopCreated`, `AppController.cpp:1767-1773`).
  The test fake emits the signal before sending the method reply, so this path
  is exercised; a KWin scheduling change that delivers the signal after the
  reply would cause `recordCreatedDesktop` to return early.
- Launch consequence: a create-triggered launch can indeed be missed, but the
  explicit-Apply phase covers it. `launchPlannedProfiles(plan)` runs
  synchronously immediately after `apply()` returns, before any queued
  late-signal dispatch can be processed, and `hasAttempted` prevents a
  duplicate; a profile assigned to the new ordinal is still launched once. The
  only launch-specific loss is the bounded retry for a first job that failed
  before its window appeared. This matches the implementation report's
  disclosure.
- Checkpoint consequence (new evidence beyond the report's disclosure): the
  same late signal is also what records the created UUID. If it arrives after
  the transaction, the UUID is absent from `created_ids`, so a later revert
  would remove only the recorded desktops, leave that created desktop in place,
  and still report a successful revert. The residual is bounded by the number
  of creates in that Apply, is the safe direction (under-removal, never
  over-removal), and requires an abnormal dispatch order; it is not a
  demonstrated failure of the tested path. It is disclosed here as a residual
  and a ledger candidate for the correction/handoff, not as a blocking defect.
- Blocks acceptance: no.

### L2 — revert over-removal and default-remove safety: disproved

- Revert can only remove UUIDs recorded in `created_ids` for expected create
  positions (`DesktopMutator.cpp:69-75, 374-382`). A pre-existing desktop is
  never in `created_ids`; a user-created extra after Apply is preserved, as
  `revertRemovesOnlyThisApplyUuids` proves (removes `gen-1`, keeps `user-x`).
- Default Apply never removes: extras are computed and removed only under
  `options.removeExtras`, and `excludedRemoveAndCurrentByDefault` plus
  `matchingPlanWritesNothing` assert zero `removeDesktop` calls on default
  paths. `ui/WorkspacePage.qml` gates the opt-in behind a dedicated checkbox
  and a modal confirmation ("removed desktops cannot be restored as the same
  desktops"; `WorkspacePage.qml` Apply handler opens `removeExtrasDialog` and
  only its `onAccepted` passes `removeExtras = true`).
- A failed or partial revert preserves the checkpoint and reports a bounded
  residual instead of guessing: hard residuals return before
  `m_checkpoint.remove()` with `revertFailed = true` and the first bounded
  error class (`DesktopMutator.cpp:429-440`), surfaced as `revert-failed` and
  `workspaceLastResidual`.
- Residual (not blocking): because recording is position-based, a contrived
  concurrent user-created desktop arriving at a pending create position during
  the sub-second transaction could be recorded and later removed by revert.
  This requires manual desktop creation exactly inside the transaction window,
  is not reachable by the tested or documented flows, and leaves no open
  correctness question for the accepted normal path. Blocks acceptance: no.

## Validation evidence

From the exact detached candidate with build products outside the checkout:

```text
configure: cmake -S . -B <external-build> -G Ninja          -> exit 0
build:     cmake --build <external-build>                    -> exit 0, 158/158 targets, 0 warnings

focused:   ctest --test-dir <external-build> --output-on-failure \
             -R '^(test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_plan|test_openrgb_protocol|test_workspace_mutator|test_placement_resolver|test_application_launcher)$'
           => exit 0; 100% tests passed out of 8; total 66.34 s
              (test_workspace_receiver 65.60 s; test_workspace_mutator 0.68 s;
               test_application_launcher 0.02 s; test_placement_resolver 0.00 s)

full:      ctest --test-dir <external-build> --output-on-failure
           => exit 0; 100% tests passed out of 21; total 68.56 s
              (includes test_workspace_lighting 0.59 s with the new
               apply/launch/refusal/privacy-guard regressions)

diff gates: git diff --check aca6c68..5087277 -> clean
            git status --short -> clean before, during, and after validation
```

Private-bus classification: `test_workspace_receiver`, `test_workspace_mutator`,
and `test_workspace_lighting` ran under the registered `dbus-run-session` route
with synthetic fake desktop-manager services on a private session bus and
`QT_QPA_PLATFORM=offscreen;QT_DISABLE_SESSION_MANAGER=1`; no real KWin was
connected to, replaced, or mutated. `test_profile_*`, `test_placement_resolver`,
and `test_application_launcher` are pure/bus-free. No application launch,
desktop mutation, bridge reload, OpenRGB connection or CLI, device open, broker
start/ARM/grab, service change, package install, `/etc`/udev change, or host
operation occurred.

First causal failure in executed validation: none. The blocking findings are
inspection defects (A2 runtime semantics, A8 documentation). No test was
weakened, skipped, or looped.

## KWin `callDBus` reply-form independent confirmation

Independently confirmed from the installed KWin build, without any live session
probe:

- Installed `libkwin.so.6.7.5` SHA-256
  `02737e1fb3a6b5923fdfc37de2d57dc65d19f9bfbe5f33b6dedb41dc7203da61`, matching
  the implementation report's recorded identity.
- The shipped metaobject string table for the scripting interface contains
  `callDBus` together with `service`, `path`, `interface`, `method`, `QJSValue`,
  and `arg1`–`arg9`, matching the declared variadic `QJSValue` argument shape.
- The dynamic symbol table contains undefined references to
  `QDBusPendingCallWatcher` (constructor, `finished`, `staticMetaObject`) and to
  `QJSValue::isCallable()`, `QJSValue::isUndefined()`, `QJSValue::isError()`,
  and `QJSValue::call(QList<QJSValue>)`.
- A bounded disassembly inspection of the installed library locates a single
  function performing `QDBusMessage::createMethodCall` →
  `setArguments` → `QDBusConnection::sessionBus` → `asyncCall` →
  `QDBusPendingCallWatcher` construction → `QObject::connectImpl` on
  `finished` → `QJSValue::isUndefined`/`isCallable` checks, with
  `QJSValue::call` invoked on the reply path.
- Conclusion: the trailing-callback reply form used by the final bridge
  (`ContextReport` reply boolean and `PlacementHint` `(desktop_id, maximize)`)
  is supported by the installed build. The bridge's empty-id no-op and
  `typeof` guards keep older peers safe. No synthetic probe was needed.

## Temporary probe

not-used. All findings were settled by static source/test inspection, the
existing registered tests, the diff/identity commands, and installed-build
inspection; no disposable product copy was created, so no probe cleanup was
required and no product or META diff resulted.

## Confirmed defects, missing persistent tests, disproved concerns, residual risks, deviations, ledger candidates

- Confirmed defects:
  1. A2 — `DesktopMutator::apply` does not stop/revert on a failed or timed-out
     `current` `Properties.Set`; it continues (including opted-in removals) and
     reports success-with-residual, contradicting the accepted contract and the
     changed docs (`src/workspace/DesktopMutator.cpp:315-324`).
  2. A8 — `docs/specification.md:555` retains the stale Slice A claim that
     Apply is hidden/disabled.
  3. A8 — the documented checkpoint path
     (`docs/specification.md:196-197`, `docs/operations.md:664-665`, and the
     implementation report) is `$XDG_CONFIG_HOME/contextdeck/workspace-checkpoint.json`,
     while the code writes `<config root>/workspace-checkpoint.json`
     (`src/app/AppController.cpp:198`).
- Missing persistent tests: none required by the implementation prompt are
  absent. A regression for the A2 `current`-failure stop/revert behavior should
  accompany any correction.
- Disproved concerns: L2 over-removal and default-remove safety; empty-diff
  mutation; trigger on user-created desktop or `currentChanged`; caption
  logging/persistence; launcher shell rejection; placement bypass of the
  both-flags gate.
- Residual risks: L1 late-dispatch launch miss (covered by the explicit-apply
  phase) and its bounded checkpoint under-recording (safe direction, partially
  disclosed); QML runtime behavior is only build-time-validated; no live
  desktop/launch/placement behavior is established by this code acceptance.
- Deviations: the 07 prompt/report pair and the 08 prompt are prepared but not
  yet public (wait-for-report); prompt byte identity is asserted against the
  persisted staged file, since a byte-level chat-transport comparison is not
  observable from here. No retargeting occurred.
- Out-of-scope ledger candidates (non-blocking, no acceptance impact): the
  ADR 0002/0004 "accepted for the M4 tree" status phrasing carried from Slice A;
  the `.desktop`-suffix desktop-id predicate accepting trivially short forms;
  `KApplicationTrader` named in the specification but not used in code; the L1
  checkpoint-disclosure gap; QML runtime not executed.

## Resolved Execution Issues / Near-Misses

- One, disclosed for completeness: before creating the disposable clones, the
  Worker read the local workspace checkout's HEAD once (`git rev-parse HEAD`)
  as an environment sanity check; it happened to show the candidate commit. All
  substantive evidence, builds, tests, and identity checks came from the fresh
  disposable clones and the staged trace files; no mutation and no acceptance
  evidence came from that checkout. No other near-miss occurred.
- No destructive Git operation, package install, service/device action, or host
  change was attempted.

## Pre-Existing Failure Classification

none. No registered test was failing at the candidate and none failed during
this review; configure/build emitted zero warnings. The Qt harness's
`org.kde.kscreen.dpms` library warning previously noted for this project is
unrelated pre-existing noise and did not appear as a test failure.

## META trace persistence and readback

- Prompt `projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/08_acceptance_00.md`
  was persisted by the ORCHESTRATOR before delivery as a regular file at the
  exact destination (real directories, no symlinks); it was read back
  completely (489 lines) and matches the delivered prompt field-for-field.
  Persisted-file SHA-256:
  `1036b892930a4e9a31a8b5fd4fd30e4f2c49622921cf33e2d4c5dee3f2904c21`. No
  collision, no differing content, and nothing was overwritten.
- Report `projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/08_report_00.md`
  was absent before this write and is the only file this exchange prepared. It
  was written once and read back completely immediately after the write
  (header, coordinates, record fields, status, matrix, leads, validation, KWin
  confirmation, defects, persistence, critique, and the singleton terminal
  lines verified).
- The implementation pair `07_implementation_00.md`/`07_report_00.md` is
  present at the exact destination in the COOPERATOR-owned META working tree
  with the required byte hashes, but is not yet published in any ref; META Git
  publication of that pair and of this prompt/report pair remains
  COOPERATOR-owned. META Git was not staged, committed, pushed, pulled, merged,
  rebased, switched, or otherwise mutated by this Worker; no META ref or
  history changed.

## Smallest next step

ORCHESTRATOR reconciliation of this PARTIAL review. One smallest coherent
correction boundary is named without granting it: (a) make the optional
`current` step fail-closed in `DesktopMutator::apply` (stop and run the revert
path on error/timeout, matching the accepted contract and existing docs), with
one focused regression; (b) resolve the checkpoint path mismatch by either
placing the checkpoint under the product directory or amending the documented
path and the report claim consistently; (c) update `docs/specification.md:555`
to describe the implemented Apply/revert controls instead of "hidden/disabled".
Because (a) and any path move change runtime behavior, the correction routes to
full-fresh re-acceptance, not scoped re-acceptance. No live IRL run, bridge
reload, deployment, or closure is authorized by this report.

Orchestration critique:

MEASURED: `DesktopMutator::apply` treats a failed/timed-out `current`
`Properties.Set` as a soft residual and continues to the opted-in removals and
the post-apply launch phase (`src/workspace/DesktopMutator.cpp:315-324`), while
the implementation prompt, the acceptance control, and the candidate's own
changed docs all require any D-Bus error to stop and revert
(`docs/specification.md:188-189`, `docs/architecture.md:149-150`); effect is a
partially applied desktop configuration that can still launch applications
under an aborted-by-contract transaction; evidence is the code path plus the
absence of any `current`-failure regression; smallest correction is the
one-branch fail-closed change with one focused test.

LEAD: the late `desktopCreated` interleaving also means a created UUID can be
absent from `created_ids` if KWin ever delivers the signal after the method
reply, so a later revert could silently under-remove that desktop; the cheapest
useful check is a disposable fake-service probe that emits `desktopCreated`
after the reply and inspects the resulting checkpoint, or a COOPERATOR-owned
live confirmation of KWin dispatch order during the IRL run.

Explicit non-claims: no acceptance-PASS, implementation-PASS at any later
phase, publication-PASS, deployment-PASS, production acceptance, physical
acceptance, whole-M2/G4 closure, independent G3 re-audit, autostart,
hibernate/hybrid sleep, general input-remapper coexistence, M3 closure, M3
physical five-zone observation, live desktop/launch/placement behavior,
remapping, deck behavior, M5 integration, per-key RGB, or measured
control-to-zone placement. Tests do not prove live desktop, compositor, or
physical device behavior. Code acceptance is not live desktop or physical
acceptance. Session 27 is not claimed to have been an independent Worker
result. This review demanded no live input, device, desktop, or launch
operation and performed none.

Logical-whole closure: not-closed

Authority for this Worker expires at this terminal report.
