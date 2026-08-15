### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `28`  
Worker exchange ordinal: `01`  
Worker session target: `fresh-worker-session`  
Worker session profile: combined test-NUC recovery/correction/deployment  
Phase: exceptional combined recovery + correction + publication + deployment  
Task identity: `FN-NUC-RELEASE-RECOVER-CORRECT-DEPLOY-28`

**PASS** | recovery + correction + publication + one successful deploy  
production-acceptance-PASS / Gate E / logical-whole closure: **not claimed** (non-independent)

Role: WORKER session 28 exchange 01. One continuous session. No subagents. No Meta write.

**Standard terminal status:** PASS  
**Phase-qualified result:** Worker 27 leftovers recovered; helper corrected; public `main` fast-forwarded; corrected SHA deployed once; live test NUC is current, healthy, restore-ready, and free of staging-path contamination.

**First causal failure of Worker 27.** Pre-cutover target readiness. The helper invoked `framenest-production check-database-ready` with only `FRAMENEST_ENV_FILE` set. That binary calls `load_settings(env_file=None)` and ignores the file selector, so it inspected the default non-production tempfile database and returned sanitized `FRAMENEST_DATABASE_NOT_READY` (exit 4). The same invocation’s `check-health` returned `FRAMENEST_HEALTH_CHECK_FAILED` (exit 5) against default TCP rather than the live UDS. Failure-window journal (20:29:40–20:30:35 UTC) was empty; `ExecMainStartTimestamp` stayed `2026-08-15 09:13:30 UTC`; `NRestarts=0`; restart never ran. Automatic rollback then hit the same production-CLI gate on `148b6c…` and reported `EXIT_ROLLBACK` 18. `framenest-db status` on both trees was already `at_head` `0028`/`0028`. `/opt/framenest/current.next` was absent and not causal. Live service remained `148b6c…` `active`. Re-running the unpublished and live production CLIs via `systemd-run` + unit `EnvironmentFile` both returned `check-database-ready` `ready`/`0028` and `check-health` `ready` (the latter proves CLI/config compatibility with the then-live UDS, not that `f5fbdce…` was serving).

**Correction commit(s).** One initial commit, no retry commit.

- `5abb2adfcd1d5f3391df9c3044b4b81ac1aac923`  
  `fix: load production EnvironmentFile and wait for NUC readiness`  
  Parent: `f5fbdce5669997f15c28ed6ffdad4cda849df4ee` (direct descendant).  
  Local branch `fix/nuc-release-environmentfile-readiness`. Local `main` not touched (`bc15b608cf718f1b7d3bb6461b217865c0e7c022`).  
  Allowlisted paths only. `framenest-production` is now invoked through oneshot `systemd-run` with the unit `EnvironmentFile`; cutover phases are classified; deploy and rollback poll readiness for 30s / 1s and use `EXIT_READINESS_TIMEOUT` on deadline.

**Public TARGET_SHA readback.**  
`git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` = `5abb2adfcd1d5f3391df9c3044b4b81ac1aac923	refs/heads/main`. Ordinary non-force fast-forward `f5fbdce…` → `5abb2ad…`. AP pin unchanged: `17b7e085139e9bcbb0e4953d26aef9b6687d541c`.

**Focused verification counts.**  
`pytest` 74 passed (`test_nuc_release_source_contract.py`, `test_nuc_release_remote_contract.py`, `test_nuc_release_docs.py`, `-q -p no:cacheprovider`). `py_compile` of `deploy/ubuntu/framenest_release.py` OK. `fish -n deploy/ubuntu/framenest-release` exit 0. No full suite.

**Exact recovered paths.** After proving live current still `148b6c…`, service `active`, and `f5fbdce…` not current:

- `/run/framenest-release-deploy/framenest_release.py`
- `/run/framenest-release-deploy/superproject.tar`
- `/run/framenest-release-deploy/ap.tar`
- `/run/framenest-release-deploy/previous-release`
- `/run/framenest-release-deploy` (`rmdir`)
- `/opt/framenest/releases/f5fbdce5669997f15c28ed6ffdad4cda849df4ee`

`/opt/framenest/current.next` was already absent (not deleted). No glob. No lock-dir `rm -rf`. Afterward all of the above absent; live `148b6c…` still present and `active` until cutover.

**Pre/post live release identity.**

| | SHA | path |
|---|---|---|
| Pre | `148b6c2012809944262399c1a166e85082606fbf` | `/opt/framenest/releases/148b6c2012809944262399c1a166e85082606fbf` |
| Post | `5abb2adfcd1d5f3391df9c3044b4b81ac1aac923` | `/opt/framenest/releases/5abb2adfcd1d5f3391df9c3044b4b81ac1aac923` |

`/opt/framenest/current` equals the post path. Marker and manifest SHA match `TARGET_SHA`. Manifest `ap_gitlink` = `17b7e085139e9bcbb0e4953d26aef9b6687d541c`. Previous `148b6c…` directory remains. `f5fbdce…` final/staging absent.

**Service/database/backup/health evidence.**  
`ActiveState=active`, `SubState=running`, `Result=success`, `ExecMainStatus=0`, `WorkingDirectory=/opt/framenest/current`. `ExecMainStartTimestamp=2026-08-15 21:15:30 UTC`. `framenest-db status`: `at_head` `0028`/`0028`. Backup `restore_readiness=ready`. Fresh pre-cutover checkpoint `auto-20260815T211522Z-cf3433de` `succeeded` at `2026-08-15T21:15:22Z`. Release-local `check-database-ready` `ready`/`0028`; `check-health` `ready`. Required console-script shebangs name `/opt/framenest/releases/5abb2adfcd1d5f3391df9c3044b4b81ac1aac923/.venv/bin/python`. Live venv `.pth` / `direct_url.json` `.staging` matches: 0. `/run/framenest-release-deploy` and `/opt/framenest/current.next` absent. No migration. No AP-pin change. No dependency change.

**Deploy invocation count.** 1 (`deploy --yes` of `5abb2ad…`, exit 0, `2026-08-15T21:14:53Z`–`21:15:42Z`). No retry.

**Residual risks.** Off-device catalog copy remains unconfigured/disabled (pre-existing). Previous `148b6c…` is still a pre-manifest SHA-only rollback tree. `systemd-run` oneshot is now part of the helper’s production-CLI contract. Canonical checkout `.venv` interpreter is broken under Cursor’s AppImage `LD_LIBRARY_PATH`; tests used the same interpreter with that variable unset (no venv rebuild). Local `main` remains an unrelated non-deployed SHA by instruction.

**Logical-whole closure:** not-closed

**Report justification:** `changed-external-state`

**Authority expiry:** all Worker 28 exchange 01 recovery/correction/publication/deployment authority expires at this terminal report.

**Privilege lifecycle.** `sudo -n true` exit 0 at the initial gate and through deploy. `sudo -K` once after evidence capture, exit 0. Follow-up `sudo -n true` exit 1, 29-byte stderr classified `password-required` without dumping the host line. No password handling. `sudo -v` was not run by this Worker.