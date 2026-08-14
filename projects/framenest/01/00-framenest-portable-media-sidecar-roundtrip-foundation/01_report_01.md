### Report for ORCHESTRATOR_CHAT

```text
Standard terminal status: PASS
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Logical-whole closure: not-closed
Report justification: new-evidence
```

## Continuity and authority

Complete bounded renewal for contained-clone creation plus read-only planning only. Exchange 01 was a repository-gate `BLOCKED` report, not a consumed planning cycle. Retained context was convenience only; contained-clone evidence is authoritative for this exchange.

## 1. Repository gates and recovery classification

**Owner checkout** `/home/agile/Projects/framenest` was not inspected beyond exchange-01 facts and was not mutated. The 37 untracked paths were not opened, enumerated, or classified.

**Section 2 identity discrepancy:** the renewed prompt wrote `/home/agile/Projects/framenest at d4c3402a4765b39cee0d8e8c4b33463b549cd4`. That value is not a Git object from exchange 01. Preserve the exchange-01 HEAD `d4c3402a4765b39cee0d8e2063d5ec8be161caf6` (parent was `e8765f7f59e36f6d9828ebde8c4b33463b549cd4`). The prompt string is a transcription mash-up of those two SHAs. No mutation was performed to “fix” it.

**Starting classification verified:** `unrelated-owner-work` primary, `stale-clone` secondary. Immediate recovery: preserve owner checkout; create one isolated clone at the exact absent target. No contrary evidence.

**Pre-clone gates:** `/home/agile/Projects/framenest-worktrees` existed; target was absent; `git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` returned `a23b4bc786357da3591a4f75087b7e8a3d50d341`.

## 2. Contained-clone creation and gate

Target: `/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w1-e02`

Authorized sequence succeeded once: `git clone --no-checkout`, detached checkout of the declared SHA, `submodule update --init --recursive .ap` checked out `041de310ea33ed1b47dd8f5fbfcc2829d1a32514`.

Contained-clone gate:

| Check | Result |
| --- | --- |
| `pwd -P` | exact target |
| origin | `https://github.com/cisarik/framenest.git` |
| branch | detached (`git status`: `HEAD (no branch)`; `git branch --show-current` empty) |
| HEAD / tree / parent / subject | declared baseline |
| public `origin/main` | declared baseline |
| `.ap` gitlink and HEAD | `041de310ea33ed1b47dd8f5fbfcc2829d1a32514` |
| worktree / index | clean |
| untracked | none |
| active Git operation | none |

Start commit and end commit of the contained clone: `a23b4bc786357da3591a4f75087b7e8a3d50d341`. Changed repository-content paths: none.

Authorized host side effect: one new standalone clone at the exact target. Owner checkout, Meta, providers, browser, deployment, and production: none.

## 3. Problem proven from current source

The live catalog is SQLite-backed. User metadata already has nontrivial semantics in `media_metadata`, `media_canonical_tags`, `media_genres`, and related domain types: display title, description, ordered canonical tags, derived Processed membership, content category, immutable acquisition source, movie genres, and creator attribution.

There is **no media-sidecar implementation owner**. `rg sidecar` in source/tests hits: a **forbidden** table name `"sidecar"` in `tests/integration/test_persistence_migrations.py`; deferred “no sidecar writes” clauses in ADRs 0010–0030, 0026, 0033; and an unrelated Tauri/Python-process meaning in ADR-0021. Backup `manifest.json` is a catalog-bundle verifier, not portable media metadata.

`SPEC.md` §11 states portable sidecar manifests are durable metadata, SQLite is an index/cache, live SQLite must not be the sole sync protocol, and sidecar writes must eventually use versioning, validation, and atomic replacement, while “the exact manifest format and schema remain unresolved.” `ROADMAP.md` still lists sidecar contracts, durable-metadata round-trip beyond the SQLite/API slice, rebuild, drift detection, and repair. ADR-0010 still forbids treating database rows as the canonical durable metadata contract.

