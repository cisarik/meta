Logical whole identity: g213-contextdeck-workspace-aware-lighting
Worker session ordinal: 05
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Acceptance Worker
Phase: acceptance
Task identity: CONTEXTDECK-M3-WORKSPACE-LIGHTING-FULL-REACCEPTANCE
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to a genuinely fresh independent Worker session
Reasoning recommendation: High
Reasoning basis: independent re-acceptance must reconcile a corrected asynchronous request-ownership state machine, preserved schema migration, deterministic five-slot composition, UI wiring, and a claimed causal-regression corpus
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E3
Internal delegation: prohibited

# ContextDeck M3 — full fresh independent code re-acceptance after correction

You are a genuinely fresh independent WORKER. You did not plan, implement,
repair, accept, or report any part of this candidate and did not participate in
M2. You receive only this complete prompt. Native Plan Mode must be OFF. Do not
use subagents.

The original M3 implementation candidate `55e9813…` returned an independent
`PARTIAL` in `03_report_00.md` because the `WorkspaceReceiver` one-in-flight
ownership invariant did not hold (A5/L1) and required causal coverage was
incomplete (A7/L2). A bounded corrector then published exactly one direct-child
commit `502ae75…` that changed request ownership semantics and added the missing
regressions. Because the correction changed runtime behavior, AP requires a
**full fresh A1–A8 re-acceptance**, not a scoped re-check. This session is that
re-acceptance.

Perform one read-only independent acceptance of the immutable public corrected
M3 candidate. Treat the implementation, acceptance, and correction reports as
claims, not as acceptance evidence. Inspect and test independently, persist one
terminal report, and stop. You have no correction, product publication, host, or
device authority.

## Acceptance and Correction Record

Acceptance candidate: `502ae75571358ec95d33c836084b5e2253850731`
Acceptance owner map: accepted M3 plan in `01_report_00.md`, completed by `01_report_01.md`; implementation under `02_implementation_00.md`; independent PARTIAL in `03_report_00.md` (A5/L1, A7/L2); bounded correction under `04_correction_00.md`
Acceptance allowlist: read-only inspection of the exact candidate, the cumulative 24 changed product paths between `ca6052e…` and `502ae75…`, directly referenced unchanged owner paths, pinned AP, and the public M3/M2 continuity records named below
Acceptance risk claims: corrected receiver request ownership; preserved schema 3 and schema-1/schema-2 migration; save/backup failure safety; deterministic five-slot resolution and all app-slot fallback branches; controller coalescing and transport suppression; minimal truthful UI; adequate durable causal regressions; truthful scope and documentation
Acceptance control matrix: A1 through A8 below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1 (this session counts as the required full-fresh correction re-acceptance)
Automatic corrections used: 1
Correction re-acceptance: full-fresh
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
`502ae75571358ec95d33c836084b5e2253850731`
Required candidate parent:
`55e981309718bcb2f94f809468eab9934acf5f51`
Required M3 implementation base (parent of parent):
`ca6052e816d4884ddeac9d7499a42c2aca089e7e`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

Canonical META: `https://github.com/cisarik/meta.git`
Required public META baseline:
`aa1c77a91165dca6c443d54604b579324427c71e`
Required M3 trace:
`projects/contextdesk/00/03-g213-contextdeck-workspace-aware-lighting/`

Required M3 trace commit/path map (prompt/report pair commits):

```text
34bf6dde9df69feea5a980b5e397942cf832381b  01_planning_00.md + 01_report_00.md
7452d615387db27595b701680b653fdf0120f0ee  01_completion_01.md + 01_report_01.md
ee6f8c90414b15a87a8b1617cc561ca542768dcd  02_implementation_00.md + 02_report_00.md
9e7fd1832122e89b96cda231827b4ea726febfe0  03_acceptance_00.md + 03_report_00.md
d6b067aeabedd777d3dc8b65d6a384767136e341  04_correction_00.md + 04_report_00.md
aa1c77a91165dca6c443d54604b579324427c71e  05_handout.md (non-exchange historical handout)
```

Required artifact SHA-256 values:

```text
01_report_00.md (accepted M3 plan)          e2d0ea52a7b6ca43ebfef427d4ab882ab466b8e1e575c4dc8e80b1f1f1ffd4f7
01_report_01.md (plan completion)           7b7511ab07d46cad2fd5b94f5832fcfcf5a7960d62aac2420a7cfcb883088eca
02_implementation_00.md (implementation prompt) 427ecd959f8d83968f8044fe5f36f35cfd7004e3cdba55a0f80234c0ea1c61d9
02_report_00.md (implementation report)     d77a944ec8b36624049234b653e712a29afb797ae5417c439ce1d4a5221a202b
03_acceptance_00.md (prior acceptance prompt) b18f80b2a0a52243aa3f47c48a38206ed8bc6d161ebb9619a4baf06cbff373d7
03_report_00.md (prior acceptance PARTIAL)  5f1e201a12478c95e6dbf7d0c40df710e46a5bdff143a8f3c515529527414e00
04_correction_00.md (correction prompt)     09365daee940c23e659439894e9b5154816c6fa907efbdb6f306ae5944492ddd
04_report_00.md (correction report)         5881b59a02b32acd1fc71466bdde9a4cdd43d4bd7bc533c7110281b3cc3385fe
05_handout.md (fresh Orchestrator handout)  a1819495d1e9099c5a9b720df481e5ba642ba4cf0637fb5575cb4a3fc9fc0bf9
```

No alternate commit, mirror, stale remote-tracking ref, or retained clone may
substitute for these identities. For the product, if public `main` has moved,
stop before testing and report the exact discrepancy; do not silently retarget.
For META, a public descendant of `aa1c77a…` may be accepted only when its
history is verifiable, the exact trace pairs and SHA-256 values above are
present unchanged, and product/AP identities remain correct; otherwise stop.

## Read-only preflight

Use fresh disposable inspection clones in the Worker container, never a
COOPERATOR checkout. Before substantive acceptance:

1. Verify this is a genuinely fresh session with no implementation, correction,
   or prior-acceptance ancestry; Native Plan Mode OFF; exact 05/01 coordinates;
   and no subagents.
2. Clone the canonical product with submodules and META over HTTPS. Fetch
   `main`, compare direct `git ls-remote` with the required public tips, and
   detach at the exact required commits.
3. If transport or cache state is stale, discard only the Worker-owned clone
   and retry the canonical HTTPS remote in a new disposable location. A safe
   retry may use `git -c http.version=HTTP/1.1`. Do not change host DNS or Git
   configuration and do not use credentials or a mirror.
4. Verify clean worktrees, candidate parent `55e9813…`, M3 base `ca6052e…`,
   candidate subject `Correct M3 workspace request ownership and regressions`,
   exact AP gitlink and checkout, and `./.ap/ap doctor` PASS.
5. Verify META ancestry and that each pair commit changed exactly the two trace
   paths mapped above, plus the handout commit changing only `05_handout.md`.
   Verify the artifact SHA-256 values above by direct computation. Confirm no
   earlier accepted artifact was modified and every pair is completely readable.
6. Verify the cumulative candidate diff `ca6052e…502ae75` changed exactly the 24
   paths listed below and no dependency, AP, broker, RGB transport, KWin bridge,
   packaging, operations, hardware-evidence, license, or host file.
7. Verify the correction child `55e9813…502ae75` changed exactly the six paths
   listed below and nothing else.
8. Verify existing required build tools and `dbus-run-session`. Install nothing.
   Missing tools are a truthful blocker, not permission to mutate the
   environment.

Use detached read-only source inspection. Put all build products outside the
product checkout in a newly created Worker-owned temporary directory. The
product worktree must remain clean throughout. META must be clean at preflight;
after persistence, only the exact owned prompt/report differences are allowed.

## Mandatory reading

Read before deciding:

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-07, RF-12, RF-18, RF-19,
  acceptance/correction escalation, phase-qualified results, and stopping;
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
  `01_completion_01.md`, `01_report_01.md`, `02_implementation_00.md`,
  `02_report_00.md`, `03_acceptance_00.md`, `03_report_00.md`,
  `04_correction_00.md`, and `04_report_00.md`;
