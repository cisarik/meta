### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 02
Worker exchange ordinal: 02

```text
Standard terminal status: PASS
Phase-qualified result: implementation-PASS
Result artifact or commit: 633fa3b3884bc865dba26643034ef0c2fc12f394
Logical-whole closure: not-closed
Report justification: new-mutation
```

## Renewed gate evidence

Contained clone `/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w2-e01` (`pwd -P` exact). Origin `https://github.com/cisarik/framenest.git`. Branch `feat/portable-media-sidecar-roundtrip-foundation`. Owner checkout was not inspected or mutated.

Pre-mutation candidate (exchange 01, unchanged parent of this commit):

```text
HEAD:    96bf7df2001c38284d9aa136b56d0109f24700d5
tree:    6febf4e683adb61024757e89dce7725a3e890a64
parent:  a23b4bc786357da3591a4f75087b7e8a3d50d341
subject: feat: add portable media sidecar codec
```

Four-path diff vs public `main` at that HEAD: `A docs/adr/0059-…`, `M docs/adr/README.md`, `A src/framenest/domain/media_sidecar.py`, `A tests/unit/domain/test_media_sidecar.py`. `.ap` gitlink and checked-out submodule `041de310ea33ed1b47dd8f5fbfcc2829d1a32514`. Tracked/index/untracked clean except the six new files of this slice. No merge/rebase/cherry-pick/revert/bisect. Credential-free `git ls-remote origin refs/heads/main` → `a23b4bc786357da3591a4f75087b7e8a3d50d341`.

Canonical interpreter `/home/agile/Projects/framenest/.venv/bin/python` (CPython 3.13.9) with `env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONNOUSERSITE=1 PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=<contained-clone>/src`. Imported modules resolve under the contained clone `src/`.

Pre-mutation codec tests: `pytest tests/unit/domain/test_media_sidecar.py` → **25 passed, exit 0**.

## Authentic red evidence

This exchange wrote focused tests before production application/filesystem modules. Retained same-exchange evidence: collection-time `ModuleNotFoundError` for `framenest.application.media_sidecar` and `framenest.infrastructure.filesystem.media_sidecar` (pytest exit 2). The surviving continuation log does not re-attach that pytest body; red was not reconstructed by deleting production modules after they existed.

Near-miss: the application port `media_sidecar_store.py` was written slightly before the application tests (port-before-tests). Codec/ADR were not modified.

## Implemented responsibility boundaries

| Layer | Owner | Responsibility |
| --- | --- | --- |
| Application | `MediaSidecarService` | catalog resolution, `SidecarDocument` projection, identity rules, export/compare/validate orchestration; no repository writes |
| Port | `MediaSidecarStore` | infrastructure-independent observe/create/replace/explicit-read; `SidecarTargetObservation` `missing`/`regular`/`unsafe` |
| Filesystem | `FilesystemMediaSidecarStore` | `openat`/`O_NOFOLLOW` walk, inode classification, 256 KiB bound, atomic install, durability, owned-temp cleanup |
| Domain codec | unchanged | schema and canonical bytes |

No CLI, HTTP, Save hook, Alembic revision, sidecar table, catalog mutation, or `pyproject.toml` entry.

## Projection, export, validation, compare, and safety

**Projection.** Explicit `media_id` + `location_id` via `MediaRepository`, `LibraryRepository`, `MediaMetadataRepository`. Requires existing logical media; location belonging to that media; availability `available`; existing library; native-flavor root; filesystem safety on the selected file. Document fields come from catalog-owned state. `created_at_ms`/`updated_at_ms` are metadata snapshot timestamps, not `LogicalMedia`. Tag definitions follow ordered metadata tag keys. Missing/mismatched catalog identity → sanitized `SIDECAR_NOT_FOUND`. Unavailable location/library/non-native root → `SIDECAR_UNAVAILABLE`. Incomplete Processed or missing tag definition → `SIDECAR_INCONSISTENT`. Messages do not include absolute paths or private payloads.

**Export.** Canonical bytes from the accepted codec. Adjacent name `{complete-media-filename}.framenest.json`.

| Existing target | Outcome |
| --- | --- |
| absent | atomically create; `created` |
| regular, same identity, exact intended bytes | `unchanged`; no `os.replace`, chmod, inode, or mtime mutation |
| regular, same identity, valid different bytes | atomically replace; `replaced` |
| foreign `media_id` or `location_id` | `SIDECAR_IDENTITY_CONFLICT` |
| malformed | `SIDECAR_MALFORMED` |
| unsupported format/version | `SIDECAR_UNSUPPORTED` |
| symlink or other non-regular inode | `SIDECAR_UNSAFE_TARGET` |

`library_id` and `relative_path` are payload fields, not foreign-identity keys. Create/replace uses `.framenest-sidecar.<16-hex>.tmp`, `O_CREAT|O_EXCL|O_NOFOLLOW` mode `0600`, write+fsync, codec-validate temp, chmod `0644`, `os.replace`, fsync directory, byte-identical readback. Cleanup unlinks only that owned temp. Previous valid target is preserved when temp write/validation/replace preparation fails.

