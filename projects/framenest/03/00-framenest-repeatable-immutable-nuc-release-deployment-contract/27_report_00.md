### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `27`  
Worker exchange ordinal: `01`  
Worker session target: `fresh-worker-session`  
Worker session profile: bounded test-NUC deployment  
Phase: deployment  
Task identity: `FN-NUC-RELEASE-DEPLOY-27`

**PARTIAL** | **deployment-PASS: not claimed**  
production-acceptance-PASS / Gate E / logical-whole closure: **not claimed**

This chat did not implement, correct, accept, publish, recover leftover state, or deploy `2d995bb…`, `011823a9…`, `de580f6f…`, `d963df7…`, or `43c9849…`, and did not perform Worker 26. Role: WORKER session 27 exchange 01. One authorized `deploy --yes` of public SHA `f5fbdce5669997f15c28ed6ffdad4cda849df4ee` was run. Cutover did not persist. Automatic rollback was attempted and reported failed. No second deploy. No `rollback --yes`. No leftover deletion. No migration. No host manifest write. Forbidden `framenest_nuc_worker_gate.fish` was not used.

**Start/end commit (canonical checkout unchanged):** `f5fbdce5669997f15c28ed6ffdad4cda849df4ee` → `f5fbdce5669997f15c28ed6ffdad4cda849df4ee`  
**Tree:** `1d22f690101f9d239207fa80ac89fc473c1c9894`  
**Parent:** `43c9849a1ff3449a3c06585571c17439ecff9025`  
**Changed files:** none  
**NUC cutover:** **did not persist** (live `/opt/framenest/current` remains `148b6c2…`)  
**Automatic rollback:** **yes, attempted; helper reported failed** (`EXIT_ROLLBACK` 18, `framenest-release: rollback failed`)  
**Git write:** none  
**Secrets omitted:** yes  
**Report justification:** `changed-external-state`  
**Logical-whole closure:** not-closed

**Public-main readback (credential-free).**  
`git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` = `f5fbdce5669997f15c28ed6ffdad4cda849df4ee	refs/heads/main`.  
`git ls-remote origin refs/heads/main` matched the same SHA.

**Local HEAD / pin / cleanliness.**  
Branch `feat/repeatable-immutable-nuc-release-deployment-contract` at `f5fbdce5669997f15c28ed6ffdad4cda849df4ee`.  
`.ap` gitlink and `.ap` `HEAD` = `17b7e085139e9bcbb0e4953d26aef9b6687d541c`.  
Tracked tree clean. Owner untracked paths preserved (`.accept-immut-work/`, `.playwright-mcp/`, `.w6-immut-work/`, `REPRO_DIR=/`, `uv.lock`). Git write: none.

**Transport.**  
Process env `FRAMENEST_NUC_SSH_*` was unset at start. Equivalent `--target/--user/--identity` taken from the already-configured operator SSH Host alias plus its IdentityFile (values omitted). Cursor shell lacked `SSH_AUTH_SOCK`; first BatchMode `ssh … true` exit **255** (publickey denied); **gpg agent-ssh-socket attached**; retry exit **0**. Forbidden `framenest_nuc_worker_gate.fish` was not used.

**Pre-deploy sanitized status** (`framenest-release status` exit **0**).  
- `active_release`: `148b6c2012809944262399c1a166e85082606fbf`  
- `release_path`: `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- `release_manifest`: `absent` (pre-manifest SHA-only; accepted)  
- `service_active`: `active`  
- `database_revision`: `0028`  
- `backup_restore_readiness`: `ready`  

No host manifest was written. No migration.

**Pre-deploy leftover probes (existence only; not deleted).**  
- `/run/framenest-release-deploy`: **absent**  
- `43c9849…` / `43c9849….staging`: **absent**  
- `f5fbdce….staging`: **absent**  
- `f5fbdce…` final: **absent**  
- live `148b6c2…` directory: **present**  
- `readlink` current: `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`

**Check** (`framenest-release check --release f5fbdce5669997f15c28ed6ffdad4cda849df4ee` exit **0**). Did not deploy and did not refresh sudo.  
- `ap_gitlink`: `17b7e085139e9bcbb0e4953d26aef9b6687d541c`  
- `public_main`: `f5fbdce5669997f15c28ed6ffdad4cda849df4ee`  
- `superproject_sha256`: `38a789232fec1329fec3b9a5ab1a67714e9fedbdc57415c483c77ed02ed1ac84`  
- `ap_archive_sha256`: `239573dae6081625e166314c284a3fadb765d4a157d9a831159aea14a3a68c84`  
- `current_release`: `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- `backup_restore_readiness`: `ready`

**Privilege probe.** Remote `sudo -n true` exit **0**.

**Deploy** (`framenest-release deploy --release f5fbdce5669997f15c28ed6ffdad4cda849df4ee --yes`).  
Exit **18** (`EXIT_ROLLBACK`, `framenest-release: rollback failed`). Duration **37s** (`2026-08-15T20:29:45Z`–`20:30:22Z`). Check gates were re-run first (same hashes as check). Helper reached post-checkpoint `previous-release` capture, then reported automatic rollback failed. Live current did not remain on `f5fbdce…`. Brief atomic switch is **not independently proven** (helper stderr discarded). No second deploy. No chained `rollback --yes`. Lock was not removed.

