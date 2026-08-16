# AP — Worker 01 implementation planning: consumer-declared execution-route and capability-gate binding

You are one fresh Worker instance assigned to the AP `WORKER` role.

Native Plan Mode is mandatory for this exchange. This is a read-only implementation-planning task. It grants no implementation, repository mutation, Git-write, publication, consumer-adoption, ledger-write, Meta-write, deployment, credential, host, or production authority.

Do not spawn subagents or delegate internally. Work as the one accountable Worker.

## 1. Authoritative coordinates

```text
Persistent role identity: WORKER
Role: WORKER
Logical whole identity: ap-consumer-declared-execution-route-and-capability-gate-binding
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: repository-grounded universal-protocol implementation planner
Phase: Planning
Task identity: AP-CONSUMER-ROUTE-BINDING-PLAN-01
Native planning mode: required
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: new complete ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
Evidence posture: non-independent planning evidence
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
Recommended reasoning: High
Recommendation basis: cross-document universal-protocol semantics spanning the canonical owner, operational and structural projections, consumer integration, executable boundaries, and backward compatibility
Escalation or downgrade gate: no in-session escalation; unresolved semantic-owner or repository-state contradiction stops for ORCHESTRATOR decision
Sub-agents/internal delegation: not-used
Development envelope activation: not-used
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none required during planning
Affected tests: planning must determine
New causal regression: consumer-declared route can be bypassed by an equivalent-looking ambient route in an authoritative prompt
Broad or full suite: not-used
Runtime or testbed: not-used
Independent acceptance: required-separate-fresh-worker after any later implementation
Repeated-gate or reasoning-loop stop: configured
Broad gate: not-used during planning
Narrow before re-broad: required
Unchanged hypothesis, repository state, and evidence: not-progress
Escalate only on: named missing evidence that changes the semantic boundary
Cost cannot falsify evidence: yes
Cooperator delivery / trace destination: not-used
External trace disposition: not-used
Working-copy topology: canonical-checkout
Topology rationale: planning must inspect the actual AP owner checkout and identify unpublished or overlapping owner work; no worktree or contained clone is necessary for read-only planning
```

The COOPERATOR has selected this logical whole for planning only. Selection does not pre-accept an AP defect, a particular implementation shape, or any repository change.

## 2. Objective

Produce one decision-complete, repository-grounded implementation plan for the smallest portable resolution of this candidate gap:

> When a consuming project has an applicable declared execution operation or capability gate, the authoritative Worker prompt may not bind the Worker strongly enough to that route or reject a contradictory equivalent-looking ambient route.

Determine first whether current AP needs any change at all.

A valid outcome may be:

* an AP change is justified;
* current public or unpublished AP already owns the complete invariant and no AP change is needed;
* the observation is valid but should be parked or rejected because a universal change would be duplicative, disproportionate, or consumer-specific;
* planning is blocked by repository state, unavailable evidence, or an ownership contradiction.

Do not plan toward an implementation merely because the logical-whole name exists.

## 3. Repositories and expected public anchors

Resolve physical repository roots independently. Expected owner paths are:

```text
AP source repository: /home/agile/Projects/ap
FrameNest consumer repository: /home/agile/Projects/framenest
Selective AP trace/archive: /home/agile/meta
```

Canonical repositories:

```text
https://github.com/cisarik/ap.git
https://github.com/cisarik/framenest.git
https://github.com/cisarik/meta.git
```

The following anchors were independently verified by the Orchestrator on 2026-08-16, but they are evidence to revalidate rather than authority to assume:

```text
AP public main: 95bd644829d48dcd188627f3e495e649df577eca
AP public tree: 9b895a1eaa95293f14964a756fa9f873e8c48a80
AP public subject: docs: mark ADR-0017 accepted

FrameNest public main: fc355d6e21d2f2781e0166906b453fa3fa91bdb7
FrameNest public tree: 00704b16a308ace5e349db1582691876e26dd613
FrameNest public parent: 5abb2adfcd1d5f3391df9c3044b4b81ac1aac923
FrameNest public subject: fix: bind Cursor Workers to declared AP exec and capability routes
FrameNest governing AP gitlink: 17b7e085139e9bcbb0e4953d26aef9b6687d541c

Meta public main: d316b675f761e3cad15a005140a5365dc36b9213
```

