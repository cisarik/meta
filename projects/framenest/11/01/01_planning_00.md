# Fresh Planner — FrameNest pre-deployment engineering convergence

You are a genuinely fresh, high-capability Planner Worker with approximately a 1M-token context window.

Use that context aggressively.

Do not perform a superficial targeted review around the findings supplied below. Your job is to understand the current FrameNest codebase as a system, independently audit it for pre-deployment engineering debt and latent defects, and then produce a rigorous bounded implementation plan.

The Cooperator specifically wants a deeper analysis than the preceding ChatOrchestrator audit.

---

## Worker identity

Persistent role identity: `WORKER`

Worker session profile: `Planner`

Worker session target: `fresh-worker-session`

Worker session ordinal: `01`

Worker exchange ordinal: `01`

Native planning mode: **required**

Planning layer: `implementation-planning`

Orchestration planning owner: `ORCHESTRATOR`

Implementation in this Worker session: **prohibited**

Plan disposition: `approval-gated`

Delivery route: manual Cooperator delivery through ChatOrchestrator

Reasoning expectation: **High**

Use the large context window to retain architecture, call chains, tests, contracts and historical context simultaneously.

Do not delegate implementation.

Read-only diagnostic commands and disposable tests are allowed.

---

# Proposed logical whole identity

Use this as the working identity unless your analysis demonstrates that a materially better bounded identity is warranted:

```text
framenest-web-client-contract-and-testability-convergence
```

If you rename or split it, justify that decision precisely.

Do not casually expand this into a general FrameNest rewrite.

---

# Repository

Canonical project:

```text
https://github.com/cisarik/framenest
```

Expected local checkout:

```text
/home/agile/Projects/framenest
```

Recent local state observed by ChatOrchestrator:

```text
branch:
feat/x-meme-browser-companion

recent local HEAD:
8c7858b62beca3c4ee92bb8f1f095b98063e2c94

expected pinned AP:
7478ddb07d2c3911f79e1aa1441f0115a31c45d8
```

These values are orientation only.

**Independently verify current local and public truth.**

You have ordinary Git/GitHub access.

Unlike ChatOrchestrator, you are not restricted to offline bundle evidence.

Before planning, establish:

- physical repository root;
- current HEAD;
- current branch;
- worktree/index state;
- canonical origin;
- current public relevant refs;
- `.ap` gitlink;
- `.ap` checkout HEAD;
- `./.ap/ap doctor`;
- any divergence between local candidate state and public state;
- whether `8c7858b...` is public or only local;
- external trace/report state relevant to this planning session.

Do not mutate the project merely to make baseline verification pass.

---

# Product context

FrameNest is a long-lived FastAPI application that has accumulated work across multiple generations of LLM-assisted development.

It includes, among other areas:

- FastAPI/Uvicorn;
- SQLite/Alembic;
- resumable uploads;
- gallery/details/admin workflows;
- AI still-frame analysis;
- media metadata and classification;
- YouTube acquisition;
- X/meme workflows;
- companion/review workflows;
- manual covers;
- admin lifecycle functionality;
- Tailscale-derived identity;
- extensive vanilla JavaScript frontend behavior;
- substantial Python and JavaScript test surfaces.

Many logical wholes have individually passed acceptance.

That does **not** imply that accumulated architecture, cross-layer contracts, testability and dormant residuals are clean.

The Cooperator specifically suspects:

- older-LLM structural debt;
- frozen or deferred implementation fragments;
- accepted residual defects;
- stale contracts;
- duplicated or contradictory behavior;
- code kept alive only by tests;
- test suites coupled to implementation text rather than behavior;
- type/domain-model mistakes hidden by permissive runtime behavior.

Your job is to investigate that suspicion rigorously.

---

# Strategic sequencing constraint

Do **not** plan UI/UX polish here.

The Cooperator wants UI/UX polish to occur very late, likely immediately before hands-on NUC testing/deployment preparation.

This planning cycle should identify and converge deeper engineering debt first.

Also do not turn this into NUC deployment work.

Out of scope for this whole unless directly required to validate a defect:

- visual redesign;
- styling polish;
- screenshot-based UX work;
- NUC deployment;
- VPS deployment;
- new user-facing features;
- speculative feature expansion.

---

# Previous ChatOrchestrator audit

The following are **leads, not accepted facts**.

Independently confirm, reject, refine or supersede them.

Do not design the plan merely by copying this list.

## Lead A — frontend monolith growth

A read-only audit observed approximately:

