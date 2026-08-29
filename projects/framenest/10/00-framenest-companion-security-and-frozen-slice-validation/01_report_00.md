### Report for ORCHESTRATOR_CHAT

1. **Logical whole identity:** framenest-companion-security-and-frozen-slice-validation; Worker session ordinal: 01; Worker exchange ordinal: 01

2. **Status: PASS** (read-only planning; one plan-only cycle used)

3. **Phase-qualified result:** not-applicable

4. **Start and end commit:** both `d8629e33a4755406f8bb1bfec565ac6a3f4fb67e` (branch `feat/x-meme-browser-companion`, porcelain empty, `.ap` gitlink == submodule HEAD == `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`, origin branch head equals local HEAD, freeze baseline `472553c` confirmed ancestor). All pre-analysis gates passed.

5. **Changed files and purpose:** none (read-only planning). **Commit and push result:** none authorized, none performed.

---

## 6. Evidence — the plan

### 6.0 Method and evidence discipline

All findings below are evidence class **`established-static`** (exact path:line re-verified this session at the baseline). `reproduced-dynamic` was **not** authorized and was not performed. Per AP discipline: a dangerous API or CWE entry is a risk signal only; exploitability conclusions are capped at **"plausible but unproven"** without dynamic reproduction. Each candidate is classified **confirmed** / **stale** (handout claim no longer matches code) / **refuted**.

---

### 6.1 Work area A — companion + extension threat map (primary)

**Assets:** catalog metadata truth (canonical + per-user alias overlays), per-actor review-opened state, publication state, AI-suggestion strings (untrusted preview data), login-key identity mapping, operator-only YouTube acquisition channel, provider secrets (server-side only), companion `chrome.storage` state, extension stable ID / private key custody.

**Trust boundaries:** (1) X page DOM → content script → service worker; (2) service worker → `tailscale_uds` backend (extension Origin allowlist + `X-FrameNest-Request: 1` + Tailscale identity + capability + pre-execution audit); (3) side panel ⇄ hosted FrameNest iframe (`framenest.companion.web.v1`, both directions origin-pinned); (4) content script ⇄ extension pages (`framenest.companion.v1`, version/type gated); (5) Unix-socket provenance → `Tailscale-User-*` header trust (middleware-only, `tailscale_uds` mode); (6) provider → server → browser rendering of suggestion strings.

**Security properties verified in code (positive confirmations to protect):**

