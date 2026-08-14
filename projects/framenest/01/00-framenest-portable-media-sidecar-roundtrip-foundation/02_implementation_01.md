# FrameNest Portable Media Sidecar — Application Projection and Secure Filesystem Store

## Authority coordinates

```text
Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 02
Worker exchange ordinal: 02
Worker session target: current-worker-session
Worker phase: implementation
Native planning mode: not-used
Maximum plan-only cycles: 0
```

This is one bounded renewal of implementation authority for the exact current Worker session. Previous exchange authority expired at its report; this prompt grants authority only for the slice below.

Do not expand or close the logical whole.

## Current accepted candidate

```text
Contained clone:
/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w2-e01

Branch:
feat/portable-media-sidecar-roundtrip-foundation

Candidate HEAD:
96bf7df2001c38284d9aa136b56d0109f24700d5

Candidate tree:
6febf4e683adb61024757e89dce7725a3e890a64

Candidate parent:
a23b4bc786357da3591a4f75087b7e8a3d50d341

Candidate subject:
feat: add portable media sidecar codec

Public main:
a23b4bc786357da3591a4f75087b7e8a3d50d341

Required AP gitlink/submodule:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

The accepted candidate has exactly these changes relative to its parent:

```text
A docs/adr/0059-portable-media-sidecar-roundtrip-foundation.md
M docs/adr/README.md
A src/framenest/domain/media_sidecar.py
A tests/unit/domain/test_media_sidecar.py
```

The candidate is an implementation-PASS slice, not independently accepted and not published.

## Mandatory repository gate

Before substantive analysis or mutation:

1. Confirm exact `pwd -P`.
2. Confirm origin is `https://github.com/cisarik/framenest.git`.
3. Confirm the expected branch and exact HEAD, tree, parent, subject, and four-path diff.
4. Confirm `.ap` gitlink and checked-out submodule HEAD.
5. Confirm tracked worktree, index, and untracked state are clean.
6. Confirm no merge, rebase, cherry-pick, revert, or bisect is active.
7. Credential-free `git ls-remote` must show public `main` still at `a23b4bc…`.
8. Read applicable repository instructions, the pinned AP protocol, ADR-0059, and `docs/WORKER_EXECUTION_CONTRACT.md` directly from this contained clone.
9. Re-run the committed sidecar codec tests before mutation.

If any invariant fails, stop without mutation and report `BLOCKED` with only the exact mismatch and smallest safe continuation.

Do not inspect, switch, clean, stash, or mutate the owner checkout.

## Canonical execution envelope

Use:

```text
/home/agile/Projects/framenest/.venv/bin/python
```

with a sanitized environment equivalent to:

```text
env -i \
  PATH=/usr/bin:/bin \
  LC_ALL=C \
  LANG=C \
  PYTHONNOUSERSITE=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH=<contained-clone>/src
```

Prove imported `framenest` modules come from the contained clone.

Do not create, repair, replace, synchronize, or install into any virtual environment. Do not run dependency or lockfile mutation commands.

## Objective

Implement the second coherent vertical slice:

> Project one explicit catalog media/location into the accepted `SidecarDocument`, and provide a secure local filesystem store supporting export, validation readback, and comparison—without a CLI, HTTP surface, catalog mutation, or publication.

The later `framenest-sidecar` CLI must be able to remain a thin adapter over this boundary.

## Required architecture

Follow existing FrameNest conventions and current semantic owners. Expected new owners are:

```text
src/framenest/application/ports/media_sidecar_store.py
src/framenest/application/media_sidecar.py
src/framenest/infrastructure/filesystem/media_sidecar.py
tests/unit/application/test_media_sidecar.py
tests/unit/infrastructure/filesystem/test_media_sidecar.py
tests/integration/test_media_sidecar_roundtrip.py
```

Exact type and callable names are implementation decisions, but responsibility must remain separated:

* application layer: catalog resolution, projection, identity rules, compare semantics;
* application port: infrastructure-independent sidecar storage/read observations;
* filesystem adapter: path safety, bounded reads, inode classification, atomic replacement and durability;
* accepted domain codec: schema and canonical bytes.

Do not add a database table, migration, dependency, HTTP route, CLI entry point, or Save hook.

Do not modify the accepted codec or ADR merely for stylistic cleanup. If a material contradiction with the frozen contract is proven, stop and report it instead of silently redesigning the format. A narrowly proven defect repair requires authentic red evidence and explicit reporting.