```text
static/app.js:
~12,776 lines
~564 functions
```

An older architecture audit reportedly saw roughly:

```text
~11,908 lines
~514 functions
```

FrameNest has continued receiving Companion/X/AI/frontend behavior since then.

The concern is not "large file = bad".

Investigate whether current size produces measurable problems such as:

- duplicated domain logic;
- hidden cross-feature coupling;
- state ownership ambiguity;
- difficult isolation;
- test-only production helpers;
- DOM mutation paths that cannot be tested independently;
- duplicated backend contracts;
- unsafe ordering dependencies;
- stale code that cannot be confidently deleted;
- structural test brittleness.

Do not prescribe framework migration.

Do not introduce React/Vue/etc. merely to solve file size.

---

# Lead B — Python source-scraping JavaScript tests

A previous audit observed roughly:

```text
tests/.../test_local_web_application.py:
~3,051 lines
~112 uses of helpers extracting JavaScript function bodies/source text
```

Investigate this deeply.

Determine:

- what those tests actually prove;
- which tests are behavioral versus textual;
- whether production refactors fail despite unchanged behavior;
- whether JS implementation structure has become part of the accidental test contract;
- whether equivalent Node tests already exist;
- whether assertions are duplicated across Python and Node;
- whether Python is parsing JS because proper seams do not exist;
- whether stale source-shape expectations are masking dead code.

Do not simply rewrite every Python test in Node.

Identify the smallest high-value migration seam.

---

# Lead C — recent stale frontend assertions

An earlier audit observed a recent commit around:

```text
22352c9
```

that reportedly repaired several stale frontend assertions without production behavior changes.

Verify this from history.

If true, use it as evidence about test architecture only if the commit actually supports that conclusion.

Do not infer more than the diff proves.

---

# Lead D — apparent production helpers without real production callers

The previous audit flagged possible examples including:

```text
applyMovieIdentificationToMetadataWorkspace()
movieSuggestionFromResult()
describeCatalogItem()
downloadIcon()
```

Some appeared to have no production callers or to exist mainly because tests referenced them.

Independently build a call/reference picture.

For each suspected dead helper distinguish:

- genuinely unreachable production code;
- indirect callback/event reference;
- template/string reference;
- browser-global API intentionally exposed;
- test-only production artifact;
- stale feature residue;
- false positive from static grep.

Do not delete code based on grep alone.

---

# Lead E — Unicode title contract drift

The previous audit reported a concrete possible client/server mismatch.

Backend reportedly validates a title approximately as:

```python
len(value) <= 240
```

while frontend uses something equivalent to:

```javascript
rawTitle.length > 240
```

JavaScript `.length` counts UTF-16 code units, while Python `len(str)` counts Unicode code points.

Reported reproducer:

```text
240 × 😀
Python/server: accepts
JavaScript/client: rejects
JS length: 480
Unicode code points: 240
```

Independently locate the actual current code and reproduce or disprove this.

Then search for **other cross-language parity defects of the same class**, including:

- length;
- normalization;
- trimming;
- empty values;
- whitespace;
- casing;
- Unicode;
- numeric ranges;
- enum values;
- booleans;
- nullable values;
- timestamp handling;
- filename rules;
- URL validation;
- media identifiers;
- classification fields.

The important question is not only whether this one defect exists.

The deeper question is whether FrameNest lacks a reliable ownership mechanism for shared client/server validation contracts.

---

# Lead F — domain type confusion

Previous audit observed something resembling:

```python
def _parse_analysis_run_id(value: str) -> MediaAnalysisRunId:
    ...
    return MediaId.from_string(value)
```

in Companion review functionality.

Reported runtime behavior returned a `MediaId` where the type annotation says `MediaAnalysisRunId`.

Existing focused tests reportedly still passed.

Independently verify.

Then search for other domain-ID confusion involving classes such as:

- media IDs;
- analysis-run IDs;
- suggestion IDs;
- upload IDs;
- YouTube/request IDs;
- lifecycle identifiers;
- other string-wrapper domain types.

Look especially for errors hidden because multiple ID classes expose identical:

```text
to_string()
from_string()
```

surfaces.

Do not propose a giant type-system rewrite unless evidence justifies it.

---

# Lead G — composition root size

A previous audit observed `create_app()` at approximately:

```text
~1,073 lines
~30 parameters
~165 assignments
~25 routers
```

Investigate whether this is merely verbose explicit composition or an actual correctness/testability problem.

Look for:

- duplicated construction;
- dependency ordering assumptions;
- mutable shared state;
- lifecycle ownership ambiguity;
- inconsistent adapter wiring;
- configuration drift;
- hidden feature toggles;
- environment-specific branches;
- objects constructed but not used;
- repeated policy construction;
- test setup pain caused directly by composition structure.

Do not refactor `create_app()` just because it is large.

If no measurable defect follows from it, park it.

---

# Lead H — secure media filesystem TOCTOU residual

Older accepted work reportedly documented a bounded filesystem race between:

```text
resolve()/validation
```

and later:

```text
os.open()
```

through intermediate filesystem path components.

Investigate current implementation and historical decision.

Determine:

- whether the residual still exists;
- threat model;
- what local write capability is required;
- whether `dirfd` / `openat` style traversal would eliminate it;
- whether this belongs before deployment;
- whether it deserves a separate security logical whole rather than contaminating this one.

Do not silently expand the current whole into filesystem hardening unless evidence makes it necessary.

---

# Lead I — possibly unused Python scaffolding

Prior audit surfaced names such as:

```text
MediaAnalysisLifecycleDisabledError
MediaSuggestionConnectionTester
YouTubeRequesterPrivateAccess
YouTubeStagingLimitExceededError
default_classification_fields()
```

Independently classify them.

Possible outcomes include:

- actually used indirectly;
- public/domain API retained intentionally;
- stale scaffold;
- future placeholder;
- test helper;
- accepted compatibility surface.

Do not remove symbols based solely on zero direct grep callers.

---

# Lead J — AP pin rebaseline drift

After the recent AP pin update, previous audit observed old AP SHA references such as:

```text
7ef45da...
```

possibly in:

```text
tests/contract/test_ap_integration.py
README.md
docs/AP_UPGRADE_OBSERVATIONS.md
```

while current `.ap` is expected at:

```text
7478ddb...
```

Verify exact current state.

Classify each stale reference:

- executable contract defect;
- intentionally historical documentation;
- stale documentation;
- generated artifact;
- legitimate old-version example.

Do not blindly replace every old SHA.

This is likely a very small rebaseline correction, not by itself a product logical whole.

If appropriate, include it as a bounded first slice or prerequisite.

---

# Required deeper audit

The previous audit is explicitly **not enough**.

Use the 1M context window to inspect the repository broadly.

Your planning report should demonstrate that you examined the whole relevant system, not only the named leads.

At minimum perform the following audit passes.

---

## 1. Repository archaeology

Study meaningful recent and historical changes.

Use:

```text
git log
git show
git blame where valuable
```

Look for language in commits/docs/reports such as:

```text
defer
deferred
freeze
frozen
residual
accepted defect
known limitation
follow-up
later
temporary
workaround
not implemented
out of scope
blocked
TODO
FIXME
HACK
XXX
```

Separate historical limitations already resolved from still-live residuals.

Do not resurrect intentionally closed work without evidence.

---

## 2. Test topology

Map major test surfaces:

- Python unit;
- integration;
- contract;
- architecture;
- browser/local-web;
- JavaScript/Node;
- Playwright if present;
- migration/database;
- CLI;
- security;
- companion;
- X;
- YouTube;
- AI analysis.

Look for:

- SKIP;
- xfail;
- disabled tests;
- commented assertions;
- huge helper abstractions;
- tests coupled to source text;
- duplicate tests proving the same behavior;
- missing tests around obvious critical branches;
- mocks replacing too much behavior;
- tests that pass while testing the wrong type/contract.

A green test suite is evidence, not proof.

---

## 3. Frontend architecture

Understand actual runtime structure of the vanilla-JS client.

Map major state domains and feature clusters.

At minimum inspect:

- globals/module-level state;
- initialization;
- DOM lookup ownership;
- event binding;
- fetch/API abstraction;
- error handling;
- modal/dialog state;
- upload state;
- gallery state;
- metadata workspace;
- admin state;
- AI analysis;
- YouTube;
- X/meme;
- companion/review;
- keyboard/accessibility behavior where architecture-relevant.

Look for actual extraction seams where pure logic can become testable without redesigning UI.

---

## 4. Client/server contracts

Create an evidence-backed map of contracts duplicated between Python and JavaScript.

Search for:

- validation;
- enums;
- string limits;
- numeric limits;
- path/URL rules;
- status names;
- lifecycle values;
- API response shapes;
- nullable fields;
- default values;
- error codes/messages relied upon programmatically.

