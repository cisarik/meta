# Worker 5 — Fresh AP-Native External Trace Contract Implementation

## External AP Execution Trace and Meta-History Architecture

### Routing and implementation authority

Persistent role identity: You are one concrete Worker instance assigned to the single persistent `WORKER` role.

Logical whole identity: `external-ap-execution-trace-and-meta-history-architecture`

Worker number: `Worker 5`

Worker session ordinal: `05`

Worker exchange ordinal: `01`

Worker session target: `fresh-worker-session`

Fresh-session reason: the governing route has materially changed from a Meta-only implementation with `cisarik/ap` read-only to a normative mutation of the sole protocol owner `cisarik/ap`. Current AP requires fresh routing for a material route-assumption change. Worker 4's retained context is neither reused nor treated as independent evidence.

Native planning mode: `not-used`

Worker session profile: `Fresh AP Protocol Implementation Worker`

Phase: `Implementation`

Task identity: `AP-EXTERNAL-TRACE-CONTRACT-IMPLEMENT-W05-X01`

Reasoning recommendation: `High` — advisory only; Michal controls the model, agent, provider, client, and reasoning configuration.

Sub-agents/internal delegation: `not-used`

Explore-style task: `not-used`

Worker topology: `single-active`

Implementation authority: `explicit`

Exact baseline: AP commit `1b0774117e1de7ecabddc7f08d15dbaf3068b09b`.

Changed-path allowlist:

```text
AP.md
AP_ORCHESTRATOR.md
AP_WORKER.md
PROMPT_CONTRACTS.md
ARTIFACT_LIFECYCLE.md
README.md
FAQ.md
GLOSSARY.md
CHANGELOG.md
docs/adr/0014-external-analytic-trace-and-worker-exchange-identity.md
docs/adr/README.md
tests/ap_tool_tests.sh
```

Implementation boundaries: implement the smallest coherent AP-native contract for stable logical-whole, Worker-session, and exchange identity plus an explicitly activated subordinate external analytic-development trace; create one local AP candidate commit; do not mutate Meta or any consuming project; do not publish.

Independence required: `no` for implementation evidence. Your implementation evidence is non-independent. Fresh Worker 6 must independently accept the exact immutable AP candidate.

Evidence tier: `E3`

Evidence tier basis: the change is locally reversible and has no production or credential effect, but it changes AP's sole normative protocol, prompt/report structural fields, routing evidence, artifact lifecycle, and semantic enforcement used by future projects and heterogeneous models.

Authorized implementation stages: exact preflight; complete required reading; baseline validation; allowlisted implementation; focused and full validation; exact diff and semantic-owner review; one local non-amended candidate commit; post-commit validation; terminal report.

Combined implementation envelope: `allowed`

Implementation stage gates: all identity, topology, status, operation, hook, baseline, public-readback, semantic-owner, allowlist, validation, staged-set, and candidate-identity gates below must pass in order.

Independent acceptance: `required-separate-fresh-worker`

Rollback or recovery checkpoint: immutable AP baseline `1b0774117e1de7ecabddc7f08d15dbaf3068b09b`; do not use destructive recovery, history rewriting, reset, restore, clean, stash, checkout, or branch switching.

Activated stricter profile: `none`

Terminal implementation report point: after the one local AP candidate commit and all post-commit checks, before publication or any Meta archival action.

### 1. Mission

Implement the universal rule set that this logical whole has shown to be missing from canonical Analytic Programming.

A fresh vendor-neutral Orchestrator or Worker that loads the governing AP commit must be able to determine, without access to any earlier model's private memory or chat history:

- the stable logical whole, Worker session, and exchange coordinates of a task;
- when a new prompt continues the exact same healthy Worker session and when a genuinely fresh session receives the next ordinal;
- that every renewed authority grant produces a distinct exchange and terminal outcome;
- how an explicitly activated external analytic-development trace records selective causal history;
- how that trace remains subordinate historical evidence rather than protocol, task authority, acceptance, publication, closure, or repository truth;
- how prompt/outcome archival avoids self-reference and dirty-worktree loops;
- how a fresh Orchestrator restores state from current AP, canonical project evidence, and only then supporting historical trace evidence.

The mutation target is only `cisarik/ap`. `cisarik/meta` is read-only historical context and is not an implementation dependency, baseline gate, or changed repository in this task.

Produce exactly one local AP candidate commit. Do not push or publish it. Return the terminal report only in chat; do not write the current prompt or report into either repository.

### 2. Cooperator decision and ORCHESTRATOR recovery synthesis

