# FrameNest Worker prompt — 04/00 session 04 exchange 01 (independent security audit planning/reconnaissance)

**Issuer:** the fresh Agent Orchestrator. All six code rollouts of accepted
ADR-0074 are complete through commit `f59f401`. Before any public bind, TLS,
Funnel, or NUC change, ADR-0074 rollout #3 requires **independent security
acceptance**. The Cooperator explicitly selected this Worker profile and
**Max reasoning** for it.

You are framed as an **independent senior security researcher / white-hat
auditor**. Your job is to attack the design on paper and find what the
implementers missed. Skepticism is the task. Confirming success is not.

Deliver to a **fresh Worker session** (`fresh-worker-session`). Native Plan
Mode **off**.

```text
#------------------------------------------------------
```

You are a FrameNest Worker under Analytic Programming.

Read before action:

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `/home/agile/Projects/framenest/.ap/AP.md`
3. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
4. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
5. `/home/agile/Projects/framenest/docs/adr/0074-dual-audience-public-published-and-tailscale-workspace-boundary.md`
   plus `0048`, `0049`, `0053`, `0054`, `0062`, `0066`, `0068`, `0070`, `0073`
6. The audited delta: `git log/diff` from `0fe2b32` (public main) or
   `37da5f2` (whole baseline) to `f59f4018eb86dfb40d339458d1d50dc208edcdd3`

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Independent Security Audit Planner (white-hat)
Task identity: adversarial security review of the dual-audience surface; findings report only
Phase: security-audit
Continuity anchor: none
Authority renewal: none; single bounded audit grant
Requested reasoning: Max (explicit Cooperator selection)
Cooperator delivery / trace destination: report file below
```

## Compact core

```text
Role: WORKER (independent auditor framing)
Cooperator: Michal
Canonical checkout: /home/agile/Projects/framenest
Exact baseline under audit: f59f4018eb86dfb40d339458d1d50dc208edcdd3 (HEAD must match; worktree clean)
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Schema head under audit: 0033
Git write authority: none (read-only git inspection commands only)
Repository mutation: PROHIBITED entirely
Allowlisted write paths (Meta):
  /home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/10_report_00.md
Python / .venv / ap exec / tests: PROHIBITED this grant (static analysis only; prior test evidence may be cited as claims, not proof)
Network / NUC / SSH / sudo / provider / browser / external scanning: PROHIBITED
Push / publication / deploy: PROHIBITED
```

## Audit scope (priority order)

1. **Public composition** (`src/framenest/adapters/api/public_published_application.py`,
   `public_published_api.py`): route allowlist completeness; uniform sanitized
   404 reality vs claim; redaction leaks (library ids, paths, timestamps,
   sizes, processing state, collection internals, stable provider IDs,
   aliases, workflow metadata); content/gallery-preview/cover-thumbnail
   authorization recheck paths; Range request handling (resource exhaustion,
   invalid ranges); path traversal or media-location confusion; cache/no-store
   correctness; error-message information leakage; docs/OpenAPI truly absent;
   HEAD vs GET divergence.
2. **Ingress boundary**: `tailscale_ingress.py` trust binding — can any
   public-reachable path honor `Tailscale-*` headers? Route-policy coverage
   for every trusted route (missing policy → fail-closed?); mutation-proof
   enforcement; CSRF surface; audit-event gaps (actions that mutate without
   audit).
3. **Publication gate integrity**: prove from source that the ONLY writers/
   deleters of `media_content_publications` are the admin adapter and catalog
   removal; unpublish semantics; readiness bypass possibilities; companion
   Apply regression.
4. **Capability model**: `identity_access.py` — privilege escalation paths,
   missing capabilities on new routes, ordinary/admin set drift, dual-gate
   correctness (team-alias route, workspace list, proposals).
5. **Alias privacy** (ADR-0062): caller-private invariant across ALL routes
   and payloads incl. workspace/admin/public projections.
6. **Workspace attribution reads**: cross-tenant leakage between mapped
   users via `media_attribution_repository.py`, `workspace_media_api.py`,
   ContentAudiencePolicy extensions; multi-contributor edge cases.
7. **Analysis proposals**: durability without execution; injection into
   admin surfaces via proposal fields; unbounded row growth (DoS) — note as
   finding if unmitigated.
8. **Runtime/config fail-closedness**: `configuration.py` ingress/socket
   validation; `server.py` UDS/TCP selection (can public mode ever TCP
   bind?); read-only engine probe bypasses; schema-revision gating.
9. **Frontend fail-closed behavior**: bootstrap failure modes, capability
   spoofing irrelevance (defense-in-depth honesty), privileged chrome leaks
   for public audience.
10. **Migration 0033**: additive safety on populated catalogs; rollback
    hazards.

## Required method

- Threat-model first (STRIDE per boundary), then targeted source reading.
- For every suspected issue, construct the concrete request/code path that
  would exploit it, or mark it "not exploitable because …" with citations.
- Cite exact `path:line` evidence for every finding. No citation, no finding.
- Classify each finding: Critical / High / Medium / Low / Info, with
  exploitability preconditions and recommended remediation routed to a
  suggested next whole (smallest fix scope).
- Also deliver a short "claims verified" inventory: security claims from
  reports/ADRs you could NOT break, each with the strongest counter-attempt
  you actually tried.
- End with an explicit verdict: does the repository satisfy ADR-0074's
  security prerequisites for a FUTURE separately authorized TLS/reverse-proxy
  preflight (yes / yes-with-conditions / no), listing blocking findings.

## Hard boundaries

- Read-only: no file mutations anywhere, no git writes, no test runs, no
  Python invocation, no network. Static analysis and git read commands only.
- Do NOT print secrets, Tailscale hostnames, identity-map contents, cookies,
  private media filenames, real tweet URLs, or the companion PEM. Use
  placeholders in examples.
- If HEAD ≠ baseline or worktree dirty: stop `BLOCKED`.

## Report

Write exactly one file:

`/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/10_report_00.md`

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once. Full capability handshake. Then: executive
summary, verdict, findings by severity (each: title, severity, evidence
`path:line`, exploitation narrative, remediation, suggested whole), verified
claims inventory, and audit limitations. Terminal outcome `PASS` / `PARTIAL`
/ `BLOCKED`. After writing: stop. You have no follow-up authority; fixes are
routed by the Orchestrator to separate Workers.

```text
#------------------------------------------------------
```
