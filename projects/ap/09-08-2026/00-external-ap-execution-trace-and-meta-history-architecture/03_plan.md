# Worker 3 — Read-Only Architecture Planner after Repository-Path Reconciliation

## External AP Execution Trace and Meta-History Architecture

💡 Native Plan Mode

### Routing and planning record

Persistent role identity: You are one fresh Worker instance assigned to the single persistent `WORKER` role.

Worker number: `Worker 3`

Worker session target: `fresh-worker-session`

Native planning mode: `required`

Worker session profile: `Read-Only Architecture Planner after Repository-Path Reconciliation`

Phase: `Implementation Planning Recovery`

Task identity: `META-TRACE-V1-PLAN-W03`

Logical whole: `External AP Execution Trace and Meta-History Architecture`

Reasoning recommendation: `High` — advisory only; Michal controls the model, agent, and reasoning configuration.

Planning cycle: `targeted-revision`

Prior planning report: `02_report.md`, SHA-256 `4de6efdcc754adfe8a27ae9f0f4b9b89208b001607f6559785030d2867cdfc18`

Targeted revision basis: `new-repository-or-external-evidence`

Changed decision boundary: inspect the already existing Meta checkout only at `/home/agile/meta`; do not look for or create `/home/agile/Projects/meta`. Accept public Meta `main` at `980d909...` as the reconciled public baseline when independently re-established. A narrowly matching pre-existing local correction to `01_report.md`, whether unstaged or committed only in the local checkout, is protected Cooperator work and is not by itself a planning blocker. This prompt grants no filesystem or repository mutation at all.

Preserved unaffected decisions: all fixed Cooperator decisions, repository authority boundaries, public-safety requirements, planning deliverables, implementation prohibition, publication separation, and ORCHESTRATOR-only closure.

Automatic targeted revisions used: `1`

Recovery authority note: Worker 1 and Worker 2 each returned `PLAN BLOCKED`; neither produced an architecture plan or exercised implementation, repository-edit, candidate-acceptance, publication, deployment, or closure authority. Worker 2 was the one automatic targeted revision. This Worker 3 session exists only because Michal supplied new repository evidence, corrected the path, and explicitly continued after the resulting ORCHESTRATOR decision; it is not a second automatic retry or a reinterpretation of unchanged evidence.

Planning layer: `implementation-planning`

Orchestration planning owner: `ORCHESTRATOR`

Worker planning scope: `repository-grounded smallest-v1 architecture for AP execution history stored in cisarik/meta`

Plan disposition: `approval-gated`

Implementation in same Worker session: `prohibited`

Planning stop event: `terminal planning report submitted`

Execution authority event: `explicit ORCHESTRATOR prompt with Native planning mode: not-used`

Post-plan implementation session: `fresh-worker-session`

Maximum plan-only cycles: `1`

### 1. Mission

Produce one complete, repository-grounded implementation plan for the smallest coherent v1 architecture in `cisarik/meta`. The architecture must preserve historical execution traces of AP-assisted work without turning Meta into a second AP protocol or a source of current task authority.

The project currently being advanced is `cisarik/ap`: this logical whole belongs under `projects/ap/...` and concerns the AP protocol's use and history. `cisarik/meta` is the subordinate storage/implementation repository for that history, not the active protocol project and not a replacement for AP. `cisarik/framenest` at `/home/agile/Projects/framenest` is a later AP consumer and is out of scope.

This remains a strictly read-only planning task. Do not implement, edit repository content, format, create project artifacts, delete, rename, stage, commit, push, publish, deploy, fetch, pull, switch, reset, clean, stash, configure, or otherwise mutate either repository.

Return one terminal report in chat for the ORCHESTRATOR to reconcile and for Michal to save as:

```text
projects/ap/09-08-2026/00-external-ap-execution-trace-and-meta-history-architecture/03_report.md
```

Do not create `03_report.md` yourself.

### 2. Role and authority boundary

The stable AP roles remain exactly:

- `COOPERATOR`: Michal; owns material product/protocol choices, subjective acceptance, privacy/public-exposure choices, irreversibility, cost, and residual risk.
- `ORCHESTRATOR`: owns routing, authority grants, report reconciliation, phase transitions, and deterministic logical-whole closure.
- `WORKER`: your role, limited to this prompt.

Planner, Implementer, Acceptance Worker, Repair Worker, Publication Worker, Teacher, and a possible future Meta-History Curator are session profiles of `WORKER`, not new roles.

