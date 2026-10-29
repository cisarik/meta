# Authoritative Worker prompt — Worker session 50, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `50`, exchange `01`. Stored under the
Meta filename mapping as `50_implementation_00.md`, with report destination
`50_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is the **continuation of C7-B/1**. Session 49 implemented the settings,
defaults and command-code removals and stopped cleanly before staging: its
scalar-only ledger authority could not accommodate four content-membership
departures that its own authorized edits caused. This grant adopts the
preserved candidate, authorizes exactly those departures, and completes,
verifies and commits C7-B/1.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 50
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C7B1 — complete the settings, defaults and command-code removals
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The candidate is nearly complete and was verified piecewise
by session 49 — settings parity preserved (14 adopted cases unchanged, module
55 passed with resolver units), focused modules 368 passed, the engine variable
switched, codes renamed with static status stability. What remains is exacting:
two stale assertions that still pin the old truth, four content-path set
departures, the final dead-code cleanup review, the four mutation
demonstrations, the full suites and the commit. Do not re-open what the
candidate already established; complete and prove it.

## The preserved candidate

The working tree carries session 49's uncommitted candidate, produced under the
previous grant's authority and adopted here:

```text
50 files changed, 764 insertions(+), 938 deletions(-)
Index empty; no untracked files; HEAD aee0a60; no commit, no push.

Production paths changed (12):
  deploy/ubuntu/kronika_release.py
  src/kronika/adapters/cli/backup.py
  src/kronika/adapters/cli/catalog.py
  src/kronika/adapters/cli/recovery.py
  src/kronika/configuration.py
  src/kronika/identity_env.py
  src/kronika/infrastructure/ai/configuration.py
  src/kronika/infrastructure/persistence/catalog_backup_workstation.py
  src/kronika/infrastructure/persistence/cli.py
  src/kronika/infrastructure/runtime/development.py
  src/kronika/infrastructure/runtime/local_state_migration.py
  src/kronika/infrastructure/runtime/production.py

The other 38 paths are the affected tests and test support.
Adopted parity file now hashes 8bf01f8382400f958427e7b309f0c23b6067c63a3b8240b320a3f285a92e62d9.
```

Verify the tree matches this state (status, diff stat, the parity hash) before
building on it; if it does not, stop and report. Treat the candidate as your
own work from this point.

## Known remaining work, exactly

1. **Four content-membership departures.** The candidate removed the last
   retired-name occurrence from exactly these files, which must therefore
   leave `EXPECTED_FRAMENEST_CONTENT_PATHS` in
   `tests/contract/test_kronika_identity_retention.py`:
   `tests/contract/test_library_cli.py`,
   `tests/contract/test_operator_cli_hygiene.py`,
   `tests/unit/infrastructure/ai/test_ai_configuration_storage.py`,
   `tests/unit/infrastructure/backup/test_catalog_backup_ops.py`.
   This removal is authorized exactly for these four entries.
2. **Two stale assertions** in `tests/contract/test_kronika_cli_and_release_readers.py`
   still pin the old truth and fail against the candidate:
   `test_release_helper_still_injects_the_old_env_file_name` (update to the
   `KRONIKA_ENV_FILE` truth) and
   `test_development_database_directory_is_unchanged` (update to the canonical
   default). Complete them, and complete any further stale assertion the
   suites reveal, listing every such edit with its previous assertion in the
   report.
3. **Ledger movement.** Re-pin every Part C scalar the final candidate moves,
   with per-tree arithmetic causes in the running comment. Session 49's
   candidate measurements guide the expected movement (`src` −65, `tests`
   −298, `deploy` −2, environment tokens 702→381, capitalized 2681→2663, host
   path counts −2/−2/−1) — regenerate every number from the final tree, never
   transcribe. Part A stays byte-unmoved; Part B stays 20.
4. **Final cleanup review.** Session 49 reported obsolete conflict types or
   helpers remaining after the resolution simplification. Remove only code
   your parse proves has no remaining caller, name each site, and keep
   `lookup_field_value` and `lookup_env` distinct with their differing
   contracts intact.
5. **Mutation demonstrations** (each named with its observed failure): restore
   one retired `FRAMENEST_` fallback → the canonical-only test fails; restore
   one retired code value → its pinning test fails; restore one
   `framenest-development` default → the defaults test fails; restore the
   retired engine variable → the engine contract test fails.
6. **Suites.** Run, through the declared routes: the focused modules (settings,
   ingress configuration, direct readers, local-state migration, recovery,
   workstation, release contract, CLI/release readers), the full declared
   Python suite, the retention module, the six JS suites and the bounded
   non-browser JS glob. Report every count, elapsed time and baseline
   difference; the JS side is expected to be unchanged sanity.
7. **Commit.** One local non-amended commit on `main` naming all changed paths
   and deletions (none expected) after every suite is green; no push.

## Verified starting state, measured by the Orchestrator on 2026-10-14

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                aee0a60a04b78685608ec5a65ec5780c7d9884e7
Public main:                  aee0a60a04b78685608ec5a65ec5780c7d9884e7
Working tree:                 the preserved candidate above (50 modified paths)
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4955 passed, 8 skipped, 3 warnings, 0 failed
Settings parity module:       37 passed at session 48; 55 passed with resolver units at session 49
Retention module:             15 passed (baseline; membership test currently fails on the candidate)
Focused candidate modules:    368 passed, 1 warning (session 49)
JS baselines (unaffected, sanity only): 27 / 42 / 54 / 6 / 12 / 30; glob 213
```

