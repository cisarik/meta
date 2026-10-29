# Authoritative Worker prompt — Worker session 60, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `60`, exchange `01`. Stored under the
Meta filename mapping as `60_implementation_00.md`, with report destination
`60_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **C8-B/P**, the preparation half of the capture software-identity
transition. C8-A/H is complete: the installed capture release now runs from
the canonical pointer `/opt/kronika/capture-current` with unchanged software,
units, account, state, token, profile and bridge protocol. This grant changes
the remaining operational identity labels in the capture software, extends
the explicit capture transition so a reviewed bridge-code change restarts the
bridge as well as the runner, fixes the stale deployment README sentence, and
produces the complete-delta review the later activation grant (C8-B/H) will
name against its exact public target.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 60
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C8BP — prepare the canonical capture software identity
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The labels this grant changes are observable on the
loopback bridge; the activation change decides which services a reviewed
software switch cycles; and the delta review is what the activation will be
approved against, so it must classify driver, runner and CLI behavior changes
exactly, not only branding.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
section 2.16 is your specification. Required outcomes:

1. **Remaining operational identity labels.** Change exactly the HTTP
   `Server` header (`BridgeRequestHandler.server_version` in
   `src/kronika_capture/bridge/server.py`) and the health payload's `api`
   label (the `{"ok": true, "api": …}` response) to the canonical capture
   identity. Derive the exact strings from the repository's canonical capture
   names (`kronika-capture`, the package `kronika_capture`); keep the bridge
   protocol version values unchanged. The CLI name is already canonical —
   keep it. **Preserve `framenest-chatgpt-page` only where it identifies the
   frozen state directory**: `config.STATE_DIR_NAME`, the `paths.py`
   docstrings, the `--state-dir` help text that names the XDG directory, the
   extension asset's state-directory join, and the state-directory tests.
   Adjust other prose only where an operational label would be false; name
   every decision. Do not change any behavior, protocol, state resolution,
   path, account or token.
2. **Explicit capture transition restarts the bridge too.** Extend
   `_cmd_capture_transition` (`deploy/ubuntu/kronika_release.py`) so the
   explicit `activate-capture` and `rollback-capture` transition restarts the
   **bridge as well as the runner**, in the safe order (bridge first, then
   runner), each restart failure wrapped in its own readiness-class message
   that still prints the release pointers, the existing drain gate, brake
   gate, identity snapshot and single readiness check unchanged, and no
   second browser launch after a readiness failure. Ordinary `deploy` and
   `rollback` remain capture-neutral — pin that they emit no bridge or runner
   action.
3. **Deployment README.** Fix `deploy/ubuntu/README.md`'s pointer-switch
   sentence: the current pointer is `/opt/kronika/capture-current`; the
   operations that switch it are `activate-capture`, `rollback-capture` and
   the explicit `migrate-capture-paths` procedure, with their different
   effects stated concisely. Keep the command examples canonical.
4. **Complete-delta review (report deliverable).** The installed capture
   release identity is recorded (release markers `94e605c17b881461fad3e22fd8c7fca32cb93976`,
   code tree `977465503254fe6cdf31673b7e107b9e0487ffe2` =
   `94e605c:src/kronika_capture`). Against the target this grant produces,
   produce the complete delta review: the four known capture-code changes
   (`_assets/extension/src/headless/driver.mjs`, `runner.mjs`, `cli.py`,
   `config.py`) plus any further capture-surface difference, each classified
   as identity, CLI/help, driver behavior, runner behavior, protocol/state, or
   test. State the exact target commit SHA and what activating it would ship.
   Do not implement behavior changes here — review the delta that already
   exists.
5. **Test-quality items from C8-A/P.** Strengthen the success-path
   assertions the C8-A/P report named as removable without a failure (the
   `poetry.toml`/`poetry.lock` existence probes, `chown -R root`,
   `chmod -R a-w`, the relocation upload, the post-install `WorkingDirectory`
   read-back) if your parse confirms the gap; name each added assertion.

## Verified starting state, measured by the Orchestrator on 2026-10-17

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                7c1ea48be1176cd454f0ce6a97dc09d32d543838
Public main:                  c0f456656c9930810e11d13e1d4684efdb3ee4ff
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      5013 passed, 8 skipped, 3 warnings, 0 failed
Focused capture/release modules: 473 passed (five-module set); 623 passed (nine-module set)
Retention module:             15 passed
JS baselines (unaffected sanity): 23 / 41 / 55 / 6 / 12 / 30; bounded glob 212
Host state (Orchestrator evidence): the capture runs from
              /opt/kronika/capture-current -> /opt/kronika/releases/94e605c…;
              bridge and runner restarted once at 2026-10-17 07:28:18/19;
              Xvfb unchanged since 2026-10-15 06:31:47; the web release is
              c0f4566 and healthy; the installed capture software still
              carries the former identity labels.
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only work: no NUC contact, no browser, no capture action.

## Authority

```text
Positive authority: edit `src/kronika_capture/**` for exactly the identity
  labels in outcome 1; edit `deploy/ubuntu/kronika_release.py` for exactly the
  capture-transition restart extension; edit `deploy/ubuntu/README.md` for the
  pointer-switch sentence; edit every test module your parse shows pinning a
  changed surface, naming each non-obvious module in the report before editing
  it; edit `tests/contract/test_kronika_identity_retention.py` only to re-pin
  a Part C scalar that your own measurement shows this grant moved, with the
  arithmetic cause stated; create exactly one local non-amended commit on
  `main`.

