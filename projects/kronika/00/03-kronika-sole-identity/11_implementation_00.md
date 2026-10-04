# Authoritative Worker prompt — Worker session 11, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `11`, exchange `01`. Stored under the
Meta filename mapping as `11_implementation_00.md`, with report destination
`11_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 11
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C1E — pin the retention ledger's content-path membership so a partial rename cannot pass
Reasoning recommendation: Low
Recommended context capacity: approximately 250k tokens
```

Rationale: this is one new pinned literal set and one new test in one existing
test module, following a design the module already uses for its Part B path
ledger. The work is mechanical; the only judgement is what belongs in the pinned
set, and the rules for that are given exactly below. That is the `Low` band.

This is ledger cut **C1e**. It changes no product behaviour at all. It exists
because cut C3's grant will write a full ledger re-pin against whatever this
settles, so this must be decided first.

## Why this correction exists

The independent audit at session `07` and the re-audit at session `09` both
established a real weakness in the retention ledger that the Orchestrator designed
at C0:

- Part A pins SHA-256 literals and a completeness cross-check. It is genuinely
  independent and strong.
- Part B pins an enumerated **20-path set**, the basenames carrying `framenest`.
  It is membership, so it is strong for what it covers.
- **Part C pins scalars.** A scalar detects *that* a total moved but not *which*
  occurrences moved. A cut that renames some things and re-pins the scalar to match
  the partial work **passes**.

The re-audit's direct answer: a genuinely missed rename would **not** reliably
fail at the cut that owns it; it survives until a later re-pin fails to reconcile,
which is C7 at the earliest. That contradicts the promise recorded in ADR-0085
lines 114-115 that a premature or missed rename "fails loudly at the cut that owns
it rather than at the end".

The Worker at session `09` also identified why a count map is the wrong fix: a
count map still lets file X fall 12→10 while file Y rises 3→5. And it noted the
module already documents the correct measure — "a content-only rename inside an
already matching file leaves the file counts unchanged, so these are the measures
that actually detect a missed content rename" — while pinning the weaker form.

## Goal

Add one pinned **membership** set to the retention ledger so that a partial rename
fails at the cut that performs it, and so that a file which should have stopped
carrying the token but did not is caught, and so that a file which should still
carry it but no longer does is also caught.

## Verified current state

```text
Repository checkout topology: standalone checkout
Expected branch: feat/kronika-identity-dual-read
Expected HEAD: 02a80485206eeeb33c43393d25514a30d7fe297f
Expected subject: docs(identity): state the resolver's measured precedence and per-channel conflict rule
Lineage: 18c357c published main -> 90c93ea C1 -> c02c675 C1b -> 24bea56 C1c -> 02a8048 C1d
Remote origin: https://github.com/cisarik/kronika
Public main: 18c357cf6f8c5ff9cc3b2c28e638510fc73a3672
The branch is deliberately unpublished. Do not push.
Working tree: clean
Containing-repository .ap gitlink and submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor: PASS, governing variant stable
Working directory: /home/agile/Projects/kronika
```

Baseline at this commit, measured by the Orchestrator through the canonical
route: Python `4355 passed, 8 skipped, 3 warnings, 0 failed`; JavaScript
`554 total, 549 passed, 0 failed, 5 skipped`. The retention module itself is
`14 passed`.

## Required mutation

Touch exactly one file: `tests/contract/test_kronika_identity_retention.py`.

### 1. The pinned membership set

Add `EXPECTED_FRAMENEST_CONTENT_PATHS: frozenset[str]` — the exact set of tracked
text paths, **excluding the ledger file itself**, whose decoded content contains
`framenest` case-insensitively.

Construction rules, so the set is unambiguous:

- Base it on the module's existing tracked-path helper, so the ledger's own
  treatment of submodules, binary files and the excluded self-path is inherited
  rather than reinvented. The re-audit verified `git ls-files` reports the `.ap`
  submodule as a directory, which broke counting earlier; the existing helper
  already filters to regular files.
