# FrameNest × X Meme Browser Companion MVP — Repository-Grounded Architecture Plan

## 0. Authoritative routing record

```text
Role: WORKER
Logical whole identity: framenest-x-meme-browser-companion-mvp
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: repository-grounded browser-companion architecture planner
Phase: planning
Task identity: FN-X-MEME-COMPANION-PLAN-01
Task type: bounded read-only implementation planning
Native planning mode: required
Reasoning recommendation: high
Evidence posture: non-independent
Authority renewal: plan approval does not grant implementation authority; implementation requires a new explicit prompt
```

Planning contract:

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: one repository-grounded MVP architecture and implementation plan for the selected logical whole
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1
```

The same-session route is preferred only if the session remains healthy and no
independence trigger appears. It still requires a new complete implementation
prompt; otherwise ORCHESTRATOR must explicitly route a fresh session.

### Cooperator delivery and trace destination

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_planning_00.md
Destination path: projects/framenest/03/03-framenest-x-meme-browser-companion-mvp/01_planning_00.md
Archival: allow-now
```

```text
External trace disposition: configured
Trace discovery: cisarik/meta repository path projects/framenest/03/03-framenest-x-meme-browser-companion-mvp
Trace project key: framenest
Trace logical-whole projection identity: 03/03-framenest-x-meme-browser-companion-mvp
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
```

Expected terminal report destination:
`projects/framenest/03/03-framenest-x-meme-browser-companion-mvp/01_report_00.md`.
The Worker has no Meta read or write authority.

## 1. Mission

Produce one expert, implementation-ready architecture plan for a tailnet-only Brave/Chromium browser companion that integrates FrameNest with X for two explicit, user-initiated journeys:

1. **Save from X:** while viewing an X post, the user deliberately asks FrameNest to acquire the post's eligible meme media through the existing authenticated X request lifecycle.
2. **Use in the X composer:** while an X composer is active, the user deliberately opens a FrameNest picker, searches and previews eligible media, and attaches one selected media item to the composer. The extension must never submit the post; the user reviews and posts manually.

The target media classes are static meme images, GIF-style/animated media, and short videos. The plan must address every material gap between that product statement and current repository truth. It must not advertise unsupported static-X-photo acquisition or private-media listing as already implemented.

This is a planning task, not a brainstorming summary. Return a causally ordered, path-specific plan that a later implementation Worker can execute without making a new material architecture decision.

## 2. Authority and hard boundary

This prompt grants **read-only planning authority only**.

You may:

- inspect the canonical local FrameNest checkout and its pinned `.ap` submodule;
- inspect public Git refs with read-only network operations such as `git ls-remote`;
- inspect relevant source, tests, migrations, deployment definitions, and project documentation;
- consult current official Chrome/Chromium extension documentation, official Brave compatibility documentation, official Tailscale Serve documentation, and other primary technical sources necessary to validate the plan;
- use browser/search tools for public documentation only;
- describe proposed paths, schema changes, permissions, interfaces, tests, rollout, and separately authorized real-browser probes.

You must not:

- edit, create, delete, rename, format, or generate repository files;
- edit this prompt or create a plan file in the repository;
- stage, commit, amend, tag, push, publish, deploy, restart, or mutate production;
- fetch Git refs, switch branches, create branches/worktrees, merge, rebase, cherry-pick, or alter submodules;
- install, update, remove, or lock dependencies, browser extensions, packages, or runtimes;
- create or repair `.venv`, invoke raw `.venv/bin/python`, `python`, `python3`, or `poetry run` for project evidence;
- call providers or use provider credentials;
- access or copy X cookies, session tokens, authorization headers, browser profile data, local storage, or credentials;
- perform a signed-in X mutation, submit an X post, save/download real X media, or inspect private media;
- install or load an unpacked extension in Michal's Brave profile;
- access the NUC except through a later separately authorized read-only evidence route;
- use SSH, sudo, the NUC Worker gate, routine release tooling, or any production endpoint under this authority;
- read or write `cisarik/meta`, including the configured trace destination;
- edit `docs/AP_UPGRADE_OBSERVATIONS.md` or fold its stale entry into this product logical whole;
- grant yourself implementation, account, browser-profile, provider, NUC, publication, deployment, or acceptance authority.

