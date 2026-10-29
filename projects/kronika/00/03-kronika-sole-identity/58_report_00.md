### Report for ORCHESTRATOR_CHAT

| Field | Value |
|---|---|
| Logical whole identity | `kronika-sole-identity` |
| Worker session ordinal | `58` |
| Worker exchange ordinal | `01` |
| Task identity | `KSI-IMPL-C8AP` |
| Persistent role | `WORKER` |
| Status | **PASS** |
| Phase-qualified result | `not-applicable` |
| Logical-whole closure | `not-closed` |
| Evidence tier | Implementation, non-independent |
| Report justification | `new-mutation` |
| Start commit | `c0f456656c9930810e11d13e1d4684efdb3ee4ff` |
| End commit | `90766ca04358af876a7fb154c44fb005612d34ad` |
| AP pin | `73e20ef80b88700d5fcbc397cd8edd4fc425869f` |
| Commit, push, publication, deployment | One local commit; no push, no publication, no deployment |
| NUC, provider and browser contact | None |

`migrate-capture-paths` is a separate two-phase command. It copies the installed capture release, rebuilds that tree's virtual environment from its own lock, and switches only the pointer and the documented path lines. Capture software is unchanged. Routine `status`, `check`, `deploy` and `rollback` do not call it.

## 1. Command, plan and two-phase shape

Literal commands:

```text
kronika-release migrate-capture-paths preflight [transport arguments]
kronika-release migrate-capture-paths apply --preflight-digest <64-hex> --yes [transport arguments]
```

`preflight` is read-only. It accepts only the former pointer `/opt/framenest/capture-current` and refuses the canonical pointer already present, both pointers present, neither pointer present, and an unverifiable pointer read (`EXIT_LAYOUT`). It reads the installed release through the existing marker resolver, so a tree that still carries `.framenest-release-sha` and `.framenest-release-manifest.json` keeps that identity. It does not call Git and does not recompute `capture_runtime_identity` from HEAD. The printed plan binds source path, release SHA, marker spellings and hashes, tree-manifest hash, the source manifest's `capture_code_tree` and bridge protocol, and the installed versus canonical unit hashes. A present bridge protocol other than `1` is refused (`EXIT_SOURCE_GATE`).

`apply` refuses without `--yes` (`EXIT_USAGE`, no SSH) and without the digest flag (argparse exit 2, no SSH). A digest that is not the fresh plan's digest is refused with `EXIT_MIGRATION` before copy, Poetry, or `systemctl`. Apply then drains and checks the brake, publishes the copied release, drains and checks the brake again, and only then stops services.

Successful output names `source_pointer`, `source_path`, `release_sha`, `marker_spellings`, `capture_code_tree`, `capture_bridge_protocol`, `target_pointer`, `target_release`, `executable`, the five unit names, and `plan_digest`.

## 2. Preservation, gate and bounded-action matrices

Preservation, observed on the fake host:

| Claim | Result |
|---|---|
| Source identity | Taken from the installed tree's own markers. The fixture manifest's `capture_code_tree` is printed unchanged. No `git` invocation. |
| Markers | Copied by `cp -a`. No `cat >` under `/opt`. Historical spellings stay the spellings that were present. |
| Tree equality | Staging manifest must equal the source manifest before `.venv` is removed. A mismatch returns `EXIT_SOURCE_GATE` and does not stop services. |
| Lock and tooling | `poetry check --lock`, `poetry env use` of the frozen CPython, and one `poetry install --only main` through `POETRY_BIN`. A changed `poetry.lock` returns `EXIT_POETRY`. The transcript contains no `uv`. |
| Pointer | One `ln -s` to `/opt/kronika/capture-current.next`, then one `mv -T` onto `/opt/kronika/capture-current`. The former symlink is removed with `rm -f`. The former release directory is not removed. |
| Units | The five written unit bodies equal the repository units. Bridge and runner `ExecStart` is `/opt/kronika/capture-current/.venv/bin/kronika-capture`. Account, state directory, token path, profile, journal and port `8765` stay in those bodies. |
| Existing target | If `/opt/kronika/releases/<sha>` already exists, apply stops with `EXIT_TRANSPORT` and does not `rm -rf` that path. |

Gates:

| Condition | Exit | Mutation |
|---|---|---|
| Live or paused capture work | `EXIT_CAPTURE_BUSY` (22) | No copy, no stop, no start |
| Brake not `brake=ok` | `EXIT_CAPTURE_BRAKE` (23) | No stop, no start |
| Unit text differs beyond the path lines | `EXIT_SOURCE_GATE` (3) | No copy |
| Protocol present and not `1` | `EXIT_SOURCE_GATE` | No copy |
| Readiness `failed` | `EXIT_SERVICE_TERMINAL` (16) | One start of bridge and one of runner; no second start; new release kept |

