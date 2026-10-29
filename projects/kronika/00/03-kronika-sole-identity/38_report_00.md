### Report for ORCHESTRATOR_CHAT

| Field | Value |
|---|---|
| Logical whole identity | `kronika-sole-identity` |
| Worker session ordinal | `38` |
| Worker exchange ordinal | `01` |
| Persistent role identity | `WORKER` |
| Worker session target | `fresh-worker-session` |
| Native planning mode | `not-used` |
| Worker session profile | Bounded Correction Worker |
| Task identity | `KSI-CORR-C6UNK` — preserve brand-free unknown unit directives |
| Status | **PASS** |
| Report justification | `new-mutation` |
| Phase-qualified result | `not-applicable` |
| Logical-whole closure | `not-closed` |
| NUC contact | none in this cut, by design |
| Start commit | `78cba281960e2f17137647bcc90aab83847a1c0c` |
| End commit | `980041cf13dd427e77263f573694aed7c1a54018` |

Repository gate matched the prompt: standalone `main`, clean tree, HEAD `78cba28…`, containing `.ap` gitlink and submodule HEAD `73e20ef80b88700d5fcbc397cd8edd4fc425869f` (`.ap` clean). Local `refs/remotes/origin/main` now equals `78cba281960e2f17137647bcc90aab83847a1c0c` (the parent, matching the prompt's public-main state; report 37's stale `b8ec042…` note is superseded). All evidence ran through `./.ap/ap exec --baseline 78cba281960e2f17137647bcc90aab83847a1c0c`. No push; `main` is 1 ahead of the local remote-tracking ref (unpublished candidate).

#### 1. Reproduced baseline refusal and post-correction preservation

Same probe file, run before the source edit and again after (synthetic input only; `[Service]` drop-in with `RuntimeDirectoryMode=0700`):

Baseline, before the edit:

```text
REFRuSED -> C6UNK transform runtime-directory-mode: REFUSED exit=27 message='unit directive RuntimeDirectoryMode is not supported'
C6UNK observation: REFUSED exit=27 message='unit directive RuntimeDirectoryMode is not supported'
```

(All six matrix cases refused at baseline; exact lines listed in the transcript above.)

After the edit, same probe:

```text
C6UNK transform runtime-directory-mode: PRESERVED byte-equal=True
C6UNK transform environment-brand-free: PRESERVED byte-equal=True
C6UNK transform unknown-brand-free: PRESERVED byte-equal=True
C6UNK transform unknown-brand-value: REFUSED exit=27 message='unit directive UnknownDirective is not supported'
C6UNK transform environment-brand-value: REFUSED exit=27 message='unit directive Environment is not supported'
C6UNK transform unknown-brand-key: REFUSED exit=27 message='unit directive FramenestMarker is not supported'
C6UNK observation: INSTALLED text='[Service]\nRuntimeDirectoryMode=0700'
```

This is exactly the live failure shape: the host's `40-runtime-directory-mode.conf` now installs through `read_migration_observation` with text byte-identical to the observed drop-in (modulo the read-path `.strip()`), with no mutation produced.

#### 2. Policy matrix

Engine site: `deploy/ubuntu/kronika_release.py` `_systemd_transform_value`, terminal branch now lines 4425–4432; the unconditional raise became:

```python
    if "framenest" in key.lower() or "framenest" in value.lower():
        raise ReleaseError(
            f"unit directive {key} is not supported", EXIT_MIGRATION
        )
    return value
```

| Case | Position | Outcome |
|---|---|---|
| `RuntimeDirectoryMode=0700` | unknown, brand-free | preserved byte-for-byte; installs via `read_migration_observation` |
| `Environment=FOO=bar` | unknown, brand-free | preserved, idempotent |
| `UnknownDirective=value` | unknown, brand-free | preserved, idempotent |
| `UnknownDirective=framenest-x` | value | refused exit 27, `unit directive UnknownDirective is not supported` |
| `Environment=FRAMENEST_X=1` | value (upper case) | refused exit 27, same message |
| `UnknownDirective=fraMeNest-x` | value (mixed case) | refused exit 27, same message |
| `FramenestMarker=value` | key | refused exit 27, `unit directive FramenestMarker is not supported` |
| `Environment=FRAMENEST_FOO=bar` | value | refused exit 27 (preflight: via `read_migration_observation`) |

Case-insensitivity is exercised in both positions (mixed-case value and mixed-case key); no brand-bearing unknown passes. Supported directives are untouched: the `User`/`Group`, `LoadCredential`, `Exec*` and path-directive branches are byte-unchanged (`git diff` shows no edits inside them), and the retention/full suites confirm the whole existing matrix.

#### 3. Every adjusted existing test line

`tests/contract/test_kronika_identity_migration.py`:

| Line | Adjusted | Why this is the intended contract, not a weakened assertion |
|---|---|---|
| 2974 | `runner.dropin_raw = "[Service]\nEnvironment=FOO=bar\n"` → `"[Service]\nEnvironment=FRAMENEST_FOO=bar\n"` | `test_preflight_refuses_an_unknown_dropin_directive` still asserts the same `pytest.raises(engine.ReleaseError)`, the same exit 27 and the same message substring, at the same observation level. The brand-free form it used moved to the preservation contract (asserted at 3499 and through `read_migration_observation` at 3514); the fixture now carries the spelling so the *refusal* half of the policy stays pinned. |
| 3141 | `"[Service]\nEnvironment=FOO=bar\n",` → `"[Service]\nEnvironment=FRAMENEST_FOO=bar\n",` | Same slot in the `test_structural_dropin_transformation_refuses_unknown_forms` loop; the entry count (6), the `pytest.raises` and the exit-27 assertion are unchanged. |
| 3144 | `"[Service]\nUnknownDirective=value\n",` → `"[Service]\nUnknownDirective=framenest-x\n",` | Same slot; the brand-free form is preserved now, so the refusal loop keeps a genuine unknown-directive refusal instead. |

No other existing test line moved. The remaining four loop entries (`LoadCredential` malformed, relative `ExecStart`, non-directive line, continued directive) are byte-unmoved.

#### 4. Mutation demonstrations

Both mutations were applied in-source, observed, restored; the working diff sha256 returned to `fadc20f485ec50ae21038ffa34be28d020d7a933135af1bb4d179bae3943a15e` after each, and the commit contains the restored source.

| Mutated name | Mutation | Observed failure |
|---|---|---|
| `remove-brand-check` | condition forced false (`if False and (...)`) | `3 failed, 204 passed` — `test_preflight_refuses_an_unknown_dropin_directive`, `test_structural_dropin_transformation_refuses_unknown_forms`, `test_structural_dropin_refuses_brand_bearing_unknown_directives`; isolated signature `Failed: DID NOT RAISE ReleaseError` (test file :3508). A brand-bearing unknown would silently install. |
| `force-unknown-refusal` | condition forced true (`if True:`) | `3 failed, 204 passed` — `test_structural_dropin_preserves_brand_free_unknown_directives`, `test_preflight_installs_a_brand_free_runtime_directory_mode_dropin`, `test_structural_dropin_transforms_a_mixed_unknown_and_supported_dropin`; signature `ReleaseError: unit directive RuntimeDirectoryMode is not supported` (engine :4426). |

No mutation survived.

#### 5. Counts and elapsed times

| Run | Result | Elapsed |
|---|---|---|
| Focused `tests/contract/test_kronika_identity_migration.py` (post-edit) | **207 passed, 0 failed** | 0.80 s |
| Full declared Python suite (`--operation test`) | **4877 passed, 8 skipped, 3 warnings, 0 failed** | 689.61 s |
| `tests/contract/test_kronika_identity_retention.py` (final) | **15 passed, 0 failed** | 0.35 s |
| Terminal focused + retention at the commit | 222 passed | 1.20 s |

Difference from the `4873/8/3/0` baseline: **+4 passed**, exactly the four new test functions; skips, warnings and failures unchanged. Focused module difference: 203 → 207 (+4). Mutation runs: `3 failed, 204 passed` each.

#### 6. Commit, Part A, Part B, Part C

```text
 deploy/ubuntu/kronika_release.py                  | 27 ++++++---
 tests/contract/test_kronika_identity_migration.py | 74 ++++++++++++++++++++++-
 tests/contract/test_kronika_identity_retention.py | 34 +++++++++--
 3 files changed, 121 insertions(+), 14 deletions(-)
```

Commit: `980041cf13dd427e77263f573694aed7c1a54018`, parent `78cba281960e2f17137647bcc90aab83847a1c0c`, one local non-amended commit, working tree clean, no push.

Part A is byte-unmoved: `FROZEN_DOCUMENT_SHA256` = 86 keys, `FROZEN_ALEMBIC_SHA256` = **36** keys (both counted from the dict at report time), the four frozen-hash tests passed in every retention run, and the commit touches no frozen document or Alembic path. Part B still measures **20**: `EXPECTED_FRAMENEST_BASENAME_PATHS` counted = 20 and its ledger test passed.

Part C movement, measured by the ledger's own counting code before any pin edit, then pinned from that measurement only:

| Scalar | Pinned before | Measured | Cause (all new lines in `test_kronika_identity_migration.py` unless stated) |
|---|---|---|---|
| `PER_TREE…["tests"]` | 2275 | **2283** (+8) | adjusted preflight fixture `FRAMENEST_FOO` (1), adjusted loop `FRAMENEST_FOO` (1), adjusted loop `framenest-x` (1), matrix `framenest-x` (1), matrix `FRAMENEST_X` (1), matrix key-bearing entry (2: expected key + fixture), matrix mixed-case value (1) |
| `PER_TREE…["deploy"]` | 246 | **248** (+2) | the new key/value brand checks, one literal each, in `kronika_release.py` |
| `ENV_PREFIX_TOKEN_COUNT` | 699 | **702** (+3) | `FRAMENEST_FOO` ×2, `FRAMENEST_X` ×1 |
| `ENV_PREFIX_DISTINCT_NAME_COUNT` | 112 | **114** (+2) | both names are new to this count |

Everything else unmoved by direct measurement: host paths 231/88/128/31/26; unit accounts 9/9; bare prefix 53; capitalized 2773/399; mutation header 73/30; console scripts 14; content-path membership added=[] removed=[]; per-tree file counts unchanged. The diff's spelling-hit inventory is complete: 10 added occurrences total (8 tests, 2 deploy), nothing truncated.

#### 7. Sites and derived branches not named by the prompt

All five branches of `transform_unit_dropin_text`, every branch of `_systemd_transform_value` (both identity refusal forms, `LoadCredential` malformed/near-miss/moved/frozen/foreign, revision and plain `Exec*` incl. unprovable-render refusals, path-list refusals, the new unknown triple) were re-derived by parsing the committed functions. The new branch's three outcomes are all exercised. Boundary findings:

- **Blank-line preservation** (`:4450` first clause) and **semicolon-comment preservation** (third clause) have no committed fixture in this module; both are pre-existing, unchanged branches (no `\n\n` or `\n;` fixture exists).
- **Both key and value brand-bearing** short-circuits to the key refusal; no distinct outcome, no fixture.
- **Case-variant spelling of a supported directive name** (e.g. `user=kronika`): not in the supported sets, brand-free → now preserved by the new `return value`. This is the specified policy's derived consequence, not a separate branch; no fixture names it.
- **Escaped spelling in an unknown value** (e.g. `Environment=FOO=fra\x6denest`): the check is the specified literal substring test, so this is preserved; reported below as a boundary, not a deviation.
- **`read_migration_observation` for unknown forms other than `RuntimeDirectoryMode`**: asserted at transform level only.

No moved or removed site is without a test; no inventory was truncated.

#### 8. Deviations, risks, missing evidence, one smallest next step

No deviation from the grant. The observed live host set (`LoadCredential`, `ReadWritePaths`, plain `RuntimeDirectoryMode=0700`) now transforms cleanly with no further unknown-directive stop expected from it. Risks/limits: the brand check is textual, so an escaped spelling in an unknown value is preserved (LEAD below); blank/semicolon fixtures remain a pre-existing gap; there is no live systemd interpretation and no host contact in this cut, by design; public branch state not directly observed (local remote-tracking ref only). Smallest next step: a fresh independent re-audit of `980041cf13dd427e77263f573694aed7c1a54018`; only after its PASS may the C6-H preflight be re-run.

#### Resolved Execution Issues / Near-Misses

1. Cleanup: removal of `/tmp/opencode/ksi38/` (three synthetic probe files: `probe_c6unk_levels.py`, `probe_c6unk_retention.py`, `probe_c6unk_parta.py`, 211 lines total) was attempted with the exact owned path and denied by the execution environment, as in session 37. The state is retained and reported: synthetic fixtures only, no secrets, no credential, no project state.
2. Measurement-before-pin discipline caught an arithmetic near-miss: draft hand arithmetic for the `tests` tree was +7, but the measurement run (and its ledger comment enumeration) showed +8 because the key-bearing matrix entry names the spelling twice on one line. The pin was set from the measurement only, never from hand arithmetic.
3. Mutation restoration was verified by working-diff sha256 equality (`fadc20f4…`), not by assumption.

#### Pre-Existing Failure Classification

none. No repository test failed in any baseline-bound run; the only red runs were the two deliberate in-source mutation demonstrations, each detected and restored.

Authority expiry: this terminal report expires the grant. No further implementation, second commit, push, publication, host contact or later cut is authorized by it.

```text
Orchestration critique:
MEASURED: none
LEAD: The new brand check is the specified literal, case-insensitive substring test on the raw directive key and value, so an unknown directive whose value encodes the spelling with escapes (for example Environment=FOO=fra\x6denest) is preserved rather than refused; whether systemd decodes such a value at runtime is unverified and irrelevant to the observed host set (its only unknown key is plain, brand-free RuntimeDirectoryMode=0700). Cheapest useful check: one synthetic escaped-value transformer probe plus a systemd unit-parser/syntax reading during the re-audit.
```