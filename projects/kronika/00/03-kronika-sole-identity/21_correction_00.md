# Authoritative Worker prompt — Worker session 21, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `21`, exchange `01`. Stored under the
Meta filename mapping as `21_correction_00.md`, with report destination
`21_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 21
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-CORR-C3B-2 — repoint the test-side references C3-B left behind
Reasoning recommendation: Medium
Recommended context capacity: approximately 300k tokens
```

Rationale: `Medium`. The changes are mechanical substitutions against verified
production names, but the derivation must be exhaustive rather than list-driven, and
one assertion needs narrowing rather than changing. Both require judgement.

This is a **correction** to cut C3-B, bounded to one commit. It is not a new cut.

## Why this prompt exists

Cut C3-B moved `src/framenest` to `src/kronika` and renamed the logging namespace,
but **no Python test could run during that cut**: the AP execution envelope validates
`provenanceModule` against `sourceRoot` on every `ap exec`, so the moment the old
package stopped existing the route closed. C3-B was therefore committed on static and
JavaScript evidence alone.

The route is now open. The Orchestrator ran the full declared suite at
`0eb6e8e562e6c22c3de4038105b84689e9b1c76b` and measured:

```text
37 failed, 4362 passed, 8 skipped, 2 warnings in 673.15s
```

**All 37 failures are test-side. No production defect was found.** The renaming cut
missed a class of test-side references that move with the rename. This prompt closes
that class.

## Verified production names — the authority for every substitution

Measured by the Orchestrator at this commit. **Substitute towards these, never
towards a guess.**

```text
root logger name                      "kronika"
                                      src/kronika/structured_logging.py:138
component logger name                 f"kronika.{component}"
                                      src/kronika/structured_logging.py:152
log handler key                      "kronika_stderr"
log formatter key                    "kronika_json"
application package directory        src/kronika
```

**These names are unchanged and must NOT be touched.** They are the deliberately
deferred class-name residue, roughly 1,423 occurrences across about 95 classes:

```text
FrameNestLogger
FrameNestJsonFormatter
FrameNestRedactionFilter
FrameNestConfigurationError
FrameNestMediaAnalysisError, FrameNestMediaCoverError, FrameNestMediaMetadataError,
FrameNestMediaUserAliasError, FrameNestUploadSessionError, and the rest of the
FrameNest*Error hierarchy
```

A test that references `FrameNestJsonFormatter` or `FrameNestRedactionFilter` is
**correct as written** and must not be repointed. Only the *logger names, handler and
formatter keys, and file paths* move.

## How you must find the sites — this is the whole point of the prompt

**Do not work from the site list below.** It is a confirmed sample, not the
specification. It exists so you can check your own derivation, and the Orchestrator is
issuing it precisely because **two previous prompts in this whole failed by issuing
per-file targets for a change that needed a derivation rule.**

Sessions 14, 15, 16 and 19 each found omissions of exactly this shape: a site the
hand-built list did not name. Derive instead:

```text
A. Parse every module under tests/ and collect, by parsing rather than by reading:
     - every logging.getLogger(...) argument and every string compared against
       record.name or a logger name
     - every subscript into a log config: ["formatters"], ["handlers"], ["loggers"]
     - every string literal or Path(...) naming a path under src/
   Then classify each as one of:
     moved-name    logger name, handler key, formatter key, or a src/ path  -> repoint
     frozen-name   a FrameNest* class name                                   -> leave alone
     unrelated     anything else                                             -> leave alone
B. Report the total per category. If your "moved-name" count differs from the number
   of failing tests, explain why before editing.
C. Fix every moved-name site you found, including any that no currently failing test
   exercises. A site in a skipped test, or on a branch the suite does not take, is
   exactly how this defect class survives a cut.
```

## The confirmed failure inventory

Grouped by cause, as measured. **The sites are samples; the cause classes are the
specification.**

