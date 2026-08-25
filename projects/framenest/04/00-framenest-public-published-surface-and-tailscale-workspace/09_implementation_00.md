# FrameNest Worker prompt — 04/00 session 03 exchange 04 (implementation: audited administrator team-alias reads)

**Issuer:** the fresh Agent Orchestrator. Exchange 03 accepted (`da06109`,
schema head `0033`). This grant authorizes rollout #6 of accepted ADR-0074:
**audited administrator team-alias reads** — the last code rollout of this
logical whole before independent security acceptance.

Deliver to the **same healthy Worker session 03** (`current-worker-session`).
Native Plan Mode **off**.

```text
#------------------------------------------------------
```

You are the same FrameNest Worker under Analytic Programming, session ordinal
03 of logical whole
`framenest-public-published-surface-and-tailscale-workspace`.

Read before action:

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `/home/agile/Projects/framenest/.ap/AP.md`
3. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
4. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
5. `/home/agile/Projects/framenest/docs/adr/0074-dual-audience-public-published-and-tailscale-workspace-boundary.md`
   ("Workspace audience", `metadata.alias.team.read`)
6. `/home/agile/Projects/framenest/docs/adr/0062-per-user-media-alias-overlay.md`
   (caller-private overlay you must not weaken)
7. Your exchange 03 report:
   `.../08_report_00.md` in this Meta folder

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 03
Worker exchange ordinal: 04
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: implement capability-gated audited administrator team-alias reads plus schema-head prose alignment
Phase: implementation
Continuity anchor: your session 03 exchange 03 terminal report; commit da06109bd4adab6f00eea2db02dc2787c98da10c
Authority renewal: complete new bounded grant; exchange 03 authority expired at its terminal report
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
Exact baseline: da06109bd4adab6f00eea2db02dc2787c98da10c (verify at start; worktree clean)
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Schema head: 0033 (no migrations authorized)
Git write authority: commits on feat/x-meme-browser-companion containing exactly allowlisted-path changes; coherent small commits permitted; no push
Allowlisted change scope (repository):
  src/framenest/domain/identity_access.py (add metadata.alias.team.read, administrator only)
  src/framenest/adapters/api/** (admin alias-read route/module, route-policy entry)
  src/framenest/application/** and src/framenest/application/ports/** and src/framenest/infrastructure/persistence/** read-side team-alias query only
  src/framenest/adapters/api/web/app.js, styles.css, index.html (minimal admin aliases view)
  tests/**
  SPEC.md (only markers you actually implemented)
  README.md, PRODUCT.md, ROADMAP.md (only the stale schema-head sentence(s): 0032 -> 0033)
Allowlisted write paths (Meta):
  /home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/09_report_00.md
Python/test execution route (canonical, exclusive):
  ./.ap/ap exec runtime-info / test / test-focus with exact --baseline da06109bd4adab6f00eea2db02dc2787c98da10c
  JavaScript tests exactly as docs/WORKER_EXECUTION_CONTRACT.md declares them.
  NO ambient python/python3/.venv invocation of any kind.
NUC / SSH / sudo / provider / external bind / push: none
```

## Task

1. **Capability**: add `metadata.alias.team.read` to the identity-access
   table for the **administrator role only**. No other capability changes;
   ordinary roles must NOT receive it.
2. **Admin read route**: add
   `GET /api/admin/media/{media_id}/aliases` requiring BOTH existing
   `media.workflow.read` AND new `metadata.alias.team.read`, returning the
   aggregated alias overlay entries across all mapped users for that media
   (login display key, alias value, timestamps as available). Read-only:
   the route and its stack must perform zero writes. Every invocation is
   audit-recorded via the trusted-ingress policy (distinct audit action,
   e.g. `metadata.alias.team.list`). Unknown media stays sanitized
   not-found.
3. **Invariants**: aliases stay caller-private per `(media_id, login_key)`
   (ADR-0062). Ordinary users keep ONLY their own alias routes; their
   payloads never include other users' aliases. Public composition returns
   uniform sanitized 404 for the new route. No alias values leak into any
   public or workspace payload.
4. **Frontend**: a minimal honest administrator aliases view in the existing
   Manage media language (per media, on demand), visible only when the
   resolved audience holds the new capability. UI hiding remains never the
   authorization mechanism.
5. **Living-doc drift fix**: update ONLY the stale schema-head sentences in
   `README.md`, `PRODUCT.md`, `ROADMAP.md` from `0032` to `0033` (the drift
   your exchange 03 honestly flagged). Nothing else in those files.
6. **Focused tests** covering at least:
   - administrator with both capabilities reads aggregated team aliases;
     audit event recorded with the distinct action;
   - denial with either capability missing (including an administrator
     lacking the new one, proving dual-gate semantics);
   - ordinary user sees only own aliases on existing routes and cannot call
     the admin route;
   - public composition 404s the route (inventory updated);
   - aggregation correctness across two mapped users' overlays for one
     media; zero-write proof (behavioral + grep);
   - schema-head sentence consistency after the prose fix.

## Validation (include evidence)

- `./.ap/ap exec test-focus --baseline da06109…` over your focused set:
  PASS with counts.
- Full declared test operation (`./.ap/ap exec test --baseline da06109…`):
  PASS; classify pre-existing failures honestly instead of fixing them.
- JS tests per canonical invocation if web assets changed.
- Grep proofs: the admin alias path performs no INSERT/UPDATE/DELETE on
  alias tables; public modules contain no alias-team references (quote).
- Commits: coherent small set; suggested final message
  `feat: audited administrator team-alias reads`; `git log --oneline -8`;
  no push.

## Hard boundaries

- No migrations; schema head stays `0033`. No alias write endpoints. No
  changes to ADR bodies. No provider/NIM/enqueue/flag changes.
- Do not print secrets, Tailscale hostnames, identity-map contents, cookies,
  private media filenames, actual alias values in reports, tweet URLs, or
  the companion PEM.
- Baseline mismatch or dirty worktree → stop `BLOCKED` before writing.
- Scope impossible inside the allowlist → stop `PARTIAL`/`BLOCKED` with the
  exact missing piece; record necessary deviations explicitly; never expand
  scope silently.

## Report

Write exactly one file:

`/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/09_report_00.md`

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once. Full capability handshake. Start/end
commits, changed files, test evidence with counts, grep proofs, terminal
outcome `PASS` / `PARTIAL` / `BLOCKED`. After the report: stop. No further
actions.

```text
#------------------------------------------------------
```