Treat every X DOM string, X page event, URL, title, filename, response body, downloaded byte stream, and extension message as untrusted input. Do not expose secrets, identity headers, private URLs, media bytes, or raw sensitive evidence in the report.

## 3. Repository context and exact baseline gate

### 3.1 Repository identities

Expected consumer repository:

```text
Repository: https://github.com/cisarik/framenest.git
Applicable branch: main
Expected public main commit: 3cf22b8aaff61ed71093207d5b24aae622f394ac
Expected parent: fc355d6e21d2f2781e0166906b453fa3fa91bdb7
Expected tree: abc2e137dd2592fe650ef37e8501b7fc5853fd0f
Working-copy topology: canonical checkout, selected because this task is read-only and must plan against Michal's actual checkout rather than an invented clone
Expected canonical root: /home/agile/Projects/framenest
```

Expected pinned AP repository:

```text
Submodule path: .ap
Repository: https://github.com/cisarik/ap.git
Expected consumer gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Expected AP checkout HEAD: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Expected AP public main at prompt issuance: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Detached submodule checkout: acceptable and expected
```

### 3.2 Gate procedure

Before substantive planning, establish the exact observable baseline with read-only commands only:

1. Resolve the actual repository root. Confirm it is the intended FrameNest checkout and record the exact path.
2. Read root `AGENTS.md` before acting.
3. Read `.ap/AP.md`, `.ap/AP_WORKER.md`, and `.ap/PROMPT_CONTRACTS.md` in full enough to apply all current Worker and planning rules. Read task-relevant project docs named below.
4. Record consumer `HEAD`, branch/detached state, concise status including untracked files, configured origin, and submodule gitlink/status.
5. Compare local consumer `HEAD` with the expected public `main` using direct read-only public evidence. Do not use `git fetch`.
6. Compare the `.ap` checkout with the consumer gitlink and expected AP public ref.
7. Confirm no active mutation owned by this Worker exists.

Classify all five states separately:

- local consumer checkout;
- local AP checkout;
- consumer public ref;
- AP public ref;
- deployed/production state.

Production truth is not directly authorized for this plan; classify it as `not re-probed under current authority`, and preserve the issuance-time historical anchor below without upgrading it to current direct evidence.

If the local checkout is missing, dirty, on an unexpected commit, has an unexpected submodule gitlink, contains unresolved changes, or contradicts the public refs, do not repair or continue as if synchronized. Report the exact discrepancy, classify whether planning can safely remain partial, and stop with `PARTIAL` or `BLOCKED` when the discrepancy could change the plan. Do not infer mutation authority from a clean checkout or expected `HEAD`.

### 3.3 Canonical execution and capability routes

