### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation  
Worker session ordinal: 01  
Worker exchange ordinal: 03

```text
Standard terminal status: PASS
Phase-qualified result: planning-PASS
Result artifact or commit: not-applicable
Logical-whole closure: not-closed
Report justification: new-material-risk
```

## Repository gate

Contained clone `/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w1-e02`:

- `pwd -P` = exact target
- origin = `https://github.com/cisarik/framenest.git`
- detached HEAD, tree `a1ea29c5fa7e6878670b243ef34b8b0b31084829`
- HEAD and public `origin/main` = `a23b4bc786357da3591a4f75087b7e8a3d50d341`
- `.ap` gitlink and HEAD = `041de310ea33ed1b47dd8f5fbfcc2829d1a32514`
- worktree and index clean; untracked none; no rebase/merge/cherry-pick/revert/bisect

Owner checkout `/home/agile/Projects/framenest` was not inspected or modified. No clone, fetch, checkout, or restoration.

Start and end commit: `a23b4bc786357da3591a4f75087b7e8a3d50d341`.  
Changed repository paths: none.

Read-only checks: the gate above plus `media_metadata_repository.py` Save/`get` timestamp behavior. No tests executed.

## Contradiction resolved

Exchange 02 required both wall-clock `sidecar_written_at_ms` and byte-identical re-export. Those cannot hold together. Current source does not define a deterministic product meaning for a sidecar write time. **`sidecar_written_at_ms` is removed from v1.** Canonical bytes contain only catalog-owned fields.

Verified catalog timestamps (`MediaMetadataSnapshot`, not `logical_media`):

- No `media_metadata` row: `created_at_ms` and `updated_at_ms` are `None`.
- First persist: both set to Save `now_ms`.
- Later real Save: `created_at_ms` preserved; `updated_at_ms` set to `now_ms`.
- Save status `unchanged`: timestamps are not rewritten.

Those two fields may remain in v1 as nullable catalog revision metadata. They are stable when the catalog is unchanged, so they do not break deterministic export.

## Revised v1 field table

Closed object; always emit every remaining key. JSON `null` or `[]` instead of omitting keys.

| Field | v1 treatment |
| --- | --- |
| `format` = `framenest-media-sidecar` | unchanged include |
| `schema_version` = `1` | unchanged include |
| `media_id`, `media_kind` | unchanged include |
| `display_title`, `description` | unchanged include (nullable) |
| `tag_keys`, `tag_definitions` `{key, display_name}` | unchanged include |
| `content_category`, `acquisition_source`, `genre_keys` | unchanged include |
| creator attribution four fields | unchanged include |
| `processed` | unchanged include |
| `created_at_ms`, `updated_at_ms` | **kept**: nullable `media_metadata` timestamps from source above |
| `location.{location_id, library_id, relative_path}` | unchanged include |
| `sidecar_written_at_ms` | **removed** |

Exclusions from exchange 02 are unchanged (publication, covers, checksums, availability, roots, secrets, requester-private state, unknown keys).

## Repeated-export / no-op semantics

Export encodes the current catalog projection to canonical bytes (no wall-clock field).

| Existing target | Export behavior | Status |
| --- | --- | --- |
| Absent | create via temp + validate + `os.replace` | `created` |
| Regular file, same `media_id` and `location_id`, file bytes equal intended encoding | success; **do not** `os.replace` | `unchanged` |
| Regular file, same identity, bytes differ (including valid non-canonical JSON) | temp + validate + `os.replace` | `replaced` |
| Regular file, foreign `media_id` or `location_id` | refuse; leave file | error `SIDECAR_IDENTITY_CONFLICT` |
| Malformed or unsupported regular file | refuse; leave file | error `SIDECAR_MALFORMED` or `SIDECAR_UNSUPPORTED` |
| Symlink, directory, socket, FIFO, device, other non-regular | refuse; do not follow; do not replace | error `SIDECAR_UNSAFE_TARGET` |

A second export with unchanged catalog must be byte-identical to the first and take the `unchanged` path. Catalog is never written.

## Canonical compare vocabulary

Public `result` values, only:

```text
match
stale
mismatch
missing
```

`not_exported` is withdrawn. `missing` is the sole public name for an absent sidecar path.

Machine-readable codes:

| `result` | `result_code` |
| --- | --- |
| `match` | `SIDECAR_COMPARE_MATCH` |
| `stale` | `SIDECAR_COMPARE_STALE` |
| `mismatch` | `SIDECAR_COMPARE_MISMATCH` |
| `missing` | `SIDECAR_COMPARE_MISSING` |

CLI: JSON stdout with `operation`, `result`, `result_code`. **Exit 0** for those four completed observations. **Exit 1** for errors (unsafe target, malformed, unsupported, identity conflict, unreadable/oversize, catalog identity not found, invalid input). No HTTP surface.

