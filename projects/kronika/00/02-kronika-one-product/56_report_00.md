### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 56
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Worker-Executed Preflight
Phase: preflight
Task identity: KRONIKA-ONE-PRODUCT-S9-RESET-PREFLIGHT
status: PASS
Phase-qualified result: not-applicable
Start commit: 5eddb81bd164207a86f23b3f236e36b66192930b
End commit: 5eddb81bd164207a86f23b3f236e36b66192930b
Report justification: new-evidence
Logical-whole closure: not-closed

No mutation was performed. This preflight does not authorize the reset.

## Repository gate

Root `/Users/agile/Projects/framenest`, branch `feat/kronika-one-product`, remote `https://github.com/cisarik/framenest.git`. `HEAD` and parent match the prompt (`5eddb81bd164207a86f23b3f236e36b66192930b`, parent `ef9920333013f3f70bf5e3443be2e51814f6b9c3`). Index and worktree were clean, including untracked files, at start and again after the host reads. `.ap` gitlink and submodule `HEAD` are `73e20ef80b88700d5fcbc397cd8edd4fc425869f`. One `git ls-remote` of `refs/heads/main` and `refs/heads/feat/kronika-one-product` both returned `5eddb81bd164207a86f23b3f236e36b66192930b`. No divergence. No Git write.

## Release and service state

NUC access was only through `scripts/operator/network/framenest_nuc_worker_gate.fish`. `--probe` printed `ssh-agent: ready`. `sudo -n true` succeeded. The workstation helper `deploy/ubuntu/framenest-release` was not invoked: it runs repository `.venv` Python and its own SSH, both outside this gate. The same read-only probes that helper uses were run through the gate. `framenest-db status` was not run: that CLI opens the catalog writable (`prepare_writable_catalog`). Live revision was read with `sqlite3 -readonly`. A follow-up `stat` of the WAL/SHM/journal siblings still failed with `No such file or directory` (exit 1), so that read created no sibling.

| Field | Value | Source |
| --- | --- | --- |
| active_release / web_release | `5eddb81bd164207a86f23b3f236e36b66192930b` | `sudo -n readlink -n /opt/framenest/current` → `/opt/framenest/releases/5eddb81bd164207a86f23b3f236e36b66192930b`; manifest key `framenest_release_sha` on that tree |
| capture_release | `94e605c17b881461fad3e22fd8c7fca32cb93976` | `sudo -n readlink -n /opt/framenest/capture-current` → `/opt/framenest/releases/94e605c17b881461fad3e22fd8c7fca32cb93976`; manifest `framenest_release_sha` |
| service_active | `active` / `running` / enabled | `systemctl is-active framenest.service`; `systemctl show` ActiveState, SubState, UnitFileState |
| database_revision | `0035` | `sudo -n sqlite3 -readonly /var/lib/framenest/catalog.sqlite3 'SELECT version_num FROM alembic_version'` |
| backup_restore_readiness | `ready` (derived) | `status.json` last success `2026-09-30T14:53:40Z`, `current_operation` null, `recent_failure` null, `pending_cleanup` null; code `STALE_AFTER` is 48 hours. CLI `framenest-backup status` was not run because its layout helper can create missing ops files |

Release-tree binaries `framenest-db` and `framenest-backup` are executable (`sudo -n test -x`, exit 0). Installed units `/etc/systemd/system/framenest.service` and `framenest-catalog-backup.service` both contain `StateDirectoryMode=0700`.

Configured catalog path, extracted alone from the service environment: `FRAMENEST_DATABASE_PATH=/var/lib/framenest/catalog.sqlite3`. SQLite header bytes at offsets 18 and 19 are `1 1` (rollback-journal format, not WAL), which matches the absent siblings.

## Classified inventory

State directory `/var/lib/framenest`: mode `700`, owner `framenest:framenest`, size 4096, link count 16, mtime `2026-09-30 15:08:07 UTC`.

| Path | Mode | Owner | Size | Links | Mtime (UTC) | Class |
| --- | --- | --- | --- | --- | --- | --- |
| `/var/lib/framenest/catalog.sqlite3` | 600 | framenest:framenest | 1134592 | 1 | 2026-09-30 15:08:07 | active catalog |
| `/var/lib/framenest/catalog.sqlite` | 644 | framenest:framenest | 0 | 1 | 2026-07-22 16:07:44 | residue; the other old application-database name |
| `catalog.sqlite3-wal`, `-shm`, `-journal` | absent | | | | | sibling not present |
| `catalog.sqlite-wal`, `-shm`, `-journal` | absent | | | | | sibling not present |
| `/var/lib/framenest/runtime-settings.json` | absent | | | | | configuration path; nothing to preserve because the file is not there |

