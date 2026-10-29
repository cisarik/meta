### Report for ORCHESTRATOR_CHAT

| Field | Value |
|---|---|
| Logical whole identity | `kronika-sole-identity` |
| Worker session / exchange | `30` / `01` |
| Task identity | `KSI-IMPL-CDATAP` |
| Persistent role | `WORKER` (Fresh Implementation Worker) |
| Status | **PARTIAL — bounded candidate produced and validated except one pin file outside this cut's authority; no commit created** |
| Report justification | `new-mutation` |
| Phase-qualified result | `not-applicable` |
| Logical-whole closure | `not-closed` |
| Start commit | `335e91d199e99e28f2585c1b25531f29bb54270c` |
| End commit | `335e91d199e99e28f2585c1b25531f29bb54270c` (HEAD unchanged; candidate staged in the index, uncommitted) |
| Publication / push | none, no push (public `main` remains `3194f48…`) |
| NUC / provider / browser contact | none |
| Authority expiry | on submission of this terminal report all authority under the prompt expires |

**Why this is `PARTIAL`, stated first.** The implementation, tests, documentation and Part C re-pin are complete and validated. The declared full suite is **not** green: exactly 3 tests fail in `tests/contract/test_kronika_product_string_agreement.py`, a pin file this prompt's positive authority does not name. My two new canonical literals (`"Kronika NUC"`, `"Kronika"` in the new module) are brand-bearing runtime strings, so the inventory reports them as 2 unexpected rows (measured 55 vs pinned 53). Per the prompt's own rule — “If a necessary change falls outside the positive scope, stop and report; do not widen scope” — I stopped rather than edit the unnamed file and did not create the commit. The exact smallest correction is at the end.

---

## 1. The interface as implemented: flags, receipt format and privacy mode

Console surface (script `kronika-catalog`, still mapped to `src/kronika/adapters/cli/catalog.py`):

```text
kronika-catalog identity-labels check
kronika-catalog identity-labels apply --yes [--include-libraries]
kronika-catalog identity-labels rollback --yes [--include-libraries]
```

- `check` — no flags. Uses `create_sqlite_readonly_engine` (plus the existing `inspect_database_migration_status` head gate) and performs reads only. It resolves devices with `display_name == "FrameNest NUC"` exactly and case-sensitively, and libraries whose `display_name` contains `FrameNest` via SQLite `instr` (case-sensitive; a `LIKE` match would have selected rows the case-sensitive replacement could not change). It prints just counts and the receipt digest: `device_candidate_count`, `device_candidate_present` (`count == 1`), `library_candidate_count`, `library_brand_present`, `receipt_digest`.
- `apply` — requires `--yes` (explicit confirmation; else exit 2) and consumes the receipt. Opens `create_sqlite_engine` and runs exactly one `BEGIN IMMEDIATE` transaction through `run_in_immediate_transaction`. Inside it re-resolves both candidate sets and refuses any drift; refuses more than one device candidate; updates the device by ID + exact `FrameNest NUC → Kronika NUC` compare-and-set; updates library rows only when the receipt carries selections **and** `--include-libraries` is present, replacing only the substring `FrameNest → Kronika` and preserving every other character. Post-commit read-back through a fresh read-only engine verifies target labels, `PRAGMA foreign_key_check`, the unchanged schema revision, and zero selected source-label residue.
- `rollback` — same confirmation and flag semantics; inverse per-row compare-and-set by ID + expected canonical value, refuses a missing/renamed row and refuses a device-label collision, then verifies restoration.
- Error surface (all messages constant, no values): `..._CONFIRMATION_REQUIRED` (2), `..._RECEIPT_NOT_FOUND` (3), `..._RECEIPT_INVALID` (2), `..._RECEIPT_EXISTS` (5), `..._STALE_RECEIPT` (5), `..._AMBIGUOUS_CANDIDATE` (5), `..._SELECTION_NOT_APPROVED` (2), `..._VERIFICATION_FAILED` (1), `..._CATALOG_BUSY` (6).

Receipt: one JSON document, version 1, sorted keys, written beside the catalog at `<catalog>.identity-labels-receipt.json` (derived; no operator path flag), created `O_CREAT|O_EXCL|O_WRONLY` at mode `0600`, `fchmod` to `0600`, fsynced, never overwritten. Fields: `version`, `created_at_ms`, `device_candidate_count`, `device_selection` ({id, old_label, new_label} or null), `library_candidate_count`, `library_selections[]`. Read through `O_RDONLY|O_NOFOLLOW` with strict regular-file, same-owner, mode `0600` and `nlink == 1` checks, then strict schema/type/UUID4/value validation and internal inverse-value validation; a tampered file is refused. Only the SHA-256 digest is ever printed; no ID, label, path or SQL reaches stdout, stderr or an exception message.

