# FrameNest Worker prompt — 04/00 session 03 exchange 03 (implementation: durable ordinary-user analysis proposals)

**Issuer:** the fresh Agent Orchestrator. Exchange 02 accepted (`5b99575`):
the contributor-scoped work gallery exists. This grant authorizes rollout #5
of accepted ADR-0074: **durable ordinary-user analysis proposals** — an
honest request channel from mapped PRO users to the administrator. It never
calls a provider, never enqueues analysis, never touches the automatic
analysis flag.

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
   ("Workspace audience", `analysis.propose`)
6. `/home/agile/Projects/framenest/docs/adr/0066-administrator-owned-x-automatic-generic-analysis.md`
   (automatic analysis boundary you must NOT cross)
7. Existing audit/mutation machinery in
   `src/framenest/adapters/api/tailscale_ingress.py` and the migration chain
   under `alembic/` (or wherever revisions live) plus
   `src/framenest/infrastructure/persistence/catalog_schema.py`
8. Your exchange 02 report:
   `.../07_report_00.md` in this Meta folder

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 03
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: implement durable administrator-visible analysis proposals without any provider execution
Phase: implementation
Continuity anchor: your session 03 exchange 02 terminal report; commit 5b9957542abfdfe6f418042a2a6628686ba35d8c
Authority renewal: complete new bounded grant; exchange 02 authority expired at its terminal report
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
Exact baseline: 5b9957542abfdfe6f418042a2a6628686ba35d8c (verify at start; worktree clean)
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Schema head: 0033 after your migration (this grant explicitly authorizes exactly one additive migration)
Git write authority: commits on feat/x-meme-browser-companion containing exactly allowlisted-path changes; coherent small commits permitted; no push
Allowlisted change scope (repository):
  src/framenest/domain/identity_access.py (add analysis.propose, ordinary + admin)
  src/framenest/adapters/api/** (workspace proposal route, admin list route, route-policy entries)
  src/framenest/application/** (proposal use-case/port modules)
  src/framenest/infrastructure/persistence/** (proposals repository, catalog_schema table)
  alembic/** (exactly one additive revision following the existing chain)
  src/framenest/adapters/api/web/app.js, styles.css (propose control + admin proposals view)
  src/framenest/adapters/api/web/index.html (chrome only)
  tests/**
  SPEC.md (only markers you actually implemented)
Allowlisted write paths (Meta):
  /home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/08_report_00.md
Python/test execution route (canonical, exclusive):
  ./.ap/ap exec runtime-info / test / test-focus with exact --baseline 5b9957542abfdfe6f418042a2a6628686ba35d8c
  JavaScript tests exactly as docs/WORKER_EXECUTION_CONTRACT.md declares them.
  NO ambient python/python3/.venv invocation of any kind.
NUC / SSH / sudo / provider / external bind / push: none
```

## Task

1. **Capability**: add `analysis.propose` to the identity-access table for
   BOTH ordinary (`user`) and administrator roles. No other capability
   changes.
2. **Durable storage**: one additive migration creating a proposals table
   (suggested name `media_analysis_proposals`) recording at minimum:
   opaque media id, proposing `login_key`, created-at ms, status (open by
   default), and nothing secret. Follow the existing catalog_schema and
   alembic revision patterns precisely; bump the declared schema head from
   `0032` to `0033` everywhere it is declared/tested. The migration must be
   additive and safe against existing catalogs.
3. **Propose route**: `POST
   /api/workspace/media/{media_id}/analysis-proposals`, guarded by
   `analysis.propose` on the trusted ingress, creating one durable proposal
   plus an audit event. It MUST NOT call any provider, enqueue any analysis
   run, flip any setting, or interact with
   `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED` in any way. Proposing for
   unknown media returns sanitized not-found; proposing twice is allowed
   (each is its own row) unless you find a stronger existing convention —
   state your choice.
4. **Admin read**: `GET /api/admin/analysis-proposals`, capability-gated
   under existing administrator workflow/analysis capabilities, paginated,
   newest first, including proposer display login, media title snapshot,
   publication/readiness state, and status. No write/lifecycle endpoints in
   this grant (dismiss/complete is later work).
5. **Frontend**: a propose-analysis control on the caller's own workspace
   items (`analysis.propose` gated) and a minimal honest administrator view
   of open proposals in the existing visual language. Public audience never
   sees either. UI hiding remains never the authorization mechanism.
6. **Focused tests** covering at least:
   - propose creates a durable row visible to admin after a fresh engine
     (durability);
   - audit event recorded; capability denials (no capability, anonymous);
   - unknown media sanitized;
   - NO provider/enqueue interaction (behavioral proof + grep proof that no
     provider/NIM module is imported by proposal code paths);
   - admin list pagination/ordering; ordinary users cannot list proposals;
     public composition 404s both routes (inventory updated);
   - migration applies cleanly on a populated 0032 catalog fixture and is
     re-runnable/idempotent per existing conventions.

## Validation (include evidence)

- `./.ap/ap exec test-focus --baseline 5b99575…` over your focused set:
  PASS with counts.
- Full declared test operation (`./.ap/ap exec test --baseline 5b99575…`):
  PASS; classify pre-existing failures honestly instead of fixing them.
- JS tests per canonical invocation if web assets changed.
- Grep proofs: proposal code imports no provider/NIM/enqueue modules; the
  public composition remains free of the two new routes (quote inventory).
- Commits: coherent small set; suggested final message
  `feat: durable ordinary-user analysis proposals`; `git log --oneline -8`;
  no push.

## Hard boundaries

- Exactly one additive migration; no destructive operations; no changes to
  existing tables/columns; schema head ends at `0033`.
- No provider, NIM, queue, scheduler, background-job, or flag changes of any
  kind. Analysis itself stays exclusively administrator-initiated as today.
- No edits to ADR bodies; living docs limited to truthful SPEC markers.
- Do not print secrets, Tailscale hostnames, identity-map contents, cookies,
  private media filenames, tweet URLs, or the companion PEM.
- Baseline mismatch or dirty worktree → stop `BLOCKED` before writing.
- Scope impossible inside the allowlist → stop `PARTIAL`/`BLOCKED` with the
  exact missing piece; record necessary deviations explicitly; never expand
  scope silently.

## Report

Write exactly one file:

`/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/08_report_00.md`

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once. Full capability handshake. Start/end
commits, changed files, migration summary, test evidence with counts, grep
proofs, terminal outcome `PASS` / `PARTIAL` / `BLOCKED`. After the report:
stop. No further actions.

```text
#------------------------------------------------------
```
