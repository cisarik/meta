# Restoration Handout — Agent Orchestrator

Era: 10 (FrameNest meta tracking)
Logical whole: `framenest-companion-security-and-frozen-slice-validation`
Trace directory: `/home/agile/meta/projects/framenest/10/00-framenest-companion-security-and-frozen-slice-validation/`
Generated: 2026-08-28 by the closing Agent Orchestrator of era 09
(`framenest-pin-adoption-and-presentation-profile`).

Begin read-only. Re-verify every immediate gate yourself before trusting any
value in this handout, and initialize `00_notes.md` beside this handout at
open (AP 7ef45da convention: handout + `00_notes.md`, then
`01_planning_00.md` + `01_report_00.md` per exchange, prompt/report pairs
archived together after the report exists).

## 1. What This Whole Is

FrameNest's companion (Brave extension + side panel) and its information
security are first-class product surfaces and have never received a dedicated
security pass. In parallel, a large frozen-but-unvalidated product slice
(Gallery/Details MVP, companion review flows, upload/acquisition paths) now
exists with known bugs that the Cooperator will surface through manual testing.
This whole makes companion + infosec security the primary objective and folds
in defect-driven validation of the frozen slice, with rendered UI/UX
acceptance belonging to the Cooperator on a current NUC.

Recommended profile: **Agent Orchestrator** (default dispatch). Rationale:
this whole requires Worker generation, evidence gates, security-sensitive
repository mutations, and tests. A Read-only Orchestrator is not sufficient
for the implementation core; it remains suitable later for pure advisory or
reconnaissance wholes. Rendered UI/UX judgment is the Cooperator's regardless
of Orchestrator profile.

## 2. Immediate Gates — re-verify at open (read-only)

```text
Canonical repository: /home/agile/Projects/framenest
Branch: feat/x-meme-browser-companion
Expected local HEAD: d8629e33a4755406f8bb1bfec565ac6a3f4fb67e
Expected origin/feat/x-meme-browser-companion: d8629e33a4755406f8bb1bfec565ac6a3f4fb67e (published 2026-08-28; push verified by the era-09 closeout)
Expected porcelain: empty
AP pin: .ap gitlink == .ap HEAD == 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26
Public AP main: 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26 (git ls-remote)
Doctor: ./.ap/ap doctor PASS with "OK resolved governing variant: stable"
Product freeze commit: 472553cadcd3d4ca87a9792a2c306bd0afeea7c1 (ancestor of HEAD; era-10 mutations must define and respect their own bounded freeze/allowlist on top of this state)
NAC ledger: docs/AP_UPGRADE_OBSERVATIONS.md — entry consumer-declared-execution-and-capability-route-binding, state accepted, retain-active, revalidated against 7ef45da (verified in era-09 acceptance)
```

If public `main` of AP has advanced beyond `7ef45da` by the time you open,
treat pin adoption as a separate future whole, not an implicit side effect.

## 3. Required Reading (at pin 7ef45da)

- `AGENTS.md` — including the new project-owned `## Cooperator Presentation
  Profile` section (status marks 🟢🟡🔴, delivery capsule, Agent-Orchestrator
  default dispatch with P14 opt-out) and the managed AP block.
- `.ap/AP.md`, `.ap/AP_ORCHESTRATOR.md`, `.ap/PROMPT_CONTRACTS.md`,
  `.ap/INTEGRATION.md`, `.ap/UPDATING.md`, `.ap/INTUITION.md`, and
  `.ap/docs/adr/0022-default-agent-dispatch-trace-integrity-and-pin-presentation.md`.
- `docs/WORKER_EXECUTION_CONTRACT.md` (Cursor/AppImage boundary; `./.ap/ap
  exec` / `ap project check` with exact baseline; no raw Python).
- `SECURITY.md` and `SPEC.md` sections 18, 19, 22, 24, 28 (network boundary,
  dual audience, AI privacy, errors, security baseline).
- `docs/X_COMPANION.md`, ADR-0061, ADR-0064, ADR-0067, ADR-0068, ADR-0069,
  ADR-0070, ADR-0072, ADR-0073, ADR-0076, ADR-0077, ADR-0078, ADR-0079
  (companion review, histories, per-field AI, aliases, analysis proposals,
  runtime setting).