| Property | Evidence |
|---|---|
| Exactly five `companion_mutation` routes (X submit, X retry, opened, apply, automatic-analysis PUT) | `tailscale_ingress.py:409-416,546-581` |
| Allowlist fail-closed when empty; mutation requires non-None Origin == external origin or allowlisted companion origin; `X-FrameNest-Request: 1` required | `tailscale_ingress.py:1023-1034,741-765,661-670` |
| GET inbox / own-history / detail need no allowlist (safe methods bypass origin gate) | `tailscale_ingress.py:741` (unsafe-methods gate only) |
| Fail-closed unclassified routes (sanitized 404 for every identity class) | `tailscale_ingress.py:633-648,709-717` |
| Header trust bound to mode, single middleware, duplicate/conflict rejection, forwarded-proto/host pinning | `tailscale_ingress.py:1-9,689-707,891-898` |
| Audit-before-mutation, fail-closed `500 AUDIT_UNAVAILABLE` on write failure | `tailscale_ingress.py:829-845`; `companion_review_api.py:442-445` |
| Capability matrix: admin-only inbox/detail (`media.workflow.read`), ordinary own-history (`x.request`), owner-fenced opened (`require_owner=not media.workflow.read`, uniform 404 otherwise), apply double-gated (`media.content.publish` ∧ `metadata.canonical.write`) | `companion_review_api.py:409-439,316-319`; owner gate `companion_review_repository.py` `_actor_owns_cataloged_x` |
| No identity/alias leakage between actors in payloads: inbox/detail/apply dicts expose no `login_key`, no actor fields; own-history filtered by `actor_login_key`; alias keyed `(media_id, login_key)`, login_key never in body | `companion_review_api.py:448-581`; `companion_review_repository.py:128-158`; `media_alias_api.py` (caller-private overlay routes) |
| Content scripts never fetch FrameNest or the CDN — zero `fetch`/`XMLHttpRequest`/`WebSocket` in content scripts | `extension/content/x_adapter.js`, `x_adapter_contract_v1.js` (grep-verified absence) |
| Extension cannot forward arbitrary URLs/HTML: `acceptXPostUrl` enforces HTTPS, X hosts, no query/hash/credentials, exact `/{handle}/status/{id}`, ≤2048 chars; alias sanitized (title canonicalized, description ≤10000, tag_keys regex + ≤32); web bridge accepts only UUIDs (`open_details` payload: `mediaId` UUID-checked at `companion_host.js:83-96`); attach carries UUID pair only | `messages.js:99-134,190-198`; `service_worker.js:188-231`; `companion_host.js:83-96,109-126`; `sidebar.js:31-39` |
| Hosted iframe rows post `open_details` with `targetOrigin = storedOrigin`, never `*`; inbound requires `event.source === frame.contentWindow` ∧ `event.origin === storedOrigin` ∧ protocol/version gate; web side posts to parent only with pinned extension origin and accepts only that origin | `sidebar.js:17-31,564-578,780-795`; `companion_host.js:57-62,64-107` |
| Text-safe rendering: **zero** `innerHTML`/`outerHTML`/`insertAdjacentHTML`/`document.write`/`eval` in `extension/` and `src/framenest/adapters/api/web/`; history rows/pending rows use `textContent` + `setAttribute`; web URL builders use `encodeURIComponent` on identity-only IDs; asset route is an exact-name allowlist of 3 files (no traversal) | grep-verified; `sidebar.js:152-174`; `app.js:4446-4475`; `application.py:331-342,1333-1341` |
| Untrusted suggestion strings bounded server-side at domain layer (control-character rejection, code-point caps, tag bounds, duplicate rejection); `extra="forbid"` on companion bodies | `domain/media_metadata.py:89-101`; `domain/media_user_alias.py:37-56`; `x_request_api.py:65-77`; `runtime_settings_api.py:26-33` |
| MV3/CSP hygiene: no `content_security_policy` override (MV3 default CSP), no remote code, no `externally_connectable`, no sandbox page, WAR limited to picker/save on `x.com|twitter.com` only, `review.html` not web-accessible and unused for history clicks, no X host permission on the service worker, `optional_host_permissions` only `https://*.ts.net/*` | `extension/manifest.json:1-46`; `X_COMPANION.md:114,208-209` |
| `chrome.storage.local` holds no secrets: only `frameNestOrigin`, `inflightClaims` (capped 16), `reviewInboxAwaitingAnalysis` (capped 16, media_id + expiry) | `service_worker.js:6-12,154-165,384-403,460-498` |
| `FRAMENEST_COMPANION_EXTENSION_ORIGINS` validator: bounded count, strict `chrome-extension://` + 32×`[a-p]` pattern, dedup; default empty | `configuration.py:231,422-433` |
| Operator-observable empty-allowlist behavior: GET inbox/own-history succeed; any mutation carrying the extension Origin returns sanitized `403 MUTATION_ORIGIN_FORBIDDEN`; rollback is removing the key or `[]` + restart; no CORS headers anywhere | `X_COMPANION.md:118-121,165-179`; `tailscale_ingress.py:1023-1034` |
| Public published reader is a true separate read-only composition (allowlist router, safe-methods guard, CORS strip, `no-store`, uniform 404, schema-head pin, forbidden derivatives) | `public_published_application.py:59-61,81-208` |
| TCP ingress rejects non-loopback bind in code | `configuration.py:461-462` |

**A-findings (risk signals, not proven exploits):**