**Claim corrections (objective unchanged):**

- “Sidecar” in this repository is overloaded (Tauri backend vs media sidecar vs backup manifest). Media-sidecar owner is still absent.
- Technical media kind already includes `image` (not only ADR-0025’s original `video` / `animated_image`).
- Schema head is Alembic `0028`; requester-private X state exists and must stay out of sidecars.
- ROADMAP Phase 6 still also requires directory naming, native OS tags, and repair workflows; this whole must not absorb those.

## 4. Product and operational value

The smallest coherent outcome is: an operator can project selected catalog metadata to a strictly versioned file next to one physical media copy, validate that file, and compare it to current catalog truth—without the sidecar becoming silent application authority, without rebuild, and without coupling ordinary metadata Save to library writes.

Value: portable selected metadata that can travel with a file; a locked v1 contract later rebuilds can consume; proof that FrameNest is not SQLite-only for durable metadata.

## 5. Semantic-owner map (current)

| Concern | Owner today |
| --- | --- |
| Logical media, location, relative path, availability | `domain/media.py`; `application/ports/media_repository.py`; `infrastructure/persistence/media_repository.py` |
| Title, description, tags, Processed derivation, creator fields | `domain/media_metadata.py`; `application/media_metadata.py`; `ports/media_metadata_repository.py`; `infrastructure/persistence/media_metadata_repository.py` |
| Category, acquisition, genres, creator kind | `domain/media_classification.py` |
| Library root locators | `domain/libraries.py`; library repository |
| Scan import | `application/media_import.py` (no sidecar writes; ADR-0026) |
| Metadata Save / API | `SaveMediaMetadata`; `adapters/api/media_metadata_api.py`; composed in `adapters/api/application.py` |
| Catalog schema | `infrastructure/persistence/catalog_schema.py` (head `0028`) |
| Filesystem write analogs | `catalog_backup.py` atomic JSON; `published_media_storage.py` / staging `O_NOFOLLOW`+fsync |
| Operator CLI analog | `framenest-backup`; `framenest-catalog` has device/library/scan only |
| Media sidecar | **none** |

## 6. Routes considered and recommendation

1. **Explicit catalog-to-sidecar projection + validate + compare** — recommended.
2. Automatic projection on metadata Save — rejected for v1: Save must not mutate media organization (ADR-0027/0030); Save would become a library write with read-only/offline/multi-location split-brain and a false SQLite+file transaction.
3. Bidirectional import/rebuild — rejected: ROADMAP rebuild/drift/repair is a later whole; would overwrite or compete with live catalog authority.

Route 1 is the smallest slice that creates a real durable artifact and round-trip evidence without claiming synchronization.

## 7. Exact v1 boundary

Operator CLI `framenest-sidecar` with three read-catalog / write-sidecar-or-read-file operations:

- `export --media-id --location-id` — project one location; atomic replace of that sidecar only.
- `validate --path` — schema/codec check; no catalog write.
- `compare --media-id --location-id` — file vs catalog; report `match` / `stale` / `mismatch` / `missing`; no catalog write.

`export` must encode, write temp, fsync, validate temp bytes, `os.replace`, directory fsync, re-read, and byte-compare to the intended encoding before reporting success.

Round-trip **proves** deterministic encode/decode and filesystem readback. It does **not** prove catalog rebuild, import, Save coupling, or multi-copy fan-out.

## 8. Schema field table

Closed v1 object. Always emit every key. Absent optionals are JSON `null` (or `[]`), never omitted.