**Validation.** `validate_path` classifies the directory entry before parse (`lstat`); symlink is unsafe, not missing; bounded read; accepted codec; `SIDECAR_MALFORMED` vs `SIDECAR_UNSUPPORTED` preserved; no catalog access. No CLI output envelope.

**Compare** (read-only): `missing` → `SIDECAR_COMPARE_MISSING`; non-regular → error, not `missing`; unreadable/oversize → error; malformed/unsupported → corresponding error; foreign identity → `SIDECAR_IDENTITY_CONFLICT`; payload equal excluding timestamps → `match`; payload differs and sidecar `updated_at_ms` older (`null` older than any int) → `stale`; payload differs and sidecar revision equal or newer (two nulls equal) → `mismatch`. Misleading timestamps cannot turn equal payload into stale/mismatch.

**Safety.** Containment under the registered root; independent `..` / `.` / empty-part refusal; real non-symlink root and parents; source media regular non-symlink (does not reuse content-reader symlink permission); sidecar symlink/dir/FIFO refused without follow/replace; Windows-flavor roots refused on POSIX; unwritable placement → `SIDECAR_LOCATION_NOT_WRITABLE`.

## Exact commands, exits, counts

Sanitized envelope throughout. Provenance: `framenest.__file__` and sidecar modules under the contained clone.

| Command | Exit | Result |
| --- | --- | --- |
| `pytest tests/unit/domain/test_media_sidecar.py` (pre-mutation) | 0 | 25 passed |
| `pytest tests/unit/application/test_media_sidecar.py tests/unit/infrastructure/filesystem/test_media_sidecar_store.py tests/integration/test_media_sidecar_roundtrip.py` | 0 | 33 passed (20+12+1) |
| related application + filesystem + migrations + round-trip | 0 | **194 passed** |
| `compileall -q` application, ports, filesystem | 0 | quiet |
| `git diff --check` | 0 | clean |
| post-commit focused (codec + application + filesystem + integration) | 0 | **58 passed** |

Related split: codec 25, application sidecar 20, `test_media_content_application` 14, `test_media_metadata` 9, filesystem suite 116, `test_persistence_migrations` 9, round-trip 1. Forbidden-product-table fragment includes `"sidecar"`; integration asserts `sqlite_master` has no sidecar table and metadata snapshot is unchanged.

## Exact changed paths

Relative to parent `96bf7df…` (this commit only):

```text
A src/framenest/application/ports/media_sidecar_store.py
A src/framenest/application/media_sidecar.py
A src/framenest/infrastructure/filesystem/media_sidecar.py
A tests/unit/application/test_media_sidecar.py
A tests/unit/infrastructure/filesystem/test_media_sidecar_store.py
A tests/integration/test_media_sidecar_roundtrip.py
```

Codec, ADR-0059, `pyproject.toml`, Alembic, HTTP, and CLI were not changed.

## Commit / tree / parent / subject

```text
commit:  633fa3b3884bc865dba26643034ef0c2fc12f394
tree:    ab04ff1b4448745625ceb97b5b904ed84746f0de
parent:  96bf7df2001c38284d9aa136b56d0109f24700d5
subject: feat: add portable media sidecar storage
```

Working tree clean. No active Git operation. Public `main` still `a23b4bc786357da3591a4f75087b7e8a3d50d341`. Feature branch has no upstream and `git ls-remote origin refs/heads/feat/portable-media-sidecar-roundtrip-foundation` is empty. No push.

## Deviations, residual risks, missing evidence

- Filesystem tests live at `tests/unit/infrastructure/filesystem/test_media_sidecar_store.py`, not the prompt basename `test_media_sidecar.py`, because pytest prepend import mode collides on duplicate `test_media_sidecar.py`.
- Port-before-tests near-miss (above).
- Authentic red pytest body is retained-exchange evidence, not re-copied in this continuation log.
- Windows `os.replace` and case-folding behavior remain incomplete, as recorded in ADR-0059; this slice rejects non-native roots only.
- Temp-name reuse after successful `os.replace` is cleaned with `unlink` of a now-absent name; residual TOCTOU between temp close and chmod is accepted for a trusted local library.
- No Windows runtime evidence beyond flavor rejection.

## Resolved execution issues or near-misses

- Export “different bytes” fixture must alter `movies/clip.mp4`, not a non-occurring `clip.mp4` token, or the store reports `unchanged`.
- Symlink parent `os.open(..., O_DIRECTORY|O_NOFOLLOW)` maps `ENOTDIR`/`ELOOP` to `SIDECAR_UNSAFE_TARGET`.
- Directory-fd walk always closes the previous fd.
- Direct interpreter use without `env -i` remains unsafe under Cursor AppImage `LD_LIBRARY_PATH` (exchange-01 fact; envelope still required).

## Pre-existing failure classification

None attributed to this slice. Existing application content/metadata and filesystem suites passed unchanged (194 including new tests).

## Smallest next step

Independent Orchestrator review of `633fa3b…`. Later authorized slice: thin `framenest-sidecar` CLI adapter over this boundary. Do not close the logical whole.

## Authority expiry

All authority from this prompt expires at this terminal report. No next Worker prompt is issued.