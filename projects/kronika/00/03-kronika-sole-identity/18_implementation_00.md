# Authoritative Worker prompt — Worker session 18, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `18`, exchange `01`. Stored under the
Meta filename mapping as `18_implementation_00.md`, with report destination
`18_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 18
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C3A — close the Python agreement-coverage gap before the package move
Reasoning recommendation: Medium
Recommended context capacity: approximately 300k tokens
```

Rationale: `Medium`. The production change is one stale test fixture and no
product behaviour at all. The work is in the test design, because the guard has to
fail per occurrence rather than in aggregate, and because aggregate failure is
precisely the defect class this cut exists to close. That design work is judgement.

This is cut **C3-A**, taken from the accepted completion plan at
`17_report_00.md` section 1.3. It must land **before C3-B**, the atomic package
move, and before C7, which removes the compatibility this guard depends on.

## Why this cut exists

Cut C2d retired forty-nine user-visible and operational occurrences of the old
brand in product code. **Nineteen of those forty-nine are not covered by any
behavioural test.** They were renamed and then proved correct only by enumeration
and diff review. Specifically:

```text
 5  argparse description and help strings
10  runtime messages in the development launcher
 4  occurrences of the category-conflict sentence
```

Every one of the nineteen reverts to **green** if changed back. The only automated
signal that anything moved is the retention ledger's whole-tree occurrence
**count**, and that counter fires when *something* moved, never on *what* it moved
to. It cannot distinguish a correct rename from a wrong one, and it trips on one
of four occurrences exactly as readily as on four of four. Session 16 proved this
by reverting each category-conflict occurrence individually and observing
`17 passed` every time.

The completion plan therefore created this cut, and it also created the
corresponding browser-side guard in cut C2c. **The Python side never got its
equivalent.** This cut writes it.

## Verified current state

Every figure below was measured by the Orchestrator at this commit, not carried
forward from an earlier turn.

```text
Repository checkout topology: standalone checkout
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                d5955d5c0478ef7fa025fa9f8cba26ef56656883
Remote origin:                https://github.com/cisarik/kronika
Public main:                  9c71bfb0a06cb30c5d747816e9067f6a25350c58
NOTE: local main is three commits ahead of public main. Work on local main. DO NOT PUSH.
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Node:                         v26.8.2
```

Baselines at this commit, measured by the Orchestrator:

```text
Python declared test:  4359 passed, 8 skipped, 3 warnings, 0 failed
JavaScript:            583 total, 578 passed, 0 failed, 5 skipped
Retention module:      15 passed
ap project check:      PASS at this baseline
```

**This cut touches no JavaScript, so the JavaScript count must not move.** That is
itself part of the evidence.

## The nineteen sites, with their exact current text

Measured by the Orchestrator. Line numbers locate the current evidence; the plan
requires you to resolve them into **AST nodes and branch identities**, because
line numbers are not durable test selectors and this guard will outlive them.

### The five argparse description and help strings

```text
adapters/cli/development.py:35
  description="Control the local Kronika browser-development server."
infrastructure/runtime/production.py:114
  help="Verify the Kronika listener answers a local /health request."
infrastructure/runtime/production.py:118
  help="Run the production Kronika server in the foreground."
infrastructure/persistence/cli.py:85
  subcommands.add_parser("migrate", help="Upgrade the Kronika database to head.")
infrastructure/persistence/cli.py:86
  subcommands.add_parser("status", help="Inspect the Kronika database revision.")
```

### The ten development-launcher runtime messages

```text
infrastructure/runtime/development.py:222  f"Kronika is already running at {self.url}"
infrastructure/runtime/development.py:273  "Kronika did not become healthy in time."
infrastructure/runtime/development.py:314  "Kronika is stopped."
infrastructure/runtime/development.py:316  "Kronika is stopped."
infrastructure/runtime/development.py:338  "Kronika stopped."
infrastructure/runtime/development.py:355  "Kronika is not running."
infrastructure/runtime/development.py:418  "Kronika is stopped."
infrastructure/runtime/development.py:468  f"Kronika is running at {_url(state.port)}"
infrastructure/runtime/development.py:479  "Managed Kronika process is running but health is not ready."
infrastructure/runtime/development.py:619  "Another Kronika runtime operation is in progress."
```

**Note lines 314, 316 and 418. They are the same literal, `"Kronika is stopped."`,
appearing three times.** This is the same duplicate-literal hazard as the
category-conflict sentence and it needs the same structural treatment.

