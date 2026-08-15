### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `11`  
Worker exchange ordinal: `01`  
Standard terminal status: **PARTIAL**  
Phase-qualified result: **not-applicable**  
deployment-PASS: **not claimed**  
production-acceptance-PASS / Gate E / logical-whole closure: **not claimed**  
This session did not implement, correct, accept, or publish `011823a9…` or `de580f6f…`, and did not perform Worker 07 deployment.  
Start/end commit (canonical checkout unchanged): `de580f6f9d18cddbc4ad7894d163a361b30ef05f` → `de580f6f9d18cddbc4ad7894d163a361b30ef05f`  
Tree: `d958914aeb1952d23d2b6aa7521a92bde14523f2`  
Parent: `011823a9dcb3d2a51e684fefd5083970f3610701`  
Changed files: none  
NUC cutover: not performed  
Automatic rollback: **no** (failure was before cutover; helper rollback path did not run)  
Git write: none  
Secrets omitted: yes  
Report justification: `changed-external-state`  
Logical-whole closure: not-closed

**Public-main readback (credential-free).**  
`git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` = `de580f6f9d18cddbc4ad7894d163a361b30ef05f	refs/heads/main`.

**Local HEAD / pin / cleanliness.**  
Branch `feat/repeatable-immutable-nuc-release-deployment-contract` at `de580f6f9d18cddbc4ad7894d163a361b30ef05f`.  
`.ap` gitlink and `.ap` `HEAD` = `17b7e085139e9bcbb0e4953d26aef9b6687d541c`.  
Tracked tree clean. Owner untracked paths preserved (`.accept-immut-work/`, `.playwright-mcp/`, `.w6-immut-work/`, `REPRO_DIR=/`, `uv.lock`). Git write: none.

**Transport.**  
Process env `FRAMENEST_NUC_SSH_*` was unset at start. Equivalent `--target/--user/--identity` taken from the already-configured operator SSH Host alias plus its IdentityFile (values omitted). Cursor shell lacked `SSH_AUTH_SOCK`; GPG `agent-ssh-socket` attached. BatchMode `ssh … true` exit **0**. Forbidden `framenest_nuc_worker_gate.fish` was not used.

**Pre-deploy sanitized status** (`framenest-release status` exit **0**).  
- `active_release`: `148b6c2012809944262399c1a166e85082606fbf`  
- `release_manifest`: `absent` (pre-manifest SHA-only; accepted)  
- `service_active`: `active`  
- `database_revision`: `0028`  
- `backup_restore_readiness`: `ready`  

Helper status succeeded on the SHA-only tree (DEPLOY-07-F01 fix on `de580f6f…`). No host manifest was written. No migration.

