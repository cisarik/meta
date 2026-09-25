# Kronika one product — S3 read-only NUC capture preflight (third, corrected launch)

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 07
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Worker-Executed Preflight
Phase: preflight
Task identity: KRONIKA-ONE-PRODUCT-S3-PREFLIGHT
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: privileged read-only verification of a real host whose exact binary paths, ports, ownership and systemd capabilities gate a later bounded mutation; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Launch precondition (changed state justifying this exchange)

The two preceding preflight exchanges (`05_report_00.md`, `06_report_00.md`)
each stopped `BLOCKED` for the same materially unchanged transport blocker: the
three `FRAMENEST_NUC_SSH_*` names were unset in the Worker process. A third
equivalent cycle is prohibited unless the launch environment actually changes.

This exchange is issued only because the Cooperator has now supplied the exact
launch-environment setup (`set -gx`, fish; `export` for bash) for the three
names and will launch this Worker from that environment. The values are never
recorded in this prompt, the report, the notes or any artifact. If the names
are still unset here, stop `BLOCKED` immediately and report that the launch
environment did not change; do not run a gate or remote command.

## Step 0 — environment precondition (before any remote command)

Check only the NAMES, never the values:

```text
test -n "$FRAMENEST_NUC_SSH_TARGET"   && echo TARGET-set   || echo TARGET-unset
test -n "$FRAMENEST_NUC_SSH_USER"     && echo USER-set     || echo USER-unset
test -n "$FRAMENEST_NUC_SSH_IDENTITY" && echo IDENTITY-set || echo IDENTITY-unset
```

If any name is unset: stop immediately with `BLOCKED`, report which names are
unset (names only), do not attempt SSH or the gate transport, and do not touch
anything else. Do not print, echo or store the values.

## Cooperator preconditions (outside the Worker)

- The three `FRAMENEST_NUC_SSH_*` names are exported into the environment that
  launches this Worker session (values never appear in prompts or reports).
- The remote sudo timestamp is established by the Cooperator outside this
  Worker (`sudo -v`, then `sudo -n true`). The Worker uses `sudo -n` only,
  never `sudo -v`, and never handles a password. A password prompt after a
  predecessor `sudo -K` is expected lifecycle state, not a host defect.
- The Worker releases the timestamp at the terminal report with remote
  `sudo -K` where the task permits.

## Starting state (verified at issuance)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `c975aba14840b97944aecc655907e3abc370341d`, parent
  `82a6a59803ed8830c19e51cd8f9bc1665c28a975`, tree
  `a80ab53cf5ee19ffe0af46de4e015519cd97d941`; clean index and worktree.
- Local `main` = `origin/main` =
  `26d28b16c08a5e7e0179a32c16646bfdc1009c81`; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- The capture units hardcode these host paths: `/usr/bin/Xvfb`,
  `/usr/bin/x11vnc`, `/usr/bin/websockify`, `/usr/bin/chromium`, `xauth`,
  `mcookie`, `/usr/bin/install`, `/tmp/.X11-unix`, and ports `8765`, `5900`,
  `6080`. The env template sets `KRONIKA_CHROMIUM_PATH=/usr/bin/chromium`.
- Planned capture paths: `/var/lib/kronika-capture`, `/run/kronika-capture`,
  `/etc/kronika-capture`, `/opt/framenest/capture-current`; account
  `kronika-capture`; package `/usr/share/novnc`.
- `private/**` is never read. Never inspect browser profiles, cookies, tokens,
  credentials, session data or other-tab content.

## Goal

Establish read-only whether the host can host the accepted capture units and
what a later bounded setup/deployment grant must change: exact binary presence
and versions, ports, accounts and paths, service/release state, systemd
credential capability, AppArmor/userns behavior, display tooling, and capacity.
Report exact observed values, mismatches against the unit and template
assumptions, unknowns, and a recommendation. No mutation.

## Required checks (read-only, through the existing gate)

1. **Step 0 precondition** above, then the gate probe
   `scripts/operator/network/framenest_nuc_worker_gate.fish --probe`
   (`ssh-agent: ready`, exit 0), then remote `sudo -n true` exit 0; a password
   prompt is reported as expected lifecycle state and stops the run.
2. **Binary paths and versions.** For each hardcoded path: existence and
   executable bit. Versions where readable without launching a browser:
   `/usr/bin/Xvfb -version`, `/usr/bin/x11vnc -version`,
   `/usr/bin/websockify --help` or version, `xauth -V`, `mcookie --version`,
   `node --version` and `command -v node`, `/usr/bin/install --version`,
   `systemctl --version`. For Chromium: `/usr/bin/chromium --version` only
   (no launch, no flags). Report exact versions; whether the path is a symlink
   and its target.
