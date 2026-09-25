# Kronika one product — S3 corrected capture host retry (lock fallback)

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 10
Worker exchange ordinal: 05
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded NUC Deployment
Phase: deployment
Task identity: KRONIKA-ONE-PRODUCT-S3-HOST-RETRY-2
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: redeploying the doubly corrected units and activating capture for the first time on the household NUC; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Current-session renewal

Continuity anchor: terminal PASS correction report `10_report_03.md` for task
`KRONIKA-ONE-PRODUCT-S3-XVFB-LOCK-CORRECTION`, Worker session 10, exchange 04,
ending at accepted commit `d63d0b725acedf49d1611224c3b5201a90e7ef90`.
Authority renewal: that exchange's authority expired at its terminal report.
This exchange grants complete new bounded deployment authority for the retry
only. Repository and environment re-gating is required before mutation.
Retained context is convenience only; on conflict with current evidence, stop
and report. Evidence posture: non-independent. New terminal report: required
(`10_report_04.md`).

## Starting state (verified at issuance)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `d63d0b725acedf49d1611224c3b5201a90e7ef90`; clean index and worktree; local
  `main` = `origin/main` = public `refs/heads/main` = that commit; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- Host state after the second correction: account uid 996, capture
  directories, two 0600 token files (untouched), five units installed and
  disabled, no chrome/Xvfb processes, no listeners on 8765/5900/6080, web
  release and `capture-current` still `94e605c`.
- `private/**` is never read. Never print or read the token value.

## Step 0 — preconditions

- The three `FRAMENEST_NUC_SSH_*` names are present (names only); otherwise
  stop `BLOCKED`.
- `scripts/operator/network/framenest_nuc_worker_gate.fish --probe` prints
  `ssh-agent: ready`; remote `sudo -n true` exits 0. Use `sudo -n` only, never
  `sudo -v`.

## Required sequence (ordered; fail closed)

All remote commands go through the worker gate and contain no shell
metacharacters. Never print a token or file contents.

1. **Deploy the doubly corrected release** from the repository root:

```text
./deploy/ubuntu/framenest-release check --release d63d0b725acedf49d1611224c3b5201a90e7ef90
./deploy/ubuntu/framenest-release deploy --release d63d0b725acedf49d1611224c3b5201a90e7ef90 --yes
```

   `check` must show `public_main` equal to the release and
   `capture_bridge_protocol` `1`; `deploy` must complete with the accepted SHA.

2. **Reinstall the corrected sources from the deployed release**, then reload
   and enable:

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

   Read-only checks: the installed Xvfb unit contains no `-nolock` and its
   `ReadWritePaths` includes `/tmp`; the bridge and runner units keep
   `--state-dir` before the subcommand. Do not modify `framenest.service`.

3. **Start and stability-check the display, then the bridge.**

```text
sudo -n systemctl start kronika-capture-xvfb.service
sudo -n systemctl is-active kronika-capture-xvfb.service
pgrep -c -x Xvfb
sleep 5
sudo -n systemctl is-active kronika-capture-xvfb.service
pgrep -c -x Xvfb
sudo -n systemctl start kronika-capture-bridge.service
sudo -n systemctl is-active kronika-capture-bridge.service
```

   Xvfb must remain `active` with exactly one process after the stability
   pause. If it fails again, stop and report the journal cause; do not start a
   second Xvfb.

4. **Activate capture.**

```text
./deploy/ubuntu/framenest-release activate-capture --release d63d0b725acedf49d1611224c3b5201a90e7ef90 --yes
```

   Expected: exit 0 with readiness `ready`, or exit 16 with `needs_admin`
   (fresh profile needs the operator login) after exactly one runner restart.
   Report the exact code and both SHAs. Do not retry activation.

5. **Verify (read-only).**

```text
sudo -n systemctl is-active kronika-capture-runner.service
pgrep -c -x chrome
ss -ltn 'sport = :8765'
ss -ltn 'sport = :5900'
ss -ltn 'sport = :6080'
readlink /opt/framenest/capture-current
readlink /opt/framenest/current
sudo -n -u kronika-capture -- /opt/framenest/capture-current/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture bridge status
```

   Expect one Chromium (`chrome`) process, loopback-only ports, both pointers
   at the accepted release, and readiness `ready` or `needs_admin`. Do not
   start the view, do not log in, do not resume, do not send an ask.

6. **Privilege release.** Remote `sudo -K`, then confirm `sudo -n true` fails
   with a password-required message.

## Authority and containment

Positive authority: the ordered commands above through the worker gate; the
release helper `check`, `deploy` and `activate-capture`; read-only verification;
the terminal report write. Host effect class: bounded reversible deployment
(overwrite five unit files and one config file, enable and start three units,
switch two release pointers, one planned runner restart).

Negative authority: no login, view, resume or ask; no token or content
reading; no account, path, token or release removal; no `framenest.service`
change or drop-in; no database action; no repository edit, commit or push; no
dependency change; no `sudo -v`; no `private/**`; no subagents. Do not print
hostnames, private network values, tokens or sockets.

## Stopping conditions

Stop and report on: an unset Step 0 name; a failed gate or privilege probe; a
release-helper gate failure or unexpected deploy result; Xvfb failing or
exiting during the stability pause; an `activate-capture` result other than the
two expected outcomes; more than one Xvfb or Chromium process; a non-loopback
listener; or any instruction conflict. Preserve the first causal failure and
do not improvise or retry.

## Completion and report contract

`PASS` means the corrected release is deployed, the corrected units are
installed and enabled, Xvfb stays active through the stability pause, the
bridge is active, capture activation completed with one of the two expected
outcomes, and the verification above is reported with exact values.
`PARTIAL`/`BLOCKED` otherwise. No login, resume or ask was performed.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the Step 0
result (names only); deploy and activation exit codes and both SHAs; the
read-only unit text checks; the Xvfb stability observations; service states;
process and port observations; the readiness JSON summary; the terminal
`sudo -K` evidence; deviations/risks/missing evidence; one smallest next step
(Cooperator login through the view); `Report justification: new-mutation`;
authority expiry; and:

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
Downloadable prompt filename: 10_deployment_04.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 10_report_04.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
