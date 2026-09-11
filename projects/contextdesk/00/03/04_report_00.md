### Report for ORCHESTRATOR_CHAT

Logical whole identity: g213-contextdeck-input-passthrough-safety  
Worker session ordinal: 04  
Worker exchange ordinal: 01  
Worker session target: fresh-worker-session  
Native planning mode: not-used  

(The prompt did not spell those four fields; they are taken from “fresh implementation WORKER” plus the stated META names `04_implementation_00.md` / `04_report_00.md`. Prior M2 sessions used 01 planning, 02 S1, 03 S2.)

- status: **PASS**
- Phase-qualified result: **implementation-PASS** (non-independent; not acceptance)
- Logical-whole closure: **not-closed**
- start commit: `69f433c382d7dffe6d8b8f1aea41ca7c6931a4f6`
- end commit: `ae1291134fd4f2c2980a6b933a29a57cb44cd058`
- Result artifact: one local commit on `main` (not pushed)
- Report justification: **new-mutation**
- Authority expiry: this implementation grant expires at this terminal report. Further mutation, S4/S5, host service operation, grabbing, acceptance, publication, META self-archival, and whole closure remain unauthorized.

## Verified repository identity and anchors

| Check | Result |
|---|---|
| Root | `/home/agile/Projects/contextdesk` |
| Remote | `https://github.com/cisarik/contextdesk.git` |
| Branch | `main`, tracking `origin/main` (now 1 local commit ahead) |
| Baseline HEAD | `69f433c382d7dffe6d8b8f1aea41ca7c6931a4f6` (matched continuity anchor) |
| AP gitlink and checkout | `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` (matched pin; unchanged) |
| Worktree at baseline | clean |
| Git locks | none |
| Broker unit during this session | `static` / `inactive` (`dead`); never enabled; never started |

## Baseline result

Poisoned Cursor AppImage `PATH` made `/usr/bin/cmake` fail with missing `CMAKE_ROOT` (already documented in `docs/operations.md`). Re-ran with `env -i … PATH=/usr/bin:/bin:/usr/sbin`.

- configure + build: exit **0**
- CTest at baseline: **7/7** passed, exit **0**

## Implementation allowlist (stated before edits; only these changed)

- `src/broker/Watchdog.h`, `src/broker/Watchdog.cpp`
- `src/broker/EventLoop.h`, `src/broker/EventLoop.cpp`
- `src/broker/IdleWait.h`, `src/broker/IdleWait.cpp`
- `src/broker/WatchdogSelftest.cpp`, `src/broker/Selftest.h`, `src/broker/main.cpp`
- `tests/unit/test_broker_watchdog.cpp`
- `CMakeLists.txt` (`libsystemd`, new sources, `test_broker_watchdog`)
- `packaging/systemd/contextdeck-broker.service` (comments only; `WatchdogSec=2` unchanged)
- `docs/operations.md`, `docs/testing-m2.md`, `docs/architecture.md` (watchdog/recovery wording)

Not touched: AP, `.ap`, `AGENTS.md`, META, `handout.md`, ROADMAP, udev/sysusers, input-remapper, G3 host files on disk, session app, IPC, grab execution.

## Implementation summary

S3 only. The broker no longer prints a version and exits. With no arguments it runs a **disarmed idle** event loop: `signalfd` + `epoll_wait`, `READY=1` once the loop is up, `WATCHDOG=1` from that same thread after each wait return (including idle timeout) and after that iteration’s work, `STOPPING=1` on SIGTERM/SIGINT. No devices opened, no grab, no uinput, no Unix-socket IPC.

`contextdeck-broker selftest` unchanged. `contextdeck-broker watchdog-selftest` is an in-process harness (no `NOTIFY_SOCKET`, no devices).

## Exact changed paths

| Path | Purpose |
|---|---|
| `src/broker/Watchdog.*` | `IWatchdog`, `sd_notify` payloads, `watchdogFeedTimeoutMs()` (half of `$WATCHDOG_USEC`) |
| `src/broker/EventLoop.*` | Single-thread loop: ready → wait → work → `WATCHDOG=1` |
| `src/broker/IdleWait.*` | Production `epoll`/`signalfd` wait |
| `src/broker/WatchdogSelftest.cpp`, `Selftest.h` | Device-free watchdog selftest |
| `src/broker/main.cpp` | Idle daemon path + `watchdog-selftest` |
| `tests/unit/test_broker_watchdog.cpp` | Progress, hang, crash, no background feed, ingest-on-loop |
| `CMakeLists.txt` | `libsystemd` + test |
| `packaging/systemd/contextdeck-broker.service` | Document feed semantics; still `Type=notify`, `WatchdogSec=2`, `Restart=no`, no `[Install]` |
| `docs/operations.md` | §6 start warning updated; new §7 crash/hang/TTY |
| `docs/testing-m2.md` | S3 evidence + later G4 procedure (not to run now) |
| `docs/architecture.md` | Watchdog bullet matches the loop |

## Watchdog / systemd design