- `SERVER.md`, `PRODUCT.md` (companion and gallery context), ADR-0074
  (dual audience), ADR-0075 (NUC routine refresh framing), ADR-0053
  (ordinary upload), ADR-0048 (Tailscale identity foundation).

## 4. Objectives (Cooperator-approved direction)

1. **Companion + Brave extension security pass (primary).** No dedicated
   security review or hardening of the companion surfaces has ever happened
   ("zabezpečenie Companion ešte vôbec"). Cover backend endpoints consumed by
   the companion, the extension itself, the side panel, and the web shell
   rendering paths (backend AND frontend). Changes that alter documented
   security contracts require corresponding SECURITY.md living updates and
   fresh independent acceptance.
2. **Infosec hardening of shipped backend surfaces** (candidates in Section
   6B) — bounded, evidence-gated fixes.
3. **Frozen-slice validation and defect triage.** The Cooperator will manually
   refresh the NUC and test with the Brave companion; concrete defects he
   reports are triaged, classified, and fixed in bounded slices. The frozen
   Gallery/Details visual behavior reopens only through concrete defects, not
   wholesale redesign (AGENTS.md product boundaries).
4. **UI/UX defects** are in scope exactly as far as they are concrete defects
   found by rendered acceptance; aesthetic reopens of the frozen Gallery and
   Details MVP remain out of scope unless the Cooperator explicitly redecides.
5. **Documentation drift editorial pass** (Section 6C) so Workers are never
   misled by stale prose.
6. **Out of scope unless separately granted:** NUC host security hardening
   (systemd sandbox uplift, AppArmor/UFW completion), NUC deployment mutations
   (the Cooperator runs `deploy/ubuntu/framenest-release` manually), pin
   adoption beyond 7ef45da, and any router/funnel exposure (forbidden always).

## 5. Cooperator Working Agreement

- Michal is the Cooperator; chat in Slovak, masculine address, feminine
  Orchestrator self-reference; one-glance first (≤5 lines) then exactly one
  status mark; one decision per message.
- Dispatch: Agent Orchestrator default (direct session dispatch of complete
  authoritative Worker prompts); copy-paste only on explicit P14 opt-out.
- He will manually: refresh the NUC after publications
  (`deploy/ubuntu/framenest-release` per ADR-0075), commit the meta trace
  directory to the meta repository, and perform rendered UI/UX and Brave
  companion acceptance over Tailscale. Never request rendered acceptance
  against code the NUC cannot serve; verify `framenest-release status`
  readback first (authoritative runtime readback, never a SHA snapshot).
- Meta trace commits are manual by Michal; Orchestrators and Workers write
  prompt/report/notes/closeout files but never commit the meta repository.

## 6. Candidate Worklist (discovery-grade, evidence-backed)

These are non-authoritative findings from the era-09 Orchestrator-direct deep
review (read-only, HEAD `d8629e3`). None is a proven vulnerability. Re-verify
each against current code before planning fixes.

### 6A. Companion + Brave extension security (never reviewed before)

- **Untrusted AI-suggestion strings rendered in DOM.** Provider suggestions
  are untrusted preview data; verify every rendering path in the side panel,
  title-bar history, review popups, and the web shell uses text-safe
  insertion (no `innerHTML` with suggestion-derived content). Files to start:
  `src/framenest/adapters/api/static/web/` shell (`index.html`, `app.js`),
  extension side panel sources, hosted Details surface.
- **Hosted Details iframe surface.** Rows post hosted `open_details` and the
  iframe stays mounted; verify sandbox attributes, allowlist, referrer
  policy, and absence of `postMessage` trust in that context.
- **Extension message-passing and MV3 hygiene.** Validate sender-origin
  checks on every runtime.onMessage channel; minimal `host_permissions`; no
  eval/remote code; service-worker CSP; content scripts never fetch FrameNest
  or the CDN (declared invariant — verify still true).
- **Status bridge untrusted page data.** X page DOM data flows into submits;
  server validates bounded exact JSON and revalidates forms, but verify the
  extension cannot forward arbitrary URLs or HTML fragments beyond the
  documented fields.
