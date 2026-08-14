# Authoritative Prompt for Fresh Worker 1

## FrameNest In-Process Lifecycle Runtime Contract — Repository-Grounded Implementation Planning

💡 Native Plan Mode

You are fresh Worker 1 for one bounded FrameNest logical whole conducted under Analytic Programming.

Read this complete prompt before taking any action.

Do not continue, reopen, correct, or reinterpret any preceding logical whole. Your sole task is read-only, repository-grounded implementation planning for the lifecycle and shutdown contract of FrameNest’s in-process coordinators.

Do not implement the plan.

---

## 1. Worker identity and mandatory routing coordinates

```text
Logical whole identity: framenest-in-process-lifecycle-runtime-contract
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
```

Planning contract:

```text
Native planning mode: required
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: exact bounded implementation design for the FrameNest in-process lifecycle runtime and shutdown contract
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
Evidence posture: non-independent
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
```

Recommended reasoning:

```text
Extra High
```

This is advisory, not protocol authority. Michal controls the model, provider, agent, reasoning configuration, cost, and whether this prompt is launched.

Extra High is recommended because the plan must reconcile asyncio cancellation, blocking executor behavior, child-process groups, durable recovery, partial-startup rollback, and one bounded process-level shutdown deadline without creating a false generic abstraction.

Delegation, sub-agents, parallel Workers, or hidden secondary workstreams are not authorized.

---

## 2. Roles and communication

Persistent roles:

```text
COOPERATOR: Michal
ORCHESTRATOR: ORCHESTRATOR_CHAT
WORKER: this fresh session
```

The ORCHESTRATOR owns:

* objective and logical-whole boundaries;
* planning acceptance or rejection;
* Worker routing;
* implementation authorization;
* candidate acceptance;
* publication, deployment, production acceptance, and closure decisions.

You do not own logical-whole closure.

Write the terminal report in professional English.

The report must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Do not place YAML, a title, commentary, a wrapper, a Native Plan Mode summary, or any other material before that heading.

Do not expose private chain-of-thought. Report conclusions, evidence, decisions, exact inspected paths, relevant commands and results, unresolved uncertainties, and concise rationale.

---

## 3. Authority envelope

Your authority is limited to read-only inspection and one decision-complete planning report.

```text
Implementation authority: none
Repository mutation authority: none
Commit authority: none
Push or publication authority: none
Deployment authority: none
Production authority: none
Provider authority: none
AP mutation authority: none
Meta mutation authority: none
Secret-access authority: none
Delegation authority: none
```

Do not:

* edit, create, delete, rename, format, or generate repository files;
* stage or commit;
* fetch into, pull, switch, checkout, merge, rebase, reset, restore, clean, stash, tag, branch, or change configuration in a canonical repository;
* initialize a worktree or modify a submodule;
* normalize owner state;
* repair local/public divergence;
* alter `.ap`;
* mutate `cisarik/ap` or `cisarik/meta`;
* SSH to the NUC;
* inspect or mutate production;
* call YouTube, X, OpenAI, or another external provider;
* inspect secrets, `.env`, credentials, browser profiles, cookies, private tabs, or unrelated private data;
* launch `cursor`, `code`, `xdg-open`, a GUI application, or an AppImage;
* install, remove, or update dependencies;
* run `uv sync`, `poetry env use`, or rebuild/delete `.venv`;
* execute a test or command that would knowingly mutate the worktree, create project caches, or alter durable state.

Use repository files, Git objects, credential-free Git transport, read-only shell inspection, and—if necessary—read-only local Python standard-library source as evidence.

If exact required evidence is unavailable without an unauthorized mutation, stop and report `BLOCKED`. Do not invent a workaround.

---

## 4. Governing repositories and issuance-time anchors

Canonical AP repository:

```text
cisarik/ap
/home/agile/Projects/ap
```

Canonical FrameNest repository:

```text
cisarik/framenest
/home/agile/Projects/framenest
```

External historical trace:

```text
cisarik/meta
/home/agile/meta
```

The ORCHESTRATOR directly verified these public refs through Git transport immediately before issuing this prompt on 2026-08-13:

```text
cisarik/ap refs/heads/main
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

cisarik/framenest refs/heads/main
a72be476f5634394287082be07380d03fa7ccd4d

cisarik/meta refs/heads/main
d3bb8a591b8e510d68521527c75bc1f2ff51bd2b
```

FrameNest public commit:

```text
commit: a72be476f5634394287082be07380d03fa7ccd4d
parent: d4c3402a4765b39cee0d8e2063d5ec8be161caf6
tree: 5f8afa3d2705fd9a60d8375e963699e9be5e9335
subject: chore: adopt current AP generation
```

Expected public FrameNest `.ap` gitlink:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

These are issuance-time anchors, not permission to trust remembered or stale local state.

---

## 5. Fresh restoration gate

Before designing the plan, perform a bounded read-only restoration gate.

### 5.1 Direct public-ref verification

Use Git transport, not GitHub webpages, search results, browser caches, remembered state, or repository badges:

```text
git ls-remote https://github.com/cisarik/ap.git refs/heads/main
git ls-remote https://github.com/cisarik/framenest.git refs/heads/main
git ls-remote https://github.com/cisarik/meta.git refs/heads/main
```

If AP or FrameNest public `main` differs from the issuance-time anchors, stop before producing an implementation plan and report `BLOCKED` with the exact observed ref. A changed canonical baseline requires ORCHESTRATOR reconciliation and renewed authority.

A changed Meta ref alone is not automatically blocking. Classify it and use only the bounded trace rules below.

### 5.2 Canonical FrameNest worktree

Inspect without changing:

* repository root and origin identity;
* branch or detached state;
* local `HEAD`;
* upstream attachment;
* `origin/main`;
* tracked/index state;
* relevant untracked state;
* availability of the exact public commit object;
* `.ap` gitlink recorded by local `HEAD`;
* `.ap` gitlink recorded by public commit `a72be476…`;
* local `.ap` checkout identity, detached/branch state, and cleanliness;
* `ap.project.conf`;
* root `AGENTS.md`;
* `docs/WORKER_EXECUTION_CONTRACT.md`.

Previously observed owner state was:

```text
branch: feat/ap-baseline-bound-execution-adoption
upstream: none
local HEAD: d4c3402a4765b39cee0d8e2063d5ec8be161caf6
origin/main: a72be476f5634394287082be07380d03fa7ccd4d
tracked/index state: clean
```

Previously observed local `.ap` state:

```text
local HEAD gitlink: 4862380f351ddd74e1c141a4babe2d0f0b43979d
local .ap checkout: 4862380f351ddd74e1c141a4babe2d0f0b43979d
detached and clean
```

Previously observed untracked owner material:

```text
.accept-immut-work/
.playwright-mcp/
.w6-immut-work/
REPRO_DIR=/
uv.lock
```

Treat these as expected observations to verify, not authorization to delete, inspect recursively, stage, ignore, or normalize them.

`uv.lock` is not project authority.

The accepted planning baseline is exact public commit:

```text
a72be476f5634394287082be07380d03fa7ccd4d
```

Inspect its code through already available immutable Git objects. Do not checkout public `main` merely to equalize the canonical owner worktree.

If unexpected tracked changes overlap the lifecycle causal surface, or the exact public object cannot be inspected without unauthorized Git mutation, report `BLOCKED`.

### 5.3 Governing AP identity

Establish which immutable AP generation governs the exact public FrameNest baseline. Read the required AP protocol and Worker guidance from that exact identity.

Do not mutate or upgrade AP.

If current AP public `main`, the FrameNest public gitlink, and locally available AP evidence cannot be reconciled read-only, report the contradiction and stop.

---

## 6. Configured external trace

```text
External trace disposition: configured
Trace discovery: cisarik/meta; /home/agile/meta; projects/framenest
Trace project key: framenest
Trace logical-whole projection identity: framenest-in-process-lifecycle-runtime-contract
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
```

