Nezávislé acceptance 13/01 je **BLOCKED**. Na hoste nie je nainštalovaný kandidát `cb72ae0` (unit aj binárka sú staršie), preto som broker nespustil a G4 som nerobil.

### Report for ORCHESTRATOR_CHAT

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 13
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Phase: acceptance
Task identity: CONTEXTDESK-G4-INDEPENDENT-ACCEPTANCE
```

- **status:** **BLOCKED**
- **phase-qualified result:** **BLOCKED**
- **Report justification:** `new-evidence`
- **Logical-whole closure:** not-closed
- **Independence required:** required-fresh-independent
- **Primary fresh acceptances used:** 0 before this run; this is the primary fresh acceptance
- **Automatic corrections used:** 0
- **Correction re-acceptance:** not-applicable
- **G4 / LEASE / ARM / live device access / physical usability:** not performed
- **Independent review of the candidate tree:** static + device-free tests only
- **Authority:** expires at this terminal report

```text
Acceptance candidate: cb72ae0388307b514182efc6936712e3da42cda4
AP pin: 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9
Evidence tier: E3
Implementation in this session: none
Meta Git: not modified
Logical-whole closure: not-closed
```

## Model / client / reasoning (requested vs observed)

| Fact | Classification |
|------|----------------|
| Requested model | Grok 4.6, selected by the COOPERATOR |
| Observed client/model label | Cursor Grok 4.6 (session communication identity; not independently attested by a provider API dump) |
| Requested reasoning | High |
| Observed reasoning mode | unknown (not independently attested) |
| Requested context | approximately 200–250k tokens |
| Observed context capacity | unknown |
| Delivery | manual; this chat’s first user message was the acceptance prompt |
| Subagents / Task dispatch | none |

Unknowns are kept unknown. A requested model is not a self-verified provider identity.

## Repository and AP gate

| Check | Result |
|-------|--------|
| Canonical checkout | `/home/agile/Projects/contextdesk` |
| Remote | `https://github.com/cisarik/contextdesk.git` |
| Branch | `main` tracking `origin/main` |
| `HEAD` | `cb72ae0388307b514182efc6936712e3da42cda4` |
| `origin/main` after authorized `git fetch origin main` | same SHA |
| Worktree | clean (`build/` gitignored; ninja reported no work) |
| `.ap` gitlink and checkout | `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9` |
| `./.ap/ap doctor` | PASS (strict pinned, managed AGENTS block, submodule clean) |

Candidate identity matches the prompt. No Git write except the authorized fetch.

## Files and commits read (this session)

Prompt `13_acceptance_00.md`; continuity `12_report_02.md` as claim/evidence only. Product: `AGENTS.md`, `README.md`, `ROADMAP.md`, `docs/operations.md`, `docs/testing-m2.md`, `docs/architecture.md`. Protocol: `.ap/AP.md` (Worker spine, RF-03/05/06/07, semantic authority), `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md` (report header, Fresh Independent Audit). Packaging: `packaging/systemd/contextdeck-broker.service`, `packaging/systemd/contextdeck-trial-cutoff.sh`, `packaging/udev/61-contextdeck-input-guard.rules`, `62-contextdeck-broker.rules`, `99-contextdeck-broker-uinput.rules`. Broker/session: `src/broker/{main,Acquisition,RealSink,ProductionRuntime,ForwardingEngine,SessionIpc,EvdevSource,EvdevGrabber,EventLoop,DeviceEnumerator,Logger,ISink}.*`, `src/app/{AppController,BrokerIpcClient,TrayController}.*`. Tests: `CMakeLists.txt` `add_test` names, `tests/unit/test_trial_cutoff.sh`, production/acquisition/forwarding/ipc excerpts. Inspected commit is `cb72ae0`, not an old clone.

No implementation, correction, package/udev/ACL/service-config mutation, daemon-reload, enable, start, ARM, LEASE, grab, or Meta write occurred in this session.

## First causal Gate 0 failure (preserved)

**Installed `/etc/systemd/system/contextdeck-broker.service` is not byte-for-byte identical to the candidate `packaging/systemd/contextdeck-broker.service`.** Live G4 was therefore not started.

