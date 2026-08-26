# WORKER TASK — Implementation (isolated worktree)

Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-ai-suggestions-alias-edit-mvp
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: implementation
Native planning mode: not-used
Implementation authority: explicit
Reasoning recommendation: High
Task identity: FRAMENEST-AI-SUGGESTIONS-ALIAS-EDIT-IMPL-01
Task type: bounded implementation
Exact baseline: 2aead540ee39a81a96425902f85e9b9a34f0d690
Independence required: no
Evidence posture: non-independent
Authority renewal: this is a fresh session; planning authority from session 01 expired. This prompt is the sole current grant.
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
Evidence tier: E2
Evidence tier basis: cross-cutting reversible local change (capability-gated Edit, metadata workspace chrome, surgical docs/ADR). Trust-boundary split is in-scope but reversible; no production, NUC, or schema migration.
Authorized implementation stages: isolated-worktree create → implement allowlisted files → focused tests → 1–3 local commits → terminal report
Combined implementation envelope: allowed
Implementation stage gates: repository gate before mutation; tests green before commit; canonical checkout remains untouched
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: isolated worktree + unpushed commits; discard worktree if BLOCKED before commit
Activated stricter profile: none
Terminal implementation report point: after local commit(s), before any push
```

```text
Development envelope activation: activated
Development envelope identity: FrameNest isolated implementation worktree (this grant)
Declared reversible class: reversible local mutation (worktree files + local commits)
Working-copy topology: isolated-worktree
Topology rationale: keep canonical public main clean; exact-source candidate at the authorized baseline
Irreversible exclusions: secrets, destruction, accounts, public exposure, unrelated owner data, publication, push, NUC, closure, schema migration, .venv reconstruction
```

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: tests/automatic_analysis_lifecycle.test.js; tests/upload_cockpit_async_ownership.test.js; tests/tailscale_identity_frontend.test.js; tests/companion_web_bridge.test.js; tests/catalog_card_ai_quick_action.test.js; tests/contract/test_local_web_application.py; tests/contract/test_x_route_policy.py; tests/contract/test_media_alias_api.py
Affected tests: the suites above plus any new allowlisted test file
New causal regression: ordinary Edit-as-alias; per-field suggestions; hosted hide Analyze/Load
Broad or full suite: not-used
Runtime or testbed: isolated worktree + declared AP exec deviation below
Independent acceptance: required-separate-fresh-worker
```

This prompt grants implementation only inside the isolated worktree and
allowlist. It grants no push, publication, NUC, provider calls, browser
automation, schema migration, or closure. Authority expires at your terminal
report.

## Source precedence

1. This prompt (includes the Cooperator-accepted freeze in §Accepted
   decisions).
2. Frozen planner artifact
   `/home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/01_report_00.md`
   except the one sentence it got wrong (Current always seeds from canonical
   GET, never alias). That sentence is **superseded** by the freeze below.
3. Repository at the exact baseline.
4. Accepted ADRs on that baseline. You add ADR-0077; you do not edit ADR
   bodies 0023, 0062, 0065, 0067, 0073, or 0076.

If the repository contradicts this grant, STOP BLOCKED with exact evidence.
Do not self-grant extra paths.

## Mandatory reading

