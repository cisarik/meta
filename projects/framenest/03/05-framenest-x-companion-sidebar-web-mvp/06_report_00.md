### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-x-companion-sidebar-web-mvp
Worker session ordinal: 06
Worker exchange ordinal: 01
```

## Terminal status

```text
Status: PASS
Phase-qualified result: deployment-PASS
production-acceptance-PASS: not claimed
independent-acceptance-PASS: not claimed
Logical-whole closure: not-closed
Report justification: changed-external-state
```

Deployment PASS is not production acceptance, not independent acceptance, and
not ORCHESTRATOR closure. Live Gallery 📎 is not claimed. Empty
`FRAMENEST_COMPANION_EXTENSION_ORIGINS` remains fail-closed on the two X POSTs.
This Worker did not write that allowlist and did not set `x_acquisition_root`.

Authority from `06_operations_00.md` expires on submission of this report.

## Capability handshake

```text
Requested route: fresh-worker-session; Native planning mode not-used; Extra High; no Max; NUC mutation inside this envelope; no product-code implementation; no push; no AP pin apply; no companion-origin host config
Client and Worker surface: Cursor Worker chat
Model: Extra High reasoning requested; model identity is not self-verified from this prompt. Client-presented identity in this session is Cursor Grok 4.6.
Reasoning effort: extra-high requested; Max not requested
Permission mode: Agent mode observed; Native planning mode not-used as routed
Enhanced or maximum mode: not requested; never inferred
Automatic model selection: off; no silent weaker fallback observed
Worker session target: fresh-worker-session
Independence requirement: no
Independent acceptance: required-separate-fresh-worker (not this session)
Sub-agents or internal delegation: not-used
Worker topology: single-active
Development envelope activation: not-used
```

Separated:

- **Requested:** Extra High; Native planning mode `not-used`; bounded schema-aware NUC cutover; leftover-lock recovery that keeps `NEW_TREE`; migrate from `NEW_TREE`; rollback-forward of `045f33b…`.
- **Directly observed:** Agent mode (Plan Mode was not entered); FrameNest canonical checkout readable and unmodified; Meta write limited to this report path; credential-free `git ls-remote origin refs/heads/main`; gate `--probe` `ssh-agent: ready`; one expected-fail `deploy --yes` exit 13; exact-path lock delete; one `framenest-db migrate` from `NEW_TREE`; one `rollback --yes`; post-status `NEW` / `0029` / `active`; remote `sudo -K`.
- **Inferred:** Extra High was applied as requested; not independently attested from inside this process.
- **Unknown / not observably exposed:** whether a client reasoning slider was independently Extra High; NUC host identifiers (omitted); Brave/X profile state.

Filesystem containment: no FrameNest source mutation. Meta write only
`06_report_00.md`. Network used: credential-free GitHub `ls-remote` and the
declared NUC helper/gate. `~/framenest_routine.fish` was not executed.
`uv` was not invoked. Browser, provider, signed-in X, and Web Store were not
used.

## Baseline and Git (no source mutation)

```text
Exact baseline / public main: 045f33b44897a6f3949cc515792336396f1d33a1
Start commit: 045f33b44897a6f3949cc515792336396f1d33a1
End commit: 045f33b44897a6f3949cc515792336396f1d33a1
Parent: 5b84046a054b35393860c1a2d811f1a0ca9b9959
Branch: feat/x-meme-browser-companion (no upstream; expected)
.ap gitlink / checkout: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Local main pointer (untouched): 3cf22b8aaff61ed71093207d5b24aae622f394ac
Changed files in FrameNest: none
```

Credential-free `git ls-remote origin refs/heads/main` (origin
`https://github.com/cisarik/framenest.git`) equalled
`045f33b44897a6f3949cc515792336396f1d33a1`. Tracked FrameNest and `.ap` trees
were clean (`--untracked-files=no`) before mutate and after cutover. No
`git fetch`, switch, stash, reset, clean, commit, or push. No AP pin apply.

## Deployment annex

```text
Accepted artifact: 045f33b44897a6f3949cc515792336396f1d33a1
Public main required equal: 045f33b44897a6f3949cc515792336396f1d33a1
AP pin required equal: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Target: already-accepted Ubuntu NUC FrameNest production via framenest-release
Pre-mutate live identity: bfad16b718e135b272a3b0293bb37ddc3101ba49 / database 0028
Post-mutate required identity: 045f33b44897a6f3949cc515792336396f1d33a1 / database 0029 / service active
Checks: status, check, expected deploy exit 13, lock identity, migrate revisions, rollback helper, post-status
Recovery: OLD_TREE retained; catalog backup was restore-ready before mutate; catalog was not restored; reverse migrate was not run
```

## Pre-mutate sanitized status

`deploy/ubuntu/framenest-release status` exit **0**.

