# ContextDesk — live suspend/resume recovery acceptance

## Identity and one bounded outcome

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 22
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Acceptance Worker — one live suspend cycle
Phase: acceptance
Task identity: CONTEXTDESK-AB10491-LIVE-SUSPEND-RESUME
Delivery: manual
Reasoning recommendation: High
Recommended context capacity: approximately 128k tokens; not a provider capacity attestation
Selected model: Cooperator choice; record actual client/model/reasoning only when observable
Evidence tier: E3
Evidence tier basis: live systemd-sleep pre/post hook, active broker stop, real suspend/resume, disarmed conditional restart, client reconnect, and G213 post-resume typing
```

Use a genuinely fresh Worker session. Worker 21 authority is expired. Do not dispatch subagents. Speak Slovak to the Cooperator; write the terminal report in English. Your single outcome is one controlled **suspend** cycle on the installed candidate: prove an independent recovery path, start and ARM the broker once, sample G213, initiate one user-confirmed suspend through the documented logind/ContextDeck path, verify the systemd-sleep hook stopped the active broker before freeze, verify the hook started it once after resume in a disarmed/no-lease state, verify the session app reconnects with STATUS only, and verify the G213 types again. This is a named live acceptance slice, not whole-G4 closure.

**Hard safety gate:** before starting the broker, ARM, or opening/grabbing any physical source, the Cooperator must independently demonstrate either a second physical keyboard operating a prepared local recovery terminal or SSH from another device operating a prepared recovery shell. The route must be capable of issuing exact unit-scoped stop/status readbacks after resume. If neither route is demonstrated, stop before start with `status: BLOCKED` and phase-qualified result `not-applicable`. A mouse, gamepad, G213, cutoff timer, or “SSH should work” is not a substitute.

The recovery route must be prepared before the timed portion. If an SSH connection drops during suspend, reconnect from the same other device after resume and prove the harmless marker/readback again. If the route cannot be recovered after resume, do not improvise with a second start/ARM; use only the pre-agreed emergency owner recovery path and classify the required recovery claim as failed/PARTIAL. Keep a second physical keyboard available as an optional additional safeguard, but do not claim it unless it is independently demonstrated.

Worker 19 already accepted the armed SIGSTOP/watchdog/held-modifier slice. Worker 20 implemented the suspend hook, Worker 21 installed it on this host, and deterministic tests are already evidence. This prompt adds only the missing live host boundary; it does not repeat the watchdog hang harness, cutoff trial, hibernate, or LED/all-control work.

## Exact candidate, installed hook, and bounded continuity

Canonical product checkout: `/home/agile/Projects/contextdesk`; remote `https://github.com/cisarik/contextdesk.git`; branch `main`; expected product `HEAD`:

```text
ab10491c49d0b6574b6953a02935a4664c39d7c2
```

Required AP gitlink and checkout: `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`; `./.ap/ap doctor` must pass. Runtime broker baseline remains `cb72ae0388307b514182efc6936712e3da42cda4`. Public META latest evidence includes Worker 21 deployment report at `978274d8cc04d7212643a8817720a1ee1d770598`. Do not silently retarget to another product/AP commit. If any identity diverges, stop before live operation.

```text
Acceptance candidate: ab10491c49d0b6574b6953a02935a4664c39d7c2
Installed hook: /usr/lib/systemd/system-sleep/contextdeck-broker
Expected hook SHA-256: 91e47888a90f3b2c1853f8bd454f1bdeb342a507efb1084767e09480d4eeac8e
Expected broker SHA-256: 8e80f2d78530b01d9cda4ab77c4ff75d2888055dadce35fbb9483a15651940a6
Expected service SHA-256: 286154ba6f443adced5dc965b0f0c4da2dfae2a44e4f77edf888c6ef96c30503
Acceptance owner map: installed systemd-sleep hook; broker service lifecycle; SessionApplication/BrokerIpcClient reconnect; G213 physical post-resume recovery
Acceptance allowlist: read-only preflight; one owner-operated broker start; one authenticated GUI LEASE/ARM; one real suspend cycle; hook post-start once; one physical pre/post sample; bounded cleanup; exact report preparation
Acceptance risk claims: pre-freeze active stop; no watchdog false abort; conditional post-resume restart; disarmed/no-lease/no-grab restart; no silent re-ARM; session reconnect; G213 usable after resume; final inactive cleanup
Acceptance control matrix: recovery proof; installed hook identity; pre-start inactive; pre-sleep active/armed; hook stop journal; suspend/resume; hook start journal; post-resume STATUS/no-ARM; G213 typing; final cleanup
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1 (Worker 19 named armed slice is inherited context, not reused as live suspend evidence)
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: live suspend/pre-post hook execution and post-resume broker/client/keyboard recovery
Out-of-scope observations: hibernate/hybrid-sleep, cutoff, SIGSTOP watchdog, held-modifier-at-death, LED return, all-control fidelity, input-remapper changes, autostart, automatic re-ARM, logical-whole closure
```

