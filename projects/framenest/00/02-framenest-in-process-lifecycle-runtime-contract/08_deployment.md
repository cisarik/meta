# Worker 8 — NUC Snapshot, Immutable Deployment and Live Lifecycle Acceptance

## Execution envelope

```text
Logical whole identity: framenest-in-process-lifecycle-runtime-contract
Worker session ordinal: 08
Worker exchange ordinal: 01
Worker role: production deployment and live-acceptance operator
Phase: pre-deployment recovery proof, immutable deployment, live acceptance
Reasoning profile requested by Cooperator: Extra High
Fresh-worker session: required
Native planning mode: not-used
Delegation: not-authorized
Source-code mutation authority: none
Commit or publication authority: none
NUC authority: explicitly authorized within this envelope
Production mutation authority: explicitly authorized within this envelope
Provider-call authority: none
Network/firewall/SSH/sudoers mutation authority: none
Logical-whole closure authority: none
```

Deploy the exact published and independently accepted FrameNest commit to the Cooperator-owned NUC, but only after proving a verified recovery point.

This is the first production deployment of the lifecycle-runtime candidate. Treat the live host as authoritative. Repository documentation and earlier reports are guidance, not proof of current NUC state.

## Exact published artifact

```text
cisarik/framenest refs/heads/main:
148b6c2012809944262399c1a166e85082606fbf

tree:
1ea47dfbdbfe78c7a20f04b0c8bc54ba31805366

parent:
5fe07b01bdfd587919d38a3d59ddd00e004d7394

grandparent:
a72be476f5634394287082be07380d03fa7ccd4d

cisarik/ap gitlink:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

expected schema head:
0028
```

Expected immutable target:

```text
/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf
```

Expected service:

```text
framenest.service
```

Historical production paths that must be verified rather than assumed:

```text
/opt/framenest/current
/etc/framenest/framenest.env
/var/lib/framenest/catalog.sqlite3
/opt/framenest/releases/
```

Do not assume the previously deployed SHA from documentation or historical reports. Read it directly from the live host.

## Required local reading

Before NUC mutation, read:

```text
/home/agile/Projects/framenest/AGENTS.md
/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md
/home/agile/Projects/framenest/docs/UBUNTU_NUC_DEPLOYMENT.md
/home/agile/Projects/framenest/deploy/systemd/framenest.service
```

Discover only relevant recovery documentation with:

```bash
rg --files /home/agile/Projects/framenest/docs \
  | rg '(backup|recovery|restore|0057|NUC|DEPLOY)' -i
```

Read the matching current recovery runbook and ADR-0057 material. Inspect the existing backup/recovery CLI implementation only as needed to determine exact commands.

Do not read the entire Meta repository. If present, `06_report.md` and `07_report.md` for this logical whole may be read selectively as supporting evidence only.

## Noninteractive SSH profile

The Cooperator has already loaded this key into `gpg-agent`:

```text
/home/agile/.ssh/id_ed25519_framenest_nuc_cachyos
fingerprint: SHA256:FuBY7/UNF4tdQfDkkcQpaJXfsxGZm7RtSk2S1VLRwwQ
```

Target:

```text
michal@framenest-nuc
```

Every SSH operation must be noninteractive and use this profile:

```bash
env SSH_AUTH_SOCK="$(gpgconf --list-dirs agent-ssh-socket)" \
  ssh -T \
  -o BatchMode=yes \
  -o RequestTTY=no \
  -o StrictHostKeyChecking=yes \
  -o IdentitiesOnly=yes \
  -o ForwardAgent=no \
  -o ClearAllForwardings=yes \
  -o ConnectTimeout=10 \
  -o ServerAliveInterval=15 \
  -o ServerAliveCountMax=2 \
  -i /home/agile/.ssh/id_ed25519_framenest_nuc_cachyos \
  michal@framenest-nuc \
  '<exact remote command>'
```

Do not place `--` after the SSH destination.

