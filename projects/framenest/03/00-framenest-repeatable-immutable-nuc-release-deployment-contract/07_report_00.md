### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `07`  
Worker exchange ordinal: `01`  
Standard terminal status: **BLOCKED**  
Phase-qualified result: **not-applicable**  
This session did not implement, correct, accept, or publish `011823a9…`  
Start/end commit (canonical checkout unchanged): `011823a9dcb3d2a51e684fefd5083970f3610701` → `011823a9dcb3d2a51e684fefd5083970f3610701`  
Tree: `2def2abf7fee549821185285c9f19449e256d804`  
Parent: `2d995bb98a8b2c96fa1925f06403b3ee156c6237`  
Changed files: none  
NUC cutover: not performed  
Automatic rollback: did not run  
Publication / production-acceptance-PASS / logical-whole closure: not claimed  
Logical-whole closure: not-closed  
Report justification: `changed-external-state`  
Secrets omitted: yes

**Public-main readback (credential-free).**  
`git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` = `011823a9dcb3d2a51e684fefd5083970f3610701	refs/heads/main`.

**Local HEAD / pin / cleanliness.**  
Branch `feat/repeatable-immutable-nuc-release-deployment-contract` at `011823a9dcb3d2a51e684fefd5083970f3610701`.  
`.ap` gitlink and `.ap` `HEAD` = `17b7e085139e9bcbb0e4953d26aef9b6687d541c`.  
Tracked tree clean. Owner untracked paths preserved. Git write: none.

**Transport.**  
Process env `FRAMENEST_NUC_SSH_*` was unset. Equivalent `--target/--user/--identity` taken from the already-configured operator SSH config Host alias plus its IdentityFile (values omitted). Direct `ssh` with the helper’s BatchMode options required the operator GPG `agent-ssh-socket` (`SSH_AUTH_SOCK`); without it, publickey was denied. The forbidden `framenest_nuc_worker_gate.fish` was not used.

**Helper `status` (mandatory stage; stop).**  
`/home/agile/Projects/framenest/deploy/ubuntu/framenest-release status` exit **20** (`framenest-release: command failed`). No sanitized status block was printed. Cause: `readlink` of `/opt/framenest/current` succeeds, but the engine then `sudo -n cat` of `.framenest-release-manifest.json` on that tree; the file is absent. Staging stopped here. `check` and `deploy --yes` were not invoked.

**Pre-deploy sanitized facts (engine command builders only; not helper `status` output).**  
- `active_release`: `148b6c2012809944262399c1a166e85082606fbf` (`.framenest-release-sha`; current symlink under `/opt/framenest/releases/<that-SHA>`)  
- `service_active`: `active`  
- `database_revision`: `0028` (`at_head`; packaged head also `0028`)  
- `backup_restore_readiness`: `ready`  
- `.framenest-release-manifest.json`: absent on the active tree  
- target dir `/opt/framenest/releases/011823a9dcb3d2a51e684fefd5083970f3610701`: absent  

**Check exit:** not run (stopped at `status`).  
**Privilege probe:** `sudo -n true` exit **0** (same BatchMode transport; after `status` failure, for classification only).  
**Deploy exit / sanitized summary:** not run. No cutover, no lock created, no second deploy, no `rm /run/framenest-release-deploy`.  
**Post-deploy status:** not-applicable.  
**Automatic rollback:** did not run.

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

Remote `sudo -K` exit **0**. Follow-up `sudo -n true` exit **1** (timestamp gone). No password handling.

**One smallest next step:** Do **not** run Gate E smoke. Orchestrator should authorize a separate correction or host-provenance task so routine `framenest-release status` can read a pre-manifest production tree (helper fallback to `.framenest-release-sha`, or an exact bounded marker write). Then issue a fresh Worker deploy of `011823a9…`. This Worker must not correct, deploy, smoke, archive, or close.

### Resolved Execution Issues / Near-Misses

- Cursor Worker shell lacked `SSH_AUTH_SOCK`; GPG agent socket was attached via `gpgconf --list-dirs agent-ssh-socket` (gate-equivalent; gate script not executed).  
- Helper `status` maps the missing-manifest `cat` to opaque EXIT_TRANSPORT `command failed`; classified with the engine’s own read-only remote builders.  
- Untracked owner paths remain; helper `check` would also fail `git status --porcelain`. Not reached.

### Pre-Existing Failure Classification

Active test-NUC release `148b6c2…` predates the ADR-0060 manifest marker. Service is active, schema is same-schema `0028`, backup restore readiness is `ready`, but canonical `status` cannot succeed until the helper accepts `.framenest-release-sha` or the host gains `.framenest-release-manifest.json`. That is a candidate-helper / pre-existing host-provenance gap, not a live cutover failure. Environment: Worker shell transport vars unset; operator SSH config + GPG agent were sufficient once attached.

Authority expiry: all Worker 07 exchange 01 deployment authority expires at this terminal report.