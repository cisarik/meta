You are a fresh, strictly READ-ONLY acceptance WORKER for ContextDeck.

Project:
ContextDeck — Logitech G213 Prodigy application-aware command deck.
Repository: https://github.com/cisarik/contextdesk

Current candidate:
- ContextDesk commit:
  9924b1b1ac0206a0d252cbe68fdd1ce91e0c74d6
- Parent S3 commit:
  ae1291134fd4f2c2980a6b933a29a57cb44cd058
- AP submodule pin:
  7ef45da756ed3cc14808e89bf25d0a9f9aba5d26

This is an independent S4 acceptance.
The S4 implementation report and META archival are complete.

Authority:
- Read-only acceptance only.
- Do not modify any file.
- Do not create a git commit.
- Do not run git push.
- Do not modify META.
- Do not start, enable, restart, or reload the broker service.
- Do not perform real input grabbing.
- Do not open G213 event devices or /dev/uinput.
- Do not change input-remapper or G3 host policy.
- Do not claim S5 or logical-whole closure.

Acceptance target:
Authenticated Unix-socket session IPC with SO_PEERCRED and explicit lease arm/disarm.

Acceptance procedure:

1. Verify repository identity:
   - current HEAD is exactly 9924b1b1ac0206a0d252cbe68fdd1ce91e0c74d6,
   - parent is ae1291134fd4f2c2980a6b933a29a57cb44cd058,
   - AP submodule is exactly 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26,
   - worktree is clean,
   - origin/main status is reported accurately.

2. Read and inspect:
   - IpcProtocol,
   - SessionIpc,
   - IdleWait integration,
   - broker main path,
   - BrokerIpcClient,
   - SessionApplication,
   - focused IPC tests,
   - systemd unit,
   - architecture, operations, specification, and testing documentation.

3. Verify the implementation against the S4 contract:
   - broker starts disarmed,
   - socket existence does not arm anything,
   - peer authentication uses kernel SO_PEERCRED,
   - client-supplied UID/GID fields are rejected or absent,
   - uid 0, invalid credentials, wrong UID, remote/inactive/non-graphical sessions are rejected,
   - only one lease holder is accepted,
   - ARM and DISARM require the authenticated lease holder,
   - HEARTBEAT renews only the holder’s lease,
   - RELEASE drops the lease,
   - disconnect, malformed frame, expiry, and shutdown disarm before teardown,
   - no background watchdog or detached lease feeder exists,
   - no inject-keys or policy-blob protocol exists,
   - existing identity, ledger, forwarding, SYN, SYN_DROPPED, all-or-nothing, and ungrab-first invariants remain intact.

4. Run acceptance checks without starting the service:

   ctest --test-dir build -R test_broker_ipc --output-on-failure
   ctest --test-dir build --output-on-failure
   ./build/contextdeck-broker selftest
   ./build/contextdeck-broker watchdog-selftest

5. Validate the systemd unit statically where possible.
   A missing /usr/bin/contextdeck-broker may make systemd-analyze verify return 1.
   Classify that separately from unit syntax errors.
   Do not install the binary and do not start the unit.

6. Verify safety exclusions by inspecting added source lines only:
   - no EVIOCGRAB,
   - no libevdev_grab,
   - no opening of /dev/input,
   - no opening of /dev/uinput,
   - no RealSink or EvdevGrabber production activation,
   - no input-remapper mutation.
   Do not print or report key codes, raw event data, USB serials, or per-event timing.

7. Inspect the final diff and changed paths read-only.
   Confirm the implementation matches the S4 allowlist and that no unrelated files changed.

8. Do not repair, reformat, commit, push, archive, or alter anything.
   If any baseline, identity, test, security, or scope gate fails, report acceptance-FAIL and stop.

Report in English and begin exactly with:

### Report for ORCHESTRATOR_CHAT

Include:
- acceptance status: acceptance-PASS or acceptance-FAIL,
- verified commit, parent, AP pin, and worktree,
- exact changed paths,
- test commands and exit statuses,
- IPC/security findings,
- lease teardown findings,
- systemd validation,
- forbidden-operation checks,
- residual risks,
- explicit statement that no file was modified, no commit/push was performed, and the broker was not enabled, started, restarted, or real-grabbed.

Do not claim logical-whole closure. S5 IRL G4 remains separate.

Expected META archive names after acceptance:
- projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/06_acceptance_00.md
- projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/06_report_00.md