- **A-F1 (established-static, low, documented residual):** workspace HTML responses set no `frame-ancestors`/`X-Frame-Options` (`application.py:1326-1341`). The workspace origin is embeddable by any page. Impact capped by design: all mutations require the exact `Origin` + non-simple header (`tailscale_ingress.py:741-765`), and identity is per-request header-injected (no cookies), so a hostile embedder cannot ride an ambient session. Deliberate: adding `frame-ancestors` would break the companion side-panel hosting contract (ADR-0063 §3). Plan: document as residual, no code change.
- **A-F2 (established-static, low, operational):** unpacked extension, no auto-update path; key rotation changes the ID and requires allowlist update (`X_COMPANION.md:151-163`). Position recorded; what changes when packed (store signing, update channel, ID continuity) documented in S1.
- **A-F3 (established-static, low):** `chrome.storage.local` per-user overlay/draft traces (origin, inflight claim ids, awaiting media ids) are readable by anything executing in the same browser profile on a shared machine; no cross-profile exposure. Mitigation deferred (profile hygiene, not product code); documented in S1.

**Stale/refuted handout claims in area A:** none — every referenced handout claim matched current code. Two path corrections: the web shell lives at `src/framenest/adapters/api/web/` (prompt said `static/web/`), and the server composition is `src/framenest/server.py` (prompt located it under `adapters/api/`). Both re-located and used.

---

### 6.2 Work area B — backend infosec candidate verification table

| # | Candidate | Verdict | Current evidence (path:line) | Notes |
|---|---|---|---|---|
| B1 | UDS socket-permission fail-closed assertion missing at startup | **Confirmed** | `src/framenest/server.py:25-30` (assert uds_path only); trust bound to provenance `tailscale_ingress.py:1-9,998-999`; systemd posture `deploy/systemd/framenest.service:24-25` (`RuntimeDirectory` + `UMask=0077`) | Nothing verifies socket/dir mode+owner at runtime. Outside systemd, `tailscale_uds` binds wherever the operator points it; a world-connectable socket lets any local process inject `Tailscale-User-Login` of a mapped admin (full admin) and reach `CHANNEL_LOCAL` YouTube operator routes (`tailscale_ingress.py:863-889`). Impact capped: "plausible but unproven" — but the fail-open gap itself is static-certain. `public_published_uds` exposure is lower (identity-absent published reads only). No existing test asserts socket permissions (checked `test_server_runtime.py`, `test_uvicorn_runtime.py`). Highest-value fix. |
| B2 | Workspace app lacks uniform 422 contract (FastAPI default echoes caller input in `{"detail": [...]}` shape) | **Confirmed** | No `RequestValidationError` handler registered in `application.py` (grep-verified absence); contrast `public_published_application.py:210-221` which maps validation → uniform 404 | Uniform error contract (`SPEC §24`, `{"error": {code, message}}` everywhere else, e.g. `companion_review_api.py:584-589`). Fix: `RequestValidationError` handler on the workspace app returning uniform `{"error":{code,message}}` (status choice: 400/422 — see open question OQ-4). |
| B3 | Adapter `str(exc)` passthroughs depend on application-layer sanitizer invariant | **Confirmed (defense-in-depth)** | `x_request_api.py:188-192,200-201,239-242,265-266,273-277`; `x_admin_api.py:107`; `library_api.py:144,146`; `youtube_request_api.py:412-424,435`; `analysis_proposal_api.py:142` | All raise sites verified static today (`x_acquisition.py:257,480-502,532,555,945,995,1060,1066,1106` etc.). Static pattern already exists at `youtube_request_api.py:440-445`. Candidate: static messages at the adapter for infrastructure/unavailable/limit classes so the invariant no longer lives solely in the application layer. |
| B4 | Public composition catch-all passes through non-uniform statuses with uniform bodies | **Confirmed** | `public_published_application.py:223-240` (statuses outside {401,403,404,405,406,415} return `exc.status_code` with a NOT_FOUND body) | Collapse to uniform 404 or pin intent; reachable statuses here are effectively only framework-raised 4xx/5xx Starlette exceptions. |
| B5 | Narrow TOCTOU in `LocalMediaContentReader` | **Confirmed (residual, narrow)** | `media_content.py:30-34` (`O_NOFOLLOW` final component only), `59-88` (`_resolve_safe_target`: flavor check, root containment, `resolve(strict=True)` both sides, `relative_to` containment), `97-102` (`os.open` on the previously resolved path) | Window between `resolve()` and `os.open()` for intermediate path components; requires local FS write access to a registered library root (actor already inside the media storage boundary). Options: `openat`-style dirfd hardening or documented residual assumption. Recommend documenting (OQ-2). |

