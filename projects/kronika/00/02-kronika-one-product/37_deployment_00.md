# Kronika one product — NUC latest accepted release and as-left state (pre-move)

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 37
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded NUC Deployment
Phase: deployment
Task identity: KRONIKA-ONE-PRODUCT-NUC-ACCEPTED-RELEASE-AND-AS-LEFT-STATE
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: bounded remote release deployment with privileged read-only inspection while the Cooperator is about to relocate the NUC; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Purpose and boundary

The Cooperator is about to power off and relocate the NUC and then park the
office PC; development continues from a MacBook. This grant brings the NUC to
the latest **accepted and published** code and documents the as-left state.
The S6 candidate `38e7bee…` is **not accepted** and must **not** be deployed:
the routine helper would refuse it (public `main` gate), and deploying an
unaccepted candidate is prohibited. No database reset, no capture action.

## Fresh-session opening

Genuinely fresh Worker session; inherit no prior authority. Independently
establish every Step 0 precondition before any action. This is exactly one
bounded routine deployment plus read-only state capture. No subagents. Never
read `private/**`, tokens, profiles or credential material. Never print
hostnames, private network values, token values, sockets or file contents.

## Starting state (verified read-only at issuance, 2026-09-27)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD `38e7beeb3921d7c0fd8e717e480754fbd18130c9`
  (parent `40e51cb2…`, tree `d6d5d314…`); clean index and worktree; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (gitlink and `.ap` HEAD).
- Local `main` = `origin/main`; public `refs/heads/main` of
  `https://github.com/cisarik/framenest.git` = `40e51cb2…` (the accepted S4-A
  release; also the target of this deployment).
- Host state is prior Worker claim, not independently verified: web pointer
  `fd277a9…`; capture pointer `94e605c…`; capture runner active under a
  temporary recovery override; one root Chromium at `needs_admin`, zero jobs;
  bridge loopback-only; view units inactive. Verify read-only; do not
  normalize divergences.
- The helper's source gate requires local `HEAD` == the requested release, so
  this grant authorizes one exact temporary detached checkout of `40e51cb2…`
  for the deployment and the return checkout to `feat/kronika-one-product`
  afterwards.

## Step 0 — preconditions (fail closed)

Names only, never values:

```text
test -n "$FRAMENEST_NUC_SSH_TARGET" && echo TARGET-set || echo TARGET-unset
test -n "$FRAMENEST_NUC_SSH_USER" && echo USER-set || echo USER-unset
test -n "$FRAMENEST_NUC_SSH_IDENTITY" && echo IDENTITY-set || echo IDENTITY-unset
```

- `scripts/operator/network/framenest_nuc_worker_gate.fish --probe` prints
  `ssh-agent: ready` and exits 0.
- Remote `sudo -n true` through the gate exits 0. The Cooperator established
  the NUC privilege timestamp before dispatch. Use `sudo -n` only; never run
  `sudo -v` or `sudo -K`; never handle or print a password.
- Repository gate: physical root, branch `feat/kronika-one-product`, HEAD
  `38e7bee…`, parent `40e51cb2…`, tree `d6d5d314…`, empty
  `git status --porcelain --untracked-files=no`, AP pin in the gitlink and
  `.ap` HEAD; local `main` = `origin/main` = `40e51cb2…`; direct
  `git ls-remote https://github.com/cisarik/framenest.git` shows
  `refs/heads/main` = `40e51cb2…` and the other public heads unchanged
  (`feat/chatgpt-page-ask-kernel` `26d28b16…`,
  `feat/x-meme-browser-companion` `7ff6546f…`; a newly transported
  `feat/kronika-one-product` `38e7bee…` may also be present).
- Classify any divergence with the five RF-12 classes; stop on unexplained
  remainder.

## Required sequence (ordered; fail closed)

Remote commands go through
`scripts/operator/network/framenest_nuc_worker_gate.fish --command '<command>'`,
one bounded command per invocation, no shell metacharacters. The release
helper's transport uses the exported names and is not run through the gate.

1. **Temporary release checkout.** Confirm clean state, then:

```text
git checkout 40e51cb2d061ead96850c9c94aa59de54d5e1310
git rev-parse HEAD
```

   HEAD must equal the release. Do not touch `.ap`.

2. **Deploy the accepted release** from the repository root:

```text
./deploy/ubuntu/framenest-release status
./deploy/ubuntu/framenest-release check --release 40e51cb2d061ead96850c9c94aa59de54d5e1310
./deploy/ubuntu/framenest-release deploy --release 40e51cb2d061ead96850c9c94aa59de54d5e1310 --yes
```

   `check` must show `public_main` equal to the release and
   `capture_bridge_protocol` `1`. `deploy` must complete with the accepted SHA
   as `web_release` and the capture release still
   `94e605c17b881461fad3e22fd8c7fca32cb93976`. Any migration continuation the
   helper performs is part of this routine deployment; report it exactly, do
   not perform any other database action.

