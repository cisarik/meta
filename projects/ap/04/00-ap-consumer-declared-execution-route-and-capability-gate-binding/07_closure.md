# ORCHESTRATOR Closure Record — AP Consumer-Declared Execution Route and Capability-Gate Binding

```text
Logical whole identity: ap-consumer-declared-execution-route-and-capability-gate-binding
Standard terminal status: PASS
Phase-qualified result: not-applicable
Result artifact or commit: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Result evidence: accepted semantic commit 10ac2ed33e7246233dd813e508f7850465119efc; accepted-state promotion 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656; fresh independent acceptance and scoped re-acceptance; one ordinary non-force publication push; credential-free public ref readback; independent fresh public clone and Git-object verification
Logical-whole closure: closed-by-ORCHESTRATOR
Report justification: explicit-closure
Authority expiry: all ORCHESTRATOR authority for this logical whole expires at this closure record; no next-whole authority is implied
```

```text
Required preceding results: satisfied
Cooperator-owned decisions: satisfied
Planning disposition: accepted
Implementation completion: satisfied
Independent acceptance: satisfied
Accepted-state lifecycle promotion: satisfied
Scoped independent re-acceptance: satisfied
Publication: satisfied
Public Git equality: satisfied
Residual-risk disposition: satisfied
Upgrade-ledger reconciliation: complete-for-this-AP-whole
Active mutation: none
Closure actor: ORCHESTRATOR
```

```text
Declared closure signal: CLOSED: PASS
Signal owner: ORCHESTRATOR
Worker emission of closure signal: prohibited
Closure authority: present
Logical-whole closure: closed-by-ORCHESTRATOR
```

The logical whole `ap-consumer-declared-execution-route-and-capability-gate-binding` is **CLOSED: PASS**.

## 1. Closure decision

The accepted and published AP revision now owns a portable invariant for binding authoritative Worker prompts to applicable consumer-declared execution operations and project-owned capability gates.

All required planning, implementation, independent acceptance, accepted-state promotion, scoped re-acceptance, publication, and final public-verification gates completed without an unresolved finding.

No further Worker is required for this AP logical whole.

The FrameNest upgrade-ledger entry, FrameNest AP-pin adoption, Meta archival, local Git-reference cleanup, NUC deployment, and product work remain outside this closure and require separate authority if selected later.

## 2. Final public AP state

```text
Repository: https://github.com/cisarik/ap.git
Public ref: refs/heads/main
Commit: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Tree: 43bc12b966133d76972ccf3884d80dceedde013b
Parent: 10ac2ed33e7246233dd813e508f7850465119efc
Subject: docs: mark ADR-0018 accepted
ADR-0018 status: Accepted
```

The complete accepted stack from the previous public baseline is:

```text
95bd644829d48dcd188627f3e495e649df577eca
  tree: 9b895a1eaa95293f14964a756fa9f873e8c48a80
  subject: docs: mark ADR-0017 accepted

  -> 10ac2ed33e7246233dd813e508f7850465119efc
     tree: b4c82c666f67d2468f133be110c8f6a1b4c95ea8
     parent: 95bd644829d48dcd188627f3e495e649df577eca
     subject: docs: bind Worker prompts to declared routes

  -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
     tree: 43bc12b966133d76972ccf3884d80dceedde013b
     parent: 10ac2ed33e7246233dd813e508f7850465119efc
     subject: docs: mark ADR-0018 accepted
```

The stack contains exactly two commits after public baseline `95bd6448…`.

## 3. Completed evidence chain