---

### 6.3 Known defect candidates — verification

| Candidate | Verdict | Evidence |
|---|---|---|
| `uq_x_post_claims_id` runtime constraint without migration counterpart | **Confirmed** | `catalog_schema.py:1211`; migration `0028_x_requester_acquisition.py:47` creates `id` as PK with no such UniqueConstraint (grep-verified). Redundant with PK; recommend drop (runtime-only) to clear drift without a schema jump — OQ-3. |
| Dead `_QUALIFYING_DUPLICATE_CANONICAL_STATES` | **Confirmed** | `upload_session_repository.py:67-71`; definition only, zero references (grep-verified). |
| Cursor-error branch keyed on message text | **Confirmed** | `youtube_request_api.py:411-419` (`"cursor" in message.lower()`); fold a typed exception into S4. |
| `analysis_run_id: MediaId` annotations | **Confirmed** | `companion_review_repository.py:345,420` (both `mark_opened` and `apply_review`); should be `MediaAnalysisRunId`; annotation-only, no runtime change. |
| `X_CATALOG_HANDOFF_FAILED` on `DUPLICATE_PENDING` unreachable | **Confirmed** | `x_acquisition.py:1080-1088` + `1004-1010`: duplicate mode is `SILENT_KEEP_SEPARATE` whenever a requester exists (every X claim has one — identity required), and `EXPLICIT` requires `requester is None`; ordinary duplicates keep-separate atomically, so `DUPLICATE_PENDING` is never the observed state. Document reachability rationale or mirror the YouTube auto-resolve if the mode ever changes. |

---

### 6.4 Work area D — documentation-drift verification table

| Item | Verdict | Current evidence |
|---|---|---|
| NUC "personal production server" present-tense framing vs ADR-0075 | **Confirmed stale** | `PRODUCT.md:91,145,258-259`; `ROADMAP.md:375,377`; `SPEC.md:7,807`; `README.md:521,625`. (README status/SECURITY/SERVER/runbook already migrated — verified `SERVER.md:53-64`, `SECURITY.md:7-19`.) |
| `public_published_uds` "future/None shipped" wording vs implemented-for-backend | **Confirmed stale** | `PRODUCT.md:72-75` ("future local-only … None of those successors is shipped"); `ROADMAP.md:399-405`. Truth: `SPEC.md:597-604` ("implemented-for-backend"), `SECURITY.md:204-210`. |
| ADR-0077/0078 absent from living docs | **Confirmed** | Zero hits for 0077/0078 in README/PRODUCT/ROADMAP/SPEC (grep-verified; only 0079 hits, e.g. `README.md:702`). Add status lines to README, PRODUCT §2, ROADMAP, SPEC §19 for `/api/media/{media_id}/ai-suggestions` (route `tailscale_ingress.py:308-311`), alias Edit affordance, per-field AI review, card 🧠. |
| `README.md:274` claims `FRAMENEST_HOST=0.0.0.0` exposure override | **Confirmed wrong** | `configuration.py:461-462` raises on any non-loopback TCP host. Reword to "loopback-only binding is enforced in code". |
| `PRODUCT.md:409` "production provider-secret integration remains unresolved" | **Confirmed stale** | `deploy/ubuntu/production_ai_deploy.py` exists; `SERVER.md:324-328` ("repository source material … under explicit operator authority per ADR-0036"); `tests/contract/test_production_ai_deployment.py` exists. Reword to the SERVER.md formulation. |
| `SERVER.md:94-95` counts four companion mutation routes | **Confirmed stale** | Five in code (`tailscale_ingress.py:409-416,546-581`); ADR-0079 §4 explicitly supersedes "exactly four" statements in living documents. |
| "Capability until later deployment proves it" prose | **Mixed** | `README.md:296-298` and `ROADMAP.md:107` (release-update contract): **stale** — a release was accepted (`aec2f009…`, schema 0028, dated history in README/SECURITY) and ADR-0075 made routine refresh normal. `docs/UBUNTU_NUC_DEPLOYMENT.md:158-161`: first sentence block contradicts ADR-0075 cadence framing → **stale in part**; `:207-208`: "repository presence alone is not proof of host-loss survival" remains true, but the workstation-pull provisioning state is **host-state not resolvable read-only from the repository** (`docs/BACKUP_AND_RECOVERY.md:174` carries the same conditional). Gated on OQ-1. |
| ADR index 0032/0060 supersession annotation; README Poetry sentence | **Confirmed** | `docs/adr/README.md:59,87` (plain "Accepted", no ADR-0075 annotation); `README.md:123` says lock generated with Poetry 2.1.4 — `poetry.lock:1` says 2.3.2, deploy pins 2.4.1 (`framenest_release.py:38`). Fix index annotations + README sentence; do not edit accepted ADR bodies (ADR-0075 carries the reinterpretation). |

