You are one Worker instance assigned to the persistent WORKER role under the pinned Analytic Programming protocol.

Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-mvp-context-lighting
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: G213-M1-03-UI-ERGONOMICS-REDESIGN
Reasoning recommendation: High, because this exchange reworks the entire user interface and presentation layer based on direct COOPERATOR hardware acceptance and UX feedback, ensuring the desktop UI truthfully and intuitively reflects the 5-zone keyboard state without confusing "untouched" with "black", hiding unready M2 features, and streamlining navigation.

Prior exchange in this logical whole: session 02 / exchange 01, implementation-PASS, commits `4416f4be7b7476bd93ef1daab6c08af9a8a4d065` .. `042fa150cab72b4cfed24d68e6e6a940d695e525`, followed by repo baseline commits `67a3d82` and `a1f76a6`. Continuity anchor: archived at projects/contextdesk/00/01-g213-contextdeck-mvp-context-lighting/02_report_00.md.

Implementation authority: explicit
Exact baseline: a1f76a6e2e2904d8984329c76e79dd21a13bab9f
Changed-path allowlist: CMakeLists.txt ; cmake/ ; src/ ; ui/ ; kwin/ ; tests/unit/ ; docs/specification.md ; docs/operations.md ; docs/testing.md
Implementation boundaries: rework the UI presentation, navigation structure, and ergonomics according to the COOPERATOR UX specification below. Keep the core model, resolver, D-Bus context receiver, OpenRGB protocol-5 client, and power actions functional. No input interception of any kind. No host policy mutation. No writes to the real keyboard during build or automated test.
Independence required: no

Material phase gate: yes
Changed material axis: primary-objective
Ordinary-only trigger: no
Routing reopened for: primary-objective
Unchanged axes reopened: none
Reason the axis changed: the COOPERATOR tested the M1 implementation IRL, verified steps 1 and 2 PASS, and established a direct product requirement to redesign the user experience: moving from technical FormLayout pages to a task-oriented, visual desktop application with 5-zone Hero strips, simplified status summaries, hidden M2 controls, and native color dialog pickers.

Capability handshake: abbreviated recheck is sufficient in a stable fresh coding client. Report product/client if directly observed, native planning mode observed as disabled/absent, writable scope, context headroom, and that commit capability is not commit authority. Do not probe credentials.

## Trace, delivery, and envelopes

External trace disposition: configured
Trace discovery: canonical META repository https://github.com/cisarik/meta.git ; local checkout /home/agile/meta
Trace project key: contextdesk
Trace logical-whole projection identity: g213-contextdeck-mvp-context-lighting
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Standard AP exchange projection: 03_correction.md + 03_report.md
Activated META-local filename grammar: meta_exchange_index = Worker exchange ordinal - 1 ; fresh-session routing inside the same logical whole advanced the session ordinal and reset the exchange ordinal, so this exchange archives later as 03_correction_00.md + 03_report_00.md under projects/contextdesk/00/01-g213-contextdeck-mvp-context-lighting/

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 03_correction_00.md
Destination path: /home/agile/meta/projects/contextdesk/00/01-g213-contextdeck-mvp-context-lighting/
Archival: wait-for-report
Do not archive your own report; the ORCHESTRATOR does that after the report exists.

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: three CTest units — test_profile_resolver, test_profile_persistence, test_openrgb_protocol
Affected tests: all three remain green; update if C++ interface types are adjusted
Broad or full suite: the full ctest run of the three units
Runtime or testbed: local CMake/CTest in a gitignored build/, plus offscreen start of the binary with verification of QML loading
Independent acceptance: not-required in this exchange; COOPERATOR IRL acceptance follows

Repeated-gate or reasoning-loop stop: configured
Broad gate: once per materially changed candidate
Narrow before re-broad: required
Unchanged hypothesis, candidate, and failing gate: not-progress
Escalate only on: a named missing technical fact only the ORCHESTRATOR or COOPERATOR can supply
Downgrade after: convergence or named risk removal
Cost cannot falsify evidence: yes

