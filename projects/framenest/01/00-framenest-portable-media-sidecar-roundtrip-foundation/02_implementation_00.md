# Worker 2 Implementation — Portable Media Sidecar v1 Domain Contract

Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used

Persistent role identity: one fresh Worker assigned to the WORKER role
Worker session profile: Bounded Test-First Domain Implementation Worker
Phase: Implementation
Implementation slice: accepted ADR-0059 plus deterministic portable-media-sidecar v1 domain codec
Reasoning recommendation: High — the slice is narrow but establishes a durable serialized-data contract whose identity, strict validation, canonical bytes, and future compatibility must be correct before filesystem writes exist
Evidence posture: non-independent
Worker topology: single-active
Internal delegation posture: not-used

Prior authority: none
Authority renewal: not-applicable; fresh Worker session
Planning disposition: accepted by the ORCHESTRATOR
Implementation authority: exact four-path slice below
Repository mutation authority: exact isolated clone and allowlist below
Host mutation authority: create exactly one isolated standalone clone at the declared absent target; execute tests through the preserved canonical interpreter
Git branch authority: create exactly one local implementation branch
Git commit authority: exactly one local candidate commit after all gates pass
Push/publication authority: none
Meta mutation authority: none
AP mutation authority: none
Deployment and production authority: none
NUC, SSH, sudo, network-control, provider, browser, private-media, account, or external-service authority: none
Logical-whole closure authority: none

Planning PASS is evidence, not implementation authority. This prompt is the complete implementation authority.

## 1. Accepted implementation objective

Create one immutable local candidate that establishes the portable-media-sidecar v1 schema and deterministic codec before any filesystem, application, repository, CLI, rebuild, or synchronization behavior exists.

Implement exactly:

```text
docs/adr/0059-portable-media-sidecar-roundtrip-foundation.md
docs/adr/README.md
src/framenest/domain/media_sidecar.py
tests/unit/domain/test_media_sidecar.py
```

No other path may change.

Expected commit subject:

```text
feat: add portable media sidecar codec
```

This slice does not complete the logical whole. It creates the accepted durable contract on which later application/filesystem and CLI slices will depend.

## 2. Canonical repository and baseline

Canonical repository:

```text
https://github.com/cisarik/framenest.git
```

Canonical public `main`:

```text
a23b4bc786357da3591a4f75087b7e8a3d50d341
```

Expected tree:

```text
a1ea29c5fa7e6878670b243ef34b8b0b31084829
```

Expected parent:

```text
4add009e1f89fcc05b9e8bc306d6ecc8e568547b
```

Expected subject:

```text
fix: reconcile selected Mullvad status
```

Expected AP gitlink and initialized submodule HEAD:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Owner checkout:

```text
/home/agile/Projects/framenest
```

The owner checkout contains unrelated historical work and must remain read-only. Do not inspect, enumerate, open, clean, stash, reset, switch, restore, or modify its tracked or untracked repository content.

Its canonical `.venv` may be used only as the preserved execution environment according to `docs/WORKER_EXECUTION_CONTRACT.md`.

Implementation target:

```text
/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w2-e01
```

Implementation branch:

```text
feat/portable-media-sidecar-roundtrip-foundation
```

## 3. Contained-clone creation

Before clone creation, require:

```bash
test -d /home/agile/Projects/framenest-worktrees
test ! -e /home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w2-e01
env GIT_TERMINAL_PROMPT=0 \
  git ls-remote https://github.com/cisarik/framenest.git refs/heads/main
```

Require public `main` exactly:

```text
a23b4bc786357da3591a4f75087b7e8a3d50d341
```

If the target exists or the public ref differs, perform no cleanup, reuse, deletion, fetch, pull, reset, or repair. Return `BLOCKED`.

If the gates pass, run the authorized creation sequence once:

```bash
target=/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w2-e01

env GIT_TERMINAL_PROMPT=0 \
  git clone --no-checkout https://github.com/cisarik/framenest.git "$target"

git -C "$target" checkout --detach \
  a23b4bc786357da3591a4f75087b7e8a3d50d341

env GIT_TERMINAL_PROMPT=0 \
  git -C "$target" submodule update --init --recursive .ap
```

