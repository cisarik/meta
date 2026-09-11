### Report for ORCHESTRATOR_CHAT

- **logical-whole identity:** `g213-contextdeck-input-passthrough-safety`
- **Worker-session ordinal:** `05`
- **Worker-exchange ordinal:** `00`
- **Worker session target:** `fresh-worker-session`
- **Native planning mode:** `not-used`
- **status:** PASS
- **phase-qualified result:** not-applicable (S4 implementation only; not acceptance)
- **Report justification:** `new-mutation`
- **Authority:** expires at this terminal report. No further mutation, grab, service operation, or archive write is authorized from this session.

This is only an S4 implementation report. It does **not** claim acceptance-PASS or logical-whole closure.

## Repository identity and verified anchors

- **Root:** `/home/agile/Projects/contextdesk`
- **Remote identity:** `https://github.com/cisarik/contextdesk`
- **Baseline HEAD (required S3 commit, verified before mutation):** `ae1291134fd4f2c2980a6b933a29a57cb44cd058`
- **Previous baseline named in the prompt:** `69f433c382d7dffe6d8b8f1aea41ca7c6931a4f6` (ancestor of S3)
- **AP submodule pin (gitlink + `.ap` HEAD):** `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`
- **Worktree before mutation:** clean
- **End commit:** `9924b1b1ac0206a0d252cbe68fdd1ce91e0c74d6`
- **Push:** not performed

## Baseline result

Clean `PATH` configure/build (`CMAKE_ROOT` is poisoned in the default environment; same documented workaround as operations.md):

- `cmake -S . -B build -G Ninja` — success
- `cmake --build build` — success (ninja: no work to do)
- `ctest --test-dir build --output-on-failure` — **exit 0**, **8/8** passed

## Implementation allowlist (stated before editing)

**In:**

- `src/broker/IpcProtocol.{h,cpp}`
- `src/broker/SessionIpc.{h,cpp}`
- `src/broker/IdleWait.{h,cpp}` (epoll extra-fd registration; proven IPC dependency on the S3 loop)
- `src/broker/main.cpp`
- `src/app/BrokerIpcClient.{h,cpp}`
- `src/app/SessionApplication.{h,cpp}`
- `tests/unit/test_broker_ipc.cpp`
- `CMakeLists.txt`
- `packaging/systemd/contextdeck-broker.service` (`RuntimeDirectoryMode` only)
- `docs/architecture.md`, `docs/operations.md`, `docs/testing-m2.md`, `docs/specification.md`

**Out:** S5 real-keyboard acceptance; host grab; `systemctl start/enable`; input-remapper; G3 udev/sysusers; AP/`.ap`/`AGENTS.md`/META/handout; key/code/serial logging; `RealSink::create`; opening `/dev/input` or `/dev/uinput`.

`RuntimeDirectoryMode` `0750` → `0755` is required so the seat user can reach the socket **without** joining group `contextdeck-broker` (that group owns G213 event nodes).

## Exact changed paths

| Path | Purpose |
|------|---------|
| `src/broker/IpcProtocol.{h,cpp}` | length-prefixed codec, command parse, no UID fields |
| `src/broker/SessionIpc.{h,cpp}` | listen/accept, `SO_PEERCRED`, lease, arm/disarm, fail-closed teardown |
| `src/broker/IdleWait.{h,cpp}` | register IPC fds on the existing signalfd epoll wait |
| `src/broker/main.cpp` | listen + `SessionIpc` on the event loop; `Acquisition` fail-closed (no devices) |
| `src/app/BrokerIpcClient.{h,cpp}` | Qt client; startup probe is `STATUS` only |
| `src/app/SessionApplication.{h,cpp}` | construct/start the client; no auto-arm |
| `tests/unit/test_broker_ipc.cpp` | device-free IPC/lease/auth tests |
| `CMakeLists.txt` | `contextdeck_ipc`, `SessionIpc`, `test_broker_ipc`, Qt Network |
| `packaging/systemd/contextdeck-broker.service` | `RuntimeDirectoryMode=0755` + comments |
| `docs/architecture.md` | Unix-socket + `SO_PEERCRED` + lease lifecycle |
| `docs/operations.md` | protocol, permissions, lifecycle, TTY recovery (§8) |
| `docs/testing-m2.md` | `test_broker_ipc` coverage |
| `docs/specification.md` | broker now exists; remapping still not executed |

## IPC protocol and `SO_PEERCRED` design

- **Socket:** `/run/contextdeck/broker.sock` (`RuntimeDirectory=contextdeck`). Tests/dev: `CONTEXTDECK_BROKER_SOCKET`.
- **Framing:** 16-bit little-endian length + 1–256 ASCII bytes. No NULs. No client UID/GID fields. Extra tokens (`LEASE uid=1000`) are malformed.
- **Commands:** `STATUS`, `LEASE` `[ms]`, `HEARTBEAT` `[ms]`, `ARM` `[ms]`, `DISARM`, `RELEASE`. Default TTL **6000** ms, clamp **1000–30000**. No inject-keys, no policy blobs, no chords.
- **Auth:** on `accept`/`attach`, `getsockopt(SO_PEERCRED)` (`ucred` pid/uid/gid from the kernel). `pid<=0` or failed creds → close, no command parse, no arm. GID is read and **ignored**. Production authorizer: logind seated local graphical session (`sd_pid_get_session`, `sd_session_get_uid` must match kernel UID, non-empty seat, type `wayland`/`x11`, `sd_session_is_active>0`, `sd_session_is_remote==0`). **uid 0 rejected.** Tests inject `FixedUidAuthorizer` / `KernelPeerCredentials` / scripted creds.
- **Permissions:** dir `0755`, socket `0666`. Connectability is not authorization. Session user is **not** added to `contextdeck-broker`.

