# WORKER TASK — Independent Acceptance (fresh checkout)

Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-gallery-card-ai-per-field-mvp
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Audit
Phase: Acceptance
Native planning mode: not-used
Reasoning recommendation: High
Task identity: FRAMENEST-GALLERY-CARD-AI-PER-FIELD-ACC-01
Independence required: yes
Evidence posture: independent
Authority renewal: this is a fresh session. Session 02 implementation authority expired at `02_report_00.md`. That report is a claim, not proof. You inherit no mutation authority from it.
Internal delegation posture: not-used
Accountable Worker: one WORKER
Material phase gate: yes
Changed material axis: independence-requirement
Routing reopened for: independence-requirement
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
Acceptance candidate: 3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18
Acceptance owner map: Cooperator-accepted plan 01_report_00.md plus implementation grant 02_implementation_00.md plus candidate ADR-0078
Acceptance allowlist: inspection of the 10 committed paths only; no product edits
Acceptance risk claims: card 🧠 opens Edit with proposal strips; 0 auto-PUT from card; 0 tag POST from card; dismissal preserves canonical; hosted 🧠 hidden; ordinary 🧠 hidden; schema head 0033; four companion_mutation unchanged; no fifth mutation; ADR-0023/0020/0062/0065/0066/0067/0073/0076/0077 bodies untouched
Acceptance control matrix: see § Control Matrix
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates only
```

```text
Evidence tier: E3
Evidence tier basis: state mutation split (eliminating silent last-write-wins auto-PUT from gallery card 🧠 in favor of per-field review); hosted hide gate; independent of the implementing session
Authorized implementation stages: none
Combined implementation envelope: prohibited
Implementation stage gates: not-applicable
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: canonical checkout remains afa0670e26d17b04570ad555ba4f922052507c6c; session-02 worktree remains untouched
Activated stricter profile: none
Terminal implementation report point: not-applicable
```

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: JS and Python matrix named below
Affected tests: same matrix re-run from a fresh checkout of 3b8f9abf
New causal regression: none authorized
Broad or full suite: not-used
Runtime or testbed: docs/WORKER_EXECUTION_CONTRACT.md plus ap.project.conf
Independent acceptance: required-separate-fresh-worker
```

```text
Development envelope activation: activated
Development envelope identity: FrameNest isolated-worktree exact-source envelope
Declared reversible class: local worktree of an existing object; worktree-local submodule checkout; one temporary provenance probe file
Working-copy topology: isolated-worktree
Topology rationale: candidate is unpublished; canonical must stay at public main; session-02 worktree must not be the acceptance working copy
Irreversible exclusions: secrets, destruction, accounts, public exposure, unrelated owner data, publication, closure, NUC, push, product commits, .venv reconstruction
```

```text
Repeated-gate or reasoning-loop stop: configured
Broad gate: once per materially changed candidate
Narrow before re-broad: required
Unchanged hypothesis, candidate, and failing gate: not-progress
Escalate only on: named missing evidence the higher profile must solve
Downgrade after: convergence or named risk removal
Cost cannot falsify evidence: yes
```

Independence rule: you did not implement `3b8f9ab…` or `365426a…`. If this
session materially authored those commits, stop BLOCKED (independence
conflict).

This prompt grants read-only acceptance evidence only. No product edits, no
commits, no push, no NUC, no publication, no closure.

## Mission

Independently accept or reject unpublished candidate
`3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18` against:

1. This prompt’s freeze and control matrix.
2. `/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/01_report_00.md`.
3. Candidate `docs/adr/0078-gallery-card-ai-per-field-review.md`.

Parent / public `main` / canonical HEAD:

```text
afa0670e26d17b04570ad555ba4f922052507c6c
```

Claim to verify, not believe:
`/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/02_report_00.md`

Do not implement. Do not replan. Do not open R4 or VPS.

## Mandatory Reading

1. This prompt.
2. `/home/agile/Projects/framenest/AGENTS.md`
3. `.ap/AP.md`, `.ap/AP_WORKER.md`
4. `docs/WORKER_EXECUTION_CONTRACT.md`
5. The plan and implementation claim named above.
6. Candidate ADR-0078. ADR-0023 / 0020 / 0062 / 0065 / 0066 / 0067 / 0073 / 0076 / 0077 bodies: inspect only, do not edit.

## Repository Gate