Treat the following as accepted design decisions, not open planning questions:

1. `cisarik/ap` is the canonical repository and sole semantic owner of the universal Analytic Programming protocol.
2. AP must be vendor-neutral and usable by different Orchestrator and Worker models, providers, clients, tools, and context implementations.
3. No universal AP rule may depend on this ORCHESTRATOR's private memory, a particular chat, or a side archive being available.
4. `cisarik/meta` is only Michal's manually managed public historical trace. It must not define AP semantics or become required for ordinary AP correctness.
5. Worker 4's two implementation grants ended truthfully as `BLOCKED` before mutation. No Meta trace implementation, validator, acceptance candidate, or closure exists.
6. The earlier Meta-only implementation route is prospectively superseded because it placed universal semantics in the wrong owner.
7. Existing AP fresh/current routing, complete authority renewal, continuity anchors, terminal-report expiry, Plan-to-Execution, independent acceptance, finite convergence, restoration, evidence hierarchy, and artifact lifecycle remain valid and must be extended rather than duplicated.
8. A Worker-session ordinal identifies one concrete Worker session inside one logical whole.
9. The initial Worker session in a logical whole is `01`; each genuinely fresh Worker session receives the next contiguous two-digit ordinal; a new logical whole resets the ordinal to `01`.
10. A separately authorized exchange with the exact same healthy current Worker session retains the Worker-session ordinal and increments a contiguous two-digit exchange ordinal.
11. Exchange `01` is structurally explicit in prompt/report metadata. In the standard Markdown/Git trace projection its filename is unsuffixed; `_01` is invalid; later filename suffixes start at `_02`.
12. A changed phase or Worker session profile does not itself create a new Worker session. A different concrete Worker instance never reuses another session's ordinal.
13. Every exchange begins with one complete authoritative prompt and ends with one terminal report, cancellation, supersession, or truthful interruption record. Retained context never renews authority.
14. Fresh independent acceptance uses a genuinely fresh Worker session and a new session ordinal. Freshness alone still does not prove independence.
15. When a Markdown/Git external trace is activated, the accepted human-readable exchange sequence is representable exactly as:

```text
01_plan.md              + 01_report.md
01_plan_02.md           + 01_report_02.md
01_implementation_03.md + 01_report_03.md
02_acceptance.md        + 02_report.md
```

16. The prompt and its actual terminal report are first archived together only after the report exists. Archive time proves archival, not delivery time.
17. An interruption companion is permitted only when no terminal Worker report exists. It records safely known cancellation, interruption, or supersession facts, never impersonates the Worker, and is mutually exclusive with the report for that exchange.
18. A late or contradictory report requires explicit ORCHESTRATOR reconciliation and a prospective correction; no artifact is silently substituted or rewritten as if it were the original outcome.
19. Historical artifacts remain interpretable under their governing AP pin. Existing Meta bootstrap history must never be retroactively renamed, renumbered, squashed, or presented as if later rules governed it.
20. The trace is a selective causal history: Cooperator intent/correction, Orchestrator decision, exact issued Worker prompt, terminal outcome, reconciliation, acceptance/publication/closure where applicable.
21. The trace is not a raw transcript, hidden chain-of-thought archive, tool log, credentials store, private-data store, live specification, roadmap, issue tracker, current handoff, acceptance authority, or task-authority source.
22. Public-safe default is mandatory for public trace projections. Secrets, credentials, private URLs, environment values, private media, sensitive payloads, and unnecessary production details are excluded.
23. The universal AP contract owns semantics and exchange coordinates. A concrete external trace owns only its storage/layout projection and local validation under AP precedence.
24. AP integration, `ap.project.conf`, managed `AGENTS.md`, CLI behavior, schema v1, stable variant selection, and consumer pins remain unchanged in this candidate.
25. This ORCHESTRATOR recovery synthesis is the decision-complete closure path after the planning budget was exhausted. Do not start another planning cycle or reopen settled ownership decisions.

### 3. Previous blockers and why they do not govern this task

The latest public historical evidence is Meta commit:

```text
092b241228e67059931cf0395a51bdb693707862
```

It archives Worker 4 exchange 02. The report says implementation did not resume because `04_implementation_02.md` had been placed untracked inside the Meta worktree even though the grant required that worktree to be clean and prohibited absorbing the prompt. No implementation, test, candidate commit, publication, or acceptance occurred.

This is accepted as truthful evidence of a failed launch topology. It does not justify a third Meta implementation retry. It establishes the following prospective rule: an externally delivered launch prompt remains outside mutation-gated worktrees until its outcome exists; a separately authorized later archive transaction may then add the exact prompt/outcome pair.

