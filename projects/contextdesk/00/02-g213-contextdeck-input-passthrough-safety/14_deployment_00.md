# ContextDesk — install the reviewed broker candidate, leave it inactive

## Identity and one outcome

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 14
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Deployment Worker — bounded host install
Phase: deployment
Task identity: CONTEXTDESK-INSTALL-CB72AE0-NO-START
Delivery: manual
Reasoning recommendation: High
Recommended context capacity: approximately 128k tokens for this bounded task; not an attestation of the selected client's capacity
Selected model: Grok 4.6, Cooperator-selected; actual model/reasoning/context remain unknown unless observed
Evidence tier: E3
Evidence tier basis: replacement of a privileged input-broker executable and system service definition
Acceptance independence: not-required for this deployment's own readback; independent live acceptance remains separate
```

Your only outcome is installation of the exact candidate broker binary and service definition, with verified identity and final `static/inactive` state. The Cooperator runs the privileged installation block you prepare. You build, inspect, supervise, read back, write your own report, and stop. Do not dispatch agents.

Continuity evidence: `12_report_02.md` reports R1/R2 implementation-PASS; `13_report_00.md` reports BLOCKED because the installed unit and binary predate the candidate. Worker 13 reported 13/13 CTest and successful device-free self-tests, with no live broker start. Its report has known formatting defects and is evidence only. The Orchestrator accepts its bounded observations for routing this installation, not as independent G4 acceptance. This prompt is new authority; neither earlier prompt remains active.

A fresh session is selected for the Cooperator's smaller-task workflow and to keep the previous review session separate from host changes. Do not reset prior planning/audit budgets. This task addresses changed host state and named missing installation evidence; it is not another primary audit.

## Exact sources and focused reading

- Product checkout: `/home/agile/Projects/contextdesk`.
- Product remote: `https://github.com/cisarik/contextdesk.git`, branch `main`.
- Exact candidate: `cb72ae0388307b514182efc6936712e3da42cda4`.
- Governing `.ap` gitlink and checkout: `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`.
- META checkout: `/home/agile/meta`, remote `https://github.com/cisarik/meta.git`.
- META continuity snapshot read by the Orchestrator: `d00fa3ba2256c985c3c828ad88ea6ee143d8f57f`.
- Relevant META directory: `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/`.

Read applicable AGENTS; the pinned AP Worker minimum-reading spine and Worker reporting/session rules; AP's “Owner-Executed Commands and Privileged Sessions” and RF-19; Prompt Contracts' report header and delivery record. Task reading is operations §9, §6 verification only, the clean-PATH build guidance, the broker CMake install rule, the service file, and report 13's installed-identity, privilege, validation, and final-state sections. Read other source only to resolve a concrete installation ambiguity. Do not reread the full project/archive or undertake broad source review.

Independently verify physical repository roots, remotes, branch, HEAD, clean product worktree, no active Git operation, matching `.ap` gitlink/HEAD, and `./.ap/ap doctor`. Read current files from that candidate. A changed candidate, wrong repository, active Git operation, or unexplained product change blocks installation; preserve owner work. META can contain the Cooperator's pending prompt/unrelated files: do not demand a globally clean META worktree or touch them.

Read-only Git commands are allowed. An ordinary `git fetch origin main` in the product checkout is allowed if needed to establish the remote ref. No other Git mutation is granted: no stage, commit, push, reset, clean, stash, switch, restore, merge, rebase, config, or AP update.

## Allowed effects and exclusions

You may generate the existing ignored product `build/` outputs using the documented commands. You may create/read back the exact report file granted below. These are explicit exceptions to source-read-only inspection.

The Cooperator-owned host block may perform only:

1. Bounded backup of the two existing installation targets, preserving their modes/ownership and hashes, in one uniquely created root-owned private temporary directory.
2. `cmake --install build --component broker` from the verified candidate build configured with prefix `/usr`.
3. `install -m 0644 packaging/systemd/contextdeck-broker.service /etc/systemd/system/contextdeck-broker.service`.
4. `systemctl daemon-reload` followed by the exact readbacks below.
5. Broker-identity read/write permission checks on `/dev/uinput` using `test -r` and `test -w` only; no device opening or event injection.
6. If a replacement fails, restoration of those exact two backed-up files and daemon-reload, with the original failure and restoration outcome preserved separately.

The only durable host targets are `/usr/bin/contextdeck-broker` and `/etc/systemd/system/contextdeck-broker.service`. Verify the CMake component installs only the named executable before use. Do not install a different component or prefix, strip the binary, or invent a service override.

No broker start/enable/restart/reload/stop, LEASE, ARM, live sockets, physical grab, GUI launch, cutoff timer activation, real input/uinput access, package installation, udev/sysusers/ACL mutation, sudoers changes, input-remapper/OpenRGB/KWin/power changes, source edits, or durable roadmap edits are authorized. Here `daemon-reload` is allowed only to load the replaced or restored service definition; it is not permission to reload/start the broker. If the broker is already active, stop this task and report the unexpected state; do not stop an owner process yourself.

Keep ordinary typed content, serials, raw input events, environment dumps, passwords, and unrelated private configuration out of tool output and reports. Inspect metadata and bounded operational state only.

## Build once and prepare the owner block

Follow operations §9: configure `build/` using Ninja and `-DCMAKE_INSTALL_PREFIX=/usr`, build, then run CTest once with `--output-on-failure`. The full suite is required by this documented installation route. No new tests or unrelated audits. Use the documented sanitized PATH route if the known ambient `CMAKE_ROOT` problem occurs; classify the initial error. Do not reconstruct the toolchain or change dependencies.

Record fresh SHA-256 for `build/contextdeck-broker` and the candidate service. The service hash expected at this candidate is `286154ba6f443adced5dc965b0f0c4da2dfae2a44e4f77edf888c6ef96c30503`. Do not require the binary to equal a previous Worker's build hash: the installed binary must equal the current verified candidate build. Check ownership/regular-file status and reject unexpected symlink targets before host writes.

Check that the report destination is available before the host step. Build/test failure blocks replacement. Capture installed hashes and service state before asking the Cooperator to execute anything.

Prepare one short paste-safe owner-executed block at a time with a stated purpose, phase marker, fail-closed preconditions, completion marker, exit status, and safe abort instructions. Use a shell explicit enough to work from the Cooperator's Fish terminal. Do not paste a large privileged script or a fragile heredoc. The block must recheck the candidate/source hashes and inactive service immediately before replacements and check each command's result.

Follow AP's owner-terminal privilege lifecycle: begin from a neutral directory, let the Cooperator authenticate with `sudo -v` in the OS prompt, verify `sudo -n true` in that same terminal, execute the bounded operations, collect their post-state, then `sudo -k` in the same reachable terminal. Use verified system executable paths for privileged commands, including `/usr/bin/cmake`; do not inherit a client/AppImage tool wrapper. Never receive a password or start a keep-alive. A successful owner-terminal timestamp does not prove that your separate Worker process has sudo access.

If `sudo -n` is unavailable in your Worker process, proceed with this already-authorized owner-executed route; do not demand passwordless sudo or terminate merely for lack of a timestamp in your terminal. Wait for complete output before advancing. Missing owner input is an intermediate wait, not a fabricated deployment result. An actual refusal, failed installation, or missing mandatory evidence is reported honestly at termination.

Retain the narrowly scoped backup through verification. Clean only this task's exact owned temporary backup after a successful install/readback; preserve it for recovery on failure and report that fact. Never use the broad operations §6 rollback, remove broker identities, or alter udev policy.

## Readback and stop point

Independently perform readable checks after the owner block, attributing privileged checks to the Cooperator's output:

| Object/check | Required evidence |
|---|---|
| Installed binary | Regular root-owned executable, mode `0755`, `cmp`/SHA-256 equality with the verified current `build/contextdeck-broker` |
| Installed service file | Regular root-owned file, mode `0644`, byte equality with the candidate service |
| Runtime directory setting | `RuntimeDirectoryMode=0755`; do not require the runtime directory to exist while inactive |
| Effective loaded unit | Expected fragment, no unexplained drop-ins, no pending daemon reload; `Type=notify`, `NotifyAccess=main`, `Restart=no`, `TimeoutStopUSec=5s`, `TimeoutAbortUSec=5s` |
| Watchdog | Candidate file has `WatchdogSec=2`; an inactive unit's `WatchdogUSec=infinity` alone is not a mismatch |
| Service state | `UnitFileState=static`, `ActiveState=inactive`, `SubState=dead`, `MainPID=0`; no new invocation |
| Unit validity | `systemd-analyze verify` installed unit succeeds; syntactic validity alone does not prove artifact equality |
| Broker-user uinput access | Owner runs `sudo -n -u contextdeck-broker test -r /dev/uinput` and the corresponding `-w` check; both exit 0, no device open |
| Existing policy | Read-only uinput ACL and G213 event/hidraw policy metadata still match operations §6; identity-resolve nodes, do not expose serials/event numbers |
| Other services | input-remapper's observed enabled/active state preserved; no other service manipulation |
| Product checkout | Same commit/AP pin; no source changes |
| Privilege and backup | Same-terminal privilege release observed, or explicitly unknown with disposition; exact owned backup cleanup or retained recovery checkpoint reported |

`systemctl is-active` may exit nonzero while correctly reporting `inactive`: evaluate the documented state rather than treating every nonzero status query as a failed install. Installation/build/verification command failures remain failures. Do not rerun unchanged broad gates to force a PASS.

On complete successful installation/readback use status PASS and phase-qualified result `deployment-PASS`, explicitly limited to installing this candidate while inactive. Otherwise use PARTIAL or BLOCKED and phase-qualified result `not-applicable`. No live G4 or physical recovery claim is in this task. The overall logical whole remains not-closed. Report once and stop; do not proceed to acceptance or produce another task grant.

## Exact report-file preparation — positive write grant

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 14_deployment_00.md
Destination path: /home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
Report filename: 14_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: this WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

You are explicitly authorized and required to create this one report file before your terminal notification:

`/home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/14_report_00.md`

This grant applies to PASS, PARTIAL, and BLOCKED outcomes. It is an explicit exception to all source/host read-only boundaries above and grants **file preparation only**. No META fetch/add/commit/push or changes to any other META file are authorized. Do not overwrite `13_report_00.md`, modify this prompt, or write `AP_DEFECTS_2.md`.

Verify physical META identity, destination parents, and symlinks. Preserve any existing report or nonidentical collision; do not overwrite it, silently choose another filename, or create a placeholder. If the exact write is blocked, identify that failure and return the complete report in chat as the fallback. Never claim a saved file without readback.

Finish the English report, write it, read it back completely, and verify its identity/content. The first line must be exactly `### Report for ORCHESTRATOR_CHAT`. Echo the three identity coordinates from this prompt once, with session target, native mode, profile, phase, and task. Include status, valid phase-qualified result, unchanged start/end commit, touched targets, build/validation results, installed hashes/modes/effective unit state, owner-versus-Worker evidence attribution, privilege/backup disposition, Git actions, remaining evidence, one smallest next step, one report justification, and authority expiry. Use `changed-external-state` as justification if installation occurred, otherwise `new-evidence`.

Include compact `Orchestration critique: MEASURED: ...; LEAD: ...`, plus resolved issues and pre-existing failures if any. `none` is valid; do not invent a required near-miss. Record `Logical-whole closure: not-closed` once. Avoid raw transcripts and repeating the report contract. Include installation/recovery failures in enough detail to preserve the cause.

After successful readback, notify the Cooperator briefly in Slovak with the result and exact report path. Do not require him to copy/paste the report from chat into META. He will add/commit/push the exact prompt/report pair after the report exists. Your authority then expires.
