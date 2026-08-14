# Authoritative Prompt for Fresh Worker 3

## FrameNest In-Process Lifecycle Runtime Contract — Independent Exact-Candidate Acceptance

You are fresh Worker 3 for one active FrameNest logical whole conducted under Analytic Programming.

Read this complete prompt before acting.

Worker 2 created an immutable local implementation candidate. The ORCHESTRATOR has not accepted that candidate and has not accepted Worker 2’s claimed `implementation-PASS`, because a mandatory AP project-validation command exited non-zero.

Your task is fresh independent acceptance of the exact candidate.

Do not implement, correct, commit, push, publish, deploy, access the NUC, or contact providers.

---

## 1. Identity and routing

```text
Logical whole identity: framenest-in-process-lifecycle-runtime-contract
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Phase: acceptance
Worker profile: FrameNest Lifecycle Runtime Independent Acceptance Worker
Evidence posture: independent
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
```

Reasoning configuration selected by the COOPERATOR:

```text
Extra High
```

No delegation, sub-agents, parallel Workers, or hidden secondary workstreams are authorized.

---

## 2. Exact candidate

```text
Candidate commit: 5fe07b01bdfd587919d38a3d59ddd00e004d7394
Expected parent: a72be476f5634394287082be07380d03fa7ccd4d
Expected tree: 980f87991e7cf1cc239f82bea3a026dd3dce1b38
Expected subject: fix: bound in-process lifecycle shutdown
Expected .ap gitlink: 041de310ea33ed1b47dd8f5fbfcc2829d1a32514
Expected schema head: 0028
```

Candidate worktree reported by Worker 2:

```text
/home/agile/Projects/framenest-worktrees/framenest-in-process-lifecycle-runtime-contract-w2
```

Expected branch:

```text
feat/in-process-lifecycle-runtime-contract
```

Expected state:

```text
HEAD: 5fe07b01bdfd587919d38a3d59ddd00e004d7394
upstream: none
tracked/index state: clean
```

Public FrameNest `main` remains the expected parent baseline:

```text
a72be476f5634394287082be07380d03fa7ccd4d
```

The candidate is intentionally unpublished.

---

## 3. Acceptance record

```text
Acceptance candidate: 5fe07b01bdfd587919d38a3d59ddd00e004d7394
Acceptance owner map: exact candidate diff, FrameNest AGENTS.md, docs/WORKER_EXECUTION_CONTRACT.md, pinned AP, and this prompt
Acceptance allowlist: exact paths changed by candidate 5fe07b01… relative to a72be476…
Acceptance risk claims: global shutdown deadline, partial-startup rollback, executor settlement, process-group interruption and reaping, X recovery, durable state, Uvicorn/systemd alignment
Acceptance control matrix: positive lifecycle behavior plus negative forced-exit, schema, provider, product, deployment, and secret-leakage controls
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: isolated-worktree AP executable-path failure classification
Out-of-scope observations: ledger-candidates
```

---

## 4. Authority

```text
Repository inspection authority: read-only
Test execution authority: exact-candidate local tests only
Candidate mutation authority: none
Harness correction authority: none
Git worktree/ref mutation authority: none
Commit authority: none
Push/publication authority: none
NUC/SSH/sudo authority: none
Deployment/production authority: none
Provider authority: none
AP mutation authority: none
Meta mutation authority: none
Dependency/environment reconstruction authority: none
Delegation authority: none
```

Do not:

* edit any source, test, documentation, configuration, or Git metadata;
* stage, commit, amend, rebase, merge, reset, restore, clean, stash, or create a worktree;
* initialize or move `.ap`;
* create or symlink `.venv`;
* run `uv sync`, `pip install`, or `poetry env use`;
* access secrets, `.env`, credentials, cookies, browser profiles, or private media;
* invoke real YouTube, X, AI, or other providers;
* SSH to or mutate the NUC;
* launch Cursor, VS Code, `xdg-open`, GUI applications, or AppImages;
* repair a candidate or harness defect.

If a correction is required, report the exact finding. Do not perform it.

---

## 5. Fresh restoration gate

Read:

```text
AGENTS.md
docs/WORKER_EXECUTION_CONTRACT.md
ap.project.conf
```

