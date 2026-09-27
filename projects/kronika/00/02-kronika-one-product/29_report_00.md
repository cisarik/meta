### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 29
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S4-A-CONTRACTS-ACCEPTANCE
status: PASS
Phase-qualified result: acceptance-PASS
Result artifact or commit: 40e51cb2d061ead96850c9c94aa59de54d5e1310
Result evidence: read-only candidate inspection, declared route, one temporary probe root
Start commit: 40e51cb2d061ead96850c9c94aa59de54d5e1310
End commit: 40e51cb2d061ead96850c9c94aa59de54d5e1310
Logical-whole closure: not-closed
Report justification: final-acceptance

Independence posture: this session began with the acceptance prompt. It did not implement or correct the S4-A row and it did not receive a prompt from another session. Verdicts come from the candidate tree, the parent blob `75e9b07b2bf2269568382e28d40a8d2ff8d4bc28:src/framenest/adapters/cli/ai.py`, the declared route, and the synthetic probe. ADR-0083 and the S4-A implementation prompt were used as the owner-map contract for field scope. Implementation and correction reports were not used as reasoning. Requested reasoning: High. This session does not self-verify a model identity.

Changed files: none in the FrameNest checkout. The only write is this report. Purpose: fresh independent acceptance of the S4-A research contracts, schema v3, and the CLI preservation correction. No product correction.

Tests and validation: declared route, both exit 0. `ap project check` PASS. `ap exec` test-focus: 451 passed. Probe exit 0. Details are in the control matrix.

Git result: no stage, commit, or push in either repository. The candidate is not on local `origin/main`. This session did not publish it.

Deviations: none in the candidate. Risks and missing evidence: no adapter and no live provider call are in this row; the live public ref was not re-queried because host contact is forbidden. See residual limitations.

Smallest next step: record this acceptance, then issue the S6 records, access and approval grant.

## Acceptance and Correction Record

```text
Acceptance candidate: 40e51cb2d061ead96850c9c94aa59de54d5e1310
  (tree ec3c6c9db49ede4bfcd3616263b388bb26451834, branch feat/kronika-one-product,
   parent 75e9b07b2bf2269568382e28d40a8d2ff8d4bc28)
Acceptance owner map: the S4-A row delta against 72009c3b525b6a46e87223cb9a143b5079d89cbf
  (10 paths: the 8 implementation paths plus the 2-path CLI preservation
  correction); implementation report 27_report_00.md; correction report
  28_report_00.md; the accepted plan and ADR-0083
Acceptance allowlist: read-only review of the candidate and governing AP; the
  declared focused route; one declared temporary probe root under /tmp
Acceptance risk claims: the seven fixed claims below
Acceptance control matrix: the fixed positive and negative controls, executed below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: none
```

Issued record had `Primary fresh acceptances used: 0`. This exchange is that primary fresh acceptance, so the completed count is 1. No out-of-scope observation was recorded.

## Identity observed

Checkout `/home/agile/Projects/framenest`, branch `feat/kronika-one-product`, clean index and worktree before the route, after the route, and after the probe. `git rev-parse HEAD 'HEAD^{tree}' 'HEAD^'` exited 0:

```text
40e51cb2d061ead96850c9c94aa59de54d5e1310
ec3c6c9db49ede4bfcd3616263b388bb26451834
75e9b07b2bf2269568382e28d40a8d2ff8d4bc28
```

HEAD subject: `fix(kronika): preserve research configuration in AI CLI writers`. Parent subject: `feat(kronika): add provider-neutral research contracts and configuration`. Governing AP gitlink and `.ap` HEAD: `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`. Local `main` and `origin/main`: `fd277a9a64a6965df76127dbec5b1735d2fb3cdd`. No upstream is configured for `feat/kronika-one-product`. `git branch -r --contains HEAD` printed no ref. `git merge-base --is-ancestor HEAD origin/main` exited 1. `private/**` was not read. No host, SSH, gate, sudo, service, provider, or credential action was performed. The live public ref was not contacted.

