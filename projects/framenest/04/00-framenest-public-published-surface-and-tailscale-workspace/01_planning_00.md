# FrameNest Worker prompt — 04/00 session 01 exchange 01 (implementation planning)

**Issuer:** the *fresh* Agent Orchestrator after reading `00_handout.md`.
This file is a complete draft. It is not a plan PASS. It is not current
authority until that Orchestrator delivers it to a Worker with Plan Mode on.

If the client cannot enable native planning mode, do **not** paste this
`required` prompt. Reissue a complete twin with `Native planning mode:
not-used` plus explicit prompt-level read-only implementation-planning
authority (PROMPT_CONTRACTS fallback).

```text
#------------------------------------------------------
```

You are a FrameNest Worker under Analytic Programming.

Read before action, in this order:

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `/home/agile/Projects/framenest/.ap/AP.md`
3. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
4. `/home/agile/Projects/framenest/.ap/PROMPT_CONTRACTS.md` (Plan-to-Execution Gate, Planning Record, compact core, capability handshake)
5. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
6. Meta restoration (evidence, not a second grant):
   `/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/00_handout.md`
7. Companion park inventory (out of scope for mutation; context only):
   `/home/agile/meta/projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/COMPANION_PARKED_BRAVE_TEST_BACKLOG.md`

Then perform **only** bounded read-only repository-grounded implementation
planning. Stop at the terminal planning report.

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Fresh Implementation Worker
Task identity: plan dual-audience published-public vs Tailscale-workspace cut
Phase: plan
Continuity anchor: none
Authority renewal: none; this is the initial grant for this logical whole
Prior logical whole identity: framenest-companion-review-inbox-ux-history-mvp
Changed objective: companion Brave UX testing parked; dual-audience public/Tailscale is the live object
```

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded dual-audience architecture; first bounded implementation slice; ADR/capability/ingress conflicts; ordered successor wholes; explicit non-goals
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: none
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
Requested product/client and exact model: Extra High reasoning; strongest available listed Worker model
Requested reasoning: Extra High
Requested native planning mode: required
```

## Compact core

```text
Role: WORKER
Cooperator: Michal
Canonical checkout: /home/agile/Projects/framenest
Exact baseline: 37da5f2b7edf8286028dbc7a0dbca65f2d031e60
Baseline meaning: verify at issue time; at predecessor rotation local HEAD was 37da5f2b7edf8286028dbc7a0dbca65f2d031e60 unpublished vs origin/main 0fe2b32e0fed2ecaccf1a481d99be5657d42b77b; do not treat 37da5f2 as live NUC
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Schema head: 0032
Git write authority: Meta report file only
Allowlisted write paths:
  /home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/01_report_00.md
Python invocation: none
NUC / SSH / sudo: none
Provider calls: none
Browser: none
Publication / deploy: none
```

```text
Cooperator delivery / trace destination: not-used
```

## Capability handshake (full)

Report each material row with: requested; observed or unknown; evidence class
(`requested` | `directly observed` | `inferred` | `unknown/not observably exposed`).

Include at least:

- Product/client and exact model
- Reasoning and effective context
- Native planning and approval/permission mode
- Repository / worktree / HEAD
- Git write containment
- Python / `.venv` / `ap exec` (must remain unused)
- Network / NUC / secrets (must remain unused)

If native planning mode is not actually enabled, stop `BLOCKED` and do not
plan. The Orchestrator must reissue the `not-used` fallback.

## Authoritative product intent (Cooperator 2026-08-25)

Plan a FrameNest that is honestly two surfaces:

1. **Tailscale workspace (paid, friends as administrators).** Mapped ordinary
   Tailscale users are a team with administrator(s). They add to a **work
   gallery**, attach, and **propose analysis**. Each mapped user has **own
   aliases**. Administrators see those users’ galleries, AI suggestions, and
   **aliases of other Tailscale users**. Administrator **Publish** in Manage
   media is the gate that makes a meme, video, gif, or **movie** visible on
   the public surface. Tailscale membership is not application administrator
   authority. “Paid” means Tailscale + identity map, not billing code.

2. **Public version (free).** Public people use a **public FrameNest origin,
   not Tailscale**. Capabilities: **search, attach, view** of **published**
   media only. No Manage media. No unpublished work gallery. No other users’
   aliases. No analysis controls.

Companion Brave extension for ordinary public people is **parked**. Public
companion, if ever resumed, would connect to the **public** origin. Do not
plan companion chrome, badge, or unpacked-extension testing in this report
except as an explicit parked successor whole.

Do not plan enabling `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED`.

The Orchestrator handout Sections 4–9 are reconnaissance hints. Prove,
cite, or replace them. Do not rubber-stamp them.