The work and brake gates run twice on the success path: before the copy, and again after publish and before stop.

Bounded actions on success, each exactly once: `systemctl stop kronika-capture-runner.service`, `systemctl stop kronika-capture-bridge.service`, `systemctl start kronika-capture-bridge.service`, `systemctl start kronika-capture-runner.service`, and one `systemctl daemon-reload`. There is no `systemctl restart`. There is no stop, start or restart of Xvfb, VNC, the view, `kronika.service` or `framenest.service`. Order is first gate, copy, second gate, stop runner, stop bridge, stage pointer, switch pointer, install units, start bridge, start runner, one readiness read.

`status`, `check`, `deploy` and `rollback` do not contain `migrate-capture-paths` or `observe_capture_path_plan` in their source. Running those four commands with the new handler replaced by a raising stub still returns success, and their SSH transcripts do not contain the new command, the capture-path scratch directory, or a bridge/runner stop or start.

## 3. Six-artifact diff and contract hash

Git diff of the six capture artifacts changes five lines and nothing else. Xvfb, VNC and the view unit are byte-identical, so they do not appear in the diff.

| File | Line |
|---|---|
| `kronika-capture.env.example` | `# KRONIKA_CAPTURE_RELEASE=/opt/kronika/capture-current` |
| `kronika-capture-bridge.service` | `WorkingDirectory=` and `ExecStart=` |
| `kronika-capture-runner.service` | `WorkingDirectory=` and `ExecStart=` |

The contract test reconstructs the former text of all six files and requires the canonicalizer to restore the current text, with exactly ten diff lines (five removals and five additions), each a documented path line.

`capture_unit_contract_sha256` is still the hash of `path + newline + stripped file text + newline` over `CAPTURE_CONTRACT_PATHS`. No test pins the previous digest. Recomputed from `git show HEAD` of the six committed files:

```text
11a1f07cc1d36294da481fcc2c64e13e44277449290db216c2c5b6cc86c3d902
```

`capture_runtime_contract_sha256` is unchanged because `CAPTURE_RUNTIME_CONTRACT` was not edited.

## 4. Mutation demonstrations

| Mutation | Observed failure |
|---|---|
| `canonicalize_capture_path_text` also rewrote `User=` lines | `test_capture_artifact_diff_is_only_the_pointer_path_lines` failed: `kronika-capture` versus `kronika-capture-widened` |
| Digest comparison replaced with `if False` | `test_apply_refuses_a_digest_that_does_not_match` got exit 0 and `apply complete` instead of `EXIT_MIGRATION` (27) |
| Work drain removed from `_enforce_capture_path_gates` | `test_busy_capture_is_refused_before_mutation` got exit 0 and `apply complete` instead of `EXIT_CAPTURE_BUSY` (22) |

All three edits were restored. The three tests then passed, and that restored tree is the committed tree.

## 5. Suites

| Suite | Result | Elapsed | Baseline difference |
|---|---|---|---|
| Focused release, capture, migration and docs modules | 609 passed, 0 failed | 22.00 s | The prompt's 429 was not a named file list. This run is the nine modules below. It contains 18 new tests, so the same files before this commit would be 591. |
| Full Python, `./.ap/ap exec --operation test` | 4,999 passed; 8 skipped; 3 warnings; 0 failed | 693.89 s | +18 passed. Skips, warnings and failures unchanged from 4,981 / 8 / 3 / 0. |
| Retention, inside the combined capture+retention run | 15 passed | 1.09 s for 68 tests (53 capture + 15 retention) | Counts unchanged after the Part C re-pin |
| `companion_web_bridge` | 23 passed, 0 failed | 82.3 ms | None |
| `companion_review_extension` | 41 passed, 0 failed | 184.5 ms | None |
| `x_companion_extension` | 55 passed, 0 failed | 129.9 ms | None |
| `companion_settings_automatic_analysis` | 6 passed, 0 failed | 10,106 ms | None |
| `kronika_ui` | 12 passed, 0 failed | 93.2 ms | None |
| `catalog_card_ai_quick_action` | 30 passed, 0 failed | 216.0 ms | None |
| Bounded frontend/cockpit/gallery glob | 212 passed, 0 failed | 756.2 ms | None |

Focused modules: `test_kronika_capture_services.py`, `test_chatgpt_page_packaging.py`, `test_nuc_release_remote_contract.py`, `test_nuc_release_source_contract.py`, `test_nuc_release_docs.py`, `test_nuc_operator_runbook.py`, `test_kronika_identity_migration.py`, `test_kronika_cli_and_release_readers.py`, `test_kronika_durable_writer_identities.py`.