Identify whether a single owner already exists and is merely bypassed, or whether duplication is structural.

---

## 5. Python domain model

Inspect typed ID wrappers, value objects, dataclasses/models, repositories and service boundaries.

Look for:

- wrong domain type returned;
- plain strings leaking through;
- interchangeable wrapper classes;
- misleading annotations;
- casts hiding mistakes;
- parser duplication;
- exceptions caught too broadly;
- impossible states represented.

Focus on defects that can survive because Python runtime typing is permissive.

---

## 6. Application/service architecture

Inspect:

- `create_app`;
- router composition;
- service creation;
- repositories;
- adapters;
- lifecycle/startup/shutdown;
- shared resources;
- dependency injection patterns;
- filesystem abstractions;
- outbound clients.

Look for duplicated or contradictory paths rather than aesthetic purity.

---

## 7. Database and migrations

Read current schema/migrations enough to identify:

- compatibility shims still alive;
- fields no longer used;
- migrations implying unfinished transitions;
- duplicate data representation;
- constraints enforced only in application code;
- lifecycle/status drift.

Do not propose schema changes without a concrete need.

---

## 8. Concurrency / filesystem / upload safety

Review high-risk code paths around:

- resumable upload;
- cancellation;
- duplicate detection;
- SHA identity;
- filesystem moves;
- TTL cleanup;
- media serving;
- manual cover writes;
- YouTube acquisition;
- sidecars/background tasks if applicable.

Search for known accepted residuals.

Classify separately if they deserve a security/reliability whole.

---

## 9. Error and observability paths

Look for:

- swallowed exceptions;
- `except Exception`;
- fire-and-forget behavior;
- inconsistent API error mappings;
- logs without useful context;
- frontend failures rendered only in console;
- states that can become silently stale.

Only elevate findings with realistic impact.

---

## 10. Dead/frozen feature paths

Search beyond obvious unused functions.

Investigate feature flags, disabled branches, classes/interfaces with only one side implemented, placeholder adapters and historical compatibility code.

Classify as:

```text
live
compatibility-required
dormant-but-intentional
test-only
dead
unknown
```

Require evidence before `dead`.

---

# Validation

Use cheap read-only execution aggressively.

You may run:

- static searches;
- compile checks;
- focused Python tests;
- Node tests;
- targeted reproductions;
- type/static tools already available;
- disposable scripts;
- Git history inspection.

Do not install arbitrary tooling or mutate project dependencies simply to improve the audit.

If full Python tests cannot run because the exact environment is unavailable, classify that honestly.

Do not turn an audit-environment issue into a product defect.

Record exact commands/results for material findings.

---

# Required planning discipline

The audit may discover many problems.

The implementation plan must **not** include all of them.

After discovery, classify findings into:

```text
A. In-scope for the next bounded logical whole
B. Immediate tiny prerequisite/rebaseline
C. Separate future logical whole
D. Explicitly parked / low value
E. False positive / already resolved
```

Prefer one coherent next whole with measurable value.

The current working hypothesis is that the best next whole concerns:

```text
web client contract + testability convergence
```

but you may reject that hypothesis.

If another problem is materially more important before NUC testing, explain why.

---

# Scope quality bar

A good next logical whole should preferably have:

- one clear engineering problem;
- concrete failure evidence;
- bounded files/components;
- limited user-visible behavior change;
- testable acceptance;
- low migration risk;
- no gratuitous framework switch;
- no architectural rewrite;
- measurable reduction in risk before UI/UX and deployment testing.

Avoid umbrella names such as:

```text
clean up codebase
refactor frontend
fix technical debt
improve architecture
```

Those are not acceptable scopes.

---

# Potential target shape

If evidence supports the current hypothesis, consider a scope resembling:

### Contract convergence

- fix verified JS↔Python validation mismatches;
- establish a reliable ownership pattern for the particular duplicated contracts discovered;
- do not build a universal schema-generation platform unless necessary.

### Domain-ID correctness

- fix verified wrong-ID construction;
- add regression protection;
- audit directly adjacent ID parser family only.

### Testability seam

- identify one coherent frontend feature cluster;
- extract pure/non-DOM logic or contract helpers;
- give them first-class Node behavior tests;
- retire the corresponding brittle Python source-body assertions.

### Dead/test-only frontend artifacts

- remove only code proven unreachable or test-only;
- migrate any legitimate behavior assertions before deletion.

### AP consumer rebaseline

