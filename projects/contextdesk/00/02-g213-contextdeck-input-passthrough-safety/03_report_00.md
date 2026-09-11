### Report for ORCHESTRATOR_CHAT

Logical whole identity: g213-contextdeck-input-passthrough-safety  
Worker session ordinal: 03  
Worker exchange ordinal: 01

- status: **PASS**
- Phase-qualified result: **implementation-PASS**
- Result artifact or commit: `1bfdefe443971b489f96063d2b881846c16c646f` .. `deb67ac3b2a161ab172c4039f2fa8b9a800ed174` (two local commits on `main`)
- Result evidence: configure + build + full CTest 7/7 green; `./build/contextdeck-broker` prints version and exits 0; `./build/contextdeck-broker selftest` exits 0 with idle counters and no device I/O; host files authored, **not** installed
- Logical-whole closure: **not-closed**
- start commit: `fcdca5cc53318439e69d11cdd671befb8dad9bcd`
- end commit: `deb67ac3b2a161ab172c4039f2fa8b9a800ed174`
- Changed files: allowlisted only (`src/broker/**`, `tests/unit/test_broker_acquisition.cpp`, `CMakeLists.txt`, `packaging/udev/**`, `packaging/sysusers.d/**`, `packaging/systemd/contextdeck-broker.service`, `docs/operations.md`)
- tests and validation: 7/7 CTest passed (6 existing + `test_broker_acquisition`); selftest ok; grab/uinput/udev/systemctl not executed (forbidden)
- commit and push result: local `1bfdefe`, `deb67ac`; push not authorized
- Report justification: **new-mutation**
- Authority expiry: implementation authority expired at this terminal report; further mutation, host installation, grabbing, acceptance, publication, META self-archival, and closure remain unauthorized

## Capability handshake

- Product/client: Cursor coding session; identity not independently attested.
- Native planning mode: prompt `not-used`; observed disabled/absent (implementation tools available; Plan Mode not used).
- Writable scope: allowlisted product paths plus gitignored `build/`; META not written.
- Context headroom: sufficient; no compaction stop.
- Commit capability exercised under prompt git authority (two stage commits); capability is not further commit authority.
- Credentials: not probed.
- Sub-agents: not used.

## Repository gate

- Root canonical checkout, remote `https://github.com/cisarik/contextdesk.git`, branch `main`.
- Baseline HEAD matched `fcdca5cc53318439e69d11cdd671befb8dad9bcd`; worktree clean excluding gitignored `build/`.
- `origin/main`: `ca3ac07c5fecfe3c983078e343ec6b3e02c75bea` (local ahead; not treated as drift; not pushed).
- `.ap` gitlink and checkout: `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`.
- No active Git operation. Ending worktree clean.
- Dependencies: `libevdev` / `libudev` unchanged; `libsystemd` **not** linked.

## Stage table

| Stage | Result | Reason |
|---|---|---|
| G1C | green | Host policy files + grab seam (`FakeGrabber` / `EvdevGrabber`) + acquisition tests; 7/7 CTest; committed `1bfdefe` |
| G2C | green | `docs/operations.md` G3 install/verify/rollback; 7/7 CTest unchanged; committed `deb67ac` |

Authorized-stage labels G1C/G2C/G3C in the prompt header were executed as the later "Stages and gates" pairing (packaging+grab together, then operations). No S4 socket.

## Changed files and purpose

**G1C `1bfdefe`** — host artifacts and exclusive-claim wiring, no host mutation:

- `packaging/sysusers.d/contextdeck-broker.conf` — system user/group `contextdeck-broker`, nologin, no home
- `packaging/udev/61-contextdeck-input-guard.rules` — revoke `uaccess` from G213 **input**, `/dev/port`, `i2c-[0-9]*`; hidraw unmatched
- `packaging/udev/62-contextdeck-broker.rules` — G213 `event*` → `GROUP=contextdeck-broker MODE=0660`; additive `setfacl` on `/dev/uinput`
- `packaging/systemd/contextdeck-broker.service` — system unit, `Type=notify`, `WatchdogSec=2`, `Restart=no`, no `[Install]`
- `src/broker/IGrabber.h`, `FakeGrabber.*`, `EvdevGrabber.*`, `GrabbingSource.*` — claim = grab, unclaim = ungrab
- `src/broker/Acquisition.h`, `Selftest.cpp` — claim hook documented; selftest uses `FakeGrabber`
- `tests/unit/test_broker_acquisition.cpp`, `CMakeLists.txt` — all-or-nothing and ungrab-first ordering

**G2C `deb67ac`** — operations hand-off only:

- `docs/operations.md` — new section 6 (G3 install / verify / rollback). Sections 1–5 unchanged.

## Contracts check

| Contract | Result |
|---|---|
| Guard udev | Implemented. `TAG-="uaccess"` on G213 `SUBSYSTEM=="input"` + `046d:c336`; `KERNEL=="port"`; `KERNEL=="i2c-[0-9]*"`. No hidraw match. |
| Broker grant | Implemented. G213 `KERNEL=="event*"` only → `contextdeck-broker` `0660`. No other keyboards. |
| uinput ACL | Implemented. `RUN+=/usr/bin/setfacl -m u:contextdeck-broker:rw /dev/uinput`. Group/mode of uinput not changed. |
| sysusers | Implemented. One `u contextdeck-broker` line, nologin, `-` home, automatic system UID. |
| systemd unit | Implemented as specified, plus `DevicePolicy=closed` so `DeviceAllow=/dev/uinput rw` and `char-input rw` actually narrow. No `[Install]`. `ExecStart=/usr/bin/contextdeck-broker` with comment to adjust until an install prefix exists. |
| Grab wiring | Exclusive claim is `IGrabber`. **Documented choice:** `libevdev_grab(dev, LIBEVDEV_GRAB)` (issues `EVIOCGRAB`). `release`/`unclaim` is `LIBEVDEV_UNGRAB`. Tests use `FakeGrabber` only. `EvdevGrabber::create(nullptr)` returns nullptr; `libevdev_grab` was not called. `RealSink::create` was not called. |
| All-or-nothing | Virtual first, then if00, then if01. Failed if01 claim → ungrab if00, destroy virtual, disarmed; no leftover grab. Failed if01 open → same, with no if01 grab attempt. |
| Ungrab-first teardown | Preserved: unclaim/ungrab physical (if01 then if00), then LIFO synthetic releases, then destroy virtual. |
| Logging | State names, error classes, counters. No key codes/names/scans/timing on runtime paths. Test fixtures use catalog codes already used by existing ledger tests. |