Focused reading only: applicable `AGENTS.md`, pinned AP acceptance/report contracts, Worker 19 acceptance report, Worker 20 implementation report, Worker 21 deployment report, current `docs/operations.md` suspend section, `docs/testing-m2.md` live-suspend section, the installed hook/service, and the small session-app broker entrypoints. Do not rerun the full CTest suite or reread the whole archive.

## Preflight and physical safety

Before any live operation verify product root/remote/branch/exact `HEAD`, clean source worktree (ignored build output allowed), no Git lock/operation, matching `.ap` gitlink and checkout, AP doctor, installed hook type/owner/mode/hash, installed broker/unit hashes/equality from Worker 21, service `static/inactive/dead`, `MainPID=0`, empty invocation, `NeedDaemonReload=no`, no broker process, no `/run/contextdeck`, no `/run/contextdeck-sleep`, no ContextDeck virtual device, no trial/cutoff units, and unchanged input-remapper/udev/ACL policy. Read-only product `git fetch origin main` is allowed; no product or META Git mutation is authorized.

Do not open event or uinput nodes during preflight. Resolve G213 by USB ancestry/interface; never copy event numbers, serials, raw events, or key names into the report. Verify the hook is a regular non-symlink executable at exactly `/usr/lib/systemd/system-sleep/contextdeck-broker` with SHA-256 `91e47888a90f3b2c1853f8bd454f1bdeb342a507efb1084767e09480d4eeac8e` and `/bin/sh -n` success. Do not modify the hook, service, power policy, hibernate mask, input-remapper, udev/ACLs, OpenRGB, KWin, or autostart.

Prepare the verified candidate `build/contextdeck` session app and an unsaved Kate/text buffer. Rehearse the exact explicit ARM path while the broker is inactive: tray or Diagnostics **`Arm G213 pass-through…`** → Qt dialog **`Arm G213 pass-through now?`** → **Yes/OK**, then cancel and return to disarmed state. Rehearse the documented suspend path without executing it: ContextDeck tray **`Suspend…`** → confirmation → **Yes** through logind. If the app's suspend action is unavailable, use only the documented logind-compatible owner path agreed before the live window and record that substitution; never write `/sys/power/state`.

Confirm the laptop is awake and the Cooperator is seated for one short interval. Do not deliberately suspend, hibernate, lock, switch power profiles, or leave the broker running unattended before the recovery route and all observers are ready. Do not change power configuration to prevent or force sleep. Hibernation is out of scope; report 21 recorded `hibernate.target` masked and this prompt must not alter it.

## Mandatory independent recovery proof

Choose one primary route and prove it **before broker start and before any ARM**:

- **SSH:** from another device, execute a harmless marker and `systemctl show -p ActiveState --value contextdeck-broker.service`; obtain successful output; prepare a shell capable of exact unit-scoped stop/status/readback commands after resume. Do not record host keys, address, password, serial, or private environment. Before the suspend cue, establish how the same device will reconnect if the SSH transport drops during sleep.
- **Second physical keyboard:** use the other keyboard to reach a prepared local terminal, type a harmless marker, and obtain the same read-only unit-state output. Keep it connected and reachable during and after the cycle. A mouse, gamepad, or G213 is not sufficient.

Record only semantic readiness (`SSH_READY` or `SECOND_KEYBOARD_READY`), not marker text. The route proof grants no unrelated host access.

## Positive runtime authority — one live suspend cycle

The Worker must prepare every instruction, observer, and recovery command before the timed portion. No model round-trip may be needed while the broker is armed or the machine is returning from sleep. The Cooperator owns the physical confirmation and may abort immediately if the keyboard or GUI becomes unsafe.