## Per-claim verdicts

### 1. Domain contracts — established

`src/framenest/domain/research.py` imports only `__future__`, `dataclasses`, and `enum`. Operation kinds are `search` and `research`. Lifecycle states partition into five non-terminal states (`admitted`, `submitting`, `running`, `validating`, `cancel_requested`) and seven terminal states (`saved`, `refused`, `failed`, `incomplete`, `cancelled`, `timeout`, `submission_unknown`), with no overlap. Remote cleanup (`not_required`, `pending`, `deleted`, `failed`, `unknown`) and accounting (`reserved`, `reconciled`, `unknown`) are separate enums on the request record. The provider descriptor, request, and observation values are frozen. Usage and prices are integers in micro-USD: one token at one micro-USD per million rounds up to `1`, and a float price is rejected. There are 22 stable `E_*` codes. `ResearchValueError` carries the fixed message `research value is invalid.` A raw string cannot be stored as `ProviderObservation.error_code`; that constructor raises `ResearchValueError` and the submitted text was absent from the message. `tests/unit/test_import_boundaries.py` is inside the passing focused route and scans the domain tree, including this module.

### 2. Application ports — established

`src/framenest/application/ports/research.py` defines `ResearchProvider`, `ResearchRequestRepository`, `ResearchBudgetLedger`, and `ResearchResultCompletion`, and nothing else. Its FrameNest import is only `framenest.domain.research`, plus `__future__` and `typing`. A synthetic fake satisfied all four protocols. Every provider method (`describe`, `submit`, `poll`, `cancel`, `release_remote`), both repository writes, both ledger methods, and `complete` returned the expected typed outcome.

### 3. Registry and selection — established

`openai-responses` is `unconfigured`, with search and research capabilities, and `submission_idempotency` `not_guaranteed`. `chatgpt-page` is `parked` with both capabilities false. `require_selectable` on it returns `E_CAPABILITY_UNAVAILABLE` for search and for research. `self-hosted` is a constant, is not in `RESEARCH_PROVIDER_DESCRIPTORS`, and selection returns `E_NOT_CONFIGURED`. The only registry ids are `chatgpt-page` and `openai-responses`. `select_research_provider` returns a frozen snapshot. After the source configuration's search deadline changed from 180 to 30, the original snapshot stayed at 180 and the later snapshot was 30. `live_ready` stayed false on an enabled configuration, and the descriptor stayed `unconfigured`. Disabled and missing configuration both return `E_DISABLED`. A disabled configuration does not select another provider. The configuration object rejects `provider_id` `chatgpt-page`, so selection cannot retarget. `ProviderRequest` has no endpoint, model, tool, api-key, or html field. `select_research_provider` takes only `config` and `kind`. No `class Fake` exists under `src/`. The research fake used by the contract test is in `tests/contract/test_research_provider_contract.py`. The probe's fake lived only under the temporary root.

### 4. Configuration schema v3 — established

`AI_CONFIG_SCHEMA_VERSION` is 3 and the accepted set is `{1, 2, 3}`. Synthetic version 1 and version 2 files kept identical bytes after `load_ai_server_config`. Loaded media selection matched the file, and `research` was `None`. Saving those loaded objects wrote schema 3, preserved the active provider, provider models, and, for version 2, the declared provider records (`providers` compared equal), and omitted `research`. A version 3 file with no `research` key loaded as `None` and a save did not invent the key. A present disabled research section round-tripped with the declared provider record, `enabled` false, the credential identifier name `KRONIKA_RESEARCH_OPENAI_API_KEY`, and no `endpoint` key. Unknown, secret-shaped, endpoint, out-of-range, boolean, null, and extra top-level values were rejected with `AiConfigurationError`. The submitted secret and endpoint were absent from the exception text and from its cause. The source bytes were unchanged. Versions `999`, `4`, `"3"`, `3.0`, `true`, and `null` were rejected the same way. Default research is disabled. Search limits are `3, 4096, 180, 500000, low`. Research limits are `20, 32768, 1800, 5000000, high`. Daily and monthly budgets are `10000000` and `30000000` micro-USD.

