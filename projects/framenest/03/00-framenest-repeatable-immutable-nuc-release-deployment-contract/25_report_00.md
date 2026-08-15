### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `25`  
Worker exchange ordinal: `01`  
Worker session target: `fresh-worker-session`  
Worker session profile: bounded leftover-lock recovery  
Phase: recovery  
Task identity: `FN-NUC-RELEASE-RECOVER-25`

**PASS** | **recovery-PASS**  
deployment-PASS: **not claimed**  
production-acceptance-PASS / Gate E / logical-whole closure: **not claimed**

This chat did not implement, correct, accept, publish, recover Worker 15 or Worker 20 leftover, or deploy `2d995bb…`, `011823a9…`, `de580f6f…`, `d963df7…`, `43c9849…`, or `f5fbdce…`. Role: WORKER session 25 exchange 01; leftover-path deletion envelope only. No cutover. No `framenest-release check` / `deploy` / `rollback`. No migration. No host manifest write. Live `/opt/framenest/current` remained `148b6c2…`. Unpublished `43c9849…` was not switched to current and is not a rollback target.

**Start/end commit (canonical checkout unchanged):** `f5fbdce5669997f15c28ed6ffdad4cda849df4ee` → `f5fbdce5669997f15c28ed6ffdad4cda849df4ee`  
**Tree:** `1d22f690101f9d239207fa80ac89fc473c1c9894`  
**Parent:** `43c9849a1ff3449a3c06585571c17439ecff9025`  
**Changed files:** none  
**NUC cutover:** not performed  
**Git write:** none  
**Secrets omitted:** yes  
**Report justification:** `changed-external-state`  
**Logical-whole closure:** not-closed

**Public-main readback (credential-free).**  
`git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` = `f5fbdce5669997f15c28ed6ffdad4cda849df4ee	refs/heads/main`.

**Local HEAD / pin / cleanliness.**  
Branch `feat/repeatable-immutable-nuc-release-deployment-contract` at `f5fbdce5669997f15c28ed6ffdad4cda849df4ee`.  
`.ap` gitlink and `.ap` `HEAD` = `17b7e085139e9bcbb0e4953d26aef9b6687d541c`.  
Tracked tree clean. Owner untracked paths preserved (`.accept-immut-work/`, `.playwright-mcp/`, `.w6-immut-work/`, `REPRO_DIR=/`, `uv.lock`). Git write: none.

**Transport.**  
Equivalent `--target/--user/--identity` taken from the already-configured operator SSH Host alias plus its IdentityFile (values omitted). Cursor shell lacked `SSH_AUTH_SOCK`; **gpg agent-ssh-socket attached**. BatchMode `ssh … true` exit **0** after attach. Forbidden `framenest_nuc_worker_gate.fish` was not used.

**Pre-recovery sanitized status** (`framenest-release status` exit **0**).  
- `active_release`: `148b6c2012809944262399c1a166e85082606fbf`  
- `release_path`: `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- `release_manifest`: `absent`  
- `service_active`: `active`  
- `database_revision`: `0028`  
- `backup_restore_readiness`: `ready`  

No host manifest was written. No migration.

**Privilege probe.** Remote `sudo -n true` exit **0**.

**Identity evidence (names/existence + shebang first line + `.pth`/`direct_url.json` leftover `.staging` only).**  
- `sudo -n readlink -n /opt/framenest/current` = `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- `sudo -n ls -1 /run/framenest-release-deploy` = exactly `ap.tar`, `framenest_release.py`, `superproject.tar` (count 3; `previous-release` absent; no extra names)  
- Unpublished `/opt/framenest/releases/43c9849a1ff3449a3c06585571c17439ecff9025` is a directory; not equal to current; path does not end in `.staging`. Fingerprint: `pyproject.toml` present, `poetry.toml` present, `.ap/AP.md` present, `.framenest-release-sha` = `43c9849a1ff3449a3c06585571c17439ecff9025`, `.framenest-release-manifest.json` present, `.venv` present including `framenest-db` / `framenest-backup`.  
- First line of `.venv/bin/framenest-db` (DEPLOY-16-F01 did **not** recur):

