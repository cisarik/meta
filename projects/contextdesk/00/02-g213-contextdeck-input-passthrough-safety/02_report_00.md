### Report for ORCHESTRATOR_CHAT

Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 02
Worker exchange ordinal: 01

- status: **PASS**
- Phase-qualified result: **implementation-PASS**
- Result artifact or commit: `1d9d6f18f906c5d3827a271d970e4308777437fa` .. `553e75b028f60f26aac846924a684069835d75d5` (three local commits on `main`)
- Result evidence: configure + build + full CTest 6/6 green; `./build/contextdeck-broker` prints version and exits 0; `./build/contextdeck-broker selftest` exits 0 with idle counters and no device I/O
- Logical-whole closure: **not-closed**
- start commit: `d03313340f427eabd06eb55269d6ae7be87984d7`
- end commit: `553e75b028f60f26aac846924a684069835d75d5`
- Changed files: allowlisted only (`CMakeLists.txt`, `src/broker/**`, `tests/unit/test_broker_*`)
- tests and validation: 6/6 CTest passed (3 existing + 3 new); selftest ok; grab/uinput/udev/IPC not tested (forbidden)
- commit and push result: local `1d9d6f1`, `6499a68`, `553e75b`; push not authorized
- Report justification: **new-mutation**
- Authority expiry: implementation authority expired at this terminal report; further mutation, grabbing, host enablement, acceptance, publication, META self-archival, and closure remain unauthorized

## Capability handshake

- Product/client: Cursor coding session; identity not independently attested.
- Native planning mode: prompt `not-used`; observed disabled/absent (implementation tools available; Plan Mode not used).
- Writable scope: allowlisted product paths plus gitignored `build/`; META not written.
- Context headroom: sufficient; no compaction stop.
- Commit capability exercised under prompt git authority; capability is not further commit authority.
- Credentials: not probed.
- Sub-agents: not used.

## Repository gate

- Root `/home/agile/Projects/contextdesk`, remote `https://github.com/cisarik/contextdesk.git`, branch `main`.
- Baseline HEAD matched `d03313340f427eabd06eb55269d6ae7be87984d7`; worktree clean excluding gitignored `build/`.
- `origin/main`: `ca3ac07c5fecfe3c983078e343ec6b3e02c75bea` (local ahead; not treated as drift; not pushed).
- `.ap` gitlink and checkout: `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`.
- No active Git operation. Ending worktree clean.
- Dependencies: `libevdev` 1.13.7, `libudev` 261; `libevdev-uinput.pc` absent as specified; linked `-levdev` only. `libsystemd` not used.

## Stage table

| Stage | Result | Reason |
|---|---|---|
| B1 | green | Identity matcher, ledger, acquisition skeleton, tests 1–2, CMake targets, version binary; committed `1d9d6f1` |
| B2 | green | ISource/ISink, FakeSource/FakeSink, forwarding with SYN pairing and repeat pass-through, RealSink compiled and never constructed; test 3; committed `6499a68` |
| B3 | green | Engine SYN_DROPPED reconciliation, ungrab-first disarm emitting balanced releases to FakeSink, `selftest` subcommand; committed `553e75b` |

## Changed files and purpose

**B1 `1d9d6f1`** — fail-closed identity and balanced ledger without grabbing:
- `CMakeLists.txt` — `contextdeck_broker_core`, `contextdeck-broker`, pkg-config `libevdev`/`libudev`, AUTOMOC off on broker targets
- `src/broker/Types.h`, `Logger.*`, `IdentityMatcher.*`, `KeyLedger.*`, `Acquisition.*`, `main.cpp`
- `tests/unit/test_broker_identity.cpp`, `tests/unit/test_broker_ledger.cpp`

**B2 `6499a68`** — 1:1 forwarding engine on fakes:
- `src/broker/ISource.h`, `ISink.h`, `FakeSource.*`, `FakeSink.*`, `ForwardingEngine.*`, `RealSink.*`
- `tests/unit/test_broker_forwarding.cpp`

**B3 `553e75b`** — dropped-sync + teardown + device-free selftest:
- `src/broker/Selftest.*`, `main.cpp` (`selftest` subcommand)
- Acquisition/ledger: ungrab-first then LIFO synthetic releases onto `ISink`
- Extra SYN_DROPPED / disarm assertions in the broker unit tests

## Contracts check

