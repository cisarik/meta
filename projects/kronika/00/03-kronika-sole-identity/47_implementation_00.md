# Authoritative Worker prompt — Worker session 47, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `47`, exchange `01`. Stored under the
Meta filename mapping as `47_implementation_00.md`, with report destination
`47_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 47
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C7B — remove the temporary compatibility layer
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. This is the removal cut: every temporary alias, fallback,
dual reader, retired path and transitional default that C3–C7-A deliberately
kept now goes, in one commit whose proofs were prepared by every previous cut.
It is the largest single repository mutation of the whole: a missed consumer of
a removed alias breaks a console, a script, a settings source or the served
extension; an over-eager removal of a retained historical artifact breaks
restore compatibility. Parse before you delete, keep every numeric status and
canonical behavior, and let the parity tests you add first prove the
simplified behavior.

This is work item **C7-B** from the accepted closure plan at
`25_report_00.md` section 2.13.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
section 2.13 is your specification. Read it in full, together with sections
2.11–2.12 for what C7-A established and section 1's tables. Its mutation list,
restated as binding outcomes:

**A. Fourteen retired console aliases.** Remove every `framenest-*` entry from
`[project.scripts]` in `pyproject.toml` (thirteen application aliases plus
`framenest-chatgpt-page`), leaving exactly the fourteen canonical
`kronika-*` entries. Do not touch the dependency list, the package
configuration or `poetry.lock`.

**B. Twenty Part B retired-basename files.** Delete exactly the twenty paths in
`EXPECTED_FRAMENEST_BASENAME_PATHS`
(`tests/contract/test_kronika_identity_retention.py`): ten `deploy/systemd/`
artifacts, three `deploy/ubuntu/` wrappers, the root launcher `framenest`,
three `scripts/operator/infosec/` and three `scripts/operator/network/`
scripts. Their canonical counterparts all exist. Before deleting each, derive
and reconcile every reference: the migration engine's artifact tables, the
routine release engine, tests that execute or assert the wrappers, docs that
name them and the Part B ledger itself. The root `framenest` launcher's
consumers move to the root `kronika` launcher.

**C. Old environment and SSH fallbacks, including mirrors.** Remove the
retired `FRAMENEST_` fallback reads from the settings sources and the shell
mirrors in the operator scripts, so old-prefix-only inputs no longer configure
the application or a script. **Before simplifying the settings sources**, add
the missing `_env_*` parity coverage the plan names — case sensitivity, prefix
overrides, empty handling and dotenv options — characterizing current behavior.
Preserve canonical settings precedence, case and empty-value behavior. Do not
force `lookup_field_value` and `lookup_env` into one function when their
contracts differ; do not change unrelated override behavior.

**D. Old readers of the transitioned protocols.** Only now, after C7-A
acceptance: remove the server's retired mutation-header acceptance (keep
`X-Kronika-Request` and the numeric statuses; update the dual message to the
canonical truth), the served companion host's retired web-protocol acceptance,
and the extension's retired readers — the retired web protocol, the retired
companion API version, the retired browser-key fallbacks and the retired alarm
acceptance (the migration receipts exist; the C7-A/C completion ran and was
rendered-accepted). Keep the served shell's dual mutation-header emission: it
is a deliberate rollback-safety residual and C7-B removes readers, not that
emitter.

**E. Command error codes.** Switch every emitted command error code value from
`FRAMENEST_*` to `KRONIKA_*` (parsed, not guessed). Preserve every numeric
exit status and the emitted message text apart from the code spelling.

**F. Local defaults and recovery.** Switch the local development defaults
(`framenest-development` and the platform application directories the
C-LOCAL-P tooling maps) to canonical locations, retaining the legacy-state
refusal safeguard. Make workstation recovery canonical-only: remove its
temporary `--remote-layout old|new` selection and the old choice it carries.

**G. Remaining finishing items.** Finish canonical production credential
tooling, backup/export defaults, temporary operational names and active
operator instructions your derivation finds — including
`scripts/operator/network/README.md`'s old names and the transitional
sentences in `AGENTS.md` that name the retained wrappers and variable spellings
as removed only in this window. Update non-frozen active documents only; leave
every frozen document and ADR byte-unmoved.

**H. Ledger.** Part B's expected set becomes the empty set; Part C scalars are
re-pinned from your own measurement with per-tree arithmetic causes; Part A
stays byte-unmoved. If any step would conflict with a frozen Part A entry,
stop and report.

## Order of work

1. `_env_*` parity coverage first (new tests prove current behavior).
2. Then the removals A→G, each with its references reconciled before deletion.
3. Then the ledger H and the suites.

Never delete a path before its consumers are moved; never move a consumer
before its replacement exists.

## Verified starting state, measured by the Orchestrator on 2026-10-13

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                aee0a60a04b78685608ec5a65ec5780c7d9884e7
Public main:                  aee0a60a04b78685608ec5a65ec5780c7d9884e7
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4955 passed, 8 skipped, 3 warnings, 0 failed
Focused Python (local web + public published): 225 passed
Retention module:             15 passed
JS baselines: companion_web_bridge 27; companion_review_extension 42;
              x_companion_extension 54; companion_settings_automatic_analysis 6;
              kronika_ui 12; catalog_card_ai_quick_action 30;
              bounded non-browser glob glob 213
Host state (Orchestrator evidence): NUC on the new layout serves `aee0a60`
              (canonical emissions, capture `94e605c`, DB `0035`, backup ready);
              the Cooperator's extension reload and rendered acceptance passed.
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report.

## Authority

```text
Positive authority: edit `pyproject.toml` for exactly the console-alias
  removal; delete exactly the twenty Part B paths; edit every tracked file
  your parse shows referencing a removed alias, wrapper, fallback, reader,
  error code, default or transitional sentence — naming each non-obvious
  module in the report before editing it; add the `_env_*` parity tests; edit
  `tests/contract/test_kronika_identity_retention.py` for Part B (empty set)
  and measured Part C re-pins with arithmetic causes; edit active non-frozen
  documents named by workstream G; create exactly one local non-amended commit
  on `main`.

