# ContextDesk — bounded input-remapper coexistence acceptance

ROLE: WORKER

Use a genuinely fresh Worker session. Worker 23 authority is expired.
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
Worker session ordinal: 24
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Phase: acceptance
Native planning mode: not-used
Worker-session profile: Fresh Independent Acceptance Worker — bounded input-remapper coexistence
Reasoning recommendation: High
Recommended context capacity: approximately 128k tokens; advisory only
Evidence tier: E3
Evidence tier basis: protected live G213 grab, independent input-remapper state and behavior, SSH recovery, and final cleanup

The named live slices from Sessions 16, 19, 22, and 23 are historical
context only. Their authority is expired. This Worker must not repeat or
reclassify those slices.

## Single bounded outcome

The single bounded outcome is independent acceptance of one input-remapper
coexistence slice:

1. Leave the existing input-remapper installation, daemon state, and
   configuration unchanged.
2. Privately select exactly one already-configured non-G213 input-remapper
   mapping. Do not record its device name, control name, output name, or
   implementation details.
3. Observe its semantic result once before the broker starts, once while the
   broker is explicitly armed and holding the G213, and once after explicit
   DISARM and broker stop.
4. During the same armed window, observe one preselected host-remappable
   G213 matrix entry on if00 and one on if01. Report only aggregate
   `if00=1/1` and `if01=1/1`; never report labels, codes, raw events, or
   typed content.
5. Verify that input-remapper remains enabled/active and unchanged throughout,
   and that the final broker state is inactive/dead with no grabbed G213
   source and no virtual device.

This is a bounded coexistence result only. It is not general
input-remapper coexistence, whole-G4 acceptance, whole-M2 acceptance, or
production readiness.

## Exact candidates and public identity

Canonical product:

- Remote: https://github.com/cisarik/contextdesk
- Branch: main
- Candidate commit:
  `ab10491c49d0b6574b6953a02935a4664c39d7c2`

Required AP:

- Gitlink and checkout:
  `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`
- `./.ap/ap doctor` must pass

Public META:

- Remote: https://github.com/cisarik/meta
- Trace:
  `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/`
- Current public descendant:
  `724c2694225b72ea671912b19bd6a02d251ae264`
- Current handoff:
  `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/00_handout_02.md`
- Session 23 archival commit:
  `c964857397ff81bb96f59abbce759dd24effd952`

Runtime baseline:

- Broker baseline:
  `cb72ae0388307b514182efc6936712e3da42cda4`
- Installed broker SHA-256:
  `8e80f2d78530b01d9cda4ab77c4ff75d2888055dadce35fbb9483a15651940a6`
- Installed unit SHA-256:
  `286154ba6f443adced5dc965b0f0c4da2dfae2a44e4f77edf888c6ef96c30503`
- Installed sleep hook SHA-256:
  `91e47888a90f3b2c1853f8bd454f1bdeb342a507efb1084767e09480d4eeac8e`

Do not silently retarget product, branch, AP, runtime, or META identity.

## Out of scope

Do not test or claim:

- whole M2 or whole G4 closure;
- general input-remapper coexistence;
- input-remapper configuration or G213 preset changes;
- all eighteen controls again;
- LED return or RGB behavior;
- suspend, hibernate, hybrid sleep, or power-action acceptance;
- watchdog, cutoff, crash, held-modifier, or death recovery;
- install, remove, rollback, or production readiness;
- autostart or automatic ARM;
- automatic re-ARM after restart, resume, crash, or reconnect;
- source, documentation, AP, packaging, host-policy, udev, or ACL changes.

No raw input, raw event lines, control names, scan values, per-event timing,
typed content, screenshots, serials, host addresses, host keys, passwords, or
private paths may appear in the report or any durable trace.

## Public-safe path allowlist

Read-only product/AP paths:

- `AGENTS.md`
- `README.md`
- `ROADMAP.md`
- `CMakeLists.txt`
- `.ap/AP.md`
- `.ap/AP_ORCHESTRATOR.md`
- `.ap/PROMPT_CONTRACTS.md`
- `.ap/AP_WORKER.md`
- `docs/architecture.md`
- `docs/operations.md`
- `docs/testing-m2.md`
- `docs/hardware/g213-control-matrix.md`
- `docs/hardware/g213-zone-map.md`
- `src/broker/Acquisition.cpp`
- `src/broker/Acquisition.h`
- `src/broker/DeviceEnumerator.cpp`
- `src/broker/DeviceEnumerator.h`
- `src/broker/EvdevGrabber.cpp`
- `src/broker/EvdevGrabber.h`
- `src/broker/EvdevSource.cpp`
- `src/broker/EvdevSource.h`
- `src/broker/ForwardingEngine.cpp`
- `src/broker/ForwardingEngine.h`
- `src/broker/ProductionRuntime.cpp`
- `src/broker/ProductionRuntime.h`
- `src/broker/SessionIpc.cpp`
- `src/broker/SessionIpc.h`
- `src/app/BrokerIpcClient.cpp`
- `src/app/BrokerIpcClient.h`
- `src/app/AppController.cpp`
- `src/app/AppController.h`
- `src/app/TrayController.cpp`
- `src/app/TrayController.h`
- `tests/unit/test_broker_acquisition.cpp`
- `tests/unit/test_broker_forwarding.cpp`
- `tests/unit/test_broker_production.cpp`
- `tests/unit/test_broker_ipc.cpp`
- `tests/unit/test_broker_ipc_client.cpp`

Read-only META paths:

- current `00_handout_02.md`;
- the public Session 16, 19, 22, and 23 prompt/report pairs.

The only permitted durable writes are the exact Worker-owned paths below:

- `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/24_acceptance_00.md`
- `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/24_report_00.md`

Do not write product, AP, packaging, host-policy, or any other META path.

## Read-only preflight

Before any broker start, ARM, physical grab, or source open:

1. Verify product remote, branch, exact candidate commit, clean worktree,
   matching AP gitlink/checkout, and `./.ap/ap doctor`.

2. Verify public META `origin/main` is
   `724c2694225b72ea671912b19bd6a02d251ae264` or a verified later descendant
   containing the current handoff and Session 23 pair.

3. Verify the installed broker, unit, and sleep hook are regular non-symlink
   files with the exact hashes above.

4. Verify the broker is `static`, `inactive`, `dead`, with `MainPID=0`, no
   active invocation, no broker process, no broker socket, no virtual device,
   and no active sleep marker.

5. Verify input-remapper is enabled/active, its existing configuration is
   readable, and at least one configured non-G213 mapping is available.
   Do not stop, restart, enable, disable, reconfigure, or otherwise manipulate
   input-remapper.

6. Run only focused deterministic tests relevant to the unchanged candidate:

   - `test_broker_acquisition`
   - `test_broker_production`
   - `test_broker_forwarding`
   - `test_broker_ipc`
   - `test_broker_ipc_client`

   If a required focused test cannot be built or run, report that limitation
   and do not claim PASS. Do not run a full product installation or full
   hardware test suite.

7. Read the relevant source and matrix documentation. Prepare any exact
   private checklist locally, but do not persist control names, codes, raw
   events, or typed content.

8. Prepare a content-free observation surface for the selected remapper
   mapping. Do not save content or capture screenshots.

If any identity, runtime, input-remapper, test, or safety precondition differs,
stop before start/ARM and report `BLOCKED` with phase-qualified result
`not-applicable`.

## Mandatory independent recovery route

Use exactly one recovery route:

SSH from another device.

No second physical keyboard is required or requested.

Before broker start and before ARM, demonstrate the route from the already
prepared SSH shell. Prepare and retain these exact unit-scoped commands:

```text
sudo -n systemctl show --no-pager --plain \
  --property=ActiveState,SubState,MainPID,InvocationID,Result \
  contextdeck-broker.service

sudo -n systemctl stop contextdeck-broker.service

sudo -n systemctl show --no-pager --plain \
  --property=ActiveState,SubState,MainPID,InvocationID,Result \
  contextdeck-broker.service
```

The proof must show successful reachability, bounded status readback, a
successful stop command against the already inactive unit, and final bounded
status readback. The Cooperator handles any operating-system password prompt.
The Worker must not see or record credentials.

Keep the SSH route usable throughout the armed window. If the G213 or GUI
becomes unsafe, the broker state becomes ambiguous, or the application stops
responding, use the prepared exact stop command immediately. No model
round-trip, address lookup, host-key lookup, or command composition may be
needed while the broker is armed.

Record only semantic readiness such as `SSH_READY`. Never record addresses,
host keys, passwords, or private paths.

## One bounded live trial

1. From `static/inactive/dead`, observe the selected existing non-G213
   input-remapper mapping once. Record only semantic success or failure.

