# Authoritative Prompt for Fresh Worker 2

## FrameNest In-Process Lifecycle Runtime Contract — Bounded Implementation Candidate

You are fresh Worker 2 for one active FrameNest logical whole conducted under Analytic Programming.

Read this complete prompt before taking any action.

Worker 1 completed repository-grounded implementation planning. The ORCHESTRATOR has reviewed that plan against exact repository evidence and accepted it with the binding corrections stated below.

Your task is to create one tested local implementation candidate from the exact accepted public baseline.

Do not enter Native Plan Mode. Do not produce another architecture plan. Implement the accepted bounded design, validate it, create one local commit, report, and stop.

---

## 1. Identity and execution routing

```text
Logical whole identity: framenest-in-process-lifecycle-runtime-contract
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Phase: implementation
Worker profile: FrameNest In-Process Lifecycle Runtime Contract Implementer
Evidence posture: non-independent
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
```

Reasoning configuration selected by the COOPERATOR:

```text
Extra High
```

Michal controls the actual model, provider, client, reasoning configuration, and launch decision. No model or provider identity grants authority.

Delegation, sub-agents, parallel Workers, Explore tasks, or hidden secondary workstreams are not authorized.

---

## 2. Roles and report language

```text
COOPERATOR: Michal
ORCHESTRATOR: ORCHESTRATOR_CHAT
WORKER: this fresh implementation session
```

Repository code, code documentation, test names, commit subject, and the terminal Worker report must use professional English.

The terminal implementation report must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

The Planner-specific artifact-first output proposal does not apply to this implementation phase.

Do not expose private chain-of-thought. Report decisions, evidence, commands, results, resolved issues, and residual risks concisely.

---

## 3. Authority envelope

Authorized:

```text
Implementation authority: explicit and bounded by this prompt
Repository mutation authority: exact isolated worktree and exact allowlist only
Worktree authority: one exact isolated worktree
Branch authority: one exact local candidate branch
Commit authority: one local commit after mandatory gates pass
Push authority: none
Publication authority: none
Deployment authority: none
Production authority: none
NUC/SSH/sudo authority: none
Provider authority: none
AP mutation authority: none
Meta mutation authority: none
Dependency authority: none
Schema-migration authority: none
Delegation authority: none
```

Do not:

* push;
* force-push;
* deploy;
* SSH to the NUC;
* invoke sudo;
* mutate systemd or host state;
* access production;
* call YouTube, X, OpenAI, or another external provider;
* access secrets, `.env`, credentials, cookies, browser profiles, private media, or unrelated private data;
* mutate `cisarik/ap` or `cisarik/meta`;
* change the FrameNest `.ap` gitlink;
* change dependencies, `pyproject.toml`, or `poetry.lock`;
* adopt or delete an incidental `uv.lock`;
* create, delete, rebuild, move, or relink the canonical `.venv`;
* run `uv sync`, `uv lock`, `pip install`, or `poetry env use`;
* launch `cursor`, `code`, `xdg-open`, a GUI program, or an AppImage;
* use `git add .` or `git add -A`;
* clean, reset, restore, stash, rebase, merge, or normalize the canonical owner checkout;
* implement unrelated refactors or adjacent backlog items;
* close the logical whole.

Implementation PASS is not acceptance, publication, deployment, production acceptance, or ORCHESTRATOR closure.

---

## 4. Canonical repositories and immutable baseline

Canonical FrameNest repository:

```text
/home/agile/Projects/framenest
```

Canonical AP repository:

```text
/home/agile/Projects/ap
```

Exact accepted FrameNest baseline:

```text
commit: a72be476f5634394287082be07380d03fa7ccd4d
parent: d4c3402a4765b39cee0d8e2063d5ec8be161caf6
tree: 5f8afa3d2705fd9a60d8375e963699e9be5e9335
subject: chore: adopt current AP generation
.ap gitlink: 041de310ea33ed1b47dd8f5fbfcc2829d1a32514
schema head: 0028
```

Issuance-time public refs verified by the ORCHESTRATOR:

```text
cisarik/ap refs/heads/main
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

cisarik/framenest refs/heads/main
a72be476f5634394287082be07380d03fa7ccd4d
```

