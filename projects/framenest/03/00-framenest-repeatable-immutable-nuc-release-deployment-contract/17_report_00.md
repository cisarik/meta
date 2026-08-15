### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: **17**  
Worker exchange ordinal: **01**

**PASS** | **implementation-PASS**

- Start SHA: `d963df7dfc7d56c75f3696e8bc3830ee81a98534`
- End SHA: `43c9849a1ff3449a3c06585571c17439ecff9025`
- Parent: `d963df7dfc7d56c75f3696e8bc3830ee81a98534`
- Push: none
- Changed files (allowlist only):
  - `deploy/ubuntu/framenest_release.py`
  - `tests/contract/test_nuc_release_remote_contract.py`
  - `tests/contract/test_nuc_release_source_contract.py`
  - `docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md`

Re-gate: HEAD was `d963df7…`; tracked tree clean; `.ap` pin `17b7e085139e9bcbb0e4953d26aef9b6687d541c`; sanitized CPython `3.13.9`. This chat did not perform Worker 16 deployment.

**Pre-fix sequence (unmodified `d963df7…`):** FakeRunner deploy installed on staging, then chown/chmod, markers, rename, then `framenest-db status` on the final path. SSH indices: install `41` → chmod `44` → rename `47` → db status `48`. Zero shebang-rewrite remote commands between install and db status.

**Regressions fail-then-pass:** four new nodes failed on unmodified `d963df7…` (`AttributeError` / missing `_remote-relocate-venv-shebangs`). After the fix, those nodes passed; then the three focused files passed together: **64 passed**.

**Post-fix nested `_remote` argv:** `sudo -n python3 <engine> _remote _remote-relocate-venv-shebangs --staging <staging> --final <final>`. Top-level `_remote-relocate-venv-shebangs` remains parser `SystemExit` 2 (ACCEPT-03-F01 stays closed). FakeRunner order: install `41` < rewrite `43` < chmod `45` < rename `48` < `framenest-db status` `49`. Happy path still writes poetry.toml, markers, rename, and db status; stdin payload count remains **6**.

**Local shebang rewrite (temp tree, no SSH):** `#!<staging>/.venv/bin/python` on `framenest-db` and `framenest-backup` becomes `#!<final>/.venv/bin/python`; `.staging` is absent afterward; a sibling file without the staging prefix is unchanged. Fail-closed if `.venv/bin` exists and zero shebangs are rewritten. Shebangs still name the in-project venv interpreter, not `CPYTHON_BIN`. Deploy still does not run `poetry install` after rename and does not move db-status before rename.

Focused pytest (sanitized env, once):

```text
.venv/bin/python -m pytest -q -p no:cacheprovider \
  tests/contract/test_nuc_release_source_contract.py \
  tests/contract/test_nuc_release_remote_contract.py \
  tests/contract/test_nuc_release_docs.py
```

Result: **64 passed**.

Leftover host state `/run/framenest-release-deploy` and unpublished `/opt/framenest/releases/d963df7…` were **not** touched (no SSH, no rm, no deploy). Opaque `EXIT_TRANSPORT` stderr discard, extract argv, SHA-only status, `--untracked-files=no`, and stdin poetry.toml/marker writes were not changed. Ubuntu runbook was not expanded.

Independent acceptance: **not claimed**.  
Next step: **fresh re-acceptance of commit `43c9849a1ff3449a3c06585571c17439ecff9025`**. This Worker does not republicate, recover the lock/unpublished tree, or deploy the new SHA.

Report justification: **new-mutation**  
Logical-whole closure: **not-closed**

Near-Misses: none in this exchange. Parked residual (opaque `EXIT_TRANSPORT` stderr discard) left untouched as instructed.

Pre-Existing Failure Classification: accepted finding `FN-NUC-RELEASE-DEPLOY-16-F01` (candidate defect: Poetry shebangs baked to staging; post-rename interpreter path gone). Corrected in-engine before chmod; host leftover unpublished tree is not a rollback target and was out of scope.

Authority expires at this terminal report.