| Field | v1 | Justification |
| --- | --- | --- |
| `format` = `framenest-media-sidecar` | include | Schema identity distinct from backup manifests and movie-identification payloads |
| `schema_version` = `1` | include | Integer versioning matching backup-manifest practice |
| `media_id` | include | Opaque UUIDv4 logical identity (ADR-0011) |
| `media_kind` | include | `video` / `animated_image` / `image` |
| `display_title` | include | Distinct from filename (ADR-0027) |
| `description` | include | Durable user text (ADR-0029) |
| `tag_keys` | include | Ordered canonical keys, max 32 |
| `tag_definitions[]` `{key, display_name}` | include | Portable meaning without dumping the global tag catalog or tag timestamps |
| `content_category` | include | First-class facet (ADR-0045) |
| `acquisition_source` | include | Immutable provenance; recorded fact, not a mutation path |
| `genre_keys` | include | Ordered; empty unless category is `movie` |
| `creator_attribution_kind` / `creator_stable_id` / `creator_handle` / `creator_display_name` | include | Structured attribution already in metadata; X source-derived values are facts, not Save-writable |
| `processed` | include | Derived catalog fact (`null` or `{collection_key: processed, processed_at_ms}`) |
| `created_at_ms` / `updated_at_ms` | include | Catalog metadata timestamps for later stale detection |
| `sidecar_written_at_ms` | include | Projection time of this file; not a catalog field |
| `location.{location_id, library_id, relative_path}` | include | Binds the file to one copy without inferring path from `MediaId` and without absolute roots |
| publication state | exclude | Server audience, not portable media metadata (ADR-0049) |
| cover facts | exclude | Separate durable cover store (ADR-0050); paths/digests are server artifacts |
| byte checksum / size / mtime | exclude | v1 must not hash originals; availability/mtime are ephemeral |
| library `root_path`, device id, DB path, Alembic, app version | exclude | Host/operational; backup already forbids path leakage |
| upload, analysis, audit, requester-private X/YouTube claim payloads | exclude | Closed wholes; secrets/private operational state |
| unknown/extension fields | exclude | Strict closed v1; unknown keys fail validation |

## 9. Authority and conflict model

- **Authoritative during normal operation:** FrameNest server process / SQLite catalog (ADR-0035).
- **Sidecar authority in v1:** none for live catalog. It is a projection.
- **Overwrite catalog?** Never in this slice.
- **Missing:** `not_exported`; catalog remains valid.
- **Malformed / duplicate JSON keys / non-UTF-8 / oversize / extra keys:** `SIDECAR_MALFORMED`; no catalog write.
- **Unsupported `format` or `schema_version`:** `SIDECAR_UNSUPPORTED`; no catalog write.
- **Stale:** file `updated_at_ms` < catalog `updated_at_ms` (compare only).
- **Mismatch:** valid file whose projection fields differ from catalog (including newer file than catalog—still not imported).
- **Identity conflict:** existing regular file whose validated `media_id`/`location_id` disagree with the export target → refuse replace.
- **Unreadable/unknown existing file:** refuse replace (do not destroy non-sidecar bytes). Operator deletes out of band.

## 10. Placement and multi-location model

- Filename: `{media_filename}.framenest.json` adjacent to the media file (`clip.mp4.framenest.json`). Full filename, not stem, avoids `foo.mp4` / `foo.mkv` collisions.
- Path construction: library `root_path` + slash-separated `relative_path` parent + sidecar name. Never from `MediaId` alone.
- **One selected `location_id` per invocation.** No write to every copy. Multiple locations remain a catalog fact (`list_locations_for_media` already exists) and are out of v1 fan-out.
- Require: location belongs to media; `availability == available`; library flavor matches host (`posix` on POSIX, `windows` on Windows, same native-flavor gate as content/scan); media is a regular non-symlink file contained in the registered root; parent dir is a real directory, not a symlink.
- Read-only / EROFS / EACCES: sanitized `SIDECAR_LOCATION_NOT_WRITABLE`. Libraries have no read-only schema flag (ADR-0013 deferred writable/read-only).
- Offline / missing / unverified / archived / non-native flavor / symlink media / root symlink: refuse.
- Case-insensitive filesystems: v1 does not probe sibling case aliases; `os.replace` follows the host. Document as a known limit; do not invent case-folding identity.
- Library scan will not import `.json` (`classify_candidate_extension`); hidden temp names starting with `.` are skipped.

