# FrameNest — Planner Worker prompt

Logical whole identity: framenest-nuc-push-workflow-and-companion-testing
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Discovery/planning-only synthesis (no implementation)
Phase: Discovery Or Intent Synthesis
Reasoning recommendation: High (spans ops tooling, documentation coherence, and product acceptance planning)
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/05/00-framenest-nuc-push-workflow-and-companion-testing/
Trace project key: framenest
Trace logical-whole projection identity: framenest-nuc-push-workflow-and-companion-testing
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

## Role

You are a fresh Planner Worker for FrameNest under Analytic Programming
(submodule pin at the canonical checkout). Your single outcome is a
decision-ready plan for the Orchestrator. You do not implement, mutate, deploy,
or test anything.

## Authority

- READ and ANALYZE only, plus bounded clarifying questions routed through your
  report.
- Canonical checkout (read-only): `/home/agile/Projects/framenest`.
- Write authority is limited to your own trace files in the discovery path
  above (`01_planning_00.md` is this issued prompt; you create
  `01_report.md`).
- Prohibited: repository mutation of any kind; Git write operations; running
  `~/nuc_update.fish`, `~/global_sudo.fish`, or any SSH/`gpgconf` command;
  NUC access beyond documents; invoking `.venv/bin/python`, `python`,
  `python3`, or `poetry run` outside `./.ap/ap project check` /
  `./.ap/ap exec` with an exact authorized baseline (you have no test
  execution authority at all in this exchange); provider calls; browser use.
- No closure, publication, deployment, or follow-on authority. Your report is
  structured claims for Orchestrator verification.

## Required reading (in order)

1. Outgoing-era handout:
   `/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/`
   (restoration handout document at that folder root).
2. `/home/agile/Projects/framenest/AGENTS.md` — note especially "NUC Routine
   Release Update" and "UI/UX Acceptance And Companion Testing Require A
   Current NUC".
3. `docs/adr/0075-nuc-development-test-target-and-routine-release-refresh.md`
   (Accepted 2026-08-26).
4. `docs/adr/0074-dual-audience-public-published-and-tailscale-workspace-boundary.md`
   (phased-rollout rules 7–8 govern companion unparking).
5. `/home/agile/meta/projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/COMPANION_PARKED_BRAVE_TEST_BACKLOG.md`
   — read completely.
6. `docs/INFOSEC.md`, `docs/ACCEPTANCE_DUAL_AUDIENCE.md`,
   `docs/WORKER_EXECUTION_CONTRACT.md`.
7. `deploy/ubuntu/README.md` and the "Routine Immutable Release Update"
   section of `docs/UBUNTU_NUC_DEPLOYMENT.md`; skim
   `deploy/ubuntu/framenest_release.py` exit codes and phase ordering.
8. Current status sections of `README.md`, `SECURITY.md`, `SERVER.md`.

## Verified facts you may rely on (Orchestrator-verified 2026-08-26)

- Public main equals local HEAD `0706818…` on branch
  `feat/x-meme-browser-companion`; worktree clean. Today's fast-forward push
  `0fe2b32 → 06af60a` published the previously unpublished stack (companion
  work + dual-audience whole) plus two new docs commits (ADR-0075 reframe;
  UI/UX-current-NUC rule).
- NUC observed state via `framenest-release status`: active release
  `a5487149…`, database revision `0032`, backup restore-readiness `ready`,
  service active. This supersedes stale handout claims of
  `aec2f009…/schema 0028`.
- Owner wrapper `~/nuc_update.fish` wraps exactly the four public subcommands
  (`status|check|deploy|rollback`) plus the documented exit-13 continuation
  (remove deploy lock dir → explicit `framenest-db migrate` from the newly
  published release tree → completion cutover via the `rollback` subcommand →
  post-status). Its two interactive `_confirm` reads failed twice under
  non-TTY orchestration today (stdin consumed by an intermediate SSH call;
  pseudo-TTY attempt hung on fish terminal-capability queries). No mutation
  occurred in either attempt — only `status` and one remote `sudo -n true`
  probe ran; `/run/framenest-release-deploy` was never created.
- The expected next refresh is therefore: public main SHA → NUC, schema jump
  `0032 → 0033` (single additive migration), using the documented
  continuation.

## Planning objective

Produce ONE decision-ready synthesis covering:

1. **First full push-to-NUC completion.** Compare at least these routes and
   recommend one with rationale, risks, stop conditions, and evidence classes:
   - (a) Cooperator runs `~/nuc_update.fish` interactively himself (baseline,
     zero new work);
   - (b) small separately-authorized repository tooling task adding a
     non-interactive confirmation mode to the wrapper pattern or documenting
     the direct four-command sequence as a runbook annex;
   - (c) Orchestrator-executed exact documented step sequence mirroring the
     wrapper logic (status → check → deploy expecting exit 13 → verify tree →
     lock removal → migrate from new tree → rollback-cutover → status), under
     standing ADR-0075 authority.
   State who executes each step and where sudo lifecycle sits.
2. **Documentation coherence pass.** The AGENTS.md UI/UX-current-NUC rule and
   ADR-0075 landed today; identify which remaining statements elsewhere
   (README Status history sentences, SECURITY support status, SERVER NUC role,
   runbook prose, ACCEPTANCE_DUAL_AUDIENCE Part B honesty banner) are now
   stale-but-historical versus genuinely misleading, and propose a minimal
   bounded editorial task if warranted — respecting "do not reopen closed
   logical wholes merely because prose elsewhere is stale".
3. **Companion Brave testing plan (era mission).** Unparking the 03/10 backlog
   per ADR-0074 rollout rule 8 requires testing against an origin+SHA that
   actually contains what the backlog tests. Plan the concrete procedure:
   precondition gate (NUC serving the current main SHA, verified how);
   extension-origin allowlist verification on the NUC environment file
   (presence/format checks only — never print values); scenario ordering over
   the backlog items; which evidence is Michal's rendered UX acceptance vs.
   deterministic API/test evidence; the routing pattern for any infosec
   findings (independent audit framing → Orchestrator triage → bounded
   remediation Worker → focused tests via `./.ap/ap exec`); and the preserved
   invariants (Apply writes metadata only and never publishes; movie
   exclusion; auto-analysis flag off in tracked files; loopback-first;
   Tailscale-only).
4. **Open questions** for the Cooperator, separated from recommendations, and
   **proposed bounded next Worker tasks** with suggested coordinate blocks
   (session/exchange ordinals) — proposals only, no self-granted authority.

## Output

- Trace file `01_report.md` in the discovery path, professional English,
  beginning exactly:
  `### Report for ORCHESTRATOR_CHAT`
- Structure: executive summary; route comparison matrix; recommended default;
  documentation triage table; numbered companion-testing procedure draft;
  open questions; proposed next-task coordinates; evidence limits.

## Transition owner

ORCHESTRATOR classifies your synthesis, resolves open questions with the
Cooperator, and issues any follow-on authoritative prompts. You decide nothing
strategic.

## Stopping rule

Stop when the decision-ready synthesis is complete or when a required input is
missing and must be requested through your report. Do not start any follow-on
phase.