Collected full-suite size was 5,007, which is 4,981 + 8 skips + 18 new tests.

## 6. Diff, commit, Part A, Part B, Part C

```text
 deploy/systemd/kronika-capture-bridge.service     |   4 +-
 deploy/systemd/kronika-capture-runner.service     |   4 +-
 deploy/systemd/kronika-capture.env.example        |   2 +-
 deploy/ubuntu/kronika_release.py                  | 710 ++++++++++++++++++++++
 docs/UBUNTU_NUC_DEPLOYMENT.md                     |  66 +-
 tests/contract/test_kronika_capture_services.py   | 598 +++++++++++++++++-
 tests/contract/test_kronika_identity_retention.py |  39 +-
 7 files changed, 1406 insertions(+), 17 deletions(-)
```

Commit: `90766ca04358af876a7fb154c44fb005612d34ad` on `main`. Working tree clean. Not pushed.

`FROZEN_ALEMBIC_SHA256` has 36 keys (`0001` through `0035`, plus `versions/__init__.py`). Part A hashes were not edited. Part B stays the empty set. Retention passed, which includes those pins.

Part C, measured by the retention assertions before the re-pin:

| Scalar | Movement | Arithmetic |
|---|---|---|
| `deploy` file count | 7 → 4 | The bridge unit, the runner unit and `kronika-capture.env.example` each lose their last `framenest` token. No other tree's file count moves. |
| `deploy` occurrences | 78 → 73 | env.example −1, bridge −2, runner −2. `kronika_release.py` adds no retired token. |
| `docs` occurrences | 749 → 751 | `UBUNTU_NUC_DEPLOYMENT.md` −1 for the planned pointer, +3 for the former pointer in the new section. |
| `tests` occurrences | 1382 → 1386 | `test_kronika_capture_services.py` −3 for the old path pins and +7 for historical marker spellings plus the negative `framenest.service` check. The file stays in the content set. |
| Content paths | −3, +0 | The same three deploy files leave. |
| `/opt/framenest` | 152 → 146 | deploy −5, tests −3, docs +2. The other host-path keys stay. |

`src`, `scripts` and `extension` occurrence counts stay. Environment-prefix, unit-account and capitalized counts stay.

## 7. Sites no test exercises

These calls are on the success path and the fake accepts them, but no assertion fails if they are removed: the `poetry.toml` and `poetry.lock` existence probes, `chown -R root`, `chmod -R a-w`, the shebang-relocation upload, and the post-install `WorkingDirectory` read-back. A tree-manifest mismatch is refused by a test. A marker-byte mismatch after an otherwise equal tree is not given its own fixture.

`deploy/ubuntu/README.md` still says `activate-capture` and `rollback-capture` are the only operations that switch `/opt/framenest/capture-current`. That sentence was outside this grant. It is now incomplete, because `migrate-capture-paths` removes that symlink. No test compares that README sentence to the units.

The live installed units, the live release markers, and the real stop/start cycle were not observed. That is C8-A/H.

## 8. Deviations, risks, missing evidence, next step

The command deletes the new release tree if a failure happens before the pointer switch, including a second-gate refusal after publish. After the switch, a readiness failure keeps the new pointer and does not start the browser again. Restoration is runbook text, not a third subcommand.

The largest host risk is an installed unit whose text differs from these repository units by more than the two path lines. Preflight will refuse before copy. This session did not read the NUC units.

Smallest next step: verify this commit, then issue C8-A/H against a fresh preflight. Do not treat `deploy/ubuntu/README.md` as the procedure; the runbook section is the procedure.

### Resolved Execution Issues / Near-Misses

The assertion `rm -rf <target>` also matched `rm -rf <target>.staging/.venv`. The tests now compare exact command lines. That correction is in the commit. The three demonstration edits were restored before the full suite.

One `python3 -c` count of the `framenest` diff was run while measuring Part C. It did not execute repository tests. The retention failures are the measurement that was re-pinned. A later `git show` hash command was re-run under `/bin/bash --noprofile` after a zsh wrapper failed; the hash above is that successful recomputation.

### Pre-Existing Failure Classification

none

```text
Orchestration critique:
MEASURED: deploy/ubuntu/README.md still says activate-capture and rollback-capture are the only operations that switch /opt/framenest/capture-current; the file is outside this grant; an operator who follows the README instead of the runbook will miss migrate-capture-paths; smallest correction is a later README sentence, not a change inside C8-A/H.
LEAD: the installed capture units may differ from these repository units beyond the path lines; the cheapest check is C8-A/H preflight, which refuses before copy.
```