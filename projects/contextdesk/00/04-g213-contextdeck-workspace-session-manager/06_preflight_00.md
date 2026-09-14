Logical whole identity: g213-contextdeck-workspace-session-manager
Worker session ordinal: 06
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Worker-Executed Preflight
Phase: Preflight
Task identity: CONTEXTDECK-M4-SLICE-B-PREFLIGHT
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to a genuinely fresh Worker session
Reasoning recommendation: High
Reasoning basis: read-only preparation for a later host-mutating, app-launching
slice on a live KDE Plasma session; the review must establish exact proposed
mutation, prerequisites, checkpoint, recovery, and stop rules
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: read-only verification of live/installed state and a
proposed host-mutation boundary; it makes no acceptance claim and grants no
implementation authority
Internal delegation: prohibited

# ContextDeck M4 Slice B — read-only preflight

You are a genuinely fresh WORKER. You did not plan, implement, accept, or repair
any part of M4 and did not participate in M1/M2/M3. Native Plan Mode must be
OFF. Do not use subagents.

Perform one bounded, strictly read-only preflight for the later M4 Slice B
(mutation/launch/placement) implementation. Your job is to verify current state,
prerequisites, the exact proposed mutation boundary, checkpoint/backup, recovery,
stop rules, and the acceptance plan, then return one readiness verdict. A `PASS`
only **recommends** a separately authorized implementation slice; it never
authorizes it, and this exchange mutates nothing.

## Acceptance and Correction Record (context only)

This is a preflight, not an acceptance. The accepted M4 plan is
`01_report_00.md` (completed by `01_report_01.md`). Slice A is code-accepted on
public candidate `aca6c68…` via `05_report_00.md`. Slice B is the mutation slice
described by the accepted plan; this preflight does not re-plan it and does not
accept anything.

## Immutable public identities

Canonical product: `https://github.com/cisarik/contextdesk`
Required public branch: `main`
Required public product `main`:
`aca6c68542bbc9f1b8ee891415a04b0a95e8372e`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

