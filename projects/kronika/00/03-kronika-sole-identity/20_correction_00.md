# Authoritative Worker prompt — Worker session 20, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `20`, exchange `01`. Stored under the
Meta filename mapping as `20_correction_00.md`, with report destination
`20_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 20
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-CORR-C3B — restore the lost set braces and close C3-B verification
Reasoning recommendation: Medium
Recommended context capacity: approximately 350k tokens
```

Rationale: `Medium`. The syntax defect is a two-line fix. The judgement is in
deciding whether the 507 re-pinned values are correct once the file parses, and in
resisting the temptation to fix anything else that a full-suite run might reveal.

This is a **correction** to cut C3-B, not a new cut. It is bounded to one commit.

## Why this prompt exists

Cut C3-B committed `76416ce08aefb3c8892fc50f52378459f56e8614` with a valid
repository transformation and **one invalid file**. Worker session 19 could not run
a single Python test, because the AP execution envelope validates `provenanceModule`
against `sourceRoot` on every `ap exec`, and the baseline's `ap.project.conf` names
the retired module. That was trap T7 behaving exactly as written, and the Worker
reported the gap rather than substituting weaker evidence.

The Cooperator has since performed the re-gate step 4 maintenance action. The AP
route is open and `ap exec --baseline 76416ce --operation runtime-info` resolves the
renamed provenance module to `src/kronika/__init__.py`. `ap project check --baseline
76416ce` passes.

The first thing the reopened route revealed is this defect:

```text
tests/contract/test_kronika_identity_retention.py:444
EXPECTED_FRAMENEST_CONTENT_PATHS: frozenset[str] = frozenset(
E   TypeError: frozenset expected at most 1 argument, got 507
```

**Scope is exactly one error.** The Orchestrator ran `pytest --collect-only` across
the entire suite: one collection error, this one, every other module collecting
cleanly. A 604-file refactor produced a single syntactic defect.

## Verified current state

```text
Repository checkout topology: standalone checkout
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                76416ce08aefb3c8892fc50f52378459f56e8614
Remote origin:                https://github.com/cisarik/kronika
Public main:                  e1d5ee510b4a1532606dba7d2a098aed71c16225
NOTE: local main is one commit ahead of public main. Work on local main. DO NOT PUSH.
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Node:                         v26.8.2
```

Environment state, established by the Orchestrator after step 4:

```text
ap exec --baseline 76416ce --operation runtime-info
  resolves to /home/agile/Projects/kronika/src/kronika/__init__.py
ap project check --baseline 76416ce            PASS
.venv/bin/kronika-db --help                   exit 0
.venv/bin/framenest-db --help                 exit 0   (retained alias still resolves)
./kronika --help                              prints "Kronika local development launcher"
./framenest --help                            prints "Kronika local development launcher"
```

JavaScript baseline at this commit, executed by the Orchestrator independently of
`ap exec`: **583 total, 578 passed, 0 failed, 5 skipped.**

There is **no Python baseline at this commit**, because the suite cannot collect.
Establishing one is part of your work.

Facts the Orchestrator verified statically and you should re-confirm rather than
assume:

```text
src/ contains exactly kronika and kronika_capture; src/framenest is absent
All 36 frozen Alembic revisions match their ledger SHA-256 pins: 36 match, 0 mismatches
No file under docs/adr/ appears in 76416ce
config.py:7   APP_NAME = "kronika-capture"          (changed, correct)
config.py:8   STATE_DIR_NAME = "framenest-chatgpt-page"  (unchanged, correct)
KronikaSettings totals 504; three surviving FrameNestSettings are ledger provenance
  comments at lines 1046, 1057 and 1066, which must keep the historical spelling
```

## The defect, and the fix

In `tests/contract/test_kronika_identity_retention.py`, the set literal braces around
`EXPECTED_FRAMENEST_CONTENT_PATHS` were lost by the mechanical re-pin pass. The call
is followed directly by its elements, so it receives 507 positional arguments instead
of one iterable.

The neighbouring set shows the intended shape exactly:

```python
EXPECTED_FRAMENEST_BASENAME_PATHS: frozenset[str] = frozenset(
    {
        "deploy/systemd/framenest-ai-credential-nvidia-nim.conf",
        ...
    }
)
```

The broken one currently reads, at these exact line numbers:

```text
444  EXPECTED_FRAMENEST_CONTENT_PATHS: frozenset[str] = frozenset(
445          ".gitignore",
...
951          "tests/youtube_request_cockpit.test.js",
952  )
```

