Logical whole identity: g213-contextdeck-workspace-session-manager
Worker session ordinal: 01
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Planner
Phase: planning
Task identity: CONTEXTDECK-M4-WORKSPACE-SESSION-MANAGER-PLAN
Native planning mode: required
Delivery route: manual COOPERATOR delivery to a genuinely fresh Worker session
Reasoning recommendation: High
Reasoning basis: the bounded plan must reconcile live host desktop-configuration
mutation authority, a durable assignment-schema decision, a typed application
launch lifecycle, compositor placement/maximization, and an opt-in
non-logging title fallback without drifting into M5 autostart or M2 input.
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E3
Evidence-tier basis: eventual implementation can mutate the live desktop
configuration and durable user schema and needs a separate fresh acceptance,
even though this planning exchange itself is read-only.
Internal delegation: prohibited

# ContextDeck M4 — plan the workspace session manager whole

You are a genuinely fresh WORKER assigned only to repository-grounded
implementation planning. Use the client's actual Native Plan Mode. You did not
participate in M1, M2, or M3 implementation or acceptance and inherit no
authority from any previous session. Do not dispatch subagents.

This is a planning grant only. It authorizes no product implementation, no host
operation, no deployment, no acceptance execution, and no Git publication. Stop
at the terminal planning report.

## Planning record and Plan-to-Execution gate

Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: M1 five-zone/OpenRGB and application-context
architecture; M3 code-accepted-but-not-physically-observed boundary; parked M2
boundaries; future remap/deck/M5 separation
Automatic targeted revisions used: 0

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: one repository-grounded, decision-complete M4 plan for
managing virtual desktops, assigning applications to desktops, launching
assigned applications on desktop/session-management events inside an already
running session, maximizing/placing them on their assigned desktop, and an
opt-in, event-driven, non-logging title fallback for unassigned focused windows
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: a separate complete ORCHESTRATOR implementation
prompt whose native planning-mode value is `not-used`
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1

The ORCHESTRATOR reconciles the plan before any implementation prompt. Native
Plan approval, "continue", retained context, or the existence of this prompt
never grants execution authority.

## Verified public candidate

Canonical product repository: `https://github.com/cisarik/contextdesk`
Expected branch: `main`
Exact product candidate:
`502ae75571358ec95d33c836084b5e2253850731`
Required parent:
`55e981309718bcb2f94f809468eab9934acf5f51`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

