### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-sole-identity
Worker session ordinal: 56
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C7B3
status: PASS
Phase-qualified result: not-applicable
Start commit: `551dd397b3cd5c9c4f5e3b1eec1cd01ea8ba0d4f`
End commit: `7ebf4955e78731170477280c3b7f9f0cdd726e5a`
Report justification: new-mutation
Logical-whole closure: not-closed

Repository gate at start matched the prompt: clean `main` at the expected SHA, public `main` `aee0a60a04b78685608ec5a65ec5780c7d9884e7`, `.ap` gitlink and submodule HEAD `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `ap project check` PASS. Local `main` was ahead of `origin/main` by the three unpublished C7-B commits. That divergence is `unpublished-candidate` and was left unpublished. No NUC, browser, provider, or push.

Changed files: 36 paths in `7ebf495`. Purpose: active documents and live evidence gates now use canonical Kronika names; frozen Part A, product source, parked capture source, and the release engine were not edited.

## 1. Document sweep and gate-rename matrix

Active documents were parsed for retired console names, wrappers, paths, commands, variables, and present-tense product statements. Frozen Part A (86 documents, ADRs 0001–0084 plus `docs/FEDORA_SERVICE.md` and `docs/NUC_HOST_BASELINE.md`) was not edited. `docs/adr/0085-kronika-sole-identity.md` was left byte-unmoved: its retired tokens are the decision text and the named residues.

Replacement rule used on living instructions: `FrameNest` to `Kronika`, `FRAMENEST_` to `KRONIKA_`, `framenest` to `kronika`, after protecting `/opt/framenest/tooling`, `/opt/framenest/capture-current`, `/mnt/framenest-catalog-offdevice`, and the dated historical release path `/opt/framenest/releases/aec2f0091c10aed2fc2033dac154a0d9651b2b6d`. Sentences that the mechanical pass made false were then rewritten.

| Edited document | What changed | What was kept on purpose |
|---|---|---|
| `docs/UBUNTU_NUC_DEPLOYMENT.md` | Current web layout, account, consoles, units, env file, and `kronika-release` commands | Tooling paths, capture pointer, off-device mount, dated release path, historical `.framenest-release-sha` reader note |
| `AGENTS.md` | Removed-wrapper claim; current provenance is `.kronika-release-*` | Same tooling paths; former wrapper names named as removed; historical marker reader note |
| `deploy/ubuntu/README.md` | Canonical release entry and `/opt/kronika/current` | `/opt/framenest/capture-current` |
| `README.md`, `PRODUCT.md`, `SERVER.md` | Current commands, settings, and product name | Dated historical release path; README also keeps the historical sidecar suffix as a reader |
| `DEVELOPMENT.md`, `docs/WORKER_EXECUTION_CONTRACT.md` | Launcher, settings, and evidence gates | None of the old gate names |
| `SECURITY.md`, `docs/ACCEPTANCE_DUAL_AUDIENCE.md`, `docs/X_COMPANION.md` | Required header `X-Kronika-Request`, canonical env and alarm `kronika.review-inbox`; removed “retained until the compatibility window” | Acceptance guide keeps its historical logical-whole id |
| `ROADMAP.md` | Current commands and alarm | S10 cell still says FrameNest was renamed to `kronika` |
| `docs/BACKUP_AND_RECOVERY.md` | Canonical backup consoles, paths, export launcher, and sudoers run-as `kronika` | Mount path; historical marker named as a reader |
| `docs/OPERATOR_NETWORK.md`, `scripts/operator/network/README.md` | Canonical scripts; retired prefixes do not supply defaults; removed wrapper named as removed | Device label `framenest-nuc` |
| `docs/INFOSEC.md`, `SPEC.md`, `COVER_PIPELINE.md`, `AI_WORKSPACE.md`, `DESKTOP.md`, `GALLERY.md`, `docs/ARCHITECTURE_FOUNDATION_EVIDENCE.md`, `docs/adr/README.md`, `.gitignore` | Current product name, package paths, and settings | `.gitignore` still ignores `/.framenest/` as a retired root-local directory |

Scanned and not edited because they contain no retired token: `docs/AP_UPGRADE_OBSERVATIONS.md`, `docs/KRONIKA_ACCESS_INVENTORY.md`.

Every remaining active-document hit was opened after the edit. None states a removed console, wrapper, path, command, or variable as the current way to operate the product.

**Gate rename.** Live opt-in names now read and document `KRONIKA_*`. Default skip is observed. Activation was not run.

| Retired gate | Canonical name | Live sites |
|---|---|---|
| `FRAMENEST_RUN_BROWSER_EVIDENCE` | `KRONIKA_RUN_BROWSER_EVIDENCE` | four `tests/browser_*_evidence.test.js` files, `DEVELOPMENT.md`, `docs/WORKER_EXECUTION_CONTRACT.md` |
| `FRAMENEST_CHROME_BIN` | `KRONIKA_CHROME_BIN` | those four browser files and the worker contract |
| `FRAMENEST_BROWSER_ROLE` | `KRONIKA_BROWSER_ROLE` | `tests/browser_catalog_removal_evidence.test.js` only |
| `FRAMENEST_RUN_REAL_MEDIA_TOOLS` | `KRONIKA_RUN_REAL_MEDIA_TOOLS` | `test_media_analysis_real_tools.py`, `test_cover_workflow_real_tools.py` |
| `FRAMENEST_RUN_NVIDIA_NIM_SMOKE` | `KRONIKA_RUN_NVIDIA_NIM_SMOKE` | `test_nvidia_nim_live.py` |

`docs/adr/0015-deterministic-local-media-analysis-preparation.md` still says `FRAMENEST_RUN_REAL_MEDIA_TOOLS=1`. That ADR is frozen Part A, so the historical sentence stays and only the live tests were renamed.

## 2. Truthfulness and classification

A reader of the active documents now gets the canonical web layout (`/opt/kronika`, user `kronika`, `kronika-*` consoles, `kronika-release`), settings prefix `KRONIKA_`, mutation requirement `X-Kronika-Request: 1`, and the fourteen canonical consoles. The served shell still emits both mutation headers; the server accepts only the canonical header. That dual emission was not changed.

Remaining retired occurrences are not zero. Ledger counts below exclude `tests/contract/test_kronika_identity_retention.py`, which pins the tokens and is class (b).

| Tree | Files | Occurrences |
|---|---:|---:|
| `src` | 184 | 1,606 |
| `tests` | 174 | 1,382 |
| `deploy` | 7 | 78 |
| `scripts` | 0 | 0 |
| `docs` | 84 | 749 |
| `extension` | 0 | 0 |

Root files are outside those prefixes. The content-path set still includes `.gitignore`, `AGENTS.md`, `PRODUCT.md`, `README.md`, `ROADMAP.md`, and `SERVER.md`.

**Residual list for CLOSE**

| Class | What remains |
|---|---|
| (a) Frozen Part A | 86 documents, byte-unmoved, including ADR-0015’s historical gate sentence |
| (b) Historical artifact or provenance | Alembic `sys.modules` alias; accepted historical release markers and sidecar/off-device marker readers; dated release path `aec2f009…`; tooling paths; S10’s “FrameNest to kronika”; acceptance logical-whole id; ADR-0085 and the ADR index citations; `/.framenest/` gitignore entry |
| (c) Negative assertion | Retired prefixes and the removed SSH wrapper named as not accepted; tests that prove old inputs do not configure live behavior |
| (d) Parked capture | Capture pointer `/opt/framenest/capture-current` in the capture units, capture env example, release engine, and the two operator docs; capture state-directory name `framenest-chatgpt-page` in ADR-0085. C8 owns the pointer move |
| (e) Dual mutation header | `src/kronika/adapters/api/web/app.js` still sends `X-FrameNest-Request` and `X-Kronika-Request`. Tests that pin that emission stay |
| (f) Action required | none in the files this grant edited |

`framenest-nuc` in `docs/OPERATOR_NETWORK.md` is a device label beside `ahw`, not a console. This grant had no host observation that the node name changed. It is carried as a host label for C9, not as a current product command.

`FROZEN_ALEMBIC_SHA256` has 36 keys. Part A hashes matched in the retention run. Part B stays empty, with the twenty canonical replacement paths still present.

## 3. Suites

| Suite | Result | Elapsed | Baseline difference |
|---|---|---:|---|
| Full Python, `./.ap/ap exec --operation test` | 4,968 passed; 8 skipped; 3 warnings; 0 failed | 691.01 s | Unchanged |
| Retention module | 15 passed | 0.35 s | Unchanged count; pins updated |
| `companion_web_bridge` | 23 passed, 0 failed | 74.398 ms | Unchanged |
| `companion_review_extension` | 41 passed, 0 failed | 172.065 ms | Unchanged |
| `x_companion_extension` | 55 passed, 0 failed | 118.272 ms | Unchanged |
| `companion_settings_automatic_analysis` | 6 passed, 0 failed | 10,067.232 ms | Unchanged |
| `kronika_ui` | 12 passed, 0 failed | 87.238 ms | Unchanged |
| `catalog_card_ai_quick_action` | 30 passed, 0 failed | 208.308 ms | Unchanged |
| Bounded non-browser JS glob | 212 passed, 0 failed | 723.966 ms | Unchanged |

The eight skips are five cover-workflow cases, two media-analysis cases, and one NVIDIA smoke case. Their skip reasons name `KRONIKA_RUN_REAL_MEDIA_TOOLS` and `KRONIKA_RUN_NVIDIA_NIM_SMOKE`. The three warnings are the existing Pydantic `OMITTED` schema warning. JavaScript used `node --test` from the worktree root. Browser-evidence suites were not activated.

## 4. Commit, Part A, Part B, Part C

`git diff --stat HEAD~1`: 36 files, 906 insertions, 883 deletions. SHA `7ebf4955e78731170477280c3b7f9f0cdd726e5a`. Working tree clean. No push.

Part A is not in the diff. Part B remains empty.

Part C, measured from `551dd39`, excluding the ledger file:

| Tree | Files | Occurrences |
|---|---|---|
| `src` | 184 + 0 = 184 | 1,606 + 0 = 1,606 |
| `tests` | 178 − 4 = 174 | 1,445 − 63 = 1,382 |
| `deploy` | 7 + 0 = 7 | 95 − 17 = 78 |
| `scripts` | 1 − 1 = 0 | 9 − 9 = 0 |
| `docs` | 88 − 4 = 84 | 1,184 − 435 = 749 |
| `extension` | 0 + 0 = 0 | 0 + 0 = 0 |

| Scalar | Arithmetic |
|---|---|
| `FRAMENEST_[A-Z0-9_]+` | 228 − 112 = 116 |
| Distinct names | 57 − 13 = 44 |
| Bare `FRAMENEST_` | 22 + 0 = 22 |
| Capitalized `FrameNest` | 2,607 − 280 = 2,327 across 365 − 22 = 343 files |
| Mutation header `X-FrameNest-Request` | 43 − 6 = 37 across 19 − 3 = 16 files |
| `/opt/framenest` | 214 − 62 = 152 |
| `/etc/framenest` | 51 − 21 = 30 |
| `/var/lib/framenest` | 87 − 23 = 64 |
| `/var/cache/framenest` | 26 − 7 = 19 |
| `/mnt/framenest-catalog-offdevice` | 23 + 0 = 23 |
| `User=framenest` | 6 − 2 = 4 |
| `Group=framenest` | 6 − 1 = 5 |

Token deltas: root −45, docs −39, tests −27, scripts −1, src 0, deploy 0. The thirteen names that no longer occur anywhere outside the ledger are `FRAMENEST_AI_MODEL_ID`, `FRAMENEST_AI_PROVIDER_ID`, `FRAMENEST_BROWSER_ROLE`, `FRAMENEST_CHROME_BIN`, `FRAMENEST_COMPANION_EXTENSION_ORIGINS`, `FRAMENEST_CURL_BIN`, `FRAMENEST_DEVELOPMENT_LOG_DIR`, `FRAMENEST_INGRESS_MODE`, `FRAMENEST_LOCAL_OWNER_LOGIN`, `FRAMENEST_NETWORK_TEST_HOOKS`, `FRAMENEST_NUC_SSH_` (the glob spelling), `FRAMENEST_RUN_BROWSER_EVIDENCE`, and `FRAMENEST_RUN_NVIDIA_NIM_SMOKE`. No distinct name was added. `FRAMENEST_RUN_REAL_MEDIA_TOOLS` remains only in frozen ADR-0015.

**Content-path departures (16), no additions:** `AI_WORKSPACE.md`, `COVER_PIPELINE.md`, `DESKTOP.md`, `DEVELOPMENT.md`, `GALLERY.md`, `SECURITY.md`, `SPEC.md`, `docs/ARCHITECTURE_FOUNDATION_EVIDENCE.md`, `docs/INFOSEC.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `docs/X_COMPANION.md`, `scripts/operator/network/README.md`, `tests/contract/test_recovery_cli.py`, `tests/integration/test_cover_workflow_real_tools.py`, `tests/integration/test_media_analysis_real_tools.py`, `tests/integration/test_nvidia_nim_live.py`.

## 5. Sites no test exercises

The full suite and the document-pin tests cover the release runbook commands, the operator-runbook service-account lines, the backup sudoers line, the product automatic-analysis setting name, and the absence of the old SSH wrapper in `AGENTS.md` and the worker contract. They do not exercise most rewritten sentences in `SPEC.md`, `SECURITY.md`, `PRODUCT.md`, `COVER_PIPELINE.md`, `X_COMPANION.md`, `DESKTOP.md`, `AI_WORKSPACE.md`, `GALLERY.md`, or `docs/ARCHITECTURE_FOUNDATION_EVIDENCE.md`.

The renamed gates were proved only in the default-skip direction. Browser suites were not activated, as this grant forbids that. Real-media and NVIDIA suites were not activated, because that would run real tools or a live provider call.

## 6. Deviations, risks, missing evidence, next step

No product source, capture source, release engine, frozen document, dependency, or Alembic revision changed. The release engine’s module-level constants still describe the former web layout; routine commands select the layout from the host. The runbook now documents the canonical layout that `kronika.service` and `NEW_WEB_LAYOUT` name.

Missing evidence: gate activation under `KRONIKA_*=1` was not run. `framenest-nuc` was not checked against the live node name. Line-by-line classification of the untouched `src` and `tests` residue was not repeated in this session; those files are outside this diff except the gate and document-pin tests, and their counts are the measured ledger.

Smallest next step: Orchestrator acceptance of `7ebf495`, then the publication, exact-main NUC refresh, and rendered regression acceptance that close C7-B. This prompt does not authorize those.

Resolved Execution Issues / Near-Misses: One `python3` process was started with a comment-only script while building the frozen-path list; it performed no read of repository logic and was not repeated. The first full-suite invocation passed trailing argv to `--operation test`, which rejects trailing argv and ran no tests; the suite was then run as `--operation test` with no trailing argv. A `grep` for TAP `ok` lines reported zero because Node’s reporter uses `✔` and `ℹ`; the `ℹ tests` / `ℹ pass` lines are the counts above.
Pre-Existing Failure Classification: none

Authority expiry: this terminal report ends the grant; no further implementation, second commit, push, publication, refresh, or host contact.

Orchestration critique:
MEASURED: `--operation test` rejects trailing argv, so the prompt’s `[-- <argv>]` form does not apply to the full suite. Evidence: the first invocation printed `operation test does not allow trailing argv` and ran nothing. Effect: the full suite must be `--operation test` with no extra pytest flags. Smallest correction: none for this result.
LEAD: `framenest-nuc` may be a live Tailscale node name or a stale label. Cheapest check: Cooperator confirmation of the current node name before C9.