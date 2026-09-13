### Report for ORCHESTRATOR_CHAT

Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-workspace-aware-lighting
Worker session ordinal: 03
Worker exchange ordinal: 01

Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Acceptance Worker
Phase: acceptance
Task identity: CONTEXTDECK-M3-WORKSPACE-LIGHTING-CODE-ACCEPTANCE
Native planning mode: not-used
Internal delegation: none

status: PARTIAL
Phase-qualified result: not-applicable
Result artifact or commit: 55e981309718bcb2f94f809468eab9934acf5f51
Result evidence: independent A1–A8 matrix and leads L1–L2 below; focused 5/5 and full 17/17 CTest green is not acceptance-PASS
Report justification: final-acceptance

Acceptance candidate: `55e981309718bcb2f94f809468eab9934acf5f51`
Acceptance owner map: accepted M3 plan in `01_report_00.md`, completed by `01_report_01.md`, implemented under `02_implementation_00.md`
Acceptance allowlist: the 24 changed product paths plus referenced unchanged owners; pinned AP; public M3/M2 continuity records named in the prompt
Acceptance risk claims: schema preservation and save safety; bounded VirtualDesktopManager observation; deterministic five-zone resolution; controller recomputation and transport suppression; minimal usable UI; adequate causal tests; truthful scope and documentation
Acceptance control matrix: A1 through A8
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: L1 in-flight overlap (temporary synthetic probe; not a product diff)
Out-of-scope observations: ledger-candidates

## Independence

This session received the complete `03_acceptance_00.md` prompt as its governing task. Native Plan Mode was unused. No subagents. This session did not plan, implement, repair, or author the candidate and did not participate in M2 implementation. Inspection used disposable HTTPS clones detached at the required public commits, not a COOPERATOR checkout. Build products were outside the product clone. The product clone remained clean. Independence is claimed for this review; a green suite does not make the review self-certifying.

## Identity, provenance, and cleanliness

| Item | Value |
|---|---|
| Product start / required parent | `ca6052e816d4884ddeac9d7499a42c2aca089e7e` |
| Product candidate and public `main` | `55e981309718bcb2f94f809468eab9934acf5f51` |
| Direct `git ls-remote` product `main` | `55e981309718bcb2f94f809468eab9934acf5f51` |
| Candidate subject | `Implement M3 workspace-aware five-zone lighting` |
| Earlier M2 park parent of required parent | `ab10491c49d0b6574b6953a02935a4664c39d7c2` (ancestor of required parent) |
| AP gitlink and checkout | `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9` |
| `./.ap/ap doctor` | PASS |
| Public META baseline | `ee6f8c90414b15a87a8b1617cc561ca542768dcd` |
| Direct `git ls-remote` META `main` | `ee6f8c90414b15a87a8b1617cc561ca542768dcd` |
| Implementation-pair parent | `7452d615387db27595b701680b653fdf0120f0ee` (exact parent of META HEAD) |
| META HEAD changed paths | only `02_implementation_00.md` and `02_report_00.md` |
| Implementation prompt SHA-256 | `427ecd959f8d83968f8044fe5f36f35cfd7004e3cdba55a0f80234c0ea1c61d9` |
| Implementation report SHA-256 | `d77a944ec8b36624049234b653e712a29afb797ae5417c439ce1d4a5221a202b` |
| Product changed paths | exactly the 24 listed paths; none outside the allowlist |
| Product clone | clean detached HEAD throughout |
| Inspection META clone | clean detached HEAD |
| `git diff --check` parent..candidate | empty, exit 0 |

Earlier accepted-plan artifacts were not modified by the implementation-pair commit. Broker, RGB transport, KWin bridge, packaging, operations/testing-m2, hardware evidence, license, AP, and host files were unchanged.

SessionApplication gained only a named `WorkspaceReceiver` member, `setWorkspaceReceiver`, and `m_workspace.start()` logging `errorClass`. Existing broker IPC client start was not newly introduced by this diff and was not armed.

## A1–A8 matrix

| Row | Result | Blocking? |
|---|---|---|
| A1 Identity, provenance, and scope | PASS | no |
| A2 Schema 3 and preserving migration | PASS | no |
| A3 Save and backup safety | PASS | no |
| A4 Pure five-slot resolution | PASS | no |
| A5 VirtualDesktopManager receiver | FAIL | yes |
| A6 Controller, session app, and UI | PASS | no |
| A7 Causal regression evidence | FAIL | yes |
| A8 Documentation and bounded claims | PASS | no |

Acceptance-PASS is prohibited because A5 and A7 failed.