```text
Repository checkout topology: standalone checkout with pinned submodule
Canonical root: /home/agile/Projects/framenest
Expected canonical branch: feat/x-meme-browser-companion
Expected canonical HEAD: afa0670e26d17b04570ad555ba4f922052507c6c
Expected canonical tree: b6eafbcdef3a8bcb728498992c003d8ad5e9a447
Expected canonical working tree: tracked-clean
Pinned submodule: .ap gitlink == .ap HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: afa0670e26d17b04570ad555ba4f922052507c6c (re-verify ls-remote)
```

Before creating a fresh checkout, verify and record those facts. Any canonical
drift: classify RF-12 and stop; never tidy canonical.

Session-02 worktree
`/home/agile/Projects/framenest-worktrees/framenest-gallery-card-ai-per-field-mvp-w2`
must still be at `3b8f9ab…`, tracked-clean. Do **not** use it as your working
copy. Do not edit or commit in it.

Create **one** fresh detached checkout of the candidate:

```text
git -C /home/agile/Projects/framenest worktree add --detach \
  /home/agile/Projects/framenest-worktrees/framenest-gallery-card-ai-per-field-mvp-w3 \
  3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18
```

If that path exists, stop and report; do not delete it. Alternative: another
unused sibling directory you report.

Worktree-local submodule only:

```text
git -C <fresh-checkout> submodule update --init .ap
```

Git writes authorized: only `worktree add` and worktree-local
`submodule update --init .ap`. No commits, add, push, rebase, force, or
canonical checkout of the candidate.

After add, re-read canonical HEAD and porcelain: must be unchanged.
Your checkout HEAD must equal `3b8f9ab…`;
`git merge-base --is-ancestor afa0670… HEAD` must succeed;
`git rev-list --count afa0670…..HEAD` equals 2.

## Positive Authority

- Read candidate, canonical, plan, claim, ADR-0078.
- Diff `3b8f9ab…` against `afa0670…`. Confirm the path set is exactly these
  10 files (or fail extras/missing):

  ```text
  GALLERY.md
  docs/adr/0078-gallery-card-ai-per-field-review.md
  docs/adr/README.md
  src/framenest/adapters/api/web/app.js
  src/framenest/adapters/api/web/styles.css
  tests/catalog_card_ai_quick_action.test.js
  tests/contract/test_local_web_application.py
  tests/contract/test_youtube_creator_taxonomy_frontend.py
  tests/metadata_alias_edit.test.js
  tests/tailscale_identity_frontend.test.js
  ```

- Confirm **no** `alembic_environment/versions/0034*`, no ADR-0023/0020/0062/0065/0066/0067/0073/0076/0077
  **body** edits, no `SECURITY.md`, no Python API modules, no persist-join
  redesign, no fifth `companion_mutation`.
- Run the declared Python and Node evidence.
- Write exactly the report file below.
- Create and delete one temporary provenance probe file as specified.

## Negative Authority

- No product, test, ADR-body, or docs edits (except the one Meta report).
- No Alembic 0034. No NUC, SSH, sudo, `gpgconf`, Funnel, VPS, providers,
  browser automation, secrets.
- No `.venv` reconstruction; no ambient `python` / `.venv/bin/python` /
  `poetry run`.
- No publication, push, or closure.
- No Max. No sub-agents.

## Control Matrix (pass/fail)

**Positive (must hold on the candidate object + tests):**

1. `handleAnalyzeCatalogCard`: confirms Analyze, POSTs preview (persist-join triggered), opens existing Edit workspace via `handleOpenMetadataWorkspace` with `previewSuggestion` and `previewPayload`.
2. Zero automatic `PUT /api/media/{id}/metadata` from card 🧠 (`app.js` card path has 0 `PUT`).
3. Zero automatic `POST /api/canonical-tags` from card 🧠.
4. Dismissing / canceling Edit dialog leaves canonical metadata unchanged.
5. In Edit workspace, `presentPreviewSuggestionInMetadataWorkspace` reveals suggestion strips without bulk replacing Current form values.
6. `identityAllowsCardAiQuickAction` requires `analysis.run` ∧ `metadata.canonical.write` ∧ `resolved` ∧ `available` ∧ incomplete metadata ∧ not movie ∧ `!companionWebHosted()`.
7. Hosted companion Gallery hides card 🧠 (`!companionWebHosted()`).
8. Ordinary users never see 🧠 (gated on `analysis.run` ∧ `metadata.canonical.write`).
9. Dead card-auto-save code cleanly removed (`applying`, `failed_save`, `applySavedAiMetadataToCatalogSurfaces`, etc.).
10. Schema head remains Alembic `0033`; no `0034_*` migration.
11. Exactly four `companion_mutation=True` routes in `tailscale_ingress.py` unchanged.
12. ADR-0078 exists and index rows note succession **without** ADR-0077 body edits.

