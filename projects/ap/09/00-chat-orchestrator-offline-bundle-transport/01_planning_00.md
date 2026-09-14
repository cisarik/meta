# Fresh Planner prompt - AP ChatOrchestrator offline Git bundle transport

You are a genuinely fresh Planner Worker for the canonical Analytic Programming repository.

This is a new bounded AP logical whole.

Persistent role identity: WORKER
Worker session profile: Planner
Worker session target: fresh-worker-session
Native planning mode: required
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Implementation in same Worker session: prohibited
Plan disposition: approval-gated
Planning stop event: terminal planning report submitted
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1

Logical whole identity: chat-orchestrator-offline-bundle-transport
Worker session ordinal: 01
Worker exchange ordinal: 01

Delivery route: manual Cooperator delivery

## Repository and authority

Canonical repository:

https://github.com/cisarik/ap.git

Work only from the Cooperator's current local canonical AP checkout and independently verify its repository identity, branch, HEAD, worktree/index state, configured remote and public `main` before relying on it.

You have normal Git and GitHub access. The network restriction discussed below applies only to the ChatOrchestrator access profile being designed. It does NOT apply to you, future Planners, Implementation Workers, Audit Workers, or a full Orchestrator.

This task is planning only.

Do not edit AP files.
Do not edit Meta.
Do not commit.
Do not push.
Do not change consumer repositories or AP pins.
Do not implement the proposed CLI command.

Return one terminal planning report beginning exactly:

### Report for ORCHESTRATOR_CHAT

The report must echo the logical-whole, session and exchange coordinates above.

## Cooperator decision already accepted

The Cooperator has encountered repeated DNS/outbound Git failures in ChatOrchestrator inspection containers. A ChatOrchestrator could sometimes inspect GitHub through web/provider surfaces but could not reliably run canonical `git clone`, `git fetch`, or `git ls-remote`.

This caused a real workflow failure: continuation was blocked before routing the next Planner even though the Cooperator possessed the exact current committed repository locally.

The Cooperator has explicitly selected an offline Git transport solution for ChatOrchestrator workflows.

The intended user experience is:

```sh
~/Projects/ap/ap bundle framenest --initial
```

at the beginning of a ChatOrchestrator session, followed after subsequent commits by:

```sh
~/Projects/ap/ap bundle framenest
```

The Cooperator stores local project checkouts below:

```text
~/Projects/
```

with AP itself normally at:

```text
~/Projects/ap
```

and a project such as FrameNest at:

```text
~/Projects/framenest
```

The simple project-name syntax is an important UX requirement. Assess how to preserve this convenience without making universal AP needlessly machine-specific. A safe optional explicit-root form may be proposed if useful, but must not displace the simple form above.

## Fundamental boundary

The offline transport is specifically for the **ChatOrchestrator** access profile.

Do not redesign ordinary Git/GitHub behavior for:

- full Orchestrators;
- Planners;
- Implementation Workers;
- diagnostic or correction Workers;
- independent Acceptance or Audit Workers;
- publication Workers;
- deployment Workers.

Those actors retain normal Git repository access and normal authorized GitHub/public-ref verification.

The purpose is not to remove GitHub from AP.

The purpose is to prevent a read-only mediated ChatOrchestrator from becoming unable to orchestrate merely because its inspection container cannot reach GitHub.

## Reproduced semantic conflict to investigate

Inspect the current repository rather than trusting this prompt blindly.

In the supplied baseline audit, the following conflict was observed:

1. AP's phase-specific gates state that public-ref gates apply only when publication authority exists.
2. The public-verification section is capability-adaptive and says independent public inspection should occur when a public remote is available.
3. RF-19 manual delivery nevertheless tells a ChatOrchestrator retrieving a manually delivered report to verify the canonical public commit before reconciliation.
4. Restoration/Continuation language can also effectively require public verification before a fresh ChatOrchestrator may continue.
5. In practice this turned a ChatOrchestrator DNS failure into a hard gate before ordinary next-Worker routing even when publication itself was not the decision being made.

Determine the exact authoritative locations and all affected projections.