Canonical META repository: `https://github.com/cisarik/meta.git`
Verified public META baseline:
`3861a6354b4f900ee50b26627be9a6786b5909f0`
M2 park trace:
`projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/`
M3 trace:
`projects/contextdesk/00/03-g213-contextdeck-workspace-aware-lighting/`
M4 trace destination:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/`

Before planning, verify without changing repository state:

1. Product root, canonical remote, active `main`, clean worktree, exact HEAD,
   exact parent, no Git operation or lock, AP gitlink/checkout equality, and
   `./.ap/ap doctor` PASS with variant `stable`.
2. Direct `git ls-remote` for product `main` equals the exact candidate. Do not
   fetch, pull, switch, reset, clean, stash, rebase, merge, or retarget.
3. Direct `git ls-remote` for META `main` equals the exact baseline above or a
   verified later descendant. If later, inspect its changed paths and accept it
   only if it does not contradict this prompt.
4. The M4 trace directory exists as a real directory containing the
   ORCHESTRATOR-authored `00_notes.md` and the optional `00_handout.md`. The
   M3 and M2 trace directories exist and contain the reports named below.
5. Apart from the exact M4 prompt/report preparation authorized below, preserve
   all owner work and stop on unexplained state.

If the product candidate, parent, AP pin, public ref, trace identity, or
repository state differs materially, stop before planning and return `BLOCKED`.
Do not silently use a nearby commit or an old clone.

## Authoritative continuity boundary

Use this exact M3 park wording wherever M3 state is restated:

> M3 workspace-aware lighting is code-accepted on `502ae75...`; its physical
> five-zone IRL observation is deferred by explicit COOPERATOR decision. M3 is
> not closed, and code acceptance is not physical acceptance.

Use this exact M2 park wording wherever M2 state is restated:

> The named live G4 slices are accepted, but the M2 logical whole remains open.
> M2 is parked with G3 host-mitigated on the authorized reference host; the
> next bounded whole is M4 workspace session manager.

Preserve these named accepted boundaries without rerunning them:

- Session 16: independently demonstrated SSH recovery, explicit authenticated
  ARM, sampled pass-through, invocation-bound cutoff/death, and post-death
  recovery.
- Session 19: GUI ARM, held-modifier watchdog abort, no restart/re-grab, and
  post-death recovery.
- Session 22: one real suspend/resume with pre-freeze stop, conditional
  disarmed restart, STATUS-only reconnect, and post-resume typing.
- Session 23: compositor LED return, deterministic LED-write failure, all
  eighteen measured host-remappable controls, explicit DISARM, and inactive
  cleanup.
- Session 24: one bounded existing non-G213 input-remapper mapping preserved
  before/during/after one armed G213 trial.

Do not issue, revive, or simulate `27_deployment_00.md`; do not reopen G3.

## COOPERATOR decisions recorded at this handoff (2026-09-14)

These are binding inputs to the plan:

1. **M4 is the selected whole.** The launch-at-Plasma-session-start concern
   belongs to M5/G8, not M4. M4 scopes launching to desktop or
   session-management events inside an already running session. The plan must
   draw this boundary explicitly.
2. **Plan now is read-only.** The plan may *model* eventual desktop
   `createDesktop`/`removeDesktop`/`setDesktopName`/`rows` changes and
   `kwinrulesrc` writes, but no mutation is authorized in this planning
   exchange. Every eventual mutation class must carry its own later bounded
   authority, with an explicit revert/checkpoint/recovery path and a named
   checkpoint. Prefer a first implementation slice that is read-only/observational
   and a separately authorized later mutation slice.
3. **Title fallback.** A caption-based fallback is acceptable only when
   opt-in, event-driven, and never polling. Define exactly what (if anything) is
   compared, stored, or surfaced; captions and titles must never be logged,
   persisted in the trace, or used as default identity.
4. **UI/UX polish is a separate later whole.** This M4 plan must not schedule a
   UI/UX review-and-polish slice. Any UI/controller change the plan genuinely
   needs for M4 functionality must be minimal and truthful, and must not
   silently change accepted M1 or M3 semantics.
5. **M3 physical testing stays deferred.** M3 remains not-closed. Do not plan
   or request the `docs/testing-m3.md` run as M4 work.

## Product boundary and invariants

ContextDesk is a Linux/KDE Plasma 6/Wayland cockpit for one Logitech G213.
Preserve:

- Logitech G213 Prodigy only, USB `046d:c336`; no other keyboards, no generic
  remapper, no Windows/macOS. Target CachyOS/Arch, Plasma 6, KWin, Wayland,
  systemd, C++20/Qt6/KF6.
- Exactly five honest RGB zones, never per-key RGB. Zone order: Left Area,
  Middle Area, Right Area, Arrow and Homekeys, Numpad.
- Foreground context is event-driven through the KWin scripting API — no
  `xdotool`/`wmctrl`/`xprop`, no title polling. Prefer KWin
  `desktopFileName`/`resourceClass`/`resourceName` identity over `/proc` or
  window captions.
- The session app never opens raw keyboard event nodes; only the input broker
  does, and it starts disabled. Never automatically ARM after restart, resume,
  crash, or reconnect. M4 must not start, ARM, grab, or probe the broker.
- One persistent OpenRGB SDK connection on loopback (protocol 5); one RGB
  backend at a time.
- Typed action model only: no arbitrary shell strings. Fail-safe default is
  pass-through; unset means inherit, not swallow.
- G213 controls in scope: F1–F12, Previous, Play/Pause, Next, Mute, Volume
  Down, Volume Up, Game Mode, Backlight. Game Mode and Backlight are
  firmware-only; never substitute PrintScreen or Pause.
- Never log ordinary typed keystrokes, raw event lines, key names, scan values,
  typed content, serials, host addresses, host keys, passwords, private paths,
  desktop IDs/names, or window captions in code logs, prompts, reports, or META.
- Suspend goes through logind/systemd policy, never `/sys/power/state`.
  Display-off must not alter KScreen topology.
- input-remapper is not inspected or reconfigured.
- Licensing is unresolved (root `LICENSE` is MIT but the COOPERATOR has not
  selected the license; gate G6). Never copy external code before an explicit
  compatible decision.

## M4 scope and explicit boundary

M4 delivers the KDE Plasma workspace session manager:

1. Configure and manage virtual desktops (count, names, custom sessions).
2. Assign specific applications to specific virtual desktops.
3. Automatically launch assigned applications on desktop initialization and
   maximize them to their respective virtual desktops.
4. Window-title-based matching as an opt-in fallback when an unassigned window
   has focus.

M4 explicitly does **not** deliver: M5 autostart/system integration at Plasma
login, general input remapping, the Super-key deck layer, per-app
consume-and-inject remapping, broker ARM/grab/pass-through, M3 physical
acceptance, production packaging, or whole G4. M4 must not become autostart.
The plan must state where the M4 → M5 boundary is and why each item falls on
one side.

## Current source facts to reconcile

Verify these from the exact candidate rather than trusting this summary:

- `src/context/WorkspaceReceiver.{h,cpp}` already subscribes to
  `org.kde.KWin` `/VirtualDesktopManager`, handles `currentChanged`,
  `countChanged`, `desktopCreated`, `desktopRemoved`, `desktopDataChanged`, and
  the `current`/`desktops` properties. M3 introduced explicit per-request
  ownership with focused regressions. M4 must reuse this seam rather than
  duplicate it.
- `src/core/Types.h` currently fixes schema version 3 (`kSchemaVersion`), with
  five zone `ZoneValue` slots and M3 zone roles. `src/core/Persistence.{h,cpp}`
  serializes schema 3 with preserving schema-1/2 migration, atomic save, and a
  bounded backup. `src/core/Resolver.{h,cpp}` resolves override → matched app →
  global.
- The existing typed profile/matcher model is the semantic owner for
  application matching. M4 desktop assignment must reuse it, not invent a
  second matcher.
- `src/app/SessionApplication.{h,cpp}`, `src/app/AppController.{h,cpp}`,
  `src/app/SettingsHost.{h,cpp}`, and `src/app/TrayController.{h,cpp}` own the
  session-app lifecycle, OpenRGB client, UI hosting, and broker client.
- `kwin/contextdeck-bridge/contents/code/main.js` already tracks
  `workspace.windowList()`, `windowActivated`, `windowAdded`, `windowRemoved`,
  resolves identity through `transientFor`, and sends
  `ContextReport`/`InventoryReport`/`Heartbeat`; it never sends captions.
- `CMakeLists.txt` owns the registered CTest suite (currently 17 tests: 14 C++
  plus `test_udev_verify`, `test_trial_cutoff`, `test_sleep_hook`). There is no
  lint config and no CI.
- Predecessor read-only reconnaissance found the reference host
  `kwinrulesrc` almost empty, `systemd-run` (systemd 261) present, `KF6Service`
  and `KF6WindowSystem` CMake configs present, `gio` and `kstart` present,
  `kioclient6` absent, no `extra-cmake-modules` and no KF6 umbrella config.
  Re-verify anything the plan depends on; mark unverifiable items as
  inferred/unknown.
- M2/M3 documentation drift exists in `README.md`/`ROADMAP.md`; the park
  wording above and the accepted reports outrank it.

## Single measurable planning outcome

Produce one decision-complete, source-grounded plan for a single later
implementation Worker to build a bounded M4 vertical slice, with an exact
observation-first implementation sequence and a separately authorized later
mutation boundary. The plan must resolve all of the following:

1. **Scope and M5 split.** Exact statement of what M4 implements (desktop
   configuration, assignment, in-session launch-on-desktop-event, maximize,
   opt-in title fallback) and the explicit boundary against M5/G8 autostart.
2. **Observation vs mutation separation.** Define the first read-only slice
   (observation, config read, assignment data model, dry-run/preview) and the
   later mutation slice(s). For every mutation class — `createDesktop`,
   `removeDesktop`, `setDesktopName`, `rows`/wrapping, and `kwinrulesrc` write —
   name the exact D-Bus/file operation, idempotence, ordering, failure handling,
   preconditions, revert/checkpoint, and recovery. No mutation is authorized
   now.
3. **Desktop management design.** Exact `VirtualDesktopManager` surface and
   semantics: `current` is a desktop UUID (not an index); `desktops` is
   `a(iss)`; `createDesktop(uint position, QString name)`,
   `removeDesktop(QString id)`, `setDesktopName(QString id, QString name)`;
   read/write `rows` and `navigationWrappingAround`. Define how custom
   "sessions" (desktop count/names per named setup) are modeled and how the
   manager avoids fighting the user's own desktop changes.
4. **Assignment schema.** Decide whether application-to-desktop assignment is a
   new schema field (schema 4?) or derived from the existing typed
   profile/matcher model. Provide representative JSON for global and
   per-application settings, enumerate allowed fields, enums, bounds, and
   unknown-field behavior, and specify preserving migration from schema 1–3
   with no silent lighting/behavior change. Reuse the existing matcher as the
   single semantic owner.
5. **Launch lifecycle.** Typed launch only: exact desktop-file/KService id,
   never shell. Decide between systemd user transient scopes
   (`systemd-run --user`, clean cgroups/lifecycle) and XDG/KService launcher,
   with rationale. Define duplicate-running detection, failure/retry behavior,
   debounce, reversibility, and explicit non-autostart posture. State exactly
   which in-session desktop/session-management events trigger a launch.
6. **Placement and maximization.** Decide between KWin Scripting
   (`window.desktops = [desktop]`, `window.maximized`) and persistent KDE
   Window Rules (`kwinrulesrc`), or a documented combination. Define how
   placement is enforced event-driven without polling, and how it interacts
   with the existing bridge and `windowActivated`/`windowAdded`.
7. **Title fallback.** Opt-in, event-driven, never polling. Define exactly what
   is compared (e.g. a user-authored pattern against a resource/class or an
   ephemeral in-memory title match), what is stored (nothing sensitive), what
   is surfaced, and the hard rule that captions/titles are never logged or
   persisted. Integrate with the existing identity matcher as fallback only.
8. **Minimal UI/controller slice.** Name the minimum truthful controls needed
   for M4 functionality (desktop configuration, assignment, opt-in fallback
   toggle, truthful state), explicitly not a UI/UX redesign, and state how
   accepted M1/M3 semantics stay unchanged.
9. **Tests and validation.** Name exact focused tests for assignment
   persistence/migration, assignment resolution, launch-lifecycle decisions
   through a testable seam, event-driven placement/maximization, desktop
   management dry-run/idempotence, and title-fallback opt-in/privacy. State
   whether each needs a new causal regression and why. State whether the
   registered CTest suite is the broad gate and why. Name the rollback/recovery
   checkpoints.
10. **Later IRL acceptance.** Provide a short, numbered, safe COOPERATOR
    checklist: mutate a desktop configuration with a revert/checkpoint, observe
    assignment, launch-on-desktop-event, maximize-to-desktop, and opt-in title
    fallback. Explicitly no raw input, no broker start/ARM/grab, no udev, no
    suspend, no autostart, no input-remapper touch.
11. **One implementation slice.** Ordered implementation sequence, exact
    candidate changed-path allowlist selected from the ceiling below,
    validation commands, one-commit publication boundary, rollback/recovery,
    and separate fresh acceptance boundary.
12. **Claim matrix.** State what implementation-PASS could establish, what a
    later fresh code acceptance could establish, what only COOPERATOR IRL
    execution can establish, and the explicit non-claims (M3 physical, M2/G4,
    G3, M5, autostart, remap, deck, per-key, production).

If one material design choice cannot be resolved from repository evidence,
return `PARTIAL` with exactly that choice and a recommended default. Do not
expand into another planning cycle by default.

## Ceiling for any later implementation changed-path allowlist

This planning prompt grants no edits. The plan must return a minimal exact
subset of this ceiling for a later separately authorized implementation:

- `CMakeLists.txt`
- `src/core/Types.h`
- `src/core/Persistence.h`
- `src/core/Persistence.cpp`
- `src/core/Resolver.h`
- `src/core/Resolver.cpp`
- `src/context/WorkspaceReceiver.h`
- `src/context/WorkspaceReceiver.cpp`
- a new `src/workspace/` component set (new only if clearly justified)
- `src/app/SessionApplication.h`
- `src/app/SessionApplication.cpp`
- `src/app/AppController.h`
- `src/app/AppController.cpp`
- `src/app/SettingsHost.h`
- `src/app/SettingsHost.cpp`
- `kwin/contextdeck-bridge/contents/code/main.js` (only if placement requires it)
- existing `ui/` QML pages and new minimal QML (only as needed)
- `tests/unit/` focused tests (existing or new)
- `docs/specification.md`
- `docs/architecture.md`
- new `docs/adr/` records for host-mutation authority, assignment schema, and
  launching
- `docs/operations.md`
- new `docs/testing-m4.md`
- `README.md`
- `ROADMAP.md`

Do not include or propose changes to `.ap/`, `src/broker/`, broker IPC,
`packaging/`, M1/M2/M3 testing files, license files, unrelated tests/UI,
generated files, dependencies, lockfiles, or host configuration. If the plan
proves one additional path essential, report `PARTIAL` and name it; do not
silently widen the ceiling.

## Read-only inspection allowlist

Read the pinned AP Worker minimum spine and, at minimum:

- `.ap/AP.md` — Semantic Authority, RF-03/RF-06/RF-12/RF-16/RF-18/RF-19,
  planning/Plan-to-Execution, Worker responsibilities, stopping conditions;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md` — Worker report header, Planning Record, Worker
  Session Target, exchange/trace contract, validation ladder, delivery record,
  Session-and-Mode, Plan-to-Execution;
