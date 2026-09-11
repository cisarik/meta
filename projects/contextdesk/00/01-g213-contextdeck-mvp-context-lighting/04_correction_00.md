You are one Worker instance assigned to the persistent WORKER role under the pinned Analytic Programming protocol.

Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-mvp-context-lighting
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: G213-M1-04-BREATHING-AND-GRADIENT-FIX
Reasoning recommendation: High, because this exchange addresses verified physical hardware and UI defects found during COOPERATOR IRL testing: Breathing mode requires mode-specific color and speed serialization in OpenRGB protocol 5 to avoid breathing invisible black, animation speed controls must be exposed for all animated native modes (Wave, Cycle, Breathing), and the 5-zone gradient generator UI must reliably apply and display colors.

Prior exchange in this logical whole: session 03 / exchange 01, implementation-PASS, commits `e46a57210c86ecbc82b0b48e5550c676608b4a51` .. `1781a40a8a92bc91ab867819b4da8ffe737b97f1`, followed by baseline commits `9fd9eac` and `2248729`. Continuity anchor: archived at projects/contextdesk/00/01-g213-contextdeck-mvp-context-lighting/03_report_00.md.

Implementation authority: explicit
Exact baseline: 22487299c8369527ec3187a550d500473e34b95f
Changed-path allowlist: CMakeLists.txt ; cmake/ ; src/ ; ui/ ; tests/unit/ ; docs/specification.md ; docs/operations.md ; docs/testing.md
Implementation boundaries: fix Breathing mode color and speed serialization, add speed parameter to animated modes in schema/model, expose speed and breathing color in the UI, and fix the 5-zone gradient generator application in `LightingPresetEditor.qml`. Keep all existing contracts, resolvers, D-Bus context receiver, and power actions functional. No input interception of any kind. No host policy mutation. No writes to the real keyboard during build or automated test.
Independence required: no

Material phase gate: yes
Changed material axis: primary-objective
Ordinary-only trigger: no
Routing reopened for: primary-objective
Unchanged axes reopened: none
Reason the axis changed: IRL hardware testing on the physical Logitech G213 confirmed that five-zone Direct lighting works, but identified that Breathing mode requires mode-specific color and speed in the OpenRGB protocol packet to be visible, animation speed is unconfigurable, and the Gradient UI generator fails to apply colors across the 5 zones.

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

Standard AP exchange projection: 04_correction.md + 04_report.md
Activated META-local filename grammar: meta_exchange_index = Worker exchange ordinal - 1 ; this exchange archives later as 04_correction_00.md + 04_report_00.md under projects/contextdesk/00/01-g213-contextdeck-mvp-context-lighting/

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 04_correction_00.md
Destination path: /home/agile/meta/projects/contextdesk/00/01-g213-contextdeck-mvp-context-lighting/
Archival: wait-for-report
Do not archive your own report; the ORCHESTRATOR does that after the report exists.

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: three CTest units — test_profile_resolver, test_profile_persistence, test_openrgb_protocol
Affected tests: all three remain green; extend test_openrgb_protocol to verify Breathing color and speed serialization, and test_profile_persistence for speed persistence
Broad or full suite: the full ctest run of the three units
Runtime or testbed: local CMake/CTest in a gitignored build/, plus offscreen start of the binary
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

Cooperator visibility: the COOPERATOR verified physical 5-zone control works on the real G213, but found Breathing was invisible and Gradient did not apply
Human decision points: none inside the allowlist if the technical defect solutions below are implemented as specified
Deterministic steps inside bounded authority: configure, build, test, offscreen smoke start, allowlisted edits, one commit per green stage
Brainstorming classification: classify extras as blocker, risk, backlog, future-logical-whole, or protocol-observation; never as implementation authority
Orchestrator visibility and Cooperator-legible closure: working Breathing animation with color & speed, and working 5-zone Gradient generator; Logical-whole closure remains not-closed

Context-pressure rule: if visible usage or compaction risk is directly observed, report it qualitatively. Stop at the nearest green stage boundary and report PARTIAL with the exact remaining stages rather than degrading a contract.

## Authority and baseline

Repository checkout topology: standalone checkout with a pinned `.ap/` submodule that is read-only evidence here
Working-copy topology: canonical-checkout, selected because main is clean and the work must build against the real host toolchain
Repository identity: https://github.com/cisarik/contextdesk.git
Expected branch: main
Expected HEAD: 22487299c8369527ec3187a550d500473e34b95f
Expected origin/main: ca3ac07c5fecfe3c983078e343ec6b3e02c75bea
Local main is intentionally ahead of origin/main by ORCHESTRATOR-owned documentation and fixup commits. Accepted; do not push and do not treat it as drift.
Working directory: /home/agile/Projects/contextdesk
Expected initial worktree: clean, excluding a gitignored build/ directory
AP gitlink and .ap HEAD: 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26
AGENTS.md, README.md, ROADMAP.md, LICENSE, handout.md, and docs/architecture.md are ORCHESTRATOR- or COOPERATOR-owned. Do not edit them. docs/specification.md, docs/operations.md, and docs/testing.md are allowlisted for updates.

