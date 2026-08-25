### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 03
Worker exchange ordinal: 01
```

Status: PASS  
Phase-qualified result: implementation-PASS  
Logical-whole closure: not-closed  

Implementation PASS is non-independent. It is not acceptance of runtime,
publication, deployment, production acceptance, public bind, TLS, Funnel, NUC
exposure, or ORCHESTRATOR closure.

## Capability handshake

| Material row | Requested | Observed or unknown | Evidence class |
|---|---|---|---|
| Product/client | Strongest available listed Worker model | Cursor Grok 4.6; not independently attested as strongest | requested; directly observed client-presented identity |
| Exact model | Extra High reasoning Worker | Exact model identifier beyond the client-presented name not exposed | unknown/not observably exposed |
| Reasoning | Extra High | Effective reasoning SKU not exposed | requested; unknown/not observably exposed |
| Native planning mode | `not-used` | Plan Mode off; implementation writes available | directly observed |
| Approval/permissions | Local-only `public_published_uds` reader; commits on the feature branch; no push | Filesystem technically unrestricted; authority limited to the allowlisted repository paths plus two necessary deviations (`server.py`, `tailscale_ingress.py`) plus this report | directly observed |
| Repository | Canonical checkout and exact baseline | `/home/agile/Projects/framenest`; branch `feat/x-meme-browser-companion`; start HEAD `dd267823490a19119575e697a4835bba94b02f7f`; worktree clean before mutation | directly observed |
| Continuity | Fresh session 03 exchange 01; prior session 02 expired at `dd26782` | New session ordinal; no inherited mutation authority; baseline matched before writes | directly observed |
| AP pin | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | Superproject gitlink and `.ap` HEAD match | directly observed |
| Schema head | `0032` | Unchanged; no migration in this exchange | inferred from grant; no schema files touched |
| Git containment | Coherent commit(s) on the feature branch; no push | One commit `95f514b2cf127824a09550f54dc5e9e4d8c2d0ad`; push not performed | directly observed |
| Python / `.venv` / `ap exec` | `./.ap/ap exec` runtime-info, test-focus, and test with exact baseline `dd26782` | All three operations ran and passed after the commit-source mutations; no ambient `python` / `python3` / `.venv` invocation | directly observed |
| JavaScript tests | Canonical `node --test` because web assets changed | 195 passed across the identity, catalog-card, admin, X, and YouTube frontend suites listed below | directly observed |
| Network, NUC, SSH, sudo, secrets | None | Unused | directly observed |
| Browser / provider calls | None | Unused | directly observed |
| Independence | Not required | Same session implemented the candidate; no self-acceptance | directly observed |

Capability, permission, and client identity did not expand task authority.

Start commit: `dd267823490a19119575e697a4835bba94b02f7f`  
End commit: `95f514b2cf127824a09550f54dc5e9e4d8c2d0ad`  
Parent of end commit: `dd267823490a19119575e697a4835bba94b02f7f`  
Branch: `feat/x-meme-browser-companion`  
End worktree: clean  
Push: not authorized; not performed  

Do not treat `dd26782` or `95f514b` as live NUC.

## Changed files and purpose

Exactly twenty FrameNest repository paths in the one authorized commit:

- `src/framenest/adapters/api/public_published_application.py` — New separately composed ASGI app: read-only engine, schema-head `0032` fail-closed, no jobs/providers/derivative generation, GET/HEAD catch-all, no-store, no CORS, `docs_url=None`.
- `src/framenest/adapters/api/public_published_api.py` — Exact GET allowlist, redacted catalog/metadata, publication recheck on direct reads, Range content via private helpers imported from `media_content_api` (not `include_router` of the workspace content API).
- `src/framenest/adapters/api/application.py` — `public_published_uds` returns the public app immediately; workspace `GET /api/audience/me` for Tailscale vs trusted loopback.
- `src/framenest/server.py` — **Deviation:** UDS bind for `public_published_uds` as well as `tailscale_uds`; otherwise this mode would TCP-bind.
- `src/framenest/adapters/api/tailscale_ingress.py` — **Deviation:** one `GET /api/audience/me` route policy so workspace bootstrap is not fail-closed 404.
- `src/framenest/domain/identity_access.py` — Audience constants and `PUBLIC_PUBLISHED_CAPABILITIES` = `gallery.read` + `media.original.read` only.
- `src/framenest/configuration.py` — Ingress mode, default distinct socket `/run/framenest/framenest-public.sock`, reject workspace socket path.
- `src/framenest/infrastructure/persistence/engine.py` — SQLite URI `mode=ro` + `PRAGMA query_only=ON` with fail-closed writable probe.
- `src/framenest/infrastructure/persistence/media_metadata_repository.py` — Canonical tags represented by published media only.
- `src/framenest/adapters/api/web/app.js` — Bootstrap `/api/audience/me`; remove permissive capability fallback; public audience hides privileged chrome; skip health/AI/upload/YouTube on public.
- `src/framenest/adapters/api/web/styles.css` — Hide privileged controls until `data-audience` and for `public_published`.
- `tests/contract/test_public_published_uds.py` — Inventory, uniform 404, unpublished≡unknown, spoofed headers, redaction, GIF/image/video/movie + Range, unpublish, fail-closed startup, readonly engine, module grep, TCP audience.
- `tests/contract/test_tailscale_ingress_security.py` — `find_route_policy` includes `/api/audience/me`.
- `tests/unit/test_configuration_ingress.py` — Default/reject/explicit public socket.
- `tests/unit/test_identity_access.py` — Public capability set.
- `tests/unit/test_server_runtime.py` — Public mode binds only UDS.
- `tests/tailscale_identity_frontend.test.js` — Audience payload, missing bootstrap fail-closed, public audience case.
- `SPEC.md`, `SERVER.md`, `SECURITY.md` — Status sentences only: local-only reader implemented; still not public bind / TLS / Funnel / NUC.

Meta report (this file; not in the FrameNest commit):

- `/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/06_report_00.md`

No schema, ADR-body, systemd, Funnel, TLS, or NUC edits.

## Validation

- `./.ap/ap project check --root /home/agile/Projects/framenest --baseline dd267823490a19119575e697a4835bba94b02f7f` → PASS (`OK trusted baseline contract: dd267823490a19119575e697a4835bba94b02f7f:ap.project.conf`).
- `./.ap/ap exec --root /home/agile/Projects/framenest --baseline dd267823490a19119575e697a4835bba94b02f7f --operation runtime-info` → PASS. Provenance: `/home/agile/Projects/framenest/.venv/bin/python`, CPython 3.13.9, `framenest.__file__` = `/home/agile/Projects/framenest/src/framenest/__init__.py`. Also reported `WARN sanitized inherited environment classes: LD_LIBRARY_PATH SSH_AUTH_SOCK VIRTUAL_ENV_DISABLE_PROMPT PROMPT_COMMAND APPDIR APPIMAGE PATH`.
- `./.ap/ap exec ... --operation test-focus -- tests/contract/test_public_published_uds.py tests/unit/test_configuration_ingress.py tests/unit/test_identity_access.py tests/unit/test_server_runtime.py tests/contract/test_tailscale_ingress_security.py -q -p no:cacheprovider` → PASS; **184 passed** in 50.21s.
- `./.ap/ap exec ... --operation test` → PASS; **3238 passed, 8 skipped**, 3 warnings in 506.38s. Skips are the existing real-tool / live-NIM gates (`FRAMENEST_RUN_REAL_MEDIA_TOOLS`, `FRAMENEST_RUN_NVIDIA_NIM_SMOKE`).
- `node --test tests/tailscale_identity_frontend.test.js tests/catalog_card_ai_quick_action.test.js tests/admin_content_publication_frontend.test.js tests/admin_batch_actions_frontend.test.js tests/admin_catalog_removal_frontend.test.js tests/x_acquisition_cockpit.test.js tests/youtube_acquisition_cockpit.test.js tests/x_companion_extension.test.js` → PASS; **195 passed**.
- `git diff --check` / `git diff --cached --check`: clean before commit.
- Changed-file list of the commit: the twenty paths above only.
- `git log --oneline -8`:

```text
95f514b feat: local-only public_published_uds reader
dd26782 feat: administrator unpublish on the sole content-publication route
ffef457 fix: make administrator publication the sole content-publication write
6aac705 docs: accept ADR-0074 dual-audience boundary and align living documents
0008ca5 docs: propose dual-audience public and Tailscale workspace boundary
37da5f2 fix: list suggestion-ready media in companion outline history
0fe2b32 fix: include omitted-category X Saves in pending review history
a548714 fix: forest chrome and gentler companion history greens
```

- No ambient Python.
- No push.

Grep proof — public composition does not import workspace-only routers; the only `include_router` is the public GET router; no `@router.post` / `@router.put` / `@router.delete` / `@router.patch` in the public modules:

```text
src/framenest/adapters/api/public_published_application.py
    app.include_router(create_public_published_api_router(dependencies))
        docs_url=None,
        redoc_url=None,
        openapi_url=None,

