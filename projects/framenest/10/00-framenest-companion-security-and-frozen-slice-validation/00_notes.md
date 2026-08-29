# Era 10 Whole Notes — `framenest-companion-security-and-frozen-slice-validation`

Handout: `00_handout_agent.md` (Agent Orchestrator profile; AP 7ef45da
profile-qualified convention).
Initialized at session open by the receiving Agent Orchestrator (do not trust
the handout's numbers — re-verify every gate read-only first and record the
observed values in the table below).

## Identity

- Logical whole: `framenest-companion-security-and-frozen-slice-validation`
- Branch: `feat/x-meme-browser-companion`
- Expected starting HEAD (verify): `d8629e33a4755406f8bb1bfec565ac6a3f4fb67e`
  (published to origin 2026-08-28)
- Product freeze baseline: `472553cadcd3d4ca87a9792a2c306bd0afeea7c1` (era-10
  work defines its own bounded freeze/allowlist on top)
- AP pin: `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` (adopted and accepted in
  era 09)
- Cooperator: Michal (Slovak chat, masculine address; English artifacts and
  prompts; one-glance + one status mark; one decision per message)
- Profile: Agent Orchestrator default dispatch (P14 opt-out only on explicit
  request)

## Gates — re-verify at open

| Gate | Expected | Verified | Result |
| --- | --- | --- | --- |
| FrameNest HEAD | `d8629e33a4755406f8bb1bfec565ac6a3f4fb67e` | `d8629e33a4755406f8bb1bfec565ac6a3f4fb67e` | PASS |
| origin branch equality | same SHA | `d8629e33a4755406f8bb1bfec565ac6a3f4fb67e` | PASS |
| Porcelain | empty | 0 lines | PASS |
| `.ap` gitlink == `.ap` HEAD | `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` | gitlink `160000 7ef45da`, worktree `7ef45da`, submodule clean | PASS |
| Public AP main | `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` | `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` (git ls-remote; not advanced) | PASS |
| `./.ap/ap doctor` | PASS, stable | PASS; `OK resolved governing variant: stable` | PASS |
| Freeze ancestor | `472553c` ancestor of HEAD | `git merge-base --is-ancestor` OK | PASS |

## Objectives

Companion + Brave extension security (primary), backend infosec hardening,
frozen-slice defect triage and validation, defect-driven UI/UX fixes,
documentation drift editorial pass. NUC host hardening, NUC deployment
mutations, and AP pin advancement are out of scope unless separately granted.
Candidate worklist with evidence and positive confirmations lives in handout
Sections 6A–6E; sequencing in handout Section 7.

## Session Log

- **Open (2026-08-28, Agent Orchestrator):** All seven immediate gates
  re-verified read-only at HEAD `d8629e33a4755406f8bb1bfec565ac6a3f4fb67e` /
  AP pin `7ef45da` — all PASS (table above). Handout numbers trusted only
  after this independent verification. NAC ledger spot-check of
  `consumer-declared-execution-and-capability-route-binding` (accepted,
  retain-active) pending alongside required reading. Next: required reading
  (handout §3), then planning exchange `01_planning_00.md` (read-only Planner
  Worker) per handout §7.
- **Required reading complete (2026-08-28):** `.ap/AP.md` (full),
  `.ap/AP_ORCHESTRATOR.md`, `.ap/PROMPT_CONTRACTS.md` (full),
  `.ap/INTEGRATION.md`, `.ap/UPDATING.md`, `.ap/INTUITION.md`,
  `.ap/docs/adr/0022`; project: `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`,
  `SECURITY.md`, `SPEC.md` §§18/19/22/24/28 (§1 line 7 confirms the stale
  "personal production" framing listed in handout 6C), `docs/X_COMPANION.md`,
  `SERVER.md`, and ADR-0048/0053/0061/0064/0067/0068/0069/0070/0072/0073/0074/
  0075/0076/0077/0078/0079. NAC ledger verified: entry
  `consumer-declared-execution-and-capability-route-binding`, state `accepted`,
  `retain-active`, last revalidated against `7ef45da` — matches handout.
  Security-routing note: this whole changes security-relevant semantic owners
  (companion/extension trust surfaces, backend fail-closed behavior); per
  handout §7.2, implementation slices should prefer
  `Independent acceptance: required-separate-fresh-worker`. Planning Worker
  prompt staged as `01_planning_00.md` (coordinates: whole
  `framenest-companion-security-and-frozen-slice-validation`, session 01,
  exchange 01; fresh-worker-session; native planning mode not-used with
  explicit prompt-level read-only planning authority — dispatched-session
  clients lack a native planning mode).
