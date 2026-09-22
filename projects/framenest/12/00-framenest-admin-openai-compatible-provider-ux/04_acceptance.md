# Independent Re-Acceptance Exchange 01 — Session 04 — Full-Fresh Re-Acceptance of the Corrected Candidate

Persistent role identity: WORKER
Logical whole identity: framenest-admin-openai-compatible-provider-registry-and-vision-probe
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: Independent Audit
Task identity: REACCEPT-ADMIN-PROVIDER-REGISTRY-AND-VISION-PROBE-AFTER-CORRECTION
Delivery route: Agent Orchestrator default dispatch (fresh session; received only this prompt text; did not implement or correct the candidate)
Reasoning recommendation: High — named risk: this is the mandatory full-fresh re-acceptance after a runtime-behavior correction on the Analyze capability boundary; it must verify the correction and re-verify the original risk claims without trusting prior reports
Recommended context capacity: approximately 250k tokens
Independence required: yes (fresh, independent of the correction author)
Sub-agents or internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Development envelope activation: not-used

## Independence posture

You are a genuinely fresh Worker session, independent of both the original
implementation (Worker session 02) and the correction (also session 02). You
must not rely on any prior Worker report as proof; the acceptance report
`03_report.md` and the implementation/correction reports are claims to
re-verify. If you discover inherited parent-context or material participation,
STOP and report it — the re-acceptance is invalid.

You have NO correction authority. Read-only inspection and read-only
execution only.

## Acceptance and Correction Record

