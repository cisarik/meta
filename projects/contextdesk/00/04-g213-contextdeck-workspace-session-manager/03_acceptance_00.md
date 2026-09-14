Logical whole identity: g213-contextdeck-workspace-session-manager
Worker session ordinal: 03
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Acceptance Worker
Phase: acceptance
Task identity: CONTEXTDECK-M4-SLICE-A-CODE-ACCEPTANCE
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to a genuinely fresh independent Worker session
Reasoning recommendation: High
Reasoning basis: independent acceptance must reconcile a durable schema migration,
opt-in non-logging title-fallback privacy, asynchronous D-Bus receiver
extensions, a new pure dry-run component, and claimed causal evidence
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E3
Internal delegation: prohibited

# ContextDeck M4 Slice A — fresh independent code acceptance

You are a genuinely fresh independent WORKER. You did not plan, implement,
repair, or report the candidate and did not participate in M1/M2/M3. You receive
only this complete prompt. Native Plan Mode must be OFF. Do not use subagents.

Perform one read-only independent acceptance of the immutable public M4 Slice A
implementation candidate. Treat the implementation report as a claim, not as
acceptance evidence. Inspect and test independently, persist one terminal
report, and stop. You have no correction, product publication, host, desktop,
launch, or device authority.

## Acceptance and Correction Record

Acceptance candidate: `c7c8eb90d31947bc32c498691ec926885f43cb64`
Acceptance owner map: accepted M4 plan in `01_report_00.md`, completed by `01_report_01.md`, implemented under `02_implementation_00.md`
Acceptance allowlist: read-only inspection of the exact candidate, the 27 changed product paths, directly referenced unchanged owner paths, pinned AP, and the public M4/M3/M2 continuity records listed below
Acceptance risk claims: preserving schema-1/2/3 migration and save safety; valid assignment-schema validation; identity-wins and opt-in non-logging title fallback; bounded VirtualDesktopManager rows/wrapping observation with preserved request ownership; pure observational WorkspacePlan; privacy-safe controller/UI; adequate causal tests; truthful scope and documentation
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
`c7c8eb90d31947bc32c498691ec926885f43cb64`
Required candidate parent:
`502ae75571358ec95d33c836084b5e2253850731`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