Development envelope activation: not-used
Internal delegation posture: not-used
Accountable Worker: one WORKER
Sub-agents or internal delegation: not-used
Do not spawn subagents, Task agents, or hidden Workers.

## Communication routing

Operator / Cooperator language: Slovak
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Direct Worker-to-Cooperator language: none; report only to the ORCHESTRATOR
Required report header: ### Report for ORCHESTRATOR_CHAT
Repository documentation language: English, public-facing, human-readable and scannable
Shell and platform presentation: summarize commands; full output only for failures or safety-critical evidence

Cooperator visibility: the COOPERATOR tested steps 1 & 2 IRL and gave exact UX specifications to make the application intuitive, clear, and beautiful on KDE Plasma 6
Human decision points: none inside the allowlist if the UX specifications below are implemented as specified
Deterministic steps inside bounded authority: configure, build, test, offscreen smoke start, allowlisted edits, one commit per green stage
Brainstorming classification: classify extras as blocker, risk, backlog, future-logical-whole, or protocol-observation; never as implementation authority
Orchestrator visibility and Cooperator-legible closure: a redesigned, beautiful, intuitive QML/Kirigami desktop interface; Logical-whole closure remains not-closed

Context-pressure rule: if visible usage or compaction risk is directly observed, report it qualitatively. Stop at the nearest green stage boundary and report PARTIAL with the exact remaining stages rather than degrading a contract.

## Authority and baseline

Repository checkout topology: standalone checkout with a pinned `.ap/` submodule that is read-only evidence here
Working-copy topology: canonical-checkout, selected because main is clean and the work must build against the real host toolchain
Repository identity: https://github.com/cisarik/contextdesk.git
Expected branch: main
Expected HEAD: a1f76a6e2e2904d8984329c76e79dd21a13bab9f
Expected origin/main: ca3ac07c5fecfe3c983078e343ec6b3e02c75bea
Local main is intentionally ahead of origin/main by ORCHESTRATOR-owned documentation and fixup commits. Accepted; do not push and do not treat it as drift.
Working directory: /home/agile/Projects/contextdesk
Expected initial worktree: clean, excluding a gitignored build/ directory
AP gitlink and .ap HEAD: 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26
AGENTS.md, README.md, ROADMAP.md, LICENSE, handout.md, and docs/architecture.md are ORCHESTRATOR- or COOPERATOR-owned. Do not edit them. docs/specification.md, docs/operations.md, and docs/testing.md are allowlisted for updates reflecting this UI redesign.

Repository gate: verify root, worktree, Git directory, remotes, branch, HEAD equality with the exact baseline, submodule gitlink equality, status including untracked files, and no active Git operation. Stop on unexplained difference; do not repair it and do not discard owner work.

Applicable execution route: canonical system CMake + Ninja + project CMakeLists + CTest + installed C++ toolchain.

