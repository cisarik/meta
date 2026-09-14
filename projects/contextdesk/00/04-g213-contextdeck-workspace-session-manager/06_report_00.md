### Report for ORCHESTRATOR_CHAT

Logical whole identity: g213-contextdeck-workspace-session-manager
Worker session ordinal: 06
Worker exchange ordinal: 01
Persistent role identity: WORKER

```text
Worker session target: fresh-worker-session
Worker session profile: Worker-Executed Preflight
Phase: Preflight
Task identity: CONTEXTDECK-M4-SLICE-B-PREFLIGHT
Native planning mode: not-used
status: PASS
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: read-only preflight evidence package; no implementation or acceptance result exists
Report justification: new-evidence
```

This is a bounded read-only preflight for the later M4 Slice B
(mutation/launch/placement) implementation. It re-plans nothing, accepts
nothing, and authorizes nothing. The single outcome is the readiness verdict
below plus the evidence and constraints a separately authorized Slice B
implementation prompt must carry.

## Scope, authority, and live-session reality

All inspection was read-only: Git ref/status/log reads, filesystem reads of
product sources, docs, installed KWin development headers and KF6 CMake package
files, `./.ap/ap doctor`, one read-only `git ls-remote` per canonical remote,
and one read-only `gdbus introspect` of the live KWin desktop manager. No
desktop configuration write, no `kwinrulesrc` write, no application launch, no
service start, no session/broker/OpenRGB start, no device access, no package,
dependency, lockfile, or toolchain change, no product/AP/META Git mutation. No
test or build was run; the ignored existing `build/` checkout was not touched.
Network use was limited to the two canonical HTTPS ref reads.

The execution environment did expose a live KDE Plasma session on Wayland with
an active session bus, so live host facts in Q2 are directly observed rather
than inferred. Reported live facts are semantic only: interface/property/method/
signal names, one desktop **count**, the `rows` value, and a wrapping boolean.
No desktop name or desktop UUID was recorded anywhere in this report.

## Q1 — Product / AP / repository state

- **Directly observed.** Canonical product `https://github.com/cisarik/contextdesk`:
  direct `git ls-remote refs/heads/main` returned
  `aca6c68542bbc9f1b8ee891415a04b0a95e8372e`, equal to local detached/attached
  `HEAD` on branch `main`; subject `Add M4 Slice A diagnostics privacy regression`.
  `git status --porcelain` empty, `git diff --stat` empty, no `index.lock`, no
  active Git operation. Only the ignored `build/` directory exists as untracked
  material.
- **Directly observed.** AP gitlink and `.ap` checkout both
  `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`; `.ap` submodule clean;
  `./.ap/ap doctor` = `PASS`, resolved governing variant `stable`, managed
  `AGENTS.md` block OK.
- **Directly observed.** Canonical META `https://github.com/cisarik/meta.git`:
  direct `git ls-remote refs/heads/main` returned
  `977c841cd18e1e733ab752d7e64f068d9079d812`, equal to local META `HEAD`; no
  descendant. M4 trace pairs `00`–`05` are committed at add-only pair commits
  (`6f14316` planning pair, `c7e1b73` completion pair, `640b65d` implementation
  pair, `06439c9` acceptance pair, `f64c634` correction pair, `977c841`
  acceptance pair). Artifact SHA-256 recomputation in the worktree equals every
  previously recorded identity: `01_report_00.md`
  `44f01b82155a6ad584f8d1f0d5851e7020dbf4b6b1d330b1862ec06c05e34fdc`,
  `01_report_01.md`
  `4a968b7694f5c8294c8674351827511f826a903db9a96aae9e83670360239f94`,
  `02_implementation_00.md`
  `b8fa2a274185c1bf784d444f50935fb82dd199e3b638ba7e3a0e736773469d38`,
  `02_report_00.md`
  `7570ee7999e684bb037fed63c7a2edc79f15fde1f2afe3a44ae1f2d69d7f8ce6`,
  `03_report_00.md`
  `8dce3dc3f98848c230c75b9e9f004430be78253b1c60aea60de01e043ba0c3d3`,
  `04_correction_00.md`
  `2e75ad46f995e83e8313580fd7d6c0693a8e52640a6b08cd1e659df72c359d9f`,
  `04_report_00.md`
  `2498af6f0f3b47181b121608623b44c5506b3c77d2c418913ce29e02dd475b13`.
  No earlier M4 artifact changed. The trace directory and every parent are real
  directories, not symlinks. This exchange's prompt
  `06_preflight_00.md` is present as a regular file, untracked pending
  COOPERATOR first-add; `06_report_00.md` did not exist before this write.
