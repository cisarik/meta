# Authoritative Worker prompt — Worker session 49, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `49`, exchange `01`. Stored under the
Meta filename mapping as `49_implementation_00.md`, with report destination
`49_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **C7-B/1**, the first of three bounded grants that execute the C7-B
removal cut. Session 48 established that C7-B does not fit one session: it
completed the parity-first checkpoint and stopped cleanly. C7-B/1 covers the
settings, defaults and command-code removals; C7-B/2 will cover the physical
removals and the retired readers; C7-B/3 will finish the tooling and active
instructions. Each grant lands exactly one local commit and its own measured
ledger movement.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 49
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C7B1 — remove settings, defaults and command-code compatibility
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The compatibility this grant removes is what currently lets
old `FRAMENEST_`-prefixed inputs still configure the application, keeps the
development defaults on retired locations and emits retired command codes. The
simplified settings sources must preserve every canonical behavior the parity
tests characterize — including the constructor-override and dotenv quirks the
checkpoint recorded — and the release engine must switch its environment-file
variable in the same commit, or the documented service-account routes break
silently.

## Adopted continuation

The working tree carries exactly one unstaged modification, produced by the
session-48 parity-first checkpoint and accepted as the foundation of this
grant:

```text
tests/contract/test_kronika_settings_parity.py
sha256 ce54c7e62e1effa354651c0601b0803c7ca693896deb30107c1d5f23f03aceaa
+80 insertions, one replaced final line (no existing test removed)
14 new parametrized cases; the module ran 37 passed at session 48
```

Verify the present bytes against that hash before building on it. Keep the
file's characterization cases green before and after the simplification;
adjust an expectation only where the retired-prefix removal itself changes the
premise, with the cause stated.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
section 2.13 is your specification; workstreams C (settings), E (codes) and F
(defaults and recovery) are this grant's scope, plus the ledger movement they
cause. Read the section in full and sections 2.11–2.12 for what C7-A
established. Required outcomes:

1. **Settings sources, canonical-only.** Remove the retired `FRAMENEST_`
   fallback from the environment resolution — `src/kronika/identity_env.py`,
   `src/kronika/configuration.py` and every other source or message that
   resolves the retired prefix, including the `ENV_FILE` selection. An
   old-prefix-only input no longer configures the application (an explicit
   test proves it: it is ignored, not an error). Preserve canonical precedence,
   the case handling and the empty-value behavior the parity cases
   characterize; keep `lookup_field_value` and `lookup_env` distinct as the
   plan requires; do not change unrelated override behavior. Where the removed
   pair made a conflicting-pair refusal obsolete, update its test to the new
   canonical-only truth.
2. **Engine environment-file variable.** In `deploy/ubuntu/kronika_release.py`
   the service-account prefix still emits `env FRAMENEST_ENV_FILE=…`; switch it
   (and its comment) to `KRONIKA_ENV_FILE`, and flip the contract assertions
   that pin it (`tests/contract/test_nuc_release_remote_contract.py` and any
   further site). The documented service-account routes (`kronika-release
   status` and friends) depend on this variable being the one the simplified
   resolver reads.
3. **Command error codes.** Flip every emitted `FRAMENEST_*` code value to
   `KRONIKA_*` — forty-two occurrences across `adapters/cli/catalog.py`,
   `adapters/cli/recovery.py`, `adapters/cli/backup.py`,
   `infrastructure/runtime/production.py`, `infrastructure/runtime/development.py`
   and `infrastructure/persistence/cli.py`, derived by parse. Preserve every
   numeric exit status and the message text apart from the code spelling.
   Update every test pinning a code. Name any active document that names a code
   without editing it (the finishing grant owns documents).
4. **Local development defaults.** Switch the retired development default
   locations to the canonical mapping the C-LOCAL-P tooling already computes:
   `DEVELOPMENT_DATABASE_DIRECTORY` (`framenest-development`) and the platform
   application/log directories in
   `src/kronika/infrastructure/runtime/development.py` (macOS and XDG). Retain
   and demonstrate the legacy-state refusal safeguard: with legacy state
   present and no canonical state, the launcher must refuse rather than create
   an empty replacement. Update the tests that pinned the defaults-unmoved
   state (`tests/contract/test_local_state_migration.py` and any further site).
5. **Workstation recovery.** Make `kronika-recovery` canonical-only: remove the
   temporary `--remote-layout old|new` selection and the old choice it carries
   (`src/kronika/adapters/cli/recovery.py` and its engine), preserving every
   other behavior, help text apart from the removed option, and numeric
   statuses. Update its tests.
6. **Ledger.** Re-pin only the Part C scalars your own measurement shows this
   grant moved, with per-tree arithmetic causes in the running comment. Part A
   stays byte-unmoved; Part B stays at 20 (the physical removals are C7-B/2).

## Verified starting state, measured by the Orchestrator on 2026-10-14

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                aee0a60a04b78685608ec5a65ec5780c7d9884e7
Public main:                  aee0a60a04b78685608ec5a65ec5780c7d9884e7
Working tree:                 one unstaged modified file —
                              tests/contract/test_kronika_settings_parity.py
                              (sha256 ce54c7e6…, the adopted continuation above);
                              no other path differs
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4955 passed, 8 skipped, 3 warnings, 0 failed
Settings parity module:       37 passed (after the adopted addition)
Retention module:             15 passed
JS baselines (unaffected, sanity only): companion_web_bridge 27;
              companion_review_extension 42; x_companion_extension 54;
              companion_settings_automatic_analysis 6; kronika_ui 12;
              catalog_card_ai_quick_action 30; bounded non-browser glob 213
```