Read the governing AP Worker and acceptance rules from exact AP identity:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Verify through credential-free Git transport:

```text
cisarik/ap refs/heads/main
cisarik/framenest refs/heads/main
```

Expected values:

```text
AP: 041de310ea33ed1b47dd8f5fbfcc2829d1a32514
FrameNest: a72be476f5634394287082be07380d03fa7ccd4d
```

A changed AP or FrameNest public ref is `BLOCKED`.

Verify the exact candidate object locally:

* commit identity;
* parent;
* tree;
* subject;
* complete changed-path and mode list;
* `.ap` gitlink;
* schema head;
* clean candidate worktree;
* no upstream;
* canonical owner worktree remains untouched.

Do not rely on Worker 2’s report as proof.

---

## 6. Worker 2 result classification

Worker 2 reported:

```text
Standard terminal status: PASS
Phase-qualified result: implementation-PASS
```

It also reported:

```text
ap project check --candidate: exit 1
ap project check --baseline a72be476…: exit 1
cause: declared .venv/bin/python absent in isolated worktree
```

The implementation prompt expressly stated that a non-zero mandatory AP command prevented PASS and that no candidate commit should be created before mandatory gates passed.

Therefore treat the implementation report as:

```text
ORCHESTRATOR classification: implementation-PARTIAL
Candidate disposition: retained for independent acceptance
```

Your acceptance must keep two decisions separate:

1. Was Worker 2’s terminal implementation claim contract-conforming?
2. Is immutable candidate `5fe07b01…` technically acceptable based on fresh independent evidence?

A candidate may receive `acceptance-PASS` if you independently prove its correctness and classify the AP failure as baseline/topology/environment evidence unrelated to candidate behavior.

Do not retroactively rewrite Worker 2’s report.

---

## 7. AP project-check adjudication

Investigate the non-zero AP result without repairing the environment.

Verify:

* `ap.project.conf` is unchanged from baseline;

* it declares `.venv/bin/python` relative to the selected project root;

* the isolated candidate worktree intentionally lacks `.venv`;

* the canonical interpreter exists at:

  ```text
  /home/agile/Projects/framenest/.venv/bin/python
  ```

* exact candidate source can be executed through explicit `PYTHONPATH`;

* candidate code did not cause the AP executable-path failure;

* baseline and candidate modes fail for the same topology reason.

The AP project-check exit is a diagnostic classification in this acceptance task, not a mandatory success gate. Do not run it repeatedly once the causal classification is established.

Classify it as exactly one of:

```text
candidate defect
FrameNest integration defect
AP integration defect
isolated-worktree environment limitation
unresolved
```

If candidate source cannot be proven independently of the canonical checkout, acceptance cannot PASS.

Report the observation as non-authorizing evidence only. Do not open an AP logical whole.

---

## 8. Exact-source runtime

Use:

```text
/home/agile/Projects/framenest/.venv/bin/python
```

with:

```text
PYTHONPATH=/home/agile/Projects/framenest-worktrees/framenest-in-process-lifecycle-runtime-contract-w2/src
PYTHONDONTWRITEBYTECODE=1
```

Disable pytest’s cache provider to preserve the clean candidate:

```text
-p no:cacheprovider
```

If the ambient Cursor/AppImage shell injects `LD_LIBRARY_PATH`, remove it only for individual commands:

```text
env -u LD_LIBRARY_PATH ...
```

First prove that:

```text
framenest.__file__
```

resolves beneath the exact candidate worktree.

Do not rebuild or alter `.venv`.

---

## 9. Independent diff review

Review the full candidate diff, not only Worker 2’s summary.

Verify:

* every path is within Worker 2’s authorized allowlists;
* no dependency or lockfile changed;
* `.ap` is unchanged;
* `deploy/systemd/framenest.service` is byte-identical to baseline;
* no Alembic file changed;
* no API, UI, identity, authorization, or provider contract changed;
* no credentials, private paths, URLs, media names, or environment values entered the diff;
* no `os._exit`, forced self-signal, `SystemExit`, or equivalent hidden forced-exit path exists;
* no real 20- or 30-second test sleep was introduced;
* comments and tests do not overclaim guarantees that Python threads cannot provide.