The consumer-declared Cursor/AppImage Python route is:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 3cf22b8aaff61ed71093207d5b24aae622f394ac
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 3cf22b8aaff61ed71093207d5b24aae622f394ac --operation <declared-operation> [-- <trailing argv>]
```

The root `ap.project.conf` and `docs/WORKER_EXECUTION_CONTRACT.md` govern allowed operations. Do not replace this route with ambient Python, copied interpreter paths, or `poetry run`. This plan should normally require no Python or test execution. If a narrow declared read-only check becomes indispensable, use only the exact AP route and explain why it was necessary. Do not use candidate mode as authority.

The project-owned NUC capability route is `scripts/operator/network/framenest_nuc_worker_gate.fish`, but it is named here only to close the route-resolution question. It is **not activated** for this task.

## 4. Mandatory repository reading and evidence map

At minimum, inspect these current owners and follow directly relevant imports, tests, configuration, and wiring:

- `AGENTS.md`
- `.ap/AP.md`
- `.ap/AP_WORKER.md`
- `.ap/PROMPT_CONTRACTS.md`
- `docs/WORKER_EXECUTION_CONTRACT.md`
- `docs/adr/0048-tailscale-remote-access-and-identity-foundation.md`
- `docs/adr/0049-durable-content-publication-boundary.md`
- `docs/adr/0055-youtube-creator-taxonomy-and-immutable-provenance.md`
- `docs/AP_UPGRADE_OBSERVATIONS.md` only to classify the known stale observation; do not edit or absorb it
- `src/framenest/adapters/api/tailscale_ingress.py`
- `src/framenest/domain/identity_access.py`
- `src/framenest/adapters/api/x_request_api.py`
- `src/framenest/adapters/api/x_admin_api.py`
- `src/framenest/application/x_acquisition.py`
- `src/framenest/domain/x_acquisition.py`
- `src/framenest/infrastructure/x/downloader.py`
- `src/framenest/infrastructure/x/staging.py`
- `src/framenest/infrastructure/persistence/x_acquisition_claim_repository.py`
- `src/framenest/adapters/api/media_catalog_api.py`
- `src/framenest/application/media_catalog.py`
- `src/framenest/infrastructure/persistence/media_catalog_repository.py`
- `src/framenest/adapters/api/content_audience_api.py`
- `src/framenest/application/content_publication.py`
- `src/framenest/adapters/api/media_content_api.py`
- `src/framenest/application/media_content.py`
- `src/framenest/application/ports/media_content.py`
- `src/framenest/domain/media.py`
- `src/framenest/domain/media_classification.py`
- `src/framenest/infrastructure/persistence/alembic_environment/versions/0028_x_requester_acquisition.py`
- current application construction/configuration that wires external origin, Tailscale ingress, identity mapping, X acquisition, catalog, and content routes
- relevant operator/deployment definitions needed to plan configuration, packaging, release, and rollback without operating them
- relevant X, media-catalog, audience, content-delivery, Tailscale-ingress, frontend, and migration tests

Do not merely list files. Build an evidence-to-owner map showing which exact current owner proves each material statement and which proposed owner would change.

## 5. Issuance-time verified anchors to revalidate

Treat the following as high-value starting evidence, not as substitutes for your own read-only verification:

1. FrameNest public `main` was `3cf22b8aaff61ed71093207d5b24aae622f394ac` when this prompt was issued.
2. The consumer pins AP `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.
3. The repeatable immutable NUC release/deployment contract was previously closed with production/public artifact `5abb2ad...`, schema `0028`, and healthy production evidence. This is historical context only; do not claim current production acceptance.
4. The X requester lifecycle currently exposes:
   - `POST /api/x/requests`
   - `GET /api/x/requests`
   - `GET /api/x/requests/{claim_id}`
   - `POST /api/x/requests/{claim_id}/retry`
   - `GET /api/admin/x/requests/{claim_id}`
5. Ordinary identities require `x.request`. Administrator identities also have `x.acquire`; confirm the exact current capability map and whether administrator submission intentionally uses the ordinary route under the administrator's own identity.
6. Current X acquisition validates X/Twitter status URLs with numeric post IDs, preserves requester ownership, implements active reuse/duplicate handling and bounded rate/admission limits, supports at most four assets, tracks per-asset lifecycle and partial success, and supports bounded retry.
7. X-acquired media uses `AcquisitionSource.X_MANUAL_CLAIM`, default content category `meme`, and `x_author` attribution.
8. The production yt-dlp X adapter currently supports native video and animated-GIF-like media represented as MP4. Static X photos are filtered by the pinned extractor and explicitly deferred even though forward-compatible image domain types exist.
9. `GET /api/media` currently uses a published-only catalog query. It supports search over title and filters including AND tag keys, content category, acquisition source, and creator dimensions. It cannot currently list requester-private media.
10. `ContentAudiencePolicy` permits administrator access, published access, and the requester's own live YouTube/X media for item/content/download routes. Therefore direct requester-private access exists, but a private picker/list query does not.
11. Content delivery supports MP4, GIF, JPG/JPEG, and PNG when audience and availability checks pass.
12. No single canonical server-side predicate currently defines “eligible X meme for the companion picker.” The plan must define one authoritative predicate and its owner.
13. Tailscale Serve ingress injects trusted identity only through the configured production ingress path, maps identity to capabilities, and applies route policy centrally.
14. Unsafe remote methods currently require both `X-FrameNest-Request: 1` and an `Origin` exactly equal to the configured FrameNest external HTTPS origin. A request originating from `chrome-extension://<id>` or X cannot be assumed to satisfy this check; the current likely failure is `MUTATION_ORIGIN_FORBIDDEN`.
15. The repository contains no accepted browser-extension implementation for this whole. X composer DOM and attachment behavior remain volatile and require an explicit adapter boundary plus later real-browser evidence.
16. `docs/AP_UPGRADE_OBSERVATIONS.md` contains a stale `untriaged` consumer-declared route-binding observation even though current AP and FrameNest public truth substantively implemented that concern. This is a separate governance reconciliation; note it without repairing it or treating it as product scope.

