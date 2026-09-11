**Acceptance status: BLOCKED.** Broker som nespustil, nearmsoval a negraboval. G4 oblasti A–G sa nevykonali.

Dôvod zastavenia: pomenovaný kandidát `9924b1b` nie je HEAD. Na disku je `899df8f` (S5 production), čistý worktree, zhodný AP pin. Druhá klávesnica nie je; SSH z iného zariadenia som neoveril.

Nižšie je terminálny Worker report (anglicky) na ručné archivovanie. META som nearoval; `09_report_00.md` ostal prázdny placeholder.

---

### Report for ORCHESTRATOR_CHAT

- **logical-whole identity:** `g213-contextdeck-input-passthrough-safety`
- **Worker-session ordinal:** `09`
- **Worker-exchange ordinal:** `00`
- **Worker session target:** `fresh-worker-session`
- **Native planning mode:** `not-used`
- **acceptance status:** **BLOCKED**
- **phase-qualified result:** S5/G4 acceptance only — **not started** (preconditions failed)
- **logical-whole closure:** not-closed
- **candidate named in prompt:** `9924b1b1ac0206a0d252cbe68fdd1ce91e0c74d6`
- **actual HEAD:** `899df8fc14a2ad67594ff432f1b00d9ab155fd79`
- **AP pin required / actual:** `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` / `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` (match)
- **Independence:** established independently; no prior G4 authority inherited
- **Authority:** expires at this terminal report

This Worker did not start, enable, arm, or grab. No G4 procedure was executed.

## Precondition results

| # | Check | Result |
|---|---|---|
| 1 | Repository identity, clean worktree, **named candidate**, AP pin | **FAIL** — worktree clean on `main...origin/main`; AP pin matches; **HEAD is `899df8f`, not named candidate `9924b1b`**. `9924b1b` is the parent (`Add authenticated Unix-socket session IPC and broker lease.`). HEAD is `Add production G213 enumerator, explicit ARM, and broker install.` Installed `/usr/bin/contextdeck-broker` is byte-identical to `build/contextdeck-broker` and contains `ProductionArmControl` / `UdevDeviceEnumerator` (HEAD artifact, not `9924b1b`). |
| 2 | `/usr/bin/contextdeck-broker` exists and is executable | **PASS** — `-rwxr-xr-x`, root-owned, executable (`test -x` exit 0). SHA-256 matches the tree build. |
| 3 | Installed unit byte-identical to `packaging/systemd/contextdeck-broker.service` | **PASS** — `diff` exit 0. |
| 4 | `systemd-analyze verify` | **PASS** — installed unit exit 0; repo unit exit 0. |
| 5 | Unit `Type=notify`, `WatchdogSec=2`, `Restart=no`, `NotifyAccess=main`, `LimitCORE=0`, `RuntimeDirectoryMode=0755`, no `[Install]` | **PASS on unit file / loaded definition.** File has `WatchdogSec=2`, `Type=notify`, `Restart=no`, `NotifyAccess=main` (via `systemctl show`), `LimitCORE=0`, `RuntimeDirectoryMode=0755`. No `[Install]` section (only a comment). Note: inactive `systemctl show WatchdogUSec=infinity` / D-Bus `t 18446744073709551615` (never-started unit). This was **not** treated as a file mismatch. No drop-ins. |
| 6 | `contextdeck-broker` static and inactive before test | **PASS** — `systemctl is-enabled` → `static` (exit 0); `systemctl is-active` → `inactive` (exit 3); `ActiveState=inactive` `SubState=dead`; `UnitFileState=static`; `WantedBy=` empty; `/run/contextdeck` absent. |
| 7 | G3 ACL policy | **PASS** (see below). |
| 8 | input-remapper enabled/active, G213 configuration untouched | **PASS** — enabled + active/running. G213 preset file present and empty (SHA-256 of empty blob `e3b0c44298fc1c14…`); `config.json` SHA-256 `26c06218a1f68319…`. This Worker did not rewrite it. |
| 9 | Independent recovery path available **and tested** | **FAIL** — no second physical keyboard (only G213 + a 2.4G mouse / remapper virtual devices). `sshd` is **active** and listens on `:22`, but SSH from another device was **not** tested. Loopback `ssh -o BatchMode=yes -o StrictHostKeyChecking=yes localhost true` → exit **255** (host key unknown). tty1 is the graphical seat; this prompt forbids assuming tty1–tty6 via a grabbed G213. This already-open Worker shell was **not** accepted as a substitute for the required second keyboard or tested off-box SSH. |

**Stop rule applied:** any precondition failure → BLOCKED; do not start or arm.

### G3 ACL (no node numbers)

G213 event nodes resolved by USB ancestry `046d:c336` plus interface number (not remembered `eventN`):

