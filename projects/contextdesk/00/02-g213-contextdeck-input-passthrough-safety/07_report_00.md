### Report for ORCHESTRATOR_CHAT

- **logical-whole identity:** `g213-contextdeck-input-passthrough-safety`
- **Worker-session ordinal:** `07`
- **Worker-exchange ordinal:** `00`
- **Worker session target:** `fresh-worker-session`
- **Native planning mode:** `not-used`
- **Worker session profile:** Fresh Independent Acceptance (S5 IRL G4)
- **acceptance status:** **BLOCKED**
- **status:** **BLOCKED**
- **phase-qualified result:** not-applicable (G4 IRL was not executed)
- **Logical-whole closure:** not-closed
- **Report justification:** `new-evidence`
- **Authority:** read-only acceptance; expires at this terminal report

Coordinates were not spelled in the prompt; they are taken from the expected META names `07_acceptance_00.md` / `07_report_00.md` plus “fresh” in the prompt.

```text
Acceptance candidate: 9924b1b1ac0206a0d252cbe68fdd1ce91e0c74d6 (AP pin 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26)
Acceptance owner map: docs/operations.md G3+G4/S5, docs/testing-m2.md, docs/architecture.md
Acceptance allowlist: host G4 procedure only; no repository mutation
Acceptance risk claims: grab, crash, hang, recovery, coexistence, uninstall
Acceptance control matrix: start-disarmed; explicit authenticated ARM; no autostart; ungrab-on-death; input-remapper unchanged; G3 ACLs restored
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: production grab path + documented S5 install + session-app ARM + production hang harness + installed unit matching S4
Out-of-scope observations: none
Escalation disposition: NEEDS_ORCHESTRATOR_DECISION
```

G4 areas A–G were **not** run. Abort was required before starting or arming the broker.

## Verified repository and AP anchors

| Anchor | Value |
|--------|--------|
| HEAD | `9924b1b1ac0206a0d252cbe68fdd1ce91e0c74d6` (matches prompt) |
| Parent | `ae1291134fd4f2c2980a6b933a29a57cb44cd058` |
| Subject | `Add authenticated Unix-socket session IPC and broker lease.` |
| AP pin (`.ap` gitlink + HEAD) | `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` |
| Worktree / index | clean |
| Branch | `main` tracks `origin/main` |
| Local `origin/main` | equal (`rev-list --left-right --count` = `0 0`). This session did **not** fetch. |

Remote identity: `https://github.com/cisarik/contextdesk`.

This candidate is the S4 IPC commit. Production `runIdleBroker()` still constructs **FailClosedSink / FailClosedSource**. `nm` on `main.cpp.o` shows those types and no `RealSink` / `EvdevGrabber`. Linked `build/contextdeck-broker`: `RealSink::create` = 0, `EvdevGrabber::create` = 0. `CMakeLists.txt` has **no** `install()` rule. `docs/operations.md` still says S4 ARM fail-closes and that starting the unit is forbidden until S5/G4; there is **no** documented S5 install procedure and **no** install prefix.

Session app `BrokerIpcClient::start()` sends **STATUS only**. Nothing in the session app calls `arm()` or `acquireLease()`. There is no documented production hang switch; `watchdog-selftest` is in-process and device-free.

## G3 precondition result

**ACL/security policy: PASS.** Unit/binary consistency with this S5 candidate: **FAIL** (abort gate).

| Check | Result |
|--------|--------|
| G213 event nodes (USB `046d:c336`, if00+if01) | group `contextdeck-broker`, mode `0660`, **no** session-user ACL |
| G213 hidraw | session-user ACL present (`rw-`) |
| `/dev/port` | **no** session-user ACL |
| `/dev/i2c-*` (8 nodes) | **no** session-user ACL |
| session user in group `input` | **no** |
| udev guard/grant vs repo | **byte-identical** |
| sysusers file vs repo | **match**; user and group `contextdeck-broker` exist |
| installed unit vs repo | **DIFF** — host `RuntimeDirectoryMode=0750` (S3-era comments); repo is `0755` |
| `/usr/bin/contextdeck-broker` | **missing** |
| `contextdeck-broker.service` | `static`, `inactive`/`dead`, not enabled, `Restart=no`, `WatchdogSec=2` in the file, `ExecStart=/usr/bin/contextdeck-broker` |
| `systemd-analyze verify` (installed and repo) | exit **1**, only missing binary |
| input-remapper | **enabled** and **active**; G213-named user config entry present; not modified |

Prompt rule: do not improvise an install prefix; do not continue if unit, binary, G3 policy, or recovery path is inconsistent. The missing binary plus `0750` vs `0755` is that inconsistency. `0750` would also make `/run/contextdeck` untraversable for the seat user unless that user joined `contextdeck-broker` (forbidden: that group owns G213 event nodes).