Do not require local Meta cleanliness, fetch Meta, modify Meta, or reproduce the old blocker. Do not copy Meta-specific path grammar into AP as universal semantics.

### 4. Repository identity and preflight

Begin in the AP workspace supplied by Michal.

Expected canonical identity:

```text
Physical top level: /home/agile/Projects/ap
Canonical remote: https://github.com/cisarik/ap.git
Expected HEAD: 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
Expected local main: 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
Expected available origin/main: 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
Expected credential-free public main: 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
Parent: 82d9db0602cfe9177f9f2a07dd662b14b339d6cd
Tree: a5ed323188189fcf12bda9559ab55defc9e0808a
Subject: fix: enforce orchestrator-only closure contract
Expected baseline suite: 91 passed, 0 failed, exit 0
```

The expected local active branch is `docs/semantic-ownership-convergence` with no upstream while `HEAD`, local `main`, available `origin/main`, and public `main` all identify the same immutable commit. Do not switch branches or attach an upstream. If the actual clean branch is `main` at the same exact commit, record the topology and continue; a branch label alone is not semantic authority.

An isolated `.git/REBASE_HEAD` containing `573975cffc5ce94c481553168abc040d4ad39557` is accepted only as inert pre-existing metadata if ordinary Git reports no active operation, no rebase directory exists, no lock exists, and no non-sample hook would affect the task. Do not remove or alter it. Any active operation or different unexplained metadata is a blocker.

Before editing:

1. Resolve the physical top level, Git/common directory, worktree list, origin identity, branch/upstream, exact object identity, local refs, and status including ignored state.
2. Verify credential-free public `refs/heads/main` with non-interactive readback. Do not inspect credentials or credential helpers.
3. Do not fetch, pull, switch, reset, clean, stash, restore, checkout, merge, rebase, or repair baseline state.
4. Verify no owner work, untracked file, staged path, concurrent mutation, active operation, lock, or non-sample hook exists.
5. Verify `05_implementation.md` is not present anywhere inside the AP worktree. If it is, stop; do not absorb, move, delete, or commit it.
6. Resolve trusted system binaries without `cursor`, `code`, `xdg-open`, GUI, AppImage, or IDE-integrated wrappers.
7. Run the baseline suite before editing:

```text
./tests/ap_tool_tests.sh
```

Require exit `0`, `passed: 91`, and `failed: 0`. Preserve the first causal failure. A non-zero exit or traceback forbids implementation PASS.

### 5. Mandatory complete reading

Read every tracked AP file before changing protocol semantics. At minimum, read the complete current versions of:

```text
README.md
AP.md
AP_ORCHESTRATOR.md
AP_WORKER.md
PROMPT_CONTRACTS.md
PROMPT_ENGINEERING_PATTERNS.md
ARTIFACT_LIFECYCLE.md
FAQ.md
GLOSSARY.md
INFOSEC.md
INTEGRATION.md
UPDATING.md
CHANGELOG.md
ap.project.conf
ap
docs/adr/0004-fresh-slice-diagnostic-lifecycle.md
docs/adr/0005-single-live-protocol-and-pinned-submodule-distribution.md
docs/adr/0006-adaptive-orchestration-and-preflight-lifecycle.md
docs/adr/0007-worker-session-evidence-and-restoration-lifecycle.md
docs/adr/0008-worker-session-target-and-authority-renewal.md
docs/adr/0009-capability-aware-worker-routing-and-execution-gates.md
docs/adr/0010-defensive-security-profile.md
docs/adr/0011-risk-routed-planning-and-bounded-closure.md
docs/adr/0012-baseline-bound-project-execution.md
docs/adr/0013-semantic-ownership-and-convergence.md
docs/adr/README.md
tests/ap_tool_tests.sh
```

Use current `AP.md` as the sole semantic authority and `PROMPT_CONTRACTS.md` only as the structural owner of exact spellings. Treat ADRs as historical rationale. Preserve all unrelated rule families and existing executable behavior.

### 6. Required semantic implementation in `AP.md`

Add one new canonical rule family, `RF-19`, named **External Analytic Trace and Worker Exchange Identity**, unless the existing map mechanically requires the next available identifier to differ. Do not distribute the new meaning across RF-05, RF-14, and RF-17 without a single discoverable semantic home.

The RF-19 map row must link to one canonical `AP.md` section and identify only deliberate structural, operational, explanatory, historical, and executable projections.