### A1 — PASS

Public product and META `main` matched the required SHAs by direct `ls-remote`. Ancestry, AP pin, doctor, 24-path diff, implementation-pair hashes, and clean read-only clones all matched. No scope escape into broker/RGB/KWin/packaging/host.

### A2 — PASS

`kSchemaVersion` is 3. Roles are only `Static`, `DesktopIndicator`, `AppColor`, and `Off`. Schema-3 zones are null or exactly five objects; `off` forbids `color`; dynamic roles are rejected in application lighting. Schema 1/2 readers remain; schema-2 five-color arrays become five Static slots; read does not rewrite bytes or activate workspace roles (`schema2ReadDoesNotRewriteBytes`, `schema1MigratesInMemoryWithoutRewritingFile`). Future schema 4, unknown fields, unknown roles, wrong counts, and `off` with color fail closed. Explicit save is the schema-3 persistence boundary. Invalid-color / some numeric-bound *tests* are missing (A7), but `parseColor` and speed integer bounds exist in `Persistence.cpp`.

### A3 — PASS

Save validates the draft, enforces 1 MiB, uses `QSaveFile` with `setDirectWriteFallback(false)` for backup and primary, and requires backup success before primary replacement. Invalid, unsupported, and schema-1 migration-fallback files are refused (`refuseOverwriteOfInvalidAndFallbackDocuments`). `failedSavePreservesPreviousBytes` and `backupRetainedAfterReplacement` cover preservation and previous-byte backup. Specification and architecture describe sequential `QSaveFile` backup then replacement and do not claim two-file transaction atomicity.

### A4 — PASS

`resolveContextLighting` prefers session override; inactive layout uses ordinary app/global resolution; active layout maps the first K indicator slots, current at 100%, inactive via `floor(channel/5)` (`dimInactiveDesktop`), absent black, explicit overflow, no wrap. `applicationSlotColor` implements Direct zones/base, Breathing (`baseColor` or `#7c3aed`), Off black, and Untouched/Wave/Cycle fallback. Unknown workspace returns untouched / `DeviceDefault`. All-black composition uses device Off. Synthetic protocol-5 encoding in `test_workspace_lighting` produces five colors and `UpdateMode` then `UpdateLeds`. Bridge loss is identity loss: unmatched identity uses app-slot fallback while workspace state is independent. Persistent tests do not cover every fallback row (A7).

### A5 — FAIL

Service/object/interface, subscribe-before-snapshot, GetAll snapshots, signal invalidation, count 1–32, unique bounded IDs/names/positions, 16 KiB metadata, current exactly once, position sort, signed/unsigned positions, owner generation, invalidation revision, coalesce, non-extendable deadline (`startDeadline` does not restart an active timer), recovery delays 1/2/4/8/16/30 s, pause/resume, and error-class logging are present in code.

The required one-in-flight-plus-one-pending invariant does **not** hold. `onSnapshotReply` always sets `m_inFlight = false` before applying the stale check. `onDeadline` and `onServiceOwnerChanged` also clear `m_inFlight` without cancelling the outstanding `QDBusPendingCall`. A logically stale watcher can therefore admit another `GetAll` while a newer request is still outstanding. Confirmed by static inspection and the temporary probe (L1). This is a candidate defect, not a Worker execution failure.

### A6 — PASS

`SessionApplication` owns `WorkspaceReceiver` via the default named connection `contextdeck-workspace`. `scheduleRecompute` coalesces; `recompute` defers workspace transport while `refreshPending` unless a session override is active; `sendLighting` suppresses equal `DesiredLighting`. Configuration-root injection defaults to empty → XDG/`~/.config` production path. QML for the four allowlisted pages compiled through the candidate's qmlcache build. Default 4+1, per-slot roles (global only), static conversion, gradient-replacement warning, desired-preview label, overflow/unavailable summary, and simulated pause copy are wired. No navigation redesign. Broker ARM UI on Diagnostics is pre-existing and was not activated by this diff.

### A7 — FAIL

Inspected test bodies, not names. Focused and full suites were green from the detached candidate in an external build directory (counts below). Receiver and lighting tests are wrapped with already-installed `dbus-run-session` and a fake `org.kde.KWin` `/VirtualDesktopManager`; they used a private bus, not the user session. Controller tests inject a temporary config root and a non-started `OpenRgbClient`.

Green aggregates do not satisfy the implementation prompt's required causal map. Missing durable assertions include:

- schema-3 invalid colors, non-object zone entries, and schema-3 numeric bounds;
- every schema-2 success form (Direct with absent zones; Cycle/Off preserve);
- full app-slot table: Direct-with-zones, Breathing, Cycle, Untouched;
- receiver count-mismatch, position/metadata-bound failures, actual list removal, retry-budget exhaustion after 1/2/4/8/16/30 s;
- deadline / owner-replacement late-reply overlap (the L1 interleaving);
- controller metadata-only name change does not increment lighting transport.

`staleReplyAndInvalidationBurst` bursts signals during a delayed GetAll but does not assert a single outstanding call. `ownerReplacementDeadlineAndRetryBudget` observes `refresh-deadline` and `recoveryAttempt() >= 1`, then pause/resume; it does not exhaust the retry budget and does not forbid overlapping GetAll.

### A8 — PASS

Docs describe schema 3, preserving migration, explicit save, VirtualDesktopManager observation, five-slot composition, limitations, and a later IRL checklist. ROADMAP/README call the tree an implementation candidate, not accepted. M2 remains parked with named Sessions 16/19/22/23/24 slices and residual independent G3 gap; full G4 is open. `docs/testing-m3.md` is a later COOPERATOR checklist and does not claim current physical, deployment, production, M4/M5, per-key, autostart, hibernate, general coexistence, or whole-G4 closure.

## Leads

### L1 — stale watcher versus newer in-flight request — confirmed — blocks acceptance

Code: `WorkspaceReceiver::onSnapshotReply` clears shared `m_inFlight` for every finished watcher, including stale generation/revision replies, then may `requestSnapshot()` from `m_pendingRefresh`. `onDeadline` increments `m_invalidationRevision`, sets `m_inFlight = false`, and does not cancel the transport call. `onServiceOwnerChanged` and `stop()` likewise drop the flag while watchers may still complete.

Temporary probe (Worker-owned disposable copy, private `dbus-run-session`, fake delayed GetAll 200 ms, deadline 40 ms, recovery 20 ms; deleted after capture): `received=3 max_outstanding=3 recovery=2 error=refresh-deadline availability=0`. Three overlapping GetAll calls existed. Product and META trees were not modified by the probe.

Consequence: more than one logical Properties.GetAll can be in flight; a late reply can start yet another request while a newer call is outstanding. Duplicate or reordered snapshots, extra D-Bus load, and a broken pending-refresh model follow. Existing tests stay green.

### L2 — claimed versus persistent causal coverage — confirmed — blocks acceptance

Implementation prompt required causal list versus actual assertions: several required rows have no persistent check (see A7). Aggregate 5/5 and 17/17 therefore do not close this lead. App-slot code contains the plan table, but tests only assert Direct-base, Wave, Off, and unmatched fallback. Schema-3 wrong types/invalid colors/numeric bounds are largely unasserted. Receiver count-mismatch, metadata bounds, removal, retry-budget exhaustion, and late-reply overlap are unasserted. Metadata-only RGB suppression is unasserted at the controller.

## Validation

Configure/build used existing tools with `env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH` as specified, Ninja generator, build directory outside the product clone. `dbus-run-session` was already installed (`find_program(... REQUIRED)` in the candidate). Nothing was installed.

Focused CTest regex `test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_lighting|test_openrgb_protocol`: **5/5 passed** in 1.08 s, exit 0. First causal failure: none.

Complete registered suite: **17/17 passed** in 2.71 s, exit 0 (`test_profile_resolver`, `test_profile_persistence`, `test_openrgb_protocol`, `test_broker_identity`, `test_broker_ledger`, `test_broker_forwarding`, `test_broker_acquisition`, `test_broker_watchdog`, `test_broker_ipc`, `test_broker_production`, `test_udev_policy`, `test_workspace_receiver`, `test_workspace_lighting`, `test_udev_verify`, `test_trial_cutoff`, `test_sleep_hook`, `test_broker_ipc_client`). First causal failure: none.

Private-bus classification: `test_workspace_receiver` and `test_workspace_lighting` (and the L1 probe) ran under `dbus-run-session`. They registered a fake `org.kde.KWin` only on that private bus. No real KWin, OpenRGB process, broker, ARM, grab, udev, or host mutation.

`git diff --check` parent..candidate: pass. Product clone `git status --short`: empty.

## Temporary probe

Identity: one Worker-owned disposable copy and build, outside the canonical product checkout, using the candidate's `WorkspaceReceiver` static library, Qt D-Bus, a fake delayed GetAll, and `dbus-run-session` only.

Design: delay 200 ms > deadline 40 ms so recovery can issue a second GetAll while the first call is still outstanding; record max concurrent outstanding replies.

Result: `max_outstanding=3` (invariant broken).

