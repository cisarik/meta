You are one Worker instance assigned to the persistent WORKER role under the pinned Analytic Programming protocol.

Persistent role identity: WORKER
Prior logical whole identity: g213-contextdeck-mvp-context-lighting
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Fresh Implementation Planning Worker
Phase: plan
Task identity: G213-M2-PLAN-INPUT-SAFETY
Reasoning recommendation: High, because input interception, device grabbing via EVIOCGRAB, uinput creation, event loop lifecycle, crash recovery, and privilege isolation must be designed to guarantee the keyboard is NEVER locked out even if ContextDeck crashes or hangs.

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-, system-, and hardware-grounded implementation plan for a dedicated, fail-safe G213 input broker, without implementation
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: none
Maximum plan-only cycles: 1

Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0

Material phase gate: yes
Changed material axis: primary-objective
Ordinary-only trigger: no
Routing reopened for: primary-objective
Unchanged axes reopened: none
Reason the axis changed: M1 (context lighting) is closed and accepted IRL; M2 opens the safety-critical input vertical (G1 physical key routing, G3 device authority, G4 pass-through broker and crash recovery).

Capability handshake: full. Report requested vs directly observed vs inferred vs unknown for product/client/model, reasoning/context pressure, native planning mode, filesystem containment, network/tools, source inspection, tests, commit, push, and any relevant provider/platform safety limits. Capability does not grant authority. Do not probe credentials.

## Trace, delivery, and envelopes

External trace disposition: configured
Trace discovery: canonical META repository https://github.com/cisarik/meta.git ; local checkout /home/agile/meta
Trace project key: contextdesk
Trace logical-whole projection identity: g213-contextdeck-input-passthrough-safety
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Standard AP exchange projection: 01_plan.md + 01_report.md
Activated META-local filename grammar: meta_exchange_index = Worker exchange ordinal - 1 ; this exchange archives later as 01_planning_00.md + 01_report_00.md under projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_planning_00.md
Destination path: /home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
Archival: wait-for-report
Do not archive your own report; the ORCHESTRATOR does that after the report exists.

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: three CTest units — test_profile_resolver, test_profile_persistence, test_openrgb_protocol (from M1)
Affected tests: none in this plan-only exchange
New causal regression: none in plan
Broad or full suite: not-used
Runtime or testbed: not-used
Independent acceptance: not-required for planning

Repeated-gate or reasoning-loop stop: configured
Broad gate: once per materially changed candidate
Narrow before re-broad: required
Unchanged hypothesis, candidate, and failing gate: not-progress
Escalate only on: named missing hardware, kernel, or permission facts only the Orchestrator/Cooperator can supply
Downgrade after: convergence or named risk removal
Cost cannot falsify evidence: yes

Development envelope activation: not-used
Internal delegation posture: not-used
Accountable Worker: one WORKER
Sub-agents or internal delegation: not-used
Do not spawn subagents, Task agents, or hidden Workers. One accountable Worker only.

## Communication routing

Operator / Cooperator language: Slovak
Orchestrator-to-Cooperator language: Slovak
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Direct Worker-to-Cooperator language: none; report only to the ORCHESTRATOR
Required report header: ### Report for ORCHESTRATOR_CHAT
Repository documentation language: English
Shell and platform presentation: report exact commands and public-safe outputs; no raw tool-log dumps

Cooperator visibility: objective, logical whole, routing, material authority, risks/trade-offs, acceptance and later closure
Human decision points: input privilege boundary (G3), physical key routing table (G1), crash-recovery invariants, autostart policy (never autostart unproven broker), and residual security risks
Deterministic steps inside bounded authority: read-only inspection and one terminal planning report; no per-step approval
Brainstorming classification: classify extras as blocker, risk, backlog, future-logical-whole, or protocol-observation; never as implementation authority
Orchestrator visibility and Cooperator-legible closure: decision-complete implementation plan for M2; Logical-whole closure remains not-closed

Context-pressure rule: if visible usage or compaction risk is directly observed, report it qualitatively; do not infer from marketing.

## Authority and baseline