Your terminal report expires all authority in this prompt. You receive no implementation, candidate-acceptance, publication, deployment, provider, production, account, credential, or closure authority. Never declare this logical whole closed.

### 3. Repository and evidence authority

There are two separate repositories:

1. `cisarik/ap`
   - canonical remote: `https://github.com/cisarik/ap.git`;
   - owns the universal AP protocol and its live executable/normative rules;
   - is read-only governing evidence in this logical whole;
   - must not be modified.

2. `cisarik/meta`
   - canonical remote: `https://github.com/cisarik/meta.git`;
   - owns historical execution traces of AP use;
   - is the only future implementation target;
   - is subordinate to current AP and current canonical project evidence;
   - must not redefine AP.

Preserve this evidence order when claims conflict:

1. current applicable production/external readback;
2. current canonical/public project Git objects and direct project evidence;
3. current canonical AP protocol at the governing immutable identity;
4. independent acceptance of an exact immutable candidate;
5. reconciled ORCHESTRATOR decisions and closure outcomes;
6. archived Worker reports as claims/evidence packages;
7. archived launch prompts as proof that instructions were issued;
8. tentative plans, brainstorming, legacy traces, and inferred narrative.

Meta history must never self-authenticate execution or silently grant current implementation, publication, deployment, provider, production, or closure authority.

### 4. Exact expected identities

Independently re-establish these facts. They are expected evidence, not a substitute for inspection.

#### AP canonical object

```text
Remote: https://github.com/cisarik/ap.git
Public/canonical main: 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
Parent: 82d9db0602cfe9177f9f2a07dd662b14b339d6cd
Tree: a5ed323188189fcf12bda9559ab55defc9e0808a
Subject: fix: enforce orchestrator-only closure contract
```

The preceding logical whole, `Semantic Consolidation and Protocol Compression`, is already final `CLOSED: PASS`. Do not reopen it.

Worker 1 observed this pre-existing local AP state at `/home/agile/Projects/ap`:

```text
active branch: docs/semantic-ownership-convergence
active branch upstream: none
HEAD: 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
local main: 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
local origin/main: 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
public main: 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
worktree: clean
```

ORCHESTRATOR reconciliation: if you re-establish that exact clean state, classify it as an accepted read-only continuation at the exact canonical object. The active topic-branch name and missing upstream are not blockers for reading immutable content and do not require a branch switch. Do not claim the active branch itself is canonical `main`; do not modify, switch, configure, fetch, or repair AP. Any object, content, ref, cleanliness, lock, operation, origin, or public-readback difference remains a real finding.

#### Meta canonical object

```text
Remote: https://github.com/cisarik/meta.git
Expected public/main HEAD: 980d909ac5d4906a109890677329280e1a9ad022
Parent: 52faf2cbc64526e4a30e7cd94b8efa4105f55505
Tree: 16dcf0b84890209dd367e6ab7df36835b2c78afb
Subject: Refactor project structure for improved organization and clarity
Expected visibility: credential-free publicly readable
```

Expected tracked files:

```text
README.md
projects/ap/09-08-2026/00-external-ap-execution-trace-and-meta-history-architecture/00_handout.md
projects/ap/09-08-2026/00-external-ap-execution-trace-and-meta-history-architecture/01_plan.md
projects/ap/09-08-2026/00-external-ap-execution-trace-and-meta-history-architecture/01_report.md
```

Expected content facts:

- `README.md` contains exactly `# meta` without a trailing newline; SHA-256 `9aa5fb381a14022307a703b595adb5e4a95e366c0a69083245ece6411216a2a4`.
- `00_handout.md` has 581 lines; SHA-256 `a1aa4fe6a5ab4d6cb320ab202dda3c64ee097ad1f943c5f11ba746894ae93a9d`; Git blob `c9b52749034eda5f0f71b2082dfe43c156048a1f`.
- public `01_plan.md` has 552 lines; SHA-256 `8875541a2a9ba441c8dabd6eba684bc723b5257f3346eced8376bcde935d927a`; Git blob `c93427000b328e015ffe3517fd1805a40be446eb`.
- public `01_report.md` has 820 lines; SHA-256 `b44a4587011503847846437d1279d143132744ad3b9442e00d188771d2ed6c4a`; Git blob `37d591c33824d21679b6157e095dfccbe0afe2dd`.
- the public `01_report.md` contains Worker 1's terminal report followed by excessive blank lines and a pasted copy of `00_handout.md`; this is a known malformed historical artifact, not a second handout and not current authority;
- Michal states that `01_report.md` has been corrected in `/home/agile/meta`; inspect and characterize the exact local delta without changing it or assuming its bytes;
- the three-commit public history begins at `24b358416e87ad83c1b7213fe7d7c298535d7730`, continues through `52faf2cbc64526e4a30e7cd94b8efa4105f55505`, and ends at the expected HEAD;
- no other tracked file, `AGENTS.md`, license, dependency manifest, test suite, automation, or configured non-sample hook exists at that baseline.

