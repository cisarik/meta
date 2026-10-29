# Authoritative Worker prompt — Worker session 52, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `52`, exchange `01`. Stored under the
Meta filename mapping as `52_implementation_00.md`, with report destination
`52_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is the **closing continuation of C7-B/1**. Sessions 49–51 built and
verified the candidate; session 51 closed the fixture-input class and ran the
full suite to completion, which exposed one final pin family:
`tests/contract/test_kronika_product_string_agreement.py`, whose inventory no
longer matches the candidate's six new canonical `"Kronika"` path-component
constants. This grant adopts the 53-file candidate, authorizes the test-side
completion authority broadly enough to close any remaining measured mismatch,
and requires the green full suite and the single commit.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 52
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C7B1 — complete the settings, defaults and command-code removals
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The candidate is productive-complete and three sessions of
verification have closed every class except measured test-side pins. What
remains is mechanical but exacting: bring the product-string inventory up to
the truth the canonical development defaults created, never weakening it into
a prefix check, then run the full suite, measure the ledger and commit.

## The preserved candidate

```text
53 files changed, 838 insertions(+), 1005 deletions(-)
Index empty; no untracked files; no deleted paths; HEAD aee0a60; no commit.

Composition: the 50 paths carried since session 49, the retention module
(session 50), and the two timer fixture modules (session 51:
tests/contract/test_catalog_backup_timer.py,
tests/contract/test_catalog_offdevice_timer.py).
Adopted parity file SHA-256:
8bf01f8382400f958427e7b309f0c23b6067c63a3b8240b320a3f285a92e62d9
```

Verify the tree matches this state (status, diff stat, parity hash) before
building on it; if it does not, stop and report. Treat the candidate as your
own work from this point.

## Known remaining work, exactly

1. **Product-string inventory completion.** In
   `tests/contract/test_kronika_product_string_agreement.py` the measured
   inventory is length 63 against the pinned `OCCURRENCE_COUNT` 57, and the
   `"Kronika"` duplicate multiplicity is 8 against the pinned 2. The six
   unexpected nodes are the `"Kronika"` path-component constants in
   `src/kronika/infrastructure/runtime/development.py` (`_database_path`,
   `_runtime_dir`, `_log_path`, indexes 0 and 1) — the candidate's canonical
   development defaults, exactly what the inventory exists to track. Update
   the inventory and its pins to the measured canonical truth (occurrence
   count, duplicate multiplicity, the six node entries, and any further
   pinned structure the tests require), with the arithmetic cause recorded.
   **Do not weaken the inventory into a prefix check or a subset pin**, and do
   not remove any other product string.
2. **Completion authority for measured test-side mismatches.** If the suites
   reveal any further pinned inventory, fixture or assertion that no longer
   matches the candidate's canonical truth, update it to the measured truth
   while preserving the test's behavioral function, and list every edit with
   its before/after. Never weaken an assertion, never delete a test that still
   has a live subject (retire only a genuinely vacuous premise, with the cause
   stated as session 51 did). If a mismatch would require editing a production
   source beyond the preserved candidate, stop and report.
3. **Suites to green.** Run the full declared Python suite to completion and
   report its counts against `4955/8/3/0`; re-run the retention module, the six
   JS suites and the bounded non-browser JS glob.
4. **Final ledger.** Regenerate every Part C number from the final tree and
   update the running comment with any movement this grant adds (the
   inventory file and pins live in `tests`); keep Part A byte-unmoved, Part B
   at 20, and the four content-path departures from session 50 exact.
5. **Commit.** One local non-amended commit on `main` naming all changed
   paths; no push.

## Verified starting state, measured by the Orchestrator on 2026-10-14

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                aee0a60a04b78685608ec5a65ec5780c7d9884e7
Public main:                  aee0a60a04b78685608ec5a65ec5780c7d9884e7
Working tree:                 the preserved 53-file candidate above
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4955 passed, 8 skipped, 3 warnings, 0 failed
Candidate full suite (session 51, completed):
                              4 failed, 4967 passed, 8 skipped, 3 warnings
                              (the four are the product-string inventory family)
Retention module:             15 passed (candidate tree)
Focused timer/reader modules: 95 passed (session 51)
Six JS suites + bounded glob: 27/42/54/6/12/30 + 213, all green
```