Before mutation, verify both refs through credential-free Git transport:

```text
git ls-remote https://github.com/cisarik/ap.git refs/heads/main
git ls-remote https://github.com/cisarik/framenest.git refs/heads/main
```

Do not use GitHub webpages, search caches, remembered refs, or repository badges as current-ref evidence.

If either public ref differs, stop before mutation and report `BLOCKED`.

---

## 5. Required repository reading

Read and obey from the exact FrameNest baseline:

```text
AGENTS.md
docs/WORKER_EXECUTION_CONTRACT.md
ap.project.conf
.ap/AP.md
.ap/AP_WORKER.md
.ap/PROMPT_CONTRACTS.md
```

Also inspect every source and test file in the authorized mutation surface before changing it.

Repository instructions and this prompt must be reconciled. If they conflict materially, stop and report the exact conflict.

---

## 6. External Meta trace disposition

```text
External trace disposition: configured
Trace discovery: cisarik/meta; projects/framenest
Trace project key: framenest
Trace logical-whole projection identity: framenest-in-process-lifecycle-runtime-contract
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
```

Direct Meta inspection for Worker 2:

```text
not required
```

Reason:

The ORCHESTRATOR has already reconciled the planning artifact, exact public repository evidence, and binding implementation corrections into this complete prompt. Reading additional historical Meta exchanges would duplicate context without changing implementation authority.

Do not inspect unrelated Meta history and do not mutate Meta.

---

## 7. Preserve the canonical owner checkout

Previously observed canonical owner state:

```text
branch: feat/ap-baseline-bound-execution-adoption
upstream: none
local HEAD: d4c3402a4765b39cee0d8e2063d5ec8be161caf6
origin/main: a72be476f5634394287082be07380d03fa7ccd4d
```

Previously observed untracked owner material:

```text
.accept-immut-work/
.playwright-mcp/
.w6-immut-work/
REPRO_DIR=/
uv.lock
```

Verify current state read-only.

Do not inspect those directories recursively, delete them, stage them, or normalize them.

Unexpected non-overlapping owner state is preserved and reported. Unexpected tracked state overlapping the implementation surface is a blocker.

Do not checkout public `main` in the canonical owner worktree.

---

## 8. Exact isolated worktree strategy

Authorized candidate branch:

```text
feat/in-process-lifecycle-runtime-contract
```

Authorized isolated worktree:

```text
/home/agile/Projects/framenest-worktrees/framenest-in-process-lifecycle-runtime-contract-w2
```

Before creation, verify:

* the path does not already exist;
* the branch does not already exist;
* no existing worktree owns the branch;
* baseline object `a72be476…` exists locally;
* the canonical owner checkout will remain untouched.

If the path or branch already exists, do not delete or reuse it. Stop and report `BLOCKED`.

Authorized worktree creation is equivalent to:

```text
git -C /home/agile/Projects/framenest worktree add \
  -b feat/in-process-lifecycle-runtime-contract \
  /home/agile/Projects/framenest-worktrees/framenest-in-process-lifecycle-runtime-contract-w2 \
  a72be476f5634394287082be07380d03fa7ccd4d
```

Creating the exact parent directory is authorized if absent.

Immediately verify in the new worktree:

```text
HEAD = a72be476f5634394287082be07380d03fa7ccd4d
branch = feat/in-process-lifecycle-runtime-contract
upstream = none
tracked/index state = clean
```

You may initialize only the `.ap` submodule inside the isolated worktree to the exact recorded gitlink if this can be done without changing the canonical owner `.ap` checkout or the gitlink.

If the Git worktree/submodule topology would alter canonical `.ap` state, do not proceed with submodule initialization. Use the already verified canonical AP executable and direct exact-source test route, or report the limitation if AP validation cannot otherwise be established.

No other branch, ref, or worktree mutation is authorized.

---

## 9. ORCHESTRATOR plan decision

```text
Plan decision: ACCEPTED WITH BINDING CORRECTIONS
Implementation authorization: explicit
Architecture reopening: prohibited
```

Accepted architecture:

* one monotonic application-lifecycle deadline;
* composition-root shutdown supervision;
* reverse-order cleanup;
* partial-startup rollback;
* deadline-aware coordinator shutdown;
* interruption of owned subprocess groups;
* cooperative cancellation at known blocking boundaries;
* durable restart recovery;
* focused deterministic tests;
* no schema change;
* no product-domain unification.

### Binding correction 1 — no forced self-termination

Do not implement:

```text
os._exit(...)
sys.exit(...)
raise SystemExit
os.kill(os.getpid(), ...)
```

or another application-controlled forced self-termination fallback.

A forced successful exit would bypass Python cleanup, buffered logging, engine disposal, and normal observability while disguising an unresolved lifecycle defect.

If the proven application contract cannot fit beneath the systemd envelope without forced self-termination, report `PARTIAL` or `BLOCKED`. Do not force PASS.

### Binding correction 2 — exact 30-second budget model

Uvicorn 0.49.0 applies `timeout_graceful_shutdown` before application lifespan shutdown while waiting for connections and server tasks.

Implement and test this allocation:

```text
External systemd TimeoutStopSec: 30 seconds
Uvicorn connection/task grace: 5 seconds
Application lifespan shutdown budget: 20 seconds
Minimum remaining external reserve: 5 seconds
```

Do not describe the full ten seconds outside the application deadline as unused reserve. Five seconds are explicitly allocated to Uvicorn before lifespan shutdown.

The application creates one monotonic absolute deadline when lifespan shutdown begins. Every coordinator and final engine-disposal step sees the same remaining budget. No component receives a new 20-second allowance.

Production values are code-owned constants, not new environment variables or settings fields.

Tests use injected millisecond-scale budgets.

### Binding correction 3 — lifecycle-owned process runners only

Do not create one global subprocess runner shared across unrelated request/API operations.

Create distinct interruptible runner instances only for background lifecycle-owned operations that require shutdown interruption, including:

* background upload validation ffprobe execution;
* background automatic media-analysis ffprobe/ffmpeg execution.

Existing request-time cover, preview, suggestion, and movie-identification adapters remain independent unless direct causal evidence proves otherwise. Do not expand into unrelated request-path lifecycle management.

### Binding correction 4 — executor truthfulness

`ThreadPoolExecutor.shutdown(wait=False)` and `cancel_futures=True` do not kill a running CPython thread.

Implementation must:

* stop new claims;
* wake runners;
* cooperatively interrupt or cancel known long-running work;
* await completion only within the shared remaining deadline;
* interrupt owned subprocess groups;
* avoid synchronous `shutdown(wait=True)` after the deadline is exhausted;
* call `wait=True` only when the running work is already known to have settled;
* use `wait=False, cancel_futures=True` only as bounded cleanup of pending work;
* log remaining unresolved work truthfully;
* never claim process-exit safety solely from executor shutdown flags.

Where long filesystem loops are part of lifecycle-owned publication or validation work, introduce the smallest thread-safe cooperative stop probe at safe chunk boundaries while preserving crash recovery.

Do not convert an intentional lifecycle interruption into a permanent user-visible content failure when existing restart recovery is the correct result.

### Binding correction 5 — X acquisition recovery

Keep YouTube and X domain behavior distinct.

X inspection and download currently execute synchronous subprocess work on the event loop. Move those calls to a bounded thread boundary so the event loop remains capable of initiating shutdown.

The X extractor must support thread-safe interruption of its currently owned process group. The worker thread remains responsible for reaping its direct child.

On restart, an asset durably left in:

```text
XAssetState.ACQUIRING
```

must be treated as interrupted acquisition work:

* clear its claim-owned staging before retry;
* retry the existing asset without creating a duplicate asset;
* preserve its stable identity;
* do not introduce a schema migration;
* do not unify X with YouTube;
* do not allow partial `artifact.mp4` bytes to be accepted under `--no-overwrites`.

The current X staging port defines `clear(stage_key)`, but `FilesystemXStaging` does not implement it. Add the smallest correct implementation delegating to its descriptor-safe cleanup behavior and prove it.

### Binding correction 6 — systemd and health stay unchanged

Do not modify:

```text
deploy/systemd/framenest.service
```

