# WORKER TASK — Implementation Planning (plan-only)

Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-companion-r4-automatic-analysis-settings-mvp
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Planner
Phase: Discovery / implementation-planning
Native planning mode: required
Reasoning recommendation: High
Task identity: FRAMENEST-COMPANION-R4-AUTO-ANALYSIS-PLAN-01
Task type: bounded read-only implementation planning
Exact baseline: 1eee09c1afcfe41b2a411784f8c43c428e610b9b
Independence required: no
Evidence posture: non-independent
Authority renewal: this is a fresh session; there is no prior Worker authority to renew. Plan approval does not grant implementation authority.
Internal delegation posture: not-used
Accountable Worker: one WORKER
Material phase gate: yes
Changed material axis: primary-objective
Routing reopened for: primary-objective
Unchanged axes reopened: none
Ordinary-only trigger: no

## Plan-to-Execution Contract

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded technical planning of (1) companion
  extension Settings dialog gaining an admin-only "Administration" section with
  an automatic-media-analysis toggle/checkbox; (2) server-side runtime-writable
  setting API (GET + PUT/PATCH) backed by a runtime-persisted setting (surviving
  service restart without committing true into git and without requiring sudo);
  (3) capability gating (admin-only: analysis.run / provider.operate vs ordinary
  denied); (4) mutation route classification (Tailscale ingress policy, audit,
  mutation trust boundary, whether companion_mutation is needed); (5) confirmation
  and cost/cloud upload copy before enabling; (6) test strategy across backend
  and extension; (7) successor ADR / docs outline. No implementation.
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
```

```text
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

```text
Canonical repository identity: https://github.com/cisarik/ap.git
Immutable version identity: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Declared variant: stable
Governing variants in effect: one
Declaration location: project governing rules
Rules from non-governing variants: none
Migration required: no
```

This prompt grants READ-ONLY planning authority only. It grants no
implementation, no FrameNest repository mutation, no Git writes, no
publication, no deployment, no NUC contact, no provider calls, no production
mutation, and no closure. Planning authority expires at your terminal report.

## Mandatory Reading

In order:

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `/home/agile/Projects/framenest/.ap/AP.md`
3. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
4. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
5. `/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/00_handout.md` (especially §4.2)
6. This prompt (self-contained task authority)

Then, at the exact baseline, inspect:

7. `docs/adr/0066-administrator-owned-x-automatic-generic-analysis.md`
8. `docs/adr/0044-automatic-background-analysis-lifecycle.md`
9. `docs/adr/0075-nuc-development-test-target-and-routine-release-refresh.md`
10. `docs/adr/0067-administrator-companion-review-inbox-and-mutation-trust.md`
11. `docs/adr/0020-on-demand-ai-suggestion-review.md`
12. `extension/ui/sidebar.html`, `extension/ui/sidebar.js`, `extension/ui/sidebar.css`
13. `src/framenest/configuration.py` (`automatic_media_analysis_enabled`)
14. `src/framenest/adapters/api/application.py` (DI and runtime configuration)
15. `src/framenest/adapters/api/tailscale_ingress.py` (route policies and capabilities)
16. `src/framenest/application/identity_access.py`
17. `tests/automatic_analysis_lifecycle.test.js`, `tests/companion_review_extension.test.js`

## Repository Gate

```text
Repository checkout topology: standalone checkout with pinned submodule
Canonical root: /home/agile/Projects/framenest
Expected branch: feat/x-meme-browser-companion
Expected HEAD: 1eee09c1afcfe41b2a411784f8c43c428e610b9b
Expected tree: 651664e754efbe9492161b402860fe368415fc17
Expected working tree: tracked-clean
Pinned submodule: .ap gitlink == .ap HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: 1eee09c1afcfe41b2a411784f8c43c428e610b9b (verified by ORCHESTRATOR)
Schema head: Alembic 0033 (0033_media_analysis_proposals.py); no 0034_* migration
Working-copy topology: canonical-checkout
Topology rationale: read-only planning against the living public baseline; no candidate worktree
```

If any gate fact differs from the above, STOP and report BLOCKED with exact
observed evidence before any analysis conclusion.

## Goal (one coherent outcome)

Produce a decision-complete, repository-grounded implementation plan for the
logical whole `framenest-companion-r4-automatic-analysis-settings-mvp`, frozen at
the exact baseline, and return it as your terminal report. No implementation in
this session.

## Problem Statement & Cooperator Intent

- **Background:** `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED` is `false` by
  default in git (ADR-0044, ADR-0066). When enabled, automatic background
  analysis runs for newly acquired administrator-owned X catalog events, incurring
  real AI provider/NIM usage costs.
- **Current UI:** Extension Settings dialog (`extension/ui/sidebar.html`) only
  has origin configuration and connect/disconnect buttons. There is no GUI
  toggle for automatic analysis.
- **Intent:**
  1. Add an **Administration** section in extension Settings dialog (`extension/ui/sidebar.html` / `sidebar.js`), visible only to administrators.
  2. Provide a checkbox toggle for "Automatic media analysis" (or exact copy).
  3. Turning it ON requires explicit confirmation of cloud upload / provider usage cost.
  4. Setting must be backed by a server-side runtime setting API (GET and write).
  5. Setting must survive server process restarts without committing `true` into git and without requiring root/sudo.
  6. Ordinary identities must never see, read, or toggle this setting.
  7. Do not unify YouTube into automatic analysis (ADR-0066 §6).

