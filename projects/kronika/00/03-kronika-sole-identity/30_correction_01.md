# Authoritative Worker prompt — Worker session 30, exchange 02

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, current Worker session `30`, exchange `02`. Stored under
the Meta filename mapping as `30_correction_01.md`, with report destination
`30_report_01.md` in the same directory. Storage naming is Meta policy and grants
no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 30
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-CDATAP — finalize the bounded catalog label maintenance candidate
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Continuity anchor: the terminal `PARTIAL` report for `KSI-IMPL-CDATAP`, session
`30`, exchange `01` (`30_report_00.md`), whose candidate is staged in the index
at `HEAD` `335e91d199e99e28f2585c1b25531f29bb54270c` and was never committed.
Prior authority expired at that report. This exchange grants complete new
bounded authority for the correction and the single commit only. Re-gate the
repository and the index before editing: the staged set must still be exactly the
seven paths named by that report. Retained context is convenience, not authority;
your evidence is non-independent; stop on any conflict with current repository or
index state.

Rationale: `High`. The candidate was complete and validated except for one pin
file outside the previous grant's allowlist. This correction is narrow, but it
finalizes the only interface that will modify live catalog rows, so its
verification must be as strict as the candidate's.

## Finding and correction scope

The previous grant omitted `tests/contract/test_kronika_product_string_agreement.py`
from its positive authority. Because the candidate adds two brand-bearing
canonical runtime literals, that agreement guard now reports two unexpected rows
and fails exactly three tests. The Orchestrator independently reproduced the
three failures and confirmed the staged scope. This is the Orchestrator's
allowlist defect; the previous stop was correct.

### Required correction

Edit `tests/contract/test_kronika_product_string_agreement.py`. The measured
drift from report 30 §8 is:

```text
unexpected rows:
  ("src/kronika/infrastructure/persistence/identity_labels.py", "<module>", "Constant", 0)
  ("src/kronika/infrastructure/persistence/identity_labels.py", "<module>", "Constant", 1)
missing:  none
changed:  none
counts:   OCCURRENCE_COUNT 53 -> 55; IN_SCOPE_OCCURRENCE_COUNT 51 -> 53
EXPECTED_DUPLICATE_LITERALS: unchanged (both literals unique)
```

Re-derive every value yourself from the tree before editing. If any value,
ordering or duplicate classification differs from this sample, stop and report;
never tune a pin until a failing run passes.

### Included secondary completions (bounded, from the same report)

1. Add one synthetic-fixture test to
   `tests/contract/test_catalog_identity_labels.py` for the library-only path:
   a receipt with library selections and no device selection, applied and rolled
   back with `--include-libraries`, asserting the same invariant and privacy
   rules as the existing matrix. Demonstrate it fails when its protection is
   removed.
2. Add one sentence to the maintenance section of
   `docs/UBUNTU_NUC_DEPLOYMENT.md` naming the execution-owner requirement: the
   command must run as the catalog owner because the private-catalog check
   compares ownership. Add or update the matching pin in
   `tests/contract/test_nuc_release_docs.py` only if your derivation shows the
   existing pins require it.

### Finalization

After the corrections, freeze and commit the candidate. `git add` exactly the
corrected paths and create **exactly one local non-amended commit on `main`**
containing the seven previously staged paths plus
`tests/contract/test_kronika_product_string_agreement.py` and any secondary file
your derivation names. Suggested subject consistent with repository style:
`feat(catalog): add bounded identity-label maintenance`. No push, no branch, no
amend, no second commit.

## Verified starting state, measured by the Orchestrator on 2026-10-08

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
HEAD:                         335e91d199e99e28f2585c1b25531f29bb54270c
Index:                        exactly the seven paths staged by exchange 30/01
Working tree:                 no unstaged changes besides the staged candidate
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Full suite at the candidate:  4733 passed, 8 skipped, 3 failed (the three
                              agreement tests confirmed by the Orchestrator)
```

```text
staged paths (verify, do not trust):
  docs/UBUNTU_NUC_DEPLOYMENT.md
  src/kronika/adapters/cli/catalog.py
  src/kronika/infrastructure/persistence/identity_labels.py
  tests/contract/test_catalog_cli.py
  tests/contract/test_catalog_identity_labels.py
  tests/contract/test_kronika_identity_retention.py
  tests/contract/test_nuc_release_docs.py
```

**No host, catalog or network contact.** The catalog row values remain carried
evidence; this cut touches no real database.

## Authority

```text
Positive authority: edit `tests/contract/test_kronika_product_string_agreement.py`
  for exactly the required correction; edit
  `tests/contract/test_catalog_identity_labels.py` for the one library-only
  test; edit `docs/UBUNTU_NUC_DEPLOYMENT.md` for the one owner sentence; edit
  `tests/contract/test_nuc_release_docs.py` only for the matching pin if the
  derivation requires it; edit `tests/contract/test_kronika_identity_retention.py`
  only to re-pin a Part C scalar your own measurement shows this correction moved;
  preserve every already-staged path exactly as staged; create exactly one local
  non-amended commit as specified.