Meta is supporting historical evidence only. It is not AP semantic authority, FrameNest product authority, current task authority, repository authority, acceptance authority, publication authority, deployment authority, production authority, or closure authority.

### 6.1 ORCHESTRATOR-selected trace scope

Do not read all of Meta and do not recursively inspect unrelated projects or old logical wholes.

Perform only this bounded trace inspection:

1. Verify Meta public `main` through the direct Git command in the restoration gate.

2. Inspect the local Meta repository root, origin, current ref, and tracked state read-only.

3. Inspect the recent project-scoped history using the equivalent of:

   ```text
   git log --oneline --decorate -- projects/framenest
   ```

4. If present, inspect the immediately preceding logical whole:

   ```text
   projects/framenest/00/01-framenest-runtime-architecture-maintainability-and-backlog-rebaseline/
   ```

   Read only its restoration handout and the completed Worker 1 prompt/report exchange needed to understand how the lifecycle candidate was selected.

5. Do not read the entire preceding AP-adoption archive. Consult only the necessary final acceptance/publication evidence from:

   ```text
   projects/framenest/00/00-framenest-current-ap-generation-adoption-and-consumer-rebaseline/
   ```

   and only if a repository/AP-pin contradiction requires historical reconciliation.

6. If the `01-...` directory is absent at the verified public Meta ref, record that fact and continue from the current authoritative prompt, exact canonical repositories, and available durable evidence. Trace lag or absence does not itself grant permission to broaden the search or block ordinary planning when higher-ranked evidence suffices.

7. Report exactly which Meta paths were consulted and what material planning fact, if any, each contributed.

Do not mutate Meta and do not create the current logical-whole directory.

For Cooperator context only, the intended archive destination after actual outcomes exist is:

```text
projects/framenest/00/02-framenest-in-process-lifecycle-runtime-contract/
```

Expected archive artifacts are:

```text
00_handout.md
01_planning.md
01_report.md
```

Archival remains Michal’s separate responsibility after the actual Worker outcome exists.

---

## 7. Closed predecessor and closed-state protection

Closed predecessor:

```text
FrameNest Runtime Architecture, Maintainability and Backlog Rebaseline
framenest-runtime-architecture-maintainability-and-backlog-rebaseline
CLOSED: PASS
```

That whole selected the current lifecycle candidate through read-only repository analysis. It created no implementation candidate and had no Worker 2.

Do not reopen the predecessor analysis or repeat its broad candidate search.

Do not reopen these accepted wholes without concrete regression evidence:

```text
Technical MVP
ordinary-user private upload
administrator review and publication
admin batch actions
durable media removal
automated catalog backup and restore verification
requester-private YouTube acquisition
YouTube/X creator taxonomy
requester-private X acquisition
off-device catalog recovery
operator-workstation pull snapshot and recovery
repository authority and Worker execution-contract convergence
current AP generation consumer convergence
runtime architecture, maintainability and backlog rebaseline
```

Coordinator lifecycle code may be included only to establish the selected process-lifecycle contract. Preserve existing product outcomes and accepted domain boundaries.

---

## 8. Logical-whole objective

Name:

```text
FrameNest In-Process Lifecycle Runtime Contract
```

Purpose:

> Establish a bounded, observable, and testable lifecycle contract for FrameNest’s six in-process coordinators so startup, runner failure, and application shutdown behave safely within the production systemd stop constraint while preserving durable recovery and existing product behavior.

This is a runtime-correctness and operational-integrity whole.

It is not:

* a product-feature whole;
* a UI/UX whole;
* a distributed-job-queue redesign;
* a schema or migration whole;
* an acquisition-domain unification;
* a general security audit;
* a broad refactor;
* a test-retirement exercise.

Your result must be an exact implementation plan suitable for approval or rejection by the ORCHESTRATOR.

---

## 9. Verified predecessor evidence to re-establish

