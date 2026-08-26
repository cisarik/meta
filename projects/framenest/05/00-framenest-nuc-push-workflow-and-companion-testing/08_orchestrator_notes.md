# Orchestrator notes — era 05 / framenest-nuc-push-workflow-and-companion-testing

Ledger storage version: 1
Maintained by: Agent Orchestrator (era 05). Append-only narrative; Git history archives superseded entries.

## 2026-08-26

- Era handout taken over from outgoing meta era
  `04/00-framenest-public-published-surface-and-tailspace-workspace`. Required
  reading completed; §1 refs verified at rotation (HEAD `c3e9ac7…`, clean
  worktree, AP pin `9c5cc44…`, backlog opens). Public main at rotation:
  `0fe2b32…`.
- Routing deviation recorded: era began with direct Cooperator interaction
  (NUC deployment question) before the Planning exchange; corrected same day
  by issuing fresh Planner Worker session 01/exchange 01
  (`01_planning_00.md`) per PROMPT_CONTRACTS RF-19 coordinates.
- Documentation cut committed and published:
  - `06af60a` docs: reframe NUC as development-test target (ADR-0075) +
    living-doc alignment (AGENTS/README/SECURITY/SERVER/runbook/ADR index).
  - `0706818` docs: require current NUC for rendered UI/UX and companion
    acceptance (AGENTS.md new standing rule; README clause).
  - Fast-forward pushes `0fe2b32 → 06af60a → 0706818` to public `main` under
    explicit Cooperator grants ("Dám push?" → yes; later "pushni").
- Observed NUC truth (supersedes handout): active release `a5487149…`, schema
  `0032`, backup restore-readiness `ready`, service active. Expected next
  transition: public main `0706818…`, schema jump `0032 → 0033` via documented
  exit-13 continuation.
- Two aborted non-interactive attempts to drive `~/nuc_update.fish` produced
  NO mutations (status + one remote `sudo -n true` probe only);
  `/run/framenest-release-deploy` never created. Root causes: ssh stdin
  consumption; fish terminal-capability query hang under pseudo-TTY.
  Route A (owner interactive run) selected thereafter.
- Planner session 01 delivered decision-ready synthesis; archived verbatim to
  `01_report.md` by Orchestrator (Worker ran under Plan Mode without FS
  write authority).
- Cooperator decisions 2026-08-26 ("pushni + vsetko default"):
  - Route A confirmed for first full push-to-NUC (Michal executes
    `~/nuc_update.fish` interactively; sudo lifecycle his).
  - Companion 03/10 Brave backlog EXPLICITLY REOPENED (era mission), gated on
    NUC serving the tested public-main SHA.
  - Apply acceptance deterministic-only; rendered Apply entry would be a
    separate product whole.
  - One owner-selected disposable public X item allowed later; acquisition
    authorized only when that scenario starts; never identified in evidence.
  - Reuse existing analyzed rows / ordinary profile; otherwise NOT RUN.
  - Allowlist-gate failure routes to a separate EnvironmentFile/restart task.
  - No synthetic live-data mutation; combine rendered + deterministic
    evidence when six analyzed rows are unavailable.
- Session 02/exchange 01 issued (`02_implementation_01.md`): documentation
  coherence + exit-13 runbook annex + two contract suites; exact baseline
  `0706818…`; local-commit-only authority.
- Pending: Michal's interactive NUC refresh run (Route A); session 02
  execution; afterwards publication of its commit and a second trivial
  same-schema refresh; then session 04 deterministic companion acceptance at
  the refreshed shared SHA.

## 2026-08-26 (doplnok)

- Route A executed by Michal interactively: full push-to-NUC PASSED.
  Evidence chain classified by Orchestrator from owner transcript:
  pre-status a5487149/0032/backup-ready -> check exit 0 (public main ==
  0706818, AP pin 9c5cc44) -> deploy exit 13 migration-required with current
  unchanged -> lock cleanup -> migrate from new tree at_head 0033/0033 ->
  rollback forward-cutover complete -> post-status active_release 0706818,
  service active, schema 0033, backup ready. All nine planner state-machine
  evidence points satisfied. NUC now serves the tested public-main SHA.
  Owner transcript contains host-specific values (SSH fingerprint, tailnet
  IP); deliberately NOT copied into repository artifacts or this ledger.
- Pending: owner terminal sudo -K confirmation; session 02 execution;
  publication of its commit; second same-schema refresh; session 04.
- Session 02/01 terminal report classified implementation-PASS. Orchestrator
  independent verification: parent==baseline, exactly the eight allowlisted
  files, canonical checkout untouched (0706818 clean), focused suites
  re-run by Orchestrator -> 35 passed, runbook migrate path only
  releases/<T>, README publication/successors claims present. Published:
  fast-forward push docs/nuc-dev-test-runbook-annex -> public main
  (0706818 -> 91410fe) under Cooperator's approved sequence; canonical era
  branch ff-merged to 91410fe so wrapper detection passes. Residual editorial
  debt recorded by Worker (runbook Current Target wording etc.) left for a
  later slice. Pending: second same-schema NUC refresh (expected deploy exit
  0), then session 04 deterministic companion acceptance at shared SHA.

## Closure 2026-08-26

- Second same-schema NUC refresh: Cooperator attests success ("tvoj skript
  prebehol"); transcript not captured. Accepted as owner attestation; the
  successor whole's preflight gate re-proves NUC SHA before any companion
  testing.
- Logical whole CLOSED by explicit Cooperator decision. Scope summary:
  push-to-NUC workflow proven end-to-end; documentation coherence published
  (main 91410fe); companion Brave testing PLANNED (session 01 synthesis) and
  TRANSFERRED unexecuted to successor whole
  05/00-framenest-companion-brave-testing-resume (base handout copy +
  Orchestrator-issued 01_addendum_2026-08-26.md recording state deltas and
  defaults). Coordinates restart there at session 01/exchange 01.