```text
repo sha256:      286154ba6f443adced5dc965b0f0c4da2dfae2a44e4f77edf888c6ef96c30503
installed sha256: 82efa58f9ecae6fd6cece9c89046cc376ae9f8cd6cc714e54d7b2377500e9ecd
cmp: DIFFER
installed file mode: 0644 (operations §9 uses install -m 0644; RuntimeDirectoryMode=0755 is present)
```

Installed unit lacks the candidate pins:

- `NotifyAccess=main` (explicit line missing; `systemctl show` still reports `NotifyAccess=main` because that is the `Type=notify` default)
- `TimeoutStopSec=5` / `TimeoutAbortSec=5` (loaded values `TimeoutStopUSec=10s`, `TimeoutAbortUSec=10s`)

Present on both: `Type=notify`, `WatchdogSec=2`, `Restart=no`, `LimitCORE=0`, `RuntimeDirectoryMode=0755`, no `[Install]`, no `RuntimeMaxSec`, no `EXTEND_TIMEOUT_USEC`, `ExecStart=/usr/bin/contextdeck-broker`.

```text
LoadState=loaded UnitFileState=static ActiveState=inactive SubState=dead
MainPID=0 InvocationID= empty NeedDaemonReload=no
is-enabled=static is-active=inactive
WatchdogUSec=infinity while inactive (file still has WatchdogSec=2; not used as identity proof)
```

This is the blocker named as LEAD in `12_report_02.md`. Starting the unit would have exercised the previously installed generation, not candidate `cb72ae0`.

## Additional Gate 0 evidence (not a rerun of the first failure)

**Installed binary does not correspond to the candidate.**

| Artifact | sha256 | mtime | R1 markers `sink-write-failed` / `led-write-failed` / `led-setup-failed` / `capability-invalid` |
|----------|--------|-------|------|
| `/usr/bin/contextdeck-broker` | `1003f28b0ad9180b433bebe18defb8b177b0ae4d3716ecc03a419379a870957a` | 2026-09-11 18:04:45 | absent |
| `build/contextdeck-broker` (ninja up-to-date with `cb72ae0`) | `8e80f2d78530b01d9cda4ab77c4ff75d2888055dadce35fbb9483a15651940a6` | 2026-09-12 08:19:14 | present |

Installed binary is executable mode `755`, root-owned, and still contains older classes `peer-rejected` / `source-open-failed`. R1 landed `2b6cf2c` on 2026-09-12 08:19:40; the `/usr` copy predates that.

**`sudo -n` is unavailable** (`sudo -n true` failed). Gate 0 item 5 (`sudo -n -u contextdeck-broker test -r/-w /dev/uinput`) was not executed. That is `NEEDS_COOPERATOR_ACTION` for the named access(2) check; it is not the first causal blocker.

G3 ACL / identity readback (no event-node numbers copied):

- G213 event pair resolved by USB `046d:c336` + interface `00`/`01` (count=2). Both `root:contextdeck-broker` mode `0660`, **no session-user ACL**.
- G213 hidraw count=2: session-user ACL **present**.
- `/dev/port`: no session-user ACL, not session-readable.
- `/dev/i2c-*`: 8 nodes, session-user ACL 0, session-readable 0.
- `/dev/uinput`: existing owner/group/mode `root:root` `0660` unchanged; `user:contextdeck-broker:rw-` present; session-user ACL still present. Session `access(2)` r/w is true for the seat user; broker-identity access(2) was **not** proven.
- Udev rule files `61-`/`62-`/`99-` are byte-identical to the candidate.
- `contextdeck-broker` user/group exist (`nologin`).
- `input-remapper.service`: `enabled` / `active` / `running`. Not stopped, disabled, or reconfigured. input-remapper-2 config JSON count=5; no G213/c336/046d substring match (mouse-preset layout; contents not dumped).
- No `contextdeck-broker` process. No `cd-trial-*` timers.

Ledger-candidate (non-blocking for this verdict): G213 event nodes still list a `uaccess` udev TAG while the session ACL is absent. Policy outcome matches the grant table; tag residue was not treated as Gate 0 PASS or as the first failure.

Optional recovery inventory (not used): `sshd` `enabled`/`active`; one additional USB keyboard-class event node and one non-USB keyboard-class node (identities not copied). No second keyboard was added. No SSH session was opened by this Worker.

## Gate 1 — build, tests, static review

