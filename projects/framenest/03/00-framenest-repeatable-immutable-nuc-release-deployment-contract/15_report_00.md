### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `15`  
Worker exchange ordinal: `01`  
Worker session target: `fresh-worker-session`  
Worker session profile: bounded leftover-lock recovery  
Phase: recovery  
Task identity: `FN-NUC-RELEASE-RECOVER-15`

**PASS** | **recovery-PASS**  
deployment-PASS: **not claimed**  
production-acceptance-PASS / Gate E / logical-whole closure: **not claimed**

This chat did not implement, correct, accept, publish, or deploy `2d995bb…`, `011823a9…`, `de580f6f…`, or `d963df7…`. Role: WORKER session 15 exchange 01; leftover-path deletion envelope only. No cutover. No `framenest-release check` / `deploy` / `rollback`. No migration. No host manifest write.

**Start/end commit (canonical checkout unchanged):** `d963df7dfc7d56c75f3696e8bc3830ee81a98534` → `d963df7dfc7d56c75f3696e8bc3830ee81a98534`  
**Tree:** `44c35046150ee1b7783f9233f4497431d64c9f17`  
**Parent:** `de580f6f9d18cddbc4ad7894d163a361b30ef05f`  
**Changed files:** none  
**NUC cutover:** not performed  
**Git write:** none  
**Secrets omitted:** yes  
**Report justification:** `changed-external-state`  
**Logical-whole closure:** not-closed

**Public-main readback (credential-free).**  
`git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` = `d963df7dfc7d56c75f3696e8bc3830ee81a98534	refs/heads/main`.

**Local HEAD / pin / cleanliness.**  
Branch `feat/repeatable-immutable-nuc-release-deployment-contract` at `d963df7dfc7d56c75f3696e8bc3830ee81a98534`.  
`.ap` gitlink and `.ap` `HEAD` = `17b7e085139e9bcbb0e4953d26aef9b6687d541c`.  
Tracked tree clean. Owner untracked paths preserved. Git write: none.

**Transport.**  
Process env `FRAMENEST_NUC_SSH_*` was unset. Equivalent `--target/--user/--identity` taken from the already-configured operator SSH Host alias plus its IdentityFile (values omitted). Cursor shell lacked `SSH_AUTH_SOCK`; **gpg agent-ssh-socket attached**. BatchMode `ssh … true` exit **0** after attach. Forbidden `framenest_nuc_worker_gate.fish` was not used.

**Pre-recovery sanitized status** (`framenest-release status` exit **0**).  
- `active_release`: `148b6c2012809944262399c1a166e85082606fbf`  
- `release_path`: `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- `release_manifest`: `absent`  
- `service_active`: `active`  
- `database_revision`: `0028`  
- `backup_restore_readiness`: `ready`  

No host manifest was written. No migration.

**Privilege probe.** Remote `sudo -n true` exit **0**.

**Identity evidence (names/existence only).**  
- `sudo -n readlink -n /opt/framenest/current` = `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- `sudo -n ls -1 /run/framenest-release-deploy` = exactly `ap.tar`, `framenest_release.py`, `superproject.tar` (count 3; no extra names)  
- Staging `/opt/framenest/releases/de580f6f9d18cddbc4ad7894d163a361b30ef05f.staging` is a directory; path ends in `.staging` and is not current. Fingerprint: `pyproject.toml` present, `.ap/AP.md` present, `poetry.toml` absent, `.framenest-release-sha` absent, `.framenest-release-manifest.json` absent, `.venv` absent.  
- Final `/opt/framenest/releases/de580f6f9d18cddbc4ad7894d163a361b30ef05f` absent.  
- Final `/opt/framenest/releases/d963df7dfc7d56c75f3696e8bc3830ee81a98534` absent.  
- Final `/opt/framenest/releases/d963df7dfc7d56c75f3696e8bc3830ee81a98534.staging` absent.  
- Live `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf` exists as a directory.  
Tarballs were not catted. Trees were not dumped.

**Exact delete commands (paths only).** All remote `sudo -n`; each exit **0**.

```text
sudo -n rm -f /run/framenest-release-deploy/framenest_release.py
sudo -n rm -f /run/framenest-release-deploy/superproject.tar
sudo -n rm -f /run/framenest-release-deploy/ap.tar
sudo -n rmdir /run/framenest-release-deploy
sudo -n rm -rf /opt/framenest/releases/de580f6f9d18cddbc4ad7894d163a361b30ef05f.staging
```

No `rm -rf /run/framenest-release-deploy`. No glob under `/opt/framenest/releases`. No other `rm`. Staging path still ended in `.staging` and was not current immediately before delete. Live current remained `148b6c2…` immediately before delete.

**Post-recovery proofs.**  
- `/run/framenest-release-deploy` absent (`test -e` exit **1**)  
- `/opt/framenest/releases/de580f6f9d18cddbc4ad7894d163a361b30ef05f.staging` absent (`test -e` exit **1**)  
- Live release directory `148b6c2…` still present (`test -d` exit **0**)  
- `readlink -n /opt/framenest/current` still `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf`  
- Final `de580f6f…`, `d963df7…`, and `d963df7….staging` still absent  

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

**One smallest next step.** Separately authorized deploy of `d963df7dfc7d56c75f3696e8bc3830ee81a98534` (not this Worker). Do not run Gate E smoke in this session. This Worker must not deploy, roll back, archive, or close.

### Resolved Execution Issues / Near-Misses

- Cursor Worker shell lacked `SSH_AUTH_SOCK`; first BatchMode publickey attempt failed; GPG `agent-ssh-socket` was attached and BatchMode then exited 0. Gate script was not executed. The failed SSH line contained a host identifier in the Worker tool log; it is omitted here.  
- Local script issued `rm -f` of `/run/framenest-release-deploy/framenest_release.py` twice; both exited 0; no extra path.  
- First probe of the three final-dir absences used a colon-delimited loop that locally hit AppImage `command not found` (exit 127) and was discarded; explicit-path re-probe showed all three absent before any delete.  
- Meta `15_report_00.md` was not written (no archival grant).

### Pre-Existing Failure Classification

Live test-NUC active tree remains pre-manifest SHA-only `148b6c2…` with service `active`, schema `0028`, and backup restore readiness `ready`. Worker 11 leftover lock and incomplete `de580f6f….staging` were re-identified and removed; they are no longer present. Published `d963df7…` was not deployed. Environment: Worker shell transport vars unset; operator SSH config plus GPG agent were sufficient once attached.

Authority expiry: all Worker 15 exchange 01 leftover-deletion authority expires at this terminal report.