- **Exchange 01 archived (2026-08-28):** `01_planning_00.md` +
  `01_report_00.md` — planning Worker (session 01, exchange 01,
  fresh-worker-session) returned **PASS**. Orchestrator spot-verification of
  material claims against HEAD `d8629e3` before acceptance: web shell at
  `src/framenest/adapters/api/web/` (not `static/web`) and
  `src/framenest/server.py` (not under `adapters/api/`) — both path
  corrections confirmed; five `companion_mutation=True` sites confirmed
  (`tailscale_ingress.py:415,553,563,571,580`); no `RequestValidationError`
  handler in `application.py` confirmed; `uq_x_post_claims_id` at
  `catalog_schema.py:1211` without 0028 counterpart confirmed; README.md:123
  Poetry 2.1.4 vs lock 2.3.2 vs deploy 2.4.1 drift confirmed. **Plan
  accepted** (advisory disposition). Key results: threat map found zero
  HTML-injection rendering paths (no `innerHTML` in `extension/` or web
  shell; `textContent`+`setAttribute`), origin-pinned postMessage both
  directions, allowlist fail-closed, capability matrix intact; A-findings
  A-F1 (workspace embeddability residual, document-only), A-F2 (unpacked
  extension position), A-F3 (`chrome.storage` shared-profile exposure,
  document-only); B1 (UDS socket-permission fail-closed startup assertion)
  confirmed as the highest-value fix; B2–B5 confirmed. Slice plan S1(docs,
  scoped acceptance) → S2(B1, fresh independent) → S3(B2+B4, fresh
  independent) → S4(B3+annotations, scoped) → S5a(hygiene, scoped) →
  S5b(constraint, fresh independent) → S6(Cooperator NUC refresh + rendered
  acceptance). **Orchestrator decision (OQ-4):** workspace validation errors
  use uniform **422** with the standard `{"error":{code,message}}` body
  (Worker recommendation; preserves retryability semantics); recorded.
  **Cooperator decisions pending, one per message:** OQ-1 (NUC
  workstation-pull provisioning host-state gating runbook
  `docs/UBUNTU_NUC_DEPLOYMENT.md:158-161,207-208` in S1), OQ-2 (B5 TOCTOU:
  document residual vs `openat` hardening; Worker recommends documenting),
  OQ-3 (`uq_x_post_claims_id`: drop runtime constraint vs migration 0034;
  Worker recommends dropping). Next: OQ-1 to Michal; S2 implementation
  dispatch (no open question) after Cooperator awareness.
- **Cooperator directive (2026-08-28, Michal):** "Nepreskakuj nic... Mas k
  dispozicii 85% svojho kontextu... Mas moju plnu doveru... zvolis tu
  najrozumnejsiu postupnost." — sequencing authority delegated; nothing
  skipped. OQ-1 remains genuinely open (host-state only the Cooperator knows);
  runbook lines excised from S1 per plan. Under delegated trust the
  Orchestrator resolved OQ-2 as DOCUMENT (B5 TOCTOU residual recorded in
  SECURITY.md; `openat` hardening stays available to a later whole) and OQ-3
  as DROP (runtime constraint converged to migrated truth; one-line revert),
  both recorded here with rationale.