- Skip binary files exactly as the module's existing `git grep -I`-shaped counting
  does.
- Exclude the ledger file itself, as the existing helpers already do.
- Key the set by repository-relative POSIX path, sorted, matching the style of the
  existing Part B set.
- Store it as a literal in the test module. It must **never** be recomputed from
  the working tree at test time, or the assertion would be tautological. State that
  reasoning in a comment, the way the Part B ledger already does.

### 2. One test

Assert set equality between the measured set and the pinned literal, with a
failure message that names both sides, as the existing Part B test does.

### 3. Demonstrate that it is not tautological and that it works

A membership assertion is exactly the kind of thing that can pass for the wrong
reason. So:

- Measure the pinned set at this baseline and report its size and its shape. The
  Orchestrator's expectation is that it is substantially **larger** than Part B's
  20 paths, because it includes files whose names are clean but whose content
  carries the token — `deploy/ubuntu/fn-production-env-deploy` is the known case.
- Show the test **failing** when the pinned set is perturbed in memory, for **both**
  directions: adding a path that should not be present, and removing a path that
  should be. A membership test that only fails on additions is half a test.
- Show, concretely, that the new assertion would have caught the partial-rename
  failure mode Part C's scalars miss. Construct the scenario in memory: remove one
  path from the measured set and re-pin a Part C scalar to compensate, then
  demonstrate that the scalars pass while the membership test fails. This is the
  deliverable that justifies the change.

### 4. Ledger discipline

Your change adds text to the ledger file itself, which the ledger excludes from
its own counting, so **no pin should move**. Confirm that and report it. If any pin
does move, stop and report rather than re-pinning.

Do not modify Part A, Part B, or any existing Part C value. Do not "improve" the
existing helpers. Do not rename anything.

## Authority

```text
Positive authority: edit exactly tests/contract/test_kronika_identity_retention.py;
  add the pinned membership set, its equality test, and any comment needed to
  explain why the set is a literal; create one additional local commit on the
  existing branch feat/kronika-identity-dual-read; run the declared AP test
  operations; run read-only Git inspection.

Negative authority: any change to any other file, including every product source
  file, every other test module, docs/**, AGENTS.md, root Markdown files,
  deploy/**, src/kronika_capture/**, pyproject.toml, ap.project.conf,
  .gitmodules and .gitignore; any change to an existing Part A hash, a Part B
  path, or an existing Part C value; any product behaviour change; any new
  branch, push, tag, merge, rebase or history rewrite; any dependency install,
  update or lockfile change; any NUC contact, including SSH, the NUC worker gate,
  and deploy/ubuntu/framenest-release in every mode; any provider or
  capture-browser contact; any execution of a kronika-capture command; any reading
  of private/, personal Fish configuration, browser profiles, cookies, tokens,
  credential stores, .secrets or ~/.config/opencode; any write to
  /home/agile/meta.

Commands: Python evidence goes only through the canonical declared route,
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  02a80485206eeeb33c43393d25514a30d7fe297f --operation <id> -- <argv>`, with
  operations declared in ap.project.conf, plus `./.ap/ap project check --root
  /home/agile/Projects/kronika --baseline
  02a80485206eeeb33c43393d25514a30d7fe297f`. Never invoke `.venv/bin/python`,
  `python`, `python3` or `poetry run` for evidence, including as a text editor.
  Read-only Git inspection is allowed (`git status`, `git rev-parse`, `git log`,
  `git show`, `git diff`, `git ls-files`, `git grep`, `git ls-remote`,
  `git submodule status`, `git merge-base`); no other Git command. Throwaway probe
  files and in-memory monkeypatches under /tmp only. Any other command must be
  stated in the report with its purpose and a confirmation that it mutated
  nothing.

Dependency authority: none.

Git authority: one additional local commit on the existing branch. No push, no new
  branch.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none. Use only synthetic values. The pinned set contains paths
  only, never content and never a value.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope; the
  accepted plan and prior reports are task context, not authority. On conflict
  between retained context and current repository evidence, stop.

