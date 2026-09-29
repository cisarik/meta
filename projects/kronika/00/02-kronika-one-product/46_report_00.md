### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 46
Worker exchange ordinal: 01
Persistent role identity: ORCHESTRATOR (autonomous execution under the Cooperator's 2026-09-28 directive; the intended fresh Worker session was not used)
Phase: deployment
Task identity: KRONIKA-ONE-PRODUCT-NUC-RELEASE-89A4029
status: PASS
Phase-qualified result: deployment-PASS (non-independent, autonomy mode)
Result artifact or commit: web release 89a402981a9eac83646199c77984c3fc21c0744d; capture release 94e605c17b881461fad3e22fd8c7fca32cb93976; host unit source 3f5dc5c469e19802aa3411988aa022b158de2ab6
Result evidence: helper status/check/cutover exit 0; pointer, `.framenest-release-sha`, schema 0034, active service, read-only as-left capture
Logical-whole closure: not-closed
Start commit: 89a402981a9eac83646199c77984c3fc21c0744d
End commit: 3f5dc5c469e19802aa3411988aa022b158de2ab6 (host unit fix committed and published after the release deployment)
Report justification: new-mutation

## What happened

1. `check --release 89a4029…` passed (`public_main` equal, `capture_bridge_protocol` 1).
2. The first `deploy --yes` stopped with exit 20 (`transport`) after it had
   already built and atomically published `/opt/framenest/releases/89a4029…`.
   The failing remote step was the same-schema DB gate:
   `framenest-db status` on the target tree failed with
   `FRAMENEST_DB_COMMAND_FAILED`.
3. Root cause: the accepted S6 private-catalog rule requires the database
   parent directory to be exactly `0700`, while the NUC's
   `/var/lib/framenest` was `0755`. The pre-S6 release tolerated that; the S6
   code fails closed.
4. Attempting `chmod 700` alone was not durable: the unit declared
   `StateDirectory=framenest` with systemd's default mode, so every service
   (re)start reset the directory to `0755`. A cutover attempt failed at
   pre-restart readiness, and the restart loop of the previous release against
   the now-`0034` database left `framenest.service` in `activating/auto-restart`
   until it was stopped.
5. Fixes:
   - Repository unit source `deploy/systemd/framenest.service` gained
     `StateDirectoryMode=0700` (commit
     `3f5dc5c469e19802aa3411988aa022b158de2ab6`, with a contract assertion in
     `tests/contract/test_fedora_systemd_service.py`; targeted tests green).
   - The updated unit was installed on the NUC and the installed file hashes
     byte-identical to the repository source; `daemon-reload` executed.
   - The state directory was set to `0700` by the operator; systemd now
     enforces the same mode at every start.
6. Documented schema-jump continuation: lock artifacts removed; migration run
   from the target tree (`framenest-db migrate` -> `0034 at_head`); cutover via
   `framenest-release rollback --release 89a4029… --yes` -> exit 0.
7. The host unit fix was published: public `main` fast-forwarded
   `89a4029… -> 3f5dc5c…` (non-force, readback verified).

## Final observed state (sanitized)

```text
active_release / web_release: 89a402981a9eac83646199c77984c3fc21c0744d
capture_release: 94e605c17b881461fad3e22fd8c7fca32cb93976 (unchanged)
release_path: /opt/framenest/releases/89a402981a9eac83646199c77984c3fc21c0744d
service_active: active
database_revision: 0034
backup_restore_readiness: ready
/opt/framenest/current -> /opt/framenest/releases/89a4029…
/var/lib/framenest mode: 700, owner framenest
capture runner/xvfb/bridge: active, Result=success, NRestarts=0
capture readiness: browser_unavailable / E_BROWSER_UNAVAILABLE; jobs 0/0; active_job null; client_connected true; zero chrome/chromium processes
tailscaled: active
public main: 3f5dc5c469e19802aa3411988aa022b158de2ab6
```

## Deviations, risks, missing evidence

- Two host mutations beyond the original route text were required by the
  accepted S6 policy and are recorded here: the state-directory mode change and
  the unit source install. Both are tightening changes owned by the service
  account; the unit was hash-verified against the repository source.
- The service was briefly down while the schema was ahead of the running
  release, until the cutover completed. It is active now.
- The NUC release tree is `89a4029…`; the host unit and public `main` are at
  `3f5dc5c…`. The next routine update will align the release tree; no function
  is missing because the unit is host-managed.
- Listener classification was not re-run to avoid printing addresses; the
  bridge port and view ports were not opened. `ss` evidence is therefore
  absent, not failing.
- Sudo timestamp: used read-only/needed steps only; the Cooperator releases it
  manually (`sudo -K`) per the standing directive.
- Non-independent execution (autonomy mode); no fresh acceptance was required
  for this routine update, and the next slice should carry the usual flow where
  the Cooperator wants it.

## Smallest next step

Continue the roadmap: S4-B native provider runtime (acceptance plan exists in
`25_report_00.md`), then S7-P -> S8 -> S9 -> S10. Before S4-B implementation,
the trace should note whether the Cooperator wants restored independent
acceptance for product-affecting slices; the deployment/unit fixes in this
window were executed autonomously and are recorded as such.