- correct stale executable AP-pin contract expectations where appropriate;
- distinguish historical documentation from stale active documentation.

This is an example shape, not pre-approval.

---

# Explicit anti-goals

Do not propose:

- rewrite `app.js` from scratch;
- React/Vue/Svelte migration;
- TypeScript migration as a prerequisite;
- full frontend modularization in one whole;
- replacement of every source-text test;
- full dependency injection redesign;
- `create_app()` rewrite without demonstrated need;
- broad database redesign;
- UI restyling;
- NUC deployment;
- VPS deployment;
- feature development.

If one of these is truly required to solve a demonstrated blocker, provide extraordinary evidence.

---

# Planner output requirements

Return a terminal report beginning exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Include the standard AP coordinates and terminal planning status.

The report must be sufficiently concrete that the Orchestrator can generate an Implementation Worker prompt without re-performing your architectural analysis.

Include these sections.

## 1. Verified baseline

Exact:

- HEAD;
- branch;
- public relationship;
- worktree/index;
- `.ap`;
- AP doctor;
- environment constraints.

## 2. Audit methodology

Summarize what you actually inspected and executed.

Not generic prose.

## 3. Architecture map

Concise but substantive picture of:

- Python backend;
- frontend;
- tests;
- major cross-layer boundaries relevant to findings.

## 4. Finding register

For every material finding include:

```text
ID
title
location(s)
evidence
reproduction if applicable
severity
confidence
current tests
why tests did/did not detect it
recommended disposition
```

Clearly distinguish verified defects from architectural smells.

## 5. Previous ChatOrchestrator lead disposition

Explicitly mark every Lead A–J as:

```text
confirmed
partially confirmed
disproved
superseded
```

with evidence.

## 6. Additional findings

This is important.

List material findings you discovered that were **not supplied by ChatOrchestrator**.

The audit is incomplete if you merely validate the supplied list.

## 7. Accepted/historical residual review

Identify meaningful still-live residual defects or frozen decisions from prior work.

Do not resurrect resolved history.

## 8. Prioritization

Rank findings by:

- correctness risk;
- security risk;
- operational risk;
- testability cost;
- likelihood of affecting NUC testing;
- cost/risk of correction.

## 9. Recommended next logical whole

Give exactly one preferred identity and a one-paragraph problem statement.

Explain why it should precede UI/UX polish.

## 10. Exact scope

List what is in scope.

## 11. Explicit non-scope

List tempting adjacent work that must remain out.

## 12. Proposed implementation architecture

Be specific.

Identify:

- files/components;
- extraction seams;
- ownership changes;
- contract changes;
- test migration;
- deletion candidates;
- compatibility constraints.

Do not write implementation code.

## 13. Implementation slices

Design the smallest safe sequence.

Prefer independently understandable slices rather than one giant mutation.

For each slice state:

```text
goal
expected files
required behavior preservation
validation
rollback boundary
```

## 14. Validation matrix

Give exact tests/checks expected from Implementation Worker.

Include regression coverage and targeted reproductions.

## 15. Acceptance matrix

Define objective PASS/BLOCKED criteria for a future fresh Acceptance Worker.

## 16. Risk review

Include:

- user-visible regression;
- browser behavior;
- persistence/data;
- concurrency;
- security;
- backward compatibility;
- deployment relevance.

## 17. Follow-up logical wholes

List only well-supported deferred candidates.

For example, if evidence supports them:

```text
secure filesystem traversal hardening
composition-root convergence
broader frontend modularization
UI/UX polish
NUC operational validation
```

Do not turn them into current scope.

## 18. Recommended Worker profile

State:

- Implementation Worker freshness;
- reasoning level;
- whether native planning mode is needed;
- whether subagents are useful;
- whether implementation should be one Worker or multiple bounded fresh sessions.

## 19. Challenge to the hypothesis

Explicitly answer:

> Is `framenest-web-client-contract-and-testability-convergence` genuinely the best next logical whole?

If yes, prove why.

If no, recommend the better one.

---

# Final planning standard

The purpose of this Planner is not to create the largest plan possible.

It is to use a very large context window to achieve **high-confidence compression**:

understand the entire relevant system deeply enough that the next implementation can be small, coherent and safe.

Be skeptical.

Follow evidence.

Distinguish:

```text
bug
latent bug
security residual
architectural smell
test debt
dead code
historical artifact
intentional compatibility
```

Do not conflate them.

Do not implement.

Do not commit.

Do not push.

Stop after the complete terminal planning report.