# AP — Worker 05 scoped independent re-acceptance of accepted-state promotion

You are one fresh Worker instance assigned to the AP `WORKER` role.

Perform one read-only, scoped, independent re-acceptance of the exact two-commit AP candidate ending at `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.

Do not implement, repair, edit, commit, push, publish, write Meta, mutate a consumer, or close the logical whole. Do not spawn subagents.

## 1. Authoritative coordinates

```text
Persistent role identity: WORKER
Role: WORKER
Logical whole identity: ap-consumer-declared-execution-route-and-capability-gate-binding
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Re-Audit
Phase: acceptance
Task identity: AP-CONSUMER-ROUTE-BINDING-REACCEPT-05
Native planning mode: not-used
Acceptance mode: scoped independent re-acceptance
Implementation authority: prohibited
Correction authority: prohibited
Publication authority: prohibited
Logical-whole closure authority: prohibited
Evidence posture: independent acceptance evidence
Recommended reasoning: Medium
Recommendation basis: bounded three-path lifecycle promotion over an already independently accepted semantic commit
Sub-agents/internal delegation: not-used
Development envelope activation: not-used
Working-copy topology: canonical-checkout
Topology rationale: immutable candidate stack is already present in the actual AP owner checkout
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none
Affected tests: none
Broad or full suite: not-used
Runtime or testbed: not-used
Cooperator delivery / trace destination: not-used
External trace disposition: not-used
```

## 2. Candidate stack

Canonical repository:

```text
Physical root: /home/agile/Projects/ap
Origin: https://github.com/cisarik/ap.git
Required branch: feat/consumer-declared-route-binding
```

Public baseline:

```text
Commit: 95bd644829d48dcd188627f3e495e649df577eca
Tree: 9b895a1eaa95293f14964a756fa9f873e8c48a80
Subject: docs: mark ADR-0017 accepted
Expected public refs/heads/main: 95bd644829d48dcd188627f3e495e649df577eca
```

Independently accepted semantic commit:

```text
Commit: 10ac2ed33e7246233dd813e508f7850465119efc
Tree: b4c82c666f67d2468f133be110c8f6a1b4c95ea8
Parent: 95bd644829d48dcd188627f3e495e649df577eca
Subject: docs: bind Worker prompts to declared routes
Prior acceptance: Worker 03 acceptance-PASS
```

Accepted-state promotion under re-acceptance:

```text
Commit: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Tree: 43bc12b966133d76972ccf3884d80dceedde013b
Parent: 10ac2ed33e7246233dd813e508f7850465119efc
Subject: docs: mark ADR-0018 accepted
Expected stack length from public baseline: exactly 2 commits
```

An Orchestrator credential-free readback immediately before this prompt confirmed:

```text
refs/heads/main = 95bd644829d48dcd188627f3e495e649df577eca
```

Revalidate it independently.

## 3. Independence gate

Before substantive inspection, confirm:

* genuinely fresh Worker 05 session;
* no participation in Worker 01 planning, Worker 02 implementation, Worker 03 acceptance, or Worker 04 promotion;
* no reused authority;
* Native Plan Mode disabled or absent;
* no internal delegation;
* no prior mutation in this session;
* no implementation, repair, or publication intent.

Treat all previous reports as claims. Establish the required facts directly from repository and public Git evidence.

Stop `BLOCKED` if independence is compromised.

## 4. Read-only authority

You may:

* inspect repository identity, status, refs, objects, trees, blobs, history, ancestry, and diffs;
* inspect relevant documentation;
* use credential-free `git ls-remote` for the canonical AP public main;
* run `git diff --check` against immutable commit ranges;
* compare file blobs and relevant sections;
* return one terminal acceptance report.

You may not:

* edit, format, create, delete, rename, stage, commit, amend, push, fetch, pull, merge, rebase, reset, restore, clean, stash, switch branches, create worktrees, tags, or refs;
* modify stale Git metadata;
* run tests, Python, dependency tools, `ap`, project operations, formatters, or generators;
* write Meta;
* mutate FrameNest, its ledger, or AP pin;
* contact NUC, credentials, environment, production, or provider services;
* correct a finding;
* emit closure.

## 5. Repository identity gate

Directly verify:

1. physical root `/home/agile/Projects/ap`;
2. canonical origin fetch/push URL;
3. `HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`;
4. tree `43bc12b966133d76972ccf3884d80dceedde013b`;
5. parent `10ac2ed33e7246233dd813e508f7850465119efc`;
6. subject `docs: mark ADR-0018 accepted`;
7. branch `feat/consumer-declared-route-binding`;
8. promotion parent has exact tree, parent, and subject stated in §2;
9. public baseline has exact identity stated in §2;
10. ancestry is exactly:
    `95bd6448…` → `10ac2ed…` → `9c5cc44…`;
11. `rev-list --count 95bd6448…..9c5cc44…` equals `2`;
12. tracked working tree clean;
13. no relevant untracked path;
14. no active merge, rebase, cherry-pick, revert, bisect, sequencer, or lock;
15. credential-free public `refs/heads/main == 95bd6448…`;
16. candidate is not already on a public remote ref;
17. root `AGENTS.md` presence or absence is recorded.

### Pre-existing local conditions

Classify directly:

* stale `.git/REBASE_HEAD`, if still present;
* absence of active rebase directories and status indicators;
* stale local `main`, if still at `4e7bfa56…`;
* whether either condition affected the immutable candidate.

Do not remove or repair either condition.

Stop on an identity mismatch, active mutation, changed public baseline, or unexplained owner work.

## 6. Exact scope matrix

### 6.1 Promotion commit against accepted semantic parent

Verify:

```text
Range: 10ac2ed33e7246233dd813e508f7850465119efc..9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

Changed paths must be exactly:

```text
CHANGELOG.md
docs/adr/0018-consumer-declared-execution-route-binding.md
docs/adr/README.md
```

No other path, mode, symlink, binary, executable, schema, test, CI, configuration, or managed-block change is permitted.

### 6.2 Original semantic commit against public baseline

Verify:

```text
Range: 95bd644829d48dcd188627f3e495e649df577eca..10ac2ed33e7246233dd813e508f7850465119efc
```

Changed paths must be exactly:

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

### 6.3 Complete stack against public baseline

Verify:

```text
Range: 95bd644829d48dcd188627f3e495e649df577eca..9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

The complete stack must still change exactly the same eight documentation paths and nothing else.

## 7. Promotion acceptance controls

Independently verify all controls.

### ADR-0018

* status is exactly `Accepted`;
* between `10ac2ed…` and `9c5cc44…`, only the status line changed;
* title, date, context, decision, semantic ownership, compatibility, consequences, limitations, relationships, and rejected alternatives are byte-equivalent;
* no publication, consumer adoption, ledger implementation, pin adoption, or closure claim was added.

### ADR index

* ADR-0018 table status is `Accepted`;
* explanatory paragraph says it records an accepted decision;
* independent-acceptance-pending wording was removed;
* portable decision summary remains intact;
* it does not claim publication, consumer adoption, pin adoption, or closure;
* no other ADR row or explanation changed.

### Changelog

* ADR-0018 is described as accepted historical rationale;
* implementation-candidate and pending-independent-acceptance wording was removed;
* consumer adoption and logical-whole closure remain separate;
* no publication claim was added;
* no unrelated changelog entry changed.

### Semantic immutability

Confirm these five semantic/projection files have identical blobs at `10ac2ed…` and `9c5cc44…`:

```text
AP.md
AP_ORCHESTRATOR.md
AP_WORKER.md
PROMPT_CONTRACTS.md
PROMPT_ENGINEERING_PATTERNS.md
```

No semantic re-acceptance finding may be waived merely because Worker 03 previously passed the first commit.

## 8. Retained semantic controls

Perform a scoped direct review sufficient to confirm the promoted stack still expresses the previously accepted invariant:

1. consumer owns exact operations, tooling, capability gates, credentials, and local values;
2. binding applies only to an applicable and usable route;
3. Orchestrator resolves baseline, project rules, route, and usability before prompt issuance;
4. usable route becomes canonical;
5. silent equivalent-looking ambient parallel route is prohibited;
6. bounded deviation uses existing task-specific fields;
7. ambient state remains convenience, not authority or guaranteed capability;
8. failure is classified before one focused declared-route reproduction;
9. no-route consumers receive exact project-owned guidance rather than AP-invented tooling;
10. Development Envelope Activation, `ap.project.conf`, and natural-language capability gates remain distinct;
11. historical pins are not reinterpreted;
12. `AP.md` remains the sole live semantic owner;
13. executable `ap` is unchanged and no prompt-validation enforcement is claimed.

This is not a second repository-wide audit. Focus on the exact accepted invariant and the promotion’s non-interference.

## 9. Verification

Required read-only checks include:

* exact commit/tree/parent/subject evidence;
* ancestry and stack count;
* exact changed-path sets for all three ranges;
* blob equality for semantic files across the promotion;
* ADR body equality except status;
* full promotion diff inspection;
* complete stack diff inspection for forbidden surfaces;
* `git diff --check` for both commits and the complete stack;
* repository status and active-operation inspection;
* credential-free public main readback;
* direct semantic spot-check from immutable candidate objects.

Every required command must exit 0 for `PASS`. A non-zero required gate forbids `PASS`.

Do not repair a failure or rerun an unchanged failing gate repeatedly.

## 10. Acceptance decision

Return `PASS` / `acceptance-PASS` only if:

* independence holds;
* every identity and ancestry gate passes;
* promotion changes exactly three lifecycle paths;
* ADR body and semantic files remain immutable;
* accepted-state wording is internally consistent;
* no premature publication/adoption/closure claim exists;
* original invariant remains intact;
* complete stack changes exactly eight documentation paths;
* public main remains the exact baseline;
* repository and external state remain untouched.

Return `PARTIAL` or `BLOCKED` with one concrete finding if any requirement fails. Do not implement a correction.

## 11. Terminal report

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Then include:

```text
Logical whole identity: ap-consumer-declared-execution-route-and-capability-gate-binding
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: acceptance-PASS | not-applicable
Result artifact or commit: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Logical-whole closure: not-closed
Report justification: final-acceptance | new-material-risk
Authority expiry: all Worker 05 exchange 01 scoped re-acceptance authority expires at this terminal report
```

Report:

1. independence gate;
2. exact repository/public identities;
3. complete two-commit ancestry;
4. three changed-path matrices;
5. lifecycle promotion acceptance controls;
6. semantic blob and ADR-body immutability;
7. retained semantic-control result;
8. required checks and exit statuses;
9. stale local-state classifications;
10. acceptance decision;
11. deviations, findings, missing evidence, and near-misses;
12. confirmation that no mutation, push, publication, Meta write, consumer change, ledger/pin change, deployment, or closure occurred;
13. smallest next step: separately authorized publication of exact tip `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.

Do not emit `CLOSED: PASS`. Stop immediately after the report.