Negative authority: every frozen document and ADR; any dependency, lockfile or
  package-configuration change; the `.ap` gitlink; any Alembic revision; any
  created, reconstructed, moved, symlinked or deleted `.venv` (the contract
  forbids it; the environment refresh is a separate Cooperator step); the
  served shell's dual mutation-header emitter; historical artifact readers and
  the Alembic `sys.modules` alias; publication; push; force; amend; branch;
  stash; any NUC contact or SSH; any migration, deployment, provider, browser
  or capture contact. If a necessary change falls outside the positive scope,
  stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline aee0a60a04b78685608ec5a65ec5780c7d9884e7 --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`. JavaScript evidence
  uses only the documented ordinary invocation from the worktree root:
  `node --test tests/<name>.test.js`. Do not activate browser-evidence suites.
  Read-only Git inspection allowed; exactly one `git add <exact paths>` (all
  paths, deletions included) and one `git commit`; no push.

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

1. **Reference reconciliation before deletion.** For every removed alias,
   wrapper, script and launcher, produce the parsed consumer table (tests,
   engines, docs, scripts) and show each consumer moved or removed before the
   path deletion. Open and classify every grep hit.
2. **Parity first.** The new `_env_*` tests characterize case sensitivity,
   prefix overrides, empty handling and dotenv options before the simplification
   and stay green after it; old-prefix-only inputs no longer configure the
   application (explicit test), canonical inputs behave identically.
3. **Removal matrix.** Console entries: exactly fourteen canonical, zero
   retired; Part B set empty; per-file ledger showing every deleted path and
   its canonical counterpart; no remaining reference to any deleted path in
   tracked files outside the retention ledger's historical comments.
4. **Reader removal matrix.** Server rejects the retired mutation header while
   every canonical request path keeps its numeric statuses; the served host
   accepts only the canonical web protocol; the extension accepts only the
   canonical protocol and API version, has no retired browser-key fallback and
   no retired alarm acceptance; the served shell's dual emission is unchanged.
5. **Behavior stability.** Command error codes are canonical; every numeric
   exit status and message is unchanged apart from the code spelling; local
   defaults are canonical with the legacy-state safeguard demonstrated;
   recovery is canonical-only and its `--remote-layout` selection is gone from
   the CLI and tests.
6. **Mutation demonstrations**, each named with its observed failure: restore
   one retired console alias → the console-ledger test fails; restore one
   retired-header acceptance → the header test fails; restore one
   old-prefix-only settings fallback → the old-prefix test fails; restore one
   `framenest-development` default → the default test fails.
7. Run, through the declared routes: the full declared Python suite, the
   retention module, every JS suite named in the starting state, and the
   bounded non-browser JS glob. Report every count, elapsed time and any
   difference from the baselines. State explicitly which suites could not run
   without the environment refresh — none is expected, since `.ap exec` uses
   the interpreter and the repository sources, not the console scripts.
8. Report every moved, removed or renamed site that no test exercises, and
   every consumer your derivation found that this prompt did not name.
9. State the exact commit SHA, `git diff --stat` (deletions included), confirm
   Part A byte-unmoved and show your own measurement with per-tree arithmetic
   for the Part B and Part C ledger updates.

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

**Collapsing pairs.** Do not collapse canonical-only with dual acceptance until
the retired reader is proven to have no remaining emitter; do not collapse
"deleted" with "unreferenced" — both proofs are required; do not collapse an
error-code rename with a numeric-status change; do not collapse a settings
simplification with a behavior change.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a removal would touch a frozen document or a historical artifact
  reader; if a numeric status or canonical behavior would change; if a Part C
  re-pin cannot be reproduced from your own measurement; if a `.venv`
  operation would be required (that is a separate Cooperator step); if context
  pressure reaches the point where a bounded rotation is cheaper than a
  degraded result — in that case stop before any commit and name exactly which
  workstreams remain.

Completion: every workstream A–H complete; the reference, removal and behavior
  matrices green with mutation demonstrations; full Python suite, JS suites,
  bounded glob and retention green through the declared routes; one local
  commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `47_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No further implementation, no second commit, no push, no
  publication, no refresh, no environment refresh, no host contact and no later
  cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `47` and exchange `01` unchanged. Then:

1. The consumer reconciliation tables per removed alias/wrapper/script/launcher.
2. The `_env_*` parity coverage and the simplified settings behavior.
3. The removal, reader-removal and behavior-stability matrices.
4. The mutation demonstrations, each with its named mutation.
5. Suites: full Python, JS, bounded glob, retention — counts, elapsed time,
   baseline differences.
6. `git diff --stat`, the commit SHA, Part A unmoved, Part B empty and Part C
   movement with per-tree cause.
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

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
  section 2.13 in full, plus sections 2.11–2.12 and 1's tables.
- `pyproject.toml`, the twenty Part B paths, and every canonical counterpart.
- `src/kronika/configuration.py`, `src/kronika/identity_env.py` and the
  settings tests.
- `src/kronika/adapters/cli/recovery.py`, the development launcher and the
  C-LOCAL-P migration tooling.
- `deploy/ubuntu/kronika_release.py` (routine engine and migration artifact
  tables), `deploy/ubuntu/kronika-release`.
- `tests/contract/test_kronika_identity_retention.py` in full.
- `AGENTS.md`, `scripts/operator/network/README.md`, the operator documents,
  `docs/UBUNTU_NUC_DEPLOYMENT.md`.
- `docs/WORKER_EXECUTION_CONTRACT.md` (the `.venv` prohibition),
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will verify the matrices and suites at the
reported commit, then run the separate Cooperator steps: the root-project
environment refresh (removing the stale installed alias scripts), the wheel and
`.venv` console evidence, the publication and the exact-main NUC refresh with
the rendered regression acceptance against the actual server/extension pair.
Only after that acceptance does the whole proceed to the capture-path cuts
(C8) and retirement (C9). No push, refresh or host contact is authorized inside
this prompt.
