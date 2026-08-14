# WORKER 02 / EXCHANGE 01 — ISOLATED-WORKTREE RECOVERY + IMPLEMENTATION

## Role and session contract

You are **Worker session 02, exchange 01** for the already-selected FrameNest logical whole:

```text
framenest-ap-continuation-bootstrap-and-ledger-adoption
```

Worker session target:

```text
fresh-worker-session
```

Native planning mode:

```text
not-used
```

You are a **fresh implementation Worker**.

You are not an Orchestrator, acceptance Worker, publication Worker, or planning Worker.

Worker 01 already terminated correctly with:

```text
preflight-BLOCKED
```

because the primary checkout at `/home/agile/Projects/framenest` is a stale clean ancestor of current public FrameNest `main`. No implementation candidate exists from Worker 01. This is therefore **the same logical whole**, not a new one.

Your authority consists of two ordered phases:

1. narrowly bounded **execution-topology recovery** by creating one isolated task worktree from the exact selected public FrameNest baseline;
2. only after that recovery succeeds, the previously selected bounded implementation.

Do not mutate the primary checkout's tracked project contents.

---

# 1. Authoritative continuation state

The Cooperator selected:

```text
Logical whole:
framenest-ap-continuation-bootstrap-and-ledger-adoption
```

The intended target AP commit is exactly:

```text
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

Worker 01 independently established the following public state:

```text
FrameNest refs/heads/main =
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb

AP refs/heads/main =
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

Worker 01 also established that the real primary checkout was:

```text
/home/agile/Projects/framenest

branch:
feat/ap-baseline-bound-execution-adoption

HEAD:
d4c3402a4765b39cee0d8e2063d5ec8be161caf6
```

with:

```text
0 commits ahead of public main
11 commits behind public main
```

and therefore unsuitable as the implementation parent.

Worker 01 found:

```text
primary-checkout .ap gitlink:
4862380f351ddd74e1c141a4babe2d0f0b43979d

public-main .ap gitlink:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Worker 01 performed no mutation and created no candidate. Its authority has expired.
Do not treat any of these facts as a substitute for your own preflight. Re-verify all material facts directly.

---

# 2. Repository identities

Primary FrameNest repository:

```text
/home/agile/Projects/framenest
```

Canonical public repositories:

```text
https://github.com/cisarik/framenest.git
https://github.com/cisarik/ap.git
```

Authorized isolated task worktree path:

```text
/home/agile/Projects/framenest-worktrees/framenest-ap-continuation-bootstrap-and-ledger-adoption-w2
```

Authorized new task branch name:

```text
feat/ap-continuation-bootstrap-and-ledger-adoption
```

The task branch and worktree must be created directly from exact FrameNest commit:

```text
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
```

Do not base them on:

* the current primary-checkout `HEAD`;
* the stale feature branch;
* local `main` without exact-SHA verification;
* a floating remote branch expression without confirming its exact object;
* any unpublished candidate from another logical whole.

---

# 3. Governing objective

Adopt published Analytic Programming commit:

```text
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

into current FrameNest public-main lineage and make the **smallest project-local activation** needed to exercise:

1. AP's **Continuation Bootstrap**;
2. AP's optional **durable upgrade-ledger storage projection**.

The resulting candidate must remain suitable for:

```text
fresh independent acceptance
→ separately authorized ordinary non-force publication
→ direct public readback
→ genuine minimal-seed fresh-Orchestrator restoration test
```

The final restoration test is explicitly **not part of Worker 02**.

---

# 4. Stage A — mandatory read-only recovery preflight

Before any mutation, work from:

```text
/home/agile/Projects/framenest
```

Read the root:

```text
AGENTS.md
```

and any project-owned execution contract it directly requires, including the existing Worker execution contract if applicable.

Then reconstruct the repository state.

At minimum verify:

* exact repository root;
* `remote.origin.url`;
* current primary-checkout branch;
* exact primary-checkout `HEAD`;
* tracked, staged, untracked, and material ignored state;
* existing registered worktrees;
* exact local `origin/main`;
* existence and type of exact object `230ce43a...`;
* credential-free public FrameNest `refs/heads/main`;
* credential-free public AP `refs/heads/main`;
* whether the authorized task branch already exists locally;
* whether the authorized worktree path already exists;
* whether another registered worktree already uses either that branch or path;
* whether anything has materially changed since Worker 01's report.