| Gate                                     | Actor                 | Result                        | Exact artifact or evidence                                                                                                       |
| ---------------------------------------- | --------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Repository restoration and ledger triage | ORCHESTRATOR          | PASS                          | FrameNest public `fc355d6…`; FrameNest AP pin `17b7e085…`; AP public baseline `95bd6448…`; unique ledger observation revalidated |
| Implementation planning                  | Worker 01             | planning disposition accepted | Frozen `Route Binding Plan`; Shape A selected; docs/projection-only implementation                                               |
| Planner-report completion                | Worker 01 exchange 02 | PASS                          | Standard report rendered without re-planning or repository mutation                                                              |
| Semantic implementation                  | Worker 02             | implementation-PASS           | `10ac2ed33e7246233dd813e508f7850465119efc`                                                                                       |
| Fresh independent acceptance             | Worker 03             | acceptance-PASS               | Exact immutable semantic candidate `10ac2ed…`; no finding                                                                        |
| Acceptance-report completion             | Worker 03 exchange 02 | acceptance-PASS               | Standard terminal acceptance report; Worker authority expired                                                                    |
| Accepted-state promotion                 | Worker 04             | implementation-PASS           | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`                                                                                       |
| Fresh scoped re-acceptance               | Worker 05             | acceptance-PASS               | Exact two-commit tip `9c5cc44…`; promotion and retained semantics independently verified                                         |
| Publication                              | Worker 06             | publication-PASS              | One ordinary non-force push of exact `9c5cc44…:refs/heads/main`; exit 0                                                          |
| Public readback                          | Worker 06             | PASS                          | Credential-free `git ls-remote` returned exact public `main = 9c5cc44…`                                                          |
| Independent closure verification         | ORCHESTRATOR          | PASS                          | Credential-free public ref readback, fresh public clone, exact Git-object and diff verification                                  |

No planning, implementation, acceptance, promotion, re-acceptance, or publication result alone constituted logical-whole closure. Closure is the explicit ORCHESTRATOR decision recorded here after reconciliation of the complete evidence chain.

## 4. Independent ORCHESTRATOR closure verification

The ORCHESTRATOR performed a new credential-free public verification after Worker 06’s publication report.

### Public branch identity

```text
git ls-remote https://github.com/cisarik/ap.git refs/heads/main
```

returned exactly:

```text
9c5cc44f8b6c92dd56ad2427d13223d7d59c5656	refs/heads/main
```

### Fresh public clone identity

A new disposable credential-free clone of canonical public AP verified:

```text
HEAD: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Tree: 43bc12b966133d76972ccf3884d80dceedde013b
Parent: 10ac2ed33e7246233dd813e508f7850465119efc
Subject: docs: mark ADR-0018 accepted
Branch status: main...origin/main
Tracked state: clean
```

### Public ancestry

Direct Git-object inspection verified exactly two commits after `95bd6448…`:

```text
10ac2ed33e7246233dd813e508f7850465119efc
  tree b4c82c666f67d2468f133be110c8f6a1b4c95ea8
  parent 95bd644829d48dcd188627f3e495e649df577eca
  subject docs: bind Worker prompts to declared routes

9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  tree 43bc12b966133d76972ccf3884d80dceedde013b
  parent 10ac2ed33e7246233dd813e508f7850465119efc
  subject docs: mark ADR-0018 accepted
