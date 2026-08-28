# Era 09 Whole Notes — `framenest-pin-adoption-and-presentation-profile`

Handout: `00_handout_agent.md` (restoration prompt, Agent Orchestrator).
Session opened: 2026-08-28 (read-only verification pass at open).

## Identity

- Logical whole: `framenest-pin-adoption-and-presentation-profile`
- Branch: `feat/x-meme-browser-companion`
- Product freeze (must not break): `472553cadcd3d4ca87a9792a2c306bd0afeea7c1`
- Cooperator: Michal (Slovak chat, masculine address; English artifacts/prompts)

## Immediate Gates — re-verified at open (do not trust handout numbers)

| Gate | Expected | Verified | Result |
| --- | --- | --- | --- |
| Public AP `main` | `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` | `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` | PASS |
| FrameNest HEAD | `85028f725537adcf922f2587d62f1bad68cd5924` | `85028f725537adcf922f2587d62f1bad68cd5924` | PASS |
| FrameNest branch | `feat/x-meme-browser-companion` | `feat/x-meme-browser-companion` | PASS |
| FrameNest porcelain | empty | empty | PASS |
| `.ap` gitlink (`HEAD:.ap`) | `86ae6e8c27d2b919d776021bee915b7292908b0e` (prior pin) | `86ae6e8c27d2b919d776021bee915b7292908b0e` | PASS |
| `.ap` worktree HEAD | `86ae6e8c27d2b919d776021bee915b7292908b0e` | `86ae6e8c27d2b919d776021bee915b7292908b0e` | PASS |
| `./.ap/ap doctor` | PASS | PASS (strict pin, clean submodule, stable variant, managed block OK) | PASS |

No contradictions between verified evidence and the handout. Evidence-over-prompt
rule: not triggered at open.

## Objectives (from handout Section 3)

1. Adopt AP pin `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` into `.ap` submodule;
   re-run `ap doctor` (strict pin, clean submodule, stable variant).
2. Establish project-owned Cooperator presentation profile in FrameNest root
   `AGENTS.md` outside the managed block (status marks 🟢🟡🔴, delivery
   package, Slovak chat / English prompt separation) per AP `INTEGRATION.md`.
3. Upgrade ledger reconciliation: revalidate
   `docs/AP_UPGRADE_OBSERVATIONS.md` entry
   `consumer-declared-execution-and-capability-route-binding` against new pin
   `7ef45da`.
4. Intuitive FrameNest deep review (read-only): FastAPI backend, loopback
   enforcement, companion review endpoints, media streaming, sqlite/alembic,
   sudo/SSH operator boundaries; stage findings as optional Discovery Record
   (`docs/discovery/`) or recommendations for later wholes. Product freeze
   strictly respected.

## Hard Boundaries (handout Section 5)

- This whole: pin adoption to `7ef45da`, `AGENTS.md` presentation profile,
  ledger triage, intuitive review.
- Not this whole: unapproved product rewrites, breaking schema migrations,
  NUC deployment without grant, pushing without grant.
- Product freeze `472553` must not be broken. Zero exposure of private media,
  credentials, or secrets. Loopback-first; Tailscale-only remote access.

## Dispatch Route

Agent Orchestrator default dispatch: complete Worker prompts via direct session
dispatch; in-session trace archival of prompt/report pairs. Opt-out (P14) only
if Michal explicitly requests copy-paste/manual mode. RF-05: parent-context
subagents cannot provide independent acceptance.

## Session Log

- 2026-08-28 — Session opened. Immediate gates re-verified read-only: all PASS,
  no drift, no contradictions. `00_notes.md` initialized.
- 2026-08-28 — Complete AP protocol study performed read-only: `AP.md` (2701
  lines), `AP_ORCHESTRATOR.md`, `PROMPT_CONTRACTS.md` (2240 lines),
  `INTEGRATION.md`, `UPDATING.md`, `INTUITION.md`, FrameNest `AGENTS.md`,
  `docs/WORKER_EXECUTION_CONTRACT.md`, `docs/AP_UPGRADE_OBSERVATIONS.md`,
  `SECURITY.md`, `PRODUCT.md`, `SERVER.md`, `SPEC.md`. Temporary read-only AP
  clone at `/tmp/opencode/ap-study` used for pin-diff study (no project
  mutation; cleanup owner Orchestrator at closure).
- 2026-08-28 — Pin diff `86ae6e8..7ef45da` studied (3 commits: be6a6ae, 2fbf8d3,
  7ef45da). Changes are documentation-only: no executable `ap` change, no
  managed-block change, no schema change. Content: ADR-0022 default agent
  dispatch + P14 opt-out, Companion Integrity Invariant, direct Orchestrator
  trace archival, Orchestrator initialization signal + profile-qualified
  handout filenames, UPDATING.md pin-time presentation review hook,
  INTEGRATION.md presentation-profile example. Prior-pin ledger disposition
  evidence paths (`.ap/ap`, ADR-0012, ADR-0018) still exist at `7ef45da`.
