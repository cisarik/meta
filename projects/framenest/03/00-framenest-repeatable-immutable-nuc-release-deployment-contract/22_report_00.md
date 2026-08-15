### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `22`  
Worker exchange ordinal: `01`  
Worker session target: `fresh-worker-session`  
Worker session profile: Bounded Correction Worker  
Task identity: `FN-NUC-RELEASE-CORRECT-22-F01`  
Finding ID: `FN-NUC-RELEASE-DEPLOY-21-F01`

**PASS** | **implementation-PASS**  
Independent acceptance: **not claimed**  
Logical-whole closure: **not-closed**  
Report justification: **new-mutation**

This chat did not perform Worker 21 deployment. Role is WORKER session 22 exchange 01. No SSH, NUC, sudo, deploy, publication, leftover-lock deletion, unpublished-tree recovery, Meta archival, or logical-whole closure.

**Start SHA:** `43c9849a1ff3449a3c06585571c17439ecff9025`  
**End SHA:** `f5fbdce5669997f15c28ed6ffdad4cda849df4ee`  
**Parent:** `43c9849a1ff3449a3c06585571c17439ecff9025`  
**Git write:** one ordinary non-force commit; no amend, rebase, or push  
**Changed files:**
- `deploy/ubuntu/framenest_release.py`
- `tests/contract/test_nuc_release_source_contract.py`
- `docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md`

`tests/contract/test_nuc_release_remote_contract.py` was on the allowlist and left unchanged: existing nodes already cover FakeRunner order `install < relocate < chmod < rename < framenest-db status`, nested `_remote _remote-relocate-venv-shebangs` parse, top-level `_remote-relocate-venv-shebangs` `SystemExit 2`, and stdin payload count `6`. Public CLI, extract argv, SHA-only status, `--untracked-files=no`, stdin `poetry.toml`/marker writes, runbook, and `pyproject.toml` were not touched.

**Identity gates.** Canonical checkout `/home/agile/Projects/framenest` on `feat/repeatable-immutable-nuc-release-deployment-contract`. Pre-commit `HEAD` `43c9849a1ff3449a3c06585571c17439ecff9025`. `.ap` gitlink and `.ap` `HEAD` `17b7e085139e9bcbb0e4953d26aef9b6687d541c`. Tracked tree was clean before mutation. Owner untracked paths preserved (`.accept-immut-work/`, `.playwright-mcp/`, `.w6-immut-work/`, `REPRO_DIR=/`, `uv.lock`). Canonical interpreter CPython `3.13.9` at `/home/agile/Projects/framenest/.venv/bin/python` under sanitized `env -i`. `.venv` was not reconstructed. `uv` was not invoked.

**Pre-fix evidence (unmodified `43c9849…`, local temp tree, no SSH).** `relocate_venv_shebangs` rewrote `.venv/bin` shebangs only. After the current shebang-only relocate:

- `framenest-db` first line named the final interpreter (`DEPLOY-16-F01` did not recur)
- `framenest.pth` still named `<staging>/src` (`.staging` present)
- `direct_url.json` still recorded `file://<staging>` with `"editable": true` (`.staging` present)

New regression nodes on unmodified `43c9849…`: **3 failed** (`test_relocate_venv_rewrites_editable_pth_and_direct_url`, `test_relocate_venv_fails_closed_when_pth_retains_staging`, `test_relocate_venv_fails_closed_when_direct_url_retains_staging`).

**Correction.** Expanded `_remote-relocate-venv-shebangs` / `relocate_venv_shebangs` to rewrite every text file under `<staging>/.venv/` that embeds the staging prefix, then fail closed if required console scripts still contain `.staging`, if any `.pth` or `direct_url.json` under `.venv` still contains `.staging`, or if `.venv` exists and zero staging-prefix rewrites occurred. Nested private argv unchanged; top-level `_remote-<verb>` remains invalid. Order remains poetry install → relocate → chown/chmod → markers → rename → `framenest-db status` on the final path. ADR-0060 gained one sentence that staging-prefix venv paths (shebangs and editable metadata) are rewritten before the tree is made non-writable.

**Post-fix local reconstruction (temp tree, no SSH).** Shebang, `.pth`, and `direct_url.json` name the final prefix; `.staging` is absent from those files; shebang names `<final>/.venv/bin/python`, not `CPYTHON_BIN`; sibling file without the staging prefix is unchanged. Same three regression nodes after the fix: **3 passed**.

**Focused pytest** (sanitized `env -i`; canonical `.venv` Python 3.13.9; `-p no:cacheprovider`; gate not piped), once:

```text
tests/contract/test_nuc_release_source_contract.py
tests/contract/test_nuc_release_remote_contract.py
tests/contract/test_nuc_release_docs.py
```

**67 passed**, exit **0**. No full suite. No SSH/NUC.

**Host leftover state not touched.** `/run/framenest-release-deploy` and unpublished `/opt/framenest/releases/43c9849a1ff3449a3c06585571c17439ecff9025` were out of scope. This Worker did not SSH, `rm`, deploy, recover, or treat that unpublished tree as a rollback target.

**Next step.** Fresh re-acceptance of commit `f5fbdce5669997f15c28ed6ffdad4cda849df4ee`. This Worker does not issue republication, leftover recovery, or deploy of the new SHA.

**Near-Misses.** None that entered the candidate. Did not invent `poetry install --no-editable`, did not add wheel/pip, did not “fix” opaque `EXIT_TRANSPORT` stderr discard, did not move `framenest-db status` before rename, and did not rename the remote verb.

**Pre-Existing Failure Classification.** Accepted finding `FN-NUC-RELEASE-DEPLOY-21-F01` (editable `.pth` / `direct_url.json` remaining on vanished staging after shebang-only relocate) is the candidate this session corrected. Parked residual: opaque `EXIT_TRANSPORT` mapping that discards `ModuleNotFoundError` stderr. Host leftover lock and unpublished `43c9849…` tree remain later recovery/deploy material. Environment: Worker shell requires `env -i` to clear AppImage `LD_LIBRARY_PATH` / `PYTHONHOME`; that is an environment fact, not a candidate defect.

Authority expires at this terminal report.