- **Readiness implication:** all immutable gates hold; Slice B can build on this
  exact product candidate and this exact plan. No prerequisite is missing.

## Q2 — Live KWin D-Bus surface (VirtualDesktopManager)

- **Directly observed** via one read-only `gdbus introspect` of
  `org.kde.KWin` `/VirtualDesktopManager`:
  - interface `org.kde.KWin.VirtualDesktopManager` present;
  - properties: `count` (readonly `u`; observed **3**), `current` (readwrite
    `s`), `rows` (readwrite `u`; observed **1**), `navigationWrappingAround`
    (readwrite `b`; observed **false**), `desktops` (readonly `a(iss)`;
    observed **3** entries);
  - methods: `createDesktop(u position, s name)`,
    `setDesktopName(s id, s name)`, `removeDesktop(s id)`;
  - signals: `countChanged(u)`, `rowsChanged(u)`, `currentChanged(s)`,
    `navigationWrappingAroundChanged(b)`, `desktopDataChanged(s,(iss))`,
    `desktopCreated(s,(iss))`, `desktopRemoved(s)`.
- Every member named by the preflight question is present. The accepted plan's
  observation (`count`/`current`/`rows`/`navigationWrappingAround`/`desktops`,
  `createDesktop`/`setDesktopName`/`removeDesktop`, `rowsChanged`/
  `navigationWrappingAroundChanged` as the newly subscribed signals) is
  confirmed and additionally the `desktopCreated`/`desktopRemoved` signals the
  Slice B launch trigger needs are present. `count` is readonly, so count
  changes go only through create/remove.
- **Directly observed (source).** The candidate's `WorkspaceReceiver` already
  subscribes `currentChanged`, `countChanged`, `desktopCreated`,
  `desktopRemoved`, `desktopDataChanged`, `rowsChanged`, and
  `navigationWrappingAroundChanged` as invalidations
  (`src/context/WorkspaceReceiver.cpp`), but discards the message payload. The
  in-transaction `desktopCreated` launch trigger therefore needs a bounded
  Slice B event surface (signal or snapshot-diff classification), not a new
  D-Bus subscription.
- **Readiness implication:** the Slice B D-Bus mutation and trigger surface is
  fully available on the live host. No blocker.

## Q3 — KWin scripting API assertions

- **Directly observed** in the installed KWin development headers:
  - `/usr/include/kwin/window.h` declares
    `Q_PROPERTY(QList<KWin::VirtualDesktop *> desktops READ desktops WRITE setDesktops NOTIFY desktopsChanged)`
    — `window.desktops` is writable;
  - the same header declares only `maximizable` and read-only
    `Q_PROPERTY(KWin::MaximizeMode maximizeMode READ maximizeMode NOTIFY maximizedChanged)`;
    there is no writable `maximized` property;
  - the same header declares
    `Q_INVOKABLE void setMaximize(bool vertically, bool horizontally, const RectF &restore = RectF());`
    — maximization must use `setMaximize(true, true)`;
  - `/usr/include/kwin/virtualdesktops.h` declares `VirtualDesktop.id` as a
    CONSTANT `QString` and writable manager `count`, `current`, and
    `navigationWrappingAround` properties.
- The accepted plan's two asserted corrections — writable `window.desktops`,
  non-writable `window.maximized` requiring `setMaximize(bool,bool)` — are
  confirmed on the installed API.