- **`FRAMENEST_COMPANION_EXTENSION_ORIGINS` operations UX.** Exact
  `chrome-extension://` allowlist, default empty, fail-closed; document how
  the Cooperator sets it on the NUC and what visible failure guidance exists
  (SECURITY.md already specifies the five gated mutation routes; SERVER.md
  historically said four — drift, see 6C).
- **Storage privacy.** Per-user overlay/edit state persisted in
  `chrome.storage` on a potentially shared machine; assess exposure and
  bounded mitigations.
- **Packing/update story.** The extension is unpacked; no auto-update path
  exists; record the position and what changes when it becomes packed.
- **Login-key privacy.** `Tailscale-User-Login`-derived identity handling in
  companion surfaces; confirm no identity/alias leakage between actors in
  history and inbox payloads.

### 6B. Backend infosec candidates

1. **UDS socket-permission assertion at startup.** Header trust in
   `tailscale_uds` is bound to socket provenance, but nothing fails closed if
   the socket is created world-connectable. Add a startup mode/owner assertion
   (or CRITICAL fail) for `tailscale_uds` and `public_published_uds` in
   `src/framenest/adapters/api/` server composition / `server.py`.
   (Evidence: `tailscale_ingress.py:1-9,71-90,998-999`; `server.py:25-30`.)
2. **Uniform 422 contract on the workspace app.** FastAPI default validation
   body echoes caller input and field paths in a different shape than the
   uniform `{"error": {code, message}}` contract; public app already maps
   validation to uniform 404. (Evidence: `application.py` lacks a
   `RequestValidationError` handler; contrast
   `public_published_application.py:210-221`.)
3. **Adapter `str(exc)` passthroughs.** All current raise sites are static
   sanitized strings, but the sanitizer invariant lives in the application
   layer; replace with static messages at the adapter for
   infrastructure/unavailable classes (pattern exists at
   `youtube_request_api.py:440-445`). Sites: `x_request_api.py:188-276`,
   `x_admin_api.py:107`, `library_api.py:144,146`,
   `youtube_request_api.py:412-433`, `analysis_proposal_api.py:142`.
4. **Public composition catch-all status pass-through.** Defensive branch
   returns non-uniform statuses with uniform bodies
   (`public_published_application.py:223-240`); collapse to 404 or pin intent.
5. **Narrow TOCTOU in `LocalMediaContentReader`** (intermediate components;
   requires local FS write access; optional `openat` hardening or documented
   residual assumption). (Evidence: `media_content.py:60-79,97-102`.)

### 6C. Documentation drift editorial pass (one bounded task)

- NUC "personal production server" present-tense framing contradicts
  ADR-0075: `PRODUCT.md:91,145,258-259`; `ROADMAP.md:375,377`;
  `SPEC.md:7,807`; `README.md:521,625` (README status/SECURITY/SERVER/runbook
  are already migrated).
- `public_published_uds` described as unshipped while implemented-for-backend:
  `PRODUCT.md:72-75`; `ROADMAP.md:401-405` (README/SPEC are correct).
- ADR-0077/0078 absent from all living docs despite shipped implementation
  (`/api/media/{media_id}/ai-suggestions`, alias edit affordance, per-field
  AI review). Add status lines to README, PRODUCT §2, ROADMAP, SPEC §19.
- `README.md:274` claims a `FRAMENEST_HOST=0.0.0.0` exposure override the
  code rejects (`configuration.py:460-462`); reword.
- `PRODUCT.md:409` says production provider-secret integration "remains
  unresolved" although ADR-0036 shipped repository source material
  (`deploy/ubuntu/production_ai_deploy.py`, systemd drop-ins,
  `infrastructure/ai/credentials.py`).
- `SERVER.md:94-95` counts four companion mutation routes; there are five
  (the fifth is `PUT /api/admin/settings/automatic-analysis`).
- Stale "capability until later deployment proves it" prose:
  `README.md:296-298`; `ROADMAP.md:107`; `docs/UBUNTU_NUC_DEPLOYMENT.md:158-161,207-208`.
- ADR index rows for 0032/0060 lack the ADR-0075 supersession annotation;
  `README.md:123` Poetry-version sentence is stale (lock says 2.3.2, deploy
  pins 2.4.1).
- Do not edit accepted ADR content in place; fix the index and living docs,
  let ADR-0075 carry reinterpretation.

### 6D. Known nits (fold into adjacent tasks)