- 2026-08-28 — Ledger entry `consumer-declared-execution-and-capability-route-binding`
  pre-validated structurally against PROMPT_CONTRACTS ledger contract: fields
  exactly once, state `accepted`, `retain-active`; only required change at
  adoption is `Last revalidated against: 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`
  (+ disposition evidence refresh).
- 2026-08-28 — Product freeze `472553c` verified as ancestor of HEAD
  `85028f7`. Precedent commits studied: `chore: adopt AP pin <sha>` touching
  `.ap` only; `docs:` commits for ledger/AGENTS text. Era-08 meta trace
  conventions verified (fresh session per phase, `NN_<phase>_00.md` +
  `NN_report_00.md`, Companion Integrity Invariant applies).
- 2026-08-28 — Orchestration planning decision: one Worker planning exchange
  (session 01 / exchange 01, fresh-worker-session, read-only, `Native planning
  mode: not-used` — dispatch client lacks native plan mode; explicit
  prompt-level read-only planning authority), then implementation (current
  session exchange 02 after plan acceptance), then fresh independent acceptance
  (session 02) — required because the route changes the sole normative protocol
  source. Intuitive FrameNest deep review remains Orchestrator-direct
  read-only discovery (non-authoritative), not a Worker audit.
- 2026-08-28 — `01_planning_00.md` authored (complete authoritative planning
  prompt). Awaiting Cooperator approval before dispatch.
- 2026-08-28 — Cooperator approved dispatch ("Schvalujem…"). Planning exchange
  01 dispatched (Agent Orchestrator default dispatch, session 01 / exchange 01,
  fresh-worker-session). Terminal report: PASS — all 9 planning-scope questions
  evidenced; no mutation (HEAD unchanged, porcelain empty re-verified); `ap
  update --check` forward update confirmed (`86ae6e8` → `7ef45da`, no
  divergence); executable `ap` byte-identical between pins; ADR-0012/0018
  unchanged at `7ef45da`; `ap init` not required; AGENTS.md insertion point
  (after `## Communication`, before `## Security Boundaries`) validated
  unoccupied and conflict-free; ledger contract-valid now and after the
  planned two-field change; `ap project check --baseline 85028f7` PASS
  (readiness only). Rollback and risk register recorded in the report.
  Orchestrator reconciliation: independent re-verification of HEAD, porcelain,
  gitlink equality, doctor PASS, and 3-commit pin diff — all claims confirmed.
  Pair `01_planning_00.md` + `01_report_00.md` archived together after the
  report existed (Companion Integrity Invariant verified: report commences
  with the required header and contains the compact core; not a prompt
  duplicate). Meta-repo Git commit of the trace pair: deferred pending
  explicit Cooperator Git authority. Planning authority expired at the
  terminal report; plan acceptance pending with the Cooperator.
- 2026-08-28 — Cooperator accepted the plan ("Akceptujem"). Routing: exchange
  02 implementation to the same current Worker session (session 01 / exchange
  02, current-worker-session, continuity anchor = terminal PASS planning
  report for FRAMENEST-PIN-ADOPTION-PLAN-01), Medium reasoning, two exact
  commits, no push. `02_implementation_00.md` authored and dispatched.
- 2026-08-28 — Implementation exchange 02 (session 01 / exchange 02): PASS,
  `implementation-PASS`. Commits `fd53578` (`chore: adopt AP pin
  7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`, `.ap` only) and `d8629e3`
  (`docs: declare Cooperator presentation profile and revalidate AP upgrade
  ledger`, AGENTS.md + ledger). All stage gates passed; no push. Orchestrator
  reconciliation: independently verified — two exact commits, delta scope
  exactly the three allowlisted paths, porcelain empty, gitlink == `.ap` HEAD
  == `7ef45da`, strict doctor PASS `stable`, ledger diff exactly the two
  intended lines, AGENTS.md pure verbatim insertion, freeze `472553c` still
  ancestor. Pair `02_implementation_00.md` + `02_report_00.md` archived
  (companion integrity verified). Implementation evidence is non-independent
  (same-session continuation); fresh independent acceptance outstanding.
- 2026-08-28 — `03_acceptance_00.md` authored (session 02 / exchange 01,
  fresh-worker-session, Fresh Independent Audit, independence required) and
  dispatched. Acceptance plan per planning report item 8: 10 checks including
  public-pin ls-remote equality, managed-block byte-identity, ledger contract,
  freeze invariance, and Companion Integrity of archived trace pairs.