---

### 6.5 Work area E — slices, sequencing, evidence tiers, acceptance

**Evidence tiers (basis):** E0 = documentation/static analysis only; E1 = static code evidence + focused Python tests via `./.ap/ap exec --root /home/agile/Projects/framenest --baseline <authorized> --operation test-focus -- <tests> -q -p no:cacheprovider`; E2 = E1 + relevant JS suites via `node --test tests/<name>.test.js` from worktree root + the focused contract set for the changed surface; E3 = rendered/browser evidence (`FRAMENEST_RUN_BROWSER_EVIDENCE=1` gated suites) or NUC `framenest-release status` readback with Cooperator rendered acceptance; E4 = fresh independent acceptance by a fresh Worker session that did not implement the candidate.

**Slice order** (security-critical path first; docs slice parallelizable at any point; no slice authorizes the next):

| Slice | Goal | Changed-path allowlist | Tier | Validation (focused) | Rollback | Stop conditions | Independent acceptance |
|---|---|---|---|---|---|---|---|
| **S1** | Docs-drift editorial pass (all verified §6.4 items) + ADR index annotations + SECURITY.md documentation-only additions: companion `chrome.storage` exposure position (A-F3), packed-extension position (A-F2), workspace-embeddability residual (A-F1), operator empty-allowlist observation text | `README.md`, `PRODUCT.md`, `ROADMAP.md`, `SPEC.md`, `SECURITY.md`, `SERVER.md`, `docs/UBUNTU_NUC_DEPLOYMENT.md` (gated on OQ-1), `docs/adr/README.md` | E0→E1 | Structure/links/semantics review; `tests/contract/test_nuc_release_docs.py`, `test_nuc_operator_runbook.py`, `test_ap_integration.py` (runbook/ADR index content is test-asserted) | Revert commit; docs-only | Any required edit inside an accepted ADR body (forbidden); OQ-1 unresolved for the two runbook lines (excise them from the slice until answered) | **Scoped acceptance sufficient** — argued: no semantic owner, no runtime behavior, no security-contract change; docs edits are their own semantic owners and Cooperator reviews wording. ADR index rows annotate, not rewrite. |
| **S2** | **B1:** fail-closed startup assertion for `tailscale_uds` and `public_published_uds`: after bind, verify socket exists, is a socket, mode has no group/other bits, owner == euid; failure → CRITICAL log + fail-closed exit before serving. Update `SECURITY.md` ingress section in the same slice | `src/framenest/server.py`, `src/framenest/configuration.py` (if a settings flag is needed — prefer none), `tests/unit/test_server_runtime.py`, `tests/contract/test_uvicorn_runtime.py`, `SECURITY.md` | E1→E2 | `test-focus`: `tests/unit/test_server_runtime.py tests/contract/test_uvicorn_runtime.py tests/contract/test_tailscale_ingress_security.py` (new fail-closed cases: permissive mode fails startup; correct systemd-like mode passes; public mode likewise) | Revert commit; restores permissive status quo (documented in slice) | If assertion would break the documented systemd deployment (`framenest.service` mode), stop and report rather than loosening | **Required-separate-fresh-worker** — alters a documented security contract (header-trust provenance precondition) and server startup semantics. |
| **S3** | **B2+B4:** uniform error contract on the workspace app (`RequestValidationError` → uniform body) + collapse/pin the public catch-all status pass-through to uniform 404 | `src/framenest/adapters/api/application.py`, `src/framenest/adapters/api/public_published_application.py`, `tests/contract/test_local_web_application.py`, `tests/contract/test_public_published_uds.py`, `tests/contract/test_x_request_api.py`, `tests/contract/test_companion_review_api.py`, `SECURITY.md` (only if 422-shape text is added) | E1→E2 | `test-focus`: `test_local_web_application.py test_public_published_uds.py test_x_request_api.py test_companion_review_api.py test_youtube_request_api.py test_upload_api.py` (uniform-shape assertions on malformed bodies) | Revert commit | If any existing client/JS suite depends on FastAPI's default 422 shape, stop and report (contract negotiation with Cooperator) | **Required-separate-fresh-worker** — changes runtime behavior of the error contract on every malformed request (documented sanitized-response contract). |
| **S4** | **B3** static adapter messages for infrastructure/unavailable/limit classes + typed cursor exception (defect candidate 3) + annotation fix `MediaAnalysisRunId` (candidate 4) | `src/framenest/adapters/api/x_request_api.py`, `x_admin_api.py`, `library_api.py`, `youtube_request_api.py`, `analysis_proposal_api.py`, `src/framenest/infrastructure/persistence/companion_review_repository.py`, focused tests for each | E1 | `test-focus`: `test_x_request_api.py test_x_companion_api.py test_youtube_request_api.py test_library_api.py test_analysis_proposal.py test_companion_review_api.py` | Revert commit | If a typed-exception change requires touching the application layer beyond the adapter, stop (scope boundary) | **Scoped acceptance sufficient** — argued: identical sanitized static messages today; no observable contract change; internal invariant hardening; annotation-only repository edit. |
| **S5a** | Hygiene + documentation of residual assumptions: remove dead constant (candidate 2); document `X_CATALOG_HANDOFF_FAILED` reachability rationale (candidate 5); document B5 TOCTOU residual assumption in `SECURITY.md` (pending OQ-2; code change only if Cooperator chooses `openat` hardening) | `src/framenest/infrastructure/persistence/upload_session_repository.py`, `src/framenest/application/x_acquisition.py` (comment/docstring only), `src/framenest/infrastructure/filesystem/media_content.py` (optional), `SECURITY.md`, focused tests | E1 | `test-focus`: `tests/unit/adapters` upload-session repository tests, `test_media_content_api.py` | Revert commit | If removing the constant reveals a hidden caller, reclassify as candidate defect, stop | **Scoped acceptance sufficient** — no runtime contract change (dead code removal, comments, documented residual). |
| **S5b** | **Candidate 1** resolution: drop runtime `uq_x_post_claims_id` (recommended, OQ-3) or add additive migration `0034` | Either `catalog_schema.py` (+test) or new `alembic_environment/versions/0034_*.py` | E1→E2 (schema) | `test-focus`: `tests/contract/test_x_request_api.py tests/unit/infrastructure` persistence tests; migration path test if 0034 | Revert commit; if 0034 shipped, documented downgrade path per runbook discipline | Any destructive rewrite of historical rows → stop (additive only) | **Required-separate-fresh-worker** — durable-data/schema-affecting trigger. |
| **S6** | Optional S3-rendered sanity pass deferred to Cooperator: NUC routine refresh via `deploy/ubuntu/framenest-release`, then Brave companion rendered acceptance over Tailscale (activates work area C intake) | None (operator/Cooperator actions) | E3 | `framenest-release status` readback **before** any rendered testing; browser companion suites where gated | n/a | Rendered acceptance against a NUC serving a different SHA → stop testing | Cooperator-owned rendered acceptance; not a Worker slice |