## Independent recovery path

**Not demonstrated as a second physical keyboard.** One extra named key device besides the G213 was a **virtual** device class (input-remapper), not a laptop/PS/2 or other physical keyboard. `sshd.service` is enabled/active. This session is local Wayland `seat0`, not SSH. tty1–6 device nodes exist; they must not be assumed reachable **from the grabbed G213**. OpenRGB was **not** running (no loopback `:6742`).

Because grab never started, this was recorded and not used.

## Exact host operations performed

Read-only only:

- git identity / cleanliness / AP pin
- mandatory docs (`AGENTS.md`, AP safety/worker contracts, `ROADMAP.md`, architecture, operations G3/G4/S5, `testing-m2.md`, hardware matrix and zone map)
- `systemctl` show/cat/`is-enabled`/`is-active` for broker and input-remapper
- file compare of installed G3 udev/sysusers/unit vs repo
- `getfacl` on G213 event/hidraw, `/dev/port`, `/dev/i2c-*` (semantic pass/fail only)
- `nm` on the local build broker
- `systemd-analyze verify` (does not start the unit)

**Not performed:** install of the binary, `daemon-reload`, start/enable/restart/reload of the broker, ARM/LEASE over the socket, session-app arm, `EVIOCGRAB`, open of G213 event nodes or `/dev/uinput`, SIGTERM/SIGKILL of a live broker, hang induction, OpenRGB start, input-remapper change, G3 udev/sysusers change, uninstall.

## G4 area results (not executed)

| Area | Result |
|------|--------|
| A. Controlled startup and lease arming | **not executed** — no installed binary; production ARM is fail-closed; session app has no ARM path; ad-hoc socket injection is forbidden |
| B. Real G213 pass-through fidelity | **not executed** — no production grab; OpenRGB was not running |
| C. SIGTERM recovery | **not executed** |
| D. SIGKILL/crash recovery | **not executed** |
| E. Hang/watchdog recovery | **not executed** — no documented production hang harness |
| F. input-remapper coexistence | **precondition only:** enabled/active, config not touched; grab-time coexistence **not executed** |
| G. Uninstall and restoration | **not executed** — this session installed nothing; G3 left in place |

## Final broker enabled/active state

- enabled: **static** (not enabled; no `[Install]` section)
- active: **inactive** / **dead**
- no real-grab path was activated
- no autostart was added

## Final ACL/security state

Unchanged from the G3 precondition PASS above. Event nodes still have no session-user ACL. Hidraw session ACL remains. `/dev/port` and `/dev/i2c-*` remain without session-user ACL. The measured OpenRGB uaccess hole was **not** reopened.

## Residual risks

- S5 production wiring does not exist on this candidate. `RealSink` / `EvdevGrabber` remain unused; `GrabbingSource::openSource()` does not open devices.
- Host unit is stale (`RuntimeDirectoryMode=0750`). Even a later install of the S4 binary would leave the seat user unable to reach the socket without a keylogging group join.
- Session app never arms; G4 “documented session-app/IPC path” for explicit ARM is not implemented.
- No documented S5 install, no CMake install prefix, no production hang harness.
- Independent physical recovery keyboard was not present; SSH exists but was not used. Grabbing on this seat would have been unsafe under the prompt’s recovery rule.
- OpenRGB was down; hidraw ACL is present but lighting function was not exercised.
- `systemctl show WatchdogUSec` on the inactive unit reported `infinity`; the file still has `WatchdogSec=2`. Not measured at runtime.

## Explicit hygiene

No repository files were modified. No commit and no push were performed. No META files were changed. G3 udev/sysusers policy was not altered. input-remapper was not stopped, disabled, or reconfigured. The broker was **not** enabled, **not** started, **not** armed, and **not** grabbed. No key codes, key names, scan values, raw events, USB serials, or per-event timing are included here.

**Logical-whole closure: not-closed.** This is not G4 PASS or FAIL. It is not whole closure.

Resolved Execution Issues / Near-Misses: an extra key device was first classed as an independent physical keyboard; recheck showed a virtual (input-remapper) device. Grab was never started.

Pre-Existing Failure Classification: S5 real-grab/install/ARM/hang path absent on candidate `9924b1b1`; installed unit still S3 `RuntimeDirectoryMode=0750`.

Smallest next step (Orchestrator / COOPERATOR; this Worker has no further authority): implement a bounded S5 production slice (enumerator + `RealSink`/`EvdevGrabber` on the broker path, CMake/docs install to `/usr/bin/contextdeck-broker`, refresh the installed unit to repo `0755`, documented session-app ARM, documented hang harness), then reissue a fresh independent G4 acceptance. Do not start the current unit.

Expected META archive names (Orchestrator / COOPERATOR; this Worker did not archive):

- `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/07_acceptance_00.md`
- `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/07_report_00.md`