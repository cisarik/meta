## Report for ORCHESTRATOR_CHAT

- **logical-whole identity:** `g213-contextdeck-input-passthrough-safety`
- **Worker-session ordinal:** `11`
- **Worker-exchange ordinal:** `00`
- **Worker session target:** `fresh-worker-session`
- **Native planning mode:** `not-used`
- **Worker session profile:** Fresh Implementation Worker — fix uinput ACL ordering
- **status:** **PASS**
- **phase-qualified result:** **implementation-PASS** (repository G3 uinput-ordering fix; host udev not installed by this session)
- **start commit:** `899df8fc14a2ad67594ff432f1b00d9ab155fd79`
- **end commit:** `24305864f54d7161048041c2e5309aa8a0f8fb1a`
- **changed files:** allowlisted product paths only (udev 62/99, operations/testing/architecture, CMake + static udev tests)
- **tests and validation:** `udevadm verify` 3/3 Success; clean-PATH configure/build; CTest **12/12**; `watchdog-selftest` ok; no grab, no `/dev/uinput` open from product code, no privileged host install
- **commit and push result:** local + `origin/main` `899df8f..2430586`
- **Logical-whole closure:** **not-closed**
- **Report justification:** `new-mutation`
- **Independence required:** no (implementation; this session cannot provide G4)
- **Authority:** expires at this terminal report

```text
Implementation authority: explicit
Exact baseline: 899df8fc14a2ad67594ff432f1b00d9ab155fd79
Required AP pin: 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26 (matched)
Changed-path allowlist: packaging/udev 62+99, docs/operations.md install/rollback/verify, docs/testing-m2.md, docs/architecture.md uinput row, CMakeLists.txt, tests/unit/test_udev_policy.cpp
Independence required: no
G4 acceptance: not claimed
Logical-whole closure: not-closed
```

## Repository gate

- Canonical checkout `/home/agile/Projects/contextdesk`, remote `https://github.com/cisarik/contextdesk.git`, branch `main`.
- Baseline HEAD matched `899df8fc14a2ad67594ff432f1b00d9ab155fd79`; worktree clean before mutation.
- `.ap` gitlink and submodule HEAD: `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`.
- Ending worktree clean; `main...origin/main` `0 0`.
- META, AP, `AGENTS.md`, `handout.md`, `ROADMAP.md`, and input-remapper were not modified.

## Exact changed paths

| Path | Purpose |
|------|---------|
| `packaging/udev/62-contextdeck-broker.rules` | G213 `event*` grant unchanged (`GROUP=contextdeck-broker`, `MODE=0660`, no `OWNER`); removed the early uinput `setfacl` RUN |
| `packaging/udev/99-contextdeck-broker-uinput.rules` | **new** — `ACTION=="add\|change"`, `KERNEL=="uinput"`, `SUBSYSTEM=="misc"`, `RUN+=/usr/bin/setfacl -m u:contextdeck-broker:rw /dev/uinput`; no `OWNER`/`GROUP`/`MODE` |
| `docs/operations.md` | Install/rollback install and remove the `99-` file; add `udevadm trigger --action=add --sysname-match=uinput --settle`; verify session ACL + `user:contextdeck-broker:rw-` + broker `access(2)` r/w; G213/hidraw/port/i2c unchanged |
| `docs/testing-m2.md` | Document `test_udev_policy` / `test_udev_verify` |
| `docs/architecture.md` | uinput row: session `uaccess` kept; broker ACL applied after that builtin |
| `CMakeLists.txt` | `test_udev_policy` + `test_udev_verify` |
| `tests/unit/test_udev_policy.cpp` | Device-free static policy: 61/62/99 rule lines, no `OWNER`, 99 sorts after `73-seat-late.rules` |

Unchanged: `packaging/udev/61-contextdeck-input-guard.rules` (G213 input / `/dev/port` / `i2c-[0-9]*` `TAG-="uaccess"`; hidraw unmatched).

## Fix

`73-seat-late.rules` queues `RUN{builtin}+="uaccess"` after `62-*`. The previous `62-` `setfacl` RUN was therefore executed **before** uaccess and was overwritten, leaving only the session-user ACL.

The additive broker ACL is now queued from `99-contextdeck-broker-uinput.rules`, which is lexicographically after `73-seat-late.rules`, so `setfacl` runs **after** uaccess. `ACTION=="add|change"` covers the same non-remove events as seat-late uaccess (a later `change` would otherwise wipe the broker ACL again). Group, mode, and the session-user uaccess ACL are not assigned by this rule.

## Tests and validation

```text
udevadm verify --resolve-names=never  (61, 62, 99)  → Success: 3  Fail: 0
udevadm verify (default name resolve)               → Success: 3  Fail: 0
env -i HOME="$HOME" PATH=/usr/bin:/bin:/usr/sbin cmake -S . -B build -G Ninja
cmake --build build
ctest --test-dir build --output-on-failure          → 12/12 Passed (0.72s)
./build/contextdeck-broker watchdog-selftest        → ok  ready=1 watchdog=3
```

New: `test_udev_policy`, `test_udev_verify`. Existing broker/profile units unchanged and green.

Not run (forbidden): start/enable/restart/reload/arm/grab of `contextdeck-broker`; opening G213 event nodes or `/dev/uinput` from product code; privileged host udev/sysusers/systemd install; input-remapper changes; META archive.

## Remaining host-install steps (COOPERATOR-run, privileged)

Do **not** enable, start, arm, or grab. Re-apply G3 udev so the installed `62-` loses the early RUN and `99-` is present:

```sh
sudo install -m 0644 packaging/udev/62-contextdeck-broker.rules \
  /etc/udev/rules.d/62-contextdeck-broker.rules
sudo install -m 0644 packaging/udev/99-contextdeck-broker-uinput.rules \
  /etc/udev/rules.d/99-contextdeck-broker-uinput.rules
sudo udevadm control --reload-rules
sudo udevadm trigger --subsystem-match=input
sudo udevadm trigger --subsystem-match=i2c-dev
sudo udevadm trigger --sysname-match=port
sudo udevadm trigger --action=add --sysname-match=uinput --settle
```

Then verify per `docs/operations.md` §6:

- `/dev/uinput` keeps the session-user ACL
- `/dev/uinput` gains `user:contextdeck-broker:rw-`
- `contextdeck-broker` can read and write `/dev/uinput` (`test -r` / `test -w`)
- G213 event/hidraw, `/dev/port`, and `/dev/i2c-*` policies remain unchanged
- input-remapper stays enabled/active and unmodified

Full install/rollback text is in `docs/operations.md` §6 (includes reinstalling 61 and the uinput trigger).

## Explicit non-claims

- Not G4 PASS/FAIL. Not logical-whole closure.
- Installed host udev still has the old `62-` RUN until the COOPERATOR reinstall above.
- Did not log key codes, key names, scan values, raw HID, serials, or typed text.

## Residual risks / smallest next step

Host still has the pre-fix `/etc/udev/rules.d/62-contextdeck-broker.rules`. After the COOPERATOR udev reinstall and verify, a **fresh independent** S5/G4 acceptance can run against `24305864f54d7161048041c2e5309aa8a0f8fb1a`. Worker 10 also reported a missing independent recovery path; that is outside this session.

Resolved Execution Issues / Near-Misses: none  
Pre-Existing Failure Classification: none (the live uinput ACL gap is the authorized bug; repository fix only)

Expected manual META archive (not written by this Worker):

- `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/11_implementation_00.md`
- `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/11_report_00.md`