### 5. Corrected physical preflight and protected local correction

Begin in the AP workspace. Resolve trusted system commands and the physical AP top level without using an editor/AppImage wrapper.

Inspect only the exact Meta candidate supplied by Michal:

```text
/home/agile/meta
```

Do not broadly scan Michal's home, `/home/agile/Projects`, or unrelated projects. Do not inspect or create `/home/agile/Projects/meta`. If `/home/agile/meta` is absent, is not the standalone checkout of the exact canonical Meta remote, or contains unrelated unexplained owner work, return `PLAN BLOCKED` without creating or repairing anything.

The reconciled public baseline is exact commit `980d909ac5d4906a109890677329280e1a9ad022`. Directly inspect the local checkout before deciding whether it is usable. The following narrowly bounded local states are planning-compatible when proved exactly and reported without mutation:

1. clean local `HEAD` at public `980d909...`;
2. local `HEAD` at `980d909...` with the only tracked worktree/index delta confined to `01_report.md`, where the delta is the Cooperator's correction of the known appended-handout/malformed-tail defect;
3. a clean unpublished local descendant of `980d909...` whose complete commit delta is confined to that same `01_report.md` correction;
4. the same correction plus only the untracked `02_plan.md` and/or `02_report.md` historical inputs, provided their exact identities and contents are reported and they are not treated as current authority.

Do not assume a correction is narrow merely from its filename. Inspect the exact diff, line count, hash, terminal-report boundary, commit graph, status, and index/worktree separation. If the correction changes Worker 1's substantive terminal claims rather than only removing the accidentally appended material and normalizing the malformed tail, report the exact safe summary and return `PLAN BLOCKED` for ORCHESTRATOR reconciliation. Do not print unsafe content.

Any `02_plan.md`, `02_report.md`, or later prompt/report outside the checkout is supplied historical input only. Do not copy it into Meta in this session. The future implementation plan must preserve the correction and must not overwrite, reset, clean, stash, amend, or silently absorb Michal's work.

For both resolved repositories, inspect:

- physical top level, absolute Git directory/common directory, standalone topology, and `git worktree list --porcelain`;
- safe canonical origin identity;
- active branch, upstream, exact HEAD/parent/tree/subject, local refs, and ahead/behind where meaningful;
- index, tracked worktree, ordinary untracked, and ignored state;
- active Git operations and lock markers without removing them; in AP, an isolated `.git/REBASE_HEAD` containing `573975cffc5ce94c481553168abc040d4ad39557` is a reconciled pre-existing stale metadata marker rather than an active rebase only if `git status` reports no active operation and no rebase directory/other operation evidence exists;
- tracked inventory, repository instructions, hooks, dependencies, tests, and automation;
- credential-free, non-interactive public `refs/heads/main` readback for only the two canonical remotes.

Classify evidence as direct local, direct public, Worker-observed, inferred, or missing. Never use public evidence to claim local cleanliness, and never use local `origin/main` alone to claim public state.

### 6. Mandatory current-source reading

Read the complete current versions at the verified AP object:

```text
AP.md
AP_ORCHESTRATOR.md
AP_WORKER.md
ARTIFACT_LIFECYCLE.md
PROMPT_CONTRACTS.md
INFOSEC.md
INTEGRATION.md
GLOSSARY.md
docs/adr/0013-semantic-ownership-and-convergence.md
tests/ap_tool_tests.sh
```

Follow directly linked owners only where necessary. Focus on roles/authority, planning gates, semantic ownership, source-of-truth hierarchy, artifact lifecycle/retention, prompt/report structure, independent acceptance, finite correction, ORCHESTRATOR-only closure, public Git evidence, INFOSEC/redaction, and consumer boundaries. Do not conduct a broad re-audit of the closed predecessor.