## 2. Synthetic fixture matrix and invariant/privacy assertions

`tests/contract/test_catalog_identity_labels.py` — 38 tests, all temporary catalogs built through `framenest-db migrate` and seeded with linked `devices`, `libraries`, `logical_media` and `physical_media_locations` rows. Matrix exercised: candidate present; candidate absent; candidate set grown after check; selected row changed; library candidate changed; two device candidates (ambiguous); stale receipt; receipt missing; receipt mode `0644`; receipt symlink; tampered inverse value; malformed/unknown-key/wrong-version receipts; `--include-libraries` without a positive selection; nothing selected; device-only apply; library apply; device-only apply then device-only rollback; full round trip; idempotent second apply; mid-transaction late-update failure; lock contention; CLI busy mapping; post-commit verification failure; one-immediate-transaction spy; case sensitivity (`framenest nuc`, `FrameNest NUC 2`, `framenest videos`); absent database setting.

Invariant assertions read through a fresh engine per snapshot: device/library IDs, relationships (`physical_media_locations.library_id`), every non-label column, schema revision `0035`, `PRAGMA foreign_key_check` empty, and no selected retired label remains. Privacy assertions: `0600` receipt, no IDs/names/paths/SQL in any output, digest equals `sha256(receipt bytes)`. The read-only check is proved by patching `identity_labels.create_sqlite_engine` to raise while `check` still exits 0. Absent inputs fail closed: missing receipt → 3, missing database setting → 4 with no file created, no candidate → selection refusal.

## 3. Guard-failure demonstrations (named mutation → observed failure)

Probe `/tmp/opencode/ksi30/probe_guard_failures.py`, 12 passed (10.0 s), each mutation applied in memory and the named repository test expected to fail. Observed failures, verbatim first lines:

| # | Mutation | Named repository test | Observed |
|---|---|---|---|
| 1 | `_require_private_regular_file` → no-op | `test_apply_refuses_a_receipt_that_is_not_privately_stored` | `assert 0 == 2` |
| 2 | `_write_receipt` O_EXCL → truncate/overwrite | `test_check_refuses_to_overwrite_an_existing_receipt` | `assert 0 == 5` |
| 3 | `_require_receipt_matches_candidates` → no-op | `test_apply_refuses_a_stale_receipt_when_the_candidate_set_grew` | error code `AMBIGUOUS_CANDIDATE` vs `STALE_RECEIPT` |
| 4 | `if len(candidates.device_rows) > 1` → `if False` | `test_apply_refuses_an_ambiguous_device_candidate_receipt` | `assert 2 == 5` |
| 5 | `_compare_and_set` rowcount check removed | `test_compare_and_set_refuses_a_mismatched_expected_value` | `DID NOT RAISE IdentityLabelsStaleReceiptError` |
| 6 | `_require_verified` → no-op | `test_apply_fails_loudly_when_a_writer_does_not_reach_the_target` | `assert 0 == 1` |
| 7 | force `include_libraries=True` in the operation | `test_apply_device_only_preserves_every_other_row_and_column` | library snapshot differs |
| 8 | `catalog._require_identity_labels_confirmation` → no-op | `test_apply_requires_explicit_confirmation` | `assert 0 == 2` |
| 9 | `create_sqlite_readonly_engine` → writable constructor | `test_check_is_read_only_about_the_catalog` | `assert 1 == 0` |
| 10 | `if include_libraries and not receipt.library_selections` → `if False` | `test_apply_refuses_libraries_without_a_positive_selection` | `assert 0 == 2` |
| 11 | `_require_no_other_label` → no-op | `test_rollback_refuses_a_label_collision_on_the_device` | `assert 0 == 5` |
| 12 | `_run_immediate_operation` → deferred `run_in_transaction` | `test_apply_uses_exactly_one_immediate_transaction` | `assert [] == ['immediate']` |

Two-layer redundancies are deliberate and reported: `_require_label` on rollback is masked by the CAS rowcount guard, and the candidate-set guard is masked by the ambiguity guard for the two-candidate case; both are demonstrated at their unique detection point above. Part A/B/C pre-staging verification probe (`probe_retention.py`, 2 passed) re-ran every retention Part A/B/C function against the tracked set plus the two new paths.

