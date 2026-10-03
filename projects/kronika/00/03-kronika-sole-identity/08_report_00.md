All gates green. Writing the terminal report.

### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: kronika-sole-identity
Worker session ordinal: 08
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-03 — restore pre-C1 process-environment semantics (F1, F2) and stop the dev launcher manufacturing a conflict (F4)
Status: PASS
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this correction, by design
Start commit: c02c6753694d5d4958045bb79f80b5eb94b9c75c
End commit: 24bea56daca28603d81cac8d7ed7e3888ba90671
Report justification: new-mutation
```

## Repository gate

Verified before editing at `/home/agile/Projects/kronika`, read-only: branch `feat/kronika-identity-dual-read`, HEAD `c02c675…`, subject and parent `90c93ea…` as issued, clean tree; `git ls-remote origin refs/heads/main` → `18c357cf6f8c5ff9cc3b2c28e638510fc73a3672`, branch unpublished; `.ap` gitlink and submodule HEAD both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`; `./.ap/ap doctor` PASS, governing variant `stable`; `./.ap/ap project check --baseline c02c675…` PASS. No stopping condition triggered.

## Oracle construction, and the evidence that licenses it

The reference is the **library's own** `BaseSettings.settings_customise_sources`, taken as `BaseSettings.__dict__["settings_customise_sources"]` from the installed library class. Patching the project class's hook to that object makes the library's own `_settings_init_sources` build the stock `EnvSettingsSource` and `DotEnvSettingsSource` from `os.environ` via the library's `parse_env_vars`, and apply the library's default source order. No project dual-prefix class participates. `test_the_stock_reference_runs_only_library_sources` asserts this by intercepting the hook and recording the constructed source classes: `['InitSettingsSource', 'EnvSettingsSource', 'DotEnvSettingsSource', 'SecretsSettingsSource']`, with no `_DualPrefix*` class among them. That is literally the pre-cut path: the pre-cut file had no `settings_customise_sources` override at all.

Evidence that today's library is a valid stand-in for `18c357c`:

- `poetry.lock` is byte-identical at both commits: `git show 18c357c:poetry.lock | sha256sum` and `git show HEAD:poetry.lock | sha256sum` both `f67d30621b0a0a2ca953d4d73f347023c15da8980e95bf4c92f5a544c844895d`. `pyproject.toml` is also byte-identical.
- The locked `pydantic-settings` version is `2.14.2`; the installed `pydantic_settings.VERSION` is `'2.14.2'`.
- The settings model itself did not change. Extracting the block from `host: str = Field(...)` to the end of the class from `git show 18c357c:src/framenest/configuration.py` and from the HEAD file gives 350 identical lines and an empty diff, and `model_config` is character-identical (`env_prefix="FRAMENEST_"`, `env_file_encoding="utf-8"`, `hide_input_in_errors=True`, `extra="ignore"`).
- The whole `18c357c..c02c675` diff of that file touches only imports, the two dual-prefix source classes, `settings_customise_sources`, the conflict error type, and `load_settings`' env-file selector.

`test_the_settings_library_is_unchanged_since_the_restoration_reference` enforces the first two of these in the suite, so the oracle cannot silently outlive its licence. If `poetry.lock` ever differs at the reference commit, that test fails and the oracle is void.

## Step-2 observations, at HEAD before any change

| # | Observation | Result |
|---|---|---|
| 1 | `framenest_port=9999 .venv/bin/framenest-db status`, hermetic `env -i`, synthetic database path under `/tmp` | `{"operation":"status","state":"uninitialized",…}`, **exit 0** — the setting was silently ignored |
| 2 | Oracle, same input | port **9999** honoured; `Framenest_Port=9999` also honoured; `framenest_host=10.0.0.2` rejected with `ValidationError` |
| 3 | `FRAMENEST_PORT= .venv/bin/framenest-db status`, hermetic `env -i` | `{"operation":"status","state":"uninitialized",…}`, **exit 0** — silently defaulted |
| 4 | Oracle, same input | **`ValidationError`** (fail closed) |

The same probe also answered the environment-file question before I wrote any code: `FRAMENEST_PORT=` in a file already raised `ValidationError` on **both** sides at HEAD, because `_DualPrefixDotEnvSettingsSource` returns `{**file_values, **resolved}` and the raw `""` survives in `file_values`. The file path never had the F2 regression. The whole file matrix (lower/mixed/upper key spelling, empty, whitespace, invalid) was already at parity at HEAD.

## What I changed, and the exact diff of every path

