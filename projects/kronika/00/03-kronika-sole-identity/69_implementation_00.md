# Authoritative Worker prompt — Worker session 69, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `69`, exchange `01`. Stored under the
Meta filename mapping as `69_implementation_00.md`, with report destination
`69_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **the X video artifact correction** (`KSI-CORR-XVIDEO`), a bounded
app-side fix discovered by the Cooperator's rendered acceptance. It is not an
identity cut and does not reopen any closed wholesale.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 69
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-CORR-XVIDEO — merge-aware X video artifact resolution
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The fix touches a fail-closed acquisition path with an
external tool behavior, and the strictness rules (single file, no symlinks, no
partials, multiple candidates fail closed) must survive the relaxation.

## The defect, measured

Every X **video** save in the catalog history fails with
`acquisition` / `X_STAGING_FAILED` ("X produced no artifact"), while every
**image** save succeeds (`cataloged`) — 2026-10-13, 2026-10-20 and 2026-10-29
all show the same pattern. A manual reproduction of the downloader's exact
yt-dlp invocation (same argv, same minimal environment, cwd = a temp
directory) printed the media id, exited 0, and left **`artifact.bin.mp4`**.
yt-dlp appends the extension when it post-processes the merged video+audio
stream, while the downloader's artifact resolution checks for the **exact**
fixed name only (`artifact.bin`), so the acquisition raises "no artifact".
The photo path (the pbs bridge writes the exact fixed name) is unaffected.

## Specification

1. **Merge-aware, still strict artifact resolution.** In
   `src/kronika/infrastructure/x/downloader.py` (and the staging helper only if
   your parse shows the resolution belongs there), resolve the acquired
   artifact as: the exact fixed name when it is a regular file; otherwise
   **exactly one** regular file in the claim's staging directory whose name is
   the fixed name followed by one appended extension segment (a short
   alphanumeric suffix; `.part`, temporary names, symlinks and directories are
   never candidates). Zero candidates keeps the existing
   `X_STAGING_FAILED` "X produced no artifact" failure unchanged. More than one
   candidate fails closed with a distinct, named error.
2. **Consumers use the resolved path.** Derive every consumer of the staging
   artifact (size, digest, returned acquisition, staging cleanup, publication
   copy) and make it use the resolved path; name each in the report. Do not
   change the staging directory contract, the fixed filename constant, the
   photo bridge behavior, the subprocess argv/env, or the understandable
   error codes beyond the one new fail-closed ambiguity code.
3. **Tests.** Find every module that exercises the downloader or the staging
   artifact path by parse (`tests/unit/infrastructure/x/…` and any contract
   module), name each before editing, and cover: a merged-video subprocess
   writing `artifact.bin.mp4` resolves and succeeds with the right size and
   digest; nothing written keeps the unchanged "no artifact" failure; two
   candidates fail closed with the named error; a symlink or a `.part`-only
   directory never resolves; the photo path stays exact-name. Add them to the
   owning module(s), or create one named test module only if no owner exists,
   and say why in the report.
4. **No unrelated behavior.** No dependency or lockfile change, no argv change,
   no error-message rewording beyond the new code, no extension/companion
   change.

## Verified starting state, measured by the Orchestrator on 2026-10-29

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                22615a7721d89777bf1614b03baec220c80d3782
Public main:                  22615a7721d89777bf1614b03baec220c80d3782 (published; NUC serves it)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4713 passed, 8 skipped, 3 warnings, 0 failed
Retention module:             15 passed
JS baselines:                 23 / 41 / 55 / 6 / 12 / 30; bounded glob 212
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only work: no host contact, no browser, no external X
acquisition.

## Authority

```text
Positive authority: edit `src/kronika/infrastructure/x/downloader.py` (and the
  staging helper only if the parse shows the resolution lives there) for
  exactly the merge-aware resolution and the named fail-closed ambiguity
  error; edit the test modules owning the downloader/staging coverage, naming
  each before editing; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a Part C
  scalar that your own measured retention failure shows this commit moved,
  with the arithmetic cause stated; create exactly one local non-amended
  commit on `main`.