- `uq_x_post_claims_id` UniqueConstraint in runtime `catalog_schema.py:1211`
  has no migration counterpart (0028) — drop or add in the next additive
  migration.
- Dead constant `_QUALIFYING_DUPLICATE_CANONICAL_STATES`
  (`upload_session_repository.py:67-71`).
- Cursor-error branch keyed on message text
  (`youtube_request_api.py:411-419`) — prefer a typed exception.
- Type annotations `analysis_run_id: MediaId` should be
  `MediaAnalysisRunId` (`companion_review_repository.py:345,420`).
- `X_CATALOG_HANDOFF_FAILED` on `DUPLICATE_PENDING` X assets is unreachable
  today; document or auto-resolve like the YouTube path if the mode ever
  changes (`x_acquisition.py:1080-1088`).

### 6E. Positive confirmations (verified solid in era-09 review; do not regress)

Capability matrix for companion/X/admin-settings endpoints (admin-only inbox,
owner-fenced opened, apply double-gated, audit events fail-closed);
extension-origin allowlist fail-closed when empty; audience policy enforced at
every direct media surface; public published reader is a true separate
read-only composition; publication chain crash-safe (0600 `O_NOFOLLOW|O_EXCL`,
fsync, verified `published -> cataloged` single transaction, retryable
cleanup); YouTube/X downloaders cookie-free with PATH-only environments;
automatic analysis triple-gated and `analyzing -> failed` fail-closed with
`ANALYSIS_OUTCOME_UNKNOWN`; workstation sudo bridge genuinely narrow
(zero-argument fixed launcher, `NOSETENV`, `RENAME_NOREPLACE`); release helper
matches ADR-0060; loopback-first enforced in code (non-loopback TCP bind
rejected); no ADR contradicts loopback-first/Tailscale-only/read-only
`/srv/media`.

## 7. Recommended Sequencing

1. Planning exchange (`01_planning_00.md`, Planner Worker, read-only):
   companion threat map against current code, defect intake plan, worklist
   slicing, acceptance strategy.
2. Bounded implementation slices with stage gates; security-contract changes
   update `SECURITY.md` in the same slice; each slice set gets fresh
   independent acceptance (this whole changes security-relevant semantic
   owners — treat evidence accordingly, prefer `required-separate-fresh-worker`).
3. Publication only with explicit per-task Cooperator grant; NUC refresh is
   manual by Michal; then rendered UI/UX + Brave companion acceptance by
   Michal over Tailscale; defects return as triaged input.
4. Docs drift editorial pass as its own bounded task (6C) — cheap, high
   value, do it early so Workers read truthful prose.
5. Closeout per AP: ledger reconciliation, Cooperator-informed closure, no
   Worker-emitted closure signals.

## 8. Boundary Constants (never reopen by side effect)

Loopback-first backends; Tailscale-only remote access; no Funnel; no router
port forwarding; Tailscale membership is not app authority; no provider
secrets to ordinary clients; `/srv/media` read-only to the service; no NUC
host mutation without explicit bounded grant; no push without per-task grant;
secrets never committed; private media, credentials, host identifiers never
exposed in artifacts or reports; product boundaries in `AGENTS.md` govern what
may be claimed as shipped.

## 9. Trace Conventions

```text
Trace directory: this directory (private, local-only; Michal commits manually)
Prompt/report pairs: 01_planning_00.md + 01_report_00.md, 02_implementation_00.md + 02_report_00.md, 03_acceptance_00.md + 03_report_00.md, ... (fresh session per phase; exchange suffix _00)
Companion integrity: a report companion commences exactly with "### Report for ORCHESTRATOR_CHAT", echoes coordinates, and is never a duplicate of its prompt; pairs are archived together by the Orchestrator after the report exists; interruption companions are named explicitly and archived the same way.
Notes: 00_notes.md is the living whole ledger of verified state and decisions.
Closeout: a final Orchestrator-authored closure file plus a closing 00_notes.md entry; no Worker ever emits project closure.
```

## 10. Session-Close Obligations

At whole close: reconcile the upgrade ledger (new observations only if they
are genuinely AP-upgrade observations targeting the canonical AP repo —
product findings are NOT ledger material), obtain Cooperator-informed closure,
clean temporary probe state, and record final HEAD/pin in `00_notes.md`.
