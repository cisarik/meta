# Kronika one product — S1 one capture package

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 01
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S1
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: the relocation spans packaging, resource lookup and twelve test surfaces, where a wrong namespace or an unresolvable asset can pass source-level tests and fail only in the built wheel; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Current-session renewal

Continuity anchor: terminal PASS report `01_report_01.md` for task
`KRONIKA-ONE-PRODUCT-S0`, Worker session 01, exchange 02, ending at accepted
documentation commit `93e7742d56d46d4725d4561bd8751b15e55e5eb5`.
Authority renewal: that exchange's authority expired at its terminal report.
This exchange grants complete new bounded implementation authority for S1 only.
Reuse rationale: the same healthy session holds the repository-grounded plan and
the exact vendor map; retained understanding reduces import and packaging error.
No independence is required for this relocation.
Repository and environment re-gating: required before mutation; re-establish
every gate below from current evidence, never from memory.
Retained context: convenience only, never authority. On any conflict between
retained context and current repository evidence, stop and report.
Evidence posture: non-independent.
New terminal report: required (`01_report_02.md`).

## Starting state (verified at issuance)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `93e7742d56d46d4725d4561bd8751b15e55e5eb5`, parent
  `26d28b16c08a5e7e0179a32c16646bfdc1009c81`, tree
  `b357c765f8ca03c03cbbe0b087b98b6aa14a75e9`, subject
  `docs(kronika): record one-product architecture and private records`; clean
  index and worktree. Local `main` = `origin/main` =
  `26d28b16c08a5e7e0179a32c16646bfdc1009c81` (unmoved).
- Governing AP gitlink and detached `.ap` HEAD:
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- The vendor kernel exists only under `vendor/kronika-ask/src/kronika/**`
  (32 files) plus `vendor/kronika-ask/upstream.json`; `src/kronika_capture/`
  does not exist.
- Python references to the kernel namespace exist in `pyproject.toml` and in
  the capture test files; `src/framenest/**` contains no `kronika` reference.
- `tests/unit/test_import_boundaries.py`, `test_package_import.py` and
  `test_api_import_boundary.py` currently cover only the `framenest` package
  boundaries and contain no kernel reference.

## Implementation authority record

Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Exact baseline: `93e7742d56d46d4725d4561bd8751b15e55e5eb5`
Changed-path allowlist:

```text
src/kronika_capture/**                                  (new; the 32 relocated files)
vendor/kronika-ask/**                                   (deleted; 32 files + upstream.json)
pyproject.toml
docs/provenance/kronika-capture.json                    (new)
tests/support/chatgpt_page_import.py
tests/unit/chatgpt_page/conftest.py
tests/unit/chatgpt_page/test_bridge_security.py
tests/unit/chatgpt_page/test_cli_surface.py
tests/unit/chatgpt_page/test_job_limits.py
tests/unit/chatgpt_page/test_projects.py
tests/contract/test_chatgpt_page_packaging.py
tests/contract/test_chatgpt_page_js_syntax.py
tests/chatgpt_page_protocol.test.js
tests/unit/test_import_boundaries.py
tests/unit/test_package_import.py
tests/unit/test_api_import_boundary.py
```

Implementation boundaries: the positive and negative authority below.
Independence required: no

## Goal

Package the existing capture kernel exactly once under its final namespace:
relocate `vendor/kronika-ask/src/kronika/**` to `src/kronika_capture/**`,
update Python imports, resource lookup, packaging, entry points and the
affected tests, record complete provenance, then retire the executable vendor
copy so one implementation remains in source and distribution. Relocation and
namespace only: no restored modes, no new job semantics, no upload enablement,
no protocol change, no dependency change, no host work.

## Exact relocation map

For every relative path below:

```text
FROM vendor/kronika-ask/src/kronika/<relative-path>
TO   src/kronika_capture/<relative-path>
```

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

All 32 files must be relocated; no vendor file may be left behind and no
duplicate implementation may remain.

## Exact changes

- Python: change `from kronika...` / `import kronika...` to the
  `kronika_capture` namespace in the relocated files; change
  `files("kronika")` in `paths.py` to `files("kronika_capture")`.
- `pyproject.toml`: package `kronika_capture` from `src`; move the packaged
  assets include to `src/kronika_capture/_assets/**/*`; add
  `kronika-capture = "kronika_capture.cli:main"`; change
  `framenest-chatgpt-page` to point at `kronika_capture.cli:main` as a
  documented compatibility alias to the same function. Do not change the
  project name, version, dependencies or lockfile.
- Preserve argv/stdin prompt input, text stdout and the rejection of CLI
  `-f`/`--file`. No behavioral change.
- Keep `kronika_capture` independent of `framenest` application, domain and
  persistence; the application will later talk to capture over the bridge.
- Tests: update the Python imports in `tests/unit/chatgpt_page/**`; remove the
  vendor `sys.path` injection (`tests/support/chatgpt_page_import.py` and the
  conftest that loads it) — delete the now-unnecessary scaffolding only if
  nothing references it, otherwise update it; update
  `tests/contract/test_chatgpt_page_packaging.py` (resource package, wheel
  names, both entry points), `tests/contract/test_chatgpt_page_js_syntax.py`
  (asset root and forbidden-module namespace) and
  `tests/chatgpt_page_protocol.test.js` (asset import paths).
- Extend `tests/unit/test_import_boundaries.py`, `test_package_import.py` and
  `test_api_import_boundary.py` only enough to enforce the new package
  independence both ways: `framenest` domain/application must not import
  `kronika_capture`, and `kronika_capture` must not import `framenest`
  internals. Keep every existing assertion intact.
- Provenance: create `docs/provenance/kronika-capture.json` before removing the
  vendor manifest, preserving its evidence. Required shape:

```text
schema_version
upstreams:
  repository identity
  full source commit (66c40d43c577276b0ad304a494fbbb1ffb6fc933)
  source tree (848f247434deea4c217170c012612b39e41557f3)
files:
  source path
  source blob
  destination path
  disposition: relocated | selectively-ported | adapted
  feature
  adaptation summary
excluded_features:
  source location
  exclusion reason
```

  Relocated, already-modified files identify both the original Kronika origin
  and the FrameNest baseline containing the adaptation. Do not introduce private
  checkout paths or circular “current commit” fields.

## Vendor retirement gate (ordered, one commit at the end)

1. Relocate the 32 files and apply the namespace, packaging, provenance and
   test changes.
2. Verify the relocated package and packaged assets through the focused checks
   below, including the wheel build inside the packaging test.
3. Only then delete `vendor/kronika-ask/**` (the 32 files and `upstream.json`).
4. Re-run the focused checks against the final tree with no vendor copy.
5. Commit only a tree with exactly one implementation. Never commit a partially
   retired duplicate.

## Positive authority

Edit exactly the allowlisted paths; stage exactly those paths; create one
commit. Run the declared route checks below.

Commands (binding route):

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 93e7742d56d46d4725d4561bd8751b15e55e5eb5

./.ap/ap exec --root /home/agile/Projects/framenest --baseline 93e7742d56d46d4725d4561bd8751b15e55e5eb5 --operation test-focus -- tests/unit/chatgpt_page tests/contract/test_chatgpt_page_packaging.py tests/contract/test_chatgpt_page_js_syntax.py tests/unit/test_import_boundaries.py tests/unit/test_package_import.py tests/unit/test_api_import_boundary.py -q -p no:cacheprovider

node --test tests/chatgpt_page_protocol.test.js
```

The packaging test's internal `poetry build` is part of the existing test, not
a new toolchain. No ambient Python, `poetry run`, or substitute route.

## Negative authority

- No functional or behavioral change to the kernel: no Search/Research
  restoration, no new job states, no idempotency/journal work, no attachment
  upload, no protocol/error-code change, no stealth or model/reasoning change.
- No `src/framenest/**` change; no migration, database, API, UI, deploy,
  systemd, host, NUC, browser, provider, network, credential or secret work.
- No dependency, lockfile, project name or version change; no venv rebuild.
- No AP, `.ap`, managed-block, `.gitmodules`, `ap.project.conf` or upgrade
  ledger change.
- No documentation change except the new provenance manifest; do not edit
  `SPEC.md`, ADR-0082 or any other document that mentions the move as history
  or plan.
- No push, publication, remote change, force, amend, rebase, reset, clean,
  stash, `git add -A`, `git add .`, `--no-verify`, `--no-gpg-sign` or config
  write. Do not read `private/**`. No subagents.
- If a required change falls outside the allowlist, stop and report.

## Validation

1. Before mutation and after the commit:
   `./.ap/ap project check` passes against the exact baseline.
2. Focused route: `tests/unit/chatgpt_page`, the two capture contract tests and
   the three import-boundary tests pass; `node --test
   tests/chatgpt_page_protocol.test.js` passes.
3. `test_chatgpt_page_packaging.py` proves the built wheel contains
   `kronika_capture/**` with all required assets and both entry points
   (`kronika-capture` and the retained `framenest-chatgpt-page` alias), and no
   vendor package.
4. `git diff --name-status <baseline>..HEAD` equals the allowlist exactly
   (added, modified and deleted paths); `git status --porcelain` is clean after
   the commit; one commit above the baseline; branch, HEAD, parent and tree
   read back.
5. No source, test or packaging reference to `vendor/kronika-ask` remains;
   historical/decision documents that describe the move (ADR-0082, SPEC.md)
   may still mention it.
6. `kronika_capture` imports resolve from `src`; `importlib.resources` resolves
   the relocated assets; the kernel stays independent of `framenest`.
7. AP pin, managed block, `.gitmodules`, `ap.project.conf` and upgrade ledger
   unchanged; `main` and `origin/main` still at `26d28b16`.
8. Provenance manifest contains every relocated file with source blob and
   destination, and the excluded-feature record.

Evidence before S2: one executable implementation in source and distribution,
complete provenance, and the accepted focused results above.

## Stopping conditions

Stop and report on: baseline, cleanliness, AP-pin or managed-block mismatch; an
unexpected pre-existing change; a needed change outside the allowlist; a
focused check that fails and cannot be corrected inside the allowlist; any
remaining vendor reference after removal; a packaging or provenance failure; a
required dependency or environment change; or any instruction conflict.
Preserve the first causal failure; do not improvise a workaround, and never
commit a partially retired duplicate.

## Completion and report contract

`PASS` means the relocation, packaging, provenance, test updates and vendor
retirement are complete within the allowlist, all validation above passed, and
one commit exists on `feat/kronika-one-product`. Use `PARTIAL` or `BLOCKED`
honestly otherwise. No push occurred.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core: status;
`Phase-qualified result: implementation-PASS` (or `not-applicable` on failure);
start and end commit; changed files and purpose; validation results including
the wheel inventory; commit result with `no push`; deviations/risks/missing
evidence; one smallest next step; `Report justification: new-mutation`;
authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

Direct communication with the Cooperator (the short completion notice) is in
Slovak, masculine address for him. This prompt and the formal report are in
English. Do not use subagents. Do not commit Meta artifacts.

Finalize the report, save it at the exact destination, read it back in full,
and verify its first line, coordinates, content and path before the short
separate completion notice with status, exact report path and SHA-256. Terminal
report, cancellation or supersession expires this authority. Do not continue
autonomously after the report.

## Trace and delivery record

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_implementation_02.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 01_report_02.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
