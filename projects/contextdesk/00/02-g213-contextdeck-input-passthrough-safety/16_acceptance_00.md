# ContextDesk — physical pass-through with independently verified recovery

## Identity and one bounded outcome

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 16
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Acceptance Worker — physical ARM with external recovery path
Phase: acceptance
Task identity: CONTEXTDESK-CB72AE0-ARM-PASSTHROUGH-RECOVERY
Delivery: manual
Reasoning recommendation: High
Recommended context capacity: approximately 128k tokens; not a provider capacity attestation
Selected model: Cooperator choice; record actual client/model/reasoning only when observable
Evidence tier: E3
Evidence tier basis: physical input grab, pass-through, and recovery after matching-invocation process death
```

Use a genuinely fresh Worker session. You did not implement or deploy the candidate, and Worker 14/15 authority is expired. Do not dispatch subagents. Speak Slovak to the Cooperator; write the terminal report in English. Your single outcome is a controlled physical trial of the unchanged `cb72ae0388307b514182efc6936712e3da42cda4`: independently verify an external recovery path, perform one explicit ARM, sample G213 pass-through, let the existing invocation-bound cutoff kill the matching broker invocation, and verify that the G213 works again. This is one acceptance slice, not whole-G4 closure.

**Hard safety gate:** do not start the broker, ARM, or open/grab any physical source until the Cooperator has independently demonstrated either (a) a second physical keyboard can operate a prepared local recovery terminal, or (b) SSH from another device can operate a prepared recovery shell. “The keyboard is plugged in”, “SSH is configured”, or “I could probably recover” is not evidence. If neither path is available and demonstrated, stop before starting anything with status `BLOCKED` and phase-qualified result `not-applicable`.

This gate is a correction to the previous Worker 15 prompt, which incorrectly called the independent path optional. The Cooperator's safety decision remains authoritative. The 45-second cutoff only limits a matching systemd invocation; it is not a substitute for an independently usable recovery path.

## Verified continuity and focused sources

Product checkout: `/home/agile/Projects/contextdesk`; remote `https://github.com/cisarik/contextdesk.git`; branch `main`; candidate `cb72ae0388307b514182efc6936712e3da42cda4`. Required AP gitlink and checkout: `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`.

META checkout: `/home/agile/meta`; remote `https://github.com/cisarik/meta.git`; trace directory `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/`. Public META `9aece75407e4282cde111c2531dc315e85badb58` contains the exact 15 prompt/report pair and the delegated notes entry. Worker 14 reports `deployment-PASS`. Worker 15 reports `PARTIAL`: matching 45-second cutoff killed an unarmed invocation; no `OK ARMED`, physical sample, or grab-recovery evidence. The Cooperator's install output corroborates Worker 14's installed identity. These are routing evidence, not a fresh host observation.

Read applicable product `AGENTS.md`, the pinned AP `AP.md`, `AP_WORKER.md`, and `PROMPT_CONTRACTS.md`; the exact 14/15 reports; operations §6 verification and §7–8 recovery/IPC; `docs/testing-m2.md` cutoff and G4 distinctions; the service and cutoff helper; and the small client/UI entrypoints needed to identify the exact ARM action. Do not reread the whole archive or rerun the unchanged full test pack. Do not modify product or AP, and do not modify META except for the exact report-file preparation explicitly granted below.

```text
Acceptance candidate: cb72ae0388307b514182efc6936712e3da42cda4
Acceptance owner map: operations §7–8; testing-m2 G4 distinctions; systemd cutoff helper; this prompt's fixed physical claims
Acceptance allowlist: read-only repository/host readback; one Cooperator-owned broker start; one external-recovery-gated authenticated LEASE/ARM; one matching-invocation cutoff; physical sample and recovery; exact report preparation
Acceptance risk claims: external recovery path independently usable; explicit ARM only; sampled pass-through; matching SIGKILL recovery; no automatic restart/re-grab; unchanged input-remapper and final inactive state
Acceptance control matrix: recovery gate; pre-ARM disarmed state; OK ARMED; physical sample; cutoff-kill identity; post-death G213 recovery; final cleanup
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: genuine ARM, sampled physical forwarding, and typing recovery after grab and matching-invocation death
Out-of-scope observations: watchdog-specific failure, held-modifier-at-death, LED-return pack, all-control fidelity, autostart, logical-whole closure
```

This is new evidence after the installation-state change, not a reset of the prior broad primary audit. Do not treat Worker 15's cutoff as ARM or pass-through evidence, and do not rerun the trial if any step is late or fails.

## Preflight and recovery-path proof

