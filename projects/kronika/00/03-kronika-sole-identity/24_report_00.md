### Report for ORCHESTRATOR_CHAT

**Logical whole:** `kronika-sole-identity` · **Worker session:** 24 · **Exchange:** 01
**Task identity:** KSI-IMPL-C5 — switch the durable writers to the canonical identity
**Report justification:** `new-mutation`
**Commit:** `3194f48f6b343a460ed5988d92999f91ef999a79` on local `main`, parent `ed5bcb481749f5a732170fd967efc5a2f940cae2`. One commit, no amend, not pushed. Tree clean; submodule still `73e20ef80b88700d5fcbc397cd8edd4fc425869f`.
**Client disclosure:** none; this client emitted no prose above the header.
**Evidence tier:** E3. Durable-artifact writer change with round-trip and rollback-floor verification. No host was contacted.

---

## 0. Gate and baselines

- Gate (pre-edit): branch `main`, HEAD `ed5bcb4`, clean tree, `ap doctor` PASS, `ap project check --baseline ed5bcb4…` PASS.
- Python baseline reproduced: **`4587 passed, 8 skipped, 3 warnings in 685.45s`** — exactly the reported figure. JavaScript reproduced: **583 total, 578 passed, 0 failed, 5 skipped**. Retention: **15 passed**.
- Post-commit: `ap project check --baseline 3194f48…` PASS; `ap exec … --operation runtime-info` resolves `/home/agile/Projects/kronika/src/kronika/__init__.py` (CPython 3.13.9).

## 1. Derivation

Derived by parsing, not from the prompt's list: an AST reference/literal probe over `src/kronika` (frozen revision directory excluded), a full parse of `deploy/ubuntu/kronika_release.py`, reads of every cited module, and a test-coverage grep. All probes ran through `./.ap/ap exec --operation test-focus` at the correct baseline.

**Persisted identities, by layer**

| Layer | Identity | Constant(s) |
|---|---|---|
| domain | generic result schema | `RESULT_SCHEMA_VERSION` |
| domain | movie result schema / prompt | `MOVIE_IDENTIFICATION_RESULT_SCHEMA_VERSION`, `MOVIE_IDENTIFICATION_PROMPT_VERSION` |
| domain | sidecar format | `SIDECAR_FORMAT` |
| application | generic prompt version | `PROMPT_VERSION` |
| application/ports | sidecar filename suffix | `SIDECAR_FILENAME_SUFFIX` |
| infrastructure/persistence | backup application name, staging prefix | `APPLICATION_NAME`, `TEMP_PREFIX` |
| infrastructure/persistence | off-device marker name/purpose, stage prefix | `MARKER_NAME`, `MARKER_PURPOSE`, `STAGE_PREFIX` |
| infrastructure/persistence | workstation marker name/purpose, stage prefix, snapshot purpose, transfer protocol | `MARKER_NAME`, `MARKER_PURPOSE`, `STAGE_PREFIX`, `SNAPSHOT_PURPOSE`, `TRANSFER_PROTOCOL_NAME` |
| infrastructure/persistence (filesystem) | sidecar temporary prefix | `_TEMP_PREFIX` |
| deploy | release markers, manifest key | `RELEASE_SHA_MARKER`, `RELEASE_MANIFEST_MARKER`, `RELEASE_SHA_MANIFEST_KEY` |

**Non-persisted identities:** `VISION_PROBE_PROMPT_VERSION` (infrastructure/ai; **zero** production references — declared only) and `SHARED_USER_AGENT` (infrastructure/ai; one outbound writer, no validating reader).

**Three acceptance categories (separately)**

1. **Raises on collapse** — built by `accepted_durable_identity`: the four analysis identities. The helper now takes `current` + one or more historical spellings, raises on any empty spelling and on any duplicate, so a writer-only change without restructuring still fails loudly. Proven by `test_the_raising_helper_still_refuses_a_collapsed_pair`.
2. **Collapses silently** — literal builders over two constants: `ACCEPTED_SIDECAR_FORMATS`, `ACCEPTED_SIDECAR_FILENAME_SUFFIXES`, `ACCEPTED_APPLICATION_NAMES`, `ACCEPTED_TEMP_PREFIXES`, off-device `ACCEPTED_MARKER_NAMES` / `ACCEPTED_MARKER_PURPOSES` / `ACCEPTED_STAGE_PREFIXES`, workstation `ACCEPTED_MARKER_NAMES` / `ACCEPTED_MARKER_PURPOSES` / `ACCEPTED_STAGE_PREFIXES` / `ACCEPTED_SNAPSHOT_PURPOSES` / `ACCEPTED_TRANSFER_PROTOCOL_NAMES`, and the engine's four accepted release tables (frozen literal data).
3. **No acceptance set** — `VISION_PROBE_PROMPT_VERSION` (never persisted), `SHARED_USER_AGENT` (never validated), the off-device marker constants (host-provisioned; no repository writer), and the workstation transfer-protocol check, which was a single-constant equality before this cut and is now an accepted-set membership.