Treat the following as claims to verify against exact public commit `a72be476…`, not as conclusions to copy.

### 9.1 Production process envelope

Expected systemd contract:

```text
KillSignal=SIGTERM
TimeoutStopSec=30s
Restart=on-failure
```

Expected Uvicorn process model:

```text
workers=1
```

The external 30-second systemd limit is not automatically the application’s internal graceful-stop budget.

### 9.2 Application lifecycle

The FastAPI lifespan reportedly starts six coordinators in this order:

```text
media analysis
upload catalog
upload publication
upload validation
YouTube acquisition
X acquisition
```

Nested `finally` blocks reportedly stop them sequentially in reverse order.

There is reportedly no explicit process-level internal deadline shared across all cleanup operations.

### 9.3 Coordinator differences

Verify at least:

* YouTube acquisition marks stopping, wakes the runner, cancels it when active, and awaits cancellation.

* X acquisition requests shutdown, wakes the runner, and awaits it without cancelling an in-flight acquisition.

* upload validation, upload catalog, upload publication, and media analysis own `ThreadPoolExecutor` instances;

* their shutdown paths reportedly use:

  ```text
  ThreadPoolExecutor.shutdown(wait=True, cancel_futures=False)
  ```

* the YouTube downloader default timeout is reportedly 7,200 seconds;

* its child-process termination path reportedly includes TERM and KILL grace periods;

* the YouTube runner reportedly catches broad `Exception` and converts runner work failure into `progressed = False`.

Distinguish verified behavior from risk inference.

The predecessor established no observed production SIGKILL, corruption, or lost-media incident. The relevant hypothesis is:

> Sequential unbounded cleanup may exceed the 30-second systemd envelope and permit forced process termination while SQLite, staging state, executor work, or a child process is active.

Your plan must prove, safely refute, or appropriately bound this hypothesis through focused deterministic validation.

---

## 10. Minimum causal inspection surface

Inspect at least:

```text
src/framenest/adapters/api/application.py
src/framenest/server.py
src/framenest/application/upload_validation_coordinator.py
src/framenest/application/upload_catalog_coordinator.py
src/framenest/application/upload_publication_coordinator.py
src/framenest/application/media_analysis_coordinator.py
src/framenest/application/youtube_acquisition.py
src/framenest/application/x_acquisition.py
src/framenest/infrastructure/youtube/downloader.py
src/framenest/infrastructure/x/downloader.py
src/framenest/infrastructure/media_analysis/process.py
deploy/systemd/framenest.service
```

Also identify the smallest relevant existing test surface by repository search.

This is an inspection minimum, not a mutation allowlist. Expand only when a directly evidenced lifecycle dependency requires it.

Do not expand into unrelated domain state machines merely because they share a file with lifecycle code.

---

## 11. Required lifecycle behavior matrix

Produce an exact matrix for all six coordinators covering:

* owned resources;
* startup behavior;
* partial-startup failure behavior;
* runner task ownership;
* blocking thread/executor ownership;
* subprocess or child-process ownership;
* notification or wake mechanism;
* normal completion behavior;
* shutdown request semantics;
* current cancellation semantics;
* current timeout/deadline behavior;
* durable recovery mechanism;
* failure visibility;
* intentional domain-specific differences that must remain distinct.

Do not force all coordinators into one abstraction merely because they share method names.

Identify which existing methods should remain semantically distinct, including as applicable:

```text
start
notify
drain
shutdown
runner_done
```

---

## 12. Required planning decisions

Answer each question with exact repository evidence and a concrete design decision.

