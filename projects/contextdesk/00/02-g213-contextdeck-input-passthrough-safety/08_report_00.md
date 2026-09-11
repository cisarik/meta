### Report for ORCHESTRATOR_CHAT

- **logical-whole identity:** `g213-contextdeck-input-passthrough-safety`
- **Worker-session ordinal:** `08`
- **Worker-exchange ordinal:** `00`
- **Worker session target:** `fresh-worker-session`
- **Native planning mode:** `not-used`
- **Worker session profile:** Fresh Implementation Worker (S5 production-prerequisite)
- **status:** **PARTIAL**
- **phase-qualified result:** repository implementation candidate produced and validated; host binary/unit install did not complete (no passwordless `sudo`)
- **Logical-whole closure:** not-closed
- **Report justification:** `new-mutation`
- **Independence required:** no (implementation; this session cannot provide G4)
- **Authority:** expires at this terminal report

Coordinates were not spelled as AP fields in the prompt; they are taken from the expected META names `08_implementation_00.md` / `08_report_00.md` plus “fresh implementation WORKER”.

```text
Implementation authority: explicit
Exact baseline: 9924b1b1ac0206a0d252cbe68fdd1ce91e0c74d6 (AP pin 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26)
Changed-path allowlist: src/broker production path + session-app ARM UI + CMake install + broker unit comment + operations/testing/architecture/specification + test_broker_production
Independence required: no
```

## Implementation status

Repository S5 production-prerequisite slice is implemented, tested, committed, and pushed.

Host install of `/usr/bin/contextdeck-broker` and refresh of the installed unit to `RuntimeDirectoryMode=0755` did **not** run. `sudo` required a password and a TTY. The broker was never enabled, started, armed, or grabbed.

A fresh independent G4 acceptance is **not** authorized yet. The previous G4 abort conditions (missing binary, installed unit `0750`) are still true on the host.

## Starting and ending commits

| Anchor | Value |
|--------|--------|
| Start HEAD | `9924b1b1ac0206a0d252cbe68fdd1ce91e0c74d6` |
| End HEAD | `899df8fc14a2ad67594ff432f1b00d9ab155fd79` |
| Subject | `Add production G213 enumerator, explicit ARM, and broker install.` |
| AP pin (`.ap` gitlink) | `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` |
| Remote | `https://github.com/cisarik/contextdesk.git` `main` (`9924b1b..899df8f`) |
| Worktree after commit/push | clean, `main...origin/main` |

## Exact changed paths

- `CMakeLists.txt`
- `src/broker/DeviceEnumerator.h`, `src/broker/DeviceEnumerator.cpp`
- `src/broker/EvdevSource.h`, `src/broker/EvdevSource.cpp`
- `src/broker/ProductionRuntime.h`, `src/broker/ProductionRuntime.cpp`
- `src/broker/IdentityMatcher.h`, `src/broker/IdentityMatcher.cpp`
- `src/broker/RealSink.h`, `src/broker/RealSink.cpp`
- `src/broker/main.cpp`, `src/broker/GrabbingSource.h`
- `src/app/AppController.h`, `src/app/AppController.cpp`
- `src/app/BrokerIpcClient.cpp`, `src/app/SessionApplication.cpp`
- `src/app/TrayController.h`, `src/app/TrayController.cpp`
- `ui/DiagnosticsPage.qml`
- `tests/unit/test_broker_production.cpp`
- `packaging/systemd/contextdeck-broker.service`
- `docs/operations.md`, `docs/testing-m2.md`, `docs/architecture.md`, `docs/specification.md`

Not modified: AP, `.ap`, `AGENTS.md`, `ROADMAP.md`, META, `handout.md`, udev, sysusers, input-remapper.

## Implementation allowlist (stated before edits)

In-scope: broker enumerator + `EvdevSource`/`RealSink`/`EvdevGrabber` wiring; explicit session-app `LEASE`+`ARM`; CMake install of `contextdeck-broker` to `${CMAKE_INSTALL_BINDIR}` under prefix `/usr`; in-tree unit comment keeping `RuntimeDirectoryMode=0755`; hang procedure docs; device-free tests; narrow ops/testing/architecture/spec updates.

Out of scope: G4 IRL, live grab, SIGTERM/SIGKILL/hang on a grabbed keyboard, G3 policy change, OpenRGB uaccess reopen, autostart, hidden hang command, META.

## Production enumerator design

