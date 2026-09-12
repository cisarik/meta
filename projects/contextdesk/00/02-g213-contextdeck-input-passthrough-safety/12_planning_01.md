You are the same Worker that completed CONTEXTDESK-M2-AP-ADOPTION-AND-STATE-RECONCILIATION. Its authority expired. This is a complete, separate planning grant.

Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 12
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: CONTEXTDESK-M2-ONE-KEYBOARD-RECOVERY-REVISION
Continuity anchor: 12_report_00.md, prior exchange 12/01, product commit 64dd12bbc34c5ab09574d8edc76ebb7bed50af2d
Reasoning recommendation: High — keyboard availability, independent recovery, and privileged test-lifecycle design.
Recommended context capacity: approximately 250k tokens
Selected model: Grok 4.6, COOPERATOR-selected; distinguish requested from observed capabilities.
Delivery: manual
Internal delegation posture: not-used
Independence required: no — planning is non-independent; later safety acceptance requires fresh independent evidence.

Confirm actual same-session continuity and Native Plan Mode. Do not simulate either or silently change the route.

## Planning contract

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: targeted revision of M2 recovery and production-readiness prerequisites for bounded testing with one physical keyboard
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1

Planning cycle: targeted-revision
Prior planning report: projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/01_report_00.md
Targeted revision basis: new-repository-or-external-evidence
Changed decision boundary: a demonstrable one-keyboard recovery path and the production prerequisites needed before first grab and before full G4 acceptance
Preserved unaffected decisions: G213-only; M1 accepted history; measured G1 control exclusions; pass-through-only M2; isolated unprivileged broker; narrow device access; explicit authenticated ARM; all-or-nothing acquisition; ungrab-first teardown; unchanged input-remapper; no unproven autostart
Automatic targeted revisions used: 1

This revision is justified by the production source gaps and updated host evidence in exchange 12/01, together with the COOPERATOR’s request to evaluate an alternative to a second keyboard/off-box SSH.

Do not reset earlier planning or blocked-acceptance history. Do not reopen the general product architecture.

“Implementation in same Worker session: allowed” selects a possible later route only. No implementation is authorized now. Plan UI approval or an automatic mode transition does not authorize execution.

## Baseline and sources

Product repository: https://github.com/cisarik/contextdesk.git
Working directory: /home/agile/Projects/contextdesk
Working-copy topology: canonical-checkout, read-only
Expected branch: main
Expected HEAD: 64dd12bbc34c5ab09574d8edc76ebb7bed50af2d
Expected parent: 24305864f54d7161048041c2e5309aa8a0f8fb1a
Governing AP gitlink and checkout: 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9

Verify identity, worktree/index, submodule state, and relevant continuity. Preserve unrelated work. If the baseline changed, report its significance without resetting or pulling the repository.

Read the applicable AP Worker foundation and targeted planning/expiry/report contracts. Additional reading:

* AGENTS.md and the M2 portions of ROADMAP.md.
* Accepted M2 plan, especially architecture, recovery, and stage contracts.
* 12_report_00.md; use earlier reports only to resolve a specific question.
* docs/operations.md sections 6–9 and docs/testing-m2.md.
* Relevant docs/architecture.md requirements.
* Broker Acquisition, RealSink, EvdevSource, ProductionRuntime, EventLoop, Watchdog, SessionIpc, and the session-app BrokerIpcClient.
* Relevant existing tests and systemd packaging.
* Matching installed systemd/libevdev documentation and primary upstream sources where needed.

Do not reread the whole archive or repeat the prior host inventory. Recheck only facts that materially affect the proposed design.

## Authority

Allowed:

* read-only repository, source, installed documentation, and narrowly relevant host metadata inspection;
* public primary-source research;
* design analysis and proposed code/configuration/commands in the report;
* the exact report and supplied notes persistence described below;
* a client-native planning artifact if required by Native Plan Mode, confined to its normal planning location and reported.

Forbidden:

* implementation or product-file edits, including AP, packaging, tests, and docs;
* product or Meta Git mutation, commits, pushes, branch changes, resets, stashes, or permission changes;
* sudo, package installation, host file installation, service operations, udev test/trigger/reload, or ACL changes;
* running ContextDeck, broker binaries, ARM/LEASE clients, input listeners, grabs, uinput creation, or signal-based experiments;
* modifying input-remapper, OpenRGB, KWin, user profiles, power state, or autostart;
* credentials, raw keyboard/HID data, private process arguments, or environment dumps;
* subagents, independent certification, G4 acceptance, or whole closure.

Read existing process/service metadata only where useful to determine the session application’s launch context. Do not start it to answer that question.

Unavailable privileged metadata does not justify escalation during this planning exchange. Identify the exact later probe if the fact is essential.

## Required outcome

Return one decision-complete implementation plan, with a recommended mechanism and exact staged validation. It must answer:

1. How will a bounded test recover when the only keyboard is grabbed and the broker or controlling app cannot cooperate?
2. What must be demonstrated without the physical keyboard before authorizing the first live trial?
3. Which source gaps must be repaired before that first trial, and which remain mandatory before full G4 acceptance?
4. What exact next implementation scope should the ChatOrchestrator authorize?

### A. Independent automatic recovery

Compare the smallest viable systemd-controlled finite service lifetime and pre-armed external cutoff options. Select one evidence-backed arrangement; combine mechanisms only for a named failure mode.

The selected design must address:

* a hung or SIGSTOP-stopped broker;
* a responsive event loop whose forwarding fails while watchdog notifications continue;
* session-app or controlling-terminal loss;
* cleanup without subsequent keyboard input, a password prompt, network access, or an LLM response;
* verified readiness before ARM, including failure to establish the recovery mechanism;
* a finite useful test window and bounded termination escalation;
* exact ownership and targeting, avoiding stale timers/PIDs affecting a later invocation;
* cleanup after success, abort, partial setup, and timeout;
* no automatic restart/re-grab and no persistent privilege widening.

Check actual systemd semantics, including applicable startup/runtime/stop/abort timeouts, kill behavior, timer accuracy, notification-based timeout extensions, and dependency/cancellation behavior. Do not assume a nominal timer delay is its observed recovery bound.

Keep recovery independent of the broker’s own event loop. A same-process timer, shell trap alone, mouse-only stop button, or untested TTY shortcut is not sufficient evidence.

Define the covered failure model and residual limitations. Do not promise recovery from arbitrary kernel or machine failure.

### B. Rehearsal before physical input

Specify a device-free rehearsal of the chosen mechanism using a harmless fixture that never opens input or uinput.

Provide exact proposed files/commands, required privileges, expected observations, deadline bounds, abort rules, and cleanup. They are proposals only and must not be executed now.

Cover at least:

* normal completion;
* a stopped/unresponsive fixture;
* a still-running fixture that represents failed forwarding despite liveness;
* loss of the controlling process/terminal;
* recovery setup failure;
* an expired or stale guard that must not affect a new invocation.

Distinguish three claims:

* the external cutoff recovered the test;
* the broker watchdog recovered a hung broker;
* physical input became usable again.

A cutoff firing during a later watchdog trial must not be reported as watchdog PASS. Device-free success does not prove physical recovery.

### C. Production gaps and stage placement

For each confirmed gap, provide the causal failure, recommended correction, precise source/interface impact, and smallest meaningful test:

* RealSink write errors are discarded. Define error propagation and safe disarm without falsely advancing synthetic-state claims or depending on successful writes during recovery.
* Production uses broad passthroughCapabilities. Define justified capability discovery during explicit ARM and preserve all-or-nothing ownership.
* The promised virtual-to-physical LED return path is missing. Address the required I/O direction, permissions, event-loop handling, and failure behavior.
* sd_pid_get_session may reject a legitimate user-manager-launched session app. Resolve the launch/authentication question without replacing authentication with UID-only trust or admitting root, remote, inactive, ambiguous, or wrong-seat clients.

Classify each as:

* required before any physical grab;
* required before complete G4;
* or a separately justified deferred item.

