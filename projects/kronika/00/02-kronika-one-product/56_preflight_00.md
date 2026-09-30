# S9 Database-Reset Read-Only Preflight — kronika-one-product, session 56

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 56
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Worker-Executed Preflight
Phase: preflight
Task identity: KRONIKA-ONE-PRODUCT-S9-RESET-PREFLIGHT
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: preparation for an irreversible, Cooperator-authorized empty-database reset; evidence must be exact and sanitized
Recommended context capacity: approximately 250k tokens
Independence required: no

## Goal (one outcome)

Produce the read-only preflight for the accepted S9 empty-database transition on
the released state `5eddb81bd164207a86f23b3f236e36b66192930b`, so that the
Orchestrator can issue one exact-object reset grant: the exact objects to reset,
verified prerequisites, a checkpoint and rollback, the exact stopped-writer
sequence, post-reset verification, and the remaining unknowns. This preflight
performs no mutation and does not authorize the reset; PASS only recommends a
separately authorized reset.

## Accepted boundary (binding; from the repository)

- `AGENTS.md` lines 280–283: the empty-database transition requires its own
  exact-object reset grant after writers stop; it grants no deletion of media,
  profiles, identity configuration, secrets or archives, and no import of the
  old test databases.
- `docs/adr/0082-kronika-one-product-and-private-records.md` section
  “Empty-Database and Deployment Transition”: identify exact database/WAL/SHM
  files, stop all writers, delete only those objects, preserve source media,
  profiles, identity configuration, secrets, other state and Git/Meta archives,
  create the empty database through normal schema/migrations, never rewrite
  migration history.
- `docs/UBUNTU_NUC_DEPLOYMENT.md` lines 81–90: preflight identifies **both old
  application databases** and their WAL/SHM files; all writers stop before
  deletion; no whole state directory, media, profile, identity configuration,
  secret or archive is removed; normal migrations create the empty catalog;
  migration history and the helper’s explicit `migration-required`
  continuation remain; rollback uses previous code and a compatible empty
  database, not deleted test data.
- Capture is parked and out of scope: its account, state, browser, profile and
  services are untouched (`/var/lib/kronika-capture`, `/opt/framenest/capture-current`,
  capture services). The web release pointer and release helper must not be
  modified by the reset.

## Repository gate

```text
Root: /Users/agile/Projects/framenest
Remote: https://github.com/cisarik/framenest.git
Branch: feat/kronika-one-product
Expected HEAD: 5eddb81bd164207a86f23b3f236e36b66192930b
Expected parent: ef9920333013f3f70bf5e3443be2e51814f6b9c3
AP gitlink and .ap HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
Required state: clean index and worktree including untracked files
```

Public `main` equals the baseline (Orchestrator-observed 2026-09-30 via
`git ls-remote`); one read-only `git ls-remote` re-check is permitted. No Git
write of any kind. Classify any difference per RF-12 and stop on unexplained
divergence.

## Reading

- AP: `.ap/AP.md` (RF-03, RF-12, RF-13, RF-18, Stopping Conditions),
  `.ap/AP_WORKER.md` (Reporting), `.ap/PROMPT_CONTRACTS.md` (Worker Report
  Header).
- Project: `AGENTS.md` (Security Boundaries, Product Boundaries),
  `docs/UBUNTU_NUC_DEPLOYMENT.md`, `docs/BACKUP_AND_RECOVERY.md`,
  `docs/adr/0082-kronika-one-product-and-private-records.md`,
  `docs/adr/0033-catalog-backup-and-recovery-foundation.md`,
  `docs/adr/0052-automated-catalog-backup-retention-and-restore-verification.md`,
  `docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md`,
  `docs/WORKER_EXECUTION_CONTRACT.md` (execution boundary).
- Code: `src/framenest/infrastructure/persistence/migrations.py`,
  `private_state.py`, `src/framenest/adapters/cli/backup.py` (create/verify/
  restore/verify-restore surfaces), `deploy/ubuntu/framenest_release.py`
  (status/check only).
- Trace: `/Users/agile/meta/projects/kronika/00/02-kronika-one-product/`
  `46_report_00.md` (worked deployment example), `55_report_00.md`, and the
  latest `00_notes.md` entries.

## Host access and hard boundaries

- NUC access only through
  `scripts/operator/network/framenest_nuc_worker_gate.fish`: first `--probe`;
  then bounded `--command` invocations. The three `FRAMENEST_NUC_SSH_*` names
  are exported in the Cooperator’s shell profile; never print their values or
  the agent socket. BatchMode SSH only.
- Read-only commands only. `sudo -n` read-only commands are permitted; never
  run `sudo -v` or `sudo -K` (Cooperator-owned lifecycle).