Repository checkout topology: standalone checkout of the product repository, with read-only inspection of adjacent AP and META checkouts as evidence only
Working-copy topology: canonical-checkout
Repository identity: https://github.com/cisarik/contextdesk.git
Expected branch: main
Expected HEAD: b5c4be6b179a3df6e3f3803c02d819c1a7b4fe8c
Expected origin/main: ca3ac07c5fecfe3c983078e343ec6b3e02c75bea
Local main is ahead of origin/main by ORCHESTRATOR-owned documentation and accepted M1 commits. Accepted; do not push.
Working directory: /home/agile/Projects/contextdesk
Expected initial worktree: clean
Tracked files: all M1 source (`src/core/`, `src/rgb/`, `src/context/`, `src/actions/`, `src/app/`, `ui/`, `kwin/`, `tests/unit/`, `docs/`, `CMakeLists.txt`, `packaging/systemd/`)
AP gitlink: 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26

Repository gate: independently verify product-repo root, physical worktree, Git directory, remotes, branch, HEAD, submodule gitlink, and status. Stop on unexplained difference; do not repair it.

Applicable execution route: none declared. Use read-only file, Git, package-query, and system-inspection commands only.

Mandatory reading:
- AGENTS.md (project invariants: G213 only, fail-safe defaults, input grabbing must not ship before handout §29 safety acceptance)
- ROADMAP.md (M1 accepted IRL; M2 objectives, gates G1, G3, G4; verified toolchain facts)
- docs/architecture.md (Process model: dedicated broker, no GUI; Input path contract; Security posture; Packaged OpenRGB udev exposure section)
- handout.md §29 (Safety acceptance: crash leaves real keyboard usable, no stuck modifiers, no duplicate/phantom events, documented TTY recovery, never autostart unproven grab)
- .ap/AP.md : Semantic Authority, §2-§3, Plan-to-Execution Gate, Planning Budget, Implementation Authority, RF-01-RF-08, RF-14, RF-15, RF-17-RF-19
- .ap/PROMPT_CONTRACTS.md : report header, Planning Record, Common Worker Task Fields
- .ap/AP_WORKER.md
- .ap/INFOSEC.md sections 3, 4.1-4.3, 5, 11, 14, 15 as advisory threat-model input

Positive authority:
- read-only inspection of /home/agile/Projects/contextdesk, /home/agile/Projects/ap, and /home/agile/meta
- read-only Git inspection
- read-only public network fetch of documentation and kernel/libevdev API headers
- read-only local system reconnaissance on this workstation: `/dev/input/by-id`, udev properties for G213, `/proc/bus/input/devices`, libevdev installed headers (`/usr/include/libevdev-1.0/libevdev/libevdev.h`, `/usr/include/libevdev-1.0/libevdev/libevdev-uinput.h`), `/dev/uinput` permissions/ACLs, systemd watchdog APIs (`sd_notify`, `WATCHDOG=1`)
- design, but do not execute, the G1 physical key routing probe
- one English terminal planning report in chat

Negative authority:
- no implementation
- no file creation, edit, delete in any tree
- no Git stage, commit, push, reset, branch
- no package install, service mutation, or udev write
- no EVIOCGRAB, evtest grab, libevdev grab, uinput creation, or /dev/input device node claim
- no keystroke logging
- no physical press of Game Mode or Backlight during this planning exchange
- no secrets, private URLs, environment dumps, or USB serial numbers in the report

## Accepted Cooperator Decisions Governing M2

1. **Safety First (Handout §29):** An ordinary userspace crash (`SIGTERM`, `SIGKILL`, `SIGSEGV`) must NEVER leave the user unable to type. Kernel file descriptor closure must automatically release `EVIOCGRAB`.
2. **Pass-Through Only in M2:** M2 introduces **zero key remapping**. The broker acquires G213 event nodes, forwards every event 1:1 through a virtual uinput device, and proves pass-through fidelity (<5 ms latency, no dropped keys, repeat semantics, indicators) and crash/hang recovery before any remapping is authorized in M3.
3. **Dedicated Broker Architecture:** The broker is a separate, unprivileged C++20 binary (`contextdeck-broker`) with NO GUI, NO OpenRGB, NO KWin scripting, NO network.
4. **All-or-Nothing Multi-Node Acquisition:** G213 has two event nodes (`event7` if00 and `event8` if01). If either grab fails, release all immediately.
5. **Synthetic Key Ledger:** Separate physical and synthetic key ownership. Every synthetic key press must have a balanced release. Never drop a modifier that another device owns. Reconcile on `SYN_DROPPED`.
6. **Lease Model:** Broker disarms if the session application disconnects, crashes, or heartbeat lease expires.
7. **Never Autostart an Unproven Broker:** Autostart remains strictly opt-in after G4 independent acceptance.