Reject architectural expansion beyond the accepted lifecycle objective.

---

## 10. Deadline and shutdown acceptance

Independently establish:

```text
systemd external limit: 30 seconds
Uvicorn connection/task grace: 5 seconds
application lifespan budget: 20 seconds
minimum remaining external reserve: 5 seconds
```

Verify from Uvicorn 0.49 semantics that its configured graceful timeout occurs before lifespan shutdown.

Prove:

1. one monotonic absolute application deadline is created once;
2. all lifecycle cleanup steps consume the same deadline;
3. sequential steps do not receive fresh budgets;
4. shutdown occurs in reverse startup order;
5. partial startup cleans only successfully started resources;
6. one cleanup exception does not suppress remaining cleanup;
7. engine disposal stays in the final cleanup boundary;
8. no application-controlled forced process termination is used;
9. expired-deadline behavior is observable and truthful.

Inspect both implementation and tests for false positives.

---

## 11. Thread and executor acceptance

For each executor-backed coordinator, establish:

* how new claims stop;
* how the runner wakes;
* what happens to pending work;
* what happens to already-running work;
* when `shutdown(wait=True)` is permitted;
* when `wait=False, cancel_futures=True` is used;
* whether the event loop remains responsive;
* which durable state permits restart recovery;
* whether any non-daemon thread can silently outlive the asserted envelope.

Explicitly reject any proof based solely on:

```text
asyncio.wait_for
task cancellation
ThreadPoolExecutor.shutdown(wait=False)
cancel_futures=True
a stopping flag
```

Acceptance requires causal evidence for each known blocking boundary.

---

## 12. Subprocess acceptance

Independently verify:

* lifecycle-owned subprocess runners track active processes thread-safely;
* process groups are session-owned;
* interruption is idempotent;
* TERM/KILL timing consumes remaining deadline rather than a fresh fixed allowance;
* the owning execution path reaps the direct child;
* stdout/stderr reader cleanup cannot deadlock shutdown;
* expected cancellation is not logged as unexpected failure;
* private argv, URLs, paths, filenames, tokens, and raw provider output are not logged.

Review at least:

```text
media-analysis SubprocessRunner
background validation ffprobe
background automatic media analysis
YouTube downloader
X extractor
```

Ensure request-time cover, preview, suggestion, and movie-identification operations were not accidentally attached to the background lifecycle interrupt boundary.

---

## 13. X recovery acceptance

Prove the complete interrupted-X path:

1. existing stable asset identity enters `ACQUIRING`;
2. shutdown interrupts and reaps the owned process;
3. restart discovers the interrupted asset;
4. descriptor-safe staging cleanup occurs before retry;
5. partial `artifact.mp4` cannot satisfy `--no-overwrites`;
6. retry uses the same asset rather than creating a duplicate;
7. legal domain transitions remain enforced;
8. no migration or YouTube/X unification was introduced.

Adjudicate Worker 2’s residual observation:

> Durable X `cleanup_state` may remain `PENDING` after successful disk clear because same-state persistence is rejected.

Determine whether this is:

```text
safe idempotent residual state
candidate correctness defect
candidate observability defect
test gap
```

Acceptance cannot PASS if it permits stuck work, duplicate work, repeated destructive cleanup, or false completed-state projection.

---

## 14. Publication and validation recovery

Verify:

* validation interrupted while `VALIDATING` remains restart-recoverable;
* lifecycle interruption is not converted incorrectly into permanent user rejection;
* publication cannot expose partial final media;
* publication temporary files remain safely retryable;
* durable commit ordering is preserved;
* catalog creation remains idempotent;
* media-analysis `ANALYZING` reconciliation remains valid;
* YouTube `DOWNLOADING` recovery remains `DOWNLOAD_PENDING`;
* schema stays `0028`.

---

## 15. Test-quality review

Inspect new and modified tests before running them.

Reject tests that:

* merely assert implementation details without proving behavior;
* accept arbitrary early process death;
* pass while a child survives;
* use a broad timing threshold that hides deadline multiplication;
* mock away the exact subprocess/thread boundary under test;
* silently skip;
* call providers;
* depend on production data;
* accept `-SIGTERM` without proving that graceful lifespan cleanup completed;
* treat a clean process exit alone as durable recovery proof.