**Check** (`framenest-release check --release de580f6f9d18cddbc4ad7894d163a361b30ef05f` exit **0**). Did not deploy and did not refresh sudo.  
- `ap_gitlink`: `17b7e085139e9bcbb0e4953d26aef9b6687d541c`  
- `public_main`: `de580f6f9d18cddbc4ad7894d163a361b30ef05f`  
- `superproject_sha256`: `2386ed9e563344be9ecdd2277ca35783a92ad1dffc5913e2f797b140c64b25d2`  
- `ap_archive_sha256`: `239573dae6081625e166314c284a3fadb765d4a157d9a831159aea14a3a68c84`  
- `current_release`: `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- `backup_restore_readiness`: `ready`

**Privilege probe.** Remote `sudo -n true` exit **0**.

**Deploy** (`framenest-release deploy --release de580f6f9d18cddbc4ad7894d163a361b30ef05f --yes`).  
Exit **20** (`framenest-release: command failed`). Duration ~19s (`2026-08-15T17:13:38Z`–`17:13:57Z`). Check gates were re-run first (same hashes). Cutover did not occur. Automatic rollback did not run. Lock was not removed. No second deploy. No `rollback --yes`. No `rm /run/framenest-release-deploy`.

**Post-deploy sanitized status** (exit **0**; current tree unchanged).  
- `active_release`: `148b6c2012809944262399c1a166e85082606fbf`  
- `release_manifest`: `absent`  
- `service_active`: `active`  
- `database_revision`: `0028`  
- `backup_restore_readiness`: `ready`  

Previous complete release `148b6c2…` remains `/opt/framenest/current` and remains the live rollback target. Target dir `/opt/framenest/releases/de580f6f9d18cddbc4ad7894d163a361b30ef05f` is absent.

**Leftover recovery state from this deploy (do not delete without a new grant).**  
- `/run/framenest-release-deploy` present, containing `framenest_release.py`, `superproject.tar`, `ap.tar`  
- Remote archive SHA-256 matched the check hashes above  
- `/opt/framenest/releases/de580f6f9d18cddbc4ad7894d163a361b30ef05f.staging` present: superproject extracted (`pyproject.toml` present), `.ap` extracted (`AP.md` present), `poetry.toml` absent, release markers absent, `.venv` absent  
A later `deploy` will fail closed on the existing lock (`EXIT_EXISTS` 9) until that state is separately authorized for recovery.

**Finding FN-NUC-RELEASE-DEPLOY-11-F01.**  
`cmd_remote_write_poetry_toml` embeds `shlex.quote(POETRY_TOML)` inside an already single-quoted `sudo -n sh -c '…'` string. `POETRY_TOML` contains newlines, so `shlex.quote` also uses single quotes. The remote shell therefore splits the command; `poetry.toml` is never written. Local `/tmp` reproduction of the exact engine string exited **127** (`in-project: command not found`) and left `poetry.toml` absent, matching the host staging tree. Helper `subprocess_runner` maps the SSH failure to opaque `EXIT_TRANSPORT` 20 (`command failed`) with stderr discarded.  
Related unreached source pattern: `cmd_remote_write_markers` uses the same nested-quote construction (not executed; markers absent because the poetry.toml write failed first). `cmd_remote_write_file` (stdin `cat`) did transfer the three lock files. This Worker has no correction authority and did not patch the engine.

**Privilege lifecycle**

Privilege requirement: sudo required for deploy  
Terminal opener: cooperator  
Timestamp establishment: sudo -v by the cooperator (outside this Worker)  
Authorization check: sudo -n true  
Password handling: operating-system prompt only  
Worker password exposure: none  
Keep-alive process: none  
Sudoers modification: none  
Privilege release: observed-sudo-k  
Gate scope: pending operation only

Remote `sudo -K` exit **0**. Follow-up `sudo -n true` exit **1** (`sudo: a password is required`). No password handling.

**One smallest next step.** Do **not** run Gate E smoke. Orchestrator should authorize a separate correction of DEPLOY-11-F01 (and the matching marker-write quoting), plus exact bounded recovery of `/run/framenest-release-deploy` and the `de580f6f….staging` tree, then a fresh deploy Worker for `de580f6f…`. This Worker must not correct, retry deploy, roll back, smoke, archive, or close.

### Resolved Execution Issues / Near-Misses

- Cursor Worker shell lacked `SSH_AUTH_SOCK`; GPG agent socket was attached via `gpgconf --list-dirs agent-ssh-socket` (gate-equivalent; gate script not executed).  
- Helper maps the poetry.toml write failure to opaque EXIT_TRANSPORT `command failed`; classified with read-only host probes plus a `/tmp` quoting reproduction of the engine string.  
- Untracked owner paths remain; they did not block `check` (DEPLOY-07-F02).  
- Meta `11_report_00.md` was not written (no archival grant).

### Pre-Existing Failure Classification

Live test-NUC active tree remains pre-manifest SHA-only `148b6c2…` with service `active`, schema `0028`, and backup restore readiness `ready`. Worker 07’s status failure is no longer live on `de580f6f…`. The leftover lock/staging are from this Worker’s single failed deploy, not from Worker 07. Environment: Worker shell transport vars unset; operator SSH config plus GPG agent were sufficient once attached.

Authority expiry: all Worker 11 exchange 01 deployment authority expires at this terminal report.