Every anchor in the final plan must be labelled as one of: directly verified repository fact, directly verified public fact, historical context, inference, proposal, unresolved question, or separately authorized acceptance requirement.

## 6. Accepted product and security decisions

Preserve these decisions unless current repository truth makes one impossible, in which case report the conflict rather than silently changing scope.

### 6.1 Product boundary

- One Brave/Chromium extension companion for FrameNest and X.
- Explicit user gestures only.
- Save the current X post's eligible media into the existing FrameNest X request lifecycle.
- Open a FrameNest picker while an X composer is active.
- Search, filter, preview, select, and attach one eligible media item.
- Never submit or schedule the X post.
- The user remains responsible for final composer content and posting.
- Target static images, GIF-style/animated media, and short videos.
- Reuse current FrameNest identities, capabilities, publication boundary, X requester ownership, catalog, and content delivery where valid.
- Support an administrator and at least two ordinary tailnet identities in acceptance planning.

### 6.2 Excluded scope

- YouTube acquisition or YouTube-specific browser actions.
- Movie/long-form media workflows.
- Other users' private or unpublished media.
- Arbitrary URL or arbitrary-file ingestion.
- Public Internet bridge, hosted SaaS proxy, or bypass of the tailnet boundary.
- Copying X authentication state or browser-profile secrets.
- X API/provider credentials unless a future separately selected architecture explicitly requires and authorizes them; do not assume them.
- Background crawling, feed scraping, bulk download, engagement automation, likes, follows, reposts, replies, or automatic submission.
- `<all_urls>` or broad host access without proven necessity.
- A generic authenticated proxy in FrameNest or the extension.
- Telemetry, analytics, advertising, or remote logging from the extension.
- Broad FrameNest UI redesign, unrelated catalog work, unrelated X cockpit redesign, or unrelated AP/ledger repair.

### 6.3 Security invariants

- Tailnet-only FrameNest origin and Tailscale Serve identity remain authoritative.
- Server-side identity and capability checks remain mandatory; extension state is never identity proof.
- Existing requester ownership and publication/audience boundaries must not weaken.
- No X cookies, X tokens, Tailscale identity headers, FrameNest secrets, browser profile data, or private account data may be copied into extension storage or messages.
- The extension stores only the smallest non-secret configuration/state necessary, with explicit lifecycle and clearing behavior.
- Permissions must be least privilege: narrow X match patterns and exact FrameNest origin patterns; justify every permission.
- Mutation trust must distinguish the approved extension origin from arbitrary web pages without trusting a caller-set secret header alone.
- Browser-enforced headers may be evidence only when the plan proves who can and cannot set them.
- Extension identifiers and development/production packaging must be stable enough for a server allowlist if the chosen design depends on origin allowlisting.
- The plan must preserve CSRF protection for ordinary FrameNest web UI mutations while enabling the extension's exact bounded mutation.
- FrameNest must never become an arbitrary cross-origin fetch proxy.
- Media queries and content retrieval must be server-authorized and bounded; untrusted filenames and response metadata must be sanitized.
- No sensitive URL, title, media byte content, user identity, X text, or stack trace in normal logs.
- No automatic post submission, even after a successful attachment.

## 7. Required architecture questions

Answer each question decisively. When direct evidence is unavailable, identify the smallest feasibility spike or Cooperator-owned acceptance probe rather than using “figure out later.”

### 7.1 Extension shape and lifecycle

- Select the exact Manifest V3 architecture: service worker, content-script adapter, UI surface, optional extension page/side panel, and message boundaries.
- Compare at least side panel, popup, and in-page overlay for the picker. Select one and reject the others with repository/product/security reasons.
- Define how Save is surfaced for an individual X post and how the active post URL is derived without scraping unrelated feed content.
- Define how composer presence and lifecycle are detected across X single-page navigation, multiple composers, modal/inline variants, rerenders, and teardown.
- Define one versioned X adapter seam with fixture-driven selectors/signals and fail-closed behavior when X changes.
- Define accessible loading, success, retry, empty, permission-denied, unavailable, and stale-adapter states.