The desired semantic correction is:

A verified offline bundle may establish exact **committed repository evidence** for a ChatOrchestrator, including commit identity, parent relationship, tree/content and AP pin, without claiming that the commit is currently the public branch head.

`public branch state not directly observed` must remain an explicit limitation.

Lack of direct ChatOrchestrator GitHub reachability must not by itself block ordinary orchestration when the currently required claim can be established from the bundle.

If a transition genuinely requires public-ref evidence, publication equality, remote synchronization or another public claim, that claim remains unproven until an actor with the necessary GitHub capability establishes it.

A subsequent Worker or full Orchestrator with GitHub access must perform its normal repository/public gate before any mutation or push for which that gate applies.

Never silently transform Cooperator-supplied bundle evidence into independently observed public evidence.

## Dispatch and copy/paste issue to investigate

Current AP also needs reassessment of its manual-delivery rule.

The Cooperator's intended behavior is:

- ChatOrchestrator workflow: Cooperator manually ferries complete Worker prompts and results as necessary.
- Full Orchestrator with an authorized functional dispatch mechanism: the Orchestrator should normally dispatch the complete Worker prompt itself.
- The Cooperator should not be forced to act as a copy/paste courier merely because it is the first Planner of a logical whole.
- An explicit Cooperator opt-out, unavailable dispatch capability, required external fresh session, independence constraint, or another real routing reason may still require manual delivery.

Inspect ADR-0022 and ADR-0023 carefully.

Current live AP intentionally superseded ADR-0022's default agent dispatch with ADR-0023's first-manual-Planner rule. The new design will therefore need an explicit prospective decision rather than pretending the historical ADR never existed.

Recommend the smallest coherent semantic change and a new ADR rather than rewriting historical ADR bodies.

GitHub access, repository access, dispatch capability, session freshness and independence must remain separate axes.

## Required offline transport design

Plan an executable `ap bundle` surface implemented in the existing `ap` tool.

It must support at minimum:

```sh
~/Projects/ap/ap bundle <project> --initial
~/Projects/ap/ap bundle <project>
```

The command is invoked from the standalone AP checkout. It must not require AP itself to be running as the project's `.ap` submodule.

Do not weaken or regress existing `init`, `doctor`, `project`, `exec`, or `update` behavior.

### Initial export

`--initial` establishes a new ChatOrchestrator transport chain for the current exact committed project state.

The resulting ZIP must contain sufficient Git-native evidence for a ChatOrchestrator to reconstruct an inspection checkout without contacting GitHub.

At minimum investigate inclusion of:

- an exact Git bundle for the project;
- an exact bundle for the project's pinned `.ap` commit;
- a small machine-readable manifest;
- human/agent import instructions;
- suitable integrity metadata.

The exported project must reconstruct the exact commit SHA rather than synthesizing a lookalike commit.

The `.ap` checkout reconstructed offline must equal the superproject gitlink.

### Subsequent export

Running:

```sh
~/Projects/ap/ap bundle <project>
```

after later committed work creates an update ZIP.

Strongly prefer a **cumulative incremental from the chain's initial baseline**, rather than an update that depends on every immediately preceding ZIP.

Example:

```text
initial: A
update 1: A..B
update 2: A..C
update 3: A..D
```

This permits a Cooperator to miss or discard update 1 or 2 and still apply update 3 to the original initial snapshot.

The newest update should therefore supersede older incremental transport files for reconstruction purposes while remaining smaller than exporting complete history every time.

If the recorded initial commit is no longer an ancestor of current HEAD because of history rewrite, wrong project, chain reset or another incompatible state, fail closed and instruct the Cooperator to create a new `--initial`.

Do not silently invent a different base.

### Export state

Do not place transport state or generated ZIPs inside the consuming project's tracked tree.

Recommend an XDG-compatible state location, for example under:

```text
${XDG_STATE_HOME:-$HOME/.local/state}/ap/
```

or another justified equivalent.

Choose an ergonomic user-visible output location suitable for repeatedly attaching the generated ZIP to ChatGPT.

Do not overwrite older packages silently.