## 11. Atomic write and recovery

Reuse backup `_atomic_write_manifest` plus published-media descriptor/`O_NOFOLLOW` discipline:

- Temp class: `.framenest-sidecar.<16-hex>.tmp` in the **same directory** as the target sidecar (rename atomicity on POSIX; hidden from scan).
- Write temp, `fsync` file, validate bytes, `os.replace`, `fsync` directory.
- Final mode `0644` (no secrets). Temp may be `0600` during write. Do not chown.
- Cleanup owner: the write function `finally`; unlink only names matching the temp class in that directory. Never delete the final sidecar on failure after a successful replace that already passed temp validation.
- Crash before replace: leftover temp only; existing sidecar preserved.
- Crash after replace: new bytes are the complete validated encoding.
- **No SQLite write on export**, so “database success / sidecar failure” cannot occur. Cross-resource atomicity is impossible and is not claimed.
- Retry: re-run `export`. Reconciliation/drift repair: not implemented; `compare` reports only.

## 12. Lifecycle interaction matrix

| Interaction | v1 |
| --- | --- |
| Scan-candidate import | excluded (no hook; ADR-0026 already forbids sidecar writes) |
| Upload-to-catalog | excluded (ADR-0043 stays closed) |
| YouTube / X acquisition | observed only as already-persisted metadata fields; no claim/staging data in sidecars |
| Ordinary metadata Save | excluded (no coupling) |
| Content publication | excluded |
| Catalog removal | excluded; leftover sidecar on retained originals is allowed (ADR-0051 retains bytes) |
| Multiple locations | explicit one-location export only |
| Backup / recovery | excluded; distinct from catalog `manifest.json` |
| Future rebuild / import | excluded |

## 13. Likely changed-path allowlist (future implementation Worker)

**New**

- `docs/adr/0059-portable-media-sidecar-roundtrip-foundation.md`
- `src/framenest/domain/media_sidecar.py`
- `src/framenest/application/media_sidecar.py`
- `src/framenest/application/ports/media_sidecar_store.py`
- `src/framenest/infrastructure/filesystem/media_sidecar.py`
- `src/framenest/adapters/cli/sidecar.py`
- `tests/unit/domain/test_media_sidecar.py`
- `tests/unit/application/test_media_sidecar.py`
- `tests/unit/infrastructure/filesystem/test_media_sidecar.py`
- `tests/contract/test_sidecar_cli.py`
- `tests/integration/test_media_sidecar_roundtrip.py`

**Edit**

- `docs/adr/README.md`
- `SPEC.md` (record v1 projection contract; keep rebuild unresolved)
- `ROADMAP.md` (Phase 3/5/6: sidecar **contract** started; rebuild/drift still open)
- `README.md`
- `PRODUCT.md` (portable projection exists; rebuild does not)
- `SECURITY.md` (allowed sidecar contents; no secrets/paths; write safety)
- `pyproject.toml` (`framenest-sidecar` console script only)
- `src/framenest/domain/__init__.py` only if current export pattern requires it

**Do not change:** metadata Save, FastAPI routers, Alembic, `poetry.lock`, browser JS, backup bundle format, upload/acquisition/removal, owner checkout `/home/agile/Projects/framenest`.

## 14. Dependency and migration disposition

No new Python dependency (`json`, `os`, `tempfile` suffice; proven in `catalog_backup.py`). No Alembic revision. Sidecars are filesystem artifacts, not catalog tables. The migrations test that forbids a `sidecar` table remains correct.

## 15. Risks and evidence tier

Risks: Windows rename atomicity and case-folding; operator writing into a read-only `/srv/media` tree; leftover temps after kill -9; confusing backup manifests with media sidecars; future pressure to import sidecars into the catalog.

Evidence tier: repository unit + contract + integration + filesystem tests on synthetic temp directories. No browser, NUC, provider, or production evidence. Exact-source provenance per `docs/WORKER_EXECUTION_CONTRACT.md` (candidate `PYTHONPATH`, not parent `.venv` imports). Independent acceptance: **required** (durable format). Publication: Orchestrator-authorized after acceptance, not mechanical. Production deployment: **not this logical whole**.

