You are a fresh implementation WORKER for the ContextDeck project.

Project:
ContextDeck — Logitech G213 Prodigy application-aware command deck.
Repository: https://github.com/cisarik/contextdesk

Current verified candidate:
- ContextDesk:
  9924b1b1ac0206a0d252cbe68fdd1ce91e0c74d6
- AP pin:
  7ef45da756ed3cc14808e89bf25d0a9f9aba5d26

S4 has acceptance-PASS.
S5 IRL G4 acceptance was attempted by a fresh independent Worker and correctly returned BLOCKED before starting or arming the broker.

Implement only the bounded S5 production-prerequisite slice.

Required work:

1. Production G213 input path
- Implement the production enumerator for the Logitech G213 USB device 046d:c336.
- Resolve devices by USB ancestry and interface identity, never by remembered eventN numbers.
- Use only the already accepted G213 interfaces and control catalog.
- Keep firmware-only Game Mode and Backlight outside the remap catalog.
- Implement and wire the production EvdevGrabber/RealSink path.
- Preserve all existing invariants:
  - identity matcher,
  - balanced acquisition ledger,
  - 1:1 forwarding,
  - SYN pairing,
  - SYN_DROPPED reconciliation,
  - all-or-nothing acquisition,
  - ungrab-first teardown,
  - crash-safe cleanup.
- Production startup must remain disarmed.
- Socket existence, session-app startup, or STATUS must never arm or grab.
- ARM must occur only after authenticated S4 lease ownership and an explicit arm request.

2. Explicit session-app ARM path
- Add a documented, deliberate session-app/user action that performs the existing authenticated LEASE + ARM flow.
- Do not auto-arm from SessionApplication::start().
- Do not arm merely because the broker is available.
- Keep DISARM and RELEASE explicit.
- Preserve fail-closed behavior for authentication, disconnect, malformed protocol, lease expiry, shutdown, and all teardown paths.

3. Installable production artifact
- Add the minimal CMake install rule required to install contextdeck-broker to /usr/bin/contextdeck-broker when using the documented /usr prefix.
- Do not invent a second install prefix.
- Update only the necessary packaging and operations documentation.
- Refresh the systemd unit in-tree so it contains the required RuntimeDirectoryMode=0755.
- Ensure the service remains Type=notify, WatchdogSec=2, Restart=no, and has no [Install] section.
- Do not add autostart.

4. Production hang harness documentation
- Add a safe, explicit, documented production hang test procedure.
- Prefer an external signal-based procedure such as controlled SIGSTOP/watchdog observation if that is sufficient.
- Do not add an always-available hidden production hang command.
- Document recovery and the final secure-state checks.
- Do not log raw input data or timing.

5. Tests
- Add or update device-free tests for enumerator filtering and production-path construction.
- Test that startup is disarmed.
- Test that explicit authenticated ARM is required.
- Test that no device is opened before ARM.
- Test fail-closed behavior for missing/invalid devices.
- Test ungrab-first and cleanup behavior.
- Keep existing IPC, watchdog, identity, ledger, forwarding, and acquisition tests green.
- Do not open the real G213 or /dev/uinput during implementation tests.

Host prerequisite operation:
After implementation, build and validate the project. If the repository documentation defines the exact host installation procedure, use it to install the built binary and refreshed unit so that:
- /usr/bin/contextdeck-broker exists and is executable,
- the installed unit matches the repository unit,
- RuntimeDirectoryMode is 0755,
- daemon-reload is performed only if required.

Do not enable, start, restart, arm, or real-grab the broker in this implementation session.
Leave the broker static and inactive.
Do not change G3 udev/sysusers policy or input-remapper.

Strict exclusions:
- Do not perform S5 IRL G4.
- Do not test real pass-through.
- Do not test SIGTERM/SIGKILL/hang on a live grabbed keyboard.
- Do not uninstall G3 policy.
- Do not leave the host with the OpenRGB uaccess hole reopened.
- Do not modify AP, .ap, AGENTS.md, ROADMAP.md, META, or handout history unless the existing project rules explicitly require a narrowly scoped documentation update; never modify META.
- Do not log key codes, key names, scan values, raw event payloads, USB serials, or per-event timing.
- Do not use GUI tools or AppImages.

Workflow:
1. Verify current HEAD, AP pin, clean state, and the S4 baseline.
2. Read AP rules, AGENTS.md, architecture, operations, testing, specification, hardware matrix, and zone map.
3. State the minimal implementation allowlist before edits.
4. Implement only this bounded slice.
5. Run focused and full tests with exact exit statuses.
6. Validate the binary and unit statically.
7. Verify the broker remains static/inactive and was never started or armed.
8. Review changed paths and diff.
9. You may create one focused ContextDesk commit and push it to the normal ContextDesk remote.
10. Do not commit, push, or modify META. META archival is performed manually by the COOPERATOR.

Stop and report BLOCKED if:
- production wiring cannot be implemented without guessing,
- the enumerator cannot safely identify the G213,
- explicit ARM cannot be connected to the authenticated lease,
- tests require real hardware,
- G3 security would be weakened,
- input-remapper would need modification,
- the binary/unit cannot be made consistent without starting the broker,
- a safety invariant is lost.

Report in English and begin exactly with:

### Report for ORCHESTRATOR_CHAT

Include:
- implementation status,
- starting and ending commits,
- exact changed paths,
- implementation allowlist,
- production enumerator design,
- RealSink/EvdevGrabber design,
- explicit ARM path,
- install procedure and resulting binary/unit state,
- hang harness documentation,
- focused/full test commands and exit statuses,
- proof that no real grab occurred,
- proof that the broker was not enabled or started,
- residual risks,
- whether a fresh independent G4 acceptance is now authorized.

Expected META archive names:
- projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/08_implementation_00.md
- projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/08_report_00.md