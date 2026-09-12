# ContextDesk — production watchdog recovery with a held modifier

## Identity and one bounded outcome

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 18
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Acceptance Worker — watchdog death with held modifier
Phase: acceptance
Task identity: CONTEXTDESK-9A89095-WATCHDOG-HELD-MODIFIER
Delivery: manual
Reasoning recommendation: High
Recommended context capacity: approximately 128k tokens; not a provider capacity attestation
Selected model: Cooperator choice; record actual client/model/reasoning only when observable
Evidence tier: E3
Evidence tier basis: live systemd watchdog abort of an armed broker and G213 recovery while a modifier is held at process death
```

Use a genuinely fresh Worker session. You did not implement or deploy the candidate, and Worker 16/17 authority is expired. Do not dispatch subagents. Speak Slovak to the Cooperator; write the terminal report in English. Your one outcome is a single, tightly bounded production watchdog claim on the unchanged runtime candidate: independently verify an external recovery path, start once, authenticate and ARM once, hold one harmless modifier when the broker event loop is stopped, let systemd's watchdog abort the matching invocation, and verify that the G213 works again after descriptor close. This is not whole-G4 closure.

**Hard safety gate:** before starting the broker or ARM, the Cooperator must independently demonstrate either a second physical keyboard can operate a prepared local recovery terminal or SSH from another device can operate a prepared recovery shell. The path must remain available through the test. If neither route is demonstrated, stop before starting anything with status `BLOCKED` and phase-qualified result `not-applicable`. A cutoff timer is not a substitute for this gate.

The previously accepted Worker 16 slice proved external SSH readiness, explicit ARM, sampled pass-through, matching-cutoff death, and post-death typing. Worker 17 changed documentation only. This prompt adds only the still-open watchdog/held-modifier evidence; it does not repeat the cutoff trial, change code, or authorize autostart.

## Exact candidate and bounded continuity

Canonical product checkout: `/home/agile/Projects/contextdesk`; remote `https://github.com/cisarik/contextdesk.git`; branch `main`; expected product `HEAD`:

```text
9a89095d97bde1cdb8ec989f06f83fcc780b8280
```

This is a documentation-only descendant of runtime code candidate `cb72ae0388307b514182efc6936712e3da42cda4`; no runtime file changed in Worker 17. Required AP gitlink and checkout: `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`; `./.ap/ap doctor` must pass. Do not silently retarget to another product commit. If the product has moved, stop and report the divergence.

META: `/home/agile/meta`, remote `https://github.com/cisarik/meta.git`; trace directory `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/`. Public META currently contains the exact Worker 16 report and Worker 17 documentation report; read their current public identities before execution. META is historical evidence and Cooperator-owned for Git archival. Do not modify META except the exact report-file preparation granted below.

```text
Acceptance candidate: 9a89095d97bde1cdb8ec989f06f83fcc780b8280 (docs-only descendant)
Runtime candidate: cb72ae0388307b514182efc6936712e3da42cda4
Acceptance owner map: docs/testing-m2.md watchdog/G4 procedure; docs/operations.md §7–8; installed systemd unit; this prompt's fixed held-modifier claim
Acceptance allowlist: read-only repository/host state; one owner-operated broker start; one authenticated LEASE/ARM; one controlled watchdog-stop/abort sequence; one physical hold/release/recovery sample; exact report preparation
Acceptance risk claims: verified external recovery path; explicit ARM; event-loop watchdog abort; no automatic restart/re-grab; G213 usable after process death while modifier was held; final inactive state
Acceptance control matrix: recovery proof; pre-ARM disarmed state; OK ARMED; held modifier at SIGSTOP; systemd watchdog result; post-death typing/modifier release; final cleanup
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1 (inherited Worker 16 named slice; this is a new missing-evidence probe, not a reset)
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: production watchdog abort and held-modifier recovery on this host
Out-of-scope observations: cutoff path, separate crash trial, lease-expiry trial, LED-return pack, all-control fidelity, autostart, logical-whole closure
```

