### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `20`  
Worker exchange ordinal: `01`  
Worker session target: `fresh-worker-session`  
Worker session profile: bounded leftover-lock recovery  
Phase: recovery  
Task identity: `FN-NUC-RELEASE-RECOVER-20`

**PASS** | **recovery-PASS**  
deployment-PASS: **not claimed**  
production-acceptance-PASS / Gate E / logical-whole closure: **not claimed**

This chat did not implement, correct, accept, publish, recover Worker 15 leftover, or deploy `2d995bb…`, `011823a9…`, `de580f6f…`, `d963df7…`, or `43c9849…`. Role: WORKER session 20 exchange 01; leftover-path deletion envelope only. No cutover. No `framenest-release check` / `deploy` / `rollback`. No migration. No host manifest write. Live `/opt/framenest/current` remained `148b6c2…`.

**Start/end commit (canonical checkout unchanged):** `43c9849a1ff3449a3c06585571c17439ecff9025` → `43c9849a1ff3449a3c06585571c17439ecff9025`  
**Tree:** `df98c395cc4d88cd8b37a92f854f79a245b0facd`  
**Parent:** `d963df7dfc7d56c75f3696e8bc3830ee81a98534`  
**Changed files:** none  
**NUC cutover:** not performed  
**Git write:** none  
**Secrets omitted:** yes  
**Report justification:** `changed-external-state`  
**Logical-whole closure:** not-closed

**Public-main readback (credential-free).**  
`git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` = `43c9849a1ff3449a3c06585571c17439ecff9025	refs/heads/main`.

**Local HEAD / pin / cleanliness.**  
Branch `feat/repeatable-immutable-nuc-release-deployment-contract` at `43c9849a1ff3449a3c06585571c17439ecff9025`.  
`.ap` gitlink and `.ap` `HEAD` = `17b7e085139e9bcbb0e4953d26aef9b6687d541c`.  
Tracked tree clean. Owner untracked paths preserved. Git write: none.

**Transport.**  
Process env `FRAMENEST_NUC_SSH_*` was unset. Equivalent `--target/--user/--identity` taken from the already-configured operator SSH Host alias plus its IdentityFile (values omitted). Cursor shell lacked `SSH_AUTH_SOCK`; **gpg agent-ssh-socket attached**. BatchMode `ssh … true` exit **0**. Forbidden `framenest_nuc_worker_gate.fish` was not used.

**Pre-recovery sanitized status** (`framenest-release status` exit **0**).  
- `active_release`: `148b6c2012809944262399c1a166e85082606fbf`  
- `release_path`: `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- `release_manifest`: `absent`  
- `service_active`: `active`  
- `database_revision`: `0028`  
- `backup_restore_readiness`: `ready`  

No host manifest was written. No migration.

**Privilege probe.** Remote `sudo -n true` exit **0**.

**Identity evidence (names/existence + one shebang first line).**  
- `sudo -n readlink -n /opt/framenest/current` = `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- `sudo -n ls -1 /run/framenest-release-deploy` = exactly `ap.tar`, `framenest_release.py`, `superproject.tar` (count 3; `previous-release` absent; no extra names)  
- Unpublished `/opt/framenest/releases/d963df7dfc7d56c75f3696e8bc3830ee81a98534` is a directory; not equal to current; path does not end in `.staging`. Fingerprint: `pyproject.toml` present, `poetry.toml` present, `.ap/AP.md` present, `.framenest-release-sha` = `d963df7dfc7d56c75f3696e8bc3830ee81a98534`, `.framenest-release-manifest.json` present, `.venv` present including `framenest-db` / `framenest-backup`.  
- First line of `.venv/bin/framenest-db`:

```text
#!/opt/framenest/releases/d963df7dfc7d56c75f3696e8bc3830ee81a98534.staging/.venv/bin/python
```

- Live `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf` exists as a directory.  
- Absent as required: `d963df7….staging`, `de580f6f….staging`, `de580f6f9d18cddbc4ad7894d163a361b30ef05f`, `43c9849a1ff3449a3c06585571c17439ecff9025`, `43c9849a1ff3449a3c06585571c17439ecff9025.staging`.  
Tarballs were not catted. Trees were not dumped.

**Exact delete commands (paths only).** All remote `sudo -n`; each exit **0**.

```text
sudo -n rm -f /run/framenest-release-deploy/framenest_release.py
sudo -n rm -f /run/framenest-release-deploy/superproject.tar
sudo -n rm -f /run/framenest-release-deploy/ap.tar
sudo -n rmdir /run/framenest-release-deploy
sudo -n rm -rf /opt/framenest/releases/d963df7dfc7d56c75f3696e8bc3830ee81a98534
```

No `rm -rf /run/framenest-release-deploy`. No glob under `/opt/framenest/releases`. No other `rm`. Immediately before the tree delete, `readlink` of current was still `148b6c2…`; the target was not current and did not end in `.staging`. Live `148b6c2…` directory still existed.

**Post-recovery proofs.**  
- `/run/framenest-release-deploy` absent (`test -e` → absent)  
- `/opt/framenest/releases/d963df7dfc7d56c75f3696e8bc3830ee81a98534` absent  
- Live release directory `148b6c2…` still present (`test -d`)  
- `readlink -n /opt/framenest/current` still `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- `d963df7….staging`, `de580f6f…`, `de580f6f….staging`, `43c9849…`, and `43c9849….staging` still absent  

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

**One smallest next step.** Separately authorized deploy of `43c9849a1ff3449a3c06585571c17439ecff9025` (`framenest-release deploy --release 43c9849… --yes`). This Worker must not deploy, check, roll back, smoke, archive, or close.

### Resolved Execution Issues / Near-Misses

- Cursor Worker shell lacked `SSH_AUTH_SOCK`; GPG agent socket was attached via `gpgconf --list-dirs agent-ssh-socket` (gate-equivalent; gate script not executed).  
- Worker 16 leftover claim was re-identified before any delete and matched exactly; Worker 15 leftover (`de580f6f….staging` / final `de580f6f…`) was already absent and was not deleted.  
- Unpublished `d963df7…` was deleted only as leftover recovery material; it was not treated as a rollback target and was never switched onto `/opt/framenest/current`.  
- Meta `20_report_00.md` was not written (no archival grant).

### Pre-Existing Failure Classification

Live test-NUC active tree remains pre-manifest SHA-only `148b6c2…` with service `active`, schema `0028`, and backup restore readiness `ready`. Worker 16 fail-closed lock and unpublished broken `d963df7…` final tree were present at identity time and are now absent. Published `43c9849…` was not deployed. Environment: Worker shell transport vars unset; operator SSH config plus GPG agent were sufficient once attached.

Authority expiry: all Worker 20 exchange 01 recovery authority expires at this terminal report.