## Catalog projection

Resolve an explicit `media_id` and `location_id` using the existing repositories:

* `MediaRepository`
* `LibraryRepository`
* `MediaMetadataRepository`

Require:

* logical media exists;
* location exists and belongs to the requested media;
* location availability is `available`;
* owning library exists;
* library root uses the native host flavor;
* selected media file and its parent satisfy the filesystem safety gates below.

Build `SidecarDocument` only from catalog-owned state:

* `media_id` and `media_kind` from `LogicalMedia`;
* display title, description, ordered tag keys, classification, genres, creator attribution, Processed state, and timestamps from `MediaMetadataSnapshot`;
* `created_at_ms` and `updated_at_ms` must be the nullable metadata timestamps, not `LogicalMedia` timestamps;
* tag definitions must correspond exactly to the ordered metadata tag keys, preserving that order;
* location identity, library identity, and relative path from the selected `MediaLocation`.

No repository write method may be called.

Missing, mismatched, unavailable, or inconsistent catalog state must produce sanitized typed failures without disclosing absolute paths or private payloads.

## Placement and target safety

The sidecar target is:

```text
{complete-media-filename}.framenest.json
```

adjacent to the selected media file.

Example:

```text
movies/clip.mp4
movies/clip.mp4.framenest.json
```

Require:

* containment beneath the registered root;
* no path traversal;
* root is a real non-symlink directory;
* every relevant parent is a real directory, not a symlink;
* source media is a regular non-symlink file;
* sidecar symlinks and all other non-regular targets are rejected without following or replacing them;
* Windows-flavor roots are rejected on POSIX and vice versa;
* read-only or unwritable placement fails with sanitized `SIDECAR_LOCATION_NOT_WRITABLE` semantics.

Do not reuse any existing content-reader behavior that permits a symlinked media source. ADR-0059 intentionally requires the stricter sidecar gate.

For explicit validation of a supplied sidecar path, classify the directory entry before opening or parsing it. A symlink is an unsafe target, never an absent file.

## Export semantics

Canonical intended bytes come from the accepted codec.

| Existing target                                   | Required outcome                                                     |
| ------------------------------------------------- | -------------------------------------------------------------------- |
| absent                                            | atomically create; status `created`                                  |
| regular, same identity, exact intended bytes      | status `unchanged`; no `os.replace`, chmod, inode, or mtime mutation |
| regular, same identity, valid but different bytes | atomically replace; status `replaced`                                |
| foreign `media_id` or `location_id`               | refuse; `SIDECAR_IDENTITY_CONFLICT`                                  |
| malformed                                         | refuse; `SIDECAR_MALFORMED`                                          |
| unsupported format/version                        | refuse; `SIDECAR_UNSUPPORTED`                                        |
| symlink or other non-regular inode                | refuse; `SIDECAR_UNSAFE_TARGET`                                      |

`library_id` and `relative_path` are payload fields, not foreign-identity keys.

For create or replace:

* use a same-directory uniquely owned temp named `.framenest-sidecar.<16-hex>.tmp`;
* create the temp without following links, initially private;
* write all intended bytes and fsync the file;
* validate the completed temp through the accepted codec;
* set the final installed mode to `0644`;
* use `os.replace` only after all pre-replace checks pass;
* fsync the containing directory;
* re-read safely and prove exact byte equality before reporting success;
* clean up only the temp created by this operation;
* never destroy the previous valid target when temp creation, write, fsync, validation, or replacement preparation fails.

Do not chown and do not mutate SQLite.

## Validation boundary

Provide the application/port capability needed for the later:

```text
framenest-sidecar validate --path ...
```

For this slice:

* safely read one explicit regular non-symlink file;
* enforce the 256 KiB bound;
* decode it with the accepted codec;
* return a typed successful observation/document;
* preserve `SIDECAR_MALFORMED` versus `SIDECAR_UNSUPPORTED`;
* do not access or mutate the catalog;
* do not invent the final CLI output envelope in this exchange.

## Compare semantics

Public comparison vocabulary is frozen:

```text
match
stale
mismatch
missing
```

with:

```text
SIDECAR_COMPARE_MATCH
SIDECAR_COMPARE_STALE
SIDECAR_COMPARE_MISMATCH
SIDECAR_COMPARE_MISSING
```

Precedence:

1. No sidecar directory entry → `missing`.
2. Existing non-regular target → error, not `missing`.
3. Unreadable or oversize regular file → error.
4. Malformed or unsupported document → corresponding error.
5. Requested `media_id` or `location_id` differs → `SIDECAR_IDENTITY_CONFLICT`.
6. Payload equals current catalog projection → `match`.
7. Payload differs and sidecar `updated_at_ms` is older → `stale`.
8. Payload differs and the sidecar revision is equal or newer → `mismatch`.

Payload equality includes every v1 field except:

```text
created_at_ms
updated_at_ms
```

Therefore misleading or manually edited timestamps cannot turn equal content into stale or mismatch.

When payload differs:

* `null` is older than any integer;
* two null revisions are equal.

Compare is read-only. It must not repair either side.

## Test-first evidence

Create focused tests before production implementation and capture an authentic red failure.

At minimum prove:

### Application

* minimal and fully populated projections;
* metadata timestamps, not logical-media timestamps;
* ordered tag-definition projection;
* Processed present and absent;
* missing media/location/library;
* media/location identity mismatch;
* unavailable location;
* no repository writes;
* exact four compare results and codes;
* payload equality wins over misleading timestamps;
* stale versus mismatch nullable-revision ordering;
* foreign identity is an error.

### Filesystem

* correct adjacent filename;
* create, replace, and unchanged behavior;
* second unchanged export keeps exact bytes and does not call `os.replace`;
* created/replaced targets are mode `0644`;
* valid non-canonical same-identity JSON is replaced canonically;
* malformed, unsupported, foreign, symlink, directory, FIFO or other practical special targets are preserved and refused;
* source-media symlink and symlink parent are refused;
* traversal and non-native roots are refused;
* bounded read and oversize rejection;
* previous target survives injected pre-replace/temp-validation failure;
* temp cleanup is limited to the owned temp;
* successful readback is byte-identical.

### Integration

Using real current SQLite repository adapters and a synthetic temporary library:

```text
catalog state
→ projection
→ export
→ validation readback
→ compare match
→ second export unchanged
```

Prove the operation does not create a sidecar table, migration, or catalog mutation.

## Validation commands

Run through the sanitized exact-source envelope:

* committed codec tests before mutation;
* new focused application/filesystem tests;
* integration round-trip test;
* relevant existing application and filesystem unit suites;
* persistence migration invariant covering the forbidden sidecar table;
* `compileall` for changed source packages;
* `git diff --check`.

Keep evidence compact but include exact commands, exit statuses, and test counts.

## Commit boundary

Create exactly one new local commit on top of `96bf7df…`.

Recommended subject:

```text
feat: add portable media sidecar storage
```

Do not amend, rebase, merge, squash, tag, or push.

At completion prove:

* new commit SHA, tree, exact parent and subject;
* exact changed paths and purposes;
* clean tracked/index/untracked state;
* no active Git operation;
* public `main` remains `a23b4bc…`;
* candidate branch still has no pushed publication attributable to this exchange.

## Explicit exclusions

Do not implement:

* `framenest-sidecar` CLI or `pyproject.toml` entry;
* FastAPI or other HTTP surface;
* metadata Save coupling;
* sidecar-to-catalog import or rebuild;
* drift repair;
* multi-location fan-out;
* background synchronization;
* database migration or sidecar table;
* covers, publication, removal, backup, acquisition, UI or deployment;
* Windows behavior beyond rejecting non-native roots and recording the existing residual;
* Meta or AP changes.

No NUC, SSH, sudo, provider, browser, production, private-media, or owner-checkout mutation.

## Terminal report

Return exactly one report beginning:

```text
### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 02
Worker exchange ordinal: 02
```

Use either:

```text
Standard terminal status: PASS
Phase-qualified result: implementation-PASS
Result artifact or commit: <new-local-commit>
Logical-whole closure: not-closed
Report justification: new-mutation
```

or a truthful `BLOCKED`/`FAIL`.

Include:

* renewed gate evidence;
* authentic red evidence;
* implemented responsibility boundaries;
* projection, export, validation, compare and safety matrices;
* exact commands, exits and counts;
* exact changed paths;
* commit/tree/parent/subject;
* public-main readback and no-push confirmation;
* deviations, residual risks and missing evidence;
* resolved execution issues or near-misses;
* pre-existing failure classification;
* smallest next step;
* authority expiry.

Do not issue the next Worker prompt. All authority expires at the terminal report.
