# S9 Empty-Catalog Transition — Fresh Independent Review (kronika-one-product, session 57)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 57
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S9-TRANSITION-REVIEW
Delivery route: manual Cooperator delivery
Reasoning recommendation: Extra High — independent review of an irreversible, destructive catalog transition on a real host; exactness and preservation evidence
Recommended context capacity: approximately 250k tokens
Independence required: yes

## Acceptance record

```text
Acceptance candidate: the S9 empty-catalog transition state at web release
  5eddb81bd164207a86f23b3f236e36b66192930b (no repository commit changed)
Acceptance owner map: host state only; trace evidence 56_preflight_00.md,
  56_report_00.md and the 00_notes.md S9 entries are evidence, not authority
Acceptance allowlist: read-only review; gate-only host access; one temporary
  probe root is not required and is not granted; no mutation of any kind
Acceptance risk claims: the fixed claims C1–C8 below
Acceptance control matrix: the controls in this grant
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none beyond the controls below
Out-of-scope observations: ledger-candidates
```

This session did not implement, approve or execute the reset. The execution
records are claims; verify them. No correction authority is granted.

## Security audit record

```text
Security task class: focused independent review (data-integrity and
  private-state specialization) of the empty-catalog transition
Owned/authorized target: the NUC host state through the worker gate, read-only
Scope: the exact-object reset, the option-B registration completion, the new
  catalog, preservation invariants, release/service integrity, side effects
Exclusions: services actions, file writes, capture state, credentials,
  private/**, provider calls, media content reads, correction
```

Threat model: assets are the catalog data boundary (old test data is
deliberately destroyed; media files, profiles, identity configuration, secrets
and archives must survive), the private-catalog mode invariant, and the
release/service identity. Attacker/local-actor model is limited to operator
error: deleting too much, importing old rows, leaving the app down, or
weakening modes. Abuse cases: wrong deletion set, missed WAL/SHM file,
unverified backup before delete, old-data import, mode regression or symlink
substitution, service left in a restart loop, capture disturbed, env edits
beyond the one agreed line.

## Access and hard boundaries

- NUC access only through
  `scripts/operator/network/framenest_nuc_worker_gate.fish`: `--probe` first,
  then bounded `--command` invocations. The three `FRAMENEST_NUC_SSH_*` names
  are exported in the Cooperator's shell profile; never print values or the
  agent socket. BatchMode SSH only.
- Read-only commands only; `sudo -n` read-only commands are permitted; never
  `sudo -v`, `sudo -K`, service start/stop/restart/reload, `daemon-reload`,
  `rm`, `chmod`, `sed -i` or any file write. No backup create/restore. Do not
  read credentials, tokens, browser profiles, `private/**` or media bytes.
- Sanitized output only: names, modes, owners, sizes, hashes, counts. Do not
  print secrets or the full environment file; extract single keys only.
- Repository access is read-only; no Git write; at most one `ls-remote`.

## Fixed claims and required verdicts

**C1 — Reset object exactness.** The only database objects removed were
`/var/lib/framenest/catalog.sqlite3` and the zero-byte
`/var/lib/framenest/catalog.sqlite`, with their six `-wal`/`-shm`/`-journal`
siblings absent before and after; the current paths are absent; nothing else
in `/var/lib/framenest` was removed (scratch files, backup and ops
directories, `chatgpt-page`, caches, covers, staging directories still
present). State the limitation that the deleted objects are verified by
recorded evidence plus current absence, not by re-observation.

