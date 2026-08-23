# Authoritative Prompt for Fresh Worker 11

## FrameNest Companion AI Review Inbox — NUC schema-changing routine update

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

Worker 09 published `6e20fc12` to public `main` (`publication-PASS`). Worker
10 ran **too early**, saw `ls-remote` still at `045f33b4`, and stopped
`BLOCKED` without NUC mutation. That BLOCKED is correct for that instant. Do
**not** resume Worker 10. The ORCHESTRATOR independently re-read public `main`
as `6e20fc12f145286e474294b79cbd120df6e38e56`. This session is the deploy.

ADR-0060 is **same-schema only**. This candidate packages Alembic **0031**.
Expect a schema jump. Do **not** pretend a single `deploy --yes` will cut
over. Do **not** run `~/framenest_routine.fish`.

Do not enter Native Plan Mode. Do not use Max. Extra High is requested; if the
client does not expose a measurable Extra High SKU, continue only while Plan
Mode stays off and Max is unused, and record that in the handshake. If Native
Plan Mode is on, stop `BLOCKED`.

Paste this prompt **only after** the COOPERATOR has established the remote
sudo timestamp **outside** this chat (`sudo -v`, then `sudo -n true` on the
NUC). You must not run `sudo -v` or handle a password. Re-verify public
`main` yourself; do not trust Worker 10's stale ls-remote.

```text
Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-companion-ai-review-inbox-mvp
Worker session ordinal: 11
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: bounded NUC deployment
Phase: deployment
Task identity: FN-COMPANION-AI-REVIEW-INBOX-DEPLOY-11
Task type: bounded schema-changing production update
Native planning mode: not-used
Reasoning recommendation: extra-high
Evidence posture: non-independent
Independence required: no
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
Prior publication report: Worker 09 / exchange 01 publication-PASS at 6e20fc12; Worker 10 BLOCKED (stale public main); authority expired
Continuity anchor: none — do not resume Worker 09 or Worker 10
Internal delegation posture: not-used
Accountable Worker: one WORKER
Material phase gate: yes
Changed material axis: production-external-service-credential-or-account-boundary
Routing reopened for: production-external-service-credential-or-account-boundary
Unchanged axes reopened: none
Ordinary-only trigger: no
Automatic model selection: off
Enhanced/maximum mode: not requested
```

```text
Deployment authority: explicit for the staged envelope in Section 10
Publication authority: none
Implementation authority: none for product source
Correction authority: none
Native planning mode: not-used
Exact baseline / release SHA: 6e20fc12f145286e474294b79cbd120df6e38e56
Independence required: no
```

```text
Evidence tier: E3
Evidence tier basis: privileged remote host mutation, catalog checkpoint, schema migrate, atomic current-symlink switch, service restart
Authorized implementation stages: Section 10; a failed gate stops the sequence
Combined implementation envelope: allowed for those stages only
Independent acceptance: not-required (Cooperator UX follows)
Rollback or recovery checkpoint: engine automatic rollback on post-switch failure; do not invent a second rollback
Activated annex: deployment + privilege lifecycle
Terminal deployment report point: after post-status proves this SHA, schema 0031, service active, backup restore_readiness ready, and sudo -K
```

```text
COOPERATOR: Michal
ORCHESTRATOR: ORCHESTRATOR_CHAT
WORKER: this fresh deployment session
```

Internal delegation, sub-agents, parallel Workers, Explore tasks, and hidden
secondary workstreams are not authorized.

Repository documentation and the terminal Worker report must use professional
English. Czech is forbidden. The terminal report must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Deployment PASS is not UX acceptance, INFOSEC R3, flag enablement, or closure.
`Logical-whole closure: not-closed`.

Protocol-variant selection:

```text
Canonical repository identity: https://github.com/cisarik/ap.git
Immutable version identity: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Declared variant: stable
Governing variants in effect: one
Declaration location: project governing rules
Rules from non-governing variants: none
Migration required: yes — production DB to packaged head 0031, separately from the helper
```

---

## 1. External trace and Meta write boundary

