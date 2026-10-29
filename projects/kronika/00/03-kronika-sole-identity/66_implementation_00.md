# Authoritative Worker prompt — Worker session 66, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `66`, exchange `01`. Stored under the
Meta filename mapping as `66_implementation_00.md`, with report destination
`66_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **the category-16 correction, part A**: retire the remaining
active-production retired spellings that the session-65 classification listed
— the web shell's superseded mutation-header mirror, the runtime thread-name
and temporary-prefix strings, and the public-published socket default. Part B
(`default_ai_config_path`'s legacy fallbacks) is a separate session with its
own migration-coherence proof.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 66
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-CORR-C9B16A — retire the category-16 active spellings, part A
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The header change moves seven frontend test mirrors with
delicate negative-assertion semantics, and the thread-name strings may be
pinned in unexpected modules that a parse must find before editing.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/65_report_00.md`
section 4 is the normative site list; the anchors below are locators, and
every site must be re-derived by parse at the start commit.

1. **The web shell's mutation header.** `src/kronika/adapters/api/web/app.js`
   builds `Object.assign({ "X-FrameNest-Request": "1" }, headers)` and then
   also sets `merged["X-Kronika-Request"] = "1"`. The canonical gate value
   applied after the merge is the contract; the retired header is a
   superseded compatibility mirror (its in-code comment's "predates the
   dual-read cut" rationale is obsolete: the only servers are the canonical
   ones, and the C7 direction removes compatibility mirrors). Change the
   helper to send only `X-Kronika-Request: "1"`, applied after the merge so a
   caller still cannot weaken it; replace the comment with the canonical-only
   contract sentence. The helper's name `framenestMutationHeaders` is a
   category-11 code-local identifier and **stays**.
2. **The header mirrors in tests** — update each in the same commit, per its
   assertion meaning, naming each module in the report:
   `tests/admin_batch_actions_frontend.test.js` (2),
   `tests/ai_providers_admin_frontend.test.js` (1),
   `tests/catalog_card_ai_quick_action.test.js` (6),
   `tests/tailscale_identity_frontend.test.js` (9),
   `tests/contract/test_local_web_application.py` (2),
   `tests/kronika_ui.test.js` (2),
   `tests/youtube_acquisition_cockpit.test.js` (1). Assertions that today
   expect the retired header present flip to: the canonical header present
   with value `1`, and the retired header **absent** from the emitted object;
   the helper-merging hostile-input cases keep the cannot-weaken semantics
   for the canonical value; source-pattern assertions match the new literal.
   `tests/contract/test_kronika_mutation_header.py` and the companion suites
   that assert the retired header is rejected stay as they are.
3. **Runtime thread names and the temporary prefix.** Rename the producer
   strings to the canonical spelling, deriving each via the repository's own
   convention, and update any test that pins them:
   `src/kronika/application/media_analysis_coordinator.py` (`name` and
   `thread_name_prefix`), `.../upload_catalog_coordinator.py` (both),
   `.../upload_publication_coordinator.py` (both),
   `.../upload_validation_coordinator.py` (both),
   `.../x_acquisition.py` (`thread_name_prefix`),
   `.../youtube_acquisition.py` (`name`),
   `src/kronika/infrastructure/persistence/catalog_backup_workstation.py`
   (`name`), `src/kronika/infrastructure/media_analysis/process.py` (the two
   stored reader-thread names), and
   `src/kronika/infrastructure/media_analysis/contact_sheet.py` (the
   `tempfile.mkdtemp` prefix).
4. **The public-published socket default.**
   `src/kronika/configuration.py`'s `DEFAULT_PUBLIC_PUBLISHED_UDS_PATH`
   becomes the canonical distinct path (`/run/kronika/kronika-public.sock`).
   `WORKSPACE_UDS_PATH` **stays unchanged**: the frozen ADR-0048/0074 bodies
   cite it (category 12). The distinctness validator keeps working. Update
   only pins of the default itself; arbitrary-path fixtures and negative
   inputs (a configured former path as hostile or sample data) stay.
5. **Not in scope.** `default_ai_config_path` and its fallbacks; category-11
   identifiers; category-15 stored keys; anything else.

