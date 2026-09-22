# Implementation Exchange 06 — Session 02 — Slice 5: Living Documents and ADR-0081

Persistent role identity: WORKER
Logical whole identity: framenest-admin-openai-compatible-provider-registry-and-vision-probe
Worker session ordinal: 02
Worker exchange ordinal: 06
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker (current-session continuation)
Phase: Implementation
Task identity: IMPLEMENT-LIVING-DOCS-AND-ADR-0081-SLICE-5
Implementation authority: explicit
Delivery route: Agent Orchestrator default dispatch into the same session (continuity anchor below)
Reasoning recommendation: High — named risk: normative sentences in SPEC/SECURITY/SERVER and a new accepted ADR become the durable contract for a security-sensitive provider boundary; wording must be exact, closed ADR bodies must not be edited, and runbook/doc-contract tests must stay green
Recommended context capacity: approximately 250k tokens
Independence required: no
Sub-agents or internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active

## Continuity anchor and authority renewal

Continuity anchor: your terminal PASS reports for exchanges 02-05
(`02_report_02.md` … `02_report_05.md`) and your commits `980db7af…`,
`e6d91d1b…`, `c66f5b6a…`, `810b606d…`. Prior authority expired at the last
report. This is a complete renewed grant for slice 5. Retained context is
convenience, not authority; repository evidence wins on conflict. Evidence in
this exchange is non-independent.

## Goal

Implement slice 5: record the now-implemented decisions in their durable
owners — SPEC §22, SECURITY.md, SERVER.md, README.md, AI_WORKSPACE.md, the
Ubuntu NUC runbook, and a new ADR-0081 with narrow supersession notes and an
ADR index row. No code changes in this slice.

## Mandatory reading

- The accepted plan
  `/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/01_report_orchestrator.md`
  §3-§9 (what was built), §11-§12 (credentials source material and exact
  documentation changes), §14 slice 5.
- The files you will edit, read fully before changing: `SPEC.md` §22 (and the
  adjacent AI sentences in §18/§21 you find relevant), `SECURITY.md` (Logs
  and Diagnostics; Secret Handling), `SERVER.md` (Server-Side AI Provider
  Boundary; Current MacBook MVP Non-Goals), `README.md` (route list, AI CLI,
  `.secrets/ai.env.fish`), `AI_WORKSPACE.md`, `docs/UBUNTU_NUC_DEPLOYMENT.md`
  ("Production AI Credential Helper"), `docs/adr/README.md` (index format).
- One existing ADR as a style model: `docs/adr/0079-administrator-automatic-analysis-runtime-setting.md`.
- Implemented reality to describe accurately: the six
  `provider.operate` routes in `src/framenest/adapters/api/ai_admin_api.py`,
  the schema-v2 config and `provider_records.py`, the generic adapter, the
  `vision-input` gating and `409 AI_MODEL_CAPABILITY_MISSING`, the ping/pong
  contract, the committed fixture, the dynamic no-restart resolution, and
  the new `deploy/systemd/framenest-ai-credential-opencode-go.conf` plus the
  helper maps.

## Repository gate (before mutation)

