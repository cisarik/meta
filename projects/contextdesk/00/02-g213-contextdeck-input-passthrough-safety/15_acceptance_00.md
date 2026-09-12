# ContextDesk — one physical pass-through and invocation-cutoff trial

## Identity and bounded result

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 15
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Acceptance Worker — one physical cutoff trial
Phase: acceptance
Task identity: CONTEXTDESK-CB72AE0-ONE-CUTOFF-TRIAL
Delivery: manual
Reasoning recommendation: High
Recommended context capacity: approximately 128k tokens; not a provider capacity attestation
Selected model: Cooperator choice; record actual client/model/reasoning only when observable
Evidence tier: E3
Evidence tier basis: physical keyboard grab and process-death recovery on the Cooperator's active seat
```

Use a genuinely fresh session with no material participation in implementing the candidate. Do not dispatch subagents. Speak Slovak to the Cooperator; write the report in English. Your one result is a measured, narrowly scoped physical trial: ordinary G213 pass-through while armed, followed by typing recovery after the existing PID1 invocation-bound cutoff kills that same broker invocation. This is not the whole G4 pack and does not close M2.

Worker 14's grant expired. This prompt supplies new authority. The Cooperator has selected smaller assignments and the documented one-keyboard cutoff route. A second keyboard or SSH is optional. Do not make either a prerequisite for this trial, and do not infer that this permits every watchdog or held-key failure experiment.

## Sources, previous evidence, and acceptance budget

Product: `/home/agile/Projects/contextdesk`, remote `https://github.com/cisarik/contextdesk.git`, branch `main`, exact candidate `cb72ae0388307b514182efc6936712e3da42cda4`. Governing AP gitlink and checkout: `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`.

META: `/home/agile/meta`, remote `https://github.com/cisarik/meta.git`; trace directory `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/`. The Orchestrator fetched public META commit `5d4bcf9811974aa71e6d17acc3c2375a5015db40` and read the exact `14_report_00.md`. Prompt 14 matches the issued bytes and was first added with its report in that commit.

Reconciliation: Worker 14 reports deployment-PASS, 13/13 CTest, exact installed identity, static/inactive broker, owner-terminal privilege release, and backup cleanup. The Cooperator separately supplied matching install output with EXIT:0. Backup cleanup and additional host checks remain attributed Worker evidence, not direct Orchestrator host observations. Worker 13's useful device-free evidence is preserved; its installation blocker is addressed by Worker 14. Neither report proves live G4.

```text
Acceptance candidate: cb72ae0388307b514182efc6936712e3da42cda4
Acceptance owner map: docs/operations.md sections 7–8; docs/testing-m2.md cutoff semantics; packaging/systemd/contextdeck-trial-cutoff.sh; this prompt's fixed physical claims
Acceptance allowlist: read-only candidate and host metadata; the single owner-operated runtime trial, bounded recovery, and artifact preparation explicitly granted below
Acceptance risk claims: explicit ARM only; sampled physical forwarding; matching-invocation cutoff death; physical typing recovery; no automatic restart/re-grab; unchanged input-remapper state
Acceptance control matrix: pre-ARM disarmed/no virtual device; positive OK ARMED and physical sample; positive cutoff-kill attribution; post-death no process/virtual device/restart and physical sample
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: physical pass-through and recovery from invocation-bound cutoff on the now-installed candidate
Out-of-scope observations: ledger-candidates
```

The budget values concern the unchanged cb72ae0 candidate since the primary attempt 13/01. Older candidate acceptance history is retained. This is named missing evidence after a verified installation-state change, not a reset or second broad primary audit. No correction or implementation is authorized.

Focused reading: applicable AGENTS, pinned AP Worker spine, reporting/independence and owner-executed privilege rules; report 14; operations sections 7–8 and section 6 verification only; testing-m2 cutoff distinctions; cutoff helper and service; `src/app/BrokerIpcClient.cpp`, `src/app/TrayController.cpp`, and the relevant broker STATUS/ARM handling. Read other source only to resolve a concrete prerequisite. Do not reread the whole archive or rerun the unchanged full acceptance/test pack.

## Preflight before starting anything

