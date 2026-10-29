# Authoritative Worker prompt — Worker session 30, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `30`, exchange `01`. Stored under the
Meta filename mapping as `30_implementation_00.md`, with report destination
`30_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 30
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-CDATAP — bounded catalog label maintenance interface
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. This cut writes the only repository interface that will ever
modify existing catalog rows: a device display name and, only if separately
authorized, selected library display names. It must be bounded, private,
compare-and-set, receipt-bound and reversible by an inverse operation, because
the execution window runs against the live private catalog with the service
stopped. Mistakes here are not caught by a red test unless the tests are built to
model stale, wrong-count, unauthorized and partially failed states.

This is work item **C-DATA-P** from the accepted closure plan at
`25_report_00.md` sections 2.5 and 1.7.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
sections 2.5 and 1.7 are your specification. Read both in full. Required
outcomes:

1. **One bounded maintenance interface.** Add `kronika-catalog identity-labels`
   with `check`, `apply` and `rollback`. It is not a general device/library CRUD
   expansion. The console script stays `kronika-catalog` mapped to
   `src/kronika/adapters/cli/catalog.py`.
2. **`check` is read-only and private.** Use the application engine with only
   reads. It resolves the device candidate itself against the expected old label
   and reports only sanitized results: whether the expected candidate exists,
   candidate counts, and whether any library display name contains the retired
   brand. It writes a private selection receipt (for example under the catalog's
   private state, mode 0600) containing the exact IDs and inverse values, and it
   **never prints IDs, library names, media paths or raw SQL**.
3. **`apply` is confirmed and receipt-bound.** It requires the approved receipt
   and an explicit confirmation, and refuses a stale receipt whose recorded
   expected state no longer matches the catalog. It opens the catalog through
   `create_sqlite_engine` and performs one `BEGIN IMMEDIATE` transaction through
   `run_in_immediate_transaction`. The device update is a compare-and-set by the
   internally resolved ID and the exact expected old label
   (`FrameNest NUC` → `Kronika NUC`).
4. **Libraries are a separate authority.** Library rows are updated only when the
   receipt actually contains library selections and the invocation explicitly
   includes them; replace only the approved brand substring and preserve every
   other character. Absent positive evidence, apply leaves libraries untouched.
5. **No destructive shortcuts.** No delete/re-register, no root or ID change, no
   schema revision, no media metadata, no `sqlite3` binary, no whole-file
   replacement. Foreign keys stay enforced and the private-catalog verification
   stays on the application path.
6. **`rollback` is receipt-bound inverse compare-and-set** using the stored
   inverse values, with the same confirmation and stale-receipt refusal.
7. **Receipt privacy.** Never echo receipt contents in command output, error
   messages or logs. Output sanitized assertions only. A digest of the receipt
   may be printed.
8. **Maintenance documentation.** Add a short procedure section to
   `docs/UBUNTU_NUC_DEPLOYMENT.md` covering the stop-writers window: check →
   review sanitized result → backup → apply with confirmation → sanitized
   read-back → receipt retention → rollback. Keep it consistent with the existing
   runbook style; the C-DATA-H window will follow it.

## Verified starting state, measured by the Orchestrator on 2026-10-08

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                335e91d199e99e28f2585c1b25531f29bb54270c
Remote origin:                https://github.com/cisarik/kronika
Public main:                  3194f48f6b343a460ed5988d92999f91ef999a79
                              (accepted cuts are local and unpublished, by design)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at 335e91d:   4696 passed, 8 skipped, 3 warnings, 0 failed
```

Facilities to reuse, verified at the baseline:

```text
catalog CLI and dispatch      src/kronika/adapters/cli/catalog.py (main 203, parser 374+)
device repository             src/kronika/infrastructure/persistence/device_repository.py
library repository            src/kronika/infrastructure/persistence/library_repository.py
engine and transactions       engine.py: create_sqlite_engine 29, run_in_transaction 174,
                              run_in_immediate_transaction 190, PRAGMA foreign_keys/busy_timeout,
                              verify_private_catalog on every connect
private catalog verification  src/kronika/infrastructure/persistence/private_state.py:52
catalog schema                src/kronika/infrastructure/persistence/catalog_schema.py
                              (devices.id FK RESTRICT; libraries rooted by device/path)
```

**The catalog row values are carried evidence, not a measured fact.** The
2026-10-02 observation recorded exactly one device whose stored `display_name` is
operator-typed `FrameNest NUC`, and the library question is unresolved. Do not
assume either; the command's `check` resolves the real candidate at execution
time. This cut performs **no live catalog access**.

## Authority

```text
Positive authority: edit `src/kronika/adapters/cli/catalog.py`; edit
  `src/kronika/infrastructure/persistence/device_repository.py`; edit
  `src/kronika/infrastructure/persistence/library_repository.py`; add exactly
  one new bounded module `src/kronika/infrastructure/persistence/identity_labels.py`
  if that is the correct home, or implement within the CLI and the repositories;
  edit `tests/contract/test_catalog_cli.py`; add
  `tests/contract/test_catalog_identity_labels.py`; edit
  `docs/UBUNTU_NUC_DEPLOYMENT.md` for the maintenance section; edit
  `tests/contract/test_nuc_release_docs.py` for the matching pins; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a Part C
  scalar that your own measurement shows this cut moved, with the arithmetic
  cause stated; create exactly one local commit on `main`.

Negative authority: every other path; `src/kronika/infrastructure/persistence/engine.py`
is frozen for this cut; any dependency or lockfile change; any change to
`pyproject.toml`, `ap.project.conf` or the `.ap` gitlink; any frozen document or
Alembic revision; publication; push; force; amend; branch; stash; any NUC
contact or SSH; any live catalog or database access, including any real
`catalog.sqlite3`, any development database and the NUC; any provider, browser
or capture contact; any secret, personal Fish configuration or browser-profile
read. If a necessary change falls outside the positive scope, stop and report;
do not widen scope.

Commands: Python evidence only through
  ./.ap/ap project check --root /home/agile/Projects/kronika --baseline 335e91d199e99e28f2585c1b25531f29bb54270c
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 335e91d199e99e28f2585c1b25531f29bb54270c --operation <id> [-- <argv>]
  (operations: runtime-info, test, test-focus). Never invoke `.venv/bin/python`,
  `python`, `python3` or `sqlite3`, including as a text editor.
  Read-only Git inspection allowed; exactly one `git add <exact paths>` and one
  `git commit`; no push.

Dependency authority: none.
Git authority: exactly one local non-amended commit; no push, no branch, no tag.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.
Side-effect authority: reversible local repository mutation only. No live
  catalog, service, host, provider, browser or account side effect.
Browser authority: none.
```

