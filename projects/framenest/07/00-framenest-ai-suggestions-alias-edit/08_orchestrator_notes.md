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

## 2026-08-26 — Planner session 01 / exchange 01 review

- Artifact: `01_report_00.md` exists. It is a Slovak Cursor Plan Mode
  document (YAML front matter, mermaid, archive-todo), **not** the
  contracted AP terminal report (`### Report for ORCHESTRATOR_CHAT`,
  coordinates, PASS/PARTIAL/BLOCKED, English). Planning authority expired
  at that delivery. This is **not** planning PASS under AP. Content is
  treated as a frozen planner artifact pending Cooperator approval plus
  one Orchestrator freeze (below). No Worker impersonation: the file was
  not rewritten.
- Gate claims in the artifact match this Orchestrator's restoration
  (HEAD `2aead54…`, tree `0900818f…`, AP pin `9c5cc44…`, Alembic `0033`).
- Repository-checked claims that hold:
  - Ordinary lacks Edit because Details ~443–444 and Gallery ~6029 gate
    on `metadata.canonical.write`; ordinary already has `alias.write`;
    alias GET/PUT exist.
  - `GET /api/media/{id}/automatic-analysis` is latest-only
    (`get_by_media_definition` → `_latest_run`).
  - `GET /api/companion/review-inbox/{media_id}` returns `suggestions[]`
    (generic analyzed history, movie 409, default limit 25 / max 100),
    capability `media.workflow.read`, **not** `companion_mutation`.
    Ordinary stays 403. Website Edit may GET it; must never POST apply.
  - `result_json` already carries title/description/tags/filename.
  - Bulk Load is `applyResolvedAiSuggestionToMetadataWorkspace` ~5494.
  - Analyze locks after `aiSuggestionApplied` (~6505–6517, ~7204).
  - Provider copy is `aiSuggestionErrorMessage` ~7285
    (`AI_PROVIDER_UNAVAILABLE`); library-scan ~10362 is a different path.
  - Essay “New AI analysis is available after confirmation.” is
    `renderMetadataAiPanel` ~6753–6755 when `aiCapability.available`.
  - Stale confirm: `metadataAiConfirmationContextIsCurrent` includes
    `aiCapabilityRevision`; mismatch returns without status (~7222).
  - Gallery 🧠 is `identityAllowsCardAiQuickAction` ∧ incomplete ∧ not
    movie; park as debt.
  - ADR-0076 still says Edit remains `metadata.canonical.write`.
- Named Orchestrator freeze **not** in the artifact as written:
  ordinary Edit **form load** must GET existing alias when non-empty,
  else seed from canonical. Artifact said Current always seeds from
  canonical GET, never alias — that would make re-open Edit ignore the
  overlay the user just saved. Gallery/Details **display** stay
  canonical. Awaiting Cooperator confirmation; then implementation
  Worker 02, not a second planning cycle.
- Implementation notes if accepted: dropdown GET `limit=100`; movie
  Edit keeps Identify, hides generic suggestions (inbox GET 409);
  isolated-worktree Python still canonical `--root` + pytest
  `--rootdir`/`pythonpath` deviation; no 0034; no fifth
  `companion_mutation`.
- No implementation issued. No FrameNest mutation.

## 2026-08-26 — Cooperator accepted the plan; Worker 02 issued

- Michal: „prijímam plán.“ Treated as acceptance of the frozen planner
  artifact plus the Orchestrator form-load freeze (ordinary Edit GET alias
  if non-empty, else canonical seed; Gallery/Details display stay
  canonical).
- Planning PASS is still not claimed (artifact lacked the AP report
  header). Product authority for implementation is this Cooperator
  acceptance + this grant, not a rewritten Worker 01 report.
- Implementation prompt staged `02_implementation_00.md`. Session 02 /
  exchange 01, `fresh-worker-session`, `Native planning mode: not-used`,
  isolated worktree, 1–3 local commits, no push. Independent acceptance
  remains a later fresh Worker.
- No FrameNest mutation in this Orchestrator turn.
