# Authoritative Worker prompt — Worker session 63, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `63`, exchange `01`. Stored under the
Meta filename mapping as `63_implementation_00.md`, with report destination
`63_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **C9-B/2**, the second of three C9-B sub-grants. It retools the
release engine to one canonical layout: the former-layout constants,
selectors, aliases, defaults and fallbacks go, the probe shape stays and
validates only the canonical unit, and an absent capture pointer stays
absent. The one-time migration commands are already gone (C9-B/1); the
living-truth document work is C9-B/3.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 63
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C9B2 — canonical layout only
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. A default argument left on a retired constant would make a
caller that omits the layout operate the deleted tree; the retool list is
long and must be resolved symbol-by-symbol in the current, already-shrunken
engine.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/61_report_00.md`
section 1 is the normative source for this grant, section 7 for its proof and
section 8 for the boundary. **The line numbers in that report refer to the
pre-C9-B/1 engine.** Resolve every site by SYMBOL in the current tree; the
lists below are the authoritative scope, not an inventory.

1. **One canonical layout.** A single canonical `WebLayout` replaces the pair.
   Its fields are today's `NEW_WEB_LAYOUT`: `kronika.service`, user/group
   `kronika`, `/opt/kronika/releases`, `/opt/kronika/current`,
   `/etc/kronika/kronika.env`, `/var/lib/kronika`, `/var/cache/kronika`,
   `/run/kronika`, `/run/kronika/kronika.sock`. The only capture pointer is
   `/opt/kronika/capture-current` and its release root is
   `/opt/kronika/releases`.
2. **Remove as selectors.** `OLD_WEB_LAYOUT`, `WEB_LAYOUTS`,
   `OLD_CAPTURE_CURRENT`, `CAPTURE_POINTERS`, and the module constants that
   are aliases of the retired layout: `SERVICE`, `SERVICE_USER`,
   `SERVICE_GROUP`, `RELEASE_ROOT`, `CURRENT`, `CAPTURE_CURRENT`, `ENV_FILE`.
3. **Retarget every builder default** that currently equals `OLD_WEB_LAYOUT`,
   `SERVICE`, `RELEASE_ROOT` or `CAPTURE_CURRENT`, resolved by symbol:
   `release_dir`, `staging_dir`, `cmd_remote_readlink_current`,
   `cmd_remote_df_capacity`, `cmd_remote_capture_current`,
   `service_account_prefix`, `cmd_remote_db_status`, `cmd_remote_backup_cli`,
   `cmd_remote_backup_status`, `cmd_remote_production_cli`,
   `cmd_remote_check_database_ready`, `cmd_remote_check_health`,
   `cmd_remote_run_scheduled_backup`, `cmd_remote_atomic_switch`,
   `cmd_remote_atomic_switch_capture`, the systemctl/journalctl builders,
   `read_current_release`, `read_optional_release_sha`,
   `read_backup_readiness`, `read_db_current_revision`, `verify_capacity`,
   `release_scoped_console_script`, `verify_unit_executables`,
   `_verify_cutover`, `_wait_ready`, `_rollback`. A parse must find no
   remaining routine builder default naming `framenest.service`,
   `/opt/framenest/current`, `/opt/framenest/capture-current`,
   `/opt/framenest/releases`, `/etc/framenest/framenest.env`,
   `/var/lib/framenest`, `/var/cache/framenest` or `/run/framenest`.
4. **Keep the probe shape.** `WebLayout`, `WebLayoutReading`,
   `HostLayoutState`, `parse_web_layout_probe`, `select_web_layout` and
   `cmd_remote_layout_probe` stay, but validate only the canonical unit. The
   new single-layout test must fail if a second candidate is added to the
   candidate set that selection consumes.
5. **Capture pointer.** `resolve_capture_pointer` treats a missing pointer as
   absent (`"none"` with the canonical capture-pointer path and the canonical
   release root); it never falls back to the retired path. The new
   capture-pointer test must fail if it does.
6. **Accepted release roots.** `accepted_release_roots` returns only
   `/opt/kronika/releases`; the on-host `_remote-extract` and
   `_remote-relocate-venv-shebangs` helpers accept writes only under it.
7. **Module docstring.** The engine's opening description still says deploy
   moves `/opt/framenest/current` and `framenest.service`; correct it to the
   canonical layout in the same commit.
8. **Tests, same commit.** Retool every module whose fixtures parametrize
   `WEB_LAYOUTS` or pin the removed constants — the planning report names
   `test_nuc_release_remote_contract.py`, `test_kronika_capture_services.py`,
   `test_kronika_cli_and_release_readers.py`,
   `test_nuc_release_source_contract.py`; name every further module before
   editing it. Add the new single-layout test, the capture-pointer test and
   the one-root assertion.

## Verified starting state, measured by the Orchestrator on 2026-10-18

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                f2c4624ded775e3446bfafef4a5a413253a03136
Public main:                  5b86d896b3ea03f89fef2c90f7af2c121d0ef915 (C9-B/1 unpublished by design)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4714 passed, 8 skipped, 3 warnings, 0 failed
Focused five-module set:      162 passed
Retention module:             15 passed
JS baselines:                 23 / 41 / 55 / 6 / 12 / 30; bounded glob 212
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only work: no host contact, no browser, no deployment.

## Authority