Read all current public Meta content and its complete three-commit public history. Also read the exact protected local `01_report.md` correction and any narrowly allowed local historical inputs described in section 5. Treat `00_handout.md`, launch prompts, and reports according to their evidence classes; none self-authenticates repository execution or grants current authority.

### 7. Fixed Cooperator decisions

The plan must preserve these decisions.

#### Path grammar

```text
projects/<project>/<DD-MM-YYYY>/<logical-whole-counter>-<logical-whole-slug>/
```

- `<project>` is the project whose AP-assisted work is traced.
- `DD-MM-YYYY`, including leading zeroes, is the logical whole's opening date.
- the two-digit counter is zero-based within the exact project/opening-date pair.
- the slug is stable lowercase kebab-case.
- artifacts remain flat inside one logical-whole directory; no `prompts/` or `reports/` subdirectories.
- lexicographic path order is not treated as universal chronological order.

This whole's exact directory is:

```text
projects/ap/09-08-2026/00-external-ap-execution-trace-and-meta-history-architecture/
```

#### Artifact grammar

```text
00_handout.md
<NN>_<phase>.md
<NN>_report.md
```

- `00` is not a Worker number; there is no automatic `00_report.md`; do not rename it to `00_handoff.md`.
- Worker numbering begins at `01`, resets per logical whole, and advances for every fresh Worker even when a phase repeats.
- `<NN>_<phase>.md` is Worker `<NN>`'s authoritative launch prompt; it has no redundant prompt suffix.
- `<NN>_report.md` is that Worker's one terminal report.
- the phase is a bounded session profile/function, never a new stable role.
- prefer `acceptance` over vague unbounded `audit` for a finite gate.
- create no placeholders for phases that never occur.
- the outgoing ORCHESTRATOR creates the next whole's `00_handout.md` only after deterministic closure of the current whole.

#### Historical boundary and usability

- This is the first whole required to follow the convention from its beginning.
- Do not backfill, rename, normalize, or invent older AP/FrameNest artifacts.
- Preserve explicit legacy absence and any honest interruption/missing-artifact state.
- Optimize for Michal manually using a project window plus `cisarik/meta/projects/<project>`, and for a future high-context model reconstructing decisions safely.
- Prefer low ceremony; no database, service, workflow engine, web app, vector index, embeddings system, or agent daemon.

### 8. Required architectural decisions

Produce a decision-ready smallest-v1 plan, not another topic list. Resolve and justify:

1. Minimum root/project documentation and the one Meta-owned normative document for path grammar, filename grammar, lifecycle, authority hierarchy, correction, and public safety.
2. How subordinate explanatory/operational/historical/executable projections avoid duplicating that owner or copying AP semantics.
3. Whether plain Markdown plus Git is sufficient or one small machine-readable manifest is materially justified; if justified, define exact path, format, required/optional fields, invariants, update owner, and the failure prevented by every field.
4. How title, project, opening date, daily ordinal, status, Worker number/profile, result identity, predecessor/successor, decisions, reconciliation, closure, and publication evidence are represented without inconsistent duplication.
5. Whether a minimal per-whole status/decision artifact is required now and how it differs from deferred summarization.
6. Interrupted/no-report Workers, abandonment, findings, repairs, repeated phases, unpublished endings, gaps, and whether numbers are ever reused.
7. Clarifications or additional instructions sent to an active Worker while retaining one launch prompt and one terminal report without silently rewriting issued instructions.
8. Corrections/amendments to committed traces, ordinary Git history, immutable historical claims, redaction disclosure, missing artifacts, and derived records.
9. Public-repository prohibitions and safe handling when an incoming Worker/Cooperator artifact already contains unsafe data.
10. Validation of dates, per-day ordinals, slugs, flat filenames, prompt/report pairing, exceptional artifacts, lifecycle rules, and false-positive boundaries.
11. Whether a dependency-free lightweight validator/tests are warranted now; define responsibilities, portability, CLI/exit semantics, fixtures, non-goals, or give an equally precise rejection.
12. Whether generated indexes are necessary; default to no unless a concrete navigation failure requires one.
13. Honest self-recording bootstrap for `00_handout.md`, `01_plan.md`, the corrected blocked `01_report.md`, `02_plan.md`, the blocked `02_report.md`, `03_plan.md`, and later artifacts without retroactively claiming later rules governed earlier commits. Distinguish the malformed public `01_report.md`, Michal's protected local correction, and the future publication of that correction without rewriting ordinary Git history.
14. Exact Meta-only changed-path allowlist, ordered implementation verticals/commits, rollback/recovery implications, stop conditions, independent acceptance, publication boundary, and ORCHESTRATOR closure boundary.
15. Explicit deferral of summarization/curation, derived indexes, search, meta-on-meta tracing, AP marketing/site work, and all consumer-project changes.

