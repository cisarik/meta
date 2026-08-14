# FrameNest Portable Media Sidecar — Thin Operator CLI and Public Contract Convergence

## Authority coordinates

```text
Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 02
Worker exchange ordinal: 03
Worker session target: current-worker-session
Worker session profile: implementation-continuation
Worker phase: implementation
Native planning mode: not-used
Maximum plan-only cycles: 0
Reasoning recommendation: high
Evidence posture: non-independent
Authority renewal: explicit for this exchange only
```

This is the final planned implementation exchange for Worker 2.

Previous authority expired at the exchange-02 report. Retained context is useful but not authority. This prompt grants one bounded continuation only.

Do not perform independent acceptance, publication, deployment, production mutation, or logical-whole closure.

## Accepted local stack

Contained clone:

```text
/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w2-e01
```

Expected branch:

```text
feat/portable-media-sidecar-roundtrip-foundation
```

Current candidate:

```text
HEAD:    633fa3b3884bc865dba26643034ef0c2fc12f394
tree:    ab04ff1b4448745625ceb97b5b904ed84746f0de
parent:  96bf7df2001c38284d9aa136b56d0109f24700d5
subject: feat: add portable media sidecar storage
```

Earlier candidate:

```text
96bf7df2001c38284d9aa136b56d0109f24700d5
tree 6febf4e683adb61024757e89dce7725a3e890a64
parent a23b4bc786357da3591a4f75087b7e8a3d50d341
subject feat: add portable media sidecar codec
```

Public baseline:

```text
a23b4bc786357da3591a4f75087b7e8a3d50d341
```

Required AP gitlink and submodule HEAD:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

## Mandatory renewed repository gate

Before substantive analysis or mutation, verify:

1. Exact `pwd -P`.
2. Exact origin repository.
3. Expected branch.
4. Exact HEAD, tree, parent, subject and ancestry above.
5. Public `main` remains exactly `a23b4bc…` via credential-free `git ls-remote`.
6. `.ap` gitlink and checked-out submodule match `041de310…`.
7. Tracked worktree, index and untracked state are clean.
8. No merge, rebase, cherry-pick, revert or bisect is active.
9. Feature branch has no upstream and no public feature ref.
10. The cumulative diff from public baseline contains exactly the existing ten paths:

```text
A docs/adr/0059-portable-media-sidecar-roundtrip-foundation.md
M docs/adr/README.md
A src/framenest/domain/media_sidecar.py
A src/framenest/application/ports/media_sidecar_store.py
A src/framenest/application/media_sidecar.py
A src/framenest/infrastructure/filesystem/media_sidecar.py
A tests/unit/domain/test_media_sidecar.py
A tests/unit/application/test_media_sidecar.py
A tests/unit/infrastructure/filesystem/test_media_sidecar_store.py
A tests/integration/test_media_sidecar_roundtrip.py
```

Read applicable repository instructions, the pinned AP protocol, ADR-0059 and `docs/WORKER_EXECUTION_CONTRACT.md` from this contained clone.

Re-run the committed focused stack before mutation:

```text
tests/unit/domain/test_media_sidecar.py
tests/unit/application/test_media_sidecar.py
tests/unit/infrastructure/filesystem/test_media_sidecar_store.py
tests/integration/test_media_sidecar_roundtrip.py
```

Expected prior evidence is 58 passing tests. A changed count is acceptable only if fully explained; any actual failure blocks mutation.

If any mandatory invariant fails, stop without mutation and report only the exact blocker and smallest safe continuation.

## Canonical execution envelope

Use the canonical interpreter only:

```text
/home/agile/Projects/framenest/.venv/bin/python
```

Run Python commands through a sanitized environment equivalent to:

```text
env -i \
  PATH=/usr/bin:/bin \
  LC_ALL=C \
  LANG=C \
  PYTHONNOUSERSITE=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH=<contained-clone>/src
```

Prove imports resolve from the contained clone.

Do not create, repair, replace, synchronize or install into a virtual environment. Do not run Poetry environment creation, dependency installation, lock regeneration or equivalent commands.

## Objective

Complete one coherent operator-facing implementation slice:

> Add the dedicated `framenest-sidecar` command as a thin adapter over the existing sidecar application service and filesystem store, then reconcile public documentation with the truthful implemented v1 projection boundary.

The command exposes:

```text
framenest-sidecar export --media-id <UUID> --location-id <UUID>
framenest-sidecar validate --path <PATH>
framenest-sidecar compare --media-id <UUID> --location-id <UUID>
```

No HTTP surface and no metadata Save coupling.

## Expected changed-path boundary

Expected new paths:

```text
src/framenest/adapters/cli/sidecar.py
tests/contract/test_sidecar_cli.py
```

Expected edited paths:

```text
pyproject.toml
README.md
PRODUCT.md
SPEC.md
ROADMAP.md
SECURITY.md
```

`tests/integration/test_media_sidecar_roundtrip.py` may be extended only when necessary to prove real CLI composition against a synthetic SQLite catalog.

Do not edit the existing codec, application service, port, filesystem store or ADR merely for cleanup.

If a new test proves a narrow lower-layer defect that prevents a truthful thin CLI:

* retain authentic red evidence;
* repair only the smallest defect consistent with the frozen contract;
* report the extra changed path and justification explicitly.

If composition requires a semantic redesign or expanded authority, stop `BLOCKED`.

## CLI composition

Add this console entry:

```toml
framenest-sidecar = "framenest.adapters.cli.sidecar:main"
```

Do not modify `poetry.lock`; adding a console-script mapping does not add a dependency.

For catalog-dependent operations, compose only existing owners:

* `load_settings`
* `inspect_database_migration_status`
* `create_sqlite_engine`
* `SqliteMediaRepository`
* `SqliteLibraryRepository`
* `SqliteMediaMetadataRepository`
* `FilesystemMediaSidecarStore`
* `MediaSidecarService`
* `dispose_engine`

Do not duplicate catalog projection, comparison, codec or filesystem safety logic inside the CLI.

`export` and `compare` require the catalog at migration head.

`validate --path` is catalog-independent:

* it must not require a usable database;
* it must not instantiate catalog repositories;
* it must not require migration readiness;
* it must use the existing safe validation boundary;
* it must not print the decoded sidecar contents.

The command must be non-interactive. Do not add `--yes`, prompts, implicit location selection, fan-out or inferred IDs.

## Argument contract

### Export

```text
framenest-sidecar export \
  --media-id <canonical UUID> \
  --location-id <canonical UUID>
```

Both arguments are required.

### Validate

```text
framenest-sidecar validate --path <sidecar path>
```

`--path` is required. Preserve the existing validation and inode-safety semantics; the CLI must not weaken them.

### Compare

```text
framenest-sidecar compare \
  --media-id <canonical UUID> \
  --location-id <canonical UUID>
```

Both arguments are required.

Missing commands, missing values, malformed identities, unexpected positional arguments and unknown options are invalid input.

## Machine-readable success contract

Every successful command emits exactly one JSON object plus one trailing newline to stdout. Stderr remains empty.

Use deterministic serialization. Do not emit human prose, absolute paths, catalog paths, library roots or sidecar contents.

### Export

```json
{
  "operation": "export",
  "result": "created",
  "result_code": "SIDECAR_EXPORT_CREATED"
}
```

Allowed pairs:

| `result`    | `result_code`              |
| ----------- | -------------------------- |
| `created`   | `SIDECAR_EXPORT_CREATED`   |
| `replaced`  | `SIDECAR_EXPORT_REPLACED`  |
| `unchanged` | `SIDECAR_EXPORT_UNCHANGED` |

Exit status: `0`.

### Validate

```json
{
  "operation": "validate",
  "result": "valid",
  "result_code": "SIDECAR_VALIDATE_VALID"
}
```

Exit status: `0`.

Do not return the decoded document.

### Compare

Allowed pairs:

| `result`   | `result_code`              |
| ---------- | -------------------------- |
| `match`    | `SIDECAR_COMPARE_MATCH`    |
| `stale`    | `SIDECAR_COMPARE_STALE`    |
| `mismatch` | `SIDECAR_COMPARE_MISMATCH` |
| `missing`  | `SIDECAR_COMPARE_MISSING`  |

