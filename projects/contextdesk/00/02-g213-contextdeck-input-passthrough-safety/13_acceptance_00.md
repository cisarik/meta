# AP acceptance prompt — exchange 13/01

You are a **fresh independent Worker**. You did not implement the candidate under review and must not inherit authority or rely on retained context from the previous Worker session. This is the first primary independent acceptance of the ContextDesk M2 input-safety candidate.

## Execution identity

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 13
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: CONTEXTDESK-G4-INDEPENDENT-ACCEPTANCE
Continuity anchor: 12_report_02.md, candidate product HEAD cb72ae0388307b514182efc6936712e3da42cda4, AP pin 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9
Reasoning recommendation: High — this acceptance crosses the physical input, systemd recovery, and security boundaries.
Recommended context capacity: approximately 200–250k tokens
Selected model: Grok 4.6, selected by the COOPERATOR; report actual client/model information only when observable.
Delivery: manual
Independence required: required-fresh-independent
Communication: Slovak progress to the COOPERATOR; English repository documentation and terminal report.
Do not spawn subagents, Task agents, or hidden Workers.
```

Use a genuinely new Worker session. Do not use `continue` on the compacted implementation session. Do not use native Plan Mode. The current complete prompt is the only acceptance authority. A terminal report expires it.

## Acceptance record

```text
Acceptance candidate: cb72ae0388307b514182efc6936712e3da42cda4
Acceptance owner map: ContextDesk M2 input-passthrough-safety acceptance; AP pin 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9
Acceptance allowlist: read-only repository/source/test/docs inspection; read-only host/service/ACL readback; explicitly authorized live G4 broker trial and recovery actions below
Acceptance risk claims: G4 pass-through fidelity; explicit ARM/LEASE boundary; orderly ungrab; kernel close-on-death ungrab; watchdog/cutoff recovery; no stuck modifiers, duplicates, or phantom events; no automatic restart/re-grab; recovery typing; no input-remapper regression
Acceptance control matrix: repository/AP identity; install and G3 preflight; service/static/inactive state; invocation-bound cutoff; source capability and G213 identity; authenticated ARM; normal typing; modifiers; LED return; orderly disarm; cutoff/crash/hang recovery; final inactive/ungrabbed state
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0 before this run; this is the primary fresh acceptance
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none after all mandatory gates pass; if a mandatory claim cannot be observed, preserve it as missing and do not issue acceptance-PASS
Out-of-scope observations: ledger-candidates
```

This is an E3 acceptance envelope. It does not authorize implementation, corrections, publication, deployment, AP updates, or Meta Git writes.

```text
Evidence tier: E3
Evidence tier basis: material production input and recovery behavior, physical-grab trust boundary, and difficult-to-reproduce kernel/systemd failure behavior
Authorized implementation stages: none
Combined implementation envelope: prohibited
Implementation stage gates: not-applicable
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: invocation-bound cutoff plus final disarm/stop/ungrab verification
Activated stricter profile: none
Terminal implementation report point: not-applicable; terminal acceptance report is required
```

## Repository and AP gate

Work only in the canonical checkout:

```text
Repository: https://github.com/cisarik/contextdesk
Working directory: /home/agile/Projects/contextdesk
Canonical checkout: yes
Branch: main
Exact candidate baseline: cb72ae0388307b514182efc6936712e3da42cda4
AP pin required: 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9
```

Before any live action, independently verify the repository root, active branch, exact `HEAD`, remote identity, worktree state, `.ap` gitlink, checked-out `.ap` commit, and AP doctor. The product `HEAD` and `.ap` gitlink must match the exact values above. If the candidate changed, the gitlink differs, the worktree is dirty in an unexplained way, or AP is not strict-pinned and healthy, stop `BLOCKED`.

Read `AGENTS.md`, the README, ROADMAP, the complete M2 documentation, the pinned `.ap/AP.md`, `.ap/AP_WORKER.md`, and `.ap/PROMPT_CONTRACTS.md`. Read the complete `12_report_02.md` from the configured trace checkout if available, plus the relevant architecture, operations, testing, service, broker, application, and test files. Inspect the current commit, not an old local clone. Do not read or expose unrelated private data.

One ordinary `git fetch origin main` is permitted solely to verify the public ref if needed. No other Git write is authorized. Do not stage, commit, push, reset, clean, stash, switch, rebase, amend, restore, or modify the repository. Do not modify Meta.

## Hard safety boundary

This Worker may perform only the read-only checks and the explicitly bounded G4 live trial described below. It may not install packages or files, run `daemon-reload`, enable the service, change udev/ACLs, stop or reconfigure input-remapper, alter OpenRGB/KWin/power/autostart configuration, modify the broker, change the service unit, or create persistent files.

Do not ask the COOPERATOR for a password and do not log credentials. Use `sudo -n` only where a named readback or already-authorized operation requires it. If a command would need an interactive password, stop and report `NEEDS_COOPERATOR_ACTION`; do not weaken permissions or use an ambient alternative.

Do not log ordinary typed text, raw key events, scan codes, device serials, hidraw dumps, screenshots, window captions, or private paths. Reports may contain only bounded status, hashes, counts, semantic test outcomes, and redacted causal errors.

The only non-read-only operations granted by this prompt are the following, and each is conditional on all preceding gates passing: manually start `contextdeck-broker.service` once for the candidate G4 trial; use the documented authenticated LEASE/ARM and DISARM/release paths; arm and cancel the exact invocation-bound cutoff; allow the documented cutoff to kill the matching invocation; and, only when a separate recovery path is available and the documented G4 procedure requires it, issue the named controlled stop/crash/hang signal. The Worker may stop the service for cleanup. These operations apply only to `/usr/bin/contextdeck-broker`, `contextdeck-broker.service`, and the current invocation. They do not authorize enable, restart, reload, daemon-reload, package/udev/ACL changes, arbitrary signals, guessed PIDs, or any other host mutation. A privileged operation must use `sudo -n`; an interactive password request is a hard stop.

## Gate 0 — installation and host preflight

The COOPERATOR-owned §9 install block must already be complete. Verify it before starting the broker. Do not perform the install yourself and do not start the unit if any check is missing.

Verify, using the documented commands and identity-based device resolution:

1. `/usr/bin/contextdeck-broker` exists, is executable, and corresponds to the candidate build/install expected by the repository.
2. `/etc/systemd/system/contextdeck-broker.service` is byte-for-byte identical to `packaging/systemd/contextdeck-broker.service` from the candidate and has the documented mode `0755`.
3. The unit is not enabled and is currently `static/inactive`; capture `LoadState`, `UnitFileState`, `ActiveState`, `SubState`, and the relevant service timeouts without starting or reloading it.
4. The G3 event-node ACLs are identity-resolved from the Logitech G213 USB ancestry and interface numbers, never from remembered `eventN` values. Event nodes have the broker policy and no session-user ACL; G213 hidraw retains the session-user ACL required for lighting; `/dev/port` and i2c policy remain protected; `/dev/uinput` retains its existing mode/group and has the named `contextdeck-broker` read/write ACL.
5. `contextdeck-broker` can read and write `/dev/uinput` through an access check only; this check must not inject events.
6. `input-remapper` remains enabled/active and its G213 preset is unchanged.
7. The service contains the required watchdog and stop/abort limits, `Restart=no`, no `Install` section, no `RuntimeMaxSec`, and no timeout-extension mechanism.

Use read-only `systemctl`, `stat`, `cmp`, `getfacl`, udev identity, and access checks as documented. Do not use `systemctl start`, `enable`, `restart`, `reload`, or `daemon-reload` during this gate. If any precondition fails, preserve the first causal result, report `BLOCKED`, and stop before any live trial.

## Gate 1 — build and static candidate review

Without touching real input or uinput devices, run the repository’s required build and test gates from the candidate checkout:

```text
cmake -S . -B build -G Ninja
cmake --build build
ctest --test-dir build --output-on-failure
systemd-analyze verify packaging/systemd/contextdeck-broker.service
```

Run the repository’s device-free self-tests, including the broker watchdog self-test and the M2 production/IPC/forwarding/acquisition tests, when the candidate documents them. Record exact exit status. A non-zero result is not a PASS.

Review the candidate statically for all of the following:

- `RealSink` write and flush failures are observable, bounded, and fail closed;
- ungrab occurs before virtual-device destruction and the ownership ledger is cleared on every path;
- production capabilities are measured from the exact G213 pair before virtual creation/claim, with `EV_KEY` union, `EV_LED` from if00 only, `EV_MSC`, and no `EV_REP`;
- the virtual uinput descriptor is in the event loop and `EV_LED` returns to physical if00 only;
- LED failure does not strand normal typing;
- authentication retains `SO_PEERCRED`, UID/session/seat/graphical checks, with only the narrow documented fallback;
- no automatic ARM, LEASE, restart, re-arm, or autostart exists;
- no ordinary keylogging or raw-event logging exists;
- systemd timeout/cutoff behavior is invocation-bound and cannot kill a stale or different invocation.

If static or device-free evidence contradicts the report or candidate contract, stop before live access and report `PARTIAL` or `BLOCKED` with the exact contradiction.

## Gate 2 — invocation-bound recovery guard

Before any future explicit ARM, start the installed broker manually through the documented service path and verify that it reaches `READY=1` while remaining disarmed. Do not start it until Gate 0 has passed.

Immediately after the current invocation is known, use the repository’s documented `packaging/systemd/contextdeck-trial-cutoff.sh` helper and PID1-owned transient timer/service. Do not invent an interface or replace it with ad-hoc `kill`, `pkill`, `killall`, guessed PIDs, or a timer detached from the invocation guard.

The guard must be armed after broker start and before ARM with these default semantics:

```text
OnActiveSec=30s
AccuracySec=1us
RandomizedDelaySec=0
Persistent=no
```

Verify that the helper:

- records the exact current `InvocationID`;
- refuses absent, inactive, or mismatched invocation identities;
- re-checks the exact identity immediately before acting;
- uses `systemctl kill --kill-whom=main --signal=SIGKILL` only for the matching unit;
- never restarts or re-arms the broker;
- returns a non-success result on setup/identity failure;
- can be cancelled after normal disarm;
- leaves no stale timer or temporary service.

If timer setup, identity verification, or status readback fails, do not ARM. Report `BLOCKED` and stop. A cutoff kill is a controlled recovery result, not a watchdog PASS.

## Gate 3 — supported authenticated ARM

Use only the product-supported authenticated session path described by the current documentation. Confirm `STATUS` while disarmed, acquire the single lease through the supported session application/diagnostics path, and ARM explicitly. Do not fabricate a raw socket command or bypass authentication.

Before ARM, verify the exact current invocation-bound cutoff is loaded and the service remains the intended candidate. The Worker may not proceed when the lease, peer identity, session identity, or cutoff identity is ambiguous. Do not change input-remapper or add a second keyboard as a prerequisite. A second keyboard, SSH session, or already-reachable TTY is an optional additional recovery route only if one is already available.

## Gate 4 — live G4 acceptance

Perform the following in the smallest safe sequence. Stop immediately on any missing key, duplicate/phantom event, stuck modifier, unexpected grab, service restart, wrong-device selection, cutoff mismatch, or loss of the recovery path. Do not “fix forward” during acceptance.

### 4.1 Identity and normal pass-through

- Confirm the broker selected exactly the Logitech G213 pair by USB ancestry and interface identity. No generic keyboard or remembered event-node number may substitute for this proof.
- With the broker armed, type in a harmless text field using ordinary letters, numbers, punctuation, navigation, function keys, and the supported G213 media controls. Verify one-for-one behavior with no missing, duplicate, delayed, or phantom input.
- Hold and release left/right Shift, Ctrl, Alt, and Super individually and in combinations. Verify that every modifier releases correctly and that no modifier remains stuck.
- Verify that unrelated keyboards/devices were not grabbed and that input-remapper remains enabled with its preset unchanged.
- Do not treat Game Mode or Backlight as software-controlled product behavior; they remain firmware-only/conditional as documented.

### 4.2 LED return path

Use lock-state changes that are safe and visible on the physical keyboard. Verify that virtual `EV_LED` state reaches the physical if00 path, is not sent to if01, and does not disturb normal typing. If the keyboard exposes no reliable visible LED result, record the limitation; do not invent a PASS.

### 4.3 Normal disarm and lease expiry

Use the supported explicit DISARM/release path and then the documented lease-expiry path, one at a time. Verify ungrab-first behavior, balanced synthetic releases where applicable, virtual-device destruction, service health, and immediate normal typing afterward. Cancel the trial cutoff after each normal completion and prove no active stale timer remains.

### 4.4 One-keyboard invocation-cutoff recovery

Start a new guarded invocation only after the normal path is clean. ARM explicitly, then deliberately allow the exact invocation-bound cutoff to expire without re-arming or restarting anything. Verify:

- the timer acted only on the matching invocation;
- the broker was killed and did not restart or re-grab;
- the unit is `inactive/failed` as appropriate, not enabled, and no stale trial timer remains;
- the physical G213 types normally again, including modifiers, after descriptor close;
- input-remapper and unrelated devices remain unchanged.

This is the primary recovery demonstration and must not require a second keyboard or SSH. If the keyboard does not recover, stop and report `BLOCKED` with the first causal status.

### 4.5 Crash/hang and watchdog recovery

Run the documented G4 crash/hang procedure only after the normal and cutoff paths have passed. Use a recovery path that does not depend on the grabbed G213 if one is available. Do not improvise a production hang command. Verify that watchdog expiry or process death leaves `Restart=no`, no automatic re-grab, and a usable keyboard after descriptor close. Include a held-modifier-at-death observation when the documented procedure makes that safe.

If a separate external recovery path is unavailable, do not simulate or claim this live watchdog evidence. Record the claim as missing and classify the result `PARTIAL`; the invocation-cutoff result remains separately identified as controlled recovery, not watchdog PASS.

### 4.6 Final safe state

After every live case, leave the broker stopped/disarmed, ungrabbed, with no virtual device, no active cutoff timer, no enabled unit, no changed ACLs, no input-remapper mutation, and no persistent test state. Confirm normal typing on the G213 and the available recovery path before ending the session.

## Acceptance verdict and stopping rules

Issue `acceptance-PASS` only when every mandatory gate and every required G4 claim has direct evidence and the final safe state is proven. An implementation report, a successful CTest suite, or a successful cutoff rehearsal alone is not acceptance-PASS.

Use `PARTIAL` when the candidate is coherent but a required live claim remains unproven. Use `BLOCKED` when a prerequisite, identity, service, cutoff, authentication, recovery, or safety gate prevents valid acceptance. Preserve the first causal failure and do not rerun unchanged broad gates. Do not make corrections in this session.

The Worker must always record:

```text
Logical-whole closure: not-closed
```

No acceptance result closes the logical whole. The Orchestrator and Cooperator decide the later G4/product transition and residual-risk disposition.

## Terminal report

Begin the report exactly with:

```text
### Report for ORCHESTRATOR_CHAT
```

Use the exact coordinates once:

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 13
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Phase: acceptance
Task identity: CONTEXTDESK-G4-INDEPENDENT-ACCEPTANCE
```

