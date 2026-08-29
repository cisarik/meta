# Restoration Handout — Agent Orchestrator

Era: 11 (FrameNest meta tracking)
Logical whole: `framenest-companion-unread-inbox-and-editor-suggestion-ux`
Trace directory: `/home/agile/meta/projects/framenest/11/00-framenest-companion-unread-inbox-and-editor-suggestion-ux/`
Generated: 2026-08-29 by the closing Agent Orchestrator of era 10
(`framenest-companion-security-and-frozen-slice-validation`).

Begin read-only. Re-verify every immediate gate yourself before trusting any
value in this handout, and initialize `00_notes.md` beside this handout at
open (AP 7ef45da convention: handout + `00_notes.md`, then
`01_planning_00.md` + `01_report_00.md` per exchange, prompt/report pairs
archived together after the report exists).

## 1. What This Whole Is

Era 10 shipped the companion/infosec security pass, documentation-drift
repair, and two Cooperator-ordered UX corrections, all published and
accepted. The Cooperator then ran two rendered testing rounds. Round 1
passed the security and chrome fixes but exposed product-UX direction; round
2 returned concrete FAILs: a tags-click no-op on previously analyzed items,
a GIF/animated-preview pause regression, a black flash on video open, an
opaque AI-provider failure ("The AI suggestion provider response was
invalid.") with no progress indication, and a generic "Save to FrameNest
failed" on X video posts. In parallel the Cooperator set two product
directions: (a) the Edit surface must ALWAYS open with the newest AI
suggestion loaded (Load button superseded; dropdown switches dynamically;
🧠 opens an empty Edit modal with a spinner while the model runs), and (b)
the companion side panel becomes a live unread-inbox surface (auto-refresh,
visible "active history" of unread analyzed items matching the badge,
unread items in history until opened, ordinary users receive analyzed items
as unread when an administrator approves analysis of their media).

This whole makes those two product directions the primary objective and
folds in the regression fixes and honest-failure UX. Recommended profile:
**Agent Orchestrator** (default dispatch), with ONE Planner Worker first
(Cooperator directive: never spawn a Worker per small item — batch).

## 2. Immediate Gates — re-verify at open (read-only)

```text
Canonical repository: /home/agile/Projects/framenest
Branch: feat/x-meme-browser-companion
Expected local HEAD: 454f181d8b011ef563ac13a28e8d894dbc497bc4
Expected origin/feat/x-meme-browser-companion == origin/main: 454f181d8b011ef563ac13a28e8d894dbc497bc4 (published 2026-08-29)
Expected porcelain: empty
AP pin: .ap gitlink == .ap HEAD == 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26; public AP main equal (git ls-remote; if advanced, pin adoption is a separate whole)
Doctor: ./.ap/ap doctor PASS with "OK resolved governing variant: stable"
NUC readback (Cooperator-owned, via his private ~/framenest.fish): active_release expected 454f181…, service active, database_revision 0033, backup_restore_readiness ready
Product freeze commit: 472553cadcd3d4ca87a9792a2c306bd0afeea7c1 (ancestor of HEAD)
NAC ledger: docs/AP_UPGRADE_OBSERVATIONS.md — single entry consumer-declared-execution-and-capability-route-binding, accepted, retain-active (unchanged through era 10)
```

Era-10 shipped commits (all accepted; do not regress): `c0f28ef` docs drift,
`6cdbe6f` harness reconciliation (AP pin + ADR-0077 alias display),
`53e6448` UDS 0600 tighten + fail-closed provenance assertion,
`460b37b` uniform 422/404 error contract, `ba54cfa` + `3acd06d` static
adapter messages + typed exceptions, `3b98b8c` hygiene + TOCTOU residual,
`c0ab08f` dropped redundant `uq_x_post_claims_id` (runtime-vs-migration
convergence test added), `2e39c4d` stale-test realignments, `22352c9` movie
JS test realignment, `c4d0200` history collapsed-by-default + toggle-only
(+ invariant test), `454f181` AI suggestion tags click-to-add.

## 3. Required Reading

- `AGENTS.md` (including the Cooperator Presentation Profile), `.ap/AP.md`,
  `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md`,
  `.ap/INTEGRATION.md`, `.ap/UPDATING.md`, `.ap/INTUITION.md`,
  `.ap/docs/adr/0022`
- `docs/WORKER_EXECUTION_CONTRACT.md`
- `SECURITY.md`, `SPEC.md` §§18/19/22/24/28, `SERVER.md`, `PRODUCT.md`,
  `docs/X_COMPANION.md`
- ADRs: 0048, 0053, 0061, 0062, 0064, 0067–0070, 0072–0079 (especially
  0072/0073/0076 companion chrome and 0077/0078 editor suggestion UX)
- Era-10 trace: `/home/agile/meta/projects/framenest/10/00-framenest-companion-security-and-frozen-slice-validation/00_notes.md`
  (full ledger of shipped work, findings, decisions)

## 4. Cooperator Working Agreement (standing, from the Cooperator)

- Michal is the Cooperator; chat in Slovak, masculine address, feminine
  Orchestrator self-reference; one-glance status block (≤5 lines) then
  exactly one status mark; one decision per message.
- **Testing style (explicit Cooperator requirement):** the Orchestrator
  writes step-by-step test instructions (numbered, one behavior per step,
  concrete expected result); the Cooperator executes them on the NUC (Brave
  companion over Tailscale, or local web at 127.0.0.1:8000) and answers with
  PASS / FAIL / PARTIAL per step plus observations. The Orchestrator never
  assumes; it asks clarifying questions and triages every report (concrete
  defect / aesthetic refinement / security observation / out-of-scope
  ledger candidate) into the confirmed-refinements ledger in `00_notes.md`.
- **Token economy (explicit Cooperator directive):** never one Worker per
  small item. ONE Planner Worker produces the batched plan; implementation
  proceeds in bounded slices; small confirmed corrections may be dispatched
  in-session as Bounded Correction Workers; everything else accumulates for
  batched implementation. The Cooperator confirms each refinement.
- **Reasoning policy (explicit Cooperator directive, era 11):** every
  Worker prompt declares a `Reasoning recommendation` matched to task risk:
  High for security, ambiguity, architecture, or multi-surface work; Medium
  only for routine bounded corrections with complete verified evidence;
  Low only for trivial mechanical steps. The Orchestrator itself reasons at
  full strength for planning, triage, and acceptance. In dispatch mode the
  Orchestrator uses its own judgment per dispatch; if the environment cannot
  vary reasoning effort per dispatched session, the declared recommendation
  still governs prompt discipline and copy-paste routing (the Cooperator
  mediates model choice there). If a hard capability limit is confirmed,
  record it as an AP upgrade observation in
  `docs/AP_UPGRADE_OBSERVATIONS.md` and route genuinely High tasks through
  Cooperator-mediated sessions. Do not silently downgrade.
- Publication requires an explicit per-task Cooperator grant. Standing
  precedent: a "fix now, then I re-test" order covers the publish + NUC
  refresh needed for the re-test — record it in notes when used.
- NUC refresh and rendered acceptance are Michal's, via his private
  `~/framenest.fish` (modes: dev/push/align/status/check/deploy/sha/logs/
  restart/migrate-status/migrate). That file is private (NUC SSH values);
  never copy it into the repository; never improvise its commands.
- Meta trace commits are manual by Michal; Orchestrators and Workers write
  trace files but never commit the meta repository.

## 5. Objectives (Cooperator-approved direction)

1. **Regression diagnosis and fixes first** (worklist §6A) — the Cooperator
   expects previously working behavior restored ("rozbité funkcionality
   treba fixnuť").
2. **Editor suggestion UX batch** (§6B) — Edit always opens with the newest
   suggestion loaded; Load button removed; dropdown onchange switches
   dynamically; 🧠 opens an empty Edit modal with an eye-candy spinner while
   the model runs (visual design delegated to the Orchestrator's judgment;
   keep it consistent with the existing design tokens).
3. **Companion unread-inbox evolution** (§6C) — live refresh, visible
   unread "active history" matching the badge, unread-in-history-until-
   opened, ordinary-user analyzed items on admin approval. This is
   first-class product scope: plan it (ONE Planner Worker), do not hide it
   inside small fixes, and record the chrome-semantics decisions against
   ADR-0072/0073/0076 (living-docs updates in the same slices; ask the
   Cooperator whether an ADR is warranted).
4. **Honest failure UX** for provider errors and unsupported saves (§6A3–4).
5. **Documentation** living updates in the same slices as behavior changes
   (X_COMPANION.md, README/PRODUCT where user-visible).
6. Out of scope unless separately granted: NUC host hardening, deployment
   mutations beyond the routine entry point, AP pin movement, router/funnel
   exposure (always forbidden), provider cost changes.

## 6. Candidate Worklist (evidence-backed; re-verify before planning)

### 6A. Regression fixes and honest failures (do first)

1. **Tags click no-op on previously analyzed items** (T4 FAIL, round 2).
   Web Edit dialog. Era-10 Orchestrator suspicion (verify first):
   `copySuggestionFieldToCurrent` (`src/framenest/adapters/api/web/app.js:6808-6829`)
   silently early-returns when the tag is already in
   `metadataWorkspace.current.tagKeys` (line ~6816) — previously analyzed
   memes usually already carry the suggested tags (e.g. the X seed tag), so
   clicks look dead with zero feedback. Also verify the unmapped path
   shipped in `454f181` (`createAndSelectMetadataTag`, app.js:7722, gated by
   `identityUsesCanonicalMetadataWrite()`) under real NUC identity, and the
   alias-mode inert path. Fix direction: visible already-added affordance
   on the strip chip + end-to-end verification of both paths. T5 FAIL
   (remove-and-re-add) likely shares this root.
2. **GIF/animated preview pause regression** (round 2: "gif sa nepozastavuje,
   vždy ide od začiatku"). Animated-image previews restart from zero on
   click instead of pause/resume. Video: opens with a black flash but
   position is remembered and pause→resume works. Anchor:
   `src/framenest/adapters/api/web/app.js` animated preview logic (~4981-5183,
   "Play animated preview" / "Show static preview" toggle at 5148-5183).
   The Cooperator states this worked before the editor rework (commits
   `6b957be`, `365426a`, `02f6d61` era) — regression-hunt there first.
   Expected behavior: click toggles pause/resume for GIF and video, position
   remembered, no black flash on open, hover cursor stays default (not
   "hand") on video previews (minor CSS).
3. **"The AI suggestion provider response was invalid."** on 🧠 (round 2).
   Anchor: `src/framenest/adapters/api/media_suggestion_api.py:68`
   (`AI_PROVIDER_INVALID_RESPONSE_MESSAGE`); transport layer
   `src/framenest/infrastructure/ai/transport.py:16`. Diagnose: transient
   provider response vs parsing/validation bug vs capability/env issue on
   the NUC. Fix honestly: retryable classification, actionable message, and
   the progress UX from §6B3 so failures land inside the modal, not as a
   dead under-item text.
4. **X video save → "Save to FrameNest failed"** (round 2; the FIRST image
   save succeeded). X acquisition is still-image only (ADR-0061/0064:
   jpg/png, WebP rejected); a video post save likely fails downstream.
   Anchor: `extension/shared/messages.js:574-612`. Fix direction: detect
   unsupported media kinds in the content script and disable/hide the save
   affordance with an explanation instead of a generic failure toast.
   Verify against the server-side error classification too.

### 6B. Editor suggestion UX batch (Cooperator-decided 2026-08-29)

1. Edit modal ALWAYS opens with the LATEST AI suggestion pre-loaded and
   revealed — web workspace AND the extension review popup. Today only a
   fresh in-session analysis auto-reveals (`presentInSessionSuggestion`,
   app.js:6846-6855); history items sit behind Load
   (`refreshMetadataSuggestionList` + `handleLoadDurableAiSuggestion`).
2. Remove the Load button (superseded by the Cooperator). Keep the dropdown;
   `onchange` immediately switches the loaded suggestion (dynamic load, no
   separate confirm step).
3. 🧠 (Gallery card and editor): open the Edit modal IMMEDIATELY in an
   empty/loading state with an eye-candy spinner making clear the AI model
   is being called; on completion load the suggestion in place (ready for
   Save); on failure show honest status inside the modal. No progress
   indication exists today ("nikde nevidím žiadny progress bar ani loader").
4. Preserve: text-safe rendering; suggestions never write canonical truth
   until Save; capability gates; the ADR-0077 alias-mode restrictions
   (ordinary users: suggestion strips read-only toward canonical tags; tag
   creation only for `metadata.canonical.write`).

### 6C. Companion unread-inbox evolution (product direction; largest item)

1. Live side-panel refresh when saves/analyses happen (no manual reopen;
   the Cooperator: "najlepšie UX by bolo keby sa sidebar aktualizoval
   automaticky").
2. Admin: newly analyzed memes appear immediately under the toolbar as a
   visible "active history" (unread) section matching the badge count;
   unread items also appear in history (unread affordance) until opened;
   opening clears unread (existing review-opened route). The Cooperator's
   anti-duplication principle: active = the unread slice of history, ONE
   conceptual list — no duplicate rows.
3. Ordinary users: analyzed items appear as unread (badge count) when an
   administrator approves analysis of their media through the admin
   "Manage media" approval flow; they do not get automatic analysis.
4. Chrome semantics touch ADR-0072/0073/0076 — update living docs in the
   same slices; propose an ADR to the Cooperator if the change is
   contract-level (his call).
5. Suggested backend shape to evaluate (not decided): the existing
   review-inbox routes already model unread for admins; extending the
   unread/active semantics to ordinary users needs a capability-matrix
   check against ADR-0074/0077 boundaries before any implementation.

## 7. Positive confirmations to protect (do not regress)

The full era-10 matrix: companion capability matrix (admin-only inbox,
owner-fenced opened, apply double-gated, audit fail-closed); extension
allowlist fail-closed; UDS 0600 tighten + fail-closed startup assertion
(`UdsProvenanceVerifyingServer`); uniform 422/404 sanitized contracts; static
adapter messages + typed exceptions; publication chain crash-safety;
cookie-free downloaders; triple-gated automatic analysis; loopback-first;
`/srv/media` read-only; five `companion_mutation` routes; history
collapsed-by-default + toggle-only (invariant test in
`tests/companion_review_extension.test.js`); tags strip click-to-add with
authority gating; text-safe rendering (no innerHTML anywhere).

## 8. Open Questions Carried From Era 10

- OQ-1 (still open): whether workstation-pull provisioning (E3 launcher,
  sudo bridge, backup store) exists on the NUC — gates two runbook passages
  (`docs/UBUNTU_NUC_DEPLOYMENT.md:158-161,207-208`). Ask Michal when
  touching the runbook; do not block anything else on it.
- Ledger candidates (era-10 notes, items 7-8 and the earlier list): stale
  test name `test_head_is_0030`; port-vs-adapter run-id typing tension
  (`application/ports/companion_review_repository.py:75,85`);
  `media_analysis_discovery_failed` DX (tolerate schema-mismatch, add
  "run framenest-db migrate" hint, optional startup migration-status
  warning); stale name in `tests/metadata_alias_edit.test.js:128`; alias-mode
  inert-strip path needs a runtime assertion.

## 9. Recommended Sequencing

1. Open gates, `00_notes.md`, then a READ-ONLY diagnosis sprint for §6A1-4
   (Orchestrator-direct or one diagnostic Worker; reproduce conditions
   read-only; classify each: regression vs pre-existing vs environment).
2. Bounded regression fixes with fresh acceptance where behavior contracts
   change; Michal re-tests each fix batch (publish → NUC refresh →
   step-by-step PASS/FAIL).
3. ONE Planner Worker: editor-UX batch (§6B) + companion unread-inbox
   (§6C) threat/UX map against current code, slicing, acceptance strategy.
4. Implementation in bounded slices; docs in-slice; independent acceptance
   for slices that change documented contracts or companion chrome
   semantics.
5. Closeout per AP: ledger reconciliation, Cooperator-informed closure,
   no Worker-emitted closure.

## 10. Boundary Constants (never reopen by side effect)

Loopback-first backends; Tailscale-only remote access; no Funnel; no router
port forwarding; Tailscale membership is not application authority; no
provider secrets to ordinary clients; `/srv/media` read-only to the service;
no NUC host mutation without explicit bounded grant; no push without
per-task grant (standing "fix now, re-test" precedent documented in era-10
notes); secrets never committed; private media, credentials, host
identifiers never exposed in artifacts or reports; product boundaries in
`AGENTS.md` govern what may be claimed as shipped.

## 11. Trace Conventions

```text
Trace directory: this directory (private, local-only; Michal commits manually)
Prompt/report pairs: 01_planning_00.md + 01_report_00.md, 02_implementation_00.md + 02_report_00.md, ... (fresh session per phase; exchange suffix _00)
Notes: 00_notes.md is the living whole ledger of verified state, decisions, and the confirmed-refinements ledger (keep that section alive — it is the Cooperator's product-direction record)
Closeout: final Orchestrator-authored closure file plus a closing 00_notes.md entry; no Worker ever emits project closure
Delivery: Agent Orchestrator default dispatch; copy-paste only on explicit P14 opt-out; download prompt filename pattern NN_<phase>_00.md; archival wait-for-report
```

## 12. Session-Close Obligations

Reconcile the upgrade ledger (only genuine AP-upgrade observations about the
canonical AP repo — product findings are NOT ledger material; the
reasoning-capability limit, if confirmed, IS one), obtain Cooperator-informed
closure, clean temporary probe state, and record final HEAD/pin in
`00_notes.md`.
