### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-public-published-surface-and-tailscale-workspace  
Worker session ordinal: 01  
Worker exchange ordinal: 02

Status: PASS  
Phase-qualified result: not-applicable  
Plan disposition: approval-gated  
Logical-whole closure: not-closed

Exchange 01's plan content is preserved verbatim as the decision record below.
This exchange performed report rendering only: it did not reopen, revise,
extend, approve, or implement the plan.

## Capability handshake

| Material row | Requested | Observed or unknown | Evidence class |
|---|---|---|---|
| Product/client | Strongest available Worker client | Codex native planner surface | directly observed |
| Exact model | Strongest available listed Worker model | Exact model identifier not exposed | unknown/not observably exposed |
| Reasoning | Extra High | Effective reasoning setting not exposed | unknown/not observably exposed |
| Effective context | Sufficient planning context | No capacity/usage telemetry; one transparent compaction occurred without losing the evidence chain | directly observed; unknown/not observably exposed |
| Native planning, exchange 01 | Required | Enabled and enforcing read-only planning | directly observed |
| Native planning mode this exchange | `not-used` | Native Plan Mode is off; report-file rendering is available | directly observed |
| Approval/permissions | Plan-only, approval-gated | Approval policy is `never`; filesystem is technically unrestricted, but authority is limited to the report path | directly observed |
| Repository | Canonical checkout and exact baseline | `/home/agile/Projects/framenest`; branch `feat/x-meme-browser-companion`; requested HEAD was established in exchange 01 | directly observed |
| Git containment | Meta report only | No Git operations; only the authorized report artifact was written | directly observed |
| Python, `.venv`, `ap exec` | Must remain unused | Unused | directly observed |
| Network, NUC, SSH, sudo, secrets | Must remain unused | Unused; no live deployment claims made | directly observed |
| Browser/provider calls | None | Unused | directly observed |

Start commit: `37da5f2b7edf8286028dbc7a0dbca65f2d031e60`  
End commit: `37da5f2b7edf8286028dbc7a0dbca65f2d031e60`  
Local `origin/main` ref observed in exchange 01: `0fe2b32e0fed2ecaccf1a481d99be5657d42b77b`  
AP checkout and gitlink observed in exchange 01: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`  
Schema head: `0032`

# FrameNest dual-audience architecture plan

## Architecture decision

Use one authoritative catalog and media store with two separately composed applications and listeners:

```text
Tailscale workspace
  -> authenticated Tailscale Serve
  -> /run/framenest/framenest.sock
  -> existing tailscale_uds application
  -> catalog/media read-write authority

Public HTTPS origin
  -> public TLS reverse proxy
  -> distinct public Unix socket
  -> new public_published_uds application
  -> same catalog/media, read-only
