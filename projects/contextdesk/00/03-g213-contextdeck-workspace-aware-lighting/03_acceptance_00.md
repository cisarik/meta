Logical whole identity: g213-contextdeck-workspace-aware-lighting
Worker session ordinal: 03
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Acceptance Worker
Phase: acceptance
Task identity: CONTEXTDECK-M3-WORKSPACE-LIGHTING-CODE-ACCEPTANCE
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to a genuinely fresh independent Worker session
Reasoning recommendation: High
Reasoning basis: independent acceptance must reconcile schema migration, asynchronous D-Bus races, deterministic five-slot composition, UI bindings, and claimed causal evidence
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E3
Internal delegation: prohibited

# ContextDeck M3 — fresh independent code acceptance

You are a genuinely fresh independent WORKER. You did not plan, implement,
repair, or report the candidate and did not participate in M2. You receive only
this complete prompt. Native Plan Mode must be OFF. Do not use subagents.

Perform one read-only independent acceptance of the immutable public M3
implementation candidate. Treat the implementation report as a claim, not as
acceptance evidence. Inspect and test independently, persist one terminal
report, and stop. You have no correction, product publication, host, or device
authority.

## Acceptance and Correction Record

Acceptance candidate: `55e981309718bcb2f94f809468eab9934acf5f51`
Acceptance owner map: accepted M3 plan in `01_report_00.md`, completed by `01_report_01.md`, implemented under `02_implementation_00.md`
Acceptance allowlist: read-only inspection of the exact candidate, the 24 changed product paths, directly referenced unchanged owner paths, pinned AP, and the public M3/M2 continuity records listed below
Acceptance risk claims: schema preservation and save safety; bounded VirtualDesktopManager observation; deterministic five-zone resolution; controller recomputation and transport suppression; minimal usable UI; adequate causal tests; truthful scope and documentation
Acceptance control matrix: A1 through A8 below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1 only if this session passes the independence gate and completes the review
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
`55e981309718bcb2f94f809468eab9934acf5f51`
Required candidate parent:
`ca6052e816d4884ddeac9d7499a42c2aca089e7e`
Earlier required parent of the M2 park commit:
`ab10491c49d0b6574b6953a02935a4664c39d7c2`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

Canonical META: `https://github.com/cisarik/meta.git`
Required public META baseline:
`ee6f8c90414b15a87a8b1617cc561ca542768dcd`
Required implementation-pair parent:
`7452d615387db27595b701680b653fdf0120f0ee`
Required M3 trace:
`projects/contextdesk/00/03-g213-contextdeck-workspace-aware-lighting/`

Required implementation prompt SHA-256:
`427ecd959f8d83968f8044fe5f36f35cfd7004e3cdba55a0f80234c0ea1c61d9`
Required implementation report SHA-256:
`d77a944ec8b36624049234b653e712a29afb797ae5417c439ce1d4a5221a202b`

No alternate commit, mirror, stale remote-tracking ref, or local retained clone
may substitute for these identities. If public `main` has moved, stop before
testing and report the exact discrepancy; do not silently retarget.

## Read-only preflight

Use fresh disposable inspection clones in the Worker container, never a
COOPERATOR checkout. Before substantive acceptance:

1. Verify this is a genuinely fresh session with no implementation ancestry,
   Native Plan Mode OFF, exact 03/01 coordinates, and no subagents.
2. Clone the canonical product with submodules and META over HTTPS. Fetch
   `main`, compare direct `git ls-remote` with the required public tips, and
   detach at the exact required commits.
3. If transport or cache state is stale, discard only the Worker-owned clone
   and retry the canonical HTTPS remote in a new disposable location. A safe
   retry may use `git -c http.version=HTTP/1.1`. Do not change host DNS or Git
   configuration and do not use credentials or a mirror.
4. Verify clean worktrees, candidate parent, candidate subject, exact AP
   gitlink and checkout, and `./.ap/ap doctor` PASS.
5. Verify META ancestry, the implementation-pair commit's exact two changed
   paths, byte identity of the prompt, report hash, complete readback, and no
   changed earlier accepted-plan artifact.