Public AP `95bd6448…` is two commits ahead of the FrameNest pin:

```text
1cd2783838cb8cc9483792bc043010b0bbdef347
95bd644829d48dcd188627f3e495e649df577eca
```

Those commits introduced and accepted ADR-0017 cost-proportional Worker grants, including optional Development Envelope Activation semantics. Determine how that newer public work affects the candidate gap.

A newer public AP revision does not govern FrameNest retroactively. FrameNest continues to be interpreted under its exact `17b7e085…` pin until a separately authorized adoption task changes the gitlink.

## 4. Delivery and native planning precondition

Before substantive work, directly confirm that Native Plan Mode is active.

If Native Plan Mode is absent, disabled, contradictory, or not observably available:

1. do not modify anything;
2. do not simulate Plan Mode;
3. stop and return `BLOCKED`;
4. identify that the Orchestrator must reissue a complete plan-only prompt with `Native planning mode: not-used`.

An accepted native planner artifact does not authorize implementation. Submit the standard terminal Worker report separately in this exchange.

## 5. Read-only repository restoration gate

Begin with the actual AP checkout. Do not trust the currently open editor, current directory, remembered SHA, branch name, retained chat context, or prior report.

For AP, FrameNest, and the selective Meta checkout, resolve and report:

* physical repository root;
* canonicalized origin fetch and push URLs;
* local `HEAD`;
* current branch or detached state;
* upstream relationship;
* concise tracked and untracked status without exposing unrelated private filenames;
* active merge, rebase, cherry-pick, revert, bisect, sequencer, or lock state;
* relevant worktree topology;
* whether local state equals public `main`, is ahead, behind, divergent, detached, an unpublished candidate, or unrelated owner work;
* direct credential-free public `refs/heads/main` identity.

Use read-only Git and filesystem inspection only. Prefer `GIT_OPTIONAL_LOCKS=0` where appropriate.

Do not run:

* `git fetch`, `pull`, `switch`, `checkout`, `reset`, `restore`, `clean`, `stash`, `rebase`, `merge`, `cherry-pick`, `commit`, `push`, `worktree add`, branch creation, tag creation, or config mutation;
* any command that edits the index, refs, worktree, submodule, or remote;
* destructive, force, or history-rewriting Git operations.

The public AP repository at `95bd6448…` had no root `AGENTS.md`. If the actual local AP checkout contains one, read it before deeper inspection and determine whether it is public, committed-but-unpublished, or uncommitted owner work. If it does not exist, explicitly record its absence and follow the repository’s current declared authority model, in which `AP.md` is the sole live normative semantic owner.

Read FrameNest root `AGENTS.md` before discovering its ledger. Do not guess or scan for ledger filenames.

### Hard repository stop

Stop with `BLOCKED` before producing an implementation plan if:

* an expected repository root is missing or resolves to the wrong repository;
* a canonical remote identity conflicts;
* an active Git mutation or unexplained lock exists;
* dirty or unpublished owner work overlaps the candidate AP owners or changes the logical-whole boundary;
* current public AP has changed and the new object cannot be inspected without a Git write;
* FrameNest’s ledger declaration or storage is missing or malformed;
* required selective Meta evidence is unavailable;
* continuing would require modifying, fetching, installing, generating, or exposing private data.

Preserve all owner work. Do not enumerate unrelated untracked filenames in the report.

## 6. Read-only authority

You may:

* inspect repository files and Git objects already present;
* use read-only Git identity, history, diff, tree, ancestry, and status commands;
* use credential-free `git ls-remote` for the three exact canonical public refs;
* use text and path search such as `rg`, `sed`, and read-only file listing;
* compare the FrameNest pin with current public AP;
* inspect the exact declared ledger entry;
* inspect only the named Meta chain;
* reason and produce the terminal planning report in chat.

You may not:

* edit, create, delete, rename, format, generate, or chmod files;
* save the plan inside AP, FrameNest, Meta, or another repository;
* change the FrameNest ledger entry;
* execute an implementation, correction, acceptance, publication, deployment, migration, or closure;
* run tests, linters, formatters, AP project operations, dependency tools, environment repair, or runtime probes;
* install or update dependencies;
* create a virtual environment or modify an existing one;
* use `python`, Poetry, uv, pip, or environment-manager commands;
* access NUC, SSH, sudo, GPG-agent, credentials, secrets, private keys, sockets, production, provider accounts, or external services other than the three public Git ref readbacks;
* write Meta;
* update the FrameNest AP pin;
* spawn subagents;
* use GUI applications, Cursor commands, browser automation, or AppImages;
* claim closure.

## 7. Mandatory evidence and reading

### 7.1 Current AP checkout

Read any applicable root `AGENTS.md` first. Then inspect at least:

* `AP.md`

  * canonical semantic-owner map;
  * RF-06;
  * RF-15;
  * RF-16;
  * prompt synthesis/readiness;
  * Compact Communication;
  * stopping conditions and anti-patterns;
* `AP_ORCHESTRATOR.md`

  * restoration;
  * model/surface routing;
  * repository, capability, permission, and side-effect gates;
  * prompt construction;
  * ledger triage;
  * stop rules;
* `AP_WORKER.md`

  * repository gate;
  * validation;
  * capability and authenticated-readback boundaries;
  * stopping and reporting;
* `PROMPT_CONTRACTS.md`

  * Common Worker Task Fields;
  * activated surface annexes;
  * capability-related records;
  * Validation Ladder;
  * Development Envelope Activation Record;
  * report and planning structures;
* `INTEGRATION.md`

  * managed integration boundary;
  * optional development-envelope declaration;
  * universal versus project-specific ownership;
* `PROMPT_ENGINEERING_PATTERNS.md`

  * P08 Stable Tool, Failure, and Cleanup Contract;
  * relevant capability/security patterns;
  * cost-proportional fixtures and negative examples;
* `docs/adr/0009-capability-aware-worker-routing-and-execution-gates.md`;
* `docs/adr/0012-baseline-bound-project-execution.md`;
* `docs/adr/0013-semantic-ownership-and-convergence.md`;
* `docs/adr/0015-monolithic-ap-test-suite-retirement.md`;
* `docs/adr/0017-cooperator-ergonomics-cost-proportional-execution.md`;
* `docs/adr/README.md`;
* current relevant `CHANGELOG.md` entries;
* executable `ap` as source;
* `ap.project.conf`;
* repository file inventory sufficient to identify every current executable validator or test surface.

Inspect README, FAQ, glossary, artifact lifecycle, INFOSEC, updating guidance, or other projections only when they contain a relevant projection or the proposed change would make them inconsistent. Do not turn this into a repository-wide prose rewrite.

### 7.2 Governing FrameNest pin and consumer evidence

Under FrameNest’s pinned `.ap` at `17b7e085…`, selectively inspect the same relevant normative and projection areas needed to distinguish:

* what FrameNest was actually governed by when the field failure occurred;
* what current public AP later added through ADR-0017;
* what remains unresolved even at current public AP.

From FrameNest inspect only the consumer-owned evidence necessary for this observation:

* root `AGENTS.md`;
* declared `ap.project.conf`;
* `docs/AP_UPGRADE_OBSERVATIONS.md`;
* `docs/WORKER_EXECUTION_CONTRACT.md`;
* `docs/OPERATOR_NETWORK.md`;
* `scripts/operator/network/README.md`;
* `scripts/operator/network/framenest_nuc_worker_gate.fish`;
* `tests/contract/test_ap_project_contract.py`;
* `tests/contract/test_worker_execution_contract.py`;
* only relevant portions of `tests/contract/test_operator_network_scripts.py`.

Do not run those tests or contact the NUC.

### 7.3 Exact ledger observation

Discover the ledger only from FrameNest root `AGENTS.md`. Revalidate exactly:

```text
Entry: consumer-declared-execution-and-capability-route-binding
Entry state: untriaged
Entry authority: non-authorizing
```

Validate all stored fields, target identity, activation snapshot, entry uniqueness, current public-safe evidence, and whether later AP public work affects its disposition.

Do not create a duplicate. Do not change its state.

### 7.4 Selective Meta evidence

Inspect only:

```text
/home/agile/meta/projects/framenest/03/01-framenest-cursor-worker-execution-boundary-convergence/01_implementation_00.md
/home/agile/meta/projects/framenest/03/01-framenest-cursor-worker-execution-boundary-convergence/01_report_00.md
/home/agile/meta/projects/framenest/03/01-framenest-cursor-worker-execution-boundary-convergence/02_acceptance_00.md
/home/agile/meta/projects/framenest/03/01-framenest-cursor-worker-execution-boundary-convergence/02_report_00.md
/home/agile/meta/projects/framenest/03/01-framenest-cursor-worker-execution-boundary-convergence/03_publication_00.md
/home/agile/meta/projects/framenest/03/01-framenest-cursor-worker-execution-boundary-convergence/03_report_00.md
/home/agile/meta/projects/framenest/03/01-framenest-cursor-worker-execution-boundary-convergence/04_closure_00.md
```

Treat Meta as historical evidence, not live semantic authority. Do not inspect the entire archive and do not write it.

## 8. Repository-grounded questions

Answer each from current evidence:

1. Does current public AP already make an applicable consumer-declared execution operation or capability gate canonical for the current Worker prompt?
2. Does AP require the Orchestrator to resolve the applicable operation/gate before issuing the prompt, or merely permit referencing it?
3. Can Development Envelope Activation legally remain `not-used` when a usable machine-readable route exists?
4. Is the optional development envelope the same concept as `ap.project.conf`, or are they separate declarations with different ownership and enforcement?
5. Can Common Worker Task Fields or allowed-command examples authorize a raw interpreter, shell, SSH, or reconstructed ambient route beside a declared operation/gate?
6. Is there a current rule that detects or rejects that contradiction?
7. Does `ap` enforce prompt construction, or only validate and execute a declared operation after the Worker actually invokes `ap exec`?
8. Can a copied raw command replace a machine-verifiable project operation without an explicit deviation record?
9. How are natural-language project capability gates represented for projects that do not encode them in `ap.project.conf`?
10. Does ADR-0017 solve the complete invariant, partially overlap it, or create a projection that this whole should minimally refine?
11. Would a new structural field reduce ambiguity, or duplicate existing development-envelope, command, capability, and side-effect fields?
12. Would executable validation observe the real failure, or merely create documentation-shaped enforcement with high maintenance cost?
13. Does local unpublished AP work already address the observation?
14. What is the smallest portable semantic change, if any, that preserves consumer ownership and historical pin meaning?

Search for supporting and contradictory rules. Do not cite only supporting language.

## 9. Candidate invariants to test, not blindly adopt

Test the smallest coherent version of these proposed invariants:

1. A consuming project owns its exact operations, commands, environment policy, capability gates, and local values.
2. Before prompt issuance, the Orchestrator resolves the governing AP baseline and any applicable consumer-declared route.
3. When an applicable declared route exists and is usable, the prompt names or activates it and treats it as canonical; copied raw commands cannot silently appear as an equivalent route.
4. A necessary deviation records the declared route that is unavailable or unsuitable, the exact alternate path, rationale, evidence class, bounded authority, and stop condition.
5. A deviation must not accidentally become a permanent second canonical route.
6. An IDE, terminal, login shell, inherited variable, retained socket, editor, or prior Worker session is convenience state, not authority or guaranteed capability.
7. Capability, credentials, technical reachability, privilege, task authority, containment, and evidence remain separate.
8. An ambient-environment failure is classified before remediation. When a declared sanitized route applies, one focused reproduction through it is preferred; environment repair or substitution requires separate authority.
9. Projects without a machine-readable route remain compatible. Fallback is exact project-owned guidance, not an AP-invented toolchain.
10. Existing pins and historical prompts retain their original meaning. Consumer adoption remains separate.
11. Machine verification is added only when a current AP-owned executable surface can observe the invariant or the plan proves a minimal new executable boundary necessary.
12. Documentation must not claim enforcement that no validator observes.