The canonical section must define all of the following compactly and without copying subordinate prose:

#### 6.1 Stable coordinates

Every newly issued authoritative Worker prompt under the new AP identity carries:

```text
Logical whole identity: <stable lowercase kebab-case identity>
Worker session ordinal: <two-digit ordinal beginning at 01>
Worker exchange ordinal: <two-digit ordinal beginning at 01>
```

Every terminal Worker report echoes the exact same three coordinates.

Normative meanings:

- logical-whole identity names the one bounded objective/outcome and remains stable until closure, cancellation, or a materially changed objective begins a new logical whole;
- Worker-session ordinal identifies one concrete Worker session only within that logical whole;
- a new logical whole resets the session ordinal to `01`;
- a genuinely fresh Worker session receives the next contiguous session ordinal;
- one session ordinal is never reassigned to a different concrete session;
- current-session renewal retains the session ordinal and increments the contiguous exchange ordinal;
- exchange `01` is the first separately authorized prompt/outcome lifecycle in that session;
- every later renewed or reissued prompt to that session increments the exchange ordinal, regardless of phase/profile changes;
- a target/profile change alone neither creates nor preserves session identity;
- coordinates record routing and continuity decisions but do not grant authority, prove delivery, establish independence, or replace the exact `Worker session target` and continuity contract;
- ambiguous, duplicated, skipped, regressed, or contradictory coordinates are a stop-and-correction condition for newly issued prompts.

#### 6.2 External analytic-development trace

Define an external analytic-development trace as an explicitly activated historical/evidentiary projection. It may preserve the selective causal chain of Cooperator intent or correction, Orchestrator decision, exact issued Worker prompt, terminal outcome or truthful interruption, reconciliation, acceptance, publication, and closure when applicable.

It must remain:

- subordinate to the governing immutable AP identity and canonical project/external evidence;
- optional for universal AP correctness unless a consuming project's own authorized rules activate it;
- unavailable as task, Git, provider, publication, deployment, production, acceptance, or closure authority;
- non-self-authenticating: archived prose is a claim/evidence package, and archive time is not proof of delivery time;
- selective rather than a full transcript or chronological diary;
- public-safe by default when stored publicly;
- replaceable by another conforming projection because AP owns semantics, not one vendor or repository.

An unavailable, stale, private, divergent, or contradictory trace does not block ordinary AP work when canonical AP, project evidence, and required restoration evidence are sufficient. It is classified and ranked, not silently trusted.

#### 6.3 Activated Markdown/Git projection

AP owns the semantic transaction and a standard interoperable Markdown/Git exchange projection, while a concrete trace repository owns its project/date/directory layout.

For an activated standard projection:

- first exchange filenames are `NN_<phase>.md` plus `NN_report.md`;
- later exchanges in the same session are `NN_<phase>_XX.md` plus `NN_report_XX.md`;
- `NN` equals the Worker-session ordinal and `XX` equals the exchange ordinal;
- unsuffixed means exchange `01`; `_01` is invalid;
- ordinals are two-digit and contiguous;
- `<phase>` is lowercase kebab-case and cannot be `report`, `interruption`, or `handout`;
- one exchange has exactly one prompt and one mutually exclusive terminal `report` or `interruption` companion;
- a completed prompt/report pair is first archived in one atomic archival transaction after the report exists;
- for Git, atomic first archival means the pair has the same unique first-add commit;
- the prompt remains external to mutation-gated worktrees until the outcome exists unless a separately authorized workflow explicitly owns a safe staging location;
- a trace implementation may define directory layout, indexes, validators, and bootstrap exceptions, but cannot redefine these semantics.

The canonical section must describe the interruption, late-report, correction, redaction, and historical-pin rules from Section 2 without creating hidden reasoning or silent history rewriting.

#### 6.4 Restoration and durable promotion

Restoration order must be explicit:

1. governing immutable AP;
2. canonical project repository and current external/production evidence;
3. accepted/reconciled durable decisions;
4. optional supporting external trace evidence;
5. tentative plans or historical narrative.

A fresh Orchestrator must verify current truth and promote accepted universal meaning to AP, project behavior to its specification, architecture to ADRs, deferred work to roadmap/issues, and security/operational rules to their owners. The trace never replaces restoration synthesis or current durable owners.

### 7. Exact structural implementation in `PROMPT_CONTRACTS.md`

Declare the file's existing structural relationship to the new RF-19 owner.

Add exact prospective prompt and report fields:

```text
Logical whole identity: <lowercase-kebab-case>
Worker session ordinal: <NN>
Worker exchange ordinal: <NN>
```

Requirements:

- the three fields are mandatory once each in every newly issued, renewed, or reissued authoritative Worker prompt under this AP identity;
- every standard terminal report echoes them once each;
- legacy prompts/reports remain interpretable under their original AP pin and are not retroactively invalidated;
- `Task identity`, session target, profile, phase, continuity anchor, and authority remain distinct;
- a current-session prompt must advance only exchange ordinal while preserving logical-whole and session coordinates;
- a fresh-session prompt inside the same logical whole advances session ordinal and resets exchange ordinal to `01`;
- a changed objective begins a new logical whole and resets both ordinals to `01`;
- independent acceptance requires fresh targeting and the next session ordinal in that logical whole;
- report-format repair through a new authoritative exchange advances the exchange ordinal; it never overwrites the earlier outcome;
- the structural examples cover plan -> same-session implementation -> same-session correction -> fresh independent acceptance.

Add one activated trace record with exact structural spellings sufficient to distinguish configured versus inactive state without imposing a particular repository on every project. Use the smallest coherent record. It must express:

- trace disposition: configured or not-used;
- canonical trace location or discovery declaration when configured;
- trace project key and logical-whole projection identity when configured;
- historical-evidence-only authority;
- archival owner separate from Worker implementation authority;
- public/private visibility classification;
- report/interruption companion outcome;
- no self-granted status.

Do not require inactive trace fields beyond the compact disposition unless needed to reject ambiguity. Do not hardcode `cisarik/meta`, a user, a host path, a language, a provider, or a client in the universal structure.

Add the standard Markdown/Git naming and atomic first-add grammar as a structural projection linked to RF-19. Keep concrete project/date/counter directory layout outside universal AP.

Update compact prompt/report requirements, planning, implementation, acceptance, correction, publication, deployment, probe, audit, and restoration fixture shapes wherever newly issued authoritative Worker prompts or standard reports would otherwise omit the three coordinates.

### 8. Orchestrator operational projection

Update `AP_ORCHESTRATOR.md` without creating new semantics. It must operationally require the Orchestrator to:

- assign and communicate the logical-whole, Worker-session, and exchange coordinates;
- reset/increment them according to RF-19;
- use current-session continuation when healthy and proportionate, not create fresh Workers merely for imperfect reports;
- use fresh routing for material route-assumption change, independence, compromised context, or existing AP triggers;
- issue a complete new prompt for every exchange after prior authority expiry;
- maintain trace configuration as project/task context rather than universal authority;
- archive, or ask the Cooperator/archive owner to archive, the exact prompt/outcome pair only after the outcome exists;
- reconcile interruptions, late reports, corrections, redactions, and supersession prospectively;
- restore a fresh Orchestrator from governing AP and current repository evidence before optional trace history;
- never require private model memory for a durable rule;
- promote accepted meaning to its canonical owner and keep the trace historical.

### 9. Worker operational projection

Update `AP_WORKER.md` without creating new semantics. It must require a Worker to:

- verify the three coordinates and their compatibility with fresh/current routing before action;
- reject ambiguous, missing, regressed, or contradictory coordinates in a newly issued prompt;
- echo exact coordinates in the terminal report;
- treat an archive, prior prompt, retained context, filename, ordinal, or report as evidence only, never current authority;
- never infer independence from a new ordinal alone;
- never create or archive its own current prompt/outcome pair unless separately granted exact archival authority after the outcome exists;
- report interruption only through an authorized non-Worker companion owner; the Worker itself returns its terminal report when able;
- stop after the terminal report because authority expires regardless of retained context or trace availability.

### 10. Artifact lifecycle projection

Add a dedicated **External Analytic Development Trace** section to `ARTIFACT_LIFECYCLE.md` and link it to RF-19.

It must operationalize:

- historical relationship, authority, consumer, discovery, retention, promotion, cleanup, and archival owner;
- selective causal content and explicit exclusions;
- public-safe/private visibility classification;
- prompt/outcome atomic archival and the self-hosting boundary;
- truthful interruption companion;
- late report, correction, redaction, supersession, and no-silent-rewrite behavior;
- bootstrap exceptions being explicit and prospective rather than invented retroactively;
- coexistence with the rule that Git history is not a reason to keep stale live handoffs or duplicate normative documents;
- distinction from Discovery Records, restoration prompts, repository handoffs, upgrade ledgers, raw transcripts, ADRs, specs, and issues.

