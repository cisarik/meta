### Report for ORCHESTRATOR_CHAT

- **logical-whole identity:** `g213-contextdeck-input-passthrough-safety`
- **Worker-session ordinal:** `10`
- **Worker-exchange ordinal:** `00`
- **Worker session target:** `fresh-worker-session`
- **Native planning mode:** `not-used`
- **Worker session profile:** Fresh Independent Acceptance — S5 IRL G4
- **status:** **BLOCKED**
- **phase-qualified result:** not-applicable
- **start commit / end commit:** `899df8fc14a2ad67594ff432f1b00d9ab155fd79` / `899df8fc14a2ad67594ff432f1b00d9ab155fd79` (unchanged)
- **changed files:** none
- **authorized Git result:** none (no commit, no push)
- **Report justification:** `new-evidence`
- **Logical-whole closure:** not-closed
- **Authority:** expires at this terminal report

```text
Acceptance candidate: 899df8fc14a2ad67594ff432f1b00d9ab155fd79
Acceptance owner map: docs/operations.md G3+S5/G4, docs/testing-m2.md Production hang harness
Acceptance allowlist: host G4 procedure only after all preconditions; no repository/META mutation
Acceptance risk claims: grab, crash, hang, recovery, coexistence, uninstall
Acceptance control matrix: start-disarmed; explicit authenticated session-app LEASE/ARM; no autostart; ungrab-on-death; input-remapper unchanged; G3 ACLs
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: independent recovery path (second physical keyboard usable, or SSH from another device independently tested)
Out-of-scope observations: installed /dev/uinput has session ACL and no contextdeck-broker named-user ACL (udev RUN from 62-contextdeck-broker.rules not visible on the node)
```

This Worker did **not** start, enable, arm, or grab the broker. Areas A–G were not executed.

```text
Consecutive terminal PARTIAL/BLOCKED reports for the same materially unchanged blocker: 2
Exact blocker: independent recovery path not demonstrated (no second physical keyboard; SSH from another device not tested)
Smallest authority expansion needed: COOPERATOR attaches a dedicated second physical keyboard and shows it types, or independently tests SSH from another device, then reissue a fresh G4 acceptance against the same candidate
Direct closure path: identify-missing-evidence
Consequence of no action: G4 cannot start without violating the grab-recovery rule
Closure decision required: identify-missing-evidence
```

Worker 09 already stopped on this recovery-path gap (alongside a wrong named candidate). This retry verified the required candidate `899df8f`; the recovery-path blocker is unchanged.

## Preconditions

| # | Check | Result |
|---|---|---|
| 1 | HEAD equals required candidate; clean worktree; AP pin | **PASS** — HEAD `899df8fc14a2ad67594ff432f1b00d9ab155fd79` (`head_match_exit=0`); `git status --porcelain=v1` empty; `.ap` gitlink and submodule HEAD `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`; `main...origin/main` `0 0` (no fetch). Subject: `Add production G213 enumerator, explicit ARM, and broker install.` |
| 2 | `/usr/bin/contextdeck-broker` executable and matches build artifact | **PASS** — `test -x` exit 0; `cmp` vs `build/contextdeck-broker` exit 0; SHA-256 `1003f28b0ad9180b433bebe18defb8b177b0ae4d3716ecc03a419379a870957a` both; `nm` shows `ProductionArmControl`, `UdevDeviceEnumerator`, `RealSink::create`, `EvdevGrabber::create`. |
| 3 | Installed unit byte-identical to repository | **PASS** — `diff` exit 0; no drop-ins (`dropin_dir_exit=2`). |
| 4 | `systemd-analyze verify` | **PASS** — installed exit 0; repo exit 0. |
| 5 | `RuntimeDirectoryMode=0755`, `Type=notify`, `WatchdogSec=2`, `Restart=no`, `NotifyAccess=main`, `LimitCORE=0`, no `[Install]` | **PASS** on unit file / loaded definition. File has Type/WatchdogSec/Restart/LimitCORE/RuntimeDirectoryMode. `NotifyAccess` is not a file key; `systemctl show` → `main` (Type=notify default). `^\[Install\]` grep exit 1 (comment only). Inactive `WatchdogUSec=infinity` as on a never-started unit; not treated as a file mismatch. |
| 6 | Broker static and inactive | **PASS** — `is-enabled` `static` (exit 0); `is-active` `inactive` (exit 3); `ActiveState=inactive` `SubState=dead`; `WantedBy`/`RequiredBy` empty; `/run/contextdeck` absent; no broker PID. |
| 7 | G3 ACL policy; hidraw session ACL; `/dev/port` and `/dev/i2c-*` | **PASS** — see below. Installed udev 61/62 and sysusers byte-identical to repo (`diff` 0). Session user not in `input` or `contextdeck-broker`. |
| 8 | input-remapper enabled, active, unchanged | **PASS** — enabled+active. `config.json` SHA-256 `26c06218a1f68319…`; G213 preset SHA-256 empty blob `e3b0c44298fc1c14…`. Not rewritten. |
| 9 | Second physical keyboard usable, **or** SSH from another device independently tested | **FAIL** — see recovery path. |

**Stop rule applied:** any precondition failure → BLOCKED; do not start or arm.

### G3 ACL (no node numbers, no serials)

G213 resolved by USB ancestry `046d:c336` plus interface number:

- Two event nodes, interfaces `00` and `01`: owner `root`, group `contextdeck-broker`, mode `0660`, **no** session-user ACL, not readable by the session user.
- Two hidraw nodes, interfaces `00` and `01`: session-user ACL **present** (`rw-`). Lighting was not exercised (OpenRGB not listening on `:6742`).
- `/dev/port`: no session-user ACL; not session-readable.
- `/dev/i2c-*`: 8 nodes, **0** session-user ACL, **0** session-readable.

