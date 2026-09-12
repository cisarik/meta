# ContextDesk — suspend/resume lifecycle recovery

## Identity and one bounded implementation outcome

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 20
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Implementation Worker — suspend/resume safe lifecycle
Phase: implementation
Task identity: CONTEXTDESK-9A89095-SUSPEND-RESUME-LIFECYCLE
Delivery: manual
Reasoning recommendation: High
Recommended context capacity: approximately 128k tokens; not a provider capacity attestation
Selected model: Cooperator choice; record actual client/model/reasoning only when observable
Evidence tier: E2
Evidence tier basis: repository implementation, deterministic tests, packaging inspection, and public readback; no live suspend in this task
```

Use a genuinely fresh Worker session. Worker 19 authority is expired. Do not dispatch subagents. Speak Slovak to the Cooperator; write the terminal report in English. Your one outcome is a small, reviewable implementation of safe broker suspend/resume lifecycle recovery on the unchanged ContextDesk architecture. Do not perform a live suspend, start the installed broker, ARM the G213, open event/uinput nodes, or make host/power-policy changes in this session.

The current requirement is not “hide the watchdog failure”. The product must treat suspend/resume as a normal lifecycle boundary:

1. Before system sleep, an active broker must be quiesced and stopped before the machine freezes, so an armed grab is released and `WatchdogSec=2` cannot kill an otherwise healthy frozen process.
2. After resume, the broker may be started once **only if it was active immediately before that sleep cycle**. It must always start disarmed, with no lease, no virtual device, and no automatic re-grab. An inactive or failed broker must not be silently started.
3. The session application must be able to reconnect to the post-resume socket using its existing bounded retry path and must not silently restore ARM intent. The user can perform the existing explicit ARM action later.
4. A failed pre-sleep stop or post-resume start must be visible in bounded journal diagnostics and must fail closed; no restart loop, power-management mutation, or broad privilege is allowed.

This is the smallest safe recovery baseline. Transparent automatic re-ARM after resume is deliberately out of scope until a separate acceptance proves device re-enumeration, policy freshness, lease semantics, and physical recovery. Do not weaken `Restart=no`, the absent `[Install]` section, or the rule that startup/socket/STATUS/LEASE never arm.

## Exact candidate and accepted continuity

Canonical product checkout: `/home/agile/Projects/contextdesk`; remote `https://github.com/cisarik/contextdesk.git`; branch `main`; expected product `HEAD`:

```text
9a89095d97bde1cdb8ec989f06f83fcc780b8280
```

Runtime candidate remains `cb72ae0388307b514182efc6936712e3da42cda4`; Worker 17's public change was documentation-only. Required AP gitlink and checkout: `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`; `./.ap/ap doctor` must pass. Do not silently retarget to another product commit. If `origin/main` has moved, read the public diff and stop for divergence rather than merging unrelated work.

META: `/home/agile/meta`, remote `https://github.com/cisarik/meta.git`; trace directory `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/`. Public META latest commit is `1bf6a913e21c309d78eff8d742f19be678731d8f`, containing Worker 19's exact acceptance prompt/report. Worker 19 is `acceptance-PASS` for the armed SIGSTOP/watchdog/held-modifier recovery slice, not whole-G4. META is historical evidence and Cooperator-owned for Git archival. Do not modify META except the exact report-file preparation granted below.

```text
Implementation candidate: 9a89095d97bde1cdb8ec989f06f83fcc780b8280
Runtime baseline: cb72ae0388307b514182efc6936712e3da42cda4
AP pin: 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9
Implementation owner map: broker/service lifecycle; packaging/systemd sleep integration; session IPC reconnect invariants; operations/architecture/testing documentation
Implementation allowlist: source, tests, packaging files, and directly affected product docs; repository build/test; one product commit and push to main
Implementation risk claims: pre-sleep broker quiescence; active-before-sleep-only restart; disarmed post-resume state; no silent re-ARM; bounded failure diagnostics; no persistent host mutation
Implementation control matrix: sleep-mode filtering; authenticated broker stop/disarm; state-marker integrity; post-resume conditional start; stale-marker and failed-stop handling; client reconnect without ARM; deterministic tests
Implementation independence: required-fresh-independent
Primary fresh implementations used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named implementation outcome: safe suspend/resume lifecycle recovery for the broker and session client
Out-of-scope: live suspend, live broker start/ARM, host installation, udev/ACL changes, watchdog redesign, automatic ARM, autostart enablement, full-G4 closure
```