**Out of scope for this whole (never reopen):** NUC host hardening; NUC deployment mutations beyond the sole routine release-update entry point; AP pin movement; router/funnel exposure (always forbidden); publication beyond explicit per-task Cooperator grant; provider calls; extension packing/store publication; `/srv/media` write access; new companion routes or manifest permission changes.

### 6.6 Work area C — frozen-slice defect intake plan

1. **Precondition (hard gate):** before any rendered UI/UX acceptance or Brave companion testing, the Cooperator (or an authorized routine refresh) runs `deploy/ubuntu/framenest-release status` and the deployment targets the exact public `main` SHA under test; the report must carry the SHA readback. Never test against code the NUC cannot serve.
2. **Intake route:** Cooperator report → Orchestrator triages against this plan's verification tables → classification: (a) **defect in frozen Gallery/Details/companion MVP** (concrete functional defect, in scope → bounded correction slice, one smallest coherent correction, fresh Worker per AP correction rules); (b) **aesthetic reopen** (out of scope unless the Cooperator explicitly redecides — recorded as Cooperator-owned decision, not a defect); (c) **security-relevant observation** (routed through this whole's threat map, evidence-class discipline applies); (d) **out-of-scope observation** (ledger candidate, no scope expansion).
3. **Required report fields from Michal:** surface (Gallery / Details / side panel / Save popup / picker / hosted iframe), steps to reproduce, observed vs expected, NUC release SHA readback, browser (Brave version), and whether the state survived a page reload. No private media filenames, no tailnet hostnames beyond what testing already exposes to the Orchestrator.
4. **Triage SLA shape:** each accepted defect becomes a new bounded logical whole (or a correction inside the currently open one) with its own allowlist; frozen-slice rule: corrections must not redesign accepted visual behavior (ADR-0078, ADR-0077 Edit chrome) — fix the defect, not the design.
5. **Known-good baseline:** the positive-confirmation matrix in §6.1 is the regression yardstick — a correction that regresses any row (capability matrix, fail-closed allowlist, audience policy, publication chain, cookie-free downloaders, triple-gated automatic analysis, narrow sudo bridge, ADR-0060 helper match, loopback-first, `/srv/media` read-only) is rejected regardless of the defect fix.