```

`rev-list --count` over the public range returned `2`.

### Public path set

The complete public stack changes exactly these eight documentation paths:

```text
M AP.md
M AP_ORCHESTRATOR.md
M AP_WORKER.md
M CHANGELOG.md
M PROMPT_CONTRACTS.md
M PROMPT_ENGINEERING_PATTERNS.md
A docs/adr/0018-consumer-declared-execution-route-binding.md
M docs/adr/README.md
```

The accepted-state promotion changes exactly:

```text
M CHANGELOG.md
M docs/adr/0018-consumer-declared-execution-route-binding.md
M docs/adr/README.md
```

No executable, schema, test, CI, configuration, managed-block, submodule, mode, symlink, binary, consumer, or product path changed.

### Public documentation checks

The fresh public clone verified:

```text
ADR-0018 status: Accepted
Complete-stack git diff --check: exit 0
Promotion-only git diff --check: exit 0
Fresh-clone status: clean
```

The executable `ap` and `ap.project.conf` are unchanged.

## 5. Accepted semantic result

AP now owns the following universal behavior through existing RF-06 and RF-16.

### 5.1 Consumer ownership

A consuming project continues to own:

* exact operations and commands;
* environment and tooling policy;
* project-owned capability gates;
* local capability values;
* credential and privilege mechanics;
* host- and project-specific execution details.

AP does not become a Python, Poetry, uv, virtual-environment, shell, IDE, AppImage, GPG-agent, SSH, sudo, workstation, host, deployment, credential, or product manager.

### 5.2 Applicability

The binding applies only when a consuming project has an execution operation or capability gate that is both:

* applicable to the current task; and
* usable in the intended Worker boundary.

AP does not assume that every project declares either surface.

### 5.3 Pre-issuance resolution

Before issuing a consequential Worker prompt, the Orchestrator resolves:

* the governing AP baseline;
* the consumer’s governing project rules;
* any declared route applicable to the task;
* whether that route is usable in the intended Worker boundary.

Listing project files as required reading does not by itself bind the Worker to the route.

### 5.4 Canonical prompt route

When an applicable declared route exists and is usable, the authoritative Worker prompt names or activates it and treats it as the canonical execution or capability path.

A copied raw interpreter, shell, remote-access command, ambient-session reconstruction, or equivalent-looking command must not silently appear as a parallel alternative.

### 5.5 Contradiction handling

An authoritative prompt that simultaneously names a declared canonical route and silently authorizes an equivalent ambient route contains a material contradiction.

Existing prompt structures remain sufficient:

* `Commands`;
* `Positive authority`;
* `Negative authority`;
* mandatory reading;
* task-specific scope and stopping conditions.

No new compact record, annex, schema field, command, parser, or prompt generator was introduced.

### 5.6 Bounded deviation

When a declared route is unavailable or unsuitable, an alternate route is lawful only through explicit task-specific authority that identifies:

* the declared route that could not be used;
* the exact alternate path;
* rationale;
* evidence class;
* bounded authority;
* stopping condition.

A deviation must not become a second standing canonical route accidentally.

### 5.7 Ambient-state boundary

An IDE, integrated terminal, login shell, inherited environment variable, retained socket, open editor, or previous Worker session is convenience state.

It is not:

* task authority;
* durable configuration;
* a verified capability in another process boundary;
* a substitute for current evidence.

Capability, credentials, reachability, privilege, containment, task authority, and evidence remain separate under RF-06.

### 5.8 Failure classification

When an ambient execution route fails and an applicable declared sanitized route exists:

* classify the ambient failure before remediation;
* prefer one focused reproduction through the declared route;
* do not silently reconstruct, repair, replace, or weaken the environment;
* stop when the declared route is unusable and no bounded deviation is authorized.

### 5.9 No-route compatibility

A project that declares no applicable route remains valid.

The fallback is exact project-owned prompt guidance, not an AP-invented toolchain or operation.

Optional Development Envelope Activation, machine-readable `ap.project.conf`, and natural-language project capability gates remain distinct surfaces.

### 5.10 Historical compatibility

Existing AP pins and historical Worker prompts retain their original meaning.

A newer public AP revision does not govern an older consumer retroactively. Consumer adoption remains a separate explicit task.

## 6. Semantic ownership and projections

`AP.md` remains the sole live normative semantic owner.

The accepted ownership map is:

| Surface                                                      | Relationship                                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `AP.md` RF-06 and RF-16                                      | Sole canonical semantic ownership                                                    |
| `AP_ORCHESTRATOR.md`                                         | Operational projection for pre-issuance resolution and prompt construction           |
| `AP_WORKER.md`                                               | Operational projection for contradiction stopping and ambient-failure classification |
| `PROMPT_CONTRACTS.md`                                        | Structural-purpose clarification of existing authority and command fields            |
| `PROMPT_ENGINEERING_PATTERNS.md` P08                         | Advisory projection and generic prompt examples                                      |
| `docs/adr/0018-consumer-declared-execution-route-binding.md` | Accepted historical decision record                                                  |
| `docs/adr/README.md`                                         | Historical index projection                                                          |
| `CHANGELOG.md`                                               | Historical delivery projection                                                       |
| executable `ap`                                              | Unchanged executable projection; no prompt-construction or prompt-validation claim   |
| consuming project rules                                      | Exact project-owned route values and gates                                           |

No second normative owner, new RF family, new structural record, executable validator, schema version, managed-block migration, or universal command was created.

## 7. Implementation shape and Complexity Budget

The accepted implementation is Shape A: minimal clarification and projection of existing RF-06/RF-16 semantics.

The completed change stayed within the accepted Complexity Budget:

```text
Canonical semantic owner files: 1
Existing RF families touched: 2
Operational/structural projection files: 4
New ADRs: 1
Executable surfaces changed: 0
New executable or conformance mechanisms: 0
Consumer repositories changed: 0
Managed blocks changed: 0
Schema versions changed: 0
New universal commands: 0
Initial semantic implementation attempts: 1
Fresh independent semantic acceptance Workers: 1
Accepted-state promotion commits: 1
Fresh scoped re-acceptance Workers: 1
Publication pushes: 1 ordinary non-force push
```

ADR-0015’s documentation-first posture remains intact. No AP conformance suite or prompt parser was introduced.

## 8. Publication result

Worker 06 performed exactly one authorized push:

```text
git push origin 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656:refs/heads/main
```

Result:

```text
Exit status: 0
Update: 95bd644..9c5cc44 -> main
Force used: no
Additional branch or tag created: no
```

Credential-free post-push readback confirmed the exact accepted tip.

No source edit, new commit, merge, rebase, amendment, tag, force operation, second push, consumer mutation, or deployment occurred during publication.

## 9. Residual-risk disposition

Residual risks are accepted and bounded.

### Documentation-only enforcement

The change does not mechanically parse or validate Worker prompts. The executable `ap` does not observe prompt text.

The invariant is enforced through:

* the normative AP contract;
* Orchestrator prompt-construction obligations;
* Worker contradiction and stopping behavior;
* independent acceptance;
* practical consumer use.

This limitation is intentional and consistent with ADR-0015.

### Natural-language capability gates

A consumer-owned capability gate may remain ambiguous if the consuming project does not name it clearly. AP does not invent the missing project policy.

### Deviation misuse

Poorly scoped deviation wording could create an accidental parallel route. The accepted protocol explicitly rejects a deviation becoming a second standing canonical route.

### Historical consumers

Consumers pinned to an earlier AP revision do not receive the new semantics until separately authorized adoption. This is compatibility behavior, not a defect.

All residuals are compatible with closure.

## 10. Pre-existing local-state classification

The implementation and acceptance Workers consistently reported two pre-existing local AP conditions:

```text
Stale local main:
4e7bfa562c961b33cf835a2e764188b190185209

