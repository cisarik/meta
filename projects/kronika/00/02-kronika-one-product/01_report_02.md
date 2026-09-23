### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 01
Worker exchange ordinal: 03

Task identity: KRONIKA-ONE-PRODUCT-S1
Persistent role identity: WORKER
Worker session profile: Implementation Worker
Phase: implementation
Native planning mode: not-used
Worker session target: current-worker-session
Evidence posture: non-independent
Independence required: no
Status: PASS
Phase-qualified result: implementation-PASS
Report justification: new-mutation

S1 is implemented and locally committed. The existing capture kernel is packaged once as `kronika_capture`; the executable vendor copy is retired. Both console entry points resolve to the same callable. Focused checks passed before and after vendor retirement. This report does not constitute independent acceptance or logical-whole closure.

#### Repository and commit evidence

- Primary checkout: `/home/agile/Projects/framenest`.
- Branch: `feat/kronika-one-product`.
- Start commit and final commit parent: `93e7742d56d46d4725d4561bd8751b15e55e5eb5`.
- Start tree: `b357c765f8ca03c03cbbe0b087b98b6aa14a75e9`.
- End commit: `96ef426f7026c818f5e75733e8f8dfc5ac2321d1`.
- End tree: `570e99abb77b062b7a3ac3c6f7f9f0be5d74dda3`.
- Subject: `feat(capture): relocate kernel into kronika_capture`.
- Exactly one commit above the assigned baseline; clean index and worktree after commit.
- Local `main` and `origin/main` both remain `26d28b16c08a5e7e0179a32c16646bfdc1009c81`. These are local ref observations; no remote query was made.
- AP gitlink and detached submodule HEAD remain `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`; submodule clean.
- Source checkout remains clean at `66c40d43c577276b0ad304a494fbbb1ffb6fc933`.
- Commit result: success; no push. No Meta artifact was staged or committed.

The continuity anchor and prepared S1 prompt were checked before mutation. The assigned baseline, clean checkout, topology, branch, refs, source inventory, AP pin, report destination and development route were re-established from current evidence.

#### Changed files and purpose

The expanded final diff (`--no-renames`) exactly matches the 79 authorized paths: 33 additions, 11 modifications and 35 deletions. Rename-aware Git reports 48 changed files.

- Added all 32 prescribed files under `src/kronika_capture/`; removed their 32 old counterparts under `vendor/kronika-ask/src/kronika/`.
- Python changes are namespace imports, the resource package lookup and package documentation. The package initializer describes the private capture kernel. The existing CLI behavior, state paths, logger names and protocol remain unchanged.
- All 18 browser assets are byte-identical to the baseline copies. The other files were compared against their baseline counterparts with the allowed namespace/documentation substitutions; the initializer's documentation-only difference was inspected separately.
- Modified `pyproject.toml`: package from `src`, relocate the asset include, add `kronika-capture = "kronika_capture.cli:main"`, and retain `framenest-chatgpt-page` as a documented alias to that same callable. Project identity, version, dependencies and lockfile are unchanged.
- Added `docs/provenance/kronika-capture.json` before removing `vendor/kronika-ask/upstream.json`.
- Deleted unreferenced vendor-path scaffolding: `tests/support/chatgpt_page_import.py` and `tests/unit/chatgpt_page/conftest.py`.
- Updated imports in `tests/unit/chatgpt_page/test_bridge_security.py`, `test_cli_surface.py`, `test_job_limits.py` and `test_projects.py`.
- Updated `tests/contract/test_chatgpt_page_packaging.py` to verify all capture files, resources, provenance, wheel contents and both entry points, including imports from the isolated extracted wheel.
- Updated `tests/contract/test_chatgpt_page_js_syntax.py` and `tests/chatgpt_page_protocol.test.js` for the new asset root; retained existing protocol and syntax assertions.
- Extended `tests/unit/test_import_boundaries.py`, `test_package_import.py` and `test_api_import_boundary.py` for source-layout resolution and package independence while preserving existing assertions.

There is no change under `src/framenest/**`, no dependency/environment change and no additional documentation change.

#### Ordered retirement and validation

The prescribed sequence was followed: create the relocated package and provenance, update packaging/tests, pass the focused checks with the old vendor copy still present, remove the exact vendor files, pass the same checks again, and commit the single-implementation tree.

Exact validation commands, run from the primary repository root:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 93e7742d56d46d4725d4561bd8751b15e55e5eb5

./.ap/ap exec --root /home/agile/Projects/framenest --baseline 93e7742d56d46d4725d4561bd8751b15e55e5eb5 --operation test-focus -- tests/unit/chatgpt_page tests/contract/test_chatgpt_page_packaging.py tests/contract/test_chatgpt_page_js_syntax.py tests/unit/test_import_boundaries.py tests/unit/test_package_import.py tests/unit/test_api_import_boundary.py -q -p no:cacheprovider