- **Implementation chain (all commits on feat/x-meme-browser-companion,
  origin untouched — 10 commits ahead of origin):**
  - `c0f28ef` S1 docs-drift pass (session 02, implementation-PASS;
    scoped acceptance: Orchestrator full diff review + 119-test focused run;
    ADR-0032 annotation placed in Link cell because a test pins the Status
    cell substring — classified near-miss, recorded).
  - `6cdbe6f` S1b harness reconciliation (session 03, correction; stale
    EXPECTED_AP_COMMIT + README gitlink → 7ef45da; alias-payload test
    realigned to ADR-0077 with strengthened anti-leak assertions + negative
    control; README:565 + PRODUCT:93 NUC framing residuals).
  - session 04: fresh acceptance of 6cdbe6f — PASS (R1–R3 verified-closed;
    two non-defeating test-hardening ledger candidates recorded below).
  - session 05: S2 first attempt BLOCKED with decisive discovery: pinned
    uvicorn 0.49.0 hardcodes `os.chmod(uds, 0o666)` post-bind
    (uvicorn/server.py:156-167) — the documented systemd posture yields a
    world-connectable admin-trust socket today; static + dynamic evidence;
    no mutation, probe reverted. Orchestrator decision: post-bind owner-only
    tighten + assert (route (a)).
  - `53e6448` S2-revised (session 06): `UdsProvenanceVerifyingServer`
    tightens bound UDS socket to 0600 then asserts S_ISSOCK/no group-other
    bits/euid ownership, fail-closed CRITICAL exit before serving; both UDS
    modes; documented-posture dynamic regression test; SECURITY.md invariant
    + honest residuals (microsecond bind window; asyncio one-iteration
    transport-level accept possibility; RuntimeDirectory contract out of
    scope). 116 tests green.
  - session 07: fresh acceptance of 53e6448 — PASS (R1–R5 verified-closed;
    independent uvicorn/CPython flow analysis confirmed no-request-read
    guarantee; ledger candidate: SECURITY.md main sentence over-broad).
  - `460b37b` S3 uniform error contract (session 08): workspace
    RequestValidationError → uniform 422 `{"error":{"code":"VALIDATION_FAILED",
    "message":"Request validation failed."}}` (OQ-4 = 422, static message, no
    caller-input echo, no-store, sanitized WARNING); public catch-all
    collapsed to uniform 404, enumerated branch byte-identical; SECURITY.md
    wording nit fixed. 313 tests green.
  - session 09: fresh acceptance of 460b37b — PASS (R1–R5 verified-closed;
    classified probe near-misses; /tmp/opencode scratch used and cleaned).
  - `ba54cfa` S4 static adapter messages (session 10): B3 sites replaced with
    identical static literals; typed `YouTubeAcquisitionInvalidCursorError`;
    MediaAnalysisRunId annotations. Two X sites intentionally left (multiple
    static literals per catch site — no discriminator); discovery: S3's
    contract broke `test_library_api` stale assertion outside S3's focused
    set (classified). Also found `companion_review.py:620` annotation ledger
    candidate.
  - `3acd06d` S4b (session 11, correction): four typed X discriminators
    (`XAcquisitionInvalidCursorError`, `XAcquisitionInvalidRequesterIdentityError`,
    `XAcquisitionNotRetryableError`, `XAcquisitionNoRetryableAssetsError`),
    byte-identical behavior, B3 complete for X; companion_review.py annotation;
    library test realigned to accepted 460b37b contract. 42 tests green.
  - session 12: fresh acceptance of 3acd06d — PASS (R1–R5 verified-closed;
    raiser inventory exhaustive; parent-version probe proves the stale test
    failed at parent). Ledger candidate: port-vs-adapter MediaId/
    MediaAnalysisRunId static-typing tension
    (application/ports/companion_review_repository.py:75,85).
  - `3b98b8c` S5a hygiene (session 13): dead `_QUALIFYING_DUPLICATE_CANONICAL_STATES`
    removed (repo-wide zero-reference verified); X_DUPLICATE_PENDING
    reachability rationale comments; B5 TOCTOU residual documented in
    SECURITY.md (OQ-2 = document). 68 tests green; scoped acceptance.
  - `c0ab08f` S5b (session 14): dropped runtime-only
    `uq_x_post_claims_id` (OQ-3 = drop); new runtime-vs-migrated convergence
    test; schema head stays 0033. 33 tests green.
  - session 15: fresh acceptance of c0ab08f — PASS (R1–R5 verified-closed;
    all 33 alembic versions grepped; convergence-test failure modes reasoned).
    Ledger candidates: stale test name `test_head_is_0030`; convergence test
    binds named non-FK constraints only (indexes/FK topology unbound).
  - `2e39c4d` S5c (session 16, correction): three stale test realignments —
    test_media_analysis_api + test_media_import_api 422-shape assertions →
    accepted 460b37b contract; test_worker_execution_contract ledger test →
    accepted/retain-active truth (stale since era-09 85028f7, pre-baseline).
    33 tests green.
  - session 17: fresh acceptance of 2e39c4d — PASS (R1–R4 verified-closed;
    every ledger assertion byte-checked; parent-version failure provability
    verified).
  - Full-suite gate at c0ab08f: 3354 passed / 3 failed → all three
    classified (two S3-induced stale 422 assertions, one era-09 ledger stale
    test) → corrected by S5c.
  - `22352c9` S5d (session 18, correction): 7 stale movie-identification JS
    contract tests realigned to current editor surfaces (durable panel →
    ADR-0077 per-field strips; `renderMetadataDurableAnalysis` →
    `renderMetadataSuggestionStrips`); anti-save/PUT/concatenation intents
    preserved and strengthened; hard-stop check not triggered (no protected
    property lost). JS gates: file 8/8, glob 187/187.
  - session 19: fresh acceptance of 22352c9 — PASS (R1–R5 verified-closed;
    per-binding existence checks, production byte-identity via cmp,
    disposition of all 12 removed assertions recorded).