Read only the applicable `AGENTS.md`, pinned AP Worker/report contracts, Worker 17 documentation report, Worker 19 acceptance report, `docs/architecture.md`, `docs/operations.md` §6–§9, `docs/testing-m2.md`, the broker service, CMake install rules, `BrokerIpcClient`, and relevant unit tests. Do not reread the whole META archive or redesign RGB/context features.

## Required design contract

Before editing, write a short design note in the Worker report and, if the chosen mechanism is non-obvious, an ADR under `docs/adr/`. The preferred mechanism is a narrowly scoped **systemd system-sleep integration** which runs as root only during `pre`/`post` sleep phases and records one ephemeral, root-owned “broker was active” fact. A different mechanism is allowed only if it has the same fail-closed semantics and is explained in the report. Do not add a permanent daemon, watchdog helper thread, shell execution to the broker, or a generic autostart unit.

The implementation must satisfy all of these invariants:

- Handle `suspend`, `hibernate`, `hybrid-sleep`, and `suspend-then-hibernate`; ignore unrelated system-sleep modes without touching the broker.
- On `pre`, inspect the exact system unit state. If and only if `ActiveState=active` (not merely enabled, static, failed, or present), atomically create a root-owned, mode-safe ephemeral marker outside the broker's removable `RuntimeDirectory`, then stop `contextdeck-broker.service` through the exact unit name and wait for the bounded service stop. If it is not active, remove/avoid a marker and do nothing.
- The stop path must preserve the existing broker teardown order on orderly SIGTERM: ungrab physical sources, balance synthetic state, destroy the virtual device, release the lease/socket, and leave the unit inactive. If the broker is already hung, systemd's existing `TimeoutStopSec=5`/kernel descriptor-close fallback remains the bounded safety path; the hook must not invent a second kill loop.
- On `post`, consume exactly one valid marker. Start the exact broker unit once only when the marker proves it was active before this sleep cycle and the pre-sleep stop completed sufficiently for the unit to be inactive. Starting is still disarmed: no LEASE, ARM, event-node open, uinput creation, or virtual device at startup. If start fails, log a bounded error and leave the unit failed/inactive; do not retry.
- Marker creation/consumption must be race-resistant, root-owned, mode `0600` (or stricter), contain no user-controlled paths, hostnames, passwords, serials, or environment, and never cause a start after reboot or an unrelated sleep. A stale/invalid/malformed marker must be removed and treated as no-restart. Do not use a broad writable directory or a predictable user-owned file.
- The hook must be idempotent for duplicate `post`, duplicate `pre`, aborted sleep, and a pre-phase where the unit changes state concurrently. It may log `skip`, `stop`, `start`, and bounded error classes, but must not disclose private machine details.
- Keep `WatchdogSec=2`, `Restart=no`, `Type=notify`, `NotifyAccess=main`, `RuntimeDirectoryMode=0755`, and no `[Install]`. Do not solve suspend by disabling the watchdog globally, inflating it to minutes, feeding it from another thread, masking sleep targets, or inhibiting user sleep.
- Preserve the existing `BrokerIpcClient` invariant: connection/retry/status probing never arms. On broker stop/restart, any prior lease/ARM intent is invalidated; the post-resume client state must be disconnected/connected/status-only until the user explicitly invokes the existing GUI ARM action. Do not add automatic LEASE/ARM in this task.
- The product must remain safe if the session app is not running, if the broker was unarmed, if the broker was armed, if the device disappears during sleep, or if the post-resume start fails. No stale virtual device or lease may be treated as valid evidence.

The Worker may improve the broker/session code if the chosen mechanism needs an explicit lifecycle hook, but avoid unnecessary source changes. A system-sleep hook may use only exact system commands and a private runtime marker; the broker itself must not invoke `systemctl`, a shell, or D-Bus methods unrelated to its existing IPC/logind authorization.

