# ContextDesk — independent reversible install/remove/rollback deployment

ROLE: WORKER

Use a genuinely fresh Worker session. Session 24 authority is expired.
Do not dispatch subagents. Speak Slovak to the Cooperator; write the
terminal report in English.

This is file-based delivery. The Cooperator must not copy/paste this prompt,
manually compose a prompt file, or manually compose a report file. The Worker
is explicitly authorized to persist the exact received prompt bytes and its
own terminal report into the META trace under the exact destinations below.
The Worker must not commit or push META. The Cooperator may perform the
separate Git publication step after the Worker terminal report exists.

Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 25
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker-session profile: Fresh Independent Deployment Worker — reversible broker install/remove/rollback
Phase: deployment
Task identity: CONTEXTDESK-AB10491-INSTALL-REMOVE-ROLLBACK
Native planning mode: not-used
Reasoning recommendation: High
Recommended context capacity: approximately 128k tokens; advisory only
Evidence tier: E3
Evidence tier basis: privileged install/remove/restore/readback of the exact
broker artifacts and G3 host policy while the broker remains inactive; no
physical input source is opened, grabbed, or exercised
Acceptance independence: not-required for this deployment; live acceptance
remains a separate phase

The logical whole remains open. Sessions 16, 19, 22, 23, and 24 are accepted
named slices only and are historical context for this Worker. Do not repeat,
reclassify, or broaden them. Session 24 established one bounded
input-remapper coexistence slice; it did not establish general coexistence.
The handoff routes install/remove/rollback before documentation and closure.
Do not route or perform autostart early.

## Single bounded outcome

Perform one independent, reversible host deployment cycle for the exact
ContextDesk broker candidate while keeping the broker static and inactive:

1. Verify the current installed broker artifacts and secure G3 policy.
2. Create a private, narrowly scoped recovery checkpoint for only the
   ContextDesk-owned files and the exact expected system identity.
3. Remove only the exact ContextDesk broker files and identity, reload the
   affected policy, and obtain bounded proof that the removal occurred.
4. Restore the checkpoint immediately, without a model round-trip while the
   broker policy is absent, and obtain bounded proof that rollback restored
   the pre-cycle state.
5. Install the current candidate through the documented install procedure,
   including the broker binary, current unit, sleep hook, sysusers identity,
   and all three ContextDesk udev rules.
6. Verify exact final artifact identity, ownership, permissions, effective
   systemd state, secure G3 policy, unchanged input-remapper state, and
   absence of any broker runtime.

The measurable result is a truthful deployment classification for this one
install/remove/rollback cycle. A PASS is limited to independent reversible
deployment evidence. It is not production-readiness acceptance and it does
not close M2 or G4.

## Exact candidates and continuity

Canonical product:

- Remote: https://github.com/cisarik/contextdesk
- Branch: main
- Candidate commit:
  ab10491c49d0b6574b6953a02935a4664c39d7c2

Required AP:

- Gitlink and checkout:
  0cf2cff483a36a4cc2254aa424a7c53bd57a97e9
- ./.ap/ap doctor must pass

Public META:

- Remote: https://github.com/cisarik/meta
- Trace:
  projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
- Current public origin/main:
  c86ae44c2eb3f1bd89ebaf7b175b58279e6f579a
- Accept a later public descendant only if its ancestry is verifiable and it
  contains the current handoff plus the exact Session 23 and Session 24
  prompt/report pairs.
- Current handoff:
  projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/00_handout_02.md
- Session 23 archival commit:
  c964857397ff81bb96f59abbce759dd24effd952
- Session 24 archival pair:
  projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/24_acceptance_00.md
  projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/24_report_00.md

Do not silently retarget the product, branch, AP, candidate, runtime, or
public META identity.

## Runtime and source identities

The documented installed pre-cycle state is:

- Runtime broker baseline:
  cb72ae0388307b514182efc6936712e3da42cda4
- Installed broker pre-cycle SHA-256:
  8e80f2d78530b01d9cda4ab77c4ff75d2888055dadce35fbb9483a15651940a6
- Installed unit pre-cycle SHA-256:
  286154ba6f443adced5dc965b0f0c4da2dfae2a44e4f77edf888c6ef96c30503