Negative authority: every other path; any external X or network action; any
  extension/companion change; the staging directory contract and the fixed
  filename constant; the subprocess argv/environment; any dependency or
  lockfile change; the `.ap` gitlink; any Alembic revision; any `.venv`
  operation; publication; push; force; amend; branch; stash; any host or
  browser action. If a necessary change falls outside the positive scope, stop
  and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 22615a7721d89777bf1614b03baec220c80d3782 --operation <id> [-- <argv>]
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

1. **Resolution matrix.** Exact fixed name resolves; one merged-name candidate
   resolves; zero candidates keeps the unchanged failure; two candidates fail
   closed with the named error; symlinks, directories and `.part` files never
   resolve.
2. **Consumers.** The size/digest/acquisition/cleanup/publication paths use the
   resolved artifact; each named in the report.
3. **Photo path unchanged** and its tests green without semantic edits.
4. **Measurement discipline.** The retention failure is measured before the
   re-pin; after values are not pre-written; no counted comment is added.
5. **Mutation demonstration.** Restore the exact-name-only resolution → the
   merged-video test fails, with the observed failure named.
6. Run, through the declared routes: the touched modules (named), the full
   declared Python suite against `4713/8/3/0`, the retention module, and the JS
   suites plus bounded glob as unaffected sanity.
7. Report every moved or removed site that no test exercises.
8. State the exact commit SHA, `git diff --stat`, Part A byte-unmoved, Part B
   still empty, and the Part C movement with its measured cause.

## Derivation and defect-pattern discipline

```text
 1. Derive site lists by PARSING the artefact. This prompt's anchors are
    locators, not an inventory.
 2. Resolve every cited symbol to its literal definition BEFORE editing.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Verify each occurrence and each caller independently.
 5. Never relax a fail-closed rule further than the measured defect requires.
 6. Never truncate an inventory. If output is truncated, disclose it.
 7. Check every mechanical probe against a known-impossible result.
 8. Regenerate every verification table at report time; never transcribe one.
 9. Open and classify every grep hit.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

**Collapsing pairs.** Do not collapse the exact-name and merged-name cases;
do not collapse the artifact resolution with the photo bridge; do not collapse
the ambiguity failure with the no-artifact failure.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the resolution needs a write outside the granted paths; if a
  consumer cannot be derived with a parse; if a frozen hash or Part A moves;
  if a Part C re-pin cannot be reproduced from your own measurement.

Completion: the merge-aware strict resolution with its consumers, the named
  tests, the measured re-pin if any, the mutation proof, and one local commit.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `69_report_00.md` in
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
echoing `kronika-sole-identity`, session `69` and exchange `01` unchanged.
Then:

1. The resolution matrix and the consumer list, each named.
2. The tests added or modified, each named, with the covered cases.
3. The measured retention re-pin with its cause (if any).
4. The mutation demonstration with the observed failure.
5. Suites: touched modules, full Python, retention, JS sanity — counts,
   elapsed time, baseline differences.
6. `git diff --stat`, the commit SHA, Part A unmoved, Part B empty, Part C
   movement.
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

- `src/kronika/infrastructure/x/downloader.py` and
  `src/kronika/infrastructure/x/staging.py` as they stand.
- `src/kronika/infrastructure/x/status_bridge.py` (the photo path, read-only)
  and the application layer that consumes the acquisition.
- Every test module that exercises the downloader or the staging artifact
  (derive by parse).
- `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`, `.ap/AP.md` §5,
  §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, the parked capture state or
profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the resolution matrix, the consumers,
the tests and the mutation at the reported commit, then arranges publication,
a routine NUC refresh, and the Cooperator's retest of the failed X video claim
through the extension's retry path before the AI acceptance continues.