- `AGENTS.md`;
- `README.md`;
- `ROADMAP.md`, especially the M3/M4/M5 sections and the backlog entries;
- `docs/architecture.md`;
- `docs/specification.md`;
- `docs/operations.md`;
- `docs/testing.md`;
- `docs/testing-m2.md` only to preserve the no-M2 boundary;
- `docs/testing-m3.md` only to preserve the deferred-M3 boundary;
- `docs/adr/` current decisions;
- `docs/hardware/` evidence relevant to the five-zone/control invariants;
- all current source/test/QML files named in the source-facts and ceiling
  sections;
- the M4 `00_notes.md` and `00_handout.md`, the M3 acceptance report, and the
  M2 park report headers needed to verify continuity.

Bounded read-only host reconnaissance is allowed only when the execution
environment actually exposes a running KDE Plasma session, and only as
non-mutating observation: D-Bus introspection and property reads of
`org.kde.KWin` `/VirtualDesktopManager`, and structural inspection of
`kwinrulesrc`. Never invoke `createDesktop`, `removeDesktop`, `setDesktopName`,
or any state-changing method; never write the configuration; never log or
persist desktop names, captions, or window titles. If the live session is not
available, mark those facts inferred/unknown and rely on repository and
documentary evidence.

Do not inspect device nodes, private configuration values, logs, home paths,
other repositories, credentials, or unrelated host state.

