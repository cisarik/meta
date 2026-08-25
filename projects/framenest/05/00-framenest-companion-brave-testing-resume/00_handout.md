# FrameNest restoration handout — next Agent Orchestrator era

Issued: 2026-08-25, by the outgoing fresh Agent Orchestrator of meta project
`04/00-framenest-public-published-surface-and-tailscale-workspace`, at the
explicit direction of the Cooperator (Michal). This handout follows the
restoration-prompt inventory of the 04/00 handout Sections 16–17. Read it
completely before any Worker prompt.

Mission of your era, verbatim intent from the Cooperator: **unfreeze the
parked FrameNest companion Brave extension acceptance testing** (the 03/10
backlog), and resolve any companion-related infosec findings that surface,
professionally and under Analytic Programming. The VPS/public-net deployment
direction is **FROZEN** — do not touch it without a new explicit Cooperator
instruction (see §6).

## 1. Canonical state at rotation (verify at start; read-only)

- Canonical checkout: `/home/agile/Projects/framenest`
- Branch: `feat/x-meme-browser-companion`
- Local HEAD at rotation: `c3e9ac7617a07b6a8e60c911a0b78b25ced71665`
- Public main: `0fe2b32e0fed2ecaccf1a481d99be5657d42b77b`
  (`git ls-remote https://github.com/cisarik/framenest.git refs/heads/main`,
  credential-free)
- The whole 04/00 stack sits UNPUBLISHED on top of older unpublished work;
  local branch is many commits ahead of its tracking branch. Do not treat
  local HEAD as live NUC.
- Production NUC still serves the older accepted release (`aec2f009…`,
  schema `0028`) per `docs/ACCEPTANCE_DUAL_AUDIENCE.md` Part B honesty
  banner — nothing from this era is deployed.
- AP pin: gitlink and checkout `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- Schema head: `0033` (`media_analysis_proposals`)
- No active Worker session anywhere; all prior authorities expired at their
  terminal reports.

## 2. What the parked 04/00 era shipped (context, not authority)

Nine commits `37da5f2..c3e9ac7` implemented accepted **ADR-0074**
(dual-audience public published surface + Tailscale workspace):

| Commit | Content |
|---|---|
| `0008ca5`,`6aac705` | ADR-0074 proposed → Accepted with Cooperator clarifications |
| `ffef457`,`dd26782` | administrator publication became sole write incl. unpublish on the same PUT; companion Apply can never publish again |
| `95f514b` | local-only `public_published_uds` reader (allowlist app, read-only engine, uniform sanitized 404) |
| `5b99575` | contributor-scoped workspace media + admin contributor filter |
| `da06109` | durable ordinary-user analysis proposals (migration 0033) |
| `f59f401` | audited admin team-alias reads (dual capability gate) |
| `bcf5ec1`→`3a21405` | independent-audit remediation (tcp loopback guard F-2, uniform 404 validation handler F-1, marker assert F-4, sanitized logs F-5, URI encoding F-6, per-user hourly proposal rate limit F-3 disposition B) |
| `be35922` | `docs/INFOSEC.md` manual + three bash operator diagnostics |
| `c3e9ac7` | repository acceptance guide + script polish |

Independent security audit verdict: **yes-with-conditions**; all conditions
closed except C3 (proxy-owned transport limits) which belongs to the frozen
TLS/preflight era. Companion-specific audit result: **no companion defect**;
the CSRF/mutation-proof/audit-before-execute machinery the companion relies
on held under adversarial review (verified-claims items 12–13).

## 3. Status of the 04/00 logical whole: PARKED, not closed

- Code/audit/docs are complete at `c3e9ac7`.
- The Cooperator has NOT yet executed the acceptance guide
  (`docs/ACCEPTANCE_DUAL_AUDIENCE.md`; Meta copy `13_report_00.md`).
  His execution results are the pending UX/security acceptance evidence.
- Deterministic closure remains possible only after he reports Part A/B
  outcomes. Until then the whole is parked by his explicit decision.
- If his acceptance run finds defects, route fixes as bounded infosec/
  product slices exactly like session 05 did (fresh or continued Worker,
  allowlist, canonical `./.ap/ap exec` test route).

## 4. Your era's mission: resume companion Brave testing (unpark 03/10)

- Authoritative backlog:
  `/home/agile/meta/projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/COMPANION_PARKED_BRAVE_TEST_BACKLOG.md`
  — read it completely before planning.
- Per ADR-0074 rollout rule 8: unpark happens only on the Cooperator's
  explicit request (he has given it for your era) and testing must run
  against an origin+SHA that actually contains what the backlog tests.
- Practical implication: production NUC runs schema `0028`; if backlog
  scenarios need newer server behavior, the path is the routine immutable
  release update ONLY: `deploy/ubuntu/framenest-release status`, then
  `framenest-release check --release <40-hex>`, then explicit separate
  deploy authority per step (AGENTS.md "NUC Routine Release Update").
  Never improvise deployment commands. Publication (push to public main)
  of the current unpublished stack requires exact Cooperator grant first.
- Companion behavior invariants you must preserve while testing: Apply
  writes metadata only and never publishes (ADR-0074); movie exclusion
  (ADR-0070); extension-origin rules per SECURITY.md; auto-analysis flag
  stays OFF in tracked files (enablement is exclusively a Cooperator NUC
  EnvironmentFile operation).
- If testing surfaces infosec gaps: route them through the proven pattern
  (independent audit framing → Orchestrator triage → bounded remediation
  Worker → focused tests via `./.ap/ap exec`) instead of ad-hoc fixes.

## 5. Parked-objects ledger you inherit

1. **04/00 Part A/B acceptance** — awaiting Michal's guide execution
   (Part B conditional on a release actually shipping this stack).
2. **Companion Brave testing (03/10)** — YOUR primary objective (§4).
3. **Companion public-origin reconnect** (ADR-0074 rollout 7) — parked until
   the public origin is actually deployed somewhere real.
4. **VPS/TLS/public-net deployment** — FROZEN by Cooperator decision
   (2026-08-25). When ever resumed: MUST reconnect with then-current
   deployment documentation (`docs/UBUNTU_NUC_DEPLOYMENT.md`, ADR-0060
   `framenest-release` contract, `docs/INFOSEC.md` §4 revalidated against
   that era's code), follow the preflight shape recorded in
   `docs/ACCEPTANCE_DUAL_AUDIENCE.md` Deployment-Freeze Annex, and take
   Cooperator operational authorization for every host mutation.
5. **INFOSEC R3** (old parked list) — remains parked unless Michal folds it
   in explicitly.
6. **cisarik/ap `FUTURE.md` idea** (white-hat auditor Worker framing as AP
   protocol brainstorming) — candidate observation only; any `.ap/` change
   needs its own explicit AP update task.
7. **Analysis-proposal dismiss/complete lifecycle** — statuses exist
   (`open/dismissed/completed`), no routes yet; future small whole.
8. **Auto-analysis enablement** — designed (ADR-0066), flag off in git;
   live enablement is Michal's NUC ops decision, never a Worker action.

## 6. Standing rules you must keep (unchanged)

- Loopback-first services; no router port-forwarding; Tailscale-only remote
  access until a superseding accepted decision exists; Funnel to the
  workspace socket forbidden.
- `/srv/media` read-only to the service; ordinary clients never receive
  provider secrets; premium gallery invariant intact.
- Communication with Michal: Slovak, masculine forms for him, feminine
  self-reference for the Orchestrator; repository artifacts professional
  English; Worker reports begin `### Report for ORCHESTRATOR_CHAT`;
  human command blocks `# [MacBook / fish]` / `# [NUC / bash]` ending with
  `#------------------------------------------------------`.