**Insert `    {` immediately after line 444 and `    }` immediately before line 952**,
matching the four-space brace indentation and eight-space element indentation already
used at line 166. Nothing else about those two regions may change. The elements
themselves must not be reordered, deduplicated or altered.

Re-derive the line numbers yourself before editing, and confirm 507 elements, because
line numbers shift. **Report the element count you measured.** If it is not 507, stop
and report rather than editing.

## The real risk: the re-pinned values are unverified

The braces are the visible defect. The larger question is whether the **507 values**
are correct, and that cannot be known until the file parses. Worker session 19
re-pinned the ledger from an independently validated shell measurement because it
could not execute the module, and it disclosed that the assertion "the module passes"
was unproduced.

The values now in the file are these, and they must survive the parse and the run:

```text
PER_TREE_FRAMENEST_FILE_COUNT["src"]                     254 -> 186
PER_TREE_FRAMENEST_FILE_COUNT["tests"]                   322 -> 184
PER_TREE_FRAMENEST_OCCURRENCE_COUNT["src"]             2919 -> 1695
PER_TREE_FRAMENEST_OCCURRENCE_COUNT["tests"]           4580 -> 1851
ENV_PREFIX_TOKEN_COUNT                                    643 -> 641
ENV_PREFIX_DISTINCT_NAME_COUNT                            101 -> 100
ENV_PREFIX_BARE_SPELLING_COUNT                             21 -> 21   unchanged
MUTATION_HEADER_OCCURRENCE_COUNT                           73 -> 73    unchanged
CAPITALIZED_OCCURRENCE_COUNT                             3264 -> 2742
CAPITALIZED_FILE_COUNT                                    474 -> 394
CONSOLE_SCRIPT_ENTRY_COUNT                                  14 -> 14    unchanged
```

`deploy`, `scripts`, `docs` and `extension` per-tree counts must be **unchanged**,
because this cut touches none of them. If the retention module fails on a value after
the braces are restored, **re-pin that value from a measurement you have taken
yourself**, state the measurement method, and report both the old and the new value
with its cause. Do not adjust a value until the test is green; adjust it until it is
**measured**.

**If a value cannot be reproduced by your own measurement, stop and report it.** Do not
tune a pin until the suite passes.

## Remaining C3-B verification this prompt must close

Worker session 19 could not produce these. They are owed, and you have the open route
to produce them.

```text
1. Wheel or sdist listing, showing kronika/ present and framenest/ absent, and all five
   previously-repathed resources present:
     src/kronika/infrastructure/persistence/alembic_environment/script.py.mako
     src/kronika/adapters/api/web/index.html
     src/kronika/adapters/api/web/styles.css
     src/kronika/adapters/api/web/app.js
     src/kronika/infrastructure/ai/fixtures/vision-probe-red-8x8.png
2. Import-level proof: an ordinary `import framenest` FAILS, while the shim makes
   `framenest.infrastructure.persistence.sqlite_batch_fk` importable and bound to the
   kronika module.
3. A fresh temporary database migrates to 0035, and a populated fixture already at 0035
   remains there with its alembic_version row unchanged.
4. The synthetic-alarm demonstration: a synthetic revision importing an unrelated
   `framenest` module FAILS. Do not add that synthetic revision to the repository.
5. Entry-point identity: all thirteen canonical and thirteen alias entry points resolve
   to the same callable; total entry count is 28; `framenest-*` names remain 14.
6. `kronika_capture` imports, and its STATE_DIR_NAME still equals `framenest-chatgpt-page`
   while its APP_NAME is `kronika-capture`.
7. The retention module executes and passes against the corrected file.
8. The full declared Python suite, with exact counts, and the JavaScript suite.
```

For items 2, 5 and 6 you need interpreter access. Use the declared `test-focus`
operation and a throwaway probe file under `/tmp`; do not add probe files to the
repository, and do not invoke `.venv/bin/python` directly.

## The ten discipline rules, binding on this cut

