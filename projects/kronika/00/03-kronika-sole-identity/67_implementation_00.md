# Authoritative Worker prompt — Worker session 67, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `67`, exchange `01`. Stored under the
Meta filename mapping as `67_implementation_00.md`, with report destination
`67_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **the category-16 correction, part B** — the last one:
`default_ai_config_path`'s legacy fallbacks switch to the canonical spelling
while every legacy source the migration tool reads stays exactly as it is,
with the migration-coherence proof made explicit.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 67
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-CORR-C9B16B — the AI-config default switch
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The switch changes a development default that existing
legacy state depends on; the migration tool, the refusal safeguard and the
tests that use the default as a fixture source must stay coherent.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/65_report_00.md`
section 4 (category 16, the `default_ai_config_path` entries) is the normative
site; the anchors below are locators and must be re-derived by parse.

1. **The fallback literals.** In
   `src/kronika/infrastructure/ai/configuration.py`, `default_ai_config_path`
   returns `~/Library/Application Support/FrameNest/ai/config.json` on darwin
   and `<$XDG_CONFIG_HOME or ~/.config>/framenest/ai/config.json` otherwise
   when no canonical environment override is set. Change exactly the two
   directory-name literals to `Kronika` and `kronika`. Keep the override
   handling, the absolute-path validation, the conflict error and the
   function's shape unchanged.
2. **Do not touch the migration module.** In
   `src/kronika/infrastructure/runtime/local_state_migration.py` keep
   `LEGACY_APP_DIRECTORY_NAME` (`FrameNest`), `LEGACY_LOWER_DIRECTORY_NAME`
   (`framenest`), `LEGACY_TEMP_DIRECTORY_NAME`, `CANONICAL_*`, the replacement
   pairs, and the legacy AI source reading (`ai_root` under the legacy
   application-support directory and the XDG legacy AI source) exactly as
   they are — those are category-15 retained sources. The migration tool and
   the refusal safeguard must keep recognizing and migrating both legacy AI
   sources to the canonical destinations.
3. **Make the coherence explicit.** Add or extend one test (name it and the
   module in the report) that binds the pair: the canonical value the
   default now returns equals the migration tool's canonical AI destination,
   and the migration tool's legacy AI source equals the path the previous
   default returned — for both the darwin and the XDG shapes. The point is
   that a developer holding a legacy AI config has a supported route to the
   new default and no silent drop.
4. **Update the pins.** `tests/contract/test_local_state_migration.py`
   currently derives fixture paths from `default_ai_config_path` (around
   lines 403 and 427); after the switch those fixtures must construct the
   legacy locations explicitly from the migration module's legacy constants
   and assert the new default's value and the migration behavior.
   `tests/unit/infrastructure/ai/test_ai_configuration_storage.py` (the
   override cases) and
   `tests/contract/test_kronika_direct_reader_routing.py` (the retired-env
   name is ignored and both calls equal the default) must be verified and
   adjusted only where the changed default moves them; name every module you
   edit. Consumers (`adapters/cli/ai.py`, `infrastructure/ai/registry.py`,
   `adapters/api/ai_admin_api.py`, `adapters/api/application.py`) call the
   function and need no change; verify and state that. The live NUC is
   unaffected (`KRONIKA_AI_CONFIG_PATH` is set there).

## Verified starting state, measured by the Orchestrator on 2026-10-19

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                063b045c0e431760cfc48996bec1160c4d4b7e0b
Public main:                  5b86d896b3ea03f89fef2c90f7af2c121d0ef915 (C9-B sequence unpublished by design)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4713 passed, 8 skipped, 3 warnings, 0 failed
Focused validation:           346 passed (retention, mutation-header, ingress, upload-validation, process, local web application)
JS baselines:                 23 / 41 / 55 / 6 / 12 / 30; bounded glob 212
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only work: no host contact, no browser, no deployment.

## Authority