```text
#!/opt/framenest/releases/43c9849a1ff3449a3c06585571c17439ecff9025/.venv/bin/python
```

- Bounded name search only under that unpublished `.venv` (`-name '*.pth' -o -name 'direct_url.json'`):  
  `lib/python3.13/site-packages/framenest.pth` and `lib/python3.13/site-packages/framenest-0.1.0.dist-info/direct_url.json` both contain `.staging` (DEPLOY-21-F01 leftover). No `find /opt/framenest/releases`. File bodies were not dumped.  
- Live `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf` exists as a directory.  
- Absent as required: `43c9849….staging`, `d963df7…`, `d963df7….staging`, `de580f6f…`, `de580f6f….staging`, `f5fbdce5669997f15c28ed6ffdad4cda849df4ee`, `f5fbdce5669997f15c28ed6ffdad4cda849df4ee.staging`.  
Tarballs were not catted. Trees were not dumped.

**Exact delete commands (paths only).** All remote `sudo -n`; each exit **0**.

```text
sudo -n rm -f /run/framenest-release-deploy/framenest_release.py
sudo -n rm -f /run/framenest-release-deploy/superproject.tar
sudo -n rm -f /run/framenest-release-deploy/ap.tar
sudo -n rmdir /run/framenest-release-deploy
sudo -n rm -rf /opt/framenest/releases/43c9849a1ff3449a3c06585571c17439ecff9025
```

No `rm -rf /run/framenest-release-deploy`. No glob under `/opt/framenest/releases`. No other `rm`. Immediately before the tree delete, `readlink` of current was still `148b6c2…`; the target was not current and did not end in `.staging`. Live `148b6c2…` directory still existed.

**Post-recovery proofs.**  
- `/run/framenest-release-deploy` absent (`test -e` → absent)  
- `/opt/framenest/releases/43c9849a1ff3449a3c06585571c17439ecff9025` absent  
- Live release directory `148b6c2…` still present (`test -d`)  
- `readlink -n /opt/framenest/current` still `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`

**Post-recovery sanitized status** (`framenest-release status` exit **0**).  
- `active_release`: `148b6c2012809944262399c1a166e85082606fbf`  
- `release_path`: `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- `release_manifest`: `absent`  
- `service_active`: `active`  
- `database_revision`: `0028`  
- `backup_restore_readiness`: `ready`  

**Privilege lifecycle**

Privilege requirement: sudo required for leftover deletion  
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

**One smallest next step.** Separately authorized deploy of public SHA `f5fbdce5669997f15c28ed6ffdad4cda849df4ee` (`framenest-release deploy --release f5fbdce5669997f15c28ed6ffdad4cda849df4ee --yes`). This Worker must not deploy, smoke, archive, or close.

### Resolved Execution Issues / Near-Misses

- Cursor Worker shell lacked `SSH_AUTH_SOCK`; GPG agent socket was attached via `gpgconf --list-dirs agent-ssh-socket` (gate-equivalent; gate script not executed).  
- First unpublished `.framenest-release-sha` read used an unprivileged redirect and got `Permission denied`; identity was re-read with `sudo -n head -n 1` before any delete and matched `43c9849a1ff3449a3c06585571c17439ecff9025`.  
- Untracked owner paths remain; they did not block recovery.  
- Meta `25_report_00.md` was not written (no archival grant).

### Pre-Existing Failure Classification

Live test-NUC active tree remains pre-manifest SHA-only `148b6c2…` with service `active`, schema `0028`, and backup restore readiness `ready`. Worker 21 leftover lock and unpublished broken `43c9849…` final tree (DEPLOY-21-F01 `.pth` / `direct_url.json` still naming vanished `.staging`) were present at identity and are now absent. Environment: operator SSH config plus GPG agent were sufficient once attached.

Authority expiry: all Worker 25 exchange 01 leftover-deletion authority expires at this terminal report.