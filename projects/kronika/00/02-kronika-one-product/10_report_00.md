### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 10
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S3-HOST
status: BLOCKED
Phase-qualified result: capture activation did not reach ready or needs_admin
Start commit: c975aba14840b97944aecc655907e3abc370341d
End commit: c975aba14840b97944aecc655907e3abc370341d
Report justification: new-mutation
Logical-whole closure: not-closed

The account, paths, token materialization, release deployment, and unit installation completed. Xvfb and the bridge did not stay up. `activate-capture` exited 16 because the runner entered `failed`, which is the readiness gate's `failed` branch, not the expected fresh-profile `needs_admin` outcome. No login, view start, resume, or ask was performed. The browser was not launched again.

## Step 0

Names only: TARGET-set, USER-set, IDENTITY-set.
`framenest_nuc_worker_gate.fish --probe` printed `ssh-agent: ready` and exited 0.
Remote `sudo -n true` exited 0.

Repository `/home/agile/Projects/framenest`, branch `feat/kronika-one-product`:
HEAD, local `main`, `origin/main`, and public `refs/heads/main` were all `c975aba14840b97944aecc655907e3abc370341d`. Index and worktree were clean. AP pin was `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`. The same HEAD and a clean worktree were observed again after the host work. No commit and no push.

Pre-state, read-only: `id -u kronika-capture` exited 1 (`no such user`). `test -e` exited 1 for `/var/lib/kronika-capture`, `/run/kronika-capture`, `/etc/kronika-capture`, `/etc/kronika-capture/credentials`, `/opt/framenest/capture-current`, the five capture unit paths, and `/etc/kronika-capture/capture.env`. Ports 8765, 5900, and 6080 had no listeners. `readlink /opt/framenest/current` was `/opt/framenest/releases/26d28b16c08a5e7e0179a32c16646bfdc1009c81`.

## Command results

Account and paths, through the gate:

- `id -u kronika-capture` before create: exit 1, user absent.
- `useradd` as specified: exit 0. A later `id -u kronika-capture` printed uid 996 and exited 0.
- `install -d` for `/var/lib/kronika-capture` (0700, kronika-capture), `/etc/kronika-capture` (0750, root:kronika-capture), and `/etc/kronika-capture/credentials` (0700, root:root): each exit 0.

Token materialization, contents never read:

- `openssl rand -out ... -base64 32`: exit 0.
- `chmod 0600`, `chown root:root`, and `install` of the credential onto `/var/lib/kronika-capture/token`: each exit 0.
- `ls -l` metadata: credential `-rw------- 1 root root 45`; state token `-rw------- 1 kronika-capture kronika-capture 45`.

Release helper, from the repository root:

- `check --release c975aba14840b97944aecc655907e3abc370341d`: exit 0. `public_main` equalled that release. `ap_gitlink` `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`. `superproject_sha256` `ee96acfbe62194891d6b5819645345b2d8b299c35a682c1b397b43c643035d20`. `ap_archive_sha256` `f330aaf483c4e8eba7bd2bc32660965fae593e4c0cef792b20c882c86e66af23`. `current_release` was the previous `26d28b16c08a5e7e0179a32c16646bfdc1009c81` tree. `backup_restore_readiness` `ready`. `capture_code_tree` `977465503254fe6cdf31673b7e107b9e0487ffe2`. `capture_runtime_contract_sha256` `691500d51dc9a2f3966de144c3592b0b984e8b2753cca4d599aee3793ee35e6b`. `capture_unit_contract_sha256` `4d4566c13a23f6dd642931f7cd9a2e618726a5a8a84fcc097daf99b459b66759`. `capture_bridge_protocol` `1`.
- `deploy --release c975aba14840b97944aecc655907e3abc370341d --yes`: exit 0. Printed `framenest-release deploy complete: c975aba14840b97944aecc655907e3abc370341d`, `web_release` that same SHA, and `capture_release: absent`.
- After deploy, `readlink /opt/framenest/current` was `/opt/framenest/releases/c975aba14840b97944aecc655907e3abc370341d`. `systemctl is-active framenest.service` was `active` (exit 0). The same web unit was still `active` after privilege release. The six capture sources were present in that release tree (`test -f` exit 0).

Unit installation:

- Five `install -m 0644` unit copies and the `capture.env` install: each exit 0.
- `systemctl daemon-reload`: exit 0.
- `systemctl enable` of xvfb, bridge, and runner: exit 0, three `multi-user.target.wants` symlinks created.
- `is-enabled`: xvfb, bridge, and runner `enabled` (exit 0); vnc and view `static` (exit 0). They were not enabled.

Start and activation:

- `systemctl start kronika-capture-xvfb.service`: exit 0. An immediate `is-active` printed `active` (exit 0). That observation raced the process exit recorded below.
- `systemctl start kronika-capture-bridge.service`: exit 0. An immediate `is-active` printed `activating` (exit 3).
- `activate-capture --release c975aba14840b97944aecc655907e3abc370341d --yes`: exit 16. Stderr: `capture readiness failed without another browser launch (capture readiness failed)`. Printed SHAs: `web_release: c975aba14840b97944aecc655907e3abc370341d` and `capture_release: c975aba14840b97944aecc655907e3abc370341d`. Activation was not repeated.