- **Inferred.** The bridge already uses KWin scripting `callDBus` for
  fire-and-forget reports; the plan's `PlacementHint(...) -> (desktop_id,
  maximize)` shape requires the KWin scripting `callDBus` trailing-callback
  form. That callback form was not independently verified from an installed
  scripting reference in this preflight. This is an implementation-time check,
  not a blocker; a synthetic script check or the installed KWin scripting
  reference resolves it inside Slice B implementation.
- **Readiness implication:** placement/maximize is technically reachable exactly
  as planned; one bounded implementation-time API check is named.

## Q4 — Launch and build capability

- **Directly observed.** CMake config packages present:
  `/usr/lib/cmake/KF6Service/` (target `KF6::Service`) and
  `/usr/lib/cmake/KF6KIO/` (targets `KF6::KIOGui`, `KF6::KIOCore`,
  `KF6::KIOWidgets`, `KF6::KIOFileWidgets`). There is no separate `KF6KIOGui`
  package; `KF6::KIOGui` is a target of the `KF6KIO` package. Both package
  version configs are 6.30.0, matching the installed `libKF6KIOGui.so.6.30.0`,
  `libKF6KIOCore.so.6.30.0`, and `libKF6Service.so.6.30.0`.
- **Directly observed.** `/usr/include/KF6/KIOGui/kio/applicationlauncherjob.h`
  exists and declares `KIO::ApplicationLauncherJob` with
  `explicit ApplicationLauncherJob(const KService::Ptr &service, QObject *parent = nullptr)`,
  `setUrls`, and `start()`. `KService::serviceByStorageId` is declared in
  `/usr/include/KF6/KService/kservice.h`, and `KApplicationTrader::query` in
  `/usr/include/KF6/KService/kapplicationtrader.h`.
- **Directly observed.** Transitive config dependencies needed by `KF6KIOConfig`
  and `KF6ServiceConfig` are all present (`KF6CoreAddons`, `KF6Config`,
  `KF6WindowSystem`, `KF6I18n`, `KF6Crash`).
- **Directly observed (source).** `CMakeLists.txt` currently uses per-component
  config-mode lookups (`find_package(KF6StatusNotifierItem/KF6Kirigami/KF6Screen
  REQUIRED)`) and has no KIO/KService dependency.
- **Exact new build dependency for Slice B:** `find_package(KF6Service REQUIRED)`
  and `find_package(KF6KIO REQUIRED)`, linking `KF6::Service` and
  `KF6::KIOGui` into the session-application target (or a small new static
  library). No `extra-cmake-modules`, no umbrella `KF6`, no package install, no
  lockfile or toolchain change. The host already satisfies it.
- **Readiness implication:** typed launch is buildable now with no host
  mutation at build time.

## Q5 — Exact proposed Slice B mutation boundary and reversibility

Restated from the accepted plan (`01_report_00.md` §2 table, §5, §6; ADR 0002,
ADR 0004). Live UUIDs are runtime-only; durable identity stays ordinal-based.

| Operation | Exact shape from the plan | Reversibility | Disposition |
|---|---|---|---|
| `createDesktop(position, name)` | trailing-only, create each missing ordinal up to desired count; never implicit; 1-based schema ordinal maps to 0-based D-Bus position | reversible-with-side-effects: revert removes exactly the desktops this Apply created; KWin may move windows off a removed desktop (**inferred** compositor behavior) | default Apply |
| `setDesktopName(id, name)` | only when the live name for that ordinal differs from the desired name; uses the live UUID for that ordinal | reversible: inverse rename from checkpoint | default Apply (conditional) |
| `rows` / `navigationWrappingAround` | `Properties.Set` only when the preview diff is non-empty | reversible: set checkpoint values | default Apply |
| `current` | optional `Properties.Set` only when the user chose "switch to this session"; never on `currentChanged` | reversible if the checkpoint UUID still exists; otherwise skip and report | excluded from default Apply; explicit opt-in |
| `removeDesktop(id)` | explicit "remove extras" only, after preview; never part of default Apply | **irreversible-ish**: UUID is destroyed, recreation mints new UUIDs, windows on it are displaced by KWin (inferred), no undo except recreate-from-checkpoint by ordinal | excluded from default Apply; needs its own explicit confirmation and an explicitly named mutation-class grant in the IRL run |
| typed application launch | `KService::serviceByStorageId` + `KIO::ApplicationLauncherJob` for a typed `.desktop` id; only on explicit `applyWorkspaceSession` and on an in-transaction `desktopCreated`; skip when inventory already matches; one attempt per profile per transaction (2 s debounce), at most one bounded retry on the matching in-transaction `desktopCreated`; bounded error class | not reverted: M4 never kills a launched application | explicit Apply + per-profile `launch` opt-in |
| bridge placement / maximize | on `windowAdded`: `PlacementHint(desktop_file_name, resource_class, resource_name)`; `window.desktops = [matched id]`; `setMaximize(true, true)` when requested; empty id = no-op; identity match wins over title fallback | not reverted: the window stays where it was placed; maximize can be changed by the user | per-profile `maximize` opt-in; event-driven; no `kwinrulesrc` |
| `kwinrulesrc` write | rejected by the product | n/a | never |

- **Exclusion recommendation.** Default Apply must be exactly create + conditional
  rename + rows/wrapping. `removeDesktop`, the optional `current` switch, launch,
  and maximize/placement stay outside the default path and must be separately
  disclosed opt-ins. The IRL grant must name the desktop create/rename/remove/
  rows/wrapping/current classes, application launch, and bridge reload
  individually; none of them is implied by the code grant.
- **Readiness implication:** the boundary is exact, bounded, and unchanged from
  the accepted plan. No new product decision is required to start Slice B.

## Q6 — Checkpoint and backup

- The planned checkpoint is a user-local `workspace-checkpoint.json` under the
  product config root (`$XDG_CONFIG_HOME/contextdeck/`, fallback
  `$HOME/.config/contextdeck/`), never the profile document, never META, never
  logs; the plan and ADR 0002 already forbid logging desktop names/ids.
- **Sufficient and safe if** the Slice B implementation pins all of: atomic
  write (`QSaveFile`), user-only permissions, overwrite-per-Apply,
  checkpoint-write-success-before-first-mutation, and a clear retention/cleanup
  rule (retain until a successful revert or the next Apply; delete on
  successful revert). The checkpoint contains runtime desktop names/UUIDs; that
  is acceptable only because it stays user-local runtime state and is never
  promoted to durable identity.
- **Rebinding after `removeDesktop`:** durable assignments store
  `desktop_ordinal` (schema 4), so a remove/recreate that mints new UUIDs
  rebinds automatically once the fresh `getAll` snapshot is mapped
  ordinal-to-UUID by the receiver. No UUID is stored in the profile, so there
  is **no gap for assignment rebinding**.
- **Exact gaps the Slice B prompt must pin (none requires replanning):**
  1. **Revert-count ownership.** The plan's IRL criterion ("confirm invert via
     checkpoint … confirm the previous layout returns") implies revert restores
     the checkpoint desktop count after a default Apply. The forward operation
     is create, so its inverse is removal. The Slice B prompt must state that
     revert removes exactly the UUIDs recorded as created by this Apply (and
     never a desktop it did not create, including user-created extras), and must
     disclose the window-displacement consequence.
  2. **`current` restore.** If the checkpoint `current` UUID no longer exists
     after a remove/recreate, revert skips the switch and reports it as a bounded
     residual instead of guessing by ordinal.
  3. **Checkpoint lifecycle.** File permissions, atomic write, overwrite/
     cleanup rule, and the no-log/no-META rule must be explicit.
  4. **Already-open windows.** Revert is desktop-configuration-only; a window
     already open before revert is not moved back, because placement is
     `windowAdded`-driven. This is a bounded, disclosed limitation.
- **Readiness implication:** checkpoint/rollback is sufficient with those four
  pinned requirements; they are implementation-prompt content, not open product
  decisions.

## Q7 — Recovery and stop rules

- **Preconditions before the first mutation (all fail-closed):**
  1. explicit user Apply with `workspace_management_enabled` and a valid,
     validated, saved session (`WorkspacePlan.sessionFound`, 1–32 desktops,
     contiguous ordinals);
  2. observation `Available` and fresh for the exact preview the user saw (no
     pending refresh, no in-flight receiver request); `Unknown`/stale stops;
  3. no KWin service-owner change and no drift between preview and Apply; any
     difference stops and re-previews;
  4. checkpoint written, verified, and atomic; failure stops before mutation;
  5. an explicit per-option decision for the opt-ins in use (`removeDesktop`
     "remove extras", optional `current` switch, launch, maximize);
  6. the exact Slice B allowlist and no out-of-grant operation.
- **Step ordering (derived from the plan, for the Slice B prompt):**
  verify preconditions → write and verify checkpoint → create missing trailing
  desktops ascending → rename non-matching desktops ascending → set `rows` if
  changed → set wrapping if changed → optional explicit `current` switch →
  explicit `removeDesktop` for the opted-in extras only → launch for
  `would_launch` profiles → placement/maximize arrives via the bridge on
  `windowAdded` → end the transaction (debounce reset). Each step gates the
  next; any error stops the sequence.
- **Abort/revert on partial failure:** stop at the first error and preserve the
  first causal failure; then run revert from the checkpoint: restore count via
  removal of exactly this-Apply-created UUIDs, restore names by ordinal, restore
  `rows`/wrapping checkpoint values, restore `current` only if its UUID still
  exists. If revert itself fails, stop with a bounded residual-state report,
  keep the checkpoint for an independent recovery route, and never loop or
  retry-storm. Launch and placement effects are not reverted; no application is
  killed.
- **Fail-closed:** any false precondition, any mutation error, any unexpected
  drift or owner loss, any need for an out-of-grant operation (including a
  `kwinrulesrc` fallback) means no first mutation or an immediate stop; nothing
  is silently widened.
- **Readiness implication:** a concrete, testable abort/revert and stop-rule set
  exists and can be carried verbatim into the Slice B prompt.

## Q8 — Acceptance plan

- **Confirmed route.** Slice B code (mutator/launcher, bridge placement/
  maximize, Apply UI, tests, docs) → one product commit and normal push →
  **fresh independent code acceptance** of that exact public candidate →
  **separate bounded COOPERATOR-owned IRL run** per `docs/testing-m4.md`:
  named profile checkpoint; explicit Apply with create/rename intent preview;
  invert via checkpoint; launch-on-apply once with no duplicate on second
  Apply; placement/maximize of the new window through the bridge; opt-in title
  fallback with flag-disabled non-match; quit without input impact.
- **Confirmed ownership.** All live desktop mutation (create/rename/remove/
  rows/wrapping/current), application launch, and the KWin bridge reload
  (`loadScript`/`kpackagetool6`) are COOPERATOR-owned host operations. They are
  **not** part of this preflight and **not** part of Slice B code execution.
  Slice B code execution is repository-only: implement, build, run the
  registered CTest suite on the private `dbus-run-session` fake, commit, push,
  verify.
- **Readiness implication:** the acceptance route is correct and already
  documented; the IRL run needs its own explicit grant.

## Q9 — Privacy and capability posture

- **Confirmed.** The Slice B design can run without logging captions, desktop
  names, or UUIDs: captions are compared only in memory for one call in
  `titleFallbackMatches`; a `TitleHint` seventh field is emitted only when both
  fallback flags are enabled, is discarded after the call, and its arguments are
  never logged; diagnostics expose counters only
  (`title-fallback-matched` / `title-fallback-ignored`), never strings; the
  checkpoint is user-local runtime state and never enters logs, prompts,
  reports, or META.
- **Confirmed residual plan.** The `05_report_00.md` acceptance residual (a
  future live caption producer outside the document-seeded diagnostics test)
  is exactly the Slice B `TitleHint` producer. The Slice B implementation must
  add a live-caption-path privacy guard when that producer is introduced (a
  regression or explicit diagnostics key-category coverage plus the no-argument-
  logging guarantee). The plan already requires the counters and the no-log
  rule; the test is the concrete guard.
- **Readiness implication:** privacy is designable and testable inside Slice B
  with one named required regression; no unresolved privacy decision remains.

## Q10 — Required capability

- **Later Slice B implementation grant (repository-only):**
  - build-dependency authority to add `find_package(KF6Service REQUIRED)` and
    `find_package(KF6KIO REQUIRED)` and link `KF6::Service`/`KF6::KIOGui`; no
    install and no network dependency change;
  - exact Slice B changed-path allowlist (to be defined by the ORCHESTRATOR;
    expected touch points: new workspace mutator/launcher sources,
    `src/app/AppController.*`, `src/app/SessionApplication.*`,
    `src/context/WorkspaceReceiver.*` or an event façade for the
    in-transaction `desktopCreated` trigger, `src/context/ContextReceiver.*`
    for `PlacementHint`, `ui/*`, `kwin/contextdeck-bridge/contents/code/main.js`
    + metadata, `CMakeLists.txt`, `tests/unit/*`, ADR statuses,
    `docs/testing-m4.md`);
  - one product commit and one normal non-force push with public-ref
    verification;
  - private-bus tests only; no real KWin call, no launch, no device, no broker,
    no host mutation at build time or test time.
- **Separate COOPERATOR-owned IRL run:**
  - explicit mutation-class authority: live `createDesktop`, `setDesktopName`,
    `removeDesktop`, `rows`/`navigationWrappingAround`/`current` writes, typed
    application launch, and the KWin bridge reload;
  - a named checkpoint: a copy of the profile document plus the product's
    `workspace-checkpoint.json` mechanism;
  - one demonstrated recovery route not related to input grabbing: demonstrate
    the checkpoint invert (the `docs/testing-m4.md` step-3 revert) before
    proceeding to launch/placement; the M2 second-keyboard/SSH grab route is not
    the M4 mechanism because M4 never grabs input, but `docs/testing-m4.md`
    precondition 2 still requires an independent session recovery route to be
    available for the whole run.
- **Readiness implication:** the capability envelope is clear and separable;
  implementation authority and host authority stay distinct.

## Mutations in this exchange

This exchange mutated nothing: no desktop configuration, no application launch,
no `kwinrulesrc`, no KWin/Plasma setting, no service, no session/broker/OpenRGB
start, no device, no package/dependency/lockfile/toolchain change, no product
Git, no AP, and no META Git change. The only file written in this exchange is
this report.

## Deviations, risks, missing evidence, ledger candidates

- **Deviations:** none material. Mandatory reading was completed, including the
  accepted plan, its completion, the Slice A implementation pair, the Slice A
  acceptance, and ADRs 0002/0003/0004. No test or build was run (one exists as
  an ignored `build/` directory); that is consistent with the read-only
  authority. The persisted prompt was read back completely and its content
  matches the delivered prompt field-for-field; a byte-level comparison against
  the chat transport is not observable from here, so byte identity is asserted
  against the persisted file (SHA-256
  `53edfeabbeec6bdc9cdf925b2a8f7b7674f8bfee3fe035b59f19ee189ca56175`).
- **Observed trace state:** META's worktree also contains one pre-existing
  unrelated untracked file under a different project's trace; it was not
  touched, and it does not affect the M4 trace or the pinned baseline.
- **Risks / missing evidence (non-blocking, ledger candidates):**
  1. KWin scripting `callDBus` trailing-callback support for `PlacementHint` is
     inferred; cheapest check is a Slice B implementation-time API check or
     synthetic script probe.
  2. KWin's window-displacement behavior when a desktop is removed is inferred;
     the IRL run's checkpoint revert is the bounded response.
  3. The checkpoint revert-count/ownership semantics, `current`-restore skip,
     and checkpoint lifecycle must be pinned in the Slice B prompt (Q6 gaps).
  4. The live-caption privacy regression must accompany the `TitleHint`
     producer.
  5. QML runtime behavior remains exercised only by build-time compilation until
     the IRL run; inherited from the Slice A acceptance.
  6. The bridge reload during IRL is host mutation and must be named in the IRL
     grant.
- **Not ledger candidates (already accepted):** the launch trigger set,
  duplicate/debounce rules, `setMaximize(bool,bool)`, no-`kwinrulesrc`, and the
  M4/M5 autostart split.

## Smallest next step

ORCHESTRATOR reconciliation of this preflight and a COOPERATOR decision on
whether to authorize a Slice B implementation grant; a PASS here only
recommends that separate authorization and grants nothing.

Orchestration critique:

MEASURED: The candidate's `WorkspaceReceiver` already subscribes
`desktopCreated`/`desktopRemoved`/`desktopDataChanged` and discards their
payload, while the accepted plan's launch trigger needs the
in-transaction-created ordinal; effect is that Slice B needs a bounded event
surface rather than a new subscription; evidence is
`src/context/WorkspaceReceiver.cpp` versus the live introspection; smallest
correction is to name that event surface in the Slice B allowlist.

LEAD: KWin scripting `callDBus` may not support the trailing-callback reply form
the `PlacementHint` arrow implies; cheapest useful check is reading the
installed KWin scripting reference or a synthetic script probe at Slice B
implementation time.

Explicit non-claims: no implementation-PASS, acceptance-PASS, deployment-PASS,
production readiness, physical acceptance, M2/G4 closure, G3 re-audit,
autostart, hibernate/hybrid sleep, general input-remapper coexistence, M3
closure, M3 physical five-zone observation, live desktop/launch/placement
behavior, remapping, deck behavior, M5 integration, per-key RGB, or measured
control-to-zone placement. This preflight does not authorize Slice B and does
not accept the Slice A candidate.

Logical-whole closure: not-closed

Authority for this Worker expires at this terminal report.
