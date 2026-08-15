# FrameNest test-NUC routine immutable release deploy (de580f6f)
You are one fresh WORKER instance under Analytic Programming.
You are not the ORCHESTRATOR. Do not re-implement, re-accept, publish, mutate
Meta or AP, change source, run migrations, write forged host manifests, or
close this logical whole. Do not perform Gate E three-identity smoke or claim
production-acceptance-PASS.
If this chat implemented, corrected, accepted, or published 011823a9… or
de580f6f…, or performed Worker 07 deployment, stop BLOCKED.
```text
Persistent role identity: WORKER
Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 11
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: bounded test-NUC deployment
Phase: deployment
Task identity: FN-NUC-RELEASE-DEPLOY-11
Native planning mode: not-used
Implementation authority: explicit for the staged deploy envelope only
Publication authority: none
Correction authority: none
Independence required: no
Evidence posture: non-independent
Recommended reasoning: High
Recommendation basis: live sudo/systemd/release/backup/schema/rollback on Michal's test NUC after published pre-manifest-status fix
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
Rollback or recovery checkpoint: engine fresh verified catalog checkpoint before cutover; automatic bounded rollback on post-switch failure; do not invent a second rollback
Activated stricter profile: none
Activated annex: deployment + privilege lifecycle.

Frozen artifact
Accepted public commit: de580f6f9d18cddbc4ad7894d163a361b30ef05f
Accepted tree: d958914aeb1952d23d2b6aa7521a92bde14523f2
Accepted parent: 011823a9dcb3d2a51e684fefd5083970f3610701
Required public refs/heads/main: de580f6f9d18cddbc4ad7894d163a361b30ef05f
Required AP pin: 17b7e085139e9bcbb0e4953d26aef9b6687d541c
Packaged schema head: 0028
Entry point: /home/agile/Projects/framenest/deploy/ubuntu/framenest-release
Exact NUC Poetry: /opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry
Exact NUC CPython: /opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13
Worker 07 observed (stale until re-read by status): active release 148b6c2012809944262399c1a166e85082606fbf, manifest absent, service active, schema 0028, backup restore readiness ready. Re-read from framenest-release status. Do not forge .framenest-release-manifest.json on that immutable tree.

Continuity from Worker 07 (authority for this exchange, not proof)
Helper status must succeed on SHA-only trees (DEPLOY-07-F01 fix is in de580f6f…).
Local ?? owner untracked must not block check (DEPLOY-07-F02).
Cursor shells may lack SSH_AUTH_SOCK; attach the operator GPG agent-ssh-socket via gpgconf --list-dirs agent-ssh-socket if BatchMode publickey fails. Do not run framenest_nuc_worker_gate.fish.
Process env FRAMENEST_NUC_SSH_* may be unset; use already-configured operator SSH Host alias / IdentityFile equivalents as
--target/--user/ --identity
. Never print those values.
Protocol and trace
Canonical repository identity: https://github.com/cisarik/ap.git Immutable version identity: 17b7e085139e9bcbb0e4953d26aef9b6687d541c Declared variant: stable Governing variants in effect: one Rules from non-governing variants: none Migration required: no

External trace disposition: configured Trace discovery: /home/agile/meta/projects/framenest/03/00-framenest-repeatable-immutable-nuc-release-deployment-contract/ Trace project key: framenest Trace logical-whole projection identity: 00-framenest-repeatable-immutable-nuc-release-deployment-contract Trace authority: historical-evidence-only Trace archival owner: Cooperator Michal; Worker must not archive Trace visibility: private Trace companion outcome: report Trace self-granted status: none Expected later archival pair after the report exists: 11_deployment_00.md + 11_report_00.md

Communication
Orchestrator-to-Worker prompt language: professional English Formal Worker report language: professional English Required report header: ### Report for ORCHESTRATOR_CHAT If sudo -n is invalid, stop; do not run sudo -v or handle a password. Logical-whole closure: not-closed

Repository identities
Working directory: /home/agile/Projects/framenest
Expected branch: feat/repeatable-immutable-nuc-release-deployment-contract
Expected HEAD: de580f6f9d18cddbc4ad7894d163a361b30ef05f
Local HEAD must equal the release SHA. Preserve untracked owner paths. Git write: none.

Mandatory reading
AGENTS.md, WORKER_EXECUTION_CONTRACT.md, UBUNTU_NUC_DEPLOYMENT.md (Routine Immutable Release Update), ADR-0060, .ap/AP.md, .ap/AP_WORKER.md, Worker 07 report as prior host claim only.

Goal
Deploy exact public SHA de580f6f… onto the test NUC: status → check → sudo -n probe → deploy --yes → status → sudo -K. deployment-PASS only if post-status shows that SHA, service active, schema 0028, backup restore readiness ready. Automatic engine rollback on post-switch failure is in-scope; improvised second rollback is not.

Authorized stages (stop at first failure)
Sanitize AppImage/LD_LIBRARY_PATH/PYTHONHOME. No pipe of gates through tail/grep. Timeouts long enough for remote poetry install.

Credential-free git ls-remote https://github.com/cisarik/framenest.git refs/heads/main equals de580f6f9d18cddbc4ad7894d163a361b30ef05f. Local HEAD and .ap pin match. Tracked tree clean (untracked may exist).
Ensure BatchMode SSH works (attach SSH_AUTH_SOCK from gpg agent-ssh-socket if needed). Do not print socket paths in the report beyond “gpg agent-ssh-socket attached” / “not needed”.
framenest-release status — must exit 0. Record sanitized active_release, release_manifest (present|absent), service_active, database_revision, backup_restore_readiness. Expect schema 0028 and restore_readiness ready. Pre-manifest SHA-only is OK. If not ready or schema ≠ 0028, stop. Do not migrate. Do not write a host manifest.
framenest-release check --release de580f6f9d18cddbc4ad7894d163a361b30ef05f — exit 0. Must not deploy or refresh sudo.
Remote sudo -n true exit 0. If fail, stop PARTIAL/BLOCKED; do not sudo -v.
Only after 1–5: framenest-release deploy --release de580f6f9d18cddbc4ad7894d163a361b30ef05f --yes
framenest-release status again. Require active_release de580f6f…, preferably release_manifest: present (new release writes both markers), service active, database_revision 0028, backup_restore_readiness ready. Previous complete release must remain as rollback target.
Remote sudo -K; record exit; confirm follow-up sudo -n true fails. Stop.
If deploy fails after cutover, trust the helper’s automatic rollback and report distinct exits. Do not rm /run/framenest-release-deploy. Prefer stop + report over a chained manual rollback --yes.

Positive authority
read-only Git/ls-remote; helper BatchMode SSH; status/check/one deploy --yes/post status; remote sudo -n as the helper does + terminal sudo -K; temp logs under fresh /tmp only.

Negative authority
No source/docs/test/lock/.ap edits; no Git write; no uv/host pip/ operator poetry install except what the helper does for the release .venv; no framenest-db migrate; no forged .framenest-release-manifest.json on 148b6c2… or any old tree; no /srv/media writes; no disk/firewall/Tailscale/ Mullvad/account/router mutation; no credential edits; no browser; no provider; no three-user smoke; no Meta archive; no closure; no second deploy; no wildcard deletion; no framenest_nuc_worker_gate.fish.

Terminal report
Begin:

### Report for ORCHESTRATOR_CHAT
Echo logical whole identity, session 11, exchange 01. Include: PASS | PARTIAL | BLOCKED; deployment-PASS | not-applicable; public-main readback; local HEAD; pre-deploy sanitized status; check exit; privilege probe; deploy exit/summary; post-deploy status; automatic rollback yes/no; privilege-release record; secrets omitted; next step = Gate E smoke (not closure); changed-external-state; Logical-whole closure: not-closed; Near-Misses; Pre-Existing Failure Classification; authority expiry.

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
PASS / deployment-PASS only if public SHA, check, deploy, and post-status all confirm de580f6f… active, schema 0028, service active, backup ready, and privilege release is honest. Do not claim production-acceptance-PASS or closure.

Authority expires at the terminal report.