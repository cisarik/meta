# FrameNest NUC ChatGPT analyze provider — publication and minimal-kernel deployment

## Identity and route

Persistent role identity: WORKER
Logical whole identity: framenest-nuc-chatgpt-analyze-provider
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session profile: Bounded NUC Deployment
Phase: deployment
Task identity: FRAMENEST-NUC-CHATGPT-ANALYZE-PROVIDER-DEPLOY
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: privileged remote host mutation with a possible schema jump and Cooperator sudo lifecycle.
Recommended context capacity: approximately 250k tokens

## Fresh-session routing

- This is a new concrete Worker session. It inherits no prior authority; verify every repository, host, and gate fact independently from current evidence.
- Independence is not claimed and not required. This is a deployment task, not acceptance.
- Native planning mode must be OFF. If it is ON, stop `BLOCKED` before any action.
- Prior authority expired at the terminal S2 report `02_report_01.md` (session 02, exchange 02). No earlier grant is live.

## Cooperator preconditions (before pasting)

1. On the NUC, outside this Worker: `sudo -v`, then `sudo -n true` to confirm the timestamp. The Worker must never run `sudo -v` or handle a password.
2. In the environment that launches this Worker session, `FRAMENEST_NUC_SSH_TARGET`, `FRAMENEST_NUC_SSH_USER`, and `FRAMENEST_NUC_SSH_IDENTITY` must be exported. Never paste their values into chat. Do not run or scrape `~/framenest_routine.fish`.
3. Keep an operator fish session that inherits the SSH agent available in case the release helper needs `SSH_AUTH_SOCK`.

## Starting state (verified at issuance)

- FrameNest HEAD `26d28b16c08a5e7e0179a32c16646bfdc1009c81` on `feat/chatgpt-page-ask-kernel`, clean index and worktree; `origin/feat/chatgpt-page-ask-kernel` equals it; `origin/main` is still `7ff6546f345827d6df20bd5b13d5e57cb4bc90db`; local `main` (`d8629e33a4755406f8bb1bfec565ac6a3f4fb67e`) is an ancestor of the candidate.
- S1 commit `0fd21b989814b7c0b78d517996812750a823ff10` and S2 commit `26d28b1…` are accepted; the vendored stripped kernel and the offline probe tooling are in the branch.
- Governing AP gitlink and detached `.ap` HEAD: `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- Packaged Alembic head at the candidate: `0033`.
- NUC current release, database revision, and backup restore-readiness are unknown until `framenest-release status` runs. Do not guess them.

## Authority record

Deployment authority: explicit for the staged envelope in "Stages" below.
Publication authority: explicit and limited to the fast-forward publication of `main` to `26d28b16c08a5e7e0179a32c16646bfdc1009c81` in stage 2. No other Git write.
Implementation authority: none for product source.
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline / release SHA: `26d28b16c08a5e7e0179a32c16646bfdc1009c81`
Independence required: no

## Goal

Public `main` equals `26d28b1…`, and live NUC `current` equals
`/opt/framenest/releases/26d28b16c08a5e7e0179a32c16646bfdc1009c81` with
`framenest.service` active, database revision `0033`, backup
`restore_readiness: ready`, the vendored kernel present in the release, the
previous complete release retained as the rollback target, and the page
provider still unregistered and unselected. No schema migration beyond the
documented `migration-required` annex, no provider or browser activity, no
service-unit installation, no environment-file edit.

## Required reading

- `AGENTS.md` (NUC Routine Release Update; Cursor Worker Execution Boundary; UI/UX acceptance gate).
- `docs/WORKER_EXECUTION_CONTRACT.md` (SSH gate, sudo lifecycle, canonical routes).
- `docs/UBUNTU_NUC_DEPLOYMENT.md` (Routine Immutable Release Update; §5 `migration-required` annex; §6–§8 readiness).
- `docs/OPERATOR_NETWORK.md`; `docs/NUC_HOST_BASELINE.md`.
- `docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md`; `docs/adr/0075-nuc-development-test-target-and-routine-release-refresh.md`.
- `.ap/AP.md` (Worker spine; RF-12, RF-13, RF-18), `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md` (report header and coordinates).
- Trace `00_handout.md` §6; `01_orchestrator_synthesis.md` D10–D11; `02_report_00.md` and `02_report_01.md`.

## Execution route and sanitization

- The only authorized host-mutation entry point is
  `deploy/ubuntu/framenest-release`. Its wrapper invokes the engine through the
  repository `.venv/bin/python` internally; that internal use is authorized for
  this entry point only. Do not call ambient `python`, `python3`, `poetry run`,
  or `uv` for anything else. This task runs no pytest.
- Bounded remote commands go through
  `scripts/operator/network/framenest_nuc_worker_gate.fish`. It performs its
  own BatchMode SSH. Do not reconstruct `gpgconf`, do not print
  `SSH_AUTH_SOCK`, and do not print transport values.
- Allow generous timeouts for `deploy` (remote `poetry install` is included);
  do not truncate outputs through pipes that could hide exit codes.
- Sanitize all evidence: no credentials, tokens, cookies, keys, sockets,
  hostnames, private network values, identity paths, or paths below approved
  generic roots. Approved release paths under `/opt/framenest/` may be named.

## Stages (stop at the first failure)

1. **Repository gate.** `git -C /home/agile/Projects/framenest` HEAD equals
   `26d28b1…`, branch `feat/chatgpt-page-ask-kernel`, clean index and worktree;
   `.ap` gitlink and detached HEAD equal
   `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`; credential-free
   `git ls-remote https://github.com/cisarik/framenest.git refs/heads/feat/chatgpt-page-ask-kernel`
   equals `26d28b1…`. Stop `BLOCKED` on any divergence.
