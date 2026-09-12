### Report for ORCHESTRATOR_CHAT

- **logical-whole identity:** `g213-contextdeck-input-passthrough-safety`
- **Worker-session ordinal:** `12`
- **Worker-exchange ordinal:** `03`
- **Worker session target:** `current-worker-session`
- **Native planning mode:** `not-used`
- **Worker session profile:** Fresh Implementation Worker
- **Phase:** implementation
- **Task identity:** `CONTEXTDESK-M2-RECOVERY-CUTOFF-AND-PRODUCTION-SAFETY`
- **status:** **PASS**
- **phase-qualified result:** **implementation-PASS** (R1 production safety + R2 invocation-bound cutoff; no live grab)
- **Report justification:** `new-mutation`
- **Logical-whole closure:** not-closed
- **Independence required:** no for this implementation; **yes** before any physical grab
- **G4 / LEASE / ARM / live device access / physical usability:** not performed, not claimed
- **Independent review:** not performed (this Worker is not independent for that review)
- **Authority:** expires at this terminal report

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 12
Worker exchange ordinal: 03
Worker session target: current-worker-session
Phase: implementation
Task identity: CONTEXTDESK-M2-RECOVERY-CUTOFF-AND-PRODUCTION-SAFETY
```

```text
Implementation authority: explicit
Exact baseline: 64dd12bbc34c5ab09574d8edc76ebb7bed50af2d
AP pin: 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9
Independence required: no for implementation; fresh independent review required before physical grab
G4 acceptance: not claimed
Logical-whole closure: not-closed
```

## Actual status

Same healthy Worker session 12, exchange 03. Continuity anchor `12_report_01.md` / product HEAD `64dd12b` / AP `0cf2cff` verified before edits. Worktree was clean; no Git lock; branch `main`. Native Plan Mode was not used.

R1 and R2 gates passed. Each slice is one fast-forward commit on `origin/main`. Stopped before physical grab, live G4, broker install/start, ARM, LEASE, and independent review.

## Product commits, AP pin, repository, push

| Anchor | Value |
|--------|--------|
| Canonical checkout | `/home/agile/Projects/contextdesk` (`https://github.com/cisarik/contextdesk`) |
| Branch | `main` (tracks `origin/main`) |
| Baseline HEAD | `64dd12bbc34c5ab09574d8edc76ebb7bed50af2d` |
| R1 commit | `2b6cf2cea5f763aef78be136dd995ad4ac602276` — `Fail closed on sink writes and measure capabilities before grab.` |
| R2 commit / end HEAD | `cb72ae0388307b514182efc6936712e3da42cda4` — `Pin broker stop timeouts and add an invocation-bound cutoff.` |
| AP pin (unchanged) | `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9` |
| R1 push | ordinary fast-forward `64dd12b..2b6cf2c` `origin/main` |
| R2 push | ordinary fast-forward `2b6cf2c..cb72ae0` `origin/main` |
| META Git | not modified |

## Files read (this exchange; observed)

Prompt `12_implementation_02.md`; continuity `12_report_01.md` (planning record); prior `12_report_00.md` (report shape only). Product: `AGENTS.md` (workspace rules), `src/broker/{ISink,FakeSink,ForwardingEngine,Acquisition,RealSink,EvdevSource,GrabbingSource,ProductionRuntime,SessionIpc,main,Selftest,WatchdogSelftest,IdleWait,Logger,Types,KeyLedger}.*`, `tests/unit/test_broker_{forwarding,acquisition,production,ipc,watchdog,ledger}.*`, `CMakeLists.txt`, `packaging/systemd/contextdeck-broker.service`, `docs/{architecture,operations,testing-m2}.md`. Protocol fragments: `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md` Worker report header. systemd/libevdev behavior was taken from installed man/API via compile and the user-bus probe (`TimersMonotonic`, `AccuracyUSec=1us`, `NotifyAccess`).

Not claimed unread as read: full `handout.md`, full `AP.md`, `README.md`, `ROADMAP.md` were not re-opened in the implementation half of this exchange.

## Allowlists and out-of-scope proof

### R1 allowlist (commit `2b6cf2c`)

`src/broker/**` and named broker tests only. No `src/app/**`. No CMake. No packaging, docs, udev, or META.

### R2 allowlist (commit `cb72ae0`)

`packaging/systemd/contextdeck-broker.service`; new `packaging/systemd/contextdeck-trial-cutoff.sh`; `tests/unit/test_trial_cutoff.sh`; `tests/unit/rehearse_trial_cutoff.sh`; `docs/operations.md` §§6–9; `docs/testing-m2.md`; `docs/architecture.md` lifecycle/recovery/auth; `CMakeLists.txt` only for `test_trial_cutoff`.

