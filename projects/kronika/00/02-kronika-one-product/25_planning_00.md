# Kronika one product — modular search/deep-research provider: architecture and revised slice plan

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 25
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: KRONIKA-ONE-PRODUCT-MODULAR-SEARCH-PROVIDER-PLAN
Delivery route: manual Cooperator delivery
Reasoning recommendation: Extra High — named risk: cross-cutting redesign of the Search/Research capability across a new external-provider trust boundary (credentials, cost caps, untrusted content), the common record model, privacy/sharing, and the S4–S10 slice order, superseding part of the accepted plan; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Planning contract

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: design the modular search/deep-research provider architecture in the existing FrameNest repository, its record/rendering/privacy integration, the provider-boundary security requirements, the revised S4–S10 slice order replacing the capture-mode S4 route, the durable documentation update, and a concrete first-provider recommendation package for Cooperator selection
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1

Planning cycle: initial
Prior planning reports: 01_report_00.md (accepted whole plan S0–S10) and 15_report_00.md (accepted S3 recovery plan)
Targeted revision basis: none
Changed decision boundary: the Search/Research provider architecture — a modular, provider-neutral provider with an external agent + web search tool as the first provider; chatgpt.com capture becomes one currently parked module
Preserved unaffected decisions: the S0–S3 repository outcomes and their acceptances; Timeline as the main page; Gallery preserved; common private-by-default records with explicit family sharing; no old-database import; the NUC stays the development/test machine; no mass `framenest` rename; the S10 public rename; the AP pin; every security boundary
Automatic targeted revisions used: 0
```

Planning authority expires at the terminal planning report. This grant does
not authorize implementation, repository mutation, acceptance, publication,
deployment, host contact or closure.

## Fresh-session opening

This is a genuinely fresh Worker session; inherit no prior authority.
Independently establish the repository evidence named below before reasoning.
Repository reading is read-only. Bounded public documentation research on
candidate providers is permitted (read-only; cite sources and dates); no
provider API calls, no credentials and no account actions. The only write this
grant allows is the terminal report at its exact destination when absent. No
subagents.

## Current Cooperator direction (binding input)

- Kronika keeps MEME and Movie and adds Search and Research, but search/deep
  research is delivered through a **modular provider abstraction**, not the
  capture modes.
- The **first provider class** is an **external provider/agent with a web
  search tool** (Cooperator decision 2026-09-26). The concrete provider,
  credentials, cost cap and privacy posture remain a Cooperator selection
  inside this planning.
- **chatgpt.com capture remains as one currently parked module**: the S3 host
  bring-up stays parked at the login boundary (Cloudflare challenge loop), the
  capture code and S3/S5 repository work stay in the tree, and nothing is
  removed or reassigned by this plan.
- The end goal remains transforming FrameNest into Kronika (S10).

## Verified starting state (read-only, 2026-09-26)

- FrameNest checkout `/home/agile/Projects/framenest`; branch
  `feat/kronika-one-product`; HEAD
  `fd277a9a64a6965df76127dbec5b1735d2fb3cdd` (parent
  `e408bb5503f359ec24542304ac1a621c6b9e4ffb`); clean; local `main` =
  `origin/main` = public `refs/heads/main` = `fd277a9…`; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (gitlink and `.ap` HEAD).
- Published S0–S3 repository work and the C3 runner temporary-directory
  correction are on public `main`; the capture host is parked with one
  healthy Chromium at `needs_admin`.
- The clean Kronika source at `/home/agile/Tools/cli_chatgpt`
  (`66c40d43…`, read-only, never modified) is available as historical
  reference for export/sanitization and record patterns; it is not a second
  implementation to port wholesale.
- `private/**` is never read. No host, SSH, gate, sudo, service, credential or
  profile action is authorized.

## Planning question

Produce a decision-complete, repository-grounded plan that:

1. **Defines the provider abstraction.** The port/interface in the existing
   FrameNest architecture (domain/application/infrastructure placement),
   capabilities (search, deep research), request/result contracts, typed
   errors, cancellation, timeouts, retries, idempotency, and a provider
   registry/selection model. It must admit the parked chatgpt.com capture and
   a future self-hosted provider without code churn.
2. **Specifies the first provider concretely.** Compare the realistic
   external-agent-with-web-search candidates against this project's
   constraints: server-side credentials only, no provider secrets to
   clients, explicit call authority, cost cap, kill switch, data
   minimization, refusal handling, and untrusted output. Recommend one
   provider (or a primary plus fallback) with exact configuration and
   credential-boundary mechanics for the Cooperator to select; state the
   exact Cooperator decision still needed before implementation.
3. **Integrates with the common record model.** How Search and Research
   results become common Kronika records: ownership from verified identity,
   private-by-default with explicit family sharing, timeline entry only after
   a complete validated save, migrations (next free Alembic revision),
   repository/domain placement, and sanitized rendering (no JavaScript, no
   external resources, full text/Markdown preserved). Preserve the existing
   catalog, media-analysis lifecycle and metadata-review approval.
4. **Specifies the agent runtime.** Where the agent/tool loop executes
   (server-side in FrameNest), tool-call limits, budget accounting (per-call
   and per-record), concurrency, retries, timeouts, cancellation, and how
   prompts/outputs are stored and classified as untrusted content. Include a
   bounded synthetic test route and the accounting record shape.
5. **Defines the provider-boundary security and privacy requirements**, in
   the project's R3 style: threat model, what data may leave the host, what
   never may (private media, unrelated records, credentials, profile data),
   credential storage, cost controls, auditability with redacted diagnostics,
   refusal/error classification, and the fresh independent review routes.
6. **Re-sequences S4–S10.** Replace the capture-mode S4 route with the
   provider slices; state precisely what happens to S5 (capture ZIP
   attachment) and S7 (application capture integration) — re-scope, defer or
   park as capture-module work — and how S6, S8, S9 and S10 are affected.
   Give each revised row: useful outcome and boundary, dependencies,
   authority/host class, checks, tier/acceptance class, recovery/stop, and
   the evidence required before the next row. Keep one implementation grant
   per row.
7. **Plans the durable documentation update** (S0-style, separate bounded
   slice): which repository documents must record the superseding direction
   (ADR, ROADMAP, PRODUCT, SPEC, SERVER, SECURITY, AGENTS, README,
   DEVELOPMENT) and the required contradiction search against the older
   capture-only Search/Research wording.
8. **States limits honestly.** No claim that any provider was called; no
   credentials; no host contact; the parked capture module is untouched.
9. **Recommends exactly one next bounded grant** for the Orchestrator to
   issue after acceptance, in the project's grant shape: identity and route,
   exact baseline and allowlist, positive and negative authority, declared
   route (`./.ap/ap project check` / `./.ap/ap exec`, `node --test`), staging
   and commit rules, stop conditions, report contract, trace and delivery
   record. If a Cooperator decision must precede it, make that the
   recommendation.

## Mandatory reading

- Governing WORKER spine, `RF-19`, AP validation, planning and stopping
  owners.
- `01_plan_sk.md` (locked direction), `01_report_00.md` §4–§10 (contracts,
  ZIP, records, UI, S0–S10 rows, validation and security checklist), and the
  accepted S3/S4 route wording this plan supersedes.
- `21_report_00.md`, `22_report_00.md`, `23_report_00.md`, `24_report_00.md`
  and the current `00_notes.md` (parked capture state; the C3 outcome; the
  current direction entry).
- FrameNest `AGENTS.md` security and product boundaries; `PRODUCT.md`,
  `SPEC.md`, `SERVER.md`, `SECURITY.md`, `ROADMAP.md`,
  `docs/adr/0082-kronika-one-product-and-private-records.md`.
- The existing catalog/records/analysis domains and migrations, the web
  shell and its rendering/sanitization conventions, and the test directory
  conventions.
- `/home/agile/Tools/cli_chatgpt` (read-only historical reference only).

Citation rule: every material claim cites its exact source location at the
baseline; line numbers are locators. Treat all host values as
Orchestrator-relayed classified evidence, not as your own observation.

## Authority and containment

Positive authority: read-only inspection of the named repository and trace
files; bounded public documentation research on candidate providers
(read-only, cited); the terminal report write at the exact destination below
when absent; full readback of the saved report.

Negative authority: no repository mutation; no test, build or interpreter
execution unless a declared read-only check is unavoidable (state it); no
host, SSH, gate, sudo, service, account, browser or credential action; no
provider API calls, keys or account actions; no `private/**`; no profile or
token access; no subagents; no second planning cycle. Do not print hostnames,
private network values, tokens, secrets or credentials.

## Completion and report contract

Status: `PASS` when the plan is decision-complete for the current evidence;
`PARTIAL` when a material cause or Cooperator decision remains genuinely open
and is stated as such; `BLOCKED` when the planning question cannot be answered
inside the boundaries. Use `Phase-qualified result: not-applicable` and
`Logical-whole closure: not-closed`. `Report justification: new-evidence`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the
architecture and interface design; the provider comparison and
recommendation with sources; the record/migration/rendering integration; the
agent runtime and accounting; the security/privacy requirements; the revised
S4–S10 table; the documentation update slice; the exact Cooperator decision
still needed; the recommended next grant; deviations and missing evidence;
authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

The formal report is in English; a short completion notice to the Cooperator
is in Slovak, masculine address. Finalize the report, save it at the exact
destination, read it back in full, verify its first line, coordinates,
content and path, then send the separate short completion notice with status,
path and SHA-256. Terminal report or cancellation expires this authority.

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
Downloadable prompt filename: 25_planning_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 25_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```
