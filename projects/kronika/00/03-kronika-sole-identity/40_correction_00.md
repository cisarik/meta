# Authoritative Worker prompt — Worker session 40, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `40`, exchange `01`. Stored under the
Meta filename mapping as `40_correction_00.md`, with report destination
`40_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 40
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-C6PS — correct the no-legacy-writers process query
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The first live C6 apply stopped fail-closed at its first gate
because the no-legacy-writers query treats a valid user with zero processes as a
failed query. The host runs procps-ng, whose `ps` exits 1 for an empty
selection; after `quiesce` stops every writer, that is the normal state. The
correction must make absence, presence and genuine query failure three
distinguishable outcomes without weakening the fail-closed property.

## The finding, exactly

Live apply output: `kronika-release: former web account process state is
unverifiable`, `MIGRATE_APPLY_EXIT=27`, after `quiesce` had stopped
`framenest.service` and the backup timers.

`cmd_remote_account_processes_absent(user)` currently runs (remote shell):

```sh
if ! ps -u <user> -o pid= >/dev/null 2>&1; then printf %s query-failed; \
else count=$(ps -u <user> -o pid= 2>/dev/null | wc -l); printf %s "$count"; fi
```

procps-ng returns **exit 1 when the selection is empty**. With every writer
stopped the selection is empty, so the guard emits `query-failed` and
`assert_no_legacy_writers` refuses. Host evidence: NUC `ps from procps-ng
4.0.4`, `ps -u nobody -o pid=` → exit 1, `ps -u framenest` → exit 0 (after the
automatic pre-write recovery restored the service). Local evidence: procps-ng
4.0.7, same behavior (`ps -u root` → 0). The defect is the success criterion,
not the query model.

The host state is already recovered: `framenest.service` and
`framenest-catalog-backup.timer` are active, the old layout serves `a37be37`,
and a failed `journal.json` remains in the control directory. Nothing in this
cut touches the host; the journal archive and retry follow separately.

## Correction specification

1. **Three distinguishable outcomes** for `cmd_remote_account_processes_absent`:
   - a valid user with zero processes → the exact token `0`;
   - a valid user with one or more processes → the exact count;
   - an unresolvable user, a missing/broken `ps`, or any other query failure →
     the exact token `query-failed`.
2. **Recommended approach** (derive your own if you can prove the same matrix):
   resolve the UID first (`id -u <user>`); refuse with `query-failed` when it
   cannot be resolved; verify the system-wide query itself works
   (`ps -e -o uid= >/dev/null 2>&1` — a live host always has processes, so this
   fails only when `ps` is broken) and refuse with `query-failed` when it does
   not; then count the lines of `ps -e -o uid=` whose value equals the UID,
   tolerating procps column spacing (for example `grep -w -c` or an equivalent
   exact numeric comparison). Never match on user-name text, whose column may
   truncate.
3. **Contract unchanged.** Keep the function name, its `query-failed` token, the
   caller messages and exit codes (`a process still runs as the former web
   account`; `former web account process state is unverifiable`; both exit 27),
   and every other behavior in `assert_no_legacy_writers` and `quiesce`.
4. **No other behavior change.**

## Verified starting state, measured by the Orchestrator on 2026-10-11

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                980041cf13dd427e77263f573694aed7c1a54018
Public main:                  980041cf13dd427e77263f573694aed7c1a54018, divergence 0 0
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at 980041c:   4877 passed, 8 skipped, 3 warnings, 0 failed
Focused migration module:     207 passed
Retention module:             15 passed
```

**No host contact.** The live host supplied the failure; all work and tests are
repository-only with synthetic fixtures. Do not infer the host's process table.

## Authority

