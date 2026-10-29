### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-sole-identity
Worker session ordinal: 35
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-C6ENC — preserve encoding for untransformed revision-form executable tokens
status: PASS
Phase-qualified result: not-applicable
Start commit: cf76f0b3a391663db7f4b0c88b872c08b69ff279
End commit: 78cba281960e2f17137647bcc90aab83847a1c0c
Report justification: new-mutation
Logical-whole closure: not-closed
NUC contact: none

Evidence posture: non-independent correction. Requested reasoning was High. No independent acceptance is claimed. The repository gate matched the prompt: standalone `main`, clean tree, HEAD `cf76f0b3a391663db7f4b0c88b872c08b69ff279`, public `origin/main` `b8ec042b5bf1835df77c81341abc75e9cf8ab059`, `.ap` gitlink and submodule HEAD `73e20ef80b88700d5fcbc397cd8edd4fc425869f`.

Changed files:

- `deploy/ubuntu/kronika_release.py` — revision-form executable tokens keep their encoding.
- `tests/contract/test_kronika_identity_migration.py` — byte-identity, reparse, refusal, and fail-closed fixtures.
- `tests/contract/test_kronika_identity_retention.py` — Part C scalars re-pinned from the measured movement.

Git result: one local non-amended commit on `main`, parent `cf76f0b3a391663db7f4b0c88b872c08b69ff279`. No push. `main` is ahead of `origin/main` by 2. Working tree clean. Persistence: this terminal report only; no report file was written.

#### 1. B1 reproduction before the edit

Reproduced through `ap exec --operation test-focus` against HEAD `cf76f0b`, before any source edit, with a temporary probe outside the repository. The probe was removed before the edit.

Foreign revision token:

```text
Input:  ExecStart={ path=/srv/audit34/framenest\x20assets ; argv[]=audit34 ; }
Output: ExecStart={ path=/srv/audit34/framenest assets ; argv[]=audit34 ; }
```

`UNIT_EXEC_PATH` captured `/srv/audit34/framenest`. `_unescape_unit_text` of that capture is `/srv/audit34/framenest`. The executable the input names is `/srv/audit34/framenest assets`.

Frozen revision token:

```text
Input:  ExecStart={ path=/opt/framenest/tooling/audit34\x20tool ; argv[]=audit34 ; }
Output: ExecStart={ path=/opt/framenest/tooling/audit34 tool ; argv[]=audit34 ; }
```

`UNIT_EXEC_PATH` captured `/opt/framenest/tooling/audit34`. The executable the input names is `/opt/framenest/tooling/audit34 tool`.

#### 2. Repair approach and the derived decode/re-render set

Chosen approach, documented on `_render_moved_revision_token`: classification still uses the decoded path. Frozen and foreign commands are returned unchanged, so the captured token is never decoded and written back. A moved token is rewritten only from its raw text. The moved roots contain no escapes, so the raw token must begin with the literal old root and a literal slash (or be exactly the root). Remainder segments separated by a literal slash are kept byte-for-byte unless the migration renames that segment, in which case the raw segment must itself be literal. The decoded path is never inserted. The caller splices the rendered token at the `UNIT_EXEC_PATH` match span and accepts the command only when that parser captures the rendered token and `_unescape_unit_text` of the capture equals `transform_path_value(decoded)`. Any other raw form raises `unit directive <key> revision path is not provably transformable` with `EXIT_MIGRATION` (27).

`_unescape_unit_text` call sites in the committed engine:

| Site | Role |
|---|---|
| `unit_executables_from_show` | Decodes a `systemctl show` field for reading. Does not write a unit. |
| `parse_web_layout_probe` | Same read-only extraction. |
| `_render_moved_revision_token` segment check | Compares a raw segment with the decoded segment and refuses on mismatch. The decoded segment is not appended. |
| Revision branch, before classification | Decodes the captured token for classification and for `transform_path_value`. |
| Revision reparse guard | Decodes the parser's capture and compares it with the intended path. The decoded text is not inserted. |

Before this repair, the only decode-and-re-render site was the revision return `command.replace(match.group(1), original, 1)`. That statement is removed. Frozen and foreign hit `return command`. Moved text is the raw rendering, not the decoded path.

Branches that do not decode:

- `LoadCredential` classifies and may rewrite the raw path text.
- Plain `Exec*` uses `SYSTEMD_EXEC_TOKEN` on the raw token, then `transform_path_value`.
- Path directives split raw whitespace tokens and classify those bodies.
- `migration_required_console_scripts` reads canonical units through `SYSTEMD_EXEC_TOKEN` and does not rewrite them.
- Environment and sudoers transformation do not call `_unescape_unit_text`.

No other branch had this decode-and-re-render mismatch, so the repair stays inside the revision branch and the new helper. A committed test keeps an escaped foreign token byte-identical through plain `ExecStart`, `ReadWritePaths`, and `LoadCredential`.

#### 3. Byte-identity and reparse evidence

All of these use `transform_unit_dropin_text`, then `UNIT_EXEC_PATH` and `_unescape_unit_text`.

| Case | Result |
|---|---|
| Frozen `\x20` token `/opt/framenest/tooling/audit34\x20tool` | Drop-in unchanged. Capture equals the raw token. Reparse is `/opt/framenest/tooling/audit34 tool`. |
| Foreign `\x20` token `/srv/audit34/framenest\x20assets` | Drop-in unchanged. Capture equals the raw token. Reparse is `/srv/audit34/framenest assets`. |
| Moved token `/var/lib/framenest/catalog\x20data/framenest.env` | Capture is `/var/lib/kronika/catalog\x20data/kronika.env`. Reparse is `/var/lib/kronika/catalog data/kronika.env`. The `\x20` remains in the capture. A second pass is unchanged. |
| Plain moved revision token from the existing under-root matrix | Still rewrites to `/var/lib/kronika/catalog.sqlite3`, and that reparse equals the canonical path. |

Near-miss refusals still raise exit 27 with `unit directive ExecStart path is not classifiable`, for an existing plain revision near-miss and for the escaped form `/opt/framenest\x2dold` (decoded `/opt/framenest-old`). Under-root leftovers still raise exit 27 with `path value under a moved root is not classifiable`, for the existing plain leftover and for `/var/lib/framenest/framenest\x2dstaging`.

Unprovable moved raw forms also fail closed at exit 27 with `unit directive ExecStart revision path is not provably transformable`: an escaped root, an escaped slash in the remainder, and an escaped segment that the migration would rename.

#### 4. Mutation demonstrations

Both mutations were applied to the engine, observed, and restored before the green runs. The commit contains the restored source.

`reinsert-decoded-token`. The frozen/foreign return was changed to `command.replace(raw_token, decoded, 1)`.

- `test_revision_form_preserves_a_frozen_escaped_token` failed: `audit34\x20tool` became `audit34 tool`.
- `test_revision_form_preserves_a_foreign_escaped_token` failed: `framenest\x20assets` became `framenest assets`.
- `test_revision_form_transforms_a_moved_token_with_an_escaped_remainder` also failed, at the idempotence assertion. The first pass still rendered `catalog\x20data`; the second pass treated that canonical token as foreign and decoded it to `catalog data`.
- The plain moved revision test passed.

`emit-decoded-remainder`. Non-renamed remainder segments were appended in decoded form.

- `test_revision_form_transforms_a_moved_token_with_an_escaped_remainder` failed while building the output. The reparse guard raised `ReleaseError: unit directive ExecStart revision path is not provably transformable`.
- The other eight selected revision-form tests passed, including frozen, foreign, plain moved, and the refusal tests.

#### 5. Validation counts

Baseline authorized for comparison: 4863 passed, 8 skipped, 3 warnings, 0 failed.

| Run | Result | Elapsed |
|---|---|---|
| Focused `tests/contract/test_kronika_identity_migration.py` | 203 passed, 0 failed | 0.96 s |
| Full declared Python suite, `test-focus` with no selector, `-p no:cacheprovider` | 4873 passed, 8 skipped, 3 warnings, 0 failed | 756.10 s |
| `tests/contract/test_kronika_identity_retention.py` | 15 passed, 0 failed | 0.42 s |

Difference from `4863/8/3/0`: **+10 passed**. Skips and warnings are unchanged. The ten new tests are the revision-form cases above, including the three parametrized unprovable raw forms and the non-revision preservation test. The previous focused count was 193; 193 + 10 = 203. The eight skips are five cover-workflow real-tool cases, two media-analysis real-tool cases, and one live NVIDIA NIM case. The three warnings are the same Pydantic non-serializable-default warnings.

#### 6. Commit, Part A, Part B, and Part C

