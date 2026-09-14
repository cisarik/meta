Logical whole identity: g213-contextdeck-workspace-session-manager
Worker session ordinal: 01
Worker exchange ordinal: 02
Persistent role identity: WORKER
Worker session target: current-worker-session
Worker session profile: Planner Report Completion Worker
Phase: planning-report-completion
Task identity: CONTEXTDECK-M4-PLAN-REPORT-COMPLETION
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to the exact Worker session that
produced the frozen M4 planning artifact
Reasoning recommendation: Medium
Reasoning basis: this is a bounded structural report repair over a frozen,
decision-complete plan; no new architecture reasoning is authorized
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E1
Evidence-tier basis: exact artifact identity, report-structure integrity, and
trace persistence only; no implementation, acceptance, or host claim
Internal delegation: prohibited

# ContextDeck M4 — render the missing valid terminal report for the frozen plan

You are the exact healthy current WORKER session that produced the technical M4
plan stored in the historical artifact below. Prior planning authority expired.
Retained context is convenience, not authority. This complete prompt grants only
report-rendering and exact trace-persistence authority.

If this is not the exact same Worker session, if the session is unhealthy or
compacted so that the frozen plan cannot be preserved faithfully, or if Native
Plan Mode cannot be disabled for this exchange, stop and report the routing
mismatch to the COOPERATOR. Do not pretend to be the current session and do not
continue in Native Plan Mode.

Continuity anchor: frozen planner artifact
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/01_report_00.md`,
18297 bytes, SHA-256
`44f01b82155a6ad584f8d1f0d5851e7020dbf4b6b1d330b1862ec06c05e34fdc`
Issued planning prompt:
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/01_planning_00.md`,
28671 bytes, SHA-256
`269ac42d446cdd5f93cc78cedcc3e3de0e4d63a1bb89a0d412c84f954e197866`
Archival status: both 01/01 files are present in the META working tree and their
first-add archival is owned by the COOPERATOR; if they are already archived,
verify the containing first-add commit added only these two paths together.
Authority renewal: prior planning authority expired; this exchange grants
report-rendering-only authority plus exact persistence of this prompt/report
pair
Evidence posture: non-independent
Repair output: standard terminal Worker report for the frozen planner artifact
Phase-qualified result: not-applicable
Frozen plan changes: prohibited
Re-planning: prohibited
Implementation: prohibited
Repository and external mutation: prohibited except the two exact local META
trace files named below
Acceptance: prohibited
Publication: prohibited
Logical-whole closure: not-closed
Planning cycle effect: none

## Why this completion exchange is required

The frozen artifact contains a detailed, source-grounded M4 technical plan, but
it is not a valid AP terminal Worker report because:

- it does not begin with `### Report for ORCHESTRATOR_CHAT`;
- it does not echo the original 01/01 prompt coordinates;
- it lacks the standard report metadata block and terminal status;
- it contains a non-public local absolute filesystem path and a stale
  self-referential statement that the companion report does not yet exist.

Do not rewrite, delete, rename, prettify, or replace that historical artifact.
Do not repair it in place. Render one new valid terminal completion report in
exchange 01/02 while treating the full technical plan as frozen evidence. The
new report must use public-safe repository-relative paths only and must not
reproduce the non-public local absolute path.

## Exact repository and artifact gate

Canonical product repository: `https://github.com/cisarik/contextdesk`
Expected product branch and public `main`:
`502ae75571358ec95d33c836084b5e2253850731`
Required product parent:
`55e981309718bcb2f94f809468eab9934acf5f51`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

Canonical META repository: `https://github.com/cisarik/meta.git`
Expected public META `main`:
`3861a6354b4f900ee50b26627be9a6786b5909f0`

Before rendering:

1. Verify the exact current-session continuity, expired prior authority, and
   Native Plan Mode OFF.
2. Verify product HEAD/public `main`, required parent, clean product worktree,
   AP gitlink/checkout equality, and `./.ap/ap doctor` PASS (variant `stable`)
   without fetching, pulling, switching, or mutating product state.
3. Verify direct public `git ls-remote` results for product and META. A later
   META descendant is acceptable only after ancestry and changed-path review
   proves that the frozen artifact, the issued prompt, and the opening notes
   remain unchanged.
4. Read the frozen artifact completely and verify its exact SHA-256 above.
   Verify the issued `01_planning_00.md` SHA-256 above. If the 01/01 pair has
   already been archived, verify the atomic first-add commit added only those
   two paths together.
5. Verify the M4 trace directory and all parents are real directories, not
   symlinks. The two new completion paths below must be absent or byte-identical
   to this exact exchange. Stop on any non-identical collision or unexplained
   META worktree state.

