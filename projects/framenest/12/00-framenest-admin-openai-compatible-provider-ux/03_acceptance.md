# Independent Acceptance Exchange 01 — Session 03 — Whole-Level Fresh Independent Acceptance

Persistent role identity: WORKER
Logical whole identity: framenest-admin-openai-compatible-provider-registry-and-vision-probe
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: Independent Audit
Task identity: ACCEPT-ADMIN-PROVIDER-REGISTRY-AND-VISION-PROBE
Delivery route: Agent Orchestrator default dispatch (this fresh session received only this prompt text as its initial context; it did not materially implement the candidate)
Reasoning recommendation: High — named risk: this acceptance covers a security-sensitive provider/credential boundary, six new mutating routes, audit-before-mutation, and normative documentation; claims must be verified directly, not trusted from prior Worker reports
Recommended context capacity: approximately 250k tokens
Independence required: yes (fresh independent acceptance)
Sub-agents or internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Development envelope activation: not-used

## Independence posture

You are a genuinely fresh Worker session. You did not materially implement
the candidate below. You must not rely on any prior Worker report as proof;
prior reports are claims. The candidate's implementation reports exist in the
same trace directory and you may read them as claims only. If you discover
that this session inherited parent-conversation history or reasoning, or that
you materially participated in this implementation, STOP and report it — the
acceptance is invalid.

You have NO correction authority. Read-only inspection and read-only
execution only. If you find a defect, report it precisely; do not fix it.

## Acceptance and Correction Record

```text
Acceptance candidate: 87411e040157c51f3e1056e8a6e62c0c8c514018 (local commit on feat/x-meme-browser-companion)
Acceptance owner map: provider configuration schema (src/framenest/infrastructure/ai/provider_records.py, configuration.py), generic adapter (openai_chat_completions.py), registry and dynamic resolution (registry.py), credentials (credentials.py), CLI (src/framenest/adapters/cli/ai.py), admin API (src/framenest/adapters/api/ai_admin_api.py), ingress route policy (tailscale_ingress.py), application composition (application.py), capability endpoints (media_suggestion_api.py, media_analysis_lifecycle_api.py), web shell (web/index.html, web/app.js, web/styles.css), deploy source material (deploy/systemd/framenest-ai-credential-opencode-go.conf, deploy/ubuntu/production_ai_deploy.py), living docs (SPEC.md §22, SECURITY.md, SERVER.md, README.md, AI_WORKSPACE.md, docs/UBUNTU_NUC_DEPLOYMENT.md, docs/adr/0081-*.md, docs/adr/README.md)
Acceptance allowlist: exactly the paths changed by 33946e08447dc92621ed6844b4b5d13a19ec29f1..87411e040157c51f3e1056e8a6e62c0c8c514018
Acceptance risk claims: R1 no secret value in v2 config, API responses, browser surfaces, or logs; R2 admin routes cannot bypass authN/authZ (provider.operate, mutation origin proof, audit-before-mutation, absent from the public composition); R3 ping/pong/analyze privacy (text-only ping; pong sends exactly one committed synthetic fixture with explicit confirmation; no catalog media; no suggestion persistence; no raw completion leakage); R4 v1 config read compatibility loses nothing and invents nothing; malformed config fails closed; R5 dynamic resolution takes effect without restart and does not widen authorization or silently change movie identification; R6 NVIDIA/Vercel behavior and frozen Gallery/Details visuals unregressed; R7 repository hygiene (only allowed paths changed, .ap untouched, no push)
Acceptance control matrix: see "Controls" below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

## Candidate and baseline

- Repository: `/home/agile/Projects/framenest`,
  `https://github.com/cisarik/framenest`.
- Baseline: `33946e08447dc92621ed6844b4b5d13a19ec29f1` (published `main`).
- Candidate chain: `33946e0 → f41df79 → 980db7a → e6d91d1 → c66f5b6 → 810b606 → 87411e0`.
- Candidate under acceptance: `87411e040157c51f3e1056e8a6e62c0c8c514018`.
- Candidate state: local commits only, no push; branch ahead of
  `origin/feat/x-meme-browser-companion` by six commits; porcelain clean.
