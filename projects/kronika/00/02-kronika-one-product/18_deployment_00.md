# Kronika one product — S3 host bring-up: deploy e408bb5 and classify current state (D1)

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 18
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded NUC Deployment
Phase: deployment
Task identity: KRONIKA-ONE-PRODUCT-S3-DEPLOY-AND-INSPECT-D1
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: deploying the accepted diagnostics/activation release to the household NUC and classifying a previously unexplained browser-startup state; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Fresh-session opening

This is a genuinely fresh Worker session; inherit no prior authority from any
other session. Independently establish the repository and environment evidence
required by Step 0 before any action. Retained context, if any, is convenience
only; on conflict with current repository or host evidence, stop and report.
No subagents. This grant is one bounded deployment and one read-only state
inspection; it does not launch a browser, log in, resume, activate or ask.

## Starting state (verified read-only at issuance, 2026-09-25)

- FrameNest checkout `/home/agile/Projects/framenest`; branch
  `feat/kronika-one-product`; HEAD
  `e408bb5503f359ec24542304ac1a621c6b9e4ffb` (parent
  `d63d0b725acedf49d1611224c3b5201a90e7ef90`, tree
  `dadc01726a354c319374832bfd385be0bdffb516`, subject
  `fix(capture): diagnose startup and require fresh activation readiness`);
  clean index and worktree; local `main` = `origin/main` = that commit; direct
  public `git ls-remote https://github.com/cisarik/framenest.git
  refs/heads/main` = that commit; other public heads unchanged
  (`feat/chatgpt-page-ask-kernel` `26d28b16`,
  `feat/x-meme-browser-companion` `7ff6546f`); AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (gitlink and `.ap` HEAD).
- Host state is a prior Worker claim from accepted reports `10_report_04.md`
  and `10_report_05.md`, not independently verified by the Orchestrator:
  web pointer `d63d0b7`; capture pointer `94e605c`; five capture units
  installed from `d63d0b7` sources and enabled; Xvfb active; bridge active on
  `127.0.0.1:8765`; runner active with `client_connected` true and no Chromium
  process; readiness `browser_unavailable` (`E_BROWSER_UNAVAILABLE`); zero
  jobs; one opaque intervention id. Verify all of this read-only in D1 and
  report divergences instead of normalizing them.
- `private/**` is never read. Never print or read the token value.

## Goal

Deploy the accepted, published release
`e408bb5503f359ec24542304ac1a621c6b9e4ffb` through the canonical release
helper, then perform the single read-only D1 state inspection of the capture
host. This is not S3 completion and establishes no browser launch. D2/D3, the
Cooperator view login, the explicit null-job resume, `activate-capture` and the
one synthetic ask remain separate later steps.

## Step 0 — preconditions (fail closed)

Check only names, never values:

```text
test -n "$FRAMENEST_NUC_SSH_TARGET" && echo TARGET-set || echo TARGET-unset
test -n "$FRAMENEST_NUC_SSH_USER" && echo USER-set || echo USER-unset
test -n "$FRAMENEST_NUC_SSH_IDENTITY" && echo IDENTITY-set || echo IDENTITY-unset
```

If any is unset, stop `BLOCKED` immediately (names only). Then:

- `scripts/operator/network/framenest_nuc_worker_gate.fish --probe` prints
  `ssh-agent: ready` and exits 0.
- Remote `sudo -n true` through the gate exits 0. The Cooperator established
  the NUC privilege timestamp before dispatch, outside this Worker. Use
  `sudo -n` only. Never run `sudo -v` or `sudo -K`; never handle or print a
  password.
- Repository gate: independently verify the physical root, branch, HEAD,
  parent, tree, clean index and worktree, local `main` = `origin/main` =
  `e408bb5503f359ec24542304ac1a621c6b9e4ffb`, public `refs/heads/main` of
  `https://github.com/cisarik/framenest.git` = the same commit via
  `git ls-remote`, and the AP pin `7478ddb0…` in both the gitlink and `.ap`
  HEAD. Classify any divergence with the five RF-12 recovery classes; stop on
  unexplained remainder.

Do not proceed on a failed or contradictory precondition.

## Required sequence (ordered; fail closed)

