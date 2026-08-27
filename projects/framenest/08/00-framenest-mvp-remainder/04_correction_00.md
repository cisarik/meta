# WORKER TASK — Bounded correction (Gallery card 🧠 available on all supported non-movie items for re-analysis)

Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-gallery-card-ai-per-field-mvp
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: Implementation
Native planning mode: not-used
Implementation authority: explicit
Reasoning recommendation: High
Task identity: FRAMENEST-GALLERY-CARD-AI-PER-FIELD-CORR-01
Task type: bounded correction
Exact baseline: 3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18
Independence required: no
Evidence posture: non-independent
Authority renewal: sessions 02 and 03 expired at their reports. This prompt is the sole current grant.
Internal delegation posture: not-used
Accountable Worker: one WORKER
Material phase gate: yes
Changed material axis: mutation-authority-or-side-effect-class
Routing reopened for: mutation-authority-or-side-effect-class
Unchanged axes reopened: none
Ordinary-only trigger: no

```text
Canonical repository identity: https://github.com/cisarik/ap.git
Immutable version identity: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Declared variant: stable
Governing variants in effect: one
Declaration location: project governing rules
Rules from non-governing variants: none
Migration required: no
```

```text
Acceptance candidate (parent): 3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18
Acceptance owner map: Cooperator live NUC re-test feedback 2026-08-27 (card 🧠 must be available for admin on all supported non-movie items, allowing re-analysis / model experimentation, not restricted to incomplete metadata)
Acceptance allowlist: see § Changed-path allowlist
Acceptance risk claims: card 🧠 opens Edit with proposal strips; 0 auto-PUT from card; dismissal preserves canonical; hosted 🧠 hidden; ordinary 🧠 hidden; card 🧠 available on complete items for re-analysis; schema head 0033; four companion_mutation unchanged
Acceptance control matrix: see § Frozen correction
Acceptance independence: not-required for this corrector; full-fresh independent acceptance is a later Worker
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates only
```

```text
Evidence tier: E3
Evidence tier basis: UI affordance predicate adjustment (allowing administrator re-analysis on all supported non-movie items via gallery card 🧠)
Authorized implementation stages: isolated-worktree create → implement allowlisted files → focused tests → 1–2 local commits → terminal report
Combined implementation envelope: allowed
Implementation stage gates: repository gate before mutation; tests green before commit; canonical checkout remains untouched
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: isolated worktree + unpushed commits; discard worktree if BLOCKED before commit
Activated stricter profile: none
Terminal implementation report point: after local commit(s), before any push
```

```text
Development envelope activation: activated
Development envelope identity: FrameNest isolated correction worktree (this grant)
Declared reversible class: reversible local mutation (worktree files + local commits)
Working-copy topology: isolated-worktree
Topology rationale: keep canonical public main clean; exact-source candidate parented on published 3b8f9abf
Irreversible exclusions: secrets, destruction, accounts, public exposure, unrelated owner data, publication, push, NUC, closure, schema migration, .venv reconstruction
```

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: tests/catalog_card_ai_quick_action.test.js; tests/metadata_alias_edit.test.js; tests/tailscale_identity_frontend.test.js; tests/contract/test_local_web_application.py; tests/contract/test_youtube_creator_taxonomy_frontend.py
Affected tests: the suites above
New causal regression: card 🧠 available on complete items for admin; ordinary still cannot see 🧠; hosted still cannot see 🧠; movie still cannot see 🧠; 0 auto-PUT
Broad or full suite: not-used
Runtime or testbed: isolated worktree + declared AP exec deviation below
Independent acceptance: required-separate-fresh-worker
```

This prompt grants correction only inside the isolated worktree and allowlist.
It grants no push, publication, NUC, provider calls, browser automation, schema
migration, or closure. Authority expires at your terminal report. You do not
self-accept. You do not close the logical whole.

## Source Precedence

1. This prompt (frozen correction below).
2. Cooperator live NUC re-test feedback on 2026-08-27.
3. Repository at the exact baseline `3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18`.
4. Accepted ADRs on that baseline (including ADR-0078).

If the repository contradicts this grant, STOP BLOCKED with exact evidence.
Do not self-grant extra paths.

## Mandatory Reading

1. This prompt.
2. `/home/agile/Projects/framenest/AGENTS.md`
3. `/home/agile/Projects/framenest/.ap/AP.md`
4. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
5. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
6. `docs/adr/0078-gallery-card-ai-per-field-review.md`
7. `src/framenest/adapters/api/web/app.js` (`cardAiQuickActionEligible`, `cardNeedsMetadata`, `identityAllowsCardAiQuickAction`)
8. `tests/catalog_card_ai_quick_action.test.js`

## Repository Gate

```text
Repository checkout topology: standalone checkout with pinned submodule
Canonical root: /home/agile/Projects/framenest
Expected canonical branch: feat/x-meme-browser-companion
Expected canonical HEAD: 3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18
Expected canonical tree: 9d1b069fa12128913b8dd4c653630f576aa26e6d
Expected canonical working tree: tracked-clean
Pinned submodule: .ap gitlink == .ap HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: 3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18
Schema head: Alembic 0033; no 0034_* migration
Working-copy topology: isolated-worktree
```

Create the worktree from the exact baseline. Do not mutate the canonical checkout:

```text
git -C /home/agile/Projects/framenest worktree add -b feat/gallery-card-ai-per-field-corr \
  /home/agile/Projects/framenest-worktrees/framenest-gallery-card-ai-per-field-mvp-w4 \
  3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18