- Installed sleep hook pre-cycle SHA-256:
  91e47888a90f3b2c1853f8bd454f1bdeb342a507efb1084767e09480d4eeac8e

The pre-cycle unit hash is intentionally the documented older installed
state. The current candidate unit source has SHA-256:

  5f729a8ebb9b480c2fb1853dd2bc0c101929c9b2f3e728d381907d4dcf70390a

The candidate and pre-cycle unit differ only in comments added by the sleep
hook product commit. Do not treat the documented pre-cycle unit hash as a
candidate identity mismatch; replace it with the current candidate unit and
verify the new hash after installation.

Current candidate source hashes:

- packaging/sysusers.d/contextdeck-broker.conf:
  99868087844ce626c30bdfa1d8ec0945da1783fd7f61022acd1a1c297d983bfc
- packaging/udev/61-contextdeck-input-guard.rules:
  c31ed56d14ba2cd94e73b2883a860c456965ea4a7fb42623aac011cd03d9ea70
- packaging/udev/62-contextdeck-broker.rules:
  070c7c98229a89f89b1ac42253e1a57fa4da927fd299090ed93a81e622a7a5ad
- packaging/udev/99-contextdeck-broker-uinput.rules:
  f10d2d709d047d1648448572cff2cbe35552aa08fe07830a5361cd948471b7b2
- packaging/systemd/contextdeck-broker.service:
  5f729a8ebb9b480c2fb1853dd2bc0c101929c9b2f3e728d381907d4dcf70390a
- packaging/systemd/contextdeck-sleep.sh:
  91e47888a90f3b2c1853f8bd454f1bdeb342a507efb1084767e09480d4eeac8e

The final broker executable must be byte-identical to the verified current
candidate build. The expected reproducible candidate hash is:

  8e80f2d78530b01d9cda4ab77c4ff75d2888055dadce35fbb9483a15651940a6

If the build hash differs, stop before host mutation unless the difference is
explained by the verified candidate and recorded without exposing private
paths. Do not silently accept an unrelated binary.

## Out of scope

Do not test or claim:

- whole M2 or whole G4 closure;
- production readiness or independent production packaging readiness;
- autostart, enablement, automatic ARM, or automatic re-ARM;
- live broker start, restart, stop, lease, ARM, DISARM, reconnect, or IPC;
- any physical G213 grab, pass-through, typing, LED, RGB, or control matrix;
- suspend, resume, hibernate, hybrid sleep, or end-user power actions;
- input-remapper coexistence beyond the read-only state-preservation check;
- crash, watchdog, cutoff, disconnect, teardown, or recovery acceptance;
- new source, test, documentation, AP, product, or META implementation work;
- package-manager installation or removal;
- changes to OpenRGB, KWin, power policy, sudoers, user profiles, or
  unrelated udev/systemd files.

No live input source may be opened. Do not read or emit raw event data.
Do not include raw input, raw event lines, key names, scan values, control
codes, per-event timing, typed content, screenshots, serials, host
addresses, host keys, passwords, credentials, private checkout paths,
private home paths, private temporary paths, or private configuration
contents in the report or any durable trace.

Because this task never starts or ARMs the broker and never opens a physical
source, an independent external recovery route is not required for this
deployment. If any necessary step would start, ARM, open, or grab a live
source, stop immediately and report BLOCKED; route a separate live acceptance
with exactly one demonstrated SSH or second-keyboard recovery route.

## Public-safe read-only path allowlist

Read-only product/AP paths:

- AGENTS.md
- README.md
- ROADMAP.md
- CMakeLists.txt
- .ap/AP.md
- .ap/AP_ORCHESTRATOR.md
- .ap/PROMPT_CONTRACTS.md
- .ap/AP_WORKER.md
- .ap/INFOSEC.md
- docs/architecture.md
- docs/operations.md
- docs/testing-m2.md
- docs/hardware/g213-control-matrix.md
- docs/hardware/g213-zone-map.md
- packaging/sysusers.d/contextdeck-broker.conf
- packaging/udev/61-contextdeck-input-guard.rules
- packaging/udev/62-contextdeck-broker.rules
- packaging/udev/99-contextdeck-broker-uinput.rules
- packaging/systemd/contextdeck-broker.service
- packaging/systemd/contextdeck-sleep.sh
- tests/unit/test_udev_policy.cpp
- tests/unit/test_sleep_hook.sh