Do not retry a failed clone, checkout, or submodule update. Leave any partial target untouched and report `BLOCKED`.

After successful creation, gate from the target:

```bash
cd "$target"
pwd -P
git status --short --branch
git status --porcelain=v1 --untracked-files=all
git remote get-url origin
git branch --show-current
git rev-parse HEAD
git rev-parse HEAD^{tree}
git rev-parse HEAD^
git show -s --format='%H%n%T%n%P%n%s' HEAD
git submodule status .ap
git -C .ap rev-parse HEAD
git diff --exit-code
git diff --cached --exit-code
env GIT_TERMINAL_PROMPT=0 git ls-remote origin refs/heads/main
```

Require:

```text
target path = exact
origin = canonical FrameNest repository
HEAD = detached exact baseline
public main = exact baseline
tree, parent, subject = exact
AP gitlink and submodule HEAD = exact
tracked worktree = clean
index = clean
untracked paths = none
active Git operation = none
```

Only after this gate, create the local branch:

```bash
git switch -c feat/portable-media-sidecar-roundtrip-foundation
```

Do not push the branch.

## 4. Mandatory focused reading

Read completely:

```text
AGENTS.md
.ap/AP.md
.ap/AP_WORKER.md
.ap/PROMPT_CONTRACTS.md
docs/WORKER_EXECUTION_CONTRACT.md

SPEC.md section governing portable sidecar manifests
ROADMAP.md sidecar, round-trip, rebuild, drift, and repair entries
SECURITY.md
docs/adr/README.md

docs/adr/0010-initial-persistence-foundation.md
docs/adr/0011-stable-domain-identities.md
docs/adr/0013-initial-library-registry.md
docs/adr/0025-minimum-persistent-media-catalog-foundation.md
docs/adr/0027-persistent-display-title-and-canonical-tags.md
docs/adr/0029-persistent-plain-text-media-description.md
docs/adr/0030-automatic-processed-collection.md
docs/adr/0033-catalog-backup-and-recovery-foundation.md
docs/adr/0035-authoritative-server-and-client-state-model.md
docs/adr/0045-content-classification-and-movie-identification.md
docs/adr/0055-youtube-creator-taxonomy-and-immutable-provenance.md

src/framenest/domain/identities.py
src/framenest/domain/media.py
src/framenest/domain/media_metadata.py
src/framenest/domain/media_classification.py
src/framenest/application/ports/media_metadata_repository.py
src/framenest/infrastructure/persistence/catalog_backup.py

tests/unit/domain/test_identities.py
tests/unit/domain/test_media.py
tests/unit/domain/test_media_metadata.py
tests/unit/domain/test_media_classification.py
tests/unit/infrastructure/backup/test_catalog_backup.py
```

Use `rg` for focused searches. Do not reopen the selected objective, plan another logical whole, or perform broad repository auditing.

Meta is supporting history only. Do not read Meta to infer task authority and do not mutate it.

## 5. Frozen v1 contract

The codec owns a closed v1 object whose keys are always emitted. Optional values use JSON `null`; collections use arrays, never omitted fields.

Root fields exactly:

```text
format
schema_version
media_id
media_kind
display_title
description
tag_keys
tag_definitions
content_category
acquisition_source
genre_keys
creator_attribution_kind
creator_stable_id
creator_handle
creator_display_name
processed
created_at_ms
updated_at_ms
location
```

Fixed identity:

```text
format = "framenest-media-sidecar"
schema_version = 1
```

Nested contracts:

```text
tag_definitions[] = {
  "key": <canonical tag key>,
  "display_name": <canonical display name>
}
```

```text
processed = null
```

or:

```text
processed = {
  "collection_key": "processed",
  "processed_at_ms": <non-negative integer>
}
```

```text
location = {
  "location_id": <canonical UUIDv4>,
  "library_id": <canonical UUIDv4>,
  "relative_path": <portable slash-separated relative path>
}
```

`created_at_ms` and `updated_at_ms` are nullable `MediaMetadataSnapshot` timestamps, not logical-media or location timestamps.