Never request, print, copy, or modify a passphrase or private key. Do not enable agent forwarding.

## Mandatory access gate

Locally verify that the exact expected key is visible through the selected agent socket.

Then run a remote preflight requiring:

```text
id -un = michal
hostname = framenest-nuc
SSH_BATCH_READY
sudo -n true exits 0
SUDO_BATCH_READY
```

Also verify the expected Ubuntu host identity and that the connection is to the intended NUC.

If SSH BatchMode or general `sudo -n` fails, stop as `BLOCKED` before production mutation. Do not fall back to interactive SSH or password entry. Tell the Orchestrator that the Cooperator must refresh the agent or `global_sudo.sh`.

The available global sudo timestamp is operational capability only for this bounded deployment. It does not authorize unrelated root changes.

## Explicitly prohibited host mutations

Do not modify:

* SSH client/server configuration;
* authorized keys;
* sudoers or `global_sudo.sh`;
* firewall, router, Wi-Fi, Tailscale, VPN, or DNS;
* users or groups except release ownership already required by the runbook;
* storage partitions, filesystems, mount configuration, or `/srv/media`;
* kernel, bootloader, unrelated packages, services, timers, or cron jobs;
* production media contents;
* secrets or provider credentials.

No real X, YouTube, OpenAI, or other external-provider call is authorized or required.

Do not print `/etc/framenest/framenest.env` or environment-variable values.

## Phase 1 — authoritative live readback

Before any mutation, record without leaking private content:

1. hostname, current user, OS release, and current time;
2. `framenest.service` unit identity, enablement, active/sub state, main PID, control group, and recent restart count;
3. resolved `/opt/framenest/current` target;
4. current release identity derived from the symlink and live executable;
5. current process executable and command path;
6. installed service-unit hash and its lifecycle settings;
7. current database path, ownership, permissions, size, integrity, and Alembic revision;
8. aggregate counts of active acquisition, validation, analysis, publication, or cleanup work without exposing titles, URLs, filenames, users, or private payloads;
9. available disk space sufficient for a new release, verified snapshot, and rollback;
10. current loopback health/readiness response;
11. bounded recent service logs for pre-existing failures;
12. existing backup/recovery services, timers, helper, and workstation-pull bridge.

Require current schema `0028`. If live schema is newer than `0028`, stop as `BLOCKED`. If it is older, stop before deployment because this logical whole was accepted as a no-schema-change deployment.

If active work exists, wait and recheck for at most five minutes. Use aggregate state only. If potentially destructive in-flight work remains, stop before cutover rather than interrupting it under the old release.

Do not trust a stale deployment SHA in documentation over direct live evidence.

## Phase 2 — mandatory verified recovery point

No release staging, service stop, symlink change, or migration may occur until this phase passes.

Use the repository’s existing accepted backup/recovery workflow. Do not invent an ad hoc `cp` of a live SQLite database.

Create a new pre-deployment catalog snapshot and record:

* snapshot identifier and creation time;
* safe artifact path;
* size;
* checksum;
* source database identity;
* schema revision;
* SQLite integrity result;
* permissions and ownership;
* retention/verification result.

Do not display catalog rows or private metadata.

### Off-device recovery lane

Exercise the established operator-workstation pull workflow using its documented CLI and existing narrow NUC export bridge.

Require:

* noninteractive transfer;
* locally verified checksum;
* correct secure permissions;
* no secret output;
* snapshot readable independently of the production database.

Do not alter the sudo bridge. If the documented bridge or CLI is unavailable or fails, stop before deployment as `BLOCKED` and report the exact boundary.

### Disposable restore drill

Restore the new snapshot to a newly created, absent, disposable database target—never over the production database.

Verify on the restored copy:

* SQLite opens successfully;
* integrity check passes;
* Alembic revision is `0028`;
* safe aggregate table/state checks match the snapshot source;
* no production path or current symlink was changed.

Remove only the exact disposable restore target after verification. Retain the verified pre-deployment snapshot needed for rollback.

