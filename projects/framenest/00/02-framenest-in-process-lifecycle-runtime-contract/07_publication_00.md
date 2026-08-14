# Worker 7 — Exact Accepted-Candidate Publication

## Execution envelope

```text
Logical whole identity: framenest-in-process-lifecycle-runtime-contract
Worker session ordinal: 07
Worker exchange ordinal: 01
Worker role: publication operator
Phase: publication
Reasoning profile requested by Cooperator: Extra High
Fresh-worker session: required
Native planning mode: not-used
Delegation: not-authorized
Source mutation authority: none
Commit authority: none
Publication authority: one exact ordinary non-force fast-forward push
Deployment authority: none
NUC authority: none
Provider-call authority: none
AP or Meta mutation authority: none
Logical-whole closure authority: none
```

Publish only the exact independently accepted FrameNest candidate. Do not implement, amend, merge, rebase, squash, test, deploy, or begin another phase.

## Accepted identity

Expected current public refs:

```text
cisarik/ap refs/heads/main:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

cisarik/framenest refs/heads/main:
a72be476f5634394287082be07380d03fa7ccd4d
```

Accepted candidate chain:

```text
public baseline:
a72be476f5634394287082be07380d03fa7ccd4d

implementation:
5fe07b01bdfd587919d38a3d59ddd00e004d7394
parent: a72be476f5634394287082be07380d03fa7ccd4d
tree:   980f87991e7cf1cc239f82bea3a026dd3dce1b38

accepted correction:
148b6c2012809944262399c1a166e85082606fbf
parent: 5fe07b01bdfd587919d38a3d59ddd00e004d7394
tree:   1ea47dfbdbfe78c7a20f04b0c8bc54ba31805366
```

Accepted worktree:

```text
/home/agile/Projects/framenest-worktrees/framenest-in-process-lifecycle-runtime-contract-w5
```

Expected branch:

```text
fix/in-process-lifecycle-upload-validation-port-boundary
```

Worker 6 independently returned `acceptance-PASS` for exact commit `148b6c20…`. Publication is authorized only for that object.

## Start gates

Before any push:

1. Verify AP and FrameNest public refs using credential-free direct `git ls-remote`.
2. Verify the accepted worktree is clean and its HEAD and tree are exact.
3. Verify the complete parent chain.
4. Verify `.ap` gitlink is `041de310…`.
5. Verify schema head is `0028`.
6. Verify the configured publication remote resolves to `cisarik/framenest`, not a fork or unrelated repository.
7. Verify:

```bash
git merge-base --is-ancestor \
  a72be476f5634394287082be07380d03fa7ccd4d \
  148b6c2012809944262399c1a166e85082606fbf
```

8. Verify the candidate is exactly two commits ahead of the expected public baseline.
9. Run `git diff --check a72be476..148b6c20` and require exit 0.
10. Record the canonical owner worktree state without modifying it.

Do not modify or clean Worker 4’s dirty worktree. It is irrelevant historical residue.

## Public-ref decision

If FrameNest public `main` is exactly:

```text
a72be476f5634394287082be07380d03fa7ccd4d
```

perform one push as authorized below.

If public `main` is already exactly:

```text
148b6c2012809944262399c1a166e85082606fbf
```

perform no push. Verify the complete public object and report an idempotent `publication-PASS`.

If public `main` is any other SHA, stop as `BLOCKED`. Do not pull, merge, rebase, overwrite, or use force.

## Sole authorized publication mutation

From the accepted clean worktree, perform one ordinary non-force push of the exact object:

```bash
env GIT_TERMINAL_PROMPT=0 \
  git push --porcelain \
  origin \
  148b6c2012809944262399c1a166e85082606fbf:refs/heads/main
```

Requirements:

* no `--force`;
* no `--force-with-lease`;
* no deletion;
* no tag push;
* no other branch or ref;
* no upstream configuration;
* no merge, rebase, squash, cherry-pick, or replacement commit;
* no second push if the first command fails or returns ambiguous output.

A non-zero or ambiguous push result prohibits PASS until direct public readback proves the exact accepted SHA. Do not retry mutation automatically.

## Mandatory public verification

After successful push—or on the already-published path—verify through credential-free direct public transport:

```text
refs/heads/main =
148b6c2012809944262399c1a166e85082606fbf
```

Then create a disposable verification repository under a path obtained from `mktemp -d`. Fetch public `main` directly from the public FrameNest repository and independently verify:

```text
HEAD:
148b6c2012809944262399c1a166e85082606fbf

tree:
1ea47dfbdbfe78c7a20f04b0c8bc54ba31805366

parent:
5fe07b01bdfd587919d38a3d59ddd00e004d7394

grandparent:
a72be476f5634394287082be07380d03fa7ccd4d
```

Also verify from the public object:

* subjects of both published commits;
* `.ap` gitlink `041de310…`;
* schema head `0028`;
* `deploy/systemd/framenest.service` still has `TimeoutStopSec=30s`;
* no additional unexpected commit exists between the baseline and accepted candidate;
* public `main` has exactly the accepted tree.

Clean up only the exact disposable `mktemp` directory. Never use a broad or unresolved deletion target.

Finally repeat credential-free `git ls-remote` for both FrameNest and AP.

## Local preservation

After publication verify:

* accepted worktree remains at exact HEAD and tree;
* accepted worktree porcelain is empty;
* no upstream was configured;
* canonical owner worktree was not changed;
* Worker 4 worktree was not touched;
* no `.ap` checkout, `.venv`, test cache, bytecode, or other artifact was created in the accepted worktree.

Do not update the canonical owner checkout merely to make it match public `main`.

## Prohibited actions

Do not:

* run product tests already covered by acceptance;
* mutate source or tests;
* create a commit;
* amend or rewrite history;
* access the NUC;
* deploy or restart FrameNest;
* create a backup or snapshot;
* invoke real providers;
* access private media or credentials;
* mutate AP or Meta;
* declare production acceptance or logical-whole closure.

Publication PASS means only that the accepted Git object is now the exact public FrameNest `main`.

## PASS standard

Report `publication-PASS` only if:

* all start gates pass;
* public baseline was either the expected baseline or already the exact candidate;
* at most one ordinary non-force push occurred;
* public `main` resolves exactly to `148b6c20…`;
* disposable public-object verification proves the accepted tree and ancestry;
* AP pin and schema remain exact;
* local project worktrees remain preserved;
* no deployment or unrelated mutation occurred.

## Terminal report

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Then provide:

```text
Logical whole identity: framenest-in-process-lifecycle-runtime-contract
Worker session ordinal: 07
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED | FAIL
Phase-qualified result: publication-PASS | not-applicable
Result artifact or commit: 148b6c2012809944262399c1a166e85082606fbf
Result evidence: <exact push and public-readback evidence>
Logical-whole closure: not-closed
Report justification: publication-mutation | idempotent-publication-verification | blocker | failure
Authority expiry: all Worker 7 authority expired at this terminal report
```

Include:

1. fresh-session and authority confirmation;
2. initial AP and FrameNest public refs;
3. exact accepted commit, tree, ancestry, and subjects;
4. remote identity verification;
5. fast-forward proof;
6. exact push command, exit code, and porcelain result—or proof that no push was necessary;
7. final direct public readback;
8. disposable public-repository verification;
9. `.ap` gitlink, schema, and systemd evidence;
10. exact number and type of publication mutations;
11. accepted and canonical worktree preservation;
12. push, deployment, NUC, provider, AP, and Meta status;
13. final publication verdict;
14. residual publication risks;
15. resolved execution issues and near-misses.

Terminate after the report. Do not begin deployment or NUC acceptance.
