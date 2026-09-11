#! Fresh Independent Acceptance Worker — S5 IRL G4 retry

Logical whole:
g213-contextdeck-input-passthrough-safety

Worker session ordinal:
10

Worker exchange ordinal:
00

Worker session target:
fresh-worker-session

Native planning mode:
not-used

Profile:
Fresh Independent Acceptance — S5 IRL G4

Read-only acceptance only:
- Do not modify repository, META, input-remapper, udev, sysusers, or systemd policy.
- Do not commit or push.
- Do not enable the broker or add autostart.
- Do not log key codes, key names, scan values, raw HID data, USB serials, window captions, typed text, or per-event timing.
- Do not use an undocumented socket client or improvised ARM path.

Repository:
 /home/agile/Projects/contextdesk

Required candidate:
899df8fc14a2ad67594ff432f1b00d9ab155fd79

Required AP pin:
7ef45da756ed3cc14808e89bf25d0a9f9aba5d26

The previous Worker 09 acceptance was BLOCKED before G4 because it named the wrong candidate and because no independent recovery path had been demonstrated. This retry must verify the actual candidate above before any service start.

Before starting or arming anything, verify:

- HEAD equals exactly the required candidate;
- worktree is clean;
- AP pin matches;
- /usr/bin/contextdeck-broker is executable and matches the build artifact;
- installed systemd unit matches the repository byte-for-byte;
- systemd-analyze verify passes;
- RuntimeDirectoryMode=0755, Type=notify, WatchdogSec=2, Restart=no, NotifyAccess=main, LimitCORE=0, and no [Install] section;
- broker is static and inactive;
- G3 ACL policy still passes;
- hidraw retains the session-user ACL;
- /dev/port and /dev/i2c-* have no session-user ACL;
- input-remapper remains enabled and active and is unchanged;
- a second physical keyboard is connected and usable, or SSH from another device has been independently tested.

If any precondition fails, report BLOCKED and stop. Do not start the broker.

If all preconditions pass, follow the documented S5/G4 procedure in docs/operations.md and execute areas A–G:

A. Controlled startup and explicit authenticated LEASE/ARM through the documented session/tray path. Confirm startup is disarmed and no auto-arm occurs.

B. Real G213 pass-through fidelity, without recording key identities or raw events.

C. SIGTERM recovery and ungrab.

D. SIGKILL/crash recovery and ungrab.

E. Production watchdog/hang recovery using only the documented harness.

F. Coexistence with enabled, unchanged input-remapper.

G. Documented uninstall/rollback and restoration of G3 policy.

Use the documented session application path; do not substitute an ad-hoc IPC client. Recheck systemd watchdog properties after the service is actually started.

After testing:

- leave broker static, inactive, disabled, unarmed, and ungrabbed;
- leave input-remapper enabled and unchanged;
- report exact exit/status results;
- classify every area as PASS, FAIL, or BLOCKED;
- claim acceptance-PASS only if all required areas pass;
- do not claim logical-whole closure;
- confirm no repository, META, commit, or push changes.

Expected report files for manual archiving:

projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/10_acceptance_00.md
projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/10_report_00.md