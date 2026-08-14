WORKER 04 / EXCHANGE 01 — PUBLICATION
Role and session contract

You are Worker session 04, exchange 01 for the existing FrameNest logical whole:

framenest-ap-continuation-bootstrap-and-ledger-adoption

Worker session target:

fresh-worker-session

Native planning mode:

not-used

You are a fresh publication Worker.

You are not:

the implementation Worker;
the acceptance Worker;
an Orchestrator;
a correction Worker;
a deployment Worker.

The exact implementation candidate has already received independent acceptance-PASS.

Your sole mutation purpose is the bounded publication of that exact accepted Git object, if and only if all publication preconditions remain true.

You have no project-content correction authority.

1. Exact accepted object

The independently accepted FrameNest candidate is:

4b04b86e4ea52c673c41624e3f2abe1e59d45907

Expected parent:

230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb

Accepted tree:

ca8d25d2aafed69cc5cd03056c47eaaaa65ef82c

Accepted subject:

docs: adopt AP 17b7e085 with continuation ledger activation

Accepted changed project paths:

.ap
AGENTS.md
README.md
docs/AP_UPGRADE_OBSERVATIONS.md
tests/contract/test_ap_integration.py

Accepted AP gitlink:

17b7e085139e9bcbb0e4953d26aef9b6687d541c

Acceptance Worker 03 independently established:

Standard terminal status: PASS
Phase-qualified result: acceptance-PASS

Do not reinterpret this as permission to modify the candidate.

2. Publication objective

If all publication gates pass, perform exactly one ordinary non-force publication of:

4b04b86e4ea52c673c41624e3f2abe1e59d45907

to:

https://github.com/cisarik/framenest.git
refs/heads/main

The intended transition is:

230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
→
4b04b86e4ea52c673c41624e3f2abe1e59d45907

No other branch, tag, ref, repository, deployment target, service, or environment is in scope.

3. Working location

Use the accepted candidate worktree:

/home/agile/Projects/framenest-worktrees/framenest-ap-continuation-bootstrap-and-ledger-adoption-w2

Expected branch:

feat/ap-continuation-bootstrap-and-ledger-adoption

Expected HEAD:

4b04b86e4ea52c673c41624e3f2abe1e59d45907

Begin read-only.

Do not modify the primary checkout:

/home/agile/Projects/framenest

Do not create another worktree unless publication becomes impossible to verify read-only from the accepted one. In that case, stop rather than expanding scope.

4. Governing reading

Before any publication mutation, read:

AGENTS.md
docs/WORKER_EXECUTION_CONTRACT.md

from the accepted candidate worktree.

Also inspect the pinned AP publication/Worker requirements needed for this publication step, including at minimum:

.ap/AP.md
.ap/AP_WORKER.md
.ap/AP_ORCHESTRATOR.md

and any directly referenced publication or authority section required to execute safely.

Do not perform a new broad acceptance audit. Acceptance is already complete.

Your task is publication-state verification plus exact-object publication.

5. Mandatory read-only publication preflight

Before any push, independently verify all of the following.

Candidate identity

Prove:

HEAD =
4b04b86e4ea52c673c41624e3f2abe1e59d45907

Prove the object exists and is a commit.

Prove:

parent =
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb

Prove:

tree =
ca8d25d2aafed69cc5cd03056c47eaaaa65ef82c

Prove exact subject.

Candidate immutability

Verify the accepted candidate worktree has:

no tracked modifications;
no staged modifications;
no unexplained submodule drift;
.ap HEAD exactly 17b7e085139e9bcbb0e4953d26aef9b6687d541c;
.ap clean.

Ordinary ignored pytest/cache residue previously observed is not a publication blocker if it remains untracked/ignored and cannot affect the candidate object.

Public FrameNest state

Perform credential-free direct Git readback:

git ls-remote https://github.com/cisarik/framenest.git refs/heads/main

Required pre-publication value:

230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
Public AP state

Perform credential-free direct Git readback:

git ls-remote https://github.com/cisarik/ap.git refs/heads/main

Expected selected AP target:

17b7e085139e9bcbb0e4953d26aef9b6687d541c

If AP public main has advanced but the accepted exact AP commit remains valid and published, do not automatically treat that as permission to retarget the candidate.

Preserve the exact accepted object.

If AP advancement creates a material governing ambiguity under the pinned AP rules, stop for Orchestrator arbitration.

Ancestry

Prove that:

230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb

is the exact parent of:

4b04b86e4ea52c673c41624e3f2abe1e59d45907

Publication must be a straightforward fast-forward of public main.

No merge, rebase, squash, amend, cherry-pick, or candidate regeneration is authorized.

6. Fail-closed publication rules

Before publication, return BLOCKED without push if any of the following occurs:

public FrameNest main no longer equals 230ce43a...;
accepted candidate HEAD differs from 4b04b86e...;
candidate object, parent, tree, or subject differs;
tracked/staged candidate mutation exists;
.ap gitlink or checkout differs materially from the accepted object;
candidate is no longer a direct fast-forward from public main;
push would require force;
remote identity differs;
credential or transport behavior is ambiguous;
publication would mutate any other ref;
candidate would need correction before publication.

Do not repair a failed publication precondition.

Do not rebase onto a newer public main.

Do not amend the accepted candidate.

Do not create a replacement commit.

Return the exact discrepancy to the Orchestrator.

7. Publication authority

Only after the complete read-only preflight passes, you are authorized to perform exactly one ordinary non-force publication attempt of the accepted object.

Preferred semantics:

git push origin \
  4b04b86e4ea52c673c41624e3f2abe1e59d45907:refs/heads/main

or an operationally equivalent ordinary porcelain command that:

publishes exactly that commit;
targets exactly refs/heads/main;
performs no force;
updates no other ref;
uses the canonical FrameNest remote.

Do not push the branch name merely because it happens to point at the candidate unless you still prove that the exact object being sent is 4b04b86e....

Exact-object publication is preferred.

One ordinary non-force push only.

8. Forbidden publication actions

You have no authority to:

edit project files;
stage;
commit;
amend;
reset;
merge;
rebase;
squash;
cherry-pick;
force-push;
push another branch;
push a tag;
delete a remote ref;
modify GitHub repository settings;
deploy;
mutate production;
mutate NUC;
mutate Tailscale/network state;
mutate provider state;
mutate database/schema state;
mutate Meta;
create archive files;
create 00_handout.md;
create continuation/handoff files;
perform the fresh-Orchestrator restoration test.

Do not run implementation or acceptance correction.

9. Immediate post-push verification

A successful push command alone is insufficient.

Immediately after the ordinary non-force push, perform credential-free direct public readback:

git ls-remote https://github.com/cisarik/framenest.git refs/heads/main

Required result:

4b04b86e4ea52c673c41624e3f2abe1e59d45907

If direct public readback does not equal the exact accepted candidate, publication cannot PASS.

Do not attempt a second corrective push unless the first push demonstrably performed no ref mutation and AP/project authority explicitly permits retry of the same exact operation.

If publication state is ambiguous, stop and report it.

10. Disposable remote-object verification

After public readback confirms:

refs/heads/main =
4b04b86e4ea52c673c41624e3f2abe1e59d45907

perform a credential-free/disposable verification sufficient to prove the published repository exposes the exact accepted object and ancestry.

Prefer a temporary/disposable Git object check that does not mutate FrameNest project worktrees.

Verify at minimum:

published HEAD =
4b04b86e4ea52c673c41624e3f2abe1e59d45907
published tree =
ca8d25d2aafed69cc5cd03056c47eaaaa65ef82c
published parent =
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb

and subject:

docs: adopt AP 17b7e085 with continuation ledger activation

If practical, verify the published .ap gitlink from the remote-fetched tree:

17b7e085139e9bcbb0e4953d26aef9b6687d541c

This is publication evidence, not a new acceptance audit.