Documented CMake needed the operations clean-`PATH` workaround (`CMAKE_ROOT` missing in the ambient client env). `env -i HOME="$HOME" PATH=/usr/bin:/bin:/usr/sbin cmake -S . -B build -G Ninja` configured; `cmake --build build` → `ninja: no work to do`.

```text
ctest --test-dir build --output-on-failure          13/13 PASS  rc=0
./build/contextdeck-broker selftest                 ok          rc=0
./build/contextdeck-broker watchdog-selftest        ok          rc=0
systemd-analyze verify packaging/...broker.service              rc=0
systemd-analyze verify /etc/systemd/system/...broker.service    rc=0  (valid stale unit, not identity PASS)
bash -n packaging/systemd/contextdeck-trial-cutoff.sh           rc=0
helper no-args usage                                            rc=2
helper --user arm missing-unit                                  rc=1  cutoff-refuse reason=missing-unit
```

`tests/unit/rehearse_trial_cutoff.sh` (six user-bus fixtures) was **not** re-run: it mutates the user bus and is outside this envelope’s live-broker allowlist. Device-free helper refusal and `test_trial_cutoff` were run.

Static review of `cb72ae0` is consistent with `12_report_02.md` and does **not** contradict the candidate contract:

- `ISink::writeEvent`/`flushSyn` return `bool`; `ForwardingEngine::ingest` fail-closes on `sink-write-failed`; `BrokerLoopWork` disarms; cleanup writes are best-effort.
- ARM order: open if00/if01 → measure (`EV_KEY` union, `EV_LED` from if00 only, `EV_MSC`, never `EV_REP`) → create virtual → `prepareVirtual` (uinput fd in the wait set) → grab. Production `main` uses empty `RealLifecycleSink` until `applyMeasuredCapabilities`; `passthroughCapabilities()` remains test/helper-only.
- Disarm: ungrab/close physical first, then synthetic releases, then `destroyVirtual`; ledger cleared on those paths. `EvdevGrabber` ungrabs in destructor.
- LED return: `drainLed` → `libevdev_kernel_set_led_value` on if00 only; `led-write-failed` does not disarm; physical `EV_LED` is not forwarded.
- Auth: `SO_PEERCRED`; reject pid≤0/root; `sd_pid_get_session` first; fallback only `-ENODATA`/`-ENXIO`/`-ENOENT` with exactly one eligible active local seated `wayland`/`x11` session.
- No automatic ARM/LEASE/restart/re-arm/autostart in broker start, `STATUS`, or session `start()` (STATUS probe only). Unit has `Restart=no` and no `[Install]`.
- Logger emits state/error-class/counters only; no ordinary keystrokes, scan codes, or serials.
- Cutoff helper: invocation identity required; refuses missing/inactive/mismatched; re-checks before `systemctl kill --kill-whom=main --signal=SIGKILL`; default `OnActiveSec=30s`, `AccuracySec=1us`, `RandomizedDelaySec=0`, `Persistent=no`; cancel/status paths; setup failure is non-zero; no `pkill`/`killall`/guessed PID/restart.

Near-miss in source (pre-existing, non-contradiction): `createVirtual` failure still calls `rollbackFrom(..., virtualCreated=true)`, which records `destroy-virtual` on a null impl; `destroyVirtual` is safe.

## Gates 2–4 — not entered

Gate 0 failed, so the broker was not started, the invocation-bound cutoff was not armed against the production unit, and authenticated ARM/LEASE was not attempted. No raw socket client was fabricated.

| Required live claim | Evidence |
|---------------------|----------|
| 4.1 Identity + pass-through + modifiers + remapper coexistence | missing |
| 4.2 LED return to physical if00 | missing |
| 4.3 Explicit DISARM and lease-expiry ungrab | missing |
| 4.4 Invocation-cutoff recovery + typing after descriptor close | missing |
| 4.5 Crash/hang/watchdog on an armed broker | missing (would be PARTIAL even after cutoff if no separate recovery path were used; not reached) |
| 4.6 Final safe state after live cases | live cases not run |

A CTest PASS and a cutoff rehearsal are not acceptance-PASS.

## Final safe state after this session