```text
Positive authority: edit `deploy/ubuntu/kronika_release.py` for exactly the
  process-query correction; edit `tests/contract/test_kronika_identity_migration.py`
  for the boundary model, tests and mutation demonstrations; edit any other test
  module you derive as directly exercising the changed command, naming it in the
  report before editing it; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a Part C
  scalar that your own measurement shows this correction moved, with the
  arithmetic cause stated; create exactly one local non-amended commit on `main`.

Negative authority: every other path; any dependency or lockfile change; any
  change to `pyproject.toml`, `ap.project.conf` or the `.ap` gitlink; any frozen
  document or Alembic revision; publication; push; force; amend; branch; stash;
  any NUC contact or SSH; any migration invocation; any provider, browser or
  capture contact; any secret or personal-configuration read. If a necessary
  change falls outside the positive scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 980041cf13dd427e77263f573694aed7c1a54018 --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`, including as a text
  editor. Read-only Git inspection allowed; exactly one `git add <exact paths>`
  and one `git commit`; no push.

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

1. Reproduce the defect shape before editing: a boundary/fake state where the
   target user exists with zero processes must currently produce the unverifiable
   refusal (through `assert_no_legacy_writers`), and after the correction must
   pass with `0`.
2. Matrix, through the real remote-command builder and the fake boundary:
   valid user + zero processes → `0`; valid user + exactly one → `1`; valid user
   + several (including leading-space UID formatting) → exact count; unknown user
   → `query-failed`; broken `ps` → `query-failed`; missing `id` result →
   `query-failed`. The `assert_no_legacy_writers` caller maps each outcome to the
   existing messages/exit codes.
3. Mutation demonstrations: restore the old `if ! ps -u …` criterion → the
   zero-process test fails with the spurious refusal; remove the ps health check
   → broken-ps reads as `0`; remove the UID resolution guard → unknown user is
   misread. Name each mutation and observed failure.
4. Run, through the declared route: the focused migration module, then the
   declared full Python suite, then the retention module. Report every count,
   elapsed time and any difference from the `4877/8/3/0` baseline.
5. Report **every moved or removed site that no test exercises**, and every
   caller or boundary branch your derivation found that this prompt did not name.
6. State the exact commit SHA, `git diff --stat`, confirm Part A is byte-unmoved
   and Part B still measures 20, and show your own measurement and cause for any
   Part C movement. Never tune a pin until a suite is green.

## Derivation and defect-pattern discipline

```text
 1. Derive the affected callers and boundary branches by PARSING the engine and
    its tests. Locators are not an inventory.
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

**Collapsing pairs.** The three outcomes must stay mutually exclusive: a valid
empty selection must never become `query-failed`, and a broken query must never
become `0`.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the correction would weaken the fail-closed query semantics; if a
  frozen hash, Part A or Part B moves; if a Part C re-pin cannot be reproduced
  from your own measurement; if a necessary change falls outside the positive
  scope.

Completion: the corrected query with the full matrix and mutation
  demonstrations; focused module, full declared Python suite and retention
  module green through the declared route; one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `40_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No further implementation, no second commit, no push, no
  publication, no host contact and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `40` and exchange `01` unchanged. Then:

1. The reproduced baseline misfire and the corrected outcomes.
2. The remote command as implemented, with the three-outcome matrix.
3. Mutation demonstrations, each with its named mutation.
4. Focused module, full-suite and retention counts with elapsed time and any
   baseline difference.
5. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, and Part C
   movement with cause.
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

- `deploy/ubuntu/kronika_release.py` — `cmd_remote_account_processes_absent`,
  `RemoteMigrationHost.assert_no_legacy_writers`, `quiesce`, `stop_writers`,
  `recover_pre_write`.
- `tests/contract/test_kronika_identity_migration.py` — the fake boundary and
  the quiesce/observation tests.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/00_notes.md`
  tail — the live failure evidence and host state.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify: the three-outcome
matrix; the fail-closed semantics unchanged for genuine failures; the full suite
green at the reported commit; and Part A and Part B unmoved. **A fresh
independent re-audit follows**, and only after its PASS may the failed journal
be archived and the apply retried.