```text
 deploy/ubuntu/kronika_release.py                  |  76 ++++++++++++-
 tests/contract/test_kronika_identity_migration.py | 132 ++++++++++++++++++++++
 tests/contract/test_kronika_identity_retention.py |  28 ++++-
 3 files changed, 227 insertions(+), 9 deletions(-)
```

Commit: `78cba281960e2f17137647bcc90aab83847a1c0c`.

Part A is byte-unmoved. The frozen-document and frozen-Alembic hash tests passed both before the re-pin and in the final retention run. `FROZEN_ALEMBIC_SHA256` has 36 keys, counted from the dict. No frozen document or Alembic file was edited.

Part B still measures 20. `EXPECTED_FRAMENEST_BASENAME_PATHS` has 20 entries, counted from the set, and the basename ledger test passed.

Part C movement, measured by the retention assertions before any pin edit:

| Scalar | Pinned before | Measured | Movement |
|---|---|---|---|
| `tests` occurrence count | 2264 | 2275 | +11 |
| `/opt/framenest` | 228 | 231 | +3 |
| `/etc/framenest` | 87 | 88 | +1 |
| `/var/lib/framenest` | 125 | 128 | +3 |

Every other retention test passed on that same pre-pin run, including per-tree file counts, content-path membership, environment-prefix counts, the mutation header, unit-account markers, capitalized `FrameNest`, and the console-script entry count. `deploy` occurrences did not move.

Cause of the +11, all in `test_kronika_identity_migration.py`, none in `kronika_release.py`: frozen escaped token (1), its decoded executable (1), foreign escaped token (1), its decoded executable (1), moved escaped token (2: the root plus `framenest.env`), escaped near-miss (1), escaped under-root leftover (2), escaped-slash remainder (1), escaped renamed segment (1). The host-path movements are the same fixtures that contain those prefixes: three under `/opt/framenest`, one under `/etc/framenest`, three under `/var/lib/framenest`. The foreign fixtures are under `/srv/audit34` and are not keys of the host-path ledger. The pins were updated to the measured values only after that assertion, and the final retention run passed 15.

#### 7. Sites no committed test exercises

- `ExecStartPre`, `ExecStartPost`, `ExecReload`, `ExecStop`, and `ExecStopPost` share the repaired revision branch. The fixtures use `ExecStart`.
- The renderer's `pair is None` refusal is unreachable after classification has already returned `moved`, because that classification requires a root match. No fixture reaches it.
- The per-segment unescape mismatch, after the segment counts already match, has no fixture. An escaped slash fails earlier, on the count check, and that path is tested.
- The reparse guard's refusing branch has no permanent fixture. Its accepting branch is taken by the moved tests. The refusing branch was shown by `emit-decoded-remainder` and then restored.
- The rename keys `framenest` and `framenest.sock` are not separate revision fixtures. `framenest.env` exercises the same rename lookup.

#### 8. Deviations, risks, missing evidence, and one smallest next step

The repair adds a fail-closed outcome for moved revision tokens whose raw form cannot be rewritten provably. Existing near-miss and under-root-leftover messages and exit 27 are unchanged. The moved token is spliced at the parser span rather than by a first-occurrence string replace.

No host contact, migration invocation, publication, or push was performed. There is no live systemd interpretation of the repaired writer.

The reparse guard's refusal path and the five sibling directive names remain fixture gaps, as listed above. The sudoers-command residual recorded for the C6 host window was not re-examined; this cut does not touch sudoers.

Smallest next step: a fresh independent re-audit of `78cba281960e2f17137647bcc90aab83847a1c0c`. The C6-H preflight stays blocked until that re-audit passes.

#### Resolved Execution Issues / Near-Misses

One ambient `python3` process was used to count `framenest` on the uncommitted diff text. It was not test evidence. The retention assertions measured the same deltas (+11, +3, +1, +3) and are the pin source. The counter's temporary file was removed. No residual effect on the commit.

#### Pre-Existing Failure Classification

none

Authority expiry: this terminal report ends the grant. No further implementation, second commit, push, publication, host contact, or later cut is authorized by it.

```text
Orchestration critique:
MEASURED: none
LEAD: Plain exec, path lists, and LoadCredential still classify the raw token, so an escape that would change the decoded classification is outside this repair. Cheapest useful check: one synthetic escaped-slash plain-exec fixture during the re-audit.
```