Read-only META paths:

- current 00_handout_02.md;
- public Session 16, 19, 22, 23, and 24 prompt/report pairs;
- public history and changed-path summary for the Session 24 archival commit.

The only permitted durable writes are these exact Worker-owned paths:

- projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/25_deployment_00.md
- projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/25_report_00.md

Do not write product source, AP files, build-tracked files, documentation,
packaging, host policy, or any other META path. Ignored build outputs are
allowed only for the documented build and validation.

## Read-only preflight

Before any privileged host operation:

1. Verify the product remote, branch, exact candidate commit, clean product
   worktree, no Git locks or active operations, matching AP gitlink/checkout,
   and ./.ap/ap doctor PASS. A read-only product fetch is allowed if needed.

2. Verify public META origin/main is the stated commit or a verified later
   descendant containing the current handoff and Session 24 pair. Verify
   ancestry and changed paths. Do not require a globally clean META worktree;
   the Worker may have only the two exact Session 25 files as its own
   uncommitted changes.

3. Read the current handoff and the listed deployment/report contracts.
   Verify Session 24 is a bounded acceptance-PASS and remains not-closed.
   Do not rely on a stale roadmap sentence over the current public report.

4. Build the exact candidate with the documented command:

   cmake -S . -B build -G Ninja -DCMAKE_INSTALL_PREFIX=/usr
   cmake --build build
   ctest --test-dir build --output-on-failure

   If the known ambient CMake root problem occurs, use the documented
   sanitized PATH route. Do not install dependencies or change the source.
   A build or CTest failure blocks host mutation. Run the suite once for this
   deployment candidate; do not rerun it to force a verdict.

5. Verify the broker component install manifest contains only the expected
   executable and sleep hook. Record the current build executable hash and
   require it to match the expected candidate hash above before installation.
   Verify source hashes and shell/udev syntax without exposing private paths.

6. Verify the exact pre-cycle host state before any removal:

   - broker executable: regular non-symlink, root-owned, mode 0755, and the
     documented pre-cycle broker hash;
   - broker unit: regular non-symlink, root-owned, mode 0644, and the
     documented pre-cycle unit hash 286154…;
   - sleep hook: regular non-symlink, root-owned, mode 0755, and the
     documented hook hash;
   - sysusers file and all three udev files: regular root-owned files,
     expected modes, and byte-identical to the candidate source;
   - broker unit: static, inactive, dead, MainPID=0, no active invocation,
     not enabled, and no daemon reload pending;
   - no broker process, socket, runtime directory, virtual device, or trial
     timer;
   - the exact broker system identity exists as the documented nologin
     system account, has no unexpected members or processes, and is not the
     session user;
   - input-remapper is enabled/active/running and its configuration is not
     changed by this task;
   - G3 policy is secure: G213 event nodes have no session-user ACL, G213
     hidraw access remains available to the session user, /dev/port and
     /dev/i2c-* have no session-user ACL, and /dev/uinput retains its
     existing identity/mode and required session and broker ACLs.

   Do not expose device node numbers, serials, UIDs/GIDs, ACL dumps, config
   contents, process command lines, or private paths. Report only semantic
   results and equality.

7. If any identity, source hash, pre-cycle hash, type, owner, mode, service
   state, policy, identity ownership, or safety precondition differs, stop
   before removal and report BLOCKED with phase-qualified result
   not-applicable. Do not repair or overwrite an unexplained state.

## Exact owned targets

The cycle may touch only these ContextDesk-owned targets:

- /usr/bin/contextdeck-broker
- /etc/systemd/system/contextdeck-broker.service
- /usr/lib/systemd/system-sleep/contextdeck-broker
- /usr/lib/sysusers.d/contextdeck-broker.conf
- /etc/udev/rules.d/61-contextdeck-input-guard.rules
- /etc/udev/rules.d/62-contextdeck-broker.rules
- /etc/udev/rules.d/99-contextdeck-broker-uinput.rules
- the exact system identity named by the sysusers file:
  contextdeck-broker

Do not use broad globs, recursive deletion, package-manager removal, or
commands that can follow symlinks. Do not alter sibling files, unrelated
users/groups, input-remapper, OpenRGB, or any other policy.

## Owner-executed reversible cycle

