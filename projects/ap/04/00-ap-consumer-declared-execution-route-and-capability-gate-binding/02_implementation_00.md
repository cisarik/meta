# AP — Worker 02 implementation: consumer-declared execution-route and capability-gate binding

You are one fresh Worker instance assigned to the AP `WORKER` role.

Implement the accepted docs/projection-only plan for one bounded logical whole. Native Plan Mode must be disabled. Do not spawn subagents or delegate internally.

This prompt grants bounded AP repository implementation and local commit authority only. It grants no push, publication, acceptance, Meta write, FrameNest mutation, ledger transition, consumer-pin adoption, deployment, credential, host, NUC, production, or closure authority.

## 1. Authoritative coordinates

```text
Persistent role identity: WORKER
Role: WORKER
Logical whole identity: ap-consumer-declared-execution-route-and-capability-gate-binding
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: AP-CONSUMER-ROUTE-BINDING-IMPL-02
Native planning mode: not-used
Planning layer: not-applicable
Implementation authority: explicitly granted within this prompt
Accepted plan identity: Route Binding Plan, Worker 01 exchanges 01–02
Accepted implementation shape: Shape A — minimal clarification and projection
Implementation attempt: initial
Implementation in this Worker session: required
Evidence posture: non-independent implementation evidence
Recommended reasoning: High
Recommendation basis: universal AP semantic change across one canonical owner, four deliberate projections, and historical compatibility, with a named duplication and contradiction risk
Escalation or downgrade gate: no autonomous escalation; stop on any semantic-owner, repository-state, or allowlist contradiction
Sub-agents/internal delegation: not-used
Development envelope activation: not-used
Working-copy topology: canonical-checkout
Topology rationale: the accepted plan requires implementation in the actual AP owner checkout; the existing clean historical branch can be preserved while a new branch is created at the exact public baseline
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none
Affected tests: none
New causal regression: consumer-declared route can be bypassed by an equivalent-looking ambient route in an authoritative Worker prompt
Broad or full suite: not-used
Runtime or testbed: not-used
Independent acceptance: required-separate-fresh-worker
Repeated-gate or reasoning-loop stop: configured
Broad gate: not-used
Narrow before re-broad: required
Unchanged hypothesis, candidate, and failing check: not-progress
Escalate only on: named semantic contradiction or missing repository evidence
Cost cannot falsify evidence: yes
Cooperator delivery / trace destination: not-used
External trace disposition: not-used
```

## 2. Accepted decision

The ORCHESTRATOR accepts the planning result as `planning-PASS`.

Implement Shape A:

> Clarify existing RF-06 and RF-16 semantics and their existing projections so that, when a consuming project has an applicable usable declared execution operation or project-owned capability gate, the Orchestrator resolves it before prompt issuance, makes it the canonical route in the authoritative Worker prompt, rejects a silent equivalent-looking ambient parallel route, and permits deviation only through an explicit bounded task-specific justification.

The implementation is documentation/projection only.

Do not reopen planning. Do not choose Shape B or Shape C. Do not create a new structural record, RF family, executable surface, command, schema version, managed-block field, conformance suite, or consumer-specific mechanism.

If current repository evidence makes Shape A internally inconsistent or impossible within the exact allowlist, stop and report the contradiction. Do not redesign the plan.

## 3. Repository and baseline

Repository:

```text
Physical root: /home/agile/Projects/ap
Canonical origin: https://github.com/cisarik/ap.git
Exact implementation baseline: 95bd644829d48dcd188627f3e495e649df577eca
Baseline tree: 9b895a1eaa95293f14964a756fa9f873e8c48a80
Baseline parent: 1cd2783838cb8cc9483792bc043010b0bbdef347
Baseline subject: docs: mark ADR-0017 accepted
Expected public ref: refs/heads/main = 95bd644829d48dcd188627f3e495e649df577eca
Implementation branch to create: feat/consumer-declared-route-binding
Containing repository: none
Consumer repository mutation: prohibited
```

Planning observed the owner checkout in this pre-implementation state:

```text
Local HEAD: 041de310ea33ed1b47dd8f5fbfcc2829d1a32514
Local branch: refactor/retire-monolithic-ap-test-suite
Tracked tree: clean
Relationship: local HEAD is an ancestor of public 95bd6448…
Root AGENTS.md: absent
Active Git operation: none
Stale .git/REBASE_HEAD: present but not an active rebase
Public 95bd6448… object: already present locally
```

These are expected observations to revalidate, not facts to assume.

A direct Orchestrator readback immediately before issuing this prompt confirmed:

```text
https://github.com/cisarik/ap.git refs/heads/main
95bd644829d48dcd188627f3e495e649df577eca
```

## 4. Native-mode and session gate

Before any repository mutation, confirm:

* this is a genuinely fresh Worker session;
* Native Plan Mode is disabled or absent;
* the received coordinates are Worker 02 exchange 01;
* no authority was inherited from Worker 01;
* no implementation occurred before this prompt;
* internal delegation is not active.

Stop `BLOCKED` if Native Plan Mode is active, the session is not fresh, or the coordinates are contradictory.

## 5. Repository preflight

Resolve the physical repository root independently. Read a root `AGENTS.md` first if one now exists.

Then verify using read-only inspection:

1. repository root and origin identity;
2. local `HEAD`, branch, tree, status, and upstream state;
3. credential-free public `refs/heads/main`;
4. presence and identity of baseline object `95bd6448…`;
5. baseline tree, parent, and subject;
6. current local HEAD is either:

   * the previously observed clean `041de310…` ancestor state; or
   * exact clean baseline `95bd6448…`;
7. no local commit outside the ancestry of public `95bd6448…`;
8. no tracked modification;
9. no untracked path overlaps the implementation allowlist, new ADR target, or files that the branch switch must replace;
10. no active merge, rebase, cherry-pick, revert, bisect, sequencer, or Git lock;
11. branch `feat/consumer-declared-route-binding` does not already exist locally or remotely;
12. `docs/adr/0018-consumer-declared-execution-route-binding.md` does not already exist at the baseline;
13. every allowed existing file matches the exact baseline before editing.

The stale `.git/REBASE_HEAD` reported by planning is not itself an active rebase when:

* neither `.git/rebase-merge` nor `.git/rebase-apply` exists;
* Git status reports no rebase;
* no sequencer or other active operation exists.

Do not delete, repair, rename, or modify the stale marker. If it prevents an authorized Git operation, stop and report the exact failure. Do not improvise inside `.git`.

Preserve unrelated owner and untracked content. Do not enumerate unrelated private filenames in the report.

### Public movement rule

If public AP `main` is no longer exactly `95bd6448…`, stop before mutation. Do not fetch, rebase, merge, or silently adopt the new baseline.

## 6. Authorized branch transition

Only after the preflight passes, create the implementation branch at the exact public baseline:

```text
git switch -c feat/consumer-declared-route-binding 95bd644829d48dcd188627f3e495e649df577eca
```

This one branch creation and worktree transition is authorized.

It must preserve the existing `refactor/retire-monolithic-ap-test-suite` branch ref unchanged. Do not delete, rename, reset, merge, rebase, or update the historical branch.

After switching, verify:

* `HEAD == 95bd6448…`;
* branch is exactly `feat/consumer-declared-route-binding`;
* baseline tree is exact;
* tracked tree is clean;
* owner untracked content remains preserved;
* no active Git operation exists.

If the exact switch fails, stop. Do not use `reset`, `checkout -f`, `clean`, `stash`, or manual `.git` repair.

## 7. Mandatory reading at the implementation baseline

Read before editing:

* `AP.md`

  * semantic-owner map;
  * RF-06;
  * RF-16;
  * current prompt authority and role/capability boundaries;
  * prompt-synthesis readiness;
  * Compact Communication;
  * stopping conditions;
  * anti-patterns;
* `AP_ORCHESTRATOR.md`

  * repository/capability/side-effect gates;
  * prompt construction;
  * stopping conditions;