### 5. CLI preservation — established

The correction diff against `75e9b07b2bf2269568382e28d40a8d2ff8d4bc28` is two paths: four added lines in `src/framenest/adapters/cli/ai.py` and the regression in `tests/unit/adapters/cli/test_ai_cli.py`. Each added line passes `research`. `configure_command`, `configure_non_interactive_command`, and `provider_add_command` pass `None` when no configuration was loaded. `provider_remove_command` passes `existing.research` and raises `AiConfigurationError` before writing when nothing was loaded, so it does not create a file and does not invent a section. No prompt, message, or other control-flow line is in that diff. `git diff --exit-code` for `src/framenest/adapters/api/ai_admin_api.py`, `tests/contract/test_ai_provider_admin_api.py`, and `tests/contract/test_ai_server_composition.py` against `72009c3b525b6a46e87223cb9a143b5079d89cbf` exited 0.

On the candidate, the four writers kept a present research section and did not invent one when the loaded section was absent. Media selection stayed `vercel-ai-gateway` and the declared `opencode-go` record stayed equal. With no file loaded, the three writing commands created a file without a `research` key, and remove rejected the call with `created=0`.

On the parent blob, none of the four functions passes a `research` keyword. Executing each parent function on a file that had a research section returned 0, removed the section, and kept the active provider and the `opencode-go` record. That is the behavior the candidate regression rejects. The candidate regression is included in the 451 passing tests.

### 6. Containment — established

`git diff --name-status 72009c3b525b6a46e87223cb9a143b5079d89cbf HEAD` is exactly these ten paths, `2320` insertions and `9` deletions:

```text
M	src/framenest/adapters/cli/ai.py
A	src/framenest/application/ports/research.py
A	src/framenest/domain/research.py
M	src/framenest/infrastructure/ai/configuration.py
A	src/framenest/infrastructure/ai/research_configuration.py
A	src/framenest/infrastructure/ai/research_registry.py
A	tests/contract/test_research_provider_contract.py
M	tests/unit/adapters/cli/test_ai_cli.py
M	tests/unit/infrastructure/ai/test_ai_configuration_storage.py
A	tests/unit/infrastructure/ai/test_research_registry.py
```

The six production files in that set import no `httpx`, `requests`, `openai`, `urllib`, `socket`, `aiohttp`, `fastapi`, `sqlalchemy`, or `pydantic`, and they contain no `http://`, `https://`, `sk-`, `Bearer `, or `api.openai.com` literal. The only `def submit` among them is the port. `.ap`, `AGENTS.md`, and `docs/AP_UPGRADE_OBSERVATIONS.md` are not in the diff. No migration, packaging, API, or UI path is in the diff. This session did not push. No remote-tracking ref contains HEAD.

### 7. Evidence honesty — established

The shipped descriptor is `unconfigured`. `live_ready` is false. Default and absent research are disabled. The registry does not contain a vendor price table or an adapter. This acceptance does not claim live readiness, account access, a price schedule, or provider behavior.

## Control matrix

Positive controls, from `/home/agile/Projects/framenest`:

```text
git rev-parse HEAD 'HEAD^{tree}' 'HEAD^'
exit 0
40e51cb2d061ead96850c9c94aa59de54d5e1310
ec3c6c9db49ede4bfcd3616263b388bb26451834
75e9b07b2bf2269568382e28d40a8d2ff8d4bc28

git diff --name-status 72009c3b525b6a46e87223cb9a143b5079d89cbf HEAD
exit 0
10 paths, listed in claim 6

git status --porcelain
exit 0
empty before the route, after the route, and after the probe

./.ap/ap project check --root /home/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310
exit 0
ap project check --baseline: PASS
WARN sanitized inherited environment classes: LD_LIBRARY_PATH SSH_AUTH_SOCK VIRTUAL_ENV_DISABLE_PROMPT PROMPT_COMMAND APPDIR APPIMAGE PATH

./.ap/ap exec --root /home/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310 --operation test-focus -- tests/unit/adapters/cli/test_ai_cli.py tests/unit/infrastructure/ai tests/unit/test_import_boundaries.py tests/contract/test_ai_server_composition.py tests/contract/test_ai_provider_admin_api.py tests/contract/test_research_provider_contract.py -q -p no:cacheprovider
exit 0
451 passed in 9.58s
same inherited-environment WARN, then OK execution trust for baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310
```

