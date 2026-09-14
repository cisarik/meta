### Report for ORCHESTRATOR_CHAT

Logical whole identity: g213-contextdeck-workspace-session-manager
Worker session ordinal: 10
Worker exchange ordinal: 01
Persistent role identity: WORKER

```text
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Acceptance Worker
Phase: acceptance
Task identity: CONTEXTDECK-M4-SLICE-B-FULL-REACCEPTANCE
Native planning mode: not-used
status: PASS
Phase-qualified result: acceptance-PASS
Result artifact or commit: db9ddc1f923f44e26f7f1d58df7446306bbdf64a
Result evidence: full fresh independent read-only re-acceptance of the exact public corrected candidate; A1–A8 all PASS; both leads confirmed non-blocking; focused 9/9 (67.25 s, including test_workspace_lighting and test_workspace_mutator) and full registered CTest 21/21 (68.96 s) from the detached candidate; the two correction regressions and the checkpoint-path regression were independently proven causal by a disposable probe against the un-fixed parent; clean checkouts and exact public identities
Report justification: final-acceptance
```

Acceptance and Correction Record (as issued and independently verified; this
Worker is the required full-fresh independent re-acceptor):

```text
Acceptance candidate: db9ddc1f923f44e26f7f1d58df7446306bbdf64a
Acceptance owner map: accepted M4 plan in 01_report_00.md completed by 01_report_01.md; Slice A implementation 02_implementation_00.md/02_report_00.md accepted via 05_report_00.md; Slice B preflight 06_report_00.md (PASS); Slice B implementation 07_implementation_00.md/07_report_00.md; Slice B independent PARTIAL 08_report_00.md (A2 current-step gating, A8 documentation/path); bounded correction 09_correction_00.md/09_report_00.md
Acceptance allowlist: read-only inspection of the exact candidate, the cumulative 35 changed product paths between aca6c68... and db9ddc1..., directly referenced unchanged owner paths, pinned AP, and the public M4 continuity records named by the prompt
Acceptance risk claims: corrected fail-closed current step; checkpoint placed in the product directory; corrected documentation; and the previously accepted Slice B claims (default/opt-in mutation split and ordering, checkpoint/revert ownership, in-transaction trigger classification, typed launcher, identity-wins placement, live-caption privacy)
Acceptance control matrix: A1 through A8
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1 (this session is the required full-fresh correction re-acceptance)
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none at issuance; none discovered (one trace-side readback limitation classified truthfully under Deviations)
Out-of-scope observations: ledger-candidates only
```

Code acceptance of any kind is not live desktop or physical acceptance. This
review establishes nothing about M2/G4 closure, M3 closure, deployment,
production readiness, G3 re-audit, autostart, hibernate/hybrid sleep, general
input-remapper coexistence, live desktop/launch/placement behavior, M5 behavior,
per-key RGB, or measured control-to-zone placement. Tests do not prove live
desktop, compositor, or physical device behavior.

## Independence and session gate

- Genuinely fresh session: this Worker did not plan, implement, repair, accept,
  or report any part of M4 and did not participate in M1/M2/M3. The only inputs
  were the complete delivered prompt, fresh disposable public clones, the pinned
  AP, and the prompt/trace artifacts at the exact persistence destinations.
  Exact coordinates `10`/`01` were verified; no implementation-session ancestry
  was inherited.
- Native Plan Mode: not used for this session and not used for any part of this
  review; no native plan approval was claimed as authority.
- Internal delegation / subagents: prohibited and not used. One accountable
  Worker produced this report. Network use was limited to the canonical HTTPS
  clone pair and the direct public-ref reads.
- All substantive inspection, builds, and tests used fresh disposable
  Worker-owned clones with build products outside the product checkout. The
  local workspace directory was not used as acceptance evidence; one benign
  orientation near-miss is disclosed under Resolved Execution Issues.

## Immutable identities, provenance, and scope

- Canonical product `https://github.com/cisarik/contextdesk`, branch `main`.
  Direct `git ls-remote refs/heads/main` readback at preflight and again at the
  final check = `db9ddc1f923f44e26f7f1d58df7446306bbdf64a`, equal to the
  detached clone HEAD. Required parent = `50872779c619a97be061d7f0df414ccae6bde7e6`
  (verified equal to HEAD's parent). Candidate subject: `Fix M4 Slice B
  current-step gating and checkpoint path`. Required original Slice B baseline
  `aca6c68542bbc9f1b8ee891415a04b0a95e8372e` resolved in the clone. No alternate
  commit, mirror, stale remote-tracking ref, or local retained clone was used.
- AP gitlink and `.ap` checkout both
  `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`; `./.ap/ap doctor` = PASS, resolved
  governing variant `stable`, `.ap` submodule clean.
- Canonical META `https://github.com/cisarik/meta.git`. Direct public
  `refs/heads/main` readback = `cfd5cee1298b76ad21afd685de9565c8191d6f7b`, equal
  to the required baseline and to the fresh clone HEAD. The correction commit
  `cfd5cee` adds exactly the two `09` pair files and nothing else; the prior
  acceptance pair commit `b25718c` is an ancestor; every earlier M4 pair commit
  (`0475e01`, `6c1d6c6`, `977c841`, `f64c634`, `06439c9`, `640b65d`, `c7e1b73`,
  `6f14316`) adds exactly its own two files. No earlier accepted-plan artifact
  changed; the trace directory and parents are real directories, not symlinks.
- Required artifact byte hashes, all recomputed in the fresh clone and all
  equal: implementation prompt `07_implementation_00.md` =
  `48d20c7be5f0a95555fc4b61abe58e4f146adad1867df5f56a03b76ad758ed48`;
  implementation report `07_report_00.md` =
  `910ff7432bea944cce7473e30f2ed66c3fabc48b6cca9dc3d9692fd6d0cc8c93`;
  prior acceptance report `08_report_00.md` =
  `010fc3e4ba1c864453b2ee0125de2c4946640e08426ba941fb0794d09a098521`;
  correction prompt `09_correction_00.md` =
  `0dc9958cee0ac5dece9581be1c0613d930b469c3af183043f7430bcc3aa8b903`;
  correction report `09_report_00.md` =
  `1f61475821f9603bc3f4ca40c516c6a843819a159025d4b2a49679e402168b8b`.
  All five were read back completely as part of the acceptance.
- Correction commit scope: `git diff --name-only
  5087277...db9ddc1` returns exactly five paths —
  `docs/specification.md`, `src/app/AppController.cpp`,
  `src/workspace/DesktopMutator.cpp`, `tests/unit/test_workspace_lighting.cpp`,
  `tests/unit/test_workspace_mutator.cpp` — matching the required correction
  scope; diffstat `5 files changed, +146/-7`. The full correction diff was
  reviewed hunk by hunk: the fail-closed `current` step, the checkpoint path
  change, the corrected `Plochy` documentation row, and the two new
  regressions; no other change.
- Cumulative candidate scope: `git diff --name-only aca6c68...db9ddc1` sorted
  equals exactly the required 35-path set (set comparison empty-diff, no
  additions or omissions); diffstat `35 files changed, +4025/-143`;
  `git diff --check aca6c68...db9ddc1` clean (exit 0). No `.ap`, broker, broker
  IPC, RGB transport, `ControlCatalog`, packaging, license, hardware-evidence,
  lockfile, generated, or host path changed.
- Dependency scope: the `CMakeLists.txt` diff adds only
  `find_package(KF6Service REQUIRED)` / `find_package(KF6KIO REQUIRED)` with
  `KF6::Service` / `KF6::KIOGui` and the new launcher/checkpoint/placement
  sources and test targets; no other package, no umbrella `KF6`, no
  `extra-cmake-modules`, no lockfile/toolchain change.
- Clean states: product worktree clean before, during, and after all build and
  test activity; `.ap` submodule clean; META clone worktree clean. Build
  products were kept outside the product checkout in a newly created
  Worker-owned temporary directory.
- Toolchain verified without installing anything: CMake 4.4.3, Ninja 1.13.2,
  CTest, `dbus-run-session`, KF6 `KF6Service` and `KF6KIO` CMake config
  packages, Qt 6 / GCC toolchain as shipped. Configure exit 0; build exit 0,
  158/158 targets, zero compiler warnings.
- Required reading: pinned `.ap` RF/acceptance sections, `AP_WORKER.md`,
  `PROMPT_CONTRACTS.md` report/acceptance/trace/expiry sections, product
  `AGENTS.md`/`README.md`/`ROADMAP.md`/specification/architecture/operations/
  testing-m4/ADR 0002/ADR 0004, and the complete public M4 artifacts
  `01_report_00.md`, `01_report_01.md`, `02_implementation_00.md`,
  `02_report_00.md`, `03_report_00.md`, `04_correction_00.md`, `04_report_00.md`,
  `05_report_00.md`, `06_report_00.md`, `07_implementation_00.md`,
  `07_report_00.md`, `08_report_00.md`, `09_correction_00.md`, `09_report_00.md`
  were read. Candidate source/tests/bridge/docs were inspected directly.

## A1–A8 acceptance matrix

### A1 — Identity, provenance, and scope: PASS

- All identities above verify exactly: product candidate/parent/public ref,
  original Slice B baseline, AP pin plus `ap doctor` PASS/`stable`, META
  baseline equality and add-only pair integrity, all five required hashes,
  complete readbacks, correction commit scope (exactly five paths), cumulative
  35-path set equality, clean checkouts, and no scope escape (no broker, RGB
  transport, packaging, license, hardware, lockfile, generated, or host change;
  the only dependency addition is the authorized `KF6Service`/`KF6KIO` pair).
- The issued prompt `10_acceptance_00.md` is present at the exact trace
  destination in the COOPERATOR-owned META working tree as a regular untracked
  file, 469 lines / 23228 bytes, SHA-256
  `a173258a0d6c92c8cc70a3eddfc7e9b379647f7204ae9c1a6a0be1d0f23f1a5a`; it was
  read back completely and matches the delivered prompt field-for-field
  (coordinates, authority/record fields, immutable identities, required
  hashes, 35-path list, A1–A8 matrix, leads, validation, trace block, terminal
  contract, and stop conditions). A mechanical chat-transport byte comparison
  is not observable from inside the session; this is the same disclosed
  verification class as prior M4 exchanges.
- Blocking: no.

### A2 — Desktop mutation executor, default/opt-in split, and fail-closed `current`: PASS

- Default Apply is exactly create + conditional rename + rows/wrapping:
  `DesktopMutator::apply` collects only `plan.desktops` entries with
  `create`/`rename`, sorts both ascending, performs creates with
  `position = ordinal - 1`, then conditional renames by ordinal-to-live-UUID,
  then `rows` and `navigationWrappingAround` only when the plan flags are true
  (`src/workspace/DesktopMutator.cpp:215-251, 283-313`). `computeWorkspacePlan`
  marks `create` only for ordinals absent from the observation and `rename`
  only when the live name differs (`src/workspace/WorkspacePlan.cpp:42-62`);
  `rows`/wrapping change flags require both desired and observed values
  (`WorkspacePlan.cpp:66-71`). Zero-call on an empty diff is enforced by
  `matchingPlanWritesNothing` (zero `createDesktop`/`setDesktopName`/`Set`/
  `removeDesktop` and no checkpoint file).
- `removeDesktop` and the `current` switch are opt-in only and never
  drift-triggered: removals run only under `options.removeExtras` for observed
  ordinals above the desired count, descending
  (`DesktopMutator.cpp:233-244, 327-333`), and `current` only under
  `options.switchCurrent` (`DesktopMutator.cpp:315`). Tests
  `excludedRemoveAndCurrentByDefault` and `optInCurrentAndRemoveRunLast` assert
  no removal/current on the default path and the current-then-removal order on
  the opt-in path.
- **Corrected `current` step is fail-closed** (`DesktopMutator.cpp:315-325`):
  a missing ordinal-1 target sets `errorClass = "current-target-missing"` and
  returns through `failApply`; a failed or timed-out `Properties.Set` returns
  through `failApply(errorClass)` (`mutation-error`, `mutation-timeout`, or
  `property-failed`). `failApply` (`DesktopMutator.cpp:269-281`) runs
  `runRevert`, returns `ok = false`, clears applying state, and the opted-in
  removals and the post-apply launch phase are never reached (the controller
  gates launch on `result.ok && !result.noChanges`,
  `src/app/AppController.cpp:1769`). The former soft residual
  `current-switch-skipped` no longer exists on the apply side; the separate
  revert-side `current-restore-skipped` residual is preserved
  (`DesktopMutator.cpp:417-428`).
- New regressions are present and causal:
  `currentSwitchFailureAbortsAndReverts` (fake `setFailMethod("Set", 1)` with
  `switchCurrent` and `removeExtras` both opted in) asserts `!ok`,
  `mutation-error`, reverted, not revert-failed, `removeDesktop` count 0, the
  user extra preserved, desktop count 3, the `current` Set attempted with the
  first-observed id, and the checkpoint deleted;
  `currentTargetMissingAbortsBeforeRemoval` (synthetic observation whose first
  ordinal is absent) asserts `!ok`, `current-target-missing`, reverted, and no
  removal. Both PASS on the candidate, and the disposable probe proved both
  FAIL on the un-fixed parent at exactly `!result.ok`
  (`test_workspace_mutator.cpp:682` and `:749`).
- Ordering/step gating is correct: each step returns through `failApply` on
  error; the checkpoint is written and verified before the first mutation
  (`DesktopMutator.cpp:255-267`); removals are last; `defaultApply...` asserts
  the full call order create → rename → rows → wrapping.
- No mutation on `currentChanged` or user-created desktops, no polling: the
  only `m_mutator.apply` call site is `applyWorkspaceSession`
  (`AppController.cpp:1768`) and the only revert call site is the explicit
  `revertWorkspaceApply` (`AppController.cpp:1806`); receiver
  `desktopCreatedObserved` is routed only to `recordCreatedDesktop` while a
  transaction is active (`AppController.cpp:1821-1827`). `kwinrulesrc` appears
  nowhere in `src/` or `kwin/`.
- Blocking: no.

### A3 — Checkpoint, revert, and stop rules: PASS

- Checkpoint path is now the product directory:
  `m_mutator.setCheckpointPath(m_store.configRoot() + "/contextdeck/workspace-checkpoint.json")`
  (`src/app/AppController.cpp:198`), which resolves to
  `<config root>/contextdeck/workspace-checkpoint.json`, user-local and never
  the profile document, logs, or META. The documented identity
  (`docs/specification.md:196-197`, `docs/operations.md:664-665`) now matches
  the code exactly.
- The path regression is real and causal:
  `productionCheckpointPathUsesProductDirectory` exists, passes on the
  candidate, and the disposable probe proved it FAILS on the un-fixed parent
  at `controller.workspaceCheckpointAvailable()`
  (`test_workspace_lighting.cpp:716`) when only the product-directory file is
  present. The test observes the production path through the existing
  config-root injection seam; the path check does not depend on parsing.
- Atomicity/permissions/lifecycle: `WorkspaceCheckpoint::save` uses
  `QSaveFile` with `setDirectWriteFallback(false)`, refuses on short write /
  flush failure, sets `ReadOwner|WriteOwner`, and commits
  (`src/workspace/WorkspaceCheckpoint.cpp:163-192`); write-and-verify happens
  before the first mutation (`DesktopMutator.cpp:190-201, 262-267`), confirmed
  by `checkpointWrittenBeforeFirstMutationAndUserOnly` (an `onBeforeMutation`
  probe observes the file present and permission bits group/other-free).
  Overwrite-per-Apply is confirmed by `checkpointOverwrittenPerApply`
  (`created_ids` becomes `gen-2`, checkpoint desktop count 3).
- Revert removes exactly this Apply's created UUIDs and nothing else:
  `runRevert` iterates only `data.createdIds`
  (`DesktopMutator.cpp:375-383`); `revertRemovesOnlyThisApplyUuids` lets a
  user-created desktop appear after Apply and confirms revert removes `gen-1`
  and preserves `user-x`. Names/rows/wrapping are restored from the checkpoint
  (`DesktopMutator.cpp:385-415`); the `current` restore is skipped with the
  bounded `current-restore-skipped` residual when the UUID is known absent
  (`DesktopMutator.cpp:417-428`; test `currentRestoreSkippedWhenUuidAbsent`).
  A hard residual keeps the checkpoint and reports the first bounded class
  (`DesktopMutator.cpp:430-435`); a successful revert deletes it
  (`DesktopMutator.cpp:439-440`).
- No application kill and no open-window move exist anywhere in the mutation
  path; the limitation is disclosed in the specification, operations, and
  testing-m4 documents.
- Fail-closed preconditions are preserved in `applyWorkspaceSession`
  (`AppController.cpp:1727-1752`): explicit invocation, `m_applyRunning`,
  `workspace_management_enabled`, valid session, receiver present, `Available`
  observation with no pending refresh and no in-flight logical request,
  unchanged owner generation, and unchanged preview fingerprint
  (`preview-stale` refusal); `applyRefusalsAreFailClosed` covers
  `management-disabled` and `preview-stale` with no desktop mutation.
- Blocking: no.

### A4 — In-transaction launch trigger classification: PASS

- `WorkspaceReceiver::onInvalidatingMessage` classifies the existing
  subscription payload: it decodes the `desktopCreated` structure, bounds and
  validates the id/position, and emits payload-free
  `desktopCreatedObserved(id, position)` without a second `GetAll` or polling;
  the normal coalesced invalidation path is unchanged
  (`src/context/WorkspaceReceiver.cpp:388-427`). Tests
  `desktopCreatedEmitsEventSurface` (signal with id and position, invalidation
  count increases, snapshot refreshes) and
  `currentChangedDoesNotEmitDesktopCreated`.
- Only the in-transaction event and the explicit Apply launch: the controller
  routes `desktopCreatedObserved` only while `m_applyRunning`
  (`AppController.cpp:1821-1827`); the mutator re-emits
  `desktopCreatedInTransaction` only for expected create positions while
  applying (`DesktopMutator.cpp:67-81`); the controller launches only for that
  ordinal (`AppController.cpp:1829-1836, 1849-1865`). The end-to-end test
  `applyLaunchesInTransactionDesktopProfilesOnce` asserts exactly one launch on
  Apply for the ordinal-3 profile and then asserts a user-created desktop and
  `currentChanged` add none.
- The created UUID is recorded in the checkpoint before the next step
  (`recordCreatedDesktop` persists on each observed create), verified by
  `checkpointWrittenBeforeFirstMutationAndUserOnly` and
  `inTransactionTriggerClassification` (created UUID `gen-1` at position 2).
  No desktop identity is logged: all receiver/mutator log sites use fixed
  bounded class strings or counts.
- Blocking: no.

### A5 — Typed launcher: PASS

- Only a validated `.desktop` id is accepted:
  `ApplicationLauncher::requestLaunch`/`retryForDesktopCreated` reject
  empty/invalid ids via `workspaceDesktopIdLooksValid`
  (`src/workspace/ApplicationLauncher.cpp:77-80, 98-101`), and
  `invalidDesktopIdsAreRejected` rejects `sh -c ...`,
  `systemd-run --user ...`, `kstart ...`, and an absolute path with zero seam
  invocations.
- The production path uses `KService::serviceByStorageId` plus
  `KIO::ApplicationLauncherJob` and connects `KJob::finished` for the bounded
  failure class (`ApplicationLauncher.cpp:148-163`); the
  `setInvokerForTest` seam is the only path used in tests, so no real job is
  started. No shell, `QProcess` of `Exec=`, `systemd-run`, or `kstart` occurs
  anywhere in `src/` or `kwin/` (grep evidence).
- Skip-if-already-running, per-profile 2 s debounce, and one bounded retry are
  implemented (`WorkspacePlan.cpp:151-206`; `ApplicationLauncher.cpp:73-107`)
  and tested through the seam (`nonLaunchIntentsNeverInvoke`,
  `invokesSeamWithTypedIdAndDebounces`,
  `boundedRetryOnlyAfterFailureBeforeWindow`, `transactionEndResetsAttempts`).
- Blocking: no.

### A6 — Placement, bridge, and live-caption privacy: PASS

- `PlacementResolver` implements identity-wins, fallback only when both flags,
  empty-id no-op, maximize selection, and management/session/`Available`
  gating (`src/workspace/PlacementResolver.cpp:8-34`); tests cover
  identity-wins, fallback gating at both flag levels, empty id, unassigned
  identity, and management disabled, plus maximize.
- Wiring is as specified: `ContextReceiver` exposes
  `PlacementHint(desktop_file_name, resource_class, resource_name) ->
  (desktop_id, maximize)` and `TitleHint(bridge_id, sequence, caption)`; the
  `ContextReport` introspection still declares exactly the six original input
  arguments plus the boolean reply
  (`src/context/ContextReceiver.cpp:178-198, 249-309`). The bridge calls
  `PlacementHint` on `windowAdded` with a trailing callback, sets
  `window.desktops = [id]`, and calls `setMaximize(true, true)` only when
  requested; an empty id is a no-op
  (`kwin/contextdeck-bridge/contents/code/main.js:137-169, 242-248`). No file
  write exists in the bridge.
- Captions: `TitleHint` is sent only while the learned flag is true, bounded at
  both ends (64 characters in JS, 256 bytes on D-Bus with rejected oversized
  input), held only until the next resolution consumes it, discarded on an
  empty hint, on an identity refresh without change, and on bridge loss, and
  never logged (only fixed-string rejection warnings without arguments).
  Non-vacuous guards exist and pass:
  `contextReceiverTitleHintIsConsumedOnce`,
  `contextReceiverRejectsOversizedTitleHint`,
  `contextReceiverPlacementHintUsesProviderAndConsumesCaption`,
  `contextReceiverDoesNotLogTitleHintArguments`, `liveCaptionPrivacyGuard`
  (drives the full controller flow, selects the fallback profile via a
  synthetic caption, then asserts the sentinel is absent from diagnostics and
  every captured log message), and
  `diagnosticsOmitWorkspacePrivacySentinels` (seeded document state, recursive
  key/value flattening, sentinel and category-fragment checks).
- KWin `callDBus` trailing-callback reply form independently re-confirmed from
  the installed build without any live session probe (details in the dedicated
  section below). `metadata.json` parses as valid JSON, version `0.2.0`, and
  describes the final bridge behavior truthfully.
- Blocking: no.

### A7 — Causal regression evidence: PASS

- Test bodies were inspected, not names or counts. The Slice B contract maps to
  persistent causal regressions: default create/rename/rows/wrapping ordering
  and no-op (`defaultApplyCreatesConditionalRenamesSetsRowsAndWrapping`,
  `matchingPlanWritesNothing`), excluded remove/current and opt-in ordering
  (`excludedRemoveAndCurrentByDefault`, `optInCurrentAndRemoveRunLast`), abort
  on error with revert (`abortOnRenameErrorRunsRevert`), the two new
  fail-closed `current` regressions, checkpoint write-before-mutation/
  permissions/overwrite/cleanup (`checkpointWrittenBeforeFirstMutationAndUserOnly`,
  `checkpointOverwrittenPerApply`), revert exactly-this-Apply and
  `current`-restore skip (`revertRemovesOnlyThisApplyUuids`,
  `currentRestoreSkippedWhenUuidAbsent`), in-transaction trigger versus
  user-created/`currentChanged` non-triggers
  (`inTransactionTriggerClassification`,
  `applyLaunchesInTransactionDesktopProfilesOnce`), launcher decisions/
  debounce/retry (`test_application_launcher`), placement identity/gating/
  no-op/maximize (`test_placement_resolver`), controller refusals
  (`applyRefusalsAreFailClosed`), the checkpoint-path regression
  (`productionCheckpointPathUsesProductDirectory`), and the caption-privacy
  guards listed under A6.
- Private-bus isolation: `CMakeLists.txt` registers `test_workspace_receiver`,
  `test_workspace_mutator`, and `test_workspace_lighting` under
  `dbus-run-session` with `QT_QPA_PLATFORM=offscreen;QT_DISABLE_SESSION_MANAGER=1`
  and synthetic fake desktop-manager services on the private session bus; the
  launcher is exercised only through its injected seam; `test_placement_resolver`
  and `test_application_launcher` are pure. No test starts the session
  application, OpenRGB, the broker, a device, a real KWin connection, or a real
  application launch.
- Focused route (exact required regex, including both corrected targets):
  exit 0, `100% tests passed out of 9`, total 67.25 s
  (`test_workspace_receiver` 65.86 s, `test_workspace_lighting` 0.59 s,
  `test_workspace_mutator` 0.74 s, `test_application_launcher` 0.02 s,
  `test_placement_resolver` 0.00 s, `test_openrgb_protocol` /
  `test_workspace_plan` / `test_profile_resolver` /
  `test_profile_persistence` 0.01 s each).
- Full registered suite: exit 0, `100% tests passed out of 21`, total 68.96 s.
- Per-function confirmation from the detached candidate:
  `dbus-run-session -- ./test_workspace_mutator
  currentSwitchFailureAbortsAndReverts currentTargetMissingAbortsBeforeRemoval`
  → `4 passed, 0 failed`; `dbus-run-session -- ./test_workspace_lighting
  productionCheckpointPathUsesProductDirectory` → `3 passed, 0 failed`.
- No persistent coverage required by the Slice B contract is missing.
- Blocking: no.

### A8 — Documentation and bounded claims: PASS

- The corrected `Plochy` row (`docs/specification.md:555`) now describes the
  implemented preview, explicit Apply and revert-from-checkpoint controls, the
  truthful preconditions, and the separate `current`/removal opt-ins; it no
  longer claims Apply is hidden/disabled.
- The checkpoint path is documented as
  `$XDG_CONFIG_HOME/contextdeck/workspace-checkpoint.json` (fallback
  `$HOME/.config/...`) in `docs/specification.md:196-197` and
  `docs/operations.md:664-665`, matching code line `AppController.cpp:198`.
- `docs/architecture.md` (M4 section) matches the mutator/checkpoint/launcher/
  receiver/placement implementation; `docs/testing-m4.md` is a later IRL
  checklist that explicitly grants no host mutation and requires a separate
  grant; ADR 0002 and ADR 0004 statuses and decisions match the code and
  disclose the no-standing-authority posture; `README.md` and `ROADMAP.md`
  describe Slice B only as an implementation candidate, "not accepted and not
  live-verified", with no autostart or production claim.
- The exact M3 park wording is preserved in `README.md` and `ROADMAP.md`; the
  exact M2 park wording is preserved in `README.md`. The M4 diff did not alter
  the park statements (verified by diff review). No physical, deployment,
  production, autostart, M5, per-key, or whole-G4 claim appears in the changed
  documents.
- Non-blocking wording nuance retained as a ledger candidate: the
  specification names `KApplicationTrader` alongside `KService`, while the
  production launcher uses `KService::serviceByStorageId`; the accepted
  decision is a typed `KService` id, so this is wording only.
- Blocking: no.

Acceptance-PASS requires all A1–A8 PASS and both leads resolved; all hold.

## Mandatory adversarial leads

### L1 — corrected fail-closed `current` and the empty-snapshot abort: confirmed (non-blocking)

- The fix is exactly fail-closed: `DesktopMutator.cpp:315-325` returns through
  `failApply` for both a missing target (`current-target-missing`) and a failed
  or timed-out `Properties.Set`; `failApply` runs the revert path, sets
  `ok = false`, and clears the applying state, and the controller's launch
  phase is gated on `result.ok` (`AppController.cpp:1769`). Opted-in removals
  cannot run because they follow the current step and are only reached on the
  success path.
- Regression causality is independently proven, not inferred: the disposable
  probe ran the candidate's two regressions against the un-fixed parent code
  and both failed exactly at `QVERIFY(!result.ok)`
  (`currentSwitchFailureAbortsAndReverts`, parent line 682;
  `currentTargetMissingAbortsBeforeRemoval`, parent line 749). On the
  candidate they pass; the parent's soft-residual behavior is the causal
  difference.
- Empty-snapshot assessment: when the observation is `Available` but has no
  ordinal-1 desktop and the user opted in to switch, the transaction now aborts
  as `current-target-missing` and reverts any desktops it created, never
  reaching removals or launch. This is acceptable fail-closed behavior: the
  state is left consistent, the failure is bounded and surfaced, and it is the
  exact precondition the correction decision required to stop. It is also not
  reachable by normal operation — KWin cannot have zero virtual desktops, and
  the receiver assigns contiguous ordinals from sorted positions — so an
  earlier controller-level precondition refusal would only change where the
  refusal is reported, not the safety outcome or the user-visible rollback.
  Either placement is lawful; the current behavior is not a blocking gap.
- Consequence: no blocking defect; no correction needed.

### L2 — checkpoint path, revert ownership, and late-dispatch residual: confirmed (non-blocking)

- Product-directory checkpoint: `AppController.cpp:198` writes
  `<config root>/contextdeck/workspace-checkpoint.json`; the regression is
  causal (probe failure on the un-fixed parent at the path check), and the
  documentation now matches the code exactly.
- Revert cannot remove a desktop this Apply did not create: `runRevert`
  iterates only `created_ids` and never any other observed or checkpoint UUID
  (`DesktopMutator.cpp:375-383`); `revertRemovesOnlyThisApplyUuids` proves a
  user-created desktop present after Apply is preserved while the Apply-created
  `gen-1` is removed. Names/rows/wrapping restore targets stored checkpoint
  entries only.
- Late-dispatch residual reconfirmed unchanged: recording requires
  `m_applying` and an expected create position (`DesktopMutator.cpp:67-81`),
  and the applying flag is cleared before `apply()` returns
  (`DesktopMutator.cpp:338-339`); the controller ignores
  `desktopCreatedObserved` outside a transaction
  (`AppController.cpp:1821-1827`). If KWin delivered the signal after the
  method reply and after the transaction ended, the created UUID would be
  absent from `created_ids`, so a later revert would under-remove that created
  desktop (never over-remove), while the launch for that ordinal remains
  covered by the explicit-Apply phase with `hasAttempted` deduplication. This
  is the safe direction, bounded by the number of creates in that Apply,
  requires abnormal signal ordering, and is disclosed as a residual; it does
  not block acceptance.
- Consequence: no blocking defect; no correction needed.

## Validation evidence

From the exact detached candidate with build products outside the checkout,
under `env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH`:

```text
configure: cmake -S . -B <owned-temp>/build-cand -G Ninja   -> exit 0
build:     cmake --build <owned-temp>/build-cand             -> exit 0, 158/158 targets, 0 warnings

focused:   ctest --test-dir <owned-temp>/build-cand --output-on-failure \
             -R '^(test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_plan|test_openrgb_protocol|test_workspace_mutator|test_placement_resolver|test_application_launcher|test_workspace_lighting)$'
           -> exit 0; 100% tests passed out of 9; total 67.25 s
              (test_workspace_receiver 65.86 s; test_workspace_lighting 0.59 s;
               test_workspace_mutator 0.74 s; test_application_launcher 0.02 s)

full:      ctest --test-dir <owned-temp>/build-cand --output-on-failure
           -> exit 0; 100% tests passed out of 21; total 68.96 s

per-fn:    dbus-run-session -- ./test_workspace_mutator \
             currentSwitchFailureAbortsAndReverts currentTargetMissingAbortsBeforeRemoval
           -> 4 passed, 0 failed
           dbus-run-session -- ./test_workspace_lighting \
             productionCheckpointPathUsesProductDirectory
           -> 3 passed, 0 failed

gates:     git diff --check aca6c68..db9ddc1        -> clean
           git diff --name-only 5087277..db9ddc1    -> exactly the five correction paths
           git status --short                        -> clean before, during, and after validation
```

Private-bus classification: the three D-Bus-touching registered targets ran
under the registered `dbus-run-session` route with synthetic fake
desktop-manager services on a private session bus and
`QT_QPA_PLATFORM=offscreen;QT_DISABLE_SESSION_MANAGER=1`; the pure targets are
bus-free. No real KWin connection, KWin replacement, bridge reload, desktop
mutation, application launch, OpenRGB connection or CLI, device open, broker
start/ARM/grab, service change, package install, `/etc`/udev change, or host
operation occurred. No test was weakened, skipped, or looped.

First causal failure in executed validation: none. The probe's two mutator and
one lighting failures are intentional parent-code results that establish
causality and are not candidate failures.

## KWin `callDBus` reply-form independent confirmation

Independently re-confirmed from the installed KWin build without any live
session probe:

- Installed `kwin` 6.7.5-1.1; `/usr/lib/libkwin.so.6` SHA-256
  `02737e1fb3a6b5923fdfc37de2d57dc65d19f9bfbe5f33b6dedb41dc7203da61`, matching
  the identity recorded by the Slice B implementation and prior acceptance.
- The shipped string table contains the `callDBus` metaobject name; the dynamic
  symbol table contains undefined references to the
  `QDBusPendingCallWatcher` constructor, `finished`, and `staticMetaObject`,
  and to `QJSValue::isCallable()` and `QJSValue::call(QList<QJSValue>)` — the
  exact reply-callback machinery. The prior acceptance additionally located
  the `createMethodCall` → `setArguments` → `asyncCall` → watcher →
  `isCallable`/`call` implementation by bounded disassembly of the same binary
  identity.
- Conclusion: the trailing-callback reply form used by the bridge
  (`ContextReport` boolean and `PlacementHint (desktop_id, maximize)`) is
  supported by the installed build; the bridge's empty-id no-op and `typeof`
  guards keep older peers safe. No synthetic script probe was needed.

## Temporary probe

- Identity/design: one Worker-owned disposable copy of the un-fixed parent tree
  (constructed read-only via `git archive` of the parent commit into a new
  owned temporary directory outside the canonical product checkout), with the
  candidate's two modified regression test files overlaid onto it, configured
  and built in a second external build directory with the existing toolchain,
  then exercised with only the three correction regressions.
- Result: `currentSwitchFailureAbortsAndReverts` FAILED at
  `!result.ok` (parent line 682), `currentTargetMissingAbortsBeforeRemoval`
  FAILED at `!result.ok` (parent line 749), and
  `productionCheckpointPathUsesProductDirectory` FAILED at
  `controller.workspaceCheckpointAvailable()` (parent line 716). This proves
  the three regressions are causal: they fail on the un-fixed parent and pass
  on the corrected candidate.
- Cleanup: the disposable copy, its build directory, and all probe logs were
  deleted after evidence capture. No product or META diff resulted; the
  canonical product checkout remained clean. No synthetic data beyond the
  tests' own fixtures was used, and no private path is recorded here.

## Confirmed defects, missing persistent tests, disproved concerns, residual risks, deviations, ledger candidates

- Confirmed defects: none in the corrected candidate. The three prior blockers
  (A2 fail-closed `current`, A8 stale `Plochy` row, A8 checkpoint path) are
  corrected, covered by causal regressions, and independently re-verified.
- Missing persistent tests: none required by the Slice B contract remain
  missing; both new correction regressions exist, are registered, execute, and
  are non-vacuous (probe-proven sign change against the parent).
- Disproved concerns: the prior A2 runtime deviation (no longer a soft
  residual); the prior A8 documentation/path mismatches (now matching); L2
  over-removal on revert; default-path removals or `current` drift; caption
  logging/persistence; launcher shell acceptance; placement bypass of the
  both-flags gate.
- Residual risks: the L1 late-dispatch under-recording (safe direction,
  abnormal ordering, disclosed); QML runtime behavior validated only by
  build-time compilation; a hypothetical old-path checkpoint written by the
  never-accepted parent candidate would be orphaned by the corrected path (not
  applicable to accepted product history); no live desktop/launch/placement
  behavior is established by this code acceptance.
- Deviations: a mechanical byte comparison of the chat-delivered prompt against
  the persisted `10_acceptance_00.md` is not observable from inside the
  session; identity was verified against the complete persisted-file readback
  and its SHA-256. Public META does not yet contain the `10` prompt (the
  baseline ends at the `09` pair) — consistent with the configured
  `wait-for-report` archival where the COOPERATOR first-adds prompt and report
  together after the report exists. No retargeting occurred.
- Out-of-scope ledger candidates (non-blocking, no acceptance impact): the
  ADR 0002/0004 "accepted for the M4 tree" status phrasing carried from Slice A;
  the `.desktop`-suffix desktop-id predicate accepting trivially short forms;
  `KApplicationTrader` named in the specification but not used in code; the
  L1 checkpoint-disclosure gap; QML runtime not executed; an orphaned
  old-path checkpoint if a host ever ran the never-accepted parent candidate.

## Resolved Execution Issues / Near-Misses

- One benign orientation near-miss, disclosed for completeness: before creating
  the disposable clones, the first environment check ran `pwd`/`ls` and tool
  version commands in the local workspace directory. No product file content
  was read there, no mutation occurred, and no acceptance evidence was derived
  from it; all substantive evidence came from the fresh disposable clones and
  the trace destination.
- The probe configure/build and the two probe regression runs were executed only
  inside the Worker-owned disposable copy as designed; none touched the
  canonical checkout.
- No destructive Git operation, package install, service/device action, or host
  change was attempted. No state from any prior Worker session was reused.

## Pre-Existing Failure Classification

none. No registered test was failing at the candidate and none failed during
this review; configure and build produced zero compiler warnings. The Qt
harness's `org.kde.kscreen.dpms` library note previously recorded for this
project is unrelated pre-existing noise and did not appear as a test failure.

## META trace persistence and readback

- Prompt `projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/10_acceptance_00.md`
  is present in the COOPERATOR-owned META working tree as a regular untracked
  file (not a symlink); it was read back completely (469 lines, 23228 bytes)
  and matches the delivered prompt field-for-field including coordinates,
  authority and record fields, immutable identities, required hashes, changed
  paths, matrix, leads, validation, trace, and terminal contracts. Persisted
  file SHA-256:
  `a173258a0d6c92c8cc70a3eddfc7e9b379647f7204ae9c1a6a0be1d0f23f1a5a`. No
  collision and nothing was overwritten.
- Report `projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/10_report_00.md`
  was absent before this write and is the only file this exchange prepared. It
  was written once and read back completely immediately after the write
  (header, coordinates, record fields, status, matrix, leads, validation,
  KWin confirmation, probe, defects, persistence, critique, and the singleton
  terminal lines verified).
- META Git was not staged, committed, pushed, pulled, merged, rebased,
  switched, or otherwise mutated by this Worker; no META ref or history
  changed, and no path other than the report was written. First-add archival of
  the exact prompt/report pair remains COOPERATOR-owned.

## Smallest next step

ORCHESTRATOR reconciliation of this acceptance-PASS for public candidate
`db9ddc1f923f44e26f7f1d58df7446306bbdf64a`. If accepted, the only next step is
the separate, explicitly granted COOPERATOR-owned live IRL run per
`docs/testing-m4.md`; that run is not granted by this report. No correction,
deployment, host enablement, M5 work, or closure is authorized.

Orchestration critique:

MEASURED: The bounded correction moved the optional `current` step onto the
existing `failApply` revert path for both a missing target and a failed/timed-out
`Properties.Set` (`src/workspace/DesktopMutator.cpp:315-325`) and moved the
checkpoint into the product directory
(`src/app/AppController.cpp:198`), with three new registered regressions (two
for the fail-closed `current` step, one for the product-directory path) and a
corrected documentation row; a disposable parent-code probe shows all three
regressions fail on the un-fixed parent and pass on the candidate, focused 9/9
and full 21/21 pass from the detached candidate, and the corrected candidate
meets A1–A8 with both leads confirmed non-blocking; effect: the prior PARTIAL
blockers are closed and the Slice B code contract is independently accepted;
smallest correction: none needed at this scope.

LEAD: The explicit-apply launch phase and the in-transaction `desktopCreated`
launch share the same debounce map, so a very early KWin signal ordering could
in principle consume an attempt before the explicit phase; the cheapest useful
check remains the COOPERATOR-owned IRL run's launch-once / second-apply-no-
duplicate step, which is already in `docs/testing-m4.md`. Unverified; not a
blocking observation.

Explicit non-claims: no implementation-PASS at this phase, no publication-PASS,
deployment-PASS, production readiness, physical acceptance, M2/G4 closure,
independent G3 re-audit, autostart, hibernate/hybrid sleep, general
input-remapper coexistence, M3 closure, M3 physical five-zone observation, live
desktop/launch/placement behavior, remapping, deck behavior, M5 integration,
per-key RGB, or measured control-to-zone placement. Tests do not prove live
desktop, compositor, or physical device behavior. Session 27 is not claimed to
have been an independent Worker result. This review demanded no live input,
device, desktop, or launch operation and performed none.

Logical-whole closure: not-closed

Authority for this Worker expires at this terminal report.