```text
1. Derive site lists by PARSING each artefact, never from a prose enumeration.
2. Resolve every cited line to its literal text BEFORE classifying it.
3. A literal in a test fixture is NOT a pin. Require assertion context.
4. Pin and verify each occurrence independently. Never per file, never per function.
5. Reject any display pin that is a whole-file or whole-function regex where the
   literal occurs more than once.
6. Never truncate an inventory. If output is truncated, disclose it and reprocess.
7. Verify every mechanical probe against a known-impossible number. A formatting
   artifact must not become a finding.
8. Regenerate every verification table at report time. Never transcribe one.
9. Open and classify every grep hit. Distinguish production presence, historical
   compatibility and negative assertions.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

Rule 7 has a direct application here. The Orchestrator found this defect only because
507 positional arguments to `frozenset` is an impossible signature for a set literal of
that size. **If a probe result looks implausible, suspect the probe.**

Rule 6 has one too. Worker session 19's own near-misses included a distinct-token
extraction that produced 363 against a pinned 101, caught because 363 exceeded the 643
total. Verify counts against an independent bound before trusting them.

Rule 8 has failed twice at the same value in this whole. `FROZEN_ALEMBIC_SHA256`
contains **36** keys, being revisions `0001` through `0035` plus `__init__.py`. **Measure
it yourself.**

## Scope boundaries

```text
You may change: tests/contract/test_kronika_identity_retention.py, and any file whose
  defect you demonstrate was caused by cut C3-B.