3. **Return checkout.** Restore the working branch and verify:

```text
git checkout feat/kronika-one-product
git rev-parse HEAD
git status --porcelain --untracked-files=no
```

   HEAD must equal `38e7bee…` and the status must be empty. If any step
   stopped while detached, report the exact state and do not improvise
   recovery.

4. **As-left read-only state capture** (one command per gate invocation,
   sanitized reporting):

```text
sudo -n true
sudo -n systemctl show kronika-capture-runner.service -p ActiveState -p SubState -p Result -p NRestarts
sudo -n systemctl show kronika-capture-xvfb.service -p ActiveState -p Result
sudo -n systemctl show kronika-capture-bridge.service -p ActiveState -p Result
sudo -n systemctl is-active framenest.service tailscaled
sudo -n systemctl is-enabled tailscaled
sudo -n readlink /opt/framenest/current
sudo -n readlink /opt/framenest/capture-current
sudo -n cat /opt/framenest/releases/40e51cb2d061ead96850c9c94aa59de54d5e1310/.framenest-release-sha
pgrep -c -x chrome
pgrep -c -x chromium
sudo -n -u kronika-capture /opt/framenest/capture-current/.venv/bin/kronika-capture --state-dir /var/lib/kronika-capture bridge status
sudo -n df -h /opt/framenest
sudo -n ss -ltn
```

   Reporting rules: for `tailscaled`, report only active/enabled states. For
   listeners, report only port numbers and whether each bind is loopback-only;
   never reproduce addresses. For the bridge status, report readiness, reason,
   opaque intervention id, jobs active/total, active_job and
   `client_connected`; if any job or browser root exists, stop and report for
   Orchestrator reconciliation. A readiness of `needs_admin` with zero jobs
   and zero browser roots is the expected parked state, not a failure.

5. **Report.** Do not start, stop, enable or disable any unit; do not open the
   view; do not log in; do not resume; do not run `activate-capture`; do not
   submit any job, prompt or ask; do not run `sudo -K`. The Cooperator
   releases the privilege timestamp manually after the report.

## Authority and containment

Positive authority: the ordered commands above; the canonical release helper
`status`, `check` and `deploy`; the exact temporary detached checkout and its
return; bounded read-only host inspection through the worker gate; the
terminal report write at the exact destination.

Negative authority: no change to the capture pointer, units, overrides,
browser, jobs, journal or state; no database reset, deletion or manual
migration; no deployment of `38e7bee…` or any other release; no repository
change, commit or push; no dependency change; no `sudo -v` or `sudo -K`; no
token, Xauthority or content reading; no `private/**`; no subagents; no tool
outside the declared route.

## Stopping conditions

Stop and report on: an unset Step 0 name; a failed gate probe or privilege
probe; a repository-gate mismatch; a helper gate failure or unexpected deploy
result; a post-deploy pointer other than the expected pair; a capture pointer
change; any capture job or browser root; a non-loopback listener; a need to
mutate anything not authorized above; or any instruction conflict. Preserve
the first causal failure; do not retry or improvise.

## Validation

```text
Evidence tier: E3
Evidence tier basis: remote host mutation (release switch) with privileged read-only inspection while the host is about to be relocated
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none — no repository change
Affected tests: none
New causal regression: none — deployment of an already accepted release
Broad or full suite: not-used
Runtime or testbed: the canonical release helper and the read-only host capture
Independent acceptance: not-required — deployment of an accepted, published release; S9 acceptance remains separate
```

## Completion and report contract

`PASS` means Step 0 passed; `status`, `check` and `deploy` completed with
`public_main` and `web_release` at `40e51cb2…` and capture release still
`94e605c…`; the checkout returned to `feat/kronika-one-product` at `38e7bee…`
clean; the as-left capture is complete with the parked state preserved; and
the report is delivered. Otherwise `PARTIAL`/`BLOCKED`.
`Report justification: new-mutation`. `Logical-whole closure: not-closed`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's coordinates (session 37, exchange 01) exactly once. Include: Step 0
results (names only; probe; `sudo -n true`; repository and public values);
helper `status` summary, `check` fields and `deploy` exit code with printed
SHAs; post-deploy pointers and the deployed `.framenest-release-sha`; the
migration continuation result if any; the return-checkout HEAD and clean
status; the as-left capture with the sanitized rules above; deviations, risks
and missing evidence; one smallest next step (the S6 correction grant on the
MacBook); and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

The formal report is in English; the short completion notice to the Cooperator
is in Slovak, masculine address. Finalize the report, save it at the exact
destination below only if absent, read it back in full, verify its first line,
coordinates, content and path, then send the separate short completion notice
with status, path and SHA-256. Terminal report or cancellation expires this
authority.

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
Downloadable prompt filename: 37_deployment_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 37_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