Reject, revise, merge, or narrow any invariant that current repository evidence does not support.

## 10. Required comparison of implementation shapes

Compare at least these three shapes in a decision table:

### Shape A — minimal clarification and projection

Refine existing RF-06/RF-16, Orchestrator prompt construction, Development Envelope Activation, command authority, and capability-gate guidance without adding a new record or executable behavior.

Evaluate whether existing fields can express:

* route identity and purpose;
* canonical use;
* contradictory-route prohibition;
* explicit bounded deviation;
* compatibility when no route exists.

### Shape B — one small deterministic structural record or contradiction rule

Use only if existing structural records cannot express the binding decision-completely.

Evaluate the smallest possible record or rule, its semantic owner, exact fields, activation trigger, inactive behavior, duplication risk, compatibility, positive example, negative contradiction example, and whether it is structural rather than a second semantic owner.

Do not default to a new command, schema version, prompt generator, parser, or managed block.

### Shape C — no AP change

If current AP already owns the invariant, or universalization would be disproportionate, recommend no AP mutation and specify a durable ledger disposition supported by evidence.

Distinguish:

* `duplicate`;
* `invalidated`;
* `parked`;
* `rejected`.

Do not use “no change” as a shortcut around contradictory evidence.

## 11. Required planning deliverable

Return one decision-complete planning report containing:

### A. Verdict

Exactly one:

```text
AP change required
No AP change required
AP change parked or rejected
Planning blocked
```

Map it to the ledger disposition recommendation without mutating the ledger.

### B. Identity and evidence reconciliation

Include:

* exact local/public AP identities and classification;
* exact FrameNest identity and governing pin;
* exact Meta identity used;
* dirty/active-operation status;
* exact ledger entry and state;
* evidence limitations.

### C. Semantic-owner and projection map

For every affected rule, identify:

* canonical semantic owner;
* structural projection;
* operational projection;
* advisory/explanatory projection;
* executable enforcement, if any;
* consumer-owned surface;
* historical ADR only.

Identify contradictions, overlaps, stale projections, and duplication risks.

### D. Chosen implementation shape

Compare Shapes A, B, and C, then recommend one with repository-grounded reasons.

If recommending change, define exact semantics including:

* applicability trigger;
* route-resolution responsibility;
* route identity and purpose;
* canonical prompt behavior;
* command contradiction behavior;
* deviation fields and lifecycle;
* unusable/missing-route behavior;
* ambient-state classification;
* capability/credential/authority separation;
* compatibility for documented-only and no-route consumers;
* historical pin compatibility;
* failure and stopping behavior.

### E. Exact later implementation allowlist

Propose the smallest exact repository-relative path allowlist for a later implementation Worker.

For each path state:

* why it is necessary;
* semantic/projection relationship;
* expected change type;
* verification owner.

Provide a separate explicit forbidden-path list.

The default posture is:

* reuse existing RF-06/RF-16;
* no new RF family;
* no new command;
* no `ap.project.conf` schema change;
* no managed-block change;
* no consumer-specific example;
* no monolithic test or conformance suite;
* no executable `ap` change unless documentation/projection cannot make the contract decision-complete and the executable can observe the real contradiction;
* no FrameNest, Meta, pin, NUC, credential, environment, or product mutation.

Any exception requires concrete evidence.

### F. Documentation versus executable decision

State exactly one:

```text
Docs/projection only
Existing executable surface adjustment required
New executable surface required
```

If executable work is recommended, prove:

* what real invariant it can observe;
* why docs/projection cannot decide it;
* why the change does not merely parse wording;
* failure model;
* maintenance owner;
* bounded context cost;
* compatibility;
* focused verification;
* relationship to ADR-0015.

### G. Verification matrix

Map every proposed changed owner to:

* direct semantic review;
* projection/relationship review;
* exact structural checks where appropriate;
* positive route-binding example;
* negative parallel-raw-route example;
* explicit deviation example;
* no-route compatibility example;
* historical pin/non-retroactivity check;
* link/path/Git evidence;
* focused executable evidence only if executable behavior changes.

Do not prescribe a full repository suite without a named decision risk.

### H. Lifecycle after plan approval

Propose the exact later sequence while granting no authority now:

1. new complete implementation prompt with `Native planning mode: not-used`;
2. one fresh Implementation Worker and one initial implementation attempt;
3. bounded correction only for one concrete classified defect;
4. fresh independent acceptance;
5. correction re-acceptance only if needed;
6. explicit AP publication gate and credential-free public readback;
7. separately authorized FrameNest ledger transition to `implemented` only after durable public AP evidence;
8. AP logical-whole closure after all declared evidence and ledger reconciliation;
9. later separate FrameNest AP-pin adoption logical whole, if the COOPERATOR selects it;
10. no automatic NUC deployment or product work.

Clarify whether AP closure should occur before or after the separately authorized consumer-ledger transition, using current AP lifecycle evidence.

### I. Rollback and residual risk

Cover:

* Git-level rollback;
* projection inconsistency recovery;
* prompt compatibility;
* consumers that never adopt;
* natural-language capability-gate ambiguity;
* limits of documentation-only enforcement;
* limits of executable prompt validation;
* risk of creating a permanent parallel route;
* risk of overfitting to FrameNest.

### J. Complexity Budget

Provide explicit numeric ceilings for the later implementation. Stay within these presumptive maxima unless repository evidence proves a smaller or slightly different coherent boundary:

```text
Canonical semantic owner files: 1
Existing RF families touched: at most 2
Operational/structural projection files: at most 4
New ADRs: at most 1
Executable surfaces changed: 0 by default; at most 1 only with proof
New executable/conformance mechanisms: 0 by default
Consumer repositories changed: 0
Managed blocks changed: 0
Schema versions changed: 0
New universal commands: 0
Plan-only cycles: exactly 1
Implementation attempts before classified correction: 1
Fresh independent acceptance Workers after implementation: 1
```

If the coherent plan needs more, stop and explain why the logical whole must be revised rather than silently expanding it.

## 12. Planning acceptance criteria

Return `PASS` / `planning-PASS` only if:

* repository identity and owner-work gates are satisfied;
* the current public AP and FrameNest pin were distinguished correctly;
* the existing ledger entry was uniquely revalidated;
* supporting and contradictory semantics were inspected;
* ADR-0017 partial overlap was reconciled;
* the plan decides whether AP needs a change;
* the chosen shape is compared against the two alternatives;
* the semantic owner and every projection are exact;
* the later path allowlist and forbidden paths are exact;
* docs-only versus executable work is explicitly decided;
* compatibility and failure behavior are decision-complete;
* verification maps to each changed owner;
* lifecycle, rollback, risks, and Complexity Budget are complete;
* no mutation occurred.

Return `PARTIAL` if useful planning evidence exists but one named non-safety-critical decision remains unresolved.

Return `BLOCKED` if repository identity, active owner work, ledger integrity, required evidence, Native Plan Mode, or read-only authority fails.

Do not manufacture `PASS` from assumptions.

## 13. Terminal report contract

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Then echo:

```text
Logical whole identity: ap-consumer-declared-execution-route-and-capability-gate-binding
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: planning-PASS | not-applicable
Logical-whole closure: not-closed
Report justification: new-evidence | new-material-risk
Authority expiry: all Worker 01 exchange 01 planning authority expires at this terminal report
```

Include the complete deliverable from §11.

End with:

* exact confirmation that no file, repository, ledger, Meta artifact, pin, public ref, environment, credential, host, NUC, or production state was changed;
* one smallest recommended next step;
* any near-miss or pre-existing-failure classification;
* an explicit statement that plan approval would still grant no implementation authority.

Stop after the terminal planning report. Do not implement, create a plan file, request permission to implement, or continue autonomously.
