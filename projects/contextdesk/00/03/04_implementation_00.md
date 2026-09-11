You are a fresh implementation WORKER for the ContextDeck project.

Project:
ContextDeck — Logitech G213 Prodigy application-aware command deck.
Repository: https://github.com/cisarik/contextdesk

Continuity anchors:
- ContextDesk verified commit: 69f433c382d7dffe6d8b8f1aea41ca7c6931a4f6
- AP submodule pin: 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26

The COOPERATOR has completed and verified G3 on the real CachyOS host:
- G213 event nodes no longer grant ACL access to the session user.
- /dev/port and /dev/i2c-* no longer grant ACL access to the session user.
- G213 hidraw access for OpenRGB remains intact.
- input-remapper is enabled and active.
- contextdeck-broker.service is static and inactive.
- The broker has never been enabled or started.

TASK: Implement S3 only.

S3 scope:
1. Add systemd watchdog integration for contextdeck-broker.
2. Configure a 2-second systemd watchdog.
3. Use sd_notify correctly, including READY=1 and WATCHDOG=1 as appropriate.
4. Feed WATCHDOG=1 from genuine progress of the real broker input event loop.
5. Ensure a hung or blocked input loop stops feeding the watchdog and is therefore detectable by systemd.
6. Add focused tests or a deterministic crash/hang harness where practical.
7. Document the crash, hang, watchdog, recovery, and TTY-recovery procedure without requiring real keyboard acceptance.

Important watchdog semantics:
- Do not implement a detached timer that continues feeding the watchdog while the input loop is hung.
- Watchdog notification must be tied to successful event-loop progress.
- Preserve the broker’s existing safety invariants:
  - identity matching,
  - balanced acquisition ledger,
  - 1:1 forwarding,
  - SYN pairing,
  - SYN_DROPPED reconciliation,
  - all-or-nothing acquisition,
  - ungrab-first teardown,
  - crash-safe release behavior.

Strict exclusions:
- Do not implement S4 Unix-socket IPC or SO_PEERCRED.
- Do not perform S5 real-keyboard acceptance.
- Do not start, enable, or exercise the broker systemd service on the host.
- Do not perform real input grabbing.
- Do not alter input-remapper.
- Do not alter the already-installed G3 host policy manually.
- Do not modify AP, .ap, AGENTS.md, META, handout history, or unrelated project areas.
- Do not log or document key codes, key names, scan values, raw event payloads, USB serials, or per-event timing.
- Do not use GUI tools, AppImages, or production access.

Workflow:
1. Verify repository identity, current HEAD, AP pin, clean state, and baseline.
2. Read the relevant AP files, AGENTS.md, broker implementation, existing tests, systemd unit, build files, and operations documentation.
3. State the minimal implementation allowlist before editing.
4. Implement only S3.
5. Add or update focused tests and documentation.
6. Run the relevant focused tests, then the full available test suite.
7. Run static systemd unit validation such as systemd-analyze verify where available.
8. Do not start or enable the service.
9. Review the final diff and staged paths explicitly.
10. Create one focused implementation commit only if all required gates pass.

Stop immediately if:
- the baseline gate fails,
- the repository or AP pin differs from the continuity anchors,
- implementation would require S4/S5 work,
- a safety invariant cannot be preserved,
- tests cannot demonstrate the watchdog behavior honestly.

Report in English and begin the terminal report exactly with:

### Report for ORCHESTRATOR_CHAT

Include:
- verified repository identity and anchors,
- baseline result,
- implementation summary,
- exact changed paths,
- watchdog/systemd design,
- tests and exact exit statuses,
- systemd validation result,
- commit hash,
- remaining risks,
- explicit statement that the broker was not enabled or started.

Do not claim acceptance-PASS or logical-whole closure. This is only the S3 implementation report.

Expected META archive names after the report exists:
- projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/04_implementation_00.md
- projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/04_report_00.md