Do not state that every AP consumer must maintain an external trace. State that an activated project may use one conforming trace and that absence does not weaken current AP authority or required evidence.

### 11. Explanatory and historical projections

#### `README.md`

Add only the minimum discovery information needed to show:

- AP owns the universal trace/session-exchange meaning in `AP.md`;
- `PROMPT_CONTRACTS.md` owns exact coordinates and standard projection grammar;
- `ARTIFACT_LIFECYCLE.md` owns operational trace handling;
- an external trace is subordinate and optional unless project rules activate it.

Do not add a Meta repository link or turn README into a second protocol.

#### `FAQ.md`

Add concise answers to:

- Why not open a fresh Worker after every imperfect report?
- How are multiple prompts to the same Worker session identified?
- Is an external trace required, and can it grant authority?
- Can a fresh Orchestrator rely on the previous model's memory?
- Why are prompt and outcome archived only after the outcome exists?

Each answer links to the canonical AP semantic owner.

#### `GLOSSARY.md`

Add compact explanatory definitions for:

- Logical Whole Identity;
- Worker Session Ordinal;
- Worker Exchange Ordinal;
- External Analytic Development Trace;
- Trace Projection;
- Interruption Companion;
- Atomic Archival Transaction.

Definitions must not create rules or conflict with existing session target, continuity anchor, restoration prompt, repository handoff, Discovery Record, or evidence terms.

#### `CHANGELOG.md`

Add one current delivery entry summarizing the prospective AP-native contract, compatibility, unchanged CLI/schema/consumer pins, and required fresh independent acceptance. Do not claim publication or closure.

#### ADR-0014 and ADR index

Create `docs/adr/0014-external-analytic-trace-and-worker-exchange-identity.md` as historical rationale with:

- Status: Accepted only as an implementation candidate decision record; do not claim public acceptance or closure in prose;
- context from repeated fresh-session routing, private-memory dependence, and dirty-worktree self-hosting failure without naming a vendor/model/user/private path;
- decision: AP-native coordinates, optional subordinate trace, standard Markdown/Git projection, atomic after-outcome archival, public-safe selective history, restoration order, and compatibility;
- semantic ownership and projections;
- consequences;
- rejected alternatives, including Meta-only semantics, raw transcripts, mandatory external service/database, fresh Worker after every report, archive-as-authority, pre-archiving prompts in mutation-gated worktrees, and hardcoded project/vendor identity;
- compatibility and migration;
- links to canonical live owners.

Update `docs/adr/README.md` with the new ADR and correct relationship status. ADR history does not own live semantics.

### 12. Executable enforcement in `tests/ap_tool_tests.sh`

Extend the dependency-free shell suite. Do not add another test framework, generated artifacts, repository fixtures, dependencies, or production/network mutation.

Required positive enforcement:

1. RF-19 exists once and links to one canonical AP section.
2. Every deliberate projection links back to RF-19 and declares its relationship.
3. Prompt/report structural examples include one valid logical whole with:
   - Worker session `01`, exchange `01`, plan;
   - same session `01`, exchange `02`, implementation;
   - same session `01`, exchange `03`, correction or changed phase;
   - fresh Worker session `02`, exchange `01`, independent acceptance.
4. Current-session renewal preserves logical whole/session coordinates and increments exchange.
5. Fresh-session routing inside one logical whole increments session and resets exchange.
6. A changed objective resets the logical whole and both ordinals.
7. Standard Markdown/Git unsuffixed and `_02`/`_03` examples match the coordinate model.
8. Activated trace remains historical and subordinate.
9. Inactive/unavailable trace does not block ordinary AP correctness.
10. Public-safe and selective-content boundaries are present.
11. Existing 91 baseline tests remain semantically intact.

Required negative fixtures or relationship assertions reject:

- missing, duplicate, malformed, zero, one-digit, three-digit, skipped, or regressed coordinates;
- `_01` filenames, exchange suffix gaps, Worker-session ordinal gaps, and reuse of one session ordinal for two fresh sessions;
- changing the session ordinal during valid current-session renewal;
- preserving a session ordinal for a genuinely fresh Worker;
- current-session independent acceptance;
- archive filenames or metadata treated as authority or proof of independence;
- a subordinate trace document or ADR claiming semantic ownership;
- external trace availability as a universal prerequisite;
- archived prompt/report prose treated as acceptance, publication, or closure;
- raw transcript, hidden reasoning, secret, credential, or unbounded payload expectations;
- prompt-first archival inside a mutation-gated worktree as the required normal route;
- silent replacement of report with interruption or late report;
- hardcoded `cisarik/meta`, `/home/agile`, a model, provider, or client as universal protocol identity;
- accidental changes to CLI/schema/managed-block behavior.