- **Final gates (2026-08-28):** full Python suite at HEAD `22352c9` → **3357
  passed, 0 failed, 8 skipped** (9:31); JS glob → **187 passed, 0 failed**;
  `ap project check` PASS; porcelain empty; 10 commits ahead of origin
  (unpublished). OQ-1 remains the only open Cooperator question.
- **Publication (2026-08-28, explicit Cooperator grant):** Michal granted
  the publication grant ("udeľujesť publikčný grant"). Executed: non-force
  push `d8629e3..22352c9` to `origin/feat/x-meme-browser-companion`; then —
  recorded as a mechanical precondition of the approved NUC refresh —
  fast-forward `origin/main` `d8629e3..22352c9` (same 10 commits, no new
  content; `deploy/ubuntu/framenest_release.py:544-548` hard-requires
  `public main == release SHA`, and main had tracked the branch 1:1). Both
  refs verified `22352c9e70737cfebe4de2c693fefc8ce55ba98b`. Schema head
  remains `0033` → no `migration-required` continuation expected on the NUC
  refresh. Next phase (Cooperator-led): Michal tests the shipped slice
  step-by-step on the refreshed NUC with the Brave companion over Tailscale,
  proposes small UI/UX refinements, reports desired details; the Orchestrator
  assists with questions and triage (work area C intake route from the
  accepted plan: concrete defect vs aesthetic reopen vs security observation
  vs out-of-scope ledger candidate). After his testing round he receives an
  expert restoration/dispatch prompt for a fresh Agent Orchestrator that
  will orchestrate Workers implementing his confirmed refinements.
- **Cooperator testing phase (opened 2026-08-28):** per Michal's directive,
  during his step-by-step testing the Orchestrator stays read-only: no
  Workers dispatched for small refinements, no direct mutation; findings are
  triaged (concrete defect / aesthetic refinement / security observation /
  out-of-scope) and accumulated in the confirmed-refinements ledger below,
  which becomes the input for the expert prompt for a fresh Agent
  Orchestrator (that Orchestrator will run ONE Planner Worker first, then
  batch implementation; Michal confirms each refinement). Only a finding
  that fully blocks his testing would trigger a bounded correction proposal,
  and only with his explicit approval.
- **NUC deployment verified (2026-08-29, Cooperator readback):**
  `framenest-release status` → `active_release: 22352c9e70737cfebe4de2c693fefc8ce55ba98b`,
  `service_active: active`, `database_revision: 0033` (same-schema update,
  no migration-required), `backup_restore_readiness: ready`. Full chain
  verified: local HEAD == origin/main == origin/branch == NUC active release
  == `22352c9`; local dev server starts clean (DB migrated to head, WARNING
  loop gone). Rendered UI/UX + Brave companion acceptance over Tailscale may
  proceed. Unified Cooperator wrapper `~/framenest.fish` created (private,
  NUC values only there; modes: dev/push/align/status/check/deploy/sha/logs/
  restart/migrate-status/migrate) — supersedes his scattered scripts; repo's
  `./framenest` development launcher unaffected.