**Writer / reader counts (persisted identities; tests excluded)**

| Identity | Writers | Readers |
|---|---:|---:|
| `RESULT_SCHEMA_VERSION` | 4 (`media_analysis_lifecycle` 340,432; `media_analysis_lifecycle_api` 111 default, 636 outbound) | 1 (`companion_review_repository` SQL `in_`) |
| `PROMPT_VERSION` | 6 (`build_suggestion_request` 412; `prompts.py` 9; `still_frame_smoke` 94; `nvidia_nim` 705; lifecycle 477; api 172) | 2 (`media_suggestion` 270, 368) |
| `MOVIE_IDENTIFICATION_RESULT_SCHEMA_VERSION` | 3 (`movie_identification` 210; `movie_identification_lifecycle` 120; api 624) | 1 (69–71) |
| `MOVIE_IDENTIFICATION_PROMPT_VERSION` | 4 (`movie_identification` 209,246,357; `movie_identification_lifecycle` 205) | 2 (64–66, 359–362) |
| `SIDECAR_FORMAT` | 2 (`encode_media_sidecar`; `SidecarDocument` default) | 3 (`__post_init__`, `decode`, `_reject_unsupported_identity`) |
| `SIDECAR_FILENAME_SUFFIX` | 1 (`sidecar_filename`) | 1 (`accepted_sidecar_filenames`, used by observe/create) |
| `APPLICATION_NAME` | 1 (`_build_manifest`) | 1 (`_validate_manifest` membership) |
| `TEMP_PREFIX` | 1 (`create_catalog_backup`) | 3 recognizers (below) |
| off-device `MARKER_NAME` / `MARKER_PURPOSE` | 0 (host-provisioned) | 2 / 1 (`_accepted_marker`, validate) |
| off-device `STAGE_PREFIX` | 1 (`publish_or_reuse_offdevice_bundle`) | 1 (`_cleanup_owned_stage`) |
| workstation `MARKER_NAME` / `MARKER_PURPOSE` | 1 each (`_write_new_marker`) | 2 / 1 |
| workstation `STAGE_PREFIX` | 1 (pull) | 1 (`_cleanup_owned_stage`) |
| workstation `SNAPSHOT_PURPOSE` | 1 (`_build_snapshot_envelope`) | 1 (`_load_snapshot_envelope`) |
| workstation `TRANSFER_PROTOCOL_NAME` | 1 (`_build_snapshot_envelope`) | 1 (`_load_snapshot_envelope`) |
| engine marker pair | 1 builder (`cmd_remote_write_markers`) + migrate re-write path | resolved through the four accepted tables |
| engine manifest key | 1 (`make_manifest`) | 1 (`manifest_release_sha`) |