6. Verify the candidate changed exactly the 24 paths listed below and no
   dependency, AP, broker, RGB transport, KWin bridge, packaging, operations,
   hardware-evidence, license, or host file.
7. Verify existing required build tools and `dbus-run-session`. Install
   nothing. Missing tools are a truthful blocker, not permission to mutate the
   environment.

Use detached read-only source inspection. Put all build products outside the
product checkout in a newly created Worker-owned temporary directory. The
product worktree must remain clean throughout. META must be clean at preflight;
after persistence, only the exact owned prompt/report differences are allowed.

## Mandatory reading

Read before deciding:

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-07, RF-12, RF-18, RF-19,
  acceptance/correction, phase-qualified results, and stopping;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Acceptance and Correction
  Record, Phase Result and Closure Record, external trace, and report expiry;
- `.ap/INFOSEC.md` only as advisory defensive review guidance;
- product `AGENTS.md`, `README.md`, `ROADMAP.md`,
  `docs/specification.md`, `docs/architecture.md`, `docs/testing-m3.md`,
  `docs/testing.md`, `docs/testing-m2.md`,
  `docs/hardware/g213-control-matrix.md`, and
  `docs/hardware/g213-zone-map.md`;
- the complete public M3 artifacts `01_planning_00.md`, `01_report_00.md`,
  `01_completion_01.md`, `01_report_01.md`, `02_implementation_00.md`, and
  `02_report_00.md`;
- M2 `00_handout_03.md` and `27_report_00.md` only for the parked boundary;
- the complete candidate diff and every changed product file;
- unchanged adjacent owners needed to judge behavior, limited to
  `src/context/ContextReceiver.{h,cpp}`, `src/context/DBusNames.h`,
  `src/rgb/OpenRgbClient.{h,cpp}`, `src/rgb/OpenRgbProtocol.{h,cpp}`,
  `src/app/main.cpp`, and directly included core headers.

Treat old documentation contradicting named M2 Sessions 22–24 as drift, not
authority to reopen M2.

## Continuity and product invariants

The named live G4 slices are accepted, but the M2 logical whole remains open.
M2 is parked with G3 host-mitigated on the authorized reference host; the next
bounded whole is M3 workspace-aware lighting.

Preserve these limits while reviewing:

- Logitech G213 Prodigy only, USB `046d:c336`.
- Linux/KDE Plasma 6/Wayland, C++20/Qt6/KF6/systemd.
- Exactly five RGB zones through the existing loopback OpenRGB SDK protocol-5
  path; never per-key RGB.
- The session app observes virtual desktops directly and never opens raw input.
- Broker stays static/inactive: no LEASE, ARM, grab, pass-through, capture, or
  automatic ARM.
- Exactly eighteen measured host-remappable controls remain the M2 matrix;
  code `166` is unresolved; Game Mode and Backlight remain firmware-only.
- input-remapper is not inspected or reconfigured.
- No secrets, raw events, key names, scan values, typed content, serials, host
  addresses, host keys, passwords, private paths, desktop IDs/names, or window
  captions may enter the report or META.
- No external G213Tray source or unresolved-license copying.

This acceptance does not cover M2/G4 closure, physical visibility, deployment,
autostart, hibernate/hybrid sleep, M4 session management, remapping, a deck
layer, M5 integration, production packaging, or general coexistence.

## Exact candidate changed paths

The candidate must have only these 24 changed paths:

```text
CMakeLists.txt
README.md
ROADMAP.md
docs/architecture.md
docs/specification.md
docs/testing-m3.md
src/app/AppController.cpp
src/app/AppController.h
src/app/SessionApplication.cpp
src/app/SessionApplication.h
src/context/WorkspaceReceiver.cpp
src/context/WorkspaceReceiver.h
src/core/Persistence.cpp
src/core/Resolver.cpp
src/core/Resolver.h
src/core/Types.h
tests/unit/test_profile_persistence.cpp
tests/unit/test_profile_resolver.cpp
tests/unit/test_workspace_lighting.cpp
tests/unit/test_workspace_receiver.cpp
ui/ColorsPage.qml
ui/DiagnosticsPage.qml
ui/LightingPresetEditor.qml
ui/OverviewPage.qml
```

