# ContextDesk — install the reviewed suspend/resume hook, leave broker inactive

## Identity and one bounded deployment outcome

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 21
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Deployment Worker — install suspend hook only
Phase: deployment
Task identity: CONTEXTDESK-AB10491-SUSPEND-HOOK-INSTALL
Delivery: manual
Reasoning recommendation: High
Recommended context capacity: approximately 128k tokens; not a provider capacity attestation
Selected model: Cooperator choice; record actual client/model/reasoning only when observable
Evidence tier: E3
Evidence tier basis: privileged installation and exact readback of one system-sleep hook; no live sleep or broker start
```

Use a genuinely fresh Worker session. Worker 20 authority is expired. Do not dispatch subagents. Speak Slovak to the Cooperator; write the terminal report in English. Your only outcome is installation and verification of the reviewed suspend/resume hook from the exact public product candidate. Do not start, stop, enable, restart, reload, ARM, or grab the broker; do not invoke suspend/hibernate; do not open G213 event/uinput nodes; and do not change udev, ACLs, input-remapper, power settings, or source.

Worker 20 produced `implementation-PASS` and public commit `ab10491c49d0b6574b6953a02935a4664c39d7c2`, adding `packaging/systemd/contextdeck-sleep.sh`, deterministic fake-systemctl tests, and documentation. Its report explicitly states that no host installation was performed. This deployment installs only the system-sleep hook so a later fresh acceptance can test the real host lifecycle.

## Exact candidate and host scope

Canonical product checkout: `/home/agile/Projects/contextdesk`; remote `https://github.com/cisarik/contextdesk.git`; branch `main`; expected product `HEAD`:

```text
ab10491c49d0b6574b6953a02935a4664c39d7c2
```

Required AP gitlink and checkout: `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`; `./.ap/ap doctor` must pass. META checkout: `/home/agile/meta`; remote `https://github.com/cisarik/meta.git`; public META latest at prompt preparation is `020e341a0eb85385fab8bcff001a1fe33a381b97`, containing Worker 20's exact prompt/report. Do not silently retarget to another product commit. If any exact identity differs, stop before privileged work.

```text
Deployment candidate: ab10491c49d0b6574b6953a02935a4664c39d7c2
Hook source: packaging/systemd/contextdeck-sleep.sh
Installed hook: /usr/lib/systemd/system-sleep/contextdeck-broker
Existing broker binary/unit: verify only; do not replace
Acceptance dependency: live host suspend/resume remains open after this deployment
Deployment allowlist: read-only product/build/host checks; one owner-operated hook installation or exact no-op verification; bounded backup/rollback of the one hook; exact report preparation
Deployment risk claims: exact reviewed hook installed as root-owned executable; no broker runtime transition; no persistent host/power-policy change beyond the hook file
Out-of-scope: broker binary/service replacement, daemon-reload, live suspend, start/ARM/grab, udev/ACL changes, autostart, automatic re-ARM, G4 closure
```

Read focused `AGENTS.md`, pinned AP deployment/report contracts, Worker 20 report, `packaging/systemd/contextdeck-sleep.sh`, CMake install lines, `docs/operations.md` suspend section, and `docs/testing-m2.md` live-suspend section. Do not reread the whole archive or modify historical reports.

## Preflight and artifact verification

Verify physical product/META/AP roots, remotes, branch, exact product `HEAD`, clean source worktree (ignored `build/` allowed), no Git lock/operation, matching `.ap` gitlink/checkout, and AP doctor. Read-only product `git fetch origin main` is allowed. No product Git mutation or META Git operation is authorized except the exact report-file preparation below.

Verify the source hook is a regular non-symlink executable, `sh -n` passes, and its SHA-256 is recorded. Build/configure the current candidate with the documented sanitized `PATH` only if needed to verify the install manifest; run the existing full CTest suite once if the build is reconfigured. Do not install a second product component or change dependencies. A staging install under a private `/tmp` directory is allowed to prove that CMake's `broker` component contains the expected hook path; remove only that exact staging directory after readback.

Before the owner block, verify the current host is safe and unchanged: `/usr/bin/contextdeck-broker` and `/etc/systemd/system/contextdeck-broker.service` are regular files with the Worker 14 hashes (`8e80f2d78530b01d9cda4ab77c4ff75d2888055dadce35fbb9483a15651940a6` and `286154ba6f443adced5dc965b0f0c4da2dfae2a44e4f77edf888c6ef96c30503`), the service is `static/inactive/dead`, `MainPID=0`, no active invocation, no broker process, no `/run/contextdeck`, no ContextDeck virtual device, no trial/cutoff unit, and input-remapper policy is unchanged. If the existing binary/unit identity is different or the broker is active, stop and report; do not repair it in this task.