```

The public application must be assembled from a public route allowlist. It must not mount the full application and depend solely on middleware to hide privileged routes.

This is required because [application.py](/home/agile/Projects/framenest/src/framenest/adapters/api/application.py) currently mounts all routers in TCP mode, while the explicit identity and route-policy middleware in [tailscale_ingress.py](/home/agile/Projects/framenest/src/framenest/adapters/api/tailscale_ingress.py) is installed only for `tailscale_uds`. Publicly binding that full application would expose a materially different trust boundary.

The workspace remains the only writer, migration owner, background-job owner, and provider-facing process. The public process opens SQLite through a read-only URI, reads media and derivatives without generating them, and fails startup rather than falling back to a writable or full-application configuration.

### Publication gate correction

The proposition that administrator `PUT /api/admin/media/{media_id}/content-publication` is currently the only publication path is false. Companion Apply currently inserts `media_content_publications` with origin `companion_review` in [companion_review_repository.py](/home/agile/Projects/framenest/src/framenest/infrastructure/persistence/companion_review_repository.py); explicit administrator publication is the other insertion path in [content_publication_repository.py](/home/agile/Projects/framenest/src/framenest/infrastructure/persistence/content_publication_repository.py).

The target decision is:

- Administrator `PUT /api/admin/media/{media_id}/content-publication`, guarded by `media.content.publish`, becomes the sole future promotion and unpublication path for every media type, including movies.
- Companion Apply continues applying reviewed metadata but must never publish.
- Historical `companion_review` publication rows and the enum value remain readable; no destructive rewrite or downgrade is performed.
- Readiness remains title + description + at least one canonical tag.
- Unpublishing stops future public requests. It cannot revoke bytes already received by public clients.

ADR-0074 must explicitly supersede ADR-0068’s readiness-triggered publication decision and ADR-0073’s preservation of that behavior, while preserving ADR-0049’s publication table and readiness model.

## Audience and interface model

### Audience bootstrap

Add `GET /api/audience/me` to each UI composition:

```json
{
  "audience": "public_published | tailscale_workspace | trusted_loopback",
  "identity": {
    "login": "string",
    "display_name": "string",
    "role": "user | admin",
    "provenance": "string"
  },
  "capabilities": ["string"]
}
```

`identity` is `null` for public and trusted-loopback callers. Public callers are not assigned a fake role or identity. Existing `GET /api/identity/me` stays workspace-only.

The frontend must bootstrap from this endpoint, treat missing/invalid bootstrap state as having no capabilities, and remove the permissive fallback in [app.js](/home/agile/Projects/framenest/src/framenest/adapters/api/web/app.js). Privileged controls start hidden and are explicitly enabled only for the resolved audience.

### Public audience

Identity-absent public callers receive only:

- `gallery.read`
- `media.original.read`

Public routes are exact GET-only routes:

- `/`
- `/assets/app.js`
- `/assets/styles.css`
- `/api/audience/me`
- `/api/media`
- `/api/media/{media_id}`
- `/api/canonical-tags`, filtered to tags represented by published media
- `/api/media/{media_id}/metadata`
- `/api/media/{media_id}/locations/{location_id}/content`
- `/api/media/{media_id}/locations/{location_id}/gallery-preview`
- `/api/media/{media_id}/cover-thumbnail`

The public catalog projection includes only opaque media/location IDs and user-facing published data: media kind, category/source, title, description, ordered tags, public creator display fields, cover readiness, and location availability. It excludes `library_id`, relative paths, file timestamps and sizes, processing state, internal collection state, stable provider IDs, aliases, and workflow metadata.

Public behavior:

- Catalog search and all direct reads recheck durable publication truth.
- Unknown and unpublished items return the same sanitized `404`.
- Every unlisted route or method returns sanitized `404`, including health, status, identity, libraries, uploads, downloads, AI, aliases, X/YouTube, companion review, operator, admin, OpenAPI, and docs.
- Tailscale identity headers are never trusted and cannot widen access.
- No CORS or public mutation support is added.
- API and content responses initially use no shared caching so an unpublished item is not retained by a reverse-proxy cache.
- Published movies appear in search and Details and support Range playback. ADR-0070’s companion movie exclusion remains intact.

The existing Attach bridge needs no new server mutation: it ultimately reads the content route using opaque media/location IDs. Until the parked public-companion successor reconnects the extension to the public origin, the public website provides search/view and the safe content seam but must not claim completed end-user Attach acceptance.

### Workspace audience

Add these capabilities to [identity_access.py](/home/agile/Projects/framenest/src/framenest/domain/identity_access.py):

- `media.workspace.read` — ordinary and administrator roles.
- `analysis.propose` — ordinary and administrator roles.
- `metadata.alias.team.read` — administrator only.

Workspace behavior:

- Existing `upload.submit`, `youtube.request`, and `x.request` remain the ways ordinary users add media.
- Add `GET /api/workspace/media`, guarded by `media.workspace.read`, returning the caller’s upload, YouTube, and X-attributed media whether published or unpublished.
- This is contributor-scoped audience extension, not ownership or a personal library. A medium may have several contribution claims.
- Extend the shared content audience policy so a caller may read their own upload-attributed content; existing YouTube/X requester-private extensions remain.
- Keep `GET /api/media` published-only.
- Enhance administrator `GET /api/admin/media` with contribution attribution and an optional normalized contributor filter. It continues returning all catalog media, including unattributed and unpublished items, under `media.workflow.read`.
- Add `POST /api/workspace/media/{media_id}/analysis-proposals`, guarded by `analysis.propose`. It creates a durable administrator-visible proposal and audit event but never calls a provider, starts analysis, or toggles automatic analysis.
- Add `GET /api/admin/analysis-proposals` under administrator workflow/analysis capabilities.
- Add `GET /api/admin/media/{media_id}/aliases`, requiring both `media.workflow.read` and `metadata.alias.team.read`, with audited access. Ordinary users retain only their own alias route; public callers receive `404`.

Existing `metadata.canonical.write`, `analysis.run`, `media.workflow.read`, and `media.content.publish` continue representing administrator authority. Tailscale membership alone never grants administrator capabilities.

## Public ingress ranking

1. **Distinct public HTTPS origin to the dedicated public ASGI socket — recommended.** It preserves one catalog while making the public route graph structurally incapable of reaching workspace APIs. The TLS/reverse-proxy product, hostname, and host placement are intentionally deferred to a separately authorized operational preflight.
2. **Tailscale Funnel to the dedicated public socket — contingency only.** It may be considered through a new operational ADR, never against `/run/framenest/framenest.sock`. It ranks lower because accepted deployment truth currently disables Funnel and it couples public availability to the NUC/Tailscale control plane.
3. **Static published export.** Strong isolation, but it introduces synchronization state and weakens live search, Range playback, movies, unpublication, and Attach.
4. **Later VPS.** Potential long-term host for the same public composition, but it requires a catalog/media projection or private tunnel and expands this work into cloud operations.

Rejected: two catalogs, optional identity on the workspace listener, public TCP binding of the current full app, Funnel to the administrator socket, or UI hiding as authorization.

## First bounded implementation whole

Create an ADR-only decision package:

- Add `docs/adr/0074-dual-audience-public-published-and-tailscale-workspace-boundary.md` with status `Proposed`.
- Add it to `docs/adr/README.md` as `Proposed`.
- Record the two-listener/one-catalog architecture, exact public route and response policy, audience bootstrap, capability additions, contributor-scoped workspace model, publication supersessions, public movie behavior, deferred companion reconnect, and phased rollout.
- Narrowly supersede the conflicting statements in ADR-0048, ADR-0068, and ADR-0073; supplement ADR-0049, ADR-0053/0054, ADR-0062, ADR-0063, and ADR-0070.
- Do not update living documents to claim shipped behavior. Update `SPEC.md`, `SERVER.md`, `SECURITY.md`, and the NUC runbook only after explicit acceptance and as implementation truth changes.
- Do not mark the ADR `Accepted` without explicit Orchestrator/Cooperator approval.

Entry evidence:

- Exact baseline and clean worktree established.
- Current ingress supports only `tcp` and `tailscale_uds`.
- Current full TCP composition is not a safe public surface.
- Companion Apply is a second current publication path.
- ADR-0074 is the next available ADR number.

Exit evidence:

- Proposed ADR and index link are internally consistent.
- Supersession, route, capability, and phase matrices match the inspected repository.
- Markdown/link checks and `git diff --check` pass.
- No runtime, deployment, or accepted-decision claim is made.
- Worker stops for approval.

Immediate successor after ADR acceptance: remove future companion-triggered publication while preserving Apply metadata behavior and historical publication-origin compatibility.

## Ordered successor wholes

1. Correct the sole publication gate and add focused compatibility tests.
2. Implement the local-only `public_published_uds` application, read-only engine, audience bootstrap, redacted DTO, public frontend branch, exact route inventory, and published movie/Range support. Do not expose it externally.
3. Perform independent security acceptance, then a separately authorized public TLS/reverse-proxy deployment preflight. No NUC, DNS, Funnel, firewall, or router mutation occurs before that authority.
4. Implement contributor-scoped workspace media, upload audience extension, and administrator contribution filtering.
5. Implement durable ordinary-user analysis proposals without enqueue/provider execution.
6. Implement audited administrator team-alias reads.
7. Reconnect the parked Brave companion to the public origin for published search/Attach/view only; do not expose the administrator review inbox there.
8. Unpark the separate 03/10 Brave acceptance backlog only on Michal’s explicit request and against the origin and SHA matching that test.

## Test and acceptance scenarios

- Companion Apply updates metadata but never creates publication; explicit administrator PUT publishes and unpublishes; historical `companion_review` rows still load.
- Public route inventory is one-to-one with the allowlist; every admin, mutation, health, operator, upload, alias, AI, companion, docs, and download route returns `404`.
- Guessed unpublished media, metadata, content, preview, and cover URLs are indistinguishable from unknown IDs.
- Published GIF, image, video, and movie reads work; video/movie Range requests return correct partial content.
- Public catalog payloads contain no library/path/workflow/private-alias fields.
- Spoofed Tailscale identity or mutation headers do not alter public capabilities.
- Public startup fails closed on missing schema, non-read-only database configuration, or unavailable catalog.
- Frontend bootstrap failure exposes no privileged controls and performs no privileged startup calls.
- Ordinary users see their own attributed unpublished media and bytes, never another user’s; administrators see all and may filter by contributor.
- Analysis proposal creation performs no provider or analysis enqueue call.
- Ordinary and public callers cannot enumerate team aliases; administrator reads are capability-checked and audited.
- Publication and unpublication become visible to new public requests without a second-catalog synchronization job.

## Assumptions and negative space

- Attribution records are contribution evidence, not ownership.
- Public publication is externally irreversible once bytes have been downloaded.
- Public hostname, TLS product, and deployment host are deliberately outside the ADR-only whole; the accepted boundary is a distinct origin and socket.
- Automatic analysis remains disabled.
- No registration, billing, payments, SaaS tenancy, personal libraries, second database, anonymous upload, public aliases, public analysis, router forwarding of the admin API, companion chrome work, or exploratory NUC Funnel change is introduced.

## Rendering result

Changed files and purpose:

- `/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/01_report_00.md` — missing AP terminal planning report rendered from the frozen exchange 01 decision record.

Validation: bounded readback of the report header, coordinate occurrence counts,
required handshake row, frozen-plan section inventory, and terminal structural
fields. No Python, tests, `ap exec`, browser, network, provider, NUC, SSH, sudo,
or Git operation was used.

Commit and push result: not authorized; not performed.

Resolved Execution Issues / Near-Misses: none.

Pre-Existing Failure Classification: none.

Deviation, risk, or missing evidence: none for this rendering-only exchange.
The plan remains advisory and approval-gated; this report is not implementation
or acceptance authority.

Smallest next step: Orchestrator review of this rendered planning report and an
explicit accept, revise, or reject decision. Any implementation requires a new
complete prompt with explicit implementation authority.

Report justification: new-mutation

Authority expiry: this report-rendering authority expires with submission of
this terminal report. No further planning, implementation, acceptance,
repository mutation, publication, deployment, or logical-whole closure is
authorized.