* `AP_WORKER.md`

  * repository and capability gates;
  * validation/failure classification;
  * stopping conditions;
* `PROMPT_CONTRACTS.md`

  * activated surface annexes;
  * Common Worker Task Fields;
  * `Positive authority`;
  * `Negative authority`;
  * `Commands`;
  * Development Envelope Activation Record;
* `PROMPT_ENGINEERING_PATTERNS.md`

  * P08;
  * its current examples and fixtures;
* `docs/adr/0009-capability-aware-worker-routing-and-execution-gates.md`;
* `docs/adr/0012-baseline-bound-project-execution.md`;
* `docs/adr/0013-semantic-ownership-and-convergence.md`;
* `docs/adr/0015-monolithic-ap-test-suite-retirement.md`;
* `docs/adr/0017-cooperator-ergonomics-cost-proportional-execution.md`;
* `docs/adr/README.md`;
* current relevant `CHANGELOG.md` structure.

Inspect default-untouched projections only enough to confirm that leaving them untouched does not create a direct contradiction. Do not edit them.

## 8. Exact implementation allowlist

You may modify or create only these eight paths:

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

No other path may be staged or committed.

### Path purposes

* `AP.md`: sole live semantic owner; clarify existing RF-06 and RF-16 and the already-owned prompt synthesis, compact communication, stopping, and anti-pattern surfaces.
* `AP_ORCHESTRATOR.md`: operational projection of pre-issuance route resolution, canonical route selection, contradiction prevention, and bounded deviation.
* `AP_WORKER.md`: operational projection of contradiction stopping and ambient-failure classification.
* `PROMPT_CONTRACTS.md`: clarify the purpose of existing command and positive/negative-authority fields; add no new record or field.
* `PROMPT_ENGINEERING_PATTERNS.md`: refine P08 and add bounded generic positive/negative guidance.
* `docs/adr/0018-consumer-declared-execution-route-binding.md`: historical decision and compatibility record.
* `docs/adr/README.md`: register ADR-0018 consistently.
* `CHANGELOG.md`: record the accepted AP change consistently with current style.

## 9. Explicit forbidden scope

Do not modify:

```text
ap
ap.project.conf
INTEGRATION.md
README.md
FAQ.md
GLOSSARY.md
ARTIFACT_LIFECYCLE.md
INFOSEC.md
UPDATING.md
.gitignore
any existing ADR body other than the new ADR-0018
any tests/ path
any CI or workflow path
any managed consumer AGENTS.md block
```

Also prohibited:

* new RF family;
* new structural annex, compact record, required field, parser, prompt generator, validator, schema version, universal command, environment manager, credential broker, capability-gate schema, or conformance suite;
* executable `ap` behavior;
* `ap.project.conf` behavior;
* dependency or runtime changes;
* FrameNest, Meta, ledger, AP pin, NUC, workstation, credentials, SSH, sudo, GPG-agent, Python, Poetry, uv, IDE, product, Brave, or X mutation;
* consumer-specific commands or examples;
* claims that AP mechanically validates prompt wording;
* copying FrameNest operational policy into universal AP;
* broad documentation cleanup or unrelated stylistic refactoring.

If direct consistency requires a forbidden path, stop and return the exact contradiction. Do not enlarge the allowlist.

## 10. Required semantics

Implement the smallest coherent version of all points below.

### 10.1 Consumer ownership

A consuming project continues to own:

* exact operations and command values;
* environment and tooling policy;
* project-owned capability gates;
* local capability values;
* credentials and privilege mechanics.

AP remains provider-, project-, language-, runtime-, shell-, IDE-, host-, and credential-neutral.

### 10.2 Applicability

The binding applies when the current task has an applicable and usable consumer-declared route, including:

* a baseline-declared `ap.project.conf` operation; or
* a project-owned capability gate named in the project’s governing rules.

Do not imply that all projects have either declaration.

Absence of an applicable declared route remains valid compatibility. The fallback is exact project-owned guidance inside the prompt, not an AP-invented toolchain or operation.

