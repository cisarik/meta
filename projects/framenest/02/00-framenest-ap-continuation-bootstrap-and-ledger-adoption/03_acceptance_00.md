WORKER 03 / EXCHANGE 01 — FRESH INDEPENDENT ACCEPTANCE
Role and routing

You are Worker session 03, exchange 01 for the existing logical whole:

framenest-ap-continuation-bootstrap-and-ledger-adoption

Worker session target:

fresh-worker-session

Native planning mode:

not-used

Worker session profile:

Fresh Independent Audit

You are a fresh independent acceptance Worker.

You are not the implementation Worker.

You did not create the candidate.

You have no implementation, correction, publication, deployment, or project-content mutation authority.

Your job is to independently accept or reject the exact immutable candidate using repository evidence, governing project rules, exact pinned AP rules, direct public Git evidence, and proportionate validation.

1. Acceptance record
Acceptance candidate: 4b04b86e4ea52c673c41624e3f2abe1e59d45907
Acceptance owner map: candidate 4b04b86e4ea52c673c41624e3f2abe1e59d45907 root AGENTS.md + docs/WORKER_EXECUTION_CONTRACT.md + pinned .ap at 17b7e085139e9bcbb0e4953d26aef9b6687d541c
Acceptance allowlist: .ap, AGENTS.md, README.md, tests/contract/test_ap_integration.py, docs/AP_UPGRADE_OBSERVATIONS.md
Acceptance risk claims: exact public-main ancestry; exact AP pin adoption; managed-block byte preservation; structurally valid optional durable ledger activation with zero synthetic entries; existing integration projection convergence; no parallel continuation mechanism; no unauthorized scope
Acceptance control matrix: positive controls = candidate-object/ancestry proof, exact five-path diff, AP gitlink/checkout identity, managed-block parent-vs-candidate byte comparison, ledger declaration/header/snapshot/zero-entry verification against target AP, README/test-pin verification, strict AP doctor, focused AP integration test, diff hygiene, direct public-ref readback; negative controls = no extra changed paths, no AP source edits, no managed-block mutation, no synthetic Entry records, no ADR/handoff/00_handout/parser/validator/Meta/deploy/production mutation, no publication
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates

Do not change these acceptance coordinates or reinterpret this as implementation authority.

2. Exact candidate and expected ancestry

Acceptance candidate:

4b04b86e4ea52c673c41624e3f2abe1e59d45907

Expected parent:

230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb

Expected candidate tree reported by Worker 02:

ca8d25d2aafed69cc5cd03056c47eaaaa65ef82c

Expected subject:

docs: adopt AP 17b7e085 with continuation ledger activation

Expected changed project paths:

.ap
AGENTS.md
README.md
docs/AP_UPGRADE_OBSERVATIONS.md
tests/contract/test_ap_integration.py

Do not trust these values merely because they are supplied. Verify them directly from Git objects.

3. Working location

Candidate worktree created by Worker 02:

/home/agile/Projects/framenest-worktrees/framenest-ap-continuation-bootstrap-and-ledger-adoption-w2

Expected task branch:

feat/ap-continuation-bootstrap-and-ledger-adoption

Begin read-only.

Do not create a new branch.

Do not create another worktree unless an unforeseen repository topology makes read-only acceptance impossible, in which case STOP and report rather than expanding authority.

Do not modify the primary checkout at:

/home/agile/Projects/framenest
4. Mandatory governing reading

Read the candidate root:

AGENTS.md

in full.

Read:

docs/WORKER_EXECUTION_CONTRACT.md

and the task-relevant candidate files.

Then read the candidate's exact pinned AP generation at:

.ap

which is expected to resolve to:

17b7e085139e9bcbb0e4953d26aef9b6687d541c

Read at minimum:

.ap/AP.md
.ap/AP_ORCHESTRATOR.md
.ap/AP_WORKER.md
.ap/PROMPT_CONTRACTS.md
.ap/INTEGRATION.md
.ap/UPDATING.md

plus any target AP document directly required to judge:

Continuation Bootstrap;
upgrade-ledger activation;
declaration structure;
ledger-file header;
activation snapshot;
empty-ledger semantics;
consumer update validation;
acceptance independence.

Judge the candidate against those exact documents, not against Worker 02's interpretation.

5. Read-only candidate gate

Before running acceptance controls, establish:

exact repository/worktree root;
exact branch;
exact HEAD;
exact candidate object type;
exact parent;
exact tree;
exact subject;
complete porcelain status;
.ap checkout state;
candidate branch upstream state;
current registered worktree relation if material.

PASS evaluation requires the candidate worktree to represent exactly:

4b04b86e4ea52c673c41624e3f2abe1e59d45907

and to contain no unexplained tracked/staged mutation.

If HEAD differs, the candidate object is missing, the candidate has been amended, or unexplained tracked state contaminates acceptance, stop fail-closed.

Ignored test/runtime residue is not automatically a failure, but classify it explicitly if present and prove it cannot alter the committed object under review.

6. Direct public-state gate

Perform credential-free direct Git readback of:

https://github.com/cisarik/framenest.git refs/heads/main
https://github.com/cisarik/ap.git refs/heads/main

Expected:

FrameNest refs/heads/main =
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb


AP refs/heads/main =
17b7e085139e9bcbb0e4953d26aef9b6687d541c

The FrameNest candidate is deliberately not yet public.

Therefore public FrameNest main must still be its expected parent during this acceptance.

If FrameNest public main changed, stop rather than rebasing, retargeting, merging, or silently accepting against a different publication baseline.

If AP public main changed away from the selected exact target, preserve the exact candidate and return the discrepancy to the Orchestrator for arbitration.

No publication authority exists.

7. Candidate-object and ancestry acceptance

Independently prove:

candidate =
4b04b86e4ea52c673c41624e3f2abe1e59d45907
candidate parent =
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb

and inspect the entire parent-to-candidate diff.

The candidate must be a single bounded continuation from the selected public FrameNest baseline.

Prove that no stale Worker 01 checkout ancestry was inserted.

Reject acceptance if the candidate requires merge, rebase, squash, or ancestry repair.

8. Exact changed-path control

Independently enumerate the committed parent-to-candidate changed paths.

The complete set must be exactly:

.ap
AGENTS.md
README.md
docs/AP_UPGRADE_OBSERVATIONS.md
tests/contract/test_ap_integration.py

No sixth project path is allowed.

Inspect file modes and object types as well as names.

.ap must remain a Git gitlink/submodule path rather than copied AP content.

Do not rely on Worker 02's allowlist report.

9. Exact AP adoption controls

Independently prove from the candidate tree:

.ap gitlink =
17b7e085139e9bcbb0e4953d26aef9b6687d541c

and from the initialized candidate checkout:

.ap HEAD =
17b7e085139e9bcbb0e4953d26aef9b6687d541c

Also prove:

.ap is clean;
configured canonical AP repository remains https://github.com/cisarik/ap.git;
.gitmodules was not changed by the candidate;
no source file inside AP was independently edited;
target AP commit is the exact published object selected by this logical whole.
10. Managed AGENTS.md block control

This is a critical acceptance claim.

Compare the AP-managed block in:

parent 230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb:AGENTS.md

against:

candidate 4b04b86e4ea52c673c41624e3f2abe1e59d45907:AGENTS.md

Extract the complete byte range from:

<!-- BEGIN MANAGED AP INTEGRATION -->

through:

<!-- END MANAGED AP INTEGRATION -->

inclusive.

Use deterministic byte-level comparison.

Acceptance requires exact byte equality.

Record:

parent byte length;
candidate byte length;
digest or equivalent exact identity;
comparison result.

Do not accept a merely semantic or visual match.

Then verify that the new ledger declaration exists only in project-owned content outside the managed block.

11. Ledger declaration acceptance

Judge the candidate's project-owned root AGENTS.md against the exact target PROMPT_CONTRACTS.md.

Expected structural declaration:

AP upgrade ledger declaration:
Upgrade ledger: upgrade https://github.com/cisarik/ap.git
Ledger storage version: 1
Ledger path: docs/AP_UPGRADE_OBSERVATIONS.md

Verify independently:

declaration is outside the managed block;
exactly one declaration exists for this target;
target string is exact;
version is exact;
path is repository-relative;
path ends in .md;
path contains no ..;
path resolves inside the repository;
no conflicting declaration exists;
no duplicate target/path declaration exists.

Do not add an executable validation requirement that target AP itself does not define.

12. Ledger-file acceptance

Inspect committed:

docs/AP_UPGRADE_OBSERVATIONS.md