```text
External trace disposition: configured
Trace discovery: cisarik/meta repository path projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp
Trace project key: framenest
Trace logical-whole projection identity: 03/09-framenest-companion-ai-review-inbox-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR after the outcome exists
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Downloadable prompt filename: 11_deployment_00.md
Destination path: projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/11_deployment_00.md
Archival: wait-for-report
```

You may **read** (historical; this prompt wins):

```text
/home/agile/meta/projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/09_publication_00.md
/home/agile/meta/projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/09_report_00.md
/home/agile/meta/projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/10_deployment_00.md
/home/agile/meta/projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/10_report_00.md
```

Frozen hashes at issuance (re-check; stop `BLOCKED` if drifted):

```text
09_publication_00.md SHA-256 de210b1fae5674e88e88900fb175af10a46c17d0c31de8b4d4351dc5140acf37
09_report_00.md SHA-256 d37f636649644413b912629759359c420d92f792ae1ce39d651289ac8f7b7e49
10_deployment_00.md SHA-256 61a59c41c558711d65119c231a7be6ffbd97109329414e897b2a1a1ea9495de2
10_report_00.md SHA-256 7a17cdcc5cb17872f319840496b06f8ff654f1abc1c5243b1a0b116f5322e41e
```

You may **write** only:

```text
/home/agile/meta/projects/framenest/03/09-framenest-companion-ai-review-inbox-mvp/11_report_00.md
```

Do not alter any other Meta path. Do not stage or commit Meta.

---

## 2. Handshake

Compact handshake before mutation. Capability does not grant authority.

Browser, provider, and publication annexes are **not** activated. Do not enable
`FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED`. Do not edit
`/etc/framenest/framenest.env`. Do not print companion origin allowlist values,
Tailscale node names, credentials, or `SSH_AUTH_SOCK`.

---

## 3. Frozen artifact

```text
Accepted public commit: 6e20fc12f145286e474294b79cbd120df6e38e56
Accepted tree: 950d6eeb0a78ad7f2b143ead724e01ccc0bc6788
Required public refs/heads/main: 6e20fc12f145286e474294b79cbd120df6e38e56
Required AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Packaged schema head: 0031
Entry point: /home/agile/Projects/framenest/deploy/ubuntu/framenest-release
Exact NUC Poetry: /opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry
Exact NUC CPython: /opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13
Release dir: /opt/framenest/releases/6e20fc12f145286e474294b79cbd120df6e38e56
Lock dir: /run/framenest-release-deploy
```

Working directory: `/home/agile/Projects/framenest`.
Expected branch: `feat/x-meme-browser-companion`.
Local HEAD must equal the release SHA. Tracked tree clean. Git write: none.

Preserve untracked owner paths. Do not print `FRAMENEST_NUC_SSH_*` values.
Pass `--target` / `--user` / `--identity` from already-configured operator
env or SSH Host alias without echoing them.

Worker 10 observed those three process env vars **unset** and correctly did
not scrape `~/framenest_routine.fish`. If they are still unset, stop
`PARTIAL` after `--probe`: the COOPERATOR must export them into this Worker
environment (not into chat, not by running the routine script). Do not invent
hostnames. Do not reconstruct `gpgconf`.

---

## 4. Why a naive `deploy --yes` is not enough

`framenest-release deploy` prepares the immutable tree, then compares
production `current_revision` to the **target** packaged `head_revision`.
Mismatch raises `migration-required` (exit **13**) **after** the tree exists at
`/opt/framenest/releases/<SHA>` and **before** cutover. The helper never
migrates. The lock directory is left behind because success-path cleanup does
not run.

A second `deploy --yes` then fails: lock exists, and the target release dir
exists.

This Worker is authorized to complete the **schema-changing** path in Section
10 without improvising a second deploy engine. `rollback --release <SHA>` is
the engine command that switches `/opt/framenest/current` to an **already
complete** release. After migrate, that is the forward cutover. It is not a
product rollback to an older SHA.

---

## 5. Required reading

- `AGENTS.md` (NUC Routine Release Update; Worker Execution Boundary)
- `docs/WORKER_EXECUTION_CONTRACT.md` (SSH gate, sudo lifecycle)
- `docs/UBUNTU_NUC_DEPLOYMENT.md` (Routine Immutable Release Update; §5 Migrate)
- `docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md`
- `.ap/AP.md`, `.ap/AP_WORKER.md`