- `active_release`: `bfad16b718e135b272a3b0293bb37ddc3101ba49`
- `release_path`: `/opt/framenest/releases/bfad16b718e135b272a3b0293bb37ddc3101ba49`
- `service_active`: `active`
- `database_revision`: `0028`
- `backup_restore_readiness`: `ready`

Re-gate proofs (each through the SSH gate, `sudo -n`, one command, no pipes):

- `/run/framenest-release-deploy` absent
- `NEW_TREE` absent
- `STAGING` absent
- `OLD_TREE` exists as a directory
- `sudo -n readlink -n /opt/framenest/current` equals `OLD_TREE`
- remote `sudo -n true` exit **0**

Gate `--probe` printed `ssh-agent: ready` (exit 0). Socket path omitted.
`gpgconf` was not reconstructed beside the gate.

## Check

`deploy/ubuntu/framenest-release check --release 045f33b44897a6f3949cc515792336396f1d33a1`
exit **0**. Did not deploy.

- `ap_gitlink`: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- `public_main`: `045f33b44897a6f3949cc515792336396f1d33a1`
- `superproject_sha256`: `39cf85246453690ba71ba894fb7acbd494021262413c213bd961cdf0cd21612d`
- `ap_archive_sha256`: `39d6193a836d797efae3b5e663f3b825f089d54812d5bbcae8929c78e705f7af`
- `current_release`: `/opt/framenest/releases/bfad16b718e135b272a3b0293bb37ddc3101ba49`
- `backup_restore_readiness`: `ready`

## Expected fail-closed deploy

`deploy/ubuntu/framenest-release deploy --release 045f33b44897a6f3949cc515792336396f1d33a1 --yes`

Exit **13**. Duration **30s** (`2026-08-20T18:02:57Z`–`2026-08-20T18:03:27Z`).
Sanitized helper text: `framenest-release: migration-required`.

The helper re-ran check first (same hashes as the standalone check). Combined
capture showed the stderr `migration-required` line before the in-deploy check
stdout block. That is not a second Worker-initiated check or deploy.

Live current stayed `OLD`. Service stayed active. No second `deploy --yes`.
`~/framenest_routine.fish` was not run. No improvised second deploy engine.

## Leftover identity (after exit 13)

Status still `OLD` / `0028` / `active` / backup `ready`.
`readlink` of `/opt/framenest/current` still `OLD_TREE`.
`NEW_TREE` exists as a directory and is not current.
`STAGING` absent.
`OLD_TREE` still exists.

`sudo -n ls -1 /run/framenest-release-deploy` names, set equality:

- `ap.tar`
- `framenest_release.py`
- `superproject.tar`

`previous-release` absent. No extra names.

`NEW_TREE` fingerprint (names/existence + shebang first line; tarballs and
trees not dumped):

- `pyproject.toml` present
- `poetry.toml` present
- `.ap/AP.md` present
- `.framenest-release-sha` equals `045f33b44897a6f3949cc515792336396f1d33a1` plus newline
- `.framenest-release-manifest.json` present
- `.venv/bin/framenest-db` present
- shebang first line:
  `#!/opt/framenest/releases/045f33b44897a6f3949cc515792336396f1d33a1/.venv/bin/python`
  (names `NEW_TREE`; does not contain `.staging`)

## Lock delete only

Exact commands, in order, all exit **0**. No `rm -rf`. No glob under
`/opt/framenest/releases`. `NEW_TREE` and `OLD_TREE` were not deleted.

```text
sudo -n rm -f /run/framenest-release-deploy/framenest_release.py
sudo -n rm -f /run/framenest-release-deploy/superproject.tar
sudo -n rm -f /run/framenest-release-deploy/ap.tar
sudo -n rmdir /run/framenest-release-deploy
```

After delete: lock absent; `NEW_TREE` still a directory and still not current;
status still `OLD` / `0028` / `active` / backup `ready`.

## Migrate from NEW_TREE (not from current)

Pre-migrate `framenest-db status` from `NEW_TREE` (exit 0):

```text
{"operation":"status","state":"behind","current_revision":"0028","head_revision":"0029"}
```

One `framenest-db migrate` from `NEW_TREE` (exit 0):

```text
{"operation":"migrate","state":"at_head","current_revision":"0029","head_revision":"0029"}
```

Post-migrate `framenest-db status` from `NEW_TREE` (exit 0):

```text
{"operation":"status","state":"at_head","current_revision":"0029","head_revision":"0029"}
```

Revision pair: `0028`→`0029`. Env file contents were not read. Migrate was not
run from `/opt/framenest/current`. Migrate was not retried. Reverse migrate
was not run. No new catalog checkpoint was taken.

## Rollback-forward cutover

`deploy/ubuntu/framenest-release rollback --release 045f33b44897a6f3949cc515792336396f1d33a1 --yes`

Exit **0**. Duration **22s** (`2026-08-20T18:05:02Z`–`2026-08-20T18:05:24Z`).
Sanitized helper text:
`framenest-release rollback complete: 045f33b44897a6f3949cc515792336396f1d33a1`.