Focused reading only: applicable `AGENTS.md`, pinned AP Worker/report contracts, exact Worker 16/17 reports, current `docs/testing-m2.md` watchdog and G4 sections, `docs/operations.md` §7–8, the installed service and its current source, and the small client/UI entrypoints needed to ARM. Do not reread the entire archive or rerun the unchanged full test suite.

## Preflight and external recovery proof

Before any live operation verify product root/remote/branch/exact `HEAD`, clean source worktree (ignored build output allowed), no Git lock/operation, matching `.ap` gitlink and checkout, AP doctor, installed broker and unit hashes/equality from Worker 14, static/inactive/dead state, `MainPID=0`, no pending daemon reload, no active trial timer, no broker process, no ContextDeck virtual device, and unchanged input-remapper/policy. Read-only product `git fetch origin main` is allowed; no other Git operation, product mutation, or META Git operation is authorized.

Expected installed artifacts remain regular non-symlink files: broker `/usr/bin/contextdeck-broker` mode `0755`, SHA-256 `8e80f2d78530b01d9cda4ab77c4ff75d2888055dadce35fbb9483a15651940a6`; service `/etc/systemd/system/contextdeck-broker.service` mode `0644`, SHA-256 `286154ba6f443adced5dc965b0f0c4da2dfae2a44e4f77edf888c6ef96c30503`. Verify `Type=notify`, `NotifyAccess=main`, `Restart=no`, `WatchdogSec=2` in the file, `TimeoutStopSec=5`, `TimeoutAbortSec=5`, `RuntimeDirectoryMode=0755`, no `RuntimeMaxSec`/`[Install]`. Inactive `WatchdogUSec=infinity` is not a file mismatch.

Do not open event or uinput nodes during preflight. Resolve G213 policy by USB ancestry/interface; preserve broker event access, hidraw seat access, uinput named-user ACL, and input-remapper enabled/active state. Owner access checks may use `test -r`/`test -w` only.

Prepare the verified candidate `build/contextdeck` session app and an unsaved Kate/text buffer. Rehearse the exact GUI path while the broker is inactive: tray or Diagnostics **`Arm G213 pass-through…`** → Qt dialog **`Arm G213 pass-through now?`** → **Yes/OK**, then cancel and return to disarmed state. This is a GUI action, not a terminal command, not a restart, and not a sudo password. Prepare status-only observation before the live window. Do not save or log buffer content.

Choose exactly one recovery route and prove it before broker start and before any ARM:

- **SSH:** from another device, execute a harmless marker and `systemctl show -p ActiveState --value contextdeck-broker.service`, obtain successful output, and leave the shell available. Do not record host keys, password, address, or private environment. The shell must be capable of issuing the exact matching-unit stop/continue/kill readbacks below.
- **Second physical keyboard:** use the other keyboard to reach a prepared local terminal, type a harmless marker, and obtain the same read-only unit-state output. Keep that keyboard connected and the recovery terminal reachable. A mouse, gamepad, or the G213 itself is not sufficient.

If the route cannot be demonstrated or drops before the final readback, do not start/ARM a second time. A route proof grants no unrelated host access.

## Positive runtime authority — one watchdog invocation

After all gates pass, the Cooperator may execute only this sequence. The Worker must prepare every instruction and recovery command before the timed portion; no model round-trip may be needed to recover the host.