This is an inspection scope, not mutation authority. Any product change,
generated file inside the checkout, commit, branch/ref operation, or push is
forbidden.

## Measurable outcome and acceptance matrix

Return one independent verdict on whether the exact public candidate satisfies
the accepted M3 code contract and is fit to proceed to a separate
COOPERATOR-owned physical five-zone checklist.

Mark every row `PASS`, `FAIL`, or `NOT TESTED`, with direct evidence:

### A1 — Identity, provenance, and scope

- exact product/AP/META public identities and ancestry;
- implementation pair byte/hash integrity;
- exact 24 changed paths and clean read-only checkouts;
- no scope escape or hidden dependency/host change.

### A2 — Schema 3 and preserving migration

- only `Static`, `DesktopIndicator`, `AppColor`, and `Off` roles;
- schema-3 zones absent/null or exactly five strict role objects;
- dynamic roles rejected in application presets;
- schemas 1 and 2 preserve their required behavior in memory;
- schema-2 five-color arrays become five Static slots without read-time
  rewrite or workspace activation;
- future/unknown fields, wrong types/counts, invalid colors/numerics, and
  incompatible fields fail closed;
- explicit save is the schema-3 persistence boundary.

### A3 — Save and backup safety

- full draft validation and 1 MiB bound;
- no-direct-fallback `QSaveFile` for backup and primary;
- backup success precedes primary replacement;
- previous bytes are preserved on causal backup/write failure;
- invalid, unsupported, and schema-1 migration-fallback source bytes are not
  overwritten;
- documentation does not claim impossible two-file atomicity.

### A4 — Pure five-slot resolution

- session override precedence and unchanged ordinary app/global resolution;
- desktop slots map the first K sorted desktops, current at 100%, inactive at
  `floor(channel/5)`, absent black, explicit overflow, and no wrap/page;
- app slots implement every accepted preset/fallback branch, including Direct
  base/zones, Breathing, Off, Untouched, Wave, Cycle, matched and unmatched;
- unknown workspace releases to `untouched`; bridge loss retains valid desktop
  state; all-black workspace resolves to device Off;
- exactly five concrete colors and protocol-5 packet ordering remain correct.

### A5 — VirtualDesktopManager receiver

- exact service/object/interface and subscribe-before-snapshot ordering;
- complete `GetAll` snapshots; signals only invalidate and refresh;
- count 1–32, count/list equality, bounded unique IDs/names/positions,
  16 KiB aggregate metadata, current exactly once, position sort, signed and
  unsigned 32-bit compatibility after bounds;
- owner generation and invalidation revision reject stale replies;
- one logical request in flight plus one pending refresh, a non-extendable 2 s
  deadline, duplicate suppression, and 1/2/4/8/16/30 s bounded recovery;
- service loss/replacement and pause/resume recover without healthy polling;
- logs expose only bounded error classes, not desktop identity.

### A6 — Controller, session app, and UI

- `SessionApplication` owns an independent named session-bus receiver;
- bursts coalesce, refresh defers workspace output, session overrides remain
  responsive, and equal effective output does not resubmit RGB state;
- application/desktop simultaneous changes use latest inputs and bridge-loss
  duplicate notifications are coalesced;
- configuration-root test seam does not change production default behavior;
- QML property/method signatures are valid and compile;
- default 4+1, per-slot roles, static conversion, gradient role replacement,
  desired-preview labeling, overflow/unavailable summary, and non-persistent
  simulated pause/resume are wired truthfully;
- no navigation redesign or broker activation.

### A7 — Causal regression evidence

- inspect test bodies, not names or aggregate pass counts;
- map every required behavior from A2–A6 to a persistent causal regression;
- confirm receiver tests use a fake service on a private `dbus-run-session`
  bus and controller tests use temporary configuration plus a non-started RGB
  client;
- missing persistent coverage required by the implementation prompt is an
  acceptance defect even if the current build is green;
- focused and complete registered CTest suites pass from the detached public
  candidate in the fresh external build directory.

### A8 — Documentation and bounded claims

