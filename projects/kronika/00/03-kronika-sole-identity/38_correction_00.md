# Authoritative Worker prompt — Worker session 38, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `38`, exchange `01`. Stored under the
Meta filename mapping as `38_correction_00.md`, with report destination
`38_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 38
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-C6UNK — preserve brand-free unknown unit directives
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The live C6 preflight now passes the foreign-path and escaped
revision cases but stops fail-closed on a benign, brand-free drop-in directive
outside the transformer's supported set. The correction replaces the blanket
unknown-directive refusal with a principled policy so the remaining real host
drop-ins install without further one-at-a-time surprises. A fresh independent
re-audit follows before the preflight is re-run.

## The finding, exactly

`migrate-identity preflight` against the live host stopped with
`kronika-release: unit directive RuntimeDirectoryMode is not supported`
(`EXIT_MIGRATION` 27; no mutation).

The complete directive-key set of the installed web drop-ins, derived by a
keys-only host probe, is:

```text
20-ai-credential.conf               LoadCredential
30-publication-write-path.conf      ReadWritePaths
40-runtime-directory-mode.conf      RuntimeDirectoryMode
framenest-research-credential.conf  LoadCredential
```

`LoadCredential` and `ReadWritePaths` are already handled structurally. Only
`RuntimeDirectoryMode=0700` (benign, no path, no identity, no retired spelling)
is refused because `transform_unit_dropin_text` refuses every directive outside
its supported sets.

## Correction specification

1. **Principled unknown-directive policy.** For a directive whose key is not in
   the supported sets, refuse only when the retired spelling appears in the
   directive key or value (case-insensitive `framenest`); otherwise preserve the
   line byte-for-byte. The refusal keeps the existing message
   `unit directive <key> is not supported` and exit 27. Nothing else about the
   transformer changes: supported directives, path classification, revision
   rendering, near-miss and leftover refusals, comment/section/blank-line
   preservation, and the continued-directive refusal all stay exactly as they
   are.
2. **No other behavior change.** Do not change the classifier, the revision
   renderer, the frozen or moved sets, sudo rules, environment transformation or
   any error code.
3. **Tests** in `tests/contract/test_kronika_identity_migration.py`:
   - `RuntimeDirectoryMode=0700` in a `[Service]` drop-in is preserved
     byte-for-byte and installs through `read_migration_observation` without
     refusal;
   - `Environment=FOO=bar` and `UnknownDirective=value` (brand-free) are
     preserved;
   - brand-bearing unknowns refuse with the same message and exit 27:
     at least `UnknownDirective=framenest-x`, `Environment=FRAMENEST_X=1`, and a
     key containing the retired spelling;
   - an end-to-end drop-in mixing `RuntimeDirectoryMode`, `ReadWritePaths` with a
     foreign token, and `LoadCredential` transforms correctly;
   - update the two existing tests that assert refusal for brand-free unknown
     forms (`test_preflight_refuses_an_unknown_dropin_directive`,
     `test_structural_dropin_transformation_refuses_unknown_forms`) to the new
     contract, keeping genuine refusal cases. Report every adjusted line.
   - the full existing matrix stays green.
4. **Mutation demonstrations:** removing the brand check makes the brand-bearing
   unknown tests fail; forcing refusal for brand-free unknowns makes the
   preservation tests fail. Name each mutation and observed failure.

## Verified starting state, measured by the Orchestrator on 2026-10-11

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                78cba281960e2f17137647bcc90aab83847a1c0c
Public main:                  78cba281960e2f17137647bcc90aab83847a1c0c, divergence 0 0
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at 78cba28:   4873 passed, 8 skipped, 3 warnings, 0 failed
Focused migration module:     203 passed
Retention module:             15 passed
```

**No host contact.** All work and tests are repository-only with synthetic
fixtures.

## Authority

```text
Positive authority: edit `deploy/ubuntu/kronika_release.py` for exactly the
  unknown-directive policy; edit
  `tests/contract/test_kronika_identity_migration.py` for the tests and mutation
  demonstrations; edit `tests/contract/test_kronika_identity_retention.py` only
  to re-pin a Part C scalar that your own measurement shows this correction
  moved, with the arithmetic cause stated; create exactly one local non-amended
  commit on `main`.

Negative authority: every other path; any dependency or lockfile change; any
  change to `pyproject.toml`, `ap.project.conf` or the `.ap` gitlink; any frozen
  document or Alembic revision; publication; push; force; amend; branch; stash;
  any NUC contact or SSH; any migration invocation; any provider, browser or
  capture contact; any secret or personal-configuration read. If a necessary
  change falls outside the positive scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 78cba281960e2f17137647bcc90aab83847a1c0c --operation <id> [-- <argv>]
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

1. Reproduce the live failure shape before editing: a `[Service]` drop-in with
   `RuntimeDirectoryMode=0700` must raise at the baseline and be preserved after
   the correction. Record both.
2. Demonstrate the policy matrix: brand-free unknown preserved; brand-bearing
   unknown refused (key and value variants); supported directives unchanged.
3. Report every adjusted existing test line and why the change is the intended
   contract, not a weakened assertion.
4. Mutation demonstrations as specified.
5. Run, through the declared route: the focused migration module, then the
   declared full Python suite, then the retention module. Report every count,
   elapsed time and any difference from the `4873/8/3/0` baseline.
6. Report **every moved or removed site that no test exercises**, and every
   branch your derivation found that this prompt did not name.
7. State the exact commit SHA, `git diff --stat`, confirm Part A is byte-unmoved
   and Part B still measures 20, and show your own measurement and cause for any
   Part C movement. Never tune a pin until a suite is green.

## Derivation and defect-pattern discipline

```text
 1. Derive the branch list by PARSING the transformer. Locators are not an
    inventory.
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

**Collapsing pairs.** The brand check must be case-insensitive and must never
silently pass a brand-bearing unknown directive through.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the policy would weaken any existing supported-directive handling or
  refusal; if a frozen hash, Part A or Part B moves; if a Part C re-pin cannot be
  reproduced from your own measurement; if a necessary change falls outside the
  positive scope.

Completion: the policy implemented and tested; the two adjusted tests reflect
  the stated contract; mutation demonstrations green; focused module, full
  declared Python suite and retention module green through the declared route;
  one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `38_report_00.md` in
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
echoing `kronika-sole-identity`, session `38` and exchange `01` unchanged. Then:

1. The reproduced baseline refusal and the post-correction preservation.
2. The policy matrix with key and value variants.
3. Every adjusted existing test line, with the contract reasoning.
4. Mutation demonstrations, each with its named mutation.
5. Focused module, full-suite and retention counts with elapsed time and any
   baseline difference.
6. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, and Part C
   movement with cause.
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

- `deploy/ubuntu/kronika_release.py` — `transform_unit_dropin_text`,
  `_systemd_transform_value` and its supported sets.
- `tests/contract/test_kronika_identity_migration.py` — the two tests to adjust
  and the full transformer matrix.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/35_report_00.md`
  (the accepted B1 repair report) and `37_report_00.md` (its accepted re-audit)
  — the transformer state this correction extends.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify: the reproduction and
the policy; the adjusted tests reflect the stated contract; brand-bearing
unknowns still refuse; the full suite is green at the reported commit; and
Part A and Part B are unmoved. **A fresh independent re-audit follows**, and
only after its PASS may the C6-H preflight be re-run.