- Forbidden without exception: starting/stopping/restarting/reloading any
  service; creating, deleting, moving, truncating or chmod-ing any file;
  running a backup create/restore; any write to `/opt/framenest`,
  `/var/lib/framenest`, `/etc`, the release trees or the capture state;
  reading credentials, tokens, browser profiles or `private/**`.
- Sanitized output: report file names, modes, owners, sizes and counts; never
  print secrets, tokens, full environment files, addresses or fingerprints.
  When reading the service environment file, extract only
  `FRAMENEST_DATABASE_PATH` (for example with a single bounded `grep`); do not
  print the rest.
- The broad Python suite and browser suites are not run; no JS tests are
  required. No product source is edited.

## Evidence to establish (per item: value + source + limitation)

1. Release and service state: `framenest-release status` (`active_release`,
   `web_release`, `capture_release`, `service_active`,
   `database_revision`, `backup_restore_readiness`).
2. Configured catalog path used by the deployed service (env extraction as
   above) and the running release tree path (`/opt/framenest/current` target).
3. Exact database object inventory in `/var/lib/framenest`: every candidate
   database file and sibling (`catalog.sqlite`, `catalog.sqlite3`, any
   `-wal`, `-shm`, `-journal`), each with mode, owner, size, link count and
   mtime; classify each as active catalog, residue, or unrelated. Include the
   `runtime-settings.json` object if present and classify it as
   configuration to preserve.
4. Writer inventory: which units can write the catalog
   (`framenest.service`, `framenest-catalog-backup.service`,
   `framenest-catalog-backup.timer`, any offdevice unit presence), their
   active state, and the exact commands the reset must use to stop writers and
   to prove they are stopped. Note that the acquisition runners run inside
   `framenest.service`; the capture services write only capture state.
5. Checkpoint: the newest verified recovery point and its evidence
   (`framenest-backup status` read-only; bundle id, attempt seq,
   restore-readiness, whether restore-verification covered the current
   revision `0035`); whether a final pre-reset backup is recommended and its
   exact command and destination; off-device configuration state.
6. Rollback: the exact documented restore procedure from a verified bundle
   (command shape and destination rules from `docs/BACKUP_AND_RECOVERY.md` and
   the backup CLI), what it restores and what it cannot restore, and the
   constraints for using it after the reset.
7. Empty-catalog creation: the exact command sequence to create and migrate a
   fresh empty catalog at the configured path as the service account (release
   tree `.venv` executable, `FRAMENEST_ENV_FILE`), and the private-catalog
   expectations (directory `0700`, database `0600`, `at_head` `0035`).
8. Identity configuration: where the deployed workspace identity mapping is
   configured and how it is preserved by the reset (it is configuration, not
   catalog data); confirm the reset scope excludes it.
9. Proposed exact reset sequence: ordered steps with exact paths and commands
   (stop, verify stopped, delete only the exact objects, create/migrate,
   verify empty and `at_head`, start, verify helper status and health), the
   stop rules, and the exact set of files that must remain untouched.
10. Post-reset verification list and what S9 integrated acceptance will then
    cover on the empty catalog (empty Timeline/Gallery states, personal
    history, disabled research forms; saved records require the later
    separately authorized provider step).

## Deliverable and report

Return PASS when the evidence is sufficient to recommend one exact reset grant;
PARTIAL when a material prerequisite, rollback detail or mapping remains
unresolved; BLOCKED when the reset must not be authorized. Include the
classified inventory table, the proposed exact mutation boundary (paths and
counts), prerequisites, checkpoint, rollback, stop rules, the ordered reset
sequence, residual unknowns, and required capability for the later grant.

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 56, 01), and carries the compact core:
status; `Phase-qualified result: not-applicable`; start and end commit
`5eddb81…` (unchanged); changed files (none in the repository; the report file
only); evidence with exact commands and results; `Report justification:
new-evidence`; deviations/risks/missing evidence; smallest next step (the
reset grant); critique; `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` (or none); `Logical-whole closure:
not-closed`; authority expiry. State explicitly that no mutation was performed
and that the preflight does not authorize the reset.

If the client’s mode prohibits the report write, preserve the complete content
in chat, mark the delivery limitation PARTIAL, and stop.

## Delivery record

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 56_preflight_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 56_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Stopping conditions

Stop honestly (PARTIAL/BLOCKED) on a failed repository gate, gate/transport
failure after one classification attempt, an unexplained divergence, a required
read that would expose secrets, any command that would mutate state, or an
unresolved conflict between the accepted reset boundary and the actual host
state. Do not improvise the reset; do not touch capture; do not run any
service action.

Authority expiry: the terminal report ends this preflight exchange; no
mutation, reset, deployment or publication is authorized by it.