- M2 `00_handout_03.md` and `27_report_00.md` only for the parked boundary;
- the complete cumulative candidate diff and every changed product file;
- unchanged adjacent owners needed to judge behavior, limited to
  `src/context/ContextReceiver.{h,cpp}`, `src/context/DBusNames.h`,
  `src/rgb/OpenRgbClient.{h,cpp}`, `src/rgb/OpenRgbProtocol.{h,cpp}`,
  `src/app/main.cpp`, and directly included core headers.

Treat old documentation contradicting named M2 Sessions 22–24 as drift, not
authority to reopen M2. Treat `03_report_00.md` as the accepted defect record
and `04_report_00.md` as the corrector's claim; neither substitutes for your own
independent inspection.

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

Cumulative `ca6052e…502ae75` must have only these 24 changed paths:

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

The correction child `55e9813…502ae75` must have only these six changed paths:

```text
src/context/WorkspaceReceiver.cpp
src/context/WorkspaceReceiver.h
tests/unit/test_profile_persistence.cpp
tests/unit/test_profile_resolver.cpp
tests/unit/test_workspace_lighting.cpp
tests/unit/test_workspace_receiver.cpp
```

This is an inspection scope, not mutation authority. Any product change,
generated file inside the checkout, commit, branch/ref operation, or push is
forbidden.

## Measurable outcome and acceptance matrix

Return one independent verdict on whether the exact public corrected candidate
satisfies the accepted M3 code contract and is fit to proceed to a separate
COOPERATOR-owned physical five-zone checklist.

Mark every row `PASS`, `FAIL`, or `NOT TESTED`, with direct evidence:

### A1 — Identity, provenance, and scope

- exact product/AP/META public identities and ancestry;
- M3 trace pair integrity and artifact SHA-256 values above;
- cumulative 24-path diff and six-path correction child, exact parent chain,
  and clean read-only checkouts;
- no scope escape or hidden dependency/host change.

### A2 — Schema 3 and preserving migration

- only `Static`, `DesktopIndicator`, `AppColor`, and `Off` roles;
- schema-3 zones absent/null or exactly five strict role objects;
- dynamic roles rejected in application presets;
- schemas 1 and 2 preserve their required behavior in memory;
- schema-2 five-color arrays become five Static slots without read-time rewrite
  or workspace activation;
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
  base/zones, Breathing, Off, Untouched, Wave, Cycle, matched, and unmatched;
- unknown workspace releases to `untouched`; bridge loss retains valid desktop
  state; all-black workspace resolves to device Off;
- exactly five concrete colors and protocol-5 packet ordering remain correct.

### A5 — VirtualDesktopManager receiver (corrected ownership)

- exact service/object/interface and subscribe-before-snapshot ordering;
- complete `GetAll` snapshots; signals only invalidate and refresh;
- count 1–32, count/list equality, bounded unique IDs/names/positions,
  16 KiB aggregate metadata, current exactly once, position sort, signed and
  unsigned 32-bit compatibility after bounds;
- **one current logical request plus at most one coalesced pending refresh** is
  preserved across initial start, invalidation bursts, deadline, service owner
  replacement, service loss, stop, pause, resume, and recovery;
- stale or late completions are observational only: they may be counted and
  destroyed but cannot clear, apply to, or admit a newer request; explicit
  request ownership (per-request identity/token) is the mechanism;
- non-extendable 2 s deadline, duplicate snapshot suppression, and
  1/2/4/8/16/30 s bounded recovery with no seventh automatic retry and budget
  reset after success;
- service loss/replacement and pause/resume recover without healthy polling;
- logs expose only bounded error classes, not desktop identity.

### A6 — Controller, session app, and UI

- `SessionApplication` owns an independent named session-bus receiver;
- bursts coalesce, refresh defers workspace output, session overrides remain
  responsive, and equal effective output does not resubmit RGB state;
- application/desktop simultaneous changes use latest inputs and bridge-loss
  duplicate notifications are coalesced;
- a metadata-only desktop name change updates UI metadata without incrementing
  RGB lighting submission when effective desired lighting is unchanged;
- configuration-root test seam does not change production default behavior;
- QML property/method signatures are valid and compile;
- default 4+1, per-slot roles, static conversion, gradient role replacement,
  desired-preview labeling, overflow/unavailable summary, and non-persistent
  simulated pause/resume are wired truthfully;
- no navigation redesign or broker activation.

### A7 — Causal regression evidence

