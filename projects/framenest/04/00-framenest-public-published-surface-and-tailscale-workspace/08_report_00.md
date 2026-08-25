### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 03
Worker exchange ordinal: 03
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
| Approval/permissions | Durable analysis proposals; commits on the feature branch; no push | Filesystem technically unrestricted; authority limited to the allowlisted repository paths plus this report | directly observed |
| Repository | Canonical checkout and exact baseline | `/home/agile/Projects/framenest`; branch `feat/x-meme-browser-companion`; start HEAD `5b9957542abfdfe6f418042a2a6628686ba35d8c`; AP pin `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | directly observed |
| Continuity | Session 03 exchange 03; exchange 02 expired at `5b99575` | Same Worker session; exchange 02 authority not reused; baseline matched and worktree clean before writes | directly observed |
| AP pin | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | Superproject gitlink and `.ap` HEAD match | directly observed |
| Schema head | `0033` after exactly one additive migration | Alembic head, catalog_schema, public required revision, SPEC, and allowlisted tests declare `0033` | directly observed |
| Git containment | Coherent commit(s) on the feature branch; no push | One commit `da06109bd4adab6f00eea2db02dc2787c98da10c`; push not performed | directly observed |
| Python / `.venv` / `ap exec` | `./.ap/ap exec` runtime-info, test-focus, and test with exact baseline `5b99575` | All three operations ran and passed; no ambient `python` / `python3` / `.venv` invocation | directly observed |
| JavaScript tests | Canonical `node --test` because web assets changed | 201 passed across the identity, workspace, catalog-card, admin, X, and YouTube frontend suites listed below | directly observed |
| Network, NUC, SSH, sudo, secrets | None | Unused | directly observed |
| Browser / provider calls | None | Unused | directly observed |
| Independence | Not required | Same session implemented the candidate; no self-acceptance | directly observed |

Capability, permission, and client identity did not expand task authority.

Start commit: `5b9957542abfdfe6f418042a2a6628686ba35d8c`  
End commit: `da06109bd4adab6f00eea2db02dc2787c98da10c`  
Parent of end commit: `5b9957542abfdfe6f418042a2a6628686ba35d8c`  
Branch: `feat/x-meme-browser-companion`  
End worktree: clean  
Push: not authorized; not performed  

Do not treat `5b99575` or `da06109` as live NUC.

## Changed files and purpose

Exactly forty-one FrameNest repository paths in the one authorized commit:

- `src/framenest/domain/identity_access.py` — `analysis.propose` on the ordinary capability set (user and admin). No other capability table edits.
- `src/framenest/application/ports/analysis_proposal.py` — Proposal row, admin page types, and repository port. No provider or enqueue types.
- `src/framenest/application/analysis_proposal.py` — `ProposeAnalysis` and `ListAnalysisProposals`. Duplicate POSTs each create a new row. Invalid media identity is treated as not-found.
- `src/framenest/infrastructure/persistence/catalog_schema.py` — Additive `media_analysis_proposals` table.
- `src/framenest/infrastructure/persistence/alembic_environment/versions/0033_media_analysis_proposals.py` — Exactly one additive revision `0033` down from `0032`.
- `src/framenest/infrastructure/persistence/analysis_proposal_repository.py` — Insert plus newest-first open-proposal list with live title, publication, and readiness join. No analysis-run writes.
- `src/framenest/adapters/api/analysis_proposal_api.py` — `POST /api/workspace/media/{media_id}/analysis-proposals` (`analysis.propose`, audit required) and `GET /api/admin/analysis-proposals` (`media.workflow.read`).
- `src/framenest/adapters/api/application.py` — Wires the proposal repository and mounts the router on the trusted app only.
- `src/framenest/adapters/api/tailscale_ingress.py` — Route policies for the two new routes, with audit on both.
- `src/framenest/adapters/api/public_published_application.py` — Required public schema revision `0033`.
- `src/framenest/adapters/api/web/app.js` — Propose-analysis control on workspace items; administrator open-proposals browser.
- `src/framenest/adapters/api/web/index.html` — Analysis-proposals chrome only.
- `src/framenest/adapters/api/web/styles.css` — Public audience never reveals the new chrome.
- `SPEC.md` — `implemented-for-backend` markers for `analysis.propose`, the two routes, and schema head `0033`. Successor `metadata.alias.team.read` left unmarked.
- Tests listed below.

Meta report (this file; not in the FrameNest commit):

- `/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/08_report_00.md`

No ADR-body, systemd, Funnel, TLS, or NUC edits. No enqueue, provider, NIM, scheduler, or `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED` changes. No dismiss/complete lifecycle endpoints.

## Migration summary

Revision `0033` creates `media_analysis_proposals` with:

- opaque `id` (UUIDv4 text)
- `media_id` FK to `logical_media.id` ON DELETE CASCADE
- `proposed_by_login_key`
- `created_at_ms`
- `status` CHECK IN (`open`, `dismissed`, `completed`), written only as `open`

No existing tables or columns are altered. A second `alembic upgrade 0033` on an already-at-head catalog is a no-op. Populated `0032` catalogs keep existing rows. Proposer display login on the admin list is the stored login key (the identity mapping has no catalog table). Title, publication, and readiness on the admin list are live joins, not frozen write-time snapshots.

Choice: proposing twice is allowed; each POST inserts its own row.

## Validation

- `./.ap/ap project check --root /home/agile/Projects/framenest --baseline 5b9957542abfdfe6f418042a2a6628686ba35d8c` → PASS (`OK trusted baseline contract: 5b9957542abfdfe6f418042a2a6628686ba35d8c:ap.project.conf`).
- `./.ap/ap exec --root /home/agile/Projects/framenest --baseline 5b9957542abfdfe6f418042a2a6628686ba35d8c --operation runtime-info` → PASS. Provenance: `/home/agile/Projects/framenest/.venv/bin/python`, CPython 3.13.9, `framenest.__file__` = `/home/agile/Projects/framenest/src/framenest/__init__.py`. Also reported `WARN sanitized inherited environment classes: LD_LIBRARY_PATH SSH_AUTH_SOCK VIRTUAL_ENV_DISABLE_PROMPT PROMPT_COMMAND APPDIR APPIMAGE PATH`.
- `./.ap/ap exec ... --operation test-focus -- tests/contract/test_analysis_proposal.py tests/unit/application/test_propose_analysis.py tests/unit/test_identity_access.py tests/integration/persistence/test_analysis_proposal_migration.py tests/contract/test_public_published_uds.py tests/contract/test_tailscale_ingress_security.py tests/contract/test_adr_0073.py tests/contract/test_workspace_media.py tests/integration/test_persistence_migrations.py tests/unit/infrastructure/runtime/test_production_runtime.py tests/unit/infrastructure/backup/test_catalog_backup.py tests/contract/test_persistence_cli.py tests/integration/persistence/test_companion_review_migration.py -q -p no:cacheprovider` → PASS; **219 passed** in 82.59s.
- `./.ap/ap exec ... --operation test` → PASS; **3260 passed, 8 skipped**, 3 warnings in 515.98s. Skips are the existing real-tool / live-NIM gates (`FRAMENEST_RUN_REAL_MEDIA_TOOLS`, `FRAMENEST_RUN_NVIDIA_NIM_SMOKE`). Prior exchange 02 full suite was 3244 passed / 8 skipped; the +16 are this slice’s new Python tests (10 contract + 2 unit + 4 migration). No pre-existing failures to classify.
- `node --test tests/tailscale_identity_frontend.test.js tests/workspace_media_frontend.test.js tests/catalog_card_ai_quick_action.test.js tests/admin_content_publication_frontend.test.js tests/admin_batch_actions_frontend.test.js tests/admin_catalog_removal_frontend.test.js tests/x_acquisition_cockpit.test.js tests/youtube_acquisition_cockpit.test.js tests/x_companion_extension.test.js` → PASS; **201 passed**.
- `git diff --check` / `git diff --cached --check`: clean before commit.
- Changed-file list of the commit: the forty-one paths above only.
- `git log --oneline -8`:

```text
da06109 feat: durable ordinary-user analysis proposals
5b99575 feat: contributor-scoped workspace media and administrator contribution filter
95f514b feat: local-only public_published_uds reader
dd26782 feat: administrator unpublish on the sole content-publication route
ffef457 fix: make administrator publication the sole content-publication write
6aac705 docs: accept ADR-0074 dual-audience boundary and align living documents
0008ca5 docs: propose dual-audience public and Tailscale workspace boundary
37da5f2 fix: list suggestion-ready media in companion outline history
```

- No ambient Python.
- No push.

Grep proof — proposal modules import no provider, NIM, enqueue, coordinator, or automatic-analysis modules. Import lines of `analysis_proposal.py`, `ports/analysis_proposal.py`, `analysis_proposal_repository.py`, `analysis_proposal_api.py`, and `0033_media_analysis_proposals.py` contain none of `nvidia`, `nim`, `media_analysis_coordinator`, `media_analysis_lifecycle`, `resolve_ai_provider`, `ai_provider`, `LocalMediaAnalysisAdapter`, `RequestManualMediaAnalysis`, `ScheduleAutomaticMediaAnalysis`, `infrastructure.ai`, or `infrastructure.media_analysis`. The repository source mentions `media_analysis_proposals` and does not mention `media_analysis_runs` or `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS`. Behavioral proof: after a successful propose, `media_analysis_runs` stays at count 0 and one proposal row exists.

Grep proof — public composition remains free of the two new routes. The only `include_router` is the public GET router; no `@router.post` / `@router.put` / `@router.delete` / `@router.patch`:

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

Ripgrep of those two files for `create_analysis_proposal_api_router`, `analysis-proposals`, `/api/workspace`, `@router.post`, `@router.put`, `@router.delete`, and `@router.patch` returned no matches. Public uniform-404 inventory now includes both new paths.

Trusted ingress policy additions:

```text
src/framenest/adapters/api/tailscale_ingress.py
    RoutePolicy(
        method="POST",
        template="/api/workspace/media/{media_id}/analysis-proposals",
        capability=CAPABILITY_ANALYSIS_PROPOSE,
        audit_action="analysis.propose",
        audit_target_type="media",
        audit_target_group="media_id",
    ),
    RoutePolicy(
        method="GET",
        template="/api/admin/analysis-proposals",
        capability=CAPABILITY_MEDIA_WORKFLOW_READ,
        audit_action="analysis.proposals.list",
        audit_target_type="analysis_proposal",
    ),