## Verification

- xvfb `is-active`: `failed` (exit 3). `Result=exit-code`, `NRestarts=0`, `ExecMainStatus=1`, last exit `2026-09-25 09:09:56 UTC`.
- bridge `is-active`: `activating` (exit 3). `SubState=auto-restart`, `ExecMainStatus=2`. `NRestarts` was 29 at the first show and 51 after `sudo -K`. The loop was still running when this report was written.
- runner `is-active`: `failed` (exit 3). `Result=exit-code`, `NRestarts=0`, `ExecMainStatus=2`, exit `2026-09-25 09:09:45 UTC`.
- vnc and view `is-active`: `inactive` (exit 3). They were not started.
- `pgrep -c -x chrome`: 0 (exit 1). `pgrep -c -x Xvfb`: 0 (exit 1).
- Ports 8765, 5900, and 6080: no listeners. No non-loopback listener was observed.
- `readlink /opt/framenest/capture-current`: `/opt/framenest/releases/c975aba14840b97944aecc655907e3abc370341d`.
- `ls -ld` metadata: `/var/lib/kronika-capture` is `drwx------` (0700), owner `kronika-capture`, link count 4, contents not listed. Both token paths remained mode 0600 with the owners above.
- The granted status command exited 2. It printed `unrecognized arguments: --state-dir /var/lib/kronika-capture` and no JSON. Readiness was therefore not observed through that command.

Journal excerpts, secret-bearing lines withheld:

- Xvfb, two start cycles and `NRestarts=0`: `(EE) Could not create lock file in /tmp/.tX99-lock`, then `status=1/FAILURE`. The second cycle was not a second `systemctl start` from this session.
- Runner, one start: the same `unrecognized arguments: --state-dir /var/lib/kronika-capture`, then `status=2/INVALIDARGUMENT`.
- Bridge: the same argument error, `status=2/INVALIDARGUMENT`, and `Restart=on-failure` rescheduling. The parent parser accepts `--state-dir` only before the subcommand. Both unit `ExecStart` lines and the granted status command place it after `bridge run`, `runner run`, or `bridge status`.

`sudo -K` through the gate exited 0. A following `sudo -n true` exited 1 with a password-required result.

## Why this is blocked

Exit 16 is an expected code only when the fresh profile reaches `needs_admin` after exactly one runner restart. The runner's `ActiveState=failed` is the gate branch `readiness=failed`. Chromium count 0 agrees: no operator-login browser is waiting. Two verified defects in the accepted units produced that result. The Xvfb process cannot create its `/tmp` lock file. The bridge and runner exit 2 because `--state-dir` is not accepted after the subcommand. The bridge restart loop is still active. No second browser launch was attempted.

Changed files: no repository file changed. Host effects that remain: service account uid 996, the capture directories, one unread token value in the two 0600 files, five installed units, `capture.env`, the deployed release pointer, `capture-current` at the accepted SHA, enabled xvfb/bridge/runner units, and the bridge unit still auto-restarting. `framenest.service` was not modified. VNC and view are installed, static, and inactive.

Validation: the ordered host commands and the three release-helper operations were run as specified. No product test suite was run. Repository Git state was rechecked and remained clean at the accepted commit.

Git result: no fetch, stage, commit, or push.

Deviations: after the stop condition, read-only `systemctl show` and `journalctl` were used to preserve the cause. One extra `sudo -n test -s` on the credential file ran before `ls -l`; it did not print contents. The `/etc/kronika-capture` directory mode was not re-stated after the successful `install -d`.

Risk: `kronika-capture-bridge.service` continues to exit 2 and restart. At the last observation `NRestarts=51`, `ActiveState=activating`, `SubState=auto-restart`.

Missing evidence: bridge status JSON; a direct byte comparison of the two token files; the systemd job id that issued the second Xvfb start.

Smallest next step: stop `kronika-capture-bridge.service` so the restart loop ends, then correct the unit command lines and the Xvfb `/tmp` lock failure in a new grant. Do not open the view, log in, resume, or ask against this failed state.

Orchestration critique:
MEASURED: bridge and runner ExecStart, and the granted status command, place `--state-dir` after the subcommand; journal and the status command both show `unrecognized arguments` and exit 2; the runner stays `failed`, so `activate-capture` exit 16 is `readiness=failed`, and the bridge restart loop continues; smallest correction is to accept `--state-dir` before the subcommand and to make the Xvfb `/tmp` lock file creatable, then stop the looping bridge unit before any login.
LEAD: the second Xvfb start (journal shows two cycles, `NRestarts=0`) was pulled in by the runner `Requires=` during the single `activate-capture` restart; cheapest check is the systemd job record for that start.
Resolved Execution Issues / Near-Misses: the first path-absent probe reused a shell `$?` overwritten by command substitutions and falsely looked present; the probe was repeated with the exit code saved immediately, all listed paths were absent, and no host mutation had been started.
Pre-existing Failure Classification: none
Authority expiry: this terminal report ends the grant; no autonomous continuation.