Inactive stale .git/REBASE_HEAD:
573975cffc5ce94c481553168abc040d4ad39557
```

The stale `REBASE_HEAD` had no accompanying `rebase-merge`, `rebase-apply`, sequencer, status indicator, or other active-operation evidence. It was classified as inactive stale metadata.

The stale local `main` was an ancestor of public main and was not the implementation branch.

Both were preserved and left untouched. Neither affected the immutable candidate, independent acceptance, publication, public branch, or fresh public clone.

This closure grants no authority to clean, delete, repair, or move either local state.

## 11. FrameNest upgrade-ledger reconciliation

The observation that initiated this AP work remains stored in FrameNest:

```text
Upgrade ledger: upgrade https://github.com/cisarik/ap.git
Ledger storage version: 1
Ledger path: docs/AP_UPGRADE_OBSERVATIONS.md

Entry: consumer-declared-execution-and-capability-route-binding
Entry state: untriaged
Entry authority: non-authorizing
```

The FrameNest observation was originally recorded against:

```text
Observed against: 5abb2adfcd1d5f3391df9c3044b4b81ac1aac923
Last revalidated against: 5abb2adfcd1d5f3391df9c3044b4b81ac1aac923
```

This AP logical whole has now produced durable public implementation evidence:

```text
Promotion target:
https://github.com/cisarik/ap.git
refs/heads/main
9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