- schema, migration, receiver, resolver, failure behavior, limitations, and
  later IRL checklist match code;
- candidate is described only as an implementation candidate;
- M2 remains parked with named accepted slices and the independent G3 gap;
- no physical, deployment, production, M4/M5, per-key, autostart, hibernate,
  general-coexistence, or whole-G4 claim.

Acceptance-PASS requires all A1–A8 rows PASS. `NOT TESTED` on a required row,
a confirmed contract defect, inadequate required persistent regression, or an
unresolved material discrepancy prohibits acceptance-PASS.

## Two mandatory adversarial leads

These are unverified leads from ORCHESTRATOR static inspection, not findings.
Independently confirm or disprove each; do not defer them silently.

### Lead L1 — stale watcher versus newer in-flight request

Trace deadline, owner replacement, pause/resume, and late-reply interleavings in
`WorkspaceReceiver`. Determine whether an older `QDBusPendingCallWatcher` can
execute `onSnapshotReply`, set the shared `m_inFlight` false, and trigger or
admit another request while a newer-generation request is still outstanding.
Also inspect whether timeout makes the old transport call merely logically
stale rather than cancelled. Require evidence that the one-in-flight invariant
holds across this exact interleaving.

### Lead L2 — claimed versus persistent causal coverage

Map the implementation prompt's required cases to actual assertions. Pay
special attention to the full app-slot fallback table; schema-3 wrong types,
invalid colors and numeric bounds; count mismatch, position/metadata bounds,
removal, retry-budget exhaustion; metadata-only transport suppression; and
deadline/owner-replacement late-reply overlap. Aggregate 5/5 and 17/17 results
alone do not resolve this lead.

For each lead report: `confirmed`, `disproved`, or `unresolved`, the exact code
and test evidence, behavioral consequence, and whether it blocks acceptance.

## Allowed validation

Use only existing tools. Run from the exact detached candidate with the build
directory outside the checkout:

```sh
env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH cmake -S . -B <owned-temp>/build -G Ninja
env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH cmake --build <owned-temp>/build

env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH \
  ctest --test-dir <owned-temp>/build --output-on-failure \
  -R '^(test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_lighting|test_openrgb_protocol)$'

env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH \
  ctest --test-dir <owned-temp>/build --output-on-failure

git diff --check ca6052e816d4884ddeac9d7499a42c2aca089e7e..55e981309718bcb2f94f809468eab9934acf5f51
git status --short
```

Record real counts and the first causal failure. Do not weaken, skip, or loop
tests to manufacture green output.

If L1 cannot be settled statically and the existing toolchain suffices, you may
create one minimal synthetic test only in a separate Worker-owned disposable
copy outside the canonical product checkout. It may use only the candidate's
existing dependencies, fake private D-Bus service, synthetic data, and no
network other than public Git verification. It must not become a product or
META diff, and the owned temporary copy/build must be deleted after evidence is
captured. Report the probe design, result, and cleanup without exposing a
private absolute path. This temporary probe does not replace a missing durable
regression test required in the product.

## Forbidden actions

- no product or AP edits, patches, staging, commit, push, branch switch, reset,
  clean, stash, rebase, merge, ref/tag/remote/config change, or force operation;
- no META history/ref mutation and no edits outside the exact prompt/report
  trace paths;
- no package installation, sudo, service management, udev, input-remapper,
  OpenRGB process, broker start/connect/ARM, KWin session-bus probe, power
  action, device open/probe/grab, or host configuration;
- no real display/session application launch if it could contact real KWin,
  OpenRGB, broker, or hardware;
- no secrets, credentials, host identifiers, or private paths in the report;
- no implementation, correction, speculative redesign, M2 reopening, physical
  acceptance, deployment, or closure.

No recovery route is needed because no live input or physical device operation
is authorized. Stop if any proposed validation would require one.

## Verdict rules

Use:

- `status: PASS` and `Phase-qualified result: acceptance-PASS` only when the
  independence gate, A1–A8, both leads, focused tests, full suite, cleanliness,
  and public identity all pass with no blocking defect or missing evidence;