Verify physical roots/remotes, exact product HEAD and branch, clean source worktree, no active Git operation, matching AP gitlink/checkout, and `./.ap/ap doctor`. An ordinary product `git fetch origin main` is allowed if needed. No other Git mutation, including META fetch, is granted. META need not be globally clean: preserve unrelated work and the Cooperator's pending prompt.

Verify installed regular files, root ownership, no symlinks, and equality with candidate artifacts:

| Object | Expected |
|---|---|
| `/usr/bin/contextdeck-broker` | mode 0755; SHA-256 `8e80f2d78530b01d9cda4ab77c4ff75d2888055dadce35fbb9483a15651940a6`; equal to the existing candidate build |
| `/etc/systemd/system/contextdeck-broker.service` | mode 0644; SHA-256 `286154ba6f443adced5dc965b0f0c4da2dfae2a44e4f77edf888c6ef96c30503`; equal to candidate service |
| Loaded unit | correct fragment, no unexplained drop-ins, no pending daemon reload; static/inactive/dead, MainPID=0 |
| Unit settings | Type=notify, NotifyAccess=main, Restart=no, WatchdogSec=2 in file, stop/abort timeouts 5s, RuntimeDirectoryMode=0755; no RuntimeMaxSec or Install section |
| Policy | identity-resolved G213 pair retains broker access and lacks session-user event ACL; hidraw and uinput seat ACLs preserved; broker uinput rw ACL; input-remapper state unchanged |

Worker 14's build hash is now a deliberate installed-artifact anchor, not a universal reproducible-build requirement. Do not replace the broker or silently accept another hash. A mismatch is a new prerequisite to report. Inactive WatchdogUSec=infinity and is-active exit 3 are not standalone failures.

Use read-only identity/ACL metadata, never open physical event nodes or uinput yourself. Owner-executed broker-user `test -r`/`test -w` access checks are permitted if fresh verification needs them. Record absence of pre-existing broker processes, trial timers, and ContextDeck virtual devices. Unexpected active resources are owner state: do not stop or adopt them.

Prepare the existing session app and a local unsaved plain-text scratch buffer before the timed window. Verify the app executable belongs to this candidate; do not silently reuse an old running binary. If needed, you may build only the existing `contextdeck` target in ignored `build/` using the documented system-tool/clean-PATH route. No install or full CTest rerun is needed on this unchanged candidate. A build failure stops before live execution. Replacing an already-running stale app requires a clear owner-managed quit/relaunch, preserving unsaved work; do not kill an unknown process.

Read the actual UI labels. The existing tray action is `Arm G213 pass-through…`, with explicit confirmation; Diagnostics offers the same action. Prepare status-only IPC/log observation and the trial instructions before starting the clock. **The UI word `armed` alone is insufficient evidence:** this candidate's client can set that label on `OK LEASE` while ARM is pending. Require `OK ARMED` or a subsequent broker STATUS with armed=1. Do not fix the UI in this task.

## Positive runtime authority and its limits

The Cooperator may perform, under your prepared bounded instructions:

1. Run the verified existing session app as the local graphical user, and open/use the scratch text buffer. Existing app profile-driven lighting may operate normally; no profile edits or new OpenRGB/KWin setup are granted.
2. Start `contextdeck-broker.service` **once** from its verified inactive state, without enable/restart.
3. Connect the session app to `/run/contextdeck/broker.sock` for authenticated STATUS, one LEASE/ARM attempt, normal heartbeats, and DISARM/RELEASE for safe abort/cleanup. The broker alone may enumerate/open the G213 event pair, create its virtual uinput device, and grab them as a consequence of that one explicit ARM.
4. Invoke the exact candidate `packaging/systemd/contextdeck-trial-cutoff.sh` on the **system manager** with `--timeout=45 arm contextdeck-broker.service <exact-current-InvocationID>`. Verify its source/path and command resolution before root execution. The helper's one transient timer/service, runtime files, and existing journal entries are allowed. Do not copy/install/modify the helper or use `--user` for this production trial.
5. Let that timer call its existing `fire` path and SIGKILL only the matching invocation. Normal sample completion must leave the timer armed so the cutoff event can be observed.
6. Clean the exact trial-owned resources, stop this invocation if still running, and reset only its resulting failed state after capturing causal evidence. No second start or ARM, even if time ran out or the first attempt failed.

