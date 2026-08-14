# Worker 4 — Fresh Bounded Correction Implementation

## Control envelope

```text
Logical whole identity: framenest-in-process-lifecycle-runtime-contract
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker role: correction implementer
Phase: bounded correction implementation
Reasoning profile requested by Cooperator: Extra High
Fresh-worker session: required
Native planning mode: not-used
Delegation: not-authorized
Maximum commits: 1
Publication authority: none
Deployment authority: none
NUC authority: none
Provider-call authority: none
Logical-whole closure authority: none
```

You are a fresh correction Worker. Treat all earlier Worker reports as evidence claims, not authority. Independently verify every Git identity and relevant source fact before mutation.

This is not publication, acceptance, deployment, NUC validation, AP development, or logical-whole closure.

## Authoritative current state

Expected public refs at handoff:

```text
cisarik/ap refs/heads/main:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

cisarik/framenest refs/heads/main:
a72be476f5634394287082be07380d03fa7ccd4d
```

Implementation candidate requiring correction:

```text
Commit:
5fe07b01bdfd587919d38a3d59ddd00e004d7394

Parent:
a72be476f5634394287082be07380d03fa7ccd4d

Tree:
980f87991e7cf1cc239f82bea3a026dd3dce1b38

Subject:
fix: bound in-process lifecycle shutdown
```

Candidate worktree used by Worker 2:

```text
/home/agile/Projects/framenest-worktrees/framenest-in-process-lifecycle-runtime-contract-w2
```

Do not modify or reuse that worktree for the correction.

Worker 3 independently classified the candidate as technically unacceptable because of one demonstrated candidate defect:

```text
tests/unit/test_import_boundaries.py::
test_application_ports_import_no_infrastructure_or_sqlalchemy
```

Causal violation:

```text
src/framenest/application/upload_validation.py

imports:

framenest.infrastructure.media_analysis.process.ProcessInterruptedError
```

The interruption intent is valid, but the application layer must not depend on infrastructure.

Worker 3’s terminal classification was:

```text
Standard terminal status: PARTIAL
Publication recommendation: prohibited
Candidate defect count demonstrated: 1
```

The original Worker 2 result remains Orchestrator-classified as `implementation-PARTIAL`, because it reported PASS despite a mandatory non-zero AP command. Do not repeat or repair that reporting defect. Your task is solely the source-layering correction.

## Required reading

Before mutation, read only what is necessary:

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
3. `/home/agile/Projects/ap/AP.md` at the expected AP generation
4. Candidate versions of:

```text
src/framenest/application/ports/upload_media_validation.py
src/framenest/application/upload_validation.py
src/framenest/infrastructure/media_validation/ffprobe.py
tests/unit/test_import_boundaries.py
```

5. Existing upload-validation, ffprobe/media-validation, and lifecycle tests selected below.

Meta history is not required for this correction. Do not read the whole `cisarik/meta` repository. No Meta commit has been identified as necessary evidence for this narrow defect.

Do not inspect `.env`, credentials, private media, provider data, or unrelated owner artifacts.

## Mission

Produce one minimal child commit of `5fe07b01…` that restores the application/infrastructure dependency boundary while preserving the candidate’s graceful interruption semantics.

The required direction is:

```text
application/upload_validation.py
        |
        v
application/ports/upload_media_validation.py
        ^
        |
infrastructure/media_validation/ffprobe.py
```

Infrastructure may depend on an application port. Application must not depend on infrastructure.

## Required correction semantics

Implement the smallest coherent correction:

1. Define a narrowly named interruption exception owned by:

```text
src/framenest/application/ports/upload_media_validation.py
```

Use naming consistent with the existing port and codebase. The type must represent interruption of media validation, not a generic infrastructure/process failure.

2. In:

```text
src/framenest/infrastructure/media_validation/ffprobe.py
```

catch the infrastructure-owned `ProcessInterruptedError` at the adapter boundary and translate it to the new port-owned interruption exception.

Preserve causal chaining with `raise ... from exc` unless existing repository conventions provide a stronger reason not to.

3. In:

```text
src/framenest/application/upload_validation.py
```

remove the infrastructure import completely, import only the port-owned interruption exception, and catch that narrow port exception.

4. Preserve the current externally observable behavior:

* lifecycle interruption must not become ordinary user rejection;
* lifecycle interruption must not become `UPLOAD_VALIDATION_INTERNAL_ERROR`;
* lifecycle interruption must remain distinguishable from invalid or unavailable media;
* no error detail, process command, path, or private payload may leak;
* ordinary ffprobe validation failures must retain their existing mapping;
* no broad `BaseException` or new broad `Exception` interception;
* no forced process termination;
* no schema, API, identity, authorization, UI, provider, or deployment change.

Do not redesign the validator port or lifecycle system. Do not change X, YouTube, publication, coordinator, executor, systemd, or SIGTERM behavior.

## Exact mutation allowlist

Only these production paths may be modified:

```text
src/framenest/application/ports/upload_media_validation.py
src/framenest/application/upload_validation.py
src/framenest/infrastructure/media_validation/ffprobe.py
```

Test mutation is not authorized. Existing tests must prove the correction.

No other path may change, including:

```text
.ap
ap.project.conf
pyproject.toml
poetry.lock
uv.lock
alembic/
deploy/
docs/
tests/
```

If a correct solution genuinely requires a path outside the allowlist, stop without that mutation and report `BLOCKED` with the exact reason.

## Git and worktree authority

Create exactly one new isolated worktree:

```text
/home/agile/Projects/framenest-worktrees/framenest-in-process-lifecycle-runtime-contract-w4
```

Create exactly one new branch:

```text
fix/in-process-lifecycle-upload-validation-boundary
```

Its initial HEAD must be exactly:

```text
5fe07b01bdfd587919d38a3d59ddd00e004d7394
```

Do not amend, rebase, cherry-pick, merge, reset, force, push, publish, deploy, or mutate public refs.

Do not modify the canonical owner worktree:

```text
/home/agile/Projects/framenest
```

Preserve all existing owner branches, untracked files, and worktrees.

If the requested branch or worktree path already exists, do not delete or overwrite it. Stop and report the collision.

Do not initialize the isolated `.ap` checkout. Do not create, copy, link, rebuild, or repair `.venv`.

## Start gates

Before creating the correction worktree:

1. Run credential-free `git ls-remote` for AP and FrameNest public `main`.
2. Require the exact expected public refs above.
3. Verify the candidate commit, parent, tree, subject, and `.ap` gitlink.
4. Verify that the candidate object is locally available.
5. Verify the Worker 2 candidate worktree is clean.
6. Record the canonical owner worktree branch, HEAD, and porcelain state without modifying it.
7. Verify the new Worker 4 worktree path and branch do not already exist.

If a public ref differs from the expected value, report `BLOCKED` before mutation. Do not silently rebase the local candidate onto a newer public main.

After worktree creation, verify:

```text
HEAD = 5fe07b01bdfd587919d38a3d59ddd00e004d7394
branch = fix/in-process-lifecycle-upload-validation-boundary
upstream = none
status = clean
```

## Runtime provenance

Use only the canonical FrameNest interpreter:

```text
/home/agile/Projects/framenest/.venv/bin/python
```

Execute the Worker 4 worktree source explicitly:

```bash
CORRECTION_ROOT=/home/agile/Projects/framenest-worktrees/framenest-in-process-lifecycle-runtime-contract-w4
FRAMENEST_PY=/home/agile/Projects/framenest/.venv/bin/python

env -u LD_LIBRARY_PATH \
  PYTHONPATH="$CORRECTION_ROOT/src" \
  PYTHONDONTWRITEBYTECODE=1 \
  "$FRAMENEST_PY" -c \
  'import framenest, sys; print(framenest.__file__); print(sys.executable)'
```

Require:

* `framenest.__file__` under the Worker 4 worktree;
* `sys.executable` equal to the canonical `.venv` interpreter;
* exit code 0.

Do not use system Python. Do not invoke Poetry to alter an environment.

The previously demonstrated isolated-worktree `ap project check` failure is an accepted environment observation for this exchange: the relative `.venv/bin/python` declared by `ap.project.conf` does not exist inside an isolated worktree. Do not reconstruct the environment and do not knowingly rerun a command that will fail for that unchanged topology. Direct exact-source gates below are mandatory.

## Mandatory validation

Run all commands from the Worker 4 worktree with:

```text
PYTHONPATH=<Worker 4 worktree>/src
PYTHONDONTWRITEBYTECODE=1
LD_LIBRARY_PATH unset
pytest cache provider disabled
canonical FrameNest .venv interpreter
```

### Gate A — import boundary

Run:

```text
tests/unit/test_import_boundaries.py
```

It must exit 0.

Also perform a static negative check proving that:

```text
src/framenest/application/upload_validation.py
```

contains no import from `framenest.infrastructure`.

Implement the negative check so that “no match” is the expected successful result, not an unexplained failed command.

### Gate B — complete candidate regression set

Build the exact Python test-file set changed between:

```text
a72be476f5634394287082be07380d03fa7ccd4d
5fe07b01bdfd587919d38a3d59ddd00e004d7394
```

under `tests/`, using Git’s tracked diff. Run every changed Python test file, plus:

```text
tests/unit/test_import_boundaries.py
```

Record the fully expanded file list in the report. Do not report only the shell expression.

The complete Gate B pytest invocation must exit 0 with no unexpected skip, traceback, hang, or leaked child process.

### Gate C — focused interruption semantics

Using the existing test files discovered through `rg --files tests`, run all existing tests whose files cover:

* upload validation;
* ffprobe/media validation;
* media-analysis process interruption;
* upload-validation lifecycle shutdown.

Record the exact expanded paths and command. Every selected test must exit 0.

Do not mutate tests to make the implementation pass.

### Gate D — source and diff integrity

Require all of the following:

* `git diff --check` exits 0;
* only the three allowlisted production paths changed;
* `.ap` gitlink remains `041de310…`;
* schema head remains `0028`;
* no dependency or lockfile change;
* systemd unit remains byte-identical to the parent;
* no credentials, `.env` content, private media names, or local owner artifacts in the diff;
* no application-layer import from infrastructure introduced anywhere by this correction;
* no tests changed;
* worktree clean after the final commit.

Do not run the known-topology-failing entire `pytest tests` command in this correction worktree. Worker 3 already used that diagnostic to isolate the sole candidate failure. This exchange instead has an exact mandatory regression set whose every executed command must terminate successfully.

## Commit authority

Only after all pre-commit mandatory gates pass, create one commit with subject:

```text
fix: restore upload validation layer boundary
```

The correction commit must have:

```text
parent = 5fe07b01bdfd587919d38a3d59ddd00e004d7394
```

After committing, rerun Gates A, B, C, and D against the committed tree.

If any mandatory post-commit gate is non-zero, hangs, produces a traceback, or reveals an unauthorized mutation, do not report PASS.

Do not create an additional repair commit. Report the exact terminal condition for Orchestrator routing.

## PASS standard

You may report `correction-PASS` only if:

* the correction commit is exactly one child of `5fe07b01…`;
* only the three allowlisted production files changed;
* the application import boundary is restored;
* interruption semantics remain correct;
* every executed mandatory test command exits 0;
* the committed worktree is clean;
* no push, deployment, NUC access, provider call, AP mutation, or Meta mutation occurred.

A correction PASS is not independent acceptance, publication approval, deployment approval, production acceptance, or logical-whole closure.

After a correction PASS, Orchestrator will route the new exact commit to a fresh independent acceptance Worker.

## Terminal report contract

Begin exactly with:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Then provide:

```text
Logical whole identity: framenest-in-process-lifecycle-runtime-contract
Worker session ordinal: 04
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED | FAIL
Phase-qualified result: correction-PASS | not-applicable
Result artifact or commit: <new SHA or not-applicable>
Result evidence: <compact exact evidence>
Logical-whole closure: not-closed
Report justification: correction-mutation | blocker | failure
Authority expiry: all Worker 4 authority expired at this terminal report
```

The report must include:

1. fresh-session and no-delegation confirmation;
2. native planning mode value;
3. public-ref readback;
4. original candidate identity;
5. new worktree and branch identity;
6. exact changed paths and purpose;
7. explanation of the final dependency direction;
8. old and new exception-mapping flow;
9. proof that application no longer imports infrastructure;
10. exact interpreter and source provenance;
11. every exact test command, exit code, count, duration, and expanded file list;
12. diff and allowlist evidence;
13. new commit SHA, parent, tree, subject, and file modes;
14. `.ap` gitlink and schema head;
15. worktree cleanliness;
16. push/publication/deployment/NUC/provider status;
17. remaining risks, if any;
18. AP empirical observations, explicitly non-authorizing;
19. FrameNest ledger observations, if concrete;
20. resolved execution issues and near-misses.

Terminate after the report. Do not continue into acceptance, publication, deployment, or another correction.
