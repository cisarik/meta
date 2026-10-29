# Authoritative Worker prompt — Worker session 33, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `33`, exchange `01`. Stored under the
Meta filename mapping as `33_correction_00.md`, with report destination
`33_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 33
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-C6GUARD — classify preserved foreign paths in unit directives
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. This is one smallest coherent correction to the C6 production
adapter, discovered by the live host preflight and required before the host
window can proceed. The change alters unit-directive transformation behavior, so
the correction must be exact, tested and provably narrow; a fresh independent
re-audit follows before the preflight is re-run.

## The finding, exactly

`migrate-identity preflight` against the live host stopped fail-closed with
`unit directive ReadWritePaths path is not classifiable`
(`EXIT_MIGRATION` 27), no mutation. The host probe identified the source: the
operator drop-in `/etc/systemd/system/framenest.service.d/30-publication-write-path.conf`
contains `ReadWritePaths=/srv/media/framenest-published` — a host-side custom
media/publication path containing the retired spelling that appears nowhere in
the repository.

`transform_path_value` deliberately preserves foreign/custom paths outside every
migrated root, and the accepted plan says "preserve custom media roots" and
forbids altering library roots or original media. But the directive-level guard
(`transformed == token and "framenest" in token` → raise) cannot distinguish a
deliberate custom path from an incomplete rename, so it refuses a form the
design intends to preserve.

## Correction specification

1. **One unified path-token classification**, used at every guard site where
   `transform_path_value` leaves a token unchanged and the token contains the
   retired spelling. Classification order:

```text
frozen prefix (MIGRATION_FROZEN_PATH_PREFIXES):        preserve, classifiable
under or equal a moved root (MIGRATION_OLD_TO_NEW_ROOTS):
    existing transform semantics (raises on leftover retired spelling)
near-miss variant of a moved root:
    token starts with the moved root's exact text but is neither equal to it
    nor under it with a path separator (for example /opt/framenest-old,
    /run/framenestx, /etc/framenest.env):                 refuse, fail closed
anything else (foreign/custom path):                    preserve, classifiable
```

2. **Apply it at every derived guard site**, not only the one that fired. Derive
   the complete set yourself from the transformer: the `SYSTEMD_PATH_DIRECTIVES`
   branch, the `LoadCredential` path, and both `Exec*` forms (plain token and
   `{ path=… }`). Report the derived set. Where a token is under a moved root,
   keep the existing transformation and its existing refusal. Where it is
   frozen, keep preserving. Where it is foreign/custom, preserve even when it
   contains the retired spelling. Only near-miss variants of a moved root
   continue to refuse.
3. **No other behavior change.** Do not alter section/comment/blank-line
   preservation, directive parsing, `LoadCredential` identifier handling, sudo
   rules, environment transformation, or any other transformer semantics. Do
   not add capabilities, do not touch the frozen sets, do not change error codes.
4. **Tests** in `tests/contract/test_kronika_identity_migration.py`, for each
   site shape: frozen token preserved; foreign/custom token containing the
   retired spelling preserved (use a synthetic foreign path such as
   `/srv/media/framenest-example` — do not embed the live host path in the
   repository); near-miss token refused; under-root leftover refused; under-root
   canonical transform unchanged. Add one end-to-end drop-in text test that
   shows the preserved foreign token alongside a transformed moved-root token
   in the same directive.
5. **Mutation demonstrations.** Show the new classification is load-bearing:
   removing the foreign-preserve path makes the foreign-token test fail;
   weakening the near-miss rule makes the near-miss test fail; removing the
   frozen check makes the frozen test fail. Name each mutation and its observed
   failure.

## Verified starting state, measured by the Orchestrator on 2026-10-10

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                b8ec042b5bf1835df77c81341abc75e9cf8ab059
Public main:                  b8ec042b5bf1835df77c81341abc75e9cf8ab059, divergence 0 0
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at b8ec042:   4828 passed, 8 skipped, 3 warnings, 0 failed
Retention module:             15 passed
```

Transformer anchors at the baseline (locators, not an inventory — re-derive):
`_systemd_transform_value` and its guard sites, `transform_unit_dropin_text`,
`transform_path_value`, `MIGRATION_FROZEN_PATH_PREFIXES`,
`MIGRATION_OLD_TO_NEW_ROOTS`, `SYSTEMD_PATH_DIRECTIVES`.

**No host contact.** The live host represented the finding; all work and tests
are repository-only with synthetic fixtures.

## Authority

```text
Positive authority: edit `deploy/ubuntu/kronika_release.py` for exactly the
  unified classification at the derived guard sites; edit
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
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline b8ec042b5bf1835df77c81341abc75e9cf8ab059 --operation <id> [-- <argv>]
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

1. Before editing, reproduce the exact live failure shape with a synthetic
   fixture: a drop-in text whose `ReadWritePaths` token is a foreign path
   containing the retired spelling must raise at the baseline, and must be
   preserved after the correction. Record both outcomes.
2. Demonstrate each guard site's classification with the full matrix: frozen,
   foreign, near-miss, under-root transform, under-root leftover.
3. Mutation demonstrations as specified.
4. Run, through the declared route: the focused migration module, then the
   declared full Python suite, then the retention module. Report every count,
   elapsed time and any difference from the `4828/8/3/0` baseline.
5. Report **every moved or removed site that no test exercises**, and every
   guard site your derivation found that this prompt did not name.
6. State the exact commit SHA, `git diff --stat`, confirm Part A is byte-unmoved
   and Part B still measures 20, and show your own measurement and cause for any
   Part C movement. Never tune a pin until a suite is green.

## Derivation and defect-pattern discipline

```text
 1. Derive the guard-site list by PARSING the transformer. The anchors above
    are locators, not an inventory.
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

**Collapsing pairs.** The classification must fail loudly for near-miss tokens
and must never silently rewrite a foreign path.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the derived guard set differs materially from this prompt's sample;
  if a change would weaken the under-root leftover refusal; if a frozen hash,
  Part A or Part B moves; if a Part C re-pin cannot be reproduced from your own
  measurement; if a necessary change falls outside the positive scope.

Completion: the unified classification implemented at every derived guard site;
  the matrix and mutation demonstrations green; focused module, full declared
  Python suite and retention module green through the declared route; one local
  commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `33_report_00.md` in
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
echoing `kronika-sole-identity`, session `33` and exchange `01` unchanged. Then:

1. The reproduced baseline failure and the post-correction preservation, both
   with exact evidence.
2. The derived guard-site set with every classification rule application.
3. The matrix results per site shape.
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

- `deploy/ubuntu/kronika_release.py` — `_systemd_transform_value`,
  `transform_unit_dropin_text`, `transform_path_value`,
  `MIGRATION_FROZEN_PATH_PREFIXES`, `MIGRATION_OLD_TO_NEW_ROOTS`,
  `MIGRATION_SEGMENT_RENAMES`, `SYSTEMD_PATH_DIRECTIVES`.
- `tests/contract/test_kronika_identity_migration.py` — the transformer and
  structural directive tests.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
  section 2.10 — the preservation clause and the apply sequence.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/28_report_00.md`
  section 2 row 13 — the audited transformation behavior this correction
  narrows.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify: the reproduction and
the correction; the complete derived guard set; the near-miss and under-root
refusals unchanged; the frozen preservation unchanged; the foreign preservation
new and narrowly scoped; the full suite green at the reported commit; and Part A
and Part B unmoved. **A fresh independent re-audit of this correction is the
next step**, and only after its PASS may the C6-H preflight be re-run.