**Post-deploy sanitized status** (exit **0**).  
- `active_release`: `148b6c2012809944262399c1a166e85082606fbf`  
- `release_path`: `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- `release_manifest`: `absent`  
- `service_active`: `active`  
- `database_revision`: `0028`  
- `backup_restore_readiness`: `ready`  

Previous complete release `148b6c2…` remains `/opt/framenest/current` and remains the live rollback target.

**Live shebang first line** (`/opt/framenest/current/.venv/bin/framenest-db`):

```text
#!/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf/.venv/bin/python
```

Does **not** name `.staging`. Does **not** name the `f5fbdce…` interpreter (cutover not live).

**Live `.pth` / `direct_url.json` leftover-`.staging`:** **no**  
Bounded find only under `/opt/framenest/current/.venv`:  
`lib/python3.13/site-packages/framenest.pth` and `lib/python3.13/site-packages/framenest-0.1.0.dist-info/direct_url.json`. Neither contains `.staging`. No `find /opt/framenest/releases`. File bodies were not dumped. Unpublished `f5fbdce…` `.pth` / shebang were not read (not in the live-current grant).

**Leftover recovery state from this deploy (do not delete without a new grant).**  
- `/run/framenest-release-deploy` **present**; `ls -1` = exactly `ap.tar`, `framenest_release.py`, `previous-release`, `superproject.tar` (count 4).  
- `previous-release` contents: `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- Staging `/opt/framenest/releases/f5fbdce….staging` **absent**.  
- Final `/opt/framenest/releases/f5fbdce5669997f15c28ed6ffdad4cda849df4ee` **present** (not current; path does not end in `.staging`). Fingerprint: `pyproject.toml` present, `poetry.toml` present, `.ap/AP.md` present, `.framenest-release-sha` = `f5fbdce5669997f15c28ed6ffdad4cda849df4ee`, `.framenest-release-manifest.json` present, `.venv` present including `framenest-db` / `framenest-backup`.  
- `43c9849…` / `.staging` still absent. Live `148b6c2…` directory still present.  

A later `deploy` will fail closed on the existing lock (`EXIT_EXISTS` 9) until that state is separately authorized for recovery. The unpublished `f5fbdce…` final tree is leftover recovery material; do not treat it as a rollback target.

**Finding FN-NUC-RELEASE-DEPLOY-27-F01.**  
Helper completed archive transfer / staging publish far enough to write `previous-release` (so same-schema `framenest-db status` and the fresh catalog checkpoint ran). The cutover `try` then failed; automatic `_rollback` ran and raised opaque `rollback failed` (`EXIT_ROLLBACK` 18). Live service afterward is still `148b6c2…` `active`, schema `0028`, backup `ready`. Inner causal SSH/systemd/health/log failure was discarded by `subprocess_runner`. This Worker has no correction authority and did not patch, retry deploy, run a second rollback, or delete leftover state. Pre-checkpoint `db status` succeeding is **not** a live-venv `.pth` proof for unpublished `f5fbdce…`.

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

Remote `sudo -K` exit **0**. Follow-up `sudo -n true` exit **1** (`sudo: a password is required`; 29-byte stderr classified without dumping the host line). No password handling. `sudo -v` was not run by this Worker.

**One smallest next step.** Do **not** run Gate E smoke. Orchestrator should authorize exact bounded recovery of `/run/framenest-release-deploy` and the unpublished `/opt/framenest/releases/f5fbdce5669997f15c28ed6ffdad4cda849df4ee` tree, plus diagnosis of `EXIT_ROLLBACK` 18 (helper stderr is opaque), then a **fresh** deploy Worker for `f5fbdce…`. This Worker must not correct, retry deploy, roll back, delete leftover, smoke, archive, or close.

### Resolved Execution Issues / Near-Misses

- Cursor Worker shell lacked `SSH_AUTH_SOCK`; first BatchMode publickey failed; GPG `agent-ssh-socket` was attached and BatchMode then exited 0 (gate-equivalent; gate script not executed).  
- Helper maps the post-checkpoint cutover/rollback failure to opaque `rollback failed` with stderr discarded; classified from exit 18, `previous-release` presence, live status, and leftover path existence only.  
- Untracked owner paths remain; they did not block `check` (DEPLOY-07-F02).  
- Worker 26 invalid remote `sudo -n` did not recur after Cooperator timestamp re-establishment.  
- Worker 21 leftover lock/`43c9849…` were absent at pre-deploy probe; leftover state after this attempt is new from this deploy.  
- Live `.pth` / `direct_url.json` under current `148b6c2…` do not contain `.staging`; unpublished `f5fbdce…` editable metadata was not probed.  
- Meta `27_report_00.md` was not written (no archival grant).

### Pre-Existing Failure Classification

Live test-NUC active tree remains pre-manifest SHA-only `148b6c2…` with service `active`, schema `0028`, and backup restore readiness `ready`. Worker 25 leftover lock/unpublished `43c9849…` were not present at the start of this session. Worker 26 sudo-timestamp failure was not present after Cooperator `sudo -v`. Candidate `f5fbdce…` was prepared into an unpublished final tree and left a lock including `previous-release`; it is not current. Environment: operator SSH config plus GPG agent were sufficient once attached.

Authority expiry: all Worker 27 exchange 01 deployment authority expires at this terminal report.