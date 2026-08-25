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
- Session 02 exchange 04 issued: administrator unpublish on the sole
  content-publication route (`05_implementation_00.md`). Next after it:
  fresh session 03 for successor whole #2, local-only `public_published_uds`.
