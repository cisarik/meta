# FrameNest NUC ChatGPT analyze provider — S3 page-runtime preflight and first operator login

## Identity and route

Persistent role identity: WORKER
Logical whole identity: framenest-nuc-chatgpt-analyze-provider
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session profile: Fresh Evidence Probe
Phase: Preflight
Task identity: FRAMENEST-NUC-CHATGPT-ANALYZE-PROVIDER-S3
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: live browser and account interaction on the NUC, a background wizard process, credentials typed only by the Cooperator, and CAPTCHA/quota stops.
Recommended context capacity: approximately 250k tokens

## Fresh-session routing

- This is a new concrete Worker session. It inherits no prior authority; establish every repository, host, and capability fact independently.
- Independence is not claimed and not required.
- Native planning mode must be OFF. If it is ON, stop `BLOCKED` before any action.
- Prior authority expired at the terminal deployment report `03_report_00.md` (session 03, exchange 01).

## Cooperator preconditions (before pasting)

1. The household ChatGPT credentials are available to the Cooperator for the wizard step; they are never typed into chat, the Worker shell, or any file.
2. The Cooperator can reach the NUC over his normal SSH route from the MacBook and can keep an SSH local port-forward open during the login.
3. On the NUC, outside this Worker: `sudo -v`, then `sudo -n true`. The Worker must never run `sudo -v` or handle a password.
4. `FRAMENEST_NUC_SSH_TARGET`, `FRAMENEST_NUC_SSH_USER`, and `FRAMENEST_NUC_SSH_IDENTITY` must be exported in the environment that launches this Worker session. Never paste their values into chat. Do not run or scrape `~/framenest_routine.fish`.

## Starting state (verified at issuance)