The Cooperator owns privileged host commands. The Worker prepares short,
explicit, fail-closed blocks and waits for complete output from each block.
Do not paste a large script or heredoc. Use verified system command paths,
exact target lists, no wildcards, no password in chat, no keep-alive, and no
model-dependent emergency action.

Use the AP owner-terminal lifecycle: the Cooperator authenticates with the
OS sudo prompt in the same reachable terminal, verifies noninteractive
authorization for the bounded block, runs the block, captures its semantic
markers and exit status, and releases the sudo timestamp after the block.
The Worker must never see or record credentials. If Worker-side sudo is
unavailable, use the authorized Cooperator-owned route; do not fabricate
privilege evidence.

### Checkpoint and remove

1. In one bounded owner block, create a uniquely named root-owned private
   temporary checkpoint with mode 0700. Verify it is not a symlink. Copy
   only the seven existing regular files above, preserving bytes, owner, and
   mode. Record only semantic checkpoint success; never report its path.

2. In the same bounded owner block or an immediately continuing block, verify
   again that the unit remains inactive and no broker process exists. Remove
   only the seven exact files, then reload udev rules, trigger only the
   documented input/i2c/port/uinput policy paths, and run systemd daemon-reload.
   Remove the exact system identity only after the files are absent and no
   process or group member uses it. Do not stop a unit; the preflight required
   it to be inactive.

3. Read back the removal semantically: all seven files absent, exact broker
   identity absent, unit not loaded/enabled, no broker process/socket/runtime
   or virtual device, and input-remapper still enabled/active. Record a
   bounded marker such as REMOVE_VERIFIED, never a raw transcript.

### Immediate rollback

4. Restore the seven files byte-for-byte from the checkpoint, preserving
   expected root ownership and modes. Recreate the exact system identity
   from the candidate sysusers file using the documented systemd-sysusers
   procedure. Reload udev rules, trigger only the documented policy paths,
   and run systemd daemon-reload.

5. Read back the rollback immediately in the same owner-controlled sequence:
   all seven files present and byte-identical to their pre-cycle checkpoint,
   expected identity present, secure G3 policy restored, input-remapper
   unchanged, broker static/inactive/dead with MainPID=0, and no runtime.
   Record ROLLBACK_VERIFIED. If rollback fails, stop and keep the checkpoint
   for recovery; do not continue to candidate installation.

### Install the current candidate

6. After rollback is independently read back, install the current candidate
   using only the documented operations:

   - install the candidate sysusers file and run systemd-sysusers;
   - install the three candidate udev rules;
   - reload udev rules and run only the documented bounded triggers;
   - install the broker component from the verified build, which installs
     the candidate broker executable and sleep hook;
   - install the candidate broker unit;
   - run systemd daemon-reload.

   Do not enable, start, restart, stop, arm, lease, connect to, or manually
   invoke the broker. Installing and reloading definitions do not grant a
   start. Do not invoke the sleep hook in production mode.

7. Run final readback only after every owner command completes. If any
   installation command fails, restore the checkpoint or the last verified
   secure state using exact targets, then report the original failure and
   recovery result separately. Do not retry a failed destructive step with a
   new broad command.

## Required final readback

Worker-independent and owner-attributed evidence must establish:

| Object | Required final state |
|---|---|
| Broker executable | regular non-symlink, root-owned, mode 0755, byte-identical to the verified candidate build, expected candidate hash |
| Broker unit | regular non-symlink, root-owned, mode 0644, byte-identical to current source, SHA-256 5f729… |
| Sleep hook | regular non-symlink, root-owned, mode 0755, byte-identical to current source, SHA-256 91e478… |
| Sysusers and udev | all four regular root-owned files, expected modes, byte-identical to current source hashes |
| System identity | exact nologin system account/group present, no unexpected members/processes, no session-user membership |
| Effective unit | static, inactive, dead, MainPID=0, no active invocation, no enablement, no pending daemon reload |
| Broker runtime | no process, socket, runtime directory, virtual device, or trial timer |
| G3 event policy | G213 event nodes have no session-user ACL and use the broker group policy |
| G3 RGB policy | G213 hidraw session access remains available |
| Other raw-I/O policy | /dev/port and /dev/i2c-* have no session-user ACL |
| uinput policy | existing owner/group/mode and session-user ACL remain, broker ACL present, access checks succeed without opening or injecting |
| input-remapper | enabled/active/running state and configuration unchanged |
| checkpoint | removed only after successful final readback, or retained for recovery on failure |
| Git/AP | product/AP identity unchanged; no product/AP Git mutation; no META commit or push |

