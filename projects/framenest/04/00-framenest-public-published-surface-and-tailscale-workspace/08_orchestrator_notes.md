# Orchestrator ledger — 04/00 framenest-public-published-surface-and-tailscale-workspace

Owner: current fresh Agent Orchestrator. Non-authorizing orchestration-planning
record under RF-19; task authority comes only from issued Worker prompts.

## Recorded Cooperator directions (2026-08-25, after planning acceptance)

### 1. End-of-whole closure support flow

At the end of this logical whole, before final closure:

1. Issue one fresh bounded Worker that generates **step-by-step human test
   instructions** for Michal so he can verify the activated surfaces himself
   (UX/security acceptance evidence collection; the Worker never closes the
   whole).
2. On that report plus full context, the Orchestrator performs deterministic
   closure only when handout Section 16 gates are satisfied.
3. Then generate the **new professional restoration prompt** for the next
   fresh Agent Orchestrator (handout Sections 16–17 inventory), including
   whether 03/10 remains parked.

### 2. Next-era direction: VPS deployment

Michal names VPS deployment as the strategic target for the next Orchestrator
era ("FrameNest worthy of VPS deploy"). Consistent with the accepted plan's
ingress ranking item 4 (VPS as long-term host for the same public
composition). Not authority inside this whole; becomes next-era objective via
the restoration prompt.

### 3. Infosec hardening after public matters

After the public-audience wholes ship, Michal wants a dedicated security
hardening track:

1. **Security Audit Planner** — independent fresh Worker, white-hat /
   senior-security-researcher framing, **Max reasoning explicitly selected by
   Michal** (overrides the default "no Max" for this future Worker only).
   Read-only audit planning/reconnaissance producing a findings-and-priorities
   report from which the Orchestrator routes fixes.
2. **Fresh Infosec Workers** — implement remediations and audit documentation
   under exact grants.
3. Candidate scope: public origin surface, ingress fail-closed behavior,
   header trust, cache policy, route allowlist completeness, alias privacy,
   publication gate integrity.

Not part of the current whole's scope. Parked INFOSEC R3 remains parked unless
Michal explicitly folds it in.

### 4. cisarik/ap brainstorming idea (candidate observation, non-authorizing)

Michal proposed recording an AP-side concept (white-hat security-audit Worker
framing / possible `FUTURE.md`) in the pinned AP repository. `.ap/` is
read-only during ordinary project work; any AP repository change requires a
separate explicit AP update task with its own authority. Recorded here as a
candidate observation to raise through a dedicated AP task; nothing was
written to `.ap/`.

### 5. Cooperator clarifications at ADR-0074 review (2026-08-25)

Michal reviewed the proposed ADR-0074 point-by-point, approved continuing,
and added these binding product clarifications (all consistent with the
accepted plan):

1. **Admin retains full companion suggestion visibility** — X-downloaded
   memes with new AI suggestions remain visible to the administrator
   (existing ADR-0067/0073 inbox/history; untouched by ADR-0074).
2. **Public audience covers all media kinds after Publish** — X memes,
   movies, YouTube videos, static images/gif/png/jpeg. Publish-by-admin
   means exactly "visible on the public origin".
3. **Every Tailscale user is a PRO user**: own gallery, own X downloads,
   own aliases (contributor-scoped workspace model).
4. **Admin is PRO-PRO**: publishes for the public and keeps own aliases.
5. **Administrator-owned automatic AI analysis is desired behavior**
   (extension shows newly analyzed items). Mapping: this is ADR-0066's
   designed administrator-owned X automatic generic analysis. The feature
   flag `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED` stays **off in git**
   (handout STOP); live enablement is a **Cooperator NUC EnvironmentFile
   operation**, a separate later ops step, never a Worker action.
6. **Public users in the extension see only public memes** (parked
   public-origin reconnect whole).

Acceptance record: Orchestrator treats ADR-0074 as **accepted with the
clarifications above**; the acceptance-materialization grant adjusts the
ADR's automatic-analysis assumption sentence to reference the ADR-0066
boundary precisely (in-git default off; enablement is a separate
Cooperator operational decision) instead of an unqualified "remains
disabled".

## Status log

- Exchange 01 (plan) delivered in chat; exchange 02 rendered
  `01_report_00.md`; Orchestrator **accepted** the plan (approval-gated).
- Implementation session 02 exchange 01 issued for the first bounded whole:
  ADR-0074 decision package (`02_implementation_00.md`).
