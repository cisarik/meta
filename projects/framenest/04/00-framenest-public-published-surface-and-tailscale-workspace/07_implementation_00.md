# FrameNest Worker prompt — 04/00 session 03 exchange 02 (implementation: contributor-scoped workspace media)

**Issuer:** the fresh Agent Orchestrator. Exchange 01 accepted (`95f514b`):
the local-only public reader exists. This grant authorizes rollout #4 of
accepted ADR-0074: the **Tailscale work gallery** as contributor-scoped
audience extension — every mapped PRO user sees their own attributed media,
published or unpublished, without inventing ownership or personal libraries.

Deliver to the **same healthy Worker session 03** (`current-worker-session`).
Native Plan Mode **off**.

```text
#------------------------------------------------------
```

You are the same FrameNest Worker under Analytic Programming, session ordinal
03 of logical whole
`framenest-public-published-surface-and-tailscale-workspace`.

Read before action:

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `/home/agile/Projects/framenest/.ap/AP.md`
3. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
4. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
5. `/home/agile/Projects/framenest/docs/adr/0074-dual-audience-public-published-and-tailscale-workspace-boundary.md`
   ("Workspace audience" section)
6. `/home/agile/Projects/framenest/docs/adr/0053-ordinary-user-upload-submission-and-administrator-review-boundary.md`
   and `docs/adr/0054-requester-private-youtube-acquisition-and-promotion-boundary.md`
7. Your exchange 01 report:
   `.../06_report_00.md` in this Meta folder

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 03
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: implement contributor-scoped workspace media list, own-attribution content reads, administrator contribution filter
Phase: implementation
Continuity anchor: your session 03 exchange 01 terminal report; commit 95f514b2cf127824a09550f54dc5e9e4d8c2d0ad
Authority renewal: complete new bounded grant; exchange 01 authority expired at its terminal report
```

```text
Requested reasoning: Extra High
Cooperator delivery / trace destination: report file below
```

## Compact core

```text
Role: WORKER
Cooperator: Michal
Canonical checkout: /home/agile/Projects/framenest
Exact baseline: 95f514b2cf127824a09550f54dc5e9e4d8c2d0ad (verify at start; worktree clean)
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Schema head: 0032 (no migrations authorized)
Git write authority: commits on feat/x-meme-browser-companion containing exactly allowlisted-path changes; coherent small commits permitted; no push
Allowlisted change scope (repository):
  src/framenest/domain/identity_access.py (add media.workspace.read capability)
  src/framenest/adapters/api/** (new workspace router/module; route-policy entries if the trusted ingress needs them)
  src/framenest/application/** attribution/workspace list use-cases and ContentAudiencePolicy extension
  src/framenest/application/ports/** and src/framenest/infrastructure/persistence/** read-side attribution queries
  src/framenest/adapters/api/web/app.js, styles.css (workspace surface + admin contributor filter)
  tests/**
  SPEC.md (only markers you actually implemented)
Allowlisted write paths (Meta):
  /home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/07_report_00.md
Python/test execution route (canonical, exclusive):
  ./.ap/ap exec runtime-info / test / test-focus with exact --baseline 95f514b2cf127824a09550f54dc5e9e4d8c2d0ad
  JavaScript tests exactly as docs/WORKER_EXECUTION_CONTRACT.md declares them.
  NO ambient python/python3/.venv invocation of any kind.
NUC / SSH / sudo / provider / external bind / push: none
```

## Task

1. **Capability**: add `media.workspace.read` to the identity-access table
   for BOTH ordinary (`user`) and administrator roles. No other capability
   changes. Tailscale membership alone still grants nothing.
2. **Workspace list**: add `GET /api/workspace/media`, guarded by
   `media.workspace.read` on the trusted ingress, returning the caller's
   attributed media — upload-attributed, YouTube requester-attributed, and
   X claim-attributed — whether published or unpublished, newest first with
   honest publication/readiness state per item. Reuse the existing
   attribution stamps (`created_by_login_key` on upload sessions, YouTube
   claims, and X claims); do not invent a new ownership table or column.
   A medium contributed by several users appears for each of them.
3. **Own-content reads**: extend the shared content audience policy so a
   mapped caller may read bytes/previews/covers of their OWN
   upload-attributed unpublished media through existing content routes.
   Existing YouTube/X requester-private extensions remain unchanged. Other
   users' unpublished media stays denied (sanitized, indistinguishable from
   unknown).
4. **Gallery invariant**: `GET /api/media` stays published-only for every
   caller including admins. The workspace list is the dedicated surface.
5. **Administrator contribution filter**: extend `GET /api/admin/media`
   (under existing `media.workflow.read`) with contribution attribution
   fields and an optional normalized contributor filter parameter. It must
   keep returning ALL catalog media by default, including unattributed and
   unpublished items. No behavior regression for existing admin queries.
6. **Frontend**: a workspace surface in the existing web visual language for
   mapped users (their own contributions with publication state and missing
   readiness fields), reachable only when the resolved audience has
   `media.workspace.read`; plus the contributor filter control in Manage
   media for administrators. Public audience never sees any of it. UI
   hiding remains never the authorization mechanism.
7. **Focused tests** covering at least:
   - ordinary user lists own upload/YT/X-attributed unpublished media;
     reads own unpublished bytes; another ordinary user's unpublished item
     is indistinguishable from unknown on every route;
   - published items behave exactly as today for everyone;
   - admin sees all catalog media; contributor filter matches normalized
     input and does not narrow default results;
   - public_published_uds exposes no `/api/workspace/*` (uniform 404);
   - capability denial without `media.workspace.read`;
   - multi-contributor media visible to each contributor.

## Validation (include evidence)

- `./.ap/ap exec test-focus --baseline 95f514b…` over your focused set:
  PASS with counts.
- Full declared test operation (`./.ap/ap exec test --baseline 95f514b…`):
  PASS; classify pre-existing failures honestly instead of fixing them.
- JS tests per canonical invocation if web assets changed.
- Grep proof: no new writes to attribution rows from this feature; the
  public composition remains free of workspace routes (quote inventory).
- Commits: coherent small set; suggested final message
  `feat: contributor-scoped workspace media and administrator contribution filter`;
  `git log --oneline -8`; no push.

## Hard boundaries

- No schema/migration edits; schema head stays 0032.
- No `analysis.propose`, alias-team-read, or publish-capability changes in
  this grant (later rollouts).
- No personal-library semantics: no owner columns, no second library, no
  anonymous or public-facing surfaces.
- No edits to ADR bodies; living docs limited to truthful SPEC markers.
- Do not print secrets, Tailscale hostnames, identity-map contents, cookies,
  private media filenames, tweet URLs, or the companion PEM.
- Baseline mismatch or dirty worktree → stop `BLOCKED` before writing.
- Scope impossible inside the allowlist → stop `PARTIAL`/`BLOCKED` with the
  exact missing piece; record any necessary deviation explicitly like your
  exchange 01 did; never expand scope silently.

## Report

Write exactly one file:

`/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/07_report_00.md`

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once. Full capability handshake. Start/end
commits, changed files, test evidence with counts, grep proofs, terminal
outcome `PASS` / `PARTIAL` / `BLOCKED`. After the report: stop. No further
actions.

```text
#------------------------------------------------------
```
