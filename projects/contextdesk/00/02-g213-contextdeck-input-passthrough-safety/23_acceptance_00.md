# ContextDesk — LED-return and all-control fidelity acceptance

ROLE: WORKER

Use a genuinely fresh Worker session. Do not dispatch subagents. Speak Slovak to the Cooperator; write the terminal report in English.

Logical whole:
g213-contextdeck-input-passthrough-safety

Worker-session ordinal: 23
Worker-exchange ordinal: 01
Worker-session target: fresh-worker-session
Phase: acceptance
Native planning mode: not-used
Worker-session profile: Fresh Independent Acceptance Worker — LED return and all-control fidelity
Reasoning recommendation: High
Evidence tier: E3

The single bounded outcome is independent acceptance of the remaining LED-return and measured all-control fidelity slice for the unchanged public product candidate. This is not whole-G4 or whole-M2 closure.

## Exact candidates and public identity

Canonical product:

- Remote: https://github.com/cisarik/contextdesk
- Branch: main
- Candidate commit: ab10491c49d0b6574b6953a02935a4664c39d7c2

Required AP:

- Gitlink and checkout: 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9
- `./.ap/ap doctor` must pass

Public META trace:

- Remote: https://github.com/cisarik/meta
- Trace: `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/`
- Current public descendant verified during routing: `0c8a1631459789815e70a7f4976edf8ee7f03629`
- This descendant contains the complete public prompt/report pairs for Sessions 21 and 22. Do not silently retarget to another product or AP commit.

Runtime baseline:

- Broker baseline: cb72ae0388307b514182efc6936712e3da42cda4
- Installed broker SHA-256: 8e80f2d78530b01d9cda4ab77c4ff75d2888055dadce35fbb9483a15651940a6
- Installed systemd unit SHA-256: 286154ba6f443adced5dc965b0f0c4da2dfae2a44e4f77edf888c6ef96c30503
- Installed sleep hook SHA-256: 91e47888a90f3b2c1853f8bd454f1bdeb342a507efb1084767e09480d4eeac8e

## Measurable acceptance outcome

PASS is allowed only when all of these are independently supported:

1. The broker returns compositor LED state to the physical G213 through the intended physical interface during one explicit armed trial.

2. The LED-return failure semantics are supported by the existing deterministic production test and source-path evidence:
   - the physical LED write failure is surfaced as the documented bounded failure;
   - the documented behavior remains no automatic broker disarm caused solely by that LED write failure;
   - no typing or pass-through claim is converted into a per-key RGB claim.

3. All eighteen host-remappable controls from the measured G213 matrix are individually exercised once through the armed pass-through path:
   - twelve matrix entries on interface `if00`;
   - six matrix entries on interface `if01`;
   - the two firmware-only entries are excluded;
   - the unresolved extra observation is not counted or guessed as a mapping contract.

4. The broker is explicitly disarmed and finally inactive/dead with no grabbed source, no virtual device, no active process, and unchanged host policy.

Record only semantic per-entry pass/fail and aggregate counts in the report. Do not record key names, scan codes, raw event lines, typed text, screenshots, serials, addresses, host keys, secrets, or private paths.

## Out of scope

Do not claim or test:

- whole G4 or whole M2 closure;
- Sessions 16, 19, or 22 again;
- watchdog death, SIGSTOP, cutoff death, held-modifier recovery, or crash recovery;
- suspend, hibernate, hybrid sleep, or suspend-then-hibernate;
- input-remapper coexistence beyond this bounded slice;
- install, remove, rollback, packaging, or production readiness;
- autostart or automatic ARM;
- G7 power-action acceptance;
- firmware-only controls;
- unresolved extra observations;
- per-key RGB;
- source, documentation, AP, or META implementation changes.

No second physical keyboard is required or permitted as a second route. SSH is the sole independent recovery route for this trial.

## Public-safe path allowlist

Read-only product paths:

- `AGENTS.md`
- `.ap/AP.md`
- `.ap/AP_ORCHESTRATOR.md`
- `.ap/PROMPT_CONTRACTS.md`
- `.ap/AP_WORKER.md`
- `docs/architecture.md`
- `docs/operations.md`
- `docs/testing-m2.md`
- `docs/hardware/g213-control-matrix.md`
- `docs/hardware/g213-zone-map.md`
- `src/broker/`
- `tests/unit/test_broker_production.cpp`
- `tests/unit/test_broker_forwarding.cpp`
- relevant existing build outputs

Read-only host checks:

- product/AP identity and worktree state;
- installed broker, unit, and sleep-hook identity;
- systemd unit state;
- existing input-remapper state;
- bounded runtime status and journal observations;
- no preflight opening of physical event or uinput nodes.

The only permitted durable write is the exact Worker report path specified below. No product source, documentation, AP, packaging, udev rule, ACL, unit, hook, or META history may be changed.

Building existing test targets is allowed if required. Do not install anything and do not run a full product installation.

## Read-only preflight

Before any broker start, ARM, physical grab, or source open:

1. Verify the physical product root, remote, branch, exact candidate commit, clean worktree, no Git operation in progress, matching AP gitlink/checkout, and `./.ap/ap doctor`.

2. Verify the installed broker and unit are regular non-symlink files with the exact hashes above. Verify the installed sleep hook has the exact hash above.

3. Verify the broker is `static`, `inactive`, `dead`, with `MainPID=0`, no active invocation, no broker process, no broker socket, and no ContextDeck virtual device.