- Two event nodes: interfaces `00` and `01`.
- Owner `root`, group `contextdeck-broker`, mode `0660`, **no** session-user ACL, no named-user ACLs.
- Two G213 hidraw nodes: session-user ACL **still present**; not claimed as lighting functional test (OpenRGB was not started).
- `/dev/port`: no session-user ACL; not readable by the session user.
- `/dev/i2c-*`: 8 nodes, **0** with session-user ACL, **0** readable by the session user.
- Session user **not** in group `input` (`id -nG` grep exit 1). Group `input` members observed: `brltty` only.
- Installed udev/sysusers files are byte-identical to the repository copies (`diff` exit 0). Not modified by this Worker.

### Why G4 did not start

Named candidate `9924b1b` is the S4 IPC commit. The host binary, unit (`RuntimeDirectoryMode=0755`), and production ARM symbols belong to HEAD `899df8f`. Accepting G4 against the named SHA would test the wrong artifact. Accepting HEAD under a prompt that names `9924b1b` would also be a false identity. Independent acceptance stops.

Recovery-path failure is an independent stop: arming a grab without a tested non-G213 recovery path is forbidden by this prompt.

## G4 areas A–G

| Area | Result |
|---|---|
| A Controlled startup and lease arming | **not executed** |
| B Real G213 pass-through fidelity | **not executed** |
| C SIGTERM recovery | **not executed** |
| D SIGKILL/crash recovery | **not executed** |
| E Watchdog/hang recovery | **not executed** |
| F input-remapper coexistence | **not executed** (pre-state observed only) |
| G Uninstall and restoration | **not executed** |

## Final host state (unchanged by this session)

- Broker: **static**, **inactive**, **not enabled**, **not armed**, **not grabbed**
- `/run/contextdeck`: absent
- G3 udev/sysusers/unit/binary: untouched
- input-remapper: enabled, active; G213 preset hash unchanged
- Repository: clean; no commits; no pushes
- META: not written by this Worker (`09_report_00.md` was already an empty untracked placeholder and was left empty)

## Residual risks

- Re-issuing G4 against `899df8f` still requires a **tested** second physical keyboard or SSH from another device **before** any ARM/grab.
- Inactive `WatchdogUSec=infinity` should be re-checked **after** a documented systemd start (unit file already has `WatchdogSec=2`).
- Session application is only at `build/contextdeck`; `/usr/bin/contextdeck` is absent. Area A requires the documented tray/Diagnostics path, not a socket client.

## Explicit non-claims

- Not G4 PASS/FAIL (procedure never started).
- Not logical-whole closure.
- Not host-install acceptance of `9924b1b` (that commit is not what is installed).
- Not a claim that production ARM works on hardware.
- Did not start OpenRGB, did not change input-remapper, udev, sysusers, or the installed unit.
- Did not log key identities, scan values, raw HID, USB serials, window captions, or typed text.

## Exact commands and exit statuses

```text
git rev-parse HEAD
  → 899df8fc14a2ad67594ff432f1b00d9ab155fd79  (exit 0)
git status --porcelain=v1
  → empty (exit 0)
git rev-parse HEAD:.ap  and  git -C .ap rev-parse HEAD
  → 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26 (exit 0)
git merge-base --is-ancestor 9924b1b1ac0206a0d252cbe68fdd1ce91e0c74d6 HEAD
  → ancestor_exit=0  (named SHA is parent, not HEAD)

test -x /usr/bin/contextdeck-broker
  → exec_exit=0
diff packaging/systemd/contextdeck-broker.service /etc/systemd/system/contextdeck-broker.service
  → diff_exit=0
cmp -s build/contextdeck-broker /usr/bin/contextdeck-broker
  → cmp_build_usr=0
systemd-analyze verify /etc/systemd/system/contextdeck-broker.service
  → verify_installed_exit=0
systemd-analyze verify packaging/systemd/contextdeck-broker.service
  → verify_repo_exit=0
systemctl is-enabled contextdeck-broker.service
  → static  (enabled_exit=0)
systemctl is-active contextdeck-broker.service
  → inactive  (active_exit=3)
systemctl is-failed contextdeck-broker.service
  → inactive  (failed_exit=1)
grep [Install] on installed+repo unit
  → comment only, install_grep_exit=0

systemctl show … WatchdogUSec
  → infinity (inactive)
busctl get-property … WatchdogUSec
  → t 18446744073709551615

systemctl is-enabled input-remapper.service
  → enabled  (exit 0)
systemctl is-active input-remapper.service
  → active  (exit 0)
id -nG | grep -x input
  → in_input_group_exit=1
systemctl is-active sshd
  → active
ssh -o BatchMode=yes -o ConnectTimeout=3 -o StrictHostKeyChecking=yes localhost true
  → ssh_localhost_exit=255

diff udev 61 / 62 / sysusers vs repo
  → 61_diff=0  62_diff=0  sysusers_diff=0

# Not run: systemctl start/stop/enable, ARM/LEASE clients, kill, SIGSTOP hang harness,
# OpenRGB start, uninstall/rollback, any grab.
```

Repository files, commits, pushes, and META files were **not** changed by this Worker.