```text
25  logging.getLogger("framenest") returns a logger with no handlers, because the
    root logger was renamed. IndexError: list index out of range.
      tests/unit/test_structured_logging.py:40
      tests/unit/test_configuration.py:297
      (the remaining failures in these two files are the same root cause reached
       through other helpers)

 4  KeyError: 'framenest_json' — the formatter key was renamed.
      tests/unit/test_server_runtime.py:185
      tests/contract/test_uvicorn_logging.py:77, :150

 1  KeyError: 'framenest_stderr' — the handler key was renamed.
      tests/contract/test_uvicorn_logging.py:89

 2  assert 0 == 1 — the test compares caplog record.name against
    "framenest.public_published_api" and "framenest.public_published_application";
    production now emits "kronika.<component>".
      tests/contract/test_public_published_uds.py

 8  hardcoded src/framenest paths. Known instances:
      tests/unit/test_server_runtime.py:25          SOURCE_ROOT = Path("src/framenest")
      tests/contract/test_workspace_media.py        a src/framenest/... module path,
                                                    FileNotFoundError
      tests/contract/test_kronika_product_string_agreement.py
                                                    one source-root constant; it
                                                    produces five failures because it
                                                    also looks for the frozen applied
                                                    revisions under the old directory

 1  an over-broad assertion, handled separately below.
      tests/contract/test_kronika_settings_parity.py
```

## The one assertion to narrow, not to change

`tests/contract/test_kronika_settings_parity.py`, in
`test_the_settings_library_is_unchanged_since_the_restoration_reference`:

```python
RESTORATION_REFERENCE = "18c357cf6f8c5ff9cc3b2c28e638510fc73a3672"

assert pydantic_settings.VERSION == locked.group(1)
assert _git_blob(RESTORATION_REFERENCE, "poetry.lock") == _git_blob("HEAD", "poetry.lock")
assert _git_blob(RESTORATION_REFERENCE, "pyproject.toml") == _git_blob("HEAD", "pyproject.toml")
```

**The Orchestrator has verified that the test's stated purpose is still satisfied.**
`poetry.lock` is byte-identical to the reference and `pydantic-settings` is still
`2.14.2`; C3-B changed only the distribution name, the packages declaration and the
script entry points, and touched no library version or dependency specifier. The first
two assertions pass. Only the third fails.

The docstring reads *"The oracle is licensed only while the library matches the older
commit."* Here **"oracle" means a reference implementation used as a measuring
standard**, and **"licensed" means permitted** — this is a parity oracle for the
dual-prefix cut, not a legal licence condition. The Orchestrator briefly misread it as
one and withdrew that reading before issuing this prompt.

**So this is an over-broad assertion, not a licence condition.** The assertion pins the
whole manifest, while the test's name and docstring claim only that the **library** is
unchanged.

**What to do:** narrow the third assertion so it asserts what the test claims — that
the **settings library** has not changed — rather than that the entire
`pyproject.toml` is byte-identical. Preserve the `poetry.lock` byte-identity assertion
exactly as it is; it is the real evidence and it still passes.

**Two things you must not do:**

- **Do not move `RESTORATION_REFERENCE` forward.** That would silently discard the
  baseline the dual-prefix parity evidence rests on.
- **Do not delete or skip the assertion.** Replacing it with nothing would leave the
  library pin unproven.

If you judge that a narrower correct assertion cannot be written without weakening the
library pin, **stop and report that judgement instead of choosing.**

## The ten discipline rules, binding on this cut

```text
1. Derive site lists by PARSING each artefact, never from a prose enumeration.
2. Resolve every cited line to its literal text BEFORE classifying it.
3. A literal in a test fixture is NOT a pin. Require assertion context.
4. Pin and verify each occurrence independently. Never per file, never per function.
5. Reject any display pin that is a whole-file or whole-function regex where the
   literal occurs more than once.
6. Never truncate an inventory. If output is truncated, disclose it and reprocess.
7. Verify every mechanical probe against a known-impossible number.
8. Regenerate every verification table at report time. Never transcribe one.
9. Open and classify every grep hit. Distinguish production presence, historical
   compatibility and negative assertions.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

Rule 3 has a live application here. Some of what you will find are **negative
assertions** that the retired spelling is absent, and some are **provenance comments**
in `tests/contract/test_kronika_identity_retention.py` that narrate what earlier cuts
did and must keep the historical spelling. **Neither is a moved-name site.** In
particular the ledger comments at lines 1046, 1057, 1066 and 378 keep
`FrameNestSettings` and `logging.getLogger("framenest")` because they describe history.

Rule 7 has a live application. `FROZEN_ALEMBIC_SHA256` contains **36** keys, revisions
`0001` through `0035` plus `__init__.py`. Measure it yourself. Two Workers in this whole
reported 38 by transcribing a remembered figure.

## Scope boundaries

```text
You may change: files under tests/ that your derivation shows contain a moved-name
  site, and the one assertion to narrow.