## Plan Must Freeze

1. **Server Architecture & Persistence Strategy:**
   - How the runtime setting is persisted across process restarts (evaluate options: SQLite KV / settings table vs runtime configuration layer vs dedicated server runtime JSON store under `/var/lib/framenest` or local data dir).
   - How `application.py` and `x_acquisition.py` / `media_analysis_lifecycle.py` dynamically observe the runtime setting without service restart.
   - Initial value resolution (environment variable default override vs persisted runtime value).
   - Verify: no `sudo`, no editing tracked git files at runtime, no schema `0034` unless strictly necessary (prefer non-schema or existing tables if viable; freeze the exact persistence mechanism).

2. **API & Route Policy (Tailscale Ingress & Capabilities):**
   - Exact endpoints (e.g. `GET /api/admin/settings/automatic-analysis` and `PUT /api/admin/settings/automatic-analysis` or similar).
   - Capability gate: which capability is required? (`analysis.run` ∧ `provider.operate` / `metadata.canonical.write` or dedicated admin capability). Ordinary must get 403.
   - Tailscale ingress route policy: is this route an ordinary Tailscale authenticated route or does it require `companion_mutation`? Evaluate whether adding a 5th `companion_mutation` is required or if it uses standard Tailscale session authentication (Origin + `X-FrameNest-Request` header). Freeze the exact policy.
   - Audit logging: record setting changes in audit log (`audit_action`).

3. **Extension UI & UX Flow (`extension/ui/sidebar.html|js|css`):**
   - Placement in Settings dialog: "Administration" section below origin/connection controls.
   - Visibility condition: displayed only when authenticated user has administrator capability (`analysis.run` / `provider.operate`).
   - Loading state: fetches current setting on Settings open.
   - Toggle behavior:
     - Checking ON: triggers confirmation dialog explaining that newly captured X media will automatically send preview frames to the configured server-side AI provider and incur usage cost.
     - Confirming: issues PUT to server, updates state.
     - Dismissing: reverts checkbox without sending PUT.
     - Unchecking OFF: issues PUT to disable, no extra confirmation required.
   - Error handling: network/server error displays localized error message in Settings.

4. **Audience & Capability Gates:**
   - Administrator vs Ordinary: ordinary companion users do not see the Administration section in Settings (and server endpoints return 403).
   - Unauthenticated / Disconnected: Administration section is hidden.

5. **Test Strategy:**
   - Server contract tests: capability checks (403 for ordinary, 200 for admin), persistence across factory re-instantiation, dynamic reaction during acquisition.
   - Extension / Frontend tests: `tests/companion_review_extension.test.js`, `tests/tailscale_identity_frontend.test.js`, etc.

6. **Docs & Architecture Records:**
   - Outline new ADR (e.g. ADR-0079: Administrator Automatic Analysis Runtime Setting in Companion).
   - Living doc alignment: PRODUCT.md, SPEC.md, `docs/X_COMPANION.md`.

7. **Out of Scope (name explicitly):**
   - Cover Studio, VPS, Funnel.
   - Automatic analysis for YouTube.
   - Ordinary user auto-analysis.
   - Changing default in git (default remains false).

8. **Proposed Implementation Allowlist & Validation Ladder:**
   - Exact file paths proposed for modification.
   - Commit structure.
   - Test commands.

9. **Numbered Cooperator Re-Test List:**
   - Numbered list of human-observable checks (1–N) on live NUC.

## Execution Route Binding (RF-16)

Python evidence uses `./.ap/ap project check` and `./.ap/ap exec`.
JavaScript evidence uses `node --test`.
NUC SSH gate is not activated.

## Positive Authority

- Read-only repository inspection at exact baseline.
- Write EXACTLY ONE file:
  `/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/06_report_00.md`
  (or chat output if planning mode prohibits writes).

## Negative Authority

- No FrameNest product edits.
- No Git writes.
- No NUC / SSH / sudo / publication.

## Report Contract

Terminal report identity: `06_report_00.md`
Begins EXACTLY: `### Report for ORCHESTRATOR_CHAT`
Professional English.
Follows all items in Plan Must Freeze.

## Human-Governance Routing

```text
Cooperator visibility: objective, routing, plan approval, later rendered UX acceptance
Human decision points: plan approval (approval-gated)
Internal delegation posture: not-used
Accountable Worker: one WORKER (this session)
```

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/
Trace project key: framenest
Trace logical-whole projection identity: framenest-companion-r4-automatic-analysis-settings-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace companion outcome: report
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 06_planning_00.md
Destination path: /home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/06_planning_00.md
Archival: wait-for-report
```

## Surface And Model Routing (requested)

```text
Client/surface announcement: Cursor Agent chat; native planning mode required
Recommended client/surface: fresh Worker Agent session
Recommended model: current High-capable Agent (Cooperator-selected High; no Max)
Recommended reasoning: High — security + runtime persistence + companion UI
Enhanced/maximum mode: requested off
Automatic model selection: off
Independence requirement: none
Worker topology: single-active
```