- 2026-08-28 — Acceptance exchange (session 02 / exchange 01, genuinely fresh
  dispatched session): **acceptance-PASS**, all 10 checks with independent
  evidence, zero findings. Highlights: public AP `main` == `7ef45da`
  (ls-remote), managed block byte-identical, Appendix A verbatim at lines
  175–204, ledger contract-valid, freeze ancestor, Companion Integrity of both
  archived pairs verified, implementation report claims fully reproduced.
  Pair `03_acceptance_00.md` + `03_report_00.md` archived. Candidate accepted
  at `d8629e3` (Acceptance PASS). Remaining: Orchestrator-direct intuitive
  deep review (objective 4, read-only discovery), then Cooperator decisions
  (push authority, meta-repo trace commit, Discovery Record staging if
  desired) and closure.
- 2026-08-28 — Objective 4 (intuitive deep review, Orchestrator-direct
  read-only discovery via three internal read-only explore passes, findings
  non-authoritative). Product-freeze respected; no finding is a proven
  vulnerability at HEAD. Highlights (full evidence in explore outputs of this
  session): (1) HTTP surface — capability matrix for companion/X/admin
  settings verified solid; extension-origin allowlist fail-closed; audience
  policy enforced at every media surface; no missing route guard. Candidate
  hardening: UDS socket-mode not asserted at startup (deployment-coupled);
  workspace app uses FastAPI default 422 body (error-contract inconsistency);
  adapter `str(exc)` passthroughs rely on app-layer sanitization (latent).
  (2) Persistence/acquisition — migration chain 0001→0033 linear, no
  backfills contrary to ADRs; publication chain crash-safe; downloaders
  cookie-free; analysis gating triple-gated; `analyzing→failed` fail-closed
  implemented as documented. Cosmetic: `uq_x_post_claims_id` schema drift;
  dead constant; brittle cursor-error message matching. (3) Operator/docs —
  sudo bridge verified genuinely narrow; release helper matches ADR-0060;
  loopback-first enforced in code. Doc drift (Medium): PRODUCT/SPEC/ROADMAP/
  README still frame NUC as "personal production server" contrary to
  ADR-0075; PRODUCT/ROADMAP call `public_published_uds` unshipped while
  implemented-for-backend; ADR-0077/0078 absent from living docs;
  README claims a `FRAMENEST_HOST=0.0.0.0` override the code rejects;
  SERVER.md says four companion mutation routes (five exist). Boundary check:
  no ADR contradicts loopback-first/Tailscale-only/read-only /srv/media.
  Findings are implementation recommendations for subsequent wholes; no
  product mutation performed.
- 2026-08-28 — Cooperator approved publication ("Prosím uverejnit komplet
  vsetko"). Push executed and verified: `origin/feat/x-meme-browser-companion`
  `afa0670..d8629e3` (origin == local HEAD). NUC refresh declared manual by
  the Cooperator (routine ADR-0075 route). Meta-repo commits declared manual
  by the Cooperator (no Orchestrator Git authority over meta).
- 2026-08-28 — Era-10 handover generated per Cooperator direction:
  `10/00-framenest-companion-security-and-frozen-slice-validation/`
  `00_handout_agent.md` (profile-qualified filename per AP 7ef45da/ADR-0022)
  + initialized `00_notes.md`. Handout embeds the complete deep-review
  candidate worklist (companion/extension security, backend infosec
  candidates, doc drift, nits, positive confirmations) and the Agent
  Orchestrator recommendation with rationale.
- 2026-08-28 — Whole closed (Cooperator-informed). `04_closure_00.md`
  written. Final state: HEAD `d8629e3` published; AP pin `7ef45da` adopted,
  accepted, and ledger-revalidated; presentation profile live in `AGENTS.md`.
  Temporary probe state cleaned (`/tmp/opencode/ap-study` removed at
  closure). Logical-whole closure: CLOSED.

## Open Items / Next Steps

1. Required reading before Exchange 01 (handout Section 2): AGENTS.md spine,
   `.ap/AP.md`, `.ap/AP_ORCHESTRATOR.md`, `.ap/PROMPT_CONTRACTS.md`,
   `.ap/UPDATING.md`, `.ap/INTEGRATION.md`, `docs/AP_UPGRADE_OBSERVATIONS.md`,
   `docs/WORKER_EXECUTION_CONTRACT.md`, `SECURITY.md`, `SPEC.md`, `PRODUCT.md`,
   `SERVER.md`, AP ADR
   `0022-default-agent-dispatch-trace-integrity-and-pin-presentation.md`.
2. Then Exchange 01 planning and dispatch (pin adoption + presentation profile
   as first candidate scope; ledger triage and deep review follow).
