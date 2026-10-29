### Report for ORCHESTRATOR_CHAT

Logical whole identity: `kronika-sole-identity`  
Worker session ordinal: `71`  
Worker exchange ordinal: `01`  
Status: **PASS — non-independent implementation evidence**  
Phase-qualified result: `not-applicable`  
Logical-whole closure: `not-closed`  
Report justification: `new-mutation`

Start commit: `f6859362f64cf4b5d5ec7529785d53e1ad483969`  
End commit: **`8c58a81234a97fdf5af9d724a3b526f19745d32a`**  
AP pin unchanged: `73e20ef80b88700d5fcbc397cd8edd4fc425869f`

Created exactly one local non-amended commit on `main`. Working tree and index are clean. No push, publication, NUC contact, browser action, provider call, credential provisioning, or dependency change occurred. Public branch state not directly observed.

#### Content matrix and source reconciliation

Created [docs/UBUNTU_NUC_CLEAN_INSTALL.md](/home/agile/Projects/kronika/docs/UBUNTU_NUC_CLEAN_INSTALL.md).

| Required area | Coverage and reconciled sources |
|---|---|
| 1. Fresh host | Sections 2–6 cover Ubuntu preparation, canonical naming/account/directories, bootstrap tooling and routine updates. Reconciled with deployment phases, `CANONICAL_WEB_LAYOUT`, the web unit and environment template. |
| 2. Frozen exceptions | Section 2 preserves both exact tooling paths, `FNCBE01`, the mount and capture state name. Checked against ADR-0085, helper constants, backup-transfer/off-device constants and capture configuration. |
| 3. Units and installation order | Sections 5, 7 and 8 cover all 10 source units/timers and four credential drop-ins. Ingress follows settings validation and deployment section 11. Tailnet SSH over Wi-Fi reflects the issued operator decision. |
| 4. Media boundaries | Section 4 keeps original media read-only and separates quarantine, publication and staging. Checked against the web unit, environment template and private-storage settings. |
| 5. Release installation/recovery | Section 6 documents the sole helper’s public forms, same-schema boundary and exit-13 continuation. Reconciled with its parser, check/deploy/rollback implementations and deployment annex. |
| 6. Backups | Section 7 covers both schedules, operator roots, retention, restore-readiness and required timer-triggered success. Checked against units, backup constants and the backup runbook. |
| 7. Parked capture | Section 8 covers dependencies, paths, credential source and stopped/default-disabled provisioning. Checked against capture units, template, state resolver and helper transition implementation. |
| 8. Operator notes | Section 9 preserves the private SSH-filename context and single exported user-dotfile source without values. Source: issued prompt and session-25 §2.20. Transport names/options match the helper. |
| 9. Checkpoints/recovery | Nine phase checkpoints and section 10 identify recovery references. The stale Tailscale policy-table route finding is explicitly historical; no route-deletion command is supplied. |
| 10. Instructions versus completion | Sections 1 and 10 explicitly state that this is a future-installation runbook, not an installation or acceptance receipt. |

The document explicitly identifies the helper’s bootstrap prerequisite: it requires an existing canonical release, catalog and restore-ready backup. An empty-host installation cannot be demonstrated through that helper alone.

#### Links and contract pin

Added one link in each required location:

- README Documentation Map.
- Existing deployment runbook.

All **27 relative-link occurrences**, covering 26 distinct targets, resolve.

Extended [tests/contract/test_nuc_release_docs.py](/home/agile/Projects/kronika/tests/contract/test_nuc_release_docs.py) with six tests covering discoverability/links, ten required areas, frozen spellings, complete unit inventory, parsed helper commands, and backup roots/environment parity. Impossible-link and impossible-command controls exercise rejection paths.

#### Measured retention re-pin

Before re-pinning, the retention module produced **4 failures and 11 passes** in 0.38 seconds. Every failure matched the new document’s measured contribution.

| Measure | Before → after | Arithmetic cause |
|---|---:|---|
| `docs` counted files | 84 → 85 | One new runbook |
| `docs` occurrences | 748 → 752 | Two tooling paths + mount + capture state name |
| Content-path membership | 448 → 449 | Only the new runbook added |
| `/opt/framenest` occurrences | 64 → 66 | Two frozen tooling paths |
| Frozen mount occurrences | 13 → 14 | One exception-table entry |

All other Part C measures remain unchanged.

**Part A is byte-unmoved:** both pin maps and assertion bodies match the baseline; all **86 frozen document hashes and 36 Alembic file hashes** match. **Part B remains empty.**

#### Validation