The report must include:

- `status` and exact `phase-qualified result` (`acceptance-PASS`, `PARTIAL`, or `BLOCKED` as applicable);
- requested and directly observed model/client/context/reasoning information, with unknowns kept unknown;
- exact candidate commit, AP pin, branch, repository path, and repository/AP gate results;
- exact files and commits read, and confirmation that no implementation occurred in this fresh session;
- Gate 0 installation, service, ACL, and input-remapper evidence;
- build, CTest, self-test, systemd, static-review, and cutoff-helper commands/results;
- authenticated ARM/LEASE evidence without secrets or raw socket/private data;
- each live G4 case, including pass-through, modifiers, LED return, normal disarm, cutoff recovery, crash/hang/watchdog evidence, and final safe state;
- exact missing evidence and why it prevents a stronger verdict;
- proof of no repository mutation, no package/udev/ACL/service configuration mutation, no autostart, and no unrelated subsystem change;
- residual risks and Cooperator-owned decisions;
- explicit statement that logical-whole closure is `not-closed`;
- one smallest next step and one allowed report justification;
- the required orchestration critique with `MEASURED` and `LEAD` labels;
- at least one near-miss or latent failure mode, classified as pre-existing, introduced, or resolved;
- why one terminal report is sufficient for this exchange;
- authority expiry after the report.

Do not claim that this report was archived or pushed to Meta. The COOPERATOR archives the exact prompt and exact report manually under:

```text
projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
```

Use these trace coordinates:

```text
Prompt filename: 13_acceptance_00.md
Report filename: 13_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: WORKER for the exact terminal report; COOPERATOR archives it
Git publication owner: COOPERATOR
```

After the terminal report, stop. Do not continue autonomously, implement a correction, perform publication, or declare project closure.