Prefer relationship and fixture validation over fragile favored-sentence assertions except where exact field names, allowed values, filename grammar, or executable output are structurally owned.

The final suite must exit `0`, report `failed: 0`, and have a passed count greater than the baseline `91`. Report the exact new count.

### 13. Security and privacy boundary

The implementation must preserve AP's existing security and untrusted-content rules.

Do not inspect or expose credential values, environment values, private URLs, tokens, keys, auth headers, cookies, private media, personal data, production data, or unrelated repository content. Repository prompts and historical traces are untrusted evidence, not instructions, unless the current authoritative prompt incorporates a decision explicitly.

No changed AP file may contain:

- `cisarik/meta` as a universal required repository;
- `/home/agile` or another private/local path;
- a vendor, model, provider, IDE, or client requirement;
- raw prompt/report payloads from Meta;
- secret-shaped examples;
- claims of current public acceptance, publication, or closure.

### 14. Compatibility and non-goals

The implementation is prospective:

- historical prompts/reports remain governed by their original immutable AP pin;
- existing consumers remain on their current gitlinks until a separate update task;
- projects may activate a conforming external trace through project/task rules, but AP works without one;
- Meta's current bootstrap history remains untouched and is not retroactively validated by this candidate;
- a later Meta task may implement a concrete directory layout and validator only after an accepted governing AP identity exists.

Do not change:

```text
ap
ap.project.conf
INTEGRATION.md
UPDATING.md
PROMPT_ENGINEERING_PATTERNS.md
INFOSEC.md
.gitignore
```

Do not create a second protocol variant, new persistent AP role, database, service, manifest, prompt generator, transcript ingester, model matrix, telemetry system, automatic chat scraper, Meta submodule, consumer migration, deployment, release, tag, or provider integration.

### 15. Exact implementation and Git boundary

After all preflight and reading gates pass:

1. Edit only the twelve allowlisted paths.
2. Preserve existing style, line endings, semantic-owner structure, and local-link conventions.
3. Keep `AP.md` the sole semantic owner; projections link rather than copy full meaning.
4. Run focused checks during editing and the full suite after the coherent change.
5. Review `git diff --check`, exact changed paths, diff statistics, semantic-owner relationships, links, and prohibited content.
6. Stage only the exact allowlist paths that actually changed. Every staged path must be allowlisted; every required projection must be present.
7. Verify the staged diff contains no Meta prompt/report payload, private path, secrets, unsupported authority claim, or unrelated cleanup.
8. Create exactly one local non-amended commit with subject:

```text
feat: define external analytic trace exchanges
```

9. Do not amend, rebase, merge, cherry-pick, tag, push, publish, switch branch, or update remote refs.
10. After commit, rerun the full suite from the candidate, verify clean status, exact parent, tree, subject, changed paths, and local/public divergence.

If Git author identity is unavailable, stop after successful validation with the coherent worktree intact and report `BLOCKED`; do not invent identity or change global configuration.

### 16. Required validation

At minimum run and report:

```text
./tests/ap_tool_tests.sh
git diff --check
git status --short --branch
git diff --stat 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
git diff --name-status 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
git diff --check 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
git show --format=fuller --stat --summary HEAD
git diff-tree --no-commit-id --name-status -r HEAD
git rev-parse HEAD^ HEAD HEAD^{tree}
git ls-remote https://github.com/cisarik/ap.git refs/heads/main
```

Use safe quoting appropriate to the active shell. Public readback must remain credential-free and non-interactive. Preserve exit codes and the first causal failure. A traceback, non-zero required check, missing negative test, dirty post-commit status, wrong staged set, or public-main movement forbids `PASS`.

### 17. Acceptance criteria

Implementation may report `PASS` only if all are true:

1. AP baseline identity and preflight matched exactly.
2. Baseline suite passed `91/0` before edits.
3. Exactly one local candidate commit exists above baseline with the required subject.
4. Changed paths are a subset of and semantically complete within the exact allowlist.
5. `AP.md` contains one discoverable canonical RF-19 semantic owner.
6. Structural, operational, explanatory, historical, and executable projections declare the correct relationship and link to the owner.
7. New prompt/report coordinates are exact, prospective, vendor-neutral, and compatible with fresh/current routing.
8. The external trace is optional, selective, public-safe, historical, subordinate, and non-self-authenticating.
9. The standard Markdown/Git projection supports the accepted same-session sequence and atomic after-report archival without imposing Meta directory layout.
10. Restoration and durable-promotion order prevents private-memory or archive authority.
11. Positive and negative enforcement covers the required matrix.
12. Full suite exits `0`, `failed: 0`, with passed count greater than `91` before and after commit.
13. No non-allowlisted file, CLI/schema behavior, consumer, Meta, production, provider, deployment, or public ref changed.
14. Worktree is clean at the exact candidate.
15. Public AP `main` remains exactly `1b077411...`.
16. The report identifies fresh Worker 6 as the required independent acceptance route and does not claim logical-whole closure.

### 18. Self-hosting and Meta archival boundary

Do not create, copy, edit, stage, or commit `05_implementation.md`, `05_report.md`, or any Meta file.

The current prompt is delivered externally. After your terminal report expires your authority, Michal may use separately held archival authority to add the exact prompt and exact report together to Meta. That archival commit is not part of the AP candidate, does not grant AP authority, and need not be referenced by its own report.

Fresh Worker 6 acceptance will target your exact AP candidate commit, not a Meta archive commit. Any later Meta trace implementation is a separate bounded task after AP acceptance/publication and must conform to the accepted governing AP identity.

### 19. Stop conditions

Stop `BLOCKED` before mutation, or preserve exact state after a later blocker, if:

- this is not a genuinely fresh Worker 5 session;
- Native Plan Mode is active;
- repository identity, topology, branch relationship, baseline, local/public refs, status, ignored state, operation, lock, hook, or owner work differs materially;
- `05_implementation.md` is present inside the AP worktree;
- baseline suite does not exit `0` with `91 passed` and `0 failed`;
- required reading is unavailable;
- implementation would require a non-allowlisted path or change to CLI/schema/consumer behavior;
- semantic ownership cannot remain singular in `AP.md`;
- the design requires Meta, private memory, a vendor, model, provider, client, or external service for universal AP correctness;
- a command would expose credentials/private data or perform unauthorized mutation;
- staged paths, tests, links, negative fixtures, candidate identity, clean status, or public readback fail;
- another process or person mutates the AP worktree during the task;
- implementation cannot produce a coherent candidate without reopening planning.

Do not repair a pre-existing repository difference. Do not weaken a gate. Do not continue into acceptance or publication.

### 20. Terminal report contract

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Then include exactly one actual value on each line:

```text
Logical whole identity: external-ap-execution-trace-and-meta-history-architecture
Worker session ordinal: 05
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS | not-applicable
Result artifact or commit: <exact AP candidate commit or not-applicable>
Result evidence: <exact evidence summary>
Logical-whole closure: not-closed
Report justification: new-mutation | new-evidence | new-material-risk | changed-external-state
Authority expiry: implementation authority expired at this terminal report
```

Use one value, not the literal alternatives. For successful implementation use `new-mutation` and `implementation-PASS`.

The report must include:

1. implementation status;
2. route, fresh-session, and capability observations without inventing model/reasoning facts;
3. exact baseline and public readback;
4. baseline suite result;
5. changed paths and semantic ownership;
6. RF-19 canonical semantics;
7. prompt/report coordinate structure;
8. Orchestrator and Worker operational projections;
9. artifact lifecycle and restoration behavior;
10. external trace activation and Meta boundary;
11. Markdown/Git projection and atomic archival;
12. compatibility and unchanged surfaces;
13. positive/negative test evidence and exact final count;
14. security/public-safety evidence;
15. exact candidate SHA, parent, tree, subject, stat, and path list;
16. post-commit cleanliness and public-main non-movement;
17. deviations, risks, and deferred work;
18. smallest next step: ORCHESTRATOR reconciliation followed by fresh Worker 6 independent acceptance of the exact candidate.

End with:

```text
Start and end commits: AP 1b0774117e1de7ecabddc7f08d15dbaf3068b09b / <candidate-or-baseline>; Meta not mutated
Changed files and purpose: <exact allowlisted list or none>
Tests and validation: <exact commands, exit statuses, passed/failed totals>
Commit and push result: <local candidate result>; no push authorized or performed
Deviations, risks, or missing evidence: <exact list or none>
Resolved Execution Issues / Near-Misses: <exact list or none>
Pre-Existing Failure Classification: Worker 4 Meta-only exchanges remained BLOCKED before mutation; no prior AP or Meta implementation candidate existed
```

Your authority ends at this terminal report. Retained context does not renew it. A Worker never accepts its own candidate or closes the logical whole.