1. This prompt (self-contained task authority).
2. The frozen planner artifact named above.
3. `/home/agile/Projects/framenest/AGENTS.md`
4. `/home/agile/Projects/framenest/.ap/AP.md`
5. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
6. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`

Then inspect at the baseline, as data: ADR-0023, 0020, 0062, 0065, 0067 §5,
0076; `identity_access.py`; `app.js` (`applyIdentityCapabilities`,
`updateMetadataControls`, catalog-card Edit ~6029, `handleOpenMetadataWorkspace`,
`applyResolvedAiSuggestionToMetadataWorkspace`, Analyze/Load, AI panel);
`index.html` metadata dialog; `media_alias_api.py`;
`PreviewImportedMediaSuggestion` / `PersistImportedPreviewAnalysis` (do **not**
redesign persist-join); companion `GET /api/companion/review-inbox/{media_id}`.

## Repository gate

```text
Repository checkout topology: standalone checkout with pinned submodule
Canonical root: /home/agile/Projects/framenest
Expected canonical branch: feat/x-meme-browser-companion
Expected canonical HEAD: 2aead540ee39a81a96425902f85e9b9a34f0d690
Expected canonical tree: 0900818f57326017712c07686c49de61d534507f
Expected canonical working tree: tracked-clean
Pinned submodule: .ap gitlink == .ap HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: 2aead540ee39a81a96425902f85e9b9a34f0d690
Schema head: Alembic 0033; no 0034_* migration
Working-copy topology: isolated-worktree
```

Create the worktree from the exact baseline. Do not mutate the canonical
checkout (no branch switch, no commits, no dirtying). Suggested identity:

```text
git -C /home/agile/Projects/framenest worktree add -b feat/ai-suggestions-alias-edit-mvp \
  /home/agile/Projects/framenest-worktrees/framenest-ai-suggestions-alias-edit-mvp-w2 \
  2aead540ee39a81a96425902f85e9b9a34f0d690
