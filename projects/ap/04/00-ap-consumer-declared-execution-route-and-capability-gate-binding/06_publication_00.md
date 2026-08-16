# AP — Worker 06 publication of accepted route-binding stack

You are one fresh Worker instance assigned to the AP `WORKER` role.

Publish the exact independently accepted two-commit AP stack ending at `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` to canonical public `refs/heads/main`.

This prompt grants authority for exactly one ordinary non-force push after all publication preconditions pass. It grants no source mutation, new commit, correction, tag, Meta write, consumer mutation, AP-pin adoption, deployment, production action, or logical-whole closure.

Do not spawn subagents.

## 1. Authoritative coordinates

```text
Persistent role identity: WORKER
Role: WORKER
Logical whole identity: ap-consumer-declared-execution-route-and-capability-gate-binding
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Publication Worker
Phase: publication
Task identity: AP-CONSUMER-ROUTE-BINDING-PUBLISH-06
Native planning mode: not-used
Publication authority: exact accepted tip to canonical refs/heads/main
Implementation authority: prohibited
Correction authority: prohibited
Acceptance authority: prohibited
Logical-whole closure authority: prohibited
Evidence posture: publication evidence
Recommended reasoning: Medium
Recommendation basis: mechanical fast-forward publication of an exact independently accepted two-commit stack
Sub-agents/internal delegation: not-used
Development envelope activation: not-used
Working-copy topology: canonical-checkout
Topology rationale: accepted immutable stack is present on the implementation branch
Validation ladder: selected
Inspection and provenance: required
Broad or full suite: not-used
Runtime or testbed: not-used
Independent acceptance: already-satisfied
Cooperator delivery / trace destination: not-used
External trace disposition: not-used
```

## 2. Exact accepted stack

Canonical repository:

```text
Physical root: /home/agile/Projects/ap
Canonical origin: https://github.com/cisarik/ap.git
Local branch: feat/consumer-declared-route-binding
```

Expected public baseline:

```text
Commit: 95bd644829d48dcd188627f3e495e649df577eca
Tree: 9b895a1eaa95293f14964a756fa9f873e8c48a80
Subject: docs: mark ADR-0017 accepted
Public ref: refs/heads/main
```

Accepted semantic commit:

```text
Commit: 10ac2ed33e7246233dd813e508f7850465119efc
Tree: b4c82c666f67d2468f133be110c8f6a1b4c95ea8
Parent: 95bd644829d48dcd188627f3e495e649df577eca
Subject: docs: bind Worker prompts to declared routes
Acceptance: Worker 03 acceptance-PASS
```

Accepted lifecycle-promotion tip:

```text
Commit: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Tree: 43bc12b966133d76972ccf3884d80dceedde013b
Parent: 10ac2ed33e7246233dd813e508f7850465119efc
Subject: docs: mark ADR-0018 accepted
Scoped re-acceptance: Worker 05 acceptance-PASS
```

Required stack:

```text
95bd644829d48dcd188627f3e495e649df577eca
  -> 10ac2ed33e7246233dd813e508f7850465119efc
  -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

An Orchestrator credential-free readback immediately before issuing this prompt confirmed:

```text
refs/heads/main = 95bd644829d48dcd188627f3e495e649df577eca
```

Revalidate this directly.

## 3. Independence and mode gate

Before any push, verify:

* genuinely fresh Worker 06 session;
* Native Plan Mode disabled or absent;
* no participation in implementation or acceptance;
* no reused Worker authority;
* no internal delegation;
* no source mutation or Git write before this prompt;
* exact publication coordinates received.

Stop if the session or Native Plan Mode state is contradictory.

## 4. Publication preflight

Using read-only inspection, directly verify all conditions:

1. repository root is `/home/agile/Projects/ap`;
2. origin fetch and push URLs canonicalize to `https://github.com/cisarik/ap.git`;
3. `HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`;
4. tree is `43bc12b966133d76972ccf3884d80dceedde013b`;
5. parent is `10ac2ed33e7246233dd813e508f7850465119efc`;
6. subject is `docs: mark ADR-0018 accepted`;
7. branch is `feat/consumer-declared-route-binding`;
8. semantic parent and public baseline match §2 exactly;
9. ancestry is exactly the two-commit fast-forward stack in §2;
10. `rev-list --count 95bd6448…..9c5cc44…` equals `2`;
11. tracked working tree is clean;
12. no relevant untracked path exists;
13. no active merge, rebase, cherry-pick, revert, bisect, sequencer, or Git lock;
14. stale `.git/REBASE_HEAD`, if present, remains inactive and untouched;
15. stale local `main`, if still `4e7bfa56…`, remains untouched;
16. credential-free `git ls-remote` reports public `refs/heads/main == 95bd6448…`;
17. no public remote ref already contains the candidate;
18. candidate stack changes exactly the accepted eight documentation paths;
19. promotion commit changes exactly the accepted three lifecycle paths;
20. no mode, symlink, binary, executable, schema, test, CI, config, managed-block, submodule, or consumer change exists;
21. ADR-0018 status at the tip is `Accepted`;
22. no candidate file claims consumer adoption, ledger implementation, pin adoption, publication already completed, or logical-whole closure;
23. no accepted object changed after Worker 05 re-acceptance.