```

If that path is taken, choose another unused sibling under
`/home/agile/Projects/framenest-worktrees/` with the same kebab and `-w4`.
Do not reuse w2 or w3 as the working copy. Worktree HEAD must equal the
baseline before your first edit.

## Frozen Correction (do not replan)

### 1. Remove `!catalogItemHasCompleteMetadata(item)` restriction from card 🧠

In `src/framenest/adapters/api/web/app.js`:
- `cardAiQuickActionEligible(item)` must check:
  - `identityAllowsCardAiQuickAction()` (requires `analysis.run` ∧ `metadata.canonical.write` ∧ resolved ∧ available ∧ `!companionWebHosted()`)
  - `selectSupportedAvailableLocation(item) !== null`
  - `(item.content_category || "general") !== "movie"`
- **Remove** `cardNeedsMetadata(item)` from `cardAiQuickActionEligible(item)`.
- Rationale: Because card 🧠 now opens the Edit dialog with per-field proposal strips (ADR-0078) and no longer performs a destructive bulk-overwrite, administrators need 🧠 available on all supported non-movie cards to re-run AI analysis (e.g. after changing AI provider/model or to explore alternative metadata drafts).
- Keep `catalogItemHasCompleteMetadata` intact for its other caller (`filterProcessedCatalogItems` for the Processed collection). If `cardNeedsMetadata` is no longer used elsewhere, clean it up or keep as internal helper if needed.

### 2. Update Tests

- In `tests/catalog_card_ai_quick_action.test.js`:
  - Update eligibility tests: `cardAiQuickActionEligible(complete)` is now `true` for administrator with supported location.
  - Update source-wiring assertions checking `cardAiQuickActionEligible`.
- In `tests/contract/test_local_web_application.py`:
  - Update assert on `cardAiQuickActionEligible` body (~line 1712).

### 3. Update Docs & ADR-0078

- In `docs/adr/0078-gallery-card-ai-per-field-review.md`:
  - Update Decision §4 and Consequences to state that card 🧠 is available for administrators on all supported non-movie items (allowing re-analysis / model experimentation), not restricted to incomplete metadata.
- In `GALLERY.md`:
  - Update description to state 🧠 is available on supported non-movie cards for administrators upon hover to run / re-run AI analysis and open the per-field review editor.

## Changed-Path Allowlist

Modify only:

1. `src/framenest/adapters/api/web/app.js`
2. `tests/catalog_card_ai_quick_action.test.js`
3. `tests/contract/test_local_web_application.py`
4. `docs/adr/0078-gallery-card-ai-per-field-review.md`
5. `GALLERY.md`

Everything else is read-only.

## Negative Authority

- No canonical checkout mutation.
- No push, force, rebase of shared history, `git add .` / `git add -A`.
- No Alembic files; schema head stays `0033`.
- No edits to ADR **bodies** 0023, 0020, 0062, 0065, 0066, 0067, 0073, 0076, 0077.
- No `SECURITY.md`. No R4 / `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED` in git.
- No fifth `companion_mutation`. No persist-join redesign. No Cover Studio.
- No ordinary `analysis.run` or `canonical.write`.
- No NUC, SSH, sudo, `gpgconf`, Funnel, VPS, browser automation, provider calls.
- No secrets; never print hosts, IPs, Tailscale values, fingerprints, or keys.
- No `.venv` reconstruction; no `poetry env use`; no ambient
  `.venv/bin/python` / `python` / `python3` / `poetry run`.
- No Max/enhanced mode. No sub-agents. No Explore-style delegation.

## Execution Route (RF-16) and Isolated-Worktree Deviation

Declared Cursor Worker Python route:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18
./.ap/ap exec --root <WORKTREE> --baseline 3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18 --operation runtime-info
./.ap/ap exec --root <WORKTREE> --baseline 3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18 --operation test-focus -- <tests> -q -p no:cacheprovider
```