- Session 02 exchange 01 reported implementation PASS: commit `0008ca5`
  (parent `37da5f2`), exactly `docs/adr/0074-…boundary.md` (new, Proposed)
  plus one `docs/adr/README.md` index row. Orchestrator independently
  verified commit shape, index row, and supersession targets against
  ADR-0068/0073 text. Candidate accepted at Orchestrator level.
- Cooperator **accepted ADR-0074 with clarifications** (see section 5,
  2026-08-25).
- Near-miss recorded: session 02 used one ambient `python3` invocation for
  markdown link enumeration, outside the grant's Python route. Honest,
  non-mutating, no FrameNest import. Corroborates the existing untriaged
  upgrade-ledger entry
  `consumer-declared-execution-and-capability-route-binding`; no new ledger
  entry opened.
- Session 02 exchange 02 reported implementation PASS: commit `6aac705`
  (parent `0008ca5`), nine allowlisted files; ADR-0074 now `Accepted`,
  auto-analysis assumption rewritten to the ADR-0066 boundary, living-doc
  guard sentences verified by Orchestrator grep. Exchange accepted.
- Session 02 exchange 03 issued: publication-gate correction
  (`04_implementation_00.md`) — companion Apply never publishes,
  administrator PUT sole write, historical `companion_review` rows readable,
  focused tests via canonical `./.ap/ap exec` route.
- Session 02 exchange 03 reported implementation PASS: commit `ffef457`
  (five files); Orchestrator re-ran focused tests independently (21 passed)
  and verified the sole remaining publication insert is the admin PUT
  adapter. Accepted. Recorded follow-up: unpublish-on-PUT was outside
  exchange 03's allowlist — scheduled as exchange 04 before any public
  reader exists.
- Session 02 exchange 04 reported implementation PASS: commit `dd26782`
  (thirteen files; unpublish on the sole route, honest statuses, audit kept).
  Orchestrator verified commit shape, writer/deleter grep (only admin
  adapter + catalog removal), and independently re-ran the new unpublish
  contract tests (4 passed). Accepted. Rollout #1 complete.
- Session 03 exchange 01 issued (fresh session): local-only
  `public_published_uds` reader per accepted ADR-0074
  (`06_implementation_00.md`). Explicitly local-only; no external exposure,
  TLS, Funnel, or NUC changes in this grant.
- Session 03 exchange 01 reported implementation PASS: commit `95f514b`
  (twenty files; local-only public reader). Two allowlist deviations
  honestly recorded (`server.py` UDS bind for the public mode; one
  `GET /api/audience/me` route-policy line in `tailscale_ingress.py`) —
  both necessary, reviewed and accepted by the Orchestrator. Orchestrator
  verified commit shape, no-mutation grep on public modules, read-only
  fail-closed engine wiring, distinct socket default, and independently
  re-ran the inventory contract suite (11 passed). Accepted.
- Session 03 exchange 02 reported implementation PASS: commit `5b99575`
  (twenty-six files; `media.workspace.read`, workspace list, own-attribution
  content reads, admin contributor filter). Orchestrator verified commit
  shape, read-only attribution grep, public-composition route freedom,
  trusted-ingress capability policy line, and independently re-ran the
  workspace contract tests (3 passed). Accepted. Rollout #4 complete.
- Session 03 exchange 03 issued: durable ordinary-user analysis proposals
  (`08_implementation_00.md`) — one additive migration to schema head 0033,
  `analysis.propose` capability, POST proposal + admin list, strict
  no-provider/no-enqueue/no-flag boundary.
- Session 03 exchange 03 reported implementation PASS: commit `da06109`
  (forty-one files; additive migration 0033 `media_analysis_proposals`,
  `analysis.propose`, POST + admin list, strict no-provider/no-enqueue
  boundary proven behaviorally and by grep). Orchestrator verified commit
  shape, schema CHECK, public required-revision bump, and independently
  re-ran proposal + migration tests (14 passed). Accepted. Flagged drift:
  README/PRODUCT/ROADMAP still say 0032 — folded into exchange 04's
  allowlist.
- Session 03 exchange 04 reported implementation PASS: commit `f59f401`
  (twenty-three files; `metadata.alias.team.read` admin-only, dual-gate
  audited team-alias route, SELECT-only stack, 0032→0033 prose fix in
  README/PRODUCT/ROADMAP). Orchestrator verified commit shape, dual
  capability policy, write-free alias path grep, and independently re-ran
  the team-alias contract tests (9 passed). Accepted.