Canonical META: `https://github.com/cisarik/meta.git`
Required public META baseline:
`640b65d785c4837f94f1547b76e32f84521fa5d1`
Required implementation-pair parent:
`c7e1b73757eaffe789796ad3faf2b4db45459c5f`
Required M4 trace:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/`

Required implementation prompt SHA-256:
`b8fa2a274185c1bf784d444f50935fb82dd199e3b638ba7e3a0e736773469d38`
Required implementation report SHA-256:
`7570ee7999e684bb037fed63c7a2edc79f15fde1f2afe3a44ae1f2d69d7f8ce6`

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
   gitlink and checkout, and `./.ap/ap doctor` PASS (variant `stable`).
5. Verify META ancestry, the implementation-pair commit's exact two changed
   paths, byte identity of the prompt, report hash, complete readback, and no
   changed earlier accepted-plan/completion artifact.
6. Verify the candidate changed exactly the 27 paths listed below and no
   dependency, AP, broker, RGB transport, KWin bridge, packaging,
   SessionApplication, hardware-evidence, license, or host file.
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
  `docs/specification.md`, `docs/architecture.md`, `docs/operations.md`,
  `docs/testing.md`, `docs/testing-m2.md`, `docs/testing-m3.md`,
  `docs/testing-m4.md`, and `docs/adr/`;
- the complete public M4 artifacts `01_planning_00.md`, `01_report_00.md`,
  `01_completion_01.md`, `01_report_01.md`, `02_implementation_00.md`, and
  `02_report_00.md`;
- M3 acceptance/`01_report_01.md` and M2 `00_handout_03.md` only for the parked
  boundaries;
- the complete candidate diff and every changed product file;
- unchanged adjacent owners needed to judge behavior, limited to
  `src/context/ContextReceiver.{h,cpp}`, `src/context/DBusNames.h`,
  `src/app/SessionApplication.{h,cpp}`, `src/app/SettingsHost.{h,cpp}`,
  `src/rgb/OpenRgbClient.{h,cpp}`, `src/rgb/OpenRgbProtocol.{h,cpp}`,
  `src/app/main.cpp`, and directly included core headers.

Treat old documentation contradicting the M2/M3 park wording as drift, not
authority to reopen M2 or M3.

## Continuity and product invariants

Use this exact M3 park wording wherever M3 state is restated:

> M3 workspace-aware lighting is code-accepted on `502ae75...`; its physical
> five-zone IRL observation is deferred by explicit COOPERATOR decision. M3 is
> not closed, and code acceptance is not physical acceptance.

Use this exact M2 park wording wherever M2 state is restated:

> The named live G4 slices are accepted, but the M2 logical whole remains open.
> M2 is parked with G3 host-mitigated on the authorized reference host; the
> next bounded whole is M4 workspace session manager.

Preserve these limits while reviewing:

- Logitech G213 Prodigy only, USB `046d:c336`.
- Linux/KDE Plasma 6/Wayland, C++20/Qt6/KF6/systemd.
- Exactly five RGB zones through the existing loopback OpenRGB SDK protocol-5
  path; never per-key RGB.
- The session app observes virtual desktops directly and never opens raw input.
- Broker stays static/inactive: no LEASE, ARM, grab, pass-through, capture, or
  automatic ARM.
- input-remapper is not inspected or reconfigured.
- No secrets, raw events, key names, scan values, typed content, serials, host
  addresses, host keys, passwords, private paths, desktop IDs/names, or window
  captions may enter the report or META.
- No external G213Tray source or unresolved-license copying.
- Slice A is observational: no live desktop mutation, no application launch, no
  `kwinrulesrc` write, no placement/maximization.

This acceptance does not cover M2/G4 closure, physical visibility, M3 closure,
deployment, autostart, hibernate/hybrid sleep, M4 Slice B behavior, remapping,
a deck layer, M5 integration, production packaging, or general coexistence.

## Exact candidate changed paths

The candidate must have only these 27 changed paths:

```text
CMakeLists.txt
README.md
ROADMAP.md
docs/adr/0002-host-desktop-mutation-authority.md
docs/adr/0003-workspace-assignment-schema.md
docs/adr/0004-typed-application-launch.md
docs/adr/README.md
docs/architecture.md
docs/operations.md
docs/specification.md
docs/testing-m4.md
src/app/AppController.cpp
src/app/AppController.h
src/context/WorkspaceReceiver.cpp
src/core/Persistence.cpp
src/core/Resolver.cpp
src/core/Resolver.h
src/core/Types.h
src/workspace/WorkspacePlan.cpp
src/workspace/WorkspacePlan.h
tests/unit/test_profile_persistence.cpp
tests/unit/test_profile_resolver.cpp
tests/unit/test_workspace_plan.cpp
tests/unit/test_workspace_receiver.cpp
ui/ApplicationsPage.qml
ui/Main.qml
ui/WorkspacePage.qml
```

This is an inspection scope, not mutation authority. Any product change,
generated file inside the checkout, commit, branch/ref operation, or push is
forbidden.

## Measurable outcome and acceptance matrix

Return one independent verdict on whether the exact public candidate satisfies
the accepted M4 Slice A code contract and is fit to proceed to a separately
authorized Slice B (mutation) planning/implementation route.

Mark every row `PASS`, `FAIL`, or `NOT TESTED`, with direct evidence:

### A1 — Identity, provenance, and scope

- exact product/AP/META public identities and ancestry;
- implementation pair byte/hash integrity;
- exact 27 changed paths and clean read-only checkouts;
- no scope escape, hidden dependency change, or host/desktop/launch side effect.

### A2 — Schema 4 and preserving migration

- `kSchemaVersion` is 4; allowed root keys are exactly the six accepted keys;
- schemas 1–3 load in memory with lighting, keys, matches, application order,
  and preferences unchanged, and no read-time rewrite or workspace activation;
- future schema 5 and unknown semantic fields fail closed;
- the new preference flags default off and `active_workspace_session_id` stays
  optional;
- `match.caption` is still rejected and captions never enter `MatchSpec`.

### A3 — Assignment schema validation and save safety

- session ids non-empty, unique, ≤128 bytes, control-free;
- `desktop_ordinal` within 1–32 and ≤ session desktop count; ordinals 1-based
  and contiguous;
- `launch_desktop_file` shape (`*.desktop` or reverse-DNS, no shell
  metacharacters) and defaulting only from `match.desktop_file_name`;
- title `pattern` bounds and `mode` in `{exact, contains, prefix}`;
- a missing `workspace` object means no launch and no placement;
- 1 MiB bound, `.bak`, atomic `QSaveFile`, unsupported/invalid preservation;
- explicit save remains the only schema-4 persistence boundary.

### A4 — Resolver: identity wins, opt-in non-logging title fallback

- existing ordinary lighting resolution overloads and semantics unchanged;
- identity matching through the typed matcher wins;
- title fallback runs only when **both** global `title_fallback_enabled` and the
  profile's `title_fallback.enabled` are true; otherwise no comparison occurs;
- comparison is in memory for one call; the caption is discarded, never stored,
  never logged, and never enters `MatchSpec`;
- empty pattern never matches; the selected profile applies only to that event.

### A5 — VirtualDesktopManager rows/wrapping receiver

- `rows` and `navigationWrappingAround` decoded from the same `GetAll`
  snapshot; unknown map keys ignored; wrong types rejected;
- `rowsChanged` and `navigationWrappingAroundChanged` treated as invalidations
  that request a complete fresh snapshot;
- existing request ownership, coalescing, one-in-flight, owner generation,
  stale-reply rejection, deadlines, and recovery unchanged;
- no second `GetAll` and no raw input access; logs expose only bounded error
  classes, not desktop identity.

### A6 — Controller and UI observational surface

- all new invokables mutate the in-memory document only; `Uložiť` remains the
  only persistence boundary;
- observed state, named-session editor, dry-run preview, and per-profile
  assignment fields are wired; Apply is hidden/disabled with truthful
  later-grant copy;
- `workspaceSummary()` stays lighting-only; diagnostics maps contain no desktop
  names/UUIDs or captions; no new logging;
- QML property/method signatures are valid and compile; no navigation redesign;
- `SessionApplication.*` and the KWin bridge are unchanged.

### A7 — Causal regression evidence

- inspect test bodies, not names or aggregate pass counts;
- map every required behavior from A2–A6 to a persistent causal regression;
- confirm receiver tests use a fake service on a private `dbus-run-session`
  bus and that `WorkspacePlan` tests are pure/bus-free;
- missing persistent coverage required by the implementation prompt is an
  acceptance defect even if the current build is green;
- focused and complete registered CTest suites pass from the detached public
  candidate in the fresh external build directory.

### A8 — Documentation, ADRs, and bounded claims

- schema 4, migration, resolution, title-fallback privacy, failure behavior,
  Slice A/B boundary, and the later IRL checklist match the code;
- ADRs 0002/0003/0004 and their index match the accepted decisions;
- the candidate is described only as an implementation candidate; M4 Slice B is
  not claimed as implemented or accepted;
- M2/M3 park wording preserved; no physical, deployment, production, autostart,
  M5, per-key, or whole-G4 claim; the duplicate ROADMAP M4/M5 rows and
  "launch on session start" wording are corrected.

Acceptance-PASS requires all A1–A8 rows PASS. `NOT TESTED` on a required row,
a confirmed contract defect, inadequate required persistent regression, or an
unresolved material discrepancy prohibits acceptance-PASS.

## Two mandatory adversarial leads

These are unverified leads from ORCHESTRATOR static reconciliation, not
findings. Independently confirm or disprove each; do not defer them silently.

### Lead L1 — legacy-schema strictness versus migration compatibility

The implementation report states that schemas 1–3 now reject schema-4-only keys
as unknown semantic fields. Independently determine whether any previously valid
schema-1/2/3 document that loaded at the baseline can now fail to load, or can
have its semantics changed, because of the new root-key handling, the new
preference defaults, or the new validation. Confirm that a legacy document that
never used workspace fields still loads with unchanged lighting/keys and is not
rewritten on read.

### Lead L2 — scope of the new pure launch-intent helpers

The report's own `MEASURED` note records that `WorkspaceLaunchDebounce` and
`workspaceEventIsLaunchTrigger` were added to `WorkspacePlan` to make Slice A
testable. Independently confirm these helpers are pure, side-effect-free, and
consistent with the frozen plan's Slice A observational intent, that they do not
introduce a live trigger, launch, D-Bus, KIO, or compositor call, and that they
do not exceed the accepted scope or alter any semantic owner.

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
  -R '^(test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_plan|test_openrgb_protocol)$'

env -u LD_LIBRARY_PATH -u QT_PLUGIN_PATH \
  ctest --test-dir <owned-temp>/build --output-on-failure

git diff --check 502ae75571358ec95d33c836084b5e2253850731..c7c8eb90d31947bc32c498691ec926885f43cb64
git status --short
```

