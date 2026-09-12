### Report for ORCHESTRATOR_CHAT

```text
Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 20
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Implementation Worker — suspend/resume safe lifecycle
Phase: implementation
Task identity: CONTEXTDESK-9A89095-SUSPEND-RESUME-LIFECYCLE
Delivery: manual
```

- **status:** **PASS**
- **phase-qualified result:** **implementation-PASS**
- **Report justification:** `changed-external-state`
- **Logical-whole closure:** not-closed
- **Start commit:** `9a89095d97bde1cdb8ec989f06f83fcc780b8280`
- **End commit:** `ab10491c49d0b6574b6953a02935a4664c39d7c2`
- **Runtime baseline (unchanged broker binary source):** `cb72ae0388307b514182efc6936712e3da42cda4`
- **AP pin:** `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`
- **Evidence tier:** E2
- **Evidence tier basis:** repository implementation, deterministic tests, packaging inspection, and public readback; no live suspend in this task
- **Independence required:** required-fresh-independent (this session implemented; it cannot self-certify live suspend acceptance)
- **Primary fresh implementations used:** 1
- **Automatic corrections used:** 0
- **Correction re-acceptance:** not-applicable
- **Authority:** expires at this terminal report

This session received the complete Worker prompt as the initial user message. Worker 19 authority was already expired. No subagents. Delivery: manual. Speak-to-Cooperator language is Slovak; this report is English.

## Model / client / reasoning (requested vs observed)

| Fact | Classification |
|------|----------------|
| Requested model | Cooperator choice |
| Observed client/model label | Cursor Grok 4.6 (session communication identity; not independently attested by a provider API dump) |
| Requested reasoning | High |
| Observed reasoning mode | unknown |
| Requested context | approximately 128k tokens |
| Observed context capacity | unknown |
| Delivery | manual |
| Subagents / Task dispatch | none |

## Repository and AP gate

Canonical product checkout `/home/agile/Projects/contextdesk`, remote `https://github.com/cisarik/contextdesk.git`, branch `main`. Authorized `git fetch origin main` left starting `HEAD` = `origin/main` = `9a89095d97bde1cdb8ec989f06f83fcc780b8280`. Product worktree clean (ignored `build/` only). No Git locks or active operations. `.ap` gitlink and checkout `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`. `./.ap/ap doctor`: PASS before mutation and after the product commit.

META destination `/home/agile/meta/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/` is a real directory, not a symlink; parents are real directories. `20_report_00.md` was absent before this write. `20_implementation_00.md` was already present (Cooperator-owned). Local META `HEAD` at start was `1bf6a913e21c309d78eff8d742f19be678731d8f` (contains Worker 19 prompt/report). META Git was not fetched, added, committed, or pushed.

No `src/` production change. Broker/session C++ behavior is unchanged; the sleep hook is a packaging executable and tests compile `BrokerIpcClient.cpp` only into `test_broker_ipc_client`.

## Design choice and rationale

Preferred mechanism, implemented: a narrowly scoped **systemd system-sleep hook** (`packaging/systemd/contextdeck-sleep.sh`, installed as `/usr/lib/systemd/system-sleep/contextdeck-broker`). ADR: `docs/adr/0001-broker-suspend-resume-sleep-hook.md`.

Rationale: `WatchdogSec=2` cannot be fed while the process is frozen. Stopping an **active** unit on `pre` releases an armed grab via the existing SIGTERM teardown (ungrab-first) and prevents a false watchdog abort. An ephemeral root-owned marker under `/run/contextdeck-sleep` (not `RuntimeDirectory=contextdeck`, which is removed on stop) records the single fact “this unit was active immediately before this sleep”. `post` consumes at most one valid marker and starts the exact unit once only if the unit is `inactive`. Start is the existing disarmed path: no `LEASE`, no `ARM`, no event-node/uinput open. Failed stop removes the marker (no post-start). Failed start is logged and not retried. Reboot clears `/run`. The broker binary still does not call `systemctl`, a shell, or sleep D-Bus APIs. `Restart=no`, absent `[Install]`, `Type=notify`, and `WatchdogSec=2` are unchanged.

Test seam: argv `--testdir DIR` only (never environment). Production systemd-sleep does not pass that flag. Tests use a fake `systemctl` confined to the temporary directory.

Transparent automatic re-ARM after resume remains out of scope.

## Marker / state-machine invariants (implemented)

- Modes handled: `suspend`, `hibernate`, `hybrid-sleep`, `suspend-then-hibernate`. Other modes log `class=skip reason=not-sleep-mode` and do not touch the unit.
- `pre` + `ActiveState=active`: atomic marker write (tmp + rename), mode `0600`, directory `0700`, payload `CONTEXTDECK_SLEEP_V1` plus current boot id; then `systemctl stop -- contextdeck-broker.service`; keep the marker only if the unit is then `inactive`.
- `pre` + not active: no new marker; keep a *valid* marker (duplicate `pre`); remove malformed/symlink/wrong-mode/wrong-boot-id markers.
- Concurrent change after the first `show`: consume marker, `class=skip reason=concurrent-change`, no stop.
- `post`: consume first; start once only if marker was valid and `ActiveState=inactive`; otherwise skip/error and never retry.
- Logs are bounded `class=skip|stop|start|error` plus a reason token. No hostnames, serials, paths, or user environment.

## Changed paths and purpose