`UdevDeviceEnumerator` scans `input` event nodes via libudev sysfs/uevent only. It does not open `/dev/input` or `/dev/uinput`.

Identity is USB ancestry, not `eventN`:

- USB parent `usb_device` must be `046d:c336`
- USB interface `bInterfaceNumber` `00` or `01`
- `evaluateIdentity()` still rejects virtual bus, `ContextDeck*` name prefix, unresolved fields, and wrong VID/PID
- `devnode` is only the later open handle

`selectG213Pair()` requires exactly one accepted if00 and one accepted if01. Missing, duplicate, or empty sets fail closed. Interface `02` and nodes without USB ancestry are ignored. Enumeration runs only inside `ProductionArmControl::arm()`, not at startup. Game Mode and Backlight remain firmware-only (no host EV_KEY; not a remap catalog).

## RealSink / EvdevGrabber design

Startup constructs `RealLifecycleSink` + two `EvdevSource` objects **disarmed**. No fd is opened until `Acquisition::arm()`.

ARM order (existing invariant): create virtual → open if00 → grab if00 → open if01 → grab if01. Failure rolls back ungrab-first.

- Virtual device uses `passthroughCapabilities()` (full KEY/LED/MSC bit sets, no `EV_REP`) so capability discovery does not open devices before ARM
- `EvdevSource::openSource()` opens the bound path `O_RDONLY|O_NONBLOCK|O_CLOEXEC`, builds libevdev, and re-checks identity against the bound USB interface tag
- `claimSource()` uses `EvdevGrabber` (`libevdev_grab` → `EVIOCGRAB`)
- Successful ARM registers evdev fds on the existing epoll wait; disarm removes fds first, then `Acquisition::disarm()`
- `BrokerLoopWork` ingests both sources after IPC; a read error fail-closes by disarming
- `SYN_DROPPED` is drained via libevdev SYNC and handed to the existing forwarding/ledger path
- Destructors ungrab then close

`FailClosedSink` / `FailClosedSource` are gone from `main.cpp`. `nm` on `main.cpp.o` shows `UdevDeviceEnumerator`, `ProductionArmControl`, `EvdevSource`, `passthroughCapabilities`. Linked `contextdeck-broker` defines `RealSink::create`, `EvdevGrabber::create`, `EvdevSource::openSource`, `ProductionArmControl::arm`.

## Explicit ARM path

`SessionApplication::start()` still only calls `BrokerIpcClient::start()`, which probes `STATUS` and does not arm.

Deliberate UI:

- Tray: **Arm G213 pass-through…** (confirm), **Disarm pass-through**, **Release broker lease**
- Diagnostics: the same three actions, with a confirm dialog on ARM

Those call the existing authenticated `LEASE` then `ARM` client. Disconnect clears `wantArm`/`wantLease` so reconnect does not re-arm. `DISARM` and `RELEASE` stay explicit. Broker-side fail-closed paths (auth, disconnect, malformed, expiry, shutdown) are unchanged.

## Install procedure and resulting binary/unit state

In-tree:

- `install(TARGETS contextdeck-broker RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR} COMPONENT broker)`
- Documented prefix remains `/usr` (`docs/operations.md` §9)
- Unit still `Type=notify`, `WatchdogSec=2`, `Restart=no`, no `[Install]`, `RuntimeDirectoryMode=0755`

Unprivileged DESTDIR probe (`cmake --install build --component broker --prefix /tmp/contextdeck-install-probe/usr`) installed **only** `.../usr/bin/contextdeck-broker`.

Host after this session:

| Check | Result |
|--------|--------|
| `/usr/bin/contextdeck-broker` | **missing** |
| installed unit vs repo | **DIFF** — host still `RuntimeDirectoryMode=0750` |
| `systemctl is-enabled contextdeck-broker` | `static` (not enabled) |
| `systemctl is-active` | `inactive` / `dead` |
| `systemd-analyze verify` (repo unit) | exit **1**, missing `/usr/bin/contextdeck-broker` |
| G3 udev vs repo | byte-identical |
| input-remapper | enabled/active, not modified |

COOPERATOR paste-safe host install (no start, no enable, no arm):