Canonical META: `https://github.com/cisarik/meta.git`
Required public META baseline:
`977c841cd18e1e733ab752d7e64f068d9079d812`
Required M4 trace:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/`

A later verified META descendant is acceptable after ancestry and changed-path
review proves no M4 artifact changed. Do not retarget product.

## Read-only authority and boundaries

Read-only inspection only. This exchange must not:

- mutate the desktop configuration: no `createDesktop`, `removeDesktop`,
  `setDesktopName`, no `rows`/`navigationWrappingAround`/`current` write;
- write `kwinrulesrc` or any KWin/Plasma configuration;
- launch any application or start any service;
- start the session application, the broker, OpenRGB, or a KWin script;
- open, probe, or grab any device, or touch the broker/ARM path;
- install, upgrade, or change any package, dependency, lockfile, or toolchain;
- mutate the product, AP, or META Git history, or write any META path other than
  the report named below.

Allowed: read-only filesystem inspection of installed KWin/Qt/KF6 headers and
CMake config files; read-only D-Bus introspection and property **reads** of
`org.kde.KWin` `/VirtualDesktopManager`; read-only inspection of `kwinrulesrc`
structure; read-only Git and build-tool presence checks; running no test or
build unless it is already configured and creates no new state.

If the execution environment does not expose a live KDE Plasma/Wayland session,
mark live host facts `inferred` or `unknown`, rely on repository and installed
header/CMake evidence, and state the limitation. Do not fabricate host state.

Never put desktop names, desktop UUIDs, window captions, serials, host addresses,
host keys, passwords, private paths, or unredacted logs into the report or META.
Report only semantic state, counts, capability classes, and boolean readiness.

## Mandatory reading

- `.ap/AP.md`: Preflight and phase-specific gates, RF-02, RF-06, RF-12, RF-18,
  RF-19, task authority, security boundaries (owner operations), stopping;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, exchange/trace, delivery
  record, Separate Read-Only Preflight expectations;
- `AGENTS.md`;
- the accepted M4 plan `01_report_00.md`, completion `01_report_01.md`,
  Slice A implementation `02_implementation_00.md`/`02_report_00.md`, acceptance
  `05_report_00.md`, and ADRs 0002/0003/0004;
- `docs/specification.md`, `docs/architecture.md`, `docs/operations.md`,
  `docs/testing-m4.md`;
- `src/workspace/WorkspacePlan.{h,cpp}`, `src/context/WorkspaceReceiver.{h,cpp}`,
  `src/core/Types.h`, `src/core/Persistence.h`,
  `src/app/AppController.{h,cpp}`;
- `kwin/contextdeck-bridge/contents/code/main.js` and `metadata.json`;
- `CMakeLists.txt` and `src/` owner files relevant to a Slice B change.

## Read-only questions to answer

Answer each with direct evidence, an evidence class (`directly observed`,
`inferred`, or `unknown`), and a readiness implication:

1. **Product/AP/repo state.** Is public product `main` exactly `aca6c68…`, the
   worktree clean, the AP pin `0cf2cff…` equal with `ap doctor` PASS/stable?
2. **KWin D-Bus surface.** Does the live session (if present) expose
   `org.kde.KWin` `/VirtualDesktopManager` with properties `count`, `current`,
   `rows`, `navigationWrappingAround`, `desktops`, methods `createDesktop`,
   `setDesktopName`, `removeDesktop`, and signals `rowsChanged`,
   `navigationWrappingAroundChanged`, `desktopCreated`, `desktopRemoved`? Report
   names/counts, never desktop UUIDs/names.
3. **KWin scripting API.** From the installed KWin headers/docs, confirm whether
   `window.desktops` is writable and whether maximization must use
   `setMaximize(bool,bool)` rather than a writable `window.maximized` (the plan
   asserted this). Cite the exact installed header path generically.
4. **Launch capability.** Are the `KF6::Service` and `KF6::KIOGui` CMake config
   packages present (exact `find_package` component names and any target names a
   Slice B build would need)? Is `KIO::ApplicationLauncherJob` available? Which
   exact new build dependency would Slice B add?
5. **Exact proposed mutation boundary.** Restate, from the accepted plan, the
   exact Slice B operations and classify each by reversibility: trailing
   `createDesktop`; conditional `setDesktopName`; `rows`/wrapping set;
   `current` set (optional); explicit `removeDesktop`; typed application launch;
   bridge placement/maximize. Identify which are irreversible-ish and must be
   excluded from default Apply or need separate authority.
6. **Checkpoint/backup.** Is the planned checkpoint (`workspace-checkpoint.json`
   in a user-local path, not the profile document, never META) sufficient and
   safe? How would revert rebind assignments after a `removeDesktop` that mints
   new UUIDs? State the exact gap, if any.
7. **Recovery and stop rules.** What is the concrete abort/revert path if a
   mutation sequence partially fails? What preconditions must hold before the
   first mutation? What makes the slice fail closed?
8. **Acceptance plan.** Confirm the route: Slice B code is followed by a fresh
   independent code acceptance and then a bounded, separate COOPERATOR-owned IRL
   run (explicit Apply; desktop create/rename + revert; launch-on-apply;
   maximize/placement; opt-in title fallback). Confirm live desktop mutation and
   launch are COOPERATOR-owned host operations and are **not** part of this
   preflight or of Slice B code execution.
9. **Privacy/capability.** Confirm that the Slice B design can run without
   logging captions/desktop names/UUIDs, and that the earlier acceptance's
   ledger residual (a future live caption producer) has a planned privacy guard
   when that producer is introduced.
10. **Required capability.** What exact capability/authority would the later
    Slice B implementation grant need (build dependency authority; no host
    mutation at build time), and what would the separate IRL run need (explicit
    mutation-class authority, a named checkpoint, one demonstrated recovery
    route not related to input grabbing)?

## Single preflight outcome

Return one of:

- `PASS`: evidence is sufficient and prerequisites are present; a separately
  authorized Slice B implementation slice may be recommended. State the exact
  verified state, the approved-if-authorized mutation boundary, checkpoint,
  rollback, step ordering, stop conditions, acceptance plan, and required
  capability.
- `PARTIAL`: a material prerequisite, risk, rollback detail, or evidence item
  remains unresolved. Name the smallest missing evidence or decision.
- `BLOCKED`: implementation must not be authorized yet. Name the causal blocker.

A `PASS` does not authorize implementation, does not accept anything, and does
not close M4.

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
Downloadable prompt filename: 06_preflight_00.md
Destination path: projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/
Report filename: 06_report_00.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

The ORCHESTRATOR persists this exact prompt bytes to
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/06_preflight_00.md`
before delivery. The WORKER may write only the report file at
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/06_report_00.md`.
Verify the persisted prompt is byte-identical to the received prompt and read it
back completely. Do not alter earlier M4 pairs or `00_notes.md`. Write and
completely read back the terminal report. Do not mutate META Git; the COOPERATOR
owns first-add archival.

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo the opening persistent-role and three coordinate fields exactly once with
values unchanged, and include:

- status `PASS`, `PARTIAL`, or `BLOCKED`; preflight phase result
  (`not-applicable` for a preflight; no implementation/acceptance result);
- exactly one `Report justification: new-evidence`;
- product/AP/META identities, direct public refs, and clean-state evidence;
- for each of the ten questions: the direct evidence, evidence class, and
  readiness implication;
- the exact proposed mutation boundary with reversibility classification and any
  exclusion recommendation;
- checkpoint, recovery, stop rules, and acceptance-plan confirmation;
- required capability for the later implementation and the separate IRL run;
- explicit statement that this exchange mutated nothing (no desktop, launch,
  `kwinrulesrc`, service, device, dependency, product, AP, or META Git change);
- deviations, risks, missing evidence, and ledger candidates;
- exactly one smallest next step: ORCHESTRATOR reconciliation and a COOPERATOR
  decision on whether to authorize a Slice B implementation grant;
- compact `Orchestration critique` with `MEASURED:` and `LEAD:`;
- exactly one `Logical-whole closure: not-closed` line;
- the exact authority-expiry sentence below.

Explicit non-claims: no implementation-PASS, acceptance-PASS, deployment-PASS,
production readiness, physical acceptance, M2/G4 closure, G3 re-audit,
autostart, hibernate/hybrid sleep, general input-remapper coexistence, M3
closure, M3 physical five-zone observation, live desktop/launch/placement
behavior, remapping, deck behavior, M5 integration, per-key RGB, or measured
control-to-zone placement.

Authority for this Worker expires at this terminal report.

## Stop conditions

Stop and report before any further inspection if the task would require a
mutation, a device or broker operation, a package change, a secret, another
META path, or a subagent. Preserve the first causal failure; do not fabricate
host state. Stop after the terminal report; do not begin Slice B, implementation,
or any live mutation.