Nine regular files directly in `/var/lib/framenest`, mode `600`, owner `framenest:framenest`, link count 1, dated 2026-07-22 or 2026-07-30, are scratch residue (names contain `.tmp` or `..` plus a deploy or restore-drill stamp). They are not the configured catalog and are outside the reset. Sizes are 241664 (eight files) and 315392 (one file).

Top-level directories, all preserved: `catalog-backups` (700, framenest, link count 60), `catalog-backup-ops` (700, framenest), `catalog-restore-verify` (700, framenest, link count 2), `ai`, `covers`, `upload-quarantine`, `x-staging`, `youtube-acquisition` (all 700, framenest), `chatgpt-page` (700, framenest; browser-profile tree, not opened), `deployment-evidence` (755, root), `catalog-backup-eb5b1b42e72f48dd4a973e5dfcf6d26d7c4adc6e-20260801T133109Z` (700, root), plus `.cache` (755, framenest), `.config` and `.local` (700, framenest).

## Exact mutation boundary for the later grant

Delete only these eight paths, and only when a fresh `stat` shows each one is absent or a regular file with link count 1 owned by `framenest`:

1. `/var/lib/framenest/catalog.sqlite3`
2. `/var/lib/framenest/catalog.sqlite`
3. `/var/lib/framenest/catalog.sqlite3-wal`
4. `/var/lib/framenest/catalog.sqlite3-shm`
5. `/var/lib/framenest/catalog.sqlite3-journal`
6. `/var/lib/framenest/catalog.sqlite-wal`
7. `/var/lib/framenest/catalog.sqlite-shm`
8. `/var/lib/framenest/catalog.sqlite-journal`

Observed present count: 2. Observed absent sibling count: 6. Re-stat after writers stop; if a sibling of these two names has appeared, it joins this same set. Any other path stays. That includes the nine scratch files, every directory above, `/etc/framenest/framenest.env`, `/opt/framenest/current`, `/opt/framenest/capture-current`, `/var/lib/kronika-capture`, `/srv/media`, backup bundles, and archives.

## Writers

`sudo -n fuser /var/lib/framenest/catalog.sqlite3` shows pid 8310. `systemctl show framenest.service -p MainPID` is 8310. `ps` comm is `framenest-produ` (truncated `framenest-production`), user `framenest`. Acquisition runners are inside this unit.

| Unit | ActiveState | SubState | Unit file | Role |
| --- | --- | --- | --- | --- |
| `framenest.service` | active | running | enabled, `/etc/systemd/system/framenest.service` | live catalog writer |
| `framenest-catalog-backup.timer` | active | waiting | enabled | can start the backup writer; next elapse `Thu 2026-10-01 03:25:54 UTC`; last trigger `Wed 2026-09-30 06:16:18 UTC` |
| `framenest-catalog-backup.service` | inactive | dead | disabled, fragment installed | oneshot `framenest-backup run-scheduled`; the timer still starts it |
| `framenest-catalog-offdevice.service` | inactive | dead | not installed (empty FragmentPath and UnitFileState) | not a writer on this host |
| `framenest-catalog-offdevice.timer` | inactive | dead | not installed | not a writer on this host |

Capture units stay up and are not writers of the catalog: `kronika-capture-runner`, `kronika-capture-bridge`, and `kronika-capture-xvfb` are active/running/enabled. `kronika-capture-vnc` and `kronika-capture-view` are inactive/dead/static.

Stop rules for the later grant: stop the timer first, then the backup service, then `framenest.service`. Do not stop, start, or reload any capture unit. Do not `daemon-reload`. Do not change `/opt/framenest/current`. After the stops, require `is-active` inactive for those three units and `fuser` on `catalog.sqlite3` to show no pid. If a pid remains, do not delete.

## Checkpoint

Newest verified recovery point, from `/var/lib/framenest/catalog-backup-ops/status.json` (mode 600, owner framenest, 7959 bytes, mtime `2026-09-30 14:53:41 UTC`):

- bundle id `auto-20260930T145340Z-2c167119`
- attempt seq 86
- completed `2026-09-30T14:53:40Z`
- alembic revision `0035` on both the backup record and `last_successful_scheduled_restore_verification`
- bundle catalog size 1130496
- last scheduled attempt state `succeeded`
- derived restore-readiness `ready`

`FRAMENEST_CATALOG_BACKUP_ROOT=/var/lib/framenest/catalog-backups` is an exact whole-line match in the environment file (`grep -c -x` returned 1). That directory is the backup destination.