Repository gate: verify root, worktree, Git directory, remotes, branch, HEAD equality with the exact baseline, submodule gitlink equality, status including untracked files, and no active Git operation. Stop on unexplained difference; do not repair it and do not discard owner work.

Applicable execution route: canonical system CMake + Ninja + project CMakeLists + CTest + installed C++ toolchain.

Mandatory reading:
- AGENTS.md, ROADMAP.md, docs/architecture.md
- docs/specification.md, docs/operations.md, docs/testing.md
- Existing protocol and UI code: src/rgb/OpenRgbProtocol.*, src/rgb/OpenRgbClient.*, src/core/Types.h, src/core/Persistence.*, src/app/AppController.*, ui/LightingPresetEditor.qml
- .ap/AP.md Worker spine: §2, §3, §5, §8, §9, §10, §12, §17, §18; RF-03, RF-06, RF-07, RF-12, RF-16, RF-18, RF-19
- .ap/AP_WORKER.md ; .ap/PROMPT_CONTRACTS.md

Activated stricter profile: none
Apply R1 inline secure-implementation review: no shell strings, no QProcess, no raw keylogging, bounded inputs.

Evidence tier: E3
Authorized implementation stages: S1 model & protocol speed/breathing color ; S2 UI speed slider & breathing color picker ; S3 gradient UI generator fix ; S4 test updates & documentation
Combined implementation envelope: allowed under explicit per-stage gates, with one commit at each green gate
Implementation stage gates: a stage is complete only when it configures, builds, passes ctest, stays inside the allowlist, and is committed
Independent acceptance: not-required in this exchange; COOPERATOR IRL acceptance follows

Positive authority:
- create and edit only allowlisted paths
- create a gitignored build/ directory and use /tmp for scratch
- run cmake, cmake --build, ctest, offscreen execution of ./build/contextdeck, read-only git
- one local non-amend commit per completed stage, staging only allowlisted paths

Negative authority:
- no path outside the allowlist: not AGENTS.md, README.md, ROADMAP.md, LICENSE, handout.md, docs/architecture.md, .ap/, .gitmodules, META
- never run openrgb in any mode (no real device writes)
- no input interception (no libevdev, uinput, EVIOCGRAB, evtest)
- no privileged commands (no sudo, doas, systemctl, udevadm)
- no KWin mutation
- no git push, rebase, reset, clean

Commands: cmake -S . -B build -G Ninja ; cmake --build build ; ctest --test-dir build --output-on-failure ; QT_QPA_PLATFORM=offscreen ./build/contextdeck ; git add of allowlisted paths ; git commit.

## Specific Defects and Technical Requirements

### 1. Breathing Mode: Mode-Specific Color and Speed
- **Root Cause from OpenRGB G213 source (`RGBController_LogitechG213.cpp`):**
  The G213 Breathing mode defines:
  `Breathing.flags = MODE_FLAG_HAS_MODE_SPECIFIC_COLOR | MODE_FLAG_HAS_SPEED;`
  `Breathing.color_mode = MODE_COLORS_MODE_SPECIFIC;`
  `Breathing.colors_min = 1; Breathing.colors_max = 1;`
  `DeviceUpdateMode()` calls:
  `if (modes[active_mode].color_mode == MODE_COLORS_MODE_SPECIFIC) { red = ...; grn = ...; blu = ...; }`
  `controller->SetMode(modes[active_mode].value, modes[active_mode].speed, direction, red, grn, blu);`
  Currently, `encodeDesiredStateFrames` sends `modes.at(*index)` without setting any color in `mode.colors`. As a result, the controller receives `red=0, grn=0, blu=0` and breathes black!
- **Fix:**
  - In `src/core/Types.h`:
    Add `std::optional<quint32> speed;` to `struct Lighting` and `struct DesiredLighting`.
    Ensure `Lighting` has a field for the primary mode color when in `Breathing` mode (can use `baseColor`, defaulting to a vibrant color like `#7c3aed`).
  - In `src/rgb/OpenRgbProtocol.cpp` (`encodeDesiredStateFrames`):
    When `desired.mode == LightingMode::Breathing`:
    Copy `ControllerMode modeCopy = modes.at(*index);`
    Ensure `modeCopy.colors.resize(1);`
    Set `modeCopy.colors[0] = desired.baseColor.value_or(Rgb{0x7c, 0x3a, 0xed});`
    If `desired.speed.has_value()`, clamp between `modeCopy.speedMin` and `modeCopy.speedMax` and set `modeCopy.speed = *desired.speed;`
    Use `modeCopy` when calling `encodeUpdateMode`.
  - When `desired.mode` is `Wave` or `Cycle`:
    Copy `ControllerMode modeCopy = modes.at(*index);`
    If `desired.speed.has_value()`, clamp and set `modeCopy.speed = *desired.speed;`
    Use `modeCopy` when calling `encodeUpdateMode`.