- Public `main` and `origin/feat/chatgpt-page-ask-kernel` both equal `26d28b16c08a5e7e0179a32c16646bfdc1009c81`; the NUC deployment report records live `current` at the same SHA, service active, database `0033`, backup ready.
- Governing AP gitlink and detached `.ap` HEAD: `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- Node and Chromium availability on the NUC, the release entry point, and the kernel state directories are unverified. This exchange resolves them.
- No page-provider state exists on the NUC yet: no `/var/lib/framenest/chatgpt-page/`, no `/run/framenest/chatgpt-page/`, no Chromium profile.

## Authority record

Probe authority: explicit for the read-only checks and the bounded state setup below.
Durable state authority: explicit and limited to creating `/var/lib/framenest/chatgpt-page/` and `/run/framenest/chatgpt-page/` and the first household login profile inside the first path.
Implementation authority: none. Git authority: none (report write only). Provider authority: none — no ask, no bridge job, no upload.
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline / release SHA: `26d28b16c08a5e7e0179a32c16646bfdc1009c81`
Independence required: no

## Goal

Resolve the NUC page-runtime prerequisites and complete the first operator login
through the deployed wizard, producing sanitized locator and transport evidence:
Node present at the required baseline, a usable Chromium binary, the release
entry point working, the two kernel state directories created with the planned
ownership, a logged-in household profile, and the wizard's post-login metrics
showing the composer locator matched and no login wall. No composer typing, no
upload, no ask, no service start.

## Required reading

- `AGENTS.md` (NUC Routine Release Update; Cursor Worker Execution Boundary; security boundaries).
- `docs/WORKER_EXECUTION_CONTRACT.md` (SSH gate, sudo lifecycle, GUI/shell safety).
- `docs/UBUNTU_NUC_DEPLOYMENT.md` (operator command execution contract; §6–§8).
- `docs/OPERATOR_NETWORK.md`.
- `.ap/AP.md` (Worker spine; RF-06, RF-11, RF-13, RF-18), `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md`.
- Trace `00_handout.md` §6; `01_orchestrator_synthesis.md` D10 and the S3 row; `03_report_00.md`.
- Vendored kernel sources you must understand before running them:
  `vendor/kronika-ask/src/kronika/cli.py` (`login` command),
  `vendor/kronika-ask/src/kronika/_assets/extension/src/headless/probe.mjs`,
  `.../headless/login_server.mjs`, `.../headless/driver.mjs`,
  `.../adapters/pack_v5.json`.

## Execution route and sanitization

- Bounded NUC commands go through
  `scripts/operator/network/framenest_nuc_worker_gate.fish`. It performs its own BatchMode SSH. Do not reconstruct `gpgconf`, do not print `SSH_AUTH_SOCK`, and do not print transport values.
- The only release entry point used is
  `/opt/framenest/current/.venv/bin/framenest-chatgpt-page` under the operator command contract
  (`sudo -n -u framenest --chdir=/opt/framenest/current env FRAMENEST_ENV_FILE=/etc/framenest/framenest.env ...`).
  Do not call ambient `python`, `python3`, `poetry`, or `uv`.
- Sanitize all evidence: no credentials, tokens, cookies, wizard URL or secret path, account details, hostnames, sockets, identity paths, or browser-profile contents. The wizard's own sanitized JSON fields may be recorded as listed below.
- Never read, copy, or inspect the Chromium profile, cookies, or credential stores. The only login evidence is the wizard's printed JSON result.

## Stages (stop at the first failure)

1. **Repository and public-state gate (read-only).** Verify FrameNest HEAD and
   public `main` equal `26d28b1…`; clean index and worktree; `.ap` gitlink and
   detached HEAD equal `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`. Then
   `deploy/ubuntu/framenest-release status` (read-only) and require
   `active_release` `26d28b1…`, `service_active` active, `database_revision`
   `0033`, `backup_restore_readiness` `ready`. If the transport variables are
   unset, stop `PARTIAL` after the gate `--probe`.
2. **NUC page-runtime preflight (read-only).** Through the gate:
   - Node: verify that plain `node` resolves and reports its version **as the
     service account under the same operator command contract the wizard will
     use** (the CLI spawns plain `node`). Require a Node runtime meeting the
     copied runner's APIs with Node 22 as the minimum planned baseline. If Node
     is missing or below the baseline, stop `PARTIAL`; bootstrap is a separate
     grant.
   - The Chromium candidates the vendored driver accepts
     (`/usr/bin/chromium`, `/usr/bin/chromium-browser`,
     `/usr/bin/ungoogled-chromium`, and any driver default): record the first
     present executable and its `--version`. If none exists, stop `PARTIAL`.
   - The release entry point: `test -x
     /opt/framenest/current/.venv/bin/framenest-chatgpt-page`, then run it with
     `--version` and `--help` as the service account. Require exit 0.
   - Packaged assets: confirm the installed package contains
     `kronika/_assets/extension/src/headless/probe.mjs`,
     `.../headless/login_server.mjs`, and `.../adapters/pack_v5.json` under
     `/opt/framenest/current/.venv/lib/python3.13/site-packages/`. Record the
     installed `pack_v5.json` SHA-256 as the pack identity for later budget
     profiles.
   - Directory state: `/var/lib/framenest` and `/run/framenest` exist;
     `/var/lib/framenest/chatgpt-page` and `/run/framenest/chatgpt-page` are
     absent. Record sanitized `df` capacity for `/opt/framenest`.
   - Confirm no `node`, `chromium`, or `chrome` process is already running
     before the probe.
3. **Bounded state setup.** Create only `/var/lib/framenest/chatgpt-page`
   (mode `0700`, owner `framenest:framenest`) and `/run/framenest/chatgpt-page`
   (mode `0750`, owner `framenest:framenest`). Create nothing else; do not
   install units, edit the environment file, or change any other host object.
4. **First operator login through the wizard.** Start exactly:
   `.../framenest-chatgpt-page --state-dir /var/lib/framenest/chatgpt-page login`
   as the service account, detached from the SSH session (`setsid`/`nohup`),
   with stdout/stderr captured to
   `/run/framenest/chatgpt-page/login-probe.out` (mode `0600`, owner
   `framenest`). The profile directory is the command's default
   `<state-dir>/chromium-profile`; do not pass a different profile.
   - Poll that file until the wizard URL appears; print the URL once to the
     Cooperator (it carries a per-session secret path and must never be written
     into the report). Wait up to 900 seconds for completion.
   - The Cooperator, from the MacBook, opens an SSH local port-forward to the
     wizard port and completes the login in a browser: email, password, and any
     one-time code; a CAPTCHA is handled by the Cooperator in the wizard view.
     The Worker never types, sees, or stores a credential.
   - Stop `PARTIAL` if the Cooperator cannot complete the login (challenge,
     quota, account lock, or unknown state). Do not retry with a different
     transport, browser, or account. Do not scrape cookies or the profile.
5. **Evidence capture and cleanup.** Read the wizard's final JSON result and
   require: `ok: true`; `composer.present: true` with a recorded strategy;
   `login_wall.present: false`; a chat URL path; a bounded title. Record
   `engine_binary`, `listener` port only, `duration_seconds`, and the pack
   identity from stage 2. Immediately delete
   `/run/framenest/chatgpt-page/login-probe.out` and confirm it is absent.
   Record the profile directory name only (not its contents).
6. **Stop.** No composer typing, no attachment, no ask, no bridge run, no
   service start, no release change, no provider call.

## Negative authority

No repository changes (only the report file), no Git write, no publication, no
deployment, no package installation, no environment-file or unit change, no
`/etc` or systemd mutation, no firewall/Tailscale/SSH configuration change, no
wildcard deletion, no reading or copying of browser-profile or credential
stores, no provider or ChatGPT ask, no upload, no Node/Chromium process beyond
the single wizard run, no subagents, native planning, or Max, no closure
signal.

## Stopping conditions

Stop and report honestly if: the repository or public-state gate diverges; the
transport variables are unset; `status` is not the expected release; Node or
Chromium is missing or below the baseline; the release entry point or packaged
assets are missing; the state directories already exist in an unexpected form;
the wizard cannot start, its URL never appears, or the Cooperator cannot
complete the login; the post-login metrics show a login wall or a missing
composer; a secret or credential appears in output; or any stage would require
prohibited action. A prerequisite failure grants no new effect and no residual
investigation.

## Completion and report contract

Finalize the complete report first, then deliver it to
`/home/agile/meta/projects/framenest/13/00-framenest-nuc-chatgpt-analyze-provider/04_report_00.md`
if and only if that file is absent, and read back its full content. No
directory creation is granted; the verified parent must already exist. This
exact write is the sole file-write exception outside the repository.

Begin the report exactly with:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo these coordinates once: logical whole identity, Worker session ordinal,
Worker exchange ordinal (`04` / `01`). Include: status (`PASS`, `PARTIAL`, or
`BLOCKED`); `Phase-qualified result: not-applicable`; start and end commit
`26d28b16c08a5e7e0179a32c16646bfdc1009c81`; changed files (`04_report_00.md`
only; no repository or product files); the sanitized preflight results (Node
path and version, Chromium path and version, entry point result, installed pack
SHA-256, capacity); the created state directories with modes; the sanitized
wizard result fields (`ok`, `composer.present` and strategy, `login_wall`,
URL path, bounded title or omitted, `engine_binary`, port, duration); the
login-probe output file deletion confirmation; the confirmation that no
credential, cookie, URL, or profile content was read or recorded; deviations
and risks; one smallest next step; exactly one report justification
(`changed-external-state`); `Logical-whole closure: not-closed`; the
Orchestration critique (`MEASURED:` / `LEAD:`), `Resolved Execution Issues /
Near-Misses`, `Pre-Existing Failure Classification: none`, an abbreviated
capability recheck, and the authority-expiry statement. Do not claim
`production-acceptance-PASS`; the composer file-input check and any upload
remain later slices.

PASS means the preflight passed, both state directories exist as specified, the
household login completed, and the wizard reported the composer present with no
login wall. PARTIAL covers a missing Node/Chromium baseline, an incomplete
login, or an SSH/transport limitation. BLOCKED covers a diverged gate or
prohibited state. Do not overwrite an existing report, create a placeholder, or
use another output path. The Cooperator archives the exact prompt and report
pair after the report exists; you have no Git archival authority for the trace.

Authority expiry: this terminal report ends the grant. Stop after it; the next
slice needs a new complete authoritative prompt.