All four are completed observations and return exit status `0`.

`missing` is not an error.

## Machine-readable error contract

All errors return exit status `1`, including invalid input.

On error:

* stdout must be empty;
* stderr must contain exactly one JSON object plus one trailing newline;
* no traceback or raw exception text may escape.

Shape:

```json
{
  "operation": "export",
  "error_code": "SIDECAR_UNAVAILABLE",
  "message": "Media sidecar operation is unavailable."
}
```

Use:

```text
SIDECAR_INVALID_INPUT
```

for parser, identity and command-shape failures, with a stable sanitized message such as:

```text
Invalid sidecar command.
```

Use:

```text
SIDECAR_CATALOG_NOT_READY
```

when `export` or `compare` cannot run because the database is not at migration head.

Preserve existing structured sidecar error codes whenever available, including:

```text
SIDECAR_NOT_FOUND
SIDECAR_UNAVAILABLE
SIDECAR_INCONSISTENT
SIDECAR_LOCATION_NOT_WRITABLE
SIDECAR_UNSAFE_TARGET
SIDECAR_MALFORMED
SIDECAR_UNSUPPORTED
SIDECAR_IDENTITY_CONFLICT
```

Use a single sanitized fallback:

```text
SIDECAR_COMMAND_FAILED
```

only for an unexpected failure.

Never include:

* absolute paths;
* database paths;
* library roots;
* sidecar payload fragments;
* private acquisition data;
* raw SQLAlchemy or OS exceptions;
* tracebacks.

If parsing fails before an operation is known, report a stable neutral operation value such as `unknown`.

## Frozen product semantics

Do not change these accepted rules:

* SQLite/catalog state is authoritative during normal operation.
* Sidecars are explicit portable projections, not a live catalog write authority.
* `export` handles exactly one explicit location.
* `validate` performs schema and codec validation only.
* `compare` is read-only and never repairs drift.
* Sidecars never overwrite the catalog.
* Ordinary metadata Save never writes sidecars.
* Missing sidecars do not invalidate catalog state.
* No import or rebuild exists.
* No multi-copy fan-out exists.
* No HTTP or browser surface exists.
* No application deployment is part of this logical whole.

## Public documentation convergence

Update documentation narrowly and truthfully.

### README.md

Add concise operator examples for the three commands and explain:

* required explicit identities;
* adjacent `{media_filename}.framenest.json` placement;
* JSON stdout and exit behavior;
* catalog authority;
* no import, rebuild, Save coupling or fan-out;
* `FRAMENEST_DATABASE_PATH` follows the existing settings boundary for catalog operations.

Do not imply production deployment.

### PRODUCT.md

Record the product value now delivered:

* selected catalog metadata can travel beside one chosen media copy;
* the artifact is deterministic and versioned;
* it remains a projection, not bidirectional synchronization.

### SPEC.md

Resolve only statements made obsolete by ADR-0059 and this implementation:

* v1 explicit projection schema now exists;
* export, validate and compare exist;
* sidecar-to-catalog import, rebuild, synchronization, drift repair and conflict resolution remain unresolved or unimplemented;
* SQLite remains authoritative in normal operation.

Do not claim the entire durable-metadata or synchronization roadmap is complete.

### ROADMAP.md

Mark only the bounded v1 contract/projection foundation as implemented or started. Preserve later work:

* import/rebuild;
* drift repair;
* automatic Save projection;
* multi-location fan-out;
* directory naming;
* native OS tags;
* cross-device synchronization.

### SECURITY.md

Document:

* strict closed schema;
* no secrets, absolute roots, device IDs or requester-private state;
* bounded 256 KiB reads;
* non-following symlink and special-file refusal;
* same-directory atomic replacement;
* foreign-identity refusal;
* catalog remains unchanged on failures;
* known Windows replace/case-folding evidence remains incomplete.

Do not add deployment or NUC instructions.

## Test-first requirements

Write focused CLI contract tests before the CLI implementation and retain authentic red evidence. The expected initial red may be a collection-time missing-module or missing-entry-point failure. Do not manufacture red by deleting completed code afterward.

