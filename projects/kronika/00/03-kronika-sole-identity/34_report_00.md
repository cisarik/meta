### Report for ORCHESTRATOR_CHAT

| Field | Value |
|---|---|
| Logical whole identity | `kronika-sole-identity` |
| Worker session ordinal | `34` |
| Worker exchange ordinal | `01` |
| Task identity | `KSI-AUDIT-C6GUARD` |
| Status | **BLOCKED** |
| Report justification | `new-evidence` |
| Phase-qualified result | `not-applicable` |
| Logical-whole closure | `not-closed` |
| Start and end commit | `cf76f0b3a391663db7f4b0c88b872c08b69ff279` |
| Worker repository changes / commits / pushes | None |
| NUC contact | None |

**The C6 host window is blocked by B1:** newly accepted frozen and foreign paths containing an escaped space are altered by the `Exec*={ path=… }` transformer. The required ordinary-token matrix passes, and the full suite matches **4863 passed / 8 skipped / 3 warnings / 0 failed**, but neither covers this preservation defect.

Escalation disposition: NEEDS_ORCHESTRATOR_DECISION

#### 1. Identity, scope and gates

Independently verified:

- Standalone checkout at `/home/agile/Projects/kronika`, branch `main`.
- Candidate: `cf76f0b3a391663db7f4b0c88b872c08b69ff279`.
- Parent: `b8ec042b5bf1835df77c81341abc75e9cf8ab059`.
- Repository and submodule clean initially and finally; HEAD unchanged.
- Recorded AP gitlink and submodule HEAD both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`.
- `ap doctor`: PASS, governing variant `stable`.
- Baseline-bound project check: PASS.
- Runtime provenance: CPython 3.13.9, importing this checkout’s `src/kronika/__init__.py`.

The candidate changes exactly these three paths:

| Path | Change |
|---|---|
| `deploy/ubuntu/kronika_release.py` | Classifier and four directive guards |
| `tests/contract/test_kronika_identity_migration.py` | Classification tests |
| `tests/contract/test_kronika_identity_retention.py` | Derived retention counts |

Diff: **283 insertions, 19 deletions**. No other path changed.

Source and AST comparison confirm:

- Classification order is **frozen → moved → near-miss → foreign**.
- `MIGRATION_FROZEN_PATH_PREFIXES`, `MIGRATION_OLD_TO_NEW_ROOTS` and `MIGRATION_SEGMENT_RENAMES` are unchanged.
- All existing `ReleaseError` calls, messages and exit-code expressions are unchanged.
- Outside the new classifier and modified `_systemd_transform_value`, the engine’s AST is unchanged.

Local `origin/main` equals the parent. **Public branch state not directly observed**; network inspection was not authorized.

#### 2. Derived guard sites and unchanged sudoers guard

Independent parent-AST inspection found exactly five guards combining unchanged transformed text with a retired-spelling check:

| Site | Parent line | Candidate line | Disposition |
|---|---:|---:|---|
| `LoadCredential` path | 4251 | 4279 | Unified classifier |
| Exec revision-form path | 4271 | 4301 | Unified classifier |
| Exec plain executable | 4287 | 4320 | Unified classifier; arguments excluded |
| Path-list token | 4309 | 4344 | Unified classifier |
| `_transform_sudoers_command` | 4378 | 4416 | Unchanged |

The internal moved-root leftover refusal and the separate identity guards also remain unchanged.

**Sudoers disposition: correctly outside this correction’s scope.** Its explicit observed-export handling remains intact. Independently exercising a synthetic foreign command path against both parent and candidate produced:

`sudo rule command path is not classifiable`, exit **27**.

**Residual host risk:** a foreign retired-spelling sudo command not handled by the observed-export special case can still stop the next preflight. Whether such a command exists on the NUC is unverified.

#### 3. Independent matrix

I constructed new fixtures independently of the correction’s tests. Results below cover ordinary, unescaped tokens through `transform_unit_dropin_text`.

| Case | Path list | LoadCredential | Exec plain | Exec revision |
|---|---:|---:|---:|---:|
| Frozen roots and descendants | 4 PASS | 4 PASS | 4 PASS | 4 PASS |
| Synthetic foreign retired-spelling path | PASS | PASS | PASS | PASS |
| Near-miss: all five roots × `-old`, `x`, `.env` | 15 PASS | 15 PASS | 15 PASS | 15 PASS |
| Moved roots, descendants and renamed segments | 15 PASS | 15 PASS | 15 PASS | 15 PASS |
| Moved-root leftover retired spelling | 5 PASS | 5 PASS | 5 PASS | 5 PASS |

These **160 cases** assert exact output or exact refusal message and exit 27. Successful transformations also pass idempotence checks.

Additional checks passed:

- One mixed path list containing foreign, moved and frozen tokens.
- Six Exec argument-opacity cases across plain/revision forms and unchanged, foreign and moved executables.
- Four foreign `LoadCredential` cases, including three relative forms.

**Additional boundary result:** two escaped-space revision cases fail the preservation contract—one foreign and one frozen. See B1 below.

#### 4. Judgment of the accepted deviations

**Exec argument opacity: acceptable and narrow.** The executable is the classified field. Preserving argument text avoids interpreting arbitrary application data as executable paths. Independent cases confirm that even arguments resembling moved-root near-misses remain unchanged. This deviation itself is non-blocking.

**Relative/foreign `LoadCredential` preservation: acceptable and narrow.** The existing transformer validates the identifier/path structure without requiring an absolute path. Preserving relative foreign values containing the retired spelling makes their treatment consistent with other foreign values. Independent parent/candidate comparisons confirm precisely that change. This deviation itself is non-blocking.

Neither judgment accepts the separate revision-encoding defect.

#### 5. Independent mutation probes

Mutants were constructed by modifying parsed ASTs in memory, using my own tests and fixtures.

| Mutation | Test | Observed outcome |
|---|---|---|
| Replace terminal foreign classification with near-miss | Foreign preservation through all four shapes | All four fail with the corresponding `ReleaseError`, exit 27 |
| Disable the near-miss prefix condition | Near-miss refusal through all four shapes | All four fail: `DID NOT RAISE ReleaseError` |
| Remove the classifier’s frozen loop | Frozen classification assertion | Fails: `expected frozen, observed moved` |

All three mutations were detected.

For the frozen mutation, directive output still remains preserved because `transform_path_value` retains its own frozen-path protection. The classification assertion—not a claimed output failure—kills this mutation.

#### 6. Read-only baseline reconstruction

Loaded the exact parent and candidate engine blobs through `git show`, compiling them into isolated in-memory modules. No checkout or repository edit occurred.

Synthetic input:

```ini
[Service]
ReadWritePaths=/srv/audit34/framenest-foreign
```

| Revision | Result |
|---|---|
| Parent `b8ec042…` | `unit directive ReadWritePaths path is not classifiable`, exit 27 |
| Candidate `cf76f0b…` | Exact input preserved |

This reproduces the original refusal shape and verifies its correction for the ordinary foreign-path case.

#### 7. Checks and retention evidence

All Python execution used AP with the exact candidate baseline.

| Check | Observed result |
|---|---|
| Focused migration module | **193 passed**, 1.00 s |
| Retention module | **15 passed**, 0.35 s |
| Full configured Python suite | **4863 passed, 8 skipped, 3 warnings, 0 failed**, 696.74 s |
| Independent matrix, mutations and structural checks | **184 passed**, 0.92 s |
| Escaped revision characterization | **Two defects reproduced**; both characterization tests passed |

The last row asserts the observed defect; it is **not** a preservation acceptance pass.

Difference from declared full-suite counts `4863/8/3/0`: **none**. Skips comprise seven real-tools cases and one live-NIM case. The three warnings are Pydantic’s non-serializable-default warnings.

The full suite used the authorized `test-focus` operation without a test selector, adding only `-p no:cacheprovider`. It collected all **4871** configured tests while avoiding pytest cache writes.

Independent retention verification established:

- **Part A:** 86 document keys and 36 Alembic keys; mappings unchanged from parent; all file hashes match; corresponding blobs unchanged.
- **Part B:** 20 keys, unchanged from parent and exactly matching tracked retired-spelling basenames.
- Part C checks pass with the candidate’s documented count changes.

#### 8. Findings, disposition and untested scope

**B1 — BLOCKING: revision-form preservation loses path encoding.**

At [the revision return path](/home/agile/Projects/kronika/deploy/ubuntu/kronika_release.py:4296), the engine decodes the captured executable before classification. For frozen and foreign classifications, line 4309 inserts that decoded value back into the serialized command without preserving its encoding.

Reproduced example:

```text
Input:  ExecStart={ path=/srv/audit34/framenest\x20assets ; argv[]=audit34 ; }
Output: ExecStart={ path=/srv/audit34/framenest assets ; argv[]=audit34 ; }
```

Reparsing with the engine’s own executable-path parser demonstrates the changed field:

| Classification | Intended executable | Executable reparsed from output |
|---|---|---|
| Foreign | `/srv/audit34/framenest assets` | `/srv/audit34/framenest` |
| Frozen | `/opt/framenest/tooling/audit34 tool` | `/opt/framenest/tooling/audit34` |

For both exact inputs, the parent refuses with `unit directive ExecStart path is not classifiable`, exit 27. The candidate instead returns altered text.

This is a regression in newly accepted input handling. The underlying decoding assumption predates the correction, but the correction exposes it for these previously refused frozen/foreign tokens. The required preservation property is therefore not established.

**Surviving design assumption:** a decoded executable token can be inserted into revision-form text without retaining or restoring its escaping.

**Non-blocking residual:** the unchanged sudoers refusal described in section 2 remains an operational preflight risk.

**Coverage limits:**

- All four changed guard sites were dynamically exercised; none remains untested as a site.
- Other directive-key aliases sharing those branches were not each independently matrix-tested.
- Unchanged syntax-error branches and other escape forms were not exhaustively probed.
- No live systemd interpretation, host inventory, preflight, deployment or service execution was performed.
- Unrelated C6 production commands were not re-audited.

The blocking conclusion concerns the demonstrated preservation contract, not a claim that the live host contains either synthetic case.

#### 9. Deviations, containment and smallest next step

No correction, repository edit, Git write, publication, host contact, provider call or report-file write occurred.

Command accounting:

- Read-only Git inspection established identity, blobs, diffs, tracked paths and final cleanliness.
- `pwd`, `cat`, `wc`, `rg`, `sed` and `nl` inspected authorized material; they mutated nothing.
- `ap doctor` verified the pinned integration without mutation.
- AP project/runtime/test operations supplied the authorized Python evidence.
- Shell temporary-file creation and cleanup affected only the two authorized synthetic probe directories below; source mutants existed only in memory.

Both directories were removed, and their absence was verified:

- `/dev/shm/kronika-c6guard-34-01.KUBS0a`
- `/dev/shm/kronika-c6guard-34-01-escape.91Tprc`

**Smallest next step:** the Orchestrator escalates B1 to the Cooperator and decides the bounded repair of revision-token preservation. The C6 host window remains blocked. This report grants no further correction or audit cycle.

#### Resolved Execution Issues / Near-Misses

An initial combined document read exceeded the output limit. Required material was subsequently read in bounded sections. No unresolved reading gap or execution-route issue remains.

#### Pre-Existing Failure Classification

None. Repository tests report no failures. B1 is not dismissed as pre-existing: the exact parent refuses the demonstrated inputs, whereas the candidate silently alters their executable fields.

Authority under this prompt expires on submission of this terminal report.

```text
Orchestration critique:
MEASURED: The correction’s preservation evidence covers unescaped revision tokens but misses the existing decoder-to-renderer boundary. Two independent cases demonstrate altered frozen/foreign executable fields. Effect: C6 acceptance is blocked. Smallest correction: preserve serialized frozen/foreign tokens and require an escaped-token regression under separate authority.
LEAD: Whether the NUC contains affected escaped paths or foreign sudo commands remains unknown. Cheapest useful check: targeted inventory during a later authorized preflight, after B1 is resolved.
```