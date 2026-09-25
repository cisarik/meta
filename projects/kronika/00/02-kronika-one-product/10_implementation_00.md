# Kronika one product — S3 bounded NUC capture host setup and deployment

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 10
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S3-HOST
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: bounded host mutation on the household NUC (service account, paths, token materialization, unit installation, release deployment) with a strict no-secret and no-login boundary; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Session declaration

This must be a genuinely fresh session launched from an environment where the
three `FRAMENEST_NUC_SSH_*` names are present (the Cooperator has placed them in
`~/.zshenv`; values are never printed). This grant performs the accepted S3 host
setup and deployment, then stops before any login. The Cooperator performs the
interactive login through the view in a separate later step. No independence
claim.

## Step 0 — preconditions

Check only names, never values:

```text
test -n "$FRAMENEST_NUC_SSH_TARGET" && echo TARGET-set || echo TARGET-unset
test -n "$FRAMENEST_NUC_SSH_USER" && echo USER-set || echo USER-unset
test -n "$FRAMENEST_NUC_SSH_IDENTITY" && echo IDENTITY-set || echo IDENTITY-unset
```

If any is unset, stop `BLOCKED` immediately (names only). Then:

- `scripts/operator/network/framenest_nuc_worker_gate.fish --probe` prints
  `ssh-agent: ready`.
- Remote `sudo -n true` through the gate exits 0. The Cooperator established
  the timestamp outside this Worker; you use `sudo -n` only, never `sudo -v`,
  never a password.
- Repository gate: `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `c975aba14840b97944aecc655907e3abc370341d`, clean index and worktree; local
  `main` = `origin/main` = that commit; public
  `git ls-remote https://github.com/cisarik/framenest.git refs/heads/main`
  equals that commit; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- Quick state recheck (read-only): `kronika-capture` account absent; capture
  paths absent; ports 8765/5900/6080 free; `/opt/framenest/current` at
  `26d28b16…`.

## Goal

Create the accepted capture host state, deploy the accepted release, install
and enable the capture units, activate capture, and verify the running state.
Stop before login. The Cooperator then opens the view, logs in interactively,
and a later step performs the explicit resume and one synthetic ask.

## Required sequence (ordered; fail closed)

All remote commands go through
`scripts/operator/network/framenest_nuc_worker_gate.fish --command '<command>'`
and must contain no shell metacharacters. Never print a token or file
contents.

1. **Account and paths.**

```text
id -u kronika-capture
sudo -n useradd --system --user-group --home /var/lib/kronika-capture --shell /usr/sbin/nologin --no-create-home kronika-capture
sudo -n install -d -m 0700 -o kronika-capture -g kronika-capture /var/lib/kronika-capture
sudo -n install -d -m 0750 -o root -g kronika-capture /etc/kronika-capture
sudo -n install -d -m 0700 -o root -g root /etc/kronika-capture/credentials
```

2. **Token materialization.** One random value, never printed. The root
   credential is the systemd source; a matching 0600 capture-owned state
   token keeps the CLI and legacy fallback functional (both consumers must
   hold the same value).

```text
sudo -n openssl rand -out /etc/kronika-capture/credentials/kronika-bridge-token -base64 32
sudo -n chmod 0600 /etc/kronika-capture/credentials/kronika-bridge-token
sudo -n chown root:root /etc/kronika-capture/credentials/kronika-bridge-token
sudo -n install -m 0600 -o kronika-capture -g kronika-capture /etc/kronika-capture/credentials/kronika-bridge-token /var/lib/kronika-capture/token
```

   Verify only metadata: `sudo -n ls -l` on both paths. If `openssl` is
   unavailable, stop and report instead of improvising a generator.

3. **Deploy the accepted release** from the repository root (helper transport
   uses the exported variables; no gate):

```text
./deploy/ubuntu/framenest-release check --release c975aba14840b97944aecc655907e3abc370341d
./deploy/ubuntu/framenest-release deploy --release c975aba14840b97944aecc655907e3abc370341d --yes
```

   `check` must show `public_main` equal to the release and the expected
   manifest; `deploy` must complete with the accepted SHA. Verify
   `readlink /opt/framenest/current` and `systemctl is-active framenest.service`.

4. **Install capture sources from the deployed release.**