```

If that path is taken, choose another unused sibling under
`/home/agile/Projects/framenest-worktrees/` with the same kebab and `-w2`.
Worktree HEAD must equal the baseline before your first edit. Do not “fix”
`origin/feat/x-meme-browser-companion` ahead-count.

## Accepted decisions (implement these)

Cooperator accepted the plan on 2026-08-26 **with this freeze** (wins over
plan §2 “Current always seeds from canonical, never alias”):

- Gallery and Details **display** stay canonical. Do not paint alias on cards.
- Ordinary Edit **form load**: `GET /api/media/{id}/alias`. If the overlay is
  non-empty, that is Current. If empty / no row, seed Current from canonical
  metadata GET.
- Ordinary dirty: title/description/tags versus **that loaded seed**.
- Ordinary Save: `PUT /api/media/{id}/alias` only
  (`display_title`, `description`, `tag_keys`). Empty content still means no
  overlay row (existing ADR-0062 `is_empty`).
- Admin Edit Save: existing canonical metadata PUT. Canonical-write wins when
  the actor has both capabilities.
- Ordinary never receives `analysis.run`, `metadata.canonical.write`, inbox
  list/detail, or Apply.

Surface matrix (plan §1), suggestions chrome (plan §3–4), provider-miss
copy/control (plan §5), docs/ADR-0077 (plan §7), and numbered re-test 1–12
(plan §10) are in force, with these operational pins:

- Suggestions list: `GET /api/companion/review-inbox/{media_id}?limit=100`
  (admin `media.workflow.read`). Website Edit **reads** only. Never
  `POST …/apply`. Ordinary remains 403. No new analysis table. No Alembic
  `0034`. If this GET cannot serve the dropdown, STOP PARTIAL with evidence;
  do **not** add a Python endpoint under this grant.
- Movie Edit: hide generic suggestions chrome (detail GET 409). Identify
  movie stays admin movie-only.
- Dropdown change: zero provider calls. Load reveals strips; does **not**
  call `applyResolvedAiSuggestionToMetadataWorkspace`. Remove “Replace
  current draft?”. ✅ copies one field (or one mapped tag append) into
  Current; zero persist until Save.
- Analyze by AI: `analysis.run` ∧ not hosted. After success, do **not** lock
  further Analyze (`aiSuggestionApplied` must not hide/disable the next
  Analyze). Confirm copy: result becomes proposal strips, does not replace
  Current. Persist-join unchanged.
- Heading **AI suggestions**. Dropdown + Load **above Title**. Footer: Save,
  Analyze (admin standalone), Cancel. Delete View details and the generated-
  automatically / confirmation-essay copy. Live region only
  (Analyzing… / Loaded / Provider unavailable) from the last POST. Stale
  confirm: short message, not silence.
- Suggested filename: admin-only note, no ✅. Omit for ordinary alias.
- Ordinary Edit: hide content-category, acquisition, genres. Tag search is
  existing keys only; no `POST /api/canonical-tags`.
- Gallery 🧠: keep admin-only bulk analyze-and-canonical-save; park as debt.
- Hosted companion Details: alias/canonical Edit **shown** per predicate;
  Analyze, Load, dropdown, and strips **hidden**.
- Four `companion_mutation` routes unchanged. Alias PUT is not one of them.

## Changed-path allowlist

Modify only:

1. `src/framenest/adapters/api/web/app.js`
2. `src/framenest/adapters/api/web/index.html`
3. `src/framenest/adapters/api/web/styles.css`
4. `tests/automatic_analysis_lifecycle.test.js`
5. `tests/upload_cockpit_async_ownership.test.js`
6. `tests/tailscale_identity_frontend.test.js`
7. `tests/companion_web_bridge.test.js`
8. `tests/catalog_card_ai_quick_action.test.js`
9. `tests/contract/test_local_web_application.py`
10. `PRODUCT.md` — surgical present tense only where this whole makes it false
    (including §2 / §17 “session-only” website AI)
11. `SPEC.md` — surgical present tense only
12. `docs/X_COMPANION.md` — surgical present tense only (“Edit stays
    capability-gated”)
13. NEW `docs/adr/0077-ordinary-alias-edit-affordance-and-per-field-ai-suggestions.md`
14. `docs/adr/README.md` — index row for 0077; successor note on the 0062 /
    0076 **index** rows only (not their bodies)
15. Optional NEW `tests/metadata_alias_edit.test.js` — only if ordinary
    Edit/Save/load cannot be expressed cleanly in the suites above

Everything else is read-only.

## Negative authority

- No canonical checkout mutation.
- No push, force, rebase of shared history, `git add .` / `git add -A`.
- No Alembic files; schema head stays `0033`.
- No edits to ADR **bodies** 0023, 0062, 0065, 0067, 0073, 0076.
- No `SECURITY.md`. No R4 / `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED` in git.
- No fifth `companion_mutation`. No persist-join redesign. No Cover Studio.
- No NUC, SSH, sudo, `gpgconf`, Funnel, VPS, browser automation, provider calls.
- No secrets; never print hosts, IPs, Tailscale values, fingerprints, or keys.
- No `.venv` reconstruction; no `poetry env use`; no ambient
  `.venv/bin/python` / `python` / `python3` / `poetry run`.
- No Max/enhanced mode. No sub-agents. No Explore-style delegation.

## Execution route (RF-16) and isolated-worktree deviation

Declared Cursor Worker Python route:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 2aead540ee39a81a96425902f85e9b9a34f0d690
./.ap/ap exec --root <WORKTREE> --baseline 2aead540ee39a81a96425902f85e9b9a34f0d690 --operation runtime-info
./.ap/ap exec --root <WORKTREE> --baseline 2aead540ee39a81a96425902f85e9b9a34f0d690 --operation test-focus -- <tests> -q -p no:cacheprovider
```

**Known miss:** `ap exec --root <WORKTREE>` fails (`declared CPython
executable does not exist`) because `ap.project.conf` uses relative
`.venv/bin/python`. Do **not** reconstruct `.venv`.

**Task-specific deviation** (not a second standing route):

```text
Declared route that could not be used: ap exec --root <WORKTREE>
Exact alternate:
  ./.ap/ap exec --root /home/agile/Projects/framenest \
    --baseline 2aead540ee39a81a96425902f85e9b9a34f0d690 \
    --operation test-focus -- <tests> -q -p no:cacheprovider \
    --rootdir=<WORKTREE> -o pythonpath=<WORKTREE>/src
Rationale: interpreter lives in the canonical Poetry .venv; candidate source
  must still be the worktree src.
Evidence class: worker-observed era-06 limitation; ledger entry remains
  untriaged and non-authorizing.
Bounded authority: this Worker session only, Python tests for this allowlist.
Stopping condition: if provenance `framenest.__file__` is not under
  <WORKTREE>/src, STOP ENVIRONMENT LIMITATION. Do not repair .venv.
```