**Match predicate:** identity matches the requested `--media-id` / `--location-id`, and **payload** fields are equal. Payload is every v1 field except `created_at_ms` and `updated_at_ms`. Exact payload equality is `match` even if sidecar timestamps were hand-edited to look older or newer. Timestamps are not stronger than content.

**Revision used only when payload differs:** sidecar `updated_at_ms` vs current catalog `updated_at_ms`. JSON `null` is older than any integer. Two nulls are equal.

## Comparison / error precedence

First applicable wins. Inode class is classified before JSON parse.

| Order | Condition | Outcome |
| --- | --- | --- |
| 1 | No directory entry at the sidecar path | `missing` / `SIDECAR_COMPARE_MISSING` |
| 2 | Entry exists and is not a regular file (symlink, directory, socket, FIFO, device) | error `SIDECAR_UNSAFE_TARGET` (not `missing`) |
| 3 | Regular file unreadable or over the 256 KiB bound | error (not a compare result) |
| 4 | Regular file fails UTF-8, JSON, duplicate keys, closed schema, or unsupported version | error `SIDECAR_MALFORMED` or `SIDECAR_UNSUPPORTED` |
| 5 | Valid sidecar whose `media_id` or `location.location_id` is not the requested identity | error `SIDECAR_IDENTITY_CONFLICT` |
| 6 | Valid same-identity sidecar; payload equals current catalog projection | `match` |
| 7 | Valid same-identity sidecar; payload differs; sidecar `updated_at_ms` older than catalog | `stale` |
| 8 | Valid same-identity sidecar; payload differs; sidecar `updated_at_ms` equal or newer | `mismatch` |

`library_id` and `relative_path` are payload, not foreign-identity keys.

## Changed atomic-write / target-safety

Unchanged: same-directory temp `.framenest-sidecar.<hex>.tmp`, `O_NOFOLLOW`, fsync file, validate temp bytes, fsync directory, final mode `0644`, no chown, cleanup only the owned temp class, no SQLite write.

**Changed:** `os.replace` is not unconditional. Byte-equal same-identity files skip replace. Replace remains only for same-identity byte changes after temp validation. Malformed, unsupported, special-file, symlink, and foreign-identity targets must not be destroyed.

Export statuses: `created` | `replaced` | `unchanged`.

## Tests added to the future validation matrix

In addition to the exchange-02 matrix:

- Codec fixtures contain no `sidecar_written_at_ms`.
- Encoding the same snapshot twice is byte-for-byte identical (clock may advance between calls).
- Second `export` of unchanged catalog: identical bytes; `unchanged`; `os.replace` not used (inode/mtime or hook).
- Same-identity valid file with different bytes: `replaced`; existing valid sidecar preserved if temp validation fails.
- Refuse replace of malformed, unsupported, symlink, directory, and foreign-identity targets; bytes unchanged.
- Compare: absent path → `missing`; symlink → error not `missing`; payload-equal with misleading `updated_at_ms` → `match`; older revision plus different title → `stale`; equal/newer revision plus different title → `mismatch`; foreign identity → error.
- CLI contract: exit 0 and the four `result`/`result_code` pairs; exit 1 for error codes.

## Unaffected exchange-02 decisions (preserved)

`framenest-sidecar` CLI; catalog-to-sidecar projection only; no import/rebuild; `{media_filename}.framenest.json`; explicit `--location-id`; catalog authoritative; sidecar never overwrites catalog; atomic same-directory replacement when bytes change; final mode `0644`; no migration; no new dependency; allowlist and exclusions unchanged except removal of `sidecar_written_at_ms` and the compare/export semantics above.

Changed likely paths: none.

## Smallest implementation step

In a later fresh implementation session: ADR-0059 plus `SidecarDocument` deterministic JSON codec unit tests that forbid `sidecar_written_at_ms` and prove byte-identical re-encode of an unchanged snapshot.

No Worker 2 prompt.

### Deviations / remaining risks

- Cursor plan file outside the repository was updated so native plan mode stays aligned. No repository plan file.
- Windows `os.replace` no-op detection remains specified from POSIX evidence.
- Tag display-name changes without a media Save leave `updated_at_ms` unchanged; payload then differs at equal revision and classifies as `mismatch`, which is intended.

### Resolved Execution Issues / Near-Misses

None this exchange. Gate ran before analysis. Owner checkout untouched.

### Pre-Existing Failure Classification

Not applicable to this targeted revision. Contained clone matched the declared baseline.

### Authority expiry

All Worker 1 exchange 03 authority expired at this terminal report. Planning PASS is not implementation authority.