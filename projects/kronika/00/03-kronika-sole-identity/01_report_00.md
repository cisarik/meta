### Report for ORCHESTRATOR_CHAT

Logical whole identity: `kronika-sole-identity`  
Worker session ordinal: `01`  
Worker exchange ordinal: `01`  
Task identity: `KSI-PLAN-01`  
Status: **BLOCKED**  
Phase-qualified result: `not-applicable`  
Logical-whole closure: `not-closed`  
Report justification: `new-evidence`

**The required green Python baseline was not established.** The authorized test operation finished with **3 failed, 4141 passed, 8 skipped, and 3 warnings**. I stopped substantive planning and did not produce or approve a decision-complete cut sequence.

### Repository and authority

Start and end commit: `0c850996cd2ef17dae4112733fd17fdc732f4699`.

- Native planning mode was active.
- The standalone checkout was on `main`, with the expected public repository remote.
- Public `main` matched the expected commit through `git ls-remote`.
- The containing gitlink and submodule HEAD both matched `73e20ef80b88700d5fcbc397cd8edd4fc425869f`. Public AP `main` also matched that pin when checked.
- `ap doctor` passed with governing variant `stable`.
- `ap project check --root /home/agile/Projects/kronika --baseline 0c850996cd2ef17dae4112733fd17fdc732f4699` passed.
- Final repository and submodule status were clean.

Changed files: **none**. No Git writes, dependency changes, NUC contact, provider calls, browser activity, or trace-file writes were performed. Test execution used the authorized routes.

### Validation and blocker

| Validation | Result |
|---|---|
| Python: declared AP `test` operation | **FAIL**, exit 1; 4152 collected; 4141 passed, 3 failed, 8 skipped, 3 warnings; 728.04 seconds |
| JavaScript: `node --test tests/*.test.js` | **PASS**, exit 0; 554 total, 549 passed, 5 skipped |
| Final tracked repository state | Clean; HEAD and AP pin unchanged |

The exact Python invocation was:

`./.ap/ap exec --root /home/agile/Projects/kronika --baseline 0c850996cd2ef17dae4112733fd17fdc732f4699 --operation test`

All three failures were in [test_operator_network_scripts.py](/home/agile/Projects/kronika/tests/contract/test_operator_network_scripts.py:847):

- `test_ssh_gate_rejects_missing_required_values[target]`
- `test_ssh_gate_rejects_missing_required_values[user]`
- `test_ssh_gate_rejects_missing_required_values[identity]`

Each failed at line 870 with **`AssertionError: assert 0 == 2`**. The test expected the Fish gate to reject an omitted required argument; the subprocess returned success. The `[command]` case passed.

The tests remove the four ambient SSH variables from the child environment, but `_run_fish` starts Fish without disabling startup configuration. The gate also deliberately accepts environment defaults. **Fish startup configuration or universal variables are a plausible explanation, not a verified cause.** I did not inspect personal Fish configuration, identity files, or credentials, and did not repair the harness or gate.

The Python skips were seven opt-in real-media-tool tests and one live NVIDIA test. The five JavaScript browser-evidence tests remained gated. No rendered or live-provider acceptance is claimed.

The stop follows the mandatory non-zero validation rule in [WORKER_EXECUTION_CONTRACT.md](/home/agile/Projects/kronika/docs/WORKER_EXECUTION_CONTRACT.md:281) and the failed-prerequisite boundary in [AP.md §18](/home/agile/Projects/kronika/.ap/AP.md:2940). The already-running suite was allowed to finish to preserve its complete result; it was not rerun.

### Re-counted inventory

These measurements cover tracked repository content. Initial ordinary `rg` counts omitted hidden tracked content; `git grep` reconciled the affected totals.

| Identity class | Measured | Difference from issued inventory |
|---|---:|---|
| Python files under `src/framenest` | 284 | None |
| Files containing case-insensitive `framenest`: src / tests / deploy / scripts / docs / extension | 254 / 314 / 19 / 7 / 87 / 12 | None |
| Matching tracked Markdown files | 100 | None; this includes nested Markdown |
| Distribution name / AP provenance module | `framenest` / `framenest` | None |
| `framenest-*` script entries | **14 total: 13 application commands plus the capture alias** | Issued table says 14 plus the alias; it double-counts one entry |
| `FRAMENEST_` tokens / distinct names | 639 / 103 | None |
| Exact-case `X-FrameNest-Request` occurrences / files | **53 / 28** | File count is 28, not 27 |
| Exact-case header matches in JavaScript test files / ADR files | **9 / 5** | Issued text says 10 / 8; these measurements use the literal spelling |
| `/opt/framenest` / `/etc/framenest` | 198 / 73 | None |
| `/var/lib/framenest` / `/var/cache/framenest` | 91 / 20 | None |
| `/mnt/framenest-catalog-offdevice` | 12 | None |
| Capitalized `FrameNest` occurrences / files | 3335 / 478 | None |

This is a partial reconnaissance inventory, not a completed classification of every occurrence.

### Material findings preserved for continuation