## Lease lifecycle and failure behavior

Broker **starts disarmed**. Listening does not arm.

1. Authenticated peer `LEASE` → one owner. Second peer → `ERR LEASE_HELD`.
2. Holder `ARM` → `IArmControl::arm()` (`AcquisitionArmControl`).
3. Holder `HEARTBEAT` renews TTL. Holder `DISARM` ungrabs but keeps the lease. Holder `RELEASE` disarms and drops the lease.
4. **Disconnect / malformed frame / lease expiry / shutdown:** `Acquisition::disarm()` **first** (ungrab physical, then LIFO synthetic releases, then destroy virtual), then drop lease and close.

Production `ARM` is wired to `Acquisition::arm()` but sources/sink **fail closed** (`createVirtual()` false). No enumerator, no `RealSink`, no evdev open. Tests use `FakeGrabber` and prove ungrab-first order. Session app starts a probe client and **does not auto-arm**.

## Security properties

- No implicit arming from socket existence.
- No group-only authorization.
- No trust of client-supplied UID/GID (those fields do not exist).
- Kernel `SO_PEERCRED` only.
- One lease.
- Release/ungrab before teardown on disconnect, malformed, expiry, and shutdown.
- Identity matching, ledger, 1:1 forwarding, SYN pairing, `SYN_DROPPED`, all-or-nothing acquisition, ungrab-first teardown **unchanged**.
- No key codes, names, scans, payloads, serials, or per-event timing in logs.

## Tests (exact exit statuses)

| Command | Exit |
|---------|------|
| baseline `ctest` (8 tests) | **0** |
| `ctest --test-dir build --output-on-failure` after S4 (9 tests) | **0** |
| `test_broker_ipc` (via CTest) | **0** |
| `./build/contextdeck-broker selftest` | **0** |
| `./build/contextdeck-broker watchdog-selftest` | **0** |

`test_broker_ipc` covers: codec bounds; rejection of client UID tokens; `SO_PEERCRED` accept/reject (wrong UID, failed creds, uid 0); lease acquire; duplicate lease; explicit arm/disarm; unauthorized ARM/DISARM; unknown `INJECT`; disconnect cleanup; malformed length; lease expiry; shutdown cleanup; listen/accept `0666` without arm-before-auth; logind rejects uid 0 / pid 0.

## systemd validation

```
systemd-analyze verify packaging/systemd/contextdeck-broker.service
```

**Exit 1** — `Command /usr/bin/contextdeck-broker is not executable: No such file or directory` (binary not installed; expected). No other unit errors reported. Still **no `[Install]`**, `Restart=no`, `WatchdogSec=2`, `Type=notify`, `LimitCORE=0`.

`systemctl is-active contextdeck-broker.service` → `inactive`  
`systemctl is-enabled contextdeck-broker.service` → `static` (no `[Install]`; cannot be enabled)

This session did **not** install, enable, start, or restart the unit.

`nm` on `main.cpp.o`: no `RealSink` / `EvdevGrabber` / `libevdev_grab` references.

## Commit hash

`9924b1b1ac0206a0d252cbe68fdd1ce91e0c74d6`  
`Add authenticated Unix-socket session IPC and broker lease.`  
Local `main` only; **not pushed**.

## Remaining risks

- Production `ARM` fail-closes until S5 binds real G213 sources and `RealSink` (still forbidden here).
- G4 still owns kernel ungrab-on-close, hang/crash on a live seat, and pass-through fidelity.
- Same-UID compromise of the seated graphical session can still `LEASE`/`ARM` (pass-through only; no inject-keys). Owned by the COOPERATOR.
- Production auth needs logind; a broker started outside a systemd seat context will reject peers.
- World-connectable socket is intentional; authorization is `SO_PEERCRED`+logind, not mode bits.
- `BrokerIpcClient::arm()` exists for later UI and is **not** called from `SessionApplication::start()`.

## Explicit non-claims

The broker was **not** enabled, **not** started, and **not** real-grabbed. No G213 event node and no `/dev/uinput` was opened. input-remapper was not modified. G3 udev/sysusers were not modified. AP/META/handout/`AGENTS.md` were not modified. This Worker did not self-archive.

**Smallest next step:** S5 IRL G4 pack (real grab/pass-through/crash/hang/TTY on this kernel), only after an Orchestrator prompt and only if G3 is actually installed on the seat.

Resolved Execution Issues / Near-Misses: systemd login API on this host is `sd_session_is_remote`, not `sd_session_get_remote`; switched at compile time. Residual: none.

Pre-Existing Failure Classification: none