1. From `static/inactive/dead`, start `contextdeck-broker.service` exactly once. Verify `active/running`, fresh nonzero `InvocationID`, nonzero `MainPID`, `armed=0`, `lease=none`, no virtual device before ARM, and watchdog settings. Do not enable, restart, reload, or start it again manually.
2. Use the already-rehearsed GUI action for exactly one authenticated `LEASE`/`ARM`. Require `OK ARMED` or authenticated STATUS `armed=1`; a transient client label or `OK LEASE` alone is insufficient. Confirm a virtual device exists and have the Cooperator type a short harmless pre-suspend sample in the unsaved buffer. Do not save or record its content. Release all keys and modifiers before requesting suspend; this task does not test held-modifier death.
3. Capture a final pre-suspend marker and the exact active `InvocationID`/`MainPID`. Confirm the recovery route remains available. Initiate **one** real `suspend` through the rehearsed ContextDeck/logind path. Do not initiate hibernate, hybrid-sleep, suspend-then-hibernate, or a second attempt. No further model interaction is allowed until the system is awake and the prepared recovery path is usable.
4. Before the machine freezes, the installed hook must log `contextdeck-sleep class=stop` and systemd must stop the active broker. Evidence must show the unit left active state before/at sleep, the armed acquisition was torn down, and no watchdog timeout caused the death. The expected transition is an orderly hook stop, not a `Result=watchdog` or manual kill. If the hook does not run or the broker remains active into the freeze, classify the pre-sleep claim failed/PARTIAL and use the recovery route only for bounded safety.
5. After resume, re-establish the primary recovery route if necessary and prove the harmless marker/unit readback again. Verify the hook logged exactly one `contextdeck-sleep class=start`, consumed its valid marker, and performed exactly one post-resume start. Verify a fresh `InvocationID`, `ActiveState=active`, `SubState=running`, `MainPID>0`, `armed=0`, `lease=none`, no virtual device, and no active `/run/contextdeck-sleep` marker. The post-resume start is expected hook behavior, not a second manual start and not autostart.
6. Verify the session app reconnects through its existing bounded retry path and receives STATUS only. Require evidence of connected/status-only state and absence of post-resume `LEASE`/`ARM` until a user action. Do not click ARM after resume in this slice. If the app does not reconnect, preserve the failure and do not restart the app or broker to make the result pass.
7. Have the Cooperator type a short harmless sample with the G213 after resume. Confirm no stuck modifier, duplicate, phantom, or silent keyboard is observed. This physical post-resume G213 result is required; typing only on the recovery route is not keyboard-recovery evidence. Capture no text, screenshot, raw event, serial, or key name.
8. Clean only owned resources: close the unsaved buffer without saving, stop the session app only if it was started for this trial, and use the verified external route for one final `systemctl stop` of the hook-started broker. Do not manually start or ARM again. Verify final `static/inactive/dead`, `MainPID=0`, no process/socket/virtual device, no sleep marker, no trial/cutoff unit, `Restart=no`, `NRestarts=0`, unchanged input-remapper/udev/ACL policy, and installed hook/broker/unit hashes unchanged. Release sudo with `sudo -k`.

If the route drops and cannot be re-established after resume, or if the G213 remains unsafe, the Cooperator may perform only the prepared bounded stop/kill recovery for the exact unit. Such fallback cannot produce live-suspend `PASS`. Unplug/replug is last-resort owner recovery and must be reported as failure of automatic recovery. Do not run another suspend or another start/ARM.

## Result and report persistence

Use status `PASS` and phase-qualified result `acceptance-PASS` only when the external recovery path was proven before start/ARM and after resume, the broker was genuinely armed before one real suspend, the hook stopped it before freeze without watchdog abort, the hook started it exactly once after resume, the new invocation was disarmed/no-lease/no-virtual-device, the session app reconnected without automatic ARM, post-resume G213 typing succeeded, and final cleanup passed. Otherwise use `PARTIAL`/`BLOCKED` with `not-applicable`. Always state `Logical-whole closure: not-closed`; do not claim full G4, production readiness, autostart, hibernate support, or automatic re-ARM.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 22_acceptance_00.md
Destination path: /home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
Report filename: 22_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: this WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

You are explicitly authorized and required to create `/home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/22_report_00.md` before terminal notification for PASS, PARTIAL, or BLOCKED. This is exact report-file preparation only; no META add/commit/push and no historical rewriting. Verify physical parents, real directory, symlinks, and collision; preserve any existing/nonidentical file and never choose an alternate name. If persistence fails, state it and provide the complete report as fallback; never claim saved bytes without complete readback.

The saved report must begin exactly `### Report for ORCHESTRATOR_CHAT`, echo this prompt's one coordinate set, include candidate/AP/hook identities, external recovery proof before and after resume, before/after unit state and InvocationID/MainPID, exact suspend mode, pre-hook stop and post-hook start evidence, watchdog/no-watchdog outcome, ARM/no-auto-ARM/reconnect outcomes, physical pre/post samples without content, marker consumption, recovery/cleanup and privilege attribution, unchanged policy/runtime, Git actions, missing evidence, one smallest next step, exactly one report justification (`new-evidence` or `changed-external-state`), compact `Orchestration critique` with `MEASURED`/`LEAD` (`none` allowed), resolved/pre-existing failures including the hibernate mask if relevant, `Logical-whole closure: not-closed`, and authority expiry. Read the report back completely before notifying the Cooperator. The Cooperator archives this exact prompt/report pair after it exists.
