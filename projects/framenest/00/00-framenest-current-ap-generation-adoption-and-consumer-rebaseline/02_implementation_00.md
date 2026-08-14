Logical whole identity: framenest-current-ap-generation-adoption-and-consumer-rebaseline
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: Implementation

Implementation authority: explicit
Exact baseline: d4c3402a4765b39cee0d8e2063d5ec8be161caf6
Changed-path allowlist: .ap; tests/contract/test_ap_integration.py; README.md
Implementation boundaries: converge the FrameNest AP consumer pin from 4862380f351ddd74e1c141a4babe2d0f0b43979d to exactly 041de310ea33ed1b47dd8f5fbfcc2829d1a32514 and update only the two approved current-generation SHA assertions; no other repository, AP, Meta, product, dependency, deployment, production, provider, network, or host mutation
Independence required: no

External trace disposition: not-used

Reasoning recommendation: Medium
Reasoning basis: planning has already resolved compatibility and produced an exact three-path implementation allowlist. The implementation is mechanically bounded but touches the AP consumer trust boundary, so retain careful repository and validation discipline without reopening architectural analysis.

## Persistent roles

You are one fresh WORKER operating under Analytic Programming.

COOPERATOR:
Michal

ORCHESTRATOR owns task routing, candidate reconciliation, independent acceptance routing, publication authorization, and logical-whole closure.

Do not choose or change model, provider, reasoning configuration, or client route.

Do not delegate to sub-agents.

Your standard terminal report must begin exactly:

### Report for ORCHESTRATOR_CHAT

## Accepted planning decision

Worker 1 completed the only authorized implementation-planning cycle with PASS.

The ORCHESTRATOR accepts that plan without revision.

Planning established:

FrameNest public implementation baseline:
d4c3402a4765b39cee0d8e2063d5ec8be161caf6

Current FrameNest AP pin:
4862380f351ddd74e1c141a4babe2d0f0b43979d

Accepted target AP generation:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

Target AP subject:
docs: converge ADR-0014 lifecycle status

The target is expected to be a normal forward descendant of the current FrameNest pin.

The executable `ap` blob was proven identical between the old and target generations.

`ap.project.conf`, the managed `AGENTS.md` AP block, `tests/contract/test_ap_project_contract.py`, and `docs/WORKER_EXECUTION_CONTRACT.md` were proven compatible unchanged.

Do not reopen those planning decisions unless fresh repository evidence directly contradicts them.

## Objective

Create exactly one reviewable FrameNest implementation candidate that:

1. moves the `.ap` gitlink to
   `041de310ea33ed1b47dd8f5fbfcc2829d1a32514`;

2. changes only `EXPECTED_AP_COMMIT` in
   `tests/contract/test_ap_integration.py`
   from
   `4862380f351ddd74e1c141a4babe2d0f0b43979d`
   to
   `041de310ea33ed1b47dd8f5fbfcc2829d1a32514`;

3. changes only the README statement describing the current AP gitlink from
   `5c2f0e197d6aecdc6aca918b22e080bb58abc7a1`
   to
   `041de310ea33ed1b47dd8f5fbfcc2829d1a32514`;

4. validates that exact candidate;

5. creates exactly one local candidate commit;

6. does not push, publish, deploy, or mutate production.

## Authority envelope

Repository mutation authority:
explicit, limited to the three allowlisted FrameNest paths.

Allowed changed paths:

.ap
tests/contract/test_ap_integration.py
README.md

No fourth path is authorized.

Git authority:

- read repository state;
- run direct public `git ls-remote`;
- create one clean detached isolated worktree from the exact authorized baseline;
- initialize the `.ap` submodule in that isolated worktree;
- fetch AP objects as required by the authorized AP update;
- run the authorized AP update;
- stage exactly the three allowlisted paths;
- create exactly one ordinary non-amend candidate commit.

Git authority does NOT include:

- push;
- force push;
- publication;
- merge;
- rebase;
- cherry-pick;
- tag creation;
- branch deletion;
- canonical-worktree cleanup;
- rewriting existing commits;
- deleting unexplained worktrees or files.

Publication authority:
none

Deployment authority:
none