```text
Positive authority: edit `src/kronika/infrastructure/ai/configuration.py` for
  exactly the two fallback literals; add or extend the coherence test in the
  module your parse shows owns it; edit every test module your parse shows
  pinning the old default or currently deriving fixtures from it, naming each
  module in the report before editing it; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a scalar
  your own measured retention failure shows this commit moved, with the
  arithmetic cause stated; create exactly one local non-amended commit on
  `main`.

Negative authority: every other path; the migration module's legacy and
  canonical constants and its legacy source reading; the refusal safeguard;
  the category-11 identifiers; the category-15 stored keys; `WORKSPACE_UDS_PATH`;
  frozen documents; any feature change; any dependency or lockfile change;
  the `.ap` gitlink; any Alembic revision; any `.venv` operation; publication;
  push; force; amend; branch; stash; any host or browser action. If a
  necessary change falls outside the positive scope, stop and report; do not
  widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 063b045c0e431760cfc48996bec1160c4d4b7e0b --operation <id> [-- <argv>]
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

1. **Default matrix.** With no override: darwin returns
   `~/Library/Application Support/Kronika/ai/config.json`; otherwise
   `config_home/kronika/ai/config.json`; the override and validation
   behaviors are unchanged.
2. **Coherence.** The new default equals the migration tool's canonical AI
   destination and the previous default value equals its legacy AI source,
   for both platform shapes, proven by the named test.
3. **Migration intact.** The migration module is diff-free; its tests stay
   green; the legacy AI sources are still recognized and migrated; the
   refusal safeguard is untouched.
4. **Measurement discipline.** The retention failure is measured before the
   re-pin; after values are not pre-written; no counted comment is added.
5. **Mutation demonstration.** Revert one fallback literal → the named
   updated test fails, with the observed failure recorded.
6. Run, through the declared routes: the touched modules (named), the full
   declared Python suite against `4713/8/3/0`, the retention module, and the
   JS suites plus bounded glob as unaffected sanity.
7. Report every moved or removed site that no test exercises.
8. State the exact commit SHA, `git diff --stat`, Part A byte-unmoved, Part B
   still empty, and the Part C movement with its measured cause.

## Derivation and defect-pattern discipline

```text
 1. Derive every site by PARSING the start commit. The session-65 lists are
    locators, not pins.
 2. Resolve every cited literal to its exact text BEFORE editing it.
 3. A literal in a test fixture is NOT a pin. Require assertion context; a
    fixture that merely uses a former path as arbitrary data stays.
 4. Verify each occurrence and each caller independently.
 5. Never truncate an inventory. If output is truncated, disclose it.
 6. Check every mechanical probe against a known-impossible result.
 7. Regenerate every verification table at report time; never transcribe one.
 8. Open and classify every grep hit.
 9. Do not add the counted substring in a new counted comment.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the migration module would need an edit; if a changed default
  breaks a fixture whose legacy source cannot be reconstructed from the
  migration constants; if a frozen hash or Part A moves; if a Part C re-pin
  cannot be reproduced from your own measurement; if context pressure reaches
  the point where a bounded rotation is cheaper than a degraded result.

Completion: the canonical fallback with its coherence test, the updated pins,
the untouched migration module, the measured retention re-pin, the mutation
demonstration, and one local commit.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `67_report_00.md` in
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
echoing `kronika-sole-identity`, session `67` and exchange `01` unchanged.
Then:

1. The default matrix with the two platform shapes.
2. The coherence test with its exact assertions.
3. The migration-intact proof and the pins updated, each named.
4. The measured retention re-pin with the arithmetic cause.
5. The mutation demonstration with its named observed failure.
6. Suites: touched modules, full Python, retention, JS sanity — counts,
   elapsed time, baseline differences.
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

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/65_report_00.md`
  section 4 (the category-16 `default_ai_config_path` entries).
- `src/kronika/infrastructure/ai/configuration.py` (the function),
  `src/kronika/infrastructure/runtime/local_state_migration.py` (read-only;
  the legacy/canonical constants and the AI source reading).
- `tests/contract/test_local_state_migration.py`,
  `tests/unit/infrastructure/ai/test_ai_configuration_storage.py`,
  `tests/contract/test_kronika_direct_reader_routing.py`.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`, `.ap/AP.md` §5,
  §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, the parked capture state or
profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the default matrix, the coherence
test and the untouched migration module at the reported commit; the
category-16 correction is then complete and the whole proceeds to the
publication, the NUC refresh and the final rendered acceptance — each a
separately authorized step.