Expected public state:

```text
FrameNest refs/heads/main =
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb

AP refs/heads/main =
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

Expected primary checkout remains the stale lineage identified by Worker 01.

### Fail-closed Stage A rules

Before creating the isolated worktree, STOP with `BLOCKED` and perform no mutation if any of the following is true:

* public FrameNest `main` differs from `230ce43a...`;
* public AP `main` differs from `17b7e085...`;
* exact FrameNest object `230ce43a...` is unavailable locally;
* the primary checkout has materially changed in a way that invalidates Worker 01's recovery classification;
* the requested task branch already exists;
* the requested worktree path already exists;
* the branch/path is already registered to another worktree;
* creating the requested worktree would overwrite or interfere with owner state;
* repository topology cannot be understood unambiguously.

Do not delete, reuse, reset, rename, prune, force-detach, or overwrite an existing branch/worktree to make room.

Do not fetch the FrameNest superproject merely to rescue a failed Stage A assumption.

Worker 01 already observed local `origin/main` at the exact selected public commit, so absence of that object is a material discrepancy requiring return to the Orchestrator.

---

# 5. Stage B — narrowly authorized execution-topology mutation

Only after Stage A passes, you are authorized to create exactly one isolated task worktree and exactly one new task branch.

Create:

```text
branch:
feat/ap-continuation-bootstrap-and-ledger-adoption

worktree:
/home/agile/Projects/framenest-worktrees/framenest-ap-continuation-bootstrap-and-ledger-adoption-w2
```

directly from:

```text
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
```

This is an explicit exception to the normal project-path mutation allowlist because Git must update its administrative branch/worktree metadata to register the isolated execution surface.

That administrative mutation is authorized **only** for creating this exact branch/worktree pair.

Do not:

* checkout the primary worktree to another commit;
* fast-forward the primary worktree;
* pull in the primary worktree;
* reset it;
* merge it;
* rebase it;
* stash its owner state;
* clean it;
* delete its untracked residue;
* alter its tracked project contents.

After creating the isolated worktree, prove:

```text
new worktree HEAD =
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
```

and that the new branch points to exactly the same commit before implementation.

If the created topology does not match exactly, stop before project-content mutation.

---

# 6. Stage C — fresh implementation preflight inside the isolated worktree

From this point onward, work in:

```text
/home/agile/Projects/framenest-worktrees/framenest-ap-continuation-bootstrap-and-ledger-adoption-w2
```

Treat this as the implementation root.

Read its root:

```text
AGENTS.md
```

in full.

Inspect:

```text
.gitmodules
README.md
tests/contract/test_ap_integration.py
```

and establish the exact public-main AP integration baseline.

Expected baseline from Worker 01:

```text
.ap gitlink =
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

README AP pin =
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

tests/contract/test_ap_integration.py EXPECTED_AP_COMMIT =
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Independently verify those values from the exact `230ce43a...` tree.

If any differs materially, stop before project-content mutation.

Also confirm:

```text
docs/AP_UPGRADE_OBSERVATIONS.md
```

does not already exist on this baseline.

---

# 7. Baseline `.ap` initialization authority

The isolated worktree may initially have an uninitialized `.ap` working directory even though the superproject gitlink is correct.

After Stage C passes, you are authorized to perform the minimum standard Git-submodule operations necessary to initialize `.ap` at the exact baseline gitlink:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

This administrative/submodule initialization is permitted.

It may obtain missing AP objects from the canonical configured submodule remote if required.

Do not:

* use `git submodule update --remote`;
* change `.gitmodules`;
* change the canonical submodule URL;
* select an arbitrary branch tip;
* run destructive cleanup inside AP;
* modify AP source content.

After initialization prove:

```text
superproject baseline gitlink =
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

checked-out .ap HEAD =
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

.ap working tree =
clean
```

---

# 8. Read the currently pinned AP before adoption

Before obtaining or adopting the target generation, read the currently pinned governing AP documents required by FrameNest, including at minimum the applicable forms of:

```text
.ap/AP.md
.ap/AP_ORCHESTRATOR.md
.ap/AP_WORKER.md
.ap/PROMPT_CONTRACTS.md
.ap/INTEGRATION.md
```

and any directly referenced AP updating/integration document required to execute an existing-consumer upgrade safely.

Do not assume the old primary checkout's `4862380f...` AP generation governs this isolated worktree.

The governing pre-adoption AP generation here is whatever exact public-main gitlink proves, expected:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

---

# 9. Obtain and inspect exact target AP generation

After all preceding recovery gates succeed, you are authorized to obtain the exact AP target object through the existing canonical `.ap` repository:

```text
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

Network Git operations inside the initialized `.ap` repository are authorized only as needed to obtain and authenticate that exact published target.

Do not yet edit FrameNest project-owned files.

Before first project-content mutation, inspect the target AP documents **at exact commit `17b7e085...`**, including at minimum:

```text
AP.md
AP_ORCHESTRATOR.md
AP_WORKER.md
PROMPT_CONTRACTS.md
INTEGRATION.md
```

plus any directly referenced target document governing:

* Continuation Bootstrap;
* consumer upgrade behavior;
* optional durable upgrade-ledger storage;
* canonical target identity;
* ledger declaration;
* ledger header;
* activation snapshot;
* active-entry lifecycle.

Do not infer these details from this prompt when the target AP text is more precise.

If the target AP contract materially contradicts this selected boundary, stop without expanding scope.

---

# 10. Capture managed-block baseline before editing

Before modifying root `AGENTS.md`, identify the exact existing managed AP block boundaries.

Capture deterministic byte-level evidence of the complete managed block before editing.

The managed AP block must remain:

```text
byte-for-byte unchanged
```

throughout this implementation.

Do not regenerate it merely because the `.ap` pin changes.

Do not run a command that rewrites the managed block unless the target AP explicitly requires that for this exact consumer upgrade. If such a requirement would contradict this selected logical-whole boundary, stop and return to the Orchestrator rather than broadening authority.

---

# 11. Project-content mutation authority

Only after all recovery, initialization, target-inspection, and managed-block-baseline gates pass, implementation mutation authority activates.

The complete authorized **project content** mutation allowlist is:

```text
.ap
AGENTS.md
README.md
tests/contract/test_ap_integration.py
docs/AP_UPGRADE_OBSERVATIONS.md
```

No other project content path may change.

For `.ap`, the intended tracked superproject mutation is only the submodule gitlink transition from the verified public-main baseline to:

```text
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

Do not independently modify files inside AP.

---

# 12. Exact implementation

## 12.1 `.ap`

Move the existing FrameNest `.ap` submodule to exactly:

```text
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

Requirements:

* preserve the existing submodule architecture;
* preserve canonical repository identity;
* use the exact commit object, not a branch tip;
* leave `.ap` itself clean;
* the superproject candidate gitlink must resolve to exactly `17b7e085...`.

Do not run `ap init` merely to activate the ledger.

Do not use a broad reinitialization mechanism when a simple exact-pin adoption suffices.

---

## 12.2 Root `AGENTS.md`

The managed AP block must remain byte-for-byte identical.

Outside that block, in **project-owned content only**, add the minimum declaration required by AP `17b7e085...` to activate the optional durable upgrade-ledger storage projection.

It must identify the canonical AP target:

```text
https://github.com/cisarik/ap.git
```

and exactly one committed Markdown ledger:

```text
docs/AP_UPGRADE_OBSERVATIONS.md
```

Use the exact target AP terminology and structure where normative.

Do not duplicate AP rules unnecessarily.

Do not create a second continuation system.

---

## 12.3 `docs/AP_UPGRADE_OBSERVATIONS.md`

Create exactly:

```text
docs/AP_UPGRADE_OBSERVATIONS.md
```

Its initial content must satisfy the exact target AP durable-ledger contract.

It must contain:

* the valid required header;
* canonical target identity;
* the valid activation snapshot required by AP;
* **zero synthetic upgrade observations**.

Do not populate the file merely to make it look active.

Do not resurrect historical/exhausted AP backlog.

Do not manufacture defects.

Do not add placeholder future work unless the AP contract literally requires an explicit empty-state representation.

If AP defines a canonical empty active-observation form, use it exactly.

This file is a durable Markdown projection, not an executable subsystem.

---

## 12.4 `README.md`

Make only the minimal AP-pin convergence necessary to reflect:

```text
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

Do not rewrite unrelated documentation.

---

## 12.5 `tests/contract/test_ap_integration.py`

Update the existing exact-pin projection so its expected AP commit becomes:

```text
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

Preserve the existing test philosophy.

Do not create:

* a new ledger parser;
* a ledger schema validator;
* a Continuation Bootstrap executor;
* a broad new test framework.

A tiny compatibility adjustment inside this already-authorized file is permissible only if directly required by the adopted AP generation and demonstrably part of the existing integration contract.

---

# 13. Explicitly forbidden scope

Do not create or modify:

* a FrameNest ADR;
* `00_handout.md`;
* any continuation/handoff artifact;
* `NEXT`, `BOOT`, resume, restoration-state, or generated-state files;
* executable ledger parsers;
* executable ledger validators;
* synthetic AP backlog;
* unrelated tests;
* `.gitmodules`;
* `ap.project.conf`;
* Meta;
* production;
* NUC;
* Tailscale/network state;
* provider state;
* deployment state;
* database/schema state;
* generated prompt archives in FrameNest.

Do not perform the future fresh-Orchestrator restoration test.

Do not create another logical whole.

---

# 14. Continuation Bootstrap intent

This logical whole is testing whether ordinary durable repository state is sufficient for later fresh-Orchestrator reconstruction.

Therefore do **not** create a special permanent continuation file.

The future fresh Orchestrator must discover the relevant state through ordinary project authority, including:

* root `AGENTS.md`;
* exact pinned AP generation;
* target AP Continuation Bootstrap rules;
* explicitly declared durable ledger;
* committed ledger activation snapshot;
* ordinary Git/public evidence.

Do not make that later test artificially easy by encoding a bespoke handoff.

This logical whole has **no outgoing Orchestrator handout**.

There must be no:

```text
00_handout.md
```

---

# 15. Validation

Validation must be narrow, deterministic, and sufficient.

Do not run an unrelated full FrameNest suite merely for volume.

## 15.1 Exact branch ancestry

Before final candidate commit, prove:

```text
task branch parent lineage includes exact baseline:
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
```

and that no stale primary-checkout commit became the parent by accident.

The implementation candidate must be a direct bounded continuation of the selected public-main baseline unless the actual implementation itself introduces the one new commit.

---

## 15.2 Exact diff allowlist

Prove all project-content changes are confined to:

```text
.ap
AGENTS.md
README.md
tests/contract/test_ap_integration.py
docs/AP_UPGRADE_OBSERVATIONS.md
```

Inspect both staged and unstaged state.

Administrative Git/worktree/submodule metadata created by the explicitly authorized topology recovery is not a project-content scope violation.

No other tracked project file may enter the candidate.

---

## 15.3 AP target proof

Prove:

```text
checked-out .ap HEAD =
17b7e085139e9bcbb0e4953d26aef9b6687d541c

candidate superproject .ap gitlink =
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

and:

```text
.ap working tree = clean
```

Also preserve evidence that the object came from the canonical configured AP repository/history.

---

## 15.4 Managed-block byte identity

Perform an exact deterministic before/after comparison of the managed AP block in root `AGENTS.md`.

PASS requires:

```text
before bytes == after bytes
```

A visual or semantic comparison alone is insufficient.

Record the comparison method and digest/length or equivalent exact evidence.

---

## 15.5 Ledger semantic proof

Using the exact target AP normative text, prove:

* project-owned `AGENTS.md` explicitly activates durable ledger storage;
* canonical target is exactly:
  `https://github.com/cisarik/ap.git`;
* declared ledger path is exactly:
  `docs/AP_UPGRADE_OBSERVATIONS.md`;
* ledger header is valid;
* activation snapshot is valid;
* zero synthetic entries exist;
* no executable ledger machinery was introduced.

Do not invent validation semantics not present in AP.

---

## 15.6 Existing focused FrameNest contract

Run the focused AP integration contract containing:

```text
tests/contract/test_ap_integration.py
```

using the repository-prescribed Python/tooling environment.

Do not substitute arbitrary system Python.

Required gate must exit zero.

A non-zero exit cannot support PASS.

---

## 15.7 AP-supported consumer validation

Use the exact target AP documentation to identify and run the applicable **non-destructive validation/check/doctor** operations for an existing consumer adopting a new pinned AP generation.

If target AP distinguishes:

* candidate validation;
* staged integration validation;
* strict/current integration validation;

apply them in their intended order where applicable.

Do not run `ap init` merely as a validator.

Do not run an AP command that would intentionally mutate paths outside the selected boundary.

If the only documented operation would broaden project mutation beyond authority, stop and return that contradiction rather than silently allowing it.

All required gates used to support PASS must exit zero.

---

## 15.8 Diff hygiene

Run:

```text
git diff --check
```

against the candidate state.

Review the complete diff manually.

Reject accidental:

* formatting churn;
* unrelated documentation edits;
* path additions;
* generated noise;
* owner-state contamination.

---

# 16. Public-ref stability gate before candidate commit

Immediately before creating the implementation candidate commit, perform a second credential-free direct readback of:

```text
https://github.com/cisarik/framenest.git refs/heads/main
https://github.com/cisarik/ap.git refs/heads/main
```

Expected values remain:

```text
FrameNest main =
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb

AP main =
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

If either has materially changed during the session, do not create the candidate commit.

Preserve the isolated worktree state and report the appropriate non-PASS result for Orchestrator arbitration.

Do not rebase or silently retarget.

---

# 17. Candidate commit authority

If and only if every required gate passes, create exactly one bounded implementation candidate commit on:

```text
feat/ap-continuation-bootstrap-and-ledger-adoption
```

The commit must contain only the selected project-content mutation.

Use a concise subject accurately describing the adoption.

Do not amend unrelated history.

After commit, record:

* candidate commit SHA;
* parent SHA;
* tree SHA;
* subject;
* exact changed paths;
* exact committed `.ap` gitlink;
* task-worktree porcelain;
* primary-checkout status to prove it remained untouched apart from authorized Git administrative topology metadata.

Do not push.

---

# 18. Independent acceptance and publication remain unauthorized

Worker 02 may perform implementation validation.

Worker 02 may **not** perform independent acceptance.

Worker 02 may **not** publish.

If Worker 02 returns `implementation-PASS`, all Worker 02 authority expires and the next actor must be a **fresh independent acceptance Worker** evaluating the exact candidate.

Only after acceptance may an independently authorized publication Worker perform an ordinary non-force publication.

Only after publication and direct public readback may the genuine minimal-seed fresh-Orchestrator Continuation Bootstrap test occur.

---

# 19. Archive identity

Do not mutate Meta.

Do not create archive files yourself.

The Cooperator/Orchestrator will archive this exact prompt and your actual terminal report externally as:

```text
02_implementation_00.md
02_report_00.md
```

Do not create them in FrameNest.

There is no `00_handout.md`.

---

# 20. Terminal-status discipline

Use:

```text
PASS
```

only when:

* recovery preflight succeeded;
* isolated worktree was created from exact `230ce43a...`;
* primary checkout remained protected;
* target AP was read at exact `17b7e085...`;
* implementation stayed inside authority;
* all required validation gates exited successfully;
* public refs remained stable through the pre-commit gate;
* exactly one candidate commit exists;
* candidate evidence is internally consistent.

Expected successful phase-qualified result:

```text
implementation-PASS
```

If Stage A fails before mutation:

```text
preflight-BLOCKED
```

If topology mutation occurred but later implementation cannot safely complete, use the exact AP-governed non-PASS status appropriate to the observed state.

Never transform a failing required gate into PASS through explanation.

Do not broaden scope to avoid a BLOCKED/PARTIAL result.

---

# 21. Required terminal report

Return one detailed English report for `ORCHESTRATOR_CHAT`.

Begin with:

```text
### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-ap-continuation-bootstrap-and-ledger-adoption
Worker session ordinal: 02
Worker exchange ordinal: 01
Standard terminal status: <exact status>
Phase-qualified result: <implementation-PASS or exact non-PASS result>
Result artifact or commit: <exact candidate SHA or not-applicable>
Result evidence: <compact strongest evidence>
Logical-whole closure: not-closed
Report justification: <new-mutation|blocked-before-mutation|appropriate classification>
Authority expiry: all Worker 02 authority expired at this terminal report
```

Then report the following.

## 1. Fresh-session confirmation

State:

* fresh Worker status;
* Native Plan Mode `not-used`;
* governing project/AP documents read;
* no inherited Worker 01 mutation authority.

## 2. Recovery preflight

Report exact:

* primary repository root;
* primary branch and HEAD;
* primary porcelain/owner-state classification;
* registered-worktree observations;
* local `origin/main`;
* direct public FrameNest main;
* direct public AP main;
* exact local presence of `230ce43a...`;
* task-branch/path absence before creation;
* whether Worker 01's stale-checkout classification remained valid.

## 3. Isolated worktree creation

Report:

* exact branch;
* exact worktree path;
* exact creation baseline;
* resulting HEAD;
* proof primary checkout tracked contents were not altered;
* any administrative Git metadata effect.

## 4. Public-main AP baseline

Report exact baseline values from the isolated worktree:

* `.ap` gitlink;
* README projection;
* integration-test projection;
* ledger-file pre-existence;
* `.gitmodules` canonical identity.

## 5. AP initialization and target acquisition

Report:

* baseline `.ap` initialization method;
* baseline checked-out SHA;
* target-object acquisition method;
* canonical source evidence;
* exact target SHA.

## 6. Target AP interpretation

Identify the exact target AP documents governing:

* Continuation Bootstrap;
* durable ledger activation;
* header;
* activation snapshot;
* canonical target;
* ledger-entry lifecycle.

Summarize only the semantics actually needed for this implementation.

## 7. Implementation

Report exact changes to:

```text
.ap
AGENTS.md
README.md
tests/contract/test_ap_integration.py
docs/AP_UPGRADE_OBSERVATIONS.md
```

## 8. Managed-block proof

Provide:

* before comparison evidence;
* after comparison evidence;
* exact result proving byte-for-byte identity.

## 9. Ledger proof

Report:

```text
canonical target
declared path
header semantics
activation snapshot
active/synthetic entry count
```

Explicitly confirm zero synthetic entries.

## 10. Validation

Report the materially relevant commands/gates and exit statuses, including:

* focused FrameNest AP integration contract;
* applicable AP doctor/candidate validation;
* managed-block exact comparison;
* ledger semantic check;
* `git diff --check`;
* diff allowlist check;
* second direct public-ref stability gate.

## 11. Candidate object

If PASS, report:

* commit SHA;
* parent;
* tree;
* subject;
* exact changed paths;
* committed `.ap` gitlink;
* final isolated-worktree status.

Explicitly prove:

```text
candidate parent =
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
```

unless Git object evidence shows an unexpected state requiring non-PASS.

## 12. Primary-checkout preservation

Report final primary checkout:

* branch;
* HEAD;
* tracked/staged status;
* owner residue status;

and confirm it was not reset, pulled, checked out, rebased, merged, cleaned, or otherwise rewritten.

## 13. Authority accounting

Explicitly confirm you did not:

* push;
* publish;
* merge;
* rebase;
* force-push;
* deploy;
* mutate production;
* mutate NUC/network/provider state;
* mutate schema/database state;
* mutate Meta;
* create ADRs;
* create `00_handout.md`;
* create continuation/handoff artifacts;
* create executable ledger tooling;
* invent AP backlog;
* perform the fresh-Orchestrator restoration test.

## 14. Next authority boundary

If implementation-PASS, state:

* logical whole remains `not-closed`;
* Worker 02 authority is expired;
* a fresh independent acceptance Worker is required next;
* publication remains separately unauthorized;
* minimal-seed fresh-Orchestrator restoration remains deferred until accepted publication plus direct public readback.

Do not provide an outgoing Orchestrator handout.

Do not propose another logical whole.

Execute only this continuation of the already-selected bounded logical whole.