The SIGTERM test may accept Uvicorn 0.49’s final `-SIGTERM` only if separate evidence proves:

* lifespan shutdown completed;
* expected durable markers were written;
* the child process was reaped;
* no forced self-termination occurred;
* SQLite/staging state is recoverable.

---

## 16. Mandatory test gates

Run the exact new and changed lifecycle tests and Worker 2’s complete focused set.

At minimum include:

```text
tests/unit/application/test_in_process_lifecycle.py
tests/integration/test_process_sigterm_lifecycle.py
tests/unit/infrastructure/test_x_staging.py
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

Run the most timing/concurrency-sensitive new tests at least three times or with an equivalent deterministic repetition strategy.

If focused gates pass, run the complete non-live Python test suite from the exact candidate source. Do not enable live/provider tests.

Every mandatory test command must exit zero. A traceback, timeout, unexplained hang, surviving child, or unexpected skip prevents acceptance PASS.

Run:

```text
git diff --check 5fe07b01^ 5fe07b01
```

No candidate mutation is permitted.

---

## 17. Positive and negative acceptance controls

Positive controls:

* bounded normal shutdown;
* partial-startup rollback;
* shared deadline;
* interrupt and reap;
* durable restart;
* sanitized runner observability;
* unchanged health;
* unchanged schema;
* exact-source process SIGTERM proof.

Negative controls:

* no forced self-exit;
* no sixfold timeout multiplication;
* no event-loop-blocking X subprocess;
* no surviving owned child;
* no false executor-thread guarantee;
* no partial X artifact reuse;
* no duplicate X asset;
* no partial published media;
* no provider call;
* no systemd change;
* no schema change;
* no secret/path leakage;
* no unauthorized diff path.

---

## 18. Verdict rules

Return `acceptance-PASS` only if all material risk claims are independently proven for exact commit `5fe07b01…`.

Worker 2’s report nonconformance does not by itself require rejection of an independently proven immutable candidate.

Return `PARTIAL` if the candidate appears sound but one material acceptance claim lacks evidence.

Return `BLOCKED` if the exact candidate or required environment cannot be inspected safely.

If a candidate defect exists:

* identify exact path, behavior, reproduction, and risk;
* state the smallest correction boundary;
* do not modify anything;
* do not create a correction prompt;
* do not push or deploy.

---

## 19. Terminal report

The report must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Then include exactly once:

```text
Logical whole identity: framenest-in-process-lifecycle-runtime-contract
Worker session ordinal: 03
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: acceptance-PASS | not-applicable
Result artifact or commit: 5fe07b01bdfd587919d38a3d59ddd00e004d7394
Result evidence: <bounded exact evidence>
Logical-whole closure: not-closed
Report justification: final-acceptance | new-evidence | new-material-risk
Authority expiry: all Worker 3 authority expired at this terminal report
```

For PASS:

```text
Standard terminal status: PASS
Phase-qualified result: acceptance-PASS
Report justification: final-acceptance
```

The report must include:

1. fresh independence confirmation;
2. public-ref verification;
3. exact candidate identity;
4. exact diff and authority review;
5. Worker 2 report-compliance classification;
6. AP project-check causal classification;
7. exact-source provenance;
8. deadline-budget verdict;
9. executor/thread verdict;
10. subprocess/reaping verdict;
11. X recovery and cleanup-state verdict;
12. durable recovery verdict;
13. test-quality review;
14. commands, exit codes, pass/skip counts, and duration;
15. repeated timing-test result;
16. complete non-live Python suite result;
17. negative-control result;
18. residual risks;
19. publication recommendation or prohibition;
20. `AP empirical observations: none` or bounded non-authorizing evidence;
21. `FrameNest ledger observations: none` or bounded non-authorizing candidates;
22. `Resolved Execution Issues / Near-Misses`.

Do not expose private chain-of-thought.

Do not implement, correct, commit, push, publish, deploy, SSH, invoke sudo, contact providers, or continue after the terminal report.