The live catalog is not that checkpoint. Live size is 1134592 and mtime is `2026-09-30 15:08:07 UTC`, after the bundle. A final quiescent backup is required inside the later grant, after writers are stopped and before any delete:

```text
sudo -n -u framenest --chdir=/opt/framenest/releases/5eddb81bd164207a86f23b3f236e36b66192930b env FRAMENEST_ENV_FILE=/etc/framenest/framenest.env /opt/framenest/releases/5eddb81bd164207a86f23b3f236e36b66192930b/.venv/bin/framenest-backup run-scheduled
```

Accept it only when the new status record is `succeeded`, alembic revision is `0035`, and the bundle size matches a fresh `stat` of `catalog.sqlite3` taken while writers are still stopped. If it does not, do not delete.

Off-device copy is not configured. `grep -c` of a non-empty `FRAMENEST_CATALOG_OFFDEVICE_DESTINATION_ID=` returned 0 (exit 1). `findmnt` of `/mnt/framenest-catalog-offdevice` produced no target (exit 1). `status.json` has no off-device success record. No off-device unit is installed.

## Rollback

S9 rollback is the same release plus a compatible empty catalog. It is not a restore of the deleted test catalog. ADR-0082 and `docs/UBUNTU_NUC_DEPLOYMENT.md` say rollback uses previous code and a compatible empty database, not deleted test data. `framenest-backup restore` writes only to an absent destination; production replacement is not implemented (BACKUP_AND_RECOVERY.md, Production Recovery). The verified bundle is the safety copy if the grant stops before delete, and the source for a later, separate recovery grant. That later recovery would import old catalog data and is outside this reset.

If `framenest-db migrate` fails after the delete, stop. Do not copy a bundle onto `/var/lib/framenest/catalog.sqlite3`. The only cleanup inside the same object set is removal of a partial new `catalog.sqlite3` and its own siblings, then stop for a new decision.

A restore drill, if a later grant wants one, keeps the documented shape and an absent disposable destination:

```text
framenest-backup restore --bundle /var/lib/framenest/catalog-backups/<bundle-id> --destination <absent-path>
```

It restores catalog rows and the Alembic revision recorded in the bundle. It does not restore media, covers, caches, `runtime-settings.json`, identity configuration, or secrets.

## Empty catalog

After the two database names and any of the six siblings are gone, and while `/var/lib/framenest` is still mode `700` owned by `framenest`:

```text
sudo -n -u framenest --chdir=/opt/framenest/releases/5eddb81bd164207a86f23b3f236e36b66192930b env FRAMENEST_ENV_FILE=/etc/framenest/framenest.env /opt/framenest/releases/5eddb81bd164207a86f23b3f236e36b66192930b/.venv/bin/framenest-db migrate
```

`framenest-db migrate` calls `upgrade_database_to_head`, which creates a missing private file and upgrades packaged Alembic history to head. Repository head revision is `0035` (`0035_research_requests_and_accounting.py`). This does not rewrite migration history. Expected private-catalog result from `private_state.py`: directory `0700`, database `0600`, owner equal to the service uid, link count 1. Then:

```text
sudo -n -u framenest --chdir=/opt/framenest/releases/5eddb81bd164207a86f23b3f236e36b66192930b env FRAMENEST_ENV_FILE=/etc/framenest/framenest.env /opt/framenest/releases/5eddb81bd164207a86f23b3f236e36b66192930b/.venv/bin/framenest-db status
```

Require `state` `at_head`, `current_revision` `0035`, `head_revision` `0035`.

## Identity configuration

Identity mapping is `FRAMENEST_IDENTITY_MAP` in `/etc/framenest/framenest.env`. The file is mode `640`, owner `root:framenest`, size 1990. A non-empty assignment of that key is present (`grep -c` returned 1). The value was not read. `runtime-settings.json` is absent, so there is no administrator overlay to keep or delete. The reset does not touch `/etc/framenest` or that overlay path. Identity configuration is outside the catalog and stays.

## Ordered reset sequence

Re-check every gate at execution time. Stop without deleting if the release pointer, database path, directory mode, or owner differs from this preflight.