If identity, continuity, artifact hash, ancestry, Native Plan Mode, or path
safety fails, stop without rewriting anything. Do not retarget to a nearby
commit or regenerate the plan.

## Frozen planning content to preserve

The complete design in `01_report_00.md` remains the frozen planner artifact.
Do not add, remove, reinterpret, or correct any of its technical decisions. The
valid completion report must identify that artifact by path and SHA-256, confirm
complete readback, and include a concise fidelity digest of these already-frozen
decisions:

- explicit M4 scope and M5/G8 split: in-session desktop management, assignment,
  in-session launch, placement/maximize, and opt-in title fallback all stay
  inside M4; Plasma-login autostart, systemd `[Install]`, and production
  lifecycle stay in M5/G8;
- two separately authorized slices: observational Slice A (schema, dry-run,
  explicit-save UI, no live desktop/launch/rules writes) and mutation Slice B;
- reuse `WorkspaceReceiver` for `VirtualDesktopManager` observation, extended
  with `rows` and `navigationWrappingAround` and the two extra invalidation
  signals; named sessions are ordinal layouts, not live UUIDs; caps 1–32;
- schema 4 on the existing document with root keys `schema_version`, `device`,
  `global`, `applications`, `preferences`, `workspace_sessions`; strict unknown
  rejection; preserving in-memory migration from schema 1–3 with no lighting or
  key change until explicit save; `MatchSpec` remains the only identity matcher
  and captions never enter `match`;
- typed launch through `KIO::ApplicationLauncherJob` for a `.desktop` id, with
  `systemd-run`, `kstart`, and shell/`Exec=` wrapping rejected; triggers limited
  to explicit `applyWorkspaceSession` and in-transaction `desktopCreated`;
  duplicate-skip, debounce, bounded failure, no kill-on-revert, and a strict
  non-autostart posture;
- placement and maximize through the existing KWin bridge on `windowAdded`
  (`window.desktops` write and `setMaximize(true, true)`; `window.maximized` is
  not writable), with `PlacementHint` and no `kwinrulesrc` write; the existing
  `ContextReport` signature stays compatible;
- opt-in, event-driven, non-polling title fallback compared in memory only;
  only the user-authored pattern/mode/enabled flags are stored; captions,
  titles, and desktop names/ids are never logged or persisted; a new
  `TitleHint` is sent only when the fallback is enabled;
- minimal UI: a `Plochy` sidebar section and `WorkspacePage.qml`, plus
  `ApplicationsPage.qml` assignment fields; Apply is hidden/disabled in Slice A;
  no UI/UX redesign and no change to accepted M1/M3 lighting semantics;
- focused causal tests for schema-4 round-trip and migration, assignment
  resolution, title-fallback gating and privacy, workspace plan diffing, and
  receiver invalidation, with the registered CTest suite as the broad gate;
- a bounded COOPERATOR IRL checklist for Slice B and the explicit non-claims.

The completion report must reproduce the exact later Slice A implementation
changed-path allowlist from the frozen artifact without changing it:

```text
CMakeLists.txt
src/core/Types.h
src/core/Persistence.h
src/core/Persistence.cpp
src/core/Resolver.h
src/core/Resolver.cpp
src/context/WorkspaceReceiver.h
src/context/WorkspaceReceiver.cpp
src/workspace/WorkspacePlan.h
src/workspace/WorkspacePlan.cpp
src/app/AppController.h
src/app/AppController.cpp
src/app/SettingsHost.cpp
ui/Main.qml
ui/ApplicationsPage.qml
ui/WorkspacePage.qml
tests/unit/test_profile_persistence.cpp
tests/unit/test_profile_resolver.cpp
tests/unit/test_workspace_receiver.cpp
tests/unit/test_workspace_plan.cpp
docs/specification.md
docs/architecture.md
docs/adr/0002-host-desktop-mutation-authority.md
docs/adr/0003-workspace-assignment-schema.md
docs/adr/0004-typed-application-launch.md
docs/adr/README.md
docs/operations.md
docs/testing-m4.md
README.md
ROADMAP.md
```

Do not perform technical re-review or introduce a critique-driven plan change.
Any concern discovered while faithfully rendering must be recorded only as a
`LEAD` for the ORCHESTRATOR; it cannot alter the frozen artifact. Record the
frozen artifact's non-public local absolute path and stale self-reference as a
public-safety observation in the report, not as a plan change.

## Authority boundary