Prove candidate source once (print `framenest.__file__` under the same
invocation). JS tests from the **worktree** root:

```text
node --test tests/automatic_analysis_lifecycle.test.js \
  tests/upload_cockpit_async_ownership.test.js \
  tests/tailscale_identity_frontend.test.js \
  tests/companion_web_bridge.test.js \
  tests/catalog_card_ai_quick_action.test.js
```

Plus the new JS file if you created it. Do not install JS toolchains.
Do not run gated browser evidence.

Minimum Python (same deviation): `tests/contract/test_local_web_application.py`,
`tests/contract/test_x_route_policy.py`, `tests/contract/test_media_alias_api.py`,
and one schema-head assertion path that still requires `0033`
(e.g. `tests/contract/test_analysis_proposal.py` or
`tests/integration/persistence/test_companion_review_migration.py`
`test_head_is_0033`). Do not run the full suite.

First failing suite: preserve output, classify (candidate / harness /
ambient-route / environment), stop that batch. Ambient encodings signature:
rerun once through `ap exec`; never inventory Pythons.

## Git authority

Inside **your worktree only**: stage explicit allowlisted paths; **1–3**
normal commits (alias Edit; suggestions chrome; docs+ADR — merge if a split
is dishonest). Commit message style: short `fix:` / `feat:` / `docs:` subject
focused on why. No push. Report each commit SHA. Canonical checkout must
remain `2aead54…` tracked-clean when you stop.

## Report contract

Write exactly:

```text
/home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/02_report_00.md
```

Begin EXACTLY:

```text
### Report for ORCHESTRATOR_CHAT
```

Professional English. Include:

1. Coordinate echo: logical whole `framenest-ai-suggestions-alias-edit-mvp`,
   session `02`, exchange `01`.
2. Status PASS | PARTIAL | BLOCKED.
3. `Phase-qualified result: implementation-PASS` only if allowlist work is
   complete and minimum-evidence suites pass; otherwise `not-applicable`.
   `Logical-whole closure: not-closed`.
4. Worktree path; baseline; each commit SHA; canonical checkout still
   `2aead54…` tracked-clean.
5. Changed files with per-file intent.
6. Exact test commands and outcomes, including the RF-16 deviation and
   `framenest.__file__` provenance.
7. Mapping: ordinary Edit show/load/save; admin suggestions chrome; hosted
   hide; no 0034; four `companion_mutation`; provider-miss copy/control.
8. Deviations, risks; empty sections say `none`.
9. One smallest next step (independent acceptance, then Cooperator
   publication + NUC).
10. Report justification: `new-mutation`.
11. Authority-expiry statement.
12. `Resolved Execution Issues / Near-Misses:` none | details.
13. `Pre-Existing Failure Classification:` none | complete classification.
14. Brief capability handshake: Plan Mode observed off; reasoning requested
    vs observed; Max observed off or unknown; qualitative context pressure.

## Human-governance routing

```text
Cooperator visibility: implementation grant already given; later independent acceptance, publication, NUC, numbered re-test
Human decision points: none inside this envelope
Deterministic steps inside bounded authority: implement, test, commit, report
Brainstorming classification: out-of-scope => future-logical-whole in the report
Internal delegation posture: not-used
Accountable Worker: one WORKER (this session)
```

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/
Trace project key: framenest
Trace logical-whole projection identity: framenest-ai-suggestions-alias-edit-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR (prompt pre-staged); Worker writes only 02_report_00.md
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_implementation_00.md
Destination path: /home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/02_implementation_00.md
Archival: wait-for-report
```

```text
Client/surface announcement: Cursor Agent chat; native planning mode not-used
Recommended client/surface: fresh Worker Agent session
Recommended reasoning: High — capability split + Edit chrome + ADR
Enhanced/maximum mode: requested off
Automatic model selection: off
Independence requirement: none for this Worker; separate fresh acceptance later
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
```