1. What lifecycle states and operations are genuinely shared across the six coordinators?
2. Which differences are intentional domain behavior and must remain distinct?
3. What is the smallest coherent implementation boundary: composition-root supervision, deadline helpers, lifecycle adapters, a structural `Protocol`, or another evidenced design?
4. How will partial-startup rollback clean up only resources that successfully started?
5. How will reverse-order shutdown remain explicit without multiplying unbounded waits?
6. What exact internal graceful-stop budget should apply below the external 30-second systemd maximum?
7. What safety reserve is retained for Uvicorn shutdown, event-loop cleanup, engine disposal, thread/process finalization, and systemd scheduling?
8. Is the budget global, per-component, or a global absolute deadline with bounded per-component operations?
9. How is one monotonic absolute deadline propagated so six sequential components cannot each consume a full timeout?
10. How are asyncio tasks, executor-backed blocking work, and child-process groups treated differently?
11. Which blocking operations can become cooperatively cancellable or bounded at their I/O boundary?
12. Which work may be abandoned only because a proven durable recovery invariant makes abandonment safe?
13. How will executor threads be prevented from silently defeating timely process exit?
14. How will child-process groups receive bounded termination and be reaped?
15. How will runner death or repeated failure become observable without leaking secrets, producing a noisy loop, or changing product outcomes?
16. Which existing recovery invariants protect SQLite, staging media, durable claims, and restart continuation?
17. Which deterministic fake-slow-work tests can use millisecond-scale injected budgets?
18. What process-level integration test can send SIGTERM to a temporary FrameNest process and prove timely exit, child cleanup, and recoverable SQLite/staging state?
19. Which existing regression tests are the smallest sufficient set for upload, validation, publication, media analysis, YouTube, X, and startup recovery?
20. Does `deploy/systemd/framenest.service` require mutation, or should it remain an immutable alignment constraint?
21. What exact implementation worktree/branch strategy preserves the canonical owner checkout?
22. What conditions would make the proposed implementation unsafe or require ORCHESTRATOR rescoping?

Explicitly distinguish:

* verified defects;
* verified current behavior;
* risk inferences;
* accepted intentional differences;
* optional refactoring;
* rejected alternatives.

---

## 13. Deadline and process-exit constraints

Do not solve the problem merely by increasing:

```text
TimeoutStopSec=30s
```

Do not assume any one of these proves bounded process exit:

```text
asyncio task cancellation
asyncio.wait_for around a blocking thread
ThreadPoolExecutor.shutdown(wait=False)
cancel_futures=True
a coordinator stop flag
waking a runner
cancelling only its outer asyncio task
```

Analyze actual Python thread lifetime, executor ownership, blocking I/O, event-loop shutdown, subprocess-group behavior, and application durability.

The plan must define:

* one exact internal production budget or a narrowly justified configurable value;
* the safety reserve beneath 30 seconds;
* monotonic deadline creation and propagation;
* cleanup ordering;
* behavior when remaining budget is exhausted;
* component-specific cancellation/termination behavior;
* what is awaited;
* what is force-terminated;
* what is safely left to durable startup recovery;
* what observability is emitted;
* what must never be logged.

Do not present a numerical budget without explaining the reserve and proving that the planned tests can validate it deterministically.

---

## 14. Durable recovery constraints

Preserve existing upload, validation, publication, media-analysis, YouTube, and X product outcomes.

The plan must identify exact existing durable invariants rather than merely saying “restart will recover.”

For every operation that may be cancelled, abandoned, or interrupted, state:

* durable state before work begins;
* transient filesystem or database state during work;
* atomic or idempotent boundary;
* startup reconciliation path;
* retry behavior;
* duplicate-work behavior;
* cleanup behavior;
* evidence that process interruption cannot silently publish partial media or lose a durable claim.

Do not introduce a schema or Alembic migration merely to simplify lifecycle control.

Expected schema remains:

```text
0028
```

If exact evidence shows the objective cannot be met without a schema or product-state change, stop and report the contradiction rather than expanding scope.

---

## 15. Runner observability constraints

Design a bounded runner-failure visibility contract.

It must address:

* runner task unexpectedly finishing;
* runner task raising;
* repeated work failures that are currently converted to “no progress”;
* startup-time failure;
* shutdown-time expected cancellation;
* logging severity and rate;
* secret and private-payload exclusion;
* whether service health, startup failure, structured logs, or another existing operator surface should represent the failure;
* how observability remains testable without real provider calls.