- Workers: Cursor/AppImage ambient Python forbidden; everything through
  `./.ap/ap project check` / `./.ap/ap exec` with exact `--baseline`; NUC
  SSH via the worker gate script; sudo lifecycle outside Workers.
- Git writes only with exact per-task grants; push/publication/deployment
  never implied by implementation authority.

## 7. Upgrade ledger (declared, unchanged)

Upgrade ledger: upgrade https://github.com/cisarik/ap.git
Ledger storage version: 1
Ledger path: docs/AP_UPGRADE_OBSERVATIONS.md

One untriaged non-authorizing entry exists
(`consumer-declared-execution-and-capability-route-binding`); two near-misses
this era (ambient python3 link enumeration; report SHA mis-transcription)
corroborate rather than extend it. Consider triage when appropriate.

## 8. Required reading before your first Worker prompt

In order: this handout; `/home/agile/Projects/framenest/AGENTS.md`;
`.ap/AP.md`; `.ap/AP_ORCHESTRATOR.md`; `.ap/PROMPT_CONTRACTS.md`;
`docs/WORKER_EXECUTION_CONTRACT.md`; `docs/adr/0074-…boundary.md`;
`docs/INFOSEC.md`; `docs/ACCEPTANCE_DUAL_AUDIENCE.md`; the 03/10 backlog
(§4 above); current `README.md`/`SECURITY.md`/`SERVER.md` status sections.

Meta trace folders:
- Outgoing era: `/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/`
  (handout, prompts `01_planning_00.md`…`14_freeze_prep_00.md`, reports,
  `08_orchestrator_notes.md` ledger — the authoritative narrative).
- Suggested trace folder for your era:
  create `/home/agile/meta/projects/framenest/05/<whole-slug>/` following
  the established file grammar (`NN_<phase>_XX.md` prompts, `NN_report_XX.md`
  reports, orchestrator notes ledger).

Start verification (all read-only): confirm §1 refs, worktree clean, AP pin
match, schema head, and that `COMPANION_PARKED_BRAVE_TEST_BACKLOG.md` opens.
Then plan your era with Plan Mode ON as usual.
