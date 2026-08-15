# FrameNest implementation evidence repair

## Routing

Persistent role identity: You are the current WORKER instance assigned to WORKER.

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`

Worker session ordinal: `02`

Worker exchange ordinal: `02`

Worker session target: `current-worker-session`

Continuity anchor: Worker 02 exchange 01 implementation report for commit `2d995bb98a8b2c96fa1925f06403b3ee156c6237`.

Native planning mode: `not-used`

Worker session profile: Diagnostic Worker performing implementation-evidence repair.

Recommended model: keep the current model and role.

Recommended reasoning: `medium`; this is a bounded deterministic environment/provenance check, not a new design or implementation task.

Automatic model selection: off.

Sub-agents/internal delegation: not-used.

Worker topology: single-active.

## Reconciliation already made by the Orchestrator

The exchange 01 report is **not accepted as implementation-PASS**. Its current reconciled status is `implementation-PARTIAL` because the mandatory full Python gate exited non-zero with 81 failures.

The absence of a worktree-local `.venv` does not by itself prove that all 81 failures are pre-existing environment defects. Do not repeat that classification without exact admissible evidence.

The candidate commit and its focused passing evidence remain valid inputs. Do not reimplement the feature and do not generate more tests in this exchange.

## Goal

Move the exact candidate commit into the Cooperator-authorized canonical FrameNest checkout, use the existing canonical Poetry-owned `.venv` without changing it, and rerun the exact-source implementation gates. Produce either:

1. an honest `implementation-PASS` with a zero-exit full Python gate; or
2. an honest `implementation-PARTIAL`/`BLOCKED` report naming the exact first causal failure.

## Repository identities and paths

Canonical repository: `/home/agile/Projects/framenest`

Contained implementation clone: `/home/agile/Projects/framenest-worktrees/framenest-repeatable-immutable-nuc-release-deployment-contract-w2`

Repository identity: `https://github.com/cisarik/framenest.git`

Authorized baseline: `4b04b86e4ea52c673c41624e3f2abe1e59d45907`

Candidate commit: `2d995bb98a8b2c96fa1925f06403b3ee156c6237`

Candidate branch: `feat/repeatable-immutable-nuc-release-deployment-contract`

Required AP pin: `17b7e085139e9bcbb0e4953d26aef9b6687d541c`

Canonical interpreter: `/home/agile/Projects/framenest/.venv/bin/python`

## Mandatory reading

Read only what is needed for this repair:

- `/home/agile/Projects/framenest/AGENTS.md`
- `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
- `/home/agile/Projects/framenest/.ap/AP.md`
- `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
- the exchange 01 terminal report and the candidate commit summary/diff

Do not reopen product design or implementation planning.

## Authority

You may:

- inspect both repositories and the exact candidate commit;
- perform bounded local Git writes needed to fetch the exact candidate branch from the contained clone into the canonical repository and switch the canonical checkout to that branch;
- use the existing canonical `.venv` and canonical Poetry installation exactly as already configured;
- run provenance, AP, focused, affected, and full Python test gates;
- write temporary test output only below a fresh exact `/tmp` directory;
- leave the canonical checkout on the exact candidate branch after successful verification.

You may not:

- edit source, tests, documentation, `.ap`, `ap.project.conf`, dependency files, or the candidate commit;
- create, delete, reconstruct, move, copy, or symlink any `.venv`;
- run `uv`, `pip install`, `poetry install`, `poetry env use`, or any dependency repair;
- use `git reset`, `git clean`, stash, force, amend, rebase, merge, push, or delete branches/files;
- touch or remove existing untracked Cooperator files;
- use SSH, NUC, sudo, systemd, Tailscale, Mullvad, provider APIs, credentials, or secrets;
- archive this prompt or a report into Meta during this exchange.

No publication, deployment, production, or logical-whole closure authority is granted.

## Mandatory preflight

1. Confirm both repository identities and that the contained clone resolves the candidate branch and candidate commit exactly.
2. Record the canonical checkout's initial branch, HEAD, AP pin, and complete status.
3. Require zero tracked changes and no active Git operation in the canonical checkout. Preserve all untracked paths. If any candidate path would collide with an untracked path, stop without switching.
4. Fetch the exact candidate branch from the contained clone into the canonical repository without force. If an existing local branch differs, stop; do not overwrite it.
5. Switch the canonical checkout to the exact candidate branch and require `HEAD == 2d995bb98a8b2c96fa1925f06403b3ee156c6237`.
6. Require the superproject and `.ap` tracked state to be clean and the `.ap` pin/HEAD to equal `17b7e085139e9bcbb0e4953d26aef9b6687d541c`.
7. Require the existing canonical interpreter to report Python 3.13.x. Do not repair it.

If any mandatory preflight fails, stop and report the exact blocker.

## Exact-source provenance gate

From `/home/agile/Projects/framenest`, use the canonical interpreter and verify that importing `framenest` resolves under:

`/home/agile/Projects/framenest/src/framenest/`

Also verify the console-script directory expected by the previously failing tests exists under the canonical `.venv`. This is observation only; do not install or regenerate scripts.

## Validation

Run from `/home/agile/Projects/framenest` with a tool timeout long enough for completion. Do not pipe a primary gate through `tail` or `grep`; preserve the real exit code and pytest summary.

1. AP/project readiness gate required by the candidate repository contract.
2. Focused candidate tests:
   - `tests/contract/test_nuc_release_source_contract.py`
   - `tests/contract/test_nuc_release_remote_contract.py`
   - `tests/contract/test_nuc_release_docs.py`
3. Affected existing tests named in exchange 01:
   - `tests/contract/test_nuc_operator_runbook.py`
   - `tests/contract/test_production_ai_deployment.py`
   - `tests/contract/test_fedora_systemd_service.py`
   - `tests/contract/test_ap_project_contract.py`
4. Full Python suite using the canonical interpreter:

```text
/home/agile/Projects/framenest/.venv/bin/python -m pytest tests -q -p no:cacheprovider
```

The full gate must finish and exit zero for `implementation-PASS`. A timeout, traceback, missing console script, or any non-zero result blocks PASS.

Do not rerun the whole suite repeatedly. One complete run is enough. If it fails, use only bounded diagnostics needed to identify the first causal class.

## Failure classification

- Candidate defect: name the exact failed node(s) and causal relation; do not fix in this exchange.
- Harness defect: name the exact conflicting repository contracts; do not edit the harness.
- Environment defect: name the exact missing/broken environment fact and the gate it prevents; do not reconstruct `.venv`.
- Pre-existing failure: do not claim this merely because a candidate worktree lacks `.venv`. It requires an exact baseline comparison with the same invocation and matching failure identity/signature. Such a comparison may be performed only if bounded and necessary after a candidate failure; it still does not turn a mandatory non-zero candidate gate into PASS.

## Terminal result

Return exactly one terminal report beginning:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo the logical whole, Worker session `02`, exchange `02`, standard terminal status, phase-qualified result, exact commit, exact gate exits and summaries, import provenance, canonical initial/final branch and HEAD, changed paths (expected: none in this exchange), deviations, and authority expiry.

Use:

- `PASS` / `implementation-PASS` only if every mandatory gate, including the full Python suite, exits zero; or
- `BLOCKED` / `implementation-PARTIAL` otherwise.

Do not claim publication readiness, deployment readiness, independent audit, NUC success, or logical-whole closure.