- **All six ADR-0074 code rollouts complete** (1 gate incl. unpublish,
  2 local public reader, 4 workspace media, 5 proposals, 6 team aliases;
  rollout 3's independent security acceptance pending; rollout 7 companion
  reconnect parked; rollout 8 unpark on Cooperator request).
- Session 04 exchange 01 reported audit PASS: verdict **yes-with-conditions**.
  No Critical/High. Conditions: C1 = F-1 public 422 validation leakage
  (Low), C2 = F-2 tcp-mode non-loopback bind guard (Medium, pre-existing),
  C3 = rate limits/body caps/timeouts owned by the future reverse-proxy
  whole (F-8), C4 = Cooperator disposition on F-3 proposal growth
  (dedupe / rate limit / dismiss route / accept). Ride-alongs: F-4 marker
  assert, F-5 sanitized error logging, F-6 URI percent-encoding. Orchestrator
  spot-verified F-1/F-2 citations in source. Audit accepted; triage:
  C1+C2+ride-alongs routed to session 05 infosec hardening slice;
  C3 recorded as mandatory acceptance item of the TLS/reverse-proxy
  preflight checklist; C4 pending Michal's product decision.
- Session 05 exchange 01 reported implementation PASS: four commits
  (`bcf5ec1`, `d3b203f`, `4b7b87e`, `3a21405`) closing F-1, F-2, F-3(B),
  F-4, F-5, F-6; full suite 3300 passed / 8 skipped. Orchestrator verified
  the chain and independently re-ran focused tests (65 passed).
  **Report accuracy near-miss:** the Worker's report mis-transcribed the
  final full SHA (actual `3a21405e08ff30a840afe655e702d931e833acf2`,
  reported `...0b0c0b7bdeddbb64ac1e2ea1a2f04e04`); same short prefix, real
  chain confirmed by git. Accepted with correction recorded.
- Cooperator explicitly requested the previously out-of-scope INFOSEC manual
  + admin/diagnostic scripts ("potrebujem si byť istý pre public net").
  Session 05 exchange 02 issued (`12_infosec_docs_00.md`): docs/INFOSEC.md
  (hardening manual + audit record), bash operator tools under
  scripts/operator/infosec/**, README pointer. After it: TLS/reverse-proxy
  deployment preflight whole remains the gate to any public bind.
- Session 05 exchange 02 reported implementation PASS: commit `be35922`
  (five files, +708): docs/INFOSEC.md manual with audit record + F-9
  numbering note + citation-dense checklist, three bash operator tools
  (`bash -n` verified by Orchestrator), README pointer. Behavioral smoke ran
  against throwaway /tmp fixtures only. Accepted.
- Session 05 exchange 03 reported PASS: Cooperator acceptance-test guide
  delivered (`13_report_00.md`); two non-blocking script polish items routed
  (executable bit, `-h` early exit). Orchestrator verified guide commands
  against launcher docs and script headers at HEAD.
- **Cooperator freeze decision (2026-08-25):** VPS/public-net/TLS deployment
  planning FROZEN for this whole; any future deploy era MUST reconnect with
  then-current deployment documentation (NUC runbook, framenest-release
  ADR-0060 contract, INFOSEC.md checklist). Acceptance guide to be mirrored
  into the repository. Whole remains open pending Michal's Part A/B
  acceptance execution — parked, not closed.
- Session 05 exchange 04 issued (final freeze preparation,
  `14_freeze_prep_00.md`): repository `docs/ACCEPTANCE_DUAL_AUDIENCE.md`
  with deploy-freeze annex + preflight shape, script polish, README pointer.
- Session 05 exchange 04 reported PASS: final commit `c3e9ac7617a07b6a8e60c911a0b78b25ced71665`
  — scripts now 100755 with `-h` exit-0 (live-verified by Orchestrator),
  `docs/ACCEPTANCE_DUAL_AUDIENCE.md` (415 lines) with Deployment-Freeze
  Annex, README pointer. Accepted. **04/00 whole is now FROZEN-PARKED:
  code+audit+docs complete at this SHA, pending Cooperator Part A/B
  acceptance execution; not closed.**
- Restoration handout for the next era authored by this Orchestrator at
  `/home/agile/meta/projects/framenest/05/00-framenest-companion-brave-testing-resume/00_handout.md`
  — mission: resume parked companion Brave extension testing (03/10 backlog)
  under Michal's explicit unfreeze authority.