At minimum prove:

### Parsing and routing

* each exact command shape;
* missing command;
* missing required arguments;
* malformed UUIDs;
* unknown arguments;
* no interactive input;
* exit `1` for invalid input.

### Success JSON

* exact export result/code pairs;
* exact validate result/code;
* exact four compare result/code pairs;
* exactly one JSON line;
* stdout-only success;
* no path or document leakage.

### Error JSON

* application/store error codes are preserved;
* invalid input and catalog-not-ready mappings;
* unexpected sanitized fallback;
* stdout empty;
* stderr contains exactly one JSON object;
* no traceback, absolute path or private marker.

### Composition

* `export` and `compare` use real current repositories and dispose the engine;
* `validate` does not load or require the catalog;
* a valid sidecar can be validated when the configured database is absent or not ready;
* console-script registration points to the new `main`;
* no repository write path is introduced.

### End-to-end synthetic evidence

Using a temporary SQLite catalog and synthetic library:

```text
CLI export
→ created
→ CLI validate
→ valid
→ CLI compare
→ match
→ second CLI export
→ unchanged
```

Then alter only appropriate synthetic catalog metadata and prove the existing compare semantics through the CLI without repairing either side.

Do not use private media, NUC, production or the owner checkout.

## Validation route

Run through the sanitized exact-source envelope:

1. Pre-mutation committed 58-test sidecar stack.
2. New CLI contract tests.
3. Updated sidecar integration test if changed.
4. Full sidecar-focused domain/application/filesystem/contract/integration stack.
5. Relevant existing CLI contract tests to detect shared convention regressions.
6. Persistence migration invariant forbidding a sidecar table.
7. Documentation contradiction searches.
8. `compileall` for changed Python packages.
9. `git diff --check`.

Use repository-native test helpers where they exist. Do not rewrite the harness merely to obtain green output.

Report exact commands, exit statuses and test counts.

## Commit boundary

Create exactly one new local commit on top of:

```text
633fa3b3884bc865dba26643034ef0c2fc12f394
```

Recommended subject:

```text
feat: add portable media sidecar CLI
```

Do not amend, rebase, merge, squash, tag or push.

At completion prove:

* new commit SHA and tree;
* parent is exactly `633fa3b…`;
* exact subject;
* exact changed paths and purposes;
* cumulative ancestry to public baseline;
* tracked/index/untracked state clean;
* no active Git operation;
* feature branch remains unpublished;
* credential-free public `main` remains `a23b4bc…`.

## Explicit exclusions

Do not implement:

* HTTP or browser sidecar APIs;
* metadata Save hooks;
* sidecar import or catalog rebuild;
* automatic drift repair;
* multi-location export;
* background synchronization;
* physical media rename;
* directory naming;
* native OS tags;
* covers;
* backup integration;
* deployment or NUC changes;
* migration or sidecar table;
* new dependency;
* AP or Meta changes.

Do not inspect or mutate the owner checkout except using its canonical `.venv` interpreter exactly as already authorized.

No SSH, sudo, provider, browser, production or private-media activity.

## Terminal report

Return exactly one report beginning:

```text
### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 02
Worker exchange ordinal: 03
```

On success:

```text
Standard terminal status: PASS
Phase-qualified result: implementation-PASS
Result artifact or commit: <new-local-commit>
Logical-whole closure: not-closed
Report justification: new-mutation
```

Otherwise return a truthful `BLOCKED` or `FAIL`.

Include:

* renewed gate evidence;
* authentic retained red evidence;
* thin-adapter composition proof;
* exact CLI commands and JSON/exit contract;
* documentation convergence summary;
* exact test commands, exits and counts;
* exact changed paths;
* commit/tree/parent/subject;
* public-main and no-push readback;
* deviations and residual risks;
* Resolved Execution Issues / Near-Misses;
* Pre-Existing Failure Classification;
* smallest next step;
* authority expiry.

Explicitly state whether any lower-layer file changed and why.

Do not issue an acceptance prompt. Do not close the logical whole.

All Worker 2 authority expires permanently at this terminal report. The next planned actor is a fresh independent acceptance Worker.