```text
 src/framenest/configuration.py                     |  21 +-
 src/framenest/identity_env.py                      |  97 ++++-
 .../infrastructure/runtime/development.py          |  29 +-
 tests/contract/test_kronika_identity_retention.py |  12 +-
 tests/contract/test_kronika_settings_parity.py     | 415 +++++++++++++++++++++
 .../runtime/test_development_runtime.py            |  88 +++++
 6 files changed, 642 insertions(+), 20 deletions(-)
```

**`src/framenest/identity_env.py`** — three additions, no change to `lookup_env`:

- `folded_identity_environment(values)` returns `{name.upper(): value for …}`. Later entry wins, which is the same collision rule the library's own comprehension applied, over the same mapping, so a case collision resolves identically.
- `lookup_field_value(suffix, *, environ=None, case_folded=None)` resolves in three ordered layers: (1) the case-exact `KRONIKA_<SUFFIX>` when non-empty; (2) the case-folded `FRAMENEST_<SUFFIX>`, **raw, including `""`**; (3) the case-folded `KRONIKA_<SUFFIX>`, empty counting as unset. `lookup_env` is still called for every field, so the cross-prefix conflict check stays the single authority, stays case-exact, and still raises before any layer returns.
- `drop_identity_environment_spellings(environ, suffixes)` removes every accepted and case-variant spelling of the given suffixes, in place.

`lookup_env` itself is byte-unchanged, so the `ENV_FILE` selector and every direct reader call site (`catalog_backup_ops`, `catalog_backup_offdevice`, `development._resolve_override`, `ai/configuration`, `framenest_release.py`, `production_ai_deploy.py`) keep their exact C1 semantics, including empty-means-unset.

**`src/framenest/configuration.py`** — `_resolved_field_values` folds `resolver_values` once and calls `lookup_field_value` instead of `lookup_env`. `_load_env_vars` of both dual-prefix sources, `settings_customise_sources`, the source ordering, `hide_input_in_errors`, `extra="ignore"`, `env_file_encoding` and the retained `env_prefix="FRAMENEST_"` are unchanged.

**`src/framenest/infrastructure/runtime/development.py`** — added `HOST_ENV`, `HOST_ENV_SUFFIX`, and `SPAWNED_SETTING_SUFFIXES = (HOST, PORT, DATABASE_PATH)`. `_spawn_server_process` now calls `drop_identity_environment_spellings(env, SPAWNED_SETTING_SUFFIXES)` before writing `env[HOST_ENV]`, `env[PORT_ENV]`, `env[DATABASE_ENV]`. What the launcher resolves and how it configures the child are unchanged; only the shape of the handed-over environment changed.

**`tests/contract/test_kronika_settings_parity.py`** (new, 22 tests) and **`tests/unit/infrastructure/runtime/test_development_runtime.py`** (+11 tests) — described below.

## Both-cases-present: my decision, and the residual divergence

**Case variants of the old spelling — exact parity.** `FRAMENEST_PORT=9998` then `framenest_port=9999` resolves to 9999, because both sides fold the same mapping with the same later-wins rule. `test_both_cases_of_one_old_name_resolve_to_the_later_value` pins it, and the parity matrix covers it structurally. I could match `18c357c` exactly here, and I do.

**Case variants across the two prefixes — one deliberate divergence.** With `KRONIKA_PORT=9998` and `framenest_port=9999`, the case-exact identity spelling wins (9998) and **no conflict is raised**, because the conflict rule must stay case-exact. Pre-C1 this input was 9999, since `KRONIKA_PORT` did not exist. That is a divergence and I am not claiming parity: the input contains the new spelling, so it is not old-spelling-only, and raising a conflict would require making the conflict rule case-insensitive, which the grant forbids. `test_the_case_exact_identity_spelling_outranks_a_case_variant_of_the_old_spelling` and `test_the_two_prefixes_in_different_cases_do_not_raise_a_conflict` pin both halves. The reverse ordering does not occur: a case variant of the compatible spelling can never shadow the identity spelling, because layer 2 is consulted before layer 3.

## Environment-file empty case: no regression existed`test_an_explicitly_empty_environment_file_value_fails_closed` pins it. Both channels are also covered differentially, so this cannot drift silently.

## Launcher environment audit (the audit's LEAD, in scope)

Every `env[...]` assignment and every `env=` subprocess construction in `src/framenest`, checked against the resolver's view:

| Site | Identity-prefixed names | Action |
|---|---|---|
| `development.py:515-517` (`_spawn_server_process`) | `FRAMENEST_HOST`, `FRAMENEST_PORT`, `FRAMENEST_DATABASE_PATH` | **fixed** — normalisation added before injection |
| `development.py:523` (`env=env`) | the same mapping | covered by the fix |
| `youtube/downloader.py:537` (`env=_subprocess_environment()`) | none — `PATH`, `LANG`, `LC_ALL`, `PYTHONIOENCODING`, `PYTHONUTF8` | no conflict possible; untouched |
| `x/downloader.py:119`, `:392` (`env=_subprocess_environment()`) | none — `PATH`, `LANG`, `LC_ALL`, `PYTHONNOUSERSITE`, `NO_COLOR` | no conflict possible; untouched |
| `development.py:640,647`; `media_analysis/process.py:401`; `x/downloader.py:115,387`; `catalog_backup_workstation.py:386` | none — no `env=` argument, environment inherited | cannot manufacture a pair; untouched |

`development.py` is the **only** place in `src/framenest` that constructs a child environment containing an identity-prefixed name. Correction to the audit's count: the launcher injects **three** names, not four; `FRAMENEST_DEVELOPMENT_RUNTIME_DIR` and `FRAMENEST_DEVELOPMENT_LOG_DIR` are read-only overrides and are never written into the child. The `LEAD` about the capture and sidecar child processes did not materialise — no such construction exists in this package.

Post-fix observation through the real launcher with `KRONIKA_HOST=0.0.0.0` and `KRONIKA_PORT=48199` in the parent: the child carries `FRAMENEST_DATABASE_PATH`, `FRAMENEST_DEVELOPMENT_LOG_DIR`, `FRAMENEST_DEVELOPMENT_RUNTIME_DIR`, `FRAMENEST_HOST`, `FRAMENEST_PORT` — one name per injected suffix, no `KRONIKA_*` — and builds settings with host `127.0.0.1` and the launcher's resolved port, no conflict.

## The parity test, and proof that it fails on broken parity

`tests/contract/test_kronika_settings_parity.py` compares, for **every** field of `FrameNestSettings` (39), **every** value in a 10-value matrix (explicitly empty, whitespace-only, whitespace-padded, numeric, IP, absolute path, bool, JSON object, JSON array, invalid), **every** case spelling (canonical, lower, alternating mixed), and **both** channels, one variable at a time: 1170 comparisons per channel, 2340 in total, each building settings twice — 4680 constructions. An outcome is either the built settings (full `model_dump`, with the `SecretStr` unmasked so two different synthetic secrets are not both masked to equality) or the failure type plus the sorted field locations the failure names. Messages are not compared, because the library embeds the source class name in `SettingsError` text and that name is exactly what this correction may change. Cost: 3.4 s and 4.0 s.

Demonstration, from `/tmp/opencode/ksi08/parity_break_demo.py`, which imports the **committed** module and calls its own `_parity_mismatches` under three in-memory reversions:

| Scenario | Reverted | Observed |
|---|---|---|
| A | `_resolved_field_values` restored to its exact `c02c675` body | **773 mismatches, test FAILED** |
| B | `folded_identity_environment` → identity (no folding) | **742 mismatches, test FAILED** |
| C | `lookup_field_value` → plain `lookup_env` | **773 mismatches, test FAILED** |

So the test detects F1 and F2 separately, not just their union. A fourth scratch file disables only the launcher's normalisation call and shows the committed launcher regression raising `AssertionError`.

## Retention ledger: every Part C movement, with its cause

Part A and Part B were not touched; the ledger diff is six numbers in Part C and nothing else.