Inspect directly adjacent code only where necessary to establish these invariants. Report unrelated observations separately; do not expand into a full project audit or new architecture.

### D. Concrete execution sequence

Prefer one coherent implementation grant with a few causal stages over many tiny exchanges.

For each proposed stage, name:

* outcome and exact changed-path allowlist;
* repository versus temporary-testbed versus privileged-host effects;
* focused existing tests and genuinely missing causal regressions;
* enter/exit criteria, rollback, and final state;
* evidence owner and any fresh independent review required.

Place independent review proportionately before the first physical grab, considering that the production path and recovery arrangement have not received such acceptance.

Provide a short proposed COOPERATOR procedure for the eventual live trial: prerequisites, visible actions, expected result, deadline, abort, and final inactive/ungrabbed state. Mark it explicitly NOT AUTHORIZED BY THIS PLANNING TASK.

Do not repeatedly uninstall security guards to manufacture test coverage. Preserve input-remapper and accepted device-access boundaries.

Identify contradictory technical-document statements that the implementation must update. Do not reopen M1 acceptance or unrelated milestone decisions.

## Validation and convergence

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: inspect relevant broker tests; do not execute
Affected tests: proposed in the plan
New causal regression: proposed only for named safety evidence gaps
Broad or full suite: not-used
Runtime or testbed: not-used
Independent acceptance: not-required for this planning exchange

Planning PASS means the revision is decision-complete and implementable under a subsequent bounded grant. Future rehearsal/hardware gates do not alone make the plan PARTIAL.

If an essential decision remains unsupported, name the single cheapest missing-evidence probe and its required authority. Do not manufacture evidence, return another broad research request, or repeat the unchanged second-keyboard gate.

No second automatic targeted revision is authorized. Unresolved repetition must include:
Escalation disposition: NEEDS_ORCHESTRATOR_DECISION

## Trace and report delivery

External trace disposition: configured
Trace discovery: https://github.com/cisarik/meta.git ; /home/agile/meta
Trace project key: contextdesk
Trace logical-whole projection identity: g213-contextdeck-input-passthrough-safety
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 12_planning_01.md
Destination path: /home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
Report filename: 12_report_01.md
Prompt persistence owner: COOPERATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

You may write the complete report to that exact path after destination/collision checks, then read it back. Preserve nonempty existing artifacts.

You may also mechanically append the following exact Orchestrator-authored entry once to the existing 00_notes.md in that directory. Preserve all earlier content; do not author additional notes:

---

## 2026-09-12 — AP adoption reconciliation and recovery revision

Orchestrator-authored; Worker is the exact mechanical persister.

Exchange 12/01 reconciled: product 64dd12bbc34c5ab09574d8edc76ebb7bed50af2d adopts AP 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9; four authorized paths changed, runtime unchanged. Prompt/report first-add commit: Meta 2d46b53420d3edfc96cf37ce99f694ec76e2d069. Host observations remain Worker-reported, not direct ChatOrchestrator measurements. G4 remains uncompleted.

## Selected delivery remains manual. Next exchange 12/02 uses the same Grok 4.6 session, High, approximately 250k context, Native Plan Mode required. Artifacts: 12_planning_01.md and 12_report_01.md. One targeted recovery revision is authorized; earlier planning and blocked-acceptance history is retained. No live grab or host mutation is granted.

These persistence exceptions do not authorize product implementation or Meta Git operations. If native controls prevent writes, preserve the complete report and exact notes through chat; report incomplete persistence without bypassing controls or reopening planning.

Begin the formal terminal report exactly:

### Report for ORCHESTRATOR_CHAT

Echo the three coordinates once. Include status, planning disposition and budget, unchanged start/end commit and AP pin, selected design and rejected alternatives, staged allowlists and validation, proposed recovery procedure, facts/assumptions/unknowns, exact remaining human decisions, persistence/readback outcome, and one smallest next implementation step.

Include the standard Orchestration critique, relevant execution issues and pre-existing limitations, exactly one report justification, and authority expiry.

Logical-whole closure: not-closed.
Do not claim implementation, rehearsal, G4, or production acceptance.
Stop after the terminal report.