**Coupled validators and cleanup recognizers (all updated and proven):**
- `catalog_backup._reject_unexpected_bundle_state` (children of a bundle directory) → now `ACCEPTED_TEMP_PREFIXES`.
- `catalog_backup._remove_owned_temp_bundle` (owned staging cleanup) → now `ACCEPTED_TEMP_PREFIXES`.
- `catalog_backup_ops._bundle_looks_complete` (retention classification; **a hardcoded former literal not in the prompt's inventory**) → now `ACCEPTED_TEMP_PREFIXES`.
- `catalog_backup_offdevice._cleanup_owned_stage` → `ACCEPTED_STAGE_PREFIXES`.
- `catalog_backup_workstation._cleanup_owned_stage` → `ACCEPTED_STAGE_PREFIXES`.
- `catalog_backup_workstation._load_snapshot_envelope` transfer-protocol equality → `ACCEPTED_TRANSFER_PROTOCOL_NAMES`.
- Engine readers (`read_release_markers`, `manifest_release_sha`) already resolve through accepted tables; confirmed still containing the former spellings.
- `_TEMP_PREFIX` (sidecar filesystem) has **no recognizer** — cleanup unlinks the exact temporary name it created; switched with no compatibility obligation.

**Sites no test exercised before this cut:** `_remove_owned_temp_bundle`, `_bundle_looks_complete`, both `_cleanup_owned_stage` former-prefix branches, `_load_snapshot_envelope` protocol validation, and the writer-default arguments of `cmd_remote_read_release_sha`/`cmd_remote_read_manifest`. All are now exercised by the new module. Sites that cannot be exercised: the off-device marker writer does not exist in the repository; `VISION_PROBE_PROMPT_VERSION` has no production reference; `SHARED_USER_AGENT` has no validating reader.

## 2. Reconciliation against the issued groups

- **Group 1 (four analysis pairs, application-layer trap)** — confirmed; `PROMPT_VERSION` is in `application/media_suggestion.py` as warned. The pair was restructured (see §3) so the alarm cannot collapse.
- **Group 2 (sidecar and the quieter trap)** — confirmed. Correction: the sidecar file **suffix** is not in `domain/media_sidecar.py`; it lives in `src/kronika/application/ports/media_sidecar_store.py:12–19`, and was switched there. The sidecar **temporary prefix** (`filesystem/media_sidecar.py:_TEMP_PREFIX`) was also derived and switched (plan: "associated temporary files"); it has no recognizer.
- **Group 3 (backup identity and temporary prefixes)** — confirmed, and the recognizer set is **three**, not one: `_reject_unexpected_bundle_state` and `_remove_owned_temp_bundle` in `catalog_backup.py`, plus the hardcoded literal in `catalog_backup_ops.py:1548` found only by derivation.
- **Group 4 (off-device and workstation)** — confirmed with one difference: the off-device marker has **no repository writer** (an authorized host task provisions it per `docs/BACKUP_AND_RECOVERY.md`), so `MARKER_NAME`/`MARKER_PURPOSE` switch as the accepted/preferred and future-provisioning spelling and as reader preference; the mount `/mnt/framenest-catalog-offdevice` is untouched (floor/target literal byte-identical).
- **Group 5 (release markers and manifest key)** — confirmed; writers switched, accepted tables untouched and still carry both former spellings. `REMOTE_DEPLOY_DIR/framenest_release.py` was not touched.
- **Group 6 (vision probe)** — confirmed; switched as an outbound identity only, with no accepted set, because it is never persisted; derivation proved it has no production sender/reader at all.
- **Group 7 (user agent)** — confirmed; the only reader is the outbound header writer, and no code validates it.
- **Group 8 (every coupled recognizer)** — derived set reported in §1; three backup recognizers, two stage recognizers, one envelope validator, plus the reader-only off-device marker.
- **Additional derived identities not named in the prompt's sample:** off-device and workstation `STAGE_PREFIX`, the workstation snapshot purpose/transfer-protocol validator, and the sidecar temporary prefix. No difference remains unreconciled.

## 3. Per identity: before → after, restructured acceptance, historical retained

**Raising (4):** writer constant now canonical; former spelling moved to `COMPATIBLE_*`; accepted set = `accepted_durable_identity(writer, compatible)`.

| Identity | Before (writer) | After (writer) | Retained historical |
|---|---|---|---|
| `RESULT_SCHEMA_VERSION` | `framenest-media-suggestion-result-v1` | `kronika-media-suggestion-result-v1` | `COMPATIBLE_RESULT_SCHEMA_VERSION` |
| `PROMPT_VERSION` | `framenest-media-suggestion-v4` | `kronika-media-suggestion-v4` | `COMPATIBLE_PROMPT_VERSION` |
| `MOVIE_IDENTIFICATION_RESULT_SCHEMA_VERSION` | `framenest-movie-identification-result-v1` | `kronika-movie-identification-result-v1` | `COMPATIBLE_MOVIE_IDENTIFICATION_RESULT_SCHEMA_VERSION` |
| `MOVIE_IDENTIFICATION_PROMPT_VERSION` | `framenest-movie-identification-prompt-v2` | `kronika-movie-identification-prompt-v2` | `COMPATIBLE_MOVIE_IDENTIFICATION_PROMPT_VERSION` |

**Silent (12 module pairs + 4 engine tables):** values swapped one-for-one; writer = canonical, `COMPATIBLE_*` = former; every accepted set builds from both constants. E.g. `SIDECAR_FORMAT` `framenest-media-sidecar` → `kronika-media-sidecar`; `TEMP_PREFIX` `.framenest-backup-` → `.kronika-backup-`; off-device/workstation marker names, purposes, stage prefixes, snapshot purpose, transfer protocol, engine `.kronika-release-*` markers and `kronika_release_sha` key. `test_each_writer_emits_the_canonical_spelling_and_retains_the_historical_one` proves, for all 16 pairs, writer literal, historical literal, `writer != historical`, and both memberships. `test_every_reader_resolves_through_the_accepted_marker_tables` keeps the engine tables proven to contain the former spellings.

## 4. Silent-collapse demonstration

`test_a_writer_only_change_would_collapse_each_silent_set` reconstructs the pre-restructure literal for each silent identity: `frozenset({writer, writer})` has length **1**, excludes the historical spelling, while the production set contains **both** and does not raise. The separate raising-alarm test proves the four analysis pairs still raise on collapse, including a duplicate historical spelling.

## 5. Round-trip evidence per artifact type, both spellings

- **Analysis rows:** existing `test_a_successful_run_stays_eligible_under_either_stored_spelling` (parameters: writer spelling and historical spelling) passes; `test_the_predicate_returns_the_same_rows_for_either_spelling` passes; writer literals pinned canonical.
- **Backup bundle:** new `test_backup_round_trip_in_both_spellings` creates with the canonical application name, verifies, rewrites the manifest to the former name and verifies, then restores the historical bundle to a new destination (`state == "restored"`).
- **Sidecar:** new `test_sidecar_round_trip_in_both_spellings` (encode canonical → decode; former-format payload decodes) and `test_sidecar_store_writes_and_reads_both_filename_spellings` (writer emits `.kronika.json`; with the canonical file removed, the former `.framenest.json` alone is observed). Explicit-path former files still validate (`test_sidecar_cli.py:290,421` unchanged).
- **Off-device marker:** existing artifact-reader test proves both name/purpose spellings validate; constants now prefer canonical.
- **Workstation marker/envelope:** `test_workstation_marker_writer_emits_the_canonical_identity` (init writes `.kronika-workstation-snapshot-store.json` with canonical purpose); both marker spellings validate; `test_workstation_envelope_reader_accepts_both_identity_spellings` accepts both snapshot purposes and transfer protocols; unknown protocol still fails closed.
- **Release markers:** writer test now asserts canonical constants and canonical manifest key; the accepted tables still contain both former spellings; the parser remains closed.
- **Non-persisted:** `VISION_PROBE_PROMPT_VERSION` and `SHARED_USER_AGENT` literal pins updated.

## 6. Rollback-floor checkpoint proof

Floor: **`ed5bcb481749f5a732170fd967efc5a2f940cae2`**, the installed complete-reader release. The exact floor modules were extracted from Git (byte-identical to the release tree) and loaded standalone; a checkpoint written by the target code verified with **identical catalog SHA-256** under both the floor and the target:

```text
floor catalog_backup.py sha256   7fa48084d00c3557c211d4674d3997c6ff3ec3f60792134dc5fbe8092c9e9339
floor media_sidecar.py   sha256   0cea68a398028835ffb687767a28b62ef7e5aebe75000c2002b6768459054a46
floor kronika_release.py sha256   f5caa74cf7aeddd4f6f2679646268cad23c00c7f0123b14918ce7803515bdfb7
target writer manifest name       kronika
FLOOR verifies target checkpoint  verified / 0035 / d9f30b3f6462314f2053f977950f8f40f43121e62b8df602c2b19f661463be84
TARGET verifies target checkpoint verified / 0035 / d9f30b3f6462314f2053f977950f8f40f43121e62b8df602c2b19f661463be84
FLOOR verifies historical checkpoint verified
FLOOR decodes target canonical sidecar    12345678-1234-4234-9234-123456789abc
FLOOR parses canonical marker presence    (['.kronika-release-manifest.json'], ['.kronika-release-sha'])
FLOOR resolves canonical manifest key     aaaa… (accepted key)
```

Assumption stated: the installed release was built from that SHA (Orchestrator-verified) and its module bytes equal `git show <floor>:<path>`; no host contact was possible.

## 7. Historical-analysis eligibility

`test_a_successful_run_stays_eligible_under_either_stored_spelling` proves a run stored under the **former** spelling is still opened and returned through the same companion-inbox query and the same ownership predicate (`_successful_generic_predicates` composes the analyzed-row and ownership predicates with the accepted-schema membership). No stored row was rewritten and no filter compares against one constant.

## 8. Old-archive restore drill

New `test_backup_round_trip_in_both_spellings` restores a historical-name bundle to a new destination and verifies the restored state; the full backup/off-device/workstation suites pass on both spellings.

## 9. Frozen residues and coupled-recognizer proof

- `FNCBE01`: `catalog_backup_transfer.py` byte-identical to the floor (`sha256 44ad74993a5aa33cdafd2339a052f553eb58bc04b5fe5e2663f3ff6a888212c6`, file absent from the diff).
- `/mnt/framenest-catalog-offdevice`: literal identical in floor and target; file absent from the diff.
- Recognizers: new tests prove `verify_catalog_backup` reports `INCOMPLETE_BUNDLE` for both `.framenest-backup-*` and `.kronika-backup-*` debris, `_remove_owned_temp_bundle` removes both and preserves foreign directories, `_bundle_looks_complete` rejects both, and both stage cleaners remove former-prefix stages while still refusing foreign names.

## 10. Diff, commit, Part A, Part B, fixtures

`git show --stat HEAD`: **35 files changed, 1031 insertions(+), 206 deletions(-)**, including one new file. Paths are exactly the 14 production files, the engine, 19 updated test files and `tests/contract/test_kronika_durable_writer_identities.py`. `git diff --diff-filter=D HEAD~1..HEAD` is **empty** (nothing removed). Frozen trees (ADRs, Alembic versions, `pyproject.toml`, `ap.project.conf`, `poetry.lock`, `RESTORATION_REFERENCE`) are absent from the diff. Part A byte-unmoved (retention PASS). Part B measured **exactly 20** paths. Every removed former-spelling line is a writer constant or a writer pin; no historical artifact fixture was rewritten. Two writer-output byte fixtures in `test_media_sidecar.py` (`MINIMAL_CANONICAL_BYTES`, `UNICODE_MOVIE_BYTES`) were re-pinned to canonical output because the writer changed them by definition; the former-format decode fixture in the same file is byte-untouched, and the new round-trip test adds explicit former-format coverage (disclosed in §13).

## 11. Full counts

- **Python, declared `test` (pre-commit, exact committed tree):** `4625 passed, 8 skipped, 3 warnings in 679.42s`. Baseline `4587`. **+38**, all 38 collected tests in the new `tests/contract/test_kronika_durable_writer_identities.py` (confirmed by running it alone: 38 passed). No test was removed or skipped; existing files changed assertions only.
- **JavaScript:** `583 tests, 578 pass, 0 fail, 5 skipped` — unchanged; no JavaScript touched.
- **Retention:** 15 passed post-commit.

## 12. Ledger movements and `FROZEN_ALEMBIC_SHA256`

Regenerated at report time:

| Pin | Before | After | Cause |
|---|---:|---:|---|
| `src` files / occurrences | 186 / 1695 | **184 / 1690** | -2 files (`ai/constants.py`, `ai/vision_probe.py` lost their only token); -5 occurrences (those two, `filesystem/media_sidecar.py` -1 temp prefix, `catalog_backup_ops.py` -1 hardcoded literal, `catalog_backup_workstation.py` -1 duplicate purpose line) |
| `tests` files / occurrences | 185 / 2006 | **183 / 2008** | -3 files (roundtrip, movie-identification lifecycle, vision-probe pins) + 1 new writer test; +26 new file, -24 retired writer pins |
| `deploy` files / occurrences | 22 / 246 | 22 / **243** | engine marker pair and manifest key became canonical; accepted tables retain both former spellings |
| `scripts` / `docs` / `extension` | 7 / 86, 88 / 1216, 8 / 145 | unchanged | untouched |
| Content-path membership | 511 | **507** | +1 new writer test, -5 whole-file (the two src outbound files and three test files above) |
| `ENV_PREFIX_TOKEN / DISTINCT / BARE` | 655 / 103 / 29 | unchanged | this cut touches no environment prefix |
| `MUTATION_HEADER` | 73 / 30 | unchanged | C7-A surface |
| Host paths (`/opt`, `/etc`, `/var/lib`, `/var/cache`, mount) | 223 / 83 / 109 / 29 / 23 | unchanged | C6 surface |
| `User=framenest`, `Group=framenest` | 8 / 8 | unchanged | C6 surface |
| Capitalized `FrameNest` occurrences / files | 2748 / 394 | unchanged | no class or message touched |
| Console-script retired entries | 14 | unchanged | `pyproject.toml` untouched |

**`FROZEN_ALEMBIC_SHA256` key count: 36** — 35 numbered revisions `0001`–`0035` plus `__init__.py`; bytes and set equality pass.

## 13. Deviations, risks, missing evidence, smallest next step

**Deviations.**
1. The sidecar **suffix** is in `application/ports/media_sidecar_store.py`, not `domain/media_sidecar.py` as the prompt's group 2 states; switched at the real location.
2. The off-device marker has **no repository writer**; the constants switched as the accepted/preferred spelling and reader preference, and no writer test can exist.
3. Two writer-output byte fixtures were re-pinned to canonical output (see §10); historical reader bytes remain covered.
4. The four `CANONICAL_*` analysis constants were renamed `COMPATIBLE_*` because the former spelling is now the historical one; their tests were updated accordingly.
5. A duplicated `SNAPSHOT_PURPOSE` assignment (same value twice) was folded into one canonical constant.
6. The sidecar temporary prefix was switched although it has no recognizer (plan: "associated temporary files").

**Risks.**
1. Publication and the routine refresh are not performed; the first canonical artifact will be the post-refresh scheduled backup, which must report `ready`. After that refresh the artifact floor becomes the C5 release, not `ed5bcb4`.
2. The NUC still runs the C4-B release, which reads both spellings; the target code is not yet installed.
3. The host-provisioned off-device marker remains former-spelling until a later host task; readers accept it.

**Missing evidence.** No host contact, no live scheduled backup, no NUC verification. The rollback-floor proof uses the floor's Git bytes, not a live process; the equality of release bytes to the installed tree is carried from the Orchestrator's verification of `ed5bcb4`.

**Smallest next step.** Publish `3194f48…` and run the routine refresh with the extra required observation — a scheduled post-refresh backup reporting `ready` — then name the C5 release as the new artifact floor for every later grant.

## Resolved Execution Issues / Near-Misses

- A first full-suite run after implementation returned 4 failures in `tests/contract/test_nuc_release_remote_contract.py`: the harness used the writer constants where it intended the historical marker rows, so two "disagreeing marker" scenarios collapsed to duplicates. Fixed by introducing `HISTORICAL_*` constants from the accepted tables and re-running; final full suite clean.
- The retention occurrence pin moved during the fix (test-side former literals retired), so the `tests` pin was re-measured and corrected from 2010 to 2008 before the final run; no figure was transcribed.
- The floor probe initially failed private-catalog permissions on its `/tmp` scratch; fixed with `0o700` parent mode. No production behavior involved.

## Pre-Existing Failure Classification

**none.** Both baselines were reproduced exactly before any edit, and every failure encountered during implementation was caused by this cut's own edits and fixed before the final full run.

```text
Orchestration critique:
MEASURED: The issued group 2 locates the sidecar suffix in domain/media_sidecar.py; the actual suffix constant is application/ports/media_sidecar_store.py:12-19, and domain/media_sidecar.py carries the sidecar *format* and the filesystem module carries the temporary prefix. Evidence: AST literal/name derivation and the file reads. Effect: a grant-only worker following the location literally would miss the suffix writer entirely. Smallest correction: cite the application/ports suffix explicitly in later grants.
MEASURED: The issued group 3 names one coupled temporary-prefix recognizer; derivation found a third hardcoded former literal at catalog_backup_ops.py:1548 (`_bundle_looks_complete`, retention classification). Evidence: full-tree parse; the new recognizer tests. Effect: without the fix, former-spelling incomplete bundles would have been misclassified as complete. Smallest correction: keep requiring a derived recognizer set rather than a named count.
LEAD: After the routine refresh, the off-device marker provisioned on the host remains former-spelling until a later host task; the reader accepts it, so the product is unaffected, but the host-side canonical provisioning spelling is still documented rather than observed. Cheapest useful check: when C6/C8 touches the host, record the marker filename and purpose present on the mounted destination as sanitized booleans.
```