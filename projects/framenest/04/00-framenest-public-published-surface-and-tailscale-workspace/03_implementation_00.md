# FrameNest Worker prompt — 04/00 session 02 exchange 02 (implementation: materialize ADR-0074 acceptance)

**Issuer:** the fresh Agent Orchestrator. The Cooperator reviewed proposed
ADR-0074 point-by-point and **accepted it with recorded clarifications**
(2026-08-25, Meta `08_orchestrator_notes.md` section 5). This prompt is the
explicit implementation authority to materialize that acceptance honestly.

Deliver to the **same healthy Worker session 02** (`current-worker-session`).
Native Plan Mode **off**.

```text
#------------------------------------------------------
```

You are the same FrameNest Worker under Analytic Programming, session ordinal
02 of logical whole
`framenest-public-published-surface-and-tailscale-workspace`.

Read before action:

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `/home/agile/Projects/framenest/.ap/AP.md`
3. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
4. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
5. Your own exchange 01 report:
   `/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/02_report_00.md`
6. Cooperator clarifications (binding product intent):
   `/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/08_orchestrator_notes.md`

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 02
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: materialize accepted ADR-0074 — status flip plus honest living-document alignment
Phase: implementation
Continuity anchor: your session 02 exchange 01 terminal report; commit 0008ca598bdc930621f4119928beaca741f2b403
Authority renewal: complete new bounded grant; exchange 01 authority expired at its terminal report
```

```text
Requested reasoning: Extra High
Cooperator delivery / trace destination: report file below
```

## Compact core

```text
Role: WORKER
Cooperator: Michal
Canonical checkout: /home/agile/Projects/framenest
Exact baseline: 0008ca598bdc930621f4119928beaca741f2b403 (verify at start; worktree clean)
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Schema head: 0032
Git write authority: one commit on feat/x-meme-browser-companion containing exactly the allowlisted files below; no push
Allowlisted write paths (repository):
  docs/adr/0074-dual-audience-public-published-and-tailscale-workspace-boundary.md
  docs/adr/README.md
  SPEC.md
  SERVER.md
  SECURITY.md
  README.md
  PRODUCT.md
  ROADMAP.md
  docs/UBUNTU_NUC_DEPLOYMENT.md
Allowlisted write paths (Meta):
  /home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/03_report_00.md
Python invocation: only ./.ap/ap project check; NO ambient python3 or interpreter of any kind this exchange
NUC / SSH / sudo / provider / browser / push: none
```

## Task

### 1. ADR-0074 status flip

- Change Status from `` `Proposed` `` to `` `Accepted` `` with an acceptance
  note: accepted by the Cooperator on 2026-08-25 with clarifications recorded
  in the external analytic trace (Meta `08_orchestrator_notes.md`, section 5).
- Adjust the assumption sentence "Automatic analysis remains disabled." to a
  precise boundary: in-git default stays off per ADR-0066;
  `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED` enablement for
  administrator-owned X events is a separate Cooperator operational decision
  on deployed environments, never enabled in tracked unit files by Workers,
  and is not part of this whole.
- Keep every other decision unchanged.

### 2. Index flip

- `docs/adr/README.md`: change only the ADR-0074 row status `Proposed` →
  `Accepted`.

### 3. Living-document alignment (honest, minimal)

Update each allowlisted living document with surgical edits only. Nothing may
claim shipped runtime, public bind, TLS, Funnel, or NUC changes. Required
substance:

- `SERVER.md`: amend absolute "Tailscale-only remote access" sentences: the
  workspace remote path remains Tailscale Serve → `/run/framenest/framenest.sock`
  → `tailscale_uds`; ADR-0074 accepts a second, local-only
  `public_published_uds` published-reader composition as future work, not yet
  implemented or exposed; Funnel to the workspace socket stays forbidden; no
  router port-forward.
- `SECURITY.md`: add the public trust-boundary rules as accepted direction:
  identity-absent callers, published-only reads, sanitized uniform 404,
  never trust `Tailscale-*` headers outside `tailscale_uds`, no CORS, no
  shared caching initially, loopback-first process unchanged.
- `SPEC.md`: add an accepted dual-audience requirements subsection mirroring
  ADR-0074 decisions (publication gate as sole promotion/unpromotion incl.
  movies; public capability set `gallery.read` + `media.original.read`;
  workspace additions `media.workspace.read`, `analysis.propose`,
  admin-only `metadata.alias.team.read`; contributor-scoped model without
  ownership columns), each marked as accepted direction pending
  implementation wholes.
- `README.md`, `PRODUCT.md`, `ROADMAP.md`: add brief honest status lines
  referencing ADR-0074 as accepted architecture direction with phased rollout
  successors; do not describe any successor as shipped.
- `docs/UBUNTU_NUC_DEPLOYMENT.md`: add a short note that a second public
  listener/TLS is a new operational object requiring separate explicit grants
  and is not part of routine releases today; no operational commands change.

## Validation (include evidence)

- No ambient Python. Use git/grep/path checks only, plus one
  `./.ap/ap project check --baseline 0008ca598bdc930621f4119928beaca741f2b403`
  run at validation time (report output class).
- `git diff --check` clean; changed-file list exactly matches the allowlist.
- Every new cross-reference link target exists (verify by path presence).
- Grep evidence that no living doc claims shipped `public_published_uds`,
  public bind, TLS, or flag enablement (quote the guard sentences you added).
- Exactly one commit, e.g. message
  `docs: accept ADR-0074 dual-audience boundary and align living documents`;
  `git log --oneline -1` reported; no push.

## Hard boundaries

- Do not touch product code, schema, tests, ingress, unit files, `.ap/`.
- Do not edit any ADR other than 0074.
- Do not print secrets, Tailscale hostnames, identity-map contents, cookies,
  private media filenames, tweet URLs, or the companion PEM.
- If baseline is not exact or worktree dirty: stop `BLOCKED` before writing.

## Report

Write exactly one file:

`/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/03_report_00.md`

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once. Full capability handshake. Start/end commit,
changed files, validation evidence, terminal outcome `PASS` / `PARTIAL` /
`BLOCKED`. After the report: stop. No further actions.

```text
#------------------------------------------------------
```