It remains the immutable external alignment constraint:

```text
KillSignal=SIGTERM
TimeoutStopSec=30s
Restart=on-failure
```

Set Uvicorn:

```text
timeout_graceful_shutdown=5
```

in `src/framenest/server.py`.

Do not change `/health`, its payload, or product-visible API behavior.

---

## 10. Required implementation behavior

### 10.1 Lifecycle helper

Create:

```text
src/framenest/application/in_process_lifecycle.py
```

It must provide the smallest coherent implementation for:

* monotonic absolute deadline creation;
* validated non-negative remaining time;
* deadline-aware awaiting;
* reverse-order shutdown;
* continuation after one coordinator shutdown fault;
* bounded sanitized observability;
* deterministic injectable test clocks or budgets.

Do not create a broad framework, generic job supervisor, Coordinator ABC hierarchy, or distributed queue.

A small structural protocol is permitted only if it reduces false coupling and remains limited to lifecycle start/shutdown behavior.

### 10.2 Composition-root lifespan

Replace the nested unbounded `finally` structure in:

```text
src/framenest/adapters/api/application.py
```

with explicit started-resource tracking and reverse-order bounded cleanup.

Requirements:

* preserve startup order:

  ```text
  media analysis
  upload catalog
  upload publication
  upload validation
  YouTube acquisition
  X acquisition
  ```

* preserve reverse shutdown order;

* clean only successfully started resources after partial startup failure;

* continue later cleanup after one shutdown error;

* use one application deadline;

* include final engine disposal inside the bounded cleanup design;

* preserve dependency injection and existing API behavior;

* permit small injected shutdown budgets for tests;

* add no new settings or environment field.

### 10.3 Four executor-backed coordinators

Update:

```text
UploadValidationCoordinator
UploadCatalogCoordinator
UploadPublicationCoordinator
MediaAnalysisCoordinator
```

to accept the shared deadline contract without forcing unrelated methods into a generic abstraction.

Preserve intentional semantics of:

```text
start
notify
drain
runner_done
```

Requirements:

* stop claiming new work before waiting;
* wake the runner;
* expose unexpected runner completion through sanitized logging;
* distinguish expected shutdown cancellation from runner failure;
* retain existing durable recovery behavior;
* settle owned executors truthfully;
* avoid event-loop blocking executor shutdown after deadline;
* preserve external-executor ownership behavior;
* do not change accepted upload/catalog/publication/analysis product outcomes.

### 10.4 YouTube acquisition

Preserve existing YouTube cancel-on-shutdown behavior.

Implement:

* deadline-aware shutdown;
* bounded TERM/KILL process-group termination using remaining budget;
* guaranteed child reaping when termination succeeds;
* expected cancellation without error logging;
* one sanitized signal for unexpected runner death or exception;
* bounded/rate-controlled visibility for repeated runner-iteration failure;
* no URL, token, cookie, media name, filesystem path, or secret leakage.

Preserve the normal 7,200-second acquisition timeout outside shutdown. Do not turn ordinary downloads into 20-second operations.

### 10.5 X acquisition

Implement:

* event-loop-safe `inspect` and `download` execution;
* deadline-aware shutdown;
* thread-safe interrupt request;
* bounded process-group TERM/KILL;
* direct-child reaping by the owning worker path;
* interrupted `ACQUIRING` recovery;
* staging cleanup before retry;
* no X/YouTube unification;
* no static-photo expansion;
* unchanged requester privacy and administrator boundaries.

`drain()` remains cooperative and test-oriented. Process shutdown may interrupt in-flight extractor work.

### 10.6 Media-analysis and validation subprocesses

Make `SubprocessRunner` safely interruptible for lifecycle-owned background work.

Requirements:

* process groups remain session-owned;
* active-process registration is thread-safe;
* interruption is idempotent;
* direct children are reaped;
* stdout/stderr reader cleanup remains bounded;
* no raw command, media path, or private payload leakage;
* request-time adapters are not globally interrupted by server lifecycle shutdown.

### 10.7 Durable recovery

Preserve schema head:

```text
0028
```

Verify and preserve:

* validation restart recovery for `VALIDATING`;
* publication temporary-file and verified-commit ordering;
* catalog idempotence;
* media-analysis `ANALYZING` reconciliation;
* YouTube `DOWNLOADING` to `DOWNLOAD_PENDING`;
* X interrupted `ACQUIRING` retry after staging cleanup.

No Alembic revision is authorized.

---

## 11. Exact source mutation allowlist

Only these source paths may be created or modified:

```text
src/framenest/application/in_process_lifecycle.py
src/framenest/adapters/api/application.py
src/framenest/server.py

src/framenest/application/upload_validation_coordinator.py
src/framenest/application/upload_catalog_coordinator.py
src/framenest/application/upload_publication_coordinator.py
src/framenest/application/media_analysis_coordinator.py
src/framenest/application/youtube_acquisition.py
src/framenest/application/x_acquisition.py

src/framenest/application/upload_validation.py
src/framenest/application/upload_publication.py

src/framenest/application/ports/published_media_storage.py
src/framenest/application/ports/x_extractor.py

src/framenest/infrastructure/filesystem/published_media_storage.py
src/framenest/infrastructure/media_analysis/process.py
src/framenest/infrastructure/media_validation/ffprobe.py
src/framenest/infrastructure/youtube/downloader.py
src/framenest/infrastructure/x/downloader.py
src/framenest/infrastructure/x/staging.py
```

Do not modify every allowed file automatically. Change only paths causally required by the implementation.

If a source change outside this allowlist becomes necessary, stop and report the exact missing path and reason. Do not expand authority yourself.

---

## 12. Exact test mutation allowlist

Only these test paths may be created or modified:

```text
tests/unit/application/test_in_process_lifecycle.py
tests/integration/test_process_sigterm_lifecycle.py
tests/unit/infrastructure/test_x_staging.py

tests/unit/application/test_upload_validation_coordinator.py
tests/unit/application/test_upload_catalog_coordinator.py
tests/unit/application/test_upload_publication_coordinator.py
tests/unit/application/test_media_analysis_coordinator.py
tests/unit/application/test_x_acquisition_lifecycle.py
tests/unit/application/test_upload_validation.py
tests/unit/application/test_media_analysis_lifecycle.py

tests/integration/test_youtube_acquisition_lifecycle.py
tests/integration/test_atomic_upload_publication.py

tests/unit/infrastructure/media_analysis/test_process.py
tests/unit/infrastructure/media_validation/test_ffprobe.py
tests/unit/infrastructure/filesystem/test_published_media_storage.py
tests/unit/infrastructure/youtube/test_downloader.py
tests/unit/infrastructure/test_x_downloader_adapter.py

tests/unit/test_server_runtime.py
tests/contract/test_health_api.py
tests/contract/test_server_process_output.py
```

The following existing alignment test must be run but not modified:

```text
tests/contract/test_fedora_systemd_service.py
```

If a required test mutation falls outside the allowlist, stop and report it.

---

## 13. Mandatory focused evidence

Use deterministic fakes and millisecond-scale injected deadlines.

Prove at least:

1. one monotonic application deadline is shared across all shutdown steps;
2. six sequential shutdowns cannot each receive a fresh full timeout;
3. reverse shutdown order is preserved;
4. partial startup cleans only resources that started;
5. one shutdown exception does not prevent later cleanup;
6. engine disposal remains in the final cleanup path;
7. normal coordinator shutdown remains clean;
8. expired deadlines do not trigger blocking executor waits;
9. known subprocess-backed thread work is interrupted and settles;
10. YouTube TERM/KILL respects remaining budget;
11. YouTube child processes are reaped;
12. X synchronous extraction no longer blocks the event loop;
13. X shutdown interrupts its active process group;
14. X interrupted `ACQUIRING` state retries after descriptor-safe staging cleanup;
15. no duplicate X asset is created during recovery;
16. media-analysis subprocess interruption is idempotent and reaps children;
17. validation ffprobe interruption remains recoverable;
18. publication cooperative interruption leaves durable retryable state and no partial final media;
19. unexpected runner death is observable once and does not leak private data;
20. expected shutdown cancellation does not produce an error;
21. Uvicorn is configured with `timeout_graceful_shutdown=5`;
22. systemd remains `TimeoutStopSec=30s`;
23. `/health` remains unchanged;
24. schema remains `0028`;
25. a temporary fake-provider-free FrameNest process receiving SIGTERM exits within the injected envelope;
26. no fake child survives the process-level test;
27. temporary SQLite and staging state remains recoverable.