## Authority and side-effect boundary

Product source mutation: prohibited
Product Git mutation: prohibited
Product commit/push: prohibited
AP mutation/update: prohibited
Host mutation: prohibited
Desktop create/remove/rename: prohibited
`kwinrulesrc` write: prohibited
Application launching: prohibited
Host service operation: prohibited
Broker start/stop/ARM/grab/probe: prohibited
Input-remapper operation: prohibited
OpenRGB/KWin installation or runtime operation: prohibited
Physical-device probing or physical acceptance: prohibited
Dependency installation/update: prohibited
Secrets/credentials/private data: prohibited
Network authority: direct public `git ls-remote` identity checks against the
two canonical HTTPS remotes only; no alternate mirror and no external research
Side effects: read-only inspection plus the exact META trace-file preparation
below only

No raw input, raw event lines, key names, scan values, typed content, serials,
host addresses, host keys, passwords, private paths, desktop names/IDs, window
captions, or unredacted tool logs may appear in the prompt/report/trace. Use
only semantic state and public repository-relative paths.

No recovery route is required because this exchange must not start, open,
probe, or grab a device. If any step would cross that boundary, stop. For a
future live-grab whole, one independently demonstrated route is enough: SSH
from another device or a second physical keyboard, not both.

## Validation ladder

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: inspect current persistence, resolver, workspace
receiver, session-app/controller, and bridge coverage; do not execute tests in
this planning exchange unless they are already available without creating build
state
Affected tests: propose exact M4 assignment/launch/placement/title-fallback
tests in the terminal plan
New causal regression: required in the later implementation for assignment
persistence/migration, assignment resolution, launch-lifecycle decisions, and
title-fallback opt-in/privacy because those behaviors do not exist in the
candidate
Broad or full suite: required-because schema/core resolver and session-app
changes can regress the existing registered M1/M2/M3 CTest surface
Runtime or testbed: not-used in this planning exchange
Independent acceptance: required-separate-fresh-worker after implementation

