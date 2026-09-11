You are a fresh implementation WORKER for ContextDeck.

Project:
ContextDeck — Logitech G213 Prodigy application-aware command deck.
Repository: https://github.com/cisarik/contextdesk

Continuity anchors:
- ContextDesk verified S3 commit:
  ae1291134fd4f2c2980a6b933a29a57cb44cd058
- Previous baseline:
  69f433c382d7dffe6d8b8f1aea41ca7c6931a4f6
- AP submodule pin:
  7ef45da756ed3cc14808e89bf25d0a9f9aba5d26

G3 host policy and S3 watchdog implementation are complete.
The S3 report was manually archived by the COOPERATOR.
This session is S4 only.

TASK: Implement S4 session-app IPC.

Required S4 scope:
1. Design and implement a local Unix-domain-socket IPC boundary between the session application and contextdeck-broker.
2. Authenticate the peer using SO_PEERCRED.
3. Implement an explicit authenticated lease for broker arm/disarm.
4. Ensure only the authorized session peer can acquire, renew, and release the lease.
5. Ensure disconnect, malformed protocol, failed authentication, lease expiry, and broker shutdown leave the broker disarmed and safe.
6. Connect lease arm/disarm to the existing broker control path without rewriting the existing input invariants.
7. Add focused tests using socketpair, temporary Unix sockets, fake grabber/sink, or other device-free mechanisms.
8. Document the IPC protocol, permissions, lifecycle, failure handling, and TTY recovery.

Security requirements:
- Broker must start disarmed.
- No implicit arming merely because the socket exists.
- No unauthenticated or group-only authorization.
- Do not trust client-supplied UID/GID values.
- Validate the kernel-provided SO_PEERCRED identity.
- Only one valid lease may control the broker.
- Release/ungrab must happen before teardown on every failure path.
- A dead, disconnected, hung, or malformed client must not leave the broker armed.
- Preserve identity matching, balanced ledger, 1:1 forwarding, SYN pairing, SYN_DROPPED reconciliation, all-or-nothing acquisition, and ungrab-first teardown.

Strict exclusions:
- Do not implement S5 real-keyboard acceptance.
- Do not perform real input grabbing on the host.
- Do not start or enable contextdeck-broker.service.
- Do not modify input-remapper.
- Do not modify G3 udev/sysusers policy.
- Do not alter the S3 watchdog design except where a direct IPC integration dependency is proven.
- Do not introduce keylogging.
- Do not log key codes, key names, scan values, raw event payloads, USB serials, or per-event timing.
- Do not modify AP, .ap, AGENTS.md, META, handout history, or unrelated project areas.
- Do not use GUI tools, AppImages, production access, or arbitrary host configuration changes.

Workflow:
1. Verify repository root, current HEAD, AP pin, clean worktree, and that HEAD is the S3 commit above.
2. Read the relevant AP files, AGENTS.md, architecture, operations documentation, broker/session code, systemd unit, and existing tests.
3. State the minimal implementation allowlist before editing.
4. Implement S4 only.
5. Add focused device-free tests for:
   - SO_PEERCRED acceptance/rejection,
   - lease acquisition,
   - duplicate lease rejection,
   - explicit arm/disarm,
   - disconnect cleanup,
   - malformed messages,
   - unauthorized commands,
   - broker shutdown cleanup,
   - no arming before authentication.
6. Run focused tests and the full CTest suite.
7. Validate the systemd unit statically where possible.
8. Do not install, enable, start, or exercise the broker service.
9. Review the final diff and staged paths explicitly.
10. Create one focused implementation commit only if all gates pass.

Stop immediately if:
- the current HEAD or AP pin differs,
- the baseline fails,
- S4 requires undocumented S5 behavior,
- a safety invariant cannot be preserved,
- authentication cannot be proven from kernel-provided credentials,
- tests would require opening the real G213 device.

Report in English and begin exactly with:

### Report for ORCHESTRATOR_CHAT

Include:
- repository identity and verified anchors,
- baseline result,
- implementation allowlist,
- exact changed paths,
- IPC protocol and SO_PEERCRED design,
- lease lifecycle and failure behavior,
- security properties,
- tests with exact exit statuses,
- systemd validation,
- commit hash,
- remaining risks,
- explicit statement that the broker was not enabled, started, or real-grabbed.

This is only an S4 implementation report.
Do not claim acceptance-PASS or logical-whole closure.

Expected META archive names:
- projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/05_implementation_00.md
- projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/05_report_00.md