### 2. Animation Speed Control in UI and Schema
- In `src/core/Persistence.cpp`:
  Support optional `speed` integer in schema 2 JSON for `Lighting` (e.g. `speed: <number>`). If absent, keep `std::nullopt`.
- In `src/app/AppController.*`:
  Expose `speed` getter/setter (e.g. `setGlobalSpeed(int)`, `setApplicationSpeed(id, int)`).
  Expose `minSpeed` / `maxSpeed` or normalized 0-100 percentage. Note: for G213, OpenRGB defines `speed_min` and `speed_max` on the mode (typically slowest to fastest). Provide a clean 0-100 slider or mapped value.
- In `ui/LightingPresetEditor.qml`:
  - Show a **Rýchlosť animácie** (Speed) slider when the current mode is `wave`, `cycle`, or `breathing`.
  - Show a **Farba dýchania** (Breathing Color) swatch / `ColorDialog` when the current mode is `breathing`.

### 3. Five-Zone Gradient Generator Fix
- In `ui/LightingPresetEditor.qml`:
  - Investigate why `applyGradient()` failed to visibly update the 5 swatches.
  - Fix color property handling: do NOT rely on reading/writing read-only properties of `ColorDialog`. Store clean `color` properties on the QML root (`startColor`, `endColor`), format them cleanly to `#rrggbb`.
  - Ensure clicking `Použiť gradient`:
    1. Immediately updates the internal `root.zones` so the 5 visual zone swatches change their displayed color immediately.
    2. Switches mode to `direct` if not already direct.
    3. Triggers `app.applyGlobalGradient(startHex, endHex)` / `app.applyApplicationGradient(...)`.
    4. Triggers `app.save()` or prompts that changes are ready to be saved with `Uložiť`.
  - Ensure the live 5-swatch preview bar under the start/end color pickers updates reactively as colors are picked.

### 4. Tests and Documentation
- In `tests/unit/test_openrgb_protocol.cpp`:
  Add test assertions verifying that `encodeDesiredStateFrames` for `Breathing` mode encodes 1 color and the specified `speed`, and that `Wave`/`Cycle` encode `speed`.
- In `tests/unit/test_profile_persistence.cpp`:
  Add test asserting that `speed` in schema 2 round-trips and is preserved.
- Update `docs/specification.md` and `docs/testing.md` to reflect the animation speed parameter and Breathing color.

## Stages and Gates

S1 — Model & Protocol: `speed` and breathing color in `Lighting`, `DesiredLighting`, and `encodeDesiredStateFrames`. Tests in `test_openrgb_protocol.cpp` and `test_profile_persistence.cpp`. Gate: build + ctest green, commit.
S2 — AppController & UI Speed / Breathing Color: expose speed and breathing color to QML, add speed slider and breathing swatch to `LightingPresetEditor.qml`. Gate: build + offscreen start green, commit.
S3 — Gradient UI Generator Fix: rework `LightingPresetEditor.qml` gradient picker bindings, immediate swatch update, and apply/save flow. Gate: build + offscreen start green, commit.
S4 — Documentation reconciliation: update `docs/specification.md` and `docs/testing.md` step instructions. Gate: commit.

## Terminal Report Contract

Begin exactly with:

### Report for ORCHESTRATOR_CHAT

Echo exactly once:
Logical whole identity: g213-contextdeck-mvp-context-lighting
Worker session ordinal: 04
Worker exchange ordinal: 01

Then include:
- status: PASS | PARTIAL | BLOCKED
- Phase-qualified result: implementation-PASS if all stages green and committed
- Result artifact or commit: exact SHA range
- Result evidence: cmake/ctest summary and offscreen start validation
- Logical-whole closure: not-closed
- start and end commit of the product repository
- changed files and purpose, grouped by stage
- defect closeout: exact explanation and code changes for Breathing mode color+speed and Gradient application
- tests and validation: 3/3 CTest units status, offscreen QML load verification
- commit and push result: local SHAs; push not authorized
- a stage table S1–S4 with status and rationale
- COOPERATOR hand-off: exact instructions to test Breathing with color/speed and Gradient on the physical keyboard
- deviations, risks, or missing evidence
- Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
- Pre-Existing Failure Classification: none | complete classification
- one smallest next step for the ORCHESTRATOR
- Report justification: new-mutation
- Authority expiry: implementation authority expired at this terminal report

Transition owner: ORCHESTRATOR
Stop after the terminal report.