Side-effect authority: reversible local test-module mutation only, plus scratch
  files under /tmp.

Browser authority: none.
```

## Verification

1. Confirm branch `feat/kronika-identity-dual-read`, HEAD `02a8048…`, clean tree,
   submodule at the pin, `ap doctor` PASS, `ap project check --baseline` PASS.
   Stop without editing if any fails.
2. Read `tests/contract/test_kronika_identity_retention.py` **in full** first, so
   you inherit its helpers and style instead of adding a parallel mechanism.
3. Reproduce the baseline once with the declared `test` operation. Expect
   `4355 passed, 8 skipped, 3 warnings`. The suite takes about eleven minutes; let
   it finish once. **Do not edit while a suite is running.**
4. Measure the set at this baseline before writing it, and report its size and
   shape.
5. Make the change.
6. Demonstrate the test failing in both directions, and demonstrate the
   compensating-scalar scenario from item 3.
7. Run the retention module. Then run the full declared `test` operation once and
   report exact counts; skips remain 8 and warnings 3.
8. Run `node --test tests/*.test.js` and report the result, which is expected
   unchanged.
9. Confirm `git diff --stat 02a8048..HEAD` lists exactly one file.
10. After the commit run `./.ap/ap project check --root /home/agile/Projects/kronika
    --baseline <new commit SHA>` and confirm PASS.

```text
Evidence tier: E1. One test module, one new pinned literal and one new assertion,
  no product behaviour, trivially reversible.
```

## Git

One additional commit on `feat/kronika-identity-dual-read`, parent
`02a80485206eeeb33c43393d25514a30d7fe297f`. Suggested subject:

```text
test(retention): pin the content-path membership set so a partial rename fails
```

Do not push. Do not create a new branch.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the baseline does not reproduce; if any existing Part A hash, Part B
  path or Part C value would have to change; if any pin moves when your change is
  applied; if you cannot demonstrate the test failing in both directions; if you
  cannot construct the compensating-scalar demonstration; if any file other than
  the retention module would need editing; if context pressure reaches the point
  where a bounded rotation is cheaper than a degraded commit.

Completion: one additional commit touching exactly one file, the membership set
  pinned as a literal, the equality test passing and demonstrated failing in both
  directions, the compensating-scalar scenario demonstrated, no existing pin
  moved, both routes green, tree clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `11_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this
  prompt expires. No further implementation, no push, no publication, no NUC
  contact, no cut C2 and no cut C3 is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `11` and exchange `01` unchanged. Then:
the exact diff; the measured set's size and shape, with how many paths it has that
Part B does not, and the known clean-name case in it; both failure
demonstrations; the compensating-scalar demonstration with what the scalars did and
what the membership test did; confirmation that no existing pin moved; baseline
and final exact counts; the branch name and all five commit SHAs on this branch;
deviations, risks and missing evidence; and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification.

Finish every terminal report with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

If your client's native surface forces any preamble above the report header,
disclose it on the first line of the report body.

## Mandatory reading

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/09_report_00.md`,
  priority 6, which is your specification.
- `tests/contract/test_kronika_identity_retention.py` **in full**. This is the
  primary input.
- `docs/adr/0085-kronika-sole-identity.md` lines 109-117, the promise this change
  is meant to make true.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/03_report_00.md`,
  the accepted plan, C3, which will write the full re-pin against whatever you
  settle.
- `tests/contract/test_fedora_systemd_service.py` and
  `tests/contract/test_ap_integration.py`, for the module conventions this
  repository already uses for pinned repository evidence.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real database, media path, profile or backup archive.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the ledger is settled and cut C2's grant can be written. C3's grant
will then re-pin the whole ledger against this membership set, which is the
strongest available detector for the package move. A3's `_env_*` parity cases and
the `lookup_field_value`/`lookup_env` collapse check belong in C3's grant, not here.