All remote commands go through
`scripts/operator/network/framenest_nuc_worker_gate.fish --command '<command>'`,
one bounded command per invocation, with no shell metacharacters. Never print a
token or file contents.

1. **Deploy the accepted release** from the repository root. The helper's
   transport uses the exported names; it is not run through the gate:

```text
./deploy/ubuntu/framenest-release status
./deploy/ubuntu/framenest-release check --release e408bb5503f359ec24542304ac1a621c6b9e4ffb
./deploy/ubuntu/framenest-release deploy --release e408bb5503f359ec24542304ac1a621c6b9e4ffb --yes
```

   `check` must show `public_main` equal to the release and
   `capture_bridge_protocol` `1`. `deploy` must complete with the accepted SHA
   as `web_release` and capture release still
   `94e605c17b881461fad3e22fd8c7fca32cb93976`. Stop on any gate failure.
   This grant is the deployment authorization; a successful check alone is
   not.

2. **D1 — read-only state inspection.** One command per gate invocation, in
   this order:

```text
sudo -n true
sudo -n systemctl show kronika-capture-runner.service -p ActiveState -p SubState -p Result -p NRestarts -p User -p Group -p ProtectSystem -p NoNewPrivileges -p ReadWritePaths
sudo -n systemctl show kronika-capture-xvfb.service -p ActiveState -p Result -p NRestarts
sudo -n systemctl show kronika-capture-bridge.service -p ActiveState -p Result
sudo -n systemctl is-active framenest.service
sudo -n readlink /opt/framenest/current
sudo -n readlink /opt/framenest/capture-current
sudo -n cat /opt/framenest/releases/e408bb5503f359ec24542304ac1a621c6b9e4ffb/.framenest-release-sha
sudo -n grep -F -e ExecStart= -e User= -e Group= -e Environment= -e ReadWritePaths= -e ProtectSystem= -e NoNewPrivileges= -e LoadCredential= -e Restart= /etc/systemd/system/kronika-capture-runner.service
sudo -n grep -F -e ExecStart= -e User= -e Group= -e ReadWritePaths= -e ProtectSystem= -e NoNewPrivileges= -e Restart= /etc/systemd/system/kronika-capture-xvfb.service
sudo -n grep -F -e ExecStart= -e User= -e Group= -e Environment= -e ReadWritePaths= -e ProtectSystem= -e NoNewPrivileges= -e LoadCredential= -e Restart= /etc/systemd/system/kronika-capture-bridge.service
pgrep -c -x chrome
pgrep -c -x chromium
ps -C chrome -o pid=,ppid=,comm=
sudo -n -u kronika-capture /opt/framenest/capture-current/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture bridge status
sudo -n -u kronika-capture test -r /run/kronika-capture/Xauthority
sudo -n test -S /tmp/.X11-unix/X99
sudo -n readlink -e /usr/bin/chromium
sudo -n sysctl -n kernel.apparmor_restrict_unprivileged_userns
sudo -n ss -ltn
```

   Notes for D1:

   - The expected post-deploy pointers are `/opt/framenest/current` =
     `e408bb5503f359ec24542304ac1a621c6b9e4ffb` and
     `/opt/framenest/capture-current` =
     `94e605c17b881461fad3e22fd8c7fca32cb93976`.
   - Installed runner and bridge units must keep `--state-dir` before the
     subcommand; the installed Xvfb unit must contain no `-nolock` and must
     include `/tmp` in `ReadWritePaths`. Compare the grep lines against the
     repository sources at `e408bb5…`.
   - Count browser roots structurally: a root is a `chrome` process whose
     parent is not another `chrome` process; `ps` output here is pid/ppid/comm
     only. Report `chrome`/`chromium` counts and the inferred root count.
   - From `ss -ltn`, report only the listening port numbers and whether each
     bind is loopback-only; do not reproduce non-loopback addresses.
   - If the runner or bridge status shows any job (`jobs.total` not `0`,
     `jobs.active` not `0`, `active_job` not `null`), or any capture browser
     root exists, stop and report for Orchestrator reconciliation.
   - A readiness of `browser_unavailable`, `needs_admin` or `starting` with
     zero jobs and zero browser roots is expected input to the later D2/D3
     blocks, not a failure of this grant.
   - Stop the D1 sequence on any material divergence from this prompt's
     expected values and report it exactly; do not mutate anything to
     normalize it.

