ap upgrade cisarik/framenest

# Fresh Orchestrator handout: consumer-declared execution-route binding in AP

## Nature of this input

Treat the first line as an AP continuation/upgrade-routing directive, not as a shell command. This handout restores discovery context and requests a decision route. It is not a Worker prompt, implementation authority, publication authority, Meta-write authority, consumer-pin adoption authority, or permission to mutate either repository.

Use one continuous fresh Orchestrator session. Do not use subagents. Route at most one Worker at a time and only after the Cooperator selects the proposed logical whole.

## Repositories and independently verified anchors

The available workspace is expected to contain:

- consumer repository: `/home/agile/Projects/framenest`, canonical repository `https://github.com/cisarik/framenest.git`;
- protocol repository: `/home/agile/Projects/ap`, canonical repository `https://github.com/cisarik/ap.git`;
- AP trace/archive repository: `/home/agile/meta`.

Do not trust these paths, a currently open editor, retained chat context, local branch names, or remembered SHAs as authority. Resolve repository roots and read their governing `AGENTS.md` files before deeper inspection. Revalidate local HEAD, branch, status, worktree state, remotes, active Git operations, and public refs directly. Preserve all owner changes and unrelated untracked content.

Known consumer evidence to revalidate:

- FrameNest public `main` and the closed candidate were `fc355d6e21d2f2781e0166906b453fa3fa91bdb7` at the terminal report.
- FrameNest's AP gitlink remained `17b7e085139e9bcbb0e4953d26aef9b6687d541c`.
- Logical whole `framenest-cursor-worker-execution-boundary-convergence` closed `PASS`.
- Its Meta chain was reported as `01_implementation_00.md` / `01_report_00.md`, `02_acceptance_00.md` / `02_report_00.md`, `03_publication_00.md` / `03_report_00.md`, and `04_closure_00.md`.
- The relevant FrameNest upgrade-ledger observation remained `untriaged`; closure explicitly did not claim an AP upgrade.
- The NUC was not deployed for this logical whole.

The current public AP SHA is deliberately not supplied. Discover it directly from the canonical remote and determine whether the local AP checkout represents public `main`, an unpublished candidate, a divergent branch, or unrelated owner work. The FrameNest pin governs FrameNest until a separately authorized adoption task; a newer public AP revision is evidence, not retroactive authority.

## Field evidence and problem statement

FrameNest repeatedly exposed two manifestations of the same boundary failure in Worker execution:

1. A project virtual-environment interpreter was invoked through raw ambient IDE state. Cursor/AppImage loader variables contaminated the process and CPython failed before application startup with `ModuleNotFoundError: No module named 'encodings'`. Workers then spent time searching for interpreters, changing `PYTHONPATH`, considering Poetry or environment repair, and reasoning about a broken virtual environment even though the project already declared a sanitized AP execution envelope.
2. Workers repeatedly found no inherited `SSH_AUTH_SOCK`, rediscovered the GPG-agent SSH socket, and reconstructed access locally. A socket exported in one terminal is only available to that process and its descendants; it is not durable authority and is not guaranteed to reach an already-running IDE agent, a fresh Worker, or a sanitized child. Remote capability and privilege gates were project-owned, but prompts and guidance could still encourage ambient reconstruction.

The closed FrameNest whole converged project guidance and prompts on its existing project-owned route. This is valid consumer evidence, not proof that AP itself is defective and not a request to encode FrameNest operations in AP.

The candidate universal gap is narrower:

> AP may define sanitized execution, project-owned development envelopes, capability handshakes, and exact prompt authority separately, yet may not bind an authoritative Worker prompt strongly enough to the consumer-declared execution operation and capability gate or reject an equivalent-looking raw ambient route in the same prompt.

## Candidate upgrade observation

Use the existing declared FrameNest ledger. Do not scan for guessed ledger filenames. Revalidate and triage exactly the matching active observation; do not create a duplicate merely because this handout uses different wording.

Suggested stable concept label, only if needed to identify the existing observation:

`consumer-declared-execution-and-capability-route-binding`

Candidate disposition statement:

- **Evidence:** a consumer had a declared sanitized execution envelope and project-owned remote capability gates, but authoritative guidance and prompts could still copy raw interpreter commands or reconstruct ambient session state; repeated failures disappeared after consumer convergence on the declared routes.
- **Potential AP gap:** prompt synthesis/projection may not require resolution and explicit activation of an applicable consumer-declared operation/gate, nor identify a contradictory undeclared parallel route.
- **Desired universal outcome:** when a consumer has declared an applicable execution route or capability gate, the Orchestrator binds the current Worker prompt to it by identity and purpose; ambient IDE/session inheritance is never assumed; deviation is explicit, bounded, evidenced, and separately justified.
- **Non-goals:** AP does not become a Python, Poetry, uv, virtualenv, shell, Cursor, AppImage, GPG-agent, SSH, sudo, workstation, host, deployment, or credential manager.

## Required read-only restoration and triage

Before proposing work:

1. Read current governing project rules from both repositories and the exact AP pin that governs FrameNest.
2. Discover the FrameNest ledger only through its declared project-owned root contract. Validate its target, active snapshot, entry identity/state, and current public-safe evidence.
3. Selectively read the closed FrameNest whole's prompt/report pairs and closure only to recover evidence needed for this observation. Do not ingest the entire Meta archive and do not treat Meta as live semantic authority.
4. Independently inspect current public AP semantics and their ownership map. At minimum reconcile the live semantic owner, Orchestrator projection, prompt structural contracts, integration guidance, prompt-engineering patterns, baseline-bound execution ADR, capability-routing ADR, and any current tests or validators that actually govern these surfaces.
5. Search for both supporting and contradictory rules. In particular, determine whether AP already makes a consumer-declared route canonical in the generated prompt, whether development-envelope activation is merely optional metadata, whether allowed-command examples can bypass it, and whether a machine-verifiable project operation can be replaced by copied raw commands without a declared deviation.
6. Distinguish three possible outcomes:
   - `duplicate` or `invalidated`: current public AP already owns the full invariant and the FrameNest issue was only stale consumer projection;
   - `accepted`: a real, portable AP semantic or projection gap remains;
   - `parked` or `rejected`: evidence is valid but an AP change would be disproportionate, non-portable, or would duplicate project-owned policy.

Do not move the ledger entry to `implemented` during triage. Do not infer implementation authority from `accepted`.

## Recommended candidate logical whole

If and only if triage supports a universal AP gap, recommend this one bounded logical whole to the Cooperator:

`ap-consumer-declared-execution-route-and-capability-gate-binding`

Objective:

> Make the consumer's applicable, declared execution operation and capability gate the canonical route rendered into the current authoritative Worker prompt, while preserving AP's provider/project neutrality, exact prompt authority, least privilege, and compatibility for consumers without a machine-readable route.

The logical whole must remain protocol-level and projection-level. It must not modify FrameNest, update its AP pin, deploy the NUC, open the Brave/X product horizon, rewrite local workstation scripts, or alter credentials/privilege state.

## Candidate invariant set for the Plan Worker to test, not blindly adopt

The Plan Worker should test the smallest coherent version of these invariants against current AP:

1. A consuming project owns its exact operations, commands, environment policy, capability gates, and local values.
2. Before prompt issuance, the Orchestrator resolves the governing AP baseline and the consumer-declared route applicable to the task.
3. When an applicable declared route exists and is usable, the prompt activates or names it and uses it as the canonical execution/capability path; copied raw commands must not silently appear as an equivalent route.
4. Any necessary deviation records the unavailable or unsuitable declared route, the exact alternate path, rationale, evidence class, bounded authority, and stop condition. Deviation must not become a permanent second route by accident.
5. An IDE, terminal, login shell, inherited environment variable, retained agent socket, open editor, or prior Worker session is convenience state, never authority or a guaranteed capability.
6. Capability, credentials, technical reachability, privilege state, and task authority remain separate. Each material gate is verified in the current Worker boundary without probing or exposing credentials.
7. An ambient-environment failure is classified before remediation. If a consumer-declared sanitized route applies, one focused reproduction through that route is preferred; the Worker must not rebuild, repair, or substitute the environment without explicit authority.
8. AP stays compatible with projects whose route is documented but not machine-readable. The fallback is exact project-owned prompt guidance, not an AP-invented toolchain.
9. Existing consumer pins and historical prompts retain their original meaning. Adoption of a newer AP revision is a separate consumer task.
10. Machine verification is added only where a current AP-owned structural contract already supports it or the plan proves a minimal executable change necessary. Documentation language must not pretend to enforce what no validator observes.

## First Orchestrator response

Return a concise Slovak restoration/triage report to the Cooperator. It must include:

- exact local and public identities for both repositories and the governing FrameNest AP pin;
- tree/branch/active-mutation status without touching owner work;
- exact ledger entry discovered through the declared root, its validated state, and the evidence revalidated;
- current AP semantic owners relevant to the candidate gap;
- one disposition recommendation with reasons;
- if accepted, the exact candidate logical-whole identity, scope, exclusions, risk class, and recommended Worker route;
- an explicit statement that no mutation, Worker launch, Meta write, AP publication, FrameNest pin update, or NUC deployment has occurred.

Stop after this report and wait for the Cooperator to select, reject, or revise the logical whole. Do not emit an implementation prompt at restoration time.

## Worker 01 route after explicit Cooperator selection

If the Cooperator selects the logical whole, issue one complete fresh implementation-planning prompt—not an implementation prompt—with at least these coordinates and gates:

```text
Role: WORKER
Logical whole: ap-consumer-declared-execution-route-and-capability-gate-binding
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
```

Recommend the lowest sufficient high-end reasoning profile available for a cross-document protocol semantic task; describe the functional need and keep the recommendation provider-neutral. Native Plan Mode is mandatory for this planning Worker. If unavailable, do not paste the prompt; reissue a complete plan-only prompt with `Native planning mode: not-used` and explicit read-only authority as current AP requires.

The planning Worker has read-only authority in `cisarik/ap`, `cisarik/framenest`, and the selectively relevant Meta chain. It must not edit, format, generate, commit, push, publish, deploy, modify ledgers, change pins, install dependencies, repair environments, contact production, or write Meta. It must not use subagents.

Required planning deliverable:

- a repository-grounded decision on whether AP needs a change at all;
- an exact semantic-owner and projection map, with contradictions and duplication risks;
- a minimal path allowlist and explicit forbidden paths for a later implementation Worker;
- exact proposed semantics, structural fields only if necessary, compatibility behavior, failure behavior, and examples;
- a decision on docs-only versus validator/runtime work, supported by current repository evidence;
- focused verification mapped to each changed owner, including negative/contradiction cases where relevant;
- publication, fresh independent acceptance, ledger transition, and closure sequence;
- rollback/recovery posture and residual risks;
- a Complexity Budget that limits semantic owners, projected documents, executable surfaces, test breadth, and plan cycles.

The plan must compare at least these implementation shapes:

- minimal clarification/projection of existing development-envelope and capability-gate semantics;
- one small deterministic prompt record or contradiction rule, if existing records cannot express the binding;
- no AP change, with a durable ledger disposition, if current AP already owns the invariant.

It must not default to a new command, parser, schema version, broad managed block, environment manager, credential broker, universal shell command, consumer-specific example, monolithic test suite, full repository rewrite, or new semantic owner. Any executable change requires evidence that documentation/projection cannot make the existing contract decision-complete.

## Later phase discipline

Planning approval grants no implementation authority. If a plan is accepted, issue a new complete implementation prompt with an exact baseline, allowlist, forbidden paths, validation, commit/publication authority, and stopping conditions. Use one initial implementation attempt; corrections require a separately classified bounded prompt. Publication and independent acceptance remain explicit gates. Update the consumer ledger to `implemented` only after durable public AP evidence exists and under separately granted consumer-ledger authority. FrameNest AP-pin adoption remains a later distinct logical whole.

Meta prompt/report archival is never implicit. If the project rules activate it, archive exact prompt/outcome pairs only after each outcome exists and under the declared archival route.

## Non-goals and hard stops

- No Brave extension or X media/download/posting work.
- No FrameNest product change, test rerun, NUC deployment, routine release, or production acceptance.
- No mutation of `global_sudo.fish`, remote sudoers, SSH keys, GPG-agent configuration, IDE launch configuration, Python installations, virtual environments, Poetry, uv, or shell startup files.
- No assumption that launching an integrated terminal changes the environment of an already-running Cursor Worker.
- No assumption that `SSH_AUTH_SOCK`, loader variables, a sudo timestamp, or other ambient state survives across sessions.
- No weakening of environment sanitization to make SSH or credentials convenient.
- No force push, destructive Git operation, dependency change, consumer-pin update, or secret output.
- Stop on repository identity conflict, dirty-path overlap, active unknown mutation, malformed ledger declaration/storage, unavailable required evidence, or a contradiction that changes the logical-whole boundary.

## Success condition for this handout

Success is not “AP was changed.” Success is a current-evidence disposition of the one consumer observation and, only if justified, a decision-complete Plan Worker route for the smallest portable AP improvement. The protocol remains universal; exact execution and access mechanics remain consumer-owned.