src/framenest/adapters/api/public_published_api.py
    @router.get("/", response_class=HTMLResponse)
    @router.get("/assets/app.js")
    @router.get("/assets/styles.css")
    @router.get("/api/audience/me", response_model=PublicAudienceResponse)
    @router.get(   # /api/media
    @router.get(   # /api/media/{media_id}
    @router.get(   # /api/canonical-tags
    @router.get(   # /api/media/{media_id}/metadata
    @router.get("/api/media/{media_id}/locations/{location_id}/content", response_model=None)
    @router.get("/api/media/{media_id}/locations/{location_id}/gallery-preview", response_model=None)
    @router.get("/api/media/{media_id}/cover-thumbnail", response_model=None)
```

Ripgrep of those two files for `create_upload_api_router`, `create_companion_review_api_router`, `create_x_admin_api_router`, `create_youtube_operator_api_router`, `create_media_alias_api_router`, `create_library_api_router`, `create_content_publication_api_router`, `create_catalog_removal_api_router`, `@router.post`, `@router.put`, `@router.delete`, and `@router.patch` returned no matches.

`public_published_api.py` imports `_full_content_response` / Range helpers from `media_content_api` so published video/movie Range can reuse the existing streamer. That is not a workspace router mount (no download/upload/admin routes).

Workspace Tailscale policy addition:

```text
src/framenest/adapters/api/tailscale_ingress.py
    RoutePolicy(method="GET", template="/api/identity/me"),
    RoutePolicy(method="GET", template="/api/audience/me"),
    RoutePolicy(method="GET", template="/api/status/cloud"),
```

## Git result

One commit created on `feat/x-meme-browser-companion`. Local branch remains ahead of `origin/feat/x-meme-browser-companion` by the pre-existing unpublished stack plus this commit. No fetch, merge, rebase, reset, tag, or push.

## Deviations, risks, or missing evidence

Two necessary allowlist deviations, recorded rather than silently expanded:

1. `src/framenest/server.py` — public mode must set `uvicorn.Config(uds=...)`; without this the public process would TCP-bind.
2. `src/framenest/adapters/api/tailscale_ingress.py` — one GET policy line for `/api/audience/me` so the workspace app can serve the same bootstrap path the frontend now requires.

Frontend privileged admin/YouTube chrome remains Tailscale-gated (`identityState.available` is true only for `tailscale_workspace`). Trusted loopback still receives explicit admin capabilities from `GET /api/audience/me` so local upload/edit keep working after the permissive `identityHasCapability` fallback was removed. Public audience gets exactly `["gallery.read","media.original.read"]`. Missing/invalid bootstrap yields zero capabilities.

This slice is local-only. It is not public bind, TLS, Funnel, or NUC enablement.

Resolved Execution Issues / Near-Misses:

- FastAPI rejected `StreamingResponse | JSONResponse` as a response model; content/preview/thumbnail routes now set `response_model=None`.
- Starlette `MutableHeaders` has no `.pop`; CORS headers are deleted by membership + `del`.
- Pydantic `model_copy` in the after-validator did not persist the default public socket; assignment `self.uds_path = ...` does.
- Importing `sqlalchemy.engine.Engine` in the public ASGI module violated the persistence import boundary; the annotation is now untyped `object`.
- Live `app.routes` after middleware did not surface GET methods for inventory; the inventory test walks the dedicated public router (and the app) instead of assuming `APIRoute` on `client.app.routes`.
- Existing frontend tests required `identityState.resolved` / `available` on admin and YouTube gates; production gates were restored to that fail-closed shape, with `available` meaning Tailscale workspace only.
- The unpublish PUT used a local `headers` variable, so the mutation-header site count was 28/29; the fetch now uses `headers: framenestMutationHeaders(...)` inline.

Pre-Existing Failure Classification: none.

## Smallest next step

Independent verification of commit `95f514b`: `public_published_uds` starts only on a distinct UDS with a read-only catalog at schema `0032`; GET allowlist matches the inventory; unpublished/unknown/unlisted/mutated methods are uniform sanitized `404`; spoofed Tailscale headers do not widen access; published GIF/image/video/movie Range works; frontend bootstrap from `/api/audience/me` fail-closes without the old loopback capability fallback. Successor ADR-0074 rollouts (TLS/Funnel/NUC public bind, workspace capability expansion) remain unauthorized.

Report justification: new-mutation

Authority expiry: this implementation authority expires with submission of this terminal report. No further commits, revisions, runtime work, publication, deployment, push, or logical-whole closure are authorized.
