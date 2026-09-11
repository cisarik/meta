Fresh Independent Acceptance Worker — S5 IRL G4

Logical whole:
g213-contextdeck-input-passthrough-safety

Worker session ordinal:
09

Worker exchange ordinal:
00

Worker session target:
fresh-worker-session

Native planning mode:
not-used

Profile:
Fresh Independent Acceptance — S5 IRL G4

You are read-only acceptance only.

Do not modify repository files.
Do not commit.
Do not push.
Do not modify META.
Do not enable the broker.
Do not add autostart.
Do not modify input-remapper, udev, sysusers, or the installed policy.
Do not print or store key codes, key names, scan values, raw HID data, USB serials, window captions, or ordinary typed keystrokes.

Repository:
 /home/agile/Projects/contextdesk

Candidate:
9924b1b1ac0206a0d252cbe68fdd1ce91e0c74d6

Required AP pin:
7ef45da756ed3cc14808e89bf25d0a9f9aba5d26

Acceptance owner map:
- docs/operations.md
- docs/testing-m2.md
- docs/architecture.md
- installed systemd unit
- installed G3 udev/sysusers policy

This is the first real S5/G4 acceptance attempt after the previous attempt was BLOCKED because:
- /usr/bin/contextdeck-broker was missing;
- installed RuntimeDirectoryMode was 0750 instead of 0755;
- production ARM was still fail-closed;
- no independent physical recovery path had been demonstrated.

Revalidate all preconditions before starting anything:

1. Repository identity, clean worktree, candidate commit, AP pin.
2. /usr/bin/contextdeck-broker exists and is executable.
3. Installed unit is byte-identical to:
   packaging/systemd/contextdeck-broker.service
4. systemd-analyze verify passes.
5. Unit is Type=notify, WatchdogSec=2, Restart=no, NotifyAccess=main, LimitCORE=0, RuntimeDirectoryMode=0755, and has no [Install] section.
6. contextdeck-broker is static and inactive before the test.
7. G3 ACL policy still passes:
   - G213 event nodes identified by USB ancestry 046d:c336 and interface number;
   - event nodes owned by group contextdeck-broker, mode 0660, no session-user ACL;
   - hidraw nodes retain the session-user ACL;
   - /dev/port and /dev/i2c-* have no session-user ACL;
   - session user is not in group input.
8. input-remapper remains enabled and active, with its G213 configuration untouched.
9. An independent recovery path is actually available and tested:
   - preferably a second physical keyboard;
   - otherwise an independently reachable SSH session from another device.
   Do not assume that tty1–tty6 can be reached through the grabbed G213.

If any precondition fails, report BLOCKED and stop. Do not start or arm the broker.

If all preconditions pass, execute the documented S5/G4 procedure from docs/operations.md only.

Required G4 areas:

A. Controlled startup and lease arming
- Start the broker manually through systemd only for this acceptance.
- Confirm it starts disarmed and does not grab before an explicit authenticated lease/ARM action.
- Use the documented session application/tray path for STATUS, LEASE, and explicit ARM.
- Do not use an improvised socket client or undocumented command sequence.
- Confirm the broker becomes armed only after explicit ARM.
- Confirm no automatic arm occurs on service start or session-app startup.

B. Real G213 pass-through fidelity
- With the real G213 grabbed, verify ordinary keyboard operation through the documented pass-through path.
- Check that forwarded events are neither duplicated nor missing.
- Check that press/release pairing and SYN behavior remain correct.
- Do not record key identities or raw event payloads.
- If OpenRGB is available, verify hidraw lighting access without starting unrelated services or changing its configuration.

C. SIGTERM recovery
- While the broker is genuinely armed, send the documented controlled SIGTERM path.
- Verify ungrab occurs and the G213 remains usable.
- Verify no stuck modifier state, duplicate events, or phantom input.
- Verify the broker does not automatically restart or re-grab.
- Use the independent recovery path if needed.

D. SIGKILL/crash recovery
- While genuinely armed, terminate the broker using the documented crash/SIGKILL procedure.
- Verify the kernel closes the event fds and the G213 becomes usable.
- Verify no stuck modifiers, duplicate events, or phantom input.
- Verify systemd Restart=no is respected and no re-grab occurs.

E. Watchdog/hang recovery
- Follow the documented production hang harness from the repository.
- Do not invent an unsafe hang method.
- Verify the watchdog detects a broker that stops feeding from its event loop.
- Verify the broker dies/reaches the documented failed state and does not re-grab.
- Verify the G213 is usable afterward.
- Record only state transitions, service state, and recovery result—not keyboard payloads or timing traces.

F. input-remapper coexistence
- Leave input-remapper enabled and active throughout.
- Do not stop, disable, reconfigure, or rewrite it.
- Verify the documented coexistence behavior while the broker is armed and after recovery.
- Verify its G213 preset/configuration is unchanged.

G. Uninstall and restoration
- Perform only the documented uninstall/rollback procedure.
- Confirm the broker unit is not enabled and is inactive before removal.
- Verify G3 ACL restoration exactly as documented.
- Verify hidraw access and input-remapper state after restoration.
- Do not claim restoration if any ACL or service state is uncertain.

At the end:
- Stop the broker and leave it disabled/static and inactive.
- Do not leave it armed.
- Do not leave input-remapper changed.
- Do not leave the G213 grabbed.
- Report exact exit/status results and PASS, FAIL, or BLOCKED for each area.
- Acceptance PASS is allowed only if all required areas pass.
- If any safety gate fails, stop immediately and report BLOCKED or FAIL as appropriate.
- This session must not claim logical-whole closure.

Use this report format:

Report for ORCHESTRATOR_CHAT

- logical-whole identity
- Worker-session ordinal
- Worker-exchange ordinal
- Worker session target
- Native planning mode
- acceptance status: PASS / FAIL / BLOCKED
- phase-qualified result: S5/G4 acceptance only
- logical-whole closure: not-closed unless explicitly authorized elsewhere
- candidate commit and AP pin
- precondition results
- G4 areas A–G with exact results
- final broker enabled/active state
- final ACL and input-remapper state
- residual risks
- explicit non-claims
- exact commands and exit statuses
- confirmation that no repository files, commits, pushes, or META files were changed

Expected META filenames, archived manually by the COOPERATOR only after the Worker report exists:

projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/09_acceptance_00.md
projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/09_report_00.md