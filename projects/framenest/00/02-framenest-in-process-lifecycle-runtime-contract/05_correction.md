# Worker 5 — Upload-Validation Boundary Correction

## Execution envelope

```text
Logical whole identity: framenest-in-process-lifecycle-runtime-contract
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker role: bounded correction implementer
Phase: correction implementation
Reasoning profile requested by Cooperator: Extra High
Fresh-worker session: required
Native planning mode: not-used
Delegation: not-authorized
Maximum commits: 1
Publication authority: none
Deployment authority: none
NUC authority: none
Provider-call authority: none
AP or Meta mutation authority: none
Logical-whole closure authority: none
```

This is a fresh correction session. Do not inherit mutation authority from Workers 2–4.

## Authoritative state

Expected public refs:

```text
cisarik/ap refs/heads/main:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

cisarik/framenest refs/heads/main:
a72be476f5634394287082be07380d03fa7ccd4d
```

Candidate requiring correction:

```text
commit:  5fe07b01bdfd587919d38a3d59ddd00e004d7394
parent:  a72be476f5634394287082be07380d03fa7ccd4d
tree:    980f87991e7cf1cc239f82bea3a026dd3dce1b38
subject: fix: bound in-process lifecycle shutdown
```

Worker 3 independently demonstrated one candidate defect:

```text
src/framenest/application/upload_validation.py
imports an infrastructure-owned ProcessInterruptedError
```

This violates:

```text
tests/unit/test_import_boundaries.py::
test_application_ports_import_no_infrastructure_or_sqlalchemy
```

Worker 4 demonstrated the correct production direction, but correctly stopped without a commit because its mutation allowlist excluded an existing candidate-authored ffprobe test that asserts the old leaked infrastructure exception.

Worker 4 created no commit. Its dirty worktree is evidence only:

```text
/home/agile/Projects/framenest-worktrees/framenest-in-process-lifecycle-runtime-contract-w4
```

Do not modify, clean, reset, commit, or reuse that worktree. Independently implement the correction in a new worktree.

## Required reading

Read only the relevant current contracts and exact candidate files:

```text
/home/agile/Projects/framenest/AGENTS.md
/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md
/home/agile/Projects/ap/AP.md

src/framenest/application/ports/upload_media_validation.py
src/framenest/application/upload_validation.py
src/framenest/infrastructure/media_validation/ffprobe.py
tests/unit/infrastructure/media_validation/test_ffprobe.py
tests/unit/application/test_upload_validation.py
tests/unit/test_import_boundaries.py
```

Do not read the whole Meta archive. No Meta evidence is necessary for this bounded correction.

## Git and worktree boundary

Create exactly one new isolated worktree:

```text
/home/agile/Projects/framenest-worktrees/framenest-in-process-lifecycle-runtime-contract-w5
```

Create exactly one new branch:

```text
fix/in-process-lifecycle-upload-validation-port-boundary
```

Its initial HEAD must be exactly:

```text
5fe07b01bdfd587919d38a3d59ddd00e004d7394
```

Before mutation:

1. Verify both public refs with credential-free `git ls-remote`.
2. Verify the candidate commit, parent, tree, subject, and `.ap` gitlink.
3. Verify the new worktree and branch do not already exist.
4. Record the canonical owner worktree state without modifying it.
5. Confirm the new worktree starts clean, has no upstream, and points to the exact candidate.

If either public ref differs, or the new identities collide, stop as `BLOCKED`. Do not delete, reset, rebase, or overwrite anything.

Do not initialize `.ap` inside the isolated worktree. Do not create, link, copy, repair, or rebuild `.venv`.

## Required correction

Establish this dependency direction:

```text
application/upload_validation.py
        |
        v
application/ports/upload_media_validation.py
        ^
        |
infrastructure/media_validation/ffprobe.py
```

Implement the smallest coherent correction:

1. Add a narrowly scoped application-port exception in:

```text
src/framenest/application/ports/upload_media_validation.py
```

Preferred name, if consistent with the existing code:

```text
UploadMediaValidationInterruptedError
```

2. In:

```text
src/framenest/infrastructure/media_validation/ffprobe.py
```

translate infrastructure-owned `ProcessInterruptedError` into the port-owned interruption exception at the adapter boundary.

Preserve exception causality with:

```python
raise UploadMediaValidationInterruptedError() from exc
```

where the original infrastructure exception is directly caught.

If an already-sanitized process result represents interruption, expose the same port exception without leaking process details.

3. In:

```text
src/framenest/application/upload_validation.py
```

remove the infrastructure import and catch only the port-owned interruption exception. Continue mapping it to the existing application-level `UploadValidationInterruptedError`.

4. Update:

```text
tests/unit/infrastructure/media_validation/test_ffprobe.py
```

so the ffprobe adapter contract expects the port-owned exception rather than `ProcessInterruptedError`.

The test must continue proving that interruption is recoverable and is not classified as invalid media or ordinary content failure.

Where applicable, prove causal translation without making the caller depend on the infrastructure exception as its public result.

Do not create a multiple-inheritance compatibility exception. The port exception must not subclass `ProcessInterruptedError`, and the adapter must not continue leaking an instance of the infrastructure exception merely to satisfy the old assertion.

## Required semantics

Preserve all of these invariants:

* interrupted validation is not ordinary user rejection;
* interruption does not become `UPLOAD_VALIDATION_INTERNAL_ERROR`;
* interruption remains distinguishable from invalid or unavailable media;
* normal ffprobe/content failures retain their existing mappings;
* no command, stderr, filesystem path, or private payload leaks;
* no new broad `Exception` or `BaseException` handling;
* no lifecycle, coordinator, X, YouTube, publication, schema, API, UI, identity, provider, dependency, systemd, or deployment change.

Do not redesign the port.

## Exact mutation allowlist

Only these four paths may change:

```text
src/framenest/application/ports/upload_media_validation.py
src/framenest/application/upload_validation.py
src/framenest/infrastructure/media_validation/ffprobe.py
tests/unit/infrastructure/media_validation/test_ffprobe.py
```

No other production or test file may change.

If another path is genuinely necessary, stop as `BLOCKED` and report why.

## Runtime provenance

Use only:

```text
/home/agile/Projects/framenest/.venv/bin/python
```

Execute the Worker 5 source explicitly:

```bash
CORRECTION_ROOT=/home/agile/Projects/framenest-worktrees/framenest-in-process-lifecycle-runtime-contract-w5
FRAMENEST_PY=/home/agile/Projects/framenest/.venv/bin/python

env -u LD_LIBRARY_PATH \
  PYTHONPATH="$CORRECTION_ROOT/src" \
  PYTHONDONTWRITEBYTECODE=1 \
  "$FRAMENEST_PY" -c \
  'import framenest, sys; print(framenest.__file__); print(sys.executable)'
```

Require candidate source under the Worker 5 worktree and the canonical interpreter.

Do not rerun the known isolated-worktree `ap project check` failure. The missing relative `.venv/bin/python` has already been classified as an isolated-worktree environment limitation. Do not reconstruct that environment.

All pytest commands must use:

```text
LD_LIBRARY_PATH unset
PYTHONPATH=<Worker 5 worktree>/src
PYTHONDONTWRITEBYTECODE=1
canonical FrameNest interpreter
-p no:cacheprovider
```

## Mandatory pre-commit gates

### Gate A — original failing vertical

Run exactly the existing ffprobe interruption test:

```text
tests/unit/infrastructure/media_validation/test_ffprobe.py::
test_ffprobe_interruption_is_recoverable_and_not_a_content_failure
```

Then run the complete file:

```text
tests/unit/infrastructure/media_validation/test_ffprobe.py
```

Both must exit 0.

### Gate B — architectural boundary

Run:

```text
tests/unit/test_import_boundaries.py
```

Expected result: all tests pass.

Perform a static negative check proving no import from `framenest.infrastructure` exists in:

```text
src/framenest/application/upload_validation.py
```

Also verify no application-layer file changed by this correction imports infrastructure.

“No match” must be handled as an expected successful negative result.

### Gate C — Worker 4 regression set

Run this exact expanded set:

```text
tests/contract/test_health_api.py
tests/contract/test_server_process_output.py
tests/integration/test_atomic_upload_publication.py
tests/integration/test_process_sigterm_lifecycle.py
tests/unit/application/test_in_process_lifecycle.py
tests/unit/application/test_media_analysis_coordinator.py
tests/unit/application/test_upload_catalog_coordinator.py
tests/unit/application/test_upload_publication_coordinator.py
tests/unit/application/test_upload_validation_coordinator.py
tests/unit/application/test_upload_validation.py
tests/unit/application/test_x_acquisition_lifecycle.py
tests/unit/infrastructure/filesystem/test_published_media_storage.py
tests/unit/infrastructure/media_analysis/test_process.py
tests/unit/infrastructure/media_validation/test_ffprobe.py
tests/unit/infrastructure/test_x_downloader_adapter.py
tests/unit/infrastructure/test_x_staging.py
tests/unit/infrastructure/youtube/test_downloader.py
tests/unit/test_server_runtime.py
tests/unit/test_import_boundaries.py
```

The expected collection is approximately 278 passing tests with only the two already observed Pydantic schema warnings. Any different count or unexpected skip must be investigated and explained.

### Gate D — focused interruption semantics

Run:

```text
tests/unit/application/test_upload_validation.py
tests/unit/application/test_upload_validation_coordinator.py
tests/unit/infrastructure/media_validation/test_ffprobe.py
tests/unit/infrastructure/media_analysis/test_ffprobe_ffmpeg.py
tests/unit/infrastructure/media_analysis/test_process.py
tests/unit/application/test_in_process_lifecycle.py
tests/integration/test_process_sigterm_lifecycle.py
```

Expected collection is approximately 148 passing tests. No unexpected skip, hang, traceback, or leaked child process is acceptable.

### Gate E — integrity

Require:

* `git diff --check` exits 0;
* exactly the four allowlisted paths changed;
* the test change reflects the new public adapter contract and does not weaken the assertion;
* no test-only production hook;
* `.ap` gitlink remains `041de310…`;
* schema remains `0028`;
* systemd unit is byte-identical to `5fe07b01…`;
* no lockfile, dependency, migration, documentation, credential, `.env`, private-media, or owner-artifact change.

Do not run the entire isolated-worktree suite. Worker 3 already classified its unrelated `.ap`, `.venv`, and console-script topology failures.

## Commit authority

Only after every pre-commit gate passes, create exactly one commit:

```text
fix: restore upload validation layer boundary
```

Required parent:

```text
5fe07b01bdfd587919d38a3d59ddd00e004d7394
```

After committing, rerun Gates A–E against the committed tree.

If a mandatory command is non-zero, hangs, or exposes an unauthorized mutation, do not report PASS and do not create a second commit.

No amend, merge, rebase, cherry-pick, force operation, push, publication, deployment, NUC access, or provider call is authorized.

## PASS standard

Report `correction-PASS` only if:

* one child commit of `5fe07b01…` exists;
* exactly the four authorized paths changed;
* the application/infrastructure boundary is restored;
* the adapter exposes the port-owned interruption contract;
* the application preserves graceful interruption semantics;
* the updated test remains semantically strong;
* every mandatory pre- and post-commit command exits 0;
* the committed worktree is clean.

Correction PASS is not independent acceptance, publication, deployment, production acceptance, or logical-whole closure.

## Terminal report

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Then provide:

```text
Logical whole identity: framenest-in-process-lifecycle-runtime-contract
Worker session ordinal: 05
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED | FAIL
Phase-qualified result: correction-PASS | not-applicable
Result artifact or commit: <new SHA or not-applicable>
Result evidence: <compact exact evidence>
Logical-whole closure: not-closed
Report justification: correction-mutation | blocker | failure
Authority expiry: all Worker 5 authority expired at this terminal report
```

Include:

1. fresh-session, no-delegation, and native-mode confirmation;
2. public-ref verification;
3. original candidate identity;
4. new worktree and branch identity;
5. exact four-path diff and purpose;
6. dependency direction and exception-flow explanation;
7. proof that the updated test validates the port contract without compatibility inheritance;
8. interpreter and exact-source provenance;
9. every exact test command, exit code, count, duration, and warnings;
10. pre- and post-commit gate results;
11. commit SHA, parent, tree, subject, and modes;
12. `.ap` gitlink and schema;
13. worktree cleanliness;
14. push, publication, deployment, NUC, and provider status;
15. residual risks;
16. AP empirical observations, explicitly non-authorizing;
17. FrameNest ledger observations, if concrete;
18. resolved execution issues and near-misses.

Terminate after the report. Do not continue into acceptance or publication.