Do not design a general monitoring platform or distributed supervisor.

---

## 16. Focused test plan

Propose exact new or modified tests with target files or narrowly described new filenames.

The focused matrix must prove, proportionately:

1. normal startup and reverse-order cleanup;
2. partial-startup rollback;
3. one global deadline that cannot be multiplied by six;
4. timeout behavior when one coordinator consumes the remaining budget;
5. cancellation of fake slow asyncio work;
6. safe handling of fake blocking executor work;
7. bounded YouTube and X child-process-group termination;
8. child reaping;
9. expected versus unexpected runner completion;
10. repeated runner failure visibility;
11. unchanged accepted domain outcomes;
12. durable SQLite and staging recovery after interruption;
13. process-level SIGTERM exit inside the internal envelope;
14. reserve below the external 30-second limit;
15. no provider calls or production data;
16. schema `0028` preservation.

Use injected millisecond-scale budgets and deterministic fakes for most tests.

Do not design tests that sleep for the actual 30-second production timeout.

Select the smallest sufficient existing regression set. Do not propose a full-suite run by default unless exact coupling evidence makes it necessary.

Do not propose FrameNest test retirement by analogy with AP’s retired monolithic test suite. The predecessor found no evidence-backed obsolete FrameNest test surface safe to remove.

---

## 17. Exact plan deliverables

The terminal report must contain one decision-complete plan with:

1. fresh restoration-gate results;
2. verified public/local/AP-pin state;
3. exact Meta paths consulted and their contribution;
4. verified lifecycle behavior matrix for all six coordinators;
5. exact external and proposed internal stop-budget model;
6. selected minimal architecture;
7. rejected alternatives and why;
8. startup ordering and partial-startup rollback;
9. reverse-order deadline propagation;
10. asyncio cancellation semantics;
11. executor and blocking-thread semantics;
12. subprocess-group termination and reaping semantics;
13. runner-failure observability contract;
14. exact durable recovery invariants;
15. exact proposed mutation allowlist;
16. explicit exclusions;
17. exact proposed test changes;
18. smallest existing regression-test selection;
19. process-level SIGTERM acceptance design;
20. candidate Git/worktree strategy preserving owner state;
21. publication boundary;
22. deployment and production-acceptance boundary;
23. rollback strategy;
24. residual risks;
25. stop conditions;
26. AP empirical observations, if any;
27. `Resolved Execution Issues / Near-Misses`, without chain-of-thought.

The mutation allowlist must be based on inspected causal evidence. Do not copy the complete inspection surface into the allowlist automatically.

The plan must be precise enough that a fresh Worker 2 could implement it under a separately issued prompt without reopening architecture.

Do not generate Worker 2’s prompt yourself.

---

## 18. Explicit exclusions

Do not include:

```text
YouTube/X domain-model unification
generic distributed job queue
multiprocess leases
SQLite WAL redesign
schema or Alembic migration
upload or acquisition product-state changes
provider calls
app.js split
broad UI/UX work
backup or restore redesign
NUC hardening
UFW or AppArmor
VPS
Kiosk
Tailscale or exit-node work
static X photo acquisition
multi-model metadata comparison
Tauri or desktop integration
Cover Studio expansion
multi-device synchronization
test-retirement work
unrelated stale-documentation repair
AP implementation
Meta implementation
```

VPS, Kiosk, exit-node work, and broad network redesign are explicitly deferred by the COOPERATOR.

The NUC is headless, and the CachyOS workstation and NUC are currently on the same router over Wi-Fi. These facts do not grant host authority and are not relevant implementation scope for this planning phase.

---

## 19. Python environment constraints

Canonical FrameNest virtual environment:

```text
/home/agile/Projects/framenest/.venv
```

Its previously observed `pyvenv.cfg` identified uv-managed CPython 3.13.9 with base executable:

```text
/home/agile/.local/share/uv/python/cpython-3.13.9-linux-x86_64-gnu/bin/python3.13
```

