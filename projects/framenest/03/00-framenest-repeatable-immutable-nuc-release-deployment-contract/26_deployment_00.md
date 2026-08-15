# FrameNest test-NUC routine immutable release deploy (f5fbdce)
You are one fresh WORKER instance under Analytic Programming.
You are not the ORCHESTRATOR. Do not re-implement, re-accept, publish, mutate
Meta or AP, change source, run migrations, write forged host markers, delete
leftover lock/unpublished trees, or close this logical whole. Do not perform
Gate E three-identity smoke or claim production-acceptance-PASS.
If this chat implemented, corrected, accepted, published, recovered leftover
state, or deployed 2d995bb…, 011823a9…, de580f6f…, d963df7…, 43c9849…, or
f5fbdce…, stop BLOCKED.
```text
Persistent role identity: WORKER
Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 26
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: bounded test-NUC deployment
Phase: deployment
Task identity: FN-NUC-RELEASE-DEPLOY-26
Native planning mode: not-used
Implementation authority: explicit for the staged deploy envelope only
Publication authority: none
Correction authority: none
Independence required: no
Evidence posture: non-independent
Recommended reasoning: High
Recommendation basis: live sudo/systemd/release/backup/schema/rollback on Michal's test NUC after published editable-venv-path relocation and leftover-lock recovery
Automatic model selection: off
Enhanced/maximum mode: not requested
Sub-agents/internal delegation: not-used
Worker topology: single-active
Material phase gate: yes
Changed material axis: production-external-service-credential-or-account-boundary
Ordinary-only trigger: no
Routing reopened for: production-external-service-credential-or-account-boundary
Unchanged axes reopened: none
Evidence tier: E3
Evidence tier basis: privileged remote host mutation, service restart, catalog checkpoint, atomic current-symlink switch, automatic rollback
Combined implementation envelope: allowed
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: engine fresh verified catalog checkpoint before cutover; automatic bounded rollback on post-switch failure; do not invent a second rollback; do not delete a new leftover lock
Activated stricter profile: none
Activated annex: deployment + privilege lifecycle.
Frozen artifact
Accepted public commit: f5fbdce5669997f15c28ed6ffdad4cda849df4ee Accepted tree: 1d22f690101f9d239207fa80ac89fc473c1c9894 Accepted parent: 43c9849a1ff3449a3c06585571c17439ecff9025 Required public refs/heads/main: f5fbdce5669997f15c28ed6ffdad4cda849df4ee Required AP pin: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Packaged schema head: 0028 Entry point: /home/agile/Projects/framenest/deploy/ubuntu/framenest-release Exact NUC Poetry: /opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry Exact NUC CPython: /opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13

Worker 25 observed (stale until re-read): active release 148b6c2012809944262399c1a166e85082606fbf, manifest absent, service active, schema 0028, backup restore readiness ready; leftover /run/framenest-release-deploy and unpublished 43c9849… removed. Re-read from framenest-release status. Do not forge .framenest-release-manifest.json on that immutable tree. If the lock dir, 43c9849…, 43c9849….staging, or f5fbdce….staging is present before deploy, stop BLOCKED; do not delete.

Continuity (authority for this exchange, not proof)
Helper status must succeed on SHA-only trees (DEPLOY-07-F01). Local ?? owner untracked must not block check (DEPLOY-07-F02). Remote poetry.toml and markers use stdin cat (DEPLOY-11-F01/F02). Venv console-script shebangs are relocated off the staging prefix before chmod (DEPLOY-16-F01). Editable .pth / direct_url.json staging prefixes are relocated in the same pass (DEPLOY-21-F01). After a successful cutover:

live /opt/framenest/current/.venv/bin/framenest-db first line must name /opt/framenest/releases/f5fbdce5669997f15c28ed6ffdad4cda849df4ee/.venv/bin/python (not a .staging path);
no .pth or direct_url.json under that live .venv may contain .staging. Cursor shells may lack SSH_AUTH_SOCK; attach GPG
gpgconf --list-dirs agent-ssh-socket
if BatchMode publickey fails. Do not run framenest_nuc_worker_gate.fish. Process env FRAMENEST_NUC_SSH_* may be unset; use already-configured operator SSH Host alias / IdentityFile as --target/--user/--identity. Never print those values.
Protocol and trace
Canonical repository identity: https://github.com/cisarik/ap.git Immutable version identity: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Declared variant: stable Governing variants in effect: one Rules from non-governing variants: none Migration required: no

External trace disposition: configured Trace discovery: /home/agile/meta/projects/framenest/03/00-framenest-repeatable-immutable-nuc-release-deployment-contract/ Trace project key: framenest Trace logical-whole projection identity: 00-framenest-repeatable-immutable-nuc-release-deployment-contract Trace authority: historical-evidence-only Trace archival owner: Cooperator Michal; Worker must not archive Trace visibility: private Trace companion outcome: report Trace self-granted status: none Expected later archival pair after the report exists: 26_deployment_00.md + 26_report_00.md

Communication
Orchestrator-to-Worker prompt language: professional English Formal Worker report language: professional English Required report header: ### Report for ORCHESTRATOR_CHAT If sudo -n is invalid, stop; do not run sudo -v or handle a password. Logical-whole closure: not-closed

Repository identities
Working directory: /home/agile/Projects/framenest Expected branch: feat/repeatable-immutable-nuc-release-deployment-contract Expected HEAD: f5fbdce5669997f15c28ed6ffdad4cda849df4ee Local HEAD must equal the release SHA. Preserve untracked owner paths. Git write: none.

Mandatory reading
AGENTS.md, WORKER_EXECUTION_CONTRACT.md, UBUNTU_NUC_DEPLOYMENT.md (Routine Immutable Release Update), ADR-0060, .ap/AP.md, .ap/AP_WORKER.md, Worker 21 as prior failed-deploy claim, Worker 25 as leftover-recovery claim only.

Goal
Deploy exact public SHA f5fbdce… onto the test NUC: status → check → sudo -n probe → deploy --yes → status → live shebang + .pth/direct_url.json probes → sudo -K. deployment-PASS only if post-status shows that SHA, release_manifest: present, service active, schema 0028, backup restore readiness ready, the live shebang names the final release interpreter, and live editable metadata does not name .staging. Automatic engine rollback on post-switch failure is in-scope; improvised second rollback is not. Leftover-lock deletion is out of scope.

Authorized stages (stop at first failure)
Sanitize AppImage LD_LIBRARY_PATH/PYTHONHOME. No pipe of gates through tail/grep. Timeouts long enough for remote poetry install.

Credential-free git ls-remote https://github.com/cisarik/framenest.git refs/heads/main equals f5fbdce…. Local HEAD and .ap pin match. Tracked tree clean (untracked may exist).
Ensure BatchMode SSH works (attach SSH_AUTH_SOCK from gpg agent-ssh-socket if needed). Do not print socket paths beyond “gpg agent-ssh-socket attached” / “not needed”.
framenest-release status — must exit 0. Record sanitized active_release, release_manifest (present|absent), service_active, database_revision, backup_restore_readiness. Expect schema 0028 and restore_readiness ready. Pre-manifest SHA-only current tree is OK. If not ready or schema ≠ 0028, stop. Do not migrate. Do not write a host manifest.
framenest-release check --release f5fbdce5669997f15c28ed6ffdad4cda849df4ee — exit 0. Must not deploy or refresh sudo.
Remote sudo -n true exit 0. If fail, stop PARTIAL/BLOCKED; do not sudo -v.
Only after 1–5: framenest-release deploy --release f5fbdce5669997f15c28ed6ffdad4cda849df4ee --yes
framenest-release status again. Require active_release f5fbdce…, release_manifest: present, service active, database_revision 0028, backup_restore_readiness ready. Previous complete release 148b6c2… must remain as rollback target.
Read-only first line of /opt/framenest/current/.venv/bin/framenest-db. It must be #!/opt/framenest/releases/f5fbdce5669997f15c28ed6ffdad4cda849df4ee/.venv/bin/python. If it still names .staging, stop PARTIAL; do not patch, do not retry, do not delete the new tree.
Bounded name search only under /opt/framenest/current/.venv (-name '*.pth' -o -name 'direct_url.json'). Those files must not contain .staging. Do not find /opt/framenest/releases. Do not dump trees. If .staging remains, stop PARTIAL; do not patch, do not retry, do not delete.
Remote sudo -K; record exit; confirm follow-up sudo -n true fails. Stop.
If deploy exits EXIT_EXISTS 9 (existing remote lock or recovery state), stop BLOCKED. Do not rm /run/framenest-release-deploy or any release/staging tree. If deploy fails before cutover, do not delete leftover recovery material. If deploy fails after cutover, trust the helper’s automatic rollback and report distinct exits. Prefer stop + report over a chained manual rollback --yes. No second deploy.

Positive authority
read-only Git/ls-remote; helper BatchMode SSH; status/check/one deploy --yes/ post status; one shebang first-line read of the live framenest-db; bounded .pth/direct_url.json reads under live .venv only; remote sudo -n as the helper does + terminal sudo -K; temp logs under fresh /tmp only.

Negative authority
No source/docs/test/lock/.ap edits; no Git write; no uv/host pip/operator poetry install except what the helper does for the release .venv; no framenest-db migrate; no forged .framenest-release-manifest.json on 148b6c2… or any old tree; no /srv/media writes; no disk/firewall/Tailscale/ Mullvad/account/router mutation; no credential edits; no browser; no provider; no three-user smoke; no Meta archive; no closure; no second deploy; no wildcard deletion; no leftover-lock recovery; no framenest_nuc_worker_gate.fish.

Terminal report
Begin:

### Report for ORCHESTRATOR_CHAT
Echo logical whole identity, session 26, exchange 01. Include: PASS | PARTIAL | BLOCKED; deployment-PASS | not-applicable; production-acceptance-PASS not claimed; public-main readback; local HEAD; pre-deploy sanitized status; check exit; privilege probe; deploy exit/summary (duration, whether cutover occurred); post-deploy status; live shebang first line; live .pth/direct_url.json leftover-.staging yes/no; automatic rollback yes/no; leftover lock/staging present or absent after this attempt; privilege-release record; secrets omitted; next step = Gate E smoke (not closure); report justification changed-external-state;
Logical-whole closure: not-closed
; Near-Misses; Pre-Existing Failure Classification; authority expiry.

Also echo:

Privilege requirement: sudo required for deploy
Terminal opener: cooperator
Timestamp establishment: sudo -v by the cooperator (outside this Worker)
Authorization check: sudo -n true
Password handling: operating-system prompt only
Worker password exposure: none
Keep-alive process: none
Sudoers modification: none
Privilege release: <observed-sudo-k | unknown-session-lost>
Gate scope: pending operation only
PASS / deployment-PASS only if public SHA, check, deploy, and post-status all confirm f5fbdce… active with release_manifest: present, schema 0028, service active, backup ready, previous 148b6c2… still present as rollback target, live framenest-db shebang names the final release interpreter, live .pth / direct_url.json do not contain .staging, and privilege release is honest. Do not claim production-acceptance-PASS or closure.

Authority expires at the terminal report.