An inactive unit may report WatchdogUSec=infinity in systemd's effective
properties. Verify WatchdogSec=2 in the candidate file and do not treat that
inactive representation alone as a mismatch. Verify the final unit has
Type=notify, NotifyAccess=main, Restart=no, TimeoutStopSec=5,
TimeoutAbortSec=5, RuntimeDirectoryMode=0755, ProtectHome=yes, and no
[Install] section.

## Classification

Use PASS with phase-qualified result deployment-PASS only if:

- the exact pre-cycle state passed preflight;
- REMOVE_VERIFIED and ROLLBACK_VERIFIED are both evidenced;
- current candidate installation completed;
- all final identity, hash, mode, service, policy, input-remapper, and
  no-runtime checks passed;
- the checkpoint was handled truthfully; and
- no excluded live or product mutation occurred.

Use PARTIAL with a deployment-qualified result when useful bounded evidence
exists but one required install/remove/rollback or final-readback claim is
incomplete. Use BLOCKED with phase-qualified result not-applicable when a
precondition or collision prevents the cycle before a valid outcome.

Never claim production readiness, whole G4, whole M2, autostart, hibernate,
hybrid-sleep, general input-remapper coexistence, live recovery, or physical
keyboard safety from this deployment. State exactly:

Logical-whole closure: not-closed

## Worker-owned prompt and report persistence

The Worker owns physical persistence of both exact exchange files. The
Cooperator must not copy/paste, reconstruct, rename, or manually save either
file.

Immediately after receiving this prompt and before consequential host work:

1. Resolve the Cooperator-provided or Worker-created META checkout for the
   public remote above.
2. Verify the exact trace directory, all parents, symlink status, and
   filename collisions.
3. Write the exact received prompt bytes to:

   projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/25_deployment_00.md

4. Read the file back completely and verify byte identity with the received
   prompt. If the destination exists with non-identical content, stop before
   host work and report the collision.

After the bounded outcome, write the complete terminal report first to:

projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/25_report_00.md

Read the report back completely and verify its identity before terminal
notification. Do not overwrite a non-identical existing report and do not
choose another filename. The Worker may write only these two exact files;
Worker Git commit and push are not authorized.

## Terminal report contract

The report must begin exactly:

### Report for ORCHESTRATOR_CHAT

It must contain exactly one coordinate echo:

Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 25
Worker exchange ordinal: 01

Also include:

- candidate, AP, current public META, handoff, and runtime identities;
- complete pre-cycle, removal, rollback, and final state classifications;
- build and CTest results plus source and installed hashes/modes/types;
- owner-versus-Worker evidence attribution and privilege release;
- REMOVE_VERIFIED and ROLLBACK_VERIFIED evidence;
- secure G3 policy and unchanged input-remapper semantic result;
- explicit statement that no broker start/ARM/grab or live source open occurred;
- checkpoint disposition without its path;
- Git actions, stating no product/AP Git mutation and no META commit/push;
- missing evidence and residual risks;
- exactly one report justification: changed-external-state;
- exactly one smallest next step;
- compact Orchestration critique with MEASURED: and LEAD: (none allowed);
- Logical-whole closure: not-closed;
- authority expiry.

Do not include control names, scan values, raw events, typed content,
screenshots, serials, addresses, host keys, passwords, private paths,
private configuration contents, numeric UID/GID values, node numbers, or
unredacted command transcripts. Use public repository-relative paths and
semantic system-state descriptions only.

The report is English. After complete readback, notify the Cooperator briefly
in Slovak with the truthful result and exact relative report path. Do not
require the Cooperator to copy/paste the report into META. The Cooperator
publishes the exact prompt/report pair separately. Worker authority expires
at the terminal report.

## Delivery record

Delivery mode: file-based; no Cooperator copy-paste
Downloadable prompt filename: 25_deployment_00.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: this WORKER
Report filename: 25_report_00.md
Report persistence owner: this WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Stop after the terminal report. Do not continue to documentation, hibernate,
G7, autostart, or any acceptance phase under this grant.
