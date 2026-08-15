### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `21`  
Worker exchange ordinal: `01`  
Worker session target: `fresh-worker-session`  
Worker session profile: bounded test-NUC deployment  
Phase: deployment  
Task identity: `FN-NUC-RELEASE-DEPLOY-21`

**PARTIAL** | **deployment-PASS: not claimed**  
production-acceptance-PASS / Gate E / logical-whole closure: **not claimed**

This chat did not implement, correct, accept, publish, or recover leftover state for `2d995bb…`, `011823a9…`, `de580f6f…`, or `d963df7…`. It performed one authorized `deploy --yes` of public SHA `43c9849a1ff3449a3c06585571c17439ecff9025`. Cutover did not occur. Automatic rollback did not run.

**Start/end commit (canonical checkout unchanged):** `43c9849a1ff3449a3c06585571c17439ecff9025` → `43c9849a1ff3449a3c06585571c17439ecff9025`  
**Tree:** `df98c395cc4d88cd8b37a92f854f79a245b0facd`  
**Parent:** `d963df7dfc7d56c75f3696e8bc3830ee81a98534`  
**Changed files:** none  
**NUC cutover:** not performed  
**Automatic rollback:** **no** (failure after staging→final rename and before previous-release capture / cutover; helper rollback path did not run)  
**Git write:** none  
**Secrets omitted:** yes  
**Report justification:** `changed-external-state`  
**Logical-whole closure:** not-closed

**Public-main readback (credential-free).**  
`git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` = `43c9849a1ff3449a3c06585571c17439ecff9025	refs/heads/main`.

**Local HEAD / pin / cleanliness.**  
Branch `feat/repeatable-immutable-nuc-release-deployment-contract` at `43c9849a1ff3449a3c06585571c17439ecff9025`.  
`.ap` gitlink and `.ap` `HEAD` = `17b7e085139e9bcbb0e4953d26aef9b6687d541c`.  
Tracked tree clean. Owner untracked paths preserved (`.accept-immut-work/`, `.playwright-mcp/`, `.w6-immut-work/`, `REPRO_DIR=/`, `uv.lock`). Git write: none.

**Transport.**  
Process env `FRAMENEST_NUC_SSH_*` was unset at start. Equivalent `--target/--user/--identity` taken from the already-configured operator SSH Host alias plus its IdentityFile (values omitted). Cursor shell lacked `SSH_AUTH_SOCK`; **gpg agent-ssh-socket attached**. BatchMode `ssh … true` exit **0**. Forbidden `framenest_nuc_worker_gate.fish` was not used.

**Pre-deploy sanitized status** (`framenest-release status` exit **0**).  
- `active_release`: `148b6c2012809944262399c1a166e85082606fbf`  
- `release_path`: `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- `release_manifest`: `absent` (pre-manifest SHA-only; accepted)  
- `service_active`: `active`  
- `database_revision`: `0028`  
- `backup_restore_readiness`: `ready`  

No host manifest was written. No migration. Pre-deploy leftover probes: `/run/framenest-release-deploy` absent, `d963df7…` absent, `d963df7….staging` absent, `de580f6f…` / `.staging` absent, `43c9849…` / `.staging` absent. Current symlink was `148b6c2…`.

**Check** (`framenest-release check --release 43c9849a1ff3449a3c06585571c17439ecff9025` exit **0**). Did not deploy and did not refresh sudo.  
- `ap_gitlink`: `17b7e085139e9bcbb0e4953d26aef9b6687d541c`  
- `public_main`: `43c9849a1ff3449a3c06585571c17439ecff9025`  
- `superproject_sha256`: `de8238c42d326ebe50ac148e4afdda9f9e0cdb29d5615b77e9635a0796f6c7cf`  
- `ap_archive_sha256`: `239573dae6081625e166314c284a3fadb765d4a157d9a831159aea14a3a68c84`  
- `current_release`: `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- `backup_restore_readiness`: `ready`

**Privilege probe.** Remote `sudo -n true` exit **0**.

**Deploy** (`framenest-release deploy --release 43c9849a1ff3449a3c06585571c17439ecff9025 --yes`).  
Exit **20** (`framenest-release: command failed`). Duration 30s (`2026-08-15T19:10:20Z`–`19:10:50Z`). Check gates were re-run first (same hashes). Cutover did not occur. Automatic rollback did not run. Lock was not removed. No second deploy. No `rollback --yes`. No `rm /run/framenest-release-deploy`. No deletion of the unpublished `43c9849…` tree.