- **Configuration:** `WatchdogSec=2` already on the unit. Feed timeout is half of `sd_watchdog_enabled()` (`$WATCHDOG_USEC=2000000` → 1000 ms); unsupervised fallback is 1000 ms.
- **READY=1:** once, before the first wait, from the loop thread (`SystemdWatchdog` → `sd_notify(0, "READY=1")`).
- **WATCHDOG=1:** only after `wait()` returns `Progress` **and** `afterWait()` (ingest/work) returns. Idle `epoll_wait` timeout is progress. `Stop` does not ping.
- **Hang detection:** a wait that ignores the timeout, or work that never returns, never emits `WATCHDOG=1`. There is no helper thread, `QTimer`, `timerfd`, or detached feeder.
- **Crash:** default systemd watchdog signal is `SIGABRT` (`WatchdogSignal=6` on the loaded unit). `Restart=no` so death does not re-grab.
- **Idle production:** no `RealSink`, no `libevdev_grab`. `nm` on `contextdeck-broker` has no `RealSink` symbols. Safety contracts (identity, ledger, 1:1+SYN, SYN_DROPPED, all-or-nothing, ungrab-first) were not rewritten; ingest-on-loop still leaves the fake ledger idle.

Installed unit on disk is still the G3 copy (`WatchdogSec=2`, comments not reinstalled). This Worker did not `daemon-reload`, install the binary, or copy the unit.

## Tests and exact exit statuses

| Command | Exit |
|---|---|
| Baseline CTest 7/7 (`env -i` clean PATH) | **0** |
| Focused `ctest -R test_broker_watchdog` | **0** (0.57 s) |
| Full CTest **8/8** | **0** |
| `./build/contextdeck-broker selftest` | **0** |
| `./build/contextdeck-broker watchdog-selftest` | **0** (`ready=1`, `watchdog=3`) |
| `./build/contextdeck-broker nope` | **1** (`error=unknown-command`) |
| Local `timeout --kill-after=1s 0.4s ./build/contextdeck-broker` (build binary, **not** the unit) | **0** (`state=idle` then `state=stopped`) |

`test_broker_watchdog` covers: exact `READY=1` / `WATCHDOG=1` / `STOPPING=1` strings; 2 s → 1 s timeout via `$WATCHDOG_USEC`; ping only after wait+work; stop does not ping; 50 ms sleep produces no extra ping; fake ingest still 1:1+SYN and idle ledger; production `SignalEpollWait` idle timeout pings; forked wait-hang and work-hang emit ready and never watchdog; forked crash through the loop is `SIGABRT` after ready without watchdog.

## systemd validation result

- `systemd-analyze verify packaging/systemd/contextdeck-broker.service`: exit **1**. Sole message: `Command /usr/bin/contextdeck-broker is not executable: No such file or directory`. Same for the installed fragment. Binary is intentionally not installed.
- Same unit copied to a temp file with `ExecStart=/usr/bin/true`: exit **0**.
- Loaded unit: `Type=notify`, `Restart=no`, `NotifyAccess=main`, `WatchdogSignal=6`, `UnitFileState=static`, `ActiveState=inactive`. `WatchdogUSec=infinity` on `systemctl show` while dead (watchdog not armed until a start, which was not done). Unit text still has `WatchdogSec=2`.

## Commit hash

`ae1291134fd4f2c2980a6b933a29a57cb44cd058`  
Message: `Feed the systemd watchdog from the broker event loop.`  
Push: **not authorized**, not performed.  
Working tree after commit: clean. AP pin unchanged.

## Remaining risks

- G4 on this kernel is still required: FD-close ungrab, 2 s as a measured recovery time, held-modifier death, VT/SysRq from the G213 while grabbed (must not be assumed).
- Host unit file was not reinstalled; comments exist only in-tree. Runtime `WatchdogSec=2` was already installed at G3.
- `ProtectHome=yes` still blocks running a home `build/` binary as the unit; `/usr/bin/contextdeck-broker` still missing.
- Idle loop has no udev monitor (would need `AF_NETLINK`; unit still `RestrictAddressFamilies=AF_UNIX`). Hotplug stays S4/S5.
- Independent acceptance was not this session.

## Broker service: not enabled, not started

`contextdeck-broker.service` was **not** enabled and **not** started. `systemctl is-enabled` → `static`; `systemctl is-active` → `inactive`. input-remapper was not changed. G3 udev/sysusers were not edited. No real input grabbing.

This is only the S3 implementation report. It is **not** acceptance-PASS and does **not** close the logical whole.

## Smallest next step

ORCHESTRATOR archives this prompt + report under the stated META names, then routes **S4** (Unix-socket IPC + `SO_PEERCRED` + lease arm/disarm) as a fresh implementation session. Do not start the broker unit for S3 “try-out”.

Resolved Execution Issues / Near-Misses: Cursor AppImage `PATH` hid CMake modules (`CMAKE_ROOT`); used the documented `env -i PATH=/usr/bin:/bin:/usr/sbin` route. Residual: any later Worker must use that route on this host.

Pre-Existing Failure Classification: none in product tests. `systemd-analyze verify` non-zero is missing `ExecStart` binary (install forbidden here), not a unit-syntax defect (temp `ExecStart=/usr/bin/true` was 0).