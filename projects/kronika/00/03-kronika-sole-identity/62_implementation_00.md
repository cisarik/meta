# Authoritative Worker prompt — Worker session 62, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `62`, exchange `01`. Stored under the
Meta filename mapping as `62_implementation_00.md`, with report destination
`62_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **C9-B/1**, the first of three C9-B sub-grants. It deletes the
one-time identity and capture-path migration commands and every helper that
exists only for them, plus the living sentences that still instruct the
operator to run those commands. The routine dual-layout selection still
exists when this commit lands — it is C9-B/2's removal, and the "no routine
route can select a deleted layout" proof is not claimed here.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 62
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C9B1 — delete the one-time migration commands
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The deletion set is large, the survivor set is precisely
constrained (marker readers, the Alembic shim, the local-state refusal, the
routine remote helpers), and the retention re-pin arithmetic must be measured,
not written in advance.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/61_report_00.md`
(session-61 planning report) sections 2, 4, 5, 6, 7 and 8 are the normative
source, refined by section 1 only where a helper is used solely by the
commands below. Derive every site by parsing; the lists here are the
authoritative scope, not a substitute for resolution.

**Delete — identity migration machinery.** `MIGRATION_DIRECTORY` and the
journal/recovery-manifest paths, `MIGRATION_PHASES`, `MIGRATION_UNIT_ARTIFACTS`,
`MIGRATION_OLD_TO_NEW_ROOTS`, `MIGRATION_SEGMENT_RENAMES`,
`MIGRATION_FROZEN_PATH_PREFIXES`, `IDENTITY_ENVIRONMENT_PATH_SUFFIXES`,
`IDENTITY_ENVIRONMENT_OPAQUE_SUFFIXES`, the engine-level
`COMPATIBLE_ENVIRONMENT_PREFIX`; the typed transformer (`EnvironmentAssignment`,
`EnvironmentTransformation`, `classify_environment_key`, `transform_path_value`,
`transform_environment_text`); the observation/plan/orchestration machinery
(`ObservedUnit`, `MigrationObservation`, `MigrationPlan`, `RemoteMigrationHost`,
`parse_tailscale_serve_status`, `classify_unit_path_token`,
`transform_unit_dropin_text`, `transform_sudoers_text`, `run_migration_apply`,
`read_migration_observation` including its private-store handling); the
`migrate-identity` CLI handlers and their parser entries.

**Delete — capture-path migration.** `CapturePathUnit`, `CapturePathPlan`,
`_require_former_capture_pointer`, `observe_capture_path_plan`,
`_print_capture_path_plan`, `_apply_capture_path_plan`,
`_remove_capture_path_trees`, `_enforce_capture_path_gates`,
`CAPTURE_PATH_SCRATCH`, `CAPTURE_PATH_REMOTE_ENGINE`, `CAPTURE_PATH_PLAN_VERSION`,
the `migrate-capture-paths` CLI handlers and their parser entries, and every
remote command builder used only by the two migrations.

**Caller rule.** Before deleting any helper, produce its complete caller list
from a parse of the current tree. Any routine caller (status, check, deploy,
rollback, activate-capture, rollback-capture, `_remote-extract`,
`_remote-relocate-venv-shebangs`, the deploy lock, the readiness checks) stops
that deletion and is reported. Never delete by name similarity.

**Do not touch.** The accepted marker tables and `read_release_markers` and
friends (lines 46–67, 1492–1617); `POETRY_BIN` and `CPYTHON_BIN`;
`_assert_logs_sanitized` and its `/etc/framenest/credentials` needle;
`alembic_compat.py` and the `versions/` directory; the entire
`local_state_migration.py` module including
`refuse_silent_legacy_state_replacement` and its `development.py` callers;
`DEPLOYMENT_STATE_DIR` in `src/kronika/infrastructure/ai/chatgpt_page/budget.py`;
`STATE_DIR_NAME` in `src/kronika_capture/config.py`; `FrameNest*` class
residues; `X-FrameNest-Request` strings; every frozen document and Part A
file; the routine dual-layout selection itself; the schema
`migration-required` continuation prose; the marker-reader sentence at
runbook 1059–1061 and the frozen tooling paths at 609–610.

**Tests.** Delete `tests/contract/test_kronika_identity_migration.py` only
after confirming that every keep in the planning report section 4 still has
its pin in another module (marker pins live in
`test_kronika_cli_and_release_readers.py`). Retool every other module whose
fixtures reference deleted symbols, naming each module in the report before
editing it. Add the new parser-surface test: after this commit the parser
exposes exactly `status`, `check`, `deploy`, `rollback`, `activate-capture`,
`rollback-capture`, and the hidden `_remote` with `_remote-extract` and
`_remote-relocate-venv-shebangs`.

**Documents.** Replace the runbook's "Capture Path Migration (Explicit; Not A
Routine Release)" section (273 onward) and its "Identity Migration (Non-Routine;
Not This Continuation)" section (1137 onward) with one explicit historical
sentence each: the cut ran, the commands are gone, routine status/check/deploy/
rollback address only the canonical layout and do not migrate. Fix
`deploy/ubuntu/README.md`'s `migrate-capture-paths` sentence the same way and
update the pin in `tests/contract/test_nuc_release_docs.py` in the same commit.
Sweep every other document and living sentence that names either deleted
command and fix or classify it in the report.

## Verified starting state, measured by the Orchestrator on 2026-10-17

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                5b86d896b3ea03f89fef2c90f7af2c121d0ef915
Public main:                  5b86d896b3ea03f89fef2c90f7af2c121d0ef915 (published)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      5016 passed, 8 skipped, 3 warnings, 0 failed
Retention module:             15 passed
JS baselines:                 23 / 41 / 55 / 6 / 12 / 30; bounded glob 212
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only work: no host contact, no browser, no deployment.