Python evidence is not this task. The authorized host mutation entry point is
`deploy/ubuntu/framenest-release` even though that wrapper uses repository
`.venv/bin/python` internally. Do not call ambient `python` / `poetry run` for
tests. Do not invoke `uv`.

---

## 6. SSH and privilege

```text
scripts/operator/network/framenest_nuc_worker_gate.fish --probe
```

Expect `ssh-agent: ready` or `ssh-agent: absent`. Do not print the socket.
Do not reconstruct `gpgconf`.

Then invoke **only** `deploy/ubuntu/framenest-release` for status/check/deploy/
rollback. That helper performs its own BatchMode SSH.

If probe is ready but the helper fails publickey because the parent lacks
`SSH_AUTH_SOCK`, stop `PARTIAL`. Do not reconstruct `gpgconf`. Ask the
ORCHESTRATOR to have the COOPERATOR rerun this exact prompt from an operator
fish session that already inherits the agent.

Remote `sudo -n true` must succeed before privileged stages. If it fails,
stop `PARTIAL` — expected after a predecessor `sudo -K`; the COOPERATOR must
re-run `sudo -v` outside this Worker. You must not `sudo -v`.

At the terminal report: remote `sudo -K`, then confirm follow-up `sudo -n true`
fails. Record both exits without passwords.

---

## 7. Goal

Live NUC `current` equals
`/opt/framenest/releases/6e20fc12f145286e474294b79cbd120df6e38e56`, service
active, database **0031/0031**, `backup_restore_readiness: ready`, previous
complete release retained as rollback target. Automatic analysis remains
**disabled**. Companion origin allowlist is not printed and not changed.

---

## 8. Orchestrator binding — schema-changing path

Exact unpublished tree path:

```text
NEW=/opt/framenest/releases/6e20fc12f145286e474294b79cbd120df6e38e56
```

Service-account migrate (same prefix the engine uses for `framenest-db`, aimed
at the unpublished tree that contains 0031):

```text
sudo -n -u framenest --chdir=/opt/framenest/releases/6e20fc12f145286e474294b79cbd120df6e38e56 \
  env FRAMENEST_ENV_FILE=/etc/framenest/framenest.env \
  /opt/framenest/releases/6e20fc12f145286e474294b79cbd120df6e38e56/.venv/bin/framenest-db migrate
```

Then prove with the same prefix `framenest-db status` that `current_revision`
and `head_revision` are both `0031`.

Lock recovery after expected exit 13: remove **only**
`/run/framenest-release-deploy` (it will not be empty, so `rmdir` is not
enough). Do **not** delete `$NEW`. Do not delete any other release. Do not
touch `/opt/framenest/current` except through `framenest-release rollback`.

Forward cutover:

```text
deploy/ubuntu/framenest-release rollback --release 6e20fc12f145286e474294b79cbd120df6e38e56 --yes
```

That command requires the lock dir to be absent (it `mkdir`s its own).

If pre-deploy `database_revision` is **already** `0031`, skip migrate and the
exit-13 path. Use a single `deploy --yes` as a same-schema update.

Keep `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED` untouched (default false /
already false).

---

## 9. Negative authority

- Native Plan Mode, Max, sub-agents
- Git write, push, source/docs/ADR edits
- `uv`; host `pip`; operator `poetry install` except what the helper does
  inside the release `.venv`
- Editing `/etc/framenest/framenest.env` or systemd credentials
- Enabling automatic analysis
- Forging `.framenest-release-manifest.json` on an old tree
- `/srv/media` writes; disk/firewall/Tailscale/Funnel/Mullvad mutation
- Browser, provider calls, signed-in X
- Wildcard deletion; deleting `$NEW` or any other `/opt/framenest/releases/*`
- Second `deploy --yes` after the tree already exists
- Improvised `ln -s` / `systemctl` cutover beside the helper
- Closure; Orchestrator restoration prompt; UX claims

---

## 10. Authorized stages (stop at the first failure)

Sanitize AppImage `LD_LIBRARY_PATH` / `PYTHONHOME` for the helper process.
Do not pipe gates through `tail`/`grep` in a way that hides exits. Timeouts
must cover remote `poetry install`.