All Python evidence used the exact authorized baseline through AP. `ap doctor`, project check and candidate-source provenance passed.

| Check | Result | Elapsed / baseline difference |
|---|---|---|
| Documentation/deployment selection | 114 passed | 4.68 s |
| Focused documentation module | 35 passed | 0.25 s; six new tests |
| Separate retention module | 15 passed | 0.35 s; unchanged count |
| Full declared Python suite | **4,765 passed, 8 skipped, 3 warnings, 0 failed** | **677.16 s**; +6 passes, unchanged skips/warnings |

The 114-test selection comprised `test_nuc_release_docs.py`, `test_nuc_operator_runbook.py`, `test_fedora_systemd_service.py`, `test_recovery_cli.py`, `test_worker_execution_contract.py`, both catalog timer modules, and `test_kronika_identity_retention.py`.

Ordinary JavaScript invocations exited zero. Node 26’s default output aggregated results by file; supplementary `--test-isolation=none` runs exposed the individual counts:

| JavaScript suite | Passed | Elapsed |
|---|---:|---:|
| `companion_web_bridge` | 23 | 0.027 s |
| `companion_review_extension` | 41 | 0.143 s |
| `x_companion_extension` | 55 | 0.076 s |
| `companion_settings_automatic_analysis` | 6 | 10.031 s |
| `kronika_ui` | 12 | 0.057 s |
| `catalog_card_ai_quick_action` | 30 | 0.176 s |
| Declared bounded glob | 216 | 1.148 s |

These counts match the declared baselines. The additional tailscale diagnostic suite passed 22 tests.

#### Git result

Commit: `8c58a81234a97fdf5af9d724a3b526f19745d32a`  
Subject: `docs: add Ubuntu NUC clean-install and recovery runbook`

```text
 README.md                                         |   1 +
 docs/UBUNTU_NUC_CLEAN_INSTALL.md                  | 408 ++++++++++++++++++++++
 docs/UBUNTU_NUC_DEPLOYMENT.md                     |   3 +
 tests/contract/test_kronika_identity_retention.py |  17 +-
 tests/contract/test_nuc_release_docs.py           | 154 ++++++++
 5 files changed, 579 insertions(+), 4 deletions(-)
```

Verified the exact parent, one-commit range, five-path boundary, unchanged AP pin, and clean final state. Commit used an explicit path list to include the measured ledger re-pin after the single successful staging operation.

#### Statements not exercised by tests

Text pins establish documentation coverage; they do not verify operator history or perform host work.

- Retained live-host identity, the Wi-Fi decision, existing private SSH filename, exported-dotfile source and historical route recovery are supplied operator facts.
- No real OS/toolchain installation, account/directory provisioning, storage permissions, effective host hardening, SSH/Tailscale configuration, deployment, migration, rollback or host recovery was exercised.
- No actual timer-triggered backup, physical off-host durability, restored-host acceptance, capture-browser readiness, login/profile operation or rendered UI/companion acceptance was demonstrated.
- Forbidden-content review was manual, supplemented by the frozen-spelling allowlist test. No installer or generated repository artifact was introduced.

#### Resolved Execution Issues / Near-Misses

- Initial Git staging hit the read-only `.git` boundary; automatic approval review then rejected attachment-derived authorization. Your explicit approval enabled the exact staging and commit.
- The initial full Python run stalled in Starlette/AnyIO’s request bridge and was interrupted, exit 130. A bounded sandbox reproduction ended at exit 137; the same focused test passed outside the sandbox in 1.44 seconds. The unchanged AP full-suite operation then passed outside the sandbox.
- The initial JavaScript summary filter expected TAP output and returned no counts. Direct output identified file aggregation; supplementary isolation-disabled runs supplied the expected individual counts.
- Oversized reads and read-only filename/glob probe errors were corrected through bounded reads and source discovery. Final inventories were regenerated without truncation.

No environment reconstruction or production-code repair occurred.

#### Pre-Existing Failure Classification

None. No failure is claimed to be pre-existing.

#### Deviations, risks, missing evidence and next step

Execution-context and JavaScript-reporting adjustments are recorded above. No implementation-scope deviation remains. Host and rendered acceptance are intentionally absent from this documentation-only cut.

Smallest next step: Orchestrator review of the exact local commit before separately arranging publication, NUC refresh and CLOSE reconciliation.

This terminal report is delivered here only; no report file was written. Worker authority expires upon its submission.

```text
Orchestration critique:
MEASURED: Automatic review rejected the attachment-delivered Git grant; explicit Cooperator approval resolved it. Smallest correction: include exact Git authority directly in the delivery message.
LEAD: none
```