## 4. Maintenance documentation and contract pins

`docs/UBUNTU_NUC_DEPLOYMENT.md` gained “Catalog Identity-Label Maintenance (Non-Routine; Stopped Writers)” (54 lines) before “Not Implemented By This Runbook”: check → review sanitized result → backup → `apply --yes` → sanitized read-back → receipt retention (never overwritten, retained until rollback is no longer needed) → `rollback --yes`, plus the no-delete/re-register/no-root/no-schema-revision statement and “never restore a whole backup to undo a label”. It contains no `sudo -u framenest` line, so the operator-runbook command parser is unaffected. `tests/contract/test_nuc_release_docs.py` pins the section title, all three canonical command forms, `--include-libraries`, the receipt filename, mode `0600`, the “device list is not sufficient” sentence and the no-schema-revision statement. `tests/contract/test_catalog_cli.py` pins that the top-level help lists the resource.

## 5. Focused, full-suite and retention counts

| Run (declared AP route, baseline `335e91d`) | Result | Elapsed |
|---|---|---|
| New module `test_catalog_identity_labels.py` | **38 passed, 0 failed** | 28.63 s |
| Combined focused: catalog CLI + identity labels + nuc docs + operator runbook + operator CLI hygiene + CLI/release readers | **220 passed, 0 failed** | 114.16 s |
| `test_kronika_identity_retention.py` after staging | **15 passed, 0 failed** | 0.36 s |
| Guard-mutation probe | **12 passed** (each mutation detected) | 10.0 s |
| Full declared suite (`--operation test`) | **4733 passed, 8 skipped, 3 warnings, 3 failed** | 725.37 s (12:05) |

Baseline `4696/8/3/0` → difference: +40 collected (38 + 1 + 1); 37 new tests pass, and 3 **pre-existing** tests now fail because the candidate adds 2 brand-bearing constants to their inventory (classification below). Skips and warnings unchanged.

## 6. Git, Part A/B and Part C

`git diff --cached --stat` (index; no unstaged diff; no commit):

```text
 docs/UBUNTU_NUC_DEPLOYMENT.md                      |   54 +
 src/kronika/adapters/cli/catalog.py                |  250 +++-
 src/kronika/infrastructure/persistence/identity_labels.py  |  826 ++++++++++++
 tests/contract/test_catalog_cli.py                 |   13 +
 tests/contract/test_catalog_identity_labels.py     | 1403 ++++++++++++++++++++
 tests/contract/test_kronika_identity_retention.py  |   92 +-
 tests/contract/test_nuc_release_docs.py            |   15 +
 7 files changed, 2641 insertions(+), 12 deletions(-)
```

**Commit SHA: none.** I stopped at the authority boundary before finalization; HEAD is unchanged and the candidate is staged and preserved. **Part A byte-unmoved:** the 86 document hashes and 36 Alembic hashes are unchanged (retention Part A green; augmented probe re-verified completeness and bytes with the new paths included). **Part B still measures 20** (retention membership test green; neither new file has a `framenest` basename). **Part C movement, measured, `git ls-files` plus the two new files then re-confirmed after staging:** `src` 1690→**1703** (+13: module 4 retired tokens; catalog 9 error-code values), `tests` 2150→**2178** (+28: the new test file), `docs` 1229→**1231** (+2: runbook label and `/var/lib/framenest` receipt path), per-tree files `src` 184→**185**, `tests` 183→**184**, content paths 507→**509**; env tokens 655→**688** (+9 values in catalog, +24 references in tests), distinct 103→**112** (+9 new codes), bare 29→**29**; capitalized 2748→**2754** (+6) and files 394→**396** (+2); host `/var/lib/framenest` 121→**122** (+1, runbook only). Mutation header 73/30, unit accounts 9/9, deploy/scripts/extension occurrences and the console-script count are unmoved.

## 7. Sites no test exercises

- `_write_receipt` failure branch (`fchmod`/`write`/`fsync` OSError → close + `_remove_owned_receipt`) and `_remove_owned_receipt` itself.
- `_is_catalog_busy` false branch (non-lock `OperationalError` re-raise).
- Verification failure caused by a schema-revision mismatch (the verification-failure test triggers a wrong label instead).
- Receipt-privacy branches for a non-regular path (directory), wrong owner and `st_nlink != 1` (mode and symlink are covered).
- Individual malformed branches of `_parse_device_selection`/`_parse_library_selections` (duplicate ID, wrong value type); the top-level malformed/version/unknown-key branches are covered.
- **Library-only apply/rollback** (receipt with no device selection but library selections, `--include-libraries`) is implemented and referenced by the design but has no test; I identified this gap at the stop boundary and did not add the test after the stop.
- The runbook does not state the execution-owner requirement (private-catalog checks compare UID), so the C-DATA-H grant must name the exact owner invocation.