### The four category-conflict occurrences

```text
application/x_acquisition.py:370            "Requested category conflicts with the existing Kronika save."
application/x_acquisition.py:374            "Requested category conflicts with the existing Kronika save."
application/x_acquisition.py:379            "Requested category conflicts with the existing Kronika save."
adapters/api/x_request_api.py:207           "Requested category conflicts with the existing Kronika save."
```

Three in one application method, one in the API layer. Measured occurrence counts
the Orchestrator confirmed: **three** in `x_acquisition.py`, **one** in
`x_request_api.py`. `x_request_api.py:204` catches the exception by class and
substitutes its own literal, which is why the single existing test at
`tests/contract/test_x_request_api.py:282` is a fixture and not a pin, and why all
four are unguarded.

## The identity source, and the one mechanism you must not duplicate

The plan requires the brand to be **derived**, never spelled, and requires that no
second production branding constant be introduced for the tests.

The established precedent is on the browser side. `tests/x_companion_extension.test.js`
derives it:

```javascript
const manifest = JSON.parse(fs.readFileSync(path.join(REPO, "extension/manifest.json"), "utf8"));
const BRAND = manifest.name.split(/\s+/)[0];
```

and independently pins the full display name:

```javascript
assert.equal(manifest.name, "Kronika X Companion", "the display name is the single product identity");
```

`extension/manifest.json` currently carries `"name": "Kronika X Companion"` and
`"version": "0.2.0"`, so the derived word is `Kronika`.

**Mirror that exactly, in Python:**

1. Read `extension/manifest.json`, take `name.split()[0]` as the brand word.
2. Independently assert the full display name equals `"Kronika X Companion"`.
3. Assert the expected message equals the **complete** string built from the
   derived word, not a substring and not a prefix.

Point 2 is what makes this an agreement guard rather than a tautology. A guard that
only derives would still pass if the manifest and the product were renamed
together. The independent full-name pin is what prevents silent dual drift, and it
must be a separate assertion from the derived comparison.

**Orchestrator verification you should know before you duplicate anything:** the
Python tests that reference `manifest.json` all reference
**`.framenest-release-manifest.json`**, the release marker, not the extension
manifest. The only other Python occurrences of `extension/manifest.json` are two
**provenance comments** inside the retention ledger. **No Python code reads the
extension manifest today**, so this derivation genuinely does not exist yet.
`tests/conftest.py` exists and is the natural place for a shared helper;
`tests/contract/conftest.py` does not.

**The derivation belongs in test code.** Do not add a branding constant to
`src/framenest` for the tests to read.

## What the guard must actually prove

The plan's proof requirement is precise, and it is the whole point of the cut:

> each of the nineteen sites must fail its own guard when that occurrence is
> independently changed to the retired brand or an incorrect replacement. Use
> isolated/in-memory mutation demonstrations; a retention-counter failure does not
> count.

Three properties follow, and all three are required.

**Property 1 — per-occurrence failure.** Change one occurrence, and only that
occurrence's own guard fails. Not a counter, not a whole-tree count, not a
neighbouring site's guard. Demonstrate this for all nineteen, or state plainly
which ones cannot be demonstrated and why.

**Property 2 — an occurrence-level structural check.** The plan requires this
explicitly:

> Also maintain an occurrence-level structural check so deleting or overlooking a
> duplicate does not make coverage appear complete.

Concretely, the guard must pin that `"Kronika is stopped."` occurs **exactly three**
times in `development.py`, that the category-conflict sentence occurs **exactly
three** times in `x_acquisition.py` and **exactly one** time in `x_request_api.py`,
and that the nineteen sites resolve to the expected number of distinct AST string
nodes. Otherwise a future cut that deletes one of three duplicates would leave the
suite green while coverage silently shrank. Derive these counts by parsing, and
make the check fail on a count that moves in either direction.

**Property 3 — behavioural, not textual, wherever behaviour is reachable.**
The plan requires exercising real behaviour:

- Exercise **parser output** for the argparse sites: build the actual parsers and
  assert on the produced help and description text, rather than reading source.
- Exercise the **individual runtime branches with controlled dependencies** for the
  development-launcher sites. Several are `RuntimeResult` returns and several are
  raised errors; each needs its own path reached deliberately, with the process
  and port dependencies controlled.
- Exercise **all four** category-conflict paths, including the API response path,
  not just the application branches.

Where a site genuinely cannot be reached behaviourally, say so explicitly and cover
it structurally instead. Do not silently downgrade a behavioural claim to a textual
one.

