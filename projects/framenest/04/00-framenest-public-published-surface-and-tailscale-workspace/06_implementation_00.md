# FrameNest Worker prompt — 04/00 session 03 exchange 01 (implementation: local-only public_published_uds reader)

**Issuer:** the fresh Agent Orchestrator. Accepted ADR-0074 rollout #1 is
complete through commit `dd26782` (sole publication gate incl. unpublish).
This grant authorizes rollout #2: the **local-only** `public_published_uds`
public reader. Nothing may be exposed externally; no TLS, no Funnel, no NUC
changes.

Deliver to a **fresh Worker session** (`fresh-worker-session`). Native Plan
Mode **off**.

```text
#------------------------------------------------------
```

You are a FrameNest Worker under Analytic Programming.

Read before action, in this order:

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `/home/agile/Projects/framenest/.ap/AP.md`
3. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
4. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
5. `/home/agile/Projects/framenest/docs/adr/0074-dual-audience-public-published-and-tailscale-workspace-boundary.md`
   (Accepted decision record — your contract)
6. `/home/agile/Projects/framenest/docs/adr/0049-durable-content-publication-boundary.md`
   and `docs/adr/0054-requester-private-youtube-acquisition-and-promotion-boundary.md`
7. Key sources: `src/framenest/adapters/api/application.py`,
   `src/framenest/adapters/api/tailscale_ingress.py` (reference only),
   `src/framenest/domain/identity_access.py`, catalog/content repositories,
   `src/framenest/adapters/api/web/app.js`

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: implement local-only public_published_uds published-reader composition per accepted ADR-0074
Phase: implementation
Continuity anchor: none
Authority renewal: none; initial grant for this session within the same logical whole
Prior authority boundary: session 02 expired at its exchange 04 terminal report (commit dd267823490a19119575e697a4835bba94b02f7f)
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
Exact baseline: dd267823490a19119575e697a4835bba94b02f7f (verify at start; worktree clean)
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Schema head: 0032 (no migrations authorized)
Git write authority: commits on feat/x-meme-browser-companion containing exactly allowlisted-path changes; coherent small commits permitted; no push
Allowlisted change scope (repository):
  src/framenest/adapters/api/application.py (composition + ingress mode)
  src/framenest/adapters/api/** new public modules (routers, audience bootstrap, redaction)
  src/framenest/domain/identity_access.py (public-audience capability constants only)
  src/framenest/settings*/config modules for ingress mode and public socket path
  src/framenest/infrastructure/persistence/** read-only engine/session wiring for the public process
  src/framenest/adapters/api/web/app.js, styles.css, new public assets as needed
  tests/** (focused + inventory tests)
  SPEC.md, SERVER.md, SECURITY.md (only marker/status sentences you actually implemented)
Allowlisted write paths (Meta):
  /home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/06_report_00.md
Python/test execution route (canonical, exclusive):
  ./.ap/ap exec runtime-info / test / test-focus with exact --baseline dd267823490a19119575e697a4835bba94b02f7f
  JavaScript tests exactly as docs/WORKER_EXECUTION_CONTRACT.md declares them.
  NO ambient python/python3/.venv invocation of any kind.
NUC / SSH / sudo / provider / external bind / push: none
```

## Task

Implement exactly what accepted ADR-0074 decides for the public reader:

1. **New ingress mode** `public_published_uds`: a separately composed ASGI
   application mounted ONLY on an exact GET-only route allowlist:
   `/`, `/assets/app.js`, `/assets/styles.css`, `/api/audience/me`,
   `/api/media`, `/api/media/{media_id}`, `/api/canonical-tags` (filtered to
   tags represented by published media), `/api/media/{media_id}/metadata`,
   `/api/media/{media_id}/locations/{location_id}/content`,
   `/api/media/{media_id}/locations/{location_id}/gallery-preview`,
   `/api/media/{media_id}/cover-thumbnail`.
   Every unlisted route/method returns sanitized uniform `404`. Do not mount
   workspace routers and hide them with middleware.
2. **Read-only engine**: the public process opens SQLite through a read-only
   URI, never writes, never runs migrations or background jobs, never calls
   providers, generates no derivatives. Startup fails closed on missing
   schema or non-read-only configuration rather than falling back.
3. **Audience bootstrap**: `GET /api/audience/me` returns audience
   `public_published`, `identity: null`, capabilities exactly
   `["gallery.read","media.original.read"]`. Never trust or honor
   `Tailscale-*` headers in this mode; they cannot widen anything.
4. **Redacted projection**: public catalog/detail payloads expose only
   opaque media/location IDs and user-facing published data per ADR-0074;
   exclude `library_id`, relative paths, timestamps/sizes, processing state,
   internal collection state, stable provider IDs, aliases, workflow
   metadata. Unknown and unpublished items return the identical sanitized
   `404`; direct reads recheck durable publication truth.
5. **No CORS, no mutation, initially no shared caching** (no-store class
   headers on API and content responses).
6. **Movies**: published movies appear in search/details with working Range
   playback through the content route; companion movie exclusion untouched.
7. **Frontend public branch**: bootstrap from `/api/audience/me`; missing or
   invalid bootstrap means zero capabilities and zero privileged controls;
   remove the permissive loopback fallback in `app.js`; privileged controls
   render only for the resolved workspace audiences.
8. **Local-only binding**: the mode binds a distinct Unix socket (default
   separate from `/run/framenest/framenest.sock`; configurable path). No TCP
   listener for this mode. It must be startable locally for tests without
   root. No external exposure, no TLS, no Funnel, no systemd/unit changes.
9. **Focused tests** covering at least: exact route inventory one-to-one
   (unlisted → 404); guessed unpublished media/metadata/content URLs
   indistinguishable from unknown; spoofed Tailscale/mutation headers change
   nothing; redaction field proofs; published GIF/image/video/movie reads
   plus video/movie Range partial content; unpublish stops visibility
   immediately; fail-closed startup cases; bootstrap failure exposes nothing.

## Validation (include evidence)

- `./.ap/ap exec test-focus --baseline dd26782…` over your focused set:
  PASS with counts.
- Full declared test operation (`./.ap/ap exec test --baseline dd26782…`):
  PASS; classify any pre-existing failure honestly instead of fixing it.
- JS tests per canonical invocation if web assets changed.
- Grep proof: workspace-only routers are not imported by the public
  composition; the public app contains no POST/PUT/DELETE/PATCH route
  declarations (quote the inventory).
- Commits: coherent small set on `feat/x-meme-browser-companion`;
  suggested final message `feat: local-only public_published_uds reader`;
  `git log --oneline -8`; no push.

## Hard boundaries

- No schema/migration edits; schema head stays 0032.
- No capability grants beyond the two public read capabilities; no alias
  routes; no upload/AI/companion/admin/operator routes in the public app.
- No edits to ADR bodies; living docs limited to truthful status sentences
  inside the allowlisted three files.
- Do not print secrets, Tailscale hostnames, identity-map contents, cookies,
  private media filenames, tweet URLs, or the companion PEM.
- Baseline mismatch or dirty worktree → stop `BLOCKED` before writing.
- If the full slice cannot complete coherently, deliver the smallest
  coherent subset as `PARTIAL` with an exact inventory of what exists and
  what remains; never claim exposure readiness.

## Report

Write exactly one file:

`/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/06_report_00.md`

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