```text
sudo -n install -m 0644 /opt/framenest/current/deploy/systemd/kronika-capture-xvfb.service /etc/systemd/system/kronika-capture-xvfb.service
sudo -n install -m 0644 /opt/framenest/current/deploy/systemd/kronika-capture-bridge.service /etc/systemd/system/kronika-capture-bridge.service
sudo -n install -m 0644 /opt/framenest/current/deploy/systemd/kronika-capture-runner.service /etc/systemd/system/kronika-capture-runner.service
sudo -n install -m 0644 /opt/framenest/current/deploy/systemd/kronika-capture-vnc.service /etc/systemd/system/kronika-capture-vnc.service
sudo -n install -m 0644 /opt/framenest/current/deploy/systemd/kronika-capture-view.service /etc/systemd/system/kronika-capture-view.service
sudo -n install -m 0644 /opt/framenest/current/deploy/systemd/kronika-capture.env.example /etc/kronika-capture/capture.env
sudo -n systemctl daemon-reload
sudo -n systemctl enable kronika-capture-xvfb.service kronika-capture-bridge.service kronika-capture-runner.service
```

   Confirm VNC and view are installed but not enabled. Do not modify
   `framenest.service` and do not install any drop-in for it.

5. **Start display and bridge, then activate capture.**

```text
sudo -n systemctl start kronika-capture-xvfb.service
sudo -n systemctl start kronika-capture-bridge.service
./deploy/ubuntu/framenest-release activate-capture --release c975aba14840b97944aecc655907e3abc370341d --yes
```

   Expected first-run outcomes: exit 0 with readiness ready, or exit 16 after
   exactly one runner restart when the fresh profile needs the operator login
   (`needs_admin`). Report the exact code and both printed SHAs. A failed
   browser launch must not cause a second restart; do not retry activation.

6. **Verify (read-only).**

```text
sudo -n systemctl is-active kronika-capture-xvfb.service
sudo -n systemctl is-active kronika-capture-bridge.service
sudo -n systemctl is-active kronika-capture-runner.service
pgrep -c -x chrome
pgrep -c -x Xvfb
ss -ltn 'sport = :8765'
ss -ltn 'sport = :5900'
ss -ltn 'sport = :6080'
readlink /opt/framenest/capture-current
sudo -n ls -ld /var/lib/kronika-capture /var/lib/kronika-capture/token /etc/kronika-capture/credentials/kronika-bridge-token
sudo -n -u kronika-capture -- /opt/framenest/capture-current/.venv/bin/kronika-capture bridge status --state-dir /var/lib/kronika-capture
```

   Expect one Chromium (`chrome`) process, one Xvfb, loopback-only ports,
   `capture-current` at the accepted release, 0700/0600 modes, and a status
   JSON whose readiness is either `ready` or `needs_admin`. Do not start the
   view units, do not log in, do not resume, do not send an ask.

7. **Privilege release.** Remote `sudo -K` through the gate, then confirm
   `sudo -n true` fails with a password-required message. Leave all view units
   stopped.

## Authority and containment

Positive authority: the ordered commands above through the worker gate; the
three read-only release-helper operations `check`, `deploy`, and
`activate-capture`; read-only verification commands; and the terminal report
write. Host effect class: bounded reversible host mutation (new service
account, new directories, one token value, five unit files, one config file,
release deployment and capture activation). No other host effect.

Negative authority: no login, no view start, no resume, no ask, no browser
profile content read, no cookie/token/credential printing, no
`framenest.service` change or drop-in, no database reset or migration, no
change to the accepted release or repository, no push, no other host service
change, no dependency/config change, no `sudo -v`, no `private/**`, no
subagents. Do not print hostnames, private network values, tokens or sockets.

## Stopping conditions

Stop and report on: an unset Step 0 name; a failed gate or privilege probe; any
unexpected pre-existing host state; a release-helper gate failure or an
unexpected deploy result; a missing capture source in the release tree; an
`activate-capture` result other than the two expected outcomes; more than one
Chromium process; a non-loopback listener; or any instruction conflict.
Preserve the first causal failure. Do not improvise host commands, do not
lower any boundary, and do not retry a failed browser launch.

## Completion and report contract

`PASS` means the account, paths, token materialization, release deployment,
unit installation/enabling, Xvfb and bridge start, and capture activation all
completed within this grant, and the verification above is reported with exact
values. Use `PARTIAL` when the setup completed but a verification could not be
observed, and `BLOCKED` when it did not complete safely. No login, resume or
ask was performed; the Cooperator login step follows.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the Step 0
result (names only); the exact command sequence and observed results,
including `check`/`deploy`/`activate-capture` exit codes and both printed
SHAs; account/path/token metadata (never contents); unit enablement states;
service states; process and port observations; the readiness JSON summary; the
terminal `sudo -K` evidence; deviations/risks/missing evidence; one smallest
next step (Cooperator login through the view); `Report justification:
new-mutation`; authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

Direct communication with the Cooperator (the short completion notice) is in
Slovak, masculine address for him. This prompt and the formal report are in
English. Do not use subagents. Do not commit Meta artifacts.

Finalize the report, save it at the exact destination, read it back in full,
and verify its first line, coordinates, content and path before the short
separate completion notice with status, exact report path and SHA-256. Terminal
report or cancellation expires this authority.

## Trace and delivery record

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 10_implementation_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 10_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