2. **Publication (the only Git write).** From the clean checkout:
   `git switch main`; `git merge --ff-only feat/chatgpt-page-ask-kernel`;
   `git push origin main` (non-force). Then verify
   `git ls-remote https://github.com/cisarik/framenest.git refs/heads/main`
   equals `26d28b16c08a5e7e0179a32c16646bfdc1009c81`. Switch back to
   `feat/chatgpt-page-ask-kernel` so HEAD is again the release SHA. No force,
   no tags, no other branch, no `main` rewrite. If the push is impossible, stop
   `PARTIAL`; do not improvise credentials or alternate remotes.
3. **SSH capability and transport.** Run
   `scripts/operator/network/framenest_nuc_worker_gate.fish --probe`. Expect
   `ssh-agent: ready` or `ssh-agent: absent`. Check only whether the three
   `FRAMENEST_NUC_SSH_*` variables are set, without printing values. If any is
   unset, stop `PARTIAL` after the probe and ask the Cooperator to export them
   into this Worker environment outside chat. Then run
   `deploy/ubuntu/framenest-release status` and require exit 0. Record the
   sanitized `active_release`, `release_path`, `service_active`,
   `database_revision`, `backup_restore_readiness`, and whether the manifest is
   present. If `backup_restore_readiness` is not `ready`, stop. Do not deploy yet.
4. **Pre-deployment check.**
   `deploy/ubuntu/framenest-release check --release 26d28b16c08a5e7e0179a32c16646bfdc1009c81`
   must exit 0. A check never deploys and never refreshes sudo. Record the
   sanitized output fields.
5. **Privilege probe.** Remote `sudo -n true` through the gate must exit 0. If
   it fails, stop `PARTIAL`: this is expected after a predecessor `sudo -K`, and
   the Cooperator must re-run `sudo -v` outside this Worker. Do not run
   `sudo -v`.
6. **Deploy.**
   - **Same-schema branch:** if stage 3 `database_revision` is already `0033`,
     run
     `deploy/ubuntu/framenest-release deploy --release 26d28b16c08a5e7e0179a32c16646bfdc1009c81 --yes`
     once and require exit 0. Skip to stage 7.
   - **Schema-jump branch:** otherwise run the same `deploy --yes` once and
     expect exit 13 (`migration-required`) after the target tree is published
     and before cutover. Require: `/opt/framenest/current` still names the
     pre-deploy release; `framenest.service` still active on it;
     `/opt/framenest/releases/26d28b1…` exists with `.framenest-release-sha`
     equal to `26d28b1…` and an executable `.venv/bin/framenest-db`;
     `/run/framenest-release-deploy` contains exactly `ap.tar`,
     `framenest_release.py`, and `superproject.tar`; target-tree
     `framenest-db status` shows `current_revision` equal to the stage-3 live
     revision and `head_revision` `0033`. Then follow the runbook §5 annex
     exactly: remove only those three files with `sudo -n rm -f` and
     `sudo -n rmdir /run/framenest-release-deploy` (no recursive delete); run
     the migrate command from the target tree under the operator command
      contract (`sudo -n -u framenest --chdir=/opt/framenest/releases/<T>
      env FRAMENEST_ENV_FILE=/etc/framenest/framenest.env
      /opt/framenest/releases/<T>/.venv/bin/framenest-db migrate`, where `<T>`
      is `26d28b16c08a5e7e0179a32c16646bfdc1009c81`); require post-migration status
     `current_revision=head_revision=0033`; then complete the documented forward
     cutover with
     `deploy/ubuntu/framenest-release rollback --release 26d28b16c08a5e7e0179a32c16646bfdc1009c81 --yes`
     and require exit 0. Never run a second `deploy --yes` once the tree
     exists; never delete the target tree; never improvise a symlink or
     `systemctl` cutover. If `deploy` exits 9 (`EXIT_EXISTS`) because a leftover
     lock predates this session, stop `BLOCKED` and report it.
