# FrameNest Worker prompt — 04/00 session 02 exchange 04 (implementation: administrator unpublish on the sole publication route)

**Issuer:** the fresh Agent Orchestrator. Exchange 03 accepted. ADR-0074
names the administrator
`PUT /api/admin/media/{media_id}/content-publication` as the sole future
**promotion and unpublication** path; today the route can only publish.
This grant completes that decision before any public reader exists.

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
5. `/home/agile/Projects/framenest/docs/adr/0074-dual-audience-public-published-and-tailscale-workspace-boundary.md`
   ("Publication gate": sole promotion/unpublication path)
6. Your exchange 03 report:
   `.../04_report_00.md` in this Meta folder

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 02
Worker exchange ordinal: 04
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: implement administrator unpublish on the sole content-publication route
Phase: implementation
Continuity anchor: your session 02 exchange 03 terminal report; commit ffef45737667de41f3b2a0066511a2f0d22473df
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
Exact baseline: ffef45737667de41f3b2a0066511a2f0d22473df (verify at start; worktree clean)
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Schema head: 0032 (no migrations authorized)
Git write authority: one commit on feat/x-meme-browser-companion containing exactly allowlisted-path changes; no push
Allowlisted change scope (repository):
  src/framenest/adapters/api/content_publication_api.py
  src/framenest/application/content_publication.py
  src/framenest/application/ports/content_publication_repository.py
  src/framenest/infrastructure/persistence/content_publication_repository.py
  src/framenest/adapters/api/web/app.js (only if Manage media needs an honest unpublish control)
  src/framenest/adapters/api/web/styles.css (only for that control)
  tests/** (focused compatibility tests)
  SPEC.md (only the unpublish requirement marker)
Allowlisted write paths (Meta):
  /home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/05_report_00.md
Python/test execution route (canonical, exclusive):
  ./.ap/ap exec runtime-info / test-focus / test with exact --baseline ffef45737667de41f3b2a0066511a2f0d22473df
  JavaScript tests exactly as docs/WORKER_EXECUTION_CONTRACT.md declares them.
  NO ambient python/python3/.venv invocation of any kind.
NUC / SSH / sudo / provider / browser automation / push: none
```

## Task

1. Extend the existing administrator route so the same capability-gated,
   audited endpoint performs unpublication (ADR-0074 "Publication gate").
   Choose the smallest honest contract shape (for example a JSON body such
   as `{"published": false}` defaulting to publish-preserving behavior, or
   an explicit action field) and keep backward compatibility for callers
   that omit the body. Statuses must be truthful and idempotent-friendly,
   e.g. `published`, `already_published`, `unpublished`,
   `already_unpublished`.
2. Unpublish removes the durable publication row for that media (the row
   pattern already exists in `catalog_removal_repository.py`). It never
   touches media bytes, metadata, aliases, analysis state, or history rows;
   historical origin values (`companion_review`, `admin_explicit`) remain
   readable wherever they are read today. Readiness computation is
   unchanged.
3. Every unpublish mutation keeps the exact existing security envelope:
   `media.content.publish` capability, verified Serve identity, mutation
   proof requirements, audit event, sanitized errors, no-store responses.
4. If Manage media exposes a publish control, add the minimal honest
   unpublish control in the same visual language; UI hiding remains never
   the authorization mechanism.
5. Focused compatibility tests covering at least:
   - PUT publish then PUT unpublish: gallery visibility stops; row removed;
   - unpublish of an unpublished item: truthful status, no error;
   - unpublish requires the admin capability (ordinary user and
     identity-absent denials unchanged);
   - historical `companion_review`-origin item unpublishes cleanly and its
     history remains readable;
   - audit event recorded for unpublish.
6. Update the SPEC.md marker only for the unpublish requirement you actually
   completed.

## Validation (include evidence)

- `./.ap/ap exec test-focus --baseline ffef457…` over your focused set:
  PASS with counts.
- Full declared test operation (`./.ap/ap exec test --baseline ffef457…`):
  PASS; classify any pre-existing failure honestly instead of fixing it.
- Grep proof: the ONLY writers/deleters of `media_content_publications`
  rows are the administrator publication adapter and catalog removal.
  Companion path stays read-only (quote it).
- JS tests for the web control per the contract's canonical invocation, if
  you touched web assets.
- `git diff --check` clean; changed-file list within allowlist; exactly one
  commit (suggested message: `feat: administrator unpublish on the sole
  content-publication route`); `git log --oneline -1`; no push.

## Hard boundaries

- No schema/migration edits; schema head stays 0032.
- No new routes beyond the existing publication route's contract; no
  capability-table changes; no ingress/Funnel/flag changes.
- No edits to ADR bodies.
- Do not print secrets, Tailscale hostnames, identity-map contents, cookies,
  private media filenames, tweet URLs, or the companion PEM.
- Baseline mismatch or dirty worktree → stop `BLOCKED` before writing.
- Scope impossible inside the allowlist → stop `PARTIAL`/`BLOCKED` with the
  exact missing piece; never expand scope silently.

## Report

Write exactly one file:

`/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/05_report_00.md`

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once. Full capability handshake. Start/end
commit, changed files, test evidence with counts, grep proofs, terminal
outcome `PASS` / `PARTIAL` / `BLOCKED`. After the report: stop. No further
actions.

```text
#------------------------------------------------------
```