```text
CMakeLists.txt
README.md
ROADMAP.md
docs/adr/0001-broker-suspend-resume-sleep-hook.md
docs/adr/README.md
docs/architecture.md
docs/operations.md
docs/testing-m2.md
packaging/systemd/contextdeck-broker.service
packaging/systemd/contextdeck-sleep.sh
tests/unit/test_broker_ipc_client.cpp
tests/unit/test_sleep_hook.sh
```

```text
 12 files changed, 1121 insertions(+), 65 deletions(-)
 create mode 100755 packaging/systemd/contextdeck-sleep.sh
 create mode 100755 tests/unit/test_sleep_hook.sh
```

Purpose: smallest safe suspend/resume lifecycle recovery for the broker and session client; install the hook with component `broker`; document that post-resume restart is conditional, always disarmed, and not automatic re-ARM; mark live host suspend acceptance still open.

## Tests and deterministic suspend simulation

Full registered CTest suite: **15/15 passed** (`ctest --test-dir build --output-on-failure`, clean `PATH`). No test opened G213 event or uinput nodes. No host `systemctl`, no write to `/run` outside the fake testdir, no `systemctl suspend`.

`test_sleep_hook` (fake `systemctl`, `sh -n` / `bash -n` on the hook, unit pins preserved):

1. non-sleep modes (`reboot`, `freeze`, `kexec`, `halt`, `poweroff`, empty) are no-ops and never call `systemctl`;
2. inactive / failed / activating / deactivating produce no marker and no start;
3. active unarmed: marker mode `600`, dir mode `700`, stop, one disarmed start, marker consumed;
4. active armed: same stop path; fake armed/lease bits cleared on stop; post-start armed=0 lease=0; no `LEASE`/`ARM` in `systemctl` argv;
5. failed pre-stop (exit 1, and stop leaving `failed`) never starts;
6. post-start failure is one attempt, marker consumed, duplicate `post` does not retry;
7. duplicate `pre` keeps a valid marker; duplicate `post` starts once; malformed / stale boot-id / concurrent change / reboot-like absence fail closed;
8. mode `0666` and symlink markers rejected; `--testdir /run` refused;
9. `BrokerIpcClient` covered by `test_broker_ipc_client`;
10. existing suite still passes.

`test_broker_ipc_client`: connect sends only `STATUS`; explicit `arm()` sends `LEASE` then `ARM`; after simulated broker loss, reconnect sends only `STATUS` (no `LEASE`/`ARM`); `requestStatus()` never arms.

This is **not** live suspend evidence.

## Privilege / host-mutation statement

No packages installed. No writes to `/etc`, `/usr`, `/run` (except fake testdirs under `/tmp`). No udev/ACL/input-remapper/OpenRGB/KWin changes. No session-app launch, no broker start, no ARM, no event/uinput open, no suspend/hibernate, no sudo. `cmake --install` was not run. Autostart remains forbidden.

## Git publication

```text
Local commit: ab10491c49d0b6574b6953a02935a4664c39d7c2
Parent:       9a89095d97bde1cdb8ec989f06f83fcc780b8280
Subject:      Stop the input broker before system sleep and restart it disarmed.
Push:         git push origin main → 9a89095..ab10491  main -> main (rc=0)
Readback:     git fetch origin main; HEAD = origin/main = FETCH_HEAD
              = git ls-remote origin refs/heads/main
              = ab10491c49d0b6574b6953a02935a4664c39d7c2
Public URL:   https://github.com/cisarik/contextdesk/commit/ab10491c49d0b6574b6953a02935a4664c39d7c2
META Git:     not modified
```

## Remaining live suspend evidence

Host suspend/resume acceptance is still open G4. This tree change does not prove: device re-enumeration after resume, LED return, all-control fidelity, production/autostart, or that an installed hook on a live seat stops an armed broker before freeze. Logical whole remains not-closed.

## Smallest next step

Issue a separately authorized fresh independent acceptance for **live host suspend/resume** of an installed hook (second keyboard or SSH first; active-before-sleep stop; disarmed post-start; no auto-ARM), or for another remaining G4 remainder (LED return / all-control). Do not treat `ab10491` as live suspend evidence, full G4, or autostart.

## Orchestration critique

```text
Orchestration critique:
MEASURED: public main is ab10491 with a systemd-sleep hook, fake-systemctl tests, and BrokerIpcClient reconnect/no-auto-ARM coverage; CTest 15/15; origin/main readback matches. Evidence: ls-remote ab10491; test_sleep_hook and test_broker_ipc_client PASS. Effect: smallest safe suspend recovery is in the tree without live power mutation. Smallest correction: none for this slice.
LEAD: live suspend still unproven. Cheapest later check: one authorized G4 host sleep with the installed hook and an already-verified recovery path.
```

## Near-miss / pre-existing

```text
Resolved Execution Issues / Near-Misses: (1) dangling symlink markers were treated as absent because test -e follows; hook now treats -L as present and rejects. (2) first client-test mock used QHash of QLocalSocket* / deleteLater and aborted in teardown; mock reduced to one QPointer client and disconnects before destroy. (3) poisoned CMAKE_ROOT; configure/build used env -i PATH as in operations.md.
Pre-Existing Failure Classification: AGENTS.md still lists watchdog/hang and held-modifier as remaining M2 work (Worker 19 already accepted those named slices); not in this allowlist. G213 event uaccess TAG residue with session ACL absent remains a non-blocking ledger-candidate from earlier G3 work.
```

```text
Prompt filename: 20_implementation_00.md
Report filename: 20_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: this WORKER
Git publication owner: COOPERATOR for META; this WORKER published the allowlisted product commit
Archival: wait-for-report
```

Authority for this Worker expires at this report.