---

7. **Deviations, risks, missing evidence:**
   - Prompt path `src/framenest/adapters/api/static/web/` corrected to `src/framenest/adapters/api/web/`; `server.py` is at `src/framenest/server.py`, not under `adapters/api/`. No other location drift.
   - OQ-1: runbook `docs/UBUNTU_NUC_DEPLOYMENT.md:158-161,207-208` workstation-pull provisioning state is host-state not resolvable from the repository read-only; S1 must not touch those two lines until the Cooperator answers whether E3 launcher/sudoers/store provisioning happened on the NUC.
   - OQ-2 (Cooperator): B5 residual — document assumption (recommended) vs `openat` hardening.
   - OQ-3 (Cooperator): candidate 1 — drop runtime constraint (recommended; clears drift with zero migration) vs add migration 0034.
   - OQ-4 (Orchestrator): S3 workspace 422 handler status code — uniform 422 with the standard body (closest to FastAPI semantics) vs 400; recommend 422 to preserve retryability semantics; either is decision-complete for the slice.
   - All exploitability conclusions in §6.1–6.2 are capped at "plausible but unproven" (no dynamic reproduction authorized). No secrets, private media filenames, host identifiers, or private network values are included in this report.
   - No test execution was performed (none authorized for planning); suite names cited are inventory evidence, not run results.

8. **One smallest next step:** route the four open questions to the Cooperator (OQ-1 host-state, OQ-2 B5 disposition, OQ-3 constraint drop-vs-migration, OQ-4 422 status), then issue the S2 implementation prompt (fresh-worker-session) as the first authorized slice.

9. **Report justification:** new-evidence

10. **Authority-expiry statement:** planning authority expires at this terminal report. Implementation of any slice requires a separate explicit Orchestrator prompt with `Native planning mode: not-used`, exact baseline, and the per-slice allowlist above. No implementation, acceptance, publication, deployment, or closure is claimed or authorized by this report.