No ROADMAP/AGENTS/README edits. No Meta Git. No `/etc`, udev, packages, OpenRGB, KWin, autostart, input-remapper, or live broker unit mutation.

## R1 implementation (four production gaps)

1. **Fail-closed sink writes.** `ISink::writeEvent` / `flushSyn` return `bool`. `libevdev_uinput_write_event` is no longer discarded. `ForwardingEngine::ingest` returns `bool`, logs bounded `sink-write-failed`, and does not retry. `BrokerLoopWork` disarms on that failure. Cleanup synthetic writes are best-effort; ungrab-first, ledger clear, and destroy still run. Physical `EV_LED` is not forwarded (avoids a loop with the return path).
2. **Measure before claim.** ARM order is open if00, open if01, measure (`EV_KEY` union, `EV_LED` from if00 only, `EV_MSC`, never `EV_REP`), `applyMeasuredCapabilities`, create virtual, `prepareVirtual` (uinput fd + optional epoll), then grab. Any earlier failure closes opened sources and creates no virtual device. Production `main` no longer constructs `passthroughCapabilities()` as the live set.
3. **Virtual LED → physical if00.** Sources open `O_RDWR`. `prepareVirtual` fail-closes before grab (`led-setup-failed`). Runtime LED drain writes if00 only via `libevdev_kernel_set_led_value`. `led-write-failed` is logged and does not disarm.
4. **Narrow logind fallback.** Keep `SO_PEERCRED`, pid>0, non-root, UID match. `sd_pid_get_session` first. Fallback only on `-ENODATA`/`-ENXIO`/`-ENOENT`: enumerate `sd_uid_get_sessions`, accept exactly one eligible active local seated `wayland`/`x11` session. Reject zero, ambiguity, inactive, remote, empty seat, non-graphical, UID mismatch, root, and other lookup errors. Not UID-only.

## R2 implementation

Unit pins: `Type=notify`, `NotifyAccess=main`, `WatchdogSec=2`, `TimeoutStopSec=5`, `TimeoutAbortSec=5`, `Restart=no`, `LimitCORE=0`, `RuntimeDirectoryMode=0755`, no `[Install]`, no `RuntimeMaxSec`, no `EXTEND_TIMEOUT_USEC`.

Helper `packaging/systemd/contextdeck-trial-cutoff.sh`: explicit unit + `InvocationID`; default 30 s (20–45); transient timer `OnActiveSec`, `AccuracySec=1us`, `RandomizedDelaySec=0`, `Persistent=no`, `RemainAfterElapse=no`; re-check identity then `systemctl kill --kill-whom=main --signal=SIGKILL`; no `pkill`/`killall`/guessed PID; no restart; cancel/status paths; setup failure is non-zero / do-not-ARM.

Docs state the 1–9 trial order, optional second keyboard/SSH, PID1/kernel/power/session limits, and that a cutoff kill is not a watchdog PASS.

## Validation

```text
R1 focused CTest (forwarding, acquisition, production, ipc, watchdog, ledger, identity): 7/7 PASS
R1+R2 full CTest: 13/13 PASS (includes new test_trial_cutoff)
./build/contextdeck-broker selftest: ok
./build/contextdeck-broker watchdog-selftest: ok
bash -n helper + both test scripts: ok
systemd-analyze verify packaging/systemd/contextdeck-broker.service: rc=0
CONTEXTDECK_CUTOFF_SEC=30 tests/unit/rehearse_trial_cutoff.sh: ok
git diff --check (R2 staged): clean
No RealSink::create / live /dev/input or /dev/uinput from tests
```

### Six device-free rehearsal cases (systemd `--user`, unique nonce, no broker/device names)

| Case | Semantic result |
|------|-----------------|
| Normal completion before cutoff | Fixture `active`; timer `OnActiveUSec=30s`, `AccuracyUSec=1us`; cancel then stop; no kill |
| Intentionally stopped/exited fixture | Arm refused (`missing-unit` after collect); do-not-ARM |
| Live-broken/hung fixture | Cutoff `SIGKILL`; live-state `failed` |
| Invoking-shell loss | Arm completed; invoker `SIGKILL`ed; cutoff still killed matching fixture (`failed`) |
| Timer/setup failure | Missing unit refused; do-not-ARM |
| Stale/mismatched invocation | New invocation stayed `active`; fire skipped |

Cleanup: `cleanup-result=none-remain`. Temporary verify unit file removed.

Fixture `Type=notify` required `NotifyAccess=all` so `systemd-notify` from a child could READY. Production stays `NotifyAccess=main` because the broker is the notifying main process.

## Proof: no broker install/start/reload/ARM/LEASE/grab; no real device access

Read-only after R2:

```text
systemctl is-active contextdeck-broker.service  → inactive
systemctl is-enabled contextdeck-broker.service → static
MainPID=0  InvocationID= empty  SubState=dead
NeedDaemonReload=no   (installed unit was not replaced; repo file only)
no contextdeck-broker process
```

Tests used FakeSink/FakeSource/GrabbingSource/libevdev in-memory templates only. Rehearsal used `sleep` notify fixtures on the user bus. No `daemon-reload`, no `systemctl start/enable` of the broker, no ARM/LEASE, no opening of G213 or uinput from product code.

## Unrelated subsystems

`input-remapper.service`: still `enabled` / `active` / `running`. Not stopped, disabled, or reconfigured. OpenRGB/KWin/udev/power/autostart untouched.

## Remaining risks and limitations

- Host `/etc/systemd/system/contextdeck-broker.service` was **not** reinstalled; a later G4 start would still use the previously installed unit until the COOPERATOR copies the repo file and `daemon-reload`s under a separate grant.
- Kernel ungrab-on-close and physical typing after SIGKILL remain G4.
- `sd_pid_get_session` fallback is unit-tested with fakes, not against a live tray launch.
- Runtime LED/sink-write paths are proven with fakes, not hardware.
- Cutoff window is 30 s by default; watchdog is 2 s; they are different events.
- PID1/user-manager, kernel hang, and power loss are outside the helper.
- This Worker is not independent for combined R1+R2 review.

## Why one terminal report is sufficient

The grant is one implementation exchange covering sequential R1 then R2, each with one commit/push and a stop before grab. Both gates passed. Further slices would need a new prompt.

## Next authorized transition

Fresh **independent** Worker/reviewer of the combined `64dd12b..cb72ae0` diff, tests, service semantics, cutoff guard, cleanup ordering, and documentation. Then a **separately authorized** live G4 / physical-recovery demonstration. Do not grab in the review exchange unless that prompt explicitly grants it.

## Orchestration critique

```text
Orchestration critique:
MEASURED: systemd's default timer AccuracySec is 1min, so a 30s OnActiveSec timer would fire late unless AccuracySec=1us is pinned. Evidence: user-bus `systemctl show` on an unpinned timer (`AccuracyUSec=1min`) versus pinned (`AccuracyUSec=1us`, `TimersMonotonic={ OnActiveUSec=30s; ... }`). Effect: a “30s cutoff” would not be 30s. Smallest correction: pin AccuracySec=1us (done in the helper).
LEAD: whether the installed system unit still lacks TimeoutStopSec/TimeoutAbortSec on disk; cheapest check is a later authorized `diff` of the repo unit against `/etc/systemd/system/contextdeck-broker.service` without start.
```

## Near-miss / latent failure

1. **Default `AccuracySec=1min` (pre-existing systemd; resolved in helper).** See MEASURED.
2. **`OnActiveUSec` is not a standalone `systemctl show -p` value** (pre-existing systemd API shape; resolved by reading `TimersMonotonic` / `AccuracyUSec=1us`). An integer-microsecond check would have refused a correctly armed 30s timer.
3. **`NotifyAccess=main` rejects `systemd-notify` from a child** (pre-existing systemd; fixture-only). First probe timed out; rehearsal uses `NotifyAccess=all`. Production broker remains `main`.
4. **systemd-run default Description leaked the Cursor AppImage path** (introduced in the first helper draft; resolved with `--description=ContextDeck trial cutoff` and `--quiet`).
5. **Exited `--collect` units report `missing-unit` rather than `inactive-unit`** (latent; still refuse ARM). Not a gate failure.

```text
Resolved Execution Issues / Near-Misses: AccuracySec default 1min; TimersMonotonic vs OnActiveUSec; NotifyAccess=main vs systemd-notify child; systemd-run Description path leak (all handled as above)
Pre-Existing Failure Classification: discarded uinput write results; unmeasured passthroughCapabilities(); physical LED copied into the virtual device; logind fail-closed on no-session; architecture text still described destroy-then-ungrab; no invocation-bound cutoff. R1/R2 resolved those in tree. G4 physical recovery remains open (pre-existing).
```

## Persistence

```text
Downloadable prompt filename: 12_implementation_02.md
Report filename: 12_report_02.md
Prompt persistence owner: COOPERATOR
Report persistence owner: WORKER (this file was absent; written here)
Git publication owner: COOPERATOR
Archival transition: wait for the COOPERATOR to persist/push the report and issue the next manual dispatch
Meta destination: projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
```

Destination verified: new regular file, not a symlink, no nonempty collision. META add/commit/push: **not performed**.

**Logical-whole closure: not-closed.** Implementation exchange complete (gates passed). Overall objective remains open until independent review and separately authorized live G4. This grant ends here.