Mandatory reading:
- AGENTS.md, ROADMAP.md, docs/architecture.md
- docs/specification.md, docs/operations.md, docs/testing.md
- Existing UI and controller code: ui/*.qml, src/app/AppController.*, src/app/TrayController.*, src/app/SettingsHost.*
- .ap/AP.md Worker spine: §2, §3, §5, §8, §9, §10, §12, §17, §18; RF-03, RF-06, RF-07, RF-12, RF-16, RF-18, RF-19
- .ap/AP_WORKER.md ; .ap/PROMPT_CONTRACTS.md

Activated stricter profile: none
Apply R1 inline secure-implementation review: no shell strings, no QProcess, no raw keylogging, bounded inputs.

Evidence tier: E3
Authorized implementation stages: S1 presentation logic & C++ helpers ; S2 navigation & Hero overview redesign ; S3 task-oriented pages (Farby, Aplikacie, Diagnostika) ; S4 Controls demotion & self-context filtering ; S5 documentation reconciliation
Combined implementation envelope: allowed under explicit per-stage gates, with one commit at each green gate
Implementation stage gates: a stage is complete only when it configures, builds, passes ctest, stays inside the allowlist, and is committed
Independent acceptance: not-required in this exchange; COOPERATOR IRL acceptance follows

Positive authority:
- create and edit only allowlisted paths
- create a gitignored build/ directory and use /tmp for scratch
- run cmake, cmake --build, ctest, offscreen execution of ./build/contextdeck, read-only git
- one local non-amend commit per completed stage, staging only allowlisted paths
- read-only public network fetch of Qt6/Kirigami documentation if needed

Negative authority:
- no path outside the allowlist: not AGENTS.md, README.md, ROADMAP.md, LICENSE, handout.md, docs/architecture.md, .ap/, .gitmodules, META
- never run openrgb in any mode (no real device writes)
- no input interception (no libevdev, uinput, EVIOCGRAB, evtest)
- no privileged commands (no sudo, doas, systemctl, udevadm)
- no KWin mutation
- no git push, rebase, reset, clean

Commands: cmake -S . -B build -G Ninja ; cmake --build build ; ctest --test-dir build --output-on-failure ; QT_QPA_PLATFORM=offscreen ./build/contextdeck ; git add of allowlisted paths ; git commit.

## COOPERATOR UX Redesign Specifications

The goal of the first screen (Overview) is: **within 2 seconds, the user must understand: "The keyboard is on Wave, ContextDeck is not touching it; here you can configure colors."**

Implement the following exact UX items:

### 1. Hero 5-Zone Keyboard Preview instead of generic FormLayout
- On the main screen, show a prominent visual representation of the G213's 5 physical lighting zones: Left Area, Middle Area, Right Area, Arrow and Homekeys, Numpad.
- When lighting is in `untouched` (device default) state: the 5 zones must **NOT** be rendered as solid black! Black means `Off`. Instead, render them as elegant, dashed/outlined/hollow or subtly animated placeholder strips, accompanied by a clear badge: `Device default (Wave)` or `Hardware Wave`.
- When in `direct` mode: the 5 strips show their exact resolved hex colors.
- When in native effect modes (`wave`, `cycle`, `breathing`): show an appropriate effect badge or color indicator.

### 2. Single-sentence Status Summary (not 7 disparate labels)
- Replace the cluttered technical labels on Overview with one clean, human-readable status sentence:
  e.g.: `OpenRGB pripojený · kontext: Firefox · svetlá: firmware Wave.`
- Low-level technical diagnostics (`ready`, `policyRevision`, raw D-Bus interface `io.github.cisarik.ContextDeck`, bridge connection ID, socket state) belong exclusively on the **Diagnostika** (Diagnostics) page.

### 3. Demote M2 Features (Remapping & Controls Chord Recorder)
- Input remapping is reserved for milestone M2. Do NOT feature the raw chord recorder or unverified key mappings on the primary workflow path.
- Remove Controls from primary navigation, or place it under a clearly separated `Advanced` / `Pokročilé` section with an explicit banner: `Remapovanie klávesov bude aktívne v M2. V M1 svieti a deteguje kontext.`

### 4. Self-Context Handling
- When the ContextDeck settings window itself has focus, do NOT display raw `io.github.cisarik.ContextDeck` or an empty context as the primary context line.
- Display either `ContextDeck (toto okno)` or preserve and display the last observed external application identity (e.g. `Posledná aplikácia: Firefox`).

### 5. Task-oriented Navigation (not code-structure pages)
- Redesign the Kirigami navigation to follow user tasks rather than internal code units. Suggested sections:
  - **Stav** (Overview / Live status & Hero)
  - **Farby** (Colors & Global Presets)
  - **Aplikácie** (Per-Application Profiles)
  - **Diagnostika** (Technical health & D-Bus metrics)
  - **Pokročilé** (Advanced: catalog, inactive M2 shortcut viewer)
- On desktop Plasma 6, avoid cramped drawer overlay modes where a clean persistent sidebar or header tab bar provides a vastly superior desktop UX. Ensure there are no duplicate redundant page titles.

### 6. Visual Color & Gradient Editing
- Clicking a zone swatch should open a system color picker (e.g., `ColorDialog` from `QtQuick.Dialogs` or native Kirigami color selector), not require typing hex strings into a text box.
- Hex input should be accessible only as an advanced option.
- Gradient generator: two visual pickers (Start Color, End Color) + a live visual preview of the resulting 5 bands, with a clear `Použiť gradient` (Apply) button.
- Save button must be labeled clearly `Uložiť` / `Save`, never `Save profiles.json`.

### 7. Empty State & Actionable Call to Action (CTA)
- When no profile has been saved yet: show an inviting empty state: `Kým neuložíš preset, G213 ostáva na predvolenom firmware efekte (Wave).`
- Primary CTA button: `Nastaviť farby` (Configure colors) which leads directly to the Color/Preset editor.

### 8. Primary vs Overflow Overview Actions
- Primary button on Overview: `Nastaviť farby` (Configure colors).
- Secondary / maintenance actions in a clean toolbar or overflow menu: `Restore device default`, `Lights off`.
- `Follow profile` action is enabled/visible only when profiles actually exist.

### 9. Documentation Reconciliation
- Update `docs/specification.md` with the redesigned page hierarchy and Hero presentation model.
- Update `docs/testing.md` step 2: clarify that text typing can be tested in any text input field, and that the hex field lives under Colors/Profiles, not the main Overview.

## Tests and Validation

- Ensure `ctest --test-dir build --output-on-failure` passes 3/3 units.
- Run offscreen verification: `QT_QPA_PLATFORM=offscreen ./build/contextdeck` to ensure QML engine loads without syntax errors, missing module imports, or fatal warnings.

## Stages and Gates

S1 — Presentation logic & C++ helpers: AppController properties for human-readable single-sentence status, self-context detection (`isSelfWindow`), last external application tracking, and color helpers. Gate: build + ctest green, commit.
S2 — Navigation & Hero Overview: Redesign `ui/Main.qml` and `ui/OverviewPage.qml` with persistent sidebar/tabs, 5-zone Hero preview with hollow/dashed untouched state, single-sentence status summary, and primary CTA. Gate: build + offscreen start green, commit.
S3 — Task-oriented Color & Profile pages: Redesign `ui/ProfilesPage.qml` and preset editor with visual color pickers (`ColorDialog`), gradient live preview, and clean `Uložiť` actions. Gate: build + offscreen start green, commit.
S4 — Demote Controls & polish Diagnostics: Move Controls behind Advanced, ensure Diagnostika holds all low-level technical fields. Gate: build + ctest green, commit.
S5 — Documentation & test script reconciliation: Update `docs/specification.md` and `docs/testing.md` to match the redesigned UI. Gate: commit.

## Terminal Report Contract

Begin exactly with:

### Report for ORCHESTRATOR_CHAT

Echo exactly once:
Logical whole identity: g213-contextdeck-mvp-context-lighting
Worker session ordinal: 03
Worker exchange ordinal: 01

Then include:
- status: PASS | PARTIAL | BLOCKED
- Phase-qualified result: implementation-PASS if all stages green and committed
- Result artifact or commit: exact SHA range
- Result evidence: cmake/ctest summary and offscreen start validation
- Logical-whole closure: not-closed
- start and end commit of the product repository
- changed files and purpose, grouped by stage
- UX closeout: mapping of each COOPERATOR item (Hero, single-sentence status, M2 demotion, self-context, task navigation, visual pickers, CTA) to concrete changes
- tests and validation: 3/3 CTest units status, offscreen QML load verification
- commit and push result: local SHAs; push not authorized
- a stage table S1–S5 with status and rationale
- COOPERATOR hand-off: how to launch and test the redesigned interface
- deviations, risks, or missing evidence
- Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
- Pre-Existing Failure Classification: none | complete classification
- one smallest next step for the ORCHESTRATOR
- Report justification: new-mutation
- Authority expiry: implementation authority expired at this terminal report

Transition owner: ORCHESTRATOR
Stop after the terminal report.