- **Confirmed-refinements ledger (Cooperator-confirmed, for the fresh
  Orchestrator prompt):**
  1. (2026-08-29, triaged during testing-open; classification: pre-existing
     DX/environment issue, NOT a regression — none of the ten commits touched
     the coordinator/repository/schema paths, verified by
     `git log d8629e3..HEAD`) On a stale or locked local development database,
     server startup produces a repeating WARNING
     `media_analysis_discovery_failed` / `MEDIA_ANALYSIS_DISCOVERY_FAILED`
     (retryable, capped-delay retry loop) with no actionable hint. Root
     mechanics: `media_analysis_coordinator.py:302-333` tolerates only
     "no such table"/"does not exist" errors mentioning `media_analysis_runs`
     (`_missing_schema_error`, :408-417); any other repository error (e.g.
     "no such column" from a stale DB shape, or a stale lock) retries
     forever. Candidate refinements (Cooperator to confirm scope): (a) add
     "no such column"/schema-mismatch to the tolerated-missing-schema
     classification; (b) include "run `poetry run framenest-db migrate`" in
     the warning context; (c) optional startup migration-status check with a
     clear WARNING when the DB is behind head. Operator fix for the current
     state is the documented `poetry run framenest-db status` + `migrate`.
  2. (2026-08-29, Cooperator testing round 1) Companion history chrome:
     spontaneous reopen on scroll/refresh + open-by-default. FIXED SAME DAY
     under his explicit "fix now, then I re-test" order: commit `c4d0200`
     (session 20 correctly BLOCKED on the stale harness; session 21 landed
     the correction + harness realignment to ADR-0072 Decision 2, which
     already mandated collapsed-on-load) + fresh acceptance (session 23) PASS.
     Product rule going forward: history collapsed by default, toggle-only,
     refreshes never change the user's chosen state, no persistence.
  3. (2026-08-29, Cooperator testing round 1) AI suggestion tags strip:
     unmapped suggested tags were inert spans ("plain div"), could not be
     added. FIXED SAME DAY: commit `454f181` (session 22) — unmapped tags
     clickable for non-alias actors via the existing
     `createAndSelectMetadataTag` (creates canonical tag + adds to draft;
     draft chips keep ×; re-addable after removal), alias-mode (ordinary
     user) stays inert with honest hint; CSS affordance added; fresh
     acceptance (session 23) PASS. Product rule: every suggested tag
     click-to-add for actors with tag-creation authority.
  4. (2026-08-29, Cooperator testing round 1) Review apply: no defect — the
     Cooperator needed step-by-step testing instructions (provided in chat;
     admin-only flow over an analyzed X item).
  5. (2026-08-29, Cooperator testing round 1) Alias edit across actors: NOT a
     defect — per-actor overlay is the accepted ADR-0062/0077 contract
     (caller-private overlay keyed by `(media_id, login_key)`; each actor
     sees their own overlay over canonical; admin seeing the unedited
     canonical title after an ordinary user edited THEIR overlay is correct,
     and the cross-actor non-leakage is a security property). Explained to
     the Cooperator; no code change.
  6. (2026-08-29, Cooperator testing round 1) Settings toggle automatic
     analysis: PASS (including hidden for ordinary user).
  7. (2026-08-29, ledger candidate) `tests/metadata_alias_edit.test.js:128`
     test NAME stale in name only ("mapped suggested tags are buttons and
     unmapped tags are not") — assertions still pass; rename in a future
     test-hygiene batch.
  8. (2026-08-29, ledger candidate) alias-mode inert-span strip path has
     source-level coverage only (tests/metadata_alias_edit.test.js:128-135,
     outside the three JS gates); runtime assertion in a future test-hardening
     batch.
- **Publication 2 (2026-08-29, under the Cooperator's "fix now, then re-test"
  order):** pushed `22352c9..454f181` to origin branch + FF main (verified
  `454f181d8b011ef563ac13a28e8d894dbc497bc4`); NUC refresh to `454f181` is
  the Cooperator's next manual step (`~/framenest.fish deploy` + `status`).
- **Cooperator testing round 2 (2026-08-29) and era handover:** T1/T2/T3
  PASS (history fix verified rendered on the NUC → NUC confirmed serving
  454f181). FAILs reported: T4/T5 (tags click no-op on previously analyzed
  memes — remove/re-add also dead; Orchestrator suspicion recorded in the
  era-11 handout: silent early-return in `copySuggestionFieldToCurrent`
  when the tag is already in the draft, app.js:6816); GIF/animated preview
  never pauses (restarts from zero) while video pauses/resumes but flashes
  black on open — regression from the editor rework era; 🧠 shows "The AI
  suggestion provider response was invalid." with no progress indication;
  X video save fails with generic "Save to FrameNest failed" (first image
  save succeeded). NEW PRODUCT DIRECTIONS decided by the Cooperator: Edit
  always opens with the newest AI suggestion loaded (Load button
  superseded; dropdown onchange switches dynamically; applies to web AND
  extension review popup); 🧠 opens an empty Edit modal immediately with an
  eye-candy spinner while the model runs (design delegated to Orchestrator
  judgment); companion live-refresh + unread "active history" matching the
  badge (unread in history until opened; ordinary users get analyzed items
  as unread when admin approves analysis of their media; no duplicates
  between active and history views). STANDING REASONING POLICY (Cooperator
  directive): every Worker prompt declares a Reasoning recommendation
  matched to task risk (High for security/ambiguous/architectural; Medium
  only for routine bounded corrections with complete evidence; Low trivial
  only); Orchestrator reasons at full strength; if the dispatch environment
  cannot vary reasoning effort, the recommendation governs discipline and
  copy-paste routing, and a confirmed hard capability limit is recorded as
  an AP upgrade observation. **Era-10 handover:** expert handout written to
  `/home/agile/meta/projects/framenest/11/00-framenest-companion-unread-inbox-and-editor-suggestion-ux/00_handout_agent.md`
  (new whole: `framenest-companion-unread-inbox-and-editor-suggestion-ux`);
  era-10 remains logically open on the Cooperator's side (his re-testing
  continues in era 11); this Orchestrator's active role ends here.
