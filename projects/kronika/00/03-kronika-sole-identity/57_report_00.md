### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-sole-identity  
Worker session ordinal: 57  
Worker exchange ordinal: 01  
Persistent role identity: WORKER  
Task identity: KSI-CORR-C7BREAD  
Status: PASS  
Phase-qualified result: not-applicable  
Report justification: new-mutation  
Logical-whole closure: not-closed  

Start commit: `7ebf4955e78731170477280c3b7f9f0cdd726e5a`  
End commit: `c0f456656c9930810e11d13e1d4684efdb3ee4ff`  
AP pin: `73e20ef80b88700d5fcbc397cd8edd4fc425869f`

Implemented and validated one local, non-amended commit on `main`. Working tree is clean; public `main` remains at the starting commit. No push, NUC contact, deployment, provider contact, or browser contact occurred. Evidence is implementation self-verification, not independent acceptance.

**1. Defect reproduction and corrected command matrix**

Before editing, both backup routes used these literal source expressions:

```python
return f"{service_account_prefix(release_path, layout)}/kronika-backup status"
return f"{service_account_prefix(release_path, layout)}/kronika-backup run-scheduled"
```

Their prefix supplied:

```python
f"sudo -n -u {layout.user} --chdir={shlex.quote(release_path)} "
f"env KRONIKA_ENV_FILE={layout.env_file} "
f"{shlex.quote(release_path)}/.venv/bin"
```

The existing production helper already supplied `systemd-run` and `--property=EnvironmentFile=…`.

The new [backup helper](/home/agile/Projects/kronika/deploy/ubuntu/kronika_release.py:813) now generates:

```python
"sudo -n systemd-run --quiet --pipe --wait --collect "
f"--uid={layout.user} --gid={layout.group} "
f"--working-directory={shlex.quote(release_path)} "
f"--property=EnvironmentFile={shlex.quote(layout.env_file)} "
f"{shlex.quote(f'{release_path}/.venv/bin/kronika-backup')} "
f"{operation}"
```

| Property | Verified result |
|---|---|
| Accepted operations | Exactly `status`, `run-scheduled` |
| Other operations | `ReleaseError("invalid command", EXIT_USAGE)` |
| Account and directory | Layout user/group and requested release directory |
| Environment | Unit `EnvironmentFile` binding |
| Output | `--quiet --pipe --wait --collect`; existing JSON consumers unchanged |
| Layout coverage | Former and canonical layouts |
| Quoting | Spaces and apostrophes in release/environment-file paths |
| Former invocation | Neither backup route uses `env KRONIKA_ENV_FILE=` |
| Database/production routes | Byte-identical to baseline |

`read_backup_readiness`, both checkpoint callers, `_cmd_status`, `_cmd_check`, and `_cmd_deploy` are byte-identical. Existing messages, exit codes, checkpoint success requirement, and bundle-ID handling remain unchanged.

Additional consumer found: **`kronika-release status`** also calls `read_backup_readiness`. Its existing status tests pass.

**2. Assertions and mutation demonstrations**

| Test | Previous assertion | Final assertion |
|---|---|---|
| `test_check_pre_manifest_uses_current_path_for_backup` | `any("kronika-backup status" in " ".join(argv) for argv, _ in runner.calls)` | Exactly one matching SSH command, equal to `cmd_remote_backup_status(PREV_PATH)` |
| `test_deploy_happy_path_sequence` | Checkpoint precedes `ln -s` | Ordering assertion retained; added exactly one command equal to `cmd_remote_run_scheduled_backup(TARGET)` |
| `test_production_create_checkpoint_returns_the_bundle_and_refuses_non_success` | `any("kronika-backup run-scheduled" in call for call in boundary.calls)` | Exactly one checkpoint call whose remote-command suffix equals the builder for `OLD_RELEASE` and `OLD_WEB_LAYOUT` |

Added regression cases:

- Eight cases pin the complete parsed command, both operations, both layouts, and ordinary/quoted paths; explicitly reject the selector-only form.
- Five cases verify unsupported operations fail with the exact usage message and exit code.

The existing backup assertions pinned command suffixes, not the old environment prefix. Other matches were fixtures, unchanged service contracts, executable-presence checks, or backup artifact names; no further test module required editing.

Observed mutation results:

| Candidate | Result |
|---|---|
| Original routes with new environment pin | 8 failed |
| Revert only `status`, ordinary-path matrix | 2 failed, 2 passed; 0.21 s |
| Revert only `run-scheduled`, ordinary-path matrix | 2 failed, 2 passed; 0.20 s |
| Restored implementation, targeted checks | 16 passed; 0.64 s |

Both individual mutations failed with:

```text
At index 2 diff: '-u' != 'systemd-run'
```

The original quoted-path cases additionally exposed `ValueError: No closing quotation`. Both route mutations were restored before final validation.

**3. Residual finding**

The backup console calls `load_catalog_backup_ops_config()`, which reads process environment directly. The database console calls `load_settings()`, whose omitted `env_file` argument honors `KRONIKA_ENV_FILE`.

That configuration-resolution divergence remains for Orchestrator disposition. Neither console was changed. No database-route alignment is proposed in this correction because behavior equivalence was not established.

Current repository defaults are canonical; the deployed historical defaults and live-root observations remain Orchestrator-provided evidence, not independently observed host evidence.

**4. Validation**

All Python evidence used the declared AP route with baseline `7ebf4955e78731170477280c3b7f9f0cdd726e5a`. AP doctor, project check, and runtime provenance passed.

| Suite | Result | Elapsed | Baseline difference |
|---|---:|---:|---:|
| Focused release/migration modules | 420 passed | 2.07 s total | +13 |
| Full declared Python suite | 4,981 passed, 8 skipped, 3 warnings | 694.69 s | +13 passed; other counts unchanged |
| Retention | 15 passed | 0.36 s | None |
| `companion_web_bridge` | 23 passed | 0.102 s | None |
| `companion_review_extension` | 41 passed | 0.341 s | None |
| `x_companion_extension` | 55 passed | 0.271 s | None |
| `companion_settings_automatic_analysis` | 6 passed | 10.087 s | None |
| `kronika_ui` | 12 passed | 0.207 s | None |
| `catalog_card_ai_quick_action` | 30 passed | 0.368 s | None |
| Bounded frontend/cockpit/gallery glob | 212 passed | 0.786 s | None |

Focused execution comprised source/remote/migration modules: **391 passed in 1.84 s**, plus release documentation contracts: **29 passed in 0.23 s**. All final gates exited zero.

**5. Commit and retention evidence**

Commit: `c0f456656c9930810e11d13e1d4684efdb3ee4ff`  
Subject: `fix(deploy): bind backup commands to unit environment`

```text
 deploy/ubuntu/kronika_release.py                   | 25 +++++++++++-
 tests/contract/test_kronika_identity_migration.py  |  8 +++-
 tests/contract/test_nuc_release_remote_contract.py | 47 ++++++++++++++++++++--
 3 files changed, 73 insertions(+), 7 deletions(-)
```

Exactly one path-specific `git add` and one `git commit` were performed. Staged and committed whitespace checks passed.

Part A is byte-unmoved: **86 document hashes and 36 Alembic hashes** independently verified, zero mismatches. Part B remains **empty**. The retention ledger itself is byte-identical.

Regenerated Part C measurements:

| Tree | Files | Occurrences | Movement |
|---|---:|---:|---:|
| src | 184 | 1,606 | 0 |
| deploy | 7 | 78 | 0 |
| scripts | 0 | 0 | 0 |
| tests | 174 | 1,382 | 0 |
| docs | 84 | 749 | 0 |
| extension | 0 | 0 | 0 |

Changed-file occurrence counts remained `69→69`, `90→90`, and `278→278`. No scalar re-pin was needed.

**6. Sites without test exercise**

None among changed executable sites: both routes and the helper’s accepted/refused branches are exercised. Actual systemd environment loading on the NUC was not exercised; that remains outside this repository-only grant.

**7. Deviations, risks, and next step**

No implementation or Git scope deviation. No additional file was edited, and no report file was written.

The smallest next step is Orchestrator review of the local commit and evidence before separately authorizing publication and NUC validation.

**Resolved Execution Issues / Near-Misses**

- Initial combined reads and collection output were truncated. Required sections were reread, and complete relevant inventories were regenerated.
- A new migration assertion initially assumed logs contained only the remote command. The harness records the full SSH invocation; the assertion was corrected to require exactly one call with the exact command suffix. Targeted and full validation then passed.
- An incorrect settings-file lookup was resolved to `src/kronika/configuration.py`.
- The initial acknowledgement was Slovak before the attached English-only instruction was read; subsequent task communication and this report are English.

**Pre-Existing Failure Classification**

None. Intentional regression/mutation failures and the corrected task-local assertion failure are distinguished above.

Authority expires on submission of this terminal report. No autonomous continuation is authorized.

Orchestration critique:  
MEASURED: none  
LEAD: none