Negative authority: every other path; `deploy/ubuntu/kronika_release.py` and
  `src/kronika/infrastructure/persistence/engine.py` are frozen; any dependency
  or lockfile change; any change to `pyproject.toml`, `ap.project.conf` or the
  `.ap` gitlink; any frozen document or Alembic revision; publication; push;
  force; amend; branch; stash; any NUC contact or SSH; any live catalog or
  database access; any provider, browser or capture contact; any secret,
  personal Fish configuration or browser-profile read. If a necessary change
  falls outside the positive scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 335e91d199e99e28f2585c1b25531f29bb54270c --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `sqlite3`, including as a text
  editor.
  Read-only Git inspection allowed; exactly one `git add <exact paths>` and one
  `git commit`; no other Git write.

Dependency authority: none.
Git authority: exactly one local non-amended commit; no push, no branch, no tag.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md, the accepted plan and report 30 are authoritative inside their
  scope. On conflict between retained context and current repository evidence,
  stop.
Side-effect authority: reversible local repository mutation only. No live
  catalog, service, host, provider, browser or account side effect.
Browser authority: none.
```

## Verification

1. Before editing, re-gate: `HEAD` unchanged, the index contains exactly the
   seven staged paths, no unstaged surprise. If not, stop and report.
2. Re-derive the agreement drift yourself; run the agreement module and record
   the exact three failures before the edit.
3. After the edit, the agreement module is green; the new library-only test is
   green and fails under its named mutation; the owner-sentence pin (if any) is
   green.
4. Run, through the declared route: the agreement module, the identity-labels
   module, the docs module, then the declared full Python suite, then the
   retention module. Report every count, elapsed time, and any difference from
   the expected all-green candidate.
5. Report **every site no test exercises**, and any derivation finding this
   prompt's sample did not name.
6. Report the single commit SHA, `git diff HEAD~1 --stat`, confirm Part A is
   byte-unmoved and Part B still measures 20, and show your own measurement and
   cause for any Part C movement. Confirm the working tree is clean and the push
   was not performed.

## Derivation and defect-pattern discipline

```text
 1. Derive site lists by PARSING each artefact. This prompt's values are a sample.
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

## Finishing

```text
Stopping conditions: stop without improvising if the repository or index gate
  does not match; if a re-derived pin value differs from the sample; if the
  agreement guard's duplicate classification changed; if a necessary change
  falls outside the positive scope; if any unrelated test fails (classify it and
  report; do not fix opportunistically); if a frozen hash, Part A or Part B
  moves; if context pressure reaches the point where a bounded rotation is
  cheaper than a degraded result.

Completion: the three agreement failures resolved from your own measurement; the
  library-only test added with its mutation demonstration; the owner sentence and
  matching pin added if required; scheduled modules and the full declared Python
  suite green; retention green; exactly one local commit; tree clean; report
  delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `30_report_01.md` in
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
echoing `kronika-sole-identity`, session `30` and exchange `02` unchanged. Then:

1. The re-gate result and the pre-edit three-failure evidence.
2. Your re-derived pin values and the edit; any difference from the sample.
3. The library-only test and its mutation demonstration.
4. The owner sentence and its pin, or the reason none was required.
5. Agreement, identity-labels, docs, full-suite and retention counts with
   elapsed times.
6. The single commit SHA, `git diff HEAD~1 --stat`, Part A unmoved, Part B still
   20, Part C movement with cause, clean tree, no push.
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

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/30_report_00.md`
  in full — your own terminal report and the finding origin.
- `tests/contract/test_kronika_product_string_agreement.py` in full — the guard
  you correct.
- `tests/contract/test_catalog_identity_labels.py` — the fixture patterns for the
  library-only test.
- `docs/UBUNTU_NUC_DEPLOYMENT.md` maintenance section and
  `tests/contract/test_nuc_release_docs.py` — the documentation surface.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12, and the current-session renewal contract.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, any real catalog database.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify: the agreement guard
was corrected from a re-derived measurement, not by tuning; the three failures
are green; the library-only test is non-vacuous; the staged candidate is
preserved; exactly one commit exists with the expected content; Part A and Part B
are unmoved; and the push was not performed. After acceptance the C-DATA-P
candidate joins the publication batch (`8a5861c` + `24d2b7d` + `335e91d` + this
commit), then the routine NUC refresh installs the command before the C-DATA-H
window.