1. **Moving Alembic files requires historical import support.** Eleven applied revision files import `framenest.infrastructure.persistence.sqlite_batch_fk`. Moving the directory and changing `DEFAULT_MIGRATION_PACKAGE` alone would break loading that history. The eventual design must preserve applied bytes and cover both fresh-database migration and loading an existing `0035` database. No adapter design or new revision is approved by this report.

2. **Capture and web share the old `/opt` hierarchy.** The capture bridge and runner unit sources use `/opt/framenest/capture-current`. The release helper also resolves capture releases beneath `/opt/framenest/releases`. A web path migration therefore needs explicit capture-path continuity; the existing `activate-capture` operation restarts the runner and cannot be used as an incidental rename step.

3. **Settings consumers extend beyond `FrameNestSettings`.** AI configuration, backup operations, off-device configuration, the development launcher, deployment helpers, and operator scripts read `FRAMENEST_` names separately. Prefix compatibility confined to `configuration.py` would be incomplete.

4. **The header is only one companion compatibility boundary.** The repository also contains branded companion protocol identifiers, message sources, connection names, globals, and browser recovery/storage keys. Their transition must preserve the existing installed extension and open browser contexts until the Cooperator-visible update step.

5. **Backup and recovery identifiers are durable contracts.** Backup verification currently requires `application.name == "framenest"`. Sidecars, workstation stores, off-device markers, and snapshot metadata also contain branded identifiers. New writers cannot change these before the corresponding readers and rollback path understand them. Existing archives must remain unchanged.

6. **AP contract migration requires an explicit trust handoff.** The pinned AP executable rejects `ap exec` when the working `ap.project.conf` differs from the authorized baseline. `--candidate` provides readiness evidence only. It cannot authorize execution against a newly renamed provenance module.

7. **Release preparation already creates a release-local environment.** The helper installs through pinned Poetry into staging and relocates staging paths in scripts and installation metadata. Its relocation checks currently require `framenest-db` and `framenest-backup`; its operational commands require the old production executable. These checks must change together with packaging and installed-unit compatibility.

8. **Historical and living documents are mixed.** The ADR index currently ends at `0084`, making `0085` the next available number at this baseline. Several living documents contain dated historical paragraphs, while documents such as the Fedora service guide explicitly retain historical evidence. A blanket filename or text replacement is insufficient.

The NUC migration remains the highest-risk prospective cut: account identity, absolute interpreter paths, release environments, credentials’ source paths, service units, persistent state, socket ingress, and rollback are coupled. Repository inspection does not prove the installed host’s current readiness.

### Incomplete deliverables and decision boundary

The full cut sequence, exact ADR text, compatibility-removal gates, per-cut mutations and rollback, answers to all thirteen planning questions, and total effort estimate **remain incomplete**. Required reading was not completed after the baseline failure. No partial outline is presented as an implementation-ready plan.

The issued identity direction remains accepted. This report does not reopen ADR-0082’s supersession decision or authorize changes to the carried residuals.

### Pre-Existing Failure Classification

- **Pre-existing claim:** asserted for the three named test failures.
- **Comparison baseline commit:** `0c850996cd2ef17dae4112733fd17fdc732f4699`.
- **Baseline predates:** `whole-logical-whole`.
- **Test identity:** the three parameterized cases listed above.
- **Failure signature:** expected exit 2; observed exit 0 at line 870.
- **Topically related to touched behavior:** yes, to the proposed operator-script and environment-prefix transition; no candidate was created.
- **Superseded by accepted authority:** none.
- **Regression exclusion evidence:** tests ran against the unchanged baseline; final tracked trees remained clean.
- **Causal classification:** baseline test failure; harness versus environment cause remains unverified.
- **Closure impact:** `blocks-closure`; not explicitly parked.

### Resolved Execution Issues / Near-Misses

- Initial inspection used read-only `git ls-tree` and `git remote -v`, which were outside the prompt’s enumerated Git-command list. They caused no mutation. Subsequent inspection used permitted forms.
- Some guessed paths did not exist, and oversized reads were truncated. Missing paths were resolved through repository searches where needed; incomplete reads are not claimed as completed.
- AP reported sanitizing inherited environment classes. The canonical project check succeeded; this is not evidence of a broken Python environment.

### Smallest next step

Issue one bounded diagnostic grant for the three failing Fish-gate test cases, using synthetic tools and the canonical AP route, with no NUC contact or personal configuration inspection. Establish the cause and disposition before authorizing completion of this planning question.

This terminal report is delivered in-session only. The Orchestrator owns storage as `01_report_00.md`. **Planning authority expires on submission; implementation in this session remains prohibited.**

Orchestration critique:  
MEASURED: The required baseline suite is red at the exact authorized commit: three missing-argument Fish-gate cases return 0 instead of 2. This prevents the requested green E2 baseline. Smallest correction: a bounded diagnostic exchange before planning resumes.  
LEAD: Fish startup configuration or universal variables may reintroduce defaults removed from the subprocess environment. Cheapest useful check: an authorized synthetic comparison with Fish startup configuration isolated, without reading or printing personal values.