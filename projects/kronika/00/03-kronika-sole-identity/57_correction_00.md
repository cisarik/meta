# Authoritative Worker prompt — Worker session 57, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `57`, exchange `01`. Stored under the
Meta filename mapping as `57_correction_00.md`, with report destination
`57_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 57
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-C7BREAD — bind the routine release backup reads to the unit environment
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The C7-B final deploy was refused fail-closed because the
engine's backup-status read resolved the wrong state root: the invoked backup
console resolves its configuration from the process environment only, while
the engine's service-account prefix supplies only the environment-file
selector. The readiness gate has therefore been reading the former-layout
backup roots since the routine engine was written, and only now — as the
former roots aged past the 48-hour freshness window — did the misread turn
into a refusal. The correction must bind the backup reads and the checkpoint
route to the same environment the systemd unit supplies, without changing any
message, status or the migration engine's checkpoint contract.

## The finding, exactly

Evidence from the live host (recorded by the Orchestrator on 2026-10-16):

- The canonical ops root `/var/lib/kronika/catalog-backup-ops/status.json`
  was written **today** (2026-10-16 03:20:41 UTC) by the daily
  `kronika-catalog-backup.service` run; its events tail carries
  `attempt_seq:130` and `scheduled_backup_and_restore_succeeded`; the
  canonical backups root holds `auto-20261016T032040Z-…` through
  `auto-20261014T193324Z-…`.
- The release check's read (`kronika-release check --release 7ebf495…`)
  returned `backup_restore_readiness: stale` with
  `last_scheduled_attempt` = `attempt_seq 124`, `completed_at_utc`
  `2026-10-12T18:56:25Z` — that is the status of the **former** ops root
  `/var/lib/framenest/catalog-backup-ops/status.json`, last written
  2026-10-12 18:56.
- Mechanism: `deploy/ubuntu/kronika_release.py`'s
  `cmd_remote_backup_status` and `cmd_remote_run_scheduled_backup` invoke
  `kronika-backup` through `service_account_prefix`, which sets only
  `env KRONIKA_ENV_FILE=<layout.env_file>`. The backup console
  (`src/kronika/adapters/cli/backup.py` →
  `src/kronika/infrastructure/persistence/catalog_backup_ops.py`) resolves
  its roots by direct process-environment lookups and falls back to its code
  defaults; it does not load the environment file. On the deployed `aee0a60`
  release those defaults are the former `/var/lib/framenest/…` roots, so the
  readiness gate and the pre-cutover checkpoint route read and write the
  former root. (The former root's bundles at 2026-10-12 09:07, 17:50 and
  18:56 are consistent with deploy checkpoints of that day.)
- Contrast: `kronika-db` calls `load_settings()`, which honors the
  `ENV_FILE` selector, so `cmd_remote_db_status` reads correctly; and
  `cmd_remote_production_cli` already runs its operations through a oneshot
  `sudo -n systemd-run --quiet --pipe --wait --collect --uid=… --gid=…
  --working-directory=… --property=EnvironmentFile=…` so the process
  environment matches the unit exactly. The backup routes never received
  that treatment.

## Correction specification

1. **One faithful backup-console helper.** Add a helper mirroring
   `cmd_remote_production_cli` that runs the release's backup console under
   the unit's environment — the established oneshot `systemd-run` pattern
   with `--uid=`/`--gid=`/`--working-directory=` and
   `--property=EnvironmentFile=<layout.env_file>` — restricted to the
   accepted operations (`status`, `run-scheduled`), failing closed on any
   other operation. Derive your own mechanism only if you can prove it binds
   the same environment; the process-environment-only form must not remain
   reachable for these operations.
2. **Rewire exactly the two routes.** `cmd_remote_backup_status` and
   `cmd_remote_run_scheduled_backup` use the new helper; their callers (the
   release check's readiness read, the routine deploy's pre-cutover
   checkpoint, and the identity migration's quiescent checkpoint) stay
   unchanged in behavior, message and exit semantics.
3. **Database route unchanged in contract.** `cmd_remote_db_status` keeps
   working exactly as today (its console honors the environment file); if
   your derivation shows an equally faithful alignment for it, propose it in
   the report with evidence, but do not change it in this commit unless the
   change is provably behavior-identical.
4. **Tests and pins.** Update every test that pins the old command shapes
   (`tests/contract/test_nuc_release_remote_contract.py` around its
   `kronika-backup status` and `cmd_remote_run_scheduled_backup` sites,
   `tests/contract/test_kronika_identity_migration.py` around its checkpoint
   assertion, and any further site your parse finds). Add the regression
   pin: both backup operations carry the unit `EnvironmentFile` binding, and
   the bare `env KRONIKA_ENV_FILE=` form no longer selects them. Keep every
   existing message and status assertion green.
5. **Mutation demonstration.** Revert one route to the direct process-env
   form → the new pin fails with its observed output; restore.
6. **Residual finding to report.** The backup console's configuration
   resolution diverges from its database sibling (process environment only
   versus environment-file support). Record it for disposition; do not
   change the console in this commit.

## Verified starting state, measured by the Orchestrator on 2026-10-16

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                7ebf4955e78731170477280c3b7f9f0cdd726e5a
Public main:                  7ebf4955e78731170477280c3b7f9f0cdd726e5a
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4968 passed, 8 skipped, 3 warnings, 0 failed
Focused release/migration contract modules: 407 passed
Retention module:             15 passed
JS baselines (unaffected sanity): 23 / 41 / 55 / 6 / 12 / 30; bounded non-browser JS glob 212
Host state (Orchestrator evidence): the canonical ops root is fresh (attempt
              130 today); the former root is frozen at attempt 124
              (2026-10-12T18:56:25Z); the C7-B final deploy is refused until
              this read is faithful.
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. No host contact; everything is repository-only.

## Authority

```text
Positive authority: edit `deploy/ubuntu/kronika_release.py` for exactly the
  backup-console helper and the two rewire sites; edit
  `tests/contract/test_nuc_release_remote_contract.py`,
  `tests/contract/test_kronika_identity_migration.py` and any further test
  module your parse shows pinning a changed command shape, naming it in the
  report before editing it; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a Part C
  scalar that your own measurement shows this correction moved, with the
  arithmetic cause stated; create exactly one local non-amended commit on
  `main`.