```text
Acceptance candidate: 7ff6546f345827d6df20bd5b13d5e57cb4bc90db (local commit on feat/x-meme-browser-companion)
Acceptance owner map: provider configuration schema (src/framenest/infrastructure/ai/provider_records.py, configuration.py), generic adapter (openai_chat_completions.py), registry and dynamic resolution (registry.py), credentials (credentials.py), CLI (src/framenest/adapters/cli/ai.py), admin API (src/framenest/adapters/api/ai_admin_api.py), ingress route policy (tailscale_ingress.py), application composition (application.py), capability endpoints (media_suggestion_api.py, media_analysis_lifecycle_api.py), automatic-analysis lifecycle (src/framenest/application/media_analysis_lifecycle.py), web shell (web/index.html, web/app.js, web/styles.css), deploy source material (deploy/systemd/framenest-ai-credential-opencode-go.conf, deploy/ubuntu/production_ai_deploy.py), living docs (SPEC.md §22, SECURITY.md, SERVER.md, README.md, AI_WORKSPACE.md, docs/UBUNTU_NUC_DEPLOYMENT.md, docs/adr/0081-*.md, docs/adr/README.md)
Acceptance allowlist: exactly the paths changed by 33946e08447dc92621ed6844b4b5d13a19ec29f1..7ff6546f345827d6df20bd5b13d5e57cb4bc90db
Acceptance risk claims: R1 no secret value in v2 config, API responses, browser surfaces, or logs; R2 admin routes cannot bypass authN/authZ; R3 ping/pong/analyze privacy; R4 v1 config read compatibility and fail-closed malformed handling; R5 dynamic resolution without restart, no authorization widening, no silent movie-identification change; R6 NVIDIA/Vercel unregressed and Gallery/Details frozen; R7 repository hygiene (only allowed paths changed, .ap untouched, no push); R8 (correction) every Analyze entry point refuses a selected model without vision_input — the two suggestion-preview routes and the durable-analysis request with 409 AI_MODEL_CAPABILITY_MISSING before any provider work, the automatic-analysis run with a non-retryable PROVIDER_MODEL_CAPABILITY_MISSING classification that is not counted as a provider submission, and no change to pong, CLI vision-probe, or existing failure classifications
Acceptance control matrix: the positive and negative controls from 03_acceptance.md, re-run and re-verified on this candidate, plus the corrected N7 and the new N8 (no provider submission counted; existing classifications unchanged)
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

## Candidate and baseline

- Baseline (published `main`): `33946e08447dc92621ed6844b4b5d13a19ec29f1`.
- Candidate chain: `33946e0 → f41df79 → 980db7a → e6d91d1 → c66f5b6 →
  810b606 → 87411e0 → 7ff6546`.
- Corrected candidate under acceptance: `7ff6546f345827d6df20bd5b13d5e57cb4bc90db`.
- Correction commit: `7ff6546` "Refuse non-vision models on Analyze paths"
  (7 paths) on top of the previously audited `87411e0`.
- Local-only; no push; verify porcelain clean and the branch ahead of
  `origin` by seven commits. No fetch; no network.

## Mandatory reading

- `.ap/AP.md` WORKER spine, RF-05 (independence), RF-07, RF-12, RF-18, §8,
  §12, §18; `.ap/AP_WORKER.md`; `.ap/PROMPT_CONTRACTS.md` Worker Report
  Header and the Acceptance and Correction Record.
- The accepted plan `01_report_orchestrator.md` §3-§13.
- Prior acceptance `03_report.md` (verdicts and evidence as claims to
  re-verify), the correction report `02_report_07.md`, and
  `git show 7ff6546` (the correction diff).

## Repository gate (read-only)

Verify: physical root, canonical remote, branch, HEAD == `7ff6546…`,
porcelain clean, `.ap` gitlink == `.ap` HEAD
`7478ddb07d2c3911f79e1aa1441f0115a31c45d8`, `./.ap/ap doctor` PASS,
`git diff --name-only 33946e0..7ff6546` equals the acceptance allowlist
(record the exact count; expect 53). Classify differences per RF-12; do not
repair.

## Controls

Positive controls (re-run on this candidate):

1. Python selection through the declared route (working spelling
   `./.ap/ap exec`):
   `./.ap/ap exec --root /home/agile/Projects/framenest --baseline 7ff6546f345827d6df20bd5b13d5e57cb4bc90db --operation test-focus -- tests/unit/infrastructure/ai tests/unit/adapters/cli/test_ai_cli.py tests/unit/test_configuration.py tests/unit/application/test_media_analysis_lifecycle.py tests/contract/test_ai_provider_admin_api.py tests/contract/test_tailscale_ingress_security.py tests/contract/test_x_route_policy.py tests/contract/test_public_published_uds.py tests/contract/test_media_suggestion_api.py tests/contract/test_media_analysis_lifecycle_api.py tests/contract/test_ai_server_composition.py tests/contract/test_automatic_analysis_settings_api.py tests/contract/test_automatic_analysis_privacy_contract.py tests/contract/test_ai_package_resources.py tests/contract/test_local_web_application.py tests/contract/test_web_package_resources.py tests/contract/test_production_ai_deployment.py tests/contract/test_nuc_operator_runbook.py tests/contract/test_nuc_release_docs.py -q -p no:cacheprovider`
2. `node --test tests/ai_providers_admin_frontend.test.js tests/tailscale_identity_frontend.test.js tests/companion_settings_automatic_analysis.test.js`.
3. Route inventory 1:1 and the six admin routes `provider.operate`-gated.
4. Fixture: 74 bytes, SHA-256
   `396f6aba97b0b4ac60a22cae643ef2df1676ab98050fa468bbcb1aadb69b9e44`,
   wheel-present.
5. Dynamic no-restart resolution.
6. Documentation asserts only behavior that the corrected code implements
   (SPEC §22:726-727, ADR-0081 decision 4, AI_WORKSPACE.md:218-220 are now
   true; no closed ADR body edited).

Negative controls (re-verify, with the corrected N7 now expected to hold):

- All prior negative controls from `03_acceptance.md` (secrets, 403/audit,
  mutation proof, public composition, built-in/active refusals, pong confirm
  and non-vision refusal, busy locks, zero provider calls on GET and UI
  render/typing, malformed config fail-closed, v1 read compatibility, no
  Gallery/Details change).
- N7 (corrected): a selected non-`vision_input` model is refused on both
  suggestion-preview routes and the durable-analysis request with
  `409 AI_MODEL_CAPABILITY_MISSING` and zero provider calls; the automatic
  analysis run fails with the non-retryable `PROVIDER_MODEL_CAPABILITY_MISSING`.
- N8 (new): the capability refusal never counts as a provider submission
  (`_PROVIDER_SUBMISSION_ERROR_CODES` excludes it); a reader raising the
  unavailable error still classifies as `PROVIDER_UNAVAILABLE`; existing
  failure classifications and pong/CLI vision-probe behavior are unchanged.

## Authority

Positive: read-only inspection; read-only execution of the declared AP route
and the `node --test` line; read-only file/hash checks; writing exactly one
file — the Meta re-acceptance report below — if absent, with full read-back.

Negative: any repository mutation or correction; any Git write; any push;
any network, provider, or credential access; NUC/SSH/sudo/browser/GUI;
ambient Python, `poetry run`, `pip`, `uv`, environment reconstruction;
weakening tests.

## Meta persistence contract (execute exactly)

```text
Meta persistence owner: this Worker, for the single report path named below.
Prompt persistence owner: ORCHESTRATOR (already written; do not rewrite it).
Exact report destination: /home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/04_report.md
Write the complete terminal report to that path after the work, then verify
byte identity. Do not create other Meta files. Do not rename. Do not commit
Meta Git. Do not commit FrameNest.
If the path already contains a terminal report, STOP (PARTIAL) — do not
overwrite.
The Cooperator must not be asked to create, paste, or rename files.
```

## Report requirements

Begin exactly with `### Report for ORCHESTRATOR_CHAT`; echo these coordinates
once (`Worker session ordinal: 04`, `Worker exchange ordinal: 01`), then:

1. The compact core with `Report justification: final-acceptance` and
   `Logical-whole closure: not-closed`.
2. `Phase-qualified result: acceptance-PASS` on PASS; `not-applicable`
   otherwise. PASS requires every claim R1-R8 and every control verified with
   direct evidence on this candidate.
3. Per-claim verdict table R1-R8 with exact evidence; explicitly state
   whether the correction resolves the original N7 finding and whether any
   new issue was introduced (cite the correction diff hunks).
4. Controls table (prior matrix re-run plus N7/N8) with results.
5. Claim-versus-evidence findings against prior reports, or `none`.
6. Out-of-scope observations as ledger candidates, or `none` (the prior
   audit's ledger candidates may be restated).
7. Residual-risk statement with acceptance disposition for each (including
   the automatic-analysis unconfigured-provider classification).
8. Independence statement and capability/model observation row.
9. Authority expiry.

Save, read back fully, verify identity, then send the Orchestrator a short
separate completion notice with status, location, and SHA-256.

## Stopping conditions

Stop and report BLOCKED or PARTIAL when the gate fails unclassifiably, the
candidate is not `7ff6546…`, the independence posture is compromised, a
control cannot be executed, or the Meta destination is occupied or unsafe.
Do not repair anything.

Authority expiry: this terminal report ends this grant; no autonomous
continuation.