The manifest should make at least the following reconstructable or explicit:

- schema/version;
- transport kind;
- project identity;
- canonical configured origin;
- exact project HEAD;
- initial/base commit;
- exact AP gitlink;
- exporter AP commit/version;
- branch/detached state;
- creation time;
- included companion repositories/submodules;
- integrity values as appropriate;
- explicit statement that no public GitHub verification was performed by the export itself.

Avoid adding a parser/runtime dependency merely for fashionable serialization. Existing Git-config style syntax is acceptable if it improves POSIX-shell portability and can be parsed reliably by Git itself.

## `.gitignore`, secrets and binary-content requirement

This requirement is security-sensitive.

Do NOT make a filesystem ZIP of the project working directory.

The package should be derived from committed Git objects.

Therefore ordinary ignored/untracked content such as:

```text
.env
.venv/
node_modules/
build/
dist/
cache files
editor files
generated local binaries
```

must never enter the package merely because those files happen to exist in the working directory.

Explain accurately that `.gitignore` does not remove an already tracked file and does not sanitize Git history.

A tracked `.env`, private key or other sensitive tracked object is fundamentally different.

Also account for the fact that a complete initial Git bundle can contain historical objects that are no longer present in the current tree.

Design a fail-closed safety check for clearly suspicious tracked or historically reachable sensitive paths, with conservative semantics and no false claim that filename scanning proves absence of secrets.

Do not silently export a repository after detecting an obvious sensitive-history condition.

Do not silently remove legitimate tracked objects from a commit, because doing so would destroy exact commit identity.

Legitimate tracked binary assets that belong to the Git commit may therefore be unavoidable. Distinguish those from ignored build/runtime binaries.

Document this limitation clearly.

## Repository cleanliness and identity

Plan strict export preconditions.

At minimum consider:

- exact Git worktree root;
- physical-path resolution;
- safe project-name/path handling with no `..` traversal;
- current HEAD resolves to a commit;
- clean index and working tree for relevant non-ignored state;
- configured canonical project origin recorded;
- initialized `.ap`;
- `.ap` checkout matches the project gitlink;
- clean `.ap`;
- no mutation performed merely to export;
- no network or GitHub access performed by `ap bundle`.

A generated bundle is a read-only transport artifact. Export must not commit, push, fetch, update refs in the source repository, alter remotes, update the AP pin or mutate project content.

Temporary private staging outside project state is acceptable when safely bounded and cleaned.

## Other submodules

The project bundle contains gitlinks, not the content of arbitrary submodules.

Do not silently claim a "complete repository snapshot" while omitting required submodule content.

Design explicit behavior.

The `.ap` submodule is required for this workflow and must be handled.

For other submodules, prefer fail-closed or explicit configured inclusion over guessing, network fetching or silently omitting them.

No network fetch may be used to fill missing bundle content.

## External trace / Meta problem

This must not be missed.

AP supports an external analytic-development trace and current workflows may store prompts/reports in another Git repository such as Meta.

A project-only bundle cannot replace GitHub report retrieval if the next required `01_report_00.md` exists only in a separate trace repository.

Design the smallest **provider-neutral and repository-neutral** mechanism that lets the ChatOrchestrator transport include an explicitly configured companion trace repository when the activated workflow needs it.

Requirements:

- Do not hardcode `cisarik/meta`.
- Do not guess arbitrary sibling repositories.
- Do not scan unrelated repositories.
- Preserve the simple repeated command `ap bundle framenest` after initial configuration.
- Companion repository provenance and exact commit must be explicit in the manifest.
- Public status of that companion repository remains a distinct claim.
- A private trace must never be uploaded merely because it exists.
- Existing RF-19 trace discovery/visibility concepts should be reused where practical instead of inventing a competing semantic owner.

Investigate whether the cleanest source of this mapping is an existing explicit project declaration, a small user-level AP transport configuration established during `--initial`, or another minimal mechanism.

Recommend one design and explain why.

## ChatOrchestrator import/reconstruction semantics