| Contract | Result |
|---|---|
| Identity matcher | Implemented. Accepts `046d:c336` if00/if01 on USB/Bluetooth only. Rejects `BUS_VIRTUAL`, name prefix `ContextDeck` (including `ContextDeck G213 passthrough`), unresolved fields, wrong VID/PID, other interfaces. Node numbers are not identity; udev property names `ID_VENDOR_ID` / `ID_MODEL_ID` / `ID_USB_INTERFACE_NUM` are the resolution contract. `candidateFromUdev()` exists and was **not** invoked. |
| Ledger | Two ledgers: physical per source, synthetic per sink. Press/release balance; repeat (`value==2`) is a no-op on the ledger; disarm LIFO; never emits a synthetic release for a key that was not synthetically pressed; other-source physical ownership is left intact on `SYN_DROPPED`. |
| Forwarding | Single-thread ingest: `EV_KEY`/`EV_LED`/`EV_MSC` then matching `SYN_REPORT` per source batch. Repeat forwarded verbatim. No remap/command catalog. Game Mode and Backlight have **no** broker identifiers. `KEY_STOP` is not special-cased. |
| `SYN_DROPPED` | Engine updates physical state from the source, forwards only minimal reconciling press/release so the virtual side matches, never treats those as commands, counters only (`droppedSync`, `keysDownPhysical`, `keysDownSynthetic`). |
| Teardown | Plan governs over the prompt's reverse wording: **ungrab physical first**, then balanced synthetic releases, then destroy virtual. Failure path releases in reverse interface order and ends disarmed. `claimSource()` is a hook; **no `EVIOCGRAB` / `libevdev_grab()`**. |
| `RealSink` | Code present (`BUS_VIRTUAL`, vendor `0x0000`, product `0x0001`, name `ContextDeck G213 passthrough`, EV_KEY union, EV_LED from if00 only, no `EV_REP`). **`RealSink::create` was never called.** |
| Logging | State names, error classes, counters. No key codes, names, scan values, or per-event timing on runtime paths. |
| CMake | Static `contextdeck_broker_core` + thin `contextdeck-broker`. No ECM, no `libevdev-uinput.pc`, no Qt in the broker core. |

Deviation named: prompt §D listed orderly disarm as synthetic-then-ungrab; Planner report §D and the causal regression required **ungrab-first**. The plan was treated as governing, as the prompt instructed.

## Tests and validation

CTest (all green):

1. `test_profile_resolver`
2. `test_profile_persistence`
3. `test_openrgb_protocol`
4. `test_broker_identity`
5. `test_broker_ledger`
6. `test_broker_forwarding`

Also: `./build/contextdeck-broker` → `contextdeck-broker 0.1.0`; `./build/contextdeck-broker selftest` → `selftest: ok` with `droppedSync=1`, `keysDownPhysical=0`, `keysDownSynthetic=0`.

Deliberately not tested: real `/dev/input`, `/dev/uinput`, `EVIOCGRAB`, udev/sysusers/systemd, IPC, latency p99, crash/SIGKILL on this kernel, Game Mode/Backlight (firmware-only; no host events), GUI/QML.

R1 inline: no key-content logging, no shell, no network in the broker, no privilege expansion. Bounded property parsing for hex IDs and interface numbers.

## COOPERATOR hand-off

What exists now: a unit-tested broker **engine** (identity, ledger, 1:1 forwarding, SYN_DROPPED, all-or-nothing acquire/disarm ordering) and a binary that links it. It cannot yet protect the seat.

What stays impossible until later stages: opening G213 event nodes, grabbing, creating the virtual uinput device, udev/sysusers/system unit (S2 / G3), watchdog/crash harness (S3), session IPC (S4), IRL G4.

Build and test:

```text
cmake -S . -B build -G Ninja
cmake --build build
ctest --test-dir build --output-on-failure
./build/contextdeck-broker
./build/contextdeck-broker selftest
```

Do not open `/dev/input`, do not create `/dev/uinput`, do not grab.

## Facts / assumptions / unknowns / open gates

- **Facts:** three local commits on `main` from baseline `d033133`; 6/6 CTest; selftest idle; no grab and no real device open in this exchange; G1 matrix encoded as "no firmware-only controls in the engine."
- **Assumptions:** `RealSink::create` will open `/dev/uinput` correctly when a later stage is authorized to call it; one union virtual device remains the plan; FD-close ungrab still needs G4 on this kernel.
- **Unknowns:** none that blocked B1–B3.
- **Gates still open:** G3 (permission model / host install), G4 (IRL interception/crash/hang/recovery), G6 licensing, G8 autostart. Grabbing, udev, systemd, and IPC remain unauthorized.

## Deviations, risks, missing evidence

- Ungrab-first vs prompt §D wording: resolved in favor of the accepted plan.
- `candidateFromUdev` and `RealSink::create` are unexercised by design.
- Host still has the measured OpenRGB `uaccess` keystroke surface; this slice does not change host policy.

## Resolved Execution Issues / Near-Misses

- **CMAKE_ROOT / PATH:** this Cursor environment can expose an AppImage `PATH` and a set `CMAKE_ROOT` that makes `cmake` fail with `Could not find CMAKE_ROOT`. Cause: client environment, not the product tree. Resolution: invoke system CMake with `PATH=/usr/bin:...` and `env -u CMAKE_ROOT`. Residual risk: a later Worker using bare `cmake` in this client may hit the same error; the product commands remain `cmake -S . -B build -G Ninja`.

## Pre-Existing Failure Classification

- none (configure still prints the existing Qt `WrapVulkanHeaders` note; tests were not red)

## Smallest next step for the ORCHESTRATOR

Archive this prompt + report in META, then route **S2** only after G3 host enablement is accepted and installed. S2 is where grab, udev, sysusers, and the system unit may exist; this session must not be continued as if grabbing were now allowed.

Transition owner: ORCHESTRATOR
Stop.