Derivation callers the prompt's sample did not name: the `_operation_name` resource gate, parser and dispatch in `catalog.py` (extended, authorized); no repository caller was needed; the runbook is also read by `test_nuc_operator_runbook.py` and `test_fedora_systemd_service.py` (unchanged, green); the product-string agreement guard is a newly discovered affected site (below).

## 8. Deviations, risks, missing evidence, smallest next step

- **Blocker (the reason for PARTIAL).** `tests/contract/test_kronika_product_string_agreement.py` is not in the grant. Its measured drift is exactly: `unexpected = [(…identity_labels.py, "<module>", "Constant", 0), (…, "Constant", 1)]`, `missing = []`, `changed = []`, measured 55 vs pinned 53. **Smallest correction:** authorize that file for exactly:

```python
("src/kronika/infrastructure/persistence/identity_labels.py", "<module>", "Constant", 0): "Kronika NUC",
("src/kronika/infrastructure/persistence/identity_labels.py", "<module>", "Constant", 1): "Kronika",
OCCURRENCE_COUNT = 55          # was 53
IN_SCOPE_OCCURRENCE_COUNT = 53 # was 51
```

  `EXPECTED_DUPLICATE_LITERALS` is unchanged (both new literals are unique). With that, the full suite is green and the cut can be committed. I did not make this edit or a commit because the prompt forbids widening scope and a knowingly-red commit would misstate completion.
- **Risk.** The receipt is intentionally never overwritten, so a fresh `check` requires the operator to remove an obsolete receipt; documented in the runbook. The command must run as the catalog owner (UID comparison in the private-catalog check); not yet stated in the section.
- **Missing evidence.** Full-suite green; library-only apply/rollback coverage; the uncovered branches in §7; rendered/operator acceptance (out of scope).
- **Smallest next step.** Issue one bounded correction grant naming `tests/contract/test_kronika_product_string_agreement.py` for the two rows and two counts above (optionally also the library-only test and the owner sentence), then commit the seven staged paths plus that file as the single C-DATA-P commit.

Resolved Execution Issues / Near-Misses: the first M11 mutation run showed a device-only rollback after a device-only apply failing post-commit verification (`libraries_verified=False`); cause was the verifier treating non-included library selections as required to be canonical; fixed by verifying only included selections and a regression test (`test_device_only_rollback_after_device_only_apply_restores_the_catalog`) was added. The runbook pin first failed on a phrase wrapped across lines; resolved by flattening the asserted text. The first Part C measurement undercounted because `git ls-files` does not see untracked files; resolved by measuring an augmented tracked set and re-verifying after the single `git add`.

Pre-Existing Failure Classification: none. The 3 full-suite failures are candidate-caused pin drift in a pre-existing guard (new canonical-brand constants), not pre-existing failures: baseline `335e91d` is `4696/8/3/0`, the failing tests are `test_every_product_string_occurrence_matches_the_pinned_inventory`, `test_the_product_string_inventory_carries_the_pinned_occurrence_count`, `test_no_product_string_occurrence_is_left_without_a_pinned_value`, and the evidence is the exact unexpected-row/count diff above.

```text
Orchestration critique:
MEASURED: The positive authority list omits tests/contract/test_kronika_product_string_agreement.py, but this cut's canonical constants ("Kronika NUC", "Kronika") necessarily add two brand-bearing runtime strings. Evidence: full suite 3 failures with unexpected=[the two rows], missing=[], changed=[]; measured 55 vs pinned 53. Effect: the required full suite cannot be green and no commit can be finalized within the grant. Smallest correction: name that file and authorize the two rows and the 53→55 / 51→53 counts.
LEAD: The library-only apply/rollback path (receipt without a device selection, library selections, --include-libraries) is implemented but untested, and the runbook omits the catalog-owner execution requirement; cheapest useful check is one synthetic fixture test for that path plus one sentence naming the owner.
```

Authority expiry: this terminal report ends the grant; no autonomous continuation, no second commit, no push, no host contact.