### 7.2 Permission, origin, identity, and CSRF model

- Produce the proposed manifest permission set and exact host/match patterns.
- State which component performs cross-origin FrameNest fetches and why content scripts may or may not do so under current Chromium rules.
- Prove how Tailscale Serve identity reaches FrameNest for extension-origin requests without copying credentials.
- Resolve the unsafe-method origin conflict. Specify exact server configuration, allowed origin form, stable extension-ID/package implications, headers, route scope, validation order, and tests.
- Explain how the design prevents an arbitrary X page script, malicious extension, or arbitrary web origin from invoking the mutation path.
- Preserve the current FrameNest web UI mutation contract.
- Define CORS behavior only if required; do not add permissive CORS by default.
- Define behavior when the user is off-tailnet, the FrameNest hostname is unreachable, identity is unmapped, or capability is denied.

### 7.3 Save flow

- Give separate administrator and ordinary-user sequence diagrams in prose or compact Mermaid-ready steps in the report.
- Specify the exact current endpoint reused or the smallest new endpoint required.
- Define request idempotency/reuse messaging, queue/rate-limit messaging, partial success, retry, and unsupported-media behavior.
- Address multi-asset posts explicitly.
- Resolve static X photo acquisition. The plan must either provide a concrete conforming extractor/ingestion design and dependency decision or classify it as a named MVP-blocking spike. Domain enum presence is not implementation evidence.
- Define when an acquired item becomes picker-eligible for its requester and when it becomes eligible for others.

### 7.4 Picker eligibility, search, preview, and content

- Define a single canonical server-side predicate for “eligible companion meme.” Include media kind, content category, acquisition source, lifecycle success, audience, publication, location availability, file/content support, and any short-video constraint.
- Decide whether eligibility belongs in the application layer, repository query specification, API adapter, or a composed policy; reject duplicating it in the extension.
- Resolve the current published-only list gap for requester-private X media. Prefer the smallest purpose-specific authenticated query contract that cannot enumerate another user's private media.
- Define exact query parameters, pagination, response projection, cache headers, empty states, and stable sorting.
- Define how the current requester's newly saved media appears without broadening the public gallery contract accidentally.
- Define preview behavior for images, GIF-style media, and video without unbounded transfer or bypassing audience checks.
- Identify exact content/download routes reused or minimally added and how filenames/MIME/size are validated.

### 7.5 Composer attachment mechanism

- Compare plausible mechanisms using current primary evidence and browser constraints: direct `File`/`DataTransfer` assignment to an eligible file input, explicit user download followed by attach, clipboard, drag/drop, a bounded extension-page transfer bridge, and Native Messaging only as a last-resort alternative.
- Select a primary mechanism and one bounded fallback.
- Do not assume that runtime messaging can transfer large binary objects; verify Chrome's serialization/transfer constraints.
- Do not assume that assigning a synthetic `File` triggers X's framework state correctly; define a separately authorized real-source spike with observable success/failure criteria.
- Bound media size, memory use, timeouts, cancellation, and cleanup. Avoid base64 for unbounded media.
- State what the X page can observe and why the data exposure is or is not acceptable for the explicit attachment action.
- Ensure the extension attaches only to the user-selected active composer and never clicks Post.
- Define recovery when the composer disappears, the input is replaced, the media type is rejected, upload fails, or X changes its DOM.

### 7.6 Minimal backend and deployment surface

- Identify the smallest backend/API/configuration changes required for extension origin trust, picker eligibility/listing, private requester items, and any content transfer needs.
- Prefer extension-specific bounded contracts over generic proxy or broad catalog changes.
- Specify exact proposed file paths and ownership boundaries.
- Identify whether schema migration `0029` or later is required. If no migration is needed, prove why. If one is needed, define columns/indexes/backfill/downgrade and privacy implications.
- Identify configuration keys and deployment/env-example changes without disclosing real values.
- Explain extension packaging, stable identifier/key strategy, developer loading, versioning, update method, NUC release inclusion or separate artifact handling, rollback, and recovery.
- Preserve the immutable release/deploy contract; do not make deployment part of implementation authority implicitly.

## 8. Primary-source research requirements

Use current primary sources for browser and tailnet claims. At minimum, revalidate the relevant portions of:

- Chrome extension cross-origin requests: `https://developer.chrome.com/docs/extensions/develop/concepts/network-requests`
- Chrome permission declarations: `https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions`
- Chrome content scripts: `https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts`
- Chrome side panel API: `https://developer.chrome.com/docs/extensions/reference/api/sidePanel`
- Chrome runtime messaging/serialization documentation relevant to binary transfer
- Chrome extension service-worker lifecycle and storage documentation relevant to the selected architecture
- Brave Chromium-extension compatibility: `https://support.brave.com/hc/en-us/articles/360055359111-Switch-to-Brave-from-Firefox`
- Tailscale Serve identity headers: `https://tailscale.com/docs/features/tailscale-serve#identity-headers`

Use X's official/publicly served application behavior only where observable without a signed-in account, and label it volatile. Do not rely on third-party blogs for material browser security or API claims. Do not treat Web Store packaging as required unless the selected MVP route needs it.

No signed-in X/Brave inspection is authorized now. If the architecture cannot be selected without one, define the smallest exact read-only or reversible probe, the account/profile surface, data touched, expected evidence, cleanup, and stop conditions. Mark it `requires separate Michal authorization`.

## 9. Planning method

Use Native Plan Mode for exactly one bounded planning cycle:

1. Gate the repository/AP baseline.
2. Build the current capability, route, audience, catalog, media, and ingress map.
3. Identify contradictions between product objective and current implementation.
4. Form explicit architecture candidates.
5. Compare them against least privilege, tailnet identity continuity, attachment feasibility, change size, testability, rollout, and recovery.
6. Select one architecture and record rejected alternatives.
7. Resolve every material decision down to exact owner/path/interface or to a smallest separately authorized spike.
8. Design a causal implementation sequence where each slice has an observable gate and does not depend on an unproven later assumption.
9. Design repository verification, synthetic browser fixtures, and real Brave/Michal acceptance as separate evidence tiers.
10. Return the terminal report and stop. Do not begin implementation even if the plan is complete.

Repeated-gate or reasoning-loop stop:

```text
Repeated-gate or reasoning-loop stop: configured
Broad gate: once for the verified baseline
Narrow before re-broad: required
Unchanged hypothesis, candidate, and failing gate: not-progress
Escalate only on: named missing evidence that materially prevents architecture selection
Downgrade after: architecture convergence or named risk removal
Second automatic planning revision: forbidden
```

One accountable Worker owns the result. Do not delegate or spawn parallel workers. Internal delegation is not authorized by this prompt.

## 10. Required terminal deliverable

Return one professional English report beginning **exactly** with:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Immediately after the heading, echo these coordinates exactly once:
the logical-whole identity, Worker-session ordinal, and Worker-exchange ordinal
from the authoritative routing record above. Preserve their exact field names
and values; do not duplicate them elsewhere in the report.

Then include all of the following numbered sections. Do not omit a section; use `not applicable` only with a concrete reason.

