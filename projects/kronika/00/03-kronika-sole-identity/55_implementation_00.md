# Authoritative Worker prompt — Worker session 55, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `55`, exchange `01`. Stored under the
Meta filename mapping as `55_implementation_00.md`, with report destination
`55_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **C7-B/2b**, re-issued after session 54 stopped before mutation on
context pressure. Session 54's inventory is carried into this grant as
evidence — its matcher table, its consumer surfaces and its additional module
list below are your starting point, to be verified, completed and then
implemented. C7-B/1 and C7-B/2a are committed and accepted; C7-B/3 finishes the
active documents; the Cooperator environment refresh follows this commit; the
publication, exact-main refresh and rendered regression acceptance close C7-B
after C7-B/3.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 55
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C7B2B — remove the temporary physical compatibility
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. This is the deletion cut: fourteen console aliases, twenty
Part B paths, the operator-script mirrors and the coupled code finishing items.
Every canonical counterpart exists; the honest work is reconciliation — active
consumers move before a path is deleted, frozen references are history, and the
ledger's Part B set becomes empty with non-vacuous coverage for the first time.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
section 2.13 is your specification. Required outcomes:

1. **Fourteen retired console aliases.** In `pyproject.toml` remove the
   thirteen application aliases and `framenest-chatgpt-page`, leaving exactly
   the fourteen canonical `kronika-*` entries. The wheel/packaging and console
   tests flip to require the canonical consoles only and to prove the retired
   aliases are absent (`test_chatgpt_page_packaging.py` currently requires
   `framenest-chatgpt-page` in the wheel; `test_kronika_cli_and_release_readers.py`,
   `test_previews_console_script.py` and the CLI suites are further consumers).
   Do not change dependencies, package configuration or `poetry.lock`. The
   parked capture module's own internal state name and bridge identity
   (`framenest-chatgpt-page` in `src/kronika_capture/**`) are NOT console
   aliases and stay unchanged for its parked cuts.
2. **The twenty Part B files.** Delete exactly the paths in
   `EXPECTED_FRAMENEST_BASENAME_PATHS` (ten `deploy/systemd/` artifacts,
   `deploy/ubuntu/framenest-catalog-export-v1`,
   `deploy/ubuntu/framenest-release`, `deploy/ubuntu/framenest_release.py`,
   the root launcher `framenest`, three `scripts/operator/infosec/` and three
   `scripts/operator/network/` scripts). Before each deletion, move or update
   every **active** consumer; the root launcher's consumers move to the root
   `kronika` launcher.
3. **Coupled engine and code finishing.** The routine and migration engines'
   artifact tables reference the retired systemd artifacts and the retained
   wrappers; reconcile them (`deploy/ubuntu/kronika_release.py` and its
   contract tests, including `test_nuc_release_source_contract.py`,
   `test_nuc_release_remote_contract.py`, `test_fedora_systemd_service.py`).
   Complete the code-side finishing items the plan names: the production
   credential tooling (`deploy/ubuntu/production_ai_deploy.py` and
   `deploy/ubuntu/fn-production-env-deploy`, which read the three
   `framenest-ai-credential-*.conf` templates this grant deletes — point them
   at the canonical templates, service, paths and console), the release
   engine's temporary operational name `REMOTE_DEPLOY_DIR`
   (`/run/framenest-release-deploy`), and the backup/export defaults your
   parse finds. Preserve every numeric status and the engine's lock/recovery
   semantics; update their tests.
4. **Operator-script mirrors.** The retained canonical scripts in
   `scripts/operator/infosec/` and `scripts/operator/network/` lose their
   retired `FRAMENEST_*` fallback resolution (the dual-prefix conflict contract
   and the `FRAMENEST_NUC_SSH_*` pair), keeping canonical behavior, surviving
   conflict handling and every exit status; update
   `test_operator_network_scripts.py`, `test_operator_infosec_scripts.py` and
   any further site.
5. **Worker-execution and release contracts.** `test_worker_execution_contract.py`
   asserts the retained wrapper and its `AGENTS.md`/
   `docs/WORKER_EXECUTION_CONTRACT.md` sentences; deleting the wrapper
   requires the minimal coupled edits to that test and exactly the sentences
   it checks in those two documents, naming them in the report. Those are the
   only document edits this grant makes beyond the minimal-suite-coupling
   allowance; the rest of the documents are C7-B/3.
6. **Frozen references are history.** The 86 frozen Part A documents stay
   byte-unmoved. Session 54's matcher scopes are the expected families —
   verify them: exact deletion paths plus bounded `./framenest` launcher
   references match 11 frozen documents; the exact fourteen console names
   match 18; the broader case-sensitive `framenest[-_.]` matches 29 (the known
   ADRs plus `docs/FEDORA_SERVICE.md` and `docs/NUC_HOST_BASELINE.md`); the
   case-insensitive token matches 77. State each scope separately. A frozen
   entry containing a historical reference never blocks a deletion; a
   deletion target being frozen would (it is not).
7. **Ledger.** `EXPECTED_FRAMENEST_BASENAME_PATHS` becomes the empty set with
   its cause recorded and **non-vacuous replacement coverage** (the
   empty-set transition must still assert something real — for example a
   sentinel or a known-impossible control — so the test cannot pass because
   nothing is measured). Record every content-path departure this grant
   causes; re-pin every moved Part C scalar with per-tree arithmetic; Part A
   stays byte-unmoved.

## Carried session-54 inventory (verify, complete, then implement)

Consumer surfaces it established: retired parser names and database-migration
guidance in the CLI adapters, persistence CLI and production runtime; the
release engine's invoked consoles and migration inputs (old installed-host
unit names cannot be replaced indiscriminately); `production_ai_deploy.py`'s
three credential templates with coupled destinations and validation; the
backup, offdevice and Fedora service contracts reading retired artifacts; the
capture packaging contract requiring the retired capture console; the
migration contract deriving tests from a nonempty Part B; the operator
contracts exercising deleted entry points and dual-prefix behavior; the
release and worker-execution contracts requiring the retained wrappers.

Additional modules it found: `test_backup_cli.py`, `test_catalog_cli.py`,
`test_catalog_backup_timer.py`, `test_catalog_offdevice_timer.py`,
`test_chatgpt_page_packaging.py`, `test_kronika_cli_and_release_readers.py`,
`test_kronika_identity_dual_read.py`, `test_nuc_release_source_contract.py`,
`test_persistence_cli.py`, `test_previews_console_script.py`,
`test_production_ai_deployment.py`, `test_recovery_cli.py`,
`test_sidecar_cli.py`, `test_worker_execution_contract.py`,
`tests/integration/test_development_launcher.py`,
`tests/unit/application/test_in_process_lifecycle.py`.

Treat this as a partial table: open and classify every hit yourself before
each deletion.

## Verified starting state, measured by the Orchestrator on 2026-10-15

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                6dd72f65976412bf92d672f9349bbd74752b0f39
Public main:                  aee0a60a04b78685608ec5a65ec5780c7d9884e7
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4971 passed, 8 skipped, 3 warnings, 0 failed
Retention module:             15 passed
JS baselines: companion_web_bridge 23; companion_review_extension 41;
              x_companion_extension 55; companion_settings_automatic_analysis 6;
              kronika_ui 12; catalog_card_ai_quick_action 30;
              bounded non-browser JS glob 212
Part B:                       20 paths, all with canonical counterparts
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only work: no NUC contact, no browser, no real X.

## Authority

```text
Positive authority: edit `pyproject.toml` for exactly the console-alias
  removal; delete exactly the twenty Part B paths; edit the retained operator
  scripts for exactly the fallback-mirror removal; edit every tracked file
  your parse shows actively consuming a removed path or the coupled finishing
  items — the engines and their contract tests, `production_ai_deploy.py`,
  `fn-production-env-deploy`, the CLI suites, the packaging and migration
  contracts, the worker-execution contract test and exactly the sentences it
  checks in `AGENTS.md` and `docs/WORKER_EXECUTION_CONTRACT.md` — naming each
  non-obvious module in the report before editing it; edit
  `tests/contract/test_kronika_identity_retention.py` for the empty Part B
  set with non-vacuous replacement coverage, the measured Part C re-pins and
  the content-path departures with arithmetic causes; make only the minimal
  name-correcting edit to a further active document if a suite cannot
  otherwise be green, naming it in the report; create exactly one local
  non-amended commit on `main`.

Negative authority: every frozen document and ADR; any dependency, lockfile or
  package-configuration change beyond the console entries; the `.ap` gitlink;
  any Alembic revision; any `.venv` operation (the refresh is a separate
  Cooperator step); historical artifact readers and the Alembic `sys.modules`
  alias; the parked capture module's internal names; active documents beyond
  the coupled sentences and the minimal-coupling allowance; publication;
  push; force; amend; branch; stash; any NUC contact or SSH; any migration,
  deployment, provider, browser or capture contact. If a necessary change
  falls outside the positive scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 6dd72f65976412bf92d672f9349bbd74752b0f39 --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`. JavaScript evidence
  uses only the documented ordinary invocation from the worktree root:
  `node --test tests/<name>.test.js`. Read-only Git inspection allowed; exactly
  one `git add <exact paths>` (deletions staged, for example with `git rm`) and
  one `git commit`; no push.

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

1. **Frozen and target sweep.** Confirm the 86 frozen entries, the empty
   deletion-target intersection, and the four matcher scopes separately with
   their expected counts; list the preserved frozen references.
2. **Consumer reconciliation table.** For every removed alias, path, launcher
   and fallback: its active consumers, each moved, updated or removed
   **before** the deletion, with evidence; open and classify every grep hit.
3. **Removal matrix.** Exactly fourteen canonical console entries and zero
   retired; Part B set empty with non-vacuous coverage; the wheel/packaging
   proof; the root launcher replaced; the operator scripts canonical with
   every exit status preserved; the finishing items complete.
4. **Behavior stability.** Full declared Python suite green against
   `4971/8/3/0`; retention green with the empty set; the six JS suites and the
   bounded glob green against `23/41/55/6/12/30` and `212`; name any case that
   requires the Cooperator environment refresh.
5. **Mutation demonstrations**, each named with its observed failure: restore
   one retired console alias → the console-ledger/packaging test fails;
   restore one deleted-path reference in an active consumer's test → the
   reconciliation test fails; restore one `FRAMENEST_NUC_SSH_*` fallback →
   its script test fails.
6. Report every moved, removed or retired site that no test exercises, and
   every consumer your derivation found that this grant did not name.
7. Commit facts: SHA, `git diff --stat` (deletions included), Part A
   byte-unmoved, Part B empty, Part C movement and content-path departures
   with per-tree arithmetic.

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

**Collapsing pairs.** Do not collapse "deleted" with "unreferenced": active
and frozen references are both required proofs. Do not collapse the empty-set
ledger transition with a vacuous test. Do not collapse an alias removal with a
dependency change; do not collapse a script mirror removal with an exit-status
change.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a deletion target were itself a frozen entry; if an edit would be
  required to a frozen document or to an active document beyond the coupled
  sentences and the minimal-coupling allowance; if a canonical behavior or
  numeric status would change; if a measured ledger value cannot be
  reproduced; if a `.venv` operation would be required; if context pressure
  reaches the point where a bounded rotation is cheaper than a degraded
  result — in that case stop before any commit and name exactly what remains,
  with the completed classification preserved in the report for the next
  grant.

Completion: the fourteen aliases gone; the twenty paths deleted with every
  active consumer reconciled; the script mirrors canonical; the finishing
  code items complete; the ledger's Part B empty with non-vacuous coverage and
  Part C re-pinned; all suites green through the declared routes (or the
  refresh-blocked cases named); one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `55_report_00.md` in
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
echoing `kronika-sole-identity`, session `55` and exchange `01` unchanged. Then:

1. The frozen/target sweep with the four matcher scopes and the consumer
   reconciliation table.
2. The removal and behavior-stability matrices.
3. The mutation demonstrations, each with its named mutation.
4. Suites: full Python, retention, JS, bounded glob — counts, elapsed time,
   baseline differences; any refresh-blocked case named.
5. `git diff --stat`, the commit SHA, Part A unmoved, Part B empty, Part C
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

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
  section 2.13 in full; `54_report_00.md` in full (the carried inventory).
- `pyproject.toml`, the twenty Part B paths and every canonical counterpart.
- `deploy/ubuntu/kronika_release.py`,
  `deploy/ubuntu/production_ai_deploy.py`,
  `deploy/ubuntu/fn-production-env-deploy` and the named contract test
  modules.
- `tests/contract/test_kronika_identity_retention.py`,
  `tests/contract/test_worker_execution_contract.py`.
- `docs/WORKER_EXECUTION_CONTRACT.md` (the `.venv` prohibition and the
  retained-wrapper sentences), `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the matrices, the empty Part B set,
the ledger and the suites at the reported commit, then runs the Cooperator
environment refresh and the wheel/console evidence, grants **C7-B/3** (the
active documents), and closes C7-B with the publication, the exact-main NUC
refresh and the rendered regression acceptance. No push, refresh or host
contact is authorized inside this prompt.