- inspect test bodies, not names or aggregate pass counts;
- map every required behavior from A2–A6, and every case required by
  `04_correction_00.md`, to a persistent causal regression;
- confirm the new receiver regressions distinguish logical active requests from
  still-finishing fake-service handlers and actually fail under the old shared
  `m_inFlight` behavior (causal, not merely present);
- confirm receiver/lighting tests use a fake service on a private
  `dbus-run-session` bus and controller tests use temporary configuration plus
  a non-started RGB client;
- missing persistent coverage required by the implementation or correction
  prompt is an acceptance defect even if the current build is green;
- focused and complete registered CTest suites pass from the detached public
  candidate in the fresh external build directory.

### A8 — Documentation and bounded claims

- schema, migration, receiver ownership, resolver, failure behavior,
  limitations, and later IRL checklist match code;
- candidate is described only as an implementation candidate;
- M2 remains parked with named accepted slices and the independent G3 gap;
- no physical, deployment, production, M4/M5, per-key, autostart, hibernate,
  general-coexistence, or whole-G4 claim.

Acceptance-PASS requires all A1–A8 rows PASS. `NOT TESTED` on a required row, a
confirmed contract defect, inadequate required persistent regression, or an
unresolved material discrepancy prohibits acceptance-PASS.

## Mandatory adversarial leads

These are re-issued leads from the prior acceptance and correction. Independently
confirm or disprove each; do not defer them silently.

### Lead L1 — corrected ownership under stale/late interleavings

Trace deadline, owner replacement, service loss, pause/stop, resume, and
late-reply interleavings in `WorkspaceReceiver`. Determine whether any stale or
late `QDBusPendingCallWatcher` can still clear current in-flight state, apply a
stale snapshot, or trigger/admit another logical request while a newer
generation/revision request is outstanding. Confirm that ownership is bound to
the current logical request and that an uncancellable remote completion is only
observational. Reproduce with code inspection and, if static reasoning is not
conclusive, with the bounded synthetic probe below.

### Lead L2 — causal versus merely present regression coverage

Map the correction prompt's required cases and the original A7 gaps to actual
assertions in the changed test files. Determine whether each new receiver test
would fail under the previous shared-`m_inFlight` design, and whether the
persistence, resolver, and controller additions assert the required branches
rather than restating schema code. Aggregate 5/5 and 17/17 results alone do not
resolve this lead.

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

git diff --check ca6052e816d4884ddeac9d7499a42c2aca089e7e..502ae75571358ec95d33c836084b5e2253850731
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

A completed negative verdict is useful evidence but is not acceptance-PASS. Do
not reclassify candidate failure as a Worker execution failure.

If the same assumption or finding survives this correction and recheck, stop
`PARTIAL` or `BLOCKED` and include exactly:

```text
Escalation disposition: NEEDS_ORCHESTRATOR_DECISION
```

A second automatic correction for the same assumption is prohibited without new
material evidence or a changed objective.

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

Downloadable prompt filename: `05_acceptance_00.md`
Destination:
`projects/contextdesk/00/03-g213-contextdeck-workspace-aware-lighting/05_acceptance_00.md`
Report filename: `05_report_00.md`
Report destination:
`projects/contextdesk/00/03-g213-contextdeck-workspace-aware-lighting/05_report_00.md`
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
  refs, ancestry, the 24-path cumulative and six-path correction diffs, trace
  prompt/report hashes, and clean states;
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
  bounded correction slice without granting it and include the escalation line
  when the same assumption survives; if PASS, name only the later
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

Stop before substantive review on non-fresh or inherited implementation,
correction, or acceptance context; Native Plan Mode mismatch; coordinate or
authority contradiction; identity/public-ref/ancestry/hash failure; dirty or
unsafe checkout; prompt collision; missing accepted plan or correction record;
required tool absence; or need for product, host, device, secret, or subagent
authority.

During review, preserve the first causal failure. Continue read-only inspection
only when safe and useful to bound the verdict; never correct the candidate or
expand the task. A confirmed blocking defect or required-evidence gap yields a
truthful `PARTIAL`, not an improvised patch.

Stop immediately after the terminal report. Do not implement a correction,
start the physical checklist, deploy, reopen M2, or begin another M3 phase.