1. **Terminal status and authority expiry** — `PASS`, `PARTIAL`, or `BLOCKED`; confirm no implementation/mutation occurred and planning authority has expired.
2. **Exact baseline and evidence ledger** — local/public consumer and AP identities, status, topology, production classification, directly verified sources, and any limitations.
3. **Current capability and ownership map** — identities, capabilities, route policies, X ownership, publication/audience rules, catalog listing, and content access with exact source owners.
4. **Selected extension architecture** — components, contexts, message/data flows, lifecycle, UI surface, and concise rejected alternatives with reasons.
5. **Permission, origin, identity, CSRF, and CORS model** — exact manifest permissions/patterns, server allowlist/config model, stable extension identity implications, trust proof, and off-tailnet/error behavior.
6. **Canonical eligible-meme server predicate** — exact predicate, authoritative owner, requester-private/public behavior, query contract, pagination/sorting, and non-enumeration guarantee.
7. **Save sequence: ordinary user** — end-to-end user gesture, post identification, service-worker request, Tailscale identity/capability, existing X lifecycle, state feedback, partial/retry/error behavior.
8. **Save sequence: administrator** — exact differences from the ordinary route and capability behavior; do not invent a privileged submit route if the current ordinary route is intentionally reused.
9. **Picker/search/preview design** — opening gesture, composer binding, query/filter model, preview/content routes, audience checks, cache/privacy behavior, and empty/error states.
10. **Composer detection and attachment design** — versioned X adapter, selected transfer/attachment mechanism, bounded fallback, media-size/memory constraints, no-submit guarantee, and failure recovery.
11. **Volatile X feasibility spike** — smallest separately authorized real-Brave/signed-in-X probe, exact observable criteria, cleanup, privacy, stop rules, and consequences for implementation ordering.
12. **Minimal backend/API/configuration delta** — current endpoints reused, smallest new or changed contracts, security rationale, and exact response/request shapes at planning precision.
13. **Exact proposed paths and owner map** — a table of every proposed new/changed file, its responsibility, and why that owner is canonical; distinguish extension, backend, tests, docs, config, and deployment packaging.
14. **Migration and durable-state implications** — migration decision, schema/index/backfill/downgrade if needed, compatibility, and privacy/data-retention effect.
15. **Privacy, secret, authentication, and abuse matrix** — asset/threat/boundary/control/test/residual-risk owner. Include malicious page, malicious extension, spoofed Origin/header, private-media enumeration, arbitrary proxying, hostile metadata, oversized media, stale adapter, and log leakage.
16. **Dependency decision** — each proposed runtime/dev dependency, primary-source justification, lockfile consequence, rejected dependency-free or alternative approach, and explicit later dependency authority needed.
17. **Causal implementation slices and gates** — start with the smallest risk-retiring spike; for each slice give paths, behavior, tests, exit gate, rollback, and dependency on prior evidence.
18. **Verification ladder** — exact unit, domain, API contract, persistence/migration, ingress security, extension fixture, local integration, packaged Brave, and production-readback gates. Separate deterministic repository claims from real-browser/user claims.
19. **Real Brave acceptance matrix** — administrator plus two ordinary tailnet identities; Save and Use journeys; static image, GIF-style, short video, own-private, published, other-private-denied, off-tailnet, capability-denied, unsupported/partial X post, X DOM drift, and manual-post guarantee. State prerequisites and which steps belong to Michal.
20. **Rollout, packaging, loading, rollback, and recovery** — stable extension ID, configuration, local developer loading, artifact/version relation, NUC release boundary, order of activation, compatibility/rollback, cleanup, and recovery from server/extension version skew.
21. **Owner documentation updates** — exact docs/ADR/operator/deployment/security/extension-user documentation proposed and why; do not use docs as a substitute for code/test ownership.
22. **Parked scope, residual risks, and stop conditions** — explicit non-MVP items, unresolved material facts, their owner, and what must stop later implementation or acceptance.
23. **Recommended implementation Worker route** — one route only: preferred current or fresh session, `Native planning mode: not-used`, lowest sufficient reasoning with named risks, exact implementation authority that must be newly granted, candidate topology, and whether later independent acceptance is required.
24. **Smallest next Orchestrator action** — one approval/revision decision only; do not ask Michal to choose among unresolved technical architectures you were required to resolve.

## 11. Quality and acceptance bar for this plan

The planning report earns `PASS` only if:

- the repository and AP gates are exact and non-contradictory;
- one architecture is selected rather than merely enumerated;
- the current mutation-origin conflict has a concrete least-privilege design and test strategy;
- the static X photo gap is handled honestly and causally;
- the private requester media-listing gap has a concrete server-authorized query design;
- the composer attachment mechanism is either evidenced enough to select or isolated behind the first smallest authorized feasibility spike;
- all exact owners and proposed paths are named;
- implementation slices are causally ordered and independently gateable;
- browser fixture evidence, real Brave evidence, Michal UX acceptance, repository acceptance, deployment, and production acceptance are not conflated;
- security, privacy, rollback, and failure recovery are first-class;
- no material item is deferred with vague language;
- no authority outside this prompt was exercised.

Return `PARTIAL` when the plan is useful but one named evidence gap prevents a safe final architecture. Return `BLOCKED` when baseline or authority contradiction makes planning unreliable. A long report is not a substitute for a selected, testable, least-privilege design.

## 12. Final stop rule

After sending the terminal report, stop. Do not edit files, create a branch, begin a spike, install the extension, access a signed-in browser, contact X, use the NUC, deploy, or continue into implementation. Plan approval by Michal or ORCHESTRATOR is a decision only; it does not reactivate this expired authority. Wait for a new complete prompt.