Verify: HEAD equals `810b606dc9ca34e696dde3cffb533abb1b193884` (this
exchange's authorized baseline), porcelain clean, branch
`feat/x-meme-browser-companion`, `.ap` gitlink unchanged,
`./.ap/ap ap doctor` PASS. Stop on any unexplained difference.

## Slice 5 deliverables (binding design)

### D1 — New ADR-0081

`docs/adr/0081-declarative-openai-compatible-provider-registry-and-administrator-vision-probe.md`,
following the repository ADR style (Status, Decision Date, Context, Decision,
Superseded statements, Deferred, Consequences, References).

- Status: `Accepted`; "Accepted by the Cooperator on 2026-09-16 as part of
  the approved plan and implementation direction for this logical whole."
- Decision date: 2026-09-16.
- Context: CLI-only operator boundary; ADR-0079 deferred website Settings;
  Cooperator intent for declarative providers; dated OpenCode Go public-docs
  facts (say plainly they are dated public documentation, re-fetched
  2026-09-16, and that the live catalog is confirmed later under a separate
  provider-call grant).
- Decision: non-secret config schema v2 declarative records; one registry
  world for built-in and declared providers; parameterized generic
  OpenAI-compatible chat-completions adapter; operator-declared
  `vision_input` capability filtering; administrator web surface under
  `provider.operate` with audit-before-mutation and website-origin mutation
  proof; ping (text-only) and pong (one committed synthetic fixture plus
  explicit cloud confirmation); credential **names** only, never values;
  dynamic no-restart resolution; `403` = credential/entitlement rejection.
- Superseded statements (narrow notes only; NEVER edit a closed ADR body):
  ADR-0020 operator-boundary and Revisit triggers fulfilled for non-secret
  provider administration; ADR-0023 deferred provider-discovery contract
  partially implemented through declared capabilities only; ADR-0035
  operator-only provider-administration phrasing read as including the
  authenticated administrator web surface; ADR-0036 credential mechanism
  extended by a third identity (`OPENCODE_API_KEY`); ADR-0044 deferred
  provider-management UI succeeded for this surface; ADR-0079 website
  Settings deferred statement succeeded for the provider surface only (the
  companion automatic-analysis checkbox is unchanged); ADR-0075 refresh
  framing unchanged.
- Deferred: model-catalog refresh, `/responses` and `/messages` protocols,
  OpenCode Zen record, loopback base URLs, per-record `response_format`,
  persistent probe history, inline media-detail model picker, persistent
  drafts, Cover Studio.

### D2 — `SPEC.md` §22 exact sentence changes

1. Replace the operator-boundary sentences: server AI provider
   administration MUST use an operator boundary — the CLI (`./framenest ai
   ...`) plus an authenticated administrator-only web surface reached through
   `provider.operate` over the trusted Tailscale workspace ingress; ordinary
   browser clients MUST NOT configure AI providers, activate models, enter
   provider API keys, receive provider API keys, or call external AI
   providers directly.
2. Replace the supported-providers sentence: NVIDIA NIM and Vercel AI
   Gateway remain supported built-in server providers, and the server
   supports operator-declared OpenAI-compatible provider records (first
   instance: OpenCode Go at `https://opencode.ai/zen/go/v1`) persisted as
   non-secret schema-versioned configuration.
3. Replace the configuration-file content sentence: only schema-versioned
   non-secret provider/model selection, declarative provider records
   (provider id, display name, protocol, base URL, credential
   environment-variable **name**, declared models, declared capabilities),
   and safe timestamps; MUST NOT contain API keys, Authorization headers,
   cookies, provider responses, prompts, frame data, media paths, or database
   paths.
4. Add the new normative sentences: administrator-initiated `ping` MUST be an
   explicit text-only provider request; administrator-initiated `pong` MUST
   send exactly one repository-owned synthetic fixture image and MUST require
   explicit cloud-upload confirmation; neither MUST use catalog media, persist
   a suggestion, or run without an explicit administrator action. Analyze
   and the vision probe MUST refuse a selected model that does not declare
   `vision_input`. A provider HTTP `403` MUST be reported as credential or
   entitlement rejection, never as invalid output. Provider declarations MUST
   be `https://` only for non-loopback hosts; local-gateway base URLs remain
   deferred.

### D3 — `SECURITY.md`

Add a paragraph naming the administrator AI provider surface: its
`provider.operate` and audit-before-mutation posture; the no-secret browser
rule; the synthetic pong fixture; the one-call-in-flight/activity-lock
posture; `403` entitlement semantics; `OPENCODE_API_KEY` support through the
ignored local `.secrets/ai.env.fish` and systemd credentials; and the dynamic
no-restart resolution. Extend the existing `.secrets/ai.env.fish` sentence to
`NVIDIA_API_KEY`, `AI_GATEWAY_API_KEY`, and/or `OPENCODE_API_KEY`. The edit
must not introduce `/home/` paths or forbidden tokens (the runbook/doc
contract tests assert their absence where they already do).

### D4 — `SERVER.md`

In "Server-Side AI Provider Boundary": replace the blanket "Ordinary browser
and desktop clients do not configure providers" wording with the precise
rule (ordinary clients never; authenticated administrators may manage
non-secret records and run ping/pong through the server); update the browser
Status modal paragraph to mention the separate administrator surface; amend
or remove the "centralized browser provider Settings" bullet in "Current
MacBook MVP Non-Goals" because it is now implemented for provider records
only (companion automatic-analysis checkbox unchanged; desktop Settings
still unshipped).

### D5 — `README.md`

Add the six admin routes to the API list, the new `vision-probe` CLI command,
the v2 config/declared-provider support, and `OPENCODE_API_KEY` support; keep
the "browser never configures providers" statement accurate for ordinary
clients. Keep the existing status/documentation-map structure and link style.

### D6 — `AI_WORKSPACE.md`

In "Current Implementation Boundary" and the "Inline Model Picker" /
"Capability Labels" sections: state that server-side provider administration
now includes the administrator web surface and declared capabilities; the
inline picker and persistent drafts remain deferred.

### D7 — `docs/UBUNTU_NUC_DEPLOYMENT.md`

In "Production AI Credential Helper": add OpenCode Go as the third supported
credential identity (`OPENCODE_API_KEY`, tracked drop-in template under
`deploy/systemd/`), additive to the existing text; do not restructure the
section or change its existing assertions.

### D8 — `docs/adr/README.md`

Add the ADR-0081 row in the existing index format.

## Exact changed-path allowlist

```text
SPEC.md
SECURITY.md
SERVER.md
README.md
AI_WORKSPACE.md
docs/adr/0081-declarative-openai-compatible-provider-registry-and-administrator-vision-probe.md (new)
docs/adr/README.md
docs/UBUNTU_NUC_DEPLOYMENT.md
```

No other file may be created, edited, deleted, or moved. Do not touch
`PRODUCT.md`, `ROADMAP.md`, `AGENTS.md`, `ap.project.conf`, any closed ADR
body, or any code or test file.

## Validation

Documentation review: every changed sentence matches implemented behavior
(cross-check `ai_admin_api.py`, `provider_records.py`, `configuration.py`,
`registry.py`, `vision_probe.py`, `deploy/ubuntu/production_ai_deploy.py`);
links and paths resolve; no closed ADR body was edited (diff shows only the
listed files); no `/home/` path or secret-shaped content added.

Docs-contract regression through the declared AP route:

```text
./.ap/ap ap exec --root /home/agile/Projects/framenest --baseline 810b606dc9ca34e696dde3cffb533abb1b193884 --operation test-focus -- tests/contract/test_nuc_operator_runbook.py tests/contract/test_nuc_release_docs.py tests/contract/test_fedora_systemd_service.py tests/contract/test_production_ai_deployment.py tests/contract/test_adr_0073.py tests/contract/test_team_alias_api.py -q -p no:cacheprovider
```

If an additive wording change genuinely breaks one of these tests, stop and
report rather than editing the test.

Validation ladder:

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the docs-contract selection above
Affected tests: the named suites; no code suites are affected
New causal regression: none — this slice is documentation-only
Broad or full suite: not-used — no project rule or named decision risk requires it for this slice
Runtime or testbed: not-used
Independent acceptance: not-required
```

## Commands (canonical execution route — binding)

```text
./.ap/ap ap project check --root /home/agile/Projects/framenest --baseline 810b606dc9ca34e696dde3cffb533abb1b193884
./.ap/ap ap exec --root /home/agile/Projects/framenest --baseline 810b606dc9ca34e696dde3cffb533abb1b193884 --operation runtime-info
```

plus the docs-contract selection above.

## Authority

Positive: edit/create only the allowlisted paths; the declared AP route;
read-only Git; stage exactly the allowlisted paths; one local commit with
subject `Record declarative provider registry and vision probe decisions`;
no push; the single Meta report below.

Negative: everything outside the allowlist; any code, test, AGENTS.md,
PRODUCT.md, ROADMAP.md, closed-ADR, or `.ap` change; any other Git write; any
network, provider, NUC, SSH, sudo, browser, GUI, environment-reconstruction,
or secret-access action; `git add .`/`-A`.

## Meta persistence contract (execute exactly)

```text
Meta persistence owner: this Worker, for the single report path named below.
Prompt persistence owner: ORCHESTRATOR (already written; do not rewrite it).
Exact report destination: /home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/02_report_06.md
Write the complete terminal report to that path after the work, then verify
byte identity. Do not create other Meta files. Do not rename. Do not commit
Meta Git. Do not commit FrameNest unless this prompt grants FrameNest Git.
If the path already contains a terminal report, STOP (PARTIAL) — do not
overwrite.
The Cooperator must not be asked to create, paste, or rename files.
```

## Report contract

Begin exactly with `### Report for ORCHESTRATOR_CHAT`; echo these coordinates
once (`Worker session ordinal: 02`, `Worker exchange ordinal: 06`); compact
core: status; `Phase-qualified result: implementation-PASS` on PASS else
`not-applicable`; start commit `810b606d…`; end commit; changed files; tests
and validation with exact counts; commit result; deviations/risks; one
smallest next step; `Report justification: new-mutation`; authority-expiry
statement; `Orchestration critique` (MEASURED/LEAD); Resolved Execution
Issues / Near-Misses and Pre-Existing Failure Classification;
`Logical-whole closure: not-closed`. Save, read back fully, verify identity,
then a short separate completion notice with location and SHA-256.

## Stopping conditions

Stop and report BLOCKED or PARTIAL when a gate fails unclassifiably, a needed
change exceeds the allowlist, a documentation-contract test must be weakened,
the execution route is unusable, the Meta destination is occupied or unsafe,
or retained context conflicts with repository evidence.

Authority expiry: this terminal report ends this grant; no autonomous
continuation.