The only durable target is `/usr/lib/systemd/system-sleep/contextdeck-broker`. If it already exists, verify it is a regular non-symlink root-owned executable and record its pre-install hash/mode. Never overwrite an unexplained symlink or non-file. Preserve a root-owned mode-0700 private backup in a uniquely created `/tmp` directory until post-readback; if no old hook exists, record that fact and use a rollback plan that removes only the newly installed exact file on failure.

## Owner-operated installation block

Prepare one short paste-safe block at a time from a neutral directory. Privileged actions are Cooperator-owned: same-terminal `sudo -v`, `sudo -n true`, exact `/usr/bin/install`, `/usr/bin/mv`, `/usr/bin/rm`, and `/usr/bin/sha256sum` paths, then `sudo -k`. No password in chat, keep-alive, sudoers change, package install, large heredoc, or model-dependent emergency step.

The block may perform only:

1. Create the exact private root-owned backup directory and back up an existing hook without following symlinks.
2. Install the verified candidate hook to `/usr/lib/systemd/system-sleep/contextdeck-broker` with mode `0755`, creating only the known parent directory if needed with root ownership and mode `0755`.
3. Read back type, symlink status, owner, mode, SHA-256, and `sh -n` for the installed hook.
4. On any installation/readback failure, restore the exact backup if one existed, or remove only the newly created exact hook, then report both original and rollback outcomes. Do not touch the broker binary/unit or run daemon-reload.

Do not start or stop any unit. Installing a system-sleep hook does not itself invoke it. Do not call the hook manually in production mode, do not pass `--testdir` on the live host, and do not run `systemctl suspend`, `hibernate`, `hybrid-sleep`, or `suspend-then-hibernate`.

## Required post-state

Worker-independent readback must show:

| Object | Required state |
|---|---|
| Hook | `/usr/lib/systemd/system-sleep/contextdeck-broker` regular non-symlink, root-owned, mode `0755`, exact SHA-256 equal to candidate source |
| Hook syntax | `/bin/sh -n` succeeds; no shell output contains secrets/private environment |
| Existing broker artifacts | binary/unit hashes and modes unchanged; no replacement attempted |
| Broker runtime | `UnitFileState=static`, `ActiveState=inactive`, `SubState=dead`, `MainPID=0`, no process/socket/virtual device |
| Host policy | input-remapper, udev/ACL, OpenRGB, KWin, power configuration unchanged |
| Git/AP | candidate/AP identity unchanged; no product or META Git mutation |
| Privilege | same-terminal `sudo -k` and exit evidence recorded; backup retained on failure or removed only after successful readback |

This deployment does not prove that systemd executes the hook, that an armed grab is released before suspend, or that the broker reconnects after resume. Those claims require a separate fresh G4 acceptance prompt after this report.

## Result and report persistence

Use status `PASS` and phase-qualified result `deployment-PASS` only when the exact hook is installed/read back and all exclusions hold. Use `PARTIAL` for a useful but incomplete installation/readback, or `BLOCKED` for identity, permission, collision, or safety precondition failure. Always state `Logical-whole closure: not-closed`; never claim live suspend acceptance, full G4, production readiness, or autostart.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 21_deployment_00.md
Destination path: /home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
Report filename: 21_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: this WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

You are explicitly authorized and required to create `/home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/21_report_00.md` before terminal notification for PASS, PARTIAL, or BLOCKED. This is exact report-file preparation only; no META add/commit/push and no historical rewriting. Verify physical parents, real directory, symlinks, and collision; preserve any existing/nonidentical file and never choose an alternate name. If persistence fails, state it and provide the complete report as fallback; never claim saved bytes without complete readback.

The saved report must begin exactly `### Report for ORCHESTRATOR_CHAT`, echo this prompt's one coordinate set, include candidate/AP identities, source/installed hook hashes, mode/owner/symlink results, backup/rollback disposition, broker inactive state and unchanged existing artifact hashes, privilege attribution, Git actions, tests/syntax/staging evidence, explicit no-live-suspend statement, remaining acceptance evidence, one smallest next step, exactly one report justification (`changed-external-state` if installed, otherwise `new-evidence`), compact `Orchestration critique` with `MEASURED`/`LEAD` (`none` allowed), resolved/pre-existing failures, `Logical-whole closure: not-closed`, and authority expiry. Read the report back completely before notifying the Cooperator. The Cooperator archives this exact prompt/report pair after it exists.
