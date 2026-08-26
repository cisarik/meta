# Orchestrator notes — era 07 / framenest-ai-suggestions-alias-edit-mvp

Ledger storage version: 1
Maintained by: Agent Orchestrator. Append-only narrative; superseded facts move to Git/history.

## 2026-08-26 — fresh Orchestrator restoration (read-only)

- Era opened from `07/00-framenest-ai-suggestions-alias-edit/00_handout.md`.
  Required reading completed before any Worker prompt: FrameNest `AGENTS.md`;
  pinned `.ap/AP.md`, `AP_ORCHESTRATOR.md`, `PROMPT_CONTRACTS.md`,
  `AP_WORKER.md`; `docs/WORKER_EXECUTION_CONTRACT.md`; declared upgrade
  ledger `docs/AP_UPGRADE_OBSERVATIONS.md`.
- Direct re-verification of handout §2 (this Orchestrator, not inherited):

  | Fact | Observed |
  |---|---|
  | Canonical checkout | `/home/agile/Projects/framenest` |
  | Canonical branch | `feat/x-meme-browser-companion` |
  | Canonical HEAD | `2aead540ee39a81a96425902f85e9b9a34f0d690` |
  | Canonical tree | `0900818f57326017712c07686c49de61d534507f` |
  | Canonical index | tracked-clean (`git status --porcelain=v1` empty) |
  | Public `refs/heads/main` | same 40-hex (credential-free `git ls-remote`) |
  | Local log -2 | `fb59c42` persist-join; `2aead54` item-9 test uninvert |
  | Tracking curiosity | ahead 29 of `origin/feat/x-meme-browser-companion`; informational; not a side quest |
  | AP gitlink | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |
  | `.ap` HEAD | same pin, detached |
  | Public `cisarik/ap` `main` | same pin |
  | Schema versions dir | `0001`–`0033` only; Alembic head file `0033_media_analysis_proposals.py`; no `0034_*` migration. ADR-0034 is AP integration, not schema. |
  | Live NUC | **not re-read**; last Cooperator-attested `active_release` `2aead54…` / schema `0033` |
  | Isolated worktrees | leftover era-06 w3–w10 and older trees present; not deleted |

- Upgrade ledger (`docs/AP_UPGRADE_OBSERVATIONS.md`): structurally valid
  header (`Ledger storage version: 1`, target
  `upgrade https://github.com/cisarik/ap.git`). One active entry
  `consumer-declared-execution-and-capability-route-binding`, state
  `untriaged`, authority `non-authorizing`. Stored
  `Last revalidated against: 5abb2adf…` is older than current HEAD.
  Operational revalidation against current repository + public AP `main`
  (`9c5cc44…`, equal to the pin): observation still holds —
  `AGENTS.md` / `WORKER_EXECUTION_CONTRACT.md` still bind Cursor Workers to
  `./.ap/ap project check` / `exec`; `ap.project.conf` still uses relative
  `executable = .venv/bin/python`. Isolated-worktree `--root <worktree>`
  launch-path miss remains a known topology limitation. The failing exec
  was not re-run this session. File SHA not updated (no FrameNest mutation
  authority). Entry remains non-authorizing and **not this kebab**.
- Restoration classification: **PARTIAL**. Useful continuity verified.
  Material uncertainty belongs to the Planner: ordinary Edit Save → alias
  PUT vs canonical; Gallery/Details read stay canonical this whole (default
  write-only); suggestions dropdown sourced from existing
  `media_analysis_runs` without a second store; first-attempt “AI provider
  is not available” vs stale copy. NUC SHA not re-read this session.
- Not BLOCKED: no in-flight Worker authority; canonical is public main;
  no unpublished candidate.
- Stage 2: already selected by Michal (`framenest-ai-suggestions-alias-edit-mvp`).
  First Worker: Planner session 01 / exchange 01. Prompt staged
  `01_planning_00.md`. Report destination `01_report_00.md`.
- Closed predecessor `framenest-companion-brave-testing-resume` remains
  closed. R1–R3′ and item 9 PASS are not reopened. R4 and VPS stay out.
- No product code implemented. No publication, NUC, Git writes in FrameNest.