Do not sleep for the real 30-second production envelope.

No real provider, real media library, NUC, or production data may be used.

---

## 14. Python runtime and exact-source execution

Canonical interpreter:

```text
/home/agile/Projects/framenest/.venv/bin/python
```

The isolated worktree must execute candidate source through:

```text
PYTHONPATH=/home/agile/Projects/framenest-worktrees/framenest-in-process-lifecycle-runtime-contract-w2/src
```

Before trusting tests, prove:

```text
framenest.__file__
```

resolves beneath the isolated worktree.

The Cursor/AppImage shell may inject a broken `LD_LIBRARY_PATH`. If necessary, remove it only for the individual command:

```text
env -u LD_LIBRARY_PATH ...
```

Do not alter the global shell, canonical environment, or `.venv`.

Set:

```text
PYTHONDONTWRITEBYTECODE=1
```

for direct candidate execution when practical.

An environment failure is not a candidate defect. Classify it truthfully and do not rebuild the environment.

---

## 15. Mandatory validation sequence

### Gate A — provenance

Prove the exact interpreter and source path resolve to the isolated candidate.

### Gate B — focused changed-surface tests

Run the new and modified lifecycle, coordinator, subprocess, downloader, staging, publication, validation, server, and SIGTERM tests.

Every mandatory command must exit zero.

### Gate C — smallest sufficient regression set

Run at least:

```text
tests/unit/application/test_upload_validation_coordinator.py
tests/unit/application/test_upload_catalog_coordinator.py
tests/unit/application/test_upload_publication_coordinator.py
tests/unit/application/test_media_analysis_coordinator.py
tests/unit/application/test_upload_validation.py
tests/unit/application/test_media_analysis_lifecycle.py
tests/unit/application/test_x_acquisition_lifecycle.py
tests/integration/test_youtube_acquisition_lifecycle.py
tests/integration/test_atomic_upload_publication.py
tests/unit/infrastructure/media_analysis/test_process.py
tests/unit/infrastructure/media_validation/test_ffprobe.py
tests/unit/infrastructure/filesystem/test_published_media_storage.py
tests/unit/infrastructure/youtube/test_downloader.py
tests/unit/infrastructure/test_x_downloader_adapter.py
tests/unit/test_server_runtime.py
tests/contract/test_health_api.py
tests/contract/test_server_process_output.py
tests/contract/test_fedora_systemd_service.py
```

A full repository suite is not required unless changed-surface evidence demonstrates broader coupling.

### Gate D — repository integrity

Run:

```text
git diff --check
```

Verify:

* only allowlisted paths changed;
* `.ap` gitlink remains exact;
* schema remains `0028`;
* `deploy/systemd/framenest.service` is byte-identical to baseline;
* no dependency or lockfile changed;
* no untracked owner content entered the candidate;
* no credentials or private paths entered the diff.

### Gate E — AP project validation

Using the exact pinned AP generation, run the candidate-compatible project check and focused execution operations if they can be performed without changing canonical owner state.

A non-zero mandatory AP command prevents PASS. If an AP command is unavailable solely because isolated-worktree submodule topology cannot be established without altering canonical state, report the exact acceptance limitation and preserve all direct exact-source evidence. Do not mutate canonical `.ap` to force the gate.

---

## 16. Failure classification

Classify failures as:

```text
candidate defect
harness defect
environment defect
acceptance limitation
non-blocking observation
```

A traceback, non-zero mandatory test, surviving child process, unexplained thread, schema drift, unauthorized path, or unresolved durable-state failure prevents implementation PASS.

Fix candidate defects only inside the authorized surface.

A harness correction is permitted only inside the exact test allowlist and only when the test is demonstrably wrong relative to the accepted contract.

Do not hide or skip a failing gate.

Do not weaken an existing invariant merely to make a new test pass.