### 10.3 Pre-issuance resolution

Before issuing a consequential Worker prompt, the Orchestrator resolves:

* the governing AP baseline;
* the consumer’s governing project rules;
* any declared route applicable to the task;
* whether that route is usable in the intended Worker boundary.

When a usable applicable route exists, merely listing project files as required reading is insufficient. The prompt names or activates the route and makes it the canonical execution or capability path for the authorized task.

### 10.4 No silent parallel route

The authoritative prompt must not silently present a copied raw interpreter, shell, SSH, ambient-session reconstruction, or equivalent-looking command as a parallel alternative to an applicable declared route.

Existing Common Worker Task Fields remain sufficient:

* `Commands`;
* `Positive authority`;
* `Negative authority`;
* mandatory reading and task-specific instructions.

Clarify their purpose rather than adding a new field or record.

### 10.5 Explicit bounded deviation

When the declared route is unavailable or unsuitable, an alternate route is lawful only through task-specific prompt authority that identifies:

* the declared route that could not be used;
* the exact alternate path;
* rationale;
* evidence class;
* bounded authority;
* stopping condition.

Express this through existing task-specific fields and prose. Do not create a new universal structural record.

A deviation must not become a second standing canonical route accidentally.

### 10.6 Ambient state

An IDE, integrated terminal, login shell, inherited environment variable, retained socket, open editor, previous Worker session, or similar ambient state is convenience state. It is not authority, durable configuration, or a guaranteed capability in another process boundary.

Keep capability, credentials, technical reachability, privilege, containment, task authority, and evidence distinct under RF-06.

### 10.7 Failure classification

When an ambient route fails and an applicable declared sanitized route exists:

* classify the ambient failure before remediation;
* prefer one focused reproduction through the declared route;
* do not reconstruct, repair, replace, or weaken the environment without explicit authority;
* stop when the declared route is unusable and no bounded deviation is authorized.

Keep this universal. Do not encode Python, Cursor, AppImage, GPG-agent, SSH, sudo, FrameNest, or workstation-specific policy as AP semantics.

### 10.8 Historical compatibility

* Existing consumer pins retain their original meaning.
* Historical Worker prompts remain interpreted under their original AP pin.
* A newer public AP revision does not govern an older consumer retroactively.
* Consumer ledger reconciliation and AP-pin adoption remain separate tasks.
* No migration or managed-block change is required.

### 10.9 Enforcement honesty

State or preserve clearly that:

* `ap project check` and `ap exec` enforce their declared project-operation boundary only when used;
* executable `ap` does not construct or validate Worker prompts;
* this logical whole strengthens normative, operational, structural-purpose, advisory, and historical documentation;
* it does not add mechanical prompt validation.

## 11. Semantic-owner discipline

`AP.md` remains the only live normative semantic owner.

Subordinate files must remain deliberate projections:

* `PROMPT_CONTRACTS.md`: structural-purpose clarification only;
* `AP_ORCHESTRATOR.md` and `AP_WORKER.md`: operational projections;
* `PROMPT_ENGINEERING_PATTERNS.md`: advisory projection;
* ADR-0018 and `CHANGELOG.md`: historical projections.

Do not repeat the complete invariant verbatim across all files. Each projection should contain only what its consumer needs and should remain traceable to the canonical RF-06/RF-16 semantics.

Do not broaden RF-15 or create RF-20.

## 12. P08 and examples

Update P08 minimally so that its adaptation questions or template distinguish:

* an applicable declared route;
* its canonical use;
* an unauthorized equivalent-looking parallel route;
* an explicit bounded deviation;
* no-route compatibility.

Add or refine one concise generic negative fixture demonstrating the contradiction. It must not use FrameNest names, paths, Python, Poetry, uv, Cursor, AppImage, SSH, GPG-agent, sudo, or NUC details.

The fixture is advisory evidence, not a validator or new structural contract.

Do not add a large fixture collection.

## 13. ADR-0018 requirements

Create:

```text
docs/adr/0018-consumer-declared-execution-route-binding.md
```

Use the repository’s established ADR style and mark its implementation-candidate status consistently with current lifecycle conventions. Do not mark it accepted before independent acceptance and publication justify that later lifecycle transition.

The ADR must record:

* context and portable field failure;
* decision to extend existing RF-06/RF-16;
* consumer ownership;
* applicability and no-route compatibility;
* canonical prompt binding;
* contradiction and deviation rules;
* ambient-state boundary;
* docs/projection-only implementation;
* semantic-owner/projection map;
* historical pin compatibility;
* consequences and limitations;
* relationship to ADR-0009, ADR-0012, ADR-0013, ADR-0015, and ADR-0017;
* rejected alternatives:

  * no AP change;
  * new structural record;
  * executable prompt parser/validator;
  * schema or command expansion;
  * consumer-specific universal policy.

Keep the ADR historical. It must not become a second normative protocol.

Update `docs/adr/README.md` and `CHANGELOG.md` consistently with candidate—not accepted/public—state.

## 14. Implementation method

Use one initial implementation attempt:

1. inspect every allowed owner/projection at the exact baseline;
2. identify the smallest insertion or clarification point;
3. edit only the allowlist;
4. review semantic ownership before polishing prose;
5. inspect the complete diff;
6. perform focused documentation verification;
7. create exactly one implementation commit if all gates pass;
8. stop and report.

Do not perform opportunistic cleanup, reflow unrelated sections, renumber unrelated content, or rewrite whole documents.

## 15. Verification

No AP test suite, Python, virtual environment, dependency, `ap`, or runtime execution is authorized or required.

Run proportionate documentation/Git verification:

### 15.1 Identity and scope

* confirm branch and baseline;
* confirm exact diff base is `95bd6448…`;
* verify changed paths are a non-empty subset of the exact eight-path allowlist;
* for PASS, require all paths needed by the accepted plan and no other path;
* verify no forbidden path changed;
* verify no submodule, mode, symlink, binary, or Git configuration change.

### 15.2 Diff hygiene

* `git diff --check`;
* inspect full diff and diff stat;
* inspect staged diff before commit;
* confirm no conflict markers, trailing whitespace, malformed Markdown fences, or broken relative links introduced;
* verify every newly referenced repository-relative path exists.

### 15.3 Semantic and projection review

Demonstrate from the final candidate:

1. canonical semantic ownership remains in `AP.md`;
2. RF-06 and RF-16 jointly own the invariant without a new RF;
3. Orchestrator resolves applicable routes before prompt issuance;
4. usable declared route is canonical;
5. silent ambient parallel route is prohibited;
6. bounded deviation uses existing task fields;
7. Worker stops on unresolved contradiction;
8. one focused declared-route reproduction follows ambient failure classification;
9. no-route and documented-only consumers remain compatible;
10. Development Envelope Activation remains distinct from `ap.project.conf`;
11. historical pin meaning is preserved;
12. no executable enforcement is claimed.

### 15.4 Four required cases

Review the candidate against four generic cases:

* **positive:** applicable usable declared route is named and canonical;
* **negative:** prompt also supplies an equivalent-looking ambient raw route without deviation—invalid;
* **deviation:** declared route unusable; exact alternate, rationale, evidence, authority, and stop condition are present;
* **no route:** consumer declares no applicable route; exact project-owned prompt guidance remains lawful without an AP-invented toolchain.

Also verify a historical consumer pinned before this change is not reinterpreted retroactively.

### 15.5 Duplication and overfitting

Search and directly review for:

* duplicated normative paragraphs across projections;
* accidental new field/record language;
* FrameNest-specific operational values or examples;
* Python/Poetry/uv/Cursor/AppImage/GPG/SSH/sudo/NUC policy promoted to universal AP;
* claims of parser or executable prompt enforcement;
* unintended edits to default-untouched files.

### 15.6 Complexity Budget

Final candidate must remain within:

```text
Canonical semantic owner files: 1
Existing RF families touched: at most 2
Operational/structural projection files: at most 4
New ADRs: 1
Executable surfaces changed: 0
New executable/conformance mechanisms: 0
Consumer repositories changed: 0
Managed blocks changed: 0
Schema versions changed: 0
New universal commands: 0
Implementation attempts before classified correction: 1
```

## 16. Git authority

After verification passes, you may create exactly one local commit.

Authorized Git writes:

* create branch `feat/consumer-declared-route-binding` at exact `95bd6448…`;
* edit only the eight allowlisted paths;
* stage only the exact changed allowlisted paths;
* create one normal commit with exact subject:

```text
docs: bind Worker prompts to declared routes
```

Do not:

* fetch, pull, merge, rebase, cherry-pick, reset, restore, clean, stash, amend, tag, push, force, delete branches, modify remotes/config, or bypass hooks;
* stage unrelated content;
* create a second commit;
* move local or remote `main`;
* publish anything.

If commit creation fails, preserve the worktree and report the first causal failure. Do not bypass hooks or improvise another Git route.

## 17. Post-commit verification

After the commit, verify:

* `HEAD` is one direct child of `95bd644829d48dcd188627f3e495e649df577eca`;
* branch is `feat/consumer-declared-route-binding`;
* subject is exactly `docs: bind Worker prompts to declared routes`;
* changed paths equal the intended allowlist subset and no forbidden path;
* candidate tree identity;
* working tree is clean except preserved unrelated pre-existing untracked content;
* no active Git operation;
* public AP `refs/heads/main` remains `95bd6448…`;
* no push occurred;
* old local branch ref remains unchanged;
* stale `.git/REBASE_HEAD`, if still present, was not modified.

The implementation commit is a candidate only. It is not accepted, public, or closed.

## 18. Hard stops

Stop without improvisation if:

* repository or public identity differs;
* public AP main moved from `95bd6448…`;
* Native Plan Mode is active;
* the Worker session is not fresh;
* owner work overlaps the allowlist;
* local AP contains an unpublished non-ancestor candidate;
* branch or ADR target already exists;
* an active Git operation or lock exists;
* stale Git metadata prevents the exact authorized branch transition;
* the change needs a forbidden path;
* the accepted semantics require a new record, RF, command, schema, executable, validator, test suite, consumer change, or Meta change;
* documentation cannot remain honest about lack of mechanical prompt validation;
* a consumer-specific example is required to make the text coherent;
* one implementation commit cannot be produced;
* any secret, credential, socket, private value, or unrelated owner content would be exposed;
* completion would require push, publication, acceptance, ledger transition, pin adoption, deployment, or closure.

Return the first causal blocker and the smallest authority or decision needed. Do not partially declare PASS.

## 19. Terminal report

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Then include:

```text
Logical whole identity: ap-consumer-declared-execution-route-and-capability-gate-binding
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS | not-applicable
Result artifact or commit: <candidate SHA or none>
Logical-whole closure: not-closed
Report justification: new-mutation | new-evidence | new-material-risk
Authority expiry: all Worker 02 exchange 01 implementation authority expires at this terminal report
```

Report:

1. preflight identities and public ref;
2. local starting state and branch transition;
3. candidate commit, tree, parent, subject, and branch;
4. exact changed paths and why each was necessary;
5. semantic-owner and projection result;
6. four-case review;
7. documentation/executable classification;
8. verification commands and exit statuses;
9. Complexity Budget result;
10. Git staging/commit result;
11. confirmation of no push/publication;
12. deviations, risks, missing evidence, and near-misses;
13. pre-existing-failure classification, including stale Git metadata;
14. one smallest next step: fresh independent acceptance of the exact candidate;
15. explicit confirmation that FrameNest, Meta, ledger, pin, NUC, environment, credentials, and production were not changed.

Return `PASS` / `implementation-PASS` only when the exact candidate commit exists, every required semantic outcome and verification gate passes, and the post-commit repository state is valid.

Do not emit `CLOSED: PASS`. Stop immediately after the terminal report.