Re-derive the git/AP gates yourself at the start; the dirty candidate tree is
intentional. If anything else fails, stop and report.

## Authority

```text
Positive authority: keep and complete the preserved candidate; edit
  `tests/contract/test_kronika_identity_retention.py` for exactly the four
  named content-path removals, the measured Part C scalar re-pins and their
  arithmetic causes; edit the two named stale assertions and any further stale
  assertion the suites reveal, listing each edit; edit the candidate's own
  files to complete the cleanup review (naming each site); make only the
  minimal name-correcting edit to an active document if a suite cannot
  otherwise be green, naming it in the report; create exactly one local
  non-amended commit on `main`.

Negative authority: every path not already in the candidate; the twenty Part B
  deletion paths; the console aliases in `pyproject.toml`; `extension/**` and
  the served web assets; the operator scripts and their mirrors (C7-B/2);
  every frozen document and ADR; any dependency, lockfile or
  package-configuration change; the `.ap` gitlink; any Alembic revision; any
  `.venv` operation (the contract forbids it; the Cooperator refresh follows
  C7-B/2); historical artifact readers and the Alembic `sys.modules` alias;
  publication; push; force; amend; branch; stash; any NUC contact or SSH; any
  migration, deployment, provider, browser or capture contact. If a necessary
  change falls outside the positive scope, stop and report; do not widen
  scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline aee0a60a04b78685608ec5a65ec5780c7d9884e7 --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`. JavaScript evidence
  uses only the documented ordinary invocation from the worktree root:
  `node --test tests/<name>.test.js`. Read-only Git inspection allowed; exactly
  one `git add <exact paths>` and one `git commit`; no push.

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

1. **Candidate integrity.** Show status, diff stat and the parity hash matching
   the preserved state before any further edit.
2. **Completion matrix.** The four content-path departures applied; both stale
   assertions now pin the canonical truth; no other stale assertion remains
   (whole-suite evidence); the cleanup review sites resolved with no caller
   left behind; `lookup_field_value` and `lookup_env` still distinct.
3. **Behavior stability.** Canonical-only resolution (old-prefix-only inputs
   ignored, mixed uses canonical, the parity cases green); engine commands
   carry `KRONIKA_ENV_FILE`; every emitted code canonical with numeric
   statuses byte-stable; canonical defaults with the demonstrated legacy-state
   refusal; recovery canonical-only.
4. **Mutation demonstrations**, the four named.
5. Suites: focused modules, full Python, retention, six JS suites, bounded
   glob — counts, elapsed time, baseline differences.
6. Every moved or removed site that no test exercises; every consumer the
   candidate touched that this grant did not name.
7. Commit facts: SHA, `git diff --stat`, Part A byte-unmoved, Part B still 20,
   Part C movement with per-tree arithmetic.

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

**Collapsing pairs.** Do not collapse the simplification with a behavior
change; do not collapse an error-code rename with a numeric-status change; do
not collapse the default switch with the safeguard; do not collapse a
content-path departure with a scalar movement — the ledger records both
exactly.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the preserved candidate does
  not match its described state; if a change would touch a Part B deletion
  path, a console alias, `extension/**`, the served web assets, the operator
  scripts or a frozen document; if a numeric status or a characterized
  behavior would change; if a Part C re-pin or a content-path departure cannot
  be reproduced from your own measurement; if a `.venv` operation would be
  required; if context pressure reaches the point where a bounded rotation is
  cheaper than a degraded result — in that case stop before any commit and
  name exactly what remains.

Completion: C7-B/1 complete — settings canonical-only with parity preserved,
  engine variable switched, codes canonical with statuses stable, canonical
  defaults with the demonstrated safeguard, recovery canonical-only, the four
  content-path departures and the measured scalars re-pinned, the cleanup
  review resolved, the four mutation demonstrations, all suites green through
  the declared routes, one local commit, report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `50_report_00.md` in
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
echoing `kronika-sole-identity`, session `50` and exchange `01` unchanged. Then:

1. Candidate integrity and the completion matrix.
2. Every stale assertion edit with its previous assertion; the cleanup-review
   sites.
3. The mutation demonstrations, each with its named mutation.
4. Suites: focused, full Python, retention, JS, bounded glob — counts, elapsed
   time, baseline differences.
5. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, Part C
   movement and content-path departures with per-tree arithmetic.
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

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/49_report_00.md`
  in full — the candidate's own record.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
  section 2.13 in full, plus 2.11–2.12.
- `tests/contract/test_kronika_identity_retention.py` and
  `tests/contract/test_kronika_cli_and_release_readers.py`.
- `src/kronika/identity_env.py`, `src/kronika/configuration.py` as they stand
  in the candidate.
- `docs/WORKER_EXECUTION_CONTRACT.md` (the `.venv` prohibition),
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the matrices, the ledger movement and
the suites at the reported commit, then grants **C7-B/2** (the physical
removals and retired readers), after which the Cooperator environment refresh,
publication and the exact-main NUC refresh follow with **C7-B/3**. No push,
refresh or host contact is authorized inside this prompt.
