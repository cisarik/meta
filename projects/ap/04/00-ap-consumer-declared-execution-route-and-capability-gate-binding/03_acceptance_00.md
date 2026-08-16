# AP — Worker 03 fresh independent acceptance: consumer-declared execution-route binding

You are one genuinely fresh Worker instance assigned to the AP `WORKER` role.

Independently accept or reject the exact local implementation candidate. You did not plan or implement it. Treat all prior Worker reports as claims, not proof.

Native Plan Mode must be disabled. Do not spawn subagents or delegate internally.

This prompt grants read-only independent acceptance authority only. It grants no correction, implementation, repository mutation, Git write, branch transition, lifecycle-status transition, push, publication, Meta write, FrameNest mutation, ledger transition, consumer-pin adoption, deployment, credential, NUC, production, or closure authority.

## 1. Authoritative coordinates

```text
Persistent role identity: WORKER
Role: WORKER
Logical whole identity: ap-consumer-declared-execution-route-and-capability-gate-binding
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: AP-CONSUMER-ROUTE-BINDING-ACCEPT-03
Native planning mode: not-used
Implementation authority: none
Correction authority: none
Acceptance authority: read-only for exact candidate
Evidence posture: fresh independent acceptance evidence
Evidence tier: E2
Recommended reasoning: High
Recommendation basis: independent review of universal normative semantics, four deliberate projections, historical compatibility, and docs-only enforcement honesty
Escalation or downgrade gate: no autonomous escalation; one concrete finding returns to the ORCHESTRATOR
Sub-agents/internal delegation: not-used
Development envelope activation: not-used
Working-copy topology: canonical-checkout
Topology rationale: exact candidate already exists in the owner checkout; acceptance must inspect that immutable Git object without moving or modifying the checkout
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none
Affected tests: none
New causal regression: consumer-declared route can be bypassed by an equivalent-looking ambient route in an authoritative Worker prompt
Broad or full suite: not-used
Runtime or testbed: not-used
Independent acceptance: current task
Repeated-gate or reasoning-loop stop: configured
Broad gate: not-used
Narrow before re-broad: required
Unchanged candidate and failing check: not-progress
Cooperator delivery / trace destination: not-used
External trace disposition: not-used
```

## 2. Exact acceptance candidate

Repository:

```text
Physical root: /home/agile/Projects/ap
Canonical origin: https://github.com/cisarik/ap.git
Expected branch: feat/consumer-declared-route-binding
Candidate commit: 10ac2ed33e7246233dd813e508f7850465119efc
Candidate tree: b4c82c666f67d2468f133be110c8f6a1b4c95ea8
Candidate parent: 95bd644829d48dcd188627f3e495e649df577eca
Candidate subject: docs: bind Worker prompts to declared routes
Expected public main: 95bd644829d48dcd188627f3e495e649df577eca
Expected commit distance: exactly one commit from public baseline
Push/publication state: candidate must remain local-only
```

The ORCHESTRATOR independently revalidated immediately before issuing this prompt:

```text
95bd644829d48dcd188627f3e495e649df577eca refs/heads/main
```

Do not assume that it remains true. Verify directly.

## 3. Session and independence gate

Before substantive inspection, confirm:

* this is a genuinely fresh Worker session;
* you did not participate in Worker 01 planning or Worker 02 implementation;
* Native Plan Mode is disabled or absent;
* you received Worker 03 exchange 01 coordinates;
* no prior Worker authority is being reused;
* no internal delegation is active;
* you will not repair any finding in this session.

If independence or routing is compromised, stop `BLOCKED`.

## 4. Repository identity gate

Resolve the physical repository root independently and verify using read-only methods:

1. root is `/home/agile/Projects/ap`;
2. origin fetch and push URLs canonicalize to `https://github.com/cisarik/ap.git`;
3. `HEAD` is exactly candidate `10ac2ed3…`;
4. current branch is exactly `feat/consumer-declared-route-binding`;
5. candidate tree, parent, subject, and one-commit ancestry are exact;
6. candidate parent object is exact public baseline `95bd6448…`;
7. credential-free public `refs/heads/main` remains `95bd6448…`;
8. local `main` and public `main` were not moved by the implementation;
9. tracked working tree is clean;
10. no untracked path overlaps the candidate’s changed paths;
11. no active merge, rebase, cherry-pick, revert, bisect, sequencer, or Git lock exists;
12. no remote branch or public ref contains the candidate;
13. no root `AGENTS.md` unexpectedly changes the governing repository rules.

Planning and implementation reported a stale orphan `.git/REBASE_HEAD` without `rebase-merge`, `rebase-apply`, sequencer state, or Git-status rebase indication. Independently classify it:

* if it is still only a stale marker and no active operation exists, record it as a pre-existing non-blocking condition;
* if any active operation exists or identity is ambiguous, stop `BLOCKED`.

Do not read unnecessary contents from stale internal metadata. Do not delete, repair, rename, or modify it.

Preserve all owner content. Do not enumerate unrelated private untracked filenames.

## 5. Read-only authority

You may:

* inspect Git objects, history, refs, ancestry, trees, status, and diffs;
* use credential-free `git ls-remote` for the exact AP public main;
* use read-only text/path inspection;
* run `git diff --check` and other non-mutating documentation/Git checks;
* classify the candidate against this acceptance contract;
* return one terminal report.

You may not:

* edit, create, delete, format, generate, rename, or chmod files;
* stage, commit, amend, switch, checkout, reset, restore, clean, stash, fetch, pull, merge, rebase, cherry-pick, tag, push, publish, or alter refs/config;
* create a worktree or branch;
* change ADR-0018 from `Implementation candidate` to `Accepted`;
* run tests, Python, Poetry, uv, pip, virtual environments, executable `ap`, `ap project check`, `ap exec`, linters, formatters, or dependency tools;
* write Meta;
* change FrameNest, its ledger, or AP pin;
* access credentials, SSH, sudo, GPG-agent, NUC, production, or external accounts;
* implement a correction;
* close the logical whole.

If a correction is needed, return the exact finding. Do not fix it.

## 6. Expected changed-path set

The candidate must change exactly:

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

No other path, file mode, symlink, binary, submodule, executable, schema, managed block, test, CI path, or Git configuration may change.

Verify the exact object-level diff against parent `95bd6448…`, not merely the current worktree.

## 7. Mandatory independent reading

Read the candidate versions of all eight changed paths.

Also inspect the unchanged baseline sources needed to detect contradiction:

* relevant canonical semantic-owner map in `AP.md`;
* RF-06;
* RF-15;
* RF-16;
* prompt-synthesis readiness;
* Compact Communication;
* stopping conditions and anti-patterns;
* `PROMPT_CONTRACTS.md` Development Envelope Activation Record and existing Common Worker Task Fields;
* `INTEGRATION.md` optional development-envelope and consumer ownership boundaries;
* executable `ap` and `ap.project.conf` as source only;
* ADR-0009;
* ADR-0012;
* ADR-0013;
* ADR-0015;
* ADR-0017;
* ADR index lifecycle meanings.

Do not inspect FrameNest or Meta unless the candidate itself introduces an unexpected dependency on them. Such a dependency is a finding; do not broaden inspection to justify it.

## 8. Acceptance owner map

Independently verify:

| Surface                          | Required relationship                                                                                                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `AP.md`                          | sole live normative semantic owner                                                                                                                                 |
| RF-06                            | capability, ambient convenience state, permission, credentials, privilege, containment, authority, and evidence separation                                         |
| RF-16                            | consumer route ownership, applicability, pre-issuance resolution, canonical binding, contradiction, bounded deviation, no-route compatibility, enforcement honesty |
| `AP_ORCHESTRATOR.md`             | operational projection only                                                                                                                                        |
| `AP_WORKER.md`                   | operational projection only                                                                                                                                        |
| `PROMPT_CONTRACTS.md`            | purpose clarification of existing fields only; no new field or record                                                                                              |
| `PROMPT_ENGINEERING_PATTERNS.md` | advisory P08 projection only                                                                                                                                       |
| ADR-0018                         | historical rationale only                                                                                                                                          |
| `CHANGELOG.md`                   | historical delivery record only                                                                                                                                    |
| `docs/adr/README.md`             | historical index/lifecycle projection only                                                                                                                         |
| executable `ap`                  | unchanged; no prompt validation claim                                                                                                                              |
| consumer projects                | exact routes and values remain consumer-owned                                                                                                                      |

Reject the candidate if a subordinate projection becomes a second normative owner or if the invariant is materially duplicated rather than projected.

## 9. Required semantic acceptance matrix

### 9.1 Consumer ownership

Confirm that consumers still own:

* exact operations and commands;
* environment and tooling policy;
* project capability gates;
* local values;
* credentials and privilege mechanics.

AP must remain language-, toolchain-, IDE-, host-, shell-, credential-, provider-, and project-neutral.

### 9.2 Applicability

Confirm the binding is triggered only when the task has an applicable usable route:

* a baseline-declared project operation; and/or
* a project-owned capability gate named by governing project rules.

Confirm AP does not require all consumers to declare such a route.

### 9.3 Pre-issuance resolution

Confirm the Orchestrator must resolve, before issuing the prompt:

* governing AP baseline;
* consumer rules;
* applicable route;
* current usability in the intended Worker boundary.

Required reading alone must not be misrepresented as canonical-route activation.

### 9.4 Canonical route

Confirm a usable applicable declared route is named or activated as the canonical execution/capability path for the task.

### 9.5 Parallel-route contradiction

Confirm an equivalent-looking ambient raw command cannot silently be authorized beside the declared route.

Check both positive and negative authority/command semantics and Worker/Orchestrator stop behavior.

### 9.6 Bounded deviation

Confirm deviation uses existing task-specific fields and includes:

* declared route not used;
* exact alternate;
* rationale;
* evidence class;
* bounded authority;
* stop condition.

Confirm no new universal compact record or structural field was introduced and deviation is not normalized into a second canonical route.

### 9.7 Ambient-state and failure behavior

Confirm:

* IDE, terminal, shell, inherited variable, socket, editor, or prior session is convenience state, not authority or guaranteed capability;
* ambient failure is classified before remediation;
* one focused reproduction through an applicable declared sanitized route is preferred;
* environment reconstruction or weakening is not silently authorized;
* unresolved contradiction or unusable route stops work.

The candidate may use generic examples of route classes, including “SSH,” only as neutral classification. It must not encode SSH-specific policy.

### 9.8 No-route compatibility

Confirm that when no applicable route exists:

* exact project-owned prompt guidance remains lawful;
* AP does not invent an operation, environment, toolchain, capability gate, credential path, or schema;
* Development Envelope Activation may remain `not-used`;
* absence does not manufacture a failure.

### 9.9 Development-envelope distinction

Confirm the candidate does not conflate:

* optional Development Envelope Activation;
* machine-readable `ap.project.conf`;
* natural-language project capability gates.

Each has distinct ownership and activation