```sh
# PURPOSE: install S5 broker binary and refresh unit; leave inactive
# ABORT: do not enable, start, restart, arm, or grab
cd /home/agile/Projects/contextdesk
cmake -S . -B build -G Ninja -DCMAKE_INSTALL_PREFIX=/usr
cmake --build build
sudo cmake --install build --component broker
sudo install -m 0644 packaging/systemd/contextdeck-broker.service \
  /etc/systemd/system/contextdeck-broker.service
sudo systemctl daemon-reload
test -x /usr/bin/contextdeck-broker
diff packaging/systemd/contextdeck-broker.service \
  /etc/systemd/system/contextdeck-broker.service
systemctl is-enabled contextdeck-broker.service
systemctl is-active contextdeck-broker.service
```

Expected: executable binary, empty `diff`, enabled=`static`, active=`inactive`.

## Hang harness documentation

Documented in `docs/testing-m2.md` (G4 only) and pointed from `docs/operations.md` §7.

External `SIGSTOP` on the broker PID from a recovery path (not the G213), observe watchdog starve (`WatchdogSec=2`), then systemd abort; `SIGCONT` or `SIGKILL` if a stopped process holds abort pending. No hidden production hang command. Recovery and final secure-state checks are in that procedure. **Not executed** in this session.

## Focused / full test commands and exit statuses

```text
cmake -S . -B build -G Ninja -DCMAKE_INSTALL_PREFIX=/usr   # configure ok
cmake --build build                                        # exit 0
./build/test_broker_production                             # exit 0
ctest --test-dir build --output-on-failure                 # exit 0, 10/10
./build/contextdeck-broker selftest                        # exit 0
./build/contextdeck-broker watchdog-selftest               # exit 0
systemd-analyze verify packaging/systemd/contextdeck-broker.service
                                                           # exit 1, missing /usr/bin/contextdeck-broker
```

CTest: profile resolver/persistence, OpenRGB protocol, identity, ledger, forwarding, acquisition, watchdog, IPC, production — all passed. Tests did not call live udev scan, did not open G213 event nodes, and did not call `RealSink::create`. Fail-closed ARM used missing enumerator results, nonexistent paths, and `/dev/null` (not an evdev device).

## Proof that no real grab occurred

- No `contextdeck-broker` PID
- Unit `inactive`/`dead` for the whole session
- Production tests never constructed `EvdevGrabber` against a live fd (`create(nullptr)` and fd-less `libevdev_new()` only)
- ARM failure paths logged `enumerate-empty` / `source-open-failed` and left sources unopened
- This session did not send `LEASE`/`ARM` to a live socket and did not start the unit

## Proof that the broker was not enabled or started

- `UnitFileState=static`, no `[Install]`
- `ActiveState=inactive`, `SubState=dead`
- `systemctl start` / `enable` / `restart` were not run
- `daemon-reload` was not run (install never reached that step)

## Residual risks

- Host is still S4-era: missing `/usr/bin/contextdeck-broker`, installed unit `RuntimeDirectoryMode=0750` (seat user cannot traverse `/run/contextdeck` without joining `contextdeck-broker`, which would be a keylogging hole)
- G4 IRL, pass-through fidelity, and kernel ungrab-on-close are unproven
- Independent physical recovery keyboard was not re-verified here
- `passthroughCapabilities()` enables a broad KEY/LED/MSC set rather than live-probed bits; extra unused uinput bits are accepted so ARM does not open devices early
- Same-UID seated graphical compromise can still `LEASE`/`ARM` pass-through (existing architecture residual)
- This implementation is non-independent evidence

## Fresh independent G4 acceptance authorized?

**No.** Do not issue G4 until the COOPERATOR completes operations §9 and a fresh Worker re-checks: binary present and executable, installed unit byte-matches repo (`0755`), G3 ACLs still PASS, broker still static/inactive before that G4 session starts it.

Smallest next step: COOPERATOR runs the install block above; Orchestrator then issues a **fresh independent** G4 acceptance. Do not start the current unit before that install.

Resolved Execution Issues / Near-Misses: host `sudo` blocked (no TTY/password). Unprivileged DESTDIR install was used to prove `COMPONENT broker` copies only the broker binary. No grab and no unit start were substituted.

Pre-Existing Failure Classification: installed unit still S3 `RuntimeDirectoryMode=0750`; `/usr/bin/contextdeck-broker` still absent on the host.

**Logical-whole closure: not-closed.** This is not G4 PASS.

Expected META archive names (Orchestrator / COOPERATOR; this Worker did not archive):

- `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/08_implementation_00.md`
- `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/08_report_00.md`