## Authority

```text
Positive authority: edit `deploy/ubuntu/kronika_release.py` for exactly the
  deletion set above; edit `tests/contract/*` for the parser-surface test, the
  deleted migration test module, the retool of modules pinning deleted
  symbols, the docs pin, and the re-pin of
  `tests/contract/test_kronika_identity_retention.py` Part C scalars that your
  own measured retention failure shows this commit moved (with the arithmetic
  cause stated); edit `docs/UBUNTU_NUC_DEPLOYMENT.md` and `deploy/ubuntu/README.md`
  for exactly the historical-sentence replacements; create exactly one local
  non-amended commit on `main`.

Negative authority: every other path; the do-not-touch list above; the routine
  dual-layout selection and its constants (C9-B/2); any other document
  rewrite; any feature change; any dependency or lockfile change; the `.ap`
  gitlink; any Alembic revision; any `.venv` operation; publication; push;
  force; amend; branch; stash; any host or browser action. If a necessary
  change falls outside the positive scope, stop and report; do not widen
  scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 5b86d896b3ea03f89fef2c90f7af2c121d0ef915 --operation <id> [-- <argv>]
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

1. **Parser surface.** The new test proves the exact remaining subcommand set
   above and that `migrate-identity` and `migrate-capture-paths` are absent.
2. **Caller evidence.** For every deleted function, the report carries its
   caller list from the parse and the statement that no routine caller exists.
3. **Keeps.** The marker-reader tests, the Alembic alias test, the local-state
   refusal tests and the packaging tests stay green without being edited
   except where a fixture literally referenced a deleted symbol, which is
   named.
4. **Documents.** No living sentence still instructs the operator to run a
   deleted command; each replacement is the single historical sentence.
5. **Measurement discipline.** The retention failure is measured before the
   re-pin; the after values are not pre-written; no counted comment is added.
6. **Mutation demonstration.** Re-adding `migrate-identity` to the parser
   fails the parser-surface test, with the observed failure named.
7. Run, through the declared routes: the touched contract modules (named in
   the report), the full declared Python suite against `5016/8/3/0`, the
   retention module, the packaging module, and the JS suites plus bounded
   glob as unaffected sanity.
8. Report every moved or removed site that no test exercises.
9. State the exact commit SHA, `git diff --stat`, Part A byte-unmoved, Part B
   still empty, and the Part C movement with its measured cause.

## Derivation and defect-pattern discipline

```text
 1. Derive site lists by PARSING each artefact. This prompt's anchors are
    locators, not an inventory.
 2. Resolve every cited symbol to its literal definition BEFORE deleting it.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Verify each occurrence and each caller independently.
 5. Never delete by name similarity; only by parsed caller evidence.
 6. Never truncate an inventory. If output is truncated, disclose it.
 7. Check every mechanical probe against a known-impossible result.
 8. Regenerate every verification table at report time; never transcribe one.
 9. Open and classify every grep hit.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

**Collapsing pairs.** Do not collapse the one-time migration commands with the
routine layout selection; do not collapse the engine-level
`COMPATIBLE_ENVIRONMENT_PREFIX` with `identity_env.py`'s strip safeguard; do
not collapse the deleted migration test module's pins with the keeps' pins in
other modules.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a routine caller of a deletion candidate exists; if a keep would
  need editing beyond a fixture that literally referenced a deleted symbol; if
  a frozen hash or Part A moves; if a Part C re-pin cannot be reproduced from
  your own measurement; if context pressure reaches the point where a bounded
  rotation is cheaper than a degraded result.

Completion: the deletion set gone with caller evidence, the retooled tests,
the new parser-surface test, the historical-sentence replacements with their
pins, the measured retention re-pin, the mutation demonstration, and one
local commit.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `62_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No further implementation, no second commit, no push,
  no publication, no host contact and no later grant is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `62` and exchange `01` unchanged.
Then:

1. The executed deletion inventory with per-symbol caller evidence.
2. The retooled test modules and the new parser-surface test.
3. The document replacements with their exact sentences and pins.
4. The measured retention re-pin with the arithmetic cause.
5. The mutation demonstration with its named observed failure.
6. Suites: touched modules, full Python, retention, packaging, JS sanity —
   counts, elapsed time, baseline differences.
7. `git diff --stat`, the commit SHA, Part A unmoved, Part B empty, Part C
   movement.
8. Every site no test exercises.
9. Deviations, risks, missing evidence, and one smallest next step.

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
  sections 2, 4, 5, 6, 7 and 8 in full.
- `deploy/ubuntu/kronika_release.py` — the whole engine, as it stands.
- `tests/contract/test_kronika_identity_migration.py`,
  `tests/contract/test_kronika_identity_retention.py`,
  `tests/contract/test_kronika_cli_and_release_readers.py`,
  `tests/contract/test_nuc_release_docs.py`,
  `tests/contract/test_nuc_release_remote_contract.py`,
  `tests/contract/test_kronika_capture_services.py`,
  `tests/contract/test_nuc_operator_runbook.py`,
  `tests/contract/test_nuc_release_source_contract.py`.
- `docs/UBUNTU_NUC_DEPLOYMENT.md`, `deploy/ubuntu/README.md`.
- `src/kronika/infrastructure/persistence/alembic_compat.py`,
  `src/kronika/infrastructure/runtime/local_state_migration.py` (read-only),
  `src/kronika/identity_env.py` (read-only).
- `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`, `.ap/AP.md` §5,
  §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, the parked capture state or
profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the deletion set, the caller
evidence, the parser test and the retention arithmetic at the reported
commit, then issues C9-B/2 (canonical layout only). No push, publication,
refresh, deployment or host contact is authorized inside this prompt.
