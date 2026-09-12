# AP implementation prompt — exchange 12/03

You are the same Worker who completed exchange `12/02`; its terminal planning report is `12_report_01.md`. That planning authority has expired. This document is the complete renewed implementation grant for the next exchange.

## Execution identity

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 12
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: CONTEXTDESK-M2-RECOVERY-CUTOFF-AND-PRODUCTION-SAFETY
Continuity anchor: 12_report_01.md, exchange 12/02, product HEAD 64dd12bbc34c5ab09574d8edc76ebb7bed50af2d, AP pin 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9
Reasoning recommendation: High — this work changes failure behavior at the input and systemd boundaries.
Recommended context capacity: approximately 250k tokens
Selected model: Grok 4.6, selected by the COOPERATOR; report actual client/model information only when observable.
Delivery: manual
Internal delegation posture: not-used
Independence required: no for implementation; a fresh independent review is required before any physical grab.
Communication: Slovak progress to the COOPERATOR; English repository documentation and terminal report.
Do not spawn subagents, Task agents, or hidden Workers.
```

Confirm that you are operating in the same healthy Worker session. Do not use native Plan Mode. Work directly from this grant, while still recording decisions and evidence in the repository and in the terminal report.

## Planning record

```text
Planning cycle: targeted-revision
Targeted revision basis: new-repository-or-external-evidence
Changed decision boundary: one-keyboard recovery plus production prerequisites before the first physical grab / full G4
Preserved unaffected decisions: G213-only; M1 accepted history; G1 firmware-only exclusions; pass-through-only; isolated broker; narrow device access; explicit authenticated ARM; all-or-nothing; ungrab-first; unchanged input-remapper; no unproven autostart
Automatic targeted revisions used: 1
```

The planning decision from `12_report_01.md` is accepted: the second keyboard or SSH path remains a valid fallback, but it is not required for the first safe recovery demonstration. Use the existing watchdog plus an invocation-bound systemd cutoff timer. The default recovery window is **30 seconds**; keep the implementation configurable in the documented range 20–45 seconds if the existing design makes that appropriate.

## Repository and history anchors

Work only in the canonical ContextDesk checkout:

```text
Repository: https://github.com/cisarik/contextdesk
Working directory: /home/agile/Projects/contextdesk
Canonical checkout: yes; verify before editing
Branch: main
Baseline product HEAD: 64dd12bbc34c5ab09574d8edc76ebb7bed50af2d
Baseline parent/reference: 24305864f54d7161048041c2e5309aa8a0f8fb1a
Baseline subject: docs: adopt AP 0cf2cff and reconcile M1/M2 root state
AP pin: 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9
Meta destination for report: projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
```

Before editing, verify the repository root, branch, `HEAD`, clean worktree, remote, AP pin, and that no Git operation is active. Preserve any pre-existing user changes. Never use `reset`, `clean`, `stash`, `switch`, `rebase`, `amend`, force push, or destructive history rewriting. Do not modify the Meta repository from the Worker checkout.

## Required reading

Read the applicable `AGENTS.md` files first. Then read the ContextDesk README, ROADMAP, the pinned AP instructions, the complete `12_report_01.md`, and the architecture, operations, testing, build, and service documentation relevant to this task. Inspect the CMake configuration, current broker/application sources, existing tests, service unit, and matching systemd, libevdev, libudev, and `sd_*` API documentation. Use the repository’s current conventions. Do not reread the entire unrelated project archive or reopen unrelated milestones unless needed to resolve an actual ambiguity.

The Worker must report the exact files and authoritative commits actually read. Do not claim to have read a file or commit that was not observed in this session.

## Scope and hard safety boundary

This grant covers two sequential local implementation slices:

1. **R1 — production safety prerequisites in code and tests.**
2. **R2 — the invocation-bound cutoff helper, service limits, documentation, and a harmless device-free rehearsal.**

The R1 and R2 slices may each have at most one local commit. Push only ordinary fast-forward commits to `origin/main`, after verifying the remote and branch. If a gate fails, stop and report the failure; do not broaden scope.

Allowed R1 paths:

- `src/broker/**`
- `src/app/**` only where the authentication/error state is directly affected
- named relevant test files and test fixtures
- CMake/build files only when required to build the changed tests

Allowed R2 paths:

- the relevant systemd service unit
- a new `packaging/systemd/contextdeck-trial-cutoff.sh` helper and its tests/fixtures
- operations documentation sections 6–9
- M2 testing/rehearsal documentation
- architecture/lifecycle/recovery documentation directly describing this mechanism
- CMake/build files only when required by the above tests

Do not install the broker, run `daemon-reload`, enable/start/restart/reload any broker service, ARM or LEASE a live session, open input or uinput devices, perform a physical grab, change udev rules/packages/ACLs/input-remapper/OpenRGB/KWin/power/autostart configuration, or alter unrelated product behavior. Do not use the second keyboard or SSH as a prerequisite. R2 fixtures may use temporary systemd user units/timers only; they must be harmless, device-free, and contain no broker/device references. Remove every temporary fixture after rehearsal, including failure paths.

Do not put secrets, raw key events, device serials, screenshots/captions, or unnecessary timing traces into Git or the report.

## R1 implementation requirements

Implement and test all four production gaps below. Keep the existing G213-only policy, all-or-nothing acquisition, explicit authentication, isolated broker, pass-through-only behavior, ungrab-first cleanup, and unchanged input-remapper policy.

### 1. Fail-closed sink writes

Make the sink interface expose the result of `libevdev_uinput_write_event` and the required synchronization/flush operation as a boolean or an equivalent observable status. A runtime forwarding failure must produce a bounded, documented `sink-write-failed` error and safely disarm the session.

The failure path must ungrab physical sources before destroying the virtual device. Cleanup writes are best effort only; clear the ownership ledger and close/destroy every owned resource even when cleanup writes fail. Do not retry indefinitely, call `EXTEND`, or log raw input data. Add causal fake-sink tests proving the error, ungrab-first ordering, ledger clearing, and resource cleanup.

### 2. Measure production capabilities before claiming devices

For the exact G213 pair, open both source devices without grabbing, verify their identity, and measure the actual capability union. The production capability set must include the measured `EV_KEY` union, `EV_LED` from if00 only, and `EV_MSC`; it must not include `EV_REP`. Create the virtual device only after validation and capability measurement, then claim/grab the physical sources.

Any discovery, identity, open, measurement, virtual-device creation, or claim failure must close all already-open resources and leave no partial virtual device or grab. Update tests to prove ordering, measured capability bits, rejection of the wrong pair, and no virtual device on invalid input.

### 3. Return virtual LED state to the physical keyboard

Open the physical source path in the mode required for writing LED events. Expose the virtual uinput file descriptor to the existing event loop. Forward `EV_LED` events received from the virtual device to the physical **if00** source only; do not send them to if01. A setup/write failure before a grab must close all resources and abort safely.

A runtime LED write failure must be observable and bounded but must not strand normal typing or disarm an otherwise healthy pass-through session. Add fake-device tests for if00 routing, if01 exclusion, setup failure, and runtime LED failure.

### 4. Narrow session-authentication fallback

Retain the existing `SO_PEERCRED` checks, positive peer PID, non-root peer UID, and session UID match. The current `sd_pid_get_session` path must continue to be used first. Add a narrow fallback only for “no session”/equivalent lookup errors where the application was launched from a user manager and the peer PID has no directly discoverable session.

The fallback must enumerate `sd_uid_get_sessions` and inspect every candidate. Accept exactly one eligible active local graphical seated session (Wayland or X11 as supported by the current contract). Reject zero candidates, ambiguity, inactive sessions, remote sessions, wrong seat, non-graphical/unsupported session type, UID mismatch, and root. Do not replace session authentication with a UID-only check. Add tests for the direct-session path, valid fallback, each rejection, and ambiguity.

## R1 verification gate

Run the focused tests for forwarding, acquisition, production capability measurement, IPC/authentication, and watchdog/error handling. Run the complete CTest suite and repository self-tests that do not require real devices. Review the changed source statically for fail-closed cleanup, no raw event logging, no unbounded retry, and correct ordering. Check the diff and allowlist. Do not access real input/uinput devices. Record commands, results, and any environment limitations in the report.

If all R1 gates pass, create the single R1 commit with a precise message and push it using a normal fast-forward push. If they do not pass, do not start R2; report the exact failing gate and stop.

## R2 implementation requirements

### Service unit limits

Pin the relevant broker service unit to the intended safety behavior:

- retain `Type=notify`
- retain `WatchdogSec=2s`
- set `TimeoutStopSec=5s`
- set `TimeoutAbortSec=5s`
- retain `Restart=no`
- retain `NotifyAccess=main`
- retain `LimitCORE=0`
- retain `RuntimeDirectoryMode=0755`
- keep the unit without an `Install` section unless the existing contract explicitly requires otherwise
- do not add `RuntimeMaxSec`
- do not use `EXTEND_TIMEOUT_USEC` or any equivalent extension mechanism

### Invocation-bound cutoff helper

Add `packaging/systemd/contextdeck-trial-cutoff.sh` (or the repository’s equivalent path if current conventions require it). It must arm a PID1-owned transient timer/service only for the current broker invocation, after the broker has started and before any future ARM action.

The helper must:

- take the exact broker service/unit and expected `InvocationID` as explicit inputs or obtain them from a clearly documented, race-safe query;
- use a transient timer with `OnActiveSec=30s`, `AccuracySec=1us`, `RandomizedDelaySec=0`, and `Persistent=no` by default;
- query the live unit’s current `InvocationID` and refuse to act when it is absent, inactive, or different from the expected value;
- make the timer service re-check the exact `InvocationID` immediately before acting;
- use `systemctl kill --kill-whom=main --signal=SIGKILL` against the exact unit when the guard matches;
- never use `pkill`, `killall`, a guessed PID, or a stale unit name without an invocation guard;
- never restart or re-arm the broker automatically;
- print only actionable state and status, without secrets or raw input data;
- leave setup failure as “do not ARM” and return a non-success status.

Implement stale-guard, missing-unit, inactive-unit, normal-completion, and shell-loss handling. The timer must be cancellable after a normal disarm and before stopping the broker. Include a status path that proves which invocation was guarded.

### Documentation

Update the operational and lifecycle documentation to describe this exact order:

1. Start the broker manually and confirm it is disarmed.
2. Read and record the current invocation identity.
3. Arm the transient cutoff with the exact invocation identity and verify that the timer is loaded with the intended 30-second parameters.
4. Only after that may a future explicit authenticated ARM be attempted.
5. On normal completion, disarm, cancel the cutoff, then stop the broker.
6. If the broker hangs or the invoking shell disappears, the watchdog/cutoff path kills only the matching invocation.
7. If timer setup, identity verification, or any prerequisite fails, do not ARM.
8. Clean up the timer and all temporary state.
9. The final state must be statically and operationally verifiable: broker inactive or safely disarmed, no grabbed physical device, no stale virtual device, no active trial timer, and unchanged input-remapper state.

Document that the second keyboard or SSH remains a valid optional recovery path. State the PID1/systemd, kernel, machine-power, and session limitations. Clearly distinguish watchdog expiry, invocation-bound cutoff expiry, and physical usability. A cutoff kill is a controlled recovery event and must not be reported as a watchdog PASS.

### Device-free rehearsal

Create a harmless temporary fixture with a unique nonce and `Type=notify`; it must not reference the broker, input devices, uinput, or production configuration. Exercise and record these cases:

- normal completion before the cutoff;
- an intentionally stopped or exited fixture;
- a live-broken/hung fixture;
- invoking-shell loss;
- timer/setup failure;
- stale or mismatched invocation guard.

For each case record only semantic state, systemd status, invocation identity, exit result, cutoff action, and cleanup result. Do not record raw input or secrets. Remove all fixture units, timers, and temporary files in every case and verify that none remain.

## R2 verification gate

Run focused helper tests and the full device-free rehearsal. Run `systemd-analyze verify` on the production unit and temporary fixtures, shell syntax checks, the complete CTest/self-test suite that does not require real devices, and a final allowlist/diff review. Confirm in read-only checks that the broker is not installed, started, armed, leased, or connected to real input/uinput devices. Confirm that unrelated subsystems and input-remapper behavior remain untouched.

If all R2 gates pass, create the single R2 commit with a precise message and push it using a normal fast-forward push. If a gate fails, report the exact failure and do not attempt a physical recovery demonstration.

## Transition to independent review

After both R1 and R2 are committed and pushed, stop before any physical grab or live G4 trial. A fresh independent Worker/reviewer must review the combined diff, tests, service semantics, cutoff guard, cleanup ordering, and documentation. This current Worker is not independent for that review. Do not perform G4, LEASE, ARM, live device access, or physical usability testing in this exchange.

## Terminal report and persistence

Write the complete terminal report in English. Use the exact exchange coordinates once:

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 12
Worker exchange ordinal: 03
Worker session target: current-worker-session
Phase: implementation
Task identity: CONTEXTDESK-M2-RECOVERY-CUTOFF-AND-PRODUCTION-SAFETY
```

The report must include:

- actual status and phase;
- exact product commits, AP pin, repository path, branch, and push results;
- files read and files changed;
- R1 and R2 allowlists and proof of no out-of-scope edits;
- implementation details for all four R1 gaps;
- focused, full, static, syntax, systemd, and rehearsal test commands/results;
- all six rehearsal cases and cleanup evidence;
- explicit proof that no broker install/start/reload/ARM/LEASE/grab and no real device access occurred;
- proof that unrelated input-remapper and other subsystems are untouched;
- remaining risks and limitations;
- explicit statement that G4 and the independent review were not performed;
- the next authorized transition: fresh independent review before any physical grab;
- an orchestration critique using `MEASURED` and `LEAD` labels;
- at least one near-miss or latent failure mode discovered;
- classification of each issue as pre-existing, introduced, or resolved;
- why one terminal report is sufficient for this exchange;
- closure state: the implementation exchange is complete only if its gates pass, while the overall objective remains open until independent review and separately authorized live G4;
- authority expiry: this grant ends after the report is complete.

Use the following persistence coordinates in the report:

```text
Downloadable prompt filename: 12_implementation_02.md
Report filename: 12_report_02.md
Prompt persistence owner: COOPERATOR
Report persistence owner: WORKER (prepare the exact file only if it is absent or empty; preserve an existing non-empty file and report the collision)
Git publication owner: COOPERATOR
Archival transition: wait for the COOPERATOR to persist/push the report and issue the next manual dispatch
Meta destination: projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
```

Do not modify Meta Git or claim that the report was published there. The COOPERATOR will persist and push the prompt/report according to the AP protocol. After producing the report and any required repository commits, stop and wait for the next manual dispatch.