Production authority:
none

Provider authority:
none

Meta mutation authority:
none

AP repository mutation authority:
none

Dependency authority:
none

Secret authority:
none

Privilege authority:
none

NUC authority:
none

Network/configuration authority:
none, except ordinary public Git read/fetch operations required by this exact repository task.

Do not modify:

AGENTS.md
ap.project.conf
tests/contract/test_ap_project_contract.py
docs/WORKER_EXECUTION_CONTRACT.md
.gitmodules
docs/adr/0034-canonical-analytic-programming-integration.md
DEVELOPMENT.md
ROADMAP.md
SECURITY.md
pyproject.toml
poetry.lock
uv.lock
src/**
migrations/**
deploy/**
cisarik/ap working tree
cisarik/meta
canonical FrameNest untracked leftovers
canonical FrameNest .venv

Do not create, delete, reconstruct, copy, move, or symlink `.venv`.

Do not run:

poetry env use
uv sync
uv lock
pip install
./.ap/ap init

Do not launch:

cursor
code
xdg-open
GUI applications
AppImages

## Repository topology

Canonical FrameNest repository:

/home/agile/Projects/framenest

Origin expected:

https://github.com/cisarik/framenest.git

Canonical AP repository:

/home/agile/Projects/ap

Origin expected:

https://github.com/cisarik/ap.git

FrameNest AP submodule:

.ap

Expected `.gitmodules` URL:

https://github.com/cisarik/ap.git

Implementation must NOT occur in the canonical FrameNest working tree because Worker 1 observed unrelated untracked leftovers there.

Use a clean isolated worktree.

Authorized isolated-worktree path:

/home/agile/Projects/framenest-ap-consumer-convergence-w2

If that path already exists, contains data, or cannot be created safely, STOP and report BLOCKED.

Do not delete or overwrite it.

Create the worktree detached from the exact baseline. No implementation branch is required.

## Mandatory pre-mutation gate

Before any mutation, establish fresh repository evidence.

### FrameNest public gate

Using direct:

git ls-remote https://github.com/cisarik/framenest.git refs/heads/main

require exact public main:

d4c3402a4765b39cee0d8e2063d5ec8be161caf6

If public FrameNest main differs, STOP.

Do not rebase, merge, update the baseline, or adapt the plan.

### AP public gate

Using direct:

git ls-remote https://github.com/cisarik/ap.git refs/heads/main

require exact public main:

041de310ea33ed1b47dd8f5fbfcc2829d1a32514

If public AP main differs, STOP.

Do not follow a newer AP commit automatically.

A changed AP public generation requires new ORCHESTRATOR reconciliation.

### Canonical repository gate

Confirm:

- `/home/agile/Projects/framenest` resolves to the expected repository;
- local HEAD is still `d4c3402...`;
- tracked/index state remains clean;
- previously observed untracked material remains classified as pre-existing and is not touched.

Canonical untracked leftovers are not implementation inputs.

Do not clean them.

## Mandatory reading

Before mutation, read only the task-relevant current authority:

From canonical FrameNest:

AGENTS.md
docs/WORKER_EXECUTION_CONTRACT.md
ap.project.conf

From the pinned `.ap` / target AP as needed:

AP.md
AP_WORKER.md
UPDATING.md

Read the accepted Worker 1 plan supplied in this task context.

Do not expand into a general documentation or architecture review.

## Isolated-worktree setup

After all public and canonical gates PASS:

1. Create:

   /home/agile/Projects/framenest-ap-consumer-convergence-w2

   as a detached Git worktree at exactly:

   d4c3402a4765b39cee0d8e2063d5ec8be161caf6

2. Initialize the `.ap` submodule so that its baseline checkout equals:

   4862380f351ddd74e1c141a4babe2d0f0b43979d

3. Verify:

   containing gitlink == `.ap` HEAD == 4862380...

4. Verify the isolated superproject has no unexplained changes.

5. Run baseline:

   ./.ap/ap doctor

Baseline doctor must exit 0 and report PASS.

A baseline failure is not authority to repair unrelated state.

Classify and stop if it cannot be resolved without leaving the authorized boundary.

## Authorized implementation sequence

After the baseline gate passes:

### Step 1 - AP update

Run the canonical AP update mechanism:

./.ap/ap update --apply

The resulting `.ap` HEAD must be exactly:

041de310ea33ed1b47dd8f5fbfcc2829d1a32514

Do not accept another commit merely because it is newer.

Immediately verify:

git -C .ap rev-parse HEAD

and the containing repository gitlink state.

### Step 2 - candidate doctor

Run:

./.ap/ap doctor --candidate

It must exit 0 and report PASS.

### Step 3 - exact SHA assertion

Edit only the `EXPECTED_AP_COMMIT` value in:

tests/contract/test_ap_integration.py

New exact value:

041de310ea33ed1b47dd8f5fbfcc2829d1a32514

Do not refactor or otherwise edit this test.

### Step 4 - README current gitlink

In README.md, change only the SHA in the living statement:

"The current AP gitlink is"

from:

5c2f0e197d6aecdc6aca918b22e080bb58abc7a1

to:

041de310ea33ed1b47dd8f5fbfcc2829d1a32514

Do not edit surrounding AP methodology prose.

Do not change historical ADR SHAs.

## Validation

Before staging, inspect the complete diff.

The only changed paths must be:

.ap
tests/contract/test_ap_integration.py
README.md

Any unexpected fourth path is a hard stop unless it is proven to be a generated/untracked non-candidate artifact that can simply remain unstaged.

Do not delete or "fix" unexpected state.

### Exact-source test execution

The canonical project Python environment is:

/home/agile/Projects/framenest/.venv/bin/python

Do not create an environment inside the isolated worktree.

For Python evidence from the isolated candidate use:

PYTHONPATH=/home/agile/Projects/framenest-ap-consumer-convergence-w2/src \
  /home/agile/Projects/framenest/.venv/bin/python -m pytest \
  tests/contract/test_ap_integration.py

The command must exit 0.

If relevant to validating exact-source provenance, confirm that imported FrameNest source resolves below the isolated worktree `src/`, not the canonical checkout.

Do not run the full FrameNest suite.

`tests/contract/test_ap_project_contract.py` is intentionally outside the mutation allowlist and is not a mandatory test because planning proved its contract unchanged. You may run it read-only only if a concrete result from the required checks makes that confirmation necessary.

### Stage

Stage exactly:

.ap
tests/contract/test_ap_integration.py
README.md

Nothing else.

After staging, confirm the index contains exactly those paths.

### Strict AP doctor

Run:

./.ap/ap doctor

against the staged candidate.

It must exit 0 and include:

ap doctor: PASS

Confirm the resolved governing variant is stable if emitted by the tool.

Optionally run the cheap project contract readiness check if useful:

./.ap/ap project check \
  --root /home/agile/Projects/framenest-ap-consumer-convergence-w2 \
  --candidate

Any mandatory non-zero exit or traceback prevents implementation PASS.

Do not repair an environment defect by reconstructing `.venv` or changing dependencies.

## Candidate commit

When and only when all mandatory checks PASS:

create exactly one ordinary commit.

Required subject:

chore: adopt current AP generation

No amend.

No second implementation commit.

Parent must be exactly:

d4c3402a4765b39cee0d8e2063d5ec8be161caf6

After commit, record:

- candidate commit SHA;
- parent SHA;
- tree SHA;
- subject;
- exact changed paths;
- exact `.ap` gitlink stored in the candidate;
- `.ap` checkout SHA;
- worktree status.

Candidate `.ap` gitlink and checkout must both equal:

041de310ea33ed1b47dd8f5fbfcc2829d1a32514

Do not push the candidate.

Do not remove the isolated worktree after producing the terminal report. Preserve it for possible independent acceptance evidence.

## Candidate PASS conditions

Implementation-PASS requires all of the following:

1. public FrameNest main was exactly `d4c3402...` immediately before mutation;
2. public AP main was exactly `041de310...` immediately before mutation;
3. isolated worktree began at exact baseline `d4c3402...`;
4. baseline AP pin and checkout were exactly `4862380...`;
5. baseline `./.ap/ap doctor` passed;
6. `.ap` was updated through the authorized AP update mechanism;
7. final `.ap` HEAD is exactly `041de310...`;
8. `doctor --candidate` passed;
9. only the three allowlisted paths changed;
10. focused `test_ap_integration.py` passed with exact candidate-source execution;
11. exactly the three allowlisted paths were staged;
12. strict staged `./.ap/ap doctor` passed;
13. exactly one candidate commit was created;
14. candidate parent is exactly `d4c3402...`;
15. candidate contains no dependency, product, migration, deployment, Meta, AP-source, NUC, or production mutation;
16. no push occurred.

## Independent acceptance boundary

Do not self-certify independent acceptance.

If implementation passes, the next intended phase is a separate fresh independent Worker.

That Worker, not you, will determine acceptance-PASS for the immutable candidate.

Do not start that phase.

## Publication and deployment boundary

Publication is NOT authorized.

Do not push.

Do not change public `refs/heads/main`.

Deployment is NOT required by the accepted plan and is NOT authorized.

Do not SSH to the NUC.

Do not inspect or mutate production merely to add evidence.

Schema remains outside this implementation and expected production schema remains `0028`.

## AP empirical-learning rule

Do not create an AP improvement proposal unless this implementation reveals a concrete protocol defect, contradiction, unsafe ambiguity, impossible state, or material process failure.

Routine fail-closed behavior, canonical-worktree dirtiness, or ordinary update friction is not automatically an AP defect.

Do not mutate `cisarik/ap`.

## Stopping conditions

Return BLOCKED or PARTIAL without improvisation if:

- either public ref differs from its exact authorized identity;
- baseline commit differs;
- isolated worktree path already exists;
- isolated baseline cannot be established cleanly;
- baseline doctor fails for a cause outside authority;
- AP update resolves to any SHA other than `041de310...`;
- an additional tracked path must change;
- `AGENTS.md`, `ap.project.conf`, project-contract tests, or Worker execution contract unexpectedly require mutation;
- exact-source testing cannot be established;
- a required validation command exits non-zero;
- a dependency/environment repair appears necessary;
- implementation would require AP, Meta, NUC, provider, production, network, or publication authority;
- secrets or credentials beyond ordinary public Git access would be required.

Do not broaden the task.

## Terminal report contract

Return exactly one terminal report and stop.

It must begin:

### Report for ORCHESTRATOR_CHAT

Then include:

Logical whole identity: framenest-current-ap-generation-adoption-and-consumer-rebaseline
Worker session ordinal: 02
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS | not-applicable
Result artifact or commit: <exact candidate SHA or not-applicable>
Result evidence: <bounded exact evidence>
Logical-whole closure: not-closed

Report:

1. public-ref gate results;
2. canonical baseline observations;
3. isolated-worktree identity;
4. baseline `.ap` identity and baseline doctor result;
5. AP update result and exact target identity;
6. changed files and exact purpose;
7. candidate and strict doctor results;
8. focused test command and exit result;
9. candidate-source provenance evidence when applicable;
10. staged-path verification;
11. candidate commit SHA, parent, tree and subject;
12. candidate `.ap` gitlink and checkout SHA;
13. final worktree status;
14. publication result: not authorized / none;
15. deployment result: not authorized / none;
16. production impact: none unless contradictory evidence was discovered;
17. AP empirical-learning evidence: none | <exact concrete evidence>;
18. deviations, risks, environment limitations, or missing evidence;
19. smallest next ORCHESTRATOR step.

Also include:

Start commit: d4c3402a4765b39cee0d8e2063d5ec8be161caf6
End commit: <candidate SHA if committed, otherwise exact observed HEAD>
Changed files: <exact list or none>
Tests and validation: <commands and results>
Commit result: <candidate SHA or none>
Push result: not authorized / none
Report justification: new-mutation | new-evidence | new-material-risk
Resolved Execution Issues / Near-Misses: none | <exact evidence>
Pre-Existing Failure Classification: none | <exact classification>
Authority expiry: implementation authority expired at this terminal report

Do not claim acceptance.

Do not claim publication.

Do not claim deployment.

Do not claim logical-whole closure.

Stop immediately after the terminal report.