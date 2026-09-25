# Kronika one product — start the capture runner and report readiness

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 10
Worker exchange ordinal: 06
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded NUC Deployment
Phase: deployment
Task identity: KRONIKA-ONE-PRODUCT-S3-RUNNER-START
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: first start of the persistent browser on the household NUC and exact readiness/intervention reporting; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Current-session renewal

Continuity anchor: terminal BLOCKED report `10_report_04.md` for task
`KRONIKA-ONE-PRODUCT-S3-HOST-RETRY-2`, Worker session 10, exchange 05, ending
at `d63d0b725acedf49d1611224c3b5201a90e7ef90`.
Authority renewal: that exchange's authority expired at its terminal report.
This exchange grants complete new bounded authority to start the persistent
runner and report readiness, for this session only.
Reuse rationale: this session holds the exact host state. Re-gate the
repository and environment before mutation; retained context is convenience
only. Evidence posture: non-independent. New terminal report: required
(`10_report_05.md`).

## Why this step

The journal carries a `needs_admin` service state (reason `E_AMBIGUOUS_SEND`)
from the failed bootstrap runs, with zero jobs and zero Chromium processes.
`activate-capture` correctly refuses (`capture has live or paused work`, exit
22) before its planned runner restart. The designed recovery requires a
running browser and an operator readiness check: start the runner, confirm the
browser and the exact readiness/intervention state, then the Cooperator logs
in and an explicit resume clears the state before activation is retried.

## Starting state (verified at issuance)

- FrameNest checkout, branch `feat/kronika-one-product`, HEAD
  `d63d0b725acedf49d1611224c3b5201a90e7ef90`; clean; local `main` =
  `origin/main` = public `refs/heads/main` = that commit; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- Host from `10_report_04.md`: web pointer at `d63d0b7`; capture pointer still
  `94e605c`; five corrected units installed and enabled; Xvfb active (lock
  fallback held); bridge active on 8765; runner inactive; no Chromium; status
  `needs_admin` / `E_AMBIGUOUS_SEND`, zero jobs.
- `private/**` is never read. Never print or read the token value.

## Step 0 — preconditions

- Three `FRAMENEST_NUC_SSH_*` names present (names only); otherwise stop
  `BLOCKED`.
- Gate `--probe` prints `ssh-agent: ready`; remote `sudo -n true` exits 0. Use
  `sudo -n` only, never `sudo -v`.

## Required sequence (ordered; fail closed)

All remote commands go through the worker gate without shell metacharacters.

1. **Pre-state (read-only):** bridge and Xvfb `is-active`; runner `is-active`;
   `pgrep -c -x chrome`; `sudo -n -u kronika-capture --
   /opt/framenest/capture-current/.venv/bin/kronika-capture --state-dir
   /var/lib/kronika-capture bridge status`.
2. **Start the persistent runner:**

```text
sudo -n systemctl start kronika-capture-runner.service
sleep 10
sudo -n systemctl is-active kronika-capture-runner.service
pgrep -c -x chrome
```

   Then read the bridge status again:

```text
sudo -n -u kronika-capture -- /opt/framenest/capture-current/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture bridge status
```

   If the first status still shows `starting`, wait once more (`sleep 10`) and
   read it again. Exactly one Chromium process is expected. If the runner
   fails or no browser appears, stop and report the journal cause.

3. **Report the exact state.** From the final status JSON, report: readiness
   state, reason, `intervention_id` (opaque identifier), active/total jobs,
   client connection, protocol, and both release pointers. Do not start the
   view, do not log in, do not resume, do not run `activate-capture`, do not
   send an ask.

4. **Privilege release.** Remote `sudo -K`; confirm `sudo -n true` fails.

## Authority and containment

Positive authority: the ordered read-only checks and the single
`systemctl start kronika-capture-runner.service`; the status command as the
capture user; the terminal report write. Host effect class: one bounded
service start, which launches the persistent browser once.

Negative authority: no view units, no login, no resume, no activation, no ask,
no token or content reading, no unit/account/path/token/release change, no
`framenest.service` change, no database action, no repository edit or push, no
dependency change, no `sudo -v`, no `private/**`, no subagents. Do not print
hostnames, private network values, tokens or sockets.

## Stopping conditions

Stop and report on: an unset Step 0 name; a failed gate or privilege probe;
the runner failing to start or exiting; more than one Chromium process; a
non-loopback listener; an unexpected readiness or job state; or any
instruction conflict. Preserve the first causal failure; do not start the
runner twice and do not improvise.

## Completion and report contract

`PASS` means the runner is active, exactly one Chromium process exists, and the
final status JSON is reported with exact values, whether readiness is `ready`
or `needs_admin`. `PARTIAL`/`BLOCKED` otherwise. No login, resume, activation
or ask was performed.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the Step 0
result; the pre-state; the runner start result and stability; the process and
port observations; the final status fields (including the opaque intervention
id); the terminal `sudo -K` evidence; deviations/risks/missing evidence; one
smallest next step (Cooperator login through the view, then explicit resume);
`Report justification: new-mutation`; authority expiry; and:

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
Downloadable prompt filename: 10_deployment_05.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 10_report_05.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