Product source mutation: prohibited
Product Git mutation: prohibited
Product commit/push: prohibited
AP mutation/update: prohibited
Host mutation: prohibited
Host service operation: prohibited
Desktop create/remove/rename or `kwinrulesrc` write: prohibited
Application launching: prohibited
Broker/OpenRGB/KWin/input-remapper operation: prohibited
Device access or probing: prohibited
Dependency installation/update: prohibited
Test/build execution: prohibited
External research: prohibited
Secrets/credentials/private data: prohibited
Network authority: direct public `git ls-remote` identity checks against the
two canonical HTTPS remotes only
Allowed side effect: exact persistence and readback of the two completion
trace files below

No raw input, raw event lines, key names, scan values, typed content, serials,
host addresses, host keys, passwords, private paths, desktop names/IDs, window
captions, or raw tool logs may enter the durable files.

## Exact trace persistence

External trace disposition: configured
Trace discovery: META README and the exact M4 trace destination
Trace project key: contextdesk
Trace logical-whole projection identity: 04-g213-contextdeck-workspace-session-manager
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_completion_01.md
Destination path: projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/
Report filename: 01_report_01.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

The ORCHESTRATOR persists this exact prompt bytes to
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/01_completion_01.md`
before delivery. The WORKER may write only the report file at
`projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/01_report_01.md`.

Before rendering, verify the already-persisted completion prompt exists and is
byte-identical to the received prompt; read it back completely. Stop on a
non-identical collision. Do not alter the 01/01 pair, `00_notes.md`, or
`00_handout.md`, create a handout, or write any other META path.

Then render the new complete terminal report to the report path. Read it back
completely and verify the header, current 01/02 coordinates, content, and
filename. Never overwrite a differing existing report. Do not stage, commit,
push, pull, merge, rebase, switch, or modify META Git history or refs. The
COOPERATOR owns atomic first-add archival of this new completion pair after the
report exists.

## Terminal completion-report contract

The new report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

It must echo the opening persistent-role and three coordinate fields exactly
once, with their values unchanged, and include:

- `status: PASS`, `PARTIAL`, or `BLOCKED`;
- the phase-qualified result fixed above;
- start/end product commit, unchanged when the gate passes;
- continuity, Native Plan Mode OFF, product/AP/META, artifact hash, ancestry,
  and clean-state evidence;
- explicit classification of `01_report_00.md` as a frozen technical planner
  artifact but invalid standard terminal companion;
- complete-readback confirmation for the frozen artifact, the issued prompt,
  and both new files;
- the faithful plan digest and exact unchanged Slice A path allowlist above;
- statement that the planning cycle and technical plan were not reopened or
  changed;
- no product/AP/host/service/desktop/launch/device/test/dependency/Git
  publication mutation;
- deviations, risks, missing evidence, and exactly one smallest next step:
  ORCHESTRATOR reconciliation and, only after acceptance, a separate fresh
  Slice A implementation Worker prompt;
- exactly one `Report justification: new-evidence`;
- `Resolved Execution Issues / Near-Misses: none` or a complete entry;
- `Pre-Existing Failure Classification: none` or a complete entry;
- compact `Orchestration critique` with `MEASURED:` and `LEAD:`;
- exactly one logical-whole not-closed line using the fixed field above;
- the exact authority-expiry sentence below.

Explicit non-claims:

- no new planning, implementation-PASS, acceptance-PASS, publication-PASS,
  deployment-PASS, physical acceptance, production readiness, whole-M2/G4
  closure, independent G3 re-audit, autostart, hibernate/hybrid sleep, general
  input-remapper coexistence, M3 closure, M3 physical five-zone observation,
  remapping, deck behavior, M5 integration, per-key RGB, or control-to-zone
  measurement;
- no claim that any desktop/session-management behavior is accepted before its
  own later implementation and acceptance;
- no claim that Session 27 was an independent Worker result;
- no claim that the malformed 01/01 companion was silently repaired in place.

Authority for this Worker expires at this terminal report.

## Stop conditions

Stop `BLOCKED` without writing over any existing file if this is not the exact
current Worker session, Native Plan Mode remains enabled, the frozen artifact
or its hash differs, repository/AP/META identity fails, the prompt/report path
collides, unexplained owner work exists, or completing the report would require
replanning, implementation, another path, a prohibited side effect, private
data, or subagents.

Use `PARTIAL` only if the exact frozen artifact is available and useful
completion evidence can be preserved but one required report-integrity item
cannot be completed. Use `PASS` only after the valid standard terminal report
and exact completion prompt are both persisted and completely read back.

Stop immediately after the terminal report. Do not begin implementation or
continue planning under this authority.