For emergency recovery only: when the same invocation remains alive and a usable owner terminal is available, positively authorize a matching-identity checked `systemctl stop`, followed if necessary by unit-main SIGKILL. Never signal a guessed PID or a different invocation. An emergency stop is not cutoff success. If input remains silent after broker death, owner unplug/replug of this G213 is a last-resort recovery; record the failure, do not claim automatic recovery or re-arm. Do not rely on grabbed-keyboard TTY/SysRq shortcuts.

No SIGSTOP, separate crash injection, intentional held modifiers at death, lease-expiry experiment, LED test pack, autostart, package/udev/ACL/service-file edits, daemon-reload, source changes, AP updates, profile saving, input-remapper manipulation, OpenRGB server changes, KWin changes, power actions, or unrelated host mutation. Ordinary framework caches/runtime IPC created by the authorized GUI and scratch editor are allowed incidental outputs; do not edit unrelated configuration or save the typed sample.

You may create one private task directory under `/tmp` for bounded status-only observation output or an unprivileged status observer if necessary. Declare its actual identity, purpose, and cleanup; no raw input logger, new ARM client, replacement cutoff, or background privilege keep-alive. Do not record screenshots, typed text, window titles, USB serials, raw events, or credentials. Reports retain semantic outcomes and bounded causal evidence only.

## One trial, prepared before the countdown

1. **Prepare everything while disarmed.** Explain in Slovak that the test can briefly interrupt this keyboard, ends by a 45-second PID1 cutoff, and requires no second keyboard. The timer depends on a functioning kernel/PID1; it is not a universal machine-hang guarantee. Arrange the scratch buffer, GUI, observation, stop/abort instructions, and one short typing sample. Do not ask the Cooperator to transcribe results while the countdown runs.
2. **Owner starts once; verify disarmed.** Capture InvocationID, live unit properties, authenticated armed=0, and absence of a new virtual device before ARM. Setup/start failure leads to cleanup/report, not another trial. If broker authentication fails, do not run the client as root or weaken permissions.
3. **Owner arms cutoff only when ready to act locally.** Use one short paste-safe block with the full verified source path, exact invocation, phase/end markers, checked exit codes, and same-terminal sudo lifecycle. Verify timer active, intended target/invocation, 45s OnActive delay, AccuracySec=1us, Persistent=no and zero randomized delay. Print a clear local success cue and deadline. Do not insert a model round-trip between this cue and the already-explained GUI confirmation. If live checks or observation cannot be arranged before the deadline, do not ARM; let cleanup finish and report incomplete evidence. Never extend/reset the timer to buy time.
4. **One explicit human ARM.** After the local guard success cue, the Cooperator confirms the UI action. Observe genuine OK ARMED/armed=1 before treating typing as pass-through evidence. A failed/late ARM is not a reason to click again. Keep the app alive and its normal heartbeat running until cutoff.
5. **Small physical sample, then release all keys.** In the unsaved buffer, the Cooperator checks ordinary text, a brief repeat, and a modifier-assisted edit for apparent missing/duplicate/stuck input. Never type into a shell or expose sample content. Finish early and release all keys well before the deadline; deliberate held-key death is out of scope. This is sampled usability, not exhaustive event fidelity.
6. **Observe cutoff and recovery.** Let the exact timer expire. Retain bounded `cutoff-kill` evidence for the matching invocation and broker exit cause. If it exited earlier, the helper skipped, or a watchdog/lease/other path ended acquisition, classify that event honestly; do not relabel it cutoff PASS. After death the Cooperator types again in the buffer and confirms usability and absence of obvious stuck modifiers. Capture no text. Verify no restart or re-grab, no broker process, and no remaining ContextDeck virtual device.
7. **Clean and report once.** Collect evidence before resetting failure markers; a killed service may legitimately show failed while no process exists. Use the helper's exact cancel path for this invocation, verify no active trial timer/service, stop only the owned app if it was launched solely for this trial, close the unsaved buffer without saving, and remove exact owned temporary files. Final broker state is static/inactive/dead with MainPID=0, no virtual device, no active trial resources, unchanged input-remapper and policy. Preserve causal failure evidence if cleanup cannot establish that state. Never rerun the trial to obtain PASS.