## Required Planning Analysis for M2

Produce a decision-complete architecture and implementation plan for Milestone M2:

### A. Hardware Topology and the G1 Physical-Control Probe
- Map G213 USB interfaces (`if00` boot keyboard, `if01` consumer/vendor) and current event nodes.
- Design an explicit, safe, non-destructive Cooperator-assisted physical probe for all 20 controls: F1–F12, Previous, Play/Pause, Next, Mute, Volume Down, Volume Up, Game Mode, Backlight.
- Document how the probe records event node, Linux EV_KEY code, repeat behavior, and firmware effects without keylogging ordinary typing.
- Explicit criteria for classifying Game Mode and Backlight (remappable host event vs firmware-only).

### B. Device Permission & Privilege Architecture (Gate G3)
- Evaluate and recommend the exact permission model for `/dev/input/event*` and `/dev/uinput`:
  - Dedicated unprivileged system user/group with narrow udev rule matching only `046d:c336`.
  - Systemd system service vs user service with socket/FD passing.
  - Why running as root or GUI sudo is strictly rejected.
  - Verify `/dev/uinput` access (`user:agile:rw-` already present via KDE Connect).
  - Explicit rollback/uninstall instructions for any host rule.

### C. Broker Architecture & Event Forwarding Engine (Gate G4)
- C++20 `libevdev` + `uinput` forwarding engine architecture.
- Uinput virtual keyboard descriptor specification: name, vendor/product ID (must be distinct from physical G213 to prevent loopback), capability bits.
- Real-time event loop (`epoll` or Qt event loop): latency budget (<5 ms p99).
- Repeat handling: native hardware repeat vs software repeat; pass-through framing.
- Multi-node grab contract: atomic-like acquisition and teardown.

### D. Crash, Hang, and Zero-Lockout Recovery Invariants
- Kernel cleanup verification: evdev FD closure drops `EVIOCGRAB`; uinput FD closure destroys virtual device.
- Watchdog design: systemd watchdog (`sd_notify("WATCHDOG=1")`) fed directly from the input event loop; hang detection triggering abort.
- Emergency recovery procedure: documented TTY switch, second keyboard, emergency kill shortcut.
- Disarm-on-disconnect: session app crash disarms the broker.

### E. Session App to Broker IPC
- Communication protocol: local Unix domain socket or private D-Bus.
- Bounded policy and heartbeat messages: arm, disarm, status query.
- Lease expiry semantics.

### F. Implementation Phasing & Stages for M2
- Define exact sequential implementation stages for M2:
  - Stage P1: G1 hardware probe execution and routing matrix.
  - Stage S1: uinput virtual keyboard & forwarding engine (without grabbing).
  - Stage S2: libevdev multi-node acquisition & all-or-nothing grab.
  - Stage S3: Watchdog, synthetic ledger, and crash/hang recovery harness.
  - Stage S4: Broker IPC & session application integration.
  - Stage S5: Safety acceptance testbed (`docs/testing-m2.md`) and operations guide.

### G. Risk Assessment & Mitigations
- Keylogging prevention (no event logging, isolated process).
- Virtual device feedback loops.
- Stuck modifier keys.
- Lost focus / race conditions.

## Decision-Complete Report Requirements

Use the standard AP terminal-report structure beginning with:

### Report for ORCHESTRATOR_CHAT

Echo exactly once:
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 01
Worker exchange ordinal: 01

Then include:
- status: PASS | PARTIAL | BLOCKED
- Phase-qualified result: not-applicable
- Result artifact or commit: not-applicable
- Result evidence: bounded read-only planning evidence
- Logical-whole closure: not-closed
- start and end commit of the product repo (both `b5c4be6b179a3df6e3f3803c02d819c1a7b4fe8c`)
- changed files: none
- the complete planning analysis covering A through G above
- facts vs assumptions vs unknowns, and named evidence gates (G1, G3, G4)
- exact implementation stages, allowlists, and stage gates for the subsequent implementation worker
- one smallest next step for the ORCHESTRATOR
- Report justification: new-evidence
- Authority expiry: planning authority expired at submission of this terminal report

Keep the report public-safe: no secrets, tokens, private URLs, personal data, or USB serial numbers.

Transition owner: ORCHESTRATOR
Stop after the terminal planning report.