Re-derive the git/AP gates yourself at the start; the dirty tree above is
intentional and is not a gate failure. If any other check fails, stop and
report.

## Authority

```text
Positive authority: keep the adopted modification to
  `tests/contract/test_kronika_settings_parity.py` and adjust it only where the
  simplification changes a premise, with the cause stated; edit
  `src/kronika/identity_env.py`, `src/kronika/configuration.py` and exactly the
  sources your parse shows resolving the retired prefix or emitting a retired
  code or default; edit `deploy/ubuntu/kronika_release.py` for exactly the
  environment-file variable and its comment; edit `src/kronika/adapters/cli/recovery.py`
  and its engine for exactly the option removal; edit the test modules your
  parse shows pinning a changed surface, naming each non-obvious module in the
  report before editing it; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a Part C
  scalar that your own measurement shows this grant moved, with the arithmetic
  cause stated; make only the minimal name-correcting edit to an active
  document if a suite cannot otherwise be green, naming it in the report;
  create exactly one local non-amended commit on `main`.

Negative authority: every other path; the twenty Part B deletion paths; the
  console aliases in `pyproject.toml`; `extension/**` and the served web
  assets; the operator scripts and their mirrors (C7-B/2); every frozen
  document and ADR; any dependency, lockfile or package-configuration change;
  the `.ap` gitlink; any Alembic revision; any `.venv` operation (the contract
  forbids it; the environment refresh is a separate Cooperator step after
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
  one `git add <exact paths>` (the adopted file included) and one `git commit`;
  no push.

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

1. **Adopted-file integrity.** Show the present sha256 of the parity file
   matching the pinned value before any edit, and the module green (37 passed)
   before the simplification.
2. **Parity preserved.** After the simplification the same module is green,
   with only premise-driven expectation changes listed individually; the
   characterized constructor-override, empty-value, none-string, dotenv
   encoding/order and precedence behaviors are unchanged.
3. **Canonical-only matrix.** `KRONIKA_*`-only inputs configure; an
   old-prefix-only input is ignored (not an error, not a fallback); mixed
   inputs use the canonical value; the removed conflicting-pair refusal's test
   reflects the canonical-only truth; the engine's service-account command
   carries `KRONIKA_ENV_FILE` and its contract assertions flip.
4. **Codes matrix.** Every emitted code is canonical; the numeric statuses and
   messages are byte-identical apart from the code spelling; every pinning
   test updated; every active-document reference named (not edited unless
   minimally required for green).
5. **Defaults and safeguard.** The development defaults are canonical; the
   legacy-state refusal is demonstrated (legacy present, canonical absent →
   refuse; the new-default tests updated); the C-LOCAL-P migration tooling
   remains able to copy legacy → canonical.
6. **Recovery.** `--remote-layout` is gone from the CLI, its engine and tests;
   every other option and status is unchanged.
7. **Mutation demonstrations**, each named with its observed failure: restore
   one retired `FRAMENEST_` fallback → the canonical-only test fails; restore
   one retired code value → its pinning test fails; restore one
   `framenest-development` default → the defaults test fails; restore the
   retired engine variable → the engine contract test fails.
8. Run, through the declared routes: the focused modules for settings, ingress
   configuration, local-state migration, recovery and the release contract;
   then the full declared Python suite; then the retention module; then the six
   JS suites and the bounded non-browser glob as unaffected sanity. Report
   every count, elapsed time and any difference from the baselines.
9. Report every moved or removed site that no test exercises, and every
   consumer your derivation found that this grant did not name.
10. State the exact commit SHA, `git diff --stat`, Part A byte-unmoved, Part B
    still 20, and your own measurement with per-tree arithmetic for the Part C
    movement.

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
change: every parity case keeps its meaning. Do not collapse an error-code
rename with a numeric-status or message change. Do not collapse the default
switch with the safeguard — the refusal is demonstrated, not assumed.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match beyond the adopted modification; if a change would touch a Part B
  deletion path, a console alias, `extension/**`, the served web assets, the
  operator scripts or a frozen document (those belong to later grants); if a
  numeric status or a characterized behavior would change; if a Part C re-pin
  cannot be reproduced from your own measurement; if a `.venv` operation would
  be required; if context pressure reaches the point where a bounded rotation
  is cheaper than a degraded result — in that case stop before any commit and
  name exactly what remains.

Completion: the settings sources canonical-only with the parity module green
  before and after; the engine variable switched; every emitted code canonical
  with statuses preserved; canonical defaults with the demonstrated safeguard;
  recovery canonical-only; the ledger movement re-pinned with causes; full
  Python, retention, JS suites and bounded glob green through the declared
  routes; one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `49_report_00.md` in
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
echoing `kronika-sole-identity`, session `49` and exchange `01` unchanged. Then:

1. The adopted-file integrity check and the pre/post parity results.
2. The canonical-only, codes, defaults/safeguard and recovery matrices.
3. The mutation demonstrations, each with its named mutation.
4. Suites: focused modules, full Python, retention, JS and bounded glob —
   counts, elapsed time, baseline differences.
5. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, Part C
   movement with per-tree cause.
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
  section 2.13 in full, plus 2.11–2.12.
- `src/kronika/identity_env.py`, `src/kronika/configuration.py` and the
  settings tests, including the adopted parity file.
- `src/kronika/infrastructure/runtime/development.py`,
  `src/kronika/infrastructure/runtime/production.py`,
  `src/kronika/adapters/cli/recovery.py`,
  `src/kronika/adapters/cli/catalog.py`, `backup.py`,
  `src/kronika/infrastructure/persistence/cli.py`.
- `deploy/ubuntu/kronika_release.py` (the service-account prefix) and
  `tests/contract/test_nuc_release_remote_contract.py`.
- `tests/contract/test_local_state_migration.py`,
  `tests/contract/test_kronika_identity_retention.py`.
- `docs/WORKER_EXECUTION_CONTRACT.md` (the `.venv` prohibition),
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the matrices and suites at the
reported commit, then grants **C7-B/2** (the physical removals and retired
readers), after which the Cooperator environment refresh, publication and the
exact-main NUC refresh follow with **C7-B/3**. No push, refresh or host
contact is authorized inside this prompt.