**Negative (must not hold):**

- Ordinary Analyze / 🧠.
- Automatic canonical PUT from card 🧠.
- Alembic `0034`.
- Fifth `companion_mutation`.
- Hosted 🧠.

## Execution Route (RF-16)

Attempt declared isolated-worktree route first:

```text
./.ap/ap project check --root <fresh-checkout> --baseline afa0670e26d17b04570ad555ba4f922052507c6c
./.ap/ap exec --root <fresh-checkout> --baseline afa0670e26d17b04570ad555ba4f922052507c6c --operation runtime-info
```

Expected miss: `declared CPython executable does not exist`. Classify
environment limitation. Do not repair. Do not fail the candidate solely for it.

**Task-specific deviation** after that classified miss:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline afa0670e26d17b04570ad555ba4f922052507c6c
./.ap/ap exec --root /home/agile/Projects/framenest --baseline afa0670e26d17b04570ad555ba4f922052507c6c --operation runtime-info
```

Provenance probe file **outside** git checkouts, e.g.
`/tmp/framenest-cardacc-03-provenance.py`, printing `framenest.__file__` and
asserting it is under `<fresh-checkout>/src/framenest/`.

Python matrix (deviation: canonical `--root` + `--rootdir` / `pythonpath` fresh-checkout):

```text
<fresh-checkout>/tests/contract/test_local_web_application.py
<fresh-checkout>/tests/contract/test_youtube_creator_taxonomy_frontend.py
<fresh-checkout>/tests/contract/test_media_ai_suggestions_api.py
<fresh-checkout>/tests/contract/test_tailscale_ingress_security.py
```

Stopping condition: if `framenest.__file__` is not under the fresh checkout
`src/`, ENVIRONMENT LIMITATION for Python provenance; still run Node; do not
fail solely for the known launch-path miss; **do** fail on candidate defects.

Node from the **fresh checkout** root:

```text
node --test tests/catalog_card_ai_quick_action.test.js \
  tests/metadata_alias_edit.test.js \
  tests/tailscale_identity_frontend.test.js
```

And broader JS suite:

```text
node --test tests/*_frontend.test.js tests/*_cockpit.test.js tests/gallery_*.test.js tests/automatic_analysis_lifecycle.test.js tests/companion_web_bridge.test.js
```

(Note: `tests/movie_identification_frontend.test.js` has known pre-existing baseline failures; classify if encountered).

## Report Contract

Write exactly:

```text
/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/03_report_00.md
```

Begin EXACTLY:

```text
### Report for ORCHESTRATOR_CHAT
```

Professional English. Include: coordinate echo (whole, session `03`, exchange
`01`); PASS | PARTIAL | BLOCKED; `Phase-qualified result: acceptance-PASS`
only if every control-matrix row holds and minimum evidence is green,
else `not-applicable`; `Logical-whole closure: not-closed`; candidate SHA;
fresh checkout path; canonical still `afa0670…` tracked-clean; w2 untouched;
path-set vs parent; control-matrix table with evidence (`path:line` or test
id); test commands and outcomes including RF-16 deviation and
`framenest.__file__`; deviations/risks; one smallest next step (Cooperator
publication, then NUC); justification `final-acceptance`; authority expiry;
Resolved Execution Issues; Pre-Existing Failure Classification; capability
handshake (Plan Mode off; Max off or unknown).

## Human-Governance Routing

```text
Cooperator visibility: acceptance verdict; later publication and NUC
Human decision points: none inside this envelope
Deterministic steps inside bounded authority: inspect, re-run tests, report
Brainstorming classification: out-of-scope => future-logical-whole
Internal delegation posture: not-used
Accountable Worker: one WORKER
```

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/
Trace project key: framenest
Trace logical-whole projection identity: framenest-gallery-card-ai-per-field-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 03_acceptance_00.md
Destination path: /home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/03_acceptance_00.md
Archival: wait-for-report
```
