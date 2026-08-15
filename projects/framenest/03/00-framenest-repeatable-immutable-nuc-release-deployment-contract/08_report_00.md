### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `08`  
Worker exchange ordinal: `01`  
Standard terminal status: **PASS**  
Phase-qualified result: **implementation-PASS**  
Start commit: `011823a9dcb3d2a51e684fefd5083970f3610701`  
End commit: `de580f6f9d18cddbc4ad7894d163a361b30ef05f`  
Tree: `d958914aeb1952d23d2b6aa7521a92bde14523f2`  
Parent: `011823a9dcb3d2a51e684fefd5083970f3610701`  
Push: none  
Independent acceptance: not claimed  
Publication / production-acceptance-PASS / deployment: not claimed  
Logical-whole closure: not-closed  
Report justification: `bounded-candidate-produced`  
Secrets omitted: yes  
This session did not perform Worker 07 deployment.

**Identity gates.** Canonical checkout `/home/agile/Projects/framenest` on `feat/repeatable-immutable-nuc-release-deployment-contract`; pre-commit `HEAD` `011823a9dcb3d2a51e684fefd5083970f3610701`. `.ap` gitlink and `.ap` `HEAD` `17b7e085139e9bcbb0e4953d26aef9b6687d541c`. Tracked tree was clean before mutation. Owner untracked paths preserved (`.accept-immut-work/`, `.playwright-mcp/`, `.w6-immut-work/`, `REPRO_DIR=/`, `uv.lock`). No active Git operation. Canonical interpreter Python 3.13.9 via sanitized `env -i`. `.venv` was not reconstructed.

**Changed files (allowlist only)**

- `deploy/ubuntu/framenest_release.py`
- `tests/contract/test_nuc_release_remote_contract.py`
- `tests/contract/test_nuc_release_source_contract.py`
- `docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md`

Public CLI unchanged. Nested `_remote _remote-extract` unchanged. New ADR-0060 releases still write both markers. ADR-0060 Status remains `Accepted`. No NUC/SSH/host-marker write.

**F01 pre-fix vs post-fix**

Unmodified `011823a9…`: FakeRunner `status` with missing manifest `cat`/`test -e` and a valid 40-hex SHA file exited **20** (`framenest-release: command failed`). Same setup for `check` also exited **20** before backup-readiness. Missing both markers also printed opaque `command failed`.

After `de580f6f…`: `read_current_release` probes markers with a sudo-success classifier (`manifest` / `sha` / `none`). SHA-only trees succeed; `status` prints `active_release` from that SHA and `release_manifest: absent`; no invented `ap_gitlink` or archive hashes. `check` reaches backup-readiness via `current_path`. Both markers absent, or an invalid SHA, fail closed with a named sanitized error (not opaque `command failed`).

**F02 pre-fix vs post-fix**

Unmodified: `verify_clean_worktrees` treated `??` owner-untracked as dirty (`EXIT_SOURCE_GATE` 3). Tracked ` M AGENTS.md` also failed (correct).

After: `--untracked-files=no` accepts `??` owner-untracked and still rejects ` M AGENTS.md`.

**Regression nodes (fail then pass)**

On unmodified `011823a9…`: 5 failed, 1 passed (`test_verify_clean_worktrees_rejects_dirty_superproject` already passed).  
After the edit: 6 passed.

**Focused pytest** (sanitized `env -i`; canonical `.venv` Python 3.13.9; `-p no:cacheprovider`; gate not piped):

```text
tests/contract/test_nuc_release_source_contract.py
tests/contract/test_nuc_release_remote_contract.py
tests/contract/test_nuc_release_docs.py
59 passed in 0.16s
exit 0
```

Full suite, JS/browser suites, SSH, sudo, and NUC contact were not run.

**Git**

Exactly one ordinary non-force commit `de580f6f9d18cddbc4ad7894d163a361b30ef05f`, parent `011823a9dcb3d2a51e684fefd5083970f3610701`, no amend/rebase/push. Tracked tree clean after commit. Owner untracked paths preserved.

**One smallest next step.** Orchestrator should issue a separate fresh Worker full-fresh re-acceptance of `de580f6f9d18cddbc4ad7894d163a361b30ef05f`, then republication, then deploy. This Worker does none of those.

### Resolved Execution Issues / Near-Misses

- Inherited Cursor AppImage `LD_LIBRARY_PATH` / `PYTHONHOME` makes `.venv/bin/python` fail with `No module named 'encodings'` unless cleared. All probes and pytest ran under `env -i` per `docs/WORKER_EXECUTION_CONTRACT.md`. `.venv` was not reconstructed.
- `test_status_missing_both_markers_fails_closed` would have passed on unmodified code if it asserted only non-zero; it asserts a named missing-marker error instead of opaque `command failed`.

### Pre-Existing Failure Classification

Live test-NUC tree `148b6c2…` remains a pre-manifest host fact. This Worker did not contact that host and did not write markers. The candidate helper now observes such a tree via `.framenest-release-sha` only. Cutover of `011823a9…` / this successor is still a later separately authorized deploy after re-acceptance and republication.

Authority expiry: all Worker 08 exchange 01 correction authority expires at this terminal report.