Re-derive the git/AP gates yourself at the start; the dirty candidate tree is
intentional. If anything else fails, stop and report.

## Authority

```text
Positive authority: keep and complete the preserved candidate; edit
  `tests/contract/test_kronika_product_string_agreement.py` for the measured
  inventory completion; edit any further test module or support file whose
  pins or fixtures no longer match the candidate's canonical truth, preserving
  each test's behavioral function and listing every edit with its before/after;
  edit `tests/contract/test_kronika_identity_retention.py` for the measured
  scalar re-pins and their arithmetic; create exactly one local non-amended
  commit on `main`.

Negative authority: production sources beyond the preserved candidate; the
  twenty Part B deletion paths; the console aliases in `pyproject.toml`;
  `extension/**` and the served web assets; the operator scripts and their
  mirrors (C7-B/2); every frozen document and ADR; any dependency, lockfile or
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
2. **Inventory completion table.** Every node added, every pin changed, with
   before/after values and the arithmetic cause; the inventory remains a full
   occurrence-accurate check (no prefix collapse, no subset pin).
3. **Completion edits table.** Every further pinned/fixture edit with its
   before/after and the preserved behavioral function; no weakened assertion.
4. **Full suite green.** Counts against `4955/8/3/0` with the arithmetic of
   any movement; retention `15`; six JS suites `27/42/54/6/12/30`; glob `213`.
5. Every moved or removed site that no test exercises; every consumer the
   candidate touched that this grant did not name.
6. Commit facts: SHA, `git diff --stat`, Part A byte-unmoved, Part B still 20,
   Part C movement and content-path departures with per-tree arithmetic.

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

**Collapsing pairs.** Do not collapse an inventory completion with an
inventory weakening: the full occurrence accuracy stays. Do not collapse a
content-path departure with a scalar movement. Do not collapse the
canonical-only simplification with any remaining dual behavior.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the preserved candidate does
  not match its described state; if a mismatch would require editing a
  production source beyond the candidate; if a change would touch a Part B
  deletion path, a console alias, `extension/**`, the served web assets, the
  operator scripts or a frozen document; if an edit would weaken an assertion
  or an inventory; if a measured ledger value cannot be reproduced; if a
  `.venv` operation would be required; if context pressure reaches the point
  where a bounded rotation is cheaper than a degraded result — in that case
  stop before any commit and name exactly what remains.

Completion: the product-string inventory complete and accurate; every
  remaining pinned/fixture mismatch closed with its edit table; the full
  Python suite green against its baseline; retention and all JS suites green;
  the final ledger measured and recorded; one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `52_report_00.md` in
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
echoing `kronika-sole-identity`, session `52` and exchange `01` unchanged. Then:

1. Candidate integrity, the inventory completion table and the completion
   edits table.
2. Suite results with counts, elapsed time and baseline differences.
3. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, Part C
   movement and content-path departures with per-tree arithmetic.
4. Every site no test exercises.
5. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification. Finish with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

## Mandatory reading

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/51_report_00.md`
  and `50_report_00.md` in full — the candidate's own record.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
  section 2.13 in full.
- `tests/contract/test_kronika_product_string_agreement.py` in full, and
  `tests/contract/test_kronika_identity_retention.py`.
- `docs/WORKER_EXECUTION_CONTRACT.md` (the `.venv` prohibition),
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the completion tables, the ledger and
the green full suite at the reported commit, then grants **C7-B/2** (the
physical removals and retired readers), after which the Cooperator environment
refresh, publication and the exact-main NUC refresh follow with **C7-B/3**. No
push, refresh or host contact is authorized inside this prompt.