```

Ordinary identity payload includes `analysis.propose`. Trusted-ingress POST records an `allowed` audit event with HTTP 201.

## Git result

One commit created on `feat/x-meme-browser-companion`. Local branch remains ahead of `origin/feat/x-meme-browser-companion` by the pre-existing unpublished stack plus this commit. No fetch, merge, rebase, reset, tag, or push.

## Deviations, risks, or missing evidence

No allowlist expansion. `index.html` is inside `src/framenest/adapters/api/**`. Living-document schema-head prose outside the allowlist is unchanged: `README.md`, `PRODUCT.md`, and `ROADMAP.md` still say schema head / revision `0032`. `SPEC.md` and allowlisted tests declare `0033`. `tests/contract/test_adr_0073.py` now asserts SPEC `0033` and keeps the README/PRODUCT/ROADMAP `0032` strings as those files were not authorized to change.

Frontend proposal chrome is Tailscale-gated plus login plus `analysis.propose` (workspace control) or `media.workflow.read` (administrator list). Public audience CSS and capability set never reveal it. UI hiding is not authorization: the public composition has no proposal router, and trusted ingress denies the capabilities without them.

Administrator list is gated by existing `media.workflow.read`, not `analysis.run`. Status CHECK permits `dismissed`/`completed` for later lifecycle work; this grant writes only `open` and has no write/lifecycle endpoints.

Resolved Execution Issues / Near-Misses:

- Pytest collection failed while both `tests/contract/test_analysis_proposal.py` and `tests/unit/application/test_analysis_proposal.py` shared a basename; the unit file was renamed to `test_propose_analysis.py`.
- A whole-file grep for `nim` matched `minimum`, and `enqueue` matched a “never enqueue” docstring. The proof inspects import lines only.
- The identity frontend mutation-site count increased from 29 to 30 with the new POST.
- `test_upgrade_from_0007_preserves_existing_catalog_rows_and_adds_empty_upload_sessions` required `media_analysis_proposals` in its expected table union after the head bump.

Pre-Existing Failure Classification: none.

## Smallest next step

Independent verification of commit `da06109`: mapped PRO users with `analysis.propose` can POST a durable administrator-visible proposal for existing media without provider or enqueue side effects; unknown media stays sanitized 404; duplicate POSTs create distinct rows; administrators with `media.workflow.read` list open proposals newest first; ordinary users cannot list; `public_published_uds` still 404s both new routes. Successor ADR-0074 rollouts (`metadata.alias.team.read`, public bind/TLS/Funnel/NUC) remain unauthorized. Dismiss/complete of proposals remains later work.

Report justification: new-mutation

Authority expiry: this implementation authority expires with submission of this terminal report. No further commits, revisions, runtime work, publication, deployment, push, or logical-whole closure are authorized.
