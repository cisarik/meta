# Kronika one product — S3 C3 deployment and the single corrected bootstrap start

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 24
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded NUC Deployment
Phase: deployment
Task identity: KRONIKA-ONE-PRODUCT-S3-C3-DEPLOY-AND-START
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: first host deployment of the accepted temporary-directory correction, its unit reinstall, and the single budgeted corrected browser start; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Fresh-session opening

This is a genuinely fresh Worker session; inherit no prior authority.
Independently establish the repository and host state from Stage 0 before any
action. This grant authorizes exactly one corrected browser start. No retry,
no rollback launch and no second diagnostic start are authorized. No
subagents. `private/**` is never read; never print or read the token value;
never inspect the browser profile or its internal locks.

## Starting state (verified read-only at issuance, 2026-09-25)

- FrameNest checkout `/home/agile/Projects/framenest`; branch
  `feat/kronika-one-product`; HEAD
  `fd277a9a64a6965df76127dbec5b1735d2fb3cdd` (parent
  `e408bb5503f359ec24542304ac1a621c6b9e4ffb`, tree
  `3b9014956a3bc738a209af51034fcac58ef5c498`, subject
  `fix(capture): point the capture runner temporary directory at its runtime dir`);
  clean; local `main` = `origin/main` = public `refs/heads/main` =
  `fd277a9…`; AP pin `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- Host state from the accepted recovery sequence: runner `inactive`; Xvfb and
  bridge `active`; web pointer `e408bb5…`; capture pointer `94e605c…`; no
  Chromium process; no recovery override; external brake `lock` absent and
  `last-start.json` valid with the 300-second interval long expired (last
  attempt 2026-09-25 16:39 UTC); `/run/kronika-capture` is writable by the
  capture account. The installed runner unit predates the C3 correction; the
  installed `/etc/kronika-capture/capture.env` has not been read.
- Accepted evidence: the instrumented launch established
  `process_singleton_posix.cc:1043 Failed to create socket directory.` and
  exit 21 on read-only general `/tmp`; C3 is accepted (`22_report_00.md`,
  acceptance-PASS) and published (`23_report_00.md`, publication-PASS).

## Goal

Deploy the accepted correction `fd277a9…` through the canonical helper,
install the corrected runner unit from the deployed release tree, perform the
read-only installed-environment and brake checks, then execute exactly one
corrected bootstrap start using the accepted temporary-override mechanism and
classify its outcome. Stop before the view, login, resume, activation or any
ask.

## Stage 0 — preconditions (fail closed)

- Names only, never values:

```text
test -n "$FRAMENEST_NUC_SSH_TARGET" && echo TARGET-set || echo TARGET-unset
test -n "$FRAMENEST_NUC_SSH_USER" && echo USER-set || echo USER-unset
test -n "$FRAMENEST_NUC_SSH_IDENTITY" && echo IDENTITY-set || echo IDENTITY-unset
```

- `scripts/operator/network/framenest_nuc_worker_gate.fish --probe` prints
  `ssh-agent: ready`. Remote `sudo -n true` through the gate exits 0. The
  Cooperator established the timestamp before dispatch; use `sudo -n` only,
  never `sudo -v` or `sudo -K`.
- Repository gate: physical root, branch, HEAD, parent, tree, clean index and
  worktree, local `main` = `origin/main` = `fd277a9…`, public
  `refs/heads/main` = `fd277a9…` via `git ls-remote`, AP pin `7478ddb0…`.
  Classify divergence with RF-12; stop on unexplained remainder.

All remote commands go through
`scripts/operator/network/framenest_nuc_worker_gate.fish --command '<command>'`,
one bounded command per invocation, no shell metacharacters.

## Stage 1 — deploy the accepted release (from the repository root; no gate)

```text
./deploy/ubuntu/framenest-release status
./deploy/ubuntu/framenest-release check --release fd277a9a64a6965df76127dbec5b1735d2fb3cdd
./deploy/ubuntu/framenest-release deploy --release fd277a9a64a6965df76127dbec5b1735d2fb3cdd --yes
```

`check` must show `public_main` = `fd277a9…` and `capture_bridge_protocol`
`1`. `deploy` must complete with web release `fd277a9…` and capture release
still `94e605c…`. Stop on any gate failure.

## Stage 2 — install and verify the corrected runner unit

```text
sudo -n install -m 0644 /opt/framenest/current/deploy/systemd/kronika-capture-runner.service /etc/systemd/system/kronika-capture-runner.service
sudo -n systemctl daemon-reload
sudo -n grep -F -e TMPDIR= -e ExecStartPre= /etc/systemd/system/kronika-capture-runner.service
```

The installed unit must contain
`Environment=TMPDIR=/run/kronika-capture/tmp` and the `ExecStartPre` with
`-m 0700` and `/run/kronika-capture/tmp`. Do not modify any other unit,
`framenest.service` or `capture.env`.

## Stage 3 — read-only installed capture environment check

```text
sudo -n grep -n TMPDIR /etc/kronika-capture/capture.env
```

An assignment (output present, exit 0) would override the unit value: stop
`BLOCKED` and report only that an assignment exists. Expected: no output,
exit 1. Do not print other file content.

## Stage 4 — brake check (metadata only, no launch)

```text
sudo -n test -e /var/lib/kronika-capture/profile.capture-launch/lock
sudo -n test -L /var/lib/kronika-capture/profile.capture-launch/lock
sudo -n stat -c '%F %U %G %a' /var/lib/kronika-capture/profile.capture-launch/last-start.json
sudo -n cat /var/lib/kronika-capture/profile.capture-launch/last-start.json
```

Require: no `lock` entry (both tests exit 1), `last-start.json` a regular file
owned by the capture account, and `started_ms` at least 300,000 ms before now.
If the lock exists, the metadata is unverifiable, or the interval has not
expired, stop and report; no lock removal, no metadata edit, no profile
inspection.

## Stage 5 — the single corrected bootstrap start (Cooperator-executed)

After Stages 1–4 pass, emit exactly the block below once to the Cooperator,
in Slovak, preceded by its one-line purpose, and ask for the complete output.
One block in flight; wait before classifying. If the paste is detectably
corrupted before anything ran, re-emit the exact block once; if it partially
ran, stop and report. This is the one authorized start; do not repeat it.

Purpose for the Cooperator: dočasný `ExecStart` override presmeruje runner na
prijatý release `fd277a9` (inštalovaná jednotka dodá `TMPDIR` a `ExecStartPre`)
a spustí runner raz; nič iné sa nemení.

```bash
# [NUC / bash]
echo "== S3-START START =="
(
set -eu
fail() { printf 'start_guard=%s\n' "$1"; exit 1; }
S3_RELEASE=fd277a9a64a6965df76127dbec5b1735d2fb3cdd

sudo -n true || fail privilege
test "$(sudo -n cat "/opt/framenest/releases/$S3_RELEASE/.framenest-release-sha")" = "$S3_RELEASE" || fail release_sha
test "$(sudo -n systemctl show kronika-capture-runner.service -p ActiveState --value)" = inactive || fail runner_state
test "$(sudo -n systemctl show kronika-capture-xvfb.service -p ActiveState --value)" = active || fail display_state
test "$(sudo -n systemctl show kronika-capture-bridge.service -p ActiveState --value)" = active || fail bridge_state
if sudo -n test -e /var/lib/kronika-capture/profile.capture-launch/lock || sudo -n test -L /var/lib/kronika-capture/profile.capture-launch/lock; then fail brake_lock_present; fi
test ! -e /run/systemd/system/kronika-capture-runner.service.d/90-s3-recovery.conf || fail override_exists
test ! -L /run/systemd/system/kronika-capture-runner.service.d/90-s3-recovery.conf || fail override_exists
echo "preconditions_ok"
sudo -n install -d -m 0755 /run/systemd/system/kronika-capture-runner.service.d
printf '%s\n' \
  '[Service]' \
  'ExecStart=' \
  "ExecStart=/opt/framenest/releases/$S3_RELEASE/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture runner run --profile /var/lib/kronika-capture/profile --port 8765 --headed" \
  | sudo -n tee /run/systemd/system/kronika-capture-runner.service.d/90-s3-recovery.conf >/dev/null
echo "override_written_ok"
sudo -n systemctl daemon-reload
echo "daemon_reload_ok"
sudo -n systemctl start kronika-capture-runner.service
echo "runner_start_ok"
)
echo "subshell_exit=$?"
echo "== S3-START DONE =="
#------------------------------------------------------
```

## Stage 6 — read-only classification (through the gate)

Wait at least 20 seconds (a bounded remote `sleep 20` is permitted), then:

```text
sudo -n systemctl show kronika-capture-runner.service -p ActiveState -p SubState -p Result -p NRestarts -p ExecMainStatus -p ExecStart
pgrep -c -x chrome
pgrep -c -x chromium
ps -C chrome -o pid=,ppid=,comm=
sudo -n -u kronika-capture /opt/framenest/capture-current/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture bridge status
sudo -n journalctl -u kronika-capture-runner.service --since "-3 min" --no-pager -n 60
sudo -n readlink /opt/framenest/current
sudo -n readlink /opt/framenest/capture-current
sudo -n ss -ltn
```

Classification:

- **Started** (success): at least one `chrome` root process; the bridge status
  shows a fresh `browser_session` and `client.connected` true; readiness is
  `needs_admin` (`E_LOGIN_REQUIRED`/`E_NEEDS_ADMIN`/captcha) or `ready`; zero
  jobs. Keep the browser and the override in place; do not start the view, do
  not log in, do not resume, do not activate, do not ask.
- **Failed**: no `chrome` root and a C1 `capture_startup` failure record in
  the bounded journal. Then clean up exactly (through the gate, one command
  per invocation): stop the runner; remove
  `/run/systemd/system/kronika-capture-runner.service.d/90-s3-recovery.conf`;
  `systemctl daemon-reload`; verify the override is absent. Preserve the
  profile, brake timestamp, journal, tokens and release pointers. Report the
  exact C1 classification; do not retry and do not improvise a correction.
- Report listener bind scope for the capture ports only; do not reproduce
  non-loopback addresses.

## Authority and containment

Positive authority: the ordered commands above; the canonical release helper
`status`, `check` and `deploy`; read-only gate inspection; the unit install
and `daemon-reload`; emitting the one exact Cooperator block and receiving its
output; bounded failure cleanup; the terminal report write.

Host effect class: bounded reversible deployment (install release `fd277a9…`,
switch the web pointer, replace one unit file), one unit-level runner start
that launches the persistent browser once, and read-only verification. No
capture-pointer change, no activation, no `rollback-capture`, no second start.

Negative authority: no view/login/resume/activation/ask; no token, journal or
profile content access; no account, path, token or release removal; no
`framenest.service` change; no database action; no repository edit, commit or
push; no dependency change; no `sudo -v` or `sudo -K`; no `private/**`; no
subagents. Do not print hostnames, private network values, tokens or sockets.

## Stopping conditions

Stop and report on: an unset Stage 0 name; a failed gate or privilege probe; a
repository-gate mismatch; a helper gate failure or unexpected deploy result; an
unexpected installed unit text; an installed `TMPDIR` assignment in
`capture.env`; a present brake lock, unverifiable metadata or unexpired
interval; a paste failure with partial execution; more than one Chromium root
on success; or any instruction conflict. Preserve the first causal failure; do
not retry the start; do not improvise.

## Validation

Validation ladder: selected.
Inspection and provenance: required — repository gate, helper outputs,
installed unit text, release identity, brake metadata.
Existing focused tests: none on the host — no repository change.
Affected tests: none.
New causal regression: none — host execution of an already accepted and
published correction; the causal evidence is the classified start.
Broad or full suite: not-used.
Runtime or testbed: the canonical release helper and the installed capture
units.
Independent acceptance: not-required for this host execution; the accepted
candidate was independently accepted at `22_report_00.md`.

## Completion and report contract

`PASS` means: Stages 0–4 passed; the accepted release is deployed and the
corrected runner unit installed and verified; the installed environment check
found no `TMPDIR` override; the brake was clean; exactly one corrected start
ran; and Stage 6 classified the outcome with a live browser session
(`needs_admin` or `ready`) or, on failure, the exact C1 classification after
cleanup. `PARTIAL`/`BLOCKED` otherwise. No view, login, resume, activation or
ask was performed.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; Stage 0–4
results with exact values; the helper `check`/`deploy` fields; installed unit
and environment findings; brake metadata result; the Cooperator block outcome
(`subshell_exit` and markers); the runner state, process counts, bridge status
summary (readiness, reason, opaque intervention id, `browser_session`, jobs,
`client_connected`), the bounded C1 record if any, and listener bind scope for
the capture ports without non-loopback addresses; cleanup outcome on failure;
deviations/risks/missing evidence; one smallest next step (Cooperator view
login, then the explicit null-job resume); `Report justification: new-mutation`;
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
verify its first line, coordinates, content and path, then send the short
separate completion notice with status, path and SHA-256. Terminal report or
cancellation expires this authority.

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
Downloadable prompt filename: 24_deployment_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 24_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