- Candidate access is local and authoritative for this acceptance; no public
  ref claim is under decision. Do not fetch; no network.

## Mandatory reading

- `.ap/AP.md` WORKER spine, especially RF-03, RF-05 (independence), RF-06,
  RF-07 (evidence tiers), RF-12, RF-18, §8, §12, §18;
  `.ap/AP_WORKER.md`; `.ap/PROMPT_CONTRACTS.md` Worker Report Header and the
  Acceptance and Correction Record.
- The accepted plan
  `/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/01_report_orchestrator.md`
  §3-§13 (binding design and control expectations).
- The implementation reports in the trace directory
  (`02_report.md` … `02_report_06.md`) as claims only.
- The changed code and tests (read the diff, not only the summaries):
  `git diff --stat 33946e0..87411e0` and the full `git diff` for the
  security-relevant files.

## Repository gate (read-only)

Independently verify before substantive review: physical root, canonical
remote, branch `feat/x-meme-browser-companion`, HEAD equal to the candidate,
porcelain clean, `.ap` gitlink equal to `.ap` HEAD
`7478ddb07d2c3911f79e1aa1441f0115a31c45d8`, `./.ap/ap ap doctor` PASS,
`git diff --name-only 33946e0..87411e0` equals the acceptance allowlist
(record the exact count). Classify differences per RF-12; do not repair.

## Controls

Positive controls (must hold with direct evidence):

1. The declared AP route runs the affected Python selection green on the
   candidate:
   `./.ap/ap ap exec --root /home/agile/Projects/framenest --baseline 87411e040157c51f3e1056e8a6e62c0c8c514018 --operation test-focus -- tests/unit/infrastructure/ai tests/unit/adapters/cli/test_ai_cli.py tests/unit/test_configuration.py tests/contract/test_ai_provider_admin_api.py tests/contract/test_tailscale_ingress_security.py tests/contract/test_x_route_policy.py tests/contract/test_public_published_uds.py tests/contract/test_media_suggestion_api.py tests/contract/test_ai_server_composition.py tests/contract/test_automatic_analysis_settings_api.py tests/contract/test_ai_package_resources.py tests/contract/test_local_web_application.py tests/contract/test_web_package_resources.py tests/contract/test_production_ai_deployment.py tests/contract/test_nuc_operator_runbook.py tests/contract/test_nuc_release_docs.py -q -p no:cacheprovider`
2. The frontend suites are green:
   `node --test tests/ai_providers_admin_frontend.test.js tests/tailscale_identity_frontend.test.js tests/companion_settings_automatic_analysis.test.js`.
3. `tests/contract/test_tailscale_ingress_security.py` proves the route
   inventory 1:1 and the six new routes are `provider.operate`-gated.
4. `tests/contract/test_ai_package_resources.py` proves the committed
   fixture is loadable and present in a built wheel; verify the fixture
   itself: exactly 74 bytes and SHA-256
   `396f6aba97b0b4ac60a22cae643ef2df1676ab98050fa468bbcb1aadb69b9e44`.
5. Dynamic no-restart resolution is proven by a test that rewrites the
   config and re-reads the capability endpoints without restart.
6. Documentation: ADR-0081 exists, is internally consistent with implemented
   behavior, and no closed ADR body was edited (diff proves it); SPEC §22
   contains the changed and added normative sentences described in the plan
   §12; the changed docs match the code.

Negative controls (must hold; cite the exact test or direct inspection):

- A secret value, key shape, Authorization header value, raw provider
  payload, or raw completion text never appears in config, API responses,
  CLI output, the JSON preview, or logs; `credential_env` is a name only.
- Ordinary and unmapped identities receive sanitized 403 for the admin
  routes, with audited denials; the public `public_published_uds` composition
  neither mounts nor returns the admin routes.
- Wrong or missing mutation origin/header is rejected; PUT/DELETE on
  built-ins and the active provider is refused; a PUT that would invalidate
  the active selection is refused; pong without explicit confirmation is
  refused; a non-`vision_input` model is refused for pong and Analyze; a bus
  lock yields the sanitized busy response.