```text
contextdeck-broker.service: static / inactive / dead / MainPID=0
no contextdeck-broker process
no cd-trial timers
input-remapper: enabled/active (unchanged)
udev/ACL/service files: not written by this Worker
repository: clean at cb72ae0; AP pin 0cf2cff
G213 typing: not grabbed by this session (broker never started)
```

## Missing evidence that prevents a stronger verdict

1. Host install of candidate unit + `/usr/bin/contextdeck-broker` matching `cb72ae0` (first causal).
2. Named `sudo -n` broker-identity uinput access(2) check.
3. All mandatory live G4 claims listed above.

## Residual risks and Cooperator-owned decisions

- Starting the currently installed unit would grab (if later armed) with pre-R1 fail-open sink writes, unmeasured capabilities, and default 10s stop/abort timeouts. Do not start it under a “continue G4” instruction.
- Kernel ungrab-on-close, physical typing after SIGKILL, LED hardware visibility, and live logind fallback remain unproven.
- `sudo` for this Worker is interactive-password blocked.
- Second USB keyboard and `sshd` exist as optional recovery inventory only; they do not waive install identity.
- ROADMAP still describes recovery-design as unresolved next work; that is documentation lag, not authority.

## Smallest next step

COOPERATOR-run **operations.md §9 only**: install the candidate broker binary and copy the candidate unit, then `daemon-reload`. **Do not enable. Do not start.** Then issue a **new** complete fresh-independent G4 acceptance prompt against the same `cb72ae0` after verifying `cmp` of the unit file and sha256 of `/usr/bin/contextdeck-broker` against a candidate build.

## Why one terminal report is sufficient

The grant is one acceptance exchange. Gate 0 failed with a preserved first causal mismatch; live trial is prohibited; corrections are prohibited. Further work needs a new prompt.

## Orchestration critique

```text
Orchestration critique:
MEASURED: the G4 host still runs the pre-R2 unit and pre-R1 broker, so an independent Worker that started the installed service would have accepted the wrong artifact. Evidence: unit cmp/diff (missing TimeoutStopSec=5, TimeoutAbortSec=5, explicit NotifyAccess=main); installed TimeoutStopUSec=10s; binary sha256 mismatch; installed strings lack sink-write-failed. Effect: Gate 0 correctly BLOCKED before grab. Smallest correction: operations §9 reinstall of binary+unit with daemon-reload, then a new fresh acceptance; no start in that install step.
LEAD: whether passwordless sudo -n can be granted for the named Gate 0 uinput access(2) check and later invocation-bound systemctl kill without weakening policy. Cheapest check: COOPERATOR runs sudo -n true and the documented contextdeck-broker uinput test.
```

## Near-miss / latent failure

1. **Stale installed unit/binary vs candidate (pre-existing host state; not resolved).** Would have been a false G4 if Gate 0 identity had been skipped.
2. **systemd `WatchdogUSec=infinity` on an inactive unit (pre-existing systemd show shape).** File still has `WatchdogSec=2`. Using `show -p WatchdogUSec` alone would have falsely failed Watchdog identity.
3. **Prompt wording “unit … mode 0755” vs operations `install -m 0644` (pre-existing prompt/docs mix).** Interpreted as `RuntimeDirectoryMode=0755`; file mode `0644` matches operations. Not first causal.
4. **G213 event `uaccess` TAG still listed while session ACL is absent (latent).** ACL policy holds; tag residue is a ledger-candidate.
5. **Cursor AppImage intercepted `pgrep` (introduced by environment; resolved with `ps -C`).**

```text
Resolved Execution Issues / Near-Miss: ambient CMAKE_ROOT failure handled with the documented clean PATH; pgrep AppImage wrap handled with ps -C; live trial withheld after unit/binary mismatch
Pre-Existing Failure Classification: host unit and /usr/bin broker are not the cb72ae0 candidate (open). Candidate-tree R1/R2 production gaps reported in 12_report_02 are present in source/tests (static/device-free). G4 physical claims remain missing (pre-existing, not exercised).
```

## Persistence

```text
Prompt filename: 13_acceptance_00.md
Report filename: 13_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: WORKER for this terminal report; COOPERATOR archives it
Git publication owner: COOPERATOR
```

This report was **not** written to Meta and was **not** pushed. Destination for later COOPERATOR archival: `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/`.

**Logical-whole closure: not-closed.** Authority for this Worker expires at this report.