**C2 — Checkpoint before deletion.** The pre-delete quiescent bundle
`/var/lib/framenest/catalog-backups/auto-20260930T155720Z-f9ead1a3/` exists
with `catalog.sqlite3` and `manifest.json`; hash the bundle catalog and verify
it matches the recorded backup digest
`fb2bf1f60be73f0e81c8a86d1d3ff43b982152f298a2e9d765f7a6cd64797a76` and size
`1134592`; read-only query the bundle to confirm it holds the pre-reset
revision `0035` and exactly one library row (`528f7733-…`, "FrameNest
Published Uploads", `/srv/media/framenest-published`).

**C3 — New catalog correctness.** `/var/lib/framenest/catalog.sqlite3` is a
regular file `600 framenest:framenest` nlink 1; `/var/lib/framenest` is `700
framenest:framenest`; `framenest-db status` (or a read-only equivalent)
reports `at_head` `0035`; `kronika_records` and `logical_media` are empty;
exactly one library and one device row exist, matching the documented
registrations (`048cb4a9-b67e-4140-a289-839f0c0e646e` "FrameNest Published
Uploads" `/srv/media/framenest-published`; `09a2cc80-2a4e-4953-a928-0bd051d18e64`
"FrameNest NUC").

**C4 — Option-B completion exactness.** The two registration rows came from
the supported commands (device and library names/root match the frozen
configuration intent); `FRAMENEST_UPLOAD_PUBLICATION_LIBRARY_ID` in
`/etc/framenest/framenest.env` equals the registered library id; the file's
key set is consistent with the deployment record; state the limitation that
no byte baseline of the pre-change environment file exists, so "exactly one
line changed" is verified against recorded values, not a byte diff.

**C5 — Release and service integrity.** `/opt/framenest/current` resolves to
`5eddb81bd164207a86f23b3f236e36b66192930b`; public `main` equals that SHA;
`/opt/framenest/capture-current` is `94e605c17b881461fad3e22fd8c7fca32cb93976`;
`framenest.service` is active/running without a restart loop (no restart
events after the recorded successful start; `NRestarts` stable);
`backup_restore_readiness` is `ready`; the catalog backup timer is active and
waiting.

**C6 — Preservation invariants.** The media files under
`/srv/media/framenest-published` are still present (report a sanitized count
and the newest mtime; do not read contents); the three capture services
(`kronika-capture-runner`, `kronika-capture-bridge`, `kronika-capture-xvfb`)
are still active; `FRAMENEST_IDENTITY_MAP` is still present in the
environment file (do not read its value); release pointers unchanged; no
media or records were imported (consistent with C3's empty tables).

**C7 — Side effects and stability.** No acquisition-runner failure events
after the recorded recovery time (search the journal since 16:12 UTC for
`RUNNER_ITERATION_FAILED`); no unexpected unit or journal anomalies around the
reset window; the repository is clean at `5eddb81…` with an unchanged AP pin
`73e20ef80b88700d5fcbc397cd8edd4fc425869f`.

**C8 — Cooperator acceptance linkage.** The recorded empty-catalog rendered
acceptance (items 1–9 PASS, item 10 NOT TESTED due to no records) is
consistent with the current empty state; the missing item is correctly
carried to the provider step and is not claimed as passed.

## Required controls (minimum)

```text
git rev-parse HEAD 'HEAD^{tree}'; git status --porcelain --untracked-files=all
GIT_TERMINAL_PROMPT=0 git ls-remote <remote> refs/heads/main
gate --probe; readlink -n /opt/framenest/current; readlink -n /opt/framenest/capture-current
stat of /var/lib/framenest and its catalog and siblings
sha256sum of the safety bundle's catalog.sqlite3
sqlite3 -readonly queries on the bundle and the live catalog (counts and rows)
systemctl is-active/show for framenest.service, the backup timer, the three capture units
journalctl read-only for the reset window and the runner-failure search
grep of single env keys (Publication library id, identity map presence)
```

Use only bounded commands without shell metacharacters beyond what the gate
permits. Prefer the repository's own sanitized forms where available. Do not
run the Python or JavaScript suites; no product tests are relevant to this
host-state review. Browser/rendered evidence is not re-run (Cooperator-owned).

## Verdict rules and report contract

All C1–C8 established yields `acceptance-PASS`; otherwise `PARTIAL` or
`BLOCKED` with the exact missing evidence and the limitations above stated.
Findings use the full finding record; out-of-scope observations become
non-authorizing ledger candidates. This review never repairs.

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 57, 01), and includes the compact core,
the Acceptance record, per-claim verdicts with evidence, the control matrix
results, limitations, residual risk, critique, and authority expiry. Use
`Phase-qualified result: acceptance-PASS | not-applicable`,
`Logical-whole closure: not-closed`, `Report justification: final-acceptance`.

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
Downloadable prompt filename: 57_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 57_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Stopping conditions

Stop (PARTIAL/BLOCKED) on a failed gate, unexplained divergence, any command
that would mutate state, a required read that would expose secrets, or a
finding that needs correction authority.

Authority expiry: the terminal report ends this review exchange.