Nothing else. In particular:
No change to any file under src/kronika/**. Production names are already correct; a
  change there is a new defect.
No change to any of the 36 Alembic revision files.
No change to docs/adr/** at all.
No change to the FrameNest* class names, anywhere, including in tests.
No change to RESTORATION_REFERENCE.
No change to the poetry.lock byte-identity assertion.
No change to any default data location, dev launcher path, AI config path, host default,
  durable writer identifier, header, companion protocol, API version, CSS, DOM or port
  identifier: those are C4-B, C5 and C7-A.
No change to the retention ledger's Part A or Part B. Part C may move only if your own
  measurement shows a count genuinely changed, and you must report old value, new value,
  the measurement and the cause.
No opportunistic cleanup. Report anything else you notice; do not fix it.
No NUC contact, no provider contact, no browser or capture-browser contact, no
  environment repair, no dependency change, no lockfile change.
```

## Authority

```text
Positive authority: edit files under tests/ to repoint every moved-name site your
  derivation finds, each reported explicitly; narrow the one over-broad assertion;
  create ONE commit on local main; run the declared AP test operations; run read-only
  Git inspection.

Negative authority: a second commit; any change outside the scope boundaries above; any
  change to a FrameNest* class name; any change to RESTORATION_REFERENCE; any deletion
  or skip of an assertion; any invocation of .venv/bin/python, python, python3 or
  poetry run for evidence; any environment repair; any dependency install, update or
  lockfile change; any NUC contact, including SSH, the NUC worker gate, and
  deploy/ubuntu/framenest-release in every mode; any provider or capture-browser
  contact; any execution of a kronika-capture command; any new branch, push, tag,
  merge, rebase or history rewrite; any reading of private/**, personal Fish
  configuration, browser profiles, cookies, tokens, credential stores, .secrets or
  ~/.config/opencode; any write to /home/agile/meta.

Commands: Python evidence goes only through
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
   0eb6e8e562e6c22c3de4038105b84689e9b1c76b --operation test-focus -- <argv>`,
  `./.ap/ap exec ... --operation test`, and
  `./.ap/ap project check --root /home/agile/Projects/kronika --baseline <baseline>`.
  **The baseline must be a full 40-character lowercase commit object ID.** After your
  commit the baseline becomes your commit SHA for the same operations.
  JavaScript evidence goes only through `node --test tests/*.test.js` and focused
  `node --test <path>`. Read-only Git inspection is allowed (`git status`, `git rev-parse`,
  `git log`, `git show`, `git diff`, `git ls-files`, `git grep`, `git ls-remote`,
  `git submodule status`, `git merge-base`); no other Git command. Throwaway probe files
  under /tmp only. Any other command must be stated in the report with its purpose and a
  confirmation that it mutated nothing.

Dependency authority: none. No lockfile change.

Git authority: exactly one commit on local main, without amend. No push.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope. On conflict
  between retained context and current repository evidence, stop.

Side-effect authority: reversible local repository mutation only, plus scratch files
  under /tmp.

Browser authority: none.
```

## Verification

1. Confirm branch `main`, HEAD `0eb6e8e562e6c22c3de4038105b84689e9b1c76b`, clean tree,
   submodule at `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `ap doctor` PASS, and
   `ap project check --baseline 0eb6e8e...` PASS. **Stop without editing if any fails.**
2. Reproduce the failure baseline once before editing. Expect exactly
   **37 failed, 4362 passed, 8 skipped, 2 warnings**. The suite takes about eleven
   minutes; let it finish. **Do not edit while a suite is running.**
3. Perform the derivation in "How you must find the sites" above. Report the moved-name,
   frozen-name and unrelated totals, and reconcile them against the confirmed inventory
   before editing. **Report every moved-name site you found that no failing test
   exercises.**
4. Make the changes.
5. Confirm by parsing that **no moved-name site remains anywhere under `tests/`**, and
   report the final per-category totals.
6. Run the affected files first, then the full declared `test` operation once. Expect
   **zero failures**. Report exact counts. The suite takes about eleven minutes.
7. Run `node --test tests/*.test.js`. Expect **583 total, 578 passed, 0 failed, 5
   skipped**, identical to the Orchestrator's run. This cut should not touch JavaScript.
8. Run the retention module. **Part A and Part B must not move.** Report any Part C
   movement with its own measurement and cause.
9. Confirm the `poetry.lock` byte-identity assertion in
   `test_kronika_settings_parity.py` is **unchanged and still present**, that
   `RESTORATION_REFERENCE` is **unchanged**, and that the first two assertions of that
   test are untouched.
10. Confirm **zero files under `src/`** appear in `git diff --stat`.
11. Commit once. Then run `./.ap/ap project check --root /home/agile/Projects/kronika
    --baseline <your commit SHA>` and `./.ap/ap exec --baseline <your commit SHA>
    --operation runtime-info`, and confirm both resolve `src/kronika/__init__.py`.

```text
Evidence tier: E2. Test-side repointing against verified production names, plus one
  assertion narrowed to its stated claim, with the full suite green.
```

## Git

One commit on local `main`, parent `0eb6e8e562e6c22c3de4038105b84689e9b1c76b`.
Suggested subject:

```text
fix(test): repoint the test-side references left behind by the package move
```

Do not push. Publication and the routine NUC refresh are separate bounded grants.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not match; if
  the failure baseline does not reproduce at 37; if your derivation and the confirmed
  inventory cannot be reconciled before editing; if narrowing the settings-parity
  assertion would weaken the library pin or move RESTORATION_REFERENCE; if any change
  would have to touch src/kronika/**, a FrameNest* class name, an Alembic revision, a
  frozen ADR, Part A or Part B; if the JavaScript count moves; if any failure remains
  that you cannot attribute; if you would need a second commit; if any step would need
  NUC, provider, browser or capture authority; if context pressure reaches the point
  where a bounded rotation is cheaper than a degraded commit.

Completion: one commit; zero failures in the full suite; zero moved-name sites remaining
  under tests/; the settings-parity assertion narrowed with the lock assertion and
  RESTORATION_REFERENCE untouched; Part A and Part B unmoved; JavaScript count unchanged;
  zero src/ files in the diff; tree clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `21_report_00.md` in /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this prompt
  expires. No further implementation, no second commit, no push, no publication, no NUC
  contact, no environment repair and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `21` and exchange `01` unchanged. Then:

1. Your derivation: the moved-name, frozen-name and unrelated totals, the method used,
   and the reconciliation against the confirmed inventory.
2. Every moved-name site you found, with its path, line and old value, **including any
   that no failing test exercises**.
3. The narrowed settings-parity assertion: the before and after text, and why the
   narrower form still proves the library is unchanged.
4. Explicit confirmation that `RESTORATION_REFERENCE`, the `poetry.lock` byte-identity
   assertion and the first two assertions of that test are untouched.
5. The exact `FrameNest*` class-name sites you deliberately left alone, as evidence that
   rule 3 and the deferral were respected.
6. Full Python counts before and after, and the JavaScript counts.
7. Ledger movements with your own measurement and cause; explicit confirmation that Part A
   and Part B did not move.
8. `git diff --stat`, with explicit confirmation that zero `src/` files appear, and the
   commit SHA.
9. `project check --baseline <your SHA>` and `runtime-info` output after your commit.
10. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification.

Finish every terminal report with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

If your client's native surface forces any preamble above the report header, disclose
it on the first line of the report body.

## Mandatory reading

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/20_report_00.md` in
  full, for what the first correction established.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/19_report_00.md`,
  sections 1, 12 and 13, for what C3-B changed and what it could not test.
- `src/kronika/structured_logging.py` in full. It is the authority for every
  substitution you make.
- `src/kronika/infrastructure/persistence/migrations.py` around lines 20-30 and 110-130.
- `tests/contract/test_kronika_settings_parity.py` in full.
- `tests/contract/test_kronika_product_string_agreement.py` in full.
- `tests/contract/test_kronika_identity_retention.py`, the path-name and content-path
  helpers and the provenance comments around lines 370-385 and 1040-1070.
- `tests/contract/test_uvicorn_logging.py`, `tests/unit/test_structured_logging.py`,
  `tests/unit/test_configuration.py`, `tests/unit/test_server_runtime.py`,
  `tests/contract/test_public_published_uds.py`, `tests/contract/test_workspace_media.py`.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `AGENTS.md` Worker Execution section,
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently re-run the full declared suite and
will expect **zero failures**, will confirm that zero `src/` files appear in the commit,
that `RESTORATION_REFERENCE` and the `poetry.lock` assertion are untouched, and that no
`FrameNest*` class name was renamed.

**Publication and deployment are separate grants.** The NUC still serves `e1d5ee5`,
which will be three commits behind local `main` once this correction lands. Note for the
sequencing: that release predates the package move, so it still runs `framenest-*`
entry points, which the current tree keeps as aliases. The Orchestrator will sequence
publication and the routine refresh after acceptance.