Verify the physical product/AP roots, remotes, branch, exact HEAD, clean source worktree, no active Git operation, matching `.ap` gitlink/checkout, and `./.ap/ap doctor`. One ordinary product `git fetch origin main` is allowed if needed to verify the public ref; no META Git operation or other META mutation is authorized except the exact report-file preparation explicitly granted at the end of this prompt. Preserve unexplained owner work and stop.

Verify installed identity without starting the unit: regular non-symlink `/usr/bin/contextdeck-broker` mode `0755`, SHA-256 `8e80f2d78530b01d9cda4ab77c4ff75d2888055dadce35fbb9483a15651940a`; regular non-symlink service mode `0644`, SHA-256 `286154ba6f443adced5dc965b0f0c4da2dfae2a44e4f77edf888c6ef96c30503`; candidate `cmp` equality; `static/inactive/dead`, `MainPID=0`, no pending reload, correct fragment/drop-ins, and `Restart=no`, `WatchdogSec=2` in the file, `TimeoutStopSec=5`, `TimeoutAbortSec=5`, `RuntimeDirectoryMode=0755`, no `RuntimeMaxSec` or `[Install]`. Inactive `WatchdogUSec=infinity` and `is-active` rc 3 are documented inactive behavior.

Read policy metadata by G213 USB ancestry/interface, not remembered node numbers: broker owns the event-node grant without session-user event ACL; hidraw and uinput seat permissions remain; `user:contextdeck-broker:rw-` exists on `/dev/uinput`; input-remapper remains enabled/active and is not changed. Fresh owner access checks may use `test -r`/`test -w` only. Do not open event or uinput nodes during read-only preflight.

Prepare the verified candidate `build/contextdeck` session app and an unsaved text buffer before the live window. It must be the candidate app, not an unknown stale process. If a build is required, build only the existing target using the documented clean-PATH route; no install and no full test rerun. Do not save the buffer, log its contents, capture screenshots, or expose window captions. A stale running app is owner state: quit/relaunch only with explicit owner control and preserved work.

### Mandatory independent recovery proof

Choose exactly one route and keep it available throughout the trial:

**Second physical keyboard route.** With the broker inactive and G213 untouched, the Cooperator uses the other keyboard to reach a prepared local terminal (or a prepared terminal already focused by that keyboard), types a harmless marker such as `W16-RECOVERY-READY`, and executes a harmless read-only command such as `systemctl show -p ActiveState --value contextdeck-broker.service`. The Worker observes the successful marker/output. The second keyboard must remain connected and reachable; do not count a gamepad, a mouse, or the G213 itself.

**SSH route.** From a different device, the Cooperator opens SSH to the target as the normal owner, executes a harmless marker and the same read-only unit-state command, and leaves that shell available. The Worker records only successful reachability and bounded state, never host keys, passwords, IPs, serials, or environment dumps. An SSH connection that cannot execute the named recovery/readback commands is not an independent path.

The route proof must happen before broker start and before any cutoff timer. Prepare the exact owner recovery commands in that route, but do not execute a stop/kill yet. If the route drops before ARM or cannot be used from the recovery path, stop without starting/arming a second time. A route proof does not grant arbitrary host access or authorize unrelated commands.

## Positive runtime authority — one invocation only

After every preflight and the hard recovery gate pass, the Cooperator may execute only this bounded sequence:

1. Start `contextdeck-broker.service` exactly once from `static/inactive`, with no enable/restart/reload/daemon-reload. Verify `active/running`, a fresh `InvocationID`, `armed=0`, `lease=none`, and no virtual device before ARM.
2. Rehearse the exact UI path while the broker remains disarmed: tray or Diagnostics button **`Arm G213 pass-through…`**, then Qt confirmation dialog **`Arm G213 pass-through now?`**, then **Yes/OK**. This means a GUI confirmation, not a terminal command, not restarting ContextDeck, and not entering a sudo password. Cancel the rehearsal and return to the disarmed state. Do not click twice during the timed attempt.
3. Arm the existing system-manager helper exactly once with `--timeout=45 arm contextdeck-broker.service <exact-current-InvocationID>`. Verify `OnActiveUSec=45s`, `AccuracySec=1us`, `Persistent=no`, `RandomizedDelayUSec=0`, exact unit/invocation guard, and active timer. Do not use `--user`, replace the helper, extend the timer, or insert another model round-trip after the GO cue.
4. Once the timer's local success marker is printed, the Cooperator immediately confirms the already-rehearsed GUI dialog once. This causes the existing authenticated session app to make one LEASE/ARM attempt. Keep the external recovery route available. Require `OK ARMED` or authenticated STATUS `armed=1`; the client's transient `armed` label after `OK LEASE` is insufficient. The Worker must not ask the Cooperator to discover controls, compose commands, or make a new safety decision during the 45-second window.
5. After genuine `armed=1`, the Cooperator samples ordinary typing in the unsaved buffer, a short repeat, and a modifier-assisted edit, then releases every key well before the deadline. Do not type into a shell, save the sample, or intentionally hold a modifier at death. The Worker records only semantic success/failure, never characters or raw events.
6. Let the existing timer expire and kill only the exact matching invocation. Capture `cutoff-kill`, PID1/unit result, and no-restart evidence. Do not classify this event as a watchdog PASS. If the timer skips, ARM never succeeds, or another path ends the invocation, report that exact outcome and do not rerun.
7. After broker death, the Cooperator types a short harmless sample again in the same unsaved buffer using the G213. Confirm that input returns and no obvious stuck modifier/duplicate/phantom behavior is seen. If the G213 remains silent, use the pre-verified second keyboard/SSH route only for bounded matching-identity recovery/readback; do not claim recovery unless post-death G213 typing is actually observed. Unplug/replug is last-resort owner recovery and must be reported as a failure of automatic recovery, not hidden.
8. Clean only owned runtime resources: exact cutoff `cancel` path, temporary observers, the owned session app, unsaved buffer, and resulting unit failed marker after causal evidence. Verify no broker process, no ContextDeck virtual device, no active cutoff timer/service, `static/inactive/dead`, `MainPID=0`, no restart/re-grab, unchanged input-remapper/policy, and unchanged installed hashes. Never start or ARM a second time.

The Worker must prepare all explanatory instructions, GUI rehearsal, observation, and recovery commands before the cutoff is armed. One short owner block at a time is permitted, with neutral directory, exact system command paths, fail-closed checks, markers, exit codes, and safe abort. Privilege is Cooperator-owned: OS password prompt only, same-terminal `sudo -v`/`sudo -n true` when needed, then `sudo -k`; no password in chat, keep-alive, sudoers change, heredoc-heavy script, guessed PID, `pkill`, `killall`, or command from a different invocation. Missing Worker sudo timestamp does not block an already-authorized owner route.

No package/udev/ACL/service-file changes, source edits, AP/META Git writes, OpenRGB/KWin/power/input-remapper changes, autostart, lease-expiry experiment, separate watchdog/SIGSTOP trial, intentional held-key death, LED pack, or broad test/audit run. No raw key logger or background observer that opens input/uinput devices. A private `/tmp` directory for status-only observation is allowed only if declared, exact-owned, and removed.

## Report, result, and persistence contract

Use `status: PASS` and `phase-qualified result: acceptance-PASS` only for this named slice when the external recovery path was proven before start, genuine `armed=1` occurred, sampled forwarding was observed, the matching cutoff killed that invocation, post-death G213 typing was observed, and final cleanup/state passed. Otherwise use `PARTIAL` with `not-applicable` when execution produced useful bounded evidence but a required claim is missing, or `BLOCKED` with `not-applicable` when a precondition stopped execution. Always state that the logical whole remains `not-closed`. Do not claim full G4, watchdog/held-modifier/LED coverage, or production readiness.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 16_acceptance_00.md
Destination path: /home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
Report filename: 16_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: this WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

You are explicitly authorized and required to create `/home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/16_report_00.md` before terminal notification for PASS, PARTIAL, or BLOCKED. This is file preparation only; no META add/commit/push and no historical rewriting. Verify the physical directory, parents, symlinks, and collision before writing. Preserve any existing/nonidentical file; never overwrite or silently choose another name. If persistence fails, report the failure and provide the complete report as fallback, never claim it was saved without complete readback.

The saved report must begin exactly `### Report for ORCHESTRATOR_CHAT`, contain exactly one coordinate set echoing this prompt, status/result, start/end commit, preflight and external recovery proof, invocation/cutoff identity, ARM/physical sample/recovery outcomes without content, before/after state, privilege attribution, cleanup, Git actions, remaining evidence, one smallest next step, one report justification (`new-evidence` or `changed-external-state`), compact `Orchestration critique` with `MEASURED`/`LEAD` (`none` allowed), resolved/pre-existing failures, `Logical-whole closure: not-closed`, and authority expiry. Do not include raw typed text, key names, scan codes, serials, screenshots, passwords, or private network details.

Read the report back completely and verify its identity before notifying the Cooperator. The Cooperator archives the exact prompt/report pair after the report exists. Do not ask him to copy/paste the report. Your authority expires at the terminal report.