## Implementation and verification authority

Before edits, record the exact product/AP identity and a clean source worktree. Read-only `git fetch origin main` is permitted. Preserve unexplained user work. Do not install packages, write `/etc`, `/usr/bin`, `/usr/lib`, `/run` outside a test sandbox, alter udev/ACLs, change input-remapper, launch the session app, start the broker, ARM the G213, open event/uinput nodes, invoke suspend/hibernate, or use sudo. No live host mutation is authorized.

Implement only the suspend/resume slice and its tests/docs. Prefer a deterministic test seam for the sleep hook (for example, injectable command/state paths or a fake systemctl harness confined to the build/test directory) rather than a test that calls real `systemctl`, writes `/run`, or sleeps the workstation. Test at least:

1. non-sleep mode is a no-op;
2. inactive/failed/activating broker produces no restart marker;
3. active unarmed broker records, stops, and resumes once;
4. active armed broker takes the same orderly stop path and post-resume state is disarmed/no lease;
5. failed pre-stop never causes post-start;
6. post-start failure is bounded and non-retrying;
7. duplicate phases, stale/malformed marker, concurrent state change, and reboot-like marker absence fail closed;
8. marker permissions/ownership/path restrictions and command arguments are checked;
9. `BrokerIpcClient` reconnect/status after broker loss cannot emit LEASE/ARM without explicit user action;
10. existing full CTest suite still passes, with no test opening real G213 event/uinput nodes.

If a shell hook is used, include a syntax check and a fully simulated fake-systemctl test. If a C++ coordinator is used, include focused unit tests for all state transitions. Do not claim live suspend evidence from simulation.

Update only directly affected documentation: architecture lifecycle/reconnect table, operations recovery/install instructions, M2 watchdog/suspend procedure, and README/ROADMAP/ADR if required. Documentation must state clearly that post-resume restart is conditional on pre-sleep active state, always disarmed, and not automatic re-ARM. Mark the real host suspend acceptance as still open. Do not rewrite historical reports.

## Git delivery

After tests pass, review `git diff`, changed-path allowlist, and secret scan. Commit the complete implementation as one focused commit with a descriptive message and push the current `main` branch to `https://github.com/cisarik/contextdesk.git`. Do not force-push, rewrite history, merge unrelated work, or modify `.ap`. Read back the public commit and changed paths exactly. If push is unavailable, report the local commit and the precise publication blocker; never claim public integration.

## Report and persistence contract

Use status `PASS` and phase-qualified result `implementation-PASS` only if the bounded suspend/resume implementation, deterministic tests, documentation, exact commit, and public push/readback all succeed. Use `PARTIAL` if useful implementation exists but a required test, docs update, commit, or public readback is missing. Use `BLOCKED` if an authority/precondition prevents safe implementation. Always state `Logical-whole closure: not-closed`; no implementation report may claim live suspend acceptance, full G4, production readiness, or autostart.

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 20_implementation_00.md
Destination path: /home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
Report filename: 20_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: this WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

You are explicitly authorized and required to create `/home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/20_report_00.md` before terminal notification for PASS, PARTIAL, or BLOCKED. This is exact report-file preparation only; no META add/commit/push and no historical rewriting. Verify physical parents, real directory, symlinks, and collision; preserve any existing/nonidentical file and never choose an alternate name. If persistence fails, state it and provide the complete report as fallback; never claim saved bytes without complete readback.

The saved report must begin exactly `### Report for ORCHESTRATOR_CHAT`, echo this prompt's one coordinate set, include the design choice and rationale, candidate/AP identities, changed paths, tests and deterministic suspend simulation outcomes, marker/state-machine invariants, client reconnect/no-auto-ARM evidence, commit and public push/readback identities, privilege/host-mutation statement, remaining live suspend evidence, one smallest next step, exactly one report justification (`new-evidence` or `changed-external-state`), compact `Orchestration critique` with `MEASURED`/`LEAD` (`none` allowed), resolved/pre-existing failures, `Logical-whole closure: not-closed`, and authority expiry. Read the report back completely before notifying the Cooperator. The Cooperator archives this exact prompt/report pair after it exists.