**Post-deploy sanitized status** (exit **0**; live current unchanged).  
- `active_release`: `148b6c2012809944262399c1a166e85082606fbf`  
- `release_path`: `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- `release_manifest`: `absent`  
- `service_active`: `active`  
- `database_revision`: `0028`  
- `backup_restore_readiness`: `ready`  

Previous complete release `148b6c2…` remains `/opt/framenest/current` and remains the live rollback target.

**Live shebang first line** (`/opt/framenest/current/.venv/bin/framenest-db`, still the pre-cutover tree):

```text
#!/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf/.venv/bin/python
```

Equivalent unpublished `43c9849…` `framenest-db` first line (DEPLOY-16-F01 did **not** recur):

```text
#!/opt/framenest/releases/43c9849a1ff3449a3c06585571c17439ecff9025/.venv/bin/python
```

Staging interpreter path is absent (`test -e` on `43c9849….staging/.venv/bin/python` → absent). Final `.venv/bin/python` is present and is a symlink to the exact tooling CPython.

**Leftover recovery state from this deploy (do not delete without a new grant).**  
- `/run/framenest-release-deploy` present; `ls -1` = exactly `ap.tar`, `framenest_release.py`, `superproject.tar` (count 3). `previous-release` absent.  
- Remote archive SHA-256 matched the check hashes above.  
- Staging `/opt/framenest/releases/43c9849….staging` absent.  
- Final `/opt/framenest/releases/43c9849a1ff3449a3c06585571c17439ecff9025` **present** (staging was renamed). Fingerprint: `pyproject.toml` present, `poetry.toml` present, `.ap/AP.md` present, `.framenest-release-sha` = `43c9849a1ff3449a3c06585571c17439ecff9025`, `.framenest-release-manifest.json` present, `.venv` present including `framenest-db` / `framenest-backup`.  
- `d963df7…` / `.staging` and `de580f6f…` / `.staging` still absent. Live `148b6c2…` directory still present.  

A later `deploy` will fail closed on the existing lock (`EXIT_EXISTS` 9) until that state is separately authorized for recovery. The unpublished `43c9849…` final tree is leftover recovery material; do not treat it as a rollback target.

**Finding FN-NUC-RELEASE-DEPLOY-21-F01.**  
Venv console-script shebangs were relocated off the staging prefix before chmod (DEPLOY-16-F01). Poetry still installed FrameNest as an editable checkout against the staging tree. After `mv` staging→final, `framenest.pth` still names the vanished staging `src`, and `direct_url.json` still records `file:///opt/framenest/releases/43c9849….staging` with `"editable": true`. Same-session helper-equivalent `framenest-db status` as the service account against the unpublished tree exited **1**:

```text
ModuleNotFoundError: No module named 'framenest'
```

Helper `subprocess_runner` maps that SSH failure to opaque `EXIT_TRANSPORT` 20 (`command failed`) with stderr discarded. Failure is after atomic publish and before checkpoint / previous-release capture / cutover. This Worker has no correction authority and did not patch the engine, retry deploy, or delete leftover state.

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

Remote `sudo -K` exit **0**. Follow-up `sudo -n true` exit **1** (`sudo: a password is required`). No password handling. `sudo -v` was not run by this Worker.

**One smallest next step.** Do **not** run Gate E smoke. Orchestrator should authorize a separate correction of DEPLOY-21-F01 (Poetry editable install / `.pth` baked to the staging path, then broken by `mv` to the final release directory), plus exact bounded recovery of `/run/framenest-release-deploy` and the unpublished `/opt/framenest/releases/43c9849a1ff3449a3c06585571c17439ecff9025` tree, then a fresh deploy Worker for `43c9849…`. This Worker must not correct, retry deploy, roll back, smoke, archive, or close.

### Resolved Execution Issues / Near-Misses

- Cursor Worker shell lacked `SSH_AUTH_SOCK`; GPG agent socket was attached via `gpgconf --list-dirs agent-ssh-socket` (gate-equivalent; gate script not executed).  
- Helper maps the post-rename `framenest-db` import failure to opaque EXIT_TRANSPORT `command failed`; classified with read-only named-file probes, shebang `head -n 1`, `.pth` / `direct_url.json` reads, and a service-account `framenest-db status` (no backup/checkpoint re-run).  
- Untracked owner paths remain; they did not block `check` (DEPLOY-07-F02).  
- DEPLOY-16-F01 (staging shebang) did not recur on this SHA.  
- Worker 16 leftover lock/`d963df7…` were absent at pre-deploy probe; leftover state after this attempt is new from this deploy.  
- Meta `21_report_00.md` was not written (no archival grant).

### Pre-Existing Failure Classification

Live test-NUC active tree remains pre-manifest SHA-only `148b6c2…` with service `active`, schema `0028`, and backup restore readiness `ready`. Worker 16 leftover lock/unpublished `d963df7…` were not present at the start of this session. Published `43c9849…` was prepared and renamed to the final release directory but is not current; console scripts name the final interpreter, but the editable `.pth` still points at the vanished staging `src`, so `framenest` is not importable. Environment: Worker shell transport vars unset; operator SSH config plus GPG agent were sufficient once attached.

Authority expiry: all Worker 21 exchange 01 deployment authority expires at this terminal report.