A known Cursor AppImage environment defect can inject `LD_LIBRARY_PATH` and break Python prefix/stdlib discovery, including:

```text
Failed to import encodings module
ModuleNotFoundError: No module named 'encodings'
```

This is not evidence of a FrameNest lifecycle defect.

Do not:

* delete or rebuild `.venv`;
* run `poetry env use`;
* run `uv sync`;
* change dependencies;
* repair the environment;
* attribute the anomaly to this logical whole.

Planning should normally require only static read-only inspection. If an environment anomaly prevents required read-only evidence, report it truthfully without mutation.

---

## 20. Candidate, publication, and deployment boundaries

An accepted plan does not authorize implementation.

The ORCHESTRATOR will review the plan against:

* exact repository evidence;
* the 30-second external constraint and internal reserve;
* thread and child-process semantics;
* durable recovery;
* closed-state protection;
* bounded path allowlist;
* focused testability;
* absence of schema/product/UI expansion;
* safe isolated candidate strategy.

If accepted, implementation requires a new complete prompt for fresh Worker 2 containing:

```text
Worker session target: fresh-worker-session
Native planning mode: not-used
```

A likely later evidence chain is:

```text
fresh Worker 1 — planning
ORCHESTRATOR plan decision
fresh Worker 2 — bounded implementation candidate
fresh Worker 3 — independent exact-candidate acceptance
fresh publication Worker — ordinary non-force fast-forward publication
separately authorized deployment or production acceptance only if required
ORCHESTRATOR closure
```

This is anticipated sequencing, not authority granted to you.

No force push is permitted.

No deployment should occur merely to equalize public repository and production SHAs.

No production or NUC action is authorized in this phase.

---

## 21. Stop conditions

Stop and report `BLOCKED` rather than guessing if:

* AP or FrameNest public `main` differs from the issuance-time anchor;
* the exact public FrameNest commit cannot be inspected read-only;
* governing AP identity cannot be established;
* unexpected tracked state overlaps the causal surface;
* repository instructions contradict this authority envelope;
* the objective requires schema or accepted product-state changes;
* a safe bounded process-exit design cannot be supported by current code evidence;
* a material security defect is discovered that would require scope expansion;
* required evidence would require secrets, production access, provider calls, dependency changes, or repository mutation;
* the plan cannot preserve durable recovery and accepted domain outcomes.

A Meta trace absence, delay, or divergence is classified but is not automatically blocking when higher-ranked evidence suffices.

Do not request implementation authority inside the report.

---

## 22. Terminal report contract

Your first output after completing the bounded planning work must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Then include exactly once:

```text
Logical whole identity: framenest-in-process-lifecycle-runtime-contract
Worker session ordinal: 01
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: planning-PASS | planning-PARTIAL | planning-BLOCKED
Result artifact or commit: terminal planning report; no repository artifact or commit
Result evidence: <concise exact evidence anchors>
Logical-whole closure: not-closed
Report justification: <new-evidence, partial-evidence, or blocking evidence>
Authority expiry: all Worker 1 authority expired at this terminal report
```

Use one actual value where alternatives are shown.

`PASS` requires a repository-grounded, internally coherent, decision-complete implementation plan satisfying this prompt.

`PARTIAL` must identify the exact missing evidence and must not pretend to authorize a second automatic planning cycle.

`BLOCKED` must identify the exact causal blocker and the smallest ORCHESTRATOR decision or renewed evidence route needed.

Include:

```text
AP empirical observations: none
```

unless actual execution evidence reveals a concrete AP defect or improvement opportunity. If there is one, report it as non-authorizing evidence only. Do not mutate AP or open an AP logical whole.

Include a concise:

```text
Resolved Execution Issues / Near-Misses
```

section. Report observable issues and resolutions without private chain-of-thought.

Submitting the terminal report ends this Worker session’s authority.

Do not implement, commit, publish, deploy, access production, mutate AP, mutate Meta, or continue working after the terminal report.