Nothing else. In particular:
No change to any file under src/kronika/** unless you first demonstrate a concrete
  defect introduced by the move, and you report it before changing it.
No change to any of the 36 Alembic revision files; their bytes must stay identical.
No change to docs/adr/** at all.
No change to default data locations, the dev launcher paths, the AI config path or any
  other host or data default: those are C4-B and C-LOCAL.
No change to any durable writer identifier, header, companion protocol, API version,
  CSS, DOM or port identifier: those are C5 and C7-A.
No deletion of any alias, wrapper or fallback. C3-B keeps them; C7-B removes them.
No change to capture STATE_DIR_NAME.
No new migration. Head stays 0035.
No opportunistic cleanup. A full-suite run will very likely reveal failures that are
  NOT caused by this cut. Report them; do not fix them.
No NUC contact, no provider contact, no browser or capture-browser contact, no
  environment repair, no dependency change, no lockfile change.
```

**The expected failures that are not defects.** Worker session 19 predicted two tests
would fail until step 4 completed. Step 4 is done, so they should now pass. If either
still fails, that **is** a defect and belongs to this correction.

## Authority

```text
Positive authority: restore the two lost set braces; re-pin any ledger value you have
  measured to be wrong, stating the measurement; fix any file whose defect you
  demonstrate was caused by C3-B; create ONE commit on local main; run the declared AP
  test operations; run read-only Git inspection.

Negative authority: a second commit; any change outside the scope boundaries above; any
  value adjustment not backed by your own measurement; any opportunistic fix; any
  invocation of .venv/bin/python, python, python3 or poetry run for evidence; any
  environment repair; any dependency install, update or lockfile change; any NUC
  contact, including SSH, the NUC worker gate, and deploy/ubuntu/framenest-release in
  every mode; any provider or capture-browser contact; any execution of a
  kronika-capture command; any new branch, push, tag, merge, rebase or history rewrite;
  any reading of private/**, personal Fish configuration, browser profiles, cookies,
  tokens, credential stores, .secrets or ~/.config/opencode; any write to
  /home/agile/meta.

Commands: Python evidence goes only through
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
   76416ce08aefb3c8892fc50f52378459f56e8614 --operation test-focus -- <argv>`,
  `./.ap/ap exec ... --operation test`, and
  `./.ap/ap project check --root /home/agile/Projects/kronika --baseline <baseline>`.
  After your commit the baseline becomes your commit SHA, for the same operations.
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

1. Confirm branch `main`, HEAD `76416ce08aefb3c8892fc50f52378459f56e8614`, clean tree,
   submodule at `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `ap doctor` PASS, and
   `ap project check --baseline 76416ce` PASS. **Stop without editing if any fails.**
2. Re-derive the defect: confirm line 444 opens the call, confirm the element count is
   **507**, and confirm line 952 is the bare closing parenthesis. Report the numbers
   before editing.
3. Re-measure `FROZEN_ALEMBIC_SHA256` and report its key count from your own
   measurement.
4. Insert the two braces. Prove with `git diff` that **exactly two lines were added** and
   that no existing line was modified, reordered or removed.
5. Run the retention module. Report its exact outcome. If it fails, diagnose, re-measure,
   re-pin from your own measurement, and report old value, new value and cause. Report
   any value you cannot reproduce.
6. Produce verification items 1 through 6 listed above, each with its actual output.
7. Run the full declared `test` operation once. Report exact counts. The Python suite
   takes about eleven minutes; let it finish. **Do not edit while a suite is running.**
8. Run `node --test tests/*.test.js`. Expect **583 total, 578 passed, 0 failed, 5
   skipped**, unchanged from the Orchestrator's own run at this commit.
9. **Classify every failure** as caused-by-C3-B, pre-existing, or not-a-defect. Report
   each with its cause. Fix only the first category, and only within the scope
   boundaries.
10. Confirm `git diff --stat` touches only reported paths.
11. Commit once. Then run `./.ap/ap project check --root /home/agile/Projects/kronika
    --baseline <your commit SHA>` and `./.ap/ap exec --baseline <your commit SHA>
    --operation runtime-info`, and confirm both resolve `src/kronika/__init__.py`.

```text
Evidence tier: E2. A syntax repair plus value re-verification, with the full suite and
  the seven C3-B verification items produced for the first time.
```

## Git

One commit on local `main`, parent `76416ce08aefb3c8892fc50f52378459f56e8614`.
Suggested subject:

```text
fix(test): restore the content-path set literal lost by the C3-B re-pin
```

Do not push. Publication and the routine NUC refresh are separate bounded grants.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not match; if
  the element count is not 507; if the brace insertion requires modifying any existing
  line; if any ledger value cannot be reproduced by your own measurement; if Part A or
  Part B would move; if the JavaScript count moves; if closing the C3-B verification
  items appears to require a change outside the scope boundaries; if you would need a
  second commit; if any step would need NUC, provider, browser or capture authority; if
  context pressure reaches the point where a bounded rotation is cheaper than a degraded
  commit.

Completion: one commit; the retention module executes and passes; the seven C3-B
  verification items produced with real output; a full Python baseline established;
  JavaScript count unchanged; Part A and Part B unmoved; every failure classified;
  tree clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `20_report_00.md` in /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

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
echoing `kronika-sole-identity`, session `20` and exchange `01` unchanged. Then:

1. The re-derived defect: line numbers, the element count you measured, and `git diff`
   proving exactly two added lines and nothing else changed.
2. Your own `FROZEN_ALEMBIC_SHA256` key count.
3. The retention module outcome. If any value moved, a table of old value, new value,
   the measurement that produced it, and the cause.
4. The seven C3-B verification items, each with its actual output, not a summary.
5. Full Python counts, and the JavaScript counts, with the Python baseline established
   for the first time at this tree.
6. Every failure, individually classified as caused-by-C3-B, pre-existing, or
   not-a-defect, with its cause and whether you fixed it.
7. `git diff --stat` and the commit SHA.
8. `project check --baseline <your SHA>` and `runtime-info` output after your commit.
9. Deviations, risks, missing evidence, and one smallest next step.

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

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/19_report_00.md` in
  full. It is the report for the cut you are correcting, including its near-misses and
  the exact commands the Orchestrator has already run.
- `docs/adr/0085-kronika-sole-identity.md`, the decision text and named frozen residues.
- `tests/contract/test_kronika_identity_retention.py` around lines 160-200 for the
  correct set shape, and 440-460 and 940-960 for the broken one.
- `src/kronika/infrastructure/persistence/alembic_compat.py` in full, and
  `src/kronika/infrastructure/persistence/migrations.py` around lines 20-30 and 110-130.
- `src/kronika/infrastructure/persistence/alembic_environment/env.py`.
- `pyproject.toml` in full, for the script table and the packages declaration.
- `tests/contract/test_chatgpt_page_packaging.py`, `test_web_package_resources.py`,
  `test_persistence_package_resources.py`, `test_ai_package_resources.py`.
- `tests/unit/test_import_boundaries.py`, which owns the renamed prefix constant.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `AGENTS.md` Worker Execution section,
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently re-run the retention module, the
`runtime-info` provenance check and the JavaScript suite, and will confirm that the
commit changed exactly two lines of one file if the values needed no re-pin. If values
did move, the Orchestrator will check each one against its own measurement.

**What this correction does not do.** It does not publish, and it does not deploy. The
NUC still serves `e1d5ee5`, which is two commits behind local `main` once this
correction lands. Publication and the routine refresh are separate grants, and the
Orchestrator will sequence them after acceptance.

**A known, accepted inconsistency remains open and is not in scope here.** The
`FrameNest*Error` domain hierarchy, `FrameNestConfigurationError`,
`FrameNestJsonFormatter`, `FrameNestRedactionFilter` and `FrameNestLogger` were
**not** renamed by C3-B, roughly 1,423 occurrences across about 95 classes. Python
class names are out of scope for the Cooperator-confirmed goal, so this does not block
acceptance, but a module under `src/kronika/` whose exceptions are `FrameNest*Error`
while their messages say `Invalid Kronika …` is incoherent. It is recorded as a
dedicated follow-up after C4-A. **Do not fix it here.**