Privileged operations remain Cooperator-owned. Prepare one short Fish-paste-safe owner block at a time, with explicit shell if needed, neutral starting directory, verified system command paths, `sudo -v` and `sudo -n true` in that same terminal, checked output and markers, then `sudo -k`. Password entry is OS-only. Missing Worker sudo timestamps do not block this already-authorized route. No heredoc-heavy/large privileged script, sudoers changes, password in chat, or assumed cross-terminal timestamp. During the live countdown recovery must not depend on another model response. Normal waits for Cooperator execution are intermediate; actual refusal or unavailable mandatory evidence is a truthful terminal outcome.

## Result criteria and exact persistence

Use status PASS and phase-qualified result `acceptance-PASS` **for this named physical cutoff slice only** when genuine ARM, sampled forwarding, matching cutoff death, post-death physical typing, and safe final state are all observed. Otherwise use PARTIAL/BLOCKED and `not-applicable`. Attribute human observations separately from Worker measurements. Do not claim full G4, watchdog PASS, held-modifier recovery, all controls/LEDs, or general production readiness. `Logical-whole closure: not-closed`.

The next routing decision belongs to the Orchestrator. Do not issue another prompt. Preserve remaining G4 claims explicitly; the source README/ROADMAP/AGENTS still need a bounded prospective reconciliation of R1/R2 implementation and the now-observed installation/trial state, without claiming all physical gates closed.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 15_acceptance_00.md
Destination path: /home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
Report filename: 15_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: this WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

You are explicitly authorized and required to write the complete English report at `/home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/15_report_00.md` and read it back completely **before terminal notification**. This applies to PASS, PARTIAL, and BLOCKED. Verify META identity, physical parents, symlinks, and absence of a conflicting file before runtime work. Preserve collisions; no overwrite or alternate filename. If actual persistence fails, report that failure and provide the complete report as the exception fallback. No META add/commit/push or historical report rewriting is granted.

Begin the saved report exactly `### Report for ORCHESTRATOR_CHAT`. Echo the three prompt coordinates once and record session target, profile, native mode, task, status/result, unchanged start/end commit, fixed claim outcomes, invocation/cutoff identity, before/after state, privileged lifecycle, sample outcomes without content, actual resource cleanup, source/evidence limits, model observations, and remaining risks. Use exactly one report justification (`new-evidence` or `changed-external-state`, as actually appropriate), one smallest next step, compact Orchestration critique with MEASURED/LEAD (`none` allowed), and resolved/pre-existing failures when applicable. State authority expiry.

One additional file preparation is explicitly granted to avoid losing reconciliation: append the following **Orchestrator-authored** entry to `/home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/00_notes.md`, preserving existing bytes. This Worker is only its persister. Verify physical path/symlink identity and the existing prefix against META `5d4bcf9811974aa71e6d17acc3c2375a5015db40`; if later notes conflict, preserve them and report the persistence exception without blocking safe cleanup. If the exact entry already exists, do not duplicate it. Do not compose additional notes or a second queue.

```markdown
## Worker 14 reconciliation and Worker 15 routing — 2026-09-12

Authored by the ContextDesk ChatOrchestrator; exact persistence delegated to Worker 15.

Public META 5d4bcf9811974aa71e6d17acc3c2375a5015db40 contains the matching first-add prompt/report pair for 14/01. The issued prompt bytes match. Deployment-PASS is reconciled only for candidate cb72ae0388307b514182efc6936712e3da42cda4 installed while inactive, under AP pin 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9. Owner install output corroborates installed hashes/state; further readback, 13/13 tests and backup cleanup are attributed Worker evidence. No physical G4 claim is accepted.

Manual delivery and smaller coherent tasks remain selected. Worker 14 authority expired. Worker 15 receives a fresh independent, single-invocation physical pass-through/cutoff evidence slice, not a repeat of the broad primary audit. Its outcome is not yet known in this entry. Remaining G4 claims and canonical product-state documentation reconciliation stay open. The AP-update whole is separate and grants no ContextDesk mutation.
```

Read back both saved artifacts and report their actual persistence outcome. Then notify the Cooperator briefly in Slovak with the report path. The Cooperator archives the exact prompt/report pair after report creation; no report copy/paste is the normal route. Your authority expires at terminal report.
