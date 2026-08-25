# FrameNest Worker prompt — 04/00 session 02 exchange 03 (implementation: publication-gate correction)

**Issuer:** the fresh Agent Orchestrator. ADR-0074 is **Accepted**
(commit `6aac705`). This grant authorizes successor whole #1 from its phased
rollout: correct the sole publication gate. Companion Apply keeps metadata
behavior; it must never publish again.

Deliver to the **same healthy Worker session 02** (`current-worker-session`).
Native Plan Mode **off**.

```text
#------------------------------------------------------
```

You are the same FrameNest Worker under Analytic Programming, session ordinal
02 of logical whole
`framenest-public-published-surface-and-tailscale-workspace`.

Read before action:

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `/home/agile/Projects/framenest/.ap/AP.md`
3. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
4. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
5. `/home/agile/Projects/framenest/docs/adr/0074-dual-audience-public-published-and-tailscale-workspace-boundary.md`
   (Accepted decision record; especially "Publication gate")
6. Prior exchanges' reports in
   `/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/`
   (`02_report_00.md`, `03_report_00.md`)

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 02
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: implement publication-gate correction — companion Apply never publishes; administrator PUT is the sole write
Phase: implementation
Continuity anchor: your session 02 exchange 02 terminal report; commit 6aac70519f3a930b67dce4be4d4f170662bf153e
Authority renewal: complete new bounded grant; exchange 02 authority expired at its terminal report
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
Exact baseline: 6aac70519f3a930b67dce4be4d4f170662bf153e (verify at start; worktree clean)
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Schema head: 0032 (no migrations authorized)
Git write authority: one commit on feat/x-meme-browser-companion containing exactly allowlisted-path changes; no push
Allowlisted change scope (repository):
  src/framenest/infrastructure/persistence/companion_review_repository.py
  src/framenest/application/companion_review/** (result/readiness models as needed)
  src/framenest/adapters/api/companion_review_api.py (contract coherence as needed)
  extension/** (only if the Apply-result consumer contract requires it)
  tests/** (new/adjusted focused compatibility tests)
  docs/X_COMPANION.md (only stale "Apply publishes" prose)
  SPEC.md (only the sole-publication-gate requirement marker)
Allowlisted write paths (Meta):
  /home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/04_report_00.md
Python/test execution route (canonical, exclusive):
  ./.ap/ap exec runtime-info / test / test-focus with exact --baseline 6aac70519f3a930b67dce4be4d4f170662bf153e
  JavaScript tests exactly as docs/WORKER_EXECUTION_CONTRACT.md declares them.
  NO ambient python/python3/.venv invocation of any kind.
NUC / SSH / sudo / provider / browser automation / push: none
```

## Task

1. Remove the companion-triggered publication write in the Apply transaction:
   `src/framenest/infrastructure/persistence/companion_review_repository.py`
   currently inserts into `media_content_publications` with origin
   `companion_review` when readiness holds. After correction, Apply performs
   metadata and tag-source writes only (preserve-and-append per ADR-0073) and
   never creates or deletes publication rows.
2. Keep the Apply-result contract honest: the result must still expose
   durable publication state, readiness (`ready`, `missing_fields`), and an
   accurate status so the extension/UI cannot mislead the administrator into
   thinking Apply published. Choose the smallest coherent adjustment (e.g.,
   explicit "requires administrator publish" status instead of "published");
   keep consumers consistent within the allowlisted scope. No capability
   changes; no new routes.
3. Historical compatibility: existing rows with origin `companion_review`
   stay readable everywhere they are read today (history, inbox, publication
   loaders). The CHECK-constraint enum value remains valid. No migration, no
   data rewrite.
4. The administrator route
   `PUT /api/admin/media/{media_id}/content-publication`
   (`media.content.publish`) remains the sole promotion/unpromotion write,
   including movies. Do not modify its behavior beyond what correctness
   requires.
5. Add focused compatibility tests covering at least:
   - ready item: Apply updates metadata/tags, creates **no** publication row;
   - already-published item: Apply leaves the publication untouched;
   - not-ready item: unchanged metadata-success behavior;
   - historical `companion_review` row loads correctly after the change;
   - administrator PUT still publishes and unpublishes.
   Follow existing test layout/patterns; name every added/changed test file.
6. Fix stale prose in `docs/X_COMPANION.md` only where it claims Apply-side
   publication; adjust the SPEC.md sole-gate requirement marker only from
   "pending" to implemented-for-backend if you actually completed it.

## Validation (include evidence)

- `./.ap/ap exec test-focus --baseline 6aac705…` over your focused set: PASS
  (report command class and summary counts).
- Full declared test operation (`./.ap/ap exec test --baseline 6aac705…`) OR
  the contract's canonical full-suite route: PASS; if any pre-existing
  failure exists outside your change, classify it honestly as
  Pre-Existing Failure Classification with file/test names, do not fix it
  silently.
- Grep proof that no companion path writes `media_content_publications`:
  quote the remaining read-only references.
- `git diff --check` clean; changed-file list within allowlist; exactly one
  commit (suggested message: `fix: make administrator publication the sole
  content-publication write`); `git log --oneline -1`; no push.

## Hard boundaries

- No schema/migration edits; schema head stays 0032.
- No capability-table changes, no new routes, no ingress changes, no Funnel,
  no automatic-analysis flag changes anywhere.
- No edits to ADR bodies (0068/0073 stay untouched; superseded textually by
  accepted ADR-0074).
- Do not print secrets, Tailscale hostnames, identity-map contents, cookies,
  private media filenames, tweet URLs, or the companion PEM.
- If baseline is not exact or worktree dirty: stop `BLOCKED` before writing.
- If you cannot complete a coherent correction inside the allowlist, stop
  `PARTIAL`/`BLOCKED` and report exactly what is missing; do not expand scope
  silently.

## Report

Write exactly one file:

`/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/04_report_00.md`

Begin exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinates once. Full capability handshake. Start/end commit,
changed files, test evidence with counts, grep proofs, terminal outcome
`PASS` / `PARTIAL` / `BLOCKED`. After the report: stop. No further actions.

```text
#------------------------------------------------------
```