The planning result is non-implementation evidence. It does not accept code or
physical behavior.

## Trace persistence contract

External trace disposition: configured
Trace discovery: META README and the exact M4 destination below
Trace project key: contextdesk
Trace logical-whole projection identity: 04-g213-contextdeck-workspace-session-manager
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_planning_00.md
Destination path: projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/
Report filename: 01_report_00.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

The ORCHESTRATOR persists this exact prompt bytes to
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/01_planning_00.md`
before delivery. The WORKER may write only the report file at
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/01_report_00.md`.

Before substantive planning, verify the already-persisted prompt file exists
and is byte-identical to the received prompt; read it back completely. Stop on
a non-identical or unsafe collision. Do not alter `00_notes.md` or
`00_handout.md`, create a handout, or write any other META path.

After planning, write the complete terminal report first to the report path,
read it back completely, and verify the header, coordinates, content, and
filename. Do not overwrite a non-identical existing report. Do not stage,
commit, push, pull, merge, rebase, or otherwise mutate META Git history or
refs. The COOPERATOR archives the exact prompt/report pair together in one
first-add commit only after the report exists.

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

It must echo the opening persistent-role and three coordinate fields exactly
once, with their values unchanged.

Include:

- status: `PASS`, `PARTIAL`, or `BLOCKED`;
- phase-qualified result: `not-applicable` (planning is not implementation);
- start and end product commit (expected unchanged exact candidate);
- verified product/AP/META identities and clean-state result;
- source-grounded current-state findings;
- the complete decision-ready plan covering all twelve measurable-outcome items;
- the exact minimal later implementation changed-path allowlist;
- the E3 implementation/acceptance evidence envelope and validation rationale;
- explicit statement that the plan made no product, AP, host, service,
  desktop-configuration, launch, device, dependency, or Git publication
  mutation;