2. Start `contextdeck-broker.service` exactly once. Do not enable, restart,
   reload, daemon-reload, or start it a second time.

3. Verify active/running state, a fresh invocation, `armed=0`, no lease, and
   no virtual device before ARM.

4. Rehearse the existing GUI ARM action while still disarmed. Cancel the
   rehearsal and return to the disarmed state.

5. Perform exactly one authenticated GUI ARM. Require authoritative broker
   evidence of `armed=1`; a transient GUI label or lease acknowledgement alone
   is insufficient.

6. While the broker is armed:

   - exercise one preselected host-remappable matrix entry on if00 and one
     on if01, recording only `if00=1/1` and `if01=1/1`;
   - exercise the selected existing non-G213 input-remapper mapping once;
   - observe the same semantic result as before ARM;
   - verify input-remapper remains active without a daemon restart or policy
     change.

7. Keep SSH available for the whole armed window. If any safety condition
   fails, stop via the prepared exact command and classify the affected claim
   truthfully. Do not retry with a second start or ARM.

8. Explicitly DISARM once through the existing authenticated application path
   if it remains usable. Stop the broker once through the owner/recovery path.

9. After DISARM and stop, verify:

   - no broker process;
   - no virtual device;
   - no grabbed physical source;
   - no lease;
   - `static/inactive/dead`;
   - `MainPID=0`;
   - unchanged installed hashes;
   - input-remapper still active;
   - unchanged input-remapper configuration and host policy.

10. Observe the same selected input-remapper mapping once after cleanup.
    Record only semantic success or failure.

Do not modify input-remapper, KWin, OpenRGB, udev, ACLs, power policy, the
sleep hook, or the systemd unit.

## Worker-owned prompt and report persistence

The Worker owns physical persistence of both exact exchange files. The
Cooperator must not copy/paste, reconstruct, rename, or manually save either
file.

Immediately after receiving this file and before consequential live work:

1. Resolve the Cooperator-provided or Worker-created META checkout for the
   public remote above.
2. Verify the exact trace directory, all parents, symlink status, and filename
   collisions.
3. Write the exact received prompt bytes to:

   `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/24_acceptance_00.md`

4. Read the file back completely and verify byte identity with the received
   prompt. If the destination contains non-identical content, stop before any
   live work and report the collision.

After the bounded outcome, write the complete terminal report first to:

`projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/24_report_00.md`

Read the report back completely and verify its identity before terminal
notification. Do not overwrite a non-identical existing report and do not
choose another filename. The Worker may write only these two exact files;
Worker Git commit and push are not authorized.

## Report classification

Use:

- `PASS` / `acceptance-PASS` only when the selected mapping succeeds before,
  during, and after the armed window; `if00=1/1` and `if01=1/1` are observed;
  SSH recovery passes; explicit ARM and DISARM pass; and cleanup passes.
- `PARTIAL` when useful bounded evidence exists but one required claim is
  missing or incomplete.
- `BLOCKED` with `not-applicable` when a precondition prevents the trial.

Always state:

`Logical-whole closure: not-closed`

Never claim general input-remapper coexistence, full G4, full M2, production
readiness, autostart, hibernate support, or complete control-matrix coverage.

## Delivery record

```text
Cooperator delivery / trace destination: configured
Delivery mode: file-based; no Cooperator copy-paste
Downloadable prompt filename: 24_acceptance_00.md
Destination path: projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: this WORKER
Report filename: 24_report_00.md
Report persistence owner: this WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

It must contain exactly one coordinate echo:

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 24
Worker exchange ordinal: 01
```

The report must also contain:

- candidate, AP, META, and runtime identities;
- focused deterministic test results;
- SSH proof and privilege attribution;
- input-remapper semantic results as baseline/armed/post only;
- G213 aggregate results only as `if00=1/1` and `if01=1/1`;
- explicit ARM and DISARM;
- final cleanup and unchanged policy;
- Git actions, stating that no Worker product/AP/META Git mutation occurred;
- missing evidence;
- exactly one report justification: `new-evidence` or
  `changed-external-state`;
- exactly one smallest next step;
- compact `Orchestration critique` with `MEASURED:` and `LEAD:`
  (`none` is allowed);
- `Logical-whole closure: not-closed`;
- authority expiry.

Do not include control names, scan values, raw events, typed content,
screenshots, serials, addresses, host keys, passwords, or private paths.

Stop after the terminal report. Worker authority expires at that point.