A ChatOrchestrator may maintain an inspection checkout in its execution container while that environment remains available, but AP must treat the container as **ephemeral cache**, not durable continuity.

Never require conversational context memory to substitute for Git state.

Initial bundle import must permit local reconstruction without GitHub.

An incremental import must verify prerequisites and exact advertised refs/commits before advancing the inspection checkout.

Use native Git bundle capabilities where appropriate. Git bundle is explicitly designed for offline transfer and supports clone, fetch, ls-remote and prerequisite verification.

The reconstructed inspection checkout may configure canonical remote URLs for identity/reference purposes without contacting those remotes, but the protocol must never misrepresent a configured URL as observed public state.

If the inspection checkout or prerequisite objects no longer exist, the ChatOrchestrator should request a new Cooperator-generated `--initial` package rather than attempting GitHub, mirrors, pinned IP addresses or guessed recovery.

A fresh ChatOrchestrator after days or weeks may simply receive a newly generated current `--initial`; replaying a long chain of historical incremental files must not be required.

## Evidence classification

Introduce the minimum semantic distinction necessary to express:

```text
exact committed bundle evidence
```

versus:

```text
independently observed current public branch evidence
```

The bundle should be strong evidence for:

- exact included commit object;
- parent relationships represented by available objects/prerequisites;
- tree and blob content;
- changed paths/diff derivable from those Git objects;
- exact pinned AP gitlink;
- exact bundled companion-trace commit.

It must NOT by itself prove:

- current GitHub branch head;
- successful push;
- current remote-tracking state;
- Cooperator's uncommitted worktree;
- absence of newer public commits;
- sender authenticity merely because hashes are internally consistent.

Preserve this distinction everywhere.

## Restoration and continuation

Audit and propose exact updates to the places that currently make fresh continuation depend too strongly on public Git availability.

At minimum inspect:

- RF-19 manual report retrieval;
- Orchestrator / ChatOrchestrator access-profile semantics;
- Continuation Bootstrap;
- Fresh Orchestrator Restoration contract;
- AP_ORCHESTRATOR continuation guidance;
- public-verification evidence ladder;
- source-of-truth wording;
- restoration handout requirements;
- relevant glossary/FAQ/projections.

Desired behavior:

A fresh full Orchestrator with GitHub access continues to independently verify repository/public truth normally.

A fresh ChatOrchestrator supplied with a valid current initial bundle independently verifies the bundle's internal Git evidence and reconstructs its inspection state locally.

It records public state as unavailable/not-directly-observed unless it has separate actual public evidence.

It may continue ordinary routing when public equality is not a gate for that transition.

It must stop or delegate verification when the next decision genuinely requires public state.

## Copy/paste routing correction

Assess and plan a prospective correction to the current first-Planner/manual-delivery semantics.

Target behavior:

```text
ChatOrchestrator:
    manual Cooperator ferry is the normal route.

Full Orchestrator with authorized dispatch:
    direct complete-prompt dispatch is the normal route.

Full Orchestrator without usable dispatch:
    manual delivery is a fallback.

Independent/fresh routing:
    actual independence/session requirements still govern and may force
    an external/manual fresh session.
```

Do not conflate GitHub capability with dispatch capability.

Preserve Cooperator sovereignty and an explicit opt-out where appropriate.

Identify every live projection/example that would become stale if this changes.

Historical ADR text must remain historical. Add a new ADR that clearly records partial supersession instead of rewriting history.

## Presentation-signal ambiguity

Audit this secondary usability issue without allowing it to derail the transport fix.

Current AP requires a visible capsule with an emoji plus textual state, while project-owned presentation controls localization/palette.

Field use has shown that "ready", "waiting", "blocked", delivery and terminal PASS can be presented inconsistently.

Determine whether a small semantic clarification of **textual state meaning** can remove ambiguity while preserving project-owned emoji choice.

Do not make an emoji itself task authority or closure authority.

Do not casually overturn the earlier decision that universal AP does not own a project-specific emoji palette.

If this cannot be fixed coherently inside this logical whole, explicitly recommend a separate follow-up and explain the boundary.

## CLI architecture