- trace prompt/report persistence and complete-readback result;
- deviations, risks, unresolved decisions, and missing evidence;
- exactly one smallest next step: ORCHESTRATOR reconciliation and, only if
  accepted, a separate implementation Worker prompt;
- exactly one `Report justification: new-evidence`;
- `Resolved Execution Issues / Near-Misses: none` or a complete entry;
- `Pre-Existing Failure Classification: none` or a complete entry;
- compact critique:

  `Orchestration critique:`

  `MEASURED: none | <verified finding; evidence; effect; smallest correction>`

  `LEAD: none | <unverified possibility; cheapest useful check>`

- exactly one `Logical-whole closure: not-closed` line;
- the exact authority-expiry sentence below.

Explicit non-claims in the report:

- no implementation-PASS, acceptance-PASS, publication-PASS, deployment-PASS,
  production readiness, M2/G4 closure, G3 independent re-audit, autostart,
  hibernate/hybrid sleep, general input-remapper coexistence, M3 closure, M3
  physical five-zone observation, M5 integration, remapping, deck-layer
  behavior, per-key RGB, or physical hardware acceptance;
- no claim that any desktop/session-management behavior is accepted before its
  own later implementation and acceptance;
- no claim that Session 27 was a fresh Worker result.

Authority for this Worker expires at this terminal report.

## Stop conditions

Stop and report `BLOCKED` before substantive planning if the session is not
genuinely fresh, Native Plan Mode is not actually enabled, coordinates or
authority are contradictory, product/AP/META identity fails, the worktree has
unexplained changes, the M2/M3 park records are missing, the M4 trace path
collides or is unsafe, required repository evidence cannot be read, or
completing the plan would require a prohibited mutation, private data,
host/device/desktop access, an additional path outside the ceiling, or
subagents.

Stop with `PARTIAL` if the repository can be analyzed but one material design
choice or required evidence item remains unresolved. Do not implement, touch
the live desktop, or silently widen scope to force PASS.

Stop with `PASS` only when the complete decision-ready plan and exact later
implementation boundary are persisted and read back. Then submit the terminal
report and do no further work under this grant.