## The one production-adjacent change: a stale fixture

```text
tests/contract/test_development_cli.py:175
  message="FrameNest is running."
```

This sits inside a fake `RuntimeStatus`. C2d deliberately left it, because fixture
data is not product prose and not an assertion. It is now **unrepresentative** of
the real message, which is `f"Kronika is running at {self.url}"`. Repair it so the
fake mirrors the real runtime result shape, and check what currently asserts on it
so those assertions stay meaningful rather than becoming vacuous.

**Do not classify every test literal as an obsolete fixture or a positive pin.**
Two negative assertions exist in this area and they are **correct and must be
retained**:

```text
tests/integration/test_development_launcher.py:64
  assert b"FrameNest" not in served_root
tests/contract/test_local_web_application.py:1228
  assert "FrameNest is running locally" not in html
```

Both assert the retired spelling is **absent**. The second is now a live tripwire
proving the served root carries no retired brand. Renaming or deleting either would
destroy real coverage. This is rule 9 below, and it is the exact mistake the
Orchestrator made when it read a grep hit as a finding without opening the line.

## The ten discipline rules, binding on this cut

```text
1. Derive site lists by PARSING each artefact, never from a prose enumeration and
   never from an earlier turn's list. The list above is a lead, not a specification.
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
10. State when a requested demonstration cannot exist. Do not fabricate a red test.
```

Rule 7 has a concrete precedent you should know. In session 16 a `sha256sum`
comparison reported **all 36** frozen Alembic revisions as changed, because the
command output differed in a trailing filename field. It was caught only because
36 of 36 is implausible for a cut that provably cannot touch them. If one of your
probes returns a total that should be impossible, treat the probe as suspect before
you treat the finding as real.

## Scope boundaries — what this cut must NOT touch

This is a test-coverage cut. Its blast radius is one fixture and new or extended
tests. **The plan states: no production behaviour or packaging changes.** Anything
below is a different cut with a different owner, and touching it here would destroy
the separation the completion plan depends on.

```text
No product string, message, help text or constant change. The nineteen sites are
  already correct; you are writing the guard, not editing them.
No package movement, no distribution or pyproject change, no ap.project.conf change.
No change to any of the 47 residual occurrences in src/framenest. Their owners are:
    the 7 default path expressions  -> C4-B and C-LOCAL
    script.py.mako                  -> C3-B
    the live mutation header        -> C7-A
    the 33 docstrings and 1 comment -> formally out of scope for this whole
No change to extension/**, src/framenest/adapters/api/web/**, any CSS, DOM hook or
  port name; any Python class or module name; any environment, storage, header or
  protocol key; any of the 36 applied Alembic revisions; deploy/**; scripts/**;
  docs/**; AGENTS.md; any root Markdown file; .gitmodules; .gitignore.
No change to FROZEN_DOCUMENT_SHA256, FROZEN_ALEMBIC_SHA256 or
  EXPECTED_FRAMENEST_BASENAME_PATHS. This cut must not move Part A or Part B.
No database or filesystem write of any kind. No NUC contact of any kind.
```

If you conclude that one of the nineteen sites is actually wrong, or that covering
it properly requires a production change, **stop and report it**. That is a finding
about the plan, not work for this grant.

## Authority

