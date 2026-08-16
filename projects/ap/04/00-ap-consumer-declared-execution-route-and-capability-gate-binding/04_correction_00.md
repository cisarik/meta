# AP — Worker 04 accepted-state promotion for ADR-0018

You are one fresh Worker instance assigned to the AP `WORKER` role.

Perform one mechanical, bounded post-acceptance lifecycle promotion. The semantic implementation at `10ac2ed33e7246233dd813e508f7850465119efc` has passed fresh independent acceptance without a finding.

Do not reopen implementation, revise semantics, repeat acceptance, publish, push, or close the logical whole. Do not spawn subagents.

## 1. Authoritative coordinates

```text
Persistent role identity: WORKER
Role: WORKER
Logical whole identity: ap-consumer-declared-execution-route-and-capability-gate-binding
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Accepted-State Promotion Worker
Phase: implementation
Task identity: AP-CONSUMER-ROUTE-BINDING-ACCEPTED-STATE-04
Native planning mode: not-used
Implementation authority: accepted-state lifecycle promotion only
Semantic implementation authority: prohibited
Correction authority: prohibited
Evidence posture: non-independent lifecycle-mutation evidence
Recommended reasoning: Medium
Recommendation basis: mechanical three-path status convergence after independent acceptance; no semantic design remains open
Sub-agents/internal delegation: not-used
Development envelope activation: not-used
Working-copy topology: canonical-checkout
Topology rationale: exact accepted candidate is already present on its implementation branch
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none
Affected tests: none
Broad or full suite: not-used
Runtime or testbed: not-used
Independent re-acceptance: required-separate-fresh-worker
Cooperator delivery / trace destination: not-used
External trace disposition: not-used
```

## 2. Accepted evidence and purpose

Fresh Worker 03 independently accepted:

```text
Accepted semantic candidate: 10ac2ed33e7246233dd813e508f7850465119efc
Tree: b4c82c666f67d2468f133be110c8f6a1b4c95ea8
Parent: 95bd644829d48dcd188627f3e495e649df577eca
Subject: docs: bind Worker prompts to declared routes
Branch: feat/consumer-declared-route-binding
Acceptance result: acceptance-PASS
Acceptance finding: none
```

The accepted candidate deliberately retains:

```text
ADR-0018 status: Implementation candidate
```

Current public AP demonstrates the required lifecycle precedent:

```text
ADR-0017 implementation commit:
1cd2783838cb8cc9483792bc043010b0bbdef347
Status: Implementation candidate

ADR-0017 accepted-state promotion:
95bd644829d48dcd188627f3e495e649df577eca
Subject: docs: mark ADR-0017 accepted
Changed paths:
CHANGELOG.md
docs/adr/0017-cooperator-ergonomics-cost-proportional-execution.md
docs/adr/README.md
```

ADR-0017’s promotion changed only lifecycle wording:

* ADR status from `Implementation candidate` to `Accepted`;
* ADR index row and explanatory paragraph to accepted state;
* changelog from implementation-candidate wording to accepted historical rationale;
* no publication, consumer adoption, or closure claim embedded in the content.

Apply the same lifecycle shape to ADR-0018 without copying unrelated ADR-0017 prose.

## 3. Repository identity

```text
Physical root: /home/agile/Projects/ap
Canonical origin: https://github.com/cisarik/ap.git
Required starting HEAD: 10ac2ed33e7246233dd813e508f7850465119efc
Required branch: feat/consumer-declared-route-binding
Required public refs/heads/main: 95bd644829d48dcd188627f3e495e649df577eca
Expected starting tree: b4c82c666f67d2468f133be110c8f6a1b4c95ea8
Accepted candidate parent: 95bd644829d48dcd188627f3e495e649df577eca
```

The acceptance report also classified:

* tracked working tree clean;
* no relevant untracked path;
* no active Git operation or lock;
* stale `.git/REBASE_HEAD` present but not active;
* stale local `main` at `4e7bfa56…`, an ancestor of public main;
* both stale states untouched and non-blocking.

Revalidate all of this. Do not assume it.

## 4. Preflight

Before mutation, verify:

1. fresh Worker session and Native Plan Mode `not-used`;
2. exact repository root and canonical origin;
3. `HEAD == 10ac2ed33e7246233dd813e508f7850465119efc`;
4. tree `b4c82c666f67d2468f133be110c8f6a1b4c95ea8`;
5. branch exactly `feat/consumer-declared-route-binding`;
6. candidate parent exactly `95bd6448…`;
7. candidate subject exactly `docs: bind Worker prompts to declared routes`;
8. credential-free public `refs/heads/main == 95bd6448…`;
9. tracked working tree clean;
10. no overlapping untracked path;
11. no active merge, rebase, cherry-pick, revert, bisect, sequencer, or lock;
12. stale `.git/REBASE_HEAD`, if present, remains non-active under the acceptance classification;
13. local `main` remains untouched;
14. ADR-0018 currently says `Status: Implementation candidate`;
15. `docs/adr/README.md` and `CHANGELOG.md` consistently describe ADR-0018 as an implementation candidate and do not already claim acceptance.

If public main moved, the accepted candidate changed, the branch differs, owner work exists, or lifecycle surfaces are already inconsistent, stop `BLOCKED`.

Do not fetch, pull, reset, switch branches, repair `.git`, or modify stale markers.

## 5. Exact mutation allowlist

You may modify exactly these three existing paths:

```text
CHANGELOG.md
docs/adr/0018-consumer-declared-execution-route-binding.md
docs/adr/README.md
```

