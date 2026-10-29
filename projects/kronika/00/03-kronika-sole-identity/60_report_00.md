### Report for ORCHESTRATOR_CHAT

Logical whole identity: `kronika-sole-identity`
Worker session ordinal: `60`
Worker exchange ordinal: `01`
Persistent role identity: `WORKER`
Worker session target: `fresh-worker-session`
Native planning mode: `not-used`
Worker session profile: Fresh Implementation Worker
Task identity: `KSI-IMPL-C8BP`
status: **PASS**
Phase-qualified result: `not-applicable`
Start commit: `7c1ea48be1176cd454f0ce6a97dc09d32d543838`
End commit: `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`
Report justification: `new-mutation`
Logical-whole closure: `not-closed`

Gates at start matched the prompt. Branch `main`, HEAD `7c1ea48be1176cd454f0ce6a97dc09d32d543838`, clean tree, local `origin/main` `c0f456656c9930810e11d13e1d4684efdb3ee4ff`. Containing gitlink and `.ap` HEAD both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`. `./.ap/ap doctor` PASS, governing variant `stable`. `./.ap/ap project check --baseline 7c1ea48be1176cd454f0ce6a97dc09d32d543838` PASS. No NUC, browser, or capture action.

Changed files are the eight paths in section 7. Non-obvious modules, named before they were edited: `tests/contract/test_nuc_release_remote_contract.py` (deploy/rollback emit no capture action), `tests/contract/test_nuc_release_docs.py` (the pointer sentence), `tests/unit/chatgpt_page/test_bridge_security.py` (the emitted identity), and `tests/contract/test_kronika_identity_retention.py` (Part C only). No push.

## 1. Identity matrix and frozen state-directory sites

Both emitted labels use `config.APP_NAME`, which is already `kronika-capture`. The package name `kronika_capture` stays the import identity and is not written into the HTTP surface.

| Surface | Result |
|---|---|
| `BridgeRequestHandler.server_version` | `kronika-capture/0.1.0` (`APP_NAME` / `BRIDGE_VERSION`) |
| Observed `Server` header | `kronika-capture/0.1.0 ` — the class value plus the space `version_string` adds because `sys_version` is `""` |
| Health body | `{"ok": true, "api": "kronika-capture", "api_version": 1}` |
| `BRIDGE_VERSION`, `API_VERSION`, `PROTO_VERSION`, `PACK_VERSION` | Unchanged: `"0.1.0"`, `1`, `1`, `5`. This commit does not edit `config.py`. |
| CLI program name | Still `kronika-capture` through `APP_NAME`. Not edited. |

`framenest-chatgpt-page` remains only where it is the frozen state directory:

| Site | Decision |
|---|---|
| `config.STATE_DIR_NAME` | Preserved |
| `paths.py` module docstring and `state_dir` docstring | Preserved; they name that directory |
| `cli.py` `--state-dir` help | Preserved; it names the XDG directory |
| `bridge_client.mjs` `resolveStateDir` | Preserved; it joins that directory name |
| `tests/unit/chatgpt_page/test_projects.py` | Existing resolution pin, not edited |
| `tests/contract/test_local_state_migration.py` | Existing fixture paths, not edited |

Other capture prose, each decided and left:

| Site | Decision |
|---|---|
| `kronika_capture/__init__.py` | "FrameNest-owned" and "FrameNest provider" are module prose. They are not emitted on the bridge or by the CLI. Left. |
| `config.py` and `cli.py` module docstrings | They describe the chatgpt-page ask function, which is still what the program does. Left. |
| `logging.getLogger("kronika.bridge")` | Already canonical. Left. |
| `jobs.hello` | Returns `proto` and `bridge_version`. It has no product `api` label. Left. |

## 2. Activation matrix and README

`activate-capture` and `rollback-capture` both go through `_cmd_capture_transition`. After the existing drain, brake, identity snapshot, and pointer switch, the command restarts `kronika-capture-bridge.service` and then `kronika-capture-runner.service`, once each. Readiness is still one check. A readiness failure does not start the browser again.

| Failure | Message | Exit | What is not done |
|---|---|---|---|
| Bridge restart | `capture bridge restart failed` | `EXIT_READINESS` (readiness class) | Runner is not restarted. Readiness is not polled. Pointers are printed. |
| Runner restart | `capture runner restart failed` | `EXIT_READINESS` | Bridge has restarted once. Readiness is not polled. Pointers are printed. |

`deploy` and `rollback` are pinned to emit no `restart`, `start`, or `stop` of either capture unit, and no `capture-current.next`. The parser help for the two capture commands now says the restart is bridge, then runner. That help text has no direct assertion; the emitted commands do.

`deploy/ubuntu/README.md` now says the pointer is `/opt/kronika/capture-current`. `deploy` and `rollback` do not switch it and do not restart either capture unit. `activate-capture` switches to a reviewed release and restarts bridge, then runner, once. `rollback-capture` switches back under the same checks and the same restart. `migrate-capture-paths` moves the installed release onto that pointer and rewrites unit paths without changing the capture software; it stops runner, then bridge, then starts bridge, then runner. The command examples are unchanged.

## 3. Complete-delta review

Installed capture release markers: `94e605c17b881461fad3e22fd8c7fca32cb93976`.
`git rev-parse 94e605c17b881461fad3e22fd8c7fca32cb93976:src/kronika_capture` is `977465503254fe6cdf31673b7e107b9e0487ffe2`.

Target commit: `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`.
Its capture code tree is `1b193a8b0afd76b8e951970691776fe0203fa360`.

`git diff --name-status 94e605c… HEAD -- src/kronika_capture` is exactly five files, `+160/−31`. No other file in that tree differs. Activating this commit switches `capture-current` onto a release built from it and, with this helper, restarts the bridge and then the runner. It does not install unit files. The process that comes up is this package, not an identity-only or path-only change.

| File | Class | What activation ships |
|---|---|---|
| `_assets/extension/src/headless/driver.mjs` | driver behavior | Startup failures carry a closed diagnostic projection (stage, reason, errno, exit, signal, endpoint, stderr class, cleanup). Stderr is classified only for the named failure wordings. The five-minute brake remains `300000`; expiry is its own reason. A second automatic browser start stays forbidden. |
| `_assets/extension/src/headless/runner.mjs` | runner behavior | A failed startup is still `browser_unavailable` and is now logged. Cleanup failure is reported. There is still no browser restart loop. |
| `cli.py` | CLI behavior | The runner and the login wizard resolve `node` from `PATH`, then `/opt/homebrew/bin` and `/usr/local/bin`. |
| `config.py` | identity | `APP_NAME` changes from `framenest-chatgpt-page` to `kronika-capture`. `STATE_DIR_NAME` and the protocol constants do not change. This file is in the installed-to-target delta and is not in this commit. |
| `bridge/server.py` | identity | This commit. The `Server` header and health `api` label become `kronika-capture`. Version fields stay. |

The release helper's new bridge restart is how this activation must be run. It is not code inside the capture package. An older helper would still restart only the runner.

## 4. Test-quality additions

All six are in `test_apply_preserves_the_release_and_bounds_the_service_cycle`. Removing the production call fails that test.

| Call | Assertion |
|---|---|
| `poetry.toml` existence | The staging `test -e` command occurs once. |
| `poetry.lock` existence | The staging `test -e` command occurs once. |
| `chown -R root:root` | The staging command occurs once, after shebang relocation and before `chmod`. |
| `chmod -R a-w` | The staging command occurs once, after `chown` and before the staging rename. |
| Relocation upload | The engine write command occurs once, its stdin is the helper's own bytes, and it precedes relocation. |
| Post-install `WorkingDirectory` | Bridge and runner are each shown twice: once before `daemon-reload`, once after. |

## 5. Mutation demonstrations

Each edit was restored before the next one. The committed tree is the restored tree.

| Mutation | Observed failure |
|---|---|
| Restore the old `server_version` literal | `test_bridge_identity_is_canonical_and_protocol_values_stay` failed in 0.31s. Expected `kronika-capture/0.1.0`; got `framenest-chatgpt-page/0.1.0`. |
| Drop the bridge restart call | `test_capture_activation_switches_once_and_reports_both_shas` failed in 0.19s. The bridge-restart count was 0, where the test requires 1. |
| Set `STATE_DIR_NAME` to `kronika-capture` | `test_development_default_uses_framenest_state_name` failed in 0.03s. `state_dir()` ended in `kronika-capture`; the test requires `framenest-chatgpt-page`. |

## 6. Suites

Python evidence used `./.ap/ap exec --baseline 7c1ea48be1176cd454f0ce6a97dc09d32d543838`. The full suite was `--operation test` with no trailing argv. JavaScript used `node --test` from the worktree root.

The prompt's five-module `473` has no file list. No five-file subset of the documented nine sums to 473 on the pre-change collection counts, so that set was not reconstructed.

| Suite | Result | Elapsed | Baseline difference |
|---|---|---:|---|
| Nine modules | 625 passed, 0 failed | 22.30 s | 623 + 2 restart tests. The identity test is outside this set. |
| Full Python | 5016 passed, 8 skipped, 3 warnings, 0 failed | 697.49 s | 5013 + 3. The third test is the bridge identity test. Skips, warnings, and failures unchanged. |
| Retention | 15 passed, 0 failed | 0.35 s | Counts match the re-pin below. |
| `companion_web_bridge` | 23 passed, 0 failed | 77.0 ms | None |
| `companion_review_extension` | 41 passed, 0 failed | 181.4 ms | None |
| `x_companion_extension` | 55 passed, 0 failed | 122.6 ms | None |
| `companion_settings_automatic_analysis` | 6 passed, 0 failed | 10.07 s | None |
| `kronika_ui` | 12 passed, 0 failed | 90.5 ms | None |
| `catalog_card_ai_quick_action` | 30 passed, 0 failed | 207.4 ms | None |
| Bounded frontend/cockpit/gallery glob | 212 passed, 0 failed | 750.1 ms | None |

The nine modules are the session-59 set: `test_kronika_capture_services.py`, `test_chatgpt_page_packaging.py`, `test_nuc_release_remote_contract.py`, `test_nuc_release_source_contract.py`, `test_nuc_release_docs.py`, `test_nuc_operator_runbook.py`, `test_kronika_identity_migration.py`, `test_kronika_cli_and_release_readers.py`, `test_kronika_durable_writer_identities.py`.

The eight skips are the five real-tool cover cases, two real-tool media-analysis cases, and one NVIDIA smoke case. The three warnings are the existing Pydantic `OMITTED` schema warning.

## 7. Diff, commit, Part A, Part B, Part C

```text
 deploy/ubuntu/README.md                            |  15 ++-
 deploy/ubuntu/kronika_release.py                   |  19 ++-
 src/kronika_capture/bridge/server.py               |   4 +-
 tests/contract/test_kronika_capture_services.py    | 127 +++++++++++++++++++--
 tests/contract/test_kronika_identity_retention.py  |  29 +++--
 tests/contract/test_nuc_release_docs.py            |  17 +++
 tests/contract/test_nuc_release_remote_contract.py |  10 ++
 tests/unit/chatgpt_page/test_bridge_security.py    |  24 +++-
 8 files changed, 219 insertions(+), 26 deletions(-)
```

Commit: `5b86d896b3ea03f89fef2c90f7af2c121d0ef915` on `main`. Parent: `7c1ea48be1176cd454f0ce6a97dc09d32d543838`. Working tree clean. Not pushed. Local `main` is three commits ahead of `origin/main`.

`FROZEN_ALEMBIC_SHA256` has 36 keys, counted as the dict entries from `0001` through `0035` plus `versions/__init__.py`, and as 36 files under the single Alembic `versions` directory. Part A hashes were not edited. Part B stays the empty set. Retention passed, including those pins.

Part C, measured by the retention failures before the re-pin. An intermediate test diff had added three incidental `framenest` spellings; those were removed before the re-pin, and the final retention run passed with `tests` unmoved.

| Scalar | Movement | Arithmetic |
|---|---|---|
| `src` files | 184 → 183 | `bridge/server.py` loses its last two retired tokens and leaves the content set. |
| `deploy` files | 4 → 3 | `deploy/ubuntu/README.md` loses its last token, the former capture pointer, and leaves. |
| `src` occurrences | 1606 → 1604 | The same two server labels. No other `src` file moves. |
| `deploy` occurrences | 73 → 72 | README −1. `kronika_release.py` adds none. |
| `/opt/framenest` | 146 → 145 | README −1. No other host-path key moves. |
| Content paths | −2, +0 | `src/kronika_capture/bridge/server.py` and `deploy/ubuntu/README.md`. |
| `tests` and the other trees | unmoved | Final retention matched the previous pins. |

## 8. Sites no test exercises

The `activate-capture` and `rollback-capture` help sentences were updated so they would not still say the runner restarts alone. No test reads those help strings. The emitted restart commands are pinned.

`bridge_client.mjs` joins `framenest-chatgpt-page` as its own literal. `test_result_limits.py` imports `BridgeClient` and does not call `resolveStateDir`. Changing only that literal would not fail `state_dir()`.

The `--state-dir` help text names the same directory. `test_cli_surface.py` checks that `--help` exits 0 and does not read the directory name.

`paths.py` docstrings are not compared as text. `state_dir()` is tested. `kronika_capture/__init__.py` was left unchanged, so its prose was not given a new pin.

`test_kronika_identity_migration.py` runs both capture commands through `CaptureRunner` and only asserts that they do not reach identity migration. The restart order is pinned in the capture-service tests.

## 9. Deviations, risks, missing evidence, next step

The parser help was edited inside the authorized helper because the old activate sentence would have been false. No capture protocol, state resolution, path, account, or token changed. Ordinary deploy and rollback were not given capture actions.

The largest behavioral risk is treating activation as an identity switch. The installed-to-target package also changes driver startup classification, runner startup logging, and Node lookup. The helper that performs the activation has to be one that restarts the bridge first; the package change alone does not do that.

Missing evidence is the live switch. This cut was repository-only. The installed capture still has the former labels until C8-B/H.

Smallest next step: verify `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`, publish it, and issue C8-B/H against that public SHA with this five-file delta named. Do not describe that activation as path-only or identity-only.

### Resolved Execution Issues / Near-Misses

`./.ap/ap doctor --root …` was rejected because doctor takes no argument. `./.ap/ap doctor` then passed.

One `python3 -c` command printed `skip` while an Alembic count regex was too broad. It did not import the repository or run tests. The key count was redone by counting the 36 dict entries and by `find` of the versions directory.

The three demonstration edits were restored before the nine-module run and the full suite.

### Pre-Existing Failure Classification

none

```text
Orchestration critique:
MEASURED: the stated five-module 473 has no file list, and no five-file subset of the documented nine sums to 473 on the pre-change collection counts; this report therefore gives the nine-module 625 and the full suite, not a reproduced 473; smallest correction is to name those five paths if a later prompt needs that count repeated.
LEAD: the JavaScript state-directory join is a second literal beside STATE_DIR_NAME; the cheapest check is one assertion of resolveStateDir under XDG_STATE_HOME.
```