If backup creation, pull, checksum, or disposable restore verification fails, do not deploy.

## Phase 3 — immutable release preparation

Verify public `cisarik/framenest/main` directly equals `148b6c20…`.

Prepare the release using the current accepted deployment runbook and the live host’s proven immutable-release conventions.

Requirements:

* obtain exact public commit `148b6c20…`;
* independently verify commit, tree, parents, and `.ap` gitlink;
* use a staging directory under the FrameNest release hierarchy;
* never construct directly inside a partially existing final release directory;
* use the declared locked production dependencies;
* use supported CPython 3.13;
* do not install development/test dependencies into production merely for acceptance;
* preserve service-user ownership and restrictive permissions;
* do not modify the current symlink during preparation;
* do not overwrite an existing immutable release.

If the exact final release directory already exists:

* verify it completely;
* reuse it only if its source identity, environment, entry point, ownership, and permissions are exact;
* otherwise stop as `BLOCKED`; do not overwrite it.

Run release-local, provider-free smoke checks as the service user. Verify imports and the production entry point from the staged release.

Verify the staged code still reports schema head `0028`.

Because this candidate contains no migration, an upgrade-to-head command must be a no-op from live revision `0028`. If it proposes or performs a schema transition, stop and invoke rollback handling.

Do not mutate the systemd unit when the installed unit is already equivalent to the accepted unit. If material drift exists, report it before cutover; do not silently normalize unrelated settings.

## Phase 4 — atomic cutover

Record the exact previous `/opt/framenest/current` target as the rollback release.

Capture a journal timestamp/cursor immediately before cutover.

Perform the documented immutable cutover:

1. stop `framenest.service`;
2. verify it stopped without systemd timeout or SIGKILL;
3. atomically switch `/opt/framenest/current` to the exact new release;
4. start `framenest.service`;
5. wait using a bounded readiness loop;
6. verify loopback health;
7. verify the running process executable resolves inside the exact new release;
8. verify schema remains `0028`;
9. verify database integrity;
10. inspect only bounded new-release journal entries.

Do not use a fixed long sleep when a bounded readiness poll is available.

The first deployment health gate must prove:

```text
current symlink = exact 148b6c20 release
service active/running
main process belongs to exact release
health returns expected success
schema = 0028
database integrity = ok
no startup traceback
no systemd start-limit or restart loop
no leaked secret or private payload
```

## Automatic rollback boundary

If any cutover, startup, health, schema, database-integrity, or initial-log gate fails:

1. stop the failed new service;
2. atomically restore the previous `current` target;
3. start the previous release;
4. verify previous-release health, process identity, schema, and integrity;
5. restore the production catalog snapshot only if the deployment actually changed or corrupted database state and service is stopped;
6. retain evidence and failed release artifacts for diagnosis unless they are unsafe;
7. report `PARTIAL` with `rollback-PASS`, or `FAIL` if rollback cannot restore service.

Do not continue testing a failed new release.

Do not restore the production database merely because application startup failed when the database remains intact and unchanged.

## Phase 5 — live graceful-stop acceptance

Only after the new release passes initial health gates, test the actual systemd lifecycle once.

Before stopping:

* record service PID, cgroup, restart counters, health, schema, and journal cursor;
* ensure no active user work exists;
* capture a monotonic start timestamp.

Issue one normal:

```text
systemctl stop framenest.service
```

through noninteractive sudo.

Measure elapsed stop time. Require:

* completion strictly below `TimeoutStopSec=30s`;
* no systemd timeout;
* no SIGKILL escalation;
* no surviving process in the former service cgroup;
* no surviving lifecycle-owned child attributable to FrameNest;
* no unexpected runner-death traceback;
* database integrity remains valid;
* schema remains `0028`.

Uvicorn 0.49 may finish graceful cleanup and then expose SIGTERM as the process exit signal. Exit `0` or the expected SIGTERM result is acceptable only if cleanup completed, systemd did not escalate, children were reaped, and durable state remains healthy.