```text
Positive authority: edit exactly the new test coverage and the one stale fixture
  identified above, plus any additional test file your own derivation shows must
  change, each reported explicitly; create one commit on local main; run the declared
  JavaScript route and the declared AP test operations; run read-only Git inspection.

Negative authority: any change to a product string, message, help text or constant
  in src/framenest; any change to the other 47 residuals listed above; any package,
  distribution, pyproject.toml or ap.project.conf change; any change to extension/**,
  src/framenest/adapters/api/web/**, any CSS, DOM or port identifier, any Python class
  or module name, any environment, storage, header or protocol key, any of the 36
  applied Alembic revision files, script.py.mako, any ADR, docs/**, AGENTS.md, any
  root Markdown file, deploy/**, scripts/**, .gitmodules or .gitignore; any change
  to Part A or Part B of the retention ledger; any executable logic change in
  product code; any addition of a production branding constant; any database or
  filesystem write; any NUC contact, including SSH, the NUC worker gate, and
  deploy/ubuntu/framenest-release in every mode; any provider or capture-browser
  contact; any execution of a kronika-capture command; any new branch, push, tag,
  merge, rebase or history rewrite; any dependency install, update or lockfile
  change; any reading of private/**, personal Fish configuration, browser profiles,
  cookies, tokens, credential stores, .secrets or ~/.config/opencode; any write to
  /home/agile/meta.

Commands: JavaScript evidence goes only through `node --test tests/*.test.js` and
  focused `node --test <path>`. Python evidence goes only through
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  d5955d5c0478ef7fa025fa9f8cba26ef56656883 --operation <id> -- <argv>`, plus
  `./.ap/ap project check --root /home/agile/Projects/kronika --baseline
  d5955d5c0478ef7fa025fa9f8cba26ef56656883`. Never invoke `.venv/bin/python`,
  `python`, `python3` or `poetry run` for evidence, including as a text editor.
  Read-only Git inspection is allowed (`git status`, `git rev-parse`, `git log`,
  `git show`, `git diff`, `git ls-files`, `git grep`, `git ls-remote`,
  `git submodule status`, `git merge-base`); no other Git command. Throwaway probe
  files under /tmp only. Any other command must be stated in the report with its
  purpose and a confirmation that it mutated nothing.

Dependency authority: none.

Git authority: one commit on local main. No push, no new branch, no tag, no merge.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.

Side-effect authority: reversible local repository mutation only, plus scratch
  files under /tmp.

Browser authority: none. Do not open Brave, do not load the extension, do not touch
  a real profile.
```

## Verification

1. Confirm branch `main`, HEAD `d5955d5c0478ef7fa025fa9f8cba26ef56656883`, clean
   tree, submodule at `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `ap doctor` PASS,
   `ap project check --baseline` PASS. **Stop without editing if any fails.**
2. Reproduce both baselines before editing. Expect Python `4359 passed, 8 skipped,
   3 warnings` and JavaScript `578 passed, 0 failed, 5 skipped`. The suite takes
   about eleven minutes; let it finish once. **Do not edit while a suite is
   running.**
3. Independently re-derive the nineteen sites by parsing, and **reconcile against
   the list above before you write a single test.** Report your count, my count,
   and every site I missed or mis-located. Explain any difference before editing.
4. Resolve all nineteen to AST nodes and branch identities, and report the
   resolution. Confirm or refute that `"Kronika is stopped."` occurs exactly three
   times in `development.py` and that the category-conflict sentence occurs
   exactly three times in `x_acquisition.py` and once in `x_request_api.py`.
5. Implement the derived identity source and its independent full-name pin.
   Demonstrate that the derived guard **fails** when the manifest display name is
   temporarily altered, and that the independent pin catches it.
6. Implement the guard coverage and the occurrence-level structural check.
7. **Prove per-occurrence failure for all nineteen.** For each site, change that
   one occurrence to the retired brand or to an incorrect replacement, show that
   its own guard fails and that no aggregate counter is what failed, then restore
   and verify the restoration. If any site cannot be demonstrated, say which and
   why, rather than substituting a whole-tree counter failure.
8. **Prove the structural check works.** Delete one of the three
   `"Kronika is stopped."` occurrences, or one of the three category-conflict
   occurrences, in a scratch copy, and show the count check fails. Restore.
9. Repair `tests/contract/test_development_cli.py:175` and demonstrate that whatever
   asserts on that fake still asserts something meaningful.
10. Confirm the two negative assertions at `test_development_launcher.py:64` and
    `test_local_web_application.py:1228` are **unchanged and still present**.
11. Run `node --test tests/*.test.js` and the full declared `test` operation once.
    Report exact counts for both. **The JavaScript count must be identical to the
    baseline. The Python count must increase** by the number of tests you added,
    and no existing test may be deleted or weakened. If the JavaScript count moves,
    stop and explain.
12. Run the retention module. **Part A and Part B must not move.** Report any Part C
    movement with its cause and re-pin only what genuinely moved. Adding test files
    that mention the derived brand in a counted tree may legitimately move Part C
    counts; adding a hardcoded retired spelling would move them wrongly.
13. Confirm `git diff --stat d5955d5..HEAD` touches only reported test paths, and
    confirm **zero** product files appear in it.
14. After the commit run `./.ap/ap project check --root /home/agile/Projects/kronika
    --baseline <new commit SHA>` and confirm PASS.

```text
Evidence tier: E2. Test-coverage addition with one fixture repair, no production
  behaviour change, and per-occurrence failure demonstrated for every guarded site.
```

## Git

One commit on local `main`, parent `d5955d5c0478ef7fa025fa9f8cba26ef56656883`.
Suggested subject:

```text
test(identity): guard every retired product string occurrence
```

Do not push. Publication is a separate bounded grant.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if either baseline does not reproduce; if your derivation and my list of
  the nineteen sites cannot be reconciled before editing; if any site turns out to
  be already covered by a behavioural assertion I did not identify, because that
  would mean the coverage picture is different from the one this grant was written
  against; if covering a site properly appears to require a production change; if
  the JavaScript count moves; if Part A or Part B would move; if proving
  per-occurrence failure would require modifying a product file outside a scratch
  copy; if any step would need a real browser profile or a provider call; if
  context pressure reaches the point where a bounded rotation is cheaper than a
  degraded commit.

Completion: one commit; zero product files in the diff; all nineteen sites guarded
  and each demonstrated failing on its own independent mutation; the occurrence-level
  structural check demonstrated failing on a deleted duplicate; the derived identity
  source with its independent full-name pin demonstrated failing on manifest drift;
  the stale fixture repaired; both negative assertions intact; retention Part A and
  Part B unmoved; JavaScript count identical; Python count increased; tree clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `18_report_00.md` in /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this
  prompt expires. No further implementation, no push, no publication, no NUC contact
  and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `18` and exchange `01` unchanged. Then:

1. Your independent derivation of the nineteen sites, with its count, and the
   reconciliation against the issued list naming every difference.
2. The AST resolution for each of the nineteen, and the measured duplicate counts
   for `"Kronika is stopped."` and the category-conflict sentence.
3. Where the new coverage lives, and why that location rather than an alternative.
4. The derived identity source and the independent full-name pin, with the manifest
   drift demonstration.
5. **A table of all nineteen sites, each with its guard type** — behavioural or
   structural — and its per-occurrence failure result. Sites you could not
   demonstrate must be marked as such, not quietly omitted.
6. The structural check demonstration against a deleted duplicate.
7. The fixture repair and the fate of every assertion that depended on it.
8. Confirmation that the two negative assertions are unchanged and present.
9. Baseline and final exact counts for both routes, with the arithmetic for the
   Python increase.
10. Every ledger movement with its cause, and explicit confirmation that Part A and
    Part B did not move.
11. `git diff --stat` and explicit confirmation that no product file appears in it.
12. The commit SHA; deviations, risks and missing evidence; and one smallest next
    step.

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

- `docs/adr/0085-kronika-sole-identity.md` in full.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/17_report_00.md`,
  sections 1.3 and 3. Section 1.3 is your specification; section 3 carries the
  decisions behind D-1 and D-6.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/16_report_00.md`,
  sections 3, 4, 9, 10 and 16. Sections 9 and 10 are the measured coverage gaps
  you are closing, and section 16 is the recommendation you are implementing.
- `tests/x_companion_extension.test.js` around lines 15-30 and 2630-2645. This is
  the precedent for the derived identity source and the independent full-name pin.
- `src/framenest/infrastructure/runtime/development.py` in full, so you can tell a
  message from a path expression and can reach each branch with controlled
  dependencies.
- `src/framenest/adapters/cli/development.py`, `src/framenest/infrastructure/runtime/production.py`
  and `src/framenest/infrastructure/persistence/cli.py` at their parser definitions.
- `src/framenest/application/x_acquisition.py` around lines 360-385, and
  `src/framenest/adapters/api/x_request_api.py` around lines 195-215.
- `tests/contract/test_development_cli.py` around lines 165-185, plus every place
  that asserts on that fake.
- `tests/contract/test_kronika_identity_retention.py` in full. It is both the
  ledger you must not move and the standing proof of the aggregate-count weakness
  this cut exists to compensate for.
- `tests/conftest.py`.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `AGENTS.md` Worker Execution section,
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance, no product string in this repository will be left without a
behavioural or structural guard, and C3-B can move the package on a base where the
identity is actually enforced rather than merely renamed. The Orchestrator will
independently re-verify that the diff contains no product file, that the two
negative assertions survived, and that the structural check fails on a deleted
duplicate.

What this cut does **not** do, and the Orchestrator will say so plainly rather than
let it pass: it does not resolve the nineteen strings by running the application.
Until C3-B, C4-B, C6 and C8 land, the nettestované reťazce that C2d left behind
are guarded but still not observed in a terminal. After this cut is published and
the NUC is refreshed, the Orchestrator and the Cooperator will read those strings
by hand from the release, which is the mitigation Worker session 16 identified and
the Orchestrator accepted.