Cleanup: probe tree deleted after evidence capture. Not a product or META diff. Does not replace a missing durable regression.

## Confirmed defects

1. `WorkspaceReceiver` one-in-flight invariant is violated across deadline, owner replacement, pause/stop, and late replies (A5, L1).
2. Required persistent causal coverage named by the implementation prompt is incomplete (A7, L2).

## Missing persistent tests

See A7 list. Aggregate green is not a substitute.

## Disproved concerns

- Public `main` had not moved; identities matched.
- Candidate path count was exactly 24.
- Receiver tests are isolated by `dbus-run-session`, not the user session bus.
- Backup path is `QSaveFile` with direct-write fallback disabled, not remove-then-copy.
- Documentation does not claim two-file transaction atomicity or physical/M2/G4 closure.
- Schema-2 five-color read does not enable workspace layout or rewrite bytes (tested).
- Subscribe-before-snapshot race is tested (`subscribeBeforeSnapshotRace`).
- Duplicate snapshot suppression is tested (`serviceLossAndDuplicateSnapshot`).
- All-black Off conversion is tested.

## Residual risks

Physical five-zone visibility, device-default restoration, compositor hang without D-Bus events, M2/G4, independent G3, deployment, autostart, and IRL checklist remain unproven. After a deadline the outstanding D-Bus call is only logically stale; late replies can still mutate in-flight accounting.

## Deviations

Validation used `env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH` as required by the prompt because the ambient Cursor AppImage pollutes those variables (`cmake` without unsetting reports missing `CMAKE_ROOT`). That is an environment workaround, not a dependency change.

## Out-of-scope ledger candidates

- `AppController::remappingState` still returns `inactive-until-M2` even though M2 production code exists; wording drift, not an M3 layout defect.
- Diagnostics still contains pre-existing Arm/Disarm/lease controls; this candidate did not start the broker.
- ROADMAP still duplicates M4/M5 table rows (pre-existing).

Resolved Execution Issues / Near-Misses: ambient AppImage `LD_LIBRARY_PATH`/`QT_PLUGIN_PATH` breaks CMake unless unset as specified; focused/full suites then ran. No product mutation was used to work around it.

Pre-Existing Failure Classification: OpenRGB client refusal of all-black Direct remains; workspace composition maps that case to device Off, as planned. Not a new transport defect.

## META persistence

External trace disposition: configured
Trace project key: contextdesk
Trace logical-whole projection identity: 03-g213-contextdeck-workspace-aware-lighting
Trace archival owner: COOPERATOR
Trace self-granted status: none

The exact received prompt was already present at
`projects/contextdesk/00/03-g213-contextdeck-workspace-aware-lighting/03_acceptance_00.md`
and is byte-identical to the delivered attachment (SHA-256
`b18f80b2a0a52243aa3f47c48a38206ed8bc6d161ebb9619a4baf06cbff373d7`, 22977 bytes).
It was read back completely and not overwritten.

This report is written to
`projects/contextdesk/00/03-g213-contextdeck-workspace-aware-lighting/03_report_00.md`
and read back completely. META Git add/commit/push remains COOPERATOR-owned. Archive the exact prompt/report pair together afterward. No other META paths were written. No META history mutation was performed.

## Non-claims

Code acceptance is not physical acceptance and does not prove M2/G4 closure, deployment, production readiness, G3 re-audit, autostart, hibernate/hybrid sleep, general input-remapper coexistence, M4/M5 behavior, per-key RGB, or measured control-to-zone placement. This PARTIAL is not acceptance-PASS.

**Smallest next step:** ORCHESTRATOR reconciliation. One bounded correction slice, not granted here: fix `WorkspaceReceiver` so in-flight ownership is bound to the current watcher (stale/late replies must not clear a newer request; deadline/owner-change/stop must cancel or ignore the old transport call), and add durable private-bus plus persistence/resolver/controller regressions for L1 and the required A7 gaps listed above. Do not start the physical M3 checklist on this candidate.

Orchestration critique:

MEASURED: `onSnapshotReply` unconditionally clears `m_inFlight`; a delayed GetAll plus non-cancelled deadline produced three overlapping GetAll on a private bus (`max_outstanding=3`). Effect: A5 FAIL and acceptance-PASS prohibited. Smallest correction: current-watcher ownership plus one causal overlap regression, together with the named missing required tests.

LEAD: none remaining inside this acceptance boundary; physical IRL remains a later COOPERATOR surface after a passing code acceptance.

Logical-whole closure: not-closed

Authority for this Worker expires at this terminal report.