They must either both be `null` or both be non-negative integers with:

```text
updated_at_ms >= created_at_ms
```

The schema must contain no:

```text
sidecar_written_at_ms
absolute library root
host path
device identity
publication state
cover state
checksum
observed size or mtime
availability
database path or revision
application version
analysis/provider/request state
requester-private acquisition state
credential, token, cookie, environment value, or secret field
extension or unknown field
```

## 6. Domain implementation

Create:

```text
src/framenest/domain/media_sidecar.py
```

Use standard-library code and existing FrameNest domain types. Add no dependency.

Provide a small explicit API built around:

```text
SIDECAR_FORMAT
SIDECAR_SCHEMA_VERSION
MAX_SIDECAR_BYTES

FrameNestMediaSidecarError
SidecarTagDefinition
SidecarProcessedState
SidecarLocation
SidecarDocument

encode_media_sidecar(document: SidecarDocument) -> bytes
decode_media_sidecar(payload: bytes) -> SidecarDocument
```

Equivalent private helpers are allowed. Do not add another public framework, repository, port, service, or abstraction.

Use existing value objects and enums where applicable:

```text
MediaId
MediaLocationId
LibraryId
MediaKind
MediaRelativePath
MediaDisplayTitle
MediaDescription
CanonicalTagKey
CanonicalTagDisplayName
MediaCollectionKey
ContentCategory
AcquisitionSource
MovieGenre
CreatorAttributionKind
```

Required invariants include:

* all identities are canonical RFC 4122 UUIDv4 values;
* no duplicate tag keys;
* `tag_definitions` has exactly one definition for every `tag_keys` entry;
* definition keys occur in the same order as `tag_keys`;
* no extra tag definition exists;
* genre keys are unique, bounded, and legal only for `movie`;
* creator fields preserve the existing FrameNest attribution combination rules;
* processed state is either absent or exactly the built-in `processed` collection with a non-negative timestamp;
* timestamps obey the nullable-pair and ordering rule;
* relative paths use the existing `MediaRelativePath` rules;
* invalid construction raises only sanitized sidecar-domain errors.

The error must expose one stable `error_code`:

```text
SIDECAR_MALFORMED
SIDECAR_UNSUPPORTED
```

Do not include raw payload bytes, user strings, paths, exception text, or secret-shaped values in ordinary error messages.

## 7. Canonical JSON encoding

The v1 byte encoding is fixed:

* UTF-8;
* no BOM;
* one JSON object;
* `sort_keys=True`;
* compact separators `(",", ":")`;
* `ensure_ascii=False`;
* `allow_nan=False`;
* exactly one trailing LF byte;
* array order preserved;
* no wall-clock or random value;
* encoded output at most 256 KiB.

Encoding the same `SidecarDocument` twice must produce identical bytes.

Decoding must:

* accept `bytes` only;
* enforce the 256 KiB bound before parsing;
* reject empty input;
* reject UTF-8 BOM and invalid UTF-8;
* reject trailing second values or non-object top-level JSON;
* reject duplicate keys at every nesting level;
* reject `NaN`, `Infinity`, and `-Infinity`;
* reject missing and unknown fields at every closed-object level;
* distinguish a present but unsupported `format` or `schema_version` as `SIDECAR_UNSUPPORTED`;
* classify all other schema, type, identity, range, and invariant failures as `SIDECAR_MALFORMED`;
* reject booleans where integers are required;
* reconstruct the typed immutable `SidecarDocument`;
* never expose the raw payload in errors.

## 8. ADR-0059

Add:

```text
docs/adr/0059-portable-media-sidecar-roundtrip-foundation.md
```

Title:

```text
ADR-0059: Portable Media Sidecar Round-Trip Foundation
```

Status:

```text
Accepted
```

Decision date:

```text
2026-08-14
```

The ADR must record:

* why SQLite must not remain the sole durable portable metadata representation;
* catalog authority during normal operation;
* sidecar v1 as an explicit projection, not live catalog authority;
* the exact closed field contract above;
* deterministic codec rules;
* removal of `sidecar_written_at_ms`;
* filename `{media_filename}.framenest.json`;
* explicit one-location selection;
* future operator operations `export`, `validate`, and `compare`;
* export outcomes `created`, `replaced`, `unchanged`;
* compare results `match`, `stale`, `mismatch`, `missing`;
* compare results are completed observations with exit zero; malformed/unsupported/unsafe/identity failures are errors;
* content equality is stronger than timestamps;
* future same-directory validated atomic replacement and byte-equal no-op;
* malformed, unsupported, special-file, symlink, and foreign-identity targets are never destroyed;
* catalog import/rebuild, Save coupling, multi-copy fan-out, synchronization, conflict resolution, UI, HTTP, migration, deployment, and production behavior are excluded;
* no new dependency and no Alembic revision;
* the current implementation boundary is only ADR + domain codec + unit tests;
* filesystem store, application projection, CLI, round-trip integration, and compare/export implementation remain later slices of the same still-open logical whole;
* known Windows replace/case-folding evidence remains incomplete.

Update `docs/adr/README.md` with exactly the new accepted ADR-0059 row. Do not modify earlier accepted ADR content.

## 9. Test-first execution

Canonical interpreter:

```text
/home/agile/Projects/framenest/.venv/bin/python
```

Do not create, copy, symlink, repair, reconstruct, replace, or mutate `.venv`. Do not run:

```text
poetry env use
uv sync
uv lock
pip install
editable install
```

Verify:

```bash
runtime=/home/agile/Projects/framenest/.venv/bin/python
target=/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w2-e01

"$runtime" --version
```

Require CPython 3.13.x.

Use a sanitized exact-source invocation:

```bash
env -i \
  PATH=/usr/bin:/bin \
  LC_ALL=C \
  LANG=C \
  PYTHONNOUSERSITE=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH="$target/src" \
  "$runtime" -c \
  'import framenest; print(framenest.__file__)'
```

Require the resolved path under the exact target.

Before mutation, run the existing focused baseline:

```bash
env -i \
  PATH=/usr/bin:/bin \
  LC_ALL=C \
  LANG=C \
  PYTHONNOUSERSITE=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH="$target/src" \
  "$runtime" -m pytest \
  tests/unit/domain/test_identities.py \
  tests/unit/domain/test_media.py \
  tests/unit/domain/test_media_metadata.py \
  tests/unit/domain/test_media_classification.py
```

Require exit zero.

Then implement test-first:

1. create only `tests/unit/domain/test_media_sidecar.py`;
2. run it before the production module exists;
3. require an authentic failure caused by the missing sidecar implementation;
4. record the exact red evidence;
5. implement the smallest production code;
6. rerun to green.

The new tests must cover at least:

Positive:

* exact canonical minimal byte fixture;
* fully populated Unicode movie fixture;
* all supported `MediaKind` values;
* empty and populated tag/genre/creator/processed states;
* deterministic repeated encode;
* encode → decode equality;
* decode → encode canonicalization;
* trailing LF and no BOM;
* order preservation for tag keys, definitions, and genres;
* nullable timestamp pair.

Negative:

* invalid UTF-8 and BOM;
* empty, oversize, non-object, or multiple JSON values;
* duplicate keys at root and nested levels;
* missing and unknown root/nested fields;
* unsupported format and schema version;
* explicit rejection of `sidecar_written_at_ms`;
* invalid UUIDs, enums, relative paths, tag definitions, genres, creator combinations, processed state, and timestamps;
* bool-as-int confusion;
* `NaN` and infinities;
* definition/key mismatch, duplicate definition, and wrong definition order;
* sanitized errors containing no input payload or private path.

After implementation run:

```bash
env -i \
  PATH=/usr/bin:/bin \
  LC_ALL=C \
  LANG=C \
  PYTHONNOUSERSITE=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH="$target/src" \
  "$runtime" -m pytest tests/unit/domain/test_media_sidecar.py
```

Then:

```bash
env -i \
  PATH=/usr/bin:/bin \
  LC_ALL=C \
  LANG=C \
  PYTHONNOUSERSITE=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH="$target/src" \
  "$runtime" -m pytest tests/unit/domain
```