7. **Post-deployment status.** Run `deploy/ubuntu/framenest-release status`
   again. Require `active_release` `26d28b1…`, `release_path`
   `/opt/framenest/releases/26d28b1…`, manifest present, `service_active`
   active, `database_revision` `0033`, `backup_restore_readiness` `ready`.
   Record the previous complete release path as the rollback target; do not
   switch to it.
8. **Release content check.** Through the gate with `sudo -n`: confirm
   `readlink -n /opt/framenest/current` is `/opt/framenest/releases/26d28b1…`;
   `test -f /opt/framenest/current/vendor/kronika-ask/upstream.json`;
   `test -d /opt/framenest/current/vendor/kronika-ask/src/kronika`. Confirm no
   provider, browser, Node, or Chromium process was started, and
   `/etc/framenest/framenest.env` and `/var/lib/framenest/ai/config.json` were
   not modified by this Worker.
9. **Privilege release.** Remote `sudo -K` through the gate, then confirm a
   follow-up `sudo -n true` fails. Record both exits without passwords.
10. **Stop.** Do not start any live probe, provider ask, browser action, or
    further deployment.

## Rollback and recovery

- The release engine performs automatic rollback on post-switch failure. Report
  it; do not chain a second manual rollback. The captured previous release from
  stage 3 is the rollback target and remains untouched.
- If `current` is unhealthy after an engine-reported failure, stop and report
  the exact sanitized state for a Cooperator decision. Do not improvise a
  downgrade, catalog restore, or manual cutover.
- A post-migration cutover failure requires explicit triage; never improvise.

## Negative authority

No product-source, docs, ADR, AP, or Kronika ref changes. No second publication
or push beyond stage 2. No `uv`, no host `pip`, no operator `poetry install`
outside the helper's own release `.venv`. No `/etc/framenest/framenest.env`
edit, no systemd unit installation or enablement, no credential handling. No
enabling of automatic analysis. No wildcard deletion; never delete
`/opt/framenest/releases/*`. No disk, firewall, Tailscale, Funnel, Mullvad, or
SSH configuration mutation. No browser, provider call, Node, or Chromium. No
`/srv/media` writes. No subagents, internal delegation, native planning, or Max.
No closure signal.

## Stopping conditions

Stop and report honestly if: the repository gate or public `main` readback
diverges; the push is impossible; the SSH probe, transport variables, or
`sudo -n true` gate fails; `status` shows backup restore-readiness not ready;
`check` is nonzero; `deploy` produces an unexpected exit, an unexpected cutover,
or a missing target tree; the lock directory contains anything other than the
three named files; post-status does not prove the exact SHA, schema `0033`,
active service, and ready backup; a secret or credential is discovered in
output; or any stage would require prohibited action. A prerequisite failure
grants no new effect and no residual investigation.

## Completion and report contract

Finalize the complete report first, then deliver it to
`/home/agile/meta/projects/framenest/13/00-framenest-nuc-chatgpt-analyze-provider/03_report_00.md`
if and only if that file is absent, and read back its full content. No
directory creation is granted; the verified parent must already exist. This
exact write is the sole file-write exception outside the repository.

Begin the report exactly with:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo these coordinates once: logical whole identity, Worker session ordinal,
Worker exchange ordinal (`03` / `01`). Include: status (`PASS`, `PARTIAL`, or
`BLOCKED`); `Phase-qualified result: deployment-PASS` when publication,
deployment, post-status, content check, and privilege release are complete
(otherwise `not-applicable`); start and end commit
`26d28b16c08a5e7e0179a32c16646bfdc1009c81` (publication creates no new commit);
changed files (`03_report_00.md` only; no repository files); publication
evidence (the credential-free `ls-remote` readback of `refs/heads/main`);
pre-deploy sanitized status; check exit; which deploy branch ran (same-schema
or exit-13 annex with migrate and forward cutover); deploy and rollback exits;
post-deploy sanitized status; release content check; rollback target; privilege
release record; confirmation that no provider, browser, Node, or Chromium
activity occurred and that automatic analysis and AI configuration were left
untouched; deviations and risks; one smallest next step; exactly one report
justification (`changed-external-state`); `Logical-whole closure: not-closed`;
the Orchestration critique (`MEASURED:` / `LEAD:`), `Resolved Execution Issues /
Near-Misses`, `Pre-Existing Failure Classification: none`, an abbreviated
capability recheck, and the authority-expiry statement. Do not claim
`production-acceptance-PASS`; live page-provider acceptance is a later phase.

PASS means public `main` and live NUC `current` both equal `26d28b1…`, service
active, schema `0033`, backup ready, vendored kernel present, and privilege
released. PARTIAL covers SSH/transport/sudo lifecycle limits. BLOCKED covers
public-main mismatch, unexpected cutover, missing target tree, or prohibited
state. Do not overwrite an existing report, create a placeholder, or use
another output path. The Cooperator archives the exact prompt and report pair
after the report exists; you have no Git archival authority for the trace.

Authority expiry: this terminal report ends the grant. Stop after it; the next
slice needs a new complete authoritative prompt.
