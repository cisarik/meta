# Authoritative Worker prompt — Worker session 54, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `54`, exchange `01`. Stored under the
Meta filename mapping as `54_implementation_00.md`, with report destination
`54_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **C7-B/2b**, the physical-removal half of the C7-B cut. C7-B/1
(`6531965`) and C7-B/2a (`6dd72f6`) are committed and accepted; the retired
readers are gone. This grant removes the fourteen retired console aliases, the
twenty Part B retired-basename files, the operator scripts' retired fallback
mirrors, and reconciles every **active** consumer before each deletion. C7-B/3
will finish the active documents; the Cooperator environment refresh follows
this commit; the publication, exact-main refresh and rendered regression
acceptance close C7-B after C7-B/3.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 54
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C7B2B — remove the temporary physical compatibility
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. This is the deletion cut the whole has prepared since C3:
every canonical counterpart exists (C-OPS supplied the last five), every
consumer was inventoried across the previous grants, and the honest work is
reconciliation — active consumers move before a path is deleted, frozen
references are history and stay, and the ledger's Part B set becomes empty for
the first time.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
section 2.13 is your specification; its console-alias, Part B file and
environment/shell-fallback items are this grant's scope. Required outcomes:

1. **Fourteen retired console aliases.** In `pyproject.toml` remove every
   retired `framenest-*` entry (the thirteen application aliases plus
   `framenest-chatgpt-page`), leaving exactly the fourteen canonical
   `kronika-*` entries. Do not change the dependency list, the package
   configuration or `poetry.lock`. Reconcile every test or tool that pins,
   invokes or enumerates the aliases; name each one.
2. **The twenty Part B files.** Delete exactly the paths in
   `EXPECTED_FRAMENEST_BASENAME_PATHS`: the ten `deploy/systemd/` artifacts,
   `deploy/ubuntu/framenest-catalog-export-v1`, `deploy/ubuntu/framenest-release`,
   `deploy/ubuntu/framenest_release.py`, the root launcher `framenest`, the
   three `scripts/operator/infosec/` and the three `scripts/operator/network/`
   scripts. Before each deletion, derive and move every **active** consumer:
   the migration and routine release engines' artifact tables, deployment and
   release-contract tests, service tests, operator-script tests, CLI parser
   references, migration guidance messages and any further site your parse
   finds. The root launcher's active consumers move to the root `kronika`
   launcher.
3. **Operator-script mirrors.** The retained canonical scripts in
   `scripts/operator/infosec/` and `scripts/operator/network/` lose their
   retired `FRAMENEST_*` fallback resolution (the dual-prefix conflict contract
   and the `FRAMENEST_NUC_SSH_*` pair), keeping their canonical behavior,
   conflict handling where it survives and every exit status. Update their
   tests (`test_operator_network_scripts.py`, `test_operator_infosec_scripts.py`
   and any further site).
4. **Frozen references are history.** The 86 frozen Part A documents stay
   byte-unmoved; their references to deletion targets are exempt and were
   already swept (29 entries, including the ADRs and `docs/FEDORA_SERVICE.md`
   and `docs/NUC_HOST_BASELINE.md`). State the matcher scopes separately (exact
   deletion-path references, retired console names, broader historical tokens).
   If a deletion target itself were frozen, stop; it is not.
5. **Active documents are C7-B/3's surface.** Do not edit active documents
   here; make only the minimal name-correcting edit if a suite cannot
   otherwise be green, naming it in the report. Known document findings to
   carry forward: `SECURITY.md`, `docs/UBUNTU_NUC_DEPLOYMENT.md`,
   `docs/ACCEPTANCE_DUAL_AUDIENCE.md`, `ROADMAP.md`, `docs/X_COMPANION.md`,
   `scripts/operator/network/README.md`, `AGENTS.md`.
6. **Ledger.** `EXPECTED_FRAMENEST_BASENAME_PATHS` becomes the empty set with
   its cause recorded; every content-path departure caused by the deletions
   and the mirror removals is recorded; every Part C scalar this grant moves is
   re-pinned with per-tree arithmetic; Part A stays byte-unmoved.
7. **Environment.** No `.venv` operation of any kind (the contract forbids it;
   the Cooperator refresh follows this commit). Name any suite or case that
   cannot be green before that refresh — none is expected, since the tests use
   the interpreter and repository sources, and the canonical `kronika-*`
   console scripts already exist in the environment.

## Verified starting state, measured by the Orchestrator on 2026-10-15

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                6dd72f65976412bf92d672f9349bbd74752b0f39
Public main:                  aee0a60a04b78685608ec5a65ec5780c7d9884e7
                              (6531965 and 6dd72f6 are local and unpublished by design)
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
  your parse shows actively consuming a removed alias, wrapper, script,
  launcher or fallback — naming each non-obvious module in the report before
  editing it; edit the tests for the removed consoles, scripts and mirrors;
  edit `tests/contract/test_kronika_identity_retention.py` for the empty Part B
  set, the measured Part C re-pins and the content-path departures with
  arithmetic causes; make only the minimal name-correcting edit to an active
  document if a suite cannot otherwise be green, naming it in the report;
  create exactly one local non-amended commit on `main`.

Negative authority: every frozen document and ADR; any dependency, lockfile or
  package-configuration change beyond the console entries; the `.ap` gitlink;
  any Alembic revision; any `.venv` operation (the refresh is a separate
  Cooperator step); historical artifact readers and the Alembic `sys.modules`
  alias; the retired reader surfaces already shipped in C7-B/2a; active
  documents beyond the minimal coupling allowance; publication; push; force;
  amend; branch; stash; any NUC contact or SSH; any migration, deployment,
  provider, browser or capture contact. If a necessary change falls outside
  the positive scope, stop and report; do not widen scope.

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

1. **Frozen and target sweep.** Confirm the 86 frozen entries and that no
   deletion target is frozen; state the matcher scopes separately; list the
   frozen references preserved (expected: the known 29-entry family).
2. **Consumer reconciliation table.** For every removed alias, file, launcher
   and fallback: its active consumers, each moved or removed **before** the
   deletion, with the evidence. Open and classify every grep hit.
3. **Removal matrix.** Console entries: exactly fourteen canonical, zero
   retired; Part B set: empty; per-path ledger with canonical counterparts and
   content-path departures; the root launcher replaced by `kronika`; the
   operator scripts' canonical behavior with every exit status preserved.
4. **Behavior stability.** The full declared Python suite green against
   `4971/8/3/0`; the retention module green (15) with Part B empty; the six JS
   suites and the bounded glob green against `23/41/55/6/12/30` and `212`;
   name any case that requires the Cooperator environment refresh.
5. **Mutation demonstrations**, each named with its observed failure: restore
   one retired console alias → the console-ledger test fails; restore one
   deleted path reference in an active consumer's test → the reconciliation
   test fails; restore one `FRAMENEST_NUC_SSH_*` fallback in a canonical script
   → its test fails.
6. Report every moved, removed or retired site that no test exercises, and
   every consumer your derivation found that this grant did not name.
7. Commit facts: SHA, `git diff --stat` (deletions included), Part A
   byte-unmoved, Part B empty, Part C movement and content-path departures with
   per-tree arithmetic.

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
and frozen references are both required proofs. Do not collapse an alias
removal with a dependency change; do not collapse a content-path departure
with a scalar movement; do not collapse a script mirror removal with an exit
status change.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a deletion target were itself a frozen entry; if an edit would be
  required to a frozen document or to an active document beyond the minimal
  coupling allowance; if a canonical behavior or numeric status would change;
  if a measured ledger value cannot be reproduced; if a `.venv` operation would
  be required; if context pressure reaches the point where a bounded rotation
  is cheaper than a degraded result — in that case stop before any commit and
  name exactly what remains.

Completion: the fourteen aliases gone; the twenty paths deleted with every
  active consumer reconciled; the script mirrors canonical; the ledger's Part
  B empty and Part C re-pinned; all suites green through the declared routes
  (or the refresh-blocked cases named); one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `54_report_00.md` in
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
echoing `kronika-sole-identity`, session `54` and exchange `01` unchanged. Then:

1. The frozen/target sweep and the consumer reconciliation table.
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
  section 2.13 in full.
- `pyproject.toml`, the twenty Part B paths and every canonical counterpart.
- `deploy/ubuntu/kronika_release.py` (migration and routine artifact tables),
  `tests/contract/test_kronika_identity_migration.py`,
  `tests/contract/test_nuc_release_remote_contract.py`,
  `tests/contract/test_nuc_release_docs.py`,
  `tests/contract/test_fedora_systemd_service.py`,
  `tests/contract/test_operator_network_scripts.py`,
  `tests/contract/test_operator_infosec_scripts.py`.
- `tests/contract/test_kronika_identity_retention.py` in full.
- `docs/WORKER_EXECUTION_CONTRACT.md` (the `.venv` prohibition),
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §12.

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