### Recovery path (the abort)

- Dedicated second physical keyboard: **absent**.
- One extra `ID_INPUT_KEYBOARD=1` USB node is the **2.4G mouse dongle** (`1ea7:0066`): same USB parent has mouse + keyboard collections; product family is mouse/2.4G, not a keyboard. Session cannot read that event node. This is not an independent recovery keyboard.
- Remaining `ID_INPUT_KEYBOARD=1` non-G213 node is **virtual** (input-remapper).
- No i8042/platform keyboard (`kb_phys_other=0`).
- `sshd` is enabled+active; **0** established SSH peers (loopback or remote). Local `loginctl`: one active Wayland seat (`remote=no`) plus a manager session. This session is not SSH.
- SSH from another device was **not** tested. Loopback SSH is not “another device” and was not used.
- An already-open Worker/Cursor shell is **not** accepted as the required recovery path (same rule as Worker 09). `tty1`–`tty6` nodes exist; they must not be assumed reachable from a grabbed G213.
- `sudo -n true` exit 1 (password required). No privileged mutation was attempted.

## G4 areas A–G

| Area | Result |
|---|---|
| A Controlled startup and authenticated LEASE/ARM via session/tray | **BLOCKED** (not executed) |
| B Real G213 pass-through fidelity | **BLOCKED** (not executed) |
| C SIGTERM recovery and ungrab | **BLOCKED** (not executed) |
| D SIGKILL/crash recovery and ungrab | **BLOCKED** (not executed) |
| E Production watchdog/hang harness | **BLOCKED** (not executed) |
| F Coexistence with enabled, unchanged input-remapper | **BLOCKED** (pre-state only; no grab) |
| G Documented uninstall/rollback and G3 restore | **BLOCKED** (not executed) |

Acceptance-PASS is **not** claimed.

## Final host state

- Broker: **static**, **inactive**, **not enabled**, **not armed**, **not grabbed**
- `/run/contextdeck`: absent
- G3 udev/sysusers/unit/binary: untouched
- input-remapper: enabled, active; hashes unchanged
- Repository: clean; no commits; no pushes
- META: not written by this Worker (`10_acceptance_00.md` was already an untracked placeholder and was left as found)

## Residual risks / missing evidence

- G4 still requires a **tested** non-G213 recovery path before any ARM/grab.
- Inactive `WatchdogUSec=infinity` must be re-checked after a documented systemd start.
- Session app exists only as `build/contextdeck` (`/usr/bin/contextdeck` absent). Area A still requires that documented tray/Diagnostics path, not a socket client.
- `/dev/uinput` currently shows a session named-user ACL and **no** `contextdeck-broker` named-user ACL. Documented G3 verify table still passes; production `RealSink` would likely fail closed until the udev `setfacl` RUN is actually present on the node. Not used as the abort (recovery path already failed).

## Explicit non-claims

- Not G4 PASS/FAIL (procedure never started).
- Not logical-whole closure.
- Not a claim that production ARM works on hardware.
- Did not start OpenRGB, did not change input-remapper, udev, sysusers, or the installed unit.
- Did not log key identities, scan values, raw HID, USB serials, window captions, typed text, or per-event timing.

## Exact commands and exit statuses

```text
git rev-parse HEAD
  → 899df8fc14a2ad67594ff432f1b00d9ab155fd79  (exit 0, match required)
git status --porcelain=v1
  → empty (exit 0)
git rev-parse HEAD:.ap  and  git -C .ap rev-parse HEAD
  → 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26 (exit 0)
git rev-list --left-right --count origin/main...HEAD
  → 0 0

test -x /usr/bin/contextdeck-broker
  → usr_exec_exit=0
cmp -s build/contextdeck-broker /usr/bin/contextdeck-broker
  → cmp_build_usr_exit=0
test -x /usr/bin/contextdeck
  → usr_session_exec_exit=1
test -x build/contextdeck
  → build_session_exec_exit=0

diff packaging/systemd/contextdeck-broker.service /etc/systemd/system/contextdeck-broker.service
  → unit_diff_exit=0
systemd-analyze verify /etc/systemd/system/contextdeck-broker.service
  → verify_installed_exit=0
systemd-analyze verify packaging/systemd/contextdeck-broker.service
  → verify_repo_exit=0
grep ^\[Install\] installed+repo unit
  → install_section_grep_exit=1
systemctl show … NotifyAccess
  → main
systemctl show … WatchdogUSec
  → infinity (inactive)

systemctl is-enabled contextdeck-broker.service
  → static  (enabled_exit=0)
systemctl is-active contextdeck-broker.service
  → inactive  (active_exit=3)
test -d /run/contextdeck
  → rundir_exists_exit=1

diff udev 61 / 62 / sysusers vs repo
  → udev61_diff=0  udev62_diff=0  sysusers_diff=0
g213_event_policy_pass=True
g213_hidraw_session_acl_pass=True
port_policy_pass=True
i2c_policy_pass=True (i2c_count=8 session_acl=0 readable_session=0)

systemctl is-enabled input-remapper.service
  → enabled  (exit 0)
systemctl is-active input-remapper.service
  → active  (exit 0)

systemctl is-active sshd.service
  → active
ssh_peer_loopback=0  ssh_peer_remote=0
second_physical_keyboard=False  (mouse-dongle keyboard collection only)
sudo -n true
  → sudo_n_exit=1

# Not run: systemctl start/stop/enable, session-app ARM, LEASE/ARM clients,
# kill, SIGSTOP hang harness, OpenRGB start, uninstall/rollback, any grab.