## Why planning is required

This is not “complex so plan.” These repository facts materially affect a
safe first implementation:

- ADR-0048 / SERVER / SECURITY / NUC runbook: Tailscale Serve to Unix
  socket only; Funnel disabled; no router port-forward; public bind requires
  explicit override and is not the current accepted remote path.
- ADR-0049: catalog vs content publication; ordinary Gallery is
  published-only; unpublished requires `media.workflow.read`. Remote callers
  without Serve identity currently `401` before that published list.
- ADR-0053: ordinary `upload.submit`; unpublished until admin publish; **no
  personal libraries and no media-level ownership**; no ordinary AI
  initiation; no anonymous upload; no public registration.
- ADR-0054: audience extension (not ownership tables) plus a dedicated My
  YouTube surface; Gallery list stays published-only. This is the closest
  existing rhyme for a Tailscale work gallery.
- ADR-0062: aliases are caller-private per `login_key`.
- ADR-0063: Gallery Attach is companion-hosted; side panel iframes Tailscale
  origin today.
- ADR-0066 / 0067 / 0073: companion review is administrator Tailscale
  surface; auto-analysis default off.
- ADR-0070: movies out of companion; public movie publish is a different
  surface.
- `src/framenest/domain/identity_access.py` capability table.
- Route policy is explicit and fail-closed (ADR-0048). A public origin that
  reuses the workspace listener is a trust-boundary defect, not a feature.

## Planning questions the report must answer

Be creative and precise. Recommend one architecture. Name rejected
alternatives with why. Do not paper over ADR conflicts; propose the exact
ADR supersession or additive ADR shape if a conflict is load-bearing.

1. **Two-audience model.** One catalog vs two catalogs. What is a “Tailscale
   user gallery” given ADR-0053’s exclusion of personal libraries? Prefer a
   model that can ship without inventing a second media database. Address
   the gap that ordinary users cannot see unpublished items in Gallery today.

2. **Publish gate.** Confirm or refute: administrator
   `PUT .../content-publication` remains the only promotion from workspace
   unpublished to public published, including movies.

3. **Public ingress.** Rank options (distinct public origin / reverse proxy
   to a published-only ASGI mode / Tailscale Funnel to a **non-admin**
   listener / static published export / later VPS). Fail-closed rules:
   public callers never receive unpublished bytes, admin routes, identity
   headers from Serve, companion mutation, uploads, alias writes, or
   analysis. Do **not** recommend Funneling `/run/framenest/framenest.sock`
   as it exists today.

4. **Public UX minimum.** Search, attach, view — map to existing Gallery /
   Details / attach composer routes and name which capabilities a
   **identity-absent** public caller would need. Name what must stay 401/403/404.

5. **Workspace UX minimum.** Ordinary mapped user: add, attach, propose
   analysis, own aliases. Administrator: Manage media, Publish, all
   workspace unpublished, all suggestions, all aliases. Name new
   capabilities vs today’s table.

6. **First bounded implementation whole.** Exactly one. Small enough to
   implement after plan acceptance without building the entire SaaS. It may
   be an ADR-only decision package if you prove code is unsafe before that
   ADR exists. State entry evidence, exit evidence, and the immediate
   successor whole.

7. **Ordered backlog** after that first whole (including parked companion
   public-origin reconnect, ordinary propose-analysis, admin alias read,
   movies-on-public if not in the first whole, unpark 03/10).

8. **Negative space.** What this whole must not become: public registration,
   payments, cloud SaaS, router port-forward of the admin API, auto-analysis
   on, companion chrome work, NUC Funnel “just to try.”

## Evidence rules

- Reconnaissance is read-only in `/home/agile/Projects/framenest`.
- Do not mutate repository files, git, ROADMAP, ADRs, or extension code.
- Do not run Python, tests, `ap exec`, NUC SSH, sudo, or browsers.
- Do not print secrets, Tailscale hostnames, live media titles, tweet URLs,
  cookies, or identity map contents.
- Cite exact paths, ADR numbers, and route/capability names from the tree.
- Worker reports are claims. If you cannot find a route, say so.

## Report

Write exactly one file:

`/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/01_report_00.md`

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once. Include the capability handshake. Keep
**approval-gated**. Do not self-approve.

Terminal planning outcomes: `PASS` (decision-complete plan, still not
implementation authority), `PARTIAL`, or `BLOCKED`.

A client-native planner canvas or Plan UI artifact does **not** replace this
file.

After the report: **stop**. Do not implement. Do not open a second planning
cycle. Do not edit FrameNest.

```text
#------------------------------------------------------
```