1. Start `contextdeck-broker.service` exactly once from `static/inactive` with no enable/restart/reload/daemon-reload. Verify `active/running`, a fresh `InvocationID`, `armed=0`, `lease=none`, no virtual device, and watchdog settings. If start or authentication fails before ARM, perform bounded cleanup and report; never retry.
2. With the external route available, use the existing authenticated session app for one LEASE/ARM attempt through the rehearsed dialog. Require `OK ARMED` or authenticated STATUS `armed=1`; do not use a transient client label after `OK LEASE` as proof. Confirm a virtual device exists and a harmless pre-death physical sample works, without recording content.
3. Select one harmless modifier (for example Shift) and have the Cooperator hold it physically. Do not combine it with a desktop shortcut or other key. Confirm the hold is active without logging the key name or raw event.
4. From the already-proven external recovery path, read the exact live `InvocationID` and `MainPID`, then send `SIGSTOP` to the **main process of this exact running unit** using a unit-scoped, identity-checked command. Do not use `pkill`, `killall`, a guessed PID, or a different invocation. The stopped event loop must stop feeding `WATCHDOG=1`.
5. Wait a bounded interval sufficient for `WatchdogSec=2` plus one missed interval. Observe systemd's watchdog result and signal. If the process remains stopped with the watchdog abort pending, send only `SIGCONT` to that same unit main process from the external route and wait for systemd's abort to complete. Do not send a manual `SIGABRT` and do not turn this into a generic crash test. If watchdog abort does not occur after the documented bounded wait, use a matching-unit `SIGKILL` only for emergency recovery, classify watchdog evidence as failed/PARTIAL, and never call that PASS.
6. After the broker is dead, have the Cooperator release the modifier and type a short harmless sample with the G213 in the same unsaved buffer. Confirm no obvious stuck modifier, duplicate, or phantom behavior. This post-death G213 result is required; typing only on the recovery keyboard is not recovery evidence. Capture no text, screenshot, serial, raw event, or key name.
7. Verify no automatic restart/re-grab (`Restart=no`, `NRestarts=0`, no process, no virtual device), no active cutoff/trial unit, unchanged input-remapper and policy, and final `static/inactive/dead`, `MainPID=0`. Reset only the resulting failed marker after all causal evidence is captured. Close the unsaved buffer without saving and remove only exact task-owned status observers/files. Do not start or ARM again.

For emergency safety, the verified external route may stop or unit-scope-kill the same invocation if it remains alive after the bounded watchdog wait or if the G213 remains unsafe. Such a fallback is recorded as a recovery action and cannot produce watchdog `PASS`. Unplug/replug is last-resort owner recovery and must be reported as failure of automatic recovery. Do not alter input-remapper, udev/ACLs, service files, packages, OpenRGB, KWin, power, autostart, source, AP, or product documentation.

Privileged actions remain Cooperator-owned. Use one short paste-safe block at a time, exact system command paths, fail-closed checks, markers and exit codes, same-terminal OS password handling, `sudo -v`/`sudo -n true` as needed, then `sudo -k`. No password in chat, keep-alive, sudoers change, large heredoc, or model-dependent emergency step.

## Result and report persistence

Use status `PASS` and phase-qualified result `acceptance-PASS` only when the external recovery path was proven before start, genuine ARM and physical pre-death operation occurred, a modifier was held at `SIGSTOP`, systemd (not a manual fallback) produced the watchdog abort, the matching invocation stayed dead without restart/re-grab, post-death G213 typing succeeded after the modifier was released, and final cleanup passed. Otherwise use `PARTIAL`/`BLOCKED` with `not-applicable`. Always state `Logical-whole closure: not-closed`; do not claim full G4, production readiness, or autostart.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 18_acceptance_00.md
Destination path: /home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
Report filename: 18_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: this WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

You are explicitly authorized and required to create `/home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/18_report_00.md` before terminal notification for PASS, PARTIAL, or BLOCKED. This is exact report-file preparation only; no META add/commit/push and no historical rewriting. Verify physical parents, real directory, symlinks, and collision; preserve any existing/nonidentical file and never choose an alternate name. If persistence fails, state it and provide the complete report as fallback; never claim saved bytes without complete readback.

The saved report must begin exactly `### Report for ORCHESTRATOR_CHAT`, echo this prompt's one coordinate set, and include candidate/runtime identities, status/result, external recovery proof, before/after state, InvocationID/MainPID, held-modifier and watchdog outcomes without key names or content, systemd result/signal, recovery/cleanup, privilege attribution, unchanged policy/runtime, Git actions, missing evidence, one smallest next step, exactly one report justification (`new-evidence` or `changed-external-state`), compact `Orchestration critique` with `MEASURED`/`LEAD` (`none` allowed), resolved/pre-existing failures, `Logical-whole closure: not-closed`, and authority expiry. Read the report back completely before notifying the Cooperator. The Cooperator archives this exact prompt/report pair after it exists.