For every proposed file, field, script, test, dependency, generated output, or automation, name its semantic owner/AP relationship, consumer, discovery path, lifecycle/retention class, update/cleanup trigger and authority, concrete prevented failure, and why a lighter alternative is insufficient.

### 9. Required terminal-plan content

Include:

1. requirement-to-owner map for every fixed decision;
2. complete proposed smallest-v1 repository tree marking existing, modified, and new paths;
3. exact future changed-path allowlist in `cisarik/meta` only, with no globs hiding unknown files;
4. outline and ownership declaration for every changed path;
5. artifact lifecycle/state model covering open, active, interrupted, reported, finding/accepted, repaired, publication when applicable, abandoned, and ORCHESTRATOR-closed states without forcing phases;
6. exact raw-artifact, clarification, amendment, correction, redaction, missing-artifact, and derived-record handling;
7. manifest and validator/test decisions at field/behavior level;
8. public-safety rules with synthetic positive/negative examples containing no real secret;
9. bounded implementation verticals/commits with baseline, paths, validation, rollback/recovery, and stop condition;
10. fixed independent acceptance matrix for the exact future candidate, including honest bootstrap proof;
11. publication and closure boundaries without granting them;
12. deferrals, risks, and one smallest next step.

If one material Cooperator choice cannot be resolved, present exact options, recommendation, trade-offs, stable plan portions, and whether it blocks a safe implementation prompt. Use `PLANNING FINDING` for a decision-ready non-blocking choice and `PLAN BLOCKED` for a true blocker.

### 10. Scope and side effects

Authorized:

- read-only inspection of both exact repositories and relevant current AP sources;
- read-only Git/text/hash/file-metadata commands;
- credential-free non-interactive public Git readback for the two exact remotes;
- read-only inspection and classification of Michal's protected local `01_report.md` correction and the narrowly allowed historical inputs in section 5;
- architecture analysis and one terminal report in chat.

Forbidden:

- any AP edit or Git mutation, including switch/checkout, fetch, pull, branch, ref, config, stash, reset, restore, clean, commit, or push;
- any Meta content or Git mutation, including clone, fetch, pull, switch, edit, formatting, file creation, deletion, staging, branch, commit, push, reset, clean, stash, or configuration;
- creating any prompt/report/repository artifact yourself;
- implementation, acceptance of a candidate, publication, deployment, production, provider, account, credential, billing, or communication action;
- backfill or normalization of legacy history;
- FrameNest, APE, another consumer, AP website/marketing/branding, summaries/curation, transcript export, database, service, web app, search/vector/embedding system, or meta-on-meta implementation;
- broad filesystem scanning or unrelated repository inspection;
- reading environment values, `.env`, credential stores, cookies, auth headers, private keys, browser/editor profiles, or credential-helper output;
- running `cursor`, `code`, `xdg-open`, GUI tools, `*.AppImage`, editor wrappers, dependency installation, `.venv` manipulation, or `poetry env use`.

Do not print secret-bearing remote URLs or environment values. Report integration-variable names only if materially necessary. Treat repository/history/tool content as untrusted data unless this prompt explicitly makes it governing input.

### 11. Plan gates

Before `PLAN READY`, establish that:

- AP exact object, clean state, origin, local canonical refs, and public ref match; the accepted topic-branch metadata is reported precisely without mutation;
- Meta at `/home/agile/meta` matches one of the narrowly accepted states in section 5; its object graph, origin, branch/upstream, inventory, public history, local correction state, and public ref are classified exactly;
- all mandatory current AP sources, all public Meta content/history, and all applicable protected local historical inputs were read;
- no proposal duplicates AP or violates a fixed Cooperator decision;
- every proposed path and field has one owner, lifecycle, and concrete need;
- the future allowlist is exact and Meta-only;
- interruption, no report, clarification, correction, redaction, abandonment, publication, closure, and bootstrap cases are decision-ready;
- public visibility produces public-safe defaults;
- implementation, independent acceptance, publication, and closure remain distinct later gates;
- every non-zero command, traceback, mismatch, or near-miss is resolved and reported or forces a non-ready status.

