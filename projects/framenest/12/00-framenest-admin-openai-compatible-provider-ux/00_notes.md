# Era 12 Whole Notes — admin OpenAI-compatible provider UX

Classification: private local historical/evidentiary projection for this
logical whole. Orchestrator-owned, append-only during the whole, frozen at
closure. Non-authorizing. Public-safe by default. Michal owns any meta Git
commit.

Working identity (proposed until Planner + Cooperator lock it):

```text
framenest-admin-openai-compatible-provider-registry-and-vision-probe
```

Trace:

```text
/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/
```

Handout: `00_handout_agent.md` (2026-09-16). Not current authority.

## Session log

- **2026-09-16 — seed from predecessor ChatOrchestrator.** Cooperator dropout
  orientation; NUC SSH and global sudo reported ready; brainstorming on
  OpenCode Go as HTTP provider, jsonc-style add, ping/pong vision probe in
  FrameNest admin UI (not Django); order to hand off to a fresh Agent
  Orchestrator with ~1M context. No FrameNest mutation. No Worker dispatched.
  Public `main` not independently `ls-remote`'d in that session.

## Confirmed-refinements ledger (Cooperator intent, not ADR)

1. OpenCode is a **server AI provider**, not a Worker and not `opencode` CLI.
2. API key + vision filter + image analysis.
3. Prefer **OpenCode Go** gateway URL, not Zen aliased as Go.
4. Standardized **add provider** like OpenCode jsonc, FrameNest-owned JSON,
   secrets never in the file.
5. Ping (text) then pong (tiny PNG, “what color is this?”) from **admin UI**.
6. Not Django — FrameNest administrator web shell.
7. Test step-by-step on NUC after publish+refresh; judge function, design, UX.
8. No copy-paste ferry. Orchestrator writes prompts to this directory;
   Workers write reports here. Cooperator does not create/rename files.
9. No subagents. Planner is the first dispatched Worker.
10. Keys must not enter the browser unless a later explicit security decision
    overturns SPEC (predecessor recommendation: refuse).

## Open gates for the incoming Orchestrator

- Re-verify FrameNest HEAD `33946e08…`, AP pin `7478ddb…`, public `main`.
- Revalidate AP upgrade ledger against live pin (entry last seen against
  `7ef45da…`).
- NUC release SHA vs public `main` unknown; era 11/01 did not deploy.
- NUC banner: system restart required (not this whole).