```text
Positive authority: edit `deploy/ubuntu/kronika_release.py` for exactly the
  canonical-layout retool in the specification; edit every test module your
  parse shows pinning a removed surface, naming each non-obvious module in the
  report before editing it; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a Part C
  scalar that your own measured retention failure shows this commit moved,
  with the arithmetic cause stated; create exactly one local non-amended
  commit on `main`.

Negative authority: every other path; every keep of the planning report
  section 4 (marker tables and readers, `POETRY_BIN`/`CPYTHON_BIN`, the
  sanitizer needle, the Alembic shim and `versions/`, `local_state_migration.py`
  and its refusal, `DEPLOYMENT_STATE_DIR`, `STATE_DIR_NAME`, `FrameNest*`
  class residues, Part A files); the C9-B/1 historical sentences and any other
  document edit (C9-B/3); any feature change; any dependency or lockfile
  change; the `.ap` gitlink; any Alembic revision; any `.venv` operation;
  publication; push; force; amend; branch; stash; any host or browser action.
  If a necessary change falls outside the positive scope, stop and report; do
  not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline f2c4624ded775e3446bfafef4a5a413253a03136 --operation <id> [-- <argv>]
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

1. **Single-layout matrix.** One canonical layout is defined; selection
   consumes exactly it; no routine builder default names a former-layout
   path; the probe functions exist with their shape.
2. **Capture pointer.** A missing pointer resolves to absent, not to the
   retired path; the live pointer read stays canonical.
3. **Accepted roots.** One root only, and the remote helpers are consistent
   with it.
4. **Keeps.** Marker-reader tests, the Alembic shim tests, the local-state
   refusal tests and the packaging tests stay green without being edited
   except where a fixture literally built a removed constant, which is named.
5. **Mutation demonstrations**, each named with its observed failure:
   (a) put a second candidate into the set that selection consumes → the
   single-layout test fails; (b) make `resolve_capture_pointer` return
   `/opt/framenest/capture-current` when no pointer exists → the
   capture-pointer test fails.
6. **Measurement discipline.** The retention failure is measured before the
   re-pin; after values are not pre-written; no counted comment is added.
7. Run, through the declared routes: the touched contract modules (named in
   the report), the full declared Python suite against `4714/8/3/0`, the
   retention module, the packaging module, and the JS suites plus bounded
   glob as unaffected sanity.
8. Report every moved or removed site that no test exercises.
9. State the exact commit SHA, `git diff --stat`, Part A byte-unmoved, Part B
   still empty, and the Part C movement with its measured cause.

## Derivation and defect-pattern discipline

```text
 1. Derive site lists by PARSING each artefact. The planning report's line
    numbers are stale; resolve symbols in the current tree.
 2. Resolve every cited symbol to its literal definition BEFORE editing it.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Verify each occurrence and each caller independently.
 5. Never retarget by name similarity; verify each default and each caller.
 6. Never truncate an inventory. If output is truncated, disclose it.
 7. Check every mechanical probe against a known-impossible result.
 8. Regenerate every verification table at report time; never transcribe one.
 9. Open and classify every grep hit.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

**Collapsing pairs.** Do not collapse the canonical layout retool with the
keep list; do not collapse a removed constant with the marker spellings that
contain the same substring; do not collapse the sanitizer needle with a path
the engine writes.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a keep would need editing beyond a fixture that literally built a
  removed constant; if a former-layout path would remain in a routine builder
  default outside the keeps; if a frozen hash or Part A moves; if a Part C
  re-pin cannot be reproduced from your own measurement; if context pressure
  reaches the point where a bounded rotation is cheaper than a degraded result.

Completion: the canonical retool with the probe shape kept, the absent-pointer
  behaviour, the one-root helper, the corrected docstring, the retooled tests
  and the three new proofs, the measured retention re-pin, the two mutation
  demonstrations, and one local commit.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `63_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `63` and exchange `01` unchanged.
Then:

1. The retool matrix: every removed selector/alias, every retargeted default,
   the kept probe shape, the absent-pointer behaviour, the one-root helper —
   with the parse evidence for each.
2. The retooled test modules and the three new proofs.
3. The measured retention re-pin with the arithmetic cause.
4. The two mutation demonstrations with their named observed failures.
5. Suites: touched modules, full Python, retention, packaging, JS sanity —
   counts, elapsed time, baseline differences.
6. `git diff --stat`, the commit SHA, Part A unmoved, Part B empty, Part C
   movement.
7. Every site no test exercises.
8. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification. Finish with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

## Mandatory reading

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/61_report_00.md`
  sections 1, 4, 7 and 8 in full.
- `deploy/ubuntu/kronika_release.py` — the whole engine, as it stands after
  C9-B/1.
- `tests/contract/test_nuc_release_remote_contract.py`,
  `tests/contract/test_kronika_capture_services.py`,
  `tests/contract/test_kronika_cli_and_release_readers.py`,
  `tests/contract/test_nuc_release_source_contract.py`,
  `tests/contract/test_kronika_identity_retention.py`,
  `tests/contract/test_chatgpt_page_packaging.py`.
- `tests/contract/test_local_state_migration.py` (read-only keep),
  `src/kronika/infrastructure/persistence/alembic_compat.py` (read-only keep).
- `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`, `.ap/AP.md` §5,
  §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, the parked capture state or
profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the retool matrix, the three proofs,
the mutations and the retention arithmetic at the reported commit, then
issues C9-B/3 (living truth). No push, publication, refresh, deployment or
host contact is authorized inside this prompt.