## Verification

1. **Synthetic fixtures only.** Build temporary catalogs in test-owned
   directories with linked device and library rows. Exercise: expected candidate
   present and absent; stale receipt; unexpected candidate count; unauthorized
   library change attempt; transaction failure mid-apply; lock contention;
   invalid private storage; idempotent verified completion; inverse rollback
   restoring the exact prior labels.
2. **Invariant assertions after apply and rollback:** the label transition
   happened; device/library IDs and relationships are unchanged; every non-label
   column is unchanged; foreign keys are valid; schema revision remains `0035`;
   the private-catalog checks pass; no selected retired label remains. Read back
   through a fresh connection. `device list` is not sufficient.
3. **Privacy assertions:** command stdout and error payloads contain no IDs,
   library names, media paths or raw SQL; the receipt is private-mode; a
   sanitized digest is the only receipt-derived output.
4. Demonstrate that each new guard fails when its protection is removed, naming
   the mutation and the observed failure. Whenever a guard reads a path, a name
   or an environment value, prove what happens when the input is absent.
5. Run, through the declared route: the focused catalog modules, then the
   declared full Python suite, then the retention module. Report every count and
   any difference from the `4696/8/3/0` baseline.
6. Report **every moved or removed site no test exercises**, and every caller
   your derivation found that this prompt's sample did not name.
7. State the exact commit SHA, `git diff --stat`, confirm Part A is byte-unmoved
   and Part B still measures 20, and show your own measurement and cause for any
   Part C movement. Never tune a pin until the suite is green. Expect `src` Part C
   movement from the new expected-label literals; measure and re-pin from the
   tree, never by memory.

## Derivation and defect-pattern discipline

```text
 1. Derive the affected CLI/repository/test site list by PARSING the artefacts.
    This prompt's anchors are locators, not an inventory.
 2. Resolve every cited line to its literal text BEFORE classifying it.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Verify each occurrence and each caller independently.
 5. Reject a guard that can pass vacuously when its input is absent.
 6. Never truncate an inventory. If output is truncated, disclose it.
 7. Check every mechanical probe against a known-impossible result.
 8. Regenerate every verification table at report time; never transcribe one.
 9. Open and classify every grep hit: production caller, test caller, historical
    compatibility, excluded prose or negative assertion.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

**Collapsing pairs.** For every acceptance set this cut touches, name whether a
collapse raises or fails silently. The device and library candidate sets must
fail loudly on ambiguity, not silently select one row.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the required change touches a frozen path or the engine module; if a
  live catalog, database or host access would be required; if a stale receipt or
  an ambiguous candidate cannot be made to fail closed; if a frozen hash, Part A
  or Part B moves; if a Part C re-pin cannot be reproduced from your own
  measurement; if context pressure reaches the point where a bounded rotation is
  cheaper than a degraded result.

Completion: the bounded interface implemented and tested with synthetic
  fixtures, privacy and invariant assertions, guard-failure demonstrations; the
  maintenance section documented and contract-pinned; focused modules, full
  declared Python suite and retention module green through the declared route;
  one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `30_report_00.md` in
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
echoing `kronika-sole-identity`, session `30` and exchange `01` unchanged. Then:

1. The interface as implemented: flags, receipt format and privacy mode.
2. The synthetic fixture matrix and the invariant/privacy assertions.
3. Guard-failure demonstrations, each with its named mutation.
4. The maintenance documentation added, with its contract pins.
5. Focused module, full-suite and retention counts with elapsed time and any
   baseline difference.
6. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, and any
   Part C movement with cause.
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
  sections 2.5 and 1.7 in full.
- `src/kronika/adapters/cli/catalog.py` in full — the command surface you extend.
- `src/kronika/infrastructure/persistence/device_repository.py`,
  `library_repository.py`, `engine.py`, `private_state.py`, `catalog_schema.py`.
- `tests/contract/test_catalog_cli.py` in full — the fixture and output patterns.
- `docs/UBUNTU_NUC_DEPLOYMENT.md` — the runbook style and where the maintenance
  section belongs.
- `tests/contract/test_nuc_release_docs.py` — the runbook contract pins.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, any real catalog database.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify: the interface is
bounded and private; apply and rollback are compare-and-set and receipt-bound;
the invariant and privacy tests are non-vacuous; no live catalog or host path was
touched; the full suite is green at the reported commit; and Part A and Part B
are unmoved. **The C-DATA-P commit joins the publication batch; after acceptance
the Orchestrator schedules publication of `8a5861c` + `24d2b7d` + `335e91d` +
this cut and then the routine NUC refresh that installs the command before the
C-DATA-H window.**