## Verified starting state, measured by the Orchestrator on 2026-10-18

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                ca280c45755e28b6363690c50d7cdaa42187de96
Public main:                  5b86d896b3ea03f89fef2c90f7af2c121d0ef915 (C9-B sequence unpublished by design)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4713 passed, 8 skipped, 3 warnings, 0 failed
Focused validation:           83 passed (retention, docs, schema-head, sidecar, state-name)
JS baselines:                 23 / 41 / 55 / 6 / 12 / 30; bounded glob 212
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only work: no host contact, no browser, no deployment.

## Authority

```text
Positive authority: edit `src/kronika/adapters/api/web/app.js` for exactly
  the canonical-only header contract; edit the named frontend/contract test
  modules for the header mirrors; edit the eleven named source modules for
  exactly the thread-name/temporary-prefix strings and `configuration.py` for
  `DEFAULT_PUBLIC_PUBLISHED_UDS_PATH`; edit every further test module your
  parse shows pinning one of those changed strings, naming each non-obvious
  module in the report before editing it; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a scalar
  your own measured retention failure shows this commit moved, with the
  arithmetic cause stated; create exactly one local non-amended commit on
  `main`.

Negative authority: every other path; `default_ai_config_path`; the
  category-11 identifiers including the helper name; the category-15 stored
  keys; `WORKSPACE_UDS_PATH`; frozen documents; the retained-and-labeled
  documents; any feature change; any dependency or lockfile change; the `.ap`
  gitlink; any Alembic revision; any `.venv` operation; publication; push;
  force; amend; branch; stash; any host or browser action. If a necessary
  change falls outside the positive scope, stop and report; do not widen
  scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline ca280c45755e28b6363690c50d7cdaa42187de96 --operation <id> [-- <argv>]
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

1. **Header matrix.** The emitted object carries exactly the canonical
   mutation header with value `1`, applied after the merge; the retired
   header appears nowhere in the emitter; each of the seven mirrors asserts
   the new contract; the server-side negative tests still reject the retired
   header.
2. **Thread/temp matrix.** Every renamed string is canonical; each pin found
   updated; no producer left emitting a retired runtime name.
3. **Socket default.** The public default is the canonical distinct path; the
   workspace constant is untouched; the distinctness validator is proven by
   its existing tests.
4. **Measurement discipline.** The retention failure is measured before the
   re-pin; after values are not pre-written; no counted comment is added.
5. **Mutation demonstrations**, each named with its observed failure:
   (a) reintroduce the retired header emission in the helper → the updated
   frontend mirror fails; (b) revert one renamed thread-name string → its pin
   (or the newly added assertion, named) fails.
6. Run, through the declared routes: the touched modules (named), the full
   declared Python suite against `4713/8/3/0`, the retention module, and the
   JS suites plus bounded glob against their exact counts — a JS count
   movement stops the cut and is reported.
7. Report every moved or removed site that no test exercises.
8. State the exact commit SHA, `git diff --stat`, Part A byte-unmoved, Part B
   still empty, and the Part C movement with its measured cause.

## Derivation and defect-pattern discipline

```text
 1. Derive every site by PARSING the start commit. The session-65 tables are
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
  match; if a changed string is pinned in a module outside the granted
  surface; if a JS suite count moves; if a frozen hash or Part A moves; if a
  Part C re-pin cannot be reproduced from your own measurement; if context
  pressure reaches the point where a bounded rotation is cheaper than a
  degraded result.

Completion: the canonical-only header with its mirrors, the canonical thread
  and temporary strings with their pins, the canonical public socket default,
  the measured retention re-pin, the two mutation demonstrations, and one
  local commit.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `66_report_00.md` in
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
echoing `kronika-sole-identity`, session `66` and exchange `01` unchanged.
Then:

1. The header matrix with each mirror's assertion change.
2. The thread/temp matrix with each renamed string and updated pin.
3. The socket default change with the validator proof.
4. The measured retention re-pin with the arithmetic cause.
5. The two mutation demonstrations with their named observed failures.
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
  sections 2, 3 and 4 in full.
- `src/kronika/adapters/api/web/app.js` (the helper and its comment),
  `src/kronika/adapters/api/tailscale_ingress.py` (the gate, read-only),
  `src/kronika/configuration.py` (the two UDS constants).
- The eleven named source modules and the seven named test modules.
- `tests/contract/test_kronika_identity_retention.py`.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`, `.ap/AP.md` §5,
  §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, the parked capture state or
profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the matrices, the mutations and the
retention arithmetic at the reported commit, then issues part B (the
AI-config default switch with the migration-coherence proof) before the
publication and refresh sequence.