Planning has no implementation/acceptance/publication/closure PASS. Always report:

```text
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
```

### 12. Terminal report contract

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Then provide actual values:

```text
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Logical-whole closure: not-closed
Report justification: new-evidence
Authority expiry: planning authority expired at this terminal report
```

Map status consistently:

- `PLAN READY` → `Standard terminal status: PASS`
- `PLANNING FINDING` → `Standard terminal status: PARTIAL`
- `PLAN BLOCKED` → `Standard terminal status: BLOCKED`

Include exactly these substantive sections:

1. `PLANNING STATUS`
2. `AUTHORITY AND INDEPENDENCE`
3. `EXECUTION ENVIRONMENT`
4. `AP BASELINE IDENTITY`
5. `META BASELINE IDENTITY`
6. `OBSERVED REPOSITORY STATE`
7. `FIXED REQUIREMENTS RECONCILIATION`
8. `CONTRADICTIONS OR OPEN DECISIONS`
9. `PROPOSED V1 ARCHITECTURE`
10. `SEMANTIC OWNERSHIP MAP`
11. `ARTIFACT LIFECYCLE AND AUTHORITY MODEL`
12. `SECURITY, REDACTION, AND VISIBILITY MODEL`
13. `EXACT PROPOSED CHANGED-PATH ALLOWLIST`
14. `IMPLEMENTATION VERTICALS AND COMMIT PLAN`
15. `VALIDATION AND INDEPENDENT ACCEPTANCE PLAN`
16. `MIGRATION, BACKFILL, AND COMPATIBILITY BOUNDARY`
17. `DEFERRED WORK`
18. `RISKS AND FAILURE MODES`
19. `SMALLEST NEXT STEP`
20. `AUTHORITY EXPIRY`

Section 2 must confirm that the session was entirely read-only and that protected Cooperator work granted no implementation authority. Section 6 must reconcile both prior Workers' blockers, the public Meta advance to `980d909...`, the corrected path `/home/agile/meta`, the protected `01_report.md` correction, and the inert AP marker. Section 13 must include every exact historical bootstrap artifact path if the plan proposes storing it; do not silently omit either blocked Worker pair or the Worker 3 pair.

End with:

```text
Start and end commits: <exact AP start/end and Meta start/end>
Changed files and purpose: none by this Worker; report exact pre-existing Cooperator correction and historical inputs without claiming them as Worker changes
Tests and validation: <commands and summarized evidence>
Commit and push result: not authorized; not performed
Deviations, risks, or missing evidence: <none or exact items>
Resolved Execution Issues / Near-Misses: <Worker 1 and Worker 2 blockers, corrected Meta path and baseline, protected local correction, AP marker, and exact residual risk>
Pre-Existing Failure Classification: <complete classification including accepted AP checkout metadata, reconciled public Meta advance, and protected local Meta state>
```

Summarize successful commands. Include full output only for failures, unexpected state, or safety-critical evidence. Never hide a non-zero command, traceback, mismatch, visibility uncertainty, unsafe-content risk, or ownership contradiction behind `PLAN READY`.

### 13. Stop conditions

Return `PLAN BLOCKED` if:

- this is not a fresh Worker 3 session or Native Plan Mode is inactive;
- AP cannot be resolved at the bounded current workspace or differs materially beyond the explicitly accepted branch/upstream metadata;
- `/home/agile/meta` is absent, is not the exact standalone canonical Meta checkout, or differs beyond the narrowly accepted states in section 5;
- either canonical remote or public main differs;
- unexplained owner work beyond the protected local correction/historical inputs, active Git operations/locks, unsafe content, or repository topology prevents a safe exact plan;
- current AP conflicts materially with a fixed Cooperator decision;
- a coherent implementation necessarily touches AP or another forbidden repository;
- a necessary product/privacy/authority choice owned by Michal blocks implementation;
- any filesystem, repository, index, ref, configuration, or remote mutation occurs;
- a required capability is unavailable.

Use `PLANNING FINDING` only when the architecture and future allowlist are decision-ready and one explicit non-blocking Cooperator choice remains. State exactly what stays stable.

Stop after the single terminal report. Do not continue into implementation even if a UI offers `Approve`, `Build`, `Continue`, or an automatic transition. Only a new complete ORCHESTRATOR prompt can grant execution authority.