Expected required header structure:

Ledger storage version: 1
Upgrade ledger: upgrade https://github.com/cisarik/ap.git
Activation snapshot: <bounded identity>

Worker 02 reported the exact activation snapshot as:

Activation snapshot: zero candidate observations at 17b7e085139e9bcbb0e4953d26aef9b6687d541c

Do not accept that wording merely because Worker 02 chose it.

Independently judge whether it is a valid bounded identity of candidate observations at activation under target AP.

Prove:

storage version matches declaration;
canonical target repeats byte-for-byte;
activation snapshot is bounded and meaningful;
file is plain committed Markdown;
no YAML/JSON/TOML/front matter or external-schema dependency was introduced;
there are exactly zero Entry: records;
no synthetic AP observation/backlog is encoded elsewhere in the candidate.

A valid empty active ledger is expected and is not itself a defect.

13. Continuation Bootstrap negative control

This candidate is intended to prepare a later genuine fresh-Orchestrator test, not to fake one now.

Search the candidate diff and relevant new project content for accidental creation of:

00_handout.md;
BOOT;
NEXT;
continuation-state files;
handoff files;
resume/restoration-state files;
generated prompt archives;
bespoke "next logical whole" state;
another persistent continuation mechanism.

Acceptance requires none of those to have been introduced.

Do not perform the future fresh-Orchestrator restoration test in this session.

That test remains post-publication.

14. README and contract projection controls

Verify candidate README.md changed only as required to project the exact AP pin:

17b7e085139e9bcbb0e4953d26aef9b6687d541c

Reject unrelated README churn.

Verify:

tests/contract/test_ap_integration.py

uses exactly:

EXPECTED_AP_COMMIT =
17b7e085139e9bcbb0e4953d26aef9b6687d541c

and inspect the complete parent-to-candidate change in that file.

The candidate must not introduce a ledger parser, ledger validator, Continuation Bootstrap executor, or unrelated testing framework.

15. Independent validation controls

Run the narrow acceptance validation independently.

At minimum:

A. Git object/diff validation

Prove exact:

candidate;
parent;
tree;
changed path set;
.ap gitlink;
managed block equality.

Run appropriate diff hygiene including:

git diff --check 230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb..4b04b86e4ea52c673c41624e3f2abe1e59d45907

or an exact equivalent.

Required result: exit 0.

B. Strict AP doctor

Because the candidate commit already records the target gitlink and the .ap checkout is expected to equal it, run:

./.ap/ap doctor

Required result: PASS / exit 0 with the governing stable variant resolved as expected.

Do not create gitlink drift merely to rerun doctor --candidate.

The implementation Worker already used candidate mode during construction; independent acceptance should validate the final committed state.

C. Focused FrameNest integration test

Run:

tests/contract/test_ap_integration.py

through the repository-approved CPython 3.13 environment and execution contract.

Using the existing primary-checkout .venv as an execution binary is permissible only if project rules allow it and doing so does not mutate or reinterpret the candidate.

Do not reconstruct, delete, or replace .venv.

Required focused test result: exit 0.

D. Ledger structural/semantic review

This remains a direct acceptance review against target AP text.

Do not invent an executable parser merely to validate a contract that intentionally has no parser requirement.

16. Explicit treatment of Worker 02's project check --candidate result

Worker 02 reported that:

./.ap/ap project check --root <worktree> --candidate

exited 1 because the isolated worktree did not contain its own declared CPython executable.

Do not blindly inherit Worker 02's conclusion that this was non-gating.

Independently read target:

.ap/UPDATING.md
.ap/INTEGRATION.md

and determine whether project check --candidate is a required existing-consumer AP-pin-update acceptance gate.

If the target AP does not require it for this workflow and the observed failure is solely the already-described isolated-worktree runtime-layout limitation, record it as:

non-gating extra probe

with rationale.

Do not manufacture a local .venv or change project configuration to make that optional command green.

If your direct AP reading instead proves it is mandatory, acceptance cannot PASS.

Return the exact contradiction without correction.

17. Mutation prohibition

This acceptance is read-only with respect to project meaning and Git history.

You have no authority to:

edit candidate files;
stage;
commit;
amend;
correct;
reset;
checkout another candidate over this branch;
merge;
rebase;
squash;
cherry-pick;
push;
publish;
change .ap pin;
run ap init;
run an AP apply/update command that mutates the candidate;
change .gitmodules;
change ap.project.conf;
create or reconstruct .venv;
mutate Meta;
deploy;
mutate production;
mutate NUC/network/provider/database state.

Ordinary test-generated ignored caches are not desired. Avoid them where feasible. If a required test creates ordinary ignored transient state, classify it and do not include or clean owner state destructively.

No correction authority

If you discover a candidate defect, do not fix it.

Return a non-PASS acceptance report identifying:

exact failed claim;
exact evidence;
smallest correction boundary;
whether full fresh re-acceptance would be required.

Any correction requires a separately authorized Worker exchange/session.

18. Acceptance decision rule

Return:

Standard terminal status: PASS
Phase-qualified result: acceptance-PASS

only if every required acceptance claim is independently supported.

A PASS must establish that candidate:

4b04b86e4ea52c673c41624e3f2abe1e59d45907

is safe to pass to a separately authorized publication Worker without candidate modification.

Acceptance-PASS still does not close the logical whole.

Publication remains unauthorized in this session.

The genuine fresh-Orchestrator Continuation Bootstrap test remains deferred until after publication and direct public readback.

19. Required archive coordinates

Do not mutate Meta yourself.

The Cooperator/Orchestrator will archive this prompt and your actual report externally as:

03_acceptance_00.md
03_report_00.md

Do not create those files in FrameNest.

There is no:

00_handout.md

for this logical whole.

20. Required terminal report

Return one detailed English report beginning exactly:

### Report for ORCHESTRATOR_CHAT


Logical whole identity: framenest-ap-continuation-bootstrap-and-ledger-adoption
Worker session ordinal: 03
Worker exchange ordinal: 01
Standard terminal status: <PASS|PARTIAL|BLOCKED>
Phase-qualified result: <acceptance-PASS or appropriate non-PASS result>
Result artifact or commit: 4b04b86e4ea52c673c41624e3f2abe1e59d45907
Result evidence: <compact strongest independent evidence>
Logical-whole closure: not-closed
Report justification: <final-acceptance if PASS, otherwise exact AP-governed justification>
Authority expiry: all Worker 03 authority expired at this terminal report

Then include:

1. Fresh independence

Prove this was a fresh Worker and that Worker 02 implementation authority was not inherited.

2. Governing sources

List project/AP files actually read and exact pinned AP SHA.

3. Candidate identity

Report exact candidate, parent, tree, subject, branch/worktree state.

4. Public-state gate

Report direct credential-free FrameNest and AP main refs.

5. Changed-path and ancestry proof

Report complete parent-to-candidate path set and exact ancestry conclusion.

6. AP adoption proof

Report candidate gitlink, .ap HEAD, canonical origin, cleanliness, .gitmodules preservation.

7. Managed-block proof

Report exact parent/candidate byte lengths/digests and equality result.

8. Ledger declaration proof

Report exact declaration, placement, uniqueness, target, version, path validity.

9. Ledger-file proof

Report exact header, activation-snapshot judgment, Entry: count, synthetic-entry count.

10. Continuation negative controls

Confirm no 00_handout.md, BOOT/NEXT, handoff, continuation-state, parser, validator, or equivalent parallel mechanism was introduced.

11. README/test projection proof

Report exact candidate projections and whether their diffs were minimal.

12. Validation

Report exact relevant commands and exits, including:

diff hygiene;
strict AP doctor;
focused integration test;
direct structural ledger review.
13. project check --candidate disposition

Explicitly classify Worker 02's exit-1 extra probe as either:

non-gating with exact AP basis, or
acceptance blocker with exact AP basis.
14. Candidate mutation accounting

Confirm no candidate correction, commit, publication, or other unauthorized mutation occurred.

15. Residual risks / deviations

State none if none remain. Otherwise identify them exactly.

16. Next authority boundary

If acceptance-PASS, state exactly:

candidate 4b04b86e4ea52c673c41624e3f2abe1e59d45907 is independently accepted;
Worker 03 authority has expired;
logical whole remains not closed;
next actor is a separately authorized publication Worker;
only ordinary non-force publication of this exact accepted object may be considered;
fresh-Orchestrator restoration test remains deferred until publication plus direct public readback.

Do not publish.

Do not provide an outgoing Orchestrator handout.

Do not propose another logical whole.