Also run:

```bash
env -i \
  PATH=/usr/bin:/bin \
  LC_ALL=C \
  LANG=C \
  PYTHONNOUSERSITE=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH="$target/src" \
  "$runtime" -m compileall -q src/framenest/domain

git diff --check
```

A full repository suite is not required for this isolated domain slice. Do not substitute a full suite for the mandatory focused tests.

Any non-zero mandatory gate or traceback prevents PASS. Classify candidate, harness, environment, or acceptance limitations accurately. Do not rebuild the environment to force green.

## 10. Explicit exclusions

Do not add or change:

```text
src/framenest/domain/__init__.py
src/framenest/application/
src/framenest/infrastructure/
src/framenest/adapters/
pyproject.toml
poetry.lock
Alembic migrations
README.md
PRODUCT.md
SPEC.md
ROADMAP.md
SECURITY.md
SERVER.md
frontend or browser code
deployment or operator documentation
```

Do not implement:

* filesystem reads or writes;
* temporary files, fsync, or `os.replace`;
* library-root resolution;
* SQLite repositories or queries;
* application projection;
* CLI or console script;
* `export`, `validate`, or `compare` execution;
* sidecar-to-catalog import;
* rebuild, repair, drift automation, or synchronization;
* metadata Save hooks;
* HTTP endpoints;
* real media access;
* provider calls;
* deployment.

If the exact domain slice cannot be implemented without another path or dependency, stop and return `PARTIAL` or `BLOCKED`. Do not broaden the allowlist.

Do not invoke `cursor`, `code`, `xdg-open`, GUI applications, browser tooling, AppImages, SSH, or sudo.

## 11. Candidate commit

Only after every required validation passes:

```bash
git status --short
git diff --check
git diff --name-only
```

Require exactly:

```text
docs/adr/0059-portable-media-sidecar-roundtrip-foundation.md
docs/adr/README.md
src/framenest/domain/media_sidecar.py
tests/unit/domain/test_media_sidecar.py
```

Stage exactly those four paths and create one commit:

```text
feat: add portable media sidecar codec
```

Do not amend, rebase, merge, squash, tag, push, publish, or deploy.

After commit, verify:

```bash
git status --short --branch
git status --porcelain=v1 --untracked-files=all
git show -s --format='%H%n%T%n%P%n%s' HEAD
git diff-tree --no-commit-id --name-status -r HEAD
env GIT_TERMINAL_PROMPT=0 git ls-remote origin refs/heads/main
```

Require:

* candidate has sole parent `a23b4bc786357da3591a4f75087b7e8a3d50d341`;
* subject exact;
* changed paths exact;
* final worktree and index clean;
* untracked paths none;
* no active Git operation;
* public `main` remains the baseline;
* candidate remains local and unpublished.

Rerun the focused sidecar test at the exact committed candidate with candidate-source provenance before reporting PASS.

## 12. Terminal report

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo:

```text
Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 02
Worker exchange ordinal: 01
```

Report:

```text
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS | implementation-PARTIAL | implementation-BLOCKED
Result artifact or commit: <exact local candidate or not-applicable>
Logical-whole closure: not-closed
Report justification: new-mutation
```

Include:

* contained-clone creation and repository gate;
* exact baseline and AP pin;
* canonical interpreter and exact-source provenance;
* authentic red evidence;
* implemented public domain API;
* exact v1 field and canonical-byte summary;
* positive and negative test matrix;
* every command with exit status and test counts;
* exact four changed paths and purpose;
* candidate SHA, tree, parent, subject, and diff;
* public-main readback confirming no publication;
* final clean status;
* confirmation of no push, Meta, AP, NUC, provider, browser, deployment, production, or private-media mutation;
* deviations, risks, and missing evidence;
* resolved execution issues/near-misses;
* pre-existing failure classification;
* one smallest next step: ORCHESTRATOR review and routing of the next implementation slice; do not request independent final acceptance yet;
* authority-expiry statement.

Do not issue another Worker prompt and do not close the logical whole.

All Worker 2 exchange 01 authority expires at the terminal report.
