### Report for ORCHESTRATOR_CHAT

- **logical-whole identity:** `g213-contextdeck-input-passthrough-safety`
- **Worker-session ordinal:** `06`
- **Worker-exchange ordinal:** `00`
- **Worker session target:** `fresh-worker-session`
- **Native planning mode:** `not-used`
- **acceptance status:** **acceptance-PASS**
- **phase-qualified result:** S4 acceptance only. Logical whole **not-closed**. S5 IRL G4 remains separate.
- **Authority:** read-only; expires at this terminal report.

## Verified identity

| Anchor | Value |
|--------|--------|
| HEAD | `9924b1b1ac0206a0d252cbe68fdd1ce91e0c74d6` |
| Parent (S3) | `ae1291134fd4f2c2980a6b933a29a57cb44cd058` |
| Subject | `Add authenticated Unix-socket session IPC and broker lease.` |
| AP pin (`.ap` gitlink + HEAD) | `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` |
| Worktree / index | clean (`git status --porcelain=v1` empty; no staged diff) |
| Branch | `main` tracks `origin/main` |
| Local `origin/main` | **equal** to HEAD (`rev-list --left-right --count` = `0 0`). This session did **not** fetch. |

Remote identity: `https://github.com/cisarik/contextdesk`.

## Exact changed paths (S4 vs S3)

Diff `ae129113…` → `9924b1b1…` is **18 paths**, all inside the S4 implementation allowlist. Nothing outside it.

| Path | Role |
|------|------|
| `src/broker/IpcProtocol.{h,cpp}` | length-prefixed codec; verbs only; no UID/GID fields |
| `src/broker/SessionIpc.{h,cpp}` | listen/accept, `SO_PEERCRED`, one lease, arm/disarm, fail-closed teardown |
| `src/broker/IdleWait.{h,cpp}` | extra epoll fds on the existing signalfd wait (S3 loop, same thread) |
| `src/broker/main.cpp` | listen + `SessionIpc` on the loop; `Acquisition` wired to fail-closed sources/sink |
| `src/app/BrokerIpcClient.{h,cpp}` | Qt client; startup probe is `STATUS` only |
| `src/app/SessionApplication.{h,cpp}` | construct/start the client; **no** `arm()` / `acquireLease()` |
| `tests/unit/test_broker_ipc.cpp` | device-free IPC/lease/auth tests |
| `CMakeLists.txt` | `contextdeck_ipc`, `SessionIpc`, `test_broker_ipc`, Qt Network |
| `packaging/systemd/contextdeck-broker.service` | `RuntimeDirectoryMode=0755` + comments |
| `docs/architecture.md`, `docs/operations.md`, `docs/testing-m2.md`, `docs/specification.md` | protocol, permissions, lifecycle, coverage |

`git diff --check` on that range: **exit 0**. Unrelated files (`src/broker` identity/ledger/forwarding/acquisition/watchdog, `packaging/udev`, `packaging/sysusers.d`, `AGENTS.md`, `ROADMAP.md`, `.ap/`) are unchanged.

## Test commands and exit statuses

Existing S4 binaries were used (objects newer than the S4 sources; no rebuild, no install). UID of this session: **1000** (not root).

| Command | Exit |
|---------|------|
| `ctest --test-dir build -R test_broker_ipc --output-on-failure` | **0** (1/1 `test_broker_ipc`) |
| `ctest --test-dir build --output-on-failure` | **0** (**9/9**) |
| `./build/contextdeck-broker selftest` | **0** |
| `./build/contextdeck-broker watchdog-selftest` | **0** |

`test_broker_ipc` covers: codec bounds; `LEASE uid=1000` malformed; `SO_PEERCRED` accept of same UID; reject of wrong UID, failed creds, and uid 0; lease acquire without arming; duplicate `ERR LEASE_HELD`; holder `ARM`/`DISARM`/`HEARTBEAT`/`RELEASE`; unauthorized `ARM`/`DISARM` and unknown `INJECT`; disconnect / zero-length frame / expiry / `shutdown` ungrab-first on `FakeGrabber`; listen mode `0666` without arm-before-auth; logind authorizer rejects uid 0 and pid 0.

Identity, ledger, forwarding, acquisition, and watchdog units still pass, so those invariants were not regressed by this slice.

## IPC / security findings

