# Kronika one product — NUC routine release update to `0d0d8c8`

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 41
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded NUC Deployment
Phase: deployment
Task identity: KRONIKA-ONE-PRODUCT-NUC-RELEASE-0D0D8C8
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — bounded remote release deployment with a schema jump and privileged read-only inspection; the Cooperator may override.
Recommended context capacity: approximately 200k tokens
Independence required: no

## Purpose and boundary

Bring the NUC to the accepted published release
`0d0d8c88bf88bf8454751a0205bc8652374796c2` through the sole routine entry
point `deploy/ubuntu/framenest-release`, and capture the as-left state
read-only. The release carries the S6 records schema (migration
`0034_kronika_records.py`) while the NUC database is expected at revision
`0033`; any migration continuation the helper performs is part of this routine
update and must be reported exactly. Do not perform any other database action,
and never reset or delete the database.

The capture module stays parked: no browser restart, login, resume,
activation, job, prompt or ask; the capture pointer must stay
`94e605c17b881461fad3e22fd8c7fca32cb93976`.

## Fresh-session opening

Genuinely fresh Worker session; inherit no prior authority. Independently
establish every Step 0 precondition before any action. This is exactly one
bounded routine deployment plus read-only state capture. No subagents. Never
read `private/**`, tokens, profiles or credential material. Never print
hostnames, addresses, private network values, token values, sockets or file
contents.

## Cooperator preconditions (established before dispatch; not Worker actions)

- The three `FRAMENEST_NUC_SSH_*` names are exported in the environment that
  launches this Worker; the Worker checks only their presence.
- The Cooperator established the NUC sudo timestamp (`sudo -v`, then
  `sudo -n true`) outside the Worker and releases it manually afterwards.
  Workers use `sudo -n` only and never run `sudo -v` or `sudo -K`.

## Starting state (verified read-only at issuance, 2026-09-28)

- FrameNest checkout `/Users/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `0d0d8c88bf88bf8454751a0205bc8652374796c2` (parent
  `5843486ddeae13ec5b331f102c5cb595bfa6e386`, tree
  `96adead05beb58f2e282ff77b9e6d29bff2c8298`, subject
  `fix(kronika): serve approved projections on household reads`); clean index
  and worktree; AP pin `73e20ef80b88700d5fcbc397cd8edd4fc425869f` (gitlink and
  `.ap` HEAD).
- Local `main` branch `40e51cb2…`; local `origin/main` `0d0d8c8…`; public
  `https://github.com/cisarik/framenest.git`: `refs/heads/main` `0d0d8c8…`,
  `refs/heads/feat/kronika-one-product` `38e7bee…`,
  `refs/heads/feat/chatgpt-page-ask-kernel` `26d28b16…`,
  `refs/heads/feat/x-meme-browser-companion` `7ff6546f…`.
- NUC prior state is a Worker claim (report `37_report_00.md`), verify
  read-only: web release `40e51cb2…`; capture release `94e605c…`; database
  revision `0033` expected; capture runner active, readiness
  `browser_unavailable` (`E_BROWSER_UNAVAILABLE`), zero jobs, zero
  chrome/chromium; `tailscaled` active and enabled. Verify; do not normalize
  divergences.

## Step 0 — preconditions (fail closed)

Names only, never values:

```text
test -n "$FRAMENEST_NUC_SSH_TARGET" && echo TARGET-set || echo TARGET-unset
test -n "$FRAMENEST_NUC_SSH_USER" && echo USER-set || echo USER-unset
test -n "$FRAMENEST_NUC_SSH_IDENTITY" && echo IDENTITY-set || echo IDENTITY-unset
```

- `scripts/operator/network/framenest_nuc_worker_gate.fish --probe` prints
  `ssh-agent: ready` and exits 0.
- Remote `sudo -n true` through the gate exits 0 (the Cooperator established
  the timestamp; do not run `sudo -v` or `sudo -K`).
- Repository gate: physical root; branch; HEAD, parent, tree, subject; empty
  `git status --porcelain --untracked-files=all`; AP pin in the gitlink and
  `.ap` HEAD; local `origin/main` `0d0d8c8…`; direct
  `git ls-remote https://github.com/cisarik/framenest.git` shows
  `refs/heads/main` `0d0d8c8…` and the other heads unchanged.
- Classify any divergence; stop on unexplained remainder.

## Required sequence (ordered; fail closed)

Remote read commands go through
`scripts/operator/network/framenest_nuc_worker_gate.fish --command '<command>'`,
one bounded command per invocation, no shell metacharacters. The release
helper's transport uses the exported names and is not run through the gate.

1. **Temporary release checkout.** Confirm clean state, then:

```text
git checkout 0d0d8c88bf88bf8454751a0205bc8652374796c2
git rev-parse HEAD
```

   HEAD must equal the release. Do not touch `.ap`.

2. **Deploy the accepted release** from the repository root:

```text
./deploy/ubuntu/framenest-release status
./deploy/ubuntu/framenest-release check --release 0d0d8c88bf88bf8454751a0205bc8652374796c2
./deploy/ubuntu/framenest-release deploy --release 0d0d8c88bf88bf8454751a0205bc8652374796c2 --yes
```

   `check` must show `public_main` equal to the release and
   `capture_bridge_protocol` `1`. `deploy` must complete with the release as
   `web_release` and the capture release still
   `94e605c17b881461fad3e22fd8c7fca32cb93976`. Any migration continuation
   (expected `0033` -> `0034`) is part of this routine deployment; report it
   exactly and perform no other database action.

3. **Post-deploy status** (read-only, once):

```text
./deploy/ubuntu/framenest-release status
```

   Report `web_release`, `capture_release`, `database_revision`,
   `service_active`, `backup_restore_readiness`.

4. **Return checkout.** Restore the working branch and verify:

```text
git checkout feat/kronika-one-product
git rev-parse HEAD
git status --porcelain --untracked-files=no
```

   HEAD must equal `0d0d8c8…` and the status must be empty. If any step
   stopped while detached, report the exact state and do not improvise
   recovery.

5. **As-left read-only state capture** (one command per gate invocation,
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
sudo -n cat /opt/framenest/releases/0d0d8c88bf88bf8454751a0205bc8652374796c2/.framenest-release-sha
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
   `client_connected`; readiness `browser_unavailable` with zero jobs and zero
   browser roots is the expected parked state, not a failure.

6. **Report.** Do not start, stop, enable or disable any unit; do not open the
   view; do not log in; do not resume; do not run `activate-capture`; do not
   submit any job, prompt or ask; do not run `sudo -K`. The Cooperator releases
   the privilege timestamp manually after the report.

## Authority and containment

Positive authority: the ordered commands above; the canonical release helper
`status`, `check` and `deploy`; the exact temporary detached checkout and its
return; bounded read-only host inspection through the worker gate; the terminal
report write at the exact destination.

Negative authority: no change to the capture pointer, units, overrides,
browser, jobs, journal or state; no database reset, deletion or manual
migration; no deployment of any other release; no repository change, commit or
push; no dependency change; no `sudo -v` or `sudo -K`; no token, Xauthority or
content reading; no `private/**`; no subagents; no tool outside the declared
route.

## Stopping conditions

Stop and report on: an unset Step 0 name; a failed gate probe or privilege
probe; a repository-gate mismatch; a helper gate failure or unexpected deploy
result; a post-deploy pointer other than the expected pair; a capture pointer
change; any capture job or browser root; a non-loopback bind of the bridge port
`8765` or of the capture view ports `5900`/`6080` (non-capture listeners such
as `22`, `443`, `631` are classified note-only, outside the capture boundary);
a need to mutate anything not authorized above; or any instruction conflict.
Preserve the first causal failure; do not retry or improvise.

## Validation

```text
Evidence tier: E3
Evidence tier basis: remote host mutation (release switch and expected schema jump) with privileged read-only inspection
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none — no repository change
Affected tests: none
New causal regression: none — routine deployment of an accepted, published release
Broad or full suite: not-used
Runtime or testbed: the canonical release helper and the read-only host capture
Independent acceptance: not-required — S9 integrated acceptance remains separate
```

## Completion and report contract

`PASS` means: Step 0 passed; `status`, `check` and `deploy` completed with
`public_main` and `web_release` at `0d0d8c8…` and capture release still
`94e605c…`; the migration continuation result is reported exactly; the checkout
returned to `feat/kronika-one-product` at `0d0d8c8…` clean; the as-left capture
is complete with the parked capture state preserved; and the report is
delivered. Otherwise `PARTIAL`/`BLOCKED`. `Report justification: new-mutation`.
`Logical-whole closure: not-closed`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's coordinates (session 41, exchange 01) exactly once. Include: Step 0
results (names only; probe; `sudo -n true`; repository and public values); the
helper `status` summary, `check` fields and `deploy` exit code with printed
SHAs; the migration continuation result; post-deploy pointers and the deployed
`.framenest-release-sha`; the return-checkout HEAD and clean status; the
as-left capture with the sanitized rules above; deviations, risks and missing
evidence; one smallest next step (the S4-B native provider runtime per
`ROADMAP.md`); and:

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
Trace discovery: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 41_deployment_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 41_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