- `status: PARTIAL` and `Phase-qualified result: not-applicable` when the
  independent review completes but finds or leaves unresolved a candidate
  defect or required-evidence gap; identify the smallest correction boundary,
  but do not implement it;
- `status: BLOCKED` and `Phase-qualified result: not-applicable` when a
  prerequisite prevents a meaningful independent decision before evidence can
  be gathered.

A completed negative verdict is useful evidence but is not acceptance-PASS.
Do not reclassify candidate failure as a Worker execution failure.

## Exact META trace persistence

External trace disposition: configured
Trace discovery: META README and exact M3 trace
Trace project key: contextdesk
Trace logical-whole projection identity: 03-g213-contextdeck-workspace-aware-lighting
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Downloadable prompt filename: `03_acceptance_00.md`
Destination:
`projects/contextdesk/00/03-g213-contextdeck-workspace-aware-lighting/03_acceptance_00.md`
Report filename: `03_report_00.md`
Report destination:
`projects/contextdesk/00/03-g213-contextdeck-workspace-aware-lighting/03_report_00.md`
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: WORKER
Report persistence owner: WORKER
META Git publication owner: COOPERATOR
Archival: wait-for-report

Before substantive validation, persist the exact received prompt bytes to its
destination and read them back completely. Require absence or exact byte
identity; never overwrite differing content. At the end, write and completely
read back the terminal report. The WORKER may prepare only these exact two META
files and may not stage, commit, push, pull, merge, rebase, switch, or alter
META history. The COOPERATOR archives the exact pair together afterward.

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo the opening persistent-role and three coordinate fields exactly once with
unchanged values. Include:

- status and phase-qualified result under the verdict rules;
- exactly one `Report justification: final-acceptance`;
- fresh-session independence evidence and `Primary fresh acceptances used`;
- product start/candidate/parent, AP pin/doctor, META identity, direct public
  refs, ancestry, changed paths, prompt/report hashes, and clean states;
- an A1–A8 matrix with `PASS`, `FAIL`, or `NOT TESTED`, evidence, and blocking
  classification;
- L1 and L2 as `confirmed`, `disproved`, or `unresolved`, with direct evidence
  and consequence;
- focused/full validation commands, exit results, actual test counts, private
  bus classification, and any first causal failure;
- temporary-probe identity, design, result, and cleanup, or `not-used`;
- confirmed defects, missing persistent tests, disproved concerns, residual
  risks, deviations, and out-of-scope ledger candidates;
- `Resolved Execution Issues / Near-Misses` and
  `Pre-Existing Failure Classification`, each truthfully populated or `none`;
- exact META prompt/report persistence and complete-readback evidence, while
  stating that META Git publication remains COOPERATOR-owned;
- one smallest next step: ORCHESTRATOR reconciliation; if non-PASS, name one
  bounded correction slice without granting it; if PASS, name only the later
  COOPERATOR-owned physical M3 checklist as not yet authorized;
- compact `Orchestration critique` with `MEASURED:` and `LEAD:`;
- exactly one `Logical-whole closure: not-closed` line;
- the exact authority-expiry sentence below.

Explicitly state that code acceptance is not physical acceptance and does not
prove M2/G4 closure, deployment, production readiness, G3 re-audit, autostart,
hibernate/hybrid sleep, general input-remapper coexistence, M4/M5 behavior,
per-key RGB, or measured control-to-zone placement.

Authority for this Worker expires at this terminal report.

## Fail-closed stop conditions

Stop before substantive review on non-fresh or inherited implementation
context, Native Plan Mode mismatch, coordinate/authority contradiction,
identity/public-ref/ancestry/hash failure, dirty or unsafe checkout, prompt
collision, missing accepted plan, required tool absence, or need for product,
host, device, secret, or subagent authority.

During review, preserve the first causal failure. Continue read-only inspection
only when safe and useful to bound the verdict; never correct the candidate or
expand the task. A confirmed blocking defect or required-evidence gap yields a
truthful `PARTIAL`, not an improvised patch.

Stop immediately after the terminal report. Do not implement a correction,
start the physical checklist, deploy, reopen M2, or begin another M3 phase.