**Known miss:** `ap exec --root <WORKTREE>` fails (`declared CPython
executable does not exist`) because `ap.project.conf` uses relative
`.venv/bin/python`. Do **not** reconstruct `.venv`.

**Task-specific deviation**:

```text
Declared route that could not be used: ap exec --root <WORKTREE>
Exact alternate:
  ./.ap/ap exec --root /home/agile/Projects/framenest \
    --baseline 3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18 \
    --operation test-focus -- <tests> -q -p no:cacheprovider \
    --rootdir=<WORKTREE> -o pythonpath=<WORKTREE>/src
Rationale: interpreter lives in the canonical Poetry .venv; candidate source
  must still be the worktree src.
Evidence class: worker-observed era-06/07/08 limitation; ledger entry remains
  untriaged and non-authorizing.
Bounded authority: this Worker session only, Python tests for this allowlist.
Stopping condition: if provenance framenest.__file__ is not under
  <WORKTREE>/src, STOP ENVIRONMENT LIMITATION. Do not repair .venv.
```

JS tests from the **worktree** root:

```text
node --test tests/catalog_card_ai_quick_action.test.js \
  tests/metadata_alias_edit.test.js \
  tests/tailscale_identity_frontend.test.js
```

Minimum Python (same deviation): `tests/contract/test_local_web_application.py`, `tests/contract/test_youtube_creator_taxonomy_frontend.py`.

## Git Authority

Inside **your worktree only**: stage explicit allowlisted paths; **1–2**
normal commits (commit 1: code + tests; commit 2: docs + ADR-0078 update).
Commit message style: short `fix:` / `docs:` subject focused on why. No push.
Report each commit SHA. Canonical checkout must remain `3b8f9abf…` tracked-clean
when you stop.

## Report Contract

Write exactly:

```text
/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/04_report_00.md
```

Begin EXACTLY:

```text
### Report for ORCHESTRATOR_CHAT
```

Professional English. Include:

1. Coordinate echo: logical whole `framenest-gallery-card-ai-per-field-mvp`,
   session `04`, exchange `01`.
2. Status PASS | PARTIAL | BLOCKED.
3. `Phase-qualified result: implementation-PASS` only if the freeze is
   implemented and minimum-evidence suites pass; otherwise `not-applicable`.
   `Logical-whole closure: not-closed`.
4. Worktree path; baseline; each commit SHA; canonical checkout still
   `3b8f9abf…` tracked-clean.
5. Changed files with per-file intent.
6. Exact test commands and outcomes, including the RF-16 deviation and
   `framenest.__file__` provenance.
7. Verification: card 🧠 available on complete items for admin re-analysis; ordinary still cannot see 🧠; hosted still cannot see 🧠; movie still cannot see 🧠; 0 auto-PUT.
8. Deviations, risks; empty sections say `none`.
9. One smallest next step (fresh independent acceptance Worker 05, then publication + NUC).
10. Report justification: `new-mutation`.
11. Authority-expiry statement.
12. `Resolved Execution Issues / Near-Misses:` none | details.
13. `Pre-Existing Failure Classification:` none | complete classification.
14. Brief capability handshake: Plan Mode observed off; reasoning requested
    vs observed; Max observed off or unknown; qualitative context pressure.

## Human-Governance Routing

```text
Cooperator visibility: correction grant already given; later independent acceptance, publication, NUC, numbered re-test
Human decision points: none inside this envelope
Deterministic steps inside bounded authority: implement, test, commit, report
Brainstorming classification: out-of-scope => future-logical-whole in the report
Internal delegation posture: not-used
Accountable Worker: one WORKER (this session)
```

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/
Trace project key: framenest
Trace logical-whole projection identity: framenest-gallery-card-ai-per-field-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR (prompt pre-staged); Worker writes only 04_report_00.md
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 04_correction_00.md
Destination path: /home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/04_correction_00.md
Archival: wait-for-report
```

```text
Client/surface announcement: Cursor Agent chat; native planning mode not-used
Recommended client/surface: fresh Worker Agent session
Recommended reasoning: High
Enhanced/maximum mode: requested off
Automatic model selection: off
Independence requirement: none for this Worker; separate fresh full-fresh acceptance later
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
```