- Broker idle path constructs `Acquisition` **disarmed**. `listen()` only binds/chmods the Unix socket and logs `ipc-listening`. Socket existence does not call `arm()`.
- Session app `BrokerIpcClient::start()` connects and sends **`STATUS` only**. `SessionApplication::start()` does not call `arm()` or `acquireLease()`.
- Peer identity is kernel `getsockopt(SO_PEERCRED)` (`ucred` pid/uid/gid). Failed creds or `pid <= 0` close the fd **before** command parse. GID is read and ignored. There are **no** client UID/GID protocol fields; extra tokens are malformed.
- Production authorizer (`LogindSeatAuthorizer`) fail-closes unless: pid > 0, **uid ≠ 0**, logind session UID equals kernel UID, non-empty seat, type `wayland` or `x11`, `sd_session_is_active > 0`, `sd_session_is_remote == 0`. Remote, inactive, non-graphical, uid 0, and bad pid are rejected in code.
- One lease fd. Second peer: `ERR LEASE_HELD`. `ARM`/`DISARM`/`HEARTBEAT`/`RELEASE` without the holder: `ERR NO_LEASE` or `ERR UNAUTHORIZED`.
- Verbs are only `STATUS`, `LEASE`, `HEARTBEAT`, `ARM`, `DISARM`, `RELEASE`. No inject-keys or policy-blob protocol. `INJECT` → `ERR UNKNOWN`.
- Directory mode `0755`, socket `0666`: connectability is not authorization (documented). Group membership is not used as auth.
- Watchdog feed remains the **event-loop thread** (`WATCHDOG=1` after wait + `afterWait`). No broker helper thread, no detached lease feeder. Session-app `QTimer` only sends holder `HEARTBEAT` on the socket; expiry/disconnect still disarm on the broker.
- Production `ARM` is `Acquisition::arm()` through **fail-closed** sink/sources (`createVirtual()` / `openSource()` false). `RealSink` / `EvdevGrabber` are **not** constructed on the broker main path (`nm` on `main.cpp.o`: no those symbols; `FailClosedSink` / `FailClosedSource` / `SessionIpc` present).

## Lease teardown findings

`releaseLease()` calls `IArmControl::disarm()` **before** clearing the lease fd. `Acquisition::disarm()` is still ungrab physical → synthetic ledger disarm → destroy virtual.

Observed in `test_broker_ipc` on `FakeGrabber` + real `Acquisition`:

- holder disconnect → disarmed, lease dropped, history `unclaim-if01` before `synthetic-disarm` before `destroy-virtual`
- malformed length prefix → disarmed, lease dropped
- TTL expiry (`expireLease`) → disarmed, lease dropped
- `shutdown()` → disarmed, lease dropped
- holder `RELEASE` → `OK RELEASED`, disarmed, lease dropped
- holder `DISARM` → unarmed, **lease kept**

`IdleWait` Stop (SIGTERM/SIGINT) skips `afterWait`, then `main` calls `ipc.shutdown()`, which still disarms first.

## systemd validation (static)

```
systemd-analyze verify packaging/systemd/contextdeck-broker.service
```

**Exit 1** — sole reported issue: `Command /usr/bin/contextdeck-broker is not executable: No such file or directory`. Classified as **missing installed binary**, not a unit-syntax error. Binary was **not** installed.

Unit still: `Type=notify`, `WatchdogSec=2`, `Restart=no`, `LimitCORE=0`, `RuntimeDirectoryMode=0755`, **no** `[Install]` section.

Host read-only: `systemctl is-active contextdeck-broker.service` → `inactive`; `is-enabled` → `static`. This session did not enable, start, restart, reload, or daemon-reload.

## Forbidden-operation checks (added S4 sources only)

Inspected added/changed sources (`IpcProtocol`, `SessionIpc`, `IdleWait`, `main.cpp`, `BrokerIpcClient`, `SessionApplication`, `test_broker_ipc`):

- no `EVIOCGRAB`
- no `libevdev_grab`
- no open of `/dev/input`
- no open of `/dev/uinput`
- no production `RealSink` / `EvdevGrabber` activation (fail-closed stand-ins in `main`; tests use `FakeGrabber`)
- no input-remapper, udev, or sysusers mutation (those paths are absent from the S4 diff)

No key codes, raw event payloads, USB serials, or per-event timing are reported here.

## Residual risks

- Production `ARM` still fail-closes until S5 binds real G213 sources and `RealSink`. That is required, not a defect.
- G4 still owns kernel ungrab-on-close, hang/crash on a live seat, and pass-through fidelity.
- Any **other** local seated graphical UID can take a free lease (`LogindSeatAuthorizer` does not pin one account). Same-UID session compromise can `LEASE`/`ARM` (pass-through only; no inject-keys). Owned by the COOPERATOR; already in architecture.
- World-connectable socket is intentional; auth is `SO_PEERCRED` + logind.
- Logind remote/inactive/non-graphical rejection is implemented but not mocked beyond uid 0 / pid 0. Non-holder `HEARTBEAT`/`RELEASE` follow the same unauthorized path as `ARM`/`DISARM` in code; only the latter pair is asserted in CTest.
- `BrokerIpcClient::arm()` exists for later UI and is unused at session start. If called, it starts the heartbeat timer before `OK ARMED`.
- Docs list `ERR UNAUTH` among replies; unauthenticated peers are closed with **no** reply (stricter). Unused token only.

## Explicit non-claims / hygiene

No repository file was modified. No commit and no push were performed. META was not written. The broker was **not** enabled, **not** started, **not** restarted, **not** reloaded, and **not** real-grabbed. No G213 event node and no `/dev/uinput` was opened. input-remapper and G3 udev/sysusers were not changed.

**Logical-whole closure: not-closed.** S5 IRL G4 remains a separate route.

Expected META archive names (Orchestrator / COOPERATOR; this Worker did not archive):

- `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/06_acceptance_00.md`
- `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/06_report_00.md`