Record real counts and the first causal failure. Do not weaken, skip, or loop
tests to manufacture green output.

If a lead cannot be settled statically and the existing toolchain suffices, you
may create one minimal synthetic test only in a separate Worker-owned disposable
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
  action, device open/probe/grab, application launch, desktop mutation, or host
  configuration;
- no real display/session application launch if it could contact real KWin,
  OpenRGB, broker, or hardware;
- no secrets, credentials, host identifiers, or private paths in the report;
- no implementation, correction, speculative redesign, M2/M3 reopening,
  physical acceptance, deployment, or closure.

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

Downloadable prompt filename: `03_acceptance_00.md`
Destination:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/03_acceptance_00.md`
Report filename: `03_report_00.md`
Report destination:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/03_report_00.md`
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
META Git publication owner: COOPERATOR
Archival: wait-for-report

The ORCHESTRATOR persists this exact prompt bytes to its destination before
delivery. Verify byte identity and read it back completely. At the end, write
and completely read back the terminal report. The WORKER may prepare only the
report file and may not stage, commit, push, pull, merge, rebase, switch, or
alter META history. The COOPERATOR archives the exact pair together afterward.

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
  bounded correction slice without granting it; if PASS, name only the
  separately authorized Slice B route as not yet granted;
- compact `Orchestration critique` with `MEASURED:` and `LEAD:`;
- exactly one `Logical-whole closure: not-closed` line;
- the exact authority-expiry sentence below.

Explicitly state that code acceptance is not live desktop or physical
acceptance and does not prove M2/G4 closure, M3 closure, deployment, production
readiness, G3 re-audit, autostart, hibernate/hybrid sleep, general
input-remapper coexistence, M4 Slice B behavior, M5 behavior, per-key RGB, or
measured control-to-zone placement.

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
start Slice B, deploy, reopen M2/M3, or begin another M4 phase.