## 16. Validation and fresh-acceptance route

Positive: untitled/empty-tags item; fully populated movie with genres and YouTube creator fields; Processed present and absent; export→validate→compare match; second export byte-identical when catalog unchanged.

Negative: duplicate JSON keys; unknown field; schema_version 2; symlink sidecar/parent/media; path traversal in relative_path; location not owned by media; offline location; existing foreign sidecar; EACCES; temp left behind on pre-replace failure; validate must not touch SQLite.

Portability: POSIX write tests; Windows flavor rejected on POSIX (mirror `media_content.py` / scanner native-flavor gates); filename construction from `MediaRelativePath.filename`.

Fresh independent acceptance Worker after implementation. No production restore, no private media.

## 17. Explicit exclusions

Catalog rebuild; sidecar→catalog import; Save-coupled writes; multi-device sync/conflicts; fan-out to every copy; remote locations; directory naming; native OS tags; covers; publication; physical rename; UI/Tauri; AP protocol; NUC deploy; secrets; requester-private acquisition; closed upload/acquisition/removal/backup wholes.

## 18. Material Cooperator decisions (recommended defaults)

The plan is decision-ready if these defaults stand:

1. **Trigger surface:** dedicated `framenest-sidecar` CLI, not FastAPI and not metadata Save.  
2. **Filename:** `{filename}.framenest.json`.  
3. **Location selection:** require `--location-id` even when only one location exists.  
4. **Final mode:** `0644`.

## 19. Expected remaining Worker / phase sequence

1. Orchestrator + Cooperator accept this plan (or override a default).  
2. Fresh implementation Worker, native planning **not-used**, allowlist above, isolated worktree + canonical `.venv` `PYTHONPATH`.  
3. Independent acceptance Worker.  
4. Optional publication (separate authority).  
5. Production/NUC rollout: later whole.  
6. Later product wholes: Save-coupled projection, import/rebuild, drift repair, multi-copy fan-out.

This Worker does not issue a Worker 2 prompt.

## 20. Smallest next implementation step

In a fresh implementation session: add accepted ADR-0059 and `src/framenest/domain/media_sidecar.py` with deterministic UTF-8 JSON codec unit tests (byte-for-byte, duplicate keys, unknown fields, unsupported version) before filesystem writes.

---

Changed repository-content paths: none.

Authorized containment side effect: created `/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w1-e02` at the declared baseline. Owner checkout preserved.

Repository / host (beyond that clone) / Meta / provider / browser / deployment / production mutations: none.

### Deviations, risks, missing evidence

- Cursor native plan presentation was updated outside the repository. No repository plan file was created.
- Trace archival (`01_planning_02.md` / `01_report_02.md`) is owned by a separately authorized archive workflow; this Worker did not write Meta.
- Windows atomic-replace behavior is specified from POSIX evidence plus existing FrameNest native-flavor gates, not from a Windows run.

### Resolved Execution Issues / Near-Misses

- Exchange 01 near-miss (protocol reads batched with a failing owner-checkout gate) did not recur; containment gates ran before sidecar reading.
- Prompt section 2 SHA was wrong; used exchange-01 HEAD; did not mutate anything to match the bad SHA.
- Did not retry clone/checkout/submodule; each authorized command succeeded once.
- Did not inspect owner untracked paths.

### Pre-Existing Failure Classification

Owner checkout remains historical feature branch + 37 untracked paths (`unrelated-owner-work`, `stale-clone`). Not modified. Public `main` already matched the declared baseline before this exchange.

### Smallest next step

Orchestrator reviews this plan; a later complete implementation prompt with native planning disabled may authorize a fresh Worker against the allowlist. This session must not implement.

Planning PASS is not implementation authority.

All Worker 1 exchange 02 authority expired at this terminal report.