---

## 17. Commit authority

After all mandatory gates pass, create exactly one local commit on:

```text
feat/in-process-lifecycle-runtime-contract
```

Required subject:

```text
fix: bound in-process lifecycle shutdown
```

Stage only exact authorized changed paths using explicit path arguments.

Do not use:

```text
git add .
git add -A
```

The commit must have exact parent:

```text
a72be476f5634394287082be07380d03fa7ccd4d
```

After committing, verify and report:

* candidate commit SHA;
* parent SHA;
* tree SHA;
* commit subject;
* exact changed paths and modes;
* worktree cleanliness;
* `.ap` gitlink;
* schema head;
* no upstream;
* no push.

If the parent is not exact, do not commit.

If mandatory validation does not pass, do not create a misleading candidate commit. Report `PARTIAL` or `BLOCKED`.

---

## 18. Explicit exclusions

Do not implement:

```text
os._exit or forced self-termination
systemd TimeoutStopSec changes
deployment scripts
NUC access or sudo changes
network architecture changes
Tailscale or exit-node work
VPS or Kiosk work
NUC hardening
YouTube/X domain unification
distributed job queue
multiprocess leases
SQLite WAL redesign
schema or Alembic migration
provider calls
static X photo acquisition
app.js refactoring
UI/UX changes
backup or restore redesign
test retirement
health endpoint expansion
new settings or environment fields
dependency changes
AP changes
Meta changes
unrelated documentation cleanup
```

Do not repair adjacent stale status documentation.

Record genuinely useful out-of-scope FrameNest observations as non-authorizing ledger candidates in the terminal report. Do not implement them.

---

## 19. Stop conditions

Stop and report rather than guessing if:

* public AP or FrameNest baseline changed;
* canonical owner state overlaps the mutation surface;
* the exact worktree path or branch already exists;
* the exact baseline cannot be inspected;
* `.ap` cannot be reconciled safely;
* a required source/test path lies outside the allowlist;
* the deadline cannot be met without forced process termination;
* a running non-daemon thread cannot be bounded or interrupted by the accepted design;
* child-process cleanup cannot be proven;
* durable recovery cannot be preserved;
* schema or accepted product behavior would need to change;
* a security defect requires broader authority;
* production, provider, secrets, dependency, or NUC access would be required;
* a mandatory gate exits non-zero.

Do not return to Native Plan Mode. State the exact blocker and the smallest missing authority or design decision.

---

## 20. Terminal report contract

The terminal report must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Then include exactly once:

```text
Logical whole identity: framenest-in-process-lifecycle-runtime-contract
Worker session ordinal: 02
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS | not-applicable
Result artifact or commit: <exact candidate commit or not-applicable>
Result evidence: <bounded exact evidence>
Logical-whole closure: not-closed
Report justification: new-mutation | new-evidence | new-material-risk
Authority expiry: all Worker 2 authority expired at this terminal report
```

For `PASS`, use:

```text
Phase-qualified result: implementation-PASS
Report justification: new-mutation
```

For `PARTIAL` or `BLOCKED`, use:

```text
Phase-qualified result: not-applicable
```

The report must include:

1. authority and fresh-session confirmation;
2. public-ref verification;
3. canonical owner-state preservation evidence;
4. isolated worktree and branch evidence;
5. start baseline;
6. concise implementation summary;
7. exact changed paths and purpose;
8. deadline-budget evidence;
9. subprocess, thread, and recovery evidence;
10. exact test commands, exit codes, and concise results;
11. failure classification;
12. AP project-validation result;
13. candidate commit, parent, tree, and subject;
14. `.ap` gitlink and schema evidence;
15. worktree cleanliness;
16. push/publication/deployment/production status;
17. residual risks;
18. `AP empirical observations: none` or concrete non-authorizing evidence;
19. `FrameNest ledger observations: none` or bounded non-authorizing candidates;
20. `Resolved Execution Issues / Near-Misses`.

Do not include private chain-of-thought.

Do not claim independent acceptance.

Do not generate the acceptance Worker prompt.

Do not push, deploy, SSH, invoke sudo, mutate production, or continue working after the terminal report.