Inspect the actual `ap` shell implementation.

Current integration commands use submodule-specific context resolution. `bundle` must additionally work when invoked from the standalone AP repository itself.

Plan the smallest clean refactor or new helper necessary.

Keep POSIX `/bin/sh` portability.

Avoid introducing an unnecessary package dependency.

Because the Cooperator specifically requires a ZIP wrapper, investigate whether Git's own facilities can create the ZIP without depending on a new external `zip` package. Do not overengineer if another already-available portable mechanism is clearly safer.

Do not introduce a large general framework.

## Validation philosophy

ADR-0015 retired the enormous monolithic AP conformance suite.

Do not recreate it.

Because `ap bundle` is new executable behavior, plan practical validation with disposable temporary Git repositories and exact smoke scenarios rather than a protocol-mirroring mega-suite.

The plan must cover at least:

- successful initial export;
- reconstruction without network;
- successful cumulative incremental export/import;
- skipping an intermediate incremental;
- dirty source refusal;
- incompatible/non-ancestor baseline refusal;
- wrong/missing `.ap` refusal;
- suspicious tracked-secret/history refusal;
- ignored `.env` not entering package;
- changed AP pin;
- missing prerequisite at ChatOrchestrator side;
- unexpected other submodule;
- configured companion trace repository;
- absence of any GitHub/network operation during export;
- existing `init`, `doctor`, `project`, `exec`, and `update` behavior remaining unchanged.

Do not add a permanent broad test surface unless you can show why the concrete new executable failure cannot be controlled proportionately under ADR-0015.

## Documentation and semantic ownership

`AP.md` remains the sole live semantic owner.

The implementation plan should identify the smallest coherent set of projections that need updating.

Inspect at least:

```text
AP.md
AP_ORCHESTRATOR.md
PROMPT_CONTRACTS.md
PROMPT_ENGINEERING_PATTERNS.md
INTEGRATION.md
README.md
FAQ.md
GLOSSARY.md
INTUITION.md
UPDATING.md
CHANGELOG.md
docs/adr/README.md
ap
```

Not every file must change. State explicitly why each changed file needs mutation and why each inspected but unchanged file does not.

Propose a new ADR for this decision. Do not alter historical ADR bodies merely to make them look current.

Existing consumers do not adopt the new behavior until they explicitly update their `.ap` gitlink.

Consumer pin update remains a separate operation after AP implementation, review, publication and acceptance.

## Planning report requirements

Return a compact but engineering-complete plan.

Your report must include:

1. Verified baseline and repository state.
2. Confirmed or disproven audit findings from this prompt.
3. Exact semantic conflicts and their authoritative locations.
4. Proposed final semantics for ChatOrchestrator bundle evidence versus public evidence.
5. Exact CLI contract for `ap bundle`.
6. ZIP/package structure.
7. Initial and cumulative-incremental algorithms.
8. State-storage and output-location design.
9. `.gitignore`, tracked-file and historical-secret treatment.
10. `.ap` and other-submodule treatment.
11. External trace/companion-repository design.
12. ChatOrchestrator reconstruction/import algorithm.
13. Full Orchestrator versus ChatOrchestrator delivery semantics.
14. Presentation-signal disposition.
15. Exact files expected to change.
16. Backward-compatibility impact.
17. Practical validation matrix.
18. Security/privacy and failure-mode review.
19. Rollback strategy.
20. Smallest implementation slices and recommended implementation Worker profile/reasoning.
21. Any finding from your own repository analysis that materially contradicts or improves this proposed design.

Do not blindly agree with the prompt. Challenge any technically incorrect assumption with repository or Git evidence.

Optimize for a simple Cooperator experience:

```sh
~/Projects/ap/ap bundle framenest --initial
# attach ZIP to fresh ChatOrchestrator

# later, after committed changes
~/Projects/ap/ap bundle framenest
# attach newest update ZIP
```

The design is successful only if the ChatOrchestrator can reconstruct exact committed project continuity without GitHub while every other AP actor keeps normal Git/GitHub behavior.

Stop after the terminal planning report. Do not implement.