## COOPERATOR install command block (not run)

Host files are in-tree only. Install is a separate COOPERATOR step. **No enable, no start.**

```sh
# COOPERATOR-run (privileged). From the repository root.
sudo install -m 0644 packaging/sysusers.d/contextdeck-broker.conf \
  /usr/lib/sysusers.d/contextdeck-broker.conf
sudo systemd-sysusers contextdeck-broker.conf

sudo install -m 0644 packaging/udev/61-contextdeck-input-guard.rules \
  /etc/udev/rules.d/61-contextdeck-input-guard.rules
sudo install -m 0644 packaging/udev/62-contextdeck-broker.rules \
  /etc/udev/rules.d/62-contextdeck-broker.rules
sudo udevadm control --reload-rules
sudo udevadm trigger --subsystem-match=input
sudo udevadm trigger --subsystem-match=i2c-dev
sudo udevadm trigger --sysname-match=port

sudo install -m 0644 packaging/systemd/contextdeck-broker.service \
  /etc/systemd/system/contextdeck-broker.service
sudo systemctl daemon-reload
```

Verify: G213 **event** nodes group `contextdeck-broker` and no session ACL; **hidraw** session ACL still present; `/dev/port` and `/dev/i2c-*` no longer user-readable; input-remapper untouched. Rollback and the "do not start" warning are in `docs/operations.md` section 6.

## Tests and validation

CTest (all green):

1. `test_profile_resolver`
2. `test_profile_persistence`
3. `test_openrgb_protocol`
4. `test_broker_identity`
5. `test_broker_ledger`
6. `test_broker_forwarding`
7. `test_broker_acquisition`

Also: `./build/contextdeck-broker` → `contextdeck-broker 0.1.0`; `./build/contextdeck-broker selftest` → `selftest: ok` with `droppedSync=1`, `keysDownPhysical=0`, `keysDownSynthetic=0`.

Deliberately not tested: real `/dev/input`, `/dev/uinput`, `libevdev_grab` on a live fd, `udevadm`, `systemctl`, sysusers install, IPC, watchdog notify, latency, crash/SIGKILL on this kernel.

R1 inline: no key-content logging, no shell, no network in the broker, host files grant only the named G213 event nodes plus additive uinput ACL, hidraw untouched, `LimitCORE=0` on the unit.

## Facts / assumptions / unknowns / open gates

- **Facts:** two local commits from baseline `fcdca5c`; 7/7 CTest; selftest idle; no grab and no real device open; host policy files exist in-tree and are not installed; G1 firmware-only Game Mode/Backlight still have no broker identifiers.
- **Assumptions:** `setfacl` is present at `/usr/bin/setfacl` on the target host (KDE Connect already used ACLs); `systemd-sysusers` will create both user and group from one `u` line; after COOPERATOR install, udev will drop session ACLs from G213 event nodes without touching hidraw.
- **Unknowns:** whether this kernel's FD-close ungrab still needs G4 proof (unchanged); whether `RestrictAddressFamilies=AF_UNIX` must later grow `AF_NETLINK` for a udev monitor (S3).
- **Gates still open:** G3 **install** (accepted, not run), G4 IRL interception/crash/hang/recovery, S3 watchdog/notify loop, S4 session IPC, G8 autostart, G6 licensing.

## Deviations, risks, missing evidence

- `DevicePolicy=closed` added to the unit so listed `DeviceAllow` entries actually restrict devices. Without it, systemd default `auto` would not narrow.
- `libsystemd` kept out. The unit is `Type=notify` + `WatchdogSec=2` as specified; the binary still prints version and exits. Starting the unit now fails closed. S3 owns `sd_notify` + watchdog pings.
- Planner S2 enter-gate said "G3 accepted **and installed**." This prompt authorized authoring the files **before** install. Install remains COOPERATOR-owned.
- Prompt rollback wording "three installed files": operations.md names all four artifacts (sysusers + two udev + unit) plus `userdel`/`groupdel`.

## Resolved Execution Issues / Near-Misses

- **CMAKE_ROOT / PATH:** same client environment as session 02/01. Cause: poisoned `CMAKE_ROOT`. Resolution: invoke system CMake with `PATH=/usr/bin:...` and `env -u CMAKE_ROOT`. Residual risk: a later Worker using bare `cmake` may hit the same error; product commands remain `cmake -S . -B build -G Ninja`.

## Pre-Existing Failure Classification

- none (configure still prints the existing Qt `WrapVulkanHeaders` note; tests were not red)

## Smallest next step for the ORCHESTRATOR

Archive this prompt + report in META. Then have the COOPERATOR run the G3 install/verify block in `docs/operations.md` section 6 (**no start, no enable**). After that, route **S3** (watchdog / `sd_notify` / crash harness) in a fresh implementation session. This session must not continue as if grabbing or host install were done.

Transition owner: ORCHESTRATOR  
Stop.