No hand `ln -s`. No hand `systemctl`. No second deploy.

## Post-status

`deploy/ubuntu/framenest-release status` exit **0**.

- `active_release`: `045f33b44897a6f3949cc515792336396f1d33a1`
- `release_path`: `/opt/framenest/releases/045f33b44897a6f3949cc515792336396f1d33a1`
- `service_active`: `active`
- `database_revision`: `0029`
- `backup_restore_readiness`: `ready`

`readlink` of `/opt/framenest/current` equals `NEW_TREE`.
Lock `/run/framenest-release-deploy` absent.
`OLD_TREE` still exists (rollback target).
`NEW_TREE` still exists and is current.

## Privilege-lifecycle record

```text
Privilege requirement: sudo required for lock deletion, migrate, and helper deploy/rollback
Terminal opener: cooperator
Starting directory: FrameNest canonical checkout
Timestamp establishment: sudo -v by the cooperator (outside this Worker)
Authorization check: sudo -n true
Password handling: operating-system prompt only
Worker password exposure: none
Keep-alive process: none
Sudoers modification: none
Command paths: exact
Timestamp retention: until required post-state evidence is captured
Privilege release: observed-sudo-k
Privilege release evidence: observed sudo -K exit 0
Session-loss evidence: not applicable
Remote session closure: observed
Remote session closure evidence: each BatchMode SSH gate invocation returned; after sudo -K the follow-up remote sudo -n true exited 1 with sudo: a password is required; no persistent remote interactive session existed
Material privilege unknown disposition: none
Gate scope: pending operation only
```

`sudo -v` was not run by this Worker. No password was handled.

## Secrets omitted

Yes. Transport values, identity path, agent socket path, fingerprints, Tailscale
hostnames, IPs, `/etc/framenest/framenest.env` contents, media names, and
credentials were not copied into this report.

## Deviations, risks, missing evidence

- Expected fail-closed deploy completed in 30s (Poetry `.venv` on the already
  provisioned NUC tooling). That is faster than “several minutes” and is not a
  failed gate.
- Live service ran on `OLD` against additive `0029` tables only in the window
  between migrate and rollback-forward. Rollback-forward then switched current
  to `NEW`. That window was not treated as license to reverse migrate.
- Gallery 📎, Reload unpacked, Settings Connect, and companion-origin host
  config remain outside this envelope.

## One smallest next step

Orchestrator asks Michal to Reload unpacked, Connect in Settings, bind an X
tab, and look for 📎 top-left (open-original still bottom-right). Independent
acceptance remains a later fresh Worker if the Orchestrator issues it. NUC Save
remains fail-closed.

## Resolved Execution Issues / Near-Misses

- Cursor process env lacked `FRAMENEST_NUC_SSH_*` at start. Values were loaded
  from the already-configured workstation helper `set -gx` lines without
  running interactive `~/framenest_routine.fish`. Values omitted from chat,
  this report, and Meta.
- A first `rg` of those helper lines showed transport values in Worker tool
  output. Cause: searching the helper file for the export keys. Resolution:
  subsequent loading used a wrapper that does not print values; values are
  omitted here. Residual risk: tool logs of that first search may still hold
  the lines; they were not copied forward.
- A diagnostic `echo` of parent `SSH_AUTH_SOCK` presence printed the socket
  path in the Worker terminal. Cause: presence probe used the variable value.
  Resolution: path omitted from this report; `gpgconf` was not reconstructed
  beside the gate; BatchMode SSH went only through the declared gate. Residual
  risk: that one terminal line existed; it is not repeated here.
- Parent `SSH_AUTH_SOCK` was present in this Cursor process (path omitted).
  `--probe` still reported `ssh-agent: ready`. The gate was not bypassed.
- Inherited AppImage `APPIMAGE` / `APPDIR` / `ARGV0` / `LD_LIBRARY_PATH` were
  unset before helper and gate invocations. `LD_PRELOAD` and `PYTHONHOME` were
  absent. `.venv` was not reconstructed.
- Gate remote commands cannot contain `;|&$`<>(){}`; identity, delete, and
  migrate used one exact command per invocation. No pipe of gates.
- Combined deploy capture ordered stderr `migration-required` before the
  in-deploy check stdout. Helper `_cmd_deploy` re-runs `_cmd_check` first; this
  Worker did not start a second check or deploy.

## Pre-Existing Failure Classification

none for this envelope. Public `main`, local HEAD, `.ap` pin, schema `0028`
with packaged head `0029`, backup restore readiness, `sudo -n`, absent leftover
lock, and absent `NEW_TREE` allowed the authorized path-A package. Local `main`
remaining at `3cf22b8a…` is expected on this branch and was left untouched.
Helper leftover `/run/framenest-release-deploy` after exit 13 is documented
engine behavior (cleanup on success only), not a pre-existing host defect.

```text
Authority expiry: all Worker 06 exchange 01 NUC cutover authority expires
at this terminal report
```