4. Verify input-remapper policy is unchanged. Do not stop, restart, disable, reconfigure, or otherwise manipulate input-remapper.

5. Run the focused deterministic tests without physical devices:
   - `test_broker_production`
   - `test_broker_forwarding`
   - any directly required existing test target needed to verify the unchanged candidate

   The production test must cover measured capability construction, LED routing to the intended interface, and the documented simulated LED-write failure behavior. If the focused tests cannot be built or run, report that limitation and do not invent a PASS.

6. Read the current source and matrix documentation to prepare an eighteen-entry private checklist. The checklist may contain the exact matrix labels locally, but no names, codes, raw events, or typed content may enter the report or META.

7. Prepare the candidate session application and a disposable unsaved content-free observation surface if needed. Do not save typed content, capture screenshots, or expose captions or text in the report.

If any identity, runtime, policy, or safety precondition differs, stop before start/ARM and report `BLOCKED` with phase-qualified result `not-applicable`.

## Mandatory independent recovery gate

Use exactly one recovery route:

SSH from another device, independently demonstrated before broker start and before ARM.

The Cooperator must execute a prepared, exact, read-only recovery proof from that other device and leave the route usable throughout the trial. The proof must demonstrate that the route can perform:

- bounded broker status readback;
- an exact unit-scoped stop command;
- final status readback.

Prepare the emergency stop/status commands before the broker is started. No model round-trip, prompt discovery, address lookup, or command composition may be needed while the broker is armed.

Record only successful reachability and bounded state. Never record host keys, passwords, addresses, serials, environment dumps, or private paths.

If SSH cannot execute the prepared readback and stop commands, stop before starting or arming and report `BLOCKED`.

## One bounded live trial

After all preflight and the SSH gate pass:

1. Start the static broker exactly once. Do not enable, restart, reload, daemon-reload, or start any second time.

2. Verify active/running state, a fresh invocation, `armed=0`, no lease, and no virtual device before ARM.

3. Rehearse the existing GUI ARM path while still disarmed. Cancel the rehearsal and return to the disarmed state.

4. Perform exactly one authenticated GUI ARM. Require authoritative broker evidence of `armed=1`; a transient client label or lease acknowledgment alone is insufficient.

5. LED-return observation:
   - exercise prepared compositor-managed LED state transitions without saving or logging input content;
   - observe the physical G213 LED response;
   - confirm that the behavior is five-zone/device-level only, never per-key RGB;
   - record only semantic success/failure.

6. All-control observation:
   - exercise each of the eighteen measured host-remappable matrix entries exactly once with a press/release;
   - use a content-free ephemeral observation method;
   - verify twelve entries on `if00` and six on `if01`;
   - do not count the two firmware-only entries;
   - do not count or infer the unresolved extra observation;
   - do not persist raw observer output, names, codes, or typed text.

7. Keep the SSH route available during the entire armed window. If the G213 becomes unsafe, the application becomes unresponsive, the broker state is ambiguous, or the route fails, use the prepared exact stop command immediately and classify the affected claim truthfully. Do not retry with a second start or ARM.

8. Explicitly disarm once through the existing authenticated application path if it remains usable. Then stop the unit through the prepared owner/recovery path and verify:

   - no broker process;
   - no virtual device;
   - no grabbed physical source;
   - no lease;
   - no active trial resource;
   - `static/inactive/dead`;
   - `MainPID=0`;
   - unchanged installed hashes;
   - unchanged input-remapper and host policy.

No suspend, cutoff, watchdog, crash, or second live trial is allowed.

## Report classification

Use:

- `PASS` / `acceptance-PASS` only when deterministic LED failure evidence, live LED return, all eighteen matrix entries, SSH recovery availability, and final cleanup all pass.
- `PARTIAL` when useful bounded evidence exists but one required claim is missing or incomplete.
- `BLOCKED` with `not-applicable` when a precondition prevents the trial.

Always state:

`Logical-whole closure: not-closed`

Never claim full G4, full M2, production readiness, autostart, hibernate support, general input-remapper coexistence, or complete RGB claims.

## Report persistence

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 23_acceptance_00.md
Destination path: /home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
Report filename: 23_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: this WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

You are explicitly authorized and required to create:

`/home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/23_report_00.md`

before terminal notification.

This is exact report-file preparation only. Do not add, commit, push, rewrite, or delete META history. Verify the physical directory, parents, symlink status, and collision before writing. Preserve any existing non-identical file and never choose an alternate filename. If persistence fails, report the failure and provide the complete report as fallback. Never claim saved bytes without complete readback.

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

It must contain exactly one coordinate set echoing this prompt, candidate/AP/runtime identities, deterministic test results, SSH proof, live LED result, aggregate all-eighteen result, interface aggregates, final cleanup, privilege attribution, unchanged policy, Git actions, missing evidence, one smallest next step, exactly one report justification (`new-evidence` or `changed-external-state`), compact `Orchestration critique` with `MEASURED` and `LEAD` (`none` allowed), resolved/pre-existing failures, `Logical-whole closure: not-closed`, and authority expiry.

Do not include raw events, key names, scan codes, typed text, screenshots, serials, passwords, host keys, network addresses, or private paths.

Read the report back completely and verify its identity before notifying the Cooperator.

The Cooperator archives this exact prompt/report pair after the report exists. Worker authority expires at the terminal report.