3. **Report.** Do not start or stop any unit; do not start the view; do not
   log in; do not read Xauthority contents; do not resume; do not run
   `activate-capture`; do not submit any job, prompt or ask; do not run
   `sudo -K`. The Cooperator releases the privilege timestamp manually after
   your report.

## Authority and containment

Positive authority: the ordered commands above; the canonical release helper
`status`, `check` and `deploy`; bounded read-only host inspection through the
worker gate; the terminal report write at the exact destination. Host effect
class: bounded reversible deployment (install release `e408bb5…`, switch the
web release pointer, the helper's routine web service refresh) plus read-only
inspection.

Negative authority: no capture pointer change; no unit install, enable,
disable, start or stop beyond the helper's own routine deploy; no drop-in or
override; no browser launch; no view, login, resume, activation or ask; no
token, Xauthority or content reading; no account, path, token or release
removal; no `framenest.service` edit; no database action; no repository edit,
commit or push; no dependency change; no `sudo -v` or `sudo -K`; no
`private/**`; no subagents; no tool outside the declared route. Do not print
hostnames, private network values, tokens or sockets.

## Stopping conditions

Stop and report on: an unset Step 0 name; a failed gate or privilege probe; a
repository-gate mismatch; a release-helper gate failure or unexpected deploy
result; a post-deploy pointer other than the expected pair; any unexpected
unit state; any capture browser process or non-zero job state; a non-loopback
listener; any need to mutate something not authorized above; or any
instruction conflict. Preserve the first causal failure; do not retry,
improvise or fall back to another route.

## Validation

Validation ladder: selected.
Inspection and provenance: required — repository gate, helper outputs,
installed unit directives and release identity.
Existing focused tests: none — no repository change.
Affected tests: none.
New causal regression: none — deployment and read-only inspection only; no
candidate change, so no test can close this grant.
Broad or full suite: not-used.
Runtime or testbed: the canonical release helper and the D1 read-only host
inspection.
Independent acceptance: not-required — deployment of an already accepted
release; final S3 host acceptance remains separate.

## Completion and report contract

`PASS` means: Step 0 passed; helper `status`, `check` and `deploy` completed
with `public_main` and `web_release` at `e408bb5…` and capture release still
`94e605c…`; D1 produced the complete classified observations with zero jobs,
zero capture browser roots, the expected pointers and unit states, and
loopback-only listeners; and the report is delivered. `PARTIAL`/`BLOCKED`
otherwise. No browser launch, login, resume, activation or ask was performed.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core, plus:

- Step 0 results: names only (TARGET/USER/IDENTITY set or unset); probe
  result; `sudo -n true` result; repository gate values; public `ls-remote`
  value.
- Helper: `status` summary fields; `check` fields (`public_main`,
  `capture_bridge_protocol`, `current_release`, other observed fields);
  `deploy` exit code and printed SHAs.
- Post-deploy: both pointers; the deployed release's
  `.framenest-release-sha`; `framenest.service` state.
- D1: per-unit systemctl show fields; installed unit directive lines; the
  process counts and inferred browser-root count; the bridge status summary
  (readiness, reason, opaque intervention id, jobs active/total, active_job,
  `client_connected`, protocol, api_version); Xauthority readable; X99 socket;
  `/usr/bin/chromium` resolution; userns value; listener classification for
  8765, 5900, 6080 and 6099 without non-loopback addresses.
- Deviations, risks, missing evidence; exact first causal error on any stop;
  one smallest next step (the Cooperator-executed D2/D3 blocks); authority
  expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

`Report justification: new-mutation`.

Direct communication with the Cooperator (the short completion notice) is in
Slovak, masculine address for him. This prompt and the formal report are in
English. Do not use subagents. Do not commit Meta artifacts.

Finalize the report, save it at the exact destination, read it back in full,
and verify its first line, coordinates, content and path before the short
separate completion notice with status, exact report path and SHA-256. Terminal
report or cancellation expires this authority; no autonomous continuation.

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
Downloadable prompt filename: 18_deployment_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 18_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