node --test tests/chatgpt_page_protocol.test.js
```

Results:

- AP project check: PASS before mutation and after commit against the exact assigned baseline. The declared sanitized environment policy was used; inherited-environment sanitization warnings were informational.
- Focused Python route before vendor deletion: 32 passed in 2.41 seconds.
- Focused Python route after vendor deletion: 32 passed in 2.43 seconds.
- Standalone Node protocol suite: 3 passed, 0 failed, 0 skipped, both before and after deletion.
- The Python contract also checks JavaScript syntax and invokes the protocol suite.
- CLI coverage retains argv/stdin prompt input, stdout answers and rejection of `-f`/`--file`. Protocol tests retain protocol v1, the unused upload locator and fail-closed handling of removed modes/kinds.
- Resource tests resolve every asset through `importlib.resources` and `packaged_extension_path`.
- Import checks cover FrameNest domain/application exclusion of capture, capture exclusion of FrameNest, capture exclusion of the FastAPI stack and capture resolution from `src`.
- Final `git diff --check` passes. Final expanded path inventory matches the allowlist exactly; unstaged and staged changes are absent after commit.
- No obsolete vendor path, vendor import helper, old Python package import or old resource lookup remains in source, tests or packaging. Provenance preserves historical vendor paths as evidence; historical/decision documents were left intact.
- Vendor directory and repository-root `dist/` are absent.
- Protected paths are unchanged: `src/framenest`, `.ap`, `.gitmodules`, `AGENTS.md` including its managed block, `ap.project.conf`, `docs/AP_UPGRADE_OBSERVATIONS.md` and `poetry.lock`.

#### Wheel inventory

The existing packaging test built the FrameNest wheel through its internal `poetry build`. It verified unique archive names, exactly the 32 expected files under `kronika_capture/`, byte equality with each source file, and no `kronika/` or `vendor/` package entries.

Capture inventory: 14 Python files and 18 assets. Paths below are relative to `kronika_capture/`:

```text
__init__.py
__main__.py
cli.py
client.py
config.py
errors.py
paths.py
projects.py
bridge/__init__.py
bridge/auth.py
bridge/jobs.py
bridge/results.py
bridge/server.py
bridge/store.py
_assets/extension/src/adapters/adapter.js
_assets/extension/src/adapters/pack_v5.json
_assets/extension/src/engine/dom_engine.js
_assets/extension/src/engine/index.js
_assets/extension/src/engine/interventions.js
_assets/extension/src/protocol.js
_assets/extension/src/url_guard.js
_assets/extension/src/headless/bridge_client.mjs
_assets/extension/src/headless/cdp_client.mjs
_assets/extension/src/headless/driver.mjs
_assets/extension/src/headless/job_engine.mjs
_assets/extension/src/headless/login_server.mjs
_assets/extension/src/headless/probe.mjs
_assets/extension/src/headless/resource_policy.mjs
_assets/extension/src/headless/runner.mjs
_assets/extension/src/headless/login_app/app.css
_assets/extension/src/headless/login_app/app.js
_assets/extension/src/headless/login_app/index.html
```

Within the authorized packaging test, an isolated child interpreter imported the extracted wheel without checkout paths or installed site packages. Both metadata entry points loaded the same `kronika_capture.cli.main` function; all 18 assets resolved; no FrameNest module was imported. This probe did not invoke either CLI or start a browser/provider. No standalone ambient Python route was used.

#### Provenance evidence

The new manifest records:

- Schema version 1.
- Original repository `https://github.com/cisarik/kronika.git`, full source commit `66c40d43c577276b0ad304a494fbbb1ffb6fc933` and tree `848f247434deea4c217170c012612b39e41557f3`.
- FrameNest baseline commit/tree and old manifest path/blob, preserving the already-adapted vendor origin separately from the original Kronika origin.
- Every one of the 32 relocated files: original source path/blob, destination, disposition, feature, adaptation summary and prior FrameNest path/blob/disposition.
- All six excluded-feature records from the prior manifest: `extension/src/job_runner.js`, `pyproject.toml`, `scripts/kronika`, `scripts/dev-setup.sh`, `extension/src/headless/deep_research.mjs` and `extension/src/headless/capture_assets.mjs`, including their exclusion reasons and source evidence.

All 32 recorded FrameNest file blobs were checked against the assigned baseline; all 38 original source blobs (relocated plus excluded) were checked against the pinned source commit. The old manifest blob is `3d072d77b6efb76408686d4231cf00e390a75e5a`. The new manifest contains no private checkout paths or circular current-commit field.

#### Deviations, risks and missing evidence

No substantive deviation from the authorized S1 scope. Evidence is implementation self-validation and is non-independent. Only the assigned focused suite was run; no full-suite, sdist, live browser/provider or deployment result is claimed. No modes, upload capability, lifecycle/journal semantics or protocol changes were introduced. No network, credential, private-data, host or environment work occurred.

Smallest next step: the Orchestrator reviews and accepts this S1 candidate and its evidence before issuing a separate bounded S2 implementation grant.

Orchestration critique:
MEASURED: none
LEAD: none
Resolved Execution Issues / Near-Misses: One patch attempt tried to delete and add the same packaging-test path in a single patch. The patch tool rejected it before mutation; a single Update operation applied the intended change. No test or environment failure occurred.
Pre-existing Failure Classification: none

Authority expiry: this terminal report expires the S1 implementation authority. No autonomous S2 work follows.
Logical-whole closure: not closed.