Every required preflight gate must pass. Do not treat a previous report as proof.

## 5. Exact changed-path controls

Complete stack against public baseline must change exactly:

```text
AP.md
AP_ORCHESTRATOR.md
AP_WORKER.md
PROMPT_CONTRACTS.md
PROMPT_ENGINEERING_PATTERNS.md
CHANGELOG.md
docs/adr/0018-consumer-declared-execution-route-binding.md
docs/adr/README.md
```

Promotion commit against `10ac2ed…` must change exactly:

```text
CHANGELOG.md
docs/adr/0018-consumer-declared-execution-route-binding.md
docs/adr/README.md
```

Run `git diff --check` against both commits and the complete stack. All must exit 0.

Do not rerun tests, Python, `ap`, dependencies, formatters, or runtime checks. Their behavior is unchanged and publication adds no source mutation.

## 6. Exact publication authority

If and only if every preflight gate passes, perform exactly one ordinary non-force push:

```text
git push origin 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656:refs/heads/main
```

This exact push is authorized once.

Prohibited:

* force, `--force`, `--force-with-lease`, deletion, mirror, atomic multi-ref, tag, branch publication, or wildcard refspec;
* push of local branch name without the exact SHA;
* a second push attempt after a non-zero or ambiguous result;
* fetch, pull, merge, rebase, reset, restore, clean, stash, switch, checkout, branch creation/deletion, tag creation, amend, or new commit;
* modification of local `main`;
* modification or deletion of stale Git metadata;
* credential inspection or output;
* source edits;
* Meta, FrameNest, ledger, pin, NUC, environment, credential, or production mutation.

If authentication is unavailable, the remote moved, push is rejected, output is ambiguous, or the command exits non-zero, stop `BLOCKED`. Do not retry or repair.

## 7. Post-push public verification

After an exit-0 push, independently run credential-free public readback:

```text
git ls-remote https://github.com/cisarik/ap.git refs/heads/main
```

For `publication-PASS`, it must return exactly:

```text
9c5cc44f8b6c92dd56ad2427d13223d7d59c5656	refs/heads/main
```

Then verify locally, without mutation:

* `HEAD` remains `9c5cc44…`;
* tree remains `43bc12b9…`;
* parent and subject remain exact;
* branch remains `feat/consumer-declared-route-binding`;
* working tree remains clean;
* accepted stack remains exactly two commits from `95bd6448…`;
* no second public ref was created;
* no tag was created;
* no source or commit changed;
* local `main` remains untouched;
* stale `.git/REBASE_HEAD` remains untouched;
* no NUC, Meta, FrameNest, ledger, pin, environment, credentials, or production state changed.

Do not move local `main` merely to match the new public ref. That requires separate authority if ever desired.

## 8. Result classification

Return `PASS` / `publication-PASS` only if:

* all preflight gates pass;
* the exact one non-force push exits 0;
* public readback equals exact accepted tip;
* local accepted objects remain unchanged;
* no unauthorized ref or state changed.

Return `BLOCKED` if a precondition fails before push or the exact push/readback fails.

Return `PARTIAL` only for a genuinely ambiguous changed-external-state outcome that cannot be classified safely. Do not retry.

Publication does not close the logical whole. Only the ORCHESTRATOR may close after reconciling the complete evidence chain and confirming no required ledger or consumer mutation belongs inside this AP whole.

## 9. Terminal report

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Then include:

```text
Logical whole identity: ap-consumer-declared-execution-route-and-capability-gate-binding
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: publication-PASS | not-applicable
Result artifact or commit: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Logical-whole closure: not-closed
Report justification: changed-external-state
Authority expiry: all Worker 06 exchange 01 publication authority expires at this terminal report
```

Report:

1. independence and mode gate;
2. exact preflight repository/public identities;
3. exact two-commit ancestry;
4. changed-path and diff-check results;
5. exact push command/refspec;
6. push exit status and concise transport result;
7. confirmation that no force was used;
8. credential-free post-push public readback;
9. post-push local repository state;
10. public refs/tags result;
11. stale local-main and stale-marker disposition;
12. deviations, risks, ambiguity, and near-misses;
13. confirmation that no source edit, new commit, Meta write, consumer/ledger/pin mutation, NUC action, deployment, credential exposure, or closure occurred;
14. smallest next step: ORCHESTRATOR evidence reconciliation and logical-whole closure.

Do not emit `CLOSED: PASS`. Stop immediately after the terminal report.