Negative and adversarial controls, under `/tmp/kronika-one-product-s4a-acceptance`, mode `0700`, synthetic data, probe exit 0:

- Fake provider: all four ports, calls `describe,submit,poll,cancel,release_remote`, all seven observation kinds. No dataclass field named `html`, `raw`, `provider_text`, or `body`. An `html` keyword was `TypeError` and did not echo the submitted value. A raw error string was `ResearchValueError` and did not echo. Answer text remains an opaque string; that is the documented text channel, not a trusted HTML field.
- Configuration: versions 1, 2, and 3, absent and present research, and the malformed cases in claim 4. Every rejection left the file bytes unchanged and did not echo the submitted secret or endpoint.
- Snapshot: frozen, stable across a deadline change, `live_ready` false. Disabled and missing selection return `E_DISABLED` and do not change the earlier snapshot's provider.
- Parked provider: `E_CAPABILITY_UNAVAILABLE` for new search and research. `self-hosted` is not selectable (`E_NOT_CONFIGURED`).
- CLI: present and absent research through all four candidate writers; missing file through the three writers and the remove rejection. Parent writers drop a present section, as recorded in claim 5.
- Leak hunt: ten paths; no endpoint field, credential value, adapter, network import, API, UI, migration, AP change, or dependency change in that diff.

## Findings

none

## Containment and cleanup

```text
Temporary root: /tmp/kronika-one-product-s4a-acceptance
Owner: this Worker session
Mode: 0700
Contents class: synthetic fixtures only
Cleanup owner: this Worker session
Cleanup outcome: removed
```

The root was removed with `rm -rf` of that exact path. A following existence test confirmed it was gone. The FrameNest index and worktree stayed clean. HEAD stayed `40e51cb2d061ead96850c9c94aa59de54d5e1310`.

## Residual risk and limitations

This row does not ship an adapter, a network client, an API, or a UI. Live account access, vendor prices, and provider behavior were not exercised and are not claimed. Answer text is an opaque string because no renderer exists in this row. ADR-0083 settings that belong to a later adapter (`endpoint`, `store`, `tool_choice`, concurrency, retries) are not stored here.

A version 1 or 2 file that already contains a `research` key is not rewritten by the read, and the loaded object ignores that key. A later save of that object would omit it. Well-formed version 1 and 2 files, which have no research section, read losslessly.

The live public `refs/heads/main` was not re-read. Local `origin/main` remains `fd277a9a64a6965df76127dbec5b1735d2fb3cdd`, and no remote-tracking ref contains the candidate.

## Orchestration critique

```text
Orchestration critique:
MEASURED: none
LEAD: live public refs/heads/main was not re-queried; host contact is outside this grant. Local origin/main is fd277a9a64a6965df76127dbec5b1735d2fb3cdd and no remote-tracking ref contains the candidate. A publication grant can re-read the public ref.
Resolved Execution Issues / Near-Misses: the probe's first CPython launch inherited the AppImage LD_LIBRARY_PATH and aborted before importing the standard library. Unsetting that variable, which ap exec already sanitizes, let the probe run. A first baseline-module load also failed until the module was registered in sys.modules. Both were probe-harness faults. The candidate was not modified. The final probe exited 0.
Pre-existing Failure Classification: none
```

Authority expiry: this terminal report ends the grant; no autonomous continuation.