Negative authority: every other path; capture behavior, protocol, state
  resolution, paths, account or token; the parked capture capabilities (no
  Search/Research, ZIP or S7-C work); ordinary deploy/rollback behavior; the
  bridge protocol version values; any document beyond `deploy/ubuntu/README.md`;
  any dependency or lockfile change; the `.ap` gitlink; any Alembic revision;
  any `.venv` operation; publication; push; force; amend; branch; stash; any
  NUC contact or SSH; any activation, migration, deployment or browser action.
  If a necessary change falls outside the positive scope, stop and report; do
  not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 7c1ea48be1176cd454f0ce6a97dc09d32d543838 --operation <id> [-- <argv>]
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

1. **Identity matrix.** The HTTP `Server` header and the health `api` label
   carry the canonical capture identity; the bridge protocol version values
   are unchanged; `framenest-chatgpt-page` remains only at the frozen
   state-directory sites (each listed); every other capture identity label
   your parse finds is either canonicalized with its decision named or
   reported. The canonical CLI name is unchanged.
2. **Activation matrix.** `activate-capture` and `rollback-capture` emit
   exactly one bridge restart and one runner restart in the safe order, with
   the existing gates, one readiness check and no second browser launch;
   each restart failure maps to its named message and the readiness exit
   class; `deploy`/`rollback` emit no capture bridge/runner action (pins).
   The restart-brake tests and activation-selection tests cover it.
3. **README.** The corrected sentence names the canonical pointer and all
   three switching operations with their different effects.
4. **Delta review.** The review table (per file: change class, what
   activating it ships) and the exact target SHA; the installed identity and
   the code-tree equality shown.
5. **Mutation demonstrations**, each named with its observed failure: revert
   the HTTP `Server` label → the identity test fails; drop the bridge restart
   → the activation-order test fails; change the state-directory token → the
   state-resolution tests fail.
6. Run, through the declared routes: the focused capture/release/migration
   modules (both the five-module and nine-module sets), the full declared
   Python suite against `5013/8/3/0`, the retention module and the JS suites
   plus bounded glob as unaffected sanity.
7. Report every moved or removed site that no test exercises, and every
   consumer your derivation found that this prompt did not name.
8. State the exact commit SHA, `git diff --stat`, Part A byte-unmoved,
   Part B still empty, and any Part C movement with cause.

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

**Collapsing pairs.** Do not collapse the frozen state-directory token with
an operational identity label; do not collapse the bridge-protocol values
with the display labels; do not collapse the explicit capture transition
with the ordinary web deploy/rollback; do not collapse a review finding with
an implementation change.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a change would touch capture behavior, protocol, state
  resolution, paths, account, token, the parked capabilities or the ordinary
  web deploy/rollback; if a frozen hash or Part A moves; if a Part C re-pin
  cannot be reproduced from your own measurement; if a `.venv` operation or
  any host or browser action would be required; if context pressure reaches
  the point where a bounded rotation is cheaper than a degraded result.

Completion: the canonical identity labels with the frozen state token
  preserved, the bridge-and-runner capture transition with its gates, the
  corrected README sentence, the complete-delta review with the exact target
  SHA, the named test-quality additions, the matrices and three mutation
  demonstrations; focused modules, full Python suite, retention and JS sanity
  green through the declared routes; one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `60_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No further implementation, no second commit, no push,
  no publication, no refresh, no capture action, no host contact and no later
  grant is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `60` and exchange `01` unchanged. Then:

1. The identity matrix and the frozen state-directory site list.
2. The activation matrix and the README correction.
3. The complete-delta review with the exact target SHA.
4. The named test-quality additions.
5. The mutation demonstrations, each with its named mutation.
6. Suites: focused, full Python, retention, JS sanity — counts, elapsed time,
   baseline differences.
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

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
  section 2.16 in full, and section 2.17 for what the later activation will
  need.
- `src/kronika_capture/**` — the bridge server, config, paths, CLI and the
  headless assets, as they stand.
- `deploy/ubuntu/kronika_release.py` — `_cmd_capture_transition`, the capture
  restart and readiness helpers, the atomic switch and the gates.
- `deploy/ubuntu/README.md`.
- The capture, release and migration contract test modules.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`, `.ap/AP.md` §5,
  §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, the parked capture state or
profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the matrices, the delta review and
the suites at the reported commit, then arranges the publication that makes
the exact target public; the **C8-B/H** activation grant follows with that
public target and the reviewed delta named against it. No push, refresh,
activation or host contact is authorized inside this prompt.