| Pin | Was | Now | Exact cause |
|---|---|---|---|
| `PER_TREE_FRAMENEST_FILE_COUNT["tests"]` | 320 | 321 | the new parity module contains the token |
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["src"]` | 2983 | 2981 | composing the launcher constants replaced three inline `FRAMENEST_*` literals in `development.py` with `HOST_ENV`/`PORT_ENV`/`DATABASE_ENV` references and added one `HOST_ENV = "FRAMENEST_HOST"` literal: −3 +1. `configuration.py` is net 0 (one `framenest.identity_env.*` docstring reference each way). |
| `PER_TREE_FRAMENEST_OCCURRENCE_COUNT["tests"]` | 4401 | 4434 | +27 in the new parity module and +6 in the launcher tests |
| `ENV_PREFIX_BARE_SPELLING_COUNT` | 16 | 18 | the two `f"FRAMENEST_{suffix}"` literals in the launcher tests; `{` ends the token, so each counts as a bare spelling |
| `CAPITALIZED_OCCURRENCE_COUNT` | 3364 | 3379 | +13 in the new parity module, +2 in the launcher tests |
| `CAPITALIZED_FILE_COUNT` | 481 | 482 | the new parity module contains `FrameNest` |

`ENV_PREFIX_TOKEN_COUNT` stayed642 and `ENV_PREFIX_DISTINCT_NAME_COUNT` stayed 101: src lost two tokens and the parity module gained exactly two (`"FRAMENEST_PORT"` and the `{"FRAMENEST_PORT": "1", …}` literal). The mutation-header, host-path, unit-account and console-script pins did not move. All 14 ledger tests pass.

## Counts

| Route | Baseline `c02c675` | Final `24bea56` |
|---|---|---|
| Python `--operation test` | `4314 passed, 8 skipped, 3 warnings` (681.83 s) | `4347 passed, 8 skipped, 3 warnings` (687.17 s) |
| JavaScript `node --test tests/*.test.js` | `554 total, 549 passed, 0 failed, 5 skipped` | `554 total, 549 passed, 0 failed, 5 skipped` |

+33 = 22 new parity tests + 11 new launcher tests (22 → 33 in the launcher module). Skips remain 8 and warnings remain 3, with the same eight named skips.

## Re-verified audit reproductions at the committed HEAD

- `framenest_port=9999` → port 9999, matching the reference. `Framenest_Port=9999` likewise.
- `FRAMENEST_PORT=` and `framenest_port=` → `ValidationError`, fail closed, matching the reference; under `framenest-db status` this is now `{"state":"error","error_code":"FRAMENEST_DB_COMMAND_FAILED"}`, **exit 1** (was exit 0).
- `FRAMENEST_PORT=" 8123 "` → 8123 on both sides.
- Conflict `KRONIKA_PORT=9998` + `FRAMENEST_PORT=9999` → `{"error_code":"FRAMENEST_DB_CONFIGURATION_FAILED","message":"Conflicting environment variables KRONIKA_PORT and FRAMENEST_PORT are set to different values."}`, **exit 2**, suffix-only, no value.
- Same-value pair `KRONIKA_PORT=9999` + `FRAMENEST_PORT=9999` → accepted, exit 0.
- `FRAMENEST_ENV_FILE=` and `KRONIKA_ENV_FILE=` → both behave as unset, exit 0; `FRAMENEST_ENV_FILE=<path>` still selects the file; a lower-case file key is still read.

## Scope verification, and one correction to the issued check

`git diff --stat 90c93ea..HEAD` is empty for every Out-of-scope path: `deploy/**`, `deploy/systemd/**`, `docs/**`, `AGENTS.md`, all root Markdown, `src/kronika_capture/**`, `pyproject.toml`, `ap.project.conf`, `.gitmodules`, `.gitignore`, the 36 applied Alembic revision files, and `src/framenest/adapters/api/tailscale_ingress.py`. F3, F5, H1, H2, H3 and D1 were not touched.

Correction to step 9 as written: `18c357c..HEAD` is **not** empty for three of those paths — `deploy/ubuntu/framenest_release.py`, `deploy/ubuntu/production_ai_deploy.py`, `src/framenest/adapters/api/tailscale_ingress.py`. Those changes were made by **C1 (`90c93ea`)**, they were already present at `c02c675` before this session started, and the accepted plan's C1 section enumerates them. `git diff --stat c02c675..HEAD` on exactly those three paths is empty, which is the property that matters: this correction added nothing there. Nothing under `docs/`, no root Markdown, no lockfile, no `ap.project.conf`, no Alembic bytes and no `src/kronika_capture/**` changed anywhere on the branch.

`ap project check --root … --baseline 24bea56daca28603d81cac8d7ed7e3888ba90671`: **PASS**. Tree clean.

## Git

Branch `feat/kronika-identity-dual-read`. Behaviour-restoration reference `18c357cf6f8c5ff9cc3b2c28e638510fc73a3672`; C1 `90c93eac94171182039a76fbb1c956e42b44da2c`; correction parent `c02c6753694d5d4958045bb79f80b5eb94b9c75c`; this commit `24bea56daca28603d81cac8d7ed7e3888ba90671`, subject `fix(identity): restore pre-cut process-environment parity for old spellings`. Not pushed; no new branch.

## Deviations, risks and missing evidence

- The issued step-9 wording needed the correction stated above; the underlying property holds.
- `poetry.lock` did **not** differ between `18c357c` and HEAD, so the oracle-licence stopping condition never triggered.
- The parity matrix sets one variable at a time, so it does not cover *simultaneous* multi-field input. The only simultaneous combinations that changed behaviour are the prefix pairs, and those are covered by dedicated tests and by the unchanged conflict suite.
- Parity is proven for the model as it exists. C3 will move the package and rename the class; the parity test references `FrameNestSettings` and will need the same rename, which is C3's business.
- The differential test shells out to `git show` for two blobs, like the retention ledger already does. If the reference commit ever becomes unreachable the test fails loudly rather than silently weakening.
- I did not run any C1b behaviour that this correction could have disturbed beyond the full suite; the suite is the evidence for that.

## Resolved Execution Issues / Near-Misses

- I first launched the baseline suite with `nohup … &` to read documents in parallel. The client killed the process group when the command hit its 120 s limit, so the background run died at 4%. I re-ran the suite in the foreground and read the documents afterwards. No repository evidence came from the aborted run, and I did not edit anything while a suite was running.
- My client restricts external directories to `/tmp/opencode/**`, narrower than the prompt's `/tmp`. All scratch files went to `/tmp/opencode/ksi08/`, still under `/tmp`. `rm` is denied by the client, so those scratch files remain: `oracle_probe_step2.py`, `verify_step8_probe.py`, `parity_break_demo.py`, `launcher_break_demo.py`, `ledger_counters_probe.py`, plus `pre_c1_configuration.py`, `pre_model.txt`, `head_model.txt`, `scratch/`, `exit/`, `baseline_python.log`.
- Two of my own probes were wrong before the code was, not the implementation: the first `_record` hook took the wrong arity, and my first launcher test put a *conflicting* `KRONIKA_*`/`FRAMENEST_*` pair in the parent environment, which the launcher correctly rejects at construction — a different failure from the one under test. The test was corrected to carry exactly one spelling in the parent, which is the realistic F4 shape and what the audit captured.
- One parametrized case initially failed with `mkdir` on `/srv` because my synthetic inherited database path was outside the writable area. Test data, not a defect.

## Pre-Existing Failure Classification

none — no test failed at any point. Baseline and final both green on both routes.

## Commands beyond the declared routes

Python evidence went only through `./.ap/ap exec --root /home/agile/Projects/kronika --baseline c02c675… --operation {test,test-focus,runtime-info}`, plus `./.ap/ap project check` and `./.ap/ap doctor`. JavaScript used `node --test tests/*.test.js`. Read-only Git: `status`, `rev-parse`, `log`, `show`, `diff`, `ls-files`, `ls-remote`, `submodule status`, and `add`/`commit` under the granted commit authority. Library sources under `.venv/…/pydantic_settings/` were **read** with the read tool and never imported by an interpreter I launched. Console-script probes used a synthetic `env -i` environment with `HOME` and `TMPDIR` under `/tmp/opencode/ksi08/exit`, one synthetic database path per run, and no inherited identity variable. No NUC, provider, capture, network or dependency action occurred; nothing outside `/tmp` was written; `git status --porcelain` is empty.

## Smallest next step

Accept this correction and issue the fresh independent re-audit of `24bea56` on the configuration trust boundary — with the oracle licence and the both-cases-present divergence as the two things it should check first — before C2 is granted.

Authority expiry: on submission of this report all authority under the prompt expires. No further implementation, no push, no publication, no NUC refresh and no later cut is authorized by it.

```text
Orchestration critique:
MEASURED: the issued step-9 check "`18c357c..HEAD` are still empty for every Out-of-scope path" cannot hold for the branch as it stands; evidence: `git diff --stat 18c357c..HEAD` is non-empty for `deploy/ubuntu/framenest_release.py`, `deploy/ubuntu/production_ai_deploy.py` and `src/framenest/adapters/api/tailscale_ingress.py`, while `git diff --stat c02c675..HEAD` is empty for all three, i.e. the delta is C1's and predates this session; effect: an auditor following the check literally will read a pre-existing C1 change as a scope breach by the correction; smallest correction: state the check as "`90c93ea..HEAD` empty for every Out-of-scope path, plus `c02c675..HEAD` empty for the three paths C1 legitimately changed".
LEAD: `_settings_init_sources` still constructs the stock `EnvSettingsSource` and `DotEnvSettingsSource` at HEAD and `settings_customise_sources` then discards them, so every settings build does the full `parse_env_vars(os.environ)` fold twice; cheapest useful check: measure one `load_settings()` call with and without a `__init__` that reuses the discarded sources, and decide in a later cut whether the redundant construction is worth removing.
```