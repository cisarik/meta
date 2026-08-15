### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `12`  
Worker exchange ordinal: `01`

**PASS** | **implementation-PASS**

This chat did not perform Worker 11 deployment. Role: WORKER session 12, bounded correction only.

**Start HEAD:** `de580f6f9d18cddbc4ad7894d163a361b30ef05f`  
**End SHA:** `d963df7dfc7d56c75f3696e8bc3830ee81a98534`  
**Parent:** `de580f6f9d18cddbc4ad7894d163a361b30ef05f`  
**Branch:** `feat/repeatable-immutable-nuc-release-deployment-contract`  
**Push:** none  
**AP pin:** `17b7e085139e9bcbb0e4953d26aef9b6687d541c`  
**Interpreter:** `/home/agile/Projects/framenest/.venv/bin/python` (CPython 3.13.9, sanitized `env -i`)

**Changed files (allowlist only):**
- `deploy/ubuntu/framenest_release.py`
- `tests/contract/test_nuc_release_remote_contract.py`

**Pre-fix broken `cmd_remote_write_poetry_toml` string (reproduced on unmodified `de580f6f…` before edit):**

```text
sudo -n sh -c 'printf %s '[virtualenvs]
in-project = true
' | cat > /opt/framenest/releases/de580f6f9d18cddbc4ad7894d163a361b30ef05f.staging/poetry.toml'
```

`cmd_remote_write_markers` used the same nested `printf %s` + `shlex.quote` construction inside already single-quoted `sudo -n sh -c '…'`.

**Post-fix builders (payload bytes are not in the command string):**

```text
sudo -n sh -c 'umask 077; cat > /opt/framenest/releases/de580f6f9d18cddbc4ad7894d163a361b30ef05f.staging/poetry.toml'
sudo -n sh -c 'umask 077; cat > …/.framenest-release-manifest.json'
sudo -n sh -c 'umask 077; cat > …/.framenest-release-sha'
```

`_cmd_deploy` now passes `POETRY_TOML.encode("utf-8")`, exact manifest JSON bytes, and `release_sha + "\n"` as `input_bytes`. Local reconstruction (`sh -c` of the `umask 077; cat > path` script with captured stdin) wrote exact `POETRY_TOML` bytes, exact manifest JSON, and SHA file with trailing newline (`poetry_bytes_match True`, `manifest_match True`, `sha_match True`).

**Regressions (fail then pass):**
- On unmodified `de580f6f…`: `test_cmd_remote_write_poetry_toml_uses_stdin_not_nested_quotes` failed (`in-project` embedded in the command). `test_cmd_remote_write_markers_uses_stdin_not_nested_quotes` failed (`TypeError`: still required payload arguments).
- After the fix: both pass. Happy-path FakeRunner deploy still reaches poetry.toml and marker writes; stdin payload count is 6 (engine, two archives, poetry.toml, manifest, SHA).

**Focused pytest (once, sanitized, no pipe of gates):**  
`tests/contract/test_nuc_release_source_contract.py`  
`tests/contract/test_nuc_release_remote_contract.py`  
`tests/contract/test_nuc_release_docs.py`  
**61 passed**, exit 0.

**Host leftover state:** not touched. No SSH, no NUC, no `rm` of `/run/framenest-release-deploy` or `de580f6f….staging`. No deploy, no publication, no Meta archival.

**Independent acceptance:** not claimed.  
**Next step:** fresh re-acceptance of commit `d963df7dfc7d56c75f3696e8bc3830ee81a98534`, then republication, then bounded lock/staging recovery plus deploy (this Worker does none of those).

**Logical-whole closure:** not-closed

**Near-Misses:** none. `cmd_remote_write_file` was left unchanged; a small `cmd_remote_cat_stdin` helper was added so poetry.toml and marker builders share the proven stdin/`cat` pattern without altering the hashed engine/archive transfer.

**Pre-Existing Failure Classification:** parked residual `EXIT_TRANSPORT` stderr discard was not touched (out of scope). Host leftover lock/staging remains an operational recovery item for a later authorized exchange.

**Authority expiry:** this terminal report expires Worker 12 exchange 01 authority.