No other path may change, be staged, or be committed.

## 6. Required mutation

Make only the smallest status-promotion changes.

### ADR-0018

Change exactly:

```text
Status: Implementation candidate
```

to:

```text
Status: Accepted
```

Do not change the ADR’s decision, context, semantics, examples, consequences, compatibility, relationships, or rejected alternatives.

### ADR index

Update only ADR-0018’s lifecycle projections:

* table status becomes `Accepted`;
* remove wording that says no independent acceptance exists;
* retain the portable decision summary and `AP.md` semantic-owner statement;
* update any ADR-0018 explanatory paragraph from “implementation candidate” to “accepted decision”;
* do not claim public publication, consumer adoption, FrameNest ledger mutation, AP-pin adoption, or closure.

Follow the concise established ADR-0017 accepted-state style, adapted to ADR-0018’s actual content.

### Changelog

Change only ADR-0018’s lifecycle wording:

* replace implementation-candidate / awaiting-independent-acceptance wording with accepted historical-rationale wording;
* preserve that consumer adoption and logical-whole closure remain separate;
* do not claim publication before it occurs;
* do not rewrite the feature summary.

## 7. Forbidden changes

Do not modify:

* `AP.md`;
* `AP_ORCHESTRATOR.md`;
* `AP_WORKER.md`;
* `PROMPT_CONTRACTS.md`;
* `PROMPT_ENGINEERING_PATTERNS.md`;
* executable `ap`;
* `ap.project.conf`;
* any other ADR;
* any test, schema, managed block, integration guide, README, FAQ, glossary, INFOSEC, artifact lifecycle, or updating guide;
* FrameNest, Meta, ledger, pin, NUC, environment, credentials, workstation, or production.

Do not:

* amend or rewrite `10ac2ed…`;
* alter accepted semantics;
* add examples or explanatory sections;
* perform opportunistic cleanup;
* create another branch;
* push or publish;
* move `main`;
* delete or repair stale Git metadata;
* emit closure.

## 8. Verification

No test suite, runtime, Python, dependency, environment, or executable `ap` invocation is required or authorized.

Verify:

1. diff base is exact accepted candidate `10ac2ed…`;
2. changed paths are exactly the three allowlisted paths;
3. ADR-0018 semantic body is byte-equivalent except for its status line;
4. ADR index changes only ADR-0018 lifecycle wording;
5. changelog changes only ADR-0018 lifecycle wording;
6. all three surfaces say `Accepted` consistently;
7. none claims publication, consumer adoption, ledger implementation, pin adoption, or closure;
8. original accepted eight-path semantic diff remains otherwise unchanged;
9. `git diff --check` exits 0;
10. full diff contains no unrelated reflow or cleanup;
11. no mode, symlink, binary, schema, test, config, or executable change;
12. stale `.git/REBASE_HEAD` and local `main` remain untouched.

## 9. Git authority

After verification passes, stage only:

```text
CHANGELOG.md
docs/adr/0018-consumer-declared-execution-route-binding.md
docs/adr/README.md
```

Create exactly one normal local commit with subject:

```text
docs: mark ADR-0018 accepted
```

Do not amend, bypass hooks, create a second commit, push, tag, fetch, merge, rebase, reset, restore, clean, stash, or change branches.

If the commit fails, preserve the worktree and report the first causal failure. Do not improvise.

## 10. Post-commit invariant

For `PASS`, verify:

```text
Promotion parent: 10ac2ed33e7246233dd813e508f7850465119efc
Promotion subject: docs: mark ADR-0018 accepted
Branch: feat/consumer-declared-route-binding
Stack length from public baseline 95bd6448…: exactly 2 commits
Changed paths in promotion commit: exactly 3
Public refs/heads/main: still 95bd644829d48dcd188627f3e495e649df577eca
Push: none
Logical-whole closure: not-closed
```

Record the full promotion commit and tree identities.

The promoted tip is a new candidate requiring a fresh scoped independent acceptance before publication. Worker 03’s acceptance of the semantic commit remains valid evidence but does not independently accept this new lifecycle commit.

## 11. Hard stops

Stop without improvisation if:

* candidate or public identity differs;
* the working tree is not clean;
* an active Git operation exists;
* the three lifecycle surfaces do not begin consistently at implementation-candidate state;
* any semantic change is needed;
* any fourth path is needed;
* publication wording cannot be avoided;
* `10ac2ed…` would need amendment;
* commit ancestry would not be exactly two commits from `95bd6448…`;
* push, Meta write, FrameNest mutation, ledger transition, pin adoption, or closure would be required.

## 12. Terminal report

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Then include:

```text
Logical whole identity: ap-consumer-declared-execution-route-and-capability-gate-binding
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS | not-applicable
Result artifact or commit: <promotion commit SHA or none>
Logical-whole closure: not-closed
Report justification: new-mutation | new-material-risk
Authority expiry: all Worker 04 exchange 01 accepted-state promotion authority expires at this terminal report
```

Report:

* exact preflight identities;
* promotion commit, tree, parent, subject, branch, and stack length;
* exact three changed paths;
* exact lifecycle wording changed in each;
* proof that no semantic body changed;
* `git diff --check` and focused verification exit statuses;
* public ref after commit;
* confirmation of no push;
* stale `REBASE_HEAD` and stale local `main` disposition;
* deviations, risks, and near-misses;
* confirmation that no other repository or external state changed;
* smallest next step: fresh scoped independent acceptance of the exact two-commit tip.

Do not emit `CLOSED: PASS`. Stop immediately after the terminal report.