However, AP-source publication does not itself authorize a FrameNest repository mutation.

Therefore:

* the FrameNest ledger remains `untriaged`;
* it was not changed to `accepted` or `implemented`;
* no disposition evidence was written into FrameNest;
* no FrameNest AP pin was changed;
* no duplicate observation was created;
* provenance remains intact.

Ledger reconciliation is complete for the purpose of this AP closure because the remaining consumer mutation is explicitly separated, preserved, and non-authorized—not forgotten or falsely claimed as complete.

A later FrameNest ledger-reconciliation task may use public AP SHA `9c5cc44…` as durable disposition evidence.

## 12. FrameNest AP-pin separation

FrameNest continues to be governed by its existing AP gitlink:

```text
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

This AP closure does not:

* run `./.ap/ap update --apply`;
* move the FrameNest `.ap` gitlink;
* alter FrameNest integration documentation;
* run consumer tests;
* publish a FrameNest commit;
* deploy FrameNest or the NUC.

Adoption of AP `9c5cc44…` by FrameNest is a later, distinct consumer logical whole requiring explicit Cooperator selection, implementation authority, independent acceptance, and publication.

## 13. What this logical whole did not do

This logical whole did not:

* modify FrameNest;
* modify the FrameNest upgrade ledger;
* update any consumer AP pin;
* modify Meta as part of Worker authority;
* deploy or contact the NUC;
* modify credentials, SSH, GPG-agent, sudo, IDE, shell, workstation, Python, Poetry, uv, or a virtual environment;
* modify executable `ap`;
* modify `ap.project.conf`;
* introduce a prompt parser or validator;
* create a conformance suite;
* create a new RF family;
* create a new structural record;
* change a schema or managed block;
* open Brave/X or other product work;
* move stale local AP `main`;
* delete stale `.git/REBASE_HEAD`;
* authorize any next logical whole.

## 14. Meta archival relationship

This closure record may be copied by the Cooperator into the external Meta trace as `07_closure.md`.

That archival copy is:

* historical evidence;
* not live AP semantic authority;
* not Worker authority;
* not implementation or publication authority;
* not a FrameNest ledger mutation;
* not a consumer-pin adoption;
* not permission for further repository or external effects.

The exact public AP repository and commit remain the durable semantic and publication evidence.

## 15. Authority expiry and next-work boundary

All authority issued in this logical whole has expired:

* Worker 01 planning and report-completion authority;
* Worker 02 implementation authority;
* Worker 03 acceptance and report-completion authority;
* Worker 04 accepted-state promotion authority;
* Worker 05 scoped re-acceptance authority;
* Worker 06 publication authority;
* ORCHESTRATOR authority for this logical whole.

No Worker may continue from a prior prompt.

No mutation, publication, Meta write, consumer-ledger update, AP-pin adoption, deployment, local-Git cleanup, or product work follows automatically from this closure.

Potential later work, only if separately selected by the Cooperator, includes:

1. FrameNest ledger reconciliation using public AP `9c5cc44…` as disposition evidence;
2. a distinct FrameNest adoption of AP `9c5cc44…`;
3. optional owner-directed reconciliation of stale local AP Git references;
4. unrelated FrameNest, NUC, or product work.

None is authorized by this record.

# CLOSED: PASS
