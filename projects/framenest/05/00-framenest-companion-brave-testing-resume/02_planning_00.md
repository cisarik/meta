# FrameNest — Planner Worker prompt (companion history correction)

Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: on (Plan Mode; no filesystem writes anywhere)
Worker session profile: Fresh Planner
Phase: planning
Reasoning recommendation: High (identity-boundary change to an audited surface: ordinary users gain a history view; cross-layer semantics across extension, API, repository)
Task identity: FRAMENEST-COMPANIE-HISTPLAN-01 — decision-ready plan for companion history correction R1–R3
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/05/00-framenest-companion-brave-testing-resume/
Trace project key: framenest
Trace logical-whole projection identity: framenest-companion-brave-testing-resume
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: private
Trace companion outcome: report (returned in chat; ORCHESTRATOR archives it as 02_report_00.md because Plan Mode grants you no write access)
Trace self-granted status: none

## Mission

Produce the decision-ready implementation plan for the Cooperator’s recorded
companion-history amendments (R1–R3 below), so a fresh implementation Worker
can execute one bounded slice at exact baseline:

```text
91410fe063d9907304cff4550f61d403880a2eeb  (= current public main)
```

You are read-only: repository inspection and reasoning only. No edits, no
Git operations, no tests execution, no NUC, no providers.

## Accepted Cooperator decisions (2026-08-26, authoritative — do not relitigate)

- **R1 click-path:** clicking ANY own row in merged history opens the hosted
  iframe popup (the same path used by the compact five). The small native
  popup is a defect to eliminate. Inside that popup admin may Edit;
  “Analyze by AI” must NOT appear in the companion-opened popup.
- **R2 admin view:** admin sees only ANALYZED items. A newly analyzed item
  appears top-most directly under the title bar with newest accent and badge
  +1 (`unopened_count`). A single click = open: accent clears, badge −1,
  popup opens in iframe. Admin must never be blocked or gated inside this
  workflow.
- **R3 ordinary view:** an ordinary user sees ALL their own saves
  immediately in the merged history, plain (no accent, no badge). This
  SUPERSEDES the prior hidden-history (ordinary 403) behavior for own-saves
  while keeping requester-private discipline: nobody sees anyone else’s
  saves.
- Badge remains an admin-side analyzed-unopened counter.
- Explicitly OUT OF SCOPE (later whole): Settings “Administration” section
  with runtime-writable auto-analysis checkbox (R4); failed-save tombstones;
  X extractor failure root cause (owner data pending).

## Required reading (in order)

1. `/home/agile/Projects/framenest/AGENTS.md`; `.ap/AP.md` (planning duties);
   `docs/WORKER_EXECUTION_CONTRACT.md`
2. Backlog: `/home/agile/meta/projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/COMPANION_PARKED_BRAVE_TEST_BACKLOG.md`
3. `docs/adr/0073-companion-merged-history-chrome-pending-visibility-x-seed-tag-and-preserving-apply.md`
4. `docs/adr/0074-dual-audience-public-published-and-tailscale-workspace-boundary.md`
5. `SECURITY.md` companion paragraphs; `docs/X_COMPANION.md`
6. Prior evidence (context, non-authorizing): trace folder `01_report_00.md`
   and `01_report_01.md` (deterministic evidence matrix + gap list)
7. Source map (verify, then extend): `extension/` (background/content/ui/shared),
   `src/framenest/adapters/api/companion_review_api.py`,
   `workspace_media_api.py`, `x_companion_api.py`, `tailscale_ingress.py`,
   `src/framenest/application/companion_review.py`, `companion_picker.py`,
   `src/framenest/infrastructure/persistence/companion_review_repository.py`,
   identity/capability resolution, web shell `app.js` hosted-details path,
   tests `tests/companion_review_extension.test.js`,
   `tests/x_companion_extension.test.js`,
   `tests/companion_web_bridge.test.js`,
   `tests/contract/test_companion_review_api.py`,
   `tests/contract/test_workspace_media.py`,
   `tests/contract/test_tailscale_ingress_security.py`

## The plan must decide and specify

1. **Identity-scoped listing contract:** exact endpoints/payloads for admin
   (analyzed-only) vs ordinary (own saves, all states). Decide whether the
   existing contributor-scoped workspace media route satisfies the ordinary
   view or a bounded companion-scoped variant is required; keep
   requester-private discipline exact (no cross-user leakage; enumerate the
   negative tests proving it).
2. **Accent + badge lifecycle:** precise state machine (new-analyzed → top +
   accent + unopened; open → accent cleared, unopened false, badge −1),
   including which field(s) persist it server-side vs client-side and how
   compact-five vs All interact with the new filters.
3. **Click-path fix:** root-cause why pending/own rows currently open a
   native popup instead of the iframe path (name the exact code site), and
   the minimal correction so every row uses `open_details`
   (`framenest.companion.web.v1`, stored exact origin, never `*`).
4. **Companion popup contents:** Edit available; “Analyze by AI” absent from
   the companion-opened popup; identify whether that requires hiding the
   button via context/query flag or a served-page conditional, without
   regressing the standalone web shell Details behavior.
5. **Security invariants preserved:** four `companion_mutation` routes
   unchanged; allowlist + `X-FrameNest-Request: 1` unchanged; publication
   sole-writer unchanged; GET surfaces newly exposed to ordinary identities
   enumerated with their capability gates; uniform sanitized failure
   postures retained.
6. **Deterministic test additions:** per rule R1–R3, name each new/changed
   test file and case (Node extension suites + Python contract/repository
   suites), including negative paths (cross-user leakage, v1 fail-closed
   retention, corrupt-JSON resilience retention).
7. **Migration needs:** expected none; state it explicitly after checking
   whether accent/unopened state already persists (0033 schema).
8. **Sequencing:** implementation → deterministic suites → publication
   (Cooperator grant) → routine NUC release refresh → Cooperator re-render
   checklist; note what changes in `docs/X_COMPANION.md` wording (known-stale
   sentence may be fixed ONLY if inside this slice’s grant).
9. **Open questions** requiring Cooperator input before or during
   implementation, each with a proposed default answer.

## Hard boundaries

Read-only. No file writes (Plan Mode), no Git writes, no NUC/SSH/sudo, no
providers, no browser automation. Do not propose scope beyond R1–R3; park
adjacent ideas in a clearly-labelled “parked observations” section.

## Output (chat text, not a file)

Return the complete plan as structured Markdown in chat, beginning exactly:

### Report for ORCHESTRATOR_CHAT

Sections: status PASS/PARTIAL/BLOCKED; decision summary per R1–R3; route
matrix (file → change → layer); state machines; security-invariant checklist;
deterministic-test matrix; sequencing; parked observations; open questions
with proposed defaults; risks; report justification: new-evidence; authority
expiry statement. Professional English. Sanitized: no hostnames, tailnet
identifiers, allowlist values, live URLs/titles/UUIDs.

## Stopping rule

Stop and return PARTIAL/BLOCKED if repository evidence contradicts an
accepted decision (e.g., R2/R3 conflict with an audited invariant you cannot
reconcile) — name the exact contradiction instead of designing around it.

## Transition owner

ORCHESTRATOR archives your plan, routes open questions to the Cooperator,
then issues the implementation prompt. You have no follow-on authority.