1. Credential-free `git ls-remote https://github.com/cisarik/framenest.git refs/heads/main`
   equals `6e20fc12f145286e474294b79cbd120df6e38e56`. Local HEAD and `.ap` pin
   match. Tracked tree clean.
2. Gate `--probe`. Then `framenest-release status` — exit 0. Record sanitized
   `active_release`, `release_manifest` (present|absent), `service_active`,
   `database_revision`, `backup_restore_readiness`. If restore readiness is not
   `ready`, stop. Do not migrate yet. Do not deploy yet.
3. `framenest-release check --release 6e20fc12f145286e474294b79cbd120df6e38e56`
   — exit 0. Must not deploy or refresh sudo.
4. Remote `sudo -n true` — exit 0.
5. **Same-schema branch:** if status `database_revision` is already `0031`:
   one `framenest-release deploy --release 6e20fc12f145286e474294b79cbd120df6e38e56 --yes`.
   Require exit 0. Skip steps 6–8.
6. **Schema-changing branch:** one `deploy --yes` of the same SHA. **Expect
   exit 13** `migration-required`. Require all of:
   - `/opt/framenest/current` still the pre-deploy release
   - `$NEW` exists with `.framenest-release-sha` and
     `.venv/bin/framenest-db`
   - service still active on the old current
   If deploy cut over anyway, or deleted `$NEW`, stop `BLOCKED`.
7. Remove only `/run/framenest-release-deploy` (recursive, that path only).
   Confirm it is absent. Confirm `$NEW` still exists.
8. Run the Section 8 migrate command. Require packaged head **0031** and
   current **0031**. Then
   `framenest-release rollback --release 6e20fc12f145286e474294b79cbd120df6e38e56 --yes`.
   Require exit 0.
9. `framenest-release status` again. Require `active_release`
   `6e20fc12…`, `release_manifest: present`, service active,
   `database_revision` `0031`, `backup_restore_readiness: ready`. Record the
   previous complete release path as the rollback target (do not switch to it).
10. Remote `sudo -K`. Confirm `sudo -n true` then fails. Stop.

If deploy exits `EXIT_EXISTS` 9 because a leftover lock from an older attempt
is already present **before** step 6, stop `BLOCKED`. Worker 10 never created
a lock. Do not delete a lock you did not create in this session unless status
proves current is unchanged and the lock is exactly `/run/framenest-release-deploy`
from a prior failed same-SHA prepare; if that is the case, report the finding
and wait — do not guess.

If post-switch failure triggers engine automatic rollback, report it. Do not
chain a second manual rollback unless current is unhealthy and the captured
previous SHA is known from this session's pre-status.

---

## 11. Tests / validation

No pytest. No browser. No NIM. Validation is helper status/check exits and the
post-cutover sanitized status in stage 9.

---

## 12. Terminal report

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

```text
Logical whole identity: framenest-companion-ai-review-inbox-mvp
Worker session ordinal: 11
Worker exchange ordinal: 01
```

Include: PASS | PARTIAL | BLOCKED; `deployment-PASS` or not;
`production-acceptance-PASS` **not claimed**; public-main readback; local HEAD;
pre-deploy sanitized status (schema without secrets); check exit; privilege
probe; which branch (same-schema deploy vs exit-13 + migrate + rollback);
deploy/rollback exits; post-status; whether automatic analysis was left
untouched; privilege-release record; secrets omitted; next step = COOPERATOR
UX test of the review inbox (not closure).
Report justification: `changed-external-state`.
`Logical-whole closure: not-closed`.

Near-misses / pre-existing classification required.

---

## 13. Quality bar

`PASS` / `deployment-PASS` only if live current SHA is `6e20fc12…`, schema
`0031`, service active, backup restore ready, auto-analysis not enabled by
this Worker, `sudo -K` done, no push of extra commits.

`PARTIAL` for sudo/SSH-agent lifecycle. `BLOCKED` for public-main mismatch,
unexpected cutover, or missing `$NEW` after exit 13.

---

## 14. Stop

After the terminal report, stop. Do not start Cooperator UX. Do not write an
Orchestrator restoration prompt. Do not close the logical whole.