- **Meta trace commit verified (2026-08-28):** Michal's manual commits
  `e8bdbe3` + `3eb5671` ("docs: add planning and report files for
  framenest-companion-security-and-frozen-slice-validation") contain all 26
  trace files (handout, notes, planning pair, 18 report companions, 4
  decision-bearing prompt companions); `git status --porcelain` in the meta
  repository is clean — nothing missing, nothing untracked, no error found.
- **Public verification at testing open:** local HEAD == origin/main ==
  origin/feat/x-meme-browser-companion ==
  `22352c9e70737cfebe4de2c693fefc8ce55ba98b` (fresh `git ls-remote`); AP pin
  local `.ap` HEAD == public AP main == `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`.
  NUC runtime state is NOT verifiable from this session (no NUC authority
  granted here) — the authoritative readback is Michal's
  `deploy/ubuntu/framenest-release status`.
- **Ledger candidates accumulated (non-authorizing, for future wholes):**
  workspace anti-leak test fixture binds empty attribution lists (test
  hardening); reverse-direction workspace overlay check analogue absent;
  port-vs-adapter run-id static-typing tension (ports/companion_review_repository.py:75,85);
  stale test name `test_head_is_0030`; convergence test binds named non-FK
  constraints only; `applyMovieIdentificationToMetadataWorkspace` /
  `movieSuggestionFromResult` currently lack UI call sites in app.js (movies
  excluded via 409 movieExcluded — flagged for product awareness, behavior
  per ADR-0077).
- **Trace archival (complete, 2026-08-28):** era-09 phase-sequence grammar.
  Archived IN FULL: `01_planning_00.md` + `01_report_00.md`; report
  companions `02_report_00.md` … `19_report_00.md` for every exchange
  (session 05's BLOCKED outcome archived as a terminal implementation-phase
  report); verbatim prompt companions for the four decision-bearing
  exchanges: `06_implementation_00.md` (route-(a) tighten+assert decision),
  `08_implementation_00.md` (OQ-4 = uniform 422; B4 collapse-to-404),
  `13_implementation_00.md` (OQ-2 = document residual), `14_implementation_00.md`
  (OQ-3 = drop constraint). CLASSIFIED GAP, not silent: full prompt texts for
  sessions 02, 03, 04, 05, 07, 09, 10, 11, 12, 15, 16, 17, 18, 19 are
  retained in the Orchestrator session transcript only (context-budget
  triage); each exchange's authority state, allowlist, and outcome is fully
  recoverable from its archived report companion plus the entries above.
  Companion integrity verified: every report companion commences with
  `### Report for ORCHESTRATOR_CHAT` and none duplicates its prompt. Michal
  commits the trace directory manually per the working agreement.
