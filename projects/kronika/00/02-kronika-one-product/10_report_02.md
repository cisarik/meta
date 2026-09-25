### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 10
Worker exchange ordinal: 03
Persistent role identity: WORKER
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded NUC Deployment
Phase: deployment
Task identity: KRONIKA-ONE-PRODUCT-S3-HOST-RETRY
status: BLOCKED
Phase-qualified result: capture activation did not reach ready or needs_admin
Start commit: 94e605c17b881461fad3e22fd8c7fca32cb93976
End commit: 94e605c17b881461fad3e22fd8c7fca32cb93976
Report justification: new-mutation
Logical-whole closure: not-closed

Continuity anchor matched exchange 02: terminal PASS report `10_report_01.md`, HEAD `94e605c17b881461fad3e22fd8c7fca32cb93976`. That exchange's authority had expired. No repository edit, commit, or push.

## Step 0

Names only: TARGET-set, USER-set, IDENTITY-set.
Probe printed `ssh-agent: ready` and exited 0. Remote `sudo -n true` exited 0.
Branch `feat/kronika-one-product` was clean. Local `main`, `origin/main`, and public `refs/heads/main` were `94e605c17b881461fad3e22fd8c7fca32cb93976`. AP pin was `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`. The worktree was clean at the same HEAD after the host work.

## Deploy and unit install

`check --release 94e605c17b881461fad3e22fd8c7fca32cb93976` exited 0. `public_main` equalled that release. `capture_bridge_protocol` was `1`. `current_release` was still `/opt/framenest/releases/c975aba14840b97944aecc655907e3abc370341d`. `backup_restore_readiness` was `ready`. `capture_unit_contract_sha256` was `c2f31eac9c042e23ac9beebb8af648baaf16ef94e6f5106924591110cb88abaa`.

`deploy --release 94e605c17b881461fad3e22fd8c7fca32cb93976 --yes` exited 0. Printed `framenest-release deploy complete: 94e605c17b881461fad3e22fd8c7fca32cb93976`, `web_release` that SHA, and `capture_release: c975aba14840b97944aecc655907e3abc370341d`.

The five unit installs and the `capture.env` install each exited 0. `daemon-reload` exited 0. `enable` of xvfb, bridge, and runner exited 0 and created the three `multi-user.target.wants` symlinks. `framenest.service` was not modified.

Installed `ExecStart` text:

```text
ExecStart=/opt/framenest/capture-current/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture bridge run --port 8765
ExecStart=/opt/framenest/capture-current/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture runner run --profile /var/lib/kronika-capture/profile --port 8765 --headed
ExecStart=/usr/bin/Xvfb :99 -screen 0 1280x800x24 -nolisten tcp -nolock -auth /run/kronika-capture/Xauthority
```

## Start and activation

`systemctl start kronika-capture-xvfb.service` exited 0. Immediate `is-active` was `active` (exit 0) and `pgrep -c -x Xvfb` was 1. A second read-only check about two seconds later was still `active` with one process. `systemctl start kronika-capture-bridge.service` exited 0 and `is-active` was `active`.

`activate-capture --release 94e605c17b881461fad3e22fd8c7fca32cb93976 --yes` exited 16. Stderr: `capture readiness failed without another browser launch (capture readiness failed)`. Printed SHAs: `web_release: 94e605c17b881461fad3e22fd8c7fca32cb93976` and `capture_release: 94e605c17b881461fad3e22fd8c7fca32cb93976`. Activation was not repeated. No second explicit Xvfb start was issued.

## Verification

- Runner `is-active`: `active` (exit 0). `NRestarts=0`, `Result=success`.
- Xvfb `is-active`: `failed` (exit 3). `NRestarts=0`, `Result=exit-code`, `ExecMainStatus=1`. `pgrep -c -x Xvfb` was 0.
- Bridge `is-active`: `active` (exit 0).
- `pgrep -c -x chrome`: 0 (exit 1).
- Port 8765: one loopback-only listener. Ports 5900 and 6080: no listeners. No non-loopback listener was observed.
- `readlink` of `/opt/framenest/capture-current` and `/opt/framenest/current`: both `/opt/framenest/releases/94e605c17b881461fad3e22fd8c7fca32cb93976`.
- Status command exited 0. Summary: `ok` true, `readiness` `browser_unavailable`, `reason` `E_BROWSER_UNAVAILABLE`, `api_version` 1, `proto` 1, `client_connected` true, jobs active 0 and total 0. Not `ready` and not `needs_admin`.

This-session Xvfb journal, hostname withheld. One explicit start at `2026-09-25T09:59:51Z` logged `Warning: the -nolock option can only be used by root`, stayed up, then at `2026-09-25T10:00:03Z` logged `(EE) Could not create lock file in /tmp/.tX99-lock` and exited 1. A second start at `2026-09-25T10:00:23Z`, not issued as another `systemctl start` from this session, logged the same root-only warning and the same lock error at `2026-09-25T10:00:35Z`. `NRestarts` stayed 0.

`sudo -K` exited 0. A following `sudo -n true` exited 1 with a password-required result.

## Why this is blocked

Exit 16 is an expected code only for readiness `ready` was not this result, and the fresh-profile `needs_admin` outcome was not this result. The status JSON is `browser_unavailable`. Chromium count is 0. The installed Xvfb accepts `-nolock` on the command line and then refuses it for the unprivileged service user, so it still tries to create `/tmp/.tX99-lock` and exits 1. The early `active` observation was inside the roughly twelve seconds before that exit. No login, view start, resume, or ask was performed.

Changed files: none in the repository. Host effects that remain: web and capture pointers at the corrected SHA, five reinstalled units and `capture.env`, the three units enabled, bridge and runner active, Xvfb failed. Account, directories, and token files were not removed or read.

Validation: the ordered host commands and the three release-helper operations were run. No product test suite was run.

Git result: no fetch, stage, commit, or push.

Deviations: after the stop condition, read-only `systemctl show` and `journalctl` recorded the Xvfb cause. One extra `is-active` and `pgrep` about two seconds after the first Xvfb check saw the process still up; that was before the lock error.
Risks: bridge and runner were left active after Xvfb had failed. `-nolock` does not remove the lock requirement for this user.
Missing evidence: the systemd job id of the second Xvfb start.
Smallest next step: correct the unprivileged Xvfb lock failure in a new grant. Do not open the view, log in, resume, or ask against `browser_unavailable`.

Orchestration critique:
MEASURED: the corrected Xvfb unit passes `-nolock`, the process logs that the option can only be used by root, then exits 1 because `/tmp/.tX99-lock` cannot be created; status readiness is `browser_unavailable` with `E_BROWSER_UNAVAILABLE`; smallest correction is a lock approach that works for the `kronika-capture` user, which is the prompt's `/tmp` `ReadWritePaths` fallback, before any login.
LEAD: the second Xvfb start at `2026-09-25T10:00:23Z` was pulled in by the runner `Requires=` during the single `activate-capture`; cheapest check is the systemd job record for that start.
Resolved Execution Issues / Near-Misses: the two-second stay check reported Xvfb `active` with one process, and that same start then exited about twelve seconds after `Started` with the lock error; no second explicit start and no activation retry followed.
Pre-existing Failure Classification: none
Authority expiry: this terminal report ends the grant; no autonomous continuation.