Negative authority: every other path; the backup console and the ops module;
`cmd_remote_production_cli` and the database route (keep their exact
  contracts); any document; any dependency or lockfile change; the `.ap`
  gitlink; any Alembic revision; any `.venv` operation; publication; push;
  force; amend; branch; stash; any NUC contact or SSH; any migration or
  deployment invocation; any provider, browser or capture contact. If a
  necessary change falls outside the positive scope, stop and report; do not
  widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 7ebf4955e78731170477280c3b7f9f0cdd726e5a --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`. JavaScript evidence
  uses only the documented ordinary invocation from the worktree root:
  `node --test tests/<name>.test.js`. Read-only Git inspection allowed;
  exactly one `git add <exact paths>` and one `git commit`; no push.

Dependency authority: none.
Git authority: exactly one local non-amended commit; no push, no branch, no tag.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.
Side-effect authority: reversible local repository mutation only.
Browser authority: none.
```

## Verification

1. **Reproduce the defect shape.** Before editing, show the current command
   strings: the fixed-backup command carries `env KRONIKA_ENV_FILE=…` only;
   the fixed-production command already carries the `systemd-run`
   `EnvironmentFile` binding. Report the literal shapes.
2. **Post-fix matrix.** Both backup operations run through the faithful
   helper: the exact `systemd-run` property set, the layout user/group, the
   release working directory, the accepted-operation refusal, and the
   unchanged JSON output path (stdout through `--pipe`). The database and
   production routes are byte-identical to before.
3. **Tests.** Every updated pin shown with its previous assertion; the new
   regression pin fails when either route is reverted (mutation
   demonstration) and passes on the final tree.
4. Run, through the declared routes: the focused release/migration contract
   modules (baseline 407), the full declared Python suite (baseline
   `4968/8/3/0`), the retention module (15) and the six JS suites plus the
   bounded glob as unaffected sanity.
5. Report every moved or removed site that no test exercises, and every
   consumer your derivation found that this prompt did not name.
6. State the exact commit SHA, `git diff --stat`, confirm Part A is
   byte-unmoved, Part B still empty, and show your own measurement for any
   Part C movement.

## Derivation and defect-pattern discipline

```text
 1. Derive site lists by PARSING each artefact. This prompt's anchors are
    locators, not an inventory.
 2. Resolve every cited line to its literal text BEFORE classifying it.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Verify each occurrence and each caller independently.
 5. Reject a guard that can pass vacuously when its input is absent.
 6. Never truncate an inventory. If output is truncated, disclose it.
 7. Check every mechanical probe against a known-impossible result.
 8. Regenerate every verification table at report time; never transcribe one.
 9. Open and classify every grep hit.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

**Collapsing pairs.** Do not collapse the faithful-environment form with the
process-environment form: the pin must distinguish them. Do not collapse the
checkpoint route's behavior with its command shape: the migration contract
(quiescent checkpoint, `state == "succeeded"`, bundle id capture) stays
identical.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a change would alter the database or production routes'
  contracts; if a message or status would change; if a frozen hash or Part A
  moves; if a Part C re-pin cannot be reproduced from your own measurement;
  if a `.venv` operation would be required; if context pressure reaches the
  point where a bounded rotation is cheaper than a degraded result.

Completion: the two backup routes bound to the unit environment with the
  regression pin and mutation demonstration; every updated assertion listed;
  focused modules, full Python suite, retention and JS sanity green through
  the declared routes; one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `57_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No further implementation, no second commit, no push, no
  publication, no refresh, no host contact and no later grant is authorized by
  it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `57` and exchange `01` unchanged. Then:

1. The reproduced defect shapes and the post-fix matrix.
2. Every updated assertion with its previous form; the mutation
   demonstration.
3. The residual finding (backup console versus database console
   configuration resolution).
4. Suites: focused, full Python, retention, JS sanity — counts, elapsed time,
   baseline differences.
5. `git diff --stat`, the commit SHA, Part A unmoved, Part B empty, Part C
   movement.
6. Every site no test exercises.
7. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification. Finish with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

## Mandatory reading

- `deploy/ubuntu/kronika_release.py` — `service_account_prefix`,
  `cmd_remote_production_cli`, `cmd_remote_backup_status`,
  `cmd_remote_run_scheduled_backup`, `cmd_remote_db_status`, the check's
  readiness read and both checkpoint callers.
- `src/kronika/adapters/cli/backup.py` and
  `src/kronika/infrastructure/persistence/catalog_backup_ops.py` — the
  configuration resolution, for the finding only.
- `tests/contract/test_nuc_release_remote_contract.py`,
  `tests/contract/test_kronika_identity_migration.py` — the pins.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`, `.ap/AP.md` §5,
  §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the matrices and suites at the
reported commit, then re-runs the C7-B final sequence with the corrected
engine: `status`, `check --release`, `deploy --release --yes` (whose own
pre-cutover checkpoint now writes the canonical root), the extension reload
and the rendered regression acceptance. No push, refresh or host contact is
authorized inside this prompt.