3. **Ports and runtime state.** `ss -ltn` (or equivalent read-only) for ports
   `8765`, `5900`, `6080`: listening or free. `/tmp/.X11-unix` exists;
   `/tmp/.X99-lock` absent; no Xvfb, chromium, x11vnc, websockify or capture
   node processes running (`pgrep -c` per name).
4. **Accounts.** Existence of `framenest` and `kronika-capture` (boolean, uid
   presence only; no private values). If `kronika-capture` is absent, say so.
5. **Paths and ownership.** For `/var/lib/kronika-capture`,
   `/run/kronika-capture`, `/etc/kronika-capture`,
   `/etc/kronika-capture/credentials`, `/opt/framenest/capture-current`: absent
   or present with owner/group/mode. Do not read file contents. If a browser
   profile directory exists, report only its owner/mode and never its contents.
6. **Web release state (read-only).** `deploy/ubuntu/framenest-release status`
   through the gate: active release SHA, service active, database revision,
   backup readiness, release directory, rollback target. Capture pointer state.
   The currently installed unit source for `framenest.service` (read-only):
   does it already carry a credential line? Do not edit it.
7. **Systemd capability.** `systemctl --version` (credential support), whether
   `LoadCredential=` is usable, and whether a credential source directory can
   later be created under `/etc/kronika-capture/`. No unit is installed,
   started, enabled, edited or reloaded.
8. **AppArmor and userns.** Read-only state relevant to the Chromium path:
   confinement status of `/usr/bin/chromium`, any existing profile for it, and
   the unprivileged-userns restriction value (e.g.
   `/proc/sys/kernel/apparmor_restrict_unprivileged_userns`). Do not launch the
   browser and do not weaken any sandbox.
9. **Display tooling.** Confirm the runner's and Xvfb unit assumptions
   (`/run/kronika-capture/Xauthority`, `DISPLAY=:99`, `-nolisten tcp`) are
   supportable. No display is started.
10. **Capacity.** Read-only free space for `/opt/framenest` and the filesystem
    holding `/var/lib/kronika-capture`; report only sanitized capacity facts.
11. **NoVNC.** `/usr/share/novnc` exists and contains the entry document
    (filename only); `websockify` present.
12. **Sudo release.** Terminal remote `sudo -K` exit 0; followed by remote
    `sudo -n true` exit 1 with a password-required message, confirming release.
    No password is handled or recorded.

## Authority and containment

Positive authority: read-only inspection through
`scripts/operator/network/framenest_nuc_worker_gate.fish`; bounded read-only
`sudo -n` commands for root-owned paths; the `framenest-release status`
read-only operation; read-only repository inspection on the dev host; and
creation of the terminal report.

Commands: the Step 0 name checks; the gate `--probe`; bounded BatchMode remote
read-only commands; `sudo -n` read-only probes; `ss`, `pgrep`, `getent`,
`test`, `ls`, `stat`, `readlink`, `command -v`, `systemctl --version`,
read-only `systemctl status`; and the native file writer for the report only.

Negative authority: no host mutation of any kind — no unit install/start/stop/
enable/reload, no file or directory creation, no package management, no
service restart, no token or credential creation, no browser launch, no display
start, no deployment, no database action, no network change. No profile,
cookie, token, credential or private-content inspection. No repository edit,
no push, no Meta commit. Do not print hostnames, private network values,
tokens, sockets, or credential material.

Side-effect class: read-only host inspection; one report write on the dev host.

## Stopping conditions

Stop and report on: a Step 0 unset name; a failed gate or privilege probe; any
check that would require mutation; sensitive output; an unexpected host state
that makes the remaining checks unsafe; or any instruction conflict. Preserve
the first causal failure. A read-only preflight never repairs anything.

## Completion and report contract

`PASS` means Step 0 passed and every required check above was observed
read-only, with exact values, mismatches, unknowns and a recommendation for the
bounded host setup/deployment grant. Use `PARTIAL` when a check could not be
completed or a material unknown remains; `BLOCKED` when the preflight cannot
proceed safely (including an unset Step 0 name). No mutation occurred; no
deployment claim is made. Use `Phase-qualified result: not-applicable` and
`Logical-whole closure: not-closed`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the Step 0
result (names only); a per-check observation table with exact sanitized values
and exit codes; the mismatch list against the unit/template assumptions;
unknowns; the sudo lifecycle evidence including the terminal release; one
smallest next step; `Report justification: new-evidence`; authority expiry;
and:

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
Downloadable prompt filename: 07_preflight_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 07_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