Then start the service once and require:

* bounded readiness success;
* health success;
* exact new-release executable;
* stable active/running state;
* no restart loop;
* schema `0028`;
* database integrity;
* bounded post-start journal without new fatal errors.

Do not trigger real provider work to manufacture an in-flight child. Existing unit/integration acceptance already proved synthetic process interruption; this phase proves the real systemd envelope and production restart.

## Phase 6 — final production readback

Record:

```text
public SHA
deployed release path
current symlink target
running executable path
service state and PID
schema revision
database integrity
health result
pre-deployment snapshot identifier/checksum
off-device snapshot verification
disposable restore result
previous rollback release
live stop duration
systemd stop result
post-restart health
journal error classification
```

Confirm the previous release and verified recovery snapshot remain available.

Do not expose secrets, catalog contents, private media names, external URLs, or user data.

## Mandatory sudo expiry

Only after all success, rollback, evidence, and cleanup actions are complete, execute remotely:

```bash
sudo -K
```

Then verify general cached sudo is no longer available by treating failure of:

```bash
sudo -n true
```

as the expected successful expiry result.

Do not invalidate sudo before completing any required rollback.

SSH may remain available; only the broad cached sudo authority must expire.

## PASS standard

Report `deployment-PASS` only if:

* noninteractive SSH and sudo worked;
* live pre-state was recorded;
* a new verified snapshot was created;
* off-device pull and checksum verification passed;
* disposable restore verification passed;
* exact public SHA was deployed immutably;
* schema remained `0028`;
* initial readiness and health passed;
* one real systemd stop completed below 30 seconds without SIGKILL;
* no owned process remained;
* restart and final health passed;
* production database remained healthy;
* rollback release and snapshot remain available;
* cached broad sudo authority was invalidated;
* no provider, network, firewall, SSH, sudoers, AP, Meta, or source mutation occurred.

A deployment failure followed by fully verified rollback is not deployment PASS. Report `PARTIAL` with phase result `rollback-PASS`.

Deployment PASS is production evidence but still not Orchestrator logical-whole closure.

## Terminal report

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Then provide:

```text
Logical whole identity: framenest-in-process-lifecycle-runtime-contract
Worker session ordinal: 08
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED | FAIL
Phase-qualified result: deployment-PASS | rollback-PASS | not-applicable
Result artifact or commit: /opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf | <previous release> | not-applicable
Result evidence: <compact production evidence>
Logical-whole closure: not-closed
Report justification: production-mutation | idempotent-production-verification | rollback | blocker | failure
Authority expiry: all Worker 8 authority expired and cached sudo invalidated at this terminal report
```

Report:

1. fresh-session, native-mode, delegation, and authority confirmation;
2. exact SSH BatchMode and sudo preflight;
3. public-ref verification;
4. authoritative NUC pre-state;
5. aggregate active-work gate;
6. exact backup command and safe snapshot metadata;
7. off-device pull and checksum proof;
8. disposable restore command and integrity/schema proof;
9. previous release and rollback boundary;
10. immutable release construction and exact source proof;
11. migration/no-op schema evidence;
12. atomic cutover commands and exit codes;
13. initial service/readiness/health/process evidence;
14. live systemd stop command, measured duration, exit classification, and absence of SIGKILL;
15. child/cgroup reaping evidence;
16. restart and final health evidence;
17. database integrity and schema before/after;
18. bounded journal classification;
19. final release/symlink/process readback;
20. retained snapshot and rollback-release evidence;
21. exact mutations and explicitly untouched boundaries;
22. rollback actions if invoked;
23. final `sudo -K` and expected `sudo -n true` failure;
24. residual production risks;
25. AP empirical observations, explicitly non-authorizing;
26. FrameNest ledger observations, if concrete;
27. resolved execution issues and near-misses.

Terminate after the report. Do not begin another logical whole.
