# FrameNest Worker prompt — 04/00 session 02 exchange 01 (implementation: ADR-0074 decision package)

**Issuer:** the fresh Agent Orchestrator after accepting the planning report
`01_report_00.md` (session 01, exchanges 01–02) of logical whole
`framenest-public-published-surface-and-tailscale-workspace`. The accepted
plan is approval-gated; this prompt is the explicit implementation authority
for its first bounded whole only.

Deliver to a **fresh Worker session** with native Plan Mode **off**.

```text
#------------------------------------------------------
```

You are a FrameNest Worker under Analytic Programming.

Read before action, in this order:

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `/home/agile/Projects/framenest/.ap/AP.md`
3. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
4. `/home/agile/Projects/framenest/.ap/PROMPT_CONTRACTS.md`
5. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
6. Accepted plan (decision record; context, not a second grant):
   `/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/01_report_00.md`
7. ADRs you must relate to without editing in place:
   `docs/adr/0048`, `0049`, `0053`, `0054`, `0062`, `0063`, `0068`, `0070`,
   `0073` under `/home/agile/Projects/framenest/docs/adr/`

Then perform exactly one bounded implementation task:

## Task — author the proposed ADR-0074 decision package

1. Create `docs/adr/0074-dual-audience-public-published-and-tailscale-workspace-boundary.md`
   with status **Proposed**. It must record, as decisions:
   - One authoritative catalog and media store; two separately composed
     applications and listeners (`tailscale_uds` workspace writer;
     new local-only `public_published_uds` public reader assembled from an
     exact GET-only route allowlist, read-only SQLite URI, fail-closed startup).
   - Publication gate correction: administrator
     `PUT /api/admin/media/{media_id}/content-publication` becomes the sole
     future promotion/unpromotion path for every media type including movies;
     companion Apply keeps applying metadata but must never publish; historical
     `companion_review` publication rows and enum value stay readable.
   - Audience bootstrap `GET /api/audience/me`; identity-absent public
     callers receive only `gallery.read` + `media.original.read`.
   - Public catalog projection redaction rules and sanitized-404 policy as in
     the accepted plan's "Public audience" section.
   - Workspace capability additions `media.workspace.read`,
     `analysis.propose`, `metadata.alias.team.read` (administrator-only), and
     the contributor-scoped unpublished-read model (ADR-0054-style audience
     extension; no ownership column, no personal libraries).
   - Public movie behavior after Publish; ADR-0070 companion exclusion intact.
   - Deferred companion reconnect to the public origin as a later whole.
   - Phased rollout matching the plan's ordered successor wholes 1–8.
   - Negative space from the plan ("Rejected", "Assumptions and negative
     space").
2. Add a relationship/supersession matrix inside ADR-0074 that:
   - narrowly supersedes only the conflicting inbound sentences of ADR-0048
     for the second origin (Tailscale remains the workspace path);
   - supersedes ADR-0068's readiness-triggered publication and ADR-0073's
     preservation of it;
   - supplements ADR-0049, ADR-0053/0054, ADR-0062, ADR-0063, ADR-0070
     without modifying them.
3. Add exactly one index entry to `docs/adr/README.md`, listed as `Proposed`.

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: implement first bounded whole — proposed ADR-0074 decision package
Phase: implementation
Continuity anchor: none
Authority renewal: none; initial implementation grant for this session
Prior authority boundary: planning expired at 01_report_00.md (sessions 01)
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
Exact baseline: 37da5f2b7edf8286028dbc7a0dbca65f2d031e60
Baseline meaning: verify at start; worktree clean; do not treat 37da5f2 as live NUC
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Schema head: 0032
Git write authority: one commit on feat/x-meme-browser-companion containing exactly the two repository files below; no push
Allowlisted write paths (repository):
  docs/adr/0074-dual-audience-public-published-and-tailscale-workspace-boundary.md (new)
  docs/adr/README.md (index entry only)
Allowlisted write paths (Meta):
  /home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/02_report_00.md
Python invocation: only ./.ap/ap project check (readiness/hygiene); no tests required by this grant
NUC / SSH / sudo: none
Provider calls / browser: none
Publication / deploy / push: none
```

## Hard boundaries

- Status stays `Proposed`. Never mark `Accepted`; acceptance is
  Cooperator-owned and happens after this report.
- Do not edit any other ADR or living document (`README`, `PRODUCT`, `SPEC`,
  `ROADMAP`, `SECURITY`, `SERVER`, NUC runbook). Their updates come after
  acceptance.
- No product code, no ingress changes, no Funnel, no router port-forward, no
  automatic-analysis flag change, no schema/migration changes.
- Do not print secrets, Tailscale hostnames, identity-map contents, cookies,
  private media filenames, tweet URLs, or the companion PEM.
- If baseline is not exact or worktree is dirty: stop `BLOCKED` before writing.

## Validation (include evidence)

- `git diff --check` clean on the staged content.
- Markdown link targets inside the new ADR resolve within the repository.
- Supersession matrix names exist: verify each cited ADR number/filename.
- `./.ap/ap project check` passes (report output class only).
- Exactly one commit created; `git log --oneline -1` and changed-file list
  reported; no push performed.

## Report

Write exactly one file:

`/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/02_report_00.md`

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once. Include full capability handshake. State
start/end commit, changed files, validation evidence, and terminal outcome
`PASS` / `PARTIAL` / `BLOCKED`. After the report: stop. No further commits,
revisions, or follow-up actions.

```text
#------------------------------------------------------
```