1. Confirm pointer `/opt/framenest/current` still resolves to `.../releases/5eddb81bd164207a86f23b3f236e36b66192930b`, capture pointer still `94e605c17b881461fad3e22fd8c7fca32cb93976`, and `FRAMENEST_DATABASE_PATH` is still `/var/lib/framenest/catalog.sqlite3`.
2. Confirm `/var/lib/framenest` is mode `700`, owner `framenest:framenest`. Do not chmod.
3. `sudo -n systemctl stop framenest-catalog-backup.timer`
4. `sudo -n systemctl stop framenest-catalog-backup.service`
5. `sudo -n systemctl stop framenest.service`
6. Prove stopped: the three units inactive, and `sudo -n fuser /var/lib/framenest/catalog.sqlite3` reports no pid.
7. Run the final `framenest-backup run-scheduled` command above. Require success at revision `0035` and a size match. Record the new bundle id.
8. Re-stat the eight paths. Refuse symlinks and any link count other than 1. Delete only the regular files in that set (`sudo -n rm -f --` with those exact paths).
9. Run `framenest-db migrate`, then `framenest-db status`. Require `at_head` / `0035`. `stat` the new database: mode `600`, owner `framenest:framenest`, link count 1. Directory still `700`.
10. `sudo -n systemctl start framenest.service`. Require `is-active` active. `ExecStartPre` runs `framenest-production check-database-ready`.
11. `sudo -n systemctl start framenest-catalog-backup.timer`. Require it `active` / `waiting`.
12. Health: the same read-only probe the release helper uses, `sudo -n systemd-run --quiet --pipe --wait --collect --uid=framenest --gid=framenest --working-directory=/opt/framenest/releases/5eddb81bd164207a86f23b3f236e36b66192930b --property=EnvironmentFile=/etc/framenest/framenest.env /opt/framenest/releases/5eddb81bd164207a86f23b3f236e36b66192930b/.venv/bin/framenest-production check-health`.
13. Confirm the web pointer and capture pointer are unchanged, and the three capture services that were active are still active.

## Post-reset verification and S9 acceptance

Host checks: empty-catalog `framenest-db status` at `0035`; private modes; service active; backup timer waiting; helper-equivalent status still shows web `5eddb81…`, capture `94e605c…`, database `0035`. No old catalog import.

S9 integrated acceptance on that empty catalog, after this reset and on the already published NUC release, covers empty Timeline, empty Gallery, empty personal history, and the disabled Search and Research forms. Saved records, administrator review of real documents, and household publication wait for a later, separately authorized provider step. Rendered acceptance stays with the Cooperator.

## Prerequisites, residual unknowns, capability

Prerequisites already true on this read: release `5eddb81…` on the host and on public `main`, service active, catalog path and revision `0035`, state directory `700`, identity file outside the catalog, capture parked and separate, off-device writer absent, a revision-`0035` restore-verified bundle exists.

The grant must still do the quiescent backup in step 7, because the live file is newer than bundle `auto-20260930T145340Z-2c167119`.

Not unresolved, and not part of the delete set: nine July scratch files; the `chatgpt-page` tree; absent `runtime-settings.json`; unconfigured off-device mount.

Required capability for the later grant: Cooperator approval of one exact-object reset; gate SSH; `sudo -n` to stop and start only `framenest-catalog-backup.timer`, `framenest-catalog-backup.service`, and `framenest.service`; one `framenest-backup run-scheduled`; `rm` of only the eight paths; `framenest-db migrate` and `status`; one `check-health` transient unit. No capture action, no release-pointer change, no environment edit, no media or archive deletion, no import.

Changed files: none in `/Users/agile/Projects/framenest`. This report file only.
Validation: repository gate and the read-only host commands above. No product suite, no JS tests, no browser suite.
Git result: no fetch, stage, commit, or push.
Deviations: status fields were gathered through the gate rather than `framenest-release status`; revision was read with `sqlite3 -readonly` rather than `framenest-db status`; restore-readiness was derived from `status.json` rather than `framenest-backup status`. `sudo -K` was not run because this prompt forbids it.
Risk: the verified bundle does not byte-match the live catalog until the grant's final backup succeeds.
Smallest next step: Orchestrator issues one exact reset grant, containing the sequence above, for Cooperator approval before any execution.
Orchestration critique:
MEASURED: live `catalog.sqlite3` is 1134592 bytes at 15:08:07 UTC versus verified bundle `auto-20260930T145340Z-2c167119` at 1130496 bytes and 14:53:40 UTC; the grant must backup after writers stop and before delete, and must refuse the delete if the new bundle size does not match.
LEAD: none
Resolved Execution Issues / Near-Misses: an ungrouped `find` name search also matched SQLite sidecars inside `/var/lib/framenest/chatgpt-page`; no file contents were read, those names are omitted here, and later inventory stayed at maxdepth 1. One local `grep` pattern was rejected by fish because it contained `$`, and one remote `grep` was rejected by the gate because it contained `|`; both were retried with allowed forms. No host file changed.
Pre-Existing Failure Classification: none
Authority expiry: this terminal report ends the preflight exchange. No mutation, reset, deployment, or publication is authorized by it.