Use a disposable temporary directory if cloning/fetching is needed.

Do not mutate the accepted worktree merely to prove remote identity.

11. Publication success rule

Return:

Standard terminal status: PASS
Phase-qualified result: publication-PASS

only if all of the following are true:

accepted candidate remained byte/object-identical;
pre-push public FrameNest main was exact parent 230ce43a...;
publication used one ordinary non-force operation;
no other ref was intentionally mutated;
push exited successfully;
credential-free direct public readback returns exact candidate 4b04b86e...;
disposable/public Git-object evidence confirms exact tree/parent identity;
no unauthorized project/environment mutation occurred.

Publication-PASS does not yet close the logical whole.

One final selected acceptance activity remains outside this Worker:

genuine minimal-seed fresh-Orchestrator restoration test

That test becomes eligible only because publication and direct public readback have succeeded.

12. Archive identity

Do not mutate Meta yourself.

The Cooperator/Orchestrator will archive this exact prompt and your actual report externally as:

04_publication_00.md
04_report_00.md

Do not create those files in FrameNest.

There is no:

00_handout.md

for this logical whole.

13. Required terminal report

Return one detailed English report beginning exactly:

### Report for ORCHESTRATOR_CHAT


Logical whole identity: framenest-ap-continuation-bootstrap-and-ledger-adoption
Worker session ordinal: 04
Worker exchange ordinal: 01
Standard terminal status: <PASS|BLOCKED|PARTIAL>
Phase-qualified result: <publication-PASS or appropriate non-PASS result>
Result artifact or commit: 4b04b86e4ea52c673c41624e3f2abe1e59d45907
Result evidence: <compact strongest publication evidence>
Logical-whole closure: not-closed
Report justification: <publication-mutation|blocked-before-publication|appropriate classification>
Authority expiry: all Worker 04 authority expired at this terminal report

Then include:

1. Fresh publication role

Confirm:

fresh Worker;
Native Plan Mode not-used;
no implementation/acceptance authority inherited;
governing publication-relevant documents read.
2. Candidate immutability preflight

Report exact:

worktree;
branch;
HEAD;
parent;
tree;
subject;
porcelain;
.ap HEAD/status;
whether ignored residue existed and its classification.
3. Pre-publication public refs

Report exact credential-free readback for:

FrameNest refs/heads/main
AP refs/heads/main
4. Fast-forward proof

Prove exact:

230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
→
4b04b86e4ea52c673c41624e3f2abe1e59d45907

with no merge/rebase/squash/correction required.

5. Publication operation

Report:

exact publication command or semantically exact operation;
target remote;
target ref;
whether force was used;
exit status;
remote response.
6. Direct public readback

Report exact post-push credential-free:

refs/heads/main

Required:

4b04b86e4ea52c673c41624e3f2abe1e59d45907
7. Published object verification

Report disposable/public verification of:

commit;
tree;
parent;
subject;
preferably .ap gitlink.
8. Mutation accounting

Explicitly confirm no:

project edit;
correction commit;
merge/rebase/squash;
force push;
extra ref push;
deployment;
production/NUC/network/provider/schema mutation;
Meta mutation;
handoff/continuation artifact;
fresh-Orchestrator restoration test.
9. Logical-whole state

If publication-PASS, state:

logical whole remains not-closed

because the final genuine minimal-seed fresh-Orchestrator restoration test has not yet been performed.

State that publication authority is expired.

10. Next authority boundary

If publication-PASS, state exactly that:

public FrameNest main now equals accepted candidate 4b04b86e4ea52c673c41624e3f2abe1e59d45907;
Worker 04 authority has expired;
no further implementation or publication mutation is authorized;
next step is the genuine minimal-seed fresh-Orchestrator restoration test against the now-published repository state;
that test must begin from the minimal continuation seed defined by the newly adopted AP, not from this Worker report as an outgoing handoff.

Do not perform that restoration test yourself.

Do not provide an outgoing Orchestrator handout.

Do not propose another logical whole.