- The providers GET performs zero provider calls; opening/typing in the UI
  performs no provider call; UI hiding is not the authorization mechanism.
- Malformed/unsupported config fails closed; a v1 file reads without
  information loss and is never written back as v1.
- Existing NVIDIA and Vercel behavior is unregressed (`test_nvidia_nim.py`,
  `test_vercel_gateway.py`, `test_media_suggestion_api.py` green), and no
  Gallery/Details visual or behavior file outside the allowlist changed.

## Authority

Positive: read-only inspection of the repository, its Git objects, the
candidate diff, the trace reports, and the tests; read-only execution of the
declared AP route and the `node --test` lines above; read-only file and hash
checks (`sha256sum`, `stat`, `file`); writing exactly one file — the Meta
acceptance report below — if absent, with full read-back.

Negative: any repository mutation; any correction; any new file outside the
Meta report; any Git write anywhere; any push; any network, provider,
NVIDIA/Vercel/OpenCode call; any credential or secret access; NUC, SSH,
sudo, browser, GUI; ambient Python, `poetry run`, `pip`, `uv`, environment
reconstruction; `git add` of anything; no weakening of tests.

## Meta persistence contract (execute exactly)

```text
Meta persistence owner: this Worker, for the single report path named below.
Prompt persistence owner: ORCHESTRATOR (already written; do not rewrite it).
Exact report destination: /home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/03_report.md
Write the complete terminal report to that path after the work, then verify
byte identity. Do not create other Meta files. Do not rename. Do not commit
Meta Git. Do not commit FrameNest.
If the path already contains a terminal report, STOP (PARTIAL) — do not
overwrite.
The Cooperator must not be asked to create, paste, or rename files.
```

## Acceptance report requirements

Begin exactly with `### Report for ORCHESTRATOR_CHAT`; echo these coordinates
once (`Worker session ordinal: 03`, `Worker exchange ordinal: 01`), and
include:

1. The compact core (status, phase-qualified result, start/end commit,
   changed files, validation, commit result, risks, next step, report
   justification `final-acceptance`, authority expiry, critique, near-misses,
   pre-existing classification, closure).
2. `Phase-qualified result: acceptance-PASS` on PASS; `not-applicable`
   otherwise. Status `PASS` only when every risk claim R1-R7 and every
   positive and negative control is verified with direct evidence; `PARTIAL`
   for verified claims with named missing evidence; `BLOCKED` when the
   candidate cannot be accepted.
3. A per-claim verdict table: R1-R7, each `verified` / `refuted` /
   `unverified (exact missing evidence)`, with exact evidence (test names,
   diff hunks, file paths, command results).
4. A controls table: each positive and negative control, its evidence, and
   its result.
5. Any discrepancy between the implementation reports and repository truth,
   as a claim-versus-evidence finding.
6. Out-of-scope observations listed as ledger candidates (non-authorizing),
   or `none`.
7. Residual-risk statement, including the automatic-analysis failure
   classification deviation (`PROVIDER_UNAVAILABLE` retryable when
   unconfigured during a scheduler run) and the indirect routed-analyze proof
   limitation — state whether each is acceptable for this whole's scope or
   requires a correction.
8. Capability/model observation row: requested vs observed client/model or
   `unknown/not observably exposed`; independence statement (fresh session,
   no material implementation participation, no parent transcript).
9. `Logical-whole closure: not-closed`; you must never emit any closure
   signal.

Save, read back fully, verify identity, then send the Orchestrator a short
separate completion notice with status, location, and SHA-256.

## Stopping conditions

Stop and report BLOCKED or PARTIAL when the repository gate fails
unclassifiably, the candidate identity is not the stated commit, the
independence posture is compromised, a required control cannot be executed
through the declared route, an environment limitation prevents evidence, or
the Meta destination is occupied or unsafe. Do not repair anything.

Authority expiry: this terminal report ends this grant; no autonomous
continuation.
