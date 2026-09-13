### Report for ORCHESTRATOR_CHAT

Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-workspace-aware-lighting
Worker session ordinal: 04
Worker exchange ordinal: 01

Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: CONTEXTDECK-M3-WORKSPACE-RECEIVER-AND-REGRESSION-CORRECTION
Native planning mode: not-used
Internal delegation: none

status: PASS
Phase-qualified result: implementation-PASS
Result artifact or commit: `502ae75571358ec95d33c836084b5e2253850731`
Result evidence: one correction commit on public `main`, focused 5/5 and full 17/17 CTest, direct `ls-remote` equality
Report justification: new-mutation

Acceptance candidate: `55e981309718bcb2f94f809468eab9934acf5f51`
Acceptance owner map: accepted M3 plan (`01_report_00.md` / `01_report_01.md`), implementation (`02_implementation_00.md` / `02_report_00.md`), independent PARTIAL `03_report_00.md` blockers A5/L1 and A7/L2
Acceptance allowlist: `WorkspaceReceiver.h/.cpp` and the four named unit-test paths; `Persistence.cpp`, `Resolver.cpp`, and `AppController.cpp` were unused
Acceptance risk claims: explicit logical request ownership; durable causal regressions for the frozen M3 contract
Acceptance control matrix: A5/L1 ownership and A7/L2 missing regressions only; A1–A8 re-acceptance is not this session
Acceptance independence: not-required for this corrector; required-fresh-independent for the next re-acceptance
Primary fresh acceptances used: 0
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: none

## Identity and publication

| Item | Value |
|---|---|
| Product start / required public `main` before mutation | `55e981309718bcb2f94f809468eab9934acf5f51` |
| Product end commit / local `HEAD` / `origin/main` / direct `ls-remote` | `502ae75571358ec95d33c836084b5e2253850731` |
| Required / actual parent | `55e981309718bcb2f94f809468eab9934acf5f51` |
| Commit subject | `Correct M3 workspace request ownership and regressions` |
| Push | one normal fast-forward of product `main` (`55e9813..502ae75`); no force, no retarget |
| AP gitlink and checkout | `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9` |
| `./.ap/ap doctor` | PASS before mutation and after publication |
| Public META baseline (unchanged) | `9e7fd1832122e89b96cda231827b4ea726febfe0` |
| Required META parent | `ee6f8c90414b15a87a8b1617cc561ca542768dcd` |
| Independent acceptance artifact | `projects/contextdesk/00/03-g213-contextdeck-workspace-aware-lighting/03_report_00.md` |
| Independent acceptance artifact SHA-256 | `5f1e201a12478c95e6dbf7d0c40df710e46a5bdff143a8f3c515529527414e00` |
| Acceptance pair commit | `9e7fd1832122e89b96cda231827b4ea726febfe0` |
| Correction prompt SHA-256 | `09365daee940c23e659439894e9b5154816c6fa907efbdb6f306ae5944492ddd` |
| Product worktree after publication | clean `main...origin/main` |

Changed product paths are exactly the six below. `.ap/`, QML, docs, CMake, RGB, broker, KWin, packaging, host configuration, `Persistence.cpp`, `Resolver.cpp`, and `AppController.cpp` were not modified.

| Path | Purpose |
|---|---|
| `src/context/WorkspaceReceiver.h` | Replace shared `m_inFlight` with `m_activeRequestId` / `m_logicalRequestCount`; `abandonCurrentRequest()` |
| `src/context/WorkspaceReceiver.cpp` | Request ownership state machine; GetAll `a{sv}` demarshal; two-pass metadata then uniqueness |
| `tests/unit/test_workspace_receiver.cpp` | Private-bus ownership, recovery, and malformed-snapshot regressions |
| `tests/unit/test_profile_persistence.cpp` | Schema-3 invalid lighting/speed and schema-2 success-form regressions |
| `tests/unit/test_profile_resolver.cpp` | App-slot contribution table and identity-loss workspace indicators |
| `tests/unit/test_workspace_lighting.cpp` | Metadata-only name change does not increment lighting submissions |

`git diff --check` was empty. `git diff-tree` of `502ae75` lists only those six allowlisted paths.

## Ownership correction

Old failure (A5/L1): every watcher cleared a single `m_inFlight` flag on finish, deadline, owner change, or stop. A stale or late completion could then admit another `requestSnapshot()`, overlapping GetAlls (`max_outstanding=3` in the acceptance probe). `start()` also combined `invalidate()` with an immediate request, queuing a redundant coalesced GetAll.

Corrected design: each logical request gets a monotonic id stored on the `QDBusPendingCallWatcher`. Only `requestId == m_activeRequestId` may clear current ownership, apply a snapshot, or start a coalesced successor. A mismatch increments `rejectedReplyCount` and returns without touching the newer request. `abandonCurrentRequest()` sets the active id to 0 on stop, deadline, and owner replacement; it does not cancel the remote GetAll. Qt D-Bus pending calls are not cancelled here; an expired transport may still complete and is observational only.

`start()` sets `errorClass=initial` and `refreshPending`, then issues one `requestSnapshot()` (no invalidate+coalesce pair). Owner replacement abandons the current request, stops recovery/coalesce, becomes Unknown, and issues one new request. `requestSnapshot()` restarts the deadline for that new logical request; `startDeadline()` still no-ops when a timer is already active, so invalidation during an in-flight request does not extend that request’s two-second bound. Recovery remains 1/2/4/8/16/30 s, event-driven, with no periodic poll.

GetAll replies that arrive as `a{sv}` are walked as a map of `QDBusVariant` values so nested `desktops` stay a `QDBusArgument` array (KWin KCM shape) instead of a lossy `QVariant::toMap()` conversion. Snapshot decode collects every row first, applies the 16 KiB aggregate metadata bound, then duplicate-id / duplicate-position checks. That makes `metadata-limit` reachable: 33 unique positions at the per-field caps cannot exceed 16 KiB, so a payload over the bound necessarily has more rows than unique positions.

## Required regression mapping

| Required case | Test / assertion | Outcome |
|---|---|---|
| One initial GetAll when no signal races | `oneInitialGetAllWithoutSignalRace`: `getAllCount()==1`, `logicalRequestCount()==1`, then `activeLogicalRequestId()==0` | PASS |
| Invalidation during initial request → one coalesced successor | `invalidationDuringInitialRequestCoalescesOneSuccessor`: `logicalRequestCount()==2`, `getAllCount()==2` | PASS |
| Late first watcher after deadline cannot clear newer request or admit a third | `lateFirstWatcherAfterDeadlineDoesNotAdmitThirdRequest`: after deadline, recovery id stays, `rejectedReplyCount` rises, `getAllCount()` stays 2 until the live reply is released | PASS |
| Former-owner reply cannot clear replacement request | `formerOwnerReplyDoesNotClearReplacementRequest`: release of held former GetAll leaves replacement id and Unknown; new owner reply becomes Available | PASS |
| Pre-stop watcher cannot alter resumed ownership | `preStopWatcherCannotAlterResumedOwnership`: pause → `observation-paused` / Unknown / active id 0; releasing the held reply keeps that state; resume → second logical request, Available | PASS |
| Deadline Unknown at bound; recovery follows configured sequence without multiplication | `productionRetryBudgetExhaustionThenEventRecovery` with production delays `{1000,2000,4000,8000,16000,30000}` and 50 ms deadline; each recovery GetAll is one logical request | PASS |
| After six production delays, no seventh automatic retry; later event can recover | same test: `getAllCount()==7` and `recoveryAttempt()==6` after a 400 ms wait; `emitCurrentChanged()` → Available, `recoveryAttempt()==0`, `logicalRequestCount()>=8` | PASS |
| Successful recovery resets budget | `successfulRecoveryResetsBudget`: `recoveryAttempt()==0` after Available | PASS |
| Duplicate valid snapshots do not notify | `duplicateValidSnapshotsDoNotNotify` and `serviceLossAndDuplicateSnapshot`: `notificationCount` unchanged while `snapshotCount` increases | PASS |
| Schema-3 invalid color strings and wrong color types | `schema3InvalidColorsTypesZonesAndSpeedBounds`: `#gg0000`, `#fff`, numeric, bool | PASS |
| Non-object zone entries and role-incompatible fields | same: string/null zones; static missing color; extra field; off+color | PASS |
| Schema-3 speed negative, fractional, wrong-type, above integer bound | same: `-1`, `1.5`, `"fast"`, `2147483648` | PASS |
| Schema-2 Direct absent zones; Cycle; Off; keys/matches/app order/preferences; read bytes unchanged; five-color zones stay Static | `schema2SuccessFormsPreserveFieldsAndReadBytes` | PASS |
| Direct base; Direct five static/off zones by physical index; Breathing explicit and default; Off black; Untouched/Wave/Cycle fallback; matched without lighting; unmatched | `applicationContributionTable` | PASS |
| Bridge/identity loss keeps workspace indicators; app slots fall back | `identityLossKeepsWorkspaceIndicators`: indicators unchanged, app slot uses global fallback `0x40` | PASS |
| Count/list mismatch; signed/unsigned out-of-range positions; duplicate position and id | `malformedCountMismatchAndPositions`; duplicate id in `malformedIdentityMetadataAndCurrent` | PASS |
| Over-bound id/name, control characters, aggregate metadata > 16 KiB | `malformedIdentityMetadataAndCurrent`: 129-byte id, 257-byte name, control char, 43 max-size rows → `metadata-limit` | PASS |
| Current missing / empty; desktop-list removal then refreshed snapshot | `missingCurrentIdIsUnknown`; empty current in `malformedIdentityMetadataAndCurrent`; `desktopRemovalProducesRefreshedSnapshot` | PASS |
| Metadata-only desktop name change updates UI metadata, not RGB submissions | `metadataOnlyNameChangeDoesNotSubmitLighting`: `displayName` and `presentationChanged`; `lightingUpdates` unchanged | PASS |

`logicalRequestCount()` / `activeLogicalRequestId()` expose no desktop identity. Fake `getAllCount` / outstanding-handler counters distinguish logical requests from still-finishing remote handlers.

## Validation

Configure/build/test used existing `/usr/bin/cmake` with `env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH` because the Cursor AppImage pollutes CMake. That is an environment workaround, not a toolchain change. Nothing was installed.

Focused CTest (`test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_lighting|test_openrgb_protocol`): **5/5 passed** in 64.76 s (`test_workspace_receiver` 64.51 s).

Complete registered CTest suite: **17/17 passed** in 66.91 s (`test_profile_resolver`, `test_profile_persistence`, `test_openrgb_protocol`, `test_broker_identity`, `test_broker_ledger`, `test_broker_forwarding`, `test_broker_acquisition`, `test_broker_watchdog`, `test_broker_ipc`, `test_broker_production`, `test_udev_policy`, `test_workspace_receiver` 65.07 s, `test_workspace_lighting`, `test_udev_verify`, `test_trial_cutoff`, `test_sleep_hook`, `test_broker_ipc_client`).

`test_workspace_receiver` and `test_workspace_lighting` run under already-installed `dbus-run-session` with a fake `org.kde.KWin` `/VirtualDesktopManager` on a private bus. No real KWin, OpenRGB process, broker, ARM, grab, udev, or other host mutation was used. Automated tests do not prove physical five-zone behavior.

## META persistence

The exact received prompt was already present at
`projects/contextdesk/00/03-g213-contextdeck-workspace-aware-lighting/04_correction_00.md`
(20660 bytes, SHA-256 `09365daee940c23e659439894e9b5154816c6fa907efbdb6f306ae5944492ddd`) and was not overwritten.

This report is written to
`projects/contextdesk/00/03-g213-contextdeck-workspace-aware-lighting/04_report_00.md`
and read back completely. Header, 04/01 coordinates, correction record, ownership design, regression table, validation, and publication evidence are present. META Git add/commit/push remains COOPERATOR-owned. Prior M3 trace files were not changed.

## Deviations, near-misses, residual risk

Resolved Execution Issues / Near-Misses:

- Single-pass uniqueness made `metadata-limit` dead: 33 unique positions at the 128/256 byte caps sum to 12288 bytes, so a duplicate-position row failed as `position-duplicate` before 16 KiB. Two-pass decode (all rows → metadata → uniqueness) is the smallest way to honor the aggregate bound without lowering it or raising `kMaxPosition`.
- `QVariant::toMap()` on GetAll `a{sv}` can convert nested `desktops` through registered `QList` helpers. Tests now marshal a real `a{sv}` argument map; the receiver walks map entries as `QDBusVariant`.
- `QTRY_COMPARE` on stale `refresh-deadline` while a recovery GetAll was in flight made `productionRetryBudgetExhaustionThenEventRecovery` assert `activeLogicalRequestId()==0` too early. The wait is now on the active id becoming 0.
- Immediate `QCOMPARE(getAllCount(), 2)` after `logicalRequestCount()==2` raced D-Bus delivery under CTest; it is now `QTRY_COMPARE`.

Pre-Existing Failure Classification: none in this correction boundary. A5/L1 and A7/L2 were the accepted PARTIAL blockers and are addressed in the published commit; this corrector cannot certify them independently.

Residual risks: this Worker’s tests are non-independent. Full-fresh A1–A8 re-acceptance of `502ae75` is still required. Physical M3 IRL, deployment, and M2/G4 remain open. Uncancellable in-flight GetAlls can still complete after abandon; they must stay observational. A silent compositor hang without D-Bus events remains undetectable.

Missing evidence: no independent re-acceptance, no physical IRL, no deployment, no META archival commit.

## Non-claims

This report does not claim acceptance-PASS, physical M3 acceptance, deployment, production readiness, M2/G4 closure, independent G3 re-audit, autostart, hibernate/hybrid sleep, general input-remapper coexistence, M4/M5 behavior, per-key RGB, or measured control-to-zone placement. Tests do not prove physical keyboard behavior. This corrector cannot self-certify.

**Smallest next step:** ORCHESTRATOR reconciliation of this correction, followed only on PASS by a separate genuinely fresh full A1–A8 re-acceptance Worker of public `502ae75571358ec95d33c836084b5e2253850731`.

Orchestration critique:
MEASURED: The 16 KiB metadata class was unreachable under unique-position-first decode; the acceptance fixture with duplicate positions was a faithful payload, not a two-row D-Bus truncation.
LEAD: